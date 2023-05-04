from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Media.DirectShow
import Windows.Win32.Media.DirectShow.Tv
import Windows.Win32.Media.KernelStreaming
import Windows.Win32.Media.MediaFoundation
import Windows.Win32.System.Com
import Windows.Win32.System.Ole
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
ANALOG_AUXIN_NETWORK_TYPE = Guid('{742ef867-09e1-40a3-82d3-9669ba35325f}')
ANALOG_FM_NETWORK_TYPE = Guid('{7728087b-2bb9-4e30-8078-449476e59dbb}')
ANALOG_TV_NETWORK_TYPE = Guid('{b820d87e-e0e3-478f-8a38-4e13f7b3df42}')
ATSCChannelTuneRequest = Guid('{0369b4e6-45b6-11d3-b650-00c04f79498e}')
ATSCComponentType = Guid('{a8dcf3d5-0780-4ef4-8a83-2cffaacb8ace}')
ATSCLocator = Guid('{8872ff1b-98fa-4d7a-8d93-c9f1055f85bb}')
ATSCTuningSpace = Guid('{a2e30750-6c3d-11d3-b653-00c04f79498e}')
class ATSC_FILTER_OPTIONS(EasyCastStructure):
    fSpecifyEtmId: Windows.Win32.Foundation.BOOL
    EtmId: UInt32
    _pack_ = 1
ATSC_TERRESTRIAL_TV_NETWORK_TYPE = Guid('{0dad2fdd-5fd7-11d3-8f50-00c04f7971e2}')
AnalogAudioComponentType = Guid('{28ab0005-e845-4ffa-aa9b-f4665236141c}')
AnalogLocator = Guid('{49638b91-48ab-48b7-a47a-7d0e75a08ede}')
AnalogRadioTuningSpace = Guid('{8a674b4c-1f63-11d3-b64c-00c04f79498e}')
AnalogTVTuningSpace = Guid('{8a674b4d-1f63-11d3-b64c-00c04f79498e}')
DTV_CardStatus_Inserted: UInt32 = 0
DTV_CardStatus_Removed: UInt32 = 1
DTV_CardStatus_Error: UInt32 = 2
DTV_CardStatus_FirmwareDownload: UInt32 = 3
OCUR_PAIRING_PROTOCOL_VERSION: UInt32 = 2
PBDA_PAIRING_PROTOCOL_VERSION: UInt32 = 3
DTV_MMIMessage_Open: UInt32 = 0
DTV_MMIMessage_Close: UInt32 = 1
DTV_Entitlement_CanDecrypt: UInt32 = 0
DTV_Entitlement_NotEntitled: UInt32 = 1
DTV_Entitlement_TechnicalFailure: UInt32 = 2
AudioType_Standard: UInt32 = 0
AudioType_Music_And_Effects: UInt32 = 1
AudioType_Visually_Impaired: UInt32 = 2
AudioType_Hearing_Impaired: UInt32 = 3
AudioType_Dialogue: UInt32 = 4
AudioType_Commentary: UInt32 = 5
AudioType_Emergency: UInt32 = 6
AudioType_Voiceover: UInt32 = 7
AudioType_Reserved: Int32 = -1
MAX_COUNTRY_CODE_STRING: UInt32 = 3
PARENTAL_CONTROL_TIME_RANGE: UInt32 = 1
REQUIRED_PARENTAL_CONTROL_TIME_RANGE: UInt32 = 2
PARENTAL_CONTROL_CONTENT_RATING: UInt32 = 256
PARENTAL_CONTROL_ATTRIB_VIOLENCE: UInt32 = 512
PARENTAL_CONTROL_ATTRIB_LANGUAGE: UInt32 = 513
PARENTAL_CONTROL_ATTRIB_SEXUAL: UInt32 = 514
PARENTAL_CONTROL_ATTRIB_DIALOGUE: UInt32 = 515
PARENTAL_CONTROL_ATTRIB_FANTASY: UInt32 = 516
PARENTAL_CONTROL_VALUE_UNDEFINED: UInt32 = 0
MPEG2_FILTER_VERSION_1_SIZE: UInt32 = 124
MPEG2_FILTER_VERSION_2_SIZE: UInt32 = 133
SID_MSVidCtl_CurrentAudioEndpoint: Guid = Guid('{cf9a88f4-abcf-4ed8-9b74-7db33445459e}')
STREAMBUFFER_EC_BASE: UInt32 = 806
EVENTID_SBE2RecControlStarted: Guid = Guid('{8966a89e-f83e-4c0e-bc3b-bfa7649e04cb}')
EVENTID_SBE2RecControlStopped: Guid = Guid('{454b1ec8-0c9b-4caa-b1a1-1e7a2666f6c3}')
SBE2_STREAM_DESC_EVENT: Guid = Guid('{2313a4ed-bf2d-454f-ad8a-d95ba7f91fee}')
SBE2_V1_STREAMS_CREATION_EVENT: Guid = Guid('{000fcf09-97f5-46ac-9769-7a83b35384fb}')
SBE2_V2_STREAMS_CREATION_EVENT: Guid = Guid('{a72530a3-0344-4cab-a2d0-fe937dbdcab3}')
SBE2_STREAM_DESC_VERSION: UInt32 = 1
SID_DRMSecureServiceChannel: Guid = Guid('{c4c4c4c4-0049-4e2b-98fb-9537f6ce516d}')
CLSID_ETFilterEncProperties: Guid = Guid('{c4c4c481-0049-4e2b-98fb-9537f6ce516d}')
CLSID_ETFilterTagProperties: Guid = Guid('{c4c4c491-0049-4e2b-98fb-9537f6ce516d}')
CLSID_PTFilter: Guid = Guid('{9cd31617-b303-4f96-8330-2eb173ea4dc6}')
CLSID_DTFilterEncProperties: Guid = Guid('{c4c4c482-0049-4e2b-98fb-9537f6ce516d}')
CLSID_DTFilterTagProperties: Guid = Guid('{c4c4c492-0049-4e2b-98fb-9537f6ce516d}')
CLSID_XDSCodecProperties: Guid = Guid('{c4c4c483-0049-4e2b-98fb-9537f6ce516d}')
CLSID_XDSCodecTagProperties: Guid = Guid('{c4c4c493-0049-4e2b-98fb-9537f6ce516d}')
CLSID_CPCAFiltersCategory: Guid = Guid('{c4c4c4fc-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_XDSCodecNewXDSRating: Guid = Guid('{c4c4c4e0-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_XDSCodecDuplicateXDSRating: Guid = Guid('{c4c4c4df-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_XDSCodecNewXDSPacket: Guid = Guid('{c4c4c4e1-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterRatingChange: Guid = Guid('{c4c4c4e2-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterRatingsBlock: Guid = Guid('{c4c4c4e3-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterRatingsUnblock: Guid = Guid('{c4c4c4e4-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterXDSPacket: Guid = Guid('{c4c4c4e5-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_ETFilterEncryptionOn: Guid = Guid('{c4c4c4e6-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_ETFilterEncryptionOff: Guid = Guid('{c4c4c4e7-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterCOPPUnblock: Guid = Guid('{c4c4c4e8-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_EncDecFilterError: Guid = Guid('{c4c4c4e9-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterCOPPBlock: Guid = Guid('{c4c4c4ea-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_ETFilterCopyOnce: Guid = Guid('{c4c4c4eb-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_ETFilterCopyNever: Guid = Guid('{c4c4c4f0-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterDataFormatOK: Guid = Guid('{c4c4c4ec-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_DTFilterDataFormatFailure: Guid = Guid('{c4c4c4ed-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_ETDTFilterLicenseOK: Guid = Guid('{c4c4c4ee-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_ETDTFilterLicenseFailure: Guid = Guid('{c4c4c4ef-0049-4e2b-98fb-9537f6ce516d}')
MEDIASUBTYPE_ETDTFilter_Tagged: Guid = Guid('{c4c4c4d0-0049-4e2b-98fb-9537f6ce516d}')
FORMATTYPE_ETDTFilter_Tagged: Guid = Guid('{c4c4c4d1-0049-4e2b-98fb-9537f6ce516d}')
MEDIASUBTYPE_CPFilters_Processed: Guid = Guid('{46adbd28-6fd0-4796-93b2-155c51dc048d}')
FORMATTYPE_CPFilters_Processed: Guid = Guid('{6739b36f-1d5f-4ac2-8192-28bb0e73d16a}')
EVENTID_EncDecFilterEvent: Guid = Guid('{4a1b465b-0fb9-4159-afbd-e33006a0f9f4}')
EVENTID_FormatNotSupportedEvent: Guid = Guid('{24b2280a-b2aa-4777-bf65-63f35e7b024a}')
EVENTID_DemultiplexerFilterDiscontinuity: Guid = Guid('{16155770-aed5-475c-bb98-95a33070df0c}')
DSATTRIB_WMDRMProtectionInfo: Guid = Guid('{40749583-6b9d-4eec-b43c-67a1801e1a9b}')
DSATTRIB_BadSampleInfo: Guid = Guid('{e4846dda-5838-42b4-b897-6f7e5faa2f2f}')
MPEG_PAT_PID: UInt32 = 0
MPEG_PAT_TID: UInt32 = 0
MPEG_CAT_PID: UInt32 = 1
MPEG_CAT_TID: UInt32 = 1
MPEG_PMT_TID: UInt32 = 2
MPEG_TSDT_PID: UInt32 = 2
MPEG_TSDT_TID: UInt32 = 3
ATSC_MGT_PID: UInt32 = 8187
ATSC_MGT_TID: UInt32 = 199
ATSC_VCT_PID: UInt32 = 8187
ATSC_VCT_TERR_TID: UInt32 = 200
ATSC_VCT_CABL_TID: UInt32 = 201
ATSC_EIT_TID: UInt32 = 203
ATSC_ETT_TID: UInt32 = 204
ATSC_RRT_TID: UInt32 = 202
ATSC_RRT_PID: UInt32 = 8187
ATSC_STT_PID: UInt32 = 8187
ATSC_STT_TID: UInt32 = 205
ATSC_PIT_TID: UInt32 = 208
DVB_NIT_PID: UInt32 = 16
DVB_NIT_ACTUAL_TID: UInt32 = 64
DVB_NIT_OTHER_TID: UInt32 = 65
DVB_SDT_PID: UInt32 = 17
DVB_SDT_ACTUAL_TID: UInt32 = 66
DVB_SDT_OTHER_TID: UInt32 = 70
DVB_BAT_PID: UInt32 = 17
DVB_BAT_TID: UInt32 = 74
DVB_EIT_PID: UInt32 = 18
DVB_EIT_ACTUAL_TID: UInt32 = 78
DVB_EIT_OTHER_TID: UInt32 = 79
DVB_RST_PID: UInt32 = 19
DVB_RST_TID: UInt32 = 113
DVB_TDT_PID: UInt32 = 20
DVB_TDT_TID: UInt32 = 112
DVB_ST_PID_16: UInt32 = 16
DVB_ST_PID_17: UInt32 = 17
DVB_ST_PID_18: UInt32 = 18
DVB_ST_PID_19: UInt32 = 19
DVB_ST_PID_20: UInt32 = 20
DVB_ST_TID: UInt32 = 114
ISDB_ST_TID: UInt32 = 114
DVB_TOT_PID: UInt32 = 20
DVB_TOT_TID: UInt32 = 115
DVB_DIT_PID: UInt32 = 30
DVB_DIT_TID: UInt32 = 126
DVB_SIT_PID: UInt32 = 31
DVB_SIT_TID: UInt32 = 127
ISDB_EMM_TID: UInt32 = 133
ISDB_BIT_PID: UInt32 = 36
ISDB_BIT_TID: UInt32 = 196
ISDB_NBIT_PID: UInt32 = 37
ISDB_NBIT_MSG_TID: UInt32 = 197
ISDB_NBIT_REF_TID: UInt32 = 198
ISDB_LDT_PID: UInt32 = 37
ISDB_LDT_TID: UInt32 = 199
ISDB_SDTT_PID: UInt32 = 35
ISDB_SDTT_ALT_PID: UInt32 = 40
ISDB_SDTT_TID: UInt32 = 195
ISDB_CDT_PID: UInt32 = 41
ISDB_CDT_TID: UInt32 = 200
SCTE_EAS_TID: UInt32 = 216
SCTE_EAS_IB_PID: UInt32 = 8187
SCTE_EAS_OOB_PID: UInt32 = 8188
CLSID_Mpeg2TableFilter: Guid = Guid('{752845f1-758f-4c83-a043-4270c593308e}')
ATSC_ETM_LOCATION_NOT_PRESENT: UInt32 = 0
ATSC_ETM_LOCATION_IN_PTC_FOR_PSIP: UInt32 = 1
ATSC_ETM_LOCATION_IN_PTC_FOR_EVENT: UInt32 = 2
ATSC_ETM_LOCATION_RESERVED: UInt32 = 3
SAMPLE_SEQ_SEQUENCE_HEADER: UInt32 = 1
SAMPLE_SEQ_GOP_HEADER: UInt32 = 2
SAMPLE_SEQ_PICTURE_HEADER: UInt32 = 3
SAMPLE_SEQ_SEQUENCE_START: UInt32 = 1
SAMPLE_SEQ_SEEK_POINT: UInt32 = 2
SAMPLE_SEQ_FRAME_START: UInt32 = 3
SAMPLE_SEQ_CONTENT_UNKNOWN: UInt32 = 0
SAMPLE_SEQ_CONTENT_I_FRAME: UInt32 = 1
SAMPLE_SEQ_CONTENT_P_FRAME: UInt32 = 2
SAMPLE_SEQ_CONTENT_B_FRAME: UInt32 = 3
SAMPLE_SEQ_CONTENT_STANDALONE_FRAME: UInt32 = 1
SAMPLE_SEQ_CONTENT_REF_FRAME: UInt32 = 2
SAMPLE_SEQ_CONTENT_NONREF_FRAME: UInt32 = 3
COMPONENT_TAG_CAPTION_MIN: UInt32 = 48
COMPONENT_TAG_CAPTION_MAX: UInt32 = 55
COMPONENT_TAG_SUPERIMPOSE_MIN: UInt32 = 56
COMPONENT_TAG_SUPERIMPOSE_MAX: UInt32 = 63
DVBS_SCAN_TABLE_MAX_SIZE: UInt32 = 400
g_wszStreamBufferRecordingDuration: String = 'Duration'
g_wszStreamBufferRecordingBitrate: String = 'Bitrate'
g_wszStreamBufferRecordingSeekable: String = 'Seekable'
g_wszStreamBufferRecordingStridable: String = 'Stridable'
g_wszStreamBufferRecordingBroadcast: String = 'Broadcast'
g_wszStreamBufferRecordingProtected: String = 'Is_Protected'
g_wszStreamBufferRecordingTrusted: String = 'Is_Trusted'
g_wszStreamBufferRecordingSignature_Name: String = 'Signature_Name'
g_wszStreamBufferRecordingHasAudio: String = 'HasAudio'
g_wszStreamBufferRecordingHasImage: String = 'HasImage'
g_wszStreamBufferRecordingHasScript: String = 'HasScript'
g_wszStreamBufferRecordingHasVideo: String = 'HasVideo'
g_wszStreamBufferRecordingCurrentBitrate: String = 'CurrentBitrate'
g_wszStreamBufferRecordingOptimalBitrate: String = 'OptimalBitrate'
g_wszStreamBufferRecordingHasAttachedImages: String = 'HasAttachedImages'
g_wszStreamBufferRecordingSkipBackward: String = 'Can_Skip_Backward'
g_wszStreamBufferRecordingSkipForward: String = 'Can_Skip_Forward'
g_wszStreamBufferRecordingNumberOfFrames: String = 'NumberOfFrames'
g_wszStreamBufferRecordingFileSize: String = 'FileSize'
g_wszStreamBufferRecordingHasArbitraryDataStream: String = 'HasArbitraryDataStream'
g_wszStreamBufferRecordingHasFileTransferStream: String = 'HasFileTransferStream'
g_wszStreamBufferRecordingTitle: String = 'Title'
g_wszStreamBufferRecordingAuthor: String = 'Author'
g_wszStreamBufferRecordingDescription: String = 'Description'
g_wszStreamBufferRecordingRating: String = 'Rating'
g_wszStreamBufferRecordingCopyright: String = 'Copyright'
g_wszStreamBufferRecordingUse_DRM: String = 'Use_DRM'
g_wszStreamBufferRecordingDRM_Flags: String = 'DRM_Flags'
g_wszStreamBufferRecordingDRM_Level: String = 'DRM_Level'
g_wszStreamBufferRecordingAlbumTitle: String = 'WM/AlbumTitle'
g_wszStreamBufferRecordingTrack: String = 'WM/Track'
g_wszStreamBufferRecordingPromotionURL: String = 'WM/PromotionURL'
g_wszStreamBufferRecordingAlbumCoverURL: String = 'WM/AlbumCoverURL'
g_wszStreamBufferRecordingGenre: String = 'WM/Genre'
g_wszStreamBufferRecordingYear: String = 'WM/Year'
g_wszStreamBufferRecordingGenreID: String = 'WM/GenreID'
g_wszStreamBufferRecordingMCDI: String = 'WM/MCDI'
g_wszStreamBufferRecordingComposer: String = 'WM/Composer'
g_wszStreamBufferRecordingLyrics: String = 'WM/Lyrics'
g_wszStreamBufferRecordingTrackNumber: String = 'WM/TrackNumber'
g_wszStreamBufferRecordingToolName: String = 'WM/ToolName'
g_wszStreamBufferRecordingToolVersion: String = 'WM/ToolVersion'
g_wszStreamBufferRecordingIsVBR: String = 'IsVBR'
g_wszStreamBufferRecordingAlbumArtist: String = 'WM/AlbumArtist'
g_wszStreamBufferRecordingBannerImageType: String = 'BannerImageType'
g_wszStreamBufferRecordingBannerImageData: String = 'BannerImageData'
g_wszStreamBufferRecordingBannerImageURL: String = 'BannerImageURL'
g_wszStreamBufferRecordingCopyrightURL: String = 'CopyrightURL'
g_wszStreamBufferRecordingAspectRatioX: String = 'AspectRatioX'
g_wszStreamBufferRecordingAspectRatioY: String = 'AspectRatioY'
g_wszStreamBufferRecordingNSCName: String = 'NSC_Name'
g_wszStreamBufferRecordingNSCAddress: String = 'NSC_Address'
g_wszStreamBufferRecordingNSCPhone: String = 'NSC_Phone'
g_wszStreamBufferRecordingNSCEmail: String = 'NSC_Email'
g_wszStreamBufferRecordingNSCDescription: String = 'NSC_Description'
STREAMBUFFER_EC_TIMEHOLE: Int32 = 806
STREAMBUFFER_EC_STALE_DATA_READ: Int32 = 807
STREAMBUFFER_EC_STALE_FILE_DELETED: Int32 = 808
STREAMBUFFER_EC_CONTENT_BECOMING_STALE: Int32 = 809
STREAMBUFFER_EC_WRITE_FAILURE: Int32 = 810
STREAMBUFFER_EC_WRITE_FAILURE_CLEAR: Int32 = 811
STREAMBUFFER_EC_READ_FAILURE: Int32 = 812
STREAMBUFFER_EC_RATE_CHANGED: Int32 = 813
STREAMBUFFER_EC_PRIMARY_AUDIO: Int32 = 814
STREAMBUFFER_EC_RATE_CHANGING_FOR_SETPOSITIONS: Int32 = 815
STREAMBUFFER_EC_SETPOSITIONS_EVENTS_DONE: Int32 = 816
AuxInTuningSpace = Guid('{f9769a06-7aca-4e39-9cfb-97bb35f0e77e}')
BDANETWORKTYPE_ATSC = Guid('{71985f51-1ca1-11d3-9cc8-00c04f7971e0}')
class BDA_DEBUG_DATA(EasyCastStructure):
    lResult: Int32
    uuidDebugDataType: Guid
    ulDataSize: UInt32
    argbDebugData: Byte * 1
BDA_DEBUG_DATA_AVAILABLE = Guid('{69c24f54-9983-497e-b415-282be4c555fb}')
BDA_DEBUG_DATA_TYPE_STRING = Guid('{a806e767-de5c-430c-80bf-a21ebe06c748}')
BDA_DigitalSignalStandard = Int32
Bda_DigitalStandard_None: BDA_DigitalSignalStandard = 0
Bda_DigitalStandard_DVB_T: BDA_DigitalSignalStandard = 1
Bda_DigitalStandard_DVB_S: BDA_DigitalSignalStandard = 2
Bda_DigitalStandard_DVB_C: BDA_DigitalSignalStandard = 4
Bda_DigitalStandard_ATSC: BDA_DigitalSignalStandard = 8
Bda_DigitalStandard_ISDB_T: BDA_DigitalSignalStandard = 16
Bda_DigitalStandard_ISDB_S: BDA_DigitalSignalStandard = 32
Bda_DigitalStandard_ISDB_C: BDA_DigitalSignalStandard = 64
class BDA_EVENT_DATA(EasyCastStructure):
    lResult: Int32
    ulEventID: UInt32
    uuidEventType: Guid
    ulEventDataLength: UInt32
    argbEventData: Byte * 1
BDA_LockType = Int32
Bda_LockType_None: BDA_LockType = 0
Bda_LockType_PLL: BDA_LockType = 1
Bda_LockType_DecoderDemod: BDA_LockType = 2
Bda_LockType_Complete: BDA_LockType = 128
BDA_SignalType = Int32
Bda_SignalType_Unknown: BDA_SignalType = 0
Bda_SignalType_Analog: BDA_SignalType = 1
Bda_SignalType_Digital: BDA_SignalType = 2
class BDA_TRANSPORT_INFO(EasyCastStructure):
    ulcbPhyiscalPacket: UInt32
    ulcbPhyiscalFrame: UInt32
    ulcbPhyiscalFrameAlignment: UInt32
    AvgTimePerFrame: Int64
BSKYB_TERRESTRIAL_TV_NETWORK_TYPE = Guid('{9e9e46c6-3aba-4f08-ad0e-cc5ac8148c2b}')
class BadSampleInfo(EasyCastStructure):
    hrReason: Windows.Win32.Foundation.HRESULT
    _pack_ = 1
BfEnTvRat_Attributes_CAE_TV = Int32
CAE_IsBlocked: BfEnTvRat_Attributes_CAE_TV = 1
CAE_ValidAttrSubmask: BfEnTvRat_Attributes_CAE_TV = 1
BfEnTvRat_Attributes_CAF_TV = Int32
CAF_IsBlocked: BfEnTvRat_Attributes_CAF_TV = 1
CAF_ValidAttrSubmask: BfEnTvRat_Attributes_CAF_TV = 1
BfEnTvRat_Attributes_MPAA = Int32
MPAA_IsBlocked: BfEnTvRat_Attributes_MPAA = 1
MPAA_ValidAttrSubmask: BfEnTvRat_Attributes_MPAA = 1
BfEnTvRat_Attributes_US_TV = Int32
US_TV_IsBlocked: BfEnTvRat_Attributes_US_TV = 1
US_TV_IsViolent: BfEnTvRat_Attributes_US_TV = 2
US_TV_IsSexualSituation: BfEnTvRat_Attributes_US_TV = 4
US_TV_IsAdultLanguage: BfEnTvRat_Attributes_US_TV = 8
US_TV_IsSexuallySuggestiveDialog: BfEnTvRat_Attributes_US_TV = 16
US_TV_ValidAttrSubmask: BfEnTvRat_Attributes_US_TV = 31
BfEnTvRat_GenericAttributes = Int32
BfEnTvRat_GenericAttributes_BfAttrNone: BfEnTvRat_GenericAttributes = 0
BfEnTvRat_GenericAttributes_BfIsBlocked: BfEnTvRat_GenericAttributes = 1
BfEnTvRat_GenericAttributes_BfIsAttr_1: BfEnTvRat_GenericAttributes = 2
BfEnTvRat_GenericAttributes_BfIsAttr_2: BfEnTvRat_GenericAttributes = 4
BfEnTvRat_GenericAttributes_BfIsAttr_3: BfEnTvRat_GenericAttributes = 8
BfEnTvRat_GenericAttributes_BfIsAttr_4: BfEnTvRat_GenericAttributes = 16
BfEnTvRat_GenericAttributes_BfIsAttr_5: BfEnTvRat_GenericAttributes = 32
BfEnTvRat_GenericAttributes_BfIsAttr_6: BfEnTvRat_GenericAttributes = 64
BfEnTvRat_GenericAttributes_BfIsAttr_7: BfEnTvRat_GenericAttributes = 128
BfEnTvRat_GenericAttributes_BfValidAttrSubmask: BfEnTvRat_GenericAttributes = 255
BroadcastEventService = Guid('{0b3ffb92-0919-4934-9d5b-619c719d0202}')
class CAPTURE_STREAMTIME(EasyCastStructure):
    StreamTime: Int64
COPPEventBlockReason = Int32
COPP_Unknown: COPPEventBlockReason = -1
COPP_BadDriver: COPPEventBlockReason = 0
COPP_NoCardHDCPSupport: COPPEventBlockReason = 1
COPP_NoMonitorHDCPSupport: COPPEventBlockReason = 2
COPP_BadCertificate: COPPEventBlockReason = 3
COPP_InvalidBusProtection: COPPEventBlockReason = 4
COPP_AeroGlassOff: COPPEventBlockReason = 5
COPP_RogueApp: COPPEventBlockReason = 6
COPP_ForbiddenVideo: COPPEventBlockReason = 7
COPP_Activate: COPPEventBlockReason = 8
COPP_DigitalAudioUnprotected: COPPEventBlockReason = 9
CPEventBitShift = Int32
CPEVENT_BITSHIFT_RATINGS: CPEventBitShift = 0
CPEVENT_BITSHIFT_COPP: CPEventBitShift = 1
CPEVENT_BITSHIFT_LICENSE: CPEventBitShift = 2
CPEVENT_BITSHIFT_ROLLBACK: CPEventBitShift = 3
CPEVENT_BITSHIFT_SAC: CPEventBitShift = 4
CPEVENT_BITSHIFT_DOWNRES: CPEventBitShift = 5
CPEVENT_BITSHIFT_STUBLIB: CPEventBitShift = 6
CPEVENT_BITSHIFT_UNTRUSTEDGRAPH: CPEventBitShift = 7
CPEVENT_BITSHIFT_PENDING_CERTIFICATE: CPEventBitShift = 8
CPEVENT_BITSHIFT_NO_PLAYREADY: CPEventBitShift = 9
CPEvents = Int32
CPEVENT_NONE: CPEvents = 0
CPEVENT_RATINGS: CPEvents = 1
CPEVENT_COPP: CPEvents = 2
CPEVENT_LICENSE: CPEvents = 3
CPEVENT_ROLLBACK: CPEvents = 4
CPEVENT_SAC: CPEvents = 5
CPEVENT_DOWNRES: CPEvents = 6
CPEVENT_STUBLIB: CPEvents = 7
CPEVENT_UNTRUSTEDGRAPH: CPEvents = 8
CPEVENT_PROTECTWINDOWED: CPEvents = 9
CPRecordingStatus = Int32
RECORDING_STOPPED: CPRecordingStatus = 0
RECORDING_STARTED: CPRecordingStatus = 1
CRID_LOCATION = Int32
CRID_LOCATION_IN_DESCRIPTOR: CRID_LOCATION = 0
CRID_LOCATION_IN_CIT: CRID_LOCATION = 1
CRID_LOCATION_DVB_RESERVED1: CRID_LOCATION = 2
CRID_LOCATION_DVB_RESERVED2: CRID_LOCATION = 3
CROSSBAR_DEFAULT_FLAGS = Int32
DEF_MODE_PROFILE: CROSSBAR_DEFAULT_FLAGS = 1
DEF_MODE_STREAMS: CROSSBAR_DEFAULT_FLAGS = 2
CXDSData = Guid('{c4c4c4f4-0049-4e2b-98fb-9537f6ce516d}')
class ChannelChangeInfo(EasyCastStructure):
    state: Windows.Win32.Media.DirectShow.Tv.ChannelChangeSpanningEvent_State
    TimeStamp: UInt64
ChannelChangeSpanningEvent_State = Int32
ChannelChangeSpanningEvent_Start: ChannelChangeSpanningEvent_State = 0
ChannelChangeSpanningEvent_End: ChannelChangeSpanningEvent_State = 2
ChannelIDTuneRequest = Guid('{3a9428a7-31a4-45e9-9efb-e055bf7bb3db}')
ChannelIDTuningSpace = Guid('{cc829a2f-3365-463f-af13-81dbb6f3a555}')
class ChannelInfo(EasyCastStructure):
    lFrequency: Int32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        DVB: _DVB_e__Struct
        DC: _DC_e__Struct
        ATSC: _ATSC_e__Struct
        class _DVB_e__Struct(EasyCastStructure):
            lONID: Int32
            lTSID: Int32
            lSID: Int32
        class _DC_e__Struct(EasyCastStructure):
            lProgNumber: Int32
        class _ATSC_e__Struct(EasyCastStructure):
            lProgNumber: Int32
ChannelTuneRequest = Guid('{0369b4e5-45b6-11d3-b650-00c04f79498e}')
ChannelType = Int32
ChannelType_ChannelTypeNone: ChannelType = 0
ChannelType_ChannelTypeOther: ChannelType = 1
ChannelType_ChannelTypeVideo: ChannelType = 2
ChannelType_ChannelTypeAudio: ChannelType = 4
ChannelType_ChannelTypeText: ChannelType = 8
ChannelType_ChannelTypeSubtitles: ChannelType = 16
ChannelType_ChannelTypeCaptions: ChannelType = 32
ChannelType_ChannelTypeSuperimpose: ChannelType = 64
ChannelType_ChannelTypeData: ChannelType = 128
class ChannelTypeInfo(EasyCastStructure):
    channelType: Windows.Win32.Media.DirectShow.Tv.ChannelType
    timeStamp: UInt64
Component = Guid('{59dc47a8-116c-11d3-9d8e-00c04f72d980}')
ComponentType = Guid('{823535a0-0318-11d3-9d8e-00c04f72d980}')
ComponentTypes = Guid('{a1a2b1c4-0e3a-11d3-9d8e-00c04f72d980}')
Components = Guid('{809b6661-94c4-49e6-b6ec-3f0f862215aa}')
CreatePropBagOnRegKey = Guid('{8a674b49-1f63-11d3-b64c-00c04f79498e}')
DESC_LINKAGE_TYPE = Int32
DESC_LINKAGE_RESERVED0: DESC_LINKAGE_TYPE = 0
DESC_LINKAGE_INFORMATION: DESC_LINKAGE_TYPE = 1
DESC_LINKAGE_EPG: DESC_LINKAGE_TYPE = 2
DESC_LINKAGE_CA_REPLACEMENT: DESC_LINKAGE_TYPE = 3
DESC_LINKAGE_COMPLETE_NET_BOUQUET_SI: DESC_LINKAGE_TYPE = 4
DESC_LINKAGE_REPLACEMENT: DESC_LINKAGE_TYPE = 5
DESC_LINKAGE_DATA: DESC_LINKAGE_TYPE = 6
DESC_LINKAGE_RESERVED1: DESC_LINKAGE_TYPE = 7
DESC_LINKAGE_USER: DESC_LINKAGE_TYPE = 8
DESC_LINKAGE_RESERVED2: DESC_LINKAGE_TYPE = 255
DIGITAL_CABLE_NETWORK_TYPE = Guid('{143827ab-f77b-498d-81ca-5a007aec28bf}')
DIRECT_TV_SATELLITE_TV_NETWORK_TYPE = Guid('{93b66fb5-93d4-4323-921c-c1f52df61d3f}')
DISPID_TUNER = Int32
DISPID_TUNER_TS_UNIQUENAME: DISPID_TUNER = 1
DISPID_TUNER_TS_FRIENDLYNAME: DISPID_TUNER = 2
DISPID_TUNER_TS_CLSID: DISPID_TUNER = 3
DISPID_TUNER_TS_NETWORKTYPE: DISPID_TUNER = 4
DISPID_TUNER_TS__NETWORKTYPE: DISPID_TUNER = 5
DISPID_TUNER_TS_CREATETUNEREQUEST: DISPID_TUNER = 6
DISPID_TUNER_TS_ENUMCATEGORYGUIDS: DISPID_TUNER = 7
DISPID_TUNER_TS_ENUMDEVICEMONIKERS: DISPID_TUNER = 8
DISPID_TUNER_TS_DEFAULTPREFERREDCOMPONENTTYPES: DISPID_TUNER = 9
DISPID_TUNER_TS_FREQMAP: DISPID_TUNER = 10
DISPID_TUNER_TS_DEFLOCATOR: DISPID_TUNER = 11
DISPID_TUNER_TS_CLONE: DISPID_TUNER = 12
DISPID_TUNER_TR_TUNINGSPACE: DISPID_TUNER = 1
DISPID_TUNER_TR_COMPONENTS: DISPID_TUNER = 2
DISPID_TUNER_TR_CLONE: DISPID_TUNER = 3
DISPID_TUNER_TR_LOCATOR: DISPID_TUNER = 4
DISPID_TUNER_CT_CATEGORY: DISPID_TUNER = 1
DISPID_TUNER_CT_MEDIAMAJORTYPE: DISPID_TUNER = 2
DISPID_TUNER_CT__MEDIAMAJORTYPE: DISPID_TUNER = 3
DISPID_TUNER_CT_MEDIASUBTYPE: DISPID_TUNER = 4
DISPID_TUNER_CT__MEDIASUBTYPE: DISPID_TUNER = 5
DISPID_TUNER_CT_MEDIAFORMATTYPE: DISPID_TUNER = 6
DISPID_TUNER_CT__MEDIAFORMATTYPE: DISPID_TUNER = 7
DISPID_TUNER_CT_MEDIATYPE: DISPID_TUNER = 8
DISPID_TUNER_CT_CLONE: DISPID_TUNER = 9
DISPID_TUNER_LCT_LANGID: DISPID_TUNER = 100
DISPID_TUNER_MP2CT_TYPE: DISPID_TUNER = 200
DISPID_TUNER_ATSCCT_FLAGS: DISPID_TUNER = 300
DISPID_TUNER_L_CARRFREQ: DISPID_TUNER = 1
DISPID_TUNER_L_INNERFECMETHOD: DISPID_TUNER = 2
DISPID_TUNER_L_INNERFECRATE: DISPID_TUNER = 3
DISPID_TUNER_L_OUTERFECMETHOD: DISPID_TUNER = 4
DISPID_TUNER_L_OUTERFECRATE: DISPID_TUNER = 5
DISPID_TUNER_L_MOD: DISPID_TUNER = 6
DISPID_TUNER_L_SYMRATE: DISPID_TUNER = 7
DISPID_TUNER_L_CLONE: DISPID_TUNER = 8
DISPID_TUNER_L_ATSC_PHYS_CHANNEL: DISPID_TUNER = 201
DISPID_TUNER_L_ATSC_TSID: DISPID_TUNER = 202
DISPID_TUNER_L_ATSC_MP2_PROGNO: DISPID_TUNER = 203
DISPID_TUNER_L_DVBT_BANDWIDTH: DISPID_TUNER = 301
DISPID_TUNER_L_DVBT_LPINNERFECMETHOD: DISPID_TUNER = 302
DISPID_TUNER_L_DVBT_LPINNERFECRATE: DISPID_TUNER = 303
DISPID_TUNER_L_DVBT_GUARDINTERVAL: DISPID_TUNER = 304
DISPID_TUNER_L_DVBT_HALPHA: DISPID_TUNER = 305
DISPID_TUNER_L_DVBT_TRANSMISSIONMODE: DISPID_TUNER = 306
DISPID_TUNER_L_DVBT_INUSE: DISPID_TUNER = 307
DISPID_TUNER_L_DVBT2_PHYSICALLAYERPIPEID: DISPID_TUNER = 351
DISPID_TUNER_L_DVBS_POLARISATION: DISPID_TUNER = 401
DISPID_TUNER_L_DVBS_WEST: DISPID_TUNER = 402
DISPID_TUNER_L_DVBS_ORBITAL: DISPID_TUNER = 403
DISPID_TUNER_L_DVBS_AZIMUTH: DISPID_TUNER = 404
DISPID_TUNER_L_DVBS_ELEVATION: DISPID_TUNER = 405
DISPID_TUNER_L_DVBS2_DISEQ_LNB_SOURCE: DISPID_TUNER = 406
DISPID_TUNER_TS_DVBS2_LOW_OSC_FREQ_OVERRIDE: DISPID_TUNER = 407
DISPID_TUNER_TS_DVBS2_HI_OSC_FREQ_OVERRIDE: DISPID_TUNER = 408
DISPID_TUNER_TS_DVBS2_LNB_SWITCH_FREQ_OVERRIDE: DISPID_TUNER = 409
DISPID_TUNER_TS_DVBS2_SPECTRAL_INVERSION_OVERRIDE: DISPID_TUNER = 410
DISPID_TUNER_L_DVBS2_ROLLOFF: DISPID_TUNER = 411
DISPID_TUNER_L_DVBS2_PILOT: DISPID_TUNER = 412
DISPID_TUNER_L_ANALOG_STANDARD: DISPID_TUNER = 601
DISPID_TUNER_L_DTV_O_MAJOR_CHANNEL: DISPID_TUNER = 701
DISPID_TUNER_C_TYPE: DISPID_TUNER = 1
DISPID_TUNER_C_STATUS: DISPID_TUNER = 2
DISPID_TUNER_C_LANGID: DISPID_TUNER = 3
DISPID_TUNER_C_DESCRIPTION: DISPID_TUNER = 4
DISPID_TUNER_C_CLONE: DISPID_TUNER = 5
DISPID_TUNER_C_MP2_PID: DISPID_TUNER = 101
DISPID_TUNER_C_MP2_PCRPID: DISPID_TUNER = 102
DISPID_TUNER_C_MP2_PROGNO: DISPID_TUNER = 103
DISPID_TUNER_C_ANALOG_AUDIO: DISPID_TUNER = 201
DISPID_TUNER_TS_DVB_SYSTEMTYPE: DISPID_TUNER = 101
DISPID_TUNER_TS_DVB2_NETWORK_ID: DISPID_TUNER = 102
DISPID_TUNER_TS_DVBS_LOW_OSC_FREQ: DISPID_TUNER = 1001
DISPID_TUNER_TS_DVBS_HI_OSC_FREQ: DISPID_TUNER = 1002
DISPID_TUNER_TS_DVBS_LNB_SWITCH_FREQ: DISPID_TUNER = 1003
DISPID_TUNER_TS_DVBS_INPUT_RANGE: DISPID_TUNER = 1004
DISPID_TUNER_TS_DVBS_SPECTRAL_INVERSION: DISPID_TUNER = 1005
DISPID_TUNER_TS_AR_MINFREQUENCY: DISPID_TUNER = 101
DISPID_TUNER_TS_AR_MAXFREQUENCY: DISPID_TUNER = 102
DISPID_TUNER_TS_AR_STEP: DISPID_TUNER = 103
DISPID_TUNER_TS_AR_COUNTRYCODE: DISPID_TUNER = 104
DISPID_TUNER_TS_AUX_COUNTRYCODE: DISPID_TUNER = 101
DISPID_TUNER_TS_ATV_MINCHANNEL: DISPID_TUNER = 101
DISPID_TUNER_TS_ATV_MAXCHANNEL: DISPID_TUNER = 102
DISPID_TUNER_TS_ATV_INPUTTYPE: DISPID_TUNER = 103
DISPID_TUNER_TS_ATV_COUNTRYCODE: DISPID_TUNER = 104
DISPID_TUNER_TS_ATSC_MINMINORCHANNEL: DISPID_TUNER = 201
DISPID_TUNER_TS_ATSC_MAXMINORCHANNEL: DISPID_TUNER = 202
DISPID_TUNER_TS_ATSC_MINPHYSCHANNEL: DISPID_TUNER = 203
DISPID_TUNER_TS_ATSC_MAXPHYSCHANNEL: DISPID_TUNER = 204
DISPID_TUNER_TS_DC_MINMAJORCHANNEL: DISPID_TUNER = 301
DISPID_TUNER_TS_DC_MAXMAJORCHANNEL: DISPID_TUNER = 302
DISPID_TUNER_TS_DC_MINSOURCEID: DISPID_TUNER = 303
DISPID_TUNER_TS_DC_MAXSOURCEID: DISPID_TUNER = 304
DISPID_CHTUNER_ATVAC_CHANNEL: DISPID_TUNER = 101
DISPID_CHTUNER_ATVDC_SYSTEM: DISPID_TUNER = 101
DISPID_CHTUNER_ATVDC_CONTENT: DISPID_TUNER = 102
DISPID_CHTUNER_CIDTR_CHANNELID: DISPID_TUNER = 101
DISPID_CHTUNER_CTR_CHANNEL: DISPID_TUNER = 101
DISPID_CHTUNER_ACTR_MINOR_CHANNEL: DISPID_TUNER = 201
DISPID_CHTUNER_DCTR_MAJOR_CHANNEL: DISPID_TUNER = 301
DISPID_CHTUNER_DCTR_SRCID: DISPID_TUNER = 302
DISPID_DVBTUNER_DVBC_ATTRIBUTESVALID: DISPID_TUNER = 101
DISPID_DVBTUNER_DVBC_PID: DISPID_TUNER = 102
DISPID_DVBTUNER_DVBC_TAG: DISPID_TUNER = 103
DISPID_DVBTUNER_DVBC_COMPONENTTYPE: DISPID_TUNER = 104
DISPID_DVBTUNER_ONID: DISPID_TUNER = 101
DISPID_DVBTUNER_TSID: DISPID_TUNER = 102
DISPID_DVBTUNER_SID: DISPID_TUNER = 103
DISPID_MP2TUNER_TSID: DISPID_TUNER = 101
DISPID_MP2TUNER_PROGNO: DISPID_TUNER = 102
DISPID_MP2TUNERFACTORY_CREATETUNEREQUEST: DISPID_TUNER = 1
class DSHOW_STREAM_DESC(EasyCastStructure):
    VersionNo: UInt32
    StreamId: UInt32
    Default: Windows.Win32.Foundation.BOOL
    Creation: Windows.Win32.Foundation.BOOL
    Reserved: UInt32
class DSMCC_ELEMENT(EasyCastStructure):
    pid: UInt16
    bComponentTag: Byte
    dwCarouselId: UInt32
    dwTransactionId: UInt32
    pNext: POINTER(Windows.Win32.Media.DirectShow.Tv.DSMCC_ELEMENT_head)
    _pack_ = 1
class DSMCC_FILTER_OPTIONS(EasyCastStructure):
    fSpecifyProtocol: Windows.Win32.Foundation.BOOL
    Protocol: Byte
    fSpecifyType: Windows.Win32.Foundation.BOOL
    Type: Byte
    fSpecifyMessageId: Windows.Win32.Foundation.BOOL
    MessageId: UInt16
    fSpecifyTransactionId: Windows.Win32.Foundation.BOOL
    fUseTrxIdMessageIdMask: Windows.Win32.Foundation.BOOL
    TransactionId: UInt32
    fSpecifyModuleVersion: Windows.Win32.Foundation.BOOL
    ModuleVersion: Byte
    fSpecifyBlockNumber: Windows.Win32.Foundation.BOOL
    BlockNumber: UInt16
    fGetModuleCall: Windows.Win32.Foundation.BOOL
    NumberOfBlocksInModule: UInt16
    _pack_ = 1
class DSMCC_SECTION(EasyCastStructure):
    TableId: Byte
    Header: _Header_e__Union
    TableIdExtension: UInt16
    Version: _Version_e__Union
    SectionNumber: Byte
    LastSectionNumber: Byte
    ProtocolDiscriminator: Byte
    DsmccType: Byte
    MessageId: UInt16
    TransactionId: UInt32
    Reserved: Byte
    AdaptationLength: Byte
    MessageLength: UInt16
    RemainingData: Byte * 1
    _pack_ = 1
    class _Header_e__Union(EasyCastUnion):
        S: Windows.Win32.Media.DirectShow.Tv.MPEG_HEADER_BITS_MIDL
        W: UInt16
        _pack_ = 1
    class _Version_e__Union(EasyCastUnion):
        S: Windows.Win32.Media.DirectShow.Tv.MPEG_HEADER_VERSION_BITS_MIDL
        B: Byte
DTFilter = Guid('{c4c4c4f2-0049-4e2b-98fb-9537f6ce516d}')
DVBCLocator = Guid('{c531d9fd-9685-4028-8b68-6e1232079f1e}')
DVBSLocator = Guid('{1df7d126-4050-47f0-a7cf-4c4ca9241333}')
DVBSTuningSpace = Guid('{b64016f3-c9a2-4066-96f0-bd9563314726}')
class DVBScramblingControlSpanningEvent(EasyCastStructure):
    ulPID: UInt32
    fScrambled: Windows.Win32.Foundation.BOOL
DVBTLocator = Guid('{9cd64701-bdf3-4d14-8e03-f12983d86664}')
DVBTLocator2 = Guid('{efe3fa02-45d7-4920-be96-53fa7f35b0e6}')
DVBTuneRequest = Guid('{15d6504a-5494-499c-886c-973c9e53b9f1}')
DVBTuningSpace = Guid('{c6b14b32-76aa-4a86-a7ac-5c79aaf58da7}')
DVB_CABLE_TV_NETWORK_TYPE = Guid('{dc0c0fe7-0485-4266-b93f-68fbf80ed834}')
class DVB_EIT_FILTER_OPTIONS(EasyCastStructure):
    fSpecifySegment: Windows.Win32.Foundation.BOOL
    bSegment: Byte
    _pack_ = 1
DVB_SATELLITE_TV_NETWORK_TYPE = Guid('{fa4b375a-45b4-4d45-8440-263957b11623}')
DVB_STRCONV_MODE = Int32
STRCONV_MODE_DVB: DVB_STRCONV_MODE = 0
STRCONV_MODE_DVB_EMPHASIS: DVB_STRCONV_MODE = 1
STRCONV_MODE_DVB_WITHOUT_EMPHASIS: DVB_STRCONV_MODE = 2
STRCONV_MODE_ISDB: DVB_STRCONV_MODE = 3
DVB_TERRESTRIAL_TV_NETWORK_TYPE = Guid('{216c62df-6d7f-4e9a-8571-05f14edb766a}')
DVDFilterState = Int32
dvdState_Undefined: DVDFilterState = -2
dvdState_Unitialized: DVDFilterState = -1
dvdState_Stopped: DVDFilterState = 0
dvdState_Paused: DVDFilterState = 1
dvdState_Running: DVDFilterState = 2
DVDMenuIDConstants = Int32
dvdMenu_Title: DVDMenuIDConstants = 2
dvdMenu_Root: DVDMenuIDConstants = 3
dvdMenu_Subpicture: DVDMenuIDConstants = 4
dvdMenu_Audio: DVDMenuIDConstants = 5
dvdMenu_Angle: DVDMenuIDConstants = 6
dvdMenu_Chapter: DVDMenuIDConstants = 7
DVDSPExt = Int32
dvdSPExt_NotSpecified: DVDSPExt = 0
dvdSPExt_Caption_Normal: DVDSPExt = 1
dvdSPExt_Caption_Big: DVDSPExt = 2
dvdSPExt_Caption_Children: DVDSPExt = 3
dvdSPExt_CC_Normal: DVDSPExt = 5
dvdSPExt_CC_Big: DVDSPExt = 6
dvdSPExt_CC_Children: DVDSPExt = 7
dvdSPExt_Forced: DVDSPExt = 9
dvdSPExt_DirectorComments_Normal: DVDSPExt = 13
dvdSPExt_DirectorComments_Big: DVDSPExt = 14
dvdSPExt_DirectorComments_Children: DVDSPExt = 15
DVDTextStringType = Int32
dvdStruct_Volume: DVDTextStringType = 1
dvdStruct_Title: DVDTextStringType = 2
dvdStruct_ParentalID: DVDTextStringType = 3
dvdStruct_PartOfTitle: DVDTextStringType = 4
dvdStruct_Cell: DVDTextStringType = 5
dvdStream_Audio: DVDTextStringType = 16
dvdStream_Subpicture: DVDTextStringType = 17
dvdStream_Angle: DVDTextStringType = 18
dvdChannel_Audio: DVDTextStringType = 32
dvdGeneral_Name: DVDTextStringType = 48
dvdGeneral_Comments: DVDTextStringType = 49
dvdTitle_Series: DVDTextStringType = 56
dvdTitle_Movie: DVDTextStringType = 57
dvdTitle_Video: DVDTextStringType = 58
dvdTitle_Album: DVDTextStringType = 59
dvdTitle_Song: DVDTextStringType = 60
dvdTitle_Other: DVDTextStringType = 63
dvdTitle_Sub_Series: DVDTextStringType = 64
dvdTitle_Sub_Movie: DVDTextStringType = 65
dvdTitle_Sub_Video: DVDTextStringType = 66
dvdTitle_Sub_Album: DVDTextStringType = 67
dvdTitle_Sub_Song: DVDTextStringType = 68
dvdTitle_Sub_Other: DVDTextStringType = 71
dvdTitle_Orig_Series: DVDTextStringType = 72
dvdTitle_Orig_Movie: DVDTextStringType = 73
dvdTitle_Orig_Video: DVDTextStringType = 74
dvdTitle_Orig_Album: DVDTextStringType = 75
dvdTitle_Orig_Song: DVDTextStringType = 76
dvdTitle_Orig_Other: DVDTextStringType = 79
dvdOther_Scene: DVDTextStringType = 80
dvdOther_Cut: DVDTextStringType = 81
dvdOther_Take: DVDTextStringType = 82
class DVR_STREAM_DESC(EasyCastStructure):
    Version: UInt32
    StreamId: UInt32
    Default: Windows.Win32.Foundation.BOOL
    Creation: Windows.Win32.Foundation.BOOL
    Reserved: UInt32
    guidSubMediaType: Guid
    guidFormatType: Guid
    MediaType: Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE
DigitalCableLocator = Guid('{03c06416-d127-407a-ab4c-fdd279abbe5d}')
DigitalCableTuneRequest = Guid('{26ec0b63-aa90-458a-8df4-5659f2c8a18a}')
DigitalCableTuningSpace = Guid('{d9bb4cee-b87a-47f1-ac92-b08d9c7813fc}')
DigitalLocator = Guid('{6e50cc0d-c19b-4bf6-810b-5bd60761f5cc}')
DisplaySizeList = Int32
DisplaySizeList_dslDefaultSize: DisplaySizeList = 0
DisplaySizeList_dslSourceSize: DisplaySizeList = 0
DisplaySizeList_dslHalfSourceSize: DisplaySizeList = 1
DisplaySizeList_dslDoubleSourceSize: DisplaySizeList = 2
DisplaySizeList_dslFullScreen: DisplaySizeList = 3
DisplaySizeList_dslHalfScreen: DisplaySizeList = 4
DisplaySizeList_dslQuarterScreen: DisplaySizeList = 5
DisplaySizeList_dslSixteenthScreen: DisplaySizeList = 6
DownResEventParam = Int32
DOWNRES_Always: DownResEventParam = 0
DOWNRES_InWindowOnly: DownResEventParam = 1
DOWNRES_Undefined: DownResEventParam = 2
class DualMonoInfo(EasyCastStructure):
    LangID1: UInt16
    LangID2: UInt16
    lISOLangCode1: Int32
    lISOLangCode2: Int32
class DvbParentalRatingDescriptor(EasyCastStructure):
    ulNumParams: UInt32
    pParams: Windows.Win32.Media.DirectShow.Tv.DvbParentalRatingParam * 1
class DvbParentalRatingParam(EasyCastStructure):
    szCountryCode: Windows.Win32.Foundation.CHAR * 4
    bRating: Byte
ECHOSTAR_SATELLITE_TV_NETWORK_TYPE = Guid('{c4f6b31b-c6bf-4759-886f-a7386dca27a0}')
ESEventFactory = Guid('{8e8a07da-71f8-40c1-a929-5e3a868ac2c6}')
ESEventService = Guid('{c20447fc-ec60-475e-813f-d2b0a6decefe}')
ETFilter = Guid('{c4c4c4f1-0049-4e2b-98fb-9537f6ce516d}')
EVENTID_ARIBcontentSpanningEvent = Guid('{3a954083-93d0-463e-90b2-0742c496edf0}')
EVENTID_AudioDescriptorSpanningEvent = Guid('{107bd41c-a6da-4691-8369-11b2cdaa288e}')
EVENTID_AudioTypeSpanningEvent = Guid('{501cbfbe-b849-42ce-9be9-3db869fb82b3}')
EVENTID_BDAConditionalAccessTAG = Guid('{efc3a459-ae8b-4b4a-8fe9-79a0d097f3ea}')
EVENTID_BDAEventingServicePendingEvent = Guid('{5ca51711-5ddc-41a6-9430-e41b8b3bbc5b}')
EVENTID_BDA_CASBroadcastMMI = Guid('{676876f0-1132-404c-a7ca-e72069a9d54f}')
EVENTID_BDA_CASCloseMMI = Guid('{5d0f550f-de2e-479d-8345-ec0e9557e8a2}')
EVENTID_BDA_CASOpenMMI = Guid('{85dac915-e593-410d-8471-d6812105f28e}')
EVENTID_BDA_CASReleaseTuner = Guid('{20c1a16b-441f-49a5-bb5c-e9a04495c6c1}')
EVENTID_BDA_CASRequestTuner = Guid('{cf39a9d8-f5d3-4685-be57-ed81dba46b27}')
EVENTID_BDA_DiseqCResponseAvailable = Guid('{efa628f8-1f2c-4b67-9ea5-acf6fa9a1f36}')
EVENTID_BDA_EncoderSignalLock = Guid('{5ec90eb9-39fa-4cfc-b93f-00bb11077f5e}')
EVENTID_BDA_FdcStatus = Guid('{05f25366-d0eb-43d2-bc3c-682b863df142}')
EVENTID_BDA_FdcTableSection = Guid('{6a0cd757-4ce3-4e5b-9444-7187b87152c5}')
EVENTID_BDA_GPNVValueUpdate = Guid('{ff75c68c-f416-4e7e-bf17-6d55c5df1575}')
EVENTID_BDA_GuideDataAvailable = Guid('{98db717a-478a-4cd4-92d0-95f66b89e5b1}')
EVENTID_BDA_GuideDataError = Guid('{ac33c448-6f73-4fd7-b341-594c360d8d74}')
EVENTID_BDA_GuideServiceInformationUpdated = Guid('{a1c3ea2b-175f-4458-b735-507d22db23a6}')
EVENTID_BDA_IsdbCASResponse = Guid('{d4cb1966-41bc-4ced-9a20-fdceac78f70d}')
EVENTID_BDA_LbigsCloseConnectionHandle = Guid('{c2f08b99-65ef-4314-9671-e99d4cce0bae}')
EVENTID_BDA_LbigsOpenConnection = Guid('{356207b2-6f31-4eb0-a271-b3fa6bb7680f}')
EVENTID_BDA_LbigsSendData = Guid('{1123277b-f1c6-4154-8b0d-48e6157059aa}')
EVENTID_BDA_RatingPinReset = Guid('{c6e048c0-c574-4c26-bcda-2f4d35eb5e85}')
EVENTID_BDA_TransprtStreamSelectorInfo = Guid('{c40f9f85-09d0-489c-9e9c-0abbb56951b0}')
EVENTID_BDA_TunerNoSignal = Guid('{e29b382b-1edd-4930-bc46-682fd72d2dfb}')
EVENTID_BDA_TunerSignalLock = Guid('{1872e740-f573-429b-a00e-d9c1e408af09}')
EVENTID_BDA_UpdateDrmStatus = Guid('{65a6f681-1462-473b-88ce-cb731427bdb5}')
EVENTID_BDA_UpdateScanState = Guid('{55702b50-7b49-42b8-a82f-4afb691b0628}')
EVENTID_CADenialCountChanged = Guid('{2a65c528-2249-4070-ac16-00390cdfb2dd}')
EVENTID_CASFailureSpanningEvent = Guid('{ead831ae-5529-4d1f-afce-0d8cd1257d30}')
EVENTID_CSDescriptorSpanningEvent = Guid('{efe779d9-97f0-4786-800d-95cf505ddc66}')
EVENTID_CandidatePostTuneData = Guid('{9f02d3d0-9f06-4369-9f1e-3ad6ca19807e}')
EVENTID_CardStatusChanged = Guid('{a265faea-f874-4b38-9ff7-c53d02969996}')
EVENTID_ChannelChangeSpanningEvent = Guid('{9067c5e5-4c5c-4205-86c8-7afe20fe1efa}')
EVENTID_ChannelInfoSpanningEvent = Guid('{41f36d80-4132-4cc2-b121-01a43219d81b}')
EVENTID_ChannelTypeSpanningEvent = Guid('{72ab1d51-87d2-489b-ba11-0e08dc210243}')
EVENTID_CtxADescriptorSpanningEvent = Guid('{3ab4a2e6-4247-4b34-896c-30afa5d21c24}')
EVENTID_DFNWithNoActualAVData = Guid('{f5689ffe-55f9-4bb3-96be-ae971c63bae0}')
EVENTID_DRMParingStatusChanged = Guid('{000906f5-f0d1-41d6-a7df-4028697669f6}')
EVENTID_DRMParingStepComplete = Guid('{5b2ebf78-b752-4420-b41e-a472dc95828e}')
EVENTID_DVBScramblingControlSpanningEvent = Guid('{4bd4e1c4-90a1-4109-8236-27f00e7dcc5b}')
EVENTID_DualMonoSpanningEvent = Guid('{a9a29b56-a84b-488c-89d5-0d4e7657c8ce}')
EVENTID_DvbParentalRatingDescriptor = Guid('{2a67a58d-eca5-4eac-abcb-e734d3776d0a}')
EVENTID_EASMessageReceived = Guid('{d10df9d5-c261-4b85-9e8a-517b3299cab2}')
EVENTID_EmmMessageSpanningEvent = Guid('{6bf00268-4f7e-4294-aa87-e9e953e43f14}')
EVENTID_EntitlementChanged = Guid('{9071ad5d-2359-4c95-8694-afa81d70bfd5}')
EVENTID_LanguageSpanningEvent = Guid('{e292666d-9c02-448d-aa8d-781a93fdc395}')
EVENTID_MMIMessage = Guid('{052c29af-09a4-4b93-890f-bd6a348968a4}')
EVENTID_NewSignalAcquired = Guid('{c87ec52d-cd18-404a-a076-c02a273d3de7}')
EVENTID_PBDAParentalControlEvent = Guid('{f947aa85-fb52-48e8-b9c5-e1e1f411a51a}')
EVENTID_PIDListSpanningEvent = Guid('{47fc8f65-e2bb-4634-9cef-fdbfe6261d5c}')
EVENTID_PSITable = Guid('{1b9c3703-d447-4e16-97bb-01799fc031ed}')
EVENTID_RRTSpanningEvent = Guid('{f6cfc8f4-da93-4f2f-bff8-ba1ee6fca3a2}')
EVENTID_STBChannelNumber = Guid('{17c4d730-d0f0-413a-8c99-500469de35ad}')
EVENTID_ServiceTerminated = Guid('{0a1d591c-e0d2-4f8e-8960-2335bef45ccb}')
EVENTID_SignalAndServiceStatusSpanningEvent = Guid('{8068c5cb-3c04-492b-b47d-0308820dce51}')
EVENTID_SignalStatusChanged = Guid('{6d9cfaf2-702d-4b01-8dff-6892ad20d191}')
EVENTID_StreamIDSpanningEvent = Guid('{caf1ab68-e153-4d41-a6b3-a7c998db75ee}')
EVENTID_StreamTypeSpanningEvent = Guid('{82af2ebc-30a6-4264-a80b-ad2e1372ac60}')
EVENTID_SubtitleSpanningEvent = Guid('{5dcec048-d0b9-4163-872c-4f32223be88a}')
EVENTID_TeletextSpanningEvent = Guid('{9599d950-5f33-4617-af7c-1e54b510daa3}')
EVENTID_TuneFailureEvent = Guid('{d97287b2-2dfd-436a-9485-99d7d4ab5a69}')
EVENTID_TuneFailureSpanningEvent = Guid('{6f8aa455-5ee1-48ab-a27c-4c8d70b9aeba}')
EVENTID_TuningChanged = Guid('{9d7e6235-4b7d-425d-a6d1-d717c33b9c4c}')
EVENTID_TuningChanging = Guid('{83183c03-c09e-45c4-a719-807a94952bf9}')
EVENTTYPE_CASDescrambleFailureEvent = Guid('{b2127d42-7be5-4f4b-9130-6679899f4f4b}')
EnTag_Mode = Int32
EnTag_Remove: EnTag_Mode = 0
EnTag_Once: EnTag_Mode = 1
EnTag_Repeat: EnTag_Mode = 2
EnTvRat_CAE_TV = Int32
CAE_TV_Exempt: EnTvRat_CAE_TV = 0
CAE_TV_C: EnTvRat_CAE_TV = 1
CAE_TV_C8: EnTvRat_CAE_TV = 2
CAE_TV_G: EnTvRat_CAE_TV = 3
CAE_TV_PG: EnTvRat_CAE_TV = 4
CAE_TV_14: EnTvRat_CAE_TV = 5
CAE_TV_18: EnTvRat_CAE_TV = 6
CAE_TV_Reserved: EnTvRat_CAE_TV = 7
EnTvRat_CAF_TV = Int32
CAF_TV_Exempt: EnTvRat_CAF_TV = 0
CAF_TV_G: EnTvRat_CAF_TV = 1
CAF_TV_8: EnTvRat_CAF_TV = 2
CAF_TV_13: EnTvRat_CAF_TV = 3
CAF_TV_16: EnTvRat_CAF_TV = 4
CAF_TV_18: EnTvRat_CAF_TV = 5
CAF_TV_Reserved6: EnTvRat_CAF_TV = 6
CAF_TV_Reserved: EnTvRat_CAF_TV = 7
EnTvRat_GenericLevel = Int32
TvRat_0: EnTvRat_GenericLevel = 0
TvRat_1: EnTvRat_GenericLevel = 1
TvRat_2: EnTvRat_GenericLevel = 2
TvRat_3: EnTvRat_GenericLevel = 3
TvRat_4: EnTvRat_GenericLevel = 4
TvRat_5: EnTvRat_GenericLevel = 5
TvRat_6: EnTvRat_GenericLevel = 6
TvRat_7: EnTvRat_GenericLevel = 7
TvRat_8: EnTvRat_GenericLevel = 8
TvRat_9: EnTvRat_GenericLevel = 9
TvRat_10: EnTvRat_GenericLevel = 10
TvRat_11: EnTvRat_GenericLevel = 11
TvRat_12: EnTvRat_GenericLevel = 12
TvRat_13: EnTvRat_GenericLevel = 13
TvRat_14: EnTvRat_GenericLevel = 14
TvRat_15: EnTvRat_GenericLevel = 15
TvRat_16: EnTvRat_GenericLevel = 16
TvRat_17: EnTvRat_GenericLevel = 17
TvRat_18: EnTvRat_GenericLevel = 18
TvRat_19: EnTvRat_GenericLevel = 19
TvRat_20: EnTvRat_GenericLevel = 20
TvRat_21: EnTvRat_GenericLevel = 21
TvRat_kLevels: EnTvRat_GenericLevel = 22
TvRat_Unblock: EnTvRat_GenericLevel = -1
TvRat_LevelDontKnow: EnTvRat_GenericLevel = 255
EnTvRat_MPAA = Int32
MPAA_NotApplicable: EnTvRat_MPAA = 0
MPAA_G: EnTvRat_MPAA = 1
MPAA_PG: EnTvRat_MPAA = 2
MPAA_PG13: EnTvRat_MPAA = 3
MPAA_R: EnTvRat_MPAA = 4
MPAA_NC17: EnTvRat_MPAA = 5
MPAA_X: EnTvRat_MPAA = 6
MPAA_NotRated: EnTvRat_MPAA = 7
EnTvRat_System = Int32
EnTvRat_System_MPAA: EnTvRat_System = 0
EnTvRat_System_US_TV: EnTvRat_System = 1
EnTvRat_System_Canadian_English: EnTvRat_System = 2
EnTvRat_System_Canadian_French: EnTvRat_System = 3
EnTvRat_System_Reserved4: EnTvRat_System = 4
EnTvRat_System_System5: EnTvRat_System = 5
EnTvRat_System_System6: EnTvRat_System = 6
EnTvRat_System_Reserved7: EnTvRat_System = 7
EnTvRat_System_PBDA: EnTvRat_System = 8
EnTvRat_System_AgeBased: EnTvRat_System = 9
EnTvRat_System_TvRat_kSystems: EnTvRat_System = 10
EnTvRat_System_TvRat_SystemDontKnow: EnTvRat_System = 255
EnTvRat_US_TV = Int32
US_TV_None: EnTvRat_US_TV = 0
US_TV_Y: EnTvRat_US_TV = 1
US_TV_Y7: EnTvRat_US_TV = 2
US_TV_G: EnTvRat_US_TV = 3
US_TV_PG: EnTvRat_US_TV = 4
US_TV_14: EnTvRat_US_TV = 5
US_TV_MA: EnTvRat_US_TV = 6
US_TV_None7: EnTvRat_US_TV = 7
EncDecEvents = Int32
ENCDEC_CPEVENT: EncDecEvents = 0
ENCDEC_RECORDING_STATUS: EncDecEvents = 1
EvalRat = Guid('{c5c5c5f1-3abc-11d6-b25b-00c04fa0c026}')
FormatNotSupportedEvents = Int32
FORMATNOTSUPPORTED_CLEAR: FormatNotSupportedEvents = 0
FORMATNOTSUPPORTED_NOTSUPPORTED: FormatNotSupportedEvents = 1
class IATSCChannelTuneRequest(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IChannelTuneRequest
    _iid_ = Guid('{0369b4e1-45b6-11d3-b650-00c04f79498e}')
    @commethod(14)
    def get_MinorChannel(self, MinorChannel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_MinorChannel(self, MinorChannel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IATSCComponentType(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMPEG2ComponentType
    _iid_ = Guid('{fc189e4d-7bd4-4125-b3b3-3a76a332cc96}')
    @commethod(28)
    def get_Flags(self, Flags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Flags(self, flags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IATSCLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDigitalLocator
    _iid_ = Guid('{bf8d986f-8c2b-4131-94d7-4d3d9fcc21ef}')
    @commethod(22)
    def get_PhysicalChannel(self, PhysicalChannel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_PhysicalChannel(self, PhysicalChannel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_TSID(self, TSID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_TSID(self, TSID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IATSCLocator2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IATSCLocator
    _iid_ = Guid('{612aa885-66cf-4090-ba0a-566f5312e4ca}')
    @commethod(26)
    def get_ProgramNumber(self, ProgramNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_ProgramNumber(self, ProgramNumber: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IATSCTuningSpace(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IAnalogTVTuningSpace
    _iid_ = Guid('{0369b4e2-45b6-11d3-b650-00c04f79498e}')
    @commethod(34)
    def get_MinMinorChannel(self, MinMinorChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_MinMinorChannel(self, NewMinMinorChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_MaxMinorChannel(self, MaxMinorChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_MaxMinorChannel(self, NewMaxMinorChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_MinPhysicalChannel(self, MinPhysicalChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_MinPhysicalChannel(self, NewMinPhysicalChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_MaxPhysicalChannel(self, MaxPhysicalChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_MaxPhysicalChannel(self, NewMaxPhysicalChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IATSC_EIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d7c212d7-76a2-4b4b-aa56-846879a80096}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSourceId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProtocolVersion(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordEventId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordStartTime(self, dwRecordIndex: UInt32, pmdtVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordEtmLocation(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordDuration(self, dwRecordIndex: UInt32, pmdVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordTitleText(self, dwRecordIndex: UInt32, pdwLength: POINTER(UInt32), ppText: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IATSC_ETT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5a142cc9-b8cf-4a86-a040-e9cadf3ef3e7}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProtocolVersion(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEtmId(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetExtendedMessageText(self, pdwLength: POINTER(UInt32), ppText: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IATSC_MGT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8877dabd-c137-4073-97e3-779407a5d87a}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProtocolVersion(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordType(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordTypePid(self, dwRecordIndex: UInt32, ppidVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordVersionNumber(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IATSC_STT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6bf42423-217d-4d6f-81e1-3a7b360ec896}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProtocolVersion(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSystemTime(self, pmdtSystemTime: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGpsUtcOffset(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDaylightSavings(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IATSC_VCT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26879a18-32f9-46c6-91f0-fb6479270e8c}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransportStreamId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProtocolVersion(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordName(self, dwRecordIndex: UInt32, pwsName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordMajorChannelNumber(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordMinorChannelNumber(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordModulationMode(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCarrierFrequency(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordTransportStreamId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordProgramNumber(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordEtmLocation(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordIsAccessControlledBitSet(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordIsHiddenBitSet(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecordIsPathSelectBitSet(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetRecordIsOutOfBandBitSet(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetRecordIsHideGuideBitSet(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRecordServiceType(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetRecordSourceId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAnalogAudioComponentType(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IComponentType
    _iid_ = Guid('{2cfeb2a8-1787-4a24-a941-c6eaec39c842}')
    @commethod(24)
    def get_AnalogAudioMode(self, Mode: POINTER(Windows.Win32.Media.DirectShow.TVAudioMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_AnalogAudioMode(self, Mode: Windows.Win32.Media.DirectShow.TVAudioMode) -> Windows.Win32.Foundation.HRESULT: ...
class IAnalogLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ILocator
    _iid_ = Guid('{34d1f26b-e339-430d-abce-738cb48984dc}')
    @commethod(22)
    def get_VideoStandard(self, AVS: POINTER(Windows.Win32.Media.DirectShow.AnalogVideoStandard)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_VideoStandard(self, AVS: Windows.Win32.Media.DirectShow.AnalogVideoStandard) -> Windows.Win32.Foundation.HRESULT: ...
class IAnalogRadioTuningSpace(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuningSpace
    _iid_ = Guid('{2a6e293b-2595-11d3-b64c-00c04f79498e}')
    @commethod(26)
    def get_MinFrequency(self, MinFrequencyVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_MinFrequency(self, NewMinFrequencyVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_MaxFrequency(self, MaxFrequencyVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_MaxFrequency(self, NewMaxFrequencyVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Step(self, StepVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Step(self, NewStepVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IAnalogRadioTuningSpace2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IAnalogRadioTuningSpace
    _iid_ = Guid('{39dd45da-2da8-46ba-8a8a-87e2b73d983a}')
    @commethod(32)
    def get_CountryCode(self, CountryCodeVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_CountryCode(self, NewCountryCodeVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IAnalogTVTuningSpace(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuningSpace
    _iid_ = Guid('{2a6e293c-2595-11d3-b64c-00c04f79498e}')
    @commethod(26)
    def get_MinChannel(self, MinChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_MinChannel(self, NewMinChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_MaxChannel(self, MaxChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_MaxChannel(self, NewMaxChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_InputType(self, InputTypeVal: POINTER(Windows.Win32.Media.DirectShow.TunerInputType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_InputType(self, NewInputTypeVal: Windows.Win32.Media.DirectShow.TunerInputType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_CountryCode(self, CountryCodeVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_CountryCode(self, NewCountryCodeVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IAtscContentAdvisoryDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ff76e60c-0283-43ea-ba32-b422238547ee}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRatingRegionCount(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordRatingRegion(self, bIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordRatedDimensions(self, bIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordRatingDimension(self, bIndexOuter: Byte, bIndexInner: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordRatingValue(self, bIndexOuter: Byte, bIndexInner: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordRatingDescriptionText(self, bIndex: Byte, pbLength: POINTER(Byte), ppText: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IAtscPsipParser(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b2c98995-5eb2-4fb1-b406-f3e8e2026a9a}')
    @commethod(3)
    def Initialize(self, punkMpeg2Data: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPAT(self, ppPAT: POINTER(Windows.Win32.Media.DirectShow.Tv.IPAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCAT(self, dwTimeout: UInt32, ppCAT: POINTER(Windows.Win32.Media.DirectShow.Tv.ICAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPMT(self, pid: UInt16, pwProgramNumber: POINTER(UInt16), ppPMT: POINTER(Windows.Win32.Media.DirectShow.Tv.IPMT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTSDT(self, ppTSDT: POINTER(Windows.Win32.Media.DirectShow.Tv.ITSDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMGT(self, ppMGT: POINTER(Windows.Win32.Media.DirectShow.Tv.IATSC_MGT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetVCT(self, tableId: Byte, fGetNextTable: Windows.Win32.Foundation.BOOL, ppVCT: POINTER(Windows.Win32.Media.DirectShow.Tv.IATSC_VCT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEIT(self, pid: UInt16, pwSourceId: POINTER(UInt16), dwTimeout: UInt32, ppEIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IATSC_EIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetETT(self, pid: UInt16, wSourceId: POINTER(UInt16), pwEventId: POINTER(UInt16), ppETT: POINTER(Windows.Win32.Media.DirectShow.Tv.IATSC_ETT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSTT(self, ppSTT: POINTER(Windows.Win32.Media.DirectShow.Tv.IATSC_STT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEAS(self, pid: UInt16, ppEAS: POINTER(Windows.Win32.Media.DirectShow.Tv.ISCTE_EAS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAttributeGet(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52dbd1ec-e48f-4528-9232-f442a68f0ae1}')
    @commethod(3)
    def GetCount(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttribIndexed(self, lIndex: Int32, pguidAttribute: POINTER(Guid), pbAttribute: POINTER(Byte), pdwAttributeLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttrib(self, guidAttribute: Guid, pbAttribute: POINTER(Byte), pdwAttributeLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAttributeSet(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{583ec3cc-4960-4857-982b-41a33ea0a006}')
    @commethod(3)
    def SetAttrib(self, guidAttribute: Guid, pbAttribute: POINTER(Byte), dwAttributeLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IAuxInTuningSpace(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuningSpace
    _iid_ = Guid('{e48244b8-7e17-4f76-a763-5090ff1e2f30}')
class IAuxInTuningSpace2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IAuxInTuningSpace
    _iid_ = Guid('{b10931ed-8bfe-4ab0-9dce-e469c29a9729}')
    @commethod(26)
    def get_CountryCode(self, CountryCodeVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_CountryCode(self, NewCountryCodeVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IBDAComparable(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b34505e0-2f0e-497b-80bc-d43f3b24ed7f}')
    @commethod(3)
    def CompareExact(self, CompareTo: Windows.Win32.System.Com.IDispatch_head, Result: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CompareEquivalent(self, CompareTo: Windows.Win32.System.Com.IDispatch_head, dwFlags: UInt32, Result: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HashExact(self, Result: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HashExactIncremental(self, PartialResult: Int64, Result: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HashEquivalent(self, dwFlags: UInt32, Result: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def HashEquivalentIncremental(self, PartialResult: Int64, dwFlags: UInt32, Result: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IBDACreateTuneRequestEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0a4a1d4-2b3c-491a-ba22-499fbadd4d12}')
    @commethod(3)
    def CreateTuneRequestEx(self, TuneRequestIID: POINTER(Guid), TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBDA_TIF_REGISTRATION(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfef4a68-ee61-415f-9ccb-cd95f2f98a3a}')
    @commethod(3)
    def RegisterTIFEx(self, pTIFInputPin: Windows.Win32.Media.DirectShow.IPin_head, ppvRegistrationContext: POINTER(UInt32), ppMpeg2DataControl: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterTIF(self, pvRegistrationContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ICAT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c6995fb-2a31-4bd7-953e-b1ad7fb7d31c}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextTable(self, dwTimeout: UInt32, ppCAT: POINTER(Windows.Win32.Media.DirectShow.Tv.ICAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
class ICaptionServiceDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{40834007-6834-46f0-bd45-d5f6a6be258c}')
    @commethod(3)
    def GetNumberOfServices(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLanguageCode(self, bIndex: Byte, LangCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCaptionServiceNumber(self, bIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCCType(self, bIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEasyReader(self, bIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWideAspectRatio(self, bIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IChannelIDTuneRequest(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuneRequest
    _iid_ = Guid('{156eff60-86f4-4e28-89fc-109799fd57ee}')
    @commethod(12)
    def get_ChannelID(self, ChannelID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_ChannelID(self, ChannelID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IChannelTuneRequest(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuneRequest
    _iid_ = Guid('{0369b4e0-45b6-11d3-b650-00c04f79498e}')
    @commethod(12)
    def get_Channel(self, Channel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Channel(self, Channel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IComponent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1a5576fc-0e19-11d3-9d8e-00c04f72d980}')
    @commethod(7)
    def get_Type(self, CT: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponentType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Type(self, CT: Windows.Win32.Media.DirectShow.Tv.IComponentType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DescLangID(self, LangID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DescLangID(self, LangID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(self, Status: POINTER(Windows.Win32.Media.DirectShow.ComponentStatus)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Status(self, Status: Windows.Win32.Media.DirectShow.ComponentStatus) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Description(self, Description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Description(self, Description: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(self, NewComponent: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponent_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentType(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6a340dc0-0311-11d3-9d8e-00c04f72d980}')
    @commethod(7)
    def get_Category(self, Category: POINTER(Windows.Win32.Media.DirectShow.ComponentCategory)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Category(self, Category: Windows.Win32.Media.DirectShow.ComponentCategory) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MediaMajorType(self, MediaMajorType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_MediaMajorType(self, MediaMajorType: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get__MediaMajorType(self, MediaMajorTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put__MediaMajorType(self, MediaMajorTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MediaSubType(self, MediaSubType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_MediaSubType(self, MediaSubType: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get__MediaSubType(self, MediaSubTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put__MediaSubType(self, MediaSubTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MediaFormatType(self, MediaFormatType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_MediaFormatType(self, MediaFormatType: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get__MediaFormatType(self, MediaFormatTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put__MediaFormatType(self, MediaFormatTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_MediaType(self, MediaType: POINTER(Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_MediaType(self, MediaType: POINTER(Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(self, NewCT: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponentType_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentTypes(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0dc13d4a-0313-11d3-9d8e-00c04f72d980}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppNewEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumComponentTypes(self, ppNewEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumComponentTypes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Item(self, Index: Windows.Win32.System.Variant.VARIANT, ComponentType: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponentType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Item(self, Index: Windows.Win32.System.Variant.VARIANT, ComponentType: Windows.Win32.Media.DirectShow.Tv.IComponentType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Add(self, ComponentType: Windows.Win32.Media.DirectShow.Tv.IComponentType_head, NewIndex: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Remove(self, Index: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Clone(self, NewList: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponentTypes_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IComponents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{39a48091-fffe-4182-a161-3ff802640e26}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppNewEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumComponents(self, ppNewEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumComponents_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Item(self, Index: Windows.Win32.System.Variant.VARIANT, ppComponent: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, Component: Windows.Win32.Media.DirectShow.Tv.IComponent_head, NewIndex: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, Index: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(self, NewList: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponents_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Item(self, Index: Windows.Win32.System.Variant.VARIANT, ppComponent: Windows.Win32.Media.DirectShow.Tv.IComponent_head) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentsOld(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fcd01846-0e19-11d3-9d8e-00c04f72d980}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppNewEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumComponents(self, ppNewEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumComponents_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Item(self, Index: Windows.Win32.System.Variant.VARIANT, ppComponent: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, Component: Windows.Win32.Media.DirectShow.Tv.IComponent_head, NewIndex: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, Index: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(self, NewList: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponents_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICreatePropBagOnRegKey(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a674b48-1f63-11d3-b64c-00c04f79498e}')
    @commethod(3)
    def Create(self, hkey: Windows.Win32.System.Registry.HKEY, subkey: Windows.Win32.Foundation.PWSTR, ulOptions: UInt32, samDesired: UInt32, iid: POINTER(Guid), ppBag: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDTFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4c4c4b2-0049-4e2b-98fb-9537f6ce516d}')
    @commethod(3)
    def get_EvalRatObjOK(self, pHrCoCreateRetVal: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrRating(self, pEnSystem: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_System), pEnRating: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel), plbfEnAttr: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_BlockedRatingAttributes(self, enSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enLevel: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, plbfEnAttr: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_BlockedRatingAttributes(self, enSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enLevel: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, lbfAttrs: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_BlockUnRated(self, pfBlockUnRatedShows: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BlockUnRated(self, fBlockUnRatedShows: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BlockUnRatedDelay(self, pmsecsDelayBeforeBlock: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_BlockUnRatedDelay(self, msecsDelayBeforeBlock: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDTFilter2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDTFilter
    _iid_ = Guid('{c4c4c4b4-0049-4e2b-98fb-9537f6ce516d}')
    @commethod(11)
    def get_ChallengeUrl(self, pbstrChallengeUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCurrLicenseExpDate(self, protType: POINTER(Windows.Win32.Media.DirectShow.Tv.ProtType), lpDateTime: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetLastErrorCode(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDTFilter3(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDTFilter2
    _iid_ = Guid('{513998cc-e929-4cdf-9fbd-bad1e0314866}')
    @commethod(14)
    def GetProtectionType(self, pProtectionType: POINTER(Windows.Win32.Media.DirectShow.Tv.ProtType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LicenseHasExpirationDate(self, pfLicenseHasExpirationDate: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetRights(self, bstrRights: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IDTFilterConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4c4c4d2-0049-4e2b-98fb-9537f6ce516d}')
    @commethod(3)
    def GetSecureChannelObject(self, ppUnkDRMSecureChannel: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDTFilterEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c4c4c4c2-0049-4e2b-98fb-9537f6ce516d}')
class IDTFilterLicenseRenewal(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a78b317-e405-4a43-994a-620d8f5ce25e}')
    @commethod(3)
    def GetLicenseRenewalData(self, ppwszFileName: POINTER(Windows.Win32.Foundation.PWSTR), ppwszExpiredKid: POINTER(Windows.Win32.Foundation.PWSTR), ppwszTunerId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBCLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDigitalLocator
    _iid_ = Guid('{6e42f36e-1dd2-43c4-9f78-69d25ae39034}')
class IDVBSLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDigitalLocator
    _iid_ = Guid('{3d7c353c-0d04-45f1-a742-f97cc1188dc8}')
    @commethod(22)
    def get_SignalPolarisation(self, PolarisationVal: POINTER(Windows.Win32.Media.DirectShow.Polarisation)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_SignalPolarisation(self, PolarisationVal: Windows.Win32.Media.DirectShow.Polarisation) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_WestPosition(self, WestLongitude: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_WestPosition(self, WestLongitude: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_OrbitalPosition(self, longitude: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_OrbitalPosition(self, longitude: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Azimuth(self, Azimuth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Azimuth(self, Azimuth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Elevation(self, Elevation: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Elevation(self, Elevation: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBSLocator2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDVBSLocator
    _iid_ = Guid('{6044634a-1733-4f99-b982-5fb12afce4f0}')
    @commethod(32)
    def get_DiseqLNBSource(self, DiseqLNBSourceVal: POINTER(Windows.Win32.Media.DirectShow.LNB_Source)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_DiseqLNBSource(self, DiseqLNBSourceVal: Windows.Win32.Media.DirectShow.LNB_Source) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_LocalOscillatorOverrideLow(self, LocalOscillatorOverrideLowVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_LocalOscillatorOverrideLow(self, LocalOscillatorOverrideLowVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_LocalOscillatorOverrideHigh(self, LocalOscillatorOverrideHighVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_LocalOscillatorOverrideHigh(self, LocalOscillatorOverrideHighVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_LocalLNBSwitchOverride(self, LocalLNBSwitchOverrideVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_LocalLNBSwitchOverride(self, LocalLNBSwitchOverrideVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_LocalSpectralInversionOverride(self, LocalSpectralInversionOverrideVal: POINTER(Windows.Win32.Media.DirectShow.SpectralInversion)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_LocalSpectralInversionOverride(self, LocalSpectralInversionOverrideVal: Windows.Win32.Media.DirectShow.SpectralInversion) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_SignalRollOff(self, RollOffVal: POINTER(Windows.Win32.Media.DirectShow.RollOff)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_SignalRollOff(self, RollOffVal: Windows.Win32.Media.DirectShow.RollOff) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_SignalPilot(self, PilotVal: POINTER(Windows.Win32.Media.DirectShow.Pilot)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_SignalPilot(self, PilotVal: Windows.Win32.Media.DirectShow.Pilot) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBSTuningSpace(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDVBTuningSpace2
    _iid_ = Guid('{cdf7be60-d954-42fd-a972-78971958e470}')
    @commethod(30)
    def get_LowOscillator(self, LowOscillator: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_LowOscillator(self, LowOscillator: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_HighOscillator(self, HighOscillator: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_HighOscillator(self, HighOscillator: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_LNBSwitch(self, LNBSwitch: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_LNBSwitch(self, LNBSwitch: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_InputRange(self, InputRange: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_InputRange(self, InputRange: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_SpectralInversion(self, SpectralInversionVal: POINTER(Windows.Win32.Media.DirectShow.SpectralInversion)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_SpectralInversion(self, SpectralInversionVal: Windows.Win32.Media.DirectShow.SpectralInversion) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBTLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDigitalLocator
    _iid_ = Guid('{8664da16-dda2-42ac-926a-c18f9127c302}')
    @commethod(22)
    def get_Bandwidth(self, BandWidthVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Bandwidth(self, BandwidthVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_LPInnerFEC(self, FEC: POINTER(Windows.Win32.Media.DirectShow.FECMethod)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_LPInnerFEC(self, FEC: Windows.Win32.Media.DirectShow.FECMethod) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_LPInnerFECRate(self, FEC: POINTER(Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_LPInnerFECRate(self, FEC: Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_HAlpha(self, Alpha: POINTER(Windows.Win32.Media.DirectShow.HierarchyAlpha)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_HAlpha(self, Alpha: Windows.Win32.Media.DirectShow.HierarchyAlpha) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Guard(self, GI: POINTER(Windows.Win32.Media.DirectShow.GuardInterval)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Guard(self, GI: Windows.Win32.Media.DirectShow.GuardInterval) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_Mode(self, mode: POINTER(Windows.Win32.Media.DirectShow.TransmissionMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_Mode(self, mode: Windows.Win32.Media.DirectShow.TransmissionMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_OtherFrequencyInUse(self, OtherFrequencyInUseVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_OtherFrequencyInUse(self, OtherFrequencyInUseVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBTLocator2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDVBTLocator
    _iid_ = Guid('{448a2edf-ae95-4b43-a3cc-747843c453d4}')
    @commethod(36)
    def get_PhysicalLayerPipeId(self, PhysicalLayerPipeIdVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_PhysicalLayerPipeId(self, PhysicalLayerPipeIdVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBTuneRequest(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuneRequest
    _iid_ = Guid('{0d6f567e-a636-42bb-83ba-ce4c1704afa2}')
    @commethod(12)
    def get_ONID(self, ONID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_ONID(self, ONID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_TSID(self, TSID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_TSID(self, TSID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_SID(self, SID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_SID(self, SID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBTuningSpace(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuningSpace
    _iid_ = Guid('{ada0b268-3b19-4e5b-acc4-49f852be13ba}')
    @commethod(26)
    def get_SystemType(self, SysType: POINTER(Windows.Win32.Media.DirectShow.DVBSystemType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_SystemType(self, SysType: Windows.Win32.Media.DirectShow.DVBSystemType) -> Windows.Win32.Foundation.HRESULT: ...
class IDVBTuningSpace2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDVBTuningSpace
    _iid_ = Guid('{843188b4-ce62-43db-966b-8145a094e040}')
    @commethod(28)
    def get_NetworkID(self, NetworkID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_NetworkID(self, NetworkID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_BAT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ece9bb0c-43b6-4558-a0ec-1812c34cd6ca}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBouquetId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordTransportStreamId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordOriginalNetworkId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetNextTable(self, ppBAT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_BAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_DIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{91bffdf9-9432-410f-86ef-1c228ed0ad70}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransitionFlag(self, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_EIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{442db029-02cb-4495-8b92-1c13375bce99}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransportStreamId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSegmentLastSectionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastTableId(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordEventId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordStartTime(self, dwRecordIndex: UInt32, pmdtVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDuration(self, dwRecordIndex: UInt32, pmdVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordRunningStatus(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordFreeCAMode(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetNextTable(self, ppEIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_EIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_EIT2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDVB_EIT
    _iid_ = Guid('{61a389e0-9b9e-4ba0-aeea-5ddd159820ea}')
    @commethod(24)
    def GetSegmentInfo(self, pbTid: POINTER(Byte), pbSegment: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetRecordSection(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_NIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c64935f4-29e4-4e22-911a-63f7f55cb097}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordTransportStreamId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordOriginalNetworkId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetNextTable(self, ppNIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_NIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_RST(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f47dcd04-1e23-4fb7-9f96-b40eead10b2b}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecordTransportStreamId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordOriginalNetworkId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordServiceId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordEventId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordRunningStatus(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_SDT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02cad8d3-fe43-48e2-90bd-450ed9a8a5fd}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransportStreamId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOriginalNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordServiceId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordEITScheduleFlag(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordEITPresentFollowingFlag(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordRunningStatus(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordFreeCAMode(self, dwRecordIndex: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNextTable(self, ppSDT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_SDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_SIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68cdce53-8bea-45c2-9d9d-acf575a089b5}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordServiceId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordRunningStatus(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetNextTable(self, dwTimeout: UInt32, ppSIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_SIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_ST(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4d5b9f23-2a02-45de-bcda-5d5dbfbfbe62}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataLength(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetData(self, ppData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_TDT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0780dc7d-d55c-4aef-97e6-6b75906e2796}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUTCTime(self, pmdtVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDVB_TOT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83295d6a-faba-4ee1-9b15-8067696910ae}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUTCTime(self, pmdtVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDigitalCableLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IATSCLocator2
    _iid_ = Guid('{48f66a11-171a-419a-9525-beeecd51584c}')
class IDigitalCableTuneRequest(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IATSCChannelTuneRequest
    _iid_ = Guid('{bad7753b-6b37-4810-ae57-3ce0c4a9e6cb}')
    @commethod(16)
    def get_MajorChannel(self, pMajorChannel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_MajorChannel(self, MajorChannel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_SourceID(self, pSourceID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_SourceID(self, SourceID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDigitalCableTuningSpace(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IATSCTuningSpace
    _iid_ = Guid('{013f9f9c-b449-4ec7-a6d2-9d4f2fc70ae5}')
    @commethod(42)
    def get_MinMajorChannel(self, MinMajorChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_MinMajorChannel(self, NewMinMajorChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_MaxMajorChannel(self, MaxMajorChannelVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_MaxMajorChannel(self, NewMaxMajorChannelVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_MinSourceID(self, MinSourceIDVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_MinSourceID(self, NewMinSourceIDVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_MaxSourceID(self, MaxSourceIDVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_MaxSourceID(self, NewMaxSourceIDVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDigitalLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ILocator
    _iid_ = Guid('{19b595d8-839a-47f0-96df-4f194f3c768c}')
class IDvbCableDeliverySystemDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfb98e36-9e1a-4862-9946-993a4e59017b}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFrequency(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFECOuter(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetModulation(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSymbolRate(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFECInner(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbComponentDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{91e405cf-80e7-457f-9096-1b9d1ce32141}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamContent(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetComponentTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLanguageCode(self, pszCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTextW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbContentDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e883881-a467-412a-9d63-6f2b6da05bf0}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordContentNibbles(self, bRecordIndex: Byte, pbValLevel1: POINTER(Byte), pbValLevel2: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordUserNibbles(self, bRecordIndex: Byte, pbVal1: POINTER(Byte), pbVal2: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbContentIdentifierDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{05e0c1ea-f661-4053-9fbf-d93b28359838}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordCrid(self, bRecordIndex: Byte, pbType: POINTER(Byte), pbLocation: POINTER(Byte), pbLength: POINTER(Byte), ppbBytes: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbDataBroadcastDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d1ebc1d6-8b60-4c20-9caf-e59382e7c400}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataBroadcastID(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSelectorLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelectorBytes(self, pbLen: POINTER(Byte), pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLangID(self, pulVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetTextLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetText(self, pbLen: POINTER(Byte), pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbDataBroadcastIDDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5f26f518-65c8-4048-91f2-9290f59f7b90}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataBroadcastID(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIDSelectorBytes(self, pbLen: POINTER(Byte), pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbDefaultAuthorityDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{05ec24d1-3a31-44e7-b408-67c60a352276}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDefaultAuthority(self, pbLength: POINTER(Byte), ppbBytes: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbExtendedEventDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c9b22eca-85f4-499f-b1db-efa93a91ee57}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDescriptorNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastDescriptorNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLanguageCode(self, pszCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordItemW(self, bRecordIndex: Byte, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrDesc: POINTER(Windows.Win32.Foundation.BSTR), pbstrItem: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConcatenatedItemW(self, pFollowingDescriptor: Windows.Win32.Media.DirectShow.Tv.IDvbExtendedEventDescriptor_head, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrDesc: POINTER(Windows.Win32.Foundation.BSTR), pbstrItem: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTextW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetConcatenatedTextW(self, FollowingDescriptor: Windows.Win32.Media.DirectShow.Tv.IDvbExtendedEventDescriptor_head, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordItemRawBytes(self, bRecordIndex: Byte, ppbRawItem: POINTER(POINTER(Byte)), pbItemLength: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbFrequencyListDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cadb613-e1dd-4512-afa8-bb7a007ef8b1}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCodingType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordCentreFrequency(self, bRecordIndex: Byte, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbHDSimulcastLogicalChannelDescriptor(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDvbLogicalChannelDescriptor2
    _iid_ = Guid('{1ea8b738-a307-4680-9e26-d0a908c824f4}')
class IDvbLinkageDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cdf8b31-994a-46fc-acfd-6a6be8934dd5}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTSId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetONId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetServiceId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLinkageType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrivateDataLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPrivateData(self, pbLen: POINTER(Byte), pbData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbLogicalChannel2Descriptor(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDvbLogicalChannelDescriptor2
    _iid_ = Guid('{f69c3747-8a30-4980-998c-01fe7f0ba35a}')
    @commethod(9)
    def GetCountOfLists(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetListId(self, bListIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetListNameW(self, bListIndex: Byte, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetListCountryCode(self, bListIndex: Byte, pszCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetListCountOfRecords(self, bChannelListIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetListRecordServiceId(self, bListIndex: Byte, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetListRecordLogicalChannelNumber(self, bListIndex: Byte, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetListRecordLogicalChannelAndVisibility(self, bListIndex: Byte, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbLogicalChannelDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf1edaff-3ffd-4cf7-8201-35756acbf85f}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordServiceId(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordLogicalChannelNumber(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbLogicalChannelDescriptor2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDvbLogicalChannelDescriptor
    _iid_ = Guid('{43aca974-4be8-4b98-bc17-9eafd788b1d7}')
    @commethod(8)
    def GetRecordLogicalChannelAndVisibility(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbMultilingualServiceNameDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2d80433b-b32c-47ef-987f-e78ebb773e34}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordLangId(self, bRecordIndex: Byte, ulVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordServiceProviderNameW(self, bRecordIndex: Byte, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordServiceNameW(self, bRecordIndex: Byte, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbNetworkNameDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b2a80cf-35b9-446c-b3e4-048b761dbc51}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkName(self, pszName: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNetworkNameW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbParentalRatingDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3ad9dde1-fb1b-4186-937f-22e6b5a72a10}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordRating(self, bRecordIndex: Byte, pszCountryCode: POINTER(Byte), pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbPrivateDataSpecifierDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5660a019-e75a-4b82-9b4c-ed2256d165a2}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPrivateDataSpecifier(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbSatelliteDeliverySystemDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02f2225a-805b-4ec5-a9a6-f9b5913cd470}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFrequency(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOrbitalPosition(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetWestEastFlag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPolarization(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetModulation(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSymbolRate(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFECInner(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbServiceAttributeDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f37bd92-d6a1-4854-b950-3a969d27f30e}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordServiceId(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordNumericSelectionFlag(self, bRecordIndex: Byte, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordVisibleServiceFlag(self, bRecordIndex: Byte, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbServiceDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9c7fbcf-e2d6-464d-b32d-2ef526e49290}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceProviderName(self, pszName: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetServiceProviderNameW(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceName(self, pszName: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProcessedServiceName(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetServiceNameEmphasized(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbServiceDescriptor2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDvbServiceDescriptor
    _iid_ = Guid('{d6c76506-85ab-487c-9b2b-36416511e4a2}')
    @commethod(11)
    def GetServiceProviderNameW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetServiceNameW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbServiceListDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{05db0d8f-6008-491a-acd3-7090952707d0}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordServiceId(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordServiceType(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbShortEventDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b170be92-5b75-458e-9c6e-b0008231491a}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLanguageCode(self, pszCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEventNameW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTextW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbSiParser(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b758a7bd-14dc-449d-b828-35909acb3b1e}')
    @commethod(3)
    def Initialize(self, punkMpeg2Data: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPAT(self, ppPAT: POINTER(Windows.Win32.Media.DirectShow.Tv.IPAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCAT(self, dwTimeout: UInt32, ppCAT: POINTER(Windows.Win32.Media.DirectShow.Tv.ICAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPMT(self, pid: UInt16, pwProgramNumber: POINTER(UInt16), ppPMT: POINTER(Windows.Win32.Media.DirectShow.Tv.IPMT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTSDT(self, ppTSDT: POINTER(Windows.Win32.Media.DirectShow.Tv.ITSDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNIT(self, tableId: Byte, pwNetworkId: POINTER(UInt16), ppNIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_NIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSDT(self, tableId: Byte, pwTransportStreamId: POINTER(UInt16), ppSDT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_SDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEIT(self, tableId: Byte, pwServiceId: POINTER(UInt16), ppEIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_EIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBAT(self, pwBouquetId: POINTER(UInt16), ppBAT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_BAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRST(self, dwTimeout: UInt32, ppRST: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_RST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetST(self, pid: UInt16, dwTimeout: UInt32, ppST: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_ST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTDT(self, ppTDT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_TDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTOT(self, ppTOT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_TOT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDIT(self, dwTimeout: UInt32, ppDIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_DIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSIT(self, dwTimeout: UInt32, ppSIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_SIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbSiParser2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDvbSiParser
    _iid_ = Guid('{0ac5525f-f816-42f4-93ba-4c0f32f46e54}')
    @commethod(18)
    def GetEIT2(self, tableId: Byte, pwServiceId: POINTER(UInt16), pbSegment: POINTER(Byte), ppEIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IDVB_EIT2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbSubtitlingDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b25fe1d-fa23-4e50-9784-6df8b26f8a49}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordLangId(self, bRecordIndex: Byte, pulVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordSubtitlingType(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordCompositionPageID(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordAncillaryPageID(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbTeletextDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9cd29d47-69c6-4f92-98a9-210af1b7303a}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordLangId(self, bRecordIndex: Byte, pulVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordTeletextType(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordMagazineNumber(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordPageNumber(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbTerrestrial2DeliverySystemDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20ee9be9-cd57-49ab-8f6e-1d07aeb8e482}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTagExtension(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCentreFrequency(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPLPId(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetT2SystemId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMultipleInputMode(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBandwidth(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGuardInterval(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTransmissionMode(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCellId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetOtherFrequencyFlag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTFSFlag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IDvbTerrestrialDeliverySystemDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ed7e1b91-d12e-420c-b41d-a49d84fe1823}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCentreFrequency(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBandwidth(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConstellation(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetHierarchyInformation(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCodeRateHPStream(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCodeRateLPStream(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGuardInterval(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTransmissionMode(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetOtherFrequencyFlag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IESCloseMmiEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IESEvent
    _iid_ = Guid('{6b80e96f-55e2-45aa-b754-0c23c8e7d5c1}')
    @commethod(8)
    def GetDialogNumber(self, pDialogNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IESEventFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{506a09b8-7f86-4e04-ac05-3303bfe8fc49}')
    @commethod(3)
    def CreateESEvent(self, pServiceProvider: Windows.Win32.System.Com.IUnknown_head, dwEventId: UInt32, guidEventType: Guid, dwEventDataLength: UInt32, pEventData: POINTER(Byte), bstrBaseUrl: Windows.Win32.Foundation.BSTR, pInitContext: Windows.Win32.System.Com.IUnknown_head, ppESEvent: POINTER(Windows.Win32.Media.DirectShow.IESEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IESEventService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ed89a619-4c06-4b2f-99eb-c7669b13047c}')
    @commethod(3)
    def FireESEvent(self, pESEvent: Windows.Win32.Media.DirectShow.IESEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
class IESEventServiceConfiguration(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33b9daae-9309-491d-a051-bcad2a70cd66}')
    @commethod(3)
    def SetParent(self, pEventService: Windows.Win32.Media.DirectShow.Tv.IESEventService_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveParent(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOwner(self, pESEvents: Windows.Win32.Media.DirectShow.IESEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveOwner(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetGraph(self, pGraph: Windows.Win32.Media.DirectShow.IFilterGraph_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveGraph(self, pGraph: Windows.Win32.Media.DirectShow.IFilterGraph_head) -> Windows.Win32.Foundation.HRESULT: ...
class IESFileExpiryDateEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IESEvent
    _iid_ = Guid('{ba9edcb6-4d36-4cfe-8c56-87a6b0ca48e1}')
    @commethod(8)
    def GetTunerId(self, pguidTunerId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetExpiryDate(self, pqwExpiryDate: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFinalExpiryDate(self, pqwExpiryDate: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMaxRenewalCount(self, dwMaxRenewalCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsEntitlementTokenPresent(self, pfEntTokenPresent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DoesExpireAfterFirstUse(self, pfExpireAfterFirstUse: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IESIsdbCasResponseEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IESEvent
    _iid_ = Guid('{2017cb03-dc0f-4c24-83ca-36307b2cd19f}')
    @commethod(8)
    def GetRequestId(self, pRequestId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStatus(self, pStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDataLength(self, pRequestLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetResponseData(self, pbData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IESLicenseRenewalResultEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IESEvent
    _iid_ = Guid('{d5a48ef5-a81b-4df0-acaa-5e35e7ea45d4}')
    @commethod(8)
    def GetCallersId(self, pdwCallersId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFileName(self, pbstrFilename: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsRenewalSuccessful(self, pfRenewalSuccessful: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsCheckEntitlementCallRequired(self, pfCheckEntTokenCallNeeded: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDescrambledStatus(self, pDescrambledStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRenewalResultCode(self, pdwRenewalResultCode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCASFailureCode(self, pdwCASFailureCode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRenewalHResult(self, phr: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetEntitlementTokenLength(self, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetEntitlementToken(self, pbData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetExpiryDate(self, pqwExpiryDate: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IESOpenMmiEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IESEvent
    _iid_ = Guid('{ba4b6526-1a35-4635-8b56-3ec612746a8c}')
    @commethod(8)
    def GetDialogNumber(self, pDialogRequest: POINTER(UInt32), pDialogNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDialogType(self, guidDialogType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDialogData(self, pbData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDialogStringData(self, pbstrBaseUrl: POINTER(Windows.Win32.Foundation.BSTR), pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IESRequestTunerEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IESEvent
    _iid_ = Guid('{54c7a5e8-c3bb-4f51-af14-e0e2c0e34c6d}')
    @commethod(8)
    def GetPriority(self, pbyPriority: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetReason(self, pbyReason: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConsequences(self, pbyConsequences: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEstimatedTime(self, pdwEstimatedTime: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IESValueUpdatedEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IESEvent
    _iid_ = Guid('{8a24c46e-bb63-4664-8602-5d9c718c146d}')
    @commethod(8)
    def GetValueNames(self, pbstrNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IETFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4c4c4b1-0049-4e2b-98fb-9537f6ce516d}')
    @commethod(3)
    def get_EvalRatObjOK(self, pHrCoCreateRetVal: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrRating(self, pEnSystem: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_System), pEnRating: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel), plbfEnAttr: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrLicenseExpDate(self, protType: POINTER(Windows.Win32.Media.DirectShow.Tv.ProtType), lpDateTime: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastErrorCode(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRecordingOn(self, fRecState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IETFilterConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4c4c4d1-0049-4e2b-98fb-9537f6ce516d}')
    @commethod(3)
    def InitLicense(self, LicenseId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSecureChannelObject(self, ppUnkDRMSecureChannel: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IETFilterEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c4c4c4c1-0049-4e2b-98fb-9537f6ce516d}')
class IEnumComponentTypes(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a674b4a-1f63-11d3-b64c-00c04f79498e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponentType_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumComponentTypes_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumComponents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2a6e2939-2595-11d3-b64c-00c04f79498e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponent_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumComponents_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumGuideDataProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae44423b-4571-475c-ad2c-f40a771d80ef}')
    @commethod(3)
    def Next(self, celt: UInt32, ppprop: POINTER(Windows.Win32.Media.DirectShow.Tv.IGuideDataProperty_head), pcelt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumGuideDataProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumMSVidGraphSegment(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3dd2903e-e0aa-11d2-b63a-00c04f79498e}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumStreamBufferRecordingAttrib(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c18a9162-1e82-4142-8c73-5690fa62fe33}')
    @commethod(3)
    def Next(self, cRequest: UInt32, pStreamBufferAttribute: POINTER(Windows.Win32.Media.DirectShow.Tv.STREAMBUFFER_ATTRIBUTE_head), pcReceived: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cRecords: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppIEnumStreamBufferAttrib: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumStreamBufferRecordingAttrib_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumTuneRequests(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1993299c-ced6-4788-87a3-420067dce0c7}')
    @commethod(3)
    def Next(self, celt: UInt32, ppprop: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head), pcelt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumTuneRequests_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumTuningSpaces(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8b8eb248-fc2b-11d2-9d8c-00c04f72d980}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumTuningSpaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEvalRat(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c5c5c5b1-3abc-11d6-b25b-00c04fa0c026}')
    @commethod(7)
    def get_BlockedRatingAttributes(self, enSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enLevel: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, plbfAttrs: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BlockedRatingAttributes(self, enSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enLevel: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, lbfAttrs: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BlockUnRated(self, pfBlockUnRatedShows: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_BlockUnRated(self, fBlockUnRatedShows: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MostRestrictiveRating(self, enSystem1: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enEnLevel1: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, lbfEnAttr1: Int32, enSystem2: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enEnLevel2: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, lbfEnAttr2: Int32, penSystem: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_System), penEnLevel: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel), plbfEnAttr: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def TestRating(self, enShowSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enShowLevel: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, lbfEnShowAttributes: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IGenericDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a5918f8-a77a-4f61-aed0-5702bdcda3e6}')
    @commethod(3)
    def Initialize(self, pbDesc: POINTER(Byte), bCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBody(self, ppbVal: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IGenericDescriptor2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor
    _iid_ = Guid('{bf02fb7e-9792-4e10-a68d-033a2cc246a5}')
    @commethod(7)
    def Initialize(self, pbDesc: POINTER(Byte), wCount: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLength(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IGpnvsCommonBase(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{907e0b5c-e42d-4f04-91f0-26f401f36907}')
    @commethod(3)
    def GetValueUpdateName(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IGuideData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61571138-5b01-43cd-aeaf-60b784a0bf93}')
    @commethod(3)
    def GetServices(self, ppEnumTuneRequests: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumTuneRequests_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetServiceProperties(self, pTuneRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head, ppEnumProperties: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumGuideDataProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGuideProgramIDs(self, pEnumPrograms: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProgramProperties(self, varProgramDescriptionID: Windows.Win32.System.Variant.VARIANT, ppEnumProperties: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumGuideDataProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetScheduleEntryIDs(self, pEnumScheduleEntries: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetScheduleEntryProperties(self, varScheduleEntryDescriptionID: Windows.Win32.System.Variant.VARIANT, ppEnumProperties: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumGuideDataProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGuideDataEvent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{efda0c80-f395-42c3-9b3c-56b37dec7bb7}')
    @commethod(3)
    def GuideDataAcquired(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProgramChanged(self, varProgramDescriptionID: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ServiceChanged(self, varServiceDescriptionID: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ScheduleEntryChanged(self, varScheduleEntryDescriptionID: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProgramDeleted(self, varProgramDescriptionID: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ServiceDeleted(self, varServiceDescriptionID: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ScheduleDeleted(self, varScheduleEntryDescriptionID: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IGuideDataLoader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4764ff7c-fa95-4525-af4d-d32236db9e38}')
    @commethod(3)
    def Init(self, pGuideStore: Windows.Win32.Media.DirectShow.Tv.IGuideData_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate(self) -> Windows.Win32.Foundation.HRESULT: ...
class IGuideDataProperty(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{88ec5e58-bb73-41d6-99ce-66c524b8b591}')
    @commethod(3)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Language(self, idLang: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Value(self, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IISDBSLocator(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDVBSLocator
    _iid_ = Guid('{c9897087-e29c-473f-9e4b-7072123dea14}')
class IISDB_BIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{537cd71e-0e46-4173-9001-ba043f3e49e2}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOriginalNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBroadcastViewPropriety(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordBroadcasterId(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IISDB_CDT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{25fa92c2-8b80-4787-a841-3a0e8f17984b}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head, bSectionNumber: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDownloadDataId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSectionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDataType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSizeOfDataModule(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDataModule(self, pbData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IISDB_EMM(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0edb556d-43ad-4938-9668-321b2ffecfd3}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTableIdExtension(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDataBytes(self, pwBufferLength: POINTER(UInt16), pbBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSharedEmmMessage(self, pwLength: POINTER(UInt16), ppbMessage: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIndividualEmmMessage(self, pUnknown: Windows.Win32.System.Com.IUnknown_head, pwLength: POINTER(UInt16), ppbMessage: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IISDB_LDT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{141a546b-02ff-4fb9-a3a3-2f074b74a9a9}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOriginalServiceId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransportStreamId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordDescriptionId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IISDB_NBIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1b1863ef-08f1-40b7-a559-3b1eff8cafa6}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOriginalNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordInformationId(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordInformationType(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordDescriptionBodyLocation(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordMessageSectionNumber(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordUserDefined(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordNumberOfKeys(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordKeys(self, dwRecordIndex: UInt32, pbKeys: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IISDB_SDT(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDVB_SDT
    _iid_ = Guid('{3f3dc9a2-bb32-4fb9-ae9e-d856848927a3}')
    @commethod(21)
    def GetRecordEITUserDefinedFlags(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IISDB_SDTT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ee60ef2d-813a-4dc7-bf92-ea13dac85313}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTableIdExt(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransportStreamId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordGroup(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordTargetVersion(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordNewVersion(self, dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDownloadLevel(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordVersionIndicator(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordScheduleTimeShiftInformation(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordCountOfSchedules(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordStartTimeByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, pmdtVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecordDurationByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, pmdVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetVersionHash(self, pdwVersionHash: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbAudioComponentDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{679d2002-2425-4be4-a4c7-d6632a574f4d}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamContent(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetComponentTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSimulcastGroupTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetESMultiLingualFlag(self, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMainComponentFlag(self, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQualityIndicator(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSamplingRate(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetLanguageCode(self, pszCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetLanguageCode2(self, pszCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTextW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbCAContractInformationDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08e18b25-a28f-4e92-821e-4fced5cc2291}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCASystemId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCAUnitId(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordComponentTag(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetContractVerificationInfoLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetContractVerificationInfo(self, bBufLength: Byte, pbBuf: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFeeNameW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbCADescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0570aa47-52bc-42ae-8ca5-969f41e81aea}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCASystemId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReservedBits(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCAPID(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPrivateDataBytes(self, pbBufferLength: POINTER(Byte), pbBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbCAServiceDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{39cbeb97-ff0b-42a7-9ab9-7b9cfe70a77a}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCASystemId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCABroadcasterGroupId(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMessageControl(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceIds(self, pbNumServiceIds: POINTER(Byte), pwServiceIds: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbComponentGroupDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a494f17f-c592-47d8-8943-64c9a34be7b9}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetComponentGroupType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordGroupId(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordNumberOfCAUnit(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordCAUnitCAUnitId(self, bRecordIndex: Byte, bCAUnitIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCAUnitNumberOfComponents(self, bRecordIndex: Byte, bCAUnitIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordCAUnitComponentTag(self, bRecordIndex: Byte, bCAUnitIndex: Byte, bComponentIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordTotalBitRate(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordTextW(self, bRecordIndex: Byte, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbDataContentDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a428100a-e646-4bd6-aa14-6087bdc08cd5}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataComponentId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEntryComponent(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSelectorLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelectorBytes(self, bBufLength: Byte, pbBuf: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordComponentRef(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLanguageCode(self, pszCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTextW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbDigitalCopyControlDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a28417e-266a-4bb8-a4bd-d782bcfb8161}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCopyControl(self, pbDigitalRecordingControlData: POINTER(Byte), pbCopyControlType: POINTER(Byte), pbAPSControlData: POINTER(Byte), pbMaximumBitrate: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordCopyControl(self, bRecordIndex: Byte, pbComponentTag: POINTER(Byte), pbDigitalRecordingControlData: POINTER(Byte), pbCopyControlType: POINTER(Byte), pbAPSControlData: POINTER(Byte), pbMaximumBitrate: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbDownloadContentDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5298661e-cb88-4f5f-a1de-5f440c185b92}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(self, pfReboot: POINTER(Windows.Win32.Foundation.BOOL), pfAddOn: POINTER(Windows.Win32.Foundation.BOOL), pfCompatibility: POINTER(Windows.Win32.Foundation.BOOL), pfModuleInfo: POINTER(Windows.Win32.Foundation.BOOL), pfTextInfo: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentSize(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDownloadId(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTimeOutValueDII(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLeakRate(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetComponentTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCompatiblityDescriptorLength(self, pwLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCompatiblityDescriptor(self, ppbData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCountOfRecords(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordModuleId(self, wRecordIndex: UInt16, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordModuleSize(self, wRecordIndex: UInt16, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordModuleInfoLength(self, wRecordIndex: UInt16, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordModuleInfo(self, wRecordIndex: UInt16, ppbData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetTextLanguageCode(self, szCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetTextW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbEmergencyInformationDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba6fa681-b973-4da1-9207-ac3e7f0341eb}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceId(self, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStartEndFlag(self, bRecordIndex: Byte, pVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignalLevel(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAreaCode(self, bRecordIndex: Byte, ppwVal: POINTER(POINTER(UInt16)), pbNumAreaCodes: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbEventGroupDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{94b06780-2e2a-44dc-a966-cc56fdabc6c2}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGroupType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordEvent(self, bRecordIndex: Byte, pwServiceId: POINTER(UInt16), pwEventId: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRefRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRefRecordEvent(self, bRecordIndex: Byte, pwOriginalNetworkId: POINTER(UInt16), pwTransportStreamId: POINTER(UInt16), pwServiceId: POINTER(UInt16), pwEventId: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbHierarchicalTransmissionDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7b3ae90-ee0b-446d-8769-f7e2aa266aa6}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFutureUse1(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetQualityLevel(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFutureUse2(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetReferencePid(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbLogoTransmissionDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e0103f49-4ae1-4f07-9098-756db1fa88cd}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLogoTransmissionType(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLogoId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLogoVersion(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDownloadDataId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLogoCharW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrChar: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbSIParameterDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f837dc36-867c-426a-9111-f62093951a45}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParameterVersion(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUpdateTime(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordNumberOfTable(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableId(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptionLength(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetTableDescriptionBytes(self, bRecordIndex: Byte, pbBufferLength: POINTER(Byte), pbBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbSeriesDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{07ef6370-1660-4f26-87fc-614adab24b11}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSeriesId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRepeatLabel(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProgramPattern(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExpireDate(self, pfValid: POINTER(Windows.Win32.Foundation.BOOL), pmdtVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEpisodeNumber(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetLastEpisodeNumber(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSeriesNameW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbSiParser2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IDvbSiParser2
    _iid_ = Guid('{900e4bb7-18cd-453f-98be-3be6aa211772}')
    @commethod(19)
    def GetSDT(self, tableId: Byte, pwTransportStreamId: POINTER(UInt16), ppSDT: POINTER(Windows.Win32.Media.DirectShow.Tv.IISDB_SDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetBIT(self, tableId: Byte, pwOriginalNetworkId: POINTER(UInt16), ppBIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IISDB_BIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetNBIT(self, tableId: Byte, pwOriginalNetworkId: POINTER(UInt16), ppNBIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IISDB_NBIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetLDT(self, tableId: Byte, pwOriginalServiceId: POINTER(UInt16), ppLDT: POINTER(Windows.Win32.Media.DirectShow.Tv.IISDB_LDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetSDTT(self, tableId: Byte, pwTableIdExt: POINTER(UInt16), ppSDTT: POINTER(Windows.Win32.Media.DirectShow.Tv.IISDB_SDTT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetCDT(self, tableId: Byte, bSectionNumber: Byte, pwDownloadDataId: POINTER(UInt16), ppCDT: POINTER(Windows.Win32.Media.DirectShow.Tv.IISDB_CDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetEMM(self, pid: UInt16, wTableIdExt: UInt16, ppEMM: POINTER(Windows.Win32.Media.DirectShow.Tv.IISDB_EMM_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbTSInformationDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d7ad183e-38f5-4210-b55f-ec8d601bbd47}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRemoteControlKeyId(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTSNameW(self, convMode: Windows.Win32.Media.DirectShow.Tv.DVB_STRCONV_MODE, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordTransmissionTypeInfo(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordNumberOfServices(self, bRecordIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordServiceIdByIndex(self, bRecordIndex: Byte, bServiceIndex: Byte, pdwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IIsdbTerrestrialDeliverySystemDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{39fae0a6-d151-44dd-a28a-765de5991670}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAreaCode(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGuardInterval(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransmissionMode(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordFrequency(self, bRecordIndex: Byte, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ILanguageComponentType(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IComponentType
    _iid_ = Guid('{b874c8ba-0fa2-11d3-9d8e-00c04f72d980}')
    @commethod(24)
    def get_LangID(self, LangID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_LangID(self, LangID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ILocator(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{286d7f89-760c-4f89-80c4-66841d2507aa}')
    @commethod(7)
    def get_CarrierFrequency(self, Frequency: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_CarrierFrequency(self, Frequency: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InnerFEC(self, FEC: POINTER(Windows.Win32.Media.DirectShow.FECMethod)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_InnerFEC(self, FEC: Windows.Win32.Media.DirectShow.FECMethod) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InnerFECRate(self, FEC: POINTER(Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_InnerFECRate(self, FEC: Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OuterFEC(self, FEC: POINTER(Windows.Win32.Media.DirectShow.FECMethod)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_OuterFEC(self, FEC: Windows.Win32.Media.DirectShow.FECMethod) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_OuterFECRate(self, FEC: POINTER(Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_OuterFECRate(self, FEC: Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Modulation(self, Modulation: POINTER(Windows.Win32.Media.DirectShow.ModulationType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Modulation(self, Modulation: Windows.Win32.Media.DirectShow.ModulationType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SymbolRate(self, Rate: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SymbolRate(self, Rate: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Clone(self, NewLocator: POINTER(Windows.Win32.Media.DirectShow.Tv.ILocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMPEG2Component(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IComponent
    _iid_ = Guid('{1493e353-1eb6-473c-802d-8e6b8ec9d2a9}')
    @commethod(16)
    def get_PID(self, PID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_PID(self, PID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_PCRPID(self, PCRPID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_PCRPID(self, PCRPID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ProgramNumber(self, ProgramNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_ProgramNumber(self, ProgramNumber: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMPEG2ComponentType(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ILanguageComponentType
    _iid_ = Guid('{2c073d84-b51c-48c9-aa9f-68971e1f6e38}')
    @commethod(26)
    def get_StreamType(self, MP2StreamType: POINTER(Windows.Win32.Media.DirectShow.MPEG2StreamType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_StreamType(self, MP2StreamType: Windows.Win32.Media.DirectShow.MPEG2StreamType) -> Windows.Win32.Foundation.HRESULT: ...
class IMPEG2TuneRequest(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuneRequest
    _iid_ = Guid('{eb7d987f-8a01-42ad-b8ae-574deee44d1a}')
    @commethod(12)
    def get_TSID(self, TSID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_TSID(self, TSID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ProgNo(self, ProgNo: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_ProgNo(self, ProgNo: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMPEG2TuneRequestFactory(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{14e11abd-ee37-4893-9ea1-6964de933e39}')
    @commethod(7)
    def CreateTuneRequest(self, TuningSpace: Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head, TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.IMPEG2TuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMPEG2TuneRequestSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1b9d5fc3-5bbc-4b6c-bb18-b9d10e3eeebf}')
class IMPEG2_TIF_CONTROL(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9bac2f9-4149-4916-b2ef-faa202326862}')
    @commethod(3)
    def RegisterTIF(self, pUnkTIF: Windows.Win32.System.Com.IUnknown_head, ppvRegistrationContext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterTIF(self, pvRegistrationContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPIDs(self, ulcPIDs: UInt32, pulPIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeletePIDs(self, ulcPIDs: UInt32, pulPIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPIDCount(self, pulcPIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPIDs(self, pulcPIDs: POINTER(UInt32), pulPIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSEventBinder(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c3a9f406-2222-436d-86d5-ba3229279efb}')
    @commethod(7)
    def Bind(self, pEventObject: Windows.Win32.System.Com.IDispatch_head, EventName: Windows.Win32.Foundation.BSTR, EventHandler: Windows.Win32.Foundation.BSTR, CancelID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Unbind(self, CancelCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidAnalogTuner(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidTuner
    _iid_ = Guid('{1c15d47e-911d-11d2-b632-00c04f79498e}')
    @commethod(22)
    def get_Channel(self, Channel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Channel(self, Channel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_VideoFrequency(self, lcc: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AudioFrequency(self, lcc: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_CountryCode(self, lcc: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_CountryCode(self, lcc: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_SAP(self, pfSapOn: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_SAP(self, fSapOn: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def ChannelAvailable(self, nChannel: Int32, SignalStrength: POINTER(Int32), fSignalPresent: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidAnalogTuner2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidAnalogTuner
    _iid_ = Guid('{37647bf7-3dde-4cc8-a4dc-0d534d3d0037}')
    @commethod(31)
    def get_TVFormats(self, Formats: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_TunerModes(self, Modes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_NumAuxInputs(self, Inputs: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidAnalogTunerEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidTunerEvent
    _iid_ = Guid('{1c15d486-911d-11d2-b632-00c04f79498e}')
class IMSVidAudioRenderer(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevice
    _iid_ = Guid('{37b0353f-a4c8-11d2-b634-00c04f79498e}')
    @commethod(16)
    def put_Volume(self, lVol: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Volume(self, lVol: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Balance(self, lBal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Balance(self, lBal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidAudioRendererDevices(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c5702cd4-9b79-11d3-b654-00c04f79498e}')
    @commethod(7)
    def get_Count(self, lCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, pD: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, v: Windows.Win32.System.Variant.VARIANT, pDB: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidAudioRenderer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pDB: Windows.Win32.Media.DirectShow.Tv.IMSVidAudioRenderer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, v: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidAudioRendererEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDeviceEvent
    _iid_ = Guid('{37b03541-a4c8-11d2-b634-00c04f79498e}')
class IMSVidAudioRendererEvent2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidAudioRendererEvent
    _iid_ = Guid('{e3f55729-353b-4c43-a028-50f79aa9a907}')
    @commethod(8)
    def AVDecAudioDualMono(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AVAudioSampleRate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AVAudioChannelConfig(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AVAudioChannelCount(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AVDecCommonMeanBitRate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AVDDSurroundMode(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AVDecCommonInputFormat(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AVDecCommonOutputFormat(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidClosedCaptioning(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFeature
    _iid_ = Guid('{99652ea1-c1f7-414f-bb7b-1c967de75983}')
    @commethod(16)
    def get_Enable(self, On: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Enable(self, On: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidClosedCaptioning2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidClosedCaptioning
    _iid_ = Guid('{e00cb864-a029-4310-9987-a873f5887d97}')
    @commethod(18)
    def get_Service(self, On: POINTER(Windows.Win32.Media.DirectShow.Tv.MSVidCCService)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_Service(self, On: Windows.Win32.Media.DirectShow.Tv.MSVidCCService) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidClosedCaptioning3(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidClosedCaptioning2
    _iid_ = Guid('{c8638e8a-7625-4c51-9366-2f40a9831fc0}')
    @commethod(20)
    def get_TeleTextFilter(self, punkTTFilter: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidCompositionSegment(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment
    _iid_ = Guid('{1c15d483-911d-11d2-b632-00c04f79498e}')
    @commethod(19)
    def Compose(self, upstream: Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head, downstream: Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Up(self, upstream: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Down(self, downstream: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidCtl(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b0edf162-910a-11d2-b632-00c04f79498e}')
    @commethod(7)
    def get_AutoSize(self, pbool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AutoSize(self, vbool: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BackColor(self, backcolor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_BackColor(self, backcolor: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Enabled(self, pbool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Enabled(self, vbool: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TabStop(self, pbool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_TabStop(self, vbool: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Window(self, phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_DisplaySize(self, CurrentValue: POINTER(Windows.Win32.Media.DirectShow.Tv.DisplaySizeList)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_DisplaySize(self, NewValue: Windows.Win32.Media.DirectShow.Tv.DisplaySizeList) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_MaintainAspectRatio(self, CurrentValue: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_MaintainAspectRatio(self, NewValue: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ColorKey(self, CurrentValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_ColorKey(self, NewValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_InputsAvailable(self, CategoryGuid: Windows.Win32.Foundation.BSTR, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_OutputsAvailable(self, CategoryGuid: Windows.Win32.Foundation.BSTR, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get__InputsAvailable(self, CategoryGuid: POINTER(Guid), pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get__OutputsAvailable(self, CategoryGuid: POINTER(Guid), pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_VideoRenderersAvailable(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRendererDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_AudioRenderersAvailable(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidAudioRendererDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_FeaturesAvailable(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidFeatures_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_InputActive(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_InputActive(self, pVal: Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_OutputsActive(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_OutputsActive(self, pVal: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevices_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_VideoRendererActive(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRenderer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_VideoRendererActive(self, pVal: Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRenderer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_AudioRendererActive(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidAudioRenderer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_AudioRendererActive(self, pVal: Windows.Win32.Media.DirectShow.Tv.IMSVidAudioRenderer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_FeaturesActive(self, pVal: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidFeatures_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_FeaturesActive(self, pVal: Windows.Win32.Media.DirectShow.Tv.IMSVidFeatures_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_State(self, lState: POINTER(Windows.Win32.Media.DirectShow.Tv.MSVidCtlStateList)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def View(self, v: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Build(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def Run(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def Decompose(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def DisableVideo(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def DisableAudio(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def ViewNext(self, v: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidDataServices(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFeature
    _iid_ = Guid('{334125c1-77e5-11d3-b653-00c04f79498e}')
class IMSVidDataServicesEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidDeviceEvent
    _iid_ = Guid('{334125c2-77e5-11d3-b653-00c04f79498e}')
class IMSVidDevice(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1c15d47c-911d-11d2-b632-00c04f79498e}')
    @commethod(7)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Status(self, Status: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Power(self, Power: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Power(self, Power: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Category(self, Guid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ClassID(self, Clsid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get__Category(self, Guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get__ClassID(self, Clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsEqualDevice(self, Device: Windows.Win32.Media.DirectShow.Tv.IMSVidDevice_head, IsEqual: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidDevice2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87bd2783-ebc0-478c-b4a0-e8e7f43ab78e}')
    @commethod(3)
    def get_DevicePath(self, DevPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidDeviceEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1c15d480-911d-11d2-b632-00c04f79498e}')
    @commethod(7)
    def StateChange(self, lpd: Windows.Win32.Media.DirectShow.Tv.IMSVidDevice_head, oldState: Int32, newState: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidEVR(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRenderer
    _iid_ = Guid('{15e496ae-82a8-4cf9-a6b6-c561dc60398f}')
    @commethod(46)
    def get_Presenter(self, ppAllocPresent: POINTER(Windows.Win32.Media.MediaFoundation.IMFVideoPresenter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_Presenter(self, pAllocPresent: Windows.Win32.Media.MediaFoundation.IMFVideoPresenter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_SuppressEffects(self, bSuppress: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_SuppressEffects(self, bSuppress: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidEVREvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDeviceEvent
    _iid_ = Guid('{349abb10-883c-4f22-8714-cecaeee45d62}')
    @commethod(8)
    def OnUserEvent(self, lEventCode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidEncoder(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFeature
    _iid_ = Guid('{c0020fd4-bee7-43d9-a495-9f213117103d}')
    @commethod(16)
    def get_VideoEncoderInterface(self, ppEncInt: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AudioEncoderInterface(self, ppEncInt: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidFeature(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidDevice
    _iid_ = Guid('{37b03547-a4c8-11d2-b634-00c04f79498e}')
class IMSVidFeatureEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidDeviceEvent
    _iid_ = Guid('{3dd2903c-e0aa-11d2-b63a-00c04f79498e}')
class IMSVidFeatures(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c5702cd5-9b79-11d3-b654-00c04f79498e}')
    @commethod(7)
    def get_Count(self, lCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, pD: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, v: Windows.Win32.System.Variant.VARIANT, pDB: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidFeature_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pDB: Windows.Win32.Media.DirectShow.Tv.IMSVidFeature_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, v: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidFilePlayback(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidPlayback
    _iid_ = Guid('{37b03539-a4c8-11d2-b634-00c04f79498e}')
    @commethod(32)
    def get_FileName(self, FileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_FileName(self, FileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidFilePlayback2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFilePlayback
    _iid_ = Guid('{2f7e44af-6e52-4660-bc08-d8d542587d72}')
    @commethod(34)
    def put__SourceFilter(self, FileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put___SourceFilter(self, FileName: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidFilePlaybackEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidPlaybackEvent
    _iid_ = Guid('{37b0353a-a4c8-11d2-b634-00c04f79498e}')
class IMSVidGenericSink(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevice
    _iid_ = Guid('{6c29b41d-455b-4c33-963a-0d28e5e555ea}')
    @commethod(16)
    def SetSinkFilter(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SinkStreams(self, pStreams: POINTER(Windows.Win32.Media.DirectShow.Tv.MSVidSinkStreams)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SinkStreams(self, Streams: Windows.Win32.Media.DirectShow.Tv.MSVidSinkStreams) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidGenericSink2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidGenericSink
    _iid_ = Guid('{6b5a28f3-47f1-4092-b168-60cabec08f1c}')
    @commethod(19)
    def AddFilter(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ResetFilterList(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidGraphSegment(ComPtr):
    extends: Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{238dec54-adeb-4005-a349-f772b9afebc4}')
    @commethod(4)
    def get_Init(self, pInit: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_Init(self, pInit: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumFilters(self, pNewEnum: POINTER(Windows.Win32.Media.DirectShow.IEnumFilters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Container(self, ppCtl: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegmentContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Container(self, pCtl: Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegmentContainer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Type(self, pType: POINTER(Windows.Win32.Media.DirectShow.Tv.MSVidSegmentType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Category(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Build(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PostBuild(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PreRun(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PostRun(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def PreStop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def PostStop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnEventNotify(self, lEventCode: Int32, lEventParm1: IntPtr, lEventParm2: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Decompose(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidGraphSegmentContainer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3dd2903d-e0aa-11d2-b63a-00c04f79498e}')
    @commethod(3)
    def get_Graph(self, ppGraph: POINTER(Windows.Win32.Media.DirectShow.IGraphBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Input(self, ppInput: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Outputs(self, ppOutputs: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_VideoRenderer(self, ppVR: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AudioRenderer(self, ppAR: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Features(self, ppFeatures: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Composites(self, ppComposites: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumMSVidGraphSegment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ParentContainer(self, ppContainer: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Decompose(self, pSegment: Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsWindowless(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFocus(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidGraphSegmentUserInput(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{301c060e-20d9-4587-9b03-f82ed9a9943c}')
    @commethod(3)
    def Click(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DblClick(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def KeyDown(self, KeyCode: POINTER(Int16), ShiftState: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def KeyPress(self, KeyAscii: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def KeyUp(self, KeyCode: POINTER(Int16), ShiftState: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MouseDown(self, ButtonState: Int16, ShiftState: Int16, x: Int32, y: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MouseMove(self, ButtonState: Int16, ShiftState: Int16, x: Int32, y: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def MouseUp(self, ButtonState: Int16, ShiftState: Int16, x: Int32, y: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidInputDevice(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidDevice
    _iid_ = Guid('{37b0353d-a4c8-11d2-b634-00c04f79498e}')
    @commethod(16)
    def IsViewable(self, v: POINTER(Windows.Win32.System.Variant.VARIANT_head), pfViewable: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def View(self, v: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidInputDeviceEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{37b0353e-a4c8-11d2-b634-00c04f79498e}')
class IMSVidInputDevices(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c5702cd1-9b79-11d3-b654-00c04f79498e}')
    @commethod(7)
    def get_Count(self, lCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, pD: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, v: Windows.Win32.System.Variant.VARIANT, pDB: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pDB: Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, v: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidOutputDevice(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidDevice
    _iid_ = Guid('{37b03546-a4c8-11d2-b634-00c04f79498e}')
class IMSVidOutputDeviceEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidDeviceEvent
    _iid_ = Guid('{2e6a14e2-571c-11d3-b652-00c04f79498e}')
class IMSVidOutputDevices(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c5702cd2-9b79-11d3-b654-00c04f79498e}')
    @commethod(7)
    def get_Count(self, lCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, pD: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, v: Windows.Win32.System.Variant.VARIANT, pDB: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pDB: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, v: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidPlayback(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevice
    _iid_ = Guid('{37b03538-a4c8-11d2-b634-00c04f79498e}')
    @commethod(18)
    def get_EnableResetOnStop(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_EnableResetOnStop(self, newVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Run(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CanStep(self, fBackwards: Windows.Win32.Foundation.VARIANT_BOOL, pfCan: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Step(self, lStep: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Rate(self, plRate: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Rate(self, plRate: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_CurrentPosition(self, lPosition: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_CurrentPosition(self, lPosition: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_PositionMode(self, lPositionMode: Windows.Win32.Media.DirectShow.Tv.PositionModeList) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_PositionMode(self, lPositionMode: POINTER(Windows.Win32.Media.DirectShow.Tv.PositionModeList)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Length(self, lLength: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidPlaybackEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidInputDeviceEvent
    _iid_ = Guid('{37b0353b-a4c8-11d2-b634-00c04f79498e}')
    @commethod(7)
    def EndOfMedia(self, lpd: Windows.Win32.Media.DirectShow.Tv.IMSVidPlayback_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidRect(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7f5000a6-a440-47ca-8acc-c0e75531a2c2}')
    @commethod(7)
    def get_Top(self, TopVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Top(self, TopVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Left(self, LeftVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Left(self, LeftVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Width(self, WidthVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Width(self, WidthVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Height(self, HeightVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Height(self, HeightVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_HWnd(self, HWndVal: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_HWnd(self, HWndVal: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Rect(self, RectVal: Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferRecordingControl(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{160621aa-bbbc-4326-a824-c395aebc6e74}')
    @commethod(7)
    def get_StartTime(self, rtStart: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_StartTime(self, rtStart: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StopTime(self, rtStop: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_StopTime(self, rtStop: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RecordingStopped(self, phResult: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RecordingStarted(self, phResult: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_RecordingType(self, dwType: POINTER(Windows.Win32.Media.DirectShow.Tv.RecordingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_RecordingAttribute(self, pRecordingAttribute: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSink(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevice
    _iid_ = Guid('{159dbb45-cd1b-4dab-83ea-5cb1f4f21d07}')
    @commethod(16)
    def get_ContentRecorder(self, pszFilename: Windows.Win32.Foundation.BSTR, pRecordingIUnknown: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferRecordingControl_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ReferenceRecorder(self, pszFilename: Windows.Win32.Foundation.BSTR, pRecordingIUnknown: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferRecordingControl_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_SinkName(self, pName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_SinkName(self, Name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def NameSetLock(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_SBESink(self, sbeConfig: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSink2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSink
    _iid_ = Guid('{2ca9fc63-c131-4e5a-955a-544a47c67146}')
    @commethod(22)
    def UnlockProfile(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSink3(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSink2
    _iid_ = Guid('{4f8721d7-7d59-4d8b-99f5-a77775586bd5}')
    @commethod(23)
    def SetMinSeek(self, pdwMin: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_AudioCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_VideoCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_CCCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_WSTCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_AudioAnalysisFilter(self, szCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_AudioAnalysisFilter(self, pszCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put__AudioAnalysisFilter(self, guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get__AudioAnalysisFilter(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_VideoAnalysisFilter(self, szCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_VideoAnalysisFilter(self, pszCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put__VideoAnalysisFilter(self, guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get__VideoAnalysisFilter(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_DataAnalysisFilter(self, szCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_DataAnalysisFilter(self, pszCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put__DataAnalysisFilter(self, guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get__DataAnalysisFilter(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_LicenseErrorCode(self, hres: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDeviceEvent
    _iid_ = Guid('{f798a36b-b05b-4bbe-9703-eaea7d61cd51}')
    @commethod(8)
    def CertificateFailure(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CertificateSuccess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WriteFailure(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSinkEvent
    _iid_ = Guid('{3d7a5166-72d7-484b-a06f-286187b80ca1}')
    @commethod(11)
    def EncryptionOn(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EncryptionOff(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent3(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSinkEvent2
    _iid_ = Guid('{735ad8d5-c259-48e9-81e7-d27953665b23}')
    @commethod(13)
    def LicenseChange(self, dwProt: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent4(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSinkEvent3
    _iid_ = Guid('{1b01dcb0-daf0-412c-a5d1-590c7f62e2b8}')
    @commethod(14)
    def WriteFailureClear(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSource(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFilePlayback
    _iid_ = Guid('{eb0c8cf9-6950-4772-87b1-47d11cf3a02f}')
    @commethod(34)
    def get_Start(self, lStart: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_RecordingAttribute(self, pRecordingAttribute: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def CurrentRatings(self, pEnSystem: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_System), pEnRating: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel), pBfEnAttr: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def MaxRatingsLevel(self, enSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, enRating: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, lbfEnAttr: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_BlockUnrated(self, bBlock: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_UnratedDelay(self, dwDelay: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_SBESource(self, sbeFilter: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSource2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSource
    _iid_ = Guid('{e4ba9059-b1ce-40d8-b9a0-d4ea4a9989d3}')
    @commethod(41)
    def put_RateEx(self, dwRate: Double, dwFramesPerSecond: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_AudioCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_VideoCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_CCCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_WSTCounter(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSourceEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFilePlaybackEvent
    _iid_ = Guid('{50ce8a7d-9c28-4da8-9042-cdfa7116f979}')
    @commethod(8)
    def CertificateFailure(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CertificateSuccess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RatingsBlocked(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RatingsUnblocked(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RatingsChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def TimeHole(self, StreamOffsetMS: Int32, SizeMS: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def StaleDataRead(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ContentBecomingStale(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def StaleFileDeleted(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSourceEvent2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSourceEvent
    _iid_ = Guid('{7aef50ce-8e22-4ba8-bc06-a92a458b4ef2}')
    @commethod(17)
    def RateChange(self, qwNewRate: Double, qwOldRate: Double) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferSourceEvent3(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidStreamBufferSourceEvent2
    _iid_ = Guid('{ceabd6ab-9b90-4570-adf1-3ce76e00a763}')
    @commethod(18)
    def BroadcastEvent(self, Guid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def BroadcastEventEx(self, Guid: Windows.Win32.Foundation.BSTR, Param1: UInt32, Param2: UInt32, Param3: UInt32, Param4: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def COPPBlocked(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def COPPUnblocked(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ContentPrimarilyAudio(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidStreamBufferV2SourceEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFilePlaybackEvent
    _iid_ = Guid('{49c771f9-41b2-4cf7-9f9a-a313a8f6027e}')
    @commethod(8)
    def RatingsChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def TimeHole(self, StreamOffsetMS: Int32, SizeMS: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def StaleDataRead(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ContentBecomingStale(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StaleFileDeleted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RateChange(self, qwNewRate: Double, qwOldRate: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def BroadcastEvent(self, Guid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def BroadcastEventEx(self, Guid: Windows.Win32.Foundation.BSTR, Param1: UInt32, Param2: UInt32, Param3: UInt32, Param4: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ContentPrimarilyAudio(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidTuner(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidVideoInputDevice
    _iid_ = Guid('{1c15d47d-911d-11d2-b632-00c04f79498e}')
    @commethod(18)
    def get_Tune(self, ppTR: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_Tune(self, pTR: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TuningSpace(self, plTS: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_TuningSpace(self, plTS: Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidTunerEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidInputDeviceEvent
    _iid_ = Guid('{1c15d485-911d-11d2-b632-00c04f79498e}')
    @commethod(7)
    def TuneChanged(self, lpd: Windows.Win32.Media.DirectShow.Tv.IMSVidTuner_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidVMR9(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRenderer
    _iid_ = Guid('{d58b0015-ebef-44bb-bbdd-3f3699d76ea1}')
    @commethod(46)
    def get_Allocator_ID(self, ID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def SetAllocator(self, AllocPresent: Windows.Win32.System.Com.IUnknown_head, ID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_SuppressEffects(self, bSuppress: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_SuppressEffects(self, bSuppress: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_Allocator(self, AllocPresent: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidVRGraphSegment(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidGraphSegment
    _iid_ = Guid('{dd47de3f-9874-4f7b-8b22-7cb2688461e7}')
    @commethod(19)
    def put__VMRendererMode(self, dwMode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_Owner(self, Window: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Owner(self, Window: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_UseOverlay(self, UseOverlayVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_UseOverlay(self, UseOverlayVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Visible(self, Visible: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Visible(self, Visible: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ColorKey(self, ColorKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_ColorKey(self, ColorKey: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Source(self, r: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Source(self, r: Windows.Win32.Foundation.RECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Destination(self, r: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Destination(self, r: Windows.Win32.Foundation.RECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_NativeSize(self, sizeval: POINTER(Windows.Win32.Foundation.SIZE_head), aspectratio: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_BorderColor(self, color: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_BorderColor(self, color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_MaintainAspectRatio(self, fMaintain: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_MaintainAspectRatio(self, fMaintain: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def DisplayChange(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def RePaint(self, hdc: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidVideoInputDevice(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidInputDevice
    _iid_ = Guid('{1c15d47f-911d-11d2-b632-00c04f79498e}')
class IMSVidVideoRenderer(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDevice
    _iid_ = Guid('{37b03540-a4c8-11d2-b634-00c04f79498e}')
    @commethod(16)
    def get_CustomCompositorClass(self, CompositorCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_CustomCompositorClass(self, CompositorCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get__CustomCompositorClass(self, CompositorCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put__CustomCompositorClass(self, CompositorCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get__CustomCompositor(self, Compositor: POINTER(Windows.Win32.Media.DirectShow.IVMRImageCompositor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put__CustomCompositor(self, Compositor: Windows.Win32.Media.DirectShow.IVMRImageCompositor_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_MixerBitmap(self, MixerPictureDisp: POINTER(Windows.Win32.System.Ole.IPictureDisp_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get__MixerBitmap(self, MixerPicture: POINTER(Windows.Win32.Media.DirectShow.IVMRMixerBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MixerBitmap(self, MixerPictureDisp: Windows.Win32.System.Ole.IPictureDisp_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put__MixerBitmap(self, MixerPicture: POINTER(Windows.Win32.Media.DirectShow.VMRALPHABITMAP_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_MixerBitmapPositionRect(self, rDest: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_MixerBitmapPositionRect(self, rDest: Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_MixerBitmapOpacity(self, opacity: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_MixerBitmapOpacity(self, opacity: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetupMixerBitmap(self, MixerPictureDisp: Windows.Win32.System.Ole.IPictureDisp_head, Opacity: Int32, rDest: Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_SourceSize(self, CurrentSize: POINTER(Windows.Win32.Media.DirectShow.Tv.SourceSizeList)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_SourceSize(self, NewSize: Windows.Win32.Media.DirectShow.Tv.SourceSizeList) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_OverScan(self, plPercent: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_OverScan(self, lPercent: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_AvailableSourceRect(self, pRect: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_MaxVidRect(self, ppVidRect: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_MinVidRect(self, ppVidRect: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_ClippedSourceRect(self, pRect: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_ClippedSourceRect(self, pRect: Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_UsingOverlay(self, UseOverlayVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_UsingOverlay(self, UseOverlayVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Capture(self, currentImage: POINTER(Windows.Win32.System.Ole.IPictureDisp_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_FramesPerSecond(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_DecimateInput(self, pDeci: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_DecimateInput(self, pDeci: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidVideoRenderer2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRenderer
    _iid_ = Guid('{6bdd5c1e-2810-4159-94bc-05511ae8549b}')
    @commethod(46)
    def get_Allocator(self, AllocPresent: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get__Allocator(self, AllocPresent: POINTER(Windows.Win32.Media.DirectShow.IVMRSurfaceAllocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Allocator_ID(self, ID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetAllocator(self, AllocPresent: Windows.Win32.System.Com.IUnknown_head, ID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def _SetAllocator2(self, AllocPresent: Windows.Win32.Media.DirectShow.IVMRSurfaceAllocator_head, ID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_SuppressEffects(self, bSuppress: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_SuppressEffects(self, bSuppress: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidVideoRendererDevices(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c5702cd3-9b79-11d3-b654-00c04f79498e}')
    @commethod(7)
    def get_Count(self, lCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, pD: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, v: Windows.Win32.System.Variant.VARIANT, pDB: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRenderer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pDB: Windows.Win32.Media.DirectShow.Tv.IMSVidVideoRenderer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, v: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidVideoRendererEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDeviceEvent
    _iid_ = Guid('{37b03545-a4c8-11d2-b634-00c04f79498e}')
    @commethod(8)
    def OverlayUnavailable(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidVideoRendererEvent2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidOutputDeviceEvent
    _iid_ = Guid('{7145ed66-4730-4fdb-8a53-fde7508d3e5e}')
    @commethod(8)
    def OverlayUnavailable(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidWebDVD(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidPlayback
    _iid_ = Guid('{cf45f88b-ac56-4ee2-a73a-ed04e2885d3c}')
    @commethod(32)
    def OnDVDEvent(self, lEvent: Int32, lParam1: IntPtr, lParam2: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def PlayTitle(self, lTitle: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def PlayChapterInTitle(self, lTitle: Int32, lChapter: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def PlayChapter(self, lChapter: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def PlayChaptersAutoStop(self, lTitle: Int32, lstrChapter: Int32, lChapterCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def PlayAtTime(self, strTime: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def PlayAtTimeInTitle(self, lTitle: Int32, strTime: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def PlayPeriodInTitleAutoStop(self, lTitle: Int32, strStartTime: Windows.Win32.Foundation.BSTR, strEndTime: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def ReplayChapter(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def PlayPrevChapter(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def PlayNextChapter(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def StillOff(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_AudioLanguage(self, lStream: Int32, fFormat: Windows.Win32.Foundation.VARIANT_BOOL, strAudioLang: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def ShowMenu(self, MenuID: Windows.Win32.Media.DirectShow.Tv.DVDMenuIDConstants) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def ReturnFromSubmenu(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_ButtonsAvailable(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_CurrentButton(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def SelectAndActivateButton(self, lButton: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def ActivateButton(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SelectRightButton(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SelectLeftButton(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SelectLowerButton(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SelectUpperButton(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ActivateAtPosition(self, xPos: Int32, yPos: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SelectAtPosition(self, xPos: Int32, yPos: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def get_ButtonAtPosition(self, xPos: Int32, yPos: Int32, plButton: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_NumberOfChapters(self, lTitle: Int32, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_TotalTitleTime(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_TitlesAvailable(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_VolumesAvailable(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_CurrentVolume(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def get_CurrentDiscSide(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_CurrentDomain(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def get_CurrentChapter(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_CurrentTitle(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def get_CurrentTime(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def DVDTimeCode2bstr(self, timeCode: Int32, pTimeStr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def get_DVDDirectory(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def put_DVDDirectory(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def IsSubpictureStreamEnabled(self, lstream: Int32, fEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def IsAudioStreamEnabled(self, lstream: Int32, fEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_CurrentSubpictureStream(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def put_CurrentSubpictureStream(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_SubpictureLanguage(self, lStream: Int32, strLanguage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def get_CurrentAudioStream(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def put_CurrentAudioStream(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def get_AudioStreamsAvailable(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_AnglesAvailable(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def get_CurrentAngle(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def put_CurrentAngle(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def get_SubpictureStreamsAvailable(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def get_SubpictureOn(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def put_SubpictureOn(self, newVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_DVDUniqueID(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def AcceptParentalLevelChange(self, fAccept: Windows.Win32.Foundation.VARIANT_BOOL, strUserName: Windows.Win32.Foundation.BSTR, strPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def NotifyParentalLevelChange(self, newVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def SelectParentalCountry(self, lCountry: Int32, strUserName: Windows.Win32.Foundation.BSTR, strPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def SelectParentalLevel(self, lParentalLevel: Int32, strUserName: Windows.Win32.Foundation.BSTR, strPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def get_TitleParentalLevels(self, lTitle: Int32, plParentalLevels: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def get_PlayerParentalCountry(self, plCountryCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def get_PlayerParentalLevel(self, plParentalLevel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def Eject(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def UOPValid(self, lUOP: Int32, pfValid: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def get_SPRM(self, lIndex: Int32, psSPRM: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def get_GPRM(self, lIndex: Int32, psSPRM: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def put_GPRM(self, lIndex: Int32, sValue: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def get_DVDTextStringType(self, lLangIndex: Int32, lStringIndex: Int32, pType: POINTER(Windows.Win32.Media.DirectShow.Tv.DVDTextStringType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def get_DVDTextString(self, lLangIndex: Int32, lStringIndex: Int32, pstrText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def get_DVDTextNumberOfStrings(self, lLangIndex: Int32, plNumOfStrings: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def get_DVDTextNumberOfLanguages(self, plNumOfLangs: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def get_DVDTextLanguageLCID(self, lLangIndex: Int32, lcid: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(104)
    def RegionChange(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(105)
    def get_DVDAdm(self, pVal: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(106)
    def DeleteBookmark(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(107)
    def RestoreBookmark(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(108)
    def SaveBookmark(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(109)
    def SelectDefaultAudioLanguage(self, lang: Int32, ext: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(110)
    def SelectDefaultSubpictureLanguage(self, lang: Int32, ext: Windows.Win32.Media.DirectShow.Tv.DVDSPExt) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(111)
    def get_PreferredSubpictureStream(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(112)
    def get_DefaultMenuLanguage(self, lang: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(113)
    def put_DefaultMenuLanguage(self, lang: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(114)
    def get_DefaultSubpictureLanguage(self, lang: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(115)
    def get_DefaultAudioLanguage(self, lang: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(116)
    def get_DefaultSubpictureLanguageExt(self, ext: POINTER(Windows.Win32.Media.DirectShow.Tv.DVDSPExt)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(117)
    def get_DefaultAudioLanguageExt(self, ext: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(118)
    def get_LanguageFromLCID(self, lcid: Int32, lang: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(119)
    def get_KaraokeAudioPresentationMode(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(120)
    def put_KaraokeAudioPresentationMode(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(121)
    def get_KaraokeChannelContent(self, lStream: Int32, lChan: Int32, lContent: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(122)
    def get_KaraokeChannelAssignment(self, lStream: Int32, lChannelAssignment: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(123)
    def RestorePreferredSettings(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(124)
    def get_ButtonRect(self, lButton: Int32, pRect: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(125)
    def get_DVDScreenInMouseCoordinates(self, ppRect: POINTER(Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(126)
    def put_DVDScreenInMouseCoordinates(self, pRect: Windows.Win32.Media.DirectShow.Tv.IMSVidRect_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidWebDVD2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidWebDVD
    _iid_ = Guid('{7027212f-ee9a-4a7c-8b67-f023714cdaff}')
    @commethod(127)
    def get_Bookmark(self, ppData: POINTER(POINTER(Byte)), pDataLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(128)
    def put_Bookmark(self, pData: POINTER(Byte), dwDataLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidWebDVDAdm(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b8be681a-eb2c-47f0-b415-94d5452f0e05}')
    @commethod(7)
    def ChangePassword(self, strUserName: Windows.Win32.Foundation.BSTR, strOld: Windows.Win32.Foundation.BSTR, strNew: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SaveParentalLevel(self, level: Int32, strUserName: Windows.Win32.Foundation.BSTR, strPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SaveParentalCountry(self, country: Int32, strUserName: Windows.Win32.Foundation.BSTR, strPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ConfirmPassword(self, strUserName: Windows.Win32.Foundation.BSTR, strPassword: Windows.Win32.Foundation.BSTR, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetParentalLevel(self, lLevel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetParentalCountry(self, lCountry: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DefaultAudioLCID(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_DefaultAudioLCID(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_DefaultSubpictureLCID(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_DefaultSubpictureLCID(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_DefaultMenuLCID(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_DefaultMenuLCID(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_BookmarkOnStop(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_BookmarkOnStop(self, newVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidWebDVDEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidPlaybackEvent
    _iid_ = Guid('{b4f7a674-9b83-49cb-a357-c63b871be958}')
    @commethod(8)
    def DVDNotify(self, lEventCode: Int32, lParam1: Windows.Win32.System.Variant.VARIANT, lParam2: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PlayForwards(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PlayBackwards(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ShowMenu(self, MenuID: Windows.Win32.Media.DirectShow.Tv.DVDMenuIDConstants, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Resume(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SelectOrActivateButton(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def StillOff(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def PauseOn(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ChangeCurrentAudioStream(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ChangeCurrentSubpictureStream(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ChangeCurrentAngle(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def PlayAtTimeInTitle(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def PlayAtTime(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def PlayChapterInTitle(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def PlayChapter(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ReplayChapter(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def PlayNextChapter(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Stop(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ReturnFromSubmenu(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def PlayTitle(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def PlayPrevChapter(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ChangeKaraokePresMode(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def ChangeVideoPresMode(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidXDS(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFeature
    _iid_ = Guid('{11ebc158-e712-4d1f-8bb3-01ed5274c4ce}')
    @commethod(16)
    def get_ChannelChangeInterface(self, punkCC: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMSVidXDSEvent(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IMSVidFeatureEvent
    _iid_ = Guid('{6db2317d-3b23-41ec-ba4b-701f407eaf3a}')
    @commethod(8)
    def RatingChange(self, PrevRatingSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, PrevLevel: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, PrevAttributes: Windows.Win32.Media.DirectShow.Tv.BfEnTvRat_GenericAttributes, NewRatingSystem: Windows.Win32.Media.DirectShow.Tv.EnTvRat_System, NewLevel: Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel, NewAttributes: Windows.Win32.Media.DirectShow.Tv.BfEnTvRat_GenericAttributes) -> Windows.Win32.Foundation.HRESULT: ...
class IMceBurnerControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5a86b91a-e71e-46c1-88a9-9bb338710552}')
    @commethod(3)
    def GetBurnerNoDecryption(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMpeg2Data(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b396d40-f380-4e3c-a514-1a82bf6ebfe6}')
    @commethod(3)
    def GetSection(self, pid: UInt16, tid: Byte, pFilter: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG2_FILTER_head), dwTimeout: UInt32, ppSectionList: POINTER(Windows.Win32.Media.DirectShow.Tv.ISectionList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTable(self, pid: UInt16, tid: Byte, pFilter: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG2_FILTER_head), dwTimeout: UInt32, ppSectionList: POINTER(Windows.Win32.Media.DirectShow.Tv.ISectionList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamOfSections(self, pid: UInt16, tid: Byte, pFilter: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG2_FILTER_head), hDataReadyEvent: Windows.Win32.Foundation.HANDLE, ppMpegStream: POINTER(Windows.Win32.Media.DirectShow.Tv.IMpeg2Stream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMpeg2Stream(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{400cc286-32a0-4ce4-9041-39571125a635}')
    @commethod(3)
    def Initialize(self, requestType: Windows.Win32.Media.DirectShow.Tv.MPEG_REQUEST_TYPE, pMpeg2Data: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head, pContext: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_CONTEXT_head), pid: UInt16, tid: Byte, pFilter: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG2_FILTER_head), hDataReadyEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SupplyDataBuffer(self, pStreamBuffer: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_STREAM_BUFFER_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMpeg2TableFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bdcdd913-9ecd-4fb2-81ae-adf747ea75a5}')
    @commethod(3)
    def AddPID(self, p: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddTable(self, p: UInt16, t: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddExtension(self, p: UInt16, t: Byte, e: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemovePID(self, p: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveTable(self, p: UInt16, t: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveExtension(self, p: UInt16, t: Byte, e: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IPAT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6623b511-4b5f-43c3-9a01-e8ff84188060}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransportStreamId(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordProgramNumber(self, dwIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordProgramMapPid(self, dwIndex: UInt32, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def FindRecordProgramMapPid(self, wProgramNumber: UInt16, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetNextTable(self, ppPAT: POINTER(Windows.Win32.Media.DirectShow.Tv.IPAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPBDAAttributesDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{313b3620-3263-45a6-9533-968befbeac03}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributePayload(self, ppbAttributeBuffer: POINTER(POINTER(Byte)), pdwAttributeLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPBDAEntitlementDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22632497-0de3-4587-aadc-d8d99017e760}')
    @commethod(3)
    def GetTag(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetToken(self, ppbTokenBuffer: POINTER(POINTER(Byte)), pdwTokenLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPBDASiParser(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9de49a74-aba2-4a18-93e1-21f17f95c3c3}')
    @commethod(3)
    def Initialize(self, punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEIT(self, dwSize: UInt32, pBuffer: POINTER(Byte), ppEIT: POINTER(Windows.Win32.Media.DirectShow.Tv.IPBDA_EIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetServices(self, dwSize: UInt32, pBuffer: POINTER(Byte), ppServices: POINTER(Windows.Win32.Media.DirectShow.Tv.IPBDA_Services_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPBDA_EIT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a35f2dea-098f-4ebd-984c-2bd4c3c8ce0a}')
    @commethod(3)
    def Initialize(self, size: UInt32, pBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTableId(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersionNumber(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceIdx(self, plwVal: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordEventId(self, dwRecordIndex: UInt32, plwVal: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordStartTime(self, dwRecordIndex: UInt32, pmdtVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_DATE_AND_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordDuration(self, dwRecordIndex: UInt32, pmdVal: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPBDA_Services(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{944eab37-eed4-4850-afd2-77e7efeb4427}')
    @commethod(3)
    def Initialize(self, size: UInt32, pBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCountOfRecords(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecordByIndex(self, dwRecordIndex: UInt32, pul64ServiceIdx: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IPMT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{01f3b398-9527-4736-94db-5195878e97a8}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgramNumber(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPcrPid(self, pPidVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCountOfRecords(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordStreamType(self, dwRecordIndex: UInt32, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordElementaryPid(self, dwRecordIndex: UInt32, pPidVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordCountOfDescriptors(self, dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByIndex(self, dwRecordIndex: UInt32, dwDescIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByTag(self, dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def QueryServiceGatewayInfo(self, ppDSMCCList: POINTER(POINTER(Windows.Win32.Media.DirectShow.Tv.DSMCC_ELEMENT_head)), puiCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def QueryMPEInfo(self, ppMPEList: POINTER(POINTER(Windows.Win32.Media.DirectShow.Tv.MPE_ELEMENT_head)), puiCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetNextTable(self, ppPMT: POINTER(Windows.Win32.Media.DirectShow.Tv.IPMT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPSITables(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{919f24c5-7b14-42ac-a4b0-2ae08daf00ac}')
    @commethod(3)
    def GetTable(self, dwTSID: UInt32, dwTID_PID: UInt32, dwHashedVer: UInt32, dwPara4: UInt32, ppIUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPTFilterLicenseRenewal(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26d836a5-0c15-44c7-ac59-b0da8728f240}')
    @commethod(3)
    def RenewLicenses(self, wszFileName: Windows.Win32.Foundation.PWSTR, wszExpiredKid: Windows.Win32.Foundation.PWSTR, dwCallersId: UInt32, bHighPriority: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseRenewal(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistTuneXml(ComPtr):
    extends: Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{0754cd31-8d15-47a9-8215-d20064157244}')
    @commethod(4)
    def InitNew(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, varValue: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pvarFragment: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistTuneXmlUtility(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{990237ae-ac11-4614-be8f-dd217a4cb4cb}')
    @commethod(3)
    def Deserialize(self, varValue: Windows.Win32.System.Variant.VARIANT, ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistTuneXmlUtility2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IPersistTuneXmlUtility
    _iid_ = Guid('{992e165f-ea24-4b2f-9a1d-009d92120451}')
    @commethod(4)
    def Serialize(self, piTuneRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head, pString: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRegisterTuner(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{359b3901-572c-4854-bb49-cdef66606a25}')
    @commethod(3)
    def Register(self, pTuner: Windows.Win32.Media.DirectShow.Tv.ITuner_head, pGraph: Windows.Win32.Media.DirectShow.IGraphBuilder_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2Crossbar(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{547b6d26-3226-487e-8253-8aa168749434}')
    @commethod(3)
    def EnableDefaultMode(self, DefaultFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInitialProfile(self, ppProfile: POINTER(Windows.Win32.Media.DirectShow.Tv.ISBE2MediaTypeProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputProfile(self, pProfile: Windows.Win32.Media.DirectShow.Tv.ISBE2MediaTypeProfile_head, pcOutputPins: POINTER(UInt32), ppOutputPins: POINTER(Windows.Win32.Media.DirectShow.IPin_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumStreams(self, ppStreams: POINTER(Windows.Win32.Media.DirectShow.Tv.ISBE2EnumStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2EnumStream(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7611092-9fbc-46ec-a7c7-548ea78b71a4}')
    @commethod(3)
    def Next(self, cRequest: UInt32, pStreamDesc: POINTER(Windows.Win32.Media.DirectShow.Tv.SBE2_STREAM_DESC_head), pcReceived: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cRecords: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppIEnumStream: POINTER(Windows.Win32.Media.DirectShow.Tv.ISBE2EnumStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2FileScan(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3e2bf5a5-4f96-4899-a1a3-75e8be9a5ac0}')
    @commethod(3)
    def RepairFile(self, filename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2GlobalEvent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{caede759-b6b1-11db-a578-0018f3fa24c6}')
    @commethod(3)
    def GetEvent(self, idEvt: POINTER(Guid), param1: UInt32, param2: UInt32, param3: UInt32, param4: UInt32, pSpanning: POINTER(Windows.Win32.Foundation.BOOL), pcb: POINTER(UInt32), pb: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2GlobalEvent2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ISBE2GlobalEvent
    _iid_ = Guid('{6d8309bf-00fe-4506-8b03-f8c65b5c9b39}')
    @commethod(4)
    def GetEventEx(self, idEvt: POINTER(Guid), param1: UInt32, param2: UInt32, param3: UInt32, param4: UInt32, pSpanning: POINTER(Windows.Win32.Foundation.BOOL), pcb: POINTER(UInt32), pb: POINTER(Byte), pStreamTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2MediaTypeProfile(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f238267d-4671-40d7-997e-25dc32cfed2a}')
    @commethod(3)
    def GetStreamCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStream(self, Index: UInt32, ppMediaType: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddStream(self, pMediaType: POINTER(Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteStream(self, Index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2SpanningEvent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{caede760-b6b1-11db-a578-0018f3fa24c6}')
    @commethod(3)
    def GetEvent(self, idEvt: POINTER(Guid), streamId: UInt32, pcb: POINTER(UInt32), pb: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class ISBE2StreamMap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{667c7745-85b1-4c55-ae55-4e25056159fc}')
    @commethod(3)
    def MapStream(self, Stream: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnmapStream(self, Stream: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumMappedStreams(self, ppStreams: POINTER(Windows.Win32.Media.DirectShow.Tv.ISBE2EnumStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISCTE_EAS(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1ff544d6-161d-4fae-9faa-4f9f492ae999}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSequencyNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProtocolVersion(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEASEventID(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOriginatorCode(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEASEventCodeLen(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEASEventCode(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRawNatureOfActivationTextLen(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRawNatureOfActivationText(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNatureOfActivationText(self, bstrIS0639code: Windows.Win32.Foundation.BSTR, pbstrString: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimeRemaining(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStartTime(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDuration(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetAlertPriority(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetDetailsOOBSourceID(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDetailsMajor(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDetailsMinor(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetDetailsAudioOOBSourceID(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetAlertText(self, bstrIS0639code: Windows.Win32.Foundation.BSTR, pbstrString: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRawAlertTextLen(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetRawAlertText(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetLocationCount(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetLocationCodes(self, bIndex: Byte, pbState: POINTER(Byte), pbCountySubdivision: POINTER(Byte), pwCounty: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetExceptionCount(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetExceptionService(self, bIndex: Byte, pbIBRef: POINTER(Byte), pwFirst: POINTER(UInt16), pwSecond: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
ISDBSLocator = Guid('{6504afed-a629-455c-a7f1-04964dea5cc4}')
ISDB_CABLE_TV_NETWORK_TYPE = Guid('{c974ddb5-41fe-4b25-9741-92f049f1d5d1}')
ISDB_SATELLITE_TV_NETWORK_TYPE = Guid('{b0a4e6a0-6a1a-4b83-bb5b-903e1d90e6b6}')
ISDB_S_NETWORK_TYPE = Guid('{a1e78202-1459-41b1-9ca9-2a92587a42cc}')
ISDB_TERRESTRIAL_TV_NETWORK_TYPE = Guid('{95037f6f-3ac7-4452-b6c4-45a9ce9292a2}')
ISDB_T_NETWORK_TYPE = Guid('{fc3855a6-c901-4f2e-aba8-90815afc6c83}')
class ISIInbandEPG(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f90ad9d0-b854-4b68-9cc1-b2cc96119d85}')
    @commethod(3)
    def StartSIEPGScan(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopSIEPGScan(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsSIEPGScanRunning(self, bRunning: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISIInbandEPGEvent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7e47913a-5a89-423d-9a2b-e15168858934}')
    @commethod(3)
    def SIObjectEvent(self, pIDVB_EIT: Windows.Win32.Media.DirectShow.Tv.IDVB_EIT2_head, dwTable_ID: UInt32, dwService_ID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IScanningTuner(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuner
    _iid_ = Guid('{1dfd0a5c-0284-11d3-9d8e-00c04f72d980}')
    @commethod(13)
    def SeekUp(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SeekDown(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ScanUp(self, MillisecondsPause: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ScanDown(self, MillisecondsPause: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AutoProgram(self) -> Windows.Win32.Foundation.HRESULT: ...
class IScanningTunerEx(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IScanningTuner
    _iid_ = Guid('{04bbd195-0e2d-4593-9bd5-4f908bc33cf5}')
    @commethod(18)
    def GetCurrentLocator(self, pILocator: POINTER(Windows.Win32.Media.DirectShow.Tv.ILocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def PerformExhaustiveScan(self, dwLowerFreq: Int32, dwHigherFreq: Int32, bFineTune: Windows.Win32.Foundation.VARIANT_BOOL, hEvent: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def TerminateCurrentScan(self, pcurrentFreq: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ResumeCurrentScan(self, hEvent: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetTunerScanningCapability(self, HardwareAssistedScanning: POINTER(Int32), NumStandardsSupported: POINTER(Int32), BroadcastStandards: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetTunerStatus(self, SecondsLeft: POINTER(Int32), CurrentLockType: POINTER(Int32), AutoDetect: POINTER(Int32), CurrentFreq: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetCurrentTunerStandardCapability(self, CurrentBroadcastStandard: Guid, SettlingTime: POINTER(Int32), TvStandardsSupported: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetScanSignalTypeFilter(self, ScanModulationTypes: Int32, AnalogVideoStandard: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ISectionList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{afec1eb5-2a64-46c6-bf4b-ae3ccb6afdb0}')
    @commethod(3)
    def Initialize(self, requestType: Windows.Win32.Media.DirectShow.Tv.MPEG_REQUEST_TYPE, pMpeg2Data: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head, pContext: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_CONTEXT_head), pid: UInt16, tid: Byte, pFilter: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG2_FILTER_head), timeout: UInt32, hDoneEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeWithRawSections(self, pmplSections: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_PACKET_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelPendingRequest(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNumberOfSections(self, pCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSectionData(self, sectionNumber: UInt16, pdwRawPacketLength: POINTER(UInt32), ppSection: POINTER(POINTER(Windows.Win32.Media.DirectShow.Tv.SECTION_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProgramIdentifier(self, pPid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableIdentifier(self, pTableId: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceLocationDescriptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{58c3c827-9d91-4215-bff3-820a49f0904c}')
    @commethod(3)
    def GetPCR_PID(self, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberOfElements(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetElementStreamType(self, bIndex: Byte, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetElementPID(self, bIndex: Byte, pwVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetElementLanguageCode(self, bIndex: Byte, LangCode: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferConfigure(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ce14dfae-4098-4af7-bbf7-d6511f835414}')
    @commethod(3)
    def SetDirectory(self, pszDirectoryName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDirectory(self, ppszDirectoryName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetBackingFileCount(self, dwMin: UInt32, dwMax: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBackingFileCount(self, pdwMin: POINTER(UInt32), pdwMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetBackingFileDuration(self, dwSeconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBackingFileDuration(self, pdwSeconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferConfigure2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IStreamBufferConfigure
    _iid_ = Guid('{53e037bf-3992-4282-ae34-2487b4dae06b}')
    @commethod(9)
    def SetMultiplexedPacketSize(self, cbBytesPerPacket: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMultiplexedPacketSize(self, pcbBytesPerPacket: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetFFTransitionRates(self, dwMaxFullFrameRate: UInt32, dwMaxNonSkippingRate: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFFTransitionRates(self, pdwMaxFullFrameRate: POINTER(UInt32), pdwMaxNonSkippingRate: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferConfigure3(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IStreamBufferConfigure2
    _iid_ = Guid('{7e2d2a1e-7192-4bd7-80c1-061fd1d10402}')
    @commethod(13)
    def SetStartRecConfig(self, fStartStopsCur: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStartRecConfig(self, pfStartStopsCur: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetNamespace(self, pszNamespace: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetNamespace(self, ppszNamespace: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferDataCounters(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9d2a2563-31ab-402e-9a6b-adb903489440}')
    @commethod(3)
    def GetData(self, pPinData: POINTER(Windows.Win32.Media.DirectShow.Tv.SBE_PIN_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResetData(self) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferInitialize(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ce50f2d-6ba7-40fb-a034-50b1a674ec78}')
    @commethod(3)
    def SetHKEY(self, hkeyRoot: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSIDs(self, cSIDs: UInt32, ppSID: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferMediaSeeking(ComPtr):
    extends: Windows.Win32.Media.DirectShow.IMediaSeeking
    _iid_ = Guid('{f61f5c26-863d-4afa-b0ba-2f81dc978596}')
class IStreamBufferMediaSeeking2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IStreamBufferMediaSeeking
    _iid_ = Guid('{3a439ab0-155f-470a-86a6-9ea54afd6eaf}')
    @commethod(20)
    def SetRateEx(self, dRate: Double, dwFramesPerSec: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferRecComp(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9e259a9b-8815-42ae-b09f-221970b154fd}')
    @commethod(3)
    def Initialize(self, pszTargetFilename: Windows.Win32.Foundation.PWSTR, pszSBRecProfileRef: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Append(self, pszSBRecording: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AppendEx(self, pszSBRecording: Windows.Win32.Foundation.PWSTR, rtStart: Int64, rtStop: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentLength(self, pcSeconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferRecordControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba9b6c99-f3c7-4ff2-92db-cfdd4851bf31}')
    @commethod(3)
    def Start(self, prtStart: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self, rtStop: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecordingStatus(self, phResult: POINTER(Windows.Win32.Foundation.HRESULT), pbStarted: POINTER(Windows.Win32.Foundation.BOOL), pbStopped: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferRecordingAttribute(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{16ca4e03-fe69-4705-bd41-5b7dfc0c95f3}')
    @commethod(3)
    def SetAttribute(self, ulReserved: UInt32, pszAttributeName: Windows.Win32.Foundation.PWSTR, StreamBufferAttributeType: Windows.Win32.Media.DirectShow.Tv.STREAMBUFFER_ATTR_DATATYPE, pbAttribute: POINTER(Byte), cbAttributeLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttributeCount(self, ulReserved: UInt32, pcAttributes: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributeByName(self, pszAttributeName: Windows.Win32.Foundation.PWSTR, pulReserved: POINTER(UInt32), pStreamBufferAttributeType: POINTER(Windows.Win32.Media.DirectShow.Tv.STREAMBUFFER_ATTR_DATATYPE), pbAttribute: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributeByIndex(self, wIndex: UInt16, pulReserved: POINTER(UInt32), pszAttributeName: Windows.Win32.Foundation.PWSTR, pcchNameLength: POINTER(UInt16), pStreamBufferAttributeType: POINTER(Windows.Win32.Media.DirectShow.Tv.STREAMBUFFER_ATTR_DATATYPE), pbAttribute: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumAttributes(self, ppIEnumStreamBufferAttrib: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumStreamBufferRecordingAttrib_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{afd1f242-7efd-45ee-ba4e-407a25c9a77a}')
    @commethod(3)
    def LockProfile(self, pszStreamBufferFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRecorder(self, pszFilename: Windows.Win32.Foundation.PWSTR, dwRecordType: UInt32, pRecordingIUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsProfileLocked(self) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferSink2(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IStreamBufferSink
    _iid_ = Guid('{db94a660-f4fb-4bfa-bcc6-fe159a4eea93}')
    @commethod(6)
    def UnlockProfile(self) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferSink3(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.IStreamBufferSink2
    _iid_ = Guid('{974723f2-887a-4452-9366-2cff3057bc8f}')
    @commethod(7)
    def SetAvailableFilter(self, prtMin: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamBufferSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1c5bd776-6ced-4f44-8164-5eab0e98db12}')
    @commethod(3)
    def SetStreamSink(self, pIStreamBufferSink: Windows.Win32.Media.DirectShow.Tv.IStreamBufferSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITSDT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d19bdb43-405b-4a7c-a791-c89110c33165}')
    @commethod(3)
    def Initialize(self, pSectionList: Windows.Win32.Media.DirectShow.Tv.ISectionList_head, pMPEGData: Windows.Win32.Media.DirectShow.Tv.IMpeg2Data_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(self, pbVal: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(self, dwIndex: UInt32, ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(self, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(Windows.Win32.Media.DirectShow.Tv.IGenericDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterForNextTable(self, hNextTableAvailable: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextTable(self, ppTSDT: POINTER(Windows.Win32.Media.DirectShow.Tv.ITSDT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForWhenCurrent(self, hNextTableIsCurrent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ConvertNextToCurrent(self) -> Windows.Win32.Foundation.HRESULT: ...
class ITuneRequest(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{07ddc146-fc3d-11d2-9d8c-00c04f72d980}')
    @commethod(7)
    def get_TuningSpace(self, TuningSpace: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Components(self, Components: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponents_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Clone(self, NewTuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Locator(self, Locator: POINTER(Windows.Win32.Media.DirectShow.Tv.ILocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Locator(self, Locator: Windows.Win32.Media.DirectShow.Tv.ILocator_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITuneRequestInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3b152df-7a90-4218-ac54-9830bee8c0b6}')
    @commethod(3)
    def GetLocatorData(self, Request: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetComponentData(self, CurrentRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateComponentList(self, CurrentRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNextProgram(self, CurrentRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head, TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPreviousProgram(self, CurrentRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head, TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNextLocator(self, CurrentRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head, TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPreviousLocator(self, CurrentRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head, TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITuneRequestInfoEx(ComPtr):
    extends: Windows.Win32.Media.DirectShow.Tv.ITuneRequestInfo
    _iid_ = Guid('{ee957c52-b0d0-4e78-8dd1-b87a08bfd893}')
    @commethod(10)
    def CreateComponentListEx(self, CurrentRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head, ppCurPMT: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITuner(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{28c52640-018a-11d3-9d8e-00c04f72d980}')
    @commethod(3)
    def get_TuningSpace(self, TuningSpace: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_TuningSpace(self, TuningSpace: Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumTuningSpaces(self, ppEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumTuningSpaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_TuneRequest(self, TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_TuneRequest(self, TuneRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Validate(self, TuneRequest: Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PreferredComponentTypes(self, ComponentTypes: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponentTypes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PreferredComponentTypes(self, ComponentTypes: Windows.Win32.Media.DirectShow.Tv.IComponentTypes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SignalStrength(self, Strength: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def TriggerSignalEvents(self, Interval: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ITunerCap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e60dfa45-8d56-4e65-a8ab-d6be9412c249}')
    @commethod(3)
    def get_SupportedNetworkTypes(self, ulcNetworkTypesMax: UInt32, pulcNetworkTypes: POINTER(UInt32), pguidNetworkTypes: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SupportedVideoFormats(self, pulAMTunerModeType: POINTER(UInt32), pulAnalogVideoStandard: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AuxInputCount(self, pulCompositeCount: POINTER(UInt32), pulSvideoCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ITunerCapEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ed3e0c66-18c8-4ea6-9300-f6841fdd35dc}')
    @commethod(3)
    def get_Has608_708Caption(self, pbHasCaption: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ITuningSpace(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{061c6e30-e622-11d2-9493-00c04f72d980}')
    @commethod(7)
    def get_UniqueName(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_UniqueName(self, Name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FriendlyName(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_FriendlyName(self, Name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CLSID(self, SpaceCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_NetworkType(self, NetworkTypeGuid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_NetworkType(self, NetworkTypeGuid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get__NetworkType(self, NetworkTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put__NetworkType(self, NetworkTypeGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateTuneRequest(self, TuneRequest: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuneRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumCategoryGUIDs(self, ppEnum: POINTER(Windows.Win32.System.Com.IEnumGUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumDeviceMonikers(self, ppEnum: POINTER(Windows.Win32.System.Com.IEnumMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DefaultPreferredComponentTypes(self, ComponentTypes: POINTER(Windows.Win32.Media.DirectShow.Tv.IComponentTypes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DefaultPreferredComponentTypes(self, NewComponentTypes: Windows.Win32.Media.DirectShow.Tv.IComponentTypes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_FrequencyMapping(self, pMapping: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_FrequencyMapping(self, Mapping: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_DefaultLocator(self, LocatorVal: POINTER(Windows.Win32.Media.DirectShow.Tv.ILocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_DefaultLocator(self, LocatorVal: Windows.Win32.Media.DirectShow.Tv.ILocator_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Clone(self, NewTS: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITuningSpaceContainer(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5b692e84-e2f1-11d2-9493-00c04f72d980}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, NewEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, varIndex: Windows.Win32.System.Variant.VARIANT, TuningSpace: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Item(self, varIndex: Windows.Win32.System.Variant.VARIANT, TuningSpace: Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def TuningSpacesForCLSID(self, SpaceCLSID: Windows.Win32.Foundation.BSTR, NewColl: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def _TuningSpacesForCLSID2(self, SpaceCLSID: POINTER(Guid), NewColl: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def TuningSpacesForName(self, Name: Windows.Win32.Foundation.BSTR, NewColl: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def FindID(self, TuningSpace: Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head, ID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Add(self, TuningSpace: Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head, NewIndex: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_EnumTuningSpaces(self, ppEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumTuningSpaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Remove(self, Index: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_MaxCount(self, MaxCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_MaxCount(self, MaxCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ITuningSpaces(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{901284e4-33fe-4b69-8d63-634a596f3756}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, NewEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, varIndex: Windows.Win32.System.Variant.VARIANT, TuningSpace: POINTER(Windows.Win32.Media.DirectShow.Tv.ITuningSpace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EnumTuningSpaces(self, NewEnum: POINTER(Windows.Win32.Media.DirectShow.Tv.IEnumTuningSpaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXDSCodec(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4c4c4b3-0049-4e2b-98fb-9537f6ce516d}')
    @commethod(3)
    def get_XDSToRatObjOK(self, pHrCoCreateRetVal: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_CCSubstreamService(self, SubstreamMask: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CCSubstreamService(self, pSubstreamMask: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetContentAdvisoryRating(self, pRat: POINTER(Int32), pPktSeqID: POINTER(Int32), pCallSeqID: POINTER(Int32), pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetXDSPacket(self, pXDSClassPkt: POINTER(Int32), pXDSTypePkt: POINTER(Int32), pBstrXDSPkt: POINTER(Windows.Win32.Foundation.BSTR), pPktSeqID: POINTER(Int32), pCallSeqID: POINTER(Int32), pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrLicenseExpDate(self, protType: POINTER(Windows.Win32.Media.DirectShow.Tv.ProtType), lpDateTime: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastErrorCode(self) -> Windows.Win32.Foundation.HRESULT: ...
class IXDSCodecConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4c4c4d3-0049-4e2b-98fb-9537f6ce516d}')
    @commethod(3)
    def GetSecureChannelObject(self, ppUnkDRMSecureChannel: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPauseBufferTime(self, dwPauseBufferTime: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IXDSCodecEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c4c4c4c3-0049-4e2b-98fb-9537f6ce516d}')
class IXDSToRat(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c5c5c5b0-3abc-11d6-b25b-00c04fa0c026}')
    @commethod(7)
    def Init(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ParseXDSBytePair(self, byte1: Byte, byte2: Byte, pEnSystem: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_System), pEnLevel: POINTER(Windows.Win32.Media.DirectShow.Tv.EnTvRat_GenericLevel), plBfEnAttributes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
KSCATEGORY_BDA_IP_SINK = Guid('{71985f4a-1ca1-11d3-9cc8-00c04f7971e0}')
KSCATEGORY_BDA_NETWORK_EPG = Guid('{71985f49-1ca1-11d3-9cc8-00c04f7971e0}')
KSCATEGORY_BDA_NETWORK_PROVIDER = Guid('{71985f4b-1ca1-11d3-9cc8-00c04f7971e0}')
KSCATEGORY_BDA_NETWORK_TUNER = Guid('{71985f48-1ca1-11d3-9cc8-00c04f7971e0}')
KSCATEGORY_BDA_RECEIVER_COMPONENT = Guid('{fd0a5af4-b41d-11d2-9c95-00c04f7971e0}')
KSCATEGORY_BDA_TRANSPORT_INFORMATION = Guid('{a2e3074f-6c3d-11d3-b653-00c04f79498e}')
KSDATAFORMAT_SPECIFIER_BDA_IP = Guid('{6b891420-db09-11d2-8f32-00c04f7971e2}')
KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT = Guid('{8deda6fd-ac5f-4334-8ecf-a4ba8fa7d0f0}')
KSDATAFORMAT_SUBTYPE_ATSC_SI = Guid('{b3c7397c-d303-414d-b33c-4ed2c9d29733}')
KSDATAFORMAT_SUBTYPE_BDA_IP = Guid('{5a9a213c-db08-11d2-8f32-00c04f7971e2}')
KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL = Guid('{499856e8-e85b-48ed-9bea-410d0dd4ef81}')
KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT = Guid('{f4aeb342-0329-4fdd-a8fd-4aff4926c978}')
KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP = Guid('{951727db-d2ce-4528-96f6-3301fabb2de0}')
KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP = Guid('{762e3f66-336f-48d1-bf83-2b00352c11f0}')
KSDATAFORMAT_SUBTYPE_DVB_SI = Guid('{e9dd31a3-221d-4adb-8532-9af309c1a408}')
KSDATAFORMAT_SUBTYPE_ISDB_SI = Guid('{4a2eeb99-6458-4538-b187-04017c41413f}')
KSDATAFORMAT_SUBTYPE_PBDA_TRANSPORT_RAW = Guid('{0d7aed42-cb9a-11db-9705-005056c00008}')
KSDATAFORMAT_TYPE_BDA_ANTENNA = Guid('{71985f41-1ca1-11d3-9cc8-00c04f7971e0}')
KSDATAFORMAT_TYPE_BDA_IF_SIGNAL = Guid('{61be0b47-a5eb-499b-9a85-5b16c07f1258}')
KSDATAFORMAT_TYPE_BDA_IP = Guid('{e25f7b8e-cccc-11d2-8f25-00c04f7971e2}')
KSDATAFORMAT_TYPE_BDA_IP_CONTROL = Guid('{dadd5799-7d5b-4b63-80fb-d1442f26b621}')
KSDATAFORMAT_TYPE_MPE = Guid('{455f176c-4b06-47ce-9aef-8caef73df7b5}')
KSDATAFORMAT_TYPE_MPEG2_SECTIONS = Guid('{455f176c-4b06-47ce-9aef-8caef73df7b5}')
class KSEVENTDATA_BDA_RF_TUNER_SCAN_S(EasyCastStructure):
    EventData: Windows.Win32.Media.KernelStreaming.KSEVENTDATA
    StartFrequency: UInt32
    EndFrequency: UInt32
    LockRequested: Windows.Win32.Media.DirectShow.Tv.BDA_LockType
KSEVENTSETID_BdaCAEvent = Guid('{488c4ccc-b768-4129-8eb1-b00a071f9068}')
KSEVENTSETID_BdaDiseqCEvent = Guid('{8b19bbf0-4184-43ac-ad3c-0c889be4c212}')
KSEVENTSETID_BdaEvent = Guid('{ae7e55b2-96d7-4e29-908f-62f95b2a1679}')
KSEVENTSETID_BdaPinEvent = Guid('{104781cd-50bd-40d5-95fb-087e0e86a591}')
KSEVENTSETID_BdaTunerEvent = Guid('{aab59e17-01c9-4ebf-93f2-fc3b79b46f91}')
KSEVENT_BDA_EVENT_TYPE = Int32
KSEVENT_BDA_EVENT_PENDINGEVENT: KSEVENT_BDA_EVENT_TYPE = 0
KSEVENT_BDA_TUNER = Int32
KSEVENT_BDA_TUNER_SCAN: KSEVENT_BDA_TUNER = 0
KSMETHODSETID_BdaChangeSync = Guid('{fd0a5af3-b41d-11d2-9c95-00c04f7971e0}')
KSMETHODSETID_BdaConditionalAccessService = Guid('{10ced3b4-320b-41bf-9824-1b2e68e71eb9}')
KSMETHODSETID_BdaDebug = Guid('{0d4a90ec-c69d-4ee2-8c5a-fb1f63a50da1}')
KSMETHODSETID_BdaDeviceConfiguration = Guid('{71985f45-1ca1-11d3-9cc8-00c04f7971e0}')
KSMETHODSETID_BdaDrmService = Guid('{bff6b5bb-b0ae-484c-9dca-73528fb0b46e}')
KSMETHODSETID_BdaEventing = Guid('{f99492da-6193-4eb0-8690-6686cbff713e}')
KSMETHODSETID_BdaGuideDataDeliveryService = Guid('{8d9d5562-1589-417d-99ce-ac531dda19f9}')
KSMETHODSETID_BdaIsdbConditionalAccess = Guid('{5e68c627-16c2-4e6c-b1e2-d00170cdaa0f}')
KSMETHODSETID_BdaMux = Guid('{942aafec-4c05-4c74-b8eb-8706c2a4943f}')
KSMETHODSETID_BdaNameValue = Guid('{36e07304-9f0d-4e88-9118-ac0ba317b7f2}')
KSMETHODSETID_BdaNameValueA = Guid('{0c24096d-5ff5-47de-a856-062e587e3727}')
KSMETHODSETID_BdaScanning = Guid('{12eb49df-6249-47f3-b190-e21e6e2f8a9c}')
KSMETHODSETID_BdaTSSelector = Guid('{1dcfafe9-b45e-41b3-bb2a-561eb129ae98}')
KSMETHODSETID_BdaTuner = Guid('{b774102f-ac07-478a-8228-2742d961fa7e}')
KSMETHODSETID_BdaUserActivity = Guid('{eda5c834-4531-483c-be0a-94e6c96ff396}')
KSMETHODSETID_BdaWmdrmSession = Guid('{4be6fa3d-07cd-4139-8b80-8c18ba3aec88}')
KSMETHODSETID_BdaWmdrmTuner = Guid('{86d979cf-a8a7-4f94-b5fb-14c0aca68fe6}')
KSMETHOD_BDA_CAS_SERVICE = Int32
KSMETHOD_BDA_CAS_CHECKENTITLEMENTTOKEN: KSMETHOD_BDA_CAS_SERVICE = 0
KSMETHOD_BDA_CAS_SETCAPTURETOKEN: KSMETHOD_BDA_CAS_SERVICE = 1
KSMETHOD_BDA_CAS_OPENBROADCASTMMI: KSMETHOD_BDA_CAS_SERVICE = 2
KSMETHOD_BDA_CAS_CLOSEMMIDIALOG: KSMETHOD_BDA_CAS_SERVICE = 3
KSMETHOD_BDA_CHANGE_SYNC = Int32
KSMETHOD_BDA_START_CHANGES: KSMETHOD_BDA_CHANGE_SYNC = 0
KSMETHOD_BDA_CHECK_CHANGES: KSMETHOD_BDA_CHANGE_SYNC = 1
KSMETHOD_BDA_COMMIT_CHANGES: KSMETHOD_BDA_CHANGE_SYNC = 2
KSMETHOD_BDA_GET_CHANGE_STATE: KSMETHOD_BDA_CHANGE_SYNC = 3
KSMETHOD_BDA_DEBUG_SERVICE = Int32
KSMETHOD_BDA_DEBUG_LEVEL: KSMETHOD_BDA_DEBUG_SERVICE = 0
KSMETHOD_BDA_DEBUG_DATA: KSMETHOD_BDA_DEBUG_SERVICE = 1
KSMETHOD_BDA_DEVICE_CONFIGURATION = Int32
KSMETHOD_BDA_CREATE_PIN_FACTORY: KSMETHOD_BDA_DEVICE_CONFIGURATION = 0
KSMETHOD_BDA_DELETE_PIN_FACTORY: KSMETHOD_BDA_DEVICE_CONFIGURATION = 1
KSMETHOD_BDA_CREATE_TOPOLOGY: KSMETHOD_BDA_DEVICE_CONFIGURATION = 2
KSMETHOD_BDA_DRM = Int32
KSMETHOD_BDA_DRM_CURRENT: KSMETHOD_BDA_DRM = 0
KSMETHOD_BDA_DRM_DRMSTATUS: KSMETHOD_BDA_DRM = 1
KSMETHOD_BDA_EVENTING_SERVICE = Int32
KSMETHOD_BDA_EVENT_DATA: KSMETHOD_BDA_EVENTING_SERVICE = 0
KSMETHOD_BDA_EVENT_COMPLETE: KSMETHOD_BDA_EVENTING_SERVICE = 1
KSMETHOD_BDA_GDDS_SERVICE = Int32
KSMETHOD_BDA_GDDS_DATATYPE: KSMETHOD_BDA_GDDS_SERVICE = 0
KSMETHOD_BDA_GDDS_DATA: KSMETHOD_BDA_GDDS_SERVICE = 1
KSMETHOD_BDA_GDDS_TUNEXMLFROMIDX: KSMETHOD_BDA_GDDS_SERVICE = 2
KSMETHOD_BDA_GDDS_GETSERVICES: KSMETHOD_BDA_GDDS_SERVICE = 3
KSMETHOD_BDA_GDDS_SERVICEFROMTUNEXML: KSMETHOD_BDA_GDDS_SERVICE = 4
KSMETHOD_BDA_GDDS_DATAUPDATE: KSMETHOD_BDA_GDDS_SERVICE = 5
KSMETHOD_BDA_GPNV_SERVICE = Int32
KSMETHOD_BDA_GPNV_GETVALUE: KSMETHOD_BDA_GPNV_SERVICE = 0
KSMETHOD_BDA_GPNV_SETVALUE: KSMETHOD_BDA_GPNV_SERVICE = 1
KSMETHOD_BDA_GPNV_NAMEFROMINDEX: KSMETHOD_BDA_GPNV_SERVICE = 2
KSMETHOD_BDA_GPNV_GETVALUEUPDATENAME: KSMETHOD_BDA_GPNV_SERVICE = 3
KSMETHOD_BDA_ISDB_CAS = Int32
KSMETHOD_BDA_ISDBCAS_SETREQUEST: KSMETHOD_BDA_ISDB_CAS = 0
KSMETHOD_BDA_ISDBCAS_RESPONSEDATA: KSMETHOD_BDA_ISDB_CAS = 1
KSMETHOD_BDA_MUX_SERVICE = Int32
KSMETHOD_BDA_MUX_GETPIDLIST: KSMETHOD_BDA_MUX_SERVICE = 0
KSMETHOD_BDA_MUX_SETPIDLIST: KSMETHOD_BDA_MUX_SERVICE = 1
KSMETHOD_BDA_SCAN_SERVICE = Int32
KSMETHOD_BDA_SCAN_CAPABILTIES: KSMETHOD_BDA_SCAN_SERVICE = 0
KSMETHOD_BDA_SCANNING_STATE: KSMETHOD_BDA_SCAN_SERVICE = 1
KSMETHOD_BDA_SCAN_FILTER: KSMETHOD_BDA_SCAN_SERVICE = 2
KSMETHOD_BDA_SCAN_START: KSMETHOD_BDA_SCAN_SERVICE = 3
KSMETHOD_BDA_SCAN_RESUME: KSMETHOD_BDA_SCAN_SERVICE = 4
KSMETHOD_BDA_SCAN_STOP: KSMETHOD_BDA_SCAN_SERVICE = 5
KSMETHOD_BDA_TS_SELECTOR = Int32
KSMETHOD_BDA_TS_SELECTOR_SETTSID: KSMETHOD_BDA_TS_SELECTOR = 0
KSMETHOD_BDA_TS_SELECTOR_GETTSINFORMATION: KSMETHOD_BDA_TS_SELECTOR = 1
KSMETHOD_BDA_TUNER_SERVICE = Int32
KSMETHOD_BDA_TUNER_SETTUNER: KSMETHOD_BDA_TUNER_SERVICE = 0
KSMETHOD_BDA_TUNER_GETTUNERSTATE: KSMETHOD_BDA_TUNER_SERVICE = 1
KSMETHOD_BDA_TUNER_SIGNALNOISERATIO: KSMETHOD_BDA_TUNER_SERVICE = 2
KSMETHOD_BDA_USERACTIVITY_SERVICE = Int32
KSMETHOD_BDA_USERACTIVITY_USEREASON: KSMETHOD_BDA_USERACTIVITY_SERVICE = 0
KSMETHOD_BDA_USERACTIVITY_INTERVAL: KSMETHOD_BDA_USERACTIVITY_SERVICE = 1
KSMETHOD_BDA_USERACTIVITY_DETECTED: KSMETHOD_BDA_USERACTIVITY_SERVICE = 2
KSMETHOD_BDA_WMDRM = Int32
KSMETHOD_BDA_WMDRM_STATUS: KSMETHOD_BDA_WMDRM = 0
KSMETHOD_BDA_WMDRM_REVINFO: KSMETHOD_BDA_WMDRM = 1
KSMETHOD_BDA_WMDRM_CRL: KSMETHOD_BDA_WMDRM = 2
KSMETHOD_BDA_WMDRM_MESSAGE: KSMETHOD_BDA_WMDRM = 3
KSMETHOD_BDA_WMDRM_REISSUELICENSE: KSMETHOD_BDA_WMDRM = 4
KSMETHOD_BDA_WMDRM_RENEWLICENSE: KSMETHOD_BDA_WMDRM = 5
KSMETHOD_BDA_WMDRM_LICENSE: KSMETHOD_BDA_WMDRM = 6
KSMETHOD_BDA_WMDRM_KEYINFO: KSMETHOD_BDA_WMDRM = 7
KSMETHOD_BDA_WMDRM_TUNER = Int32
KSMETHOD_BDA_WMDRMTUNER_CANCELCAPTURETOKEN: KSMETHOD_BDA_WMDRM_TUNER = 0
KSMETHOD_BDA_WMDRMTUNER_SETPIDPROTECTION: KSMETHOD_BDA_WMDRM_TUNER = 1
KSMETHOD_BDA_WMDRMTUNER_GETPIDPROTECTION: KSMETHOD_BDA_WMDRM_TUNER = 2
KSMETHOD_BDA_WMDRMTUNER_SETSYNCVALUE: KSMETHOD_BDA_WMDRM_TUNER = 3
KSMETHOD_BDA_WMDRMTUNER_STARTCODEPROFILE: KSMETHOD_BDA_WMDRM_TUNER = 4
KSMETHOD_BDA_WMDRMTUNER_PURCHASE_ENTITLEMENT: KSMETHOD_BDA_WMDRM_TUNER = 5
class KSM_BDA_BUFFER(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulBufferSize: UInt32
    argbBuffer: Byte * 1
class KSM_BDA_CAS_CAPTURETOKEN(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulTokenLength: UInt32
    argbToken: Byte * 1
class KSM_BDA_CAS_CLOSEMMIDIALOG(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: Windows.Win32.Foundation.CHAR * 12
    ulDialogNumber: UInt32
    ulReason: UInt32
class KSM_BDA_CAS_ENTITLEMENTTOKEN(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: Windows.Win32.Foundation.CHAR * 12
    ulRequestType: UInt32
    ulEntitlementTokenLen: UInt32
    argbEntitlementToken: Byte * 1
class KSM_BDA_CAS_OPENBROADCASTMMI(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: Windows.Win32.Foundation.CHAR * 12
    ulEventId: UInt32
class KSM_BDA_DEBUG_LEVEL(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ucDebugLevel: Byte
    ulDebugStringSize: UInt32
    argbDebugString: Byte * 1
class KSM_BDA_DRM_SETDRM(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    NewDRMuuid: Guid
class KSM_BDA_EVENT_COMPLETE(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulEventID: UInt32
    ulEventResult: UInt32
class KSM_BDA_GDDS_SERVICEFROMTUNEXML(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulTuneXmlLength: UInt32
    argbTuneXml: Byte * 1
class KSM_BDA_GDDS_TUNEXMLFROMIDX(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulIdx: UInt64
class KSM_BDA_GPNV_GETVALUE(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulNameLength: UInt32
    cLanguage: Windows.Win32.Foundation.CHAR * 12
    argbData: Byte * 1
class KSM_BDA_GPNV_NAMEINDEX(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulValueNameIndex: UInt32
class KSM_BDA_GPNV_SETVALUE(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulDialogRequest: UInt32
    cLanguage: Windows.Win32.Foundation.CHAR * 12
    ulNameLength: UInt32
    ulValueLength: UInt32
    argbName: Byte * 1
class KSM_BDA_ISDBCAS_REQUEST(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulRequestID: UInt32
    ulIsdbCommandSize: UInt32
    argbIsdbCommandData: Byte * 1
class KSM_BDA_PIN(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    Anonymous: _Anonymous_e__Union
    Reserved: UInt32
    class _Anonymous_e__Union(EasyCastUnion):
        PinId: UInt32
        PinType: UInt32
class KSM_BDA_PIN_PAIR(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(EasyCastUnion):
        InputPinId: UInt32
        InputPinType: UInt32
    class _Anonymous2_e__Union(EasyCastUnion):
        OutputPinId: UInt32
        OutputPinType: UInt32
class KSM_BDA_SCAN_CAPABILTIES(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    uuidBroadcastStandard: Guid
class KSM_BDA_SCAN_FILTER(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulScanModulationTypeSize: UInt32
    AnalogVideoStandards: UInt64
    argbScanModulationTypes: Byte * 1
class KSM_BDA_SCAN_START(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    LowerFrequency: UInt32
    HigherFrequency: UInt32
class KSM_BDA_TS_SELECTOR_SETTSID(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    usTSID: UInt16
class KSM_BDA_TUNER_TUNEREQUEST(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulTuneLength: UInt32
    argbTuneData: Byte * 1
class KSM_BDA_USERACTIVITY_USEREASON(EasyCastStructure):
    Method: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulUseReason: UInt32
class KSM_BDA_WMDRMTUNER_GETPIDPROTECTION(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulPID: UInt32
class KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: Windows.Win32.Foundation.CHAR * 12
    ulPurchaseTokenLength: UInt32
    argbDataBuffer: Byte * 1
class KSM_BDA_WMDRMTUNER_SETPIDPROTECTION(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulPID: UInt32
    uuidKeyID: Guid
class KSM_BDA_WMDRMTUNER_SYNCVALUE(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulSyncValue: UInt32
class KSM_BDA_WMDRM_LICENSE(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    uuidKeyID: Guid
class KSM_BDA_WMDRM_RENEWLICENSE(EasyCastStructure):
    NodeMethod: Windows.Win32.Media.KernelStreaming.KSM_NODE
    ulXMRLicenseLength: UInt32
    ulEntitlementTokenLength: UInt32
    argbDataBuffer: Byte * 1
KSNODE_BDA_8PSK_DEMODULATOR = Guid('{e957a0e7-dd98-4a3c-810b-3525157ab62e}')
KSNODE_BDA_8VSB_DEMODULATOR = Guid('{71985f4f-1ca1-11d3-9cc8-00c04f7971e0}')
KSNODE_BDA_ANALOG_DEMODULATOR = Guid('{634db199-27dd-46b8-acfb-ecc98e61a2ad}')
KSNODE_BDA_COFDM_DEMODULATOR = Guid('{2dac6e05-edbe-4b9c-b387-1b6fad7d6495}')
KSNODE_BDA_COMMON_CA_POD = Guid('{d83ef8fc-f3b8-45ab-8b71-ecf7c339deb4}')
KSNODE_BDA_DRI_DRM = Guid('{4f95ad74-cefb-42d2-94a9-68c5b2c1aabe}')
KSNODE_BDA_IP_SINK = Guid('{71985f4e-1ca1-11d3-9cc8-00c04f7971e0}')
KSNODE_BDA_ISDB_S_DEMODULATOR = Guid('{edde230a-9086-432d-b8a5-6670263807e9}')
KSNODE_BDA_ISDB_T_DEMODULATOR = Guid('{fcea3ae3-2cb2-464d-8f5d-305c0bb778a2}')
KSNODE_BDA_OPENCABLE_POD = Guid('{345812a0-fb7c-4790-aa7e-b1db88ac19c9}')
KSNODE_BDA_PBDA_CAS = Guid('{c026869f-7129-4e71-8696-ec8f75299b77}')
KSNODE_BDA_PBDA_DRM = Guid('{9eeebd03-eea1-450f-96ae-633e6de63cce}')
KSNODE_BDA_PBDA_ISDBCAS = Guid('{f2cf2ab3-5b9d-40ae-ab7c-4e7ad0bd1c52}')
KSNODE_BDA_PBDA_MUX = Guid('{f88c7787-6678-4f4b-a13e-da09861d682b}')
KSNODE_BDA_PBDA_TUNER = Guid('{aa5e8286-593c-4979-9494-46a2a9dfe076}')
KSNODE_BDA_PID_FILTER = Guid('{f5412789-b0a0-44e1-ae4f-ee999b1b7fbe}')
KSNODE_BDA_QAM_DEMODULATOR = Guid('{71985f4d-1ca1-11d3-9cc8-00c04f7971e0}')
KSNODE_BDA_QPSK_DEMODULATOR = Guid('{6390c905-27c1-4d67-bdb7-77c50d079300}')
KSNODE_BDA_RF_TUNER = Guid('{71985f4c-1ca1-11d3-9cc8-00c04f7971e0}')
KSNODE_BDA_TS_SELECTOR = Guid('{5eddf185-fed1-4f45-9685-bbb73c323cfc}')
KSNODE_BDA_VIDEO_ENCODER = Guid('{d98429e3-65c9-4ac4-93aa-766782833b7a}')
KSPROPERTY_BDA_AUTODEMODULATE = Int32
KSPROPERTY_BDA_AUTODEMODULATE_START: KSPROPERTY_BDA_AUTODEMODULATE = 0
KSPROPERTY_BDA_AUTODEMODULATE_STOP: KSPROPERTY_BDA_AUTODEMODULATE = 1
KSPROPERTY_BDA_CA = Int32
KSPROPERTY_BDA_ECM_MAP_STATUS: KSPROPERTY_BDA_CA = 0
KSPROPERTY_BDA_CA_MODULE_STATUS: KSPROPERTY_BDA_CA = 1
KSPROPERTY_BDA_CA_SMART_CARD_STATUS: KSPROPERTY_BDA_CA = 2
KSPROPERTY_BDA_CA_MODULE_UI: KSPROPERTY_BDA_CA = 3
KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS: KSPROPERTY_BDA_CA = 4
KSPROPERTY_BDA_CA_REMOVE_PROGRAM: KSPROPERTY_BDA_CA = 5
KSPROPERTY_BDA_CA_EVENT = Int32
KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED: KSPROPERTY_BDA_CA_EVENT = 0
KSEVENT_BDA_CA_MODULE_STATUS_CHANGED: KSPROPERTY_BDA_CA_EVENT = 1
KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED: KSPROPERTY_BDA_CA_EVENT = 2
KSEVENT_BDA_CA_MODULE_UI_REQUESTED: KSPROPERTY_BDA_CA_EVENT = 3
KSPROPERTY_BDA_DIGITAL_DEMODULATOR = Int32
KSPROPERTY_BDA_MODULATION_TYPE: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 0
KSPROPERTY_BDA_INNER_FEC_TYPE: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 1
KSPROPERTY_BDA_INNER_FEC_RATE: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 2
KSPROPERTY_BDA_OUTER_FEC_TYPE: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 3
KSPROPERTY_BDA_OUTER_FEC_RATE: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 4
KSPROPERTY_BDA_SYMBOL_RATE: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 5
KSPROPERTY_BDA_SPECTRAL_INVERSION: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 6
KSPROPERTY_BDA_GUARD_INTERVAL: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 7
KSPROPERTY_BDA_TRANSMISSION_MODE: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 8
KSPROPERTY_BDA_ROLL_OFF: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 9
KSPROPERTY_BDA_PILOT: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 10
KSPROPERTY_BDA_SIGNALTIMEOUTS: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 11
KSPROPERTY_BDA_PLP_NUMBER: KSPROPERTY_BDA_DIGITAL_DEMODULATOR = 12
KSPROPERTY_BDA_DISEQC_COMMAND = Int32
KSPROPERTY_BDA_DISEQC_ENABLE: KSPROPERTY_BDA_DISEQC_COMMAND = 0
KSPROPERTY_BDA_DISEQC_LNB_SOURCE: KSPROPERTY_BDA_DISEQC_COMMAND = 1
KSPROPERTY_BDA_DISEQC_USETONEBURST: KSPROPERTY_BDA_DISEQC_COMMAND = 2
KSPROPERTY_BDA_DISEQC_REPEATS: KSPROPERTY_BDA_DISEQC_COMMAND = 3
KSPROPERTY_BDA_DISEQC_SEND: KSPROPERTY_BDA_DISEQC_COMMAND = 4
KSPROPERTY_BDA_DISEQC_RESPONSE: KSPROPERTY_BDA_DISEQC_COMMAND = 5
KSPROPERTY_BDA_DISEQC_EVENT = Int32
KSEVENT_BDA_DISEQC_DATA_RECEIVED: KSPROPERTY_BDA_DISEQC_EVENT = 0
KSPROPERTY_BDA_ETHERNET_FILTER = Int32
KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST_SIZE: KSPROPERTY_BDA_ETHERNET_FILTER = 0
KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST: KSPROPERTY_BDA_ETHERNET_FILTER = 1
KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_MODE: KSPROPERTY_BDA_ETHERNET_FILTER = 2
KSPROPERTY_BDA_FREQUENCY_FILTER = Int32
KSPROPERTY_BDA_RF_TUNER_FREQUENCY: KSPROPERTY_BDA_FREQUENCY_FILTER = 0
KSPROPERTY_BDA_RF_TUNER_POLARITY: KSPROPERTY_BDA_FREQUENCY_FILTER = 1
KSPROPERTY_BDA_RF_TUNER_RANGE: KSPROPERTY_BDA_FREQUENCY_FILTER = 2
KSPROPERTY_BDA_RF_TUNER_TRANSPONDER: KSPROPERTY_BDA_FREQUENCY_FILTER = 3
KSPROPERTY_BDA_RF_TUNER_BANDWIDTH: KSPROPERTY_BDA_FREQUENCY_FILTER = 4
KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER: KSPROPERTY_BDA_FREQUENCY_FILTER = 5
KSPROPERTY_BDA_RF_TUNER_CAPS: KSPROPERTY_BDA_FREQUENCY_FILTER = 6
KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS: KSPROPERTY_BDA_FREQUENCY_FILTER = 7
KSPROPERTY_BDA_RF_TUNER_STANDARD: KSPROPERTY_BDA_FREQUENCY_FILTER = 8
KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE: KSPROPERTY_BDA_FREQUENCY_FILTER = 9
KSPROPERTY_BDA_IPv4_FILTER = Int32
KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST_SIZE: KSPROPERTY_BDA_IPv4_FILTER = 0
KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST: KSPROPERTY_BDA_IPv4_FILTER = 1
KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_MODE: KSPROPERTY_BDA_IPv4_FILTER = 2
KSPROPERTY_BDA_IPv6_FILTER = Int32
KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST_SIZE: KSPROPERTY_BDA_IPv6_FILTER = 0
KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST: KSPROPERTY_BDA_IPv6_FILTER = 1
KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_MODE: KSPROPERTY_BDA_IPv6_FILTER = 2
KSPROPERTY_BDA_LNB_INFO = Int32
KSPROPERTY_BDA_LNB_LOF_LOW_BAND: KSPROPERTY_BDA_LNB_INFO = 0
KSPROPERTY_BDA_LNB_LOF_HIGH_BAND: KSPROPERTY_BDA_LNB_INFO = 1
KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY: KSPROPERTY_BDA_LNB_INFO = 2
KSPROPERTY_BDA_NULL_TRANSFORM = Int32
KSPROPERTY_BDA_NULL_TRANSFORM_START: KSPROPERTY_BDA_NULL_TRANSFORM = 0
KSPROPERTY_BDA_NULL_TRANSFORM_STOP: KSPROPERTY_BDA_NULL_TRANSFORM = 1
KSPROPERTY_BDA_PIDFILTER = Int32
KSPROPERTY_BDA_PIDFILTER_MAP_PIDS: KSPROPERTY_BDA_PIDFILTER = 0
KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS: KSPROPERTY_BDA_PIDFILTER = 1
KSPROPERTY_BDA_PIDFILTER_LIST_PIDS: KSPROPERTY_BDA_PIDFILTER = 2
KSPROPERTY_BDA_PIN_CONTROL = Int32
KSPROPERTY_BDA_PIN_ID: KSPROPERTY_BDA_PIN_CONTROL = 0
KSPROPERTY_BDA_PIN_TYPE: KSPROPERTY_BDA_PIN_CONTROL = 1
KSPROPERTY_BDA_PIN_EVENT = Int32
KSEVENT_BDA_PIN_CONNECTED: KSPROPERTY_BDA_PIN_EVENT = 0
KSEVENT_BDA_PIN_DISCONNECTED: KSPROPERTY_BDA_PIN_EVENT = 1
class KSPROPERTY_BDA_RF_TUNER_CAPS_S(EasyCastStructure):
    Property: Windows.Win32.Media.KernelStreaming.KSP_NODE
    Mode: UInt32
    AnalogStandardsSupported: UInt32
    DigitalStandardsSupported: UInt32
    MinFrequency: UInt32
    MaxFrequency: UInt32
    SettlingTime: UInt32
    AnalogSensingRange: UInt32
    DigitalSensingRange: UInt32
    MilliSecondsPerMHz: UInt32
class KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S(EasyCastStructure):
    Property: Windows.Win32.Media.KernelStreaming.KSP_NODE
    CurrentFrequency: UInt32
    FrequencyRangeMin: UInt32
    FrequencyRangeMax: UInt32
    MilliSecondsLeft: UInt32
class KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S(EasyCastStructure):
    Property: Windows.Win32.Media.KernelStreaming.KSP_NODE
    AutoDetect: Windows.Win32.Foundation.BOOL
class KSPROPERTY_BDA_RF_TUNER_STANDARD_S(EasyCastStructure):
    Property: Windows.Win32.Media.KernelStreaming.KSP_NODE
    SignalType: Windows.Win32.Media.DirectShow.Tv.BDA_SignalType
    SignalStandard: UInt32
KSPROPERTY_BDA_SIGNAL_STATS = Int32
KSPROPERTY_BDA_SIGNAL_STRENGTH: KSPROPERTY_BDA_SIGNAL_STATS = 0
KSPROPERTY_BDA_SIGNAL_QUALITY: KSPROPERTY_BDA_SIGNAL_STATS = 1
KSPROPERTY_BDA_SIGNAL_PRESENT: KSPROPERTY_BDA_SIGNAL_STATS = 2
KSPROPERTY_BDA_SIGNAL_LOCKED: KSPROPERTY_BDA_SIGNAL_STATS = 3
KSPROPERTY_BDA_SAMPLE_TIME: KSPROPERTY_BDA_SIGNAL_STATS = 4
KSPROPERTY_BDA_SIGNAL_LOCK_CAPS: KSPROPERTY_BDA_SIGNAL_STATS = 5
KSPROPERTY_BDA_SIGNAL_LOCK_TYPE: KSPROPERTY_BDA_SIGNAL_STATS = 6
KSPROPERTY_BDA_TOPOLOGY = Int32
KSPROPERTY_BDA_NODE_TYPES: KSPROPERTY_BDA_TOPOLOGY = 0
KSPROPERTY_BDA_PIN_TYPES: KSPROPERTY_BDA_TOPOLOGY = 1
KSPROPERTY_BDA_TEMPLATE_CONNECTIONS: KSPROPERTY_BDA_TOPOLOGY = 2
KSPROPERTY_BDA_NODE_METHODS: KSPROPERTY_BDA_TOPOLOGY = 3
KSPROPERTY_BDA_NODE_PROPERTIES: KSPROPERTY_BDA_TOPOLOGY = 4
KSPROPERTY_BDA_NODE_EVENTS: KSPROPERTY_BDA_TOPOLOGY = 5
KSPROPERTY_BDA_CONTROLLING_PIN_ID: KSPROPERTY_BDA_TOPOLOGY = 6
KSPROPERTY_BDA_NODE_DESCRIPTORS: KSPROPERTY_BDA_TOPOLOGY = 7
KSPROPERTY_BDA_VOID_TRANSFORM = Int32
KSPROPERTY_BDA_VOID_TRANSFORM_START: KSPROPERTY_BDA_VOID_TRANSFORM = 0
KSPROPERTY_BDA_VOID_TRANSFORM_STOP: KSPROPERTY_BDA_VOID_TRANSFORM = 1
KSPROPERTY_IDS_BDA_TABLE = Int32
KSPROPERTY_BDA_TABLE_SECTION: KSPROPERTY_IDS_BDA_TABLE = 0
KSPROPSETID_BdaAutodemodulate = Guid('{ddf15b12-bd25-11d2-9ca0-00c04f7971e0}')
KSPROPSETID_BdaCA = Guid('{b0693766-5278-4ec6-b9e1-3ce40560ef5a}')
KSPROPSETID_BdaDigitalDemodulator = Guid('{ef30f379-985b-4d10-b640-a79d5e04e1e0}')
KSPROPSETID_BdaDiseqCommand = Guid('{f84e2ab0-3c6b-45e3-a0fc-8669d4b81f11}')
KSPROPSETID_BdaEthernetFilter = Guid('{71985f43-1ca1-11d3-9cc8-00c04f7971e0}')
KSPROPSETID_BdaFrequencyFilter = Guid('{71985f47-1ca1-11d3-9cc8-00c04f7971e0}')
KSPROPSETID_BdaIPv4Filter = Guid('{71985f44-1ca1-11d3-9cc8-00c04f7971e0}')
KSPROPSETID_BdaIPv6Filter = Guid('{e1785a74-2a23-4fb3-9245-a8f88017ef33}')
KSPROPSETID_BdaLNBInfo = Guid('{992cf102-49f9-4719-a664-c4f23e2408f4}')
KSPROPSETID_BdaNullTransform = Guid('{ddf15b0d-bd25-11d2-9ca0-00c04f7971e0}')
KSPROPSETID_BdaPIDFilter = Guid('{d0a67d65-08df-4fec-8533-e5b550410b85}')
KSPROPSETID_BdaPinControl = Guid('{0ded49d5-a8b7-4d5d-97a1-12b0c195874d}')
KSPROPSETID_BdaSignalStats = Guid('{1347d106-cf3a-428a-a5cb-ac0d9a2a4338}')
KSPROPSETID_BdaTableSection = Guid('{516b99c5-971c-4aaf-b3f3-d9fda8a15e16}')
KSPROPSETID_BdaTopology = Guid('{a14ee835-0a23-11d3-9cc7-00c04f7971e0}')
KSPROPSETID_BdaVoidTransform = Guid('{71985f46-1ca1-11d3-9cc8-00c04f7971e0}')
class KSP_BDA_NODE_PIN(EasyCastStructure):
    Property: Windows.Win32.Media.KernelStreaming.KSIDENTIFIER
    ulNodeType: UInt32
    ulInputPinId: UInt32
    ulOutputPinId: UInt32
class KSP_NODE_ESPID(EasyCastStructure):
    Property: Windows.Win32.Media.KernelStreaming.KSP_NODE
    EsPid: UInt32
class KS_DATARANGE_BDA_ANTENNA(EasyCastStructure):
    DataRange: Windows.Win32.Media.KernelStreaming.KSDATAFORMAT
class KS_DATARANGE_BDA_TRANSPORT(EasyCastStructure):
    DataRange: Windows.Win32.Media.KernelStreaming.KSDATAFORMAT
    BdaTransportInfo: Windows.Win32.Media.DirectShow.Tv.BDA_TRANSPORT_INFO
class LONG_SECTION(EasyCastStructure):
    TableId: Byte
    Header: _Header_e__Union
    TableIdExtension: UInt16
    Version: _Version_e__Union
    SectionNumber: Byte
    LastSectionNumber: Byte
    RemainingData: Byte * 1
    _pack_ = 1
    class _Header_e__Union(EasyCastUnion):
        S: Windows.Win32.Media.DirectShow.Tv.MPEG_HEADER_BITS_MIDL
        W: UInt16
        _pack_ = 1
    class _Version_e__Union(EasyCastUnion):
        S: Windows.Win32.Media.DirectShow.Tv.MPEG_HEADER_VERSION_BITS_MIDL
        B: Byte
LanguageComponentType = Guid('{1be49f30-0e1b-11d3-9d8e-00c04f72d980}')
class LanguageInfo(EasyCastStructure):
    LangID: UInt16
    lISOLangCode: Int32
LicenseEventBlockReason = Int32
LIC_BadLicense: LicenseEventBlockReason = 0
LIC_NeedIndiv: LicenseEventBlockReason = 1
LIC_Expired: LicenseEventBlockReason = 2
LIC_NeedActivation: LicenseEventBlockReason = 3
LIC_ExtenderBlocked: LicenseEventBlockReason = 4
Locator = Guid('{0888c883-ac4f-4943-b516-2c38d9b34562}')
MPEG2Component = Guid('{055cb2d7-2969-45cd-914b-76890722f112}')
MPEG2ComponentType = Guid('{418008f3-cf67-4668-9628-10dc52be1d08}')
MPEG2TuneRequest = Guid('{0955ac62-bf2e-4cba-a2b9-a63f772d46cf}')
MPEG2TuneRequestFactory = Guid('{2c63e4eb-4cea-41b8-919c-e947ea19a77c}')
class MPEG2_FILTER(EasyCastStructure):
    bVersionNumber: Byte
    wFilterSize: UInt16
    fUseRawFilteringBits: Windows.Win32.Foundation.BOOL
    Filter: Byte * 16
    Mask: Byte * 16
    fSpecifyTableIdExtension: Windows.Win32.Foundation.BOOL
    TableIdExtension: UInt16
    fSpecifyVersion: Windows.Win32.Foundation.BOOL
    Version: Byte
    fSpecifySectionNumber: Windows.Win32.Foundation.BOOL
    SectionNumber: Byte
    fSpecifyCurrentNext: Windows.Win32.Foundation.BOOL
    fNext: Windows.Win32.Foundation.BOOL
    fSpecifyDsmccOptions: Windows.Win32.Foundation.BOOL
    Dsmcc: Windows.Win32.Media.DirectShow.Tv.DSMCC_FILTER_OPTIONS
    fSpecifyAtscOptions: Windows.Win32.Foundation.BOOL
    Atsc: Windows.Win32.Media.DirectShow.Tv.ATSC_FILTER_OPTIONS
    _pack_ = 1
class MPEG2_FILTER2(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    fSpecifyDvbEitOptions: Windows.Win32.Foundation.BOOL
    DvbEit: Windows.Win32.Media.DirectShow.Tv.DVB_EIT_FILTER_OPTIONS
    _pack_ = 1
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        bVersion1Bytes: Byte * 124
        class _Anonymous_e__Struct(EasyCastStructure):
            bVersionNumber: Byte
            wFilterSize: UInt16
            fUseRawFilteringBits: Windows.Win32.Foundation.BOOL
            Filter: Byte * 16
            Mask: Byte * 16
            fSpecifyTableIdExtension: Windows.Win32.Foundation.BOOL
            TableIdExtension: UInt16
            fSpecifyVersion: Windows.Win32.Foundation.BOOL
            Version: Byte
            fSpecifySectionNumber: Windows.Win32.Foundation.BOOL
            SectionNumber: Byte
            fSpecifyCurrentNext: Windows.Win32.Foundation.BOOL
            fNext: Windows.Win32.Foundation.BOOL
            fSpecifyDsmccOptions: Windows.Win32.Foundation.BOOL
            Dsmcc: Windows.Win32.Media.DirectShow.Tv.DSMCC_FILTER_OPTIONS
            fSpecifyAtscOptions: Windows.Win32.Foundation.BOOL
            Atsc: Windows.Win32.Media.DirectShow.Tv.ATSC_FILTER_OPTIONS
            _pack_ = 1
class MPEG_BCS_DEMUX(EasyCastStructure):
    AVMGraphId: UInt32
    _pack_ = 1
class MPEG_CONTEXT(EasyCastStructure):
    Type: Windows.Win32.Media.DirectShow.Tv.MPEG_CONTEXT_TYPE
    U: _U_e__Union
    _pack_ = 1
    class _U_e__Union(EasyCastUnion):
        Demux: Windows.Win32.Media.DirectShow.Tv.MPEG_BCS_DEMUX
        Winsock: Windows.Win32.Media.DirectShow.Tv.MPEG_WINSOCK
MPEG_CONTEXT_TYPE = Int32
MPEG_CONTEXT_BCS_DEMUX: MPEG_CONTEXT_TYPE = 0
MPEG_CONTEXT_WINSOCK: MPEG_CONTEXT_TYPE = 1
MPEG_CURRENT_NEXT_BIT = Int32
MPEG_SECTION_IS_NEXT: MPEG_CURRENT_NEXT_BIT = 0
MPEG_SECTION_IS_CURRENT: MPEG_CURRENT_NEXT_BIT = 1
class MPEG_DATE(EasyCastStructure):
    Date: Byte
    Month: Byte
    Year: UInt16
    _pack_ = 1
class MPEG_DATE_AND_TIME(EasyCastStructure):
    D: Windows.Win32.Media.DirectShow.Tv.MPEG_DATE
    T: Windows.Win32.Media.DirectShow.Tv.MPEG_TIME
    _pack_ = 1
class MPEG_HEADER_BITS(EasyCastStructure):
    _bitfield: UInt16
    _pack_ = 1
class MPEG_HEADER_BITS_MIDL(EasyCastStructure):
    Bits: UInt16
    _pack_ = 1
class MPEG_HEADER_VERSION_BITS(EasyCastStructure):
    _bitfield: Byte
class MPEG_HEADER_VERSION_BITS_MIDL(EasyCastStructure):
    Bits: Byte
class MPEG_PACKET_LIST(EasyCastStructure):
    wPacketCount: UInt16
    PacketList: POINTER(Windows.Win32.Media.DirectShow.Tv.MPEG_RQST_PACKET_head) * 1
    _pack_ = 1
MPEG_REQUEST_TYPE = Int32
MPEG_RQST_UNKNOWN: MPEG_REQUEST_TYPE = 0
MPEG_RQST_GET_SECTION: MPEG_REQUEST_TYPE = 1
MPEG_RQST_GET_SECTION_ASYNC: MPEG_REQUEST_TYPE = 2
MPEG_RQST_GET_TABLE: MPEG_REQUEST_TYPE = 3
MPEG_RQST_GET_TABLE_ASYNC: MPEG_REQUEST_TYPE = 4
MPEG_RQST_GET_SECTIONS_STREAM: MPEG_REQUEST_TYPE = 5
MPEG_RQST_GET_PES_STREAM: MPEG_REQUEST_TYPE = 6
MPEG_RQST_GET_TS_STREAM: MPEG_REQUEST_TYPE = 7
MPEG_RQST_START_MPE_STREAM: MPEG_REQUEST_TYPE = 8
class MPEG_RQST_PACKET(EasyCastStructure):
    dwLength: UInt32
    pSection: POINTER(Windows.Win32.Media.DirectShow.Tv.SECTION_head)
    _pack_ = 1
class MPEG_SERVICE_REQUEST(EasyCastStructure):
    Type: Windows.Win32.Media.DirectShow.Tv.MPEG_REQUEST_TYPE
    Context: Windows.Win32.Media.DirectShow.Tv.MPEG_CONTEXT
    Pid: UInt16
    TableId: Byte
    Filter: Windows.Win32.Media.DirectShow.Tv.MPEG2_FILTER
    Flags: UInt32
    _pack_ = 1
class MPEG_SERVICE_RESPONSE(EasyCastStructure):
    IPAddress: UInt32
    Port: UInt16
    _pack_ = 1
class MPEG_STREAM_BUFFER(EasyCastStructure):
    hr: Windows.Win32.Foundation.HRESULT
    dwDataBufferSize: UInt32
    dwSizeOfDataRead: UInt32
    pDataBuffer: POINTER(Byte)
    _pack_ = 1
class MPEG_STREAM_FILTER(EasyCastStructure):
    wPidValue: UInt16
    dwFilterSize: UInt32
    fCrcEnabled: Windows.Win32.Foundation.BOOL
    rgchFilter: Byte * 16
    rgchMask: Byte * 16
    _pack_ = 1
class MPEG_TIME(EasyCastStructure):
    Hours: Byte
    Minutes: Byte
    Seconds: Byte
    _pack_ = 1
class MPEG_WINSOCK(EasyCastStructure):
    AVMGraphId: UInt32
    _pack_ = 1
class MPE_ELEMENT(EasyCastStructure):
    pid: UInt16
    bComponentTag: Byte
    pNext: POINTER(Windows.Win32.Media.DirectShow.Tv.MPE_ELEMENT_head)
    _pack_ = 1
MSEventBinder = Guid('{577faa18-4518-445e-8f70-1473f8cf4ba4}')
MSVidAnalogCaptureToCCA = Guid('{942b7909-a28e-49a1-a207-34ebcbcb4b3b}')
MSVidAnalogCaptureToDataServices = Guid('{c5702cd6-9b79-11d3-b654-00c04f79498e}')
MSVidAnalogCaptureToOverlayMixer = Guid('{e18af75a-08af-11d3-b64a-00c04f79498e}')
MSVidAnalogCaptureToStreamBufferSink = Guid('{9f50e8b1-9530-4ddc-825e-1af81d47aed6}')
MSVidAnalogCaptureToXDS = Guid('{3540d440-5b1d-49cb-821a-e84b8cf065a7}')
MSVidAnalogTVToEncoder = Guid('{28953661-0231-41db-8986-21ff4388ee9b}')
MSVidAnalogTunerDevice = Guid('{1c15d484-911d-11d2-b632-00c04f79498e}')
MSVidAudioRenderer = Guid('{37b03544-a4c8-11d2-b634-00c04f79498e}')
MSVidAudioRendererDevices = Guid('{c5702ccf-9b79-11d3-b654-00c04f79498e}')
MSVidBDATunerDevice = Guid('{a2e3074e-6c3d-11d3-b653-00c04f79498e}')
MSVidCCA = Guid('{86151827-e47b-45ee-8421-d10e6e690979}')
MSVidCCAToStreamBufferSink = Guid('{3ef76d68-8661-4843-8b8f-c37163d8c9ce}')
MSVidCCService = Int32
MSVidCCService_None: MSVidCCService = 0
MSVidCCService_Caption1: MSVidCCService = 1
MSVidCCService_Caption2: MSVidCCService = 2
MSVidCCService_Text1: MSVidCCService = 3
MSVidCCService_Text2: MSVidCCService = 4
MSVidCCService_XDS: MSVidCCService = 5
MSVidCCToAR = Guid('{d76334ca-d89e-4baf-86ab-ddb59372afc2}')
MSVidCCToVMR = Guid('{c4bf2784-ae00-41ba-9828-9c953bd3c54a}')
MSVidClosedCaptioning = Guid('{7f9cb14d-48e4-43b6-9346-1aebc39c64d3}')
MSVidClosedCaptioningSI = Guid('{92ed88bf-879e-448f-b6b6-a385bceb846d}')
MSVidCtl = Guid('{b0edf163-910a-11d2-b632-00c04f79498e}')
MSVidCtlButtonstate = Int32
MSVIDCTL_LEFT_BUTTON: MSVidCtlButtonstate = 1
MSVIDCTL_RIGHT_BUTTON: MSVidCtlButtonstate = 2
MSVIDCTL_MIDDLE_BUTTON: MSVidCtlButtonstate = 4
MSVIDCTL_X_BUTTON1: MSVidCtlButtonstate = 8
MSVIDCTL_X_BUTTON2: MSVidCtlButtonstate = 16
MSVIDCTL_SHIFT: MSVidCtlButtonstate = 1
MSVIDCTL_CTRL: MSVidCtlButtonstate = 2
MSVIDCTL_ALT: MSVidCtlButtonstate = 4
MSVidCtlStateList = Int32
STATE_UNBUILT: MSVidCtlStateList = -1
STATE_STOP: MSVidCtlStateList = 0
STATE_PAUSE: MSVidCtlStateList = 1
STATE_PLAY: MSVidCtlStateList = 2
MSVidDataServices = Guid('{334125c0-77e5-11d3-b653-00c04f79498e}')
MSVidDataServicesToStreamBufferSink = Guid('{38f03426-e83b-4e68-b65b-dcae73304838}')
MSVidDataServicesToXDS = Guid('{0429ec6e-1144-4bed-b88b-2fb9899a4a3d}')
MSVidDevice = Guid('{6e40476f-9c49-4c3e-8bb9-8587958eff74}')
MSVidDevice2 = Guid('{30997f7d-b3b5-4a1c-983a-1fe8098cb77d}')
MSVidDigitalCaptureToCCA = Guid('{73d14237-b9db-4efa-a6dd-84350421fb2f}')
MSVidDigitalCaptureToITV = Guid('{5d8e73f7-4989-4ac8-8a98-39ba0d325302}')
MSVidDigitalCaptureToStreamBufferSink = Guid('{abe40035-27c3-4a2f-8153-6624471608af}')
MSVidEVR = Guid('{c45268a2-fa81-4e19-b1e3-72edbd60aeda}')
MSVidEncoder = Guid('{bb530c63-d9df-4b49-9439-63453962e598}')
MSVidEncoderToStreamBufferSink = Guid('{a0b9b497-afbc-45ad-a8a6-9b077c40d4f2}')
MSVidFeature = Guid('{7748530b-c08a-47ea-b24c-be8695ff405f}')
MSVidFeatures = Guid('{c5702cd0-9b79-11d3-b654-00c04f79498e}')
MSVidFilePlaybackDevice = Guid('{37b0353c-a4c8-11d2-b634-00c04f79498e}')
MSVidFilePlaybackToAudioRenderer = Guid('{cc23f537-18d4-4ece-93bd-207a84726979}')
MSVidFilePlaybackToVideoRenderer = Guid('{b401c5eb-8457-427f-84ea-a4d2363364b0}')
MSVidGenericComposite = Guid('{2764bce5-cc39-11d2-b639-00c04f79498e}')
MSVidGenericSink = Guid('{4a5869cf-929d-4040-ae03-fcafc5b9cd42}')
MSVidITVCapture = Guid('{5740a302-ef0b-45ce-bf3b-4470a14a8980}')
MSVidITVPlayback = Guid('{9e797ed0-5253-4243-a9b7-bd06c58f8ef3}')
MSVidITVToStreamBufferSink = Guid('{92b94828-1af7-4e6e-9ebf-770657f77af5}')
MSVidInputDevice = Guid('{ac1972f2-138a-4ca3-90da-ae51112eda28}')
MSVidInputDevices = Guid('{c5702ccc-9b79-11d3-b654-00c04f79498e}')
MSVidMPEG2DecoderToClosedCaptioning = Guid('{6ad28ee1-5002-4e71-aaf7-bd077907b1a4}')
MSVidOutput = Guid('{87eb890d-03ad-4e9d-9866-376e5ec572ed}')
MSVidOutputDevices = Guid('{c5702ccd-9b79-11d3-b654-00c04f79498e}')
MSVidRect = Guid('{cb4276e6-7d5f-4cf1-9727-629c5e6db6ae}')
MSVidSBESourceToCC = Guid('{9193a8f9-0cba-400e-aa97-eb4709164576}')
MSVidSBESourceToGenericSink = Guid('{991da7e5-953f-435b-be5e-b92a05edfc42}')
MSVidSBESourceToITV = Guid('{2291478c-5ee3-4bef-ab5d-b5ff2cf58352}')
MSVidSegmentType = Int32
MSVidSEG_SOURCE: MSVidSegmentType = 0
MSVidSEG_XFORM: MSVidSegmentType = 1
MSVidSEG_DEST: MSVidSegmentType = 2
MSVidSinkStreams = Int32
MSVidSink_Video: MSVidSinkStreams = 1
MSVidSink_Audio: MSVidSinkStreams = 2
MSVidSink_Other: MSVidSinkStreams = 4
MSVidStreamBufferRecordingControl = Guid('{caafdd83-cefc-4e3d-ba03-175f17a24f91}')
MSVidStreamBufferSink = Guid('{9e77aac4-35e5-42a1-bdc2-8f3ff399847c}')
MSVidStreamBufferSource = Guid('{ad8e510d-217f-409b-8076-29c5e73b98e8}')
MSVidStreamBufferSourceToVideoRenderer = Guid('{3c4708dc-b181-46a8-8da8-4ab0371758cd}')
MSVidStreamBufferV2Source = Guid('{fd351ea1-4173-4af4-821d-80d4ae979048}')
MSVidVMR9 = Guid('{24dc3975-09bf-4231-8655-3ee71f43837d}')
MSVidVideoInputDevice = Guid('{95f4820b-bb3a-4e2d-bc64-5b817bc2c30e}')
MSVidVideoPlaybackDevice = Guid('{1990d634-1a5e-4071-a34a-53aaffce9f36}')
MSVidVideoRenderer = Guid('{37b03543-a4c8-11d2-b634-00c04f79498e}')
MSVidVideoRendererDevices = Guid('{c5702cce-9b79-11d3-b654-00c04f79498e}')
MSVidWebDVD = Guid('{011b3619-fe63-4814-8a84-15a194ce9ce3}')
MSVidWebDVDAdm = Guid('{fa7c375b-66a7-4280-879d-fd459c84bb02}')
MSVidWebDVDToAudioRenderer = Guid('{8d04238e-9fd1-41c6-8de3-9e1ee309e935}')
MSVidWebDVDToVideoRenderer = Guid('{267db0b3-55e3-4902-949b-df8f5cec0191}')
MSVidXDS = Guid('{0149eedf-d08f-4142-8d73-d23903d21e90}')
MSViddispidList = Int32
MSViddispidList_dispidInputs: MSViddispidList = 0
MSViddispidList_dispidOutputs: MSViddispidList = 1
MSViddispidList_dispid_Inputs: MSViddispidList = 2
MSViddispidList_dispid_Outputs: MSViddispidList = 3
MSViddispidList_dispidVideoRenderers: MSViddispidList = 4
MSViddispidList_dispidAudioRenderers: MSViddispidList = 5
MSViddispidList_dispidFeatures: MSViddispidList = 6
MSViddispidList_dispidInput: MSViddispidList = 7
MSViddispidList_dispidOutput: MSViddispidList = 8
MSViddispidList_dispidVideoRenderer: MSViddispidList = 9
MSViddispidList_dispidAudioRenderer: MSViddispidList = 10
MSViddispidList_dispidSelectedFeatures: MSViddispidList = 11
MSViddispidList_dispidView: MSViddispidList = 12
MSViddispidList_dispidBuild: MSViddispidList = 13
MSViddispidList_dispidPause: MSViddispidList = 14
MSViddispidList_dispidRun: MSViddispidList = 15
MSViddispidList_dispidStop: MSViddispidList = 16
MSViddispidList_dispidDecompose: MSViddispidList = 17
MSViddispidList_dispidDisplaySize: MSViddispidList = 18
MSViddispidList_dispidMaintainAspectRatio: MSViddispidList = 19
MSViddispidList_dispidColorKey: MSViddispidList = 20
MSViddispidList_dispidStateChange: MSViddispidList = 21
MSViddispidList_dispidgetState: MSViddispidList = 22
MSViddispidList_dispidunbind: MSViddispidList = 23
MSViddispidList_dispidbind: MSViddispidList = 24
MSViddispidList_dispidDisableVideo: MSViddispidList = 25
MSViddispidList_dispidDisableAudio: MSViddispidList = 26
MSViddispidList_dispidViewNext: MSViddispidList = 27
MSViddispidList_dispidServiceP: MSViddispidList = 28
Mpeg2Data = Guid('{c666e115-bb62-4027-a113-82d643fe2d99}')
Mpeg2DataLib = Guid('{dbaf6c1b-b6a4-4898-ae65-204f0d9509a1}')
Mpeg2Stream = Guid('{f91d96c7-8509-4d0b-ab26-a0dd10904bb7}')
class Mpeg2TableSampleHdr(EasyCastStructure):
    SectionCount: Byte
    Reserved: Byte * 3
    SectionOffsets: Int32 * 1
    _pack_ = 1
class PBDAParentalControl(EasyCastStructure):
    rating_system_count: UInt32
    rating_systems: POINTER(Windows.Win32.Media.DirectShow.Tv.RATING_SYSTEM_head)
    _pack_ = 1
PBDA_ALWAYS_TUNE_IN_MUX = Guid('{1e1d7141-583f-4ac2-b019-1f430eda0f4c}')
class PBDA_TAG_ATTRIBUTE(EasyCastStructure):
    TableUUId: Guid
    TableId: Byte
    VersionNo: UInt16
    TableDataSize: UInt32
    TableData: Byte * 1
class PIC_SEQ_SAMPLE(EasyCastStructure):
    _bitfield: UInt32
class PIDListSpanningEvent(EasyCastStructure):
    wPIDCount: UInt16
    pulPIDs: UInt32 * 1
class PID_BITS(EasyCastStructure):
    _bitfield: UInt16
    _pack_ = 1
class PID_BITS_MIDL(EasyCastStructure):
    Bits: UInt16
    _pack_ = 1
PINNAME_BDA_ANALOG_AUDIO = Guid('{d28a580a-9b1f-4b0c-9c33-9bf0a8ea636b}')
PINNAME_BDA_ANALOG_VIDEO = Guid('{5c0c8281-5667-486c-8482-63e31f01a6e9}')
PINNAME_BDA_FM_RADIO = Guid('{d2855fed-b2d3-4eeb-9bd0-193436a2f890}')
PINNAME_BDA_IF_PIN = Guid('{1a9d4a42-f3cd-48a1-9aea-71de133cbe14}')
PINNAME_BDA_OPENCABLE_PSIP_PIN = Guid('{297bb104-e5c9-4ace-b123-95c3cbb24d4f}')
PINNAME_BDA_TRANSPORT = Guid('{78216a81-cfa8-493e-9711-36a61c08bd9d}')
PINNAME_IPSINK_INPUT = Guid('{3fdffa70-ac9a-11d2-8f17-00c04f7971e2}')
PINNAME_MPE = Guid('{c1b06d73-1dbb-11d3-8f46-00c04f7971e2}')
PersistTuneXmlUtility = Guid('{e77026b0-b97f-4cbb-b7fb-f4f03ad69f11}')
PositionModeList = Int32
PositionModeList_FrameMode: PositionModeList = 0
PositionModeList_TenthsSecondsMode: PositionModeList = 1
class ProgramElement(EasyCastStructure):
    wProgramNumber: UInt16
    wProgramMapPID: UInt16
ProtType = Int32
PROT_COPY_FREE: ProtType = 1
PROT_COPY_ONCE: ProtType = 2
PROT_COPY_NEVER: ProtType = 3
PROT_COPY_NEVER_REALLY: ProtType = 4
PROT_COPY_NO_MORE: ProtType = 5
PROT_COPY_FREE_CIT: ProtType = 6
PROT_COPY_BF: ProtType = 7
PROT_COPY_CN_RECORDING_STOP: ProtType = 8
PROT_COPY_FREE_SECURE: ProtType = 9
PROT_COPY_INVALID: ProtType = 50
class RATING_ATTRIBUTE(EasyCastStructure):
    rating_attribute_id: UInt32
    rating_attribute_value: UInt32
    _pack_ = 1
class RATING_INFO(EasyCastStructure):
    rating_system_count: UInt32
    lpratingsystem: POINTER(Windows.Win32.Media.DirectShow.Tv.RATING_SYSTEM_head)
    _pack_ = 1
class RATING_SYSTEM(EasyCastStructure):
    rating_system_id: Guid
    _bitfield: Byte
    country_code: Byte * 3
    rating_attribute_count: UInt32
    lpratingattrib: POINTER(Windows.Win32.Media.DirectShow.Tv.RATING_ATTRIBUTE_head)
    _pack_ = 1
RECORDING_TYPE = Int32
RECORDING_TYPE_CONTENT: RECORDING_TYPE = 0
RECORDING_TYPE_REFERENCE: RECORDING_TYPE = 1
RecordingType = Int32
CONTENT: RecordingType = 0
REFERENCE: RecordingType = 1
RevokedComponent = Int32
REVOKED_COPP: RevokedComponent = 0
REVOKED_SAC: RevokedComponent = 1
REVOKED_APP_STUB: RevokedComponent = 2
REVOKED_SECURE_PIPELINE: RevokedComponent = 3
REVOKED_MAX_TYPES: RevokedComponent = 4
class SAMPLE_LIVE_STREAM_TIME(EasyCastStructure):
    qwStreamTime: UInt64
    qwLiveTime: UInt64
class SAMPLE_SEQ_OFFSET(EasyCastStructure):
    _bitfield: UInt32
class SBE2_STREAM_DESC(EasyCastStructure):
    Version: UInt32
    StreamId: UInt32
    Default: UInt32
    Reserved: UInt32
class SBE_PIN_DATA(EasyCastStructure):
    cDataBytes: UInt64
    cSamplesProcessed: UInt64
    cDiscontinuities: UInt64
    cSyncPoints: UInt64
    cTimestamps: UInt64
class SECTION(EasyCastStructure):
    TableId: Byte
    Header: _Header_e__Union
    SectionData: Byte * 1
    _pack_ = 1
    class _Header_e__Union(EasyCastUnion):
        S: Windows.Win32.Media.DirectShow.Tv.MPEG_HEADER_BITS_MIDL
        W: UInt16
        _pack_ = 1
class STREAMBUFFER_ATTRIBUTE(EasyCastStructure):
    pszName: Windows.Win32.Foundation.PWSTR
    StreamBufferAttributeType: Windows.Win32.Media.DirectShow.Tv.STREAMBUFFER_ATTR_DATATYPE
    pbAttribute: POINTER(Byte)
    cbLength: UInt16
STREAMBUFFER_ATTR_DATATYPE = Int32
STREAMBUFFER_TYPE_DWORD: STREAMBUFFER_ATTR_DATATYPE = 0
STREAMBUFFER_TYPE_STRING: STREAMBUFFER_ATTR_DATATYPE = 1
STREAMBUFFER_TYPE_BINARY: STREAMBUFFER_ATTR_DATATYPE = 2
STREAMBUFFER_TYPE_BOOL: STREAMBUFFER_ATTR_DATATYPE = 3
STREAMBUFFER_TYPE_QWORD: STREAMBUFFER_ATTR_DATATYPE = 4
STREAMBUFFER_TYPE_WORD: STREAMBUFFER_ATTR_DATATYPE = 5
STREAMBUFFER_TYPE_GUID: STREAMBUFFER_ATTR_DATATYPE = 6
SectionList = Guid('{73da5d04-4347-45d3-a9dc-fae9ddbe558d}')
SegDispidList = Int32
SegDispidList_dispidName: SegDispidList = 0
SegDispidList_dispidStatus: SegDispidList = 1
SegDispidList_dispidDevImageSourceWidth: SegDispidList = 2
SegDispidList_dispidDevImageSourceHeight: SegDispidList = 3
SegDispidList_dispidDevCountryCode: SegDispidList = 4
SegDispidList_dispidDevOverScan: SegDispidList = 5
SegDispidList_dispidSegment: SegDispidList = 6
SegDispidList_dispidDevVolume: SegDispidList = 7
SegDispidList_dispidDevBalance: SegDispidList = 8
SegDispidList_dispidDevPower: SegDispidList = 9
SegDispidList_dispidTuneChan: SegDispidList = 10
SegDispidList_dispidDevVideoSubchannel: SegDispidList = 11
SegDispidList_dispidDevAudioSubchannel: SegDispidList = 12
SegDispidList_dispidChannelAvailable: SegDispidList = 13
SegDispidList_dispidDevVideoFrequency: SegDispidList = 14
SegDispidList_dispidDevAudioFrequency: SegDispidList = 15
SegDispidList_dispidCount: SegDispidList = 16
SegDispidList_dispidDevFileName: SegDispidList = 17
SegDispidList_dispidVisible: SegDispidList = 18
SegDispidList_dispidOwner: SegDispidList = 19
SegDispidList_dispidMessageDrain: SegDispidList = 20
SegDispidList_dispidViewable: SegDispidList = 21
SegDispidList_dispidDevView: SegDispidList = 22
SegDispidList_dispidKSCat: SegDispidList = 23
SegDispidList_dispidCLSID: SegDispidList = 24
SegDispidList_dispid_KSCat: SegDispidList = 25
SegDispidList_dispid_CLSID: SegDispidList = 26
SegDispidList_dispidTune: SegDispidList = 27
SegDispidList_dispidTS: SegDispidList = 28
SegDispidList_dispidDevSAP: SegDispidList = 29
SegDispidList_dispidClip: SegDispidList = 30
SegDispidList_dispidRequestedClipRect: SegDispidList = 31
SegDispidList_dispidClippedSourceRect: SegDispidList = 32
SegDispidList_dispidAvailableSourceRect: SegDispidList = 33
SegDispidList_dispidMediaPosition: SegDispidList = 34
SegDispidList_dispidDevRun: SegDispidList = 35
SegDispidList_dispidDevPause: SegDispidList = 36
SegDispidList_dispidDevStop: SegDispidList = 37
SegDispidList_dispidCCEnable: SegDispidList = 38
SegDispidList_dispidDevStep: SegDispidList = 39
SegDispidList_dispidDevCanStep: SegDispidList = 40
SegDispidList_dispidSourceSize: SegDispidList = 41
SegDispidList_dispid_playtitle: SegDispidList = 42
SegDispidList_dispid_playchapterintitle: SegDispidList = 43
SegDispidList_dispid_playchapter: SegDispidList = 44
SegDispidList_dispid_playchaptersautostop: SegDispidList = 45
SegDispidList_dispid_playattime: SegDispidList = 46
SegDispidList_dispid_playattimeintitle: SegDispidList = 47
SegDispidList_dispid_playperiodintitleautostop: SegDispidList = 48
SegDispidList_dispid_replaychapter: SegDispidList = 49
SegDispidList_dispid_playprevchapter: SegDispidList = 50
SegDispidList_dispid_playnextchapter: SegDispidList = 51
SegDispidList_dispid_playforwards: SegDispidList = 52
SegDispidList_dispid_playbackwards: SegDispidList = 53
SegDispidList_dispid_stilloff: SegDispidList = 54
SegDispidList_dispid_audiolanguage: SegDispidList = 55
SegDispidList_dispid_showmenu: SegDispidList = 56
SegDispidList_dispid_resume: SegDispidList = 57
SegDispidList_dispid_returnfromsubmenu: SegDispidList = 58
SegDispidList_dispid_buttonsavailable: SegDispidList = 59
SegDispidList_dispid_currentbutton: SegDispidList = 60
SegDispidList_dispid_SelectAndActivateButton: SegDispidList = 61
SegDispidList_dispid_ActivateButton: SegDispidList = 62
SegDispidList_dispid_SelectRightButton: SegDispidList = 63
SegDispidList_dispid_SelectLeftButton: SegDispidList = 64
SegDispidList_dispid_SelectLowerButton: SegDispidList = 65
SegDispidList_dispid_SelectUpperButton: SegDispidList = 66
SegDispidList_dispid_ActivateAtPosition: SegDispidList = 67
SegDispidList_dispid_SelectAtPosition: SegDispidList = 68
SegDispidList_dispid_ButtonAtPosition: SegDispidList = 69
SegDispidList_dispid_NumberOfChapters: SegDispidList = 70
SegDispidList_dispid_TotalTitleTime: SegDispidList = 71
SegDispidList_dispid_TitlesAvailable: SegDispidList = 72
SegDispidList_dispid_VolumesAvailable: SegDispidList = 73
SegDispidList_dispid_CurrentVolume: SegDispidList = 74
SegDispidList_dispid_CurrentDiscSide: SegDispidList = 75
SegDispidList_dispid_CurrentDomain: SegDispidList = 76
SegDispidList_dispid_CurrentChapter: SegDispidList = 77
SegDispidList_dispid_CurrentTitle: SegDispidList = 78
SegDispidList_dispid_CurrentTime: SegDispidList = 79
SegDispidList_dispid_FramesPerSecond: SegDispidList = 80
SegDispidList_dispid_DVDTimeCode2bstr: SegDispidList = 81
SegDispidList_dispid_DVDDirectory: SegDispidList = 82
SegDispidList_dispid_IsSubpictureStreamEnabled: SegDispidList = 83
SegDispidList_dispid_IsAudioStreamEnabled: SegDispidList = 84
SegDispidList_dispid_CurrentSubpictureStream: SegDispidList = 85
SegDispidList_dispid_SubpictureLanguage: SegDispidList = 86
SegDispidList_dispid_CurrentAudioStream: SegDispidList = 87
SegDispidList_dispid_AudioStreamsAvailable: SegDispidList = 88
SegDispidList_dispid_AnglesAvailable: SegDispidList = 89
SegDispidList_dispid_CurrentAngle: SegDispidList = 90
SegDispidList_dispid_CCActive: SegDispidList = 91
SegDispidList_dispid_CurrentCCService: SegDispidList = 92
SegDispidList_dispid_SubpictureStreamsAvailable: SegDispidList = 93
SegDispidList_dispid_SubpictureOn: SegDispidList = 94
SegDispidList_dispid_DVDUniqueID: SegDispidList = 95
SegDispidList_dispid_EnableResetOnStop: SegDispidList = 96
SegDispidList_dispid_AcceptParentalLevelChange: SegDispidList = 97
SegDispidList_dispid_NotifyParentalLevelChange: SegDispidList = 98
SegDispidList_dispid_SelectParentalCountry: SegDispidList = 99
SegDispidList_dispid_SelectParentalLevel: SegDispidList = 100
SegDispidList_dispid_TitleParentalLevels: SegDispidList = 101
SegDispidList_dispid_PlayerParentalCountry: SegDispidList = 102
SegDispidList_dispid_PlayerParentalLevel: SegDispidList = 103
SegDispidList_dispid_Eject: SegDispidList = 104
SegDispidList_dispid_UOPValid: SegDispidList = 105
SegDispidList_dispid_SPRM: SegDispidList = 106
SegDispidList_dispid_GPRM: SegDispidList = 107
SegDispidList_dispid_DVDTextStringType: SegDispidList = 108
SegDispidList_dispid_DVDTextString: SegDispidList = 109
SegDispidList_dispid_DVDTextNumberOfStrings: SegDispidList = 110
SegDispidList_dispid_DVDTextNumberOfLanguages: SegDispidList = 111
SegDispidList_dispid_DVDTextLanguageLCID: SegDispidList = 112
SegDispidList_dispid_RegionChange: SegDispidList = 113
SegDispidList_dispid_DVDAdm: SegDispidList = 114
SegDispidList_dispid_DeleteBookmark: SegDispidList = 115
SegDispidList_dispid_RestoreBookmark: SegDispidList = 116
SegDispidList_dispid_SaveBookmark: SegDispidList = 117
SegDispidList_dispid_SelectDefaultAudioLanguage: SegDispidList = 118
SegDispidList_dispid_SelectDefaultSubpictureLanguage: SegDispidList = 119
SegDispidList_dispid_PreferredSubpictureStream: SegDispidList = 120
SegDispidList_dispid_DefaultMenuLanguage: SegDispidList = 121
SegDispidList_dispid_DefaultSubpictureLanguage: SegDispidList = 122
SegDispidList_dispid_DefaultAudioLanguage: SegDispidList = 123
SegDispidList_dispid_DefaultSubpictureLanguageExt: SegDispidList = 124
SegDispidList_dispid_DefaultAudioLanguageExt: SegDispidList = 125
SegDispidList_dispid_LanguageFromLCID: SegDispidList = 126
SegDispidList_dispid_KaraokeAudioPresentationMode: SegDispidList = 127
SegDispidList_dispid_KaraokeChannelContent: SegDispidList = 128
SegDispidList_dispid_KaraokeChannelAssignment: SegDispidList = 129
SegDispidList_dispid_RestorePreferredSettings: SegDispidList = 130
SegDispidList_dispid_ButtonRect: SegDispidList = 131
SegDispidList_dispid_DVDScreenInMouseCoordinates: SegDispidList = 132
SegDispidList_dispid_CustomCompositorClass: SegDispidList = 133
SegDispidList_dispidCustomCompositorClass: SegDispidList = 134
SegDispidList_dispid_CustomCompositor: SegDispidList = 135
SegDispidList_dispidMixerBitmap: SegDispidList = 136
SegDispidList_dispid_MixerBitmap: SegDispidList = 137
SegDispidList_dispidMixerBitmapOpacity: SegDispidList = 138
SegDispidList_dispidMixerBitmapRect: SegDispidList = 139
SegDispidList_dispidSetupMixerBitmap: SegDispidList = 140
SegDispidList_dispidUsingOverlay: SegDispidList = 141
SegDispidList_dispidDisplayChange: SegDispidList = 142
SegDispidList_dispidRePaint: SegDispidList = 143
SegDispidList_dispid_IsEqualDevice: SegDispidList = 144
SegDispidList_dispidrate: SegDispidList = 145
SegDispidList_dispidposition: SegDispidList = 146
SegDispidList_dispidpositionmode: SegDispidList = 147
SegDispidList_dispidlength: SegDispidList = 148
SegDispidList_dispidChangePassword: SegDispidList = 149
SegDispidList_dispidSaveParentalLevel: SegDispidList = 150
SegDispidList_dispidSaveParentalCountry: SegDispidList = 151
SegDispidList_dispidConfirmPassword: SegDispidList = 152
SegDispidList_dispidGetParentalLevel: SegDispidList = 153
SegDispidList_dispidGetParentalCountry: SegDispidList = 154
SegDispidList_dispidDefaultAudioLCID: SegDispidList = 155
SegDispidList_dispidDefaultSubpictureLCID: SegDispidList = 156
SegDispidList_dispidDefaultMenuLCID: SegDispidList = 157
SegDispidList_dispidBookmarkOnStop: SegDispidList = 158
SegDispidList_dispidMaxVidRect: SegDispidList = 159
SegDispidList_dispidMinVidRect: SegDispidList = 160
SegDispidList_dispidCapture: SegDispidList = 161
SegDispidList_dispid_DecimateInput: SegDispidList = 162
SegDispidList_dispidAlloctor: SegDispidList = 163
SegDispidList_dispid_Allocator: SegDispidList = 164
SegDispidList_dispidAllocPresentID: SegDispidList = 165
SegDispidList_dispidSetAllocator: SegDispidList = 166
SegDispidList_dispid_SetAllocator: SegDispidList = 167
SegDispidList_dispidStreamBufferSinkName: SegDispidList = 168
SegDispidList_dispidStreamBufferSourceName: SegDispidList = 169
SegDispidList_dispidStreamBufferContentRecording: SegDispidList = 170
SegDispidList_dispidStreamBufferReferenceRecording: SegDispidList = 171
SegDispidList_dispidstarttime: SegDispidList = 172
SegDispidList_dispidstoptime: SegDispidList = 173
SegDispidList_dispidrecordingstopped: SegDispidList = 174
SegDispidList_dispidrecordingstarted: SegDispidList = 175
SegDispidList_dispidNameSetLock: SegDispidList = 176
SegDispidList_dispidrecordingtype: SegDispidList = 177
SegDispidList_dispidstart: SegDispidList = 178
SegDispidList_dispidRecordingAttribute: SegDispidList = 179
SegDispidList_dispid_RecordingAttribute: SegDispidList = 180
SegDispidList_dispidSBEConfigure: SegDispidList = 181
SegDispidList_dispid_CurrentRatings: SegDispidList = 182
SegDispidList_dispid_MaxRatingsLevel: SegDispidList = 183
SegDispidList_dispid_audioencoderint: SegDispidList = 184
SegDispidList_dispid_videoencoderint: SegDispidList = 185
SegDispidList_dispidService: SegDispidList = 186
SegDispidList_dispid_BlockUnrated: SegDispidList = 187
SegDispidList_dispid_UnratedDelay: SegDispidList = 188
SegDispidList_dispid_SuppressEffects: SegDispidList = 189
SegDispidList_dispidsbesource: SegDispidList = 190
SegDispidList_dispidSetSinkFilter: SegDispidList = 191
SegDispidList_dispid_SinkStreams: SegDispidList = 192
SegDispidList_dispidTVFormats: SegDispidList = 193
SegDispidList_dispidModes: SegDispidList = 194
SegDispidList_dispidAuxInputs: SegDispidList = 195
SegDispidList_dispidTeleTextFilter: SegDispidList = 196
SegDispidList_dispid_channelchangeint: SegDispidList = 197
SegDispidList_dispidUnlockProfile: SegDispidList = 198
SegDispidList_dispid_AddFilter: SegDispidList = 199
SegDispidList_dispidSetMinSeek: SegDispidList = 200
SegDispidList_dispidRateEx: SegDispidList = 201
SegDispidList_dispidaudiocounter: SegDispidList = 202
SegDispidList_dispidvideocounter: SegDispidList = 203
SegDispidList_dispidcccounter: SegDispidList = 204
SegDispidList_dispidwstcounter: SegDispidList = 205
SegDispidList_dispid_audiocounter: SegDispidList = 206
SegDispidList_dispid_videocounter: SegDispidList = 207
SegDispidList_dispid_cccounter: SegDispidList = 208
SegDispidList_dispid_wstcounter: SegDispidList = 209
SegDispidList_dispidaudioanalysis: SegDispidList = 210
SegDispidList_dispidvideoanalysis: SegDispidList = 211
SegDispidList_dispiddataanalysis: SegDispidList = 212
SegDispidList_dispidaudio_analysis: SegDispidList = 213
SegDispidList_dispidvideo_analysis: SegDispidList = 214
SegDispidList_dispiddata_analysis: SegDispidList = 215
SegDispidList_dispid_resetFilterList: SegDispidList = 216
SegDispidList_dispidDevicePath: SegDispidList = 217
SegDispidList_dispid_SourceFilter: SegDispidList = 218
SegDispidList_dispid__SourceFilter: SegDispidList = 219
SegDispidList_dispidUserEvent: SegDispidList = 220
SegDispidList_dispid_Bookmark: SegDispidList = 221
SegDispidList_LastReservedDeviceDispid: SegDispidList = 16383
SegEventidList = Int32
SegEventidList_eventidStateChange: SegEventidList = 0
SegEventidList_eventidOnTuneChanged: SegEventidList = 1
SegEventidList_eventidEndOfMedia: SegEventidList = 2
SegEventidList_eventidDVDNotify: SegEventidList = 3
SegEventidList_eventidPlayForwards: SegEventidList = 4
SegEventidList_eventidPlayBackwards: SegEventidList = 5
SegEventidList_eventidShowMenu: SegEventidList = 6
SegEventidList_eventidResume: SegEventidList = 7
SegEventidList_eventidSelectOrActivateButton: SegEventidList = 8
SegEventidList_eventidStillOff: SegEventidList = 9
SegEventidList_eventidPauseOn: SegEventidList = 10
SegEventidList_eventidChangeCurrentAudioStream: SegEventidList = 11
SegEventidList_eventidChangeCurrentSubpictureStream: SegEventidList = 12
SegEventidList_eventidChangeCurrentAngle: SegEventidList = 13
SegEventidList_eventidPlayAtTimeInTitle: SegEventidList = 14
SegEventidList_eventidPlayAtTime: SegEventidList = 15
SegEventidList_eventidPlayChapterInTitle: SegEventidList = 16
SegEventidList_eventidPlayChapter: SegEventidList = 17
SegEventidList_eventidReplayChapter: SegEventidList = 18
SegEventidList_eventidPlayNextChapter: SegEventidList = 19
SegEventidList_eventidStop: SegEventidList = 20
SegEventidList_eventidReturnFromSubmenu: SegEventidList = 21
SegEventidList_eventidPlayTitle: SegEventidList = 22
SegEventidList_eventidPlayPrevChapter: SegEventidList = 23
SegEventidList_eventidChangeKaraokePresMode: SegEventidList = 24
SegEventidList_eventidChangeVideoPresMode: SegEventidList = 25
SegEventidList_eventidOverlayUnavailable: SegEventidList = 26
SegEventidList_eventidSinkCertificateFailure: SegEventidList = 27
SegEventidList_eventidSinkCertificateSuccess: SegEventidList = 28
SegEventidList_eventidSourceCertificateFailure: SegEventidList = 29
SegEventidList_eventidSourceCertificateSuccess: SegEventidList = 30
SegEventidList_eventidRatingsBlocked: SegEventidList = 31
SegEventidList_eventidRatingsUnlocked: SegEventidList = 32
SegEventidList_eventidRatingsChanged: SegEventidList = 33
SegEventidList_eventidWriteFailure: SegEventidList = 34
SegEventidList_eventidTimeHole: SegEventidList = 35
SegEventidList_eventidStaleDataRead: SegEventidList = 36
SegEventidList_eventidContentBecomingStale: SegEventidList = 37
SegEventidList_eventidStaleFileDeleted: SegEventidList = 38
SegEventidList_eventidEncryptionOn: SegEventidList = 39
SegEventidList_eventidEncryptionOff: SegEventidList = 40
SegEventidList_eventidRateChange: SegEventidList = 41
SegEventidList_eventidLicenseChange: SegEventidList = 42
SegEventidList_eventidCOPPBlocked: SegEventidList = 43
SegEventidList_eventidCOPPUnblocked: SegEventidList = 44
SegEventidList_dispidlicenseerrorcode: SegEventidList = 45
SegEventidList_eventidBroadcastEvent: SegEventidList = 46
SegEventidList_eventidBroadcastEventEx: SegEventidList = 47
SegEventidList_eventidContentPrimarilyAudio: SegEventidList = 48
SegEventidList_dispidAVDecAudioDualMonoEvent: SegEventidList = 49
SegEventidList_dispidAVAudioSampleRateEvent: SegEventidList = 50
SegEventidList_dispidAVAudioChannelConfigEvent: SegEventidList = 51
SegEventidList_dispidAVAudioChannelCountEvent: SegEventidList = 52
SegEventidList_dispidAVDecCommonMeanBitRateEvent: SegEventidList = 53
SegEventidList_dispidAVDDSurroundModeEvent: SegEventidList = 54
SegEventidList_dispidAVDecCommonInputFormatEvent: SegEventidList = 55
SegEventidList_dispidAVDecCommonOutputFormatEvent: SegEventidList = 56
SegEventidList_eventidWriteFailureClear: SegEventidList = 57
SegEventidList_LastReservedDeviceEvent: SegEventidList = 16383
SignalAndServiceStatusSpanningEvent_State = Int32
SignalAndServiceStatusSpanningEvent_None: SignalAndServiceStatusSpanningEvent_State = -1
SignalAndServiceStatusSpanningEvent_Clear: SignalAndServiceStatusSpanningEvent_State = 0
SignalAndServiceStatusSpanningEvent_NoTVSignal: SignalAndServiceStatusSpanningEvent_State = 1
SignalAndServiceStatusSpanningEvent_ServiceOffAir: SignalAndServiceStatusSpanningEvent_State = 2
SignalAndServiceStatusSpanningEvent_WeakTVSignal: SignalAndServiceStatusSpanningEvent_State = 3
SignalAndServiceStatusSpanningEvent_NoSubscription: SignalAndServiceStatusSpanningEvent_State = 4
SignalAndServiceStatusSpanningEvent_AllAVScrambled: SignalAndServiceStatusSpanningEvent_State = 5
SourceSizeList = Int32
SourceSizeList_sslFullSize: SourceSizeList = 0
SourceSizeList_sslClipByOverScan: SourceSizeList = 1
SourceSizeList_sslClipByClipRect: SourceSizeList = 2
class SpanningEventDescriptor(EasyCastStructure):
    wDataLen: UInt16
    wProgNumber: UInt16
    wSID: UInt16
    bDescriptor: Byte * 1
class SpanningEventEmmMessage(EasyCastStructure):
    bCAbroadcasterGroupId: Byte
    bMessageControl: Byte
    wServiceId: UInt16
    wTableIdExtension: UInt16
    bDeletionStatus: Byte
    bDisplayingDuration1: Byte
    bDisplayingDuration2: Byte
    bDisplayingDuration3: Byte
    bDisplayingCycle: Byte
    bFormatVersion: Byte
    bDisplayPosition: Byte
    wMessageLength: UInt16
    szMessageArea: Char * 1
SystemTuningSpaces = Guid('{d02aac50-027e-11d3-9d8e-00c04f72d980}')
class TID_EXTENSION(EasyCastStructure):
    wTidExt: UInt16
    wCount: UInt16
    _pack_ = 1
TIFLoad = Guid('{14eb8748-1753-4393-95ae-4f7e7a87aad6}')
class TRANSPORT_PROPERTIES(EasyCastStructure):
    PID: UInt32
    PCR: Int64
    Fields: _Fields_e__Union
    class _Fields_e__Union(EasyCastUnion):
        Others: _Others
        Value: Int64
        class _Others(EasyCastStructure):
            _bitfield: Int64
TuneRequest = Guid('{b46e0d38-ab35-4a06-a137-70576b01b39f}')
TunerMarshaler = Guid('{6438570b-0c08-4a25-9504-8012bb4d50cf}')
TuningSpace = Guid('{5ffdc5e6-b83a-4b55-b6e8-c69e765fe9db}')
class UDCR_TAG(EasyCastStructure):
    bVersion: Byte
    KID: Byte * 25
    ullBaseCounter: UInt64
    ullBaseCounterRange: UInt64
    fScrambled: Windows.Win32.Foundation.BOOL
    bStreamMark: Byte
    dwReserved1: UInt32
    dwReserved2: UInt32
VA_COLOR_PRIMARIES = Int32
VA_PRIMARIES_ITU_R_BT_709: VA_COLOR_PRIMARIES = 1
VA_PRIMARIES_UNSPECIFIED: VA_COLOR_PRIMARIES = 2
VA_PRIMARIES_ITU_R_BT_470_SYSTEM_M: VA_COLOR_PRIMARIES = 4
VA_PRIMARIES_ITU_R_BT_470_SYSTEM_B_G: VA_COLOR_PRIMARIES = 5
VA_PRIMARIES_SMPTE_170M: VA_COLOR_PRIMARIES = 6
VA_PRIMARIES_SMPTE_240M: VA_COLOR_PRIMARIES = 7
VA_PRIMARIES_H264_GENERIC_FILM: VA_COLOR_PRIMARIES = 8
VA_MATRIX_COEFFICIENTS = Int32
VA_MATRIX_COEFF_H264_RGB: VA_MATRIX_COEFFICIENTS = 0
VA_MATRIX_COEFF_ITU_R_BT_709: VA_MATRIX_COEFFICIENTS = 1
VA_MATRIX_COEFF_UNSPECIFIED: VA_MATRIX_COEFFICIENTS = 2
VA_MATRIX_COEFF_FCC: VA_MATRIX_COEFFICIENTS = 4
VA_MATRIX_COEFF_ITU_R_BT_470_SYSTEM_B_G: VA_MATRIX_COEFFICIENTS = 5
VA_MATRIX_COEFF_SMPTE_170M: VA_MATRIX_COEFFICIENTS = 6
VA_MATRIX_COEFF_SMPTE_240M: VA_MATRIX_COEFFICIENTS = 7
VA_MATRIX_COEFF_H264_YCgCo: VA_MATRIX_COEFFICIENTS = 8
class VA_OPTIONAL_VIDEO_PROPERTIES(EasyCastStructure):
    dwPictureHeight: UInt16
    dwPictureWidth: UInt16
    dwAspectRatioX: UInt16
    dwAspectRatioY: UInt16
    VAVideoFormat: Windows.Win32.Media.DirectShow.Tv.VA_VIDEO_FORMAT
    VAColorPrimaries: Windows.Win32.Media.DirectShow.Tv.VA_COLOR_PRIMARIES
    VATransferCharacteristics: Windows.Win32.Media.DirectShow.Tv.VA_TRANSFER_CHARACTERISTICS
    VAMatrixCoefficients: Windows.Win32.Media.DirectShow.Tv.VA_MATRIX_COEFFICIENTS
VA_TRANSFER_CHARACTERISTICS = Int32
VA_TRANSFER_CHARACTERISTICS_ITU_R_BT_709: VA_TRANSFER_CHARACTERISTICS = 1
VA_TRANSFER_CHARACTERISTICS_UNSPECIFIED: VA_TRANSFER_CHARACTERISTICS = 2
VA_TRANSFER_CHARACTERISTICS_ITU_R_BT_470_SYSTEM_M: VA_TRANSFER_CHARACTERISTICS = 4
VA_TRANSFER_CHARACTERISTICS_ITU_R_BT_470_SYSTEM_B_G: VA_TRANSFER_CHARACTERISTICS = 5
VA_TRANSFER_CHARACTERISTICS_SMPTE_170M: VA_TRANSFER_CHARACTERISTICS = 6
VA_TRANSFER_CHARACTERISTICS_SMPTE_240M: VA_TRANSFER_CHARACTERISTICS = 7
VA_TRANSFER_CHARACTERISTICS_LINEAR: VA_TRANSFER_CHARACTERISTICS = 8
VA_TRANSFER_CHARACTERISTICS_H264_LOG_100_TO_1: VA_TRANSFER_CHARACTERISTICS = 9
VA_TRANSFER_CHARACTERISTICS_H264_LOG_316_TO_1: VA_TRANSFER_CHARACTERISTICS = 10
VA_VIDEO_FORMAT = Int32
VA_VIDEO_COMPONENT: VA_VIDEO_FORMAT = 0
VA_VIDEO_PAL: VA_VIDEO_FORMAT = 1
VA_VIDEO_NTSC: VA_VIDEO_FORMAT = 2
VA_VIDEO_SECAM: VA_VIDEO_FORMAT = 3
VA_VIDEO_MAC: VA_VIDEO_FORMAT = 4
VA_VIDEO_UNSPECIFIED: VA_VIDEO_FORMAT = 5
class WMDRMProtectionInfo(EasyCastStructure):
    wszKID: UInt16 * 25
    qwCounter: UInt64
    qwIndex: UInt64
    bOffset: Byte
    _pack_ = 1
XDSCodec = Guid('{c4c4c4f3-0049-4e2b-98fb-9537f6ce516d}')
XDSToRat = Guid('{c5c5c5f0-3abc-11d6-b25b-00c04fa0c026}')
class _IMSVidCtlEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b0edf164-910a-11d2-b632-00c04f79498e}')
make_head(_module, 'ATSC_FILTER_OPTIONS')
make_head(_module, 'BDA_DEBUG_DATA')
make_head(_module, 'BDA_EVENT_DATA')
make_head(_module, 'BDA_TRANSPORT_INFO')
make_head(_module, 'BadSampleInfo')
make_head(_module, 'CAPTURE_STREAMTIME')
make_head(_module, 'ChannelChangeInfo')
make_head(_module, 'ChannelInfo')
make_head(_module, 'ChannelTypeInfo')
make_head(_module, 'DSHOW_STREAM_DESC')
make_head(_module, 'DSMCC_ELEMENT')
make_head(_module, 'DSMCC_FILTER_OPTIONS')
make_head(_module, 'DSMCC_SECTION')
make_head(_module, 'DVBScramblingControlSpanningEvent')
make_head(_module, 'DVB_EIT_FILTER_OPTIONS')
make_head(_module, 'DVR_STREAM_DESC')
make_head(_module, 'DualMonoInfo')
make_head(_module, 'DvbParentalRatingDescriptor')
make_head(_module, 'DvbParentalRatingParam')
make_head(_module, 'IATSCChannelTuneRequest')
make_head(_module, 'IATSCComponentType')
make_head(_module, 'IATSCLocator')
make_head(_module, 'IATSCLocator2')
make_head(_module, 'IATSCTuningSpace')
make_head(_module, 'IATSC_EIT')
make_head(_module, 'IATSC_ETT')
make_head(_module, 'IATSC_MGT')
make_head(_module, 'IATSC_STT')
make_head(_module, 'IATSC_VCT')
make_head(_module, 'IAnalogAudioComponentType')
make_head(_module, 'IAnalogLocator')
make_head(_module, 'IAnalogRadioTuningSpace')
make_head(_module, 'IAnalogRadioTuningSpace2')
make_head(_module, 'IAnalogTVTuningSpace')
make_head(_module, 'IAtscContentAdvisoryDescriptor')
make_head(_module, 'IAtscPsipParser')
make_head(_module, 'IAttributeGet')
make_head(_module, 'IAttributeSet')
make_head(_module, 'IAuxInTuningSpace')
make_head(_module, 'IAuxInTuningSpace2')
make_head(_module, 'IBDAComparable')
make_head(_module, 'IBDACreateTuneRequestEx')
make_head(_module, 'IBDA_TIF_REGISTRATION')
make_head(_module, 'ICAT')
make_head(_module, 'ICaptionServiceDescriptor')
make_head(_module, 'IChannelIDTuneRequest')
make_head(_module, 'IChannelTuneRequest')
make_head(_module, 'IComponent')
make_head(_module, 'IComponentType')
make_head(_module, 'IComponentTypes')
make_head(_module, 'IComponents')
make_head(_module, 'IComponentsOld')
make_head(_module, 'ICreatePropBagOnRegKey')
make_head(_module, 'IDTFilter')
make_head(_module, 'IDTFilter2')
make_head(_module, 'IDTFilter3')
make_head(_module, 'IDTFilterConfig')
make_head(_module, 'IDTFilterEvents')
make_head(_module, 'IDTFilterLicenseRenewal')
make_head(_module, 'IDVBCLocator')
make_head(_module, 'IDVBSLocator')
make_head(_module, 'IDVBSLocator2')
make_head(_module, 'IDVBSTuningSpace')
make_head(_module, 'IDVBTLocator')
make_head(_module, 'IDVBTLocator2')
make_head(_module, 'IDVBTuneRequest')
make_head(_module, 'IDVBTuningSpace')
make_head(_module, 'IDVBTuningSpace2')
make_head(_module, 'IDVB_BAT')
make_head(_module, 'IDVB_DIT')
make_head(_module, 'IDVB_EIT')
make_head(_module, 'IDVB_EIT2')
make_head(_module, 'IDVB_NIT')
make_head(_module, 'IDVB_RST')
make_head(_module, 'IDVB_SDT')
make_head(_module, 'IDVB_SIT')
make_head(_module, 'IDVB_ST')
make_head(_module, 'IDVB_TDT')
make_head(_module, 'IDVB_TOT')
make_head(_module, 'IDigitalCableLocator')
make_head(_module, 'IDigitalCableTuneRequest')
make_head(_module, 'IDigitalCableTuningSpace')
make_head(_module, 'IDigitalLocator')
make_head(_module, 'IDvbCableDeliverySystemDescriptor')
make_head(_module, 'IDvbComponentDescriptor')
make_head(_module, 'IDvbContentDescriptor')
make_head(_module, 'IDvbContentIdentifierDescriptor')
make_head(_module, 'IDvbDataBroadcastDescriptor')
make_head(_module, 'IDvbDataBroadcastIDDescriptor')
make_head(_module, 'IDvbDefaultAuthorityDescriptor')
make_head(_module, 'IDvbExtendedEventDescriptor')
make_head(_module, 'IDvbFrequencyListDescriptor')
make_head(_module, 'IDvbHDSimulcastLogicalChannelDescriptor')
make_head(_module, 'IDvbLinkageDescriptor')
make_head(_module, 'IDvbLogicalChannel2Descriptor')
make_head(_module, 'IDvbLogicalChannelDescriptor')
make_head(_module, 'IDvbLogicalChannelDescriptor2')
make_head(_module, 'IDvbMultilingualServiceNameDescriptor')
make_head(_module, 'IDvbNetworkNameDescriptor')
make_head(_module, 'IDvbParentalRatingDescriptor')
make_head(_module, 'IDvbPrivateDataSpecifierDescriptor')
make_head(_module, 'IDvbSatelliteDeliverySystemDescriptor')
make_head(_module, 'IDvbServiceAttributeDescriptor')
make_head(_module, 'IDvbServiceDescriptor')
make_head(_module, 'IDvbServiceDescriptor2')
make_head(_module, 'IDvbServiceListDescriptor')
make_head(_module, 'IDvbShortEventDescriptor')
make_head(_module, 'IDvbSiParser')
make_head(_module, 'IDvbSiParser2')
make_head(_module, 'IDvbSubtitlingDescriptor')
make_head(_module, 'IDvbTeletextDescriptor')
make_head(_module, 'IDvbTerrestrial2DeliverySystemDescriptor')
make_head(_module, 'IDvbTerrestrialDeliverySystemDescriptor')
make_head(_module, 'IESCloseMmiEvent')
make_head(_module, 'IESEventFactory')
make_head(_module, 'IESEventService')
make_head(_module, 'IESEventServiceConfiguration')
make_head(_module, 'IESFileExpiryDateEvent')
make_head(_module, 'IESIsdbCasResponseEvent')
make_head(_module, 'IESLicenseRenewalResultEvent')
make_head(_module, 'IESOpenMmiEvent')
make_head(_module, 'IESRequestTunerEvent')
make_head(_module, 'IESValueUpdatedEvent')
make_head(_module, 'IETFilter')
make_head(_module, 'IETFilterConfig')
make_head(_module, 'IETFilterEvents')
make_head(_module, 'IEnumComponentTypes')
make_head(_module, 'IEnumComponents')
make_head(_module, 'IEnumGuideDataProperties')
make_head(_module, 'IEnumMSVidGraphSegment')
make_head(_module, 'IEnumStreamBufferRecordingAttrib')
make_head(_module, 'IEnumTuneRequests')
make_head(_module, 'IEnumTuningSpaces')
make_head(_module, 'IEvalRat')
make_head(_module, 'IGenericDescriptor')
make_head(_module, 'IGenericDescriptor2')
make_head(_module, 'IGpnvsCommonBase')
make_head(_module, 'IGuideData')
make_head(_module, 'IGuideDataEvent')
make_head(_module, 'IGuideDataLoader')
make_head(_module, 'IGuideDataProperty')
make_head(_module, 'IISDBSLocator')
make_head(_module, 'IISDB_BIT')
make_head(_module, 'IISDB_CDT')
make_head(_module, 'IISDB_EMM')
make_head(_module, 'IISDB_LDT')
make_head(_module, 'IISDB_NBIT')
make_head(_module, 'IISDB_SDT')
make_head(_module, 'IISDB_SDTT')
make_head(_module, 'IIsdbAudioComponentDescriptor')
make_head(_module, 'IIsdbCAContractInformationDescriptor')
make_head(_module, 'IIsdbCADescriptor')
make_head(_module, 'IIsdbCAServiceDescriptor')
make_head(_module, 'IIsdbComponentGroupDescriptor')
make_head(_module, 'IIsdbDataContentDescriptor')
make_head(_module, 'IIsdbDigitalCopyControlDescriptor')
make_head(_module, 'IIsdbDownloadContentDescriptor')
make_head(_module, 'IIsdbEmergencyInformationDescriptor')
make_head(_module, 'IIsdbEventGroupDescriptor')
make_head(_module, 'IIsdbHierarchicalTransmissionDescriptor')
make_head(_module, 'IIsdbLogoTransmissionDescriptor')
make_head(_module, 'IIsdbSIParameterDescriptor')
make_head(_module, 'IIsdbSeriesDescriptor')
make_head(_module, 'IIsdbSiParser2')
make_head(_module, 'IIsdbTSInformationDescriptor')
make_head(_module, 'IIsdbTerrestrialDeliverySystemDescriptor')
make_head(_module, 'ILanguageComponentType')
make_head(_module, 'ILocator')
make_head(_module, 'IMPEG2Component')
make_head(_module, 'IMPEG2ComponentType')
make_head(_module, 'IMPEG2TuneRequest')
make_head(_module, 'IMPEG2TuneRequestFactory')
make_head(_module, 'IMPEG2TuneRequestSupport')
make_head(_module, 'IMPEG2_TIF_CONTROL')
make_head(_module, 'IMSEventBinder')
make_head(_module, 'IMSVidAnalogTuner')
make_head(_module, 'IMSVidAnalogTuner2')
make_head(_module, 'IMSVidAnalogTunerEvent')
make_head(_module, 'IMSVidAudioRenderer')
make_head(_module, 'IMSVidAudioRendererDevices')
make_head(_module, 'IMSVidAudioRendererEvent')
make_head(_module, 'IMSVidAudioRendererEvent2')
make_head(_module, 'IMSVidClosedCaptioning')
make_head(_module, 'IMSVidClosedCaptioning2')
make_head(_module, 'IMSVidClosedCaptioning3')
make_head(_module, 'IMSVidCompositionSegment')
make_head(_module, 'IMSVidCtl')
make_head(_module, 'IMSVidDataServices')
make_head(_module, 'IMSVidDataServicesEvent')
make_head(_module, 'IMSVidDevice')
make_head(_module, 'IMSVidDevice2')
make_head(_module, 'IMSVidDeviceEvent')
make_head(_module, 'IMSVidEVR')
make_head(_module, 'IMSVidEVREvent')
make_head(_module, 'IMSVidEncoder')
make_head(_module, 'IMSVidFeature')
make_head(_module, 'IMSVidFeatureEvent')
make_head(_module, 'IMSVidFeatures')
make_head(_module, 'IMSVidFilePlayback')
make_head(_module, 'IMSVidFilePlayback2')
make_head(_module, 'IMSVidFilePlaybackEvent')
make_head(_module, 'IMSVidGenericSink')
make_head(_module, 'IMSVidGenericSink2')
make_head(_module, 'IMSVidGraphSegment')
make_head(_module, 'IMSVidGraphSegmentContainer')
make_head(_module, 'IMSVidGraphSegmentUserInput')
make_head(_module, 'IMSVidInputDevice')
make_head(_module, 'IMSVidInputDeviceEvent')
make_head(_module, 'IMSVidInputDevices')
make_head(_module, 'IMSVidOutputDevice')
make_head(_module, 'IMSVidOutputDeviceEvent')
make_head(_module, 'IMSVidOutputDevices')
make_head(_module, 'IMSVidPlayback')
make_head(_module, 'IMSVidPlaybackEvent')
make_head(_module, 'IMSVidRect')
make_head(_module, 'IMSVidStreamBufferRecordingControl')
make_head(_module, 'IMSVidStreamBufferSink')
make_head(_module, 'IMSVidStreamBufferSink2')
make_head(_module, 'IMSVidStreamBufferSink3')
make_head(_module, 'IMSVidStreamBufferSinkEvent')
make_head(_module, 'IMSVidStreamBufferSinkEvent2')
make_head(_module, 'IMSVidStreamBufferSinkEvent3')
make_head(_module, 'IMSVidStreamBufferSinkEvent4')
make_head(_module, 'IMSVidStreamBufferSource')
make_head(_module, 'IMSVidStreamBufferSource2')
make_head(_module, 'IMSVidStreamBufferSourceEvent')
make_head(_module, 'IMSVidStreamBufferSourceEvent2')
make_head(_module, 'IMSVidStreamBufferSourceEvent3')
make_head(_module, 'IMSVidStreamBufferV2SourceEvent')
make_head(_module, 'IMSVidTuner')
make_head(_module, 'IMSVidTunerEvent')
make_head(_module, 'IMSVidVMR9')
make_head(_module, 'IMSVidVRGraphSegment')
make_head(_module, 'IMSVidVideoInputDevice')
make_head(_module, 'IMSVidVideoRenderer')
make_head(_module, 'IMSVidVideoRenderer2')
make_head(_module, 'IMSVidVideoRendererDevices')
make_head(_module, 'IMSVidVideoRendererEvent')
make_head(_module, 'IMSVidVideoRendererEvent2')
make_head(_module, 'IMSVidWebDVD')
make_head(_module, 'IMSVidWebDVD2')
make_head(_module, 'IMSVidWebDVDAdm')
make_head(_module, 'IMSVidWebDVDEvent')
make_head(_module, 'IMSVidXDS')
make_head(_module, 'IMSVidXDSEvent')
make_head(_module, 'IMceBurnerControl')
make_head(_module, 'IMpeg2Data')
make_head(_module, 'IMpeg2Stream')
make_head(_module, 'IMpeg2TableFilter')
make_head(_module, 'IPAT')
make_head(_module, 'IPBDAAttributesDescriptor')
make_head(_module, 'IPBDAEntitlementDescriptor')
make_head(_module, 'IPBDASiParser')
make_head(_module, 'IPBDA_EIT')
make_head(_module, 'IPBDA_Services')
make_head(_module, 'IPMT')
make_head(_module, 'IPSITables')
make_head(_module, 'IPTFilterLicenseRenewal')
make_head(_module, 'IPersistTuneXml')
make_head(_module, 'IPersistTuneXmlUtility')
make_head(_module, 'IPersistTuneXmlUtility2')
make_head(_module, 'IRegisterTuner')
make_head(_module, 'ISBE2Crossbar')
make_head(_module, 'ISBE2EnumStream')
make_head(_module, 'ISBE2FileScan')
make_head(_module, 'ISBE2GlobalEvent')
make_head(_module, 'ISBE2GlobalEvent2')
make_head(_module, 'ISBE2MediaTypeProfile')
make_head(_module, 'ISBE2SpanningEvent')
make_head(_module, 'ISBE2StreamMap')
make_head(_module, 'ISCTE_EAS')
make_head(_module, 'ISIInbandEPG')
make_head(_module, 'ISIInbandEPGEvent')
make_head(_module, 'IScanningTuner')
make_head(_module, 'IScanningTunerEx')
make_head(_module, 'ISectionList')
make_head(_module, 'IServiceLocationDescriptor')
make_head(_module, 'IStreamBufferConfigure')
make_head(_module, 'IStreamBufferConfigure2')
make_head(_module, 'IStreamBufferConfigure3')
make_head(_module, 'IStreamBufferDataCounters')
make_head(_module, 'IStreamBufferInitialize')
make_head(_module, 'IStreamBufferMediaSeeking')
make_head(_module, 'IStreamBufferMediaSeeking2')
make_head(_module, 'IStreamBufferRecComp')
make_head(_module, 'IStreamBufferRecordControl')
make_head(_module, 'IStreamBufferRecordingAttribute')
make_head(_module, 'IStreamBufferSink')
make_head(_module, 'IStreamBufferSink2')
make_head(_module, 'IStreamBufferSink3')
make_head(_module, 'IStreamBufferSource')
make_head(_module, 'ITSDT')
make_head(_module, 'ITuneRequest')
make_head(_module, 'ITuneRequestInfo')
make_head(_module, 'ITuneRequestInfoEx')
make_head(_module, 'ITuner')
make_head(_module, 'ITunerCap')
make_head(_module, 'ITunerCapEx')
make_head(_module, 'ITuningSpace')
make_head(_module, 'ITuningSpaceContainer')
make_head(_module, 'ITuningSpaces')
make_head(_module, 'IXDSCodec')
make_head(_module, 'IXDSCodecConfig')
make_head(_module, 'IXDSCodecEvents')
make_head(_module, 'IXDSToRat')
make_head(_module, 'KSEVENTDATA_BDA_RF_TUNER_SCAN_S')
make_head(_module, 'KSM_BDA_BUFFER')
make_head(_module, 'KSM_BDA_CAS_CAPTURETOKEN')
make_head(_module, 'KSM_BDA_CAS_CLOSEMMIDIALOG')
make_head(_module, 'KSM_BDA_CAS_ENTITLEMENTTOKEN')
make_head(_module, 'KSM_BDA_CAS_OPENBROADCASTMMI')
make_head(_module, 'KSM_BDA_DEBUG_LEVEL')
make_head(_module, 'KSM_BDA_DRM_SETDRM')
make_head(_module, 'KSM_BDA_EVENT_COMPLETE')
make_head(_module, 'KSM_BDA_GDDS_SERVICEFROMTUNEXML')
make_head(_module, 'KSM_BDA_GDDS_TUNEXMLFROMIDX')
make_head(_module, 'KSM_BDA_GPNV_GETVALUE')
make_head(_module, 'KSM_BDA_GPNV_NAMEINDEX')
make_head(_module, 'KSM_BDA_GPNV_SETVALUE')
make_head(_module, 'KSM_BDA_ISDBCAS_REQUEST')
make_head(_module, 'KSM_BDA_PIN')
make_head(_module, 'KSM_BDA_PIN_PAIR')
make_head(_module, 'KSM_BDA_SCAN_CAPABILTIES')
make_head(_module, 'KSM_BDA_SCAN_FILTER')
make_head(_module, 'KSM_BDA_SCAN_START')
make_head(_module, 'KSM_BDA_TS_SELECTOR_SETTSID')
make_head(_module, 'KSM_BDA_TUNER_TUNEREQUEST')
make_head(_module, 'KSM_BDA_USERACTIVITY_USEREASON')
make_head(_module, 'KSM_BDA_WMDRMTUNER_GETPIDPROTECTION')
make_head(_module, 'KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT')
make_head(_module, 'KSM_BDA_WMDRMTUNER_SETPIDPROTECTION')
make_head(_module, 'KSM_BDA_WMDRMTUNER_SYNCVALUE')
make_head(_module, 'KSM_BDA_WMDRM_LICENSE')
make_head(_module, 'KSM_BDA_WMDRM_RENEWLICENSE')
make_head(_module, 'KSPROPERTY_BDA_RF_TUNER_CAPS_S')
make_head(_module, 'KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S')
make_head(_module, 'KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S')
make_head(_module, 'KSPROPERTY_BDA_RF_TUNER_STANDARD_S')
make_head(_module, 'KSP_BDA_NODE_PIN')
make_head(_module, 'KSP_NODE_ESPID')
make_head(_module, 'KS_DATARANGE_BDA_ANTENNA')
make_head(_module, 'KS_DATARANGE_BDA_TRANSPORT')
make_head(_module, 'LONG_SECTION')
make_head(_module, 'LanguageInfo')
make_head(_module, 'MPEG2_FILTER')
make_head(_module, 'MPEG2_FILTER2')
make_head(_module, 'MPEG_BCS_DEMUX')
make_head(_module, 'MPEG_CONTEXT')
make_head(_module, 'MPEG_DATE')
make_head(_module, 'MPEG_DATE_AND_TIME')
make_head(_module, 'MPEG_HEADER_BITS')
make_head(_module, 'MPEG_HEADER_BITS_MIDL')
make_head(_module, 'MPEG_HEADER_VERSION_BITS')
make_head(_module, 'MPEG_HEADER_VERSION_BITS_MIDL')
make_head(_module, 'MPEG_PACKET_LIST')
make_head(_module, 'MPEG_RQST_PACKET')
make_head(_module, 'MPEG_SERVICE_REQUEST')
make_head(_module, 'MPEG_SERVICE_RESPONSE')
make_head(_module, 'MPEG_STREAM_BUFFER')
make_head(_module, 'MPEG_STREAM_FILTER')
make_head(_module, 'MPEG_TIME')
make_head(_module, 'MPEG_WINSOCK')
make_head(_module, 'MPE_ELEMENT')
make_head(_module, 'Mpeg2TableSampleHdr')
make_head(_module, 'PBDAParentalControl')
make_head(_module, 'PBDA_TAG_ATTRIBUTE')
make_head(_module, 'PIC_SEQ_SAMPLE')
make_head(_module, 'PIDListSpanningEvent')
make_head(_module, 'PID_BITS')
make_head(_module, 'PID_BITS_MIDL')
make_head(_module, 'ProgramElement')
make_head(_module, 'RATING_ATTRIBUTE')
make_head(_module, 'RATING_INFO')
make_head(_module, 'RATING_SYSTEM')
make_head(_module, 'SAMPLE_LIVE_STREAM_TIME')
make_head(_module, 'SAMPLE_SEQ_OFFSET')
make_head(_module, 'SBE2_STREAM_DESC')
make_head(_module, 'SBE_PIN_DATA')
make_head(_module, 'SECTION')
make_head(_module, 'STREAMBUFFER_ATTRIBUTE')
make_head(_module, 'SpanningEventDescriptor')
make_head(_module, 'SpanningEventEmmMessage')
make_head(_module, 'TID_EXTENSION')
make_head(_module, 'TRANSPORT_PROPERTIES')
make_head(_module, 'UDCR_TAG')
make_head(_module, 'VA_OPTIONAL_VIDEO_PROPERTIES')
make_head(_module, 'WMDRMProtectionInfo')
make_head(_module, '_IMSVidCtlEvents')
