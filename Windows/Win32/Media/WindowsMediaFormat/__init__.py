from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Media.WindowsMediaFormat
import Windows.Win32.System.Com
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
class AM_WMT_EVENT_DATA(EasyCastStructure):
    hrStatus: Windows.Win32.Foundation.HRESULT
    pData: c_void_p
WMT_VIDEOIMAGE_SAMPLE_INPUT_FRAME: UInt32 = 1
WMT_VIDEOIMAGE_SAMPLE_OUTPUT_FRAME: UInt32 = 2
WMT_VIDEOIMAGE_SAMPLE_USES_CURRENT_INPUT_FRAME: UInt32 = 4
WMT_VIDEOIMAGE_SAMPLE_USES_PREVIOUS_INPUT_FRAME: UInt32 = 8
WMT_VIDEOIMAGE_SAMPLE_MOTION: UInt32 = 1
WMT_VIDEOIMAGE_SAMPLE_ROTATION: UInt32 = 2
WMT_VIDEOIMAGE_SAMPLE_BLENDING: UInt32 = 4
WMT_VIDEOIMAGE_SAMPLE_ADV_BLENDING: UInt32 = 8
WMT_VIDEOIMAGE_INTEGER_DENOMINATOR: Int32 = 65536
WMT_VIDEOIMAGE_MAGIC_NUMBER: UInt32 = 491406834
WMT_VIDEOIMAGE_MAGIC_NUMBER_2: UInt32 = 491406835
WMT_VIDEOIMAGE_TRANSITION_BOW_TIE: UInt32 = 11
WMT_VIDEOIMAGE_TRANSITION_CIRCLE: UInt32 = 12
WMT_VIDEOIMAGE_TRANSITION_CROSS_FADE: UInt32 = 13
WMT_VIDEOIMAGE_TRANSITION_DIAGONAL: UInt32 = 14
WMT_VIDEOIMAGE_TRANSITION_DIAMOND: UInt32 = 15
WMT_VIDEOIMAGE_TRANSITION_FADE_TO_COLOR: UInt32 = 16
WMT_VIDEOIMAGE_TRANSITION_FILLED_V: UInt32 = 17
WMT_VIDEOIMAGE_TRANSITION_FLIP: UInt32 = 18
WMT_VIDEOIMAGE_TRANSITION_INSET: UInt32 = 19
WMT_VIDEOIMAGE_TRANSITION_IRIS: UInt32 = 20
WMT_VIDEOIMAGE_TRANSITION_PAGE_ROLL: UInt32 = 21
WMT_VIDEOIMAGE_TRANSITION_RECTANGLE: UInt32 = 23
WMT_VIDEOIMAGE_TRANSITION_REVEAL: UInt32 = 24
WMT_VIDEOIMAGE_TRANSITION_SLIDE: UInt32 = 27
WMT_VIDEOIMAGE_TRANSITION_SPLIT: UInt32 = 29
WMT_VIDEOIMAGE_TRANSITION_STAR: UInt32 = 30
WMT_VIDEOIMAGE_TRANSITION_WHEEL: UInt32 = 31
WM_SampleExtension_ContentType_Size: UInt32 = 1
WM_SampleExtension_PixelAspectRatio_Size: UInt32 = 2
WM_SampleExtension_Timecode_Size: UInt32 = 14
WM_SampleExtension_SampleDuration_Size: UInt32 = 2
WM_SampleExtension_ChromaLocation_Size: UInt32 = 1
WM_SampleExtension_ColorSpaceInfo_Size: UInt32 = 3
WM_CT_REPEAT_FIRST_FIELD: UInt32 = 16
WM_CT_BOTTOM_FIELD_FIRST: UInt32 = 32
WM_CT_TOP_FIELD_FIRST: UInt32 = 64
WM_CT_INTERLACED: UInt32 = 128
WM_CL_INTERLACED420: UInt32 = 0
WM_CL_PROGRESSIVE420: UInt32 = 1
WM_MAX_VIDEO_STREAMS: UInt32 = 63
WM_MAX_STREAMS: UInt32 = 63
WMDRM_IMPORT_INIT_STRUCT_DEFINED: UInt32 = 1
DRM_OPL_TYPES: UInt32 = 1
g_dwWMSpecialAttributes: UInt32 = 20
g_wszWMDuration: String = 'Duration'
g_wszWMBitrate: String = 'Bitrate'
g_wszWMSeekable: String = 'Seekable'
g_wszWMStridable: String = 'Stridable'
g_wszWMBroadcast: String = 'Broadcast'
g_wszWMProtected: String = 'Is_Protected'
g_wszWMTrusted: String = 'Is_Trusted'
g_wszWMSignature_Name: String = 'Signature_Name'
g_wszWMHasAudio: String = 'HasAudio'
g_wszWMHasImage: String = 'HasImage'
g_wszWMHasScript: String = 'HasScript'
g_wszWMHasVideo: String = 'HasVideo'
g_wszWMCurrentBitrate: String = 'CurrentBitrate'
g_wszWMOptimalBitrate: String = 'OptimalBitrate'
g_wszWMHasAttachedImages: String = 'HasAttachedImages'
g_wszWMSkipBackward: String = 'Can_Skip_Backward'
g_wszWMSkipForward: String = 'Can_Skip_Forward'
g_wszWMNumberOfFrames: String = 'NumberOfFrames'
g_wszWMFileSize: String = 'FileSize'
g_wszWMHasArbitraryDataStream: String = 'HasArbitraryDataStream'
g_wszWMHasFileTransferStream: String = 'HasFileTransferStream'
g_wszWMContainerFormat: String = 'WM/ContainerFormat'
g_dwWMContentAttributes: UInt32 = 5
g_wszWMTitle: String = 'Title'
g_wszWMTitleSort: String = 'TitleSort'
g_wszWMAuthor: String = 'Author'
g_wszWMAuthorSort: String = 'AuthorSort'
g_wszWMDescription: String = 'Description'
g_wszWMRating: String = 'Rating'
g_wszWMCopyright: String = 'Copyright'
g_wszWMUse_DRM: String = 'Use_DRM'
g_wszWMDRM_Flags: String = 'DRM_Flags'
g_wszWMDRM_Level: String = 'DRM_Level'
g_wszWMUse_Advanced_DRM: String = 'Use_Advanced_DRM'
g_wszWMDRM_KeySeed: String = 'DRM_KeySeed'
g_wszWMDRM_KeyID: String = 'DRM_KeyID'
g_wszWMDRM_ContentID: String = 'DRM_ContentID'
g_wszWMDRM_SourceID: String = 'DRM_SourceID'
g_wszWMDRM_IndividualizedVersion: String = 'DRM_IndividualizedVersion'
g_wszWMDRM_LicenseAcqURL: String = 'DRM_LicenseAcqURL'
g_wszWMDRM_V1LicenseAcqURL: String = 'DRM_V1LicenseAcqURL'
g_wszWMDRM_HeaderSignPrivKey: String = 'DRM_HeaderSignPrivKey'
g_wszWMDRM_LASignaturePrivKey: String = 'DRM_LASignaturePrivKey'
g_wszWMDRM_LASignatureCert: String = 'DRM_LASignatureCert'
g_wszWMDRM_LASignatureLicSrvCert: String = 'DRM_LASignatureLicSrvCert'
g_wszWMDRM_LASignatureRootCert: String = 'DRM_LASignatureRootCert'
g_wszWMAlbumTitle: String = 'WM/AlbumTitle'
g_wszWMAlbumTitleSort: String = 'WM/AlbumTitleSort'
g_wszWMTrack: String = 'WM/Track'
g_wszWMPromotionURL: String = 'WM/PromotionURL'
g_wszWMAlbumCoverURL: String = 'WM/AlbumCoverURL'
g_wszWMGenre: String = 'WM/Genre'
g_wszWMYear: String = 'WM/Year'
g_wszWMGenreID: String = 'WM/GenreID'
g_wszWMMCDI: String = 'WM/MCDI'
g_wszWMComposer: String = 'WM/Composer'
g_wszWMComposerSort: String = 'WM/ComposerSort'
g_wszWMLyrics: String = 'WM/Lyrics'
g_wszWMTrackNumber: String = 'WM/TrackNumber'
g_wszWMToolName: String = 'WM/ToolName'
g_wszWMToolVersion: String = 'WM/ToolVersion'
g_wszWMIsVBR: String = 'IsVBR'
g_wszWMAlbumArtist: String = 'WM/AlbumArtist'
g_wszWMAlbumArtistSort: String = 'WM/AlbumArtistSort'
g_wszWMBannerImageType: String = 'BannerImageType'
g_wszWMBannerImageData: String = 'BannerImageData'
g_wszWMBannerImageURL: String = 'BannerImageURL'
g_wszWMCopyrightURL: String = 'CopyrightURL'
g_wszWMAspectRatioX: String = 'AspectRatioX'
g_wszWMAspectRatioY: String = 'AspectRatioY'
g_wszASFLeakyBucketPairs: String = 'ASFLeakyBucketPairs'
g_dwWMNSCAttributes: UInt32 = 5
g_wszWMNSCName: String = 'NSC_Name'
g_wszWMNSCAddress: String = 'NSC_Address'
g_wszWMNSCPhone: String = 'NSC_Phone'
g_wszWMNSCEmail: String = 'NSC_Email'
g_wszWMNSCDescription: String = 'NSC_Description'
g_wszWMWriter: String = 'WM/Writer'
g_wszWMConductor: String = 'WM/Conductor'
g_wszWMProducer: String = 'WM/Producer'
g_wszWMDirector: String = 'WM/Director'
g_wszWMContentGroupDescription: String = 'WM/ContentGroupDescription'
g_wszWMSubTitle: String = 'WM/SubTitle'
g_wszWMPartOfSet: String = 'WM/PartOfSet'
g_wszWMProtectionType: String = 'WM/ProtectionType'
g_wszWMVideoHeight: String = 'WM/VideoHeight'
g_wszWMVideoWidth: String = 'WM/VideoWidth'
g_wszWMVideoFrameRate: String = 'WM/VideoFrameRate'
g_wszWMMediaClassPrimaryID: String = 'WM/MediaClassPrimaryID'
g_wszWMMediaClassSecondaryID: String = 'WM/MediaClassSecondaryID'
g_wszWMPeriod: String = 'WM/Period'
g_wszWMCategory: String = 'WM/Category'
g_wszWMPicture: String = 'WM/Picture'
g_wszWMLyrics_Synchronised: String = 'WM/Lyrics_Synchronised'
g_wszWMOriginalLyricist: String = 'WM/OriginalLyricist'
g_wszWMOriginalArtist: String = 'WM/OriginalArtist'
g_wszWMOriginalAlbumTitle: String = 'WM/OriginalAlbumTitle'
g_wszWMOriginalReleaseYear: String = 'WM/OriginalReleaseYear'
g_wszWMOriginalFilename: String = 'WM/OriginalFilename'
g_wszWMPublisher: String = 'WM/Publisher'
g_wszWMEncodedBy: String = 'WM/EncodedBy'
g_wszWMEncodingSettings: String = 'WM/EncodingSettings'
g_wszWMEncodingTime: String = 'WM/EncodingTime'
g_wszWMAuthorURL: String = 'WM/AuthorURL'
g_wszWMUserWebURL: String = 'WM/UserWebURL'
g_wszWMAudioFileURL: String = 'WM/AudioFileURL'
g_wszWMAudioSourceURL: String = 'WM/AudioSourceURL'
g_wszWMLanguage: String = 'WM/Language'
g_wszWMParentalRating: String = 'WM/ParentalRating'
g_wszWMBeatsPerMinute: String = 'WM/BeatsPerMinute'
g_wszWMInitialKey: String = 'WM/InitialKey'
g_wszWMMood: String = 'WM/Mood'
g_wszWMText: String = 'WM/Text'
g_wszWMDVDID: String = 'WM/DVDID'
g_wszWMWMContentID: String = 'WM/WMContentID'
g_wszWMWMCollectionID: String = 'WM/WMCollectionID'
g_wszWMWMCollectionGroupID: String = 'WM/WMCollectionGroupID'
g_wszWMUniqueFileIdentifier: String = 'WM/UniqueFileIdentifier'
g_wszWMModifiedBy: String = 'WM/ModifiedBy'
g_wszWMRadioStationName: String = 'WM/RadioStationName'
g_wszWMRadioStationOwner: String = 'WM/RadioStationOwner'
g_wszWMPlaylistDelay: String = 'WM/PlaylistDelay'
g_wszWMCodec: String = 'WM/Codec'
g_wszWMDRM: String = 'WM/DRM'
g_wszWMISRC: String = 'WM/ISRC'
g_wszWMProvider: String = 'WM/Provider'
g_wszWMProviderRating: String = 'WM/ProviderRating'
g_wszWMProviderStyle: String = 'WM/ProviderStyle'
g_wszWMContentDistributor: String = 'WM/ContentDistributor'
g_wszWMSubscriptionContentID: String = 'WM/SubscriptionContentID'
g_wszWMWMADRCPeakReference: String = 'WM/WMADRCPeakReference'
g_wszWMWMADRCPeakTarget: String = 'WM/WMADRCPeakTarget'
g_wszWMWMADRCAverageReference: String = 'WM/WMADRCAverageReference'
g_wszWMWMADRCAverageTarget: String = 'WM/WMADRCAverageTarget'
g_wszWMStreamTypeInfo: String = 'WM/StreamTypeInfo'
g_wszWMPeakBitrate: String = 'WM/PeakBitrate'
g_wszWMASFPacketCount: String = 'WM/ASFPacketCount'
g_wszWMASFSecurityObjectsSize: String = 'WM/ASFSecurityObjectsSize'
g_wszWMSharedUserRating: String = 'WM/SharedUserRating'
g_wszWMSubTitleDescription: String = 'WM/SubTitleDescription'
g_wszWMMediaCredits: String = 'WM/MediaCredits'
g_wszWMParentalRatingReason: String = 'WM/ParentalRatingReason'
g_wszWMOriginalReleaseTime: String = 'WM/OriginalReleaseTime'
g_wszWMMediaStationCallSign: String = 'WM/MediaStationCallSign'
g_wszWMMediaStationName: String = 'WM/MediaStationName'
g_wszWMMediaNetworkAffiliation: String = 'WM/MediaNetworkAffiliation'
g_wszWMMediaOriginalChannel: String = 'WM/MediaOriginalChannel'
g_wszWMMediaOriginalBroadcastDateTime: String = 'WM/MediaOriginalBroadcastDateTime'
g_wszWMMediaIsStereo: String = 'WM/MediaIsStereo'
g_wszWMVideoClosedCaptioning: String = 'WM/VideoClosedCaptioning'
g_wszWMMediaIsRepeat: String = 'WM/MediaIsRepeat'
g_wszWMMediaIsLive: String = 'WM/MediaIsLive'
g_wszWMMediaIsTape: String = 'WM/MediaIsTape'
g_wszWMMediaIsDelay: String = 'WM/MediaIsDelay'
g_wszWMMediaIsSubtitled: String = 'WM/MediaIsSubtitled'
g_wszWMMediaIsPremiere: String = 'WM/MediaIsPremiere'
g_wszWMMediaIsFinale: String = 'WM/MediaIsFinale'
g_wszWMMediaIsSAP: String = 'WM/MediaIsSAP'
g_wszWMProviderCopyright: String = 'WM/ProviderCopyright'
g_wszWMISAN: String = 'WM/ISAN'
g_wszWMADID: String = 'WM/ADID'
g_wszWMWMShadowFileSourceFileType: String = 'WM/WMShadowFileSourceFileType'
g_wszWMWMShadowFileSourceDRMType: String = 'WM/WMShadowFileSourceDRMType'
g_wszWMWMCPDistributor: String = 'WM/WMCPDistributor'
g_wszWMWMCPDistributorID: String = 'WM/WMCPDistributorID'
g_wszWMSeasonNumber: String = 'WM/SeasonNumber'
g_wszWMEpisodeNumber: String = 'WM/EpisodeNumber'
g_wszEarlyDataDelivery: String = 'EarlyDataDelivery'
g_wszJustInTimeDecode: String = 'JustInTimeDecode'
g_wszSingleOutputBuffer: String = 'SingleOutputBuffer'
g_wszSoftwareScaling: String = 'SoftwareScaling'
g_wszDeliverOnReceive: String = 'DeliverOnReceive'
g_wszScrambledAudio: String = 'ScrambledAudio'
g_wszDedicatedDeliveryThread: String = 'DedicatedDeliveryThread'
g_wszEnableDiscreteOutput: String = 'EnableDiscreteOutput'
g_wszSpeakerConfig: String = 'SpeakerConfig'
g_wszDynamicRangeControl: String = 'DynamicRangeControl'
g_wszAllowInterlacedOutput: String = 'AllowInterlacedOutput'
g_wszVideoSampleDurations: String = 'VideoSampleDurations'
g_wszStreamLanguage: String = 'StreamLanguage'
g_wszEnableWMAProSPDIFOutput: String = 'EnableWMAProSPDIFOutput'
g_wszDeinterlaceMode: String = 'DeinterlaceMode'
g_wszInitialPatternForInverseTelecine: String = 'InitialPatternForInverseTelecine'
g_wszJPEGCompressionQuality: String = 'JPEGCompressionQuality'
g_wszWatermarkCLSID: String = 'WatermarkCLSID'
g_wszWatermarkConfig: String = 'WatermarkConfig'
g_wszInterlacedCoding: String = 'InterlacedCoding'
g_wszFixedFrameRate: String = 'FixedFrameRate'
g_wszOriginalSourceFormatTag: String = '_SOURCEFORMATTAG'
g_wszOriginalWaveFormat: String = '_ORIGINALWAVEFORMAT'
g_wszEDL: String = '_EDL'
g_wszComplexity: String = '_COMPLEXITYEX'
g_wszDecoderComplexityRequested: String = '_DECODERCOMPLEXITYPROFILE'
g_wszReloadIndexOnSeek: String = 'ReloadIndexOnSeek'
g_wszStreamNumIndexObjects: String = 'StreamNumIndexObjects'
g_wszFailSeekOnError: String = 'FailSeekOnError'
g_wszPermitSeeksBeyondEndOfStream: String = 'PermitSeeksBeyondEndOfStream'
g_wszUsePacketAtSeekPoint: String = 'UsePacketAtSeekPoint'
g_wszSourceBufferTime: String = 'SourceBufferTime'
g_wszSourceMaxBytesAtOnce: String = 'SourceMaxBytesAtOnce'
g_wszVBREnabled: String = '_VBRENABLED'
g_wszVBRQuality: String = '_VBRQUALITY'
g_wszVBRBitrateMax: String = '_RMAX'
g_wszVBRBufferWindowMax: String = '_BMAX'
g_wszVBRPeak: String = 'VBR Peak'
g_wszBufferAverage: String = 'Buffer Average'
g_wszComplexityMax: String = '_COMPLEXITYEXMAX'
g_wszComplexityOffline: String = '_COMPLEXITYEXOFFLINE'
g_wszComplexityLive: String = '_COMPLEXITYEXLIVE'
g_wszIsVBRSupported: String = '_ISVBRSUPPORTED'
g_wszNumPasses: String = '_PASSESUSED'
g_wszMusicSpeechClassMode: String = 'MusicSpeechClassMode'
g_wszMusicClassMode: String = 'MusicClassMode'
g_wszSpeechClassMode: String = 'SpeechClassMode'
g_wszMixedClassMode: String = 'MixedClassMode'
g_wszSpeechCaps: String = 'SpeechFormatCap'
g_wszPeakValue: String = 'PeakValue'
g_wszAverageLevel: String = 'AverageLevel'
g_wszFold6To2Channels3: String = 'Fold6To2Channels3'
g_wszFoldToChannelsTemplate: String = 'Fold%luTo%luChannels%lu'
g_wszDeviceConformanceTemplate: String = 'DeviceConformanceTemplate'
g_wszEnableFrameInterpolation: String = 'EnableFrameInterpolation'
g_wszNeedsPreviousSample: String = 'NeedsPreviousSample'
g_wszWMIsCompilation: String = 'WM/IsCompilation'
WMMEDIASUBTYPE_Base: Guid = Guid('00000000-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIATYPE_Video: Guid = Guid('73646976-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_RGB1: Guid = Guid('e436eb78-524f-11ce-9f-53-00-20-af-0b-a7-70')
WMMEDIASUBTYPE_RGB4: Guid = Guid('e436eb79-524f-11ce-9f-53-00-20-af-0b-a7-70')
WMMEDIASUBTYPE_RGB8: Guid = Guid('e436eb7a-524f-11ce-9f-53-00-20-af-0b-a7-70')
WMMEDIASUBTYPE_RGB565: Guid = Guid('e436eb7b-524f-11ce-9f-53-00-20-af-0b-a7-70')
WMMEDIASUBTYPE_RGB555: Guid = Guid('e436eb7c-524f-11ce-9f-53-00-20-af-0b-a7-70')
WMMEDIASUBTYPE_RGB24: Guid = Guid('e436eb7d-524f-11ce-9f-53-00-20-af-0b-a7-70')
WMMEDIASUBTYPE_RGB32: Guid = Guid('e436eb7e-524f-11ce-9f-53-00-20-af-0b-a7-70')
WMMEDIASUBTYPE_I420: Guid = Guid('30323449-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_IYUV: Guid = Guid('56555949-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_YV12: Guid = Guid('32315659-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_YUY2: Guid = Guid('32595559-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_P422: Guid = Guid('32323450-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_UYVY: Guid = Guid('59565955-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_YVYU: Guid = Guid('55595659-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_YVU9: Guid = Guid('39555659-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_VIDEOIMAGE: Guid = Guid('1d4a45f2-e5f6-4b44-83-88-f0-ae-5c-0e-0c-37')
WMMEDIASUBTYPE_MP43: Guid = Guid('3334504d-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_MP4S: Guid = Guid('5334504d-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_M4S2: Guid = Guid('3253344d-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMV1: Guid = Guid('31564d57-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMV2: Guid = Guid('32564d57-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_MSS1: Guid = Guid('3153534d-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_MPEG2_VIDEO: Guid = Guid('e06d8026-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
WMMEDIATYPE_Audio: Guid = Guid('73647561-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_PCM: Guid = Guid('00000001-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_DRM: Guid = Guid('00000009-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMAudioV9: Guid = Guid('00000162-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMAudio_Lossless: Guid = Guid('00000163-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_MSS2: Guid = Guid('3253534d-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMSP1: Guid = Guid('0000000a-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMSP2: Guid = Guid('0000000b-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMV3: Guid = Guid('33564d57-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMVP: Guid = Guid('50564d57-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WVP2: Guid = Guid('32505657-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMVA: Guid = Guid('41564d57-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WVC1: Guid = Guid('31435657-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMAudioV8: Guid = Guid('00000161-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMAudioV7: Guid = Guid('00000161-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WMAudioV2: Guid = Guid('00000161-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_ACELPnet: Guid = Guid('00000130-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_MP3: Guid = Guid('00000055-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIASUBTYPE_WebStream: Guid = Guid('776257d4-c627-41cb-8f-81-7a-c7-ff-1c-40-cc')
WMMEDIATYPE_Script: Guid = Guid('73636d64-0000-0010-80-00-00-aa-00-38-9b-71')
WMMEDIATYPE_Image: Guid = Guid('34a50fd8-8aa5-4386-81-fe-a0-ef-e0-48-8e-31')
WMMEDIATYPE_FileTransfer: Guid = Guid('d9e47579-930e-4427-ad-fc-ad-80-f2-90-e4-70')
WMMEDIATYPE_Text: Guid = Guid('9bba1ea7-5ab2-4829-ba-57-09-40-20-9b-cf-3e')
WMFORMAT_VideoInfo: Guid = Guid('05589f80-c356-11ce-bf-01-00-aa-00-55-59-5a')
WMFORMAT_MPEG2Video: Guid = Guid('e06d80e3-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
WMFORMAT_WaveFormatEx: Guid = Guid('05589f81-c356-11ce-bf-01-00-aa-00-55-59-5a')
WMFORMAT_Script: Guid = Guid('5c8510f2-debe-4ca7-bb-a5-f0-7a-10-4f-8d-ff')
WMFORMAT_WebStream: Guid = Guid('da1e6b13-8359-4050-b3-98-38-8e-96-5b-f0-0c')
WMSCRIPTTYPE_TwoStrings: Guid = Guid('82f38a70-c29f-11d1-97-ad-00-a0-c9-5e-a8-50')
WM_SampleExtensionGUID_OutputCleanPoint: Guid = Guid('f72a3c6f-6eb4-4ebc-b1-92-09-ad-97-59-e8-28')
WM_SampleExtensionGUID_Timecode: Guid = Guid('399595ec-8667-4e2d-8f-db-98-81-4c-e7-6c-1e')
WM_SampleExtensionGUID_ChromaLocation: Guid = Guid('4c5acca0-9276-4b2c-9e-4c-a0-ed-ef-dd-21-7e')
WM_SampleExtensionGUID_ColorSpaceInfo: Guid = Guid('f79ada56-30eb-4f2b-9f-7a-f2-4b-13-9a-11-57')
WM_SampleExtensionGUID_UserDataInfo: Guid = Guid('732bb4fa-78be-4549-99-bd-02-db-1a-55-b7-a8')
WM_SampleExtensionGUID_FileName: Guid = Guid('e165ec0e-19ed-45d7-b4-a7-25-cb-d1-e2-8e-9b')
WM_SampleExtensionGUID_ContentType: Guid = Guid('d590dc20-07bc-436c-9c-f7-f3-bb-fb-f1-a4-dc')
WM_SampleExtensionGUID_PixelAspectRatio: Guid = Guid('1b1ee554-f9ea-4bc8-82-1a-37-6b-74-e4-c4-b8')
WM_SampleExtensionGUID_SampleDuration: Guid = Guid('c6bd9450-867f-4907-83-a3-c7-79-21-b7-33-ad')
WM_SampleExtensionGUID_SampleProtectionSalt: Guid = Guid('5403deee-b9ee-438f-aa-83-38-04-99-7e-56-9d')
CLSID_WMMUTEX_Language: Guid = Guid('d6e22a00-35da-11d1-90-34-00-a0-c9-03-49-be')
CLSID_WMMUTEX_Bitrate: Guid = Guid('d6e22a01-35da-11d1-90-34-00-a0-c9-03-49-be')
CLSID_WMMUTEX_Presentation: Guid = Guid('d6e22a02-35da-11d1-90-34-00-a0-c9-03-49-be')
CLSID_WMMUTEX_Unknown: Guid = Guid('d6e22a03-35da-11d1-90-34-00-a0-c9-03-49-be')
CLSID_WMBandwidthSharing_Exclusive: Guid = Guid('af6060aa-5197-11d2-b6-af-00-c0-4f-d9-08-e9')
CLSID_WMBandwidthSharing_Partial: Guid = Guid('af6060ab-5197-11d2-b6-af-00-c0-4f-d9-08-e9')
WMT_DMOCATEGORY_AUDIO_WATERMARK: Guid = Guid('65221c5a-fa75-4b39-b5-0c-06-c3-36-b6-a3-ef')
WMT_DMOCATEGORY_VIDEO_WATERMARK: Guid = Guid('187cc922-8efc-4404-9d-af-63-f4-83-0d-f1-bc')
CLSID_ClientNetManager: Guid = Guid('cd12a3ce-9c42-11d2-be-ed-00-60-08-2f-20-54')
@winfunctype('WMVCore.dll')
def WMIsContentProtected(pwszFileName: Windows.Win32.Foundation.PWSTR, pfIsProtected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriter(pUnkCert: Windows.Win32.System.Com.IUnknown_head, ppWriter: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateReader(pUnkCert: Windows.Win32.System.Com.IUnknown_head, dwRights: UInt32, ppReader: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateSyncReader(pUnkCert: Windows.Win32.System.Com.IUnknown_head, dwRights: UInt32, ppSyncReader: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMSyncReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateEditor(ppEditor: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMMetadataEditor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateIndexer(ppIndexer: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMIndexer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateBackupRestorer(pCallback: Windows.Win32.System.Com.IUnknown_head, ppBackup: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMLicenseBackup_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateProfileManager(ppProfileManager: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMProfileManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriterFileSink(ppSink: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMWriterFileSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriterNetworkSink(ppSink: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMWriterNetworkSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriterPushSink(ppSink: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMWriterPushSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
class DRM_COPY_OPL(EasyCastStructure):
    wMinimumCopyLevel: UInt16
    oplIdIncludes: Windows.Win32.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS
    oplIdExcludes: Windows.Win32.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS
class DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS(EasyCastStructure):
    wCompressedDigitalVideo: UInt16
    wUncompressedDigitalVideo: UInt16
    wAnalogVideo: UInt16
    wCompressedDigitalAudio: UInt16
    wUncompressedDigitalAudio: UInt16
class DRM_OPL_OUTPUT_IDS(EasyCastStructure):
    cIds: UInt16
    rgIds: POINTER(Guid)
class DRM_OUTPUT_PROTECTION(EasyCastStructure):
    guidId: Guid
    bConfigData: Byte
class DRM_PLAY_OPL(EasyCastStructure):
    minOPL: Windows.Win32.Media.WindowsMediaFormat.DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS
    oplIdReserved: Windows.Win32.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS
    vopi: Windows.Win32.Media.WindowsMediaFormat.DRM_VIDEO_OUTPUT_PROTECTION_IDS
class DRM_VAL16(EasyCastStructure):
    val: Byte * 16
class DRM_VIDEO_OUTPUT_PROTECTION_IDS(EasyCastStructure):
    cEntries: UInt16
    rgVop: POINTER(Windows.Win32.Media.WindowsMediaFormat.DRM_OUTPUT_PROTECTION_head)
class INSNetSourceCreator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('0c0e4080-9081-11d2-be-ec-00-60-08-2f-20-54')
    @commethod(3)
    def Initialize(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateNetSource(self, pszStreamName: Windows.Win32.Foundation.PWSTR, pMonitor: Windows.Win32.System.Com.IUnknown_head, pData: POINTER(Byte), pUserContext: Windows.Win32.System.Com.IUnknown_head, pCallback: Windows.Win32.System.Com.IUnknown_head, qwContext: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetSourceProperties(self, pszStreamName: Windows.Win32.Foundation.PWSTR, ppPropertiesNode: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNetSourceSharedNamespace(self, ppSharedNamespace: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNetSourceAdminInterface(self, pszStreamName: Windows.Win32.Foundation.PWSTR, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNumProtocolsSupported(self, pcProtocols: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProtocolName(self, dwProtocolNum: UInt32, pwszProtocolName: Windows.Win32.Foundation.PWSTR, pcchProtocolName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e1cd3524-03d7-11d2-9e-ed-00-60-97-d2-d7-cf')
    @commethod(3)
    def GetLength(self, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLength(self, dwLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxLength(self, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBuffer(self, ppdwBuffer: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBufferAndLength(self, ppdwBuffer: POINTER(POINTER(Byte)), pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer
    _iid_ = Guid('4f528693-1035-43fe-b4-28-75-75-61-ad-3a-68')
    @commethod(8)
    def GetSampleProperties(self, cbProperties: UInt32, pbProperties: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSampleProperties(self, cbProperties: UInt32, pbProperties: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer2
    _iid_ = Guid('c87ceaaf-75be-4bc4-84-eb-ac-27-98-50-76-72')
    @commethod(10)
    def SetProperty(self, guidBufferProperty: Guid, pvBufferProperty: c_void_p, dwBufferPropertySize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProperty(self, guidBufferProperty: Guid, pvBufferProperty: c_void_p, pdwBufferPropertySize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer4(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer3
    _iid_ = Guid('b6b8fd5a-32e2-49d4-a9-10-c2-6c-c8-54-65-ed')
    @commethod(12)
    def GetPropertyCount(self, pcBufferProperties: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPropertyByIndex(self, dwBufferPropertyIndex: UInt32, pguidBufferProperty: POINTER(Guid), pvBufferProperty: c_void_p, pdwBufferPropertySize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMAddressAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bb3c6389-1633-4e92-af-14-9f-31-73-ba-39-d0')
    @commethod(3)
    def GetAccessEntryCount(self, aeType: Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, pcEntries: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAccessEntry(self, aeType: Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, dwEntryNum: UInt32, pAddrAccessEntry: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_ADDRESS_ACCESSENTRY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddAccessEntry(self, aeType: Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, pAddrAccessEntry: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_ADDRESS_ACCESSENTRY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAccessEntry(self, aeType: Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, dwEntryNum: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMAddressAccess2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMAddressAccess
    _iid_ = Guid('65a83fc2-3e98-4d4d-81-b5-2a-74-28-86-b3-3d')
    @commethod(7)
    def GetAccessEntryEx(self, aeType: Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, dwEntryNum: UInt32, pbstrAddress: POINTER(Windows.Win32.Foundation.BSTR), pbstrMask: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddAccessEntryEx(self, aeType: Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, bstrAddress: Windows.Win32.Foundation.BSTR, bstrMask: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWMAuthorizer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d9b67d36-a9ad-4eb4-ba-ef-db-28-4e-f5-50-4c')
    @commethod(3)
    def GetCertCount(self, pcCerts: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCert(self, dwIndex: UInt32, ppbCertData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSharedData(self, dwCertIndex: UInt32, pbSharedData: POINTER(Byte), pbCert: POINTER(Byte), ppbSharedData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IWMBackupRestoreProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('3c8e0da6-996f-4ff3-a1-af-48-38-f9-37-7e-2e')
    @commethod(3)
    def GetPropCount(self, pcProps: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropByIndex(self, wIndex: UInt16, pwszName: Windows.Win32.Foundation.PWSTR, pcchNameLen: POINTER(UInt16), pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropByName(self, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProp(self, pszName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveProp(self, pcwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAllProps(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMBandwidthSharing(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMStreamList
    _iid_ = Guid('ad694af1-f8d9-42f8-bc-47-70-31-1b-0c-4f-9e')
    @commethod(6)
    def GetType(self, pguidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetType(self, guidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBandwidth(self, pdwBitrate: POINTER(UInt32), pmsBufferWindow: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBandwidth(self, dwBitrate: UInt32, msBufferWindow: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMClientConnections(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('73c66010-a299-41df-b1-f0-cc-f0-3b-09-c1-c6')
    @commethod(3)
    def GetClientCount(self, pcClients: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClientProperties(self, dwClientNum: UInt32, pClientProperties: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_CLIENT_PROPERTIES_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMClientConnections2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMClientConnections
    _iid_ = Guid('4091571e-4701-4593-bb-3d-d5-f5-f0-c7-42-46')
    @commethod(5)
    def GetClientInfo(self, dwClientNum: UInt32, pwszNetworkAddress: Windows.Win32.Foundation.PWSTR, pcchNetworkAddress: POINTER(UInt32), pwszPort: Windows.Win32.Foundation.PWSTR, pcchPort: POINTER(UInt32), pwszDNSName: Windows.Win32.Foundation.PWSTR, pcchDNSName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a970f41e-34de-4a98-b3-ba-e4-b3-ca-75-28-f0')
    @commethod(3)
    def GetCodecInfoCount(self, guidType: POINTER(Guid), pcCodecs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCodecFormatCount(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pcFormat: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCodecFormat(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, dwFormatIndex: UInt32, ppIStreamConfig: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecInfo2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMCodecInfo
    _iid_ = Guid('aa65e273-b686-4056-91-ec-dd-76-8d-4d-f7-10')
    @commethod(6)
    def GetCodecName(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, wszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCodecFormatDesc(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, dwFormatIndex: UInt32, ppIStreamConfig: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head), wszDesc: Windows.Win32.Foundation.PWSTR, pcchDesc: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecInfo3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMCodecInfo2
    _iid_ = Guid('7e51f487-4d93-4f98-8a-b4-27-d0-56-5a-dc-51')
    @commethod(8)
    def GetCodecFormatProp(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, dwFormatIndex: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCodecProp(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCodecEnumerationSetting(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pszName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), dwSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCodecEnumerationSetting(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCredentialCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('342e0eb7-e651-450c-97-5b-2a-ce-2c-90-c4-8e')
    @commethod(3)
    def AcquireCredentials(self, pwszRealm: Windows.Win32.Foundation.PWSTR, pwszSite: Windows.Win32.Foundation.PWSTR, pwszUser: Windows.Win32.Foundation.PWSTR, cchUser: UInt32, pwszPassword: Windows.Win32.Foundation.PWSTR, cchPassword: UInt32, hrStatus: Windows.Win32.Foundation.HRESULT, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMEditor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('ff130ebc-a6c3-42a6-b4-01-c3-38-2c-3e-08-b3')
    @commethod(3)
    def GetDRMProperty(self, pwstrName: Windows.Win32.Foundation.PWSTR, pdwType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMMessageParser(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a73a0072-25a0-4c99-b4-a5-ed-e8-10-1a-6c-39')
    @commethod(3)
    def ParseRegistrationReqMsg(self, pbRegistrationReqMsg: POINTER(Byte), cbRegistrationReqMsg: UInt32, ppDeviceCert: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pDeviceSerialNumber: POINTER(Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ParseLicenseRequestMsg(self, pbLicenseRequestMsg: POINTER(Byte), cbLicenseRequestMsg: UInt32, ppDeviceCert: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pDeviceSerialNumber: POINTER(Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16_head), pbstrAction: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d2827540-3ee7-432c-b1-4c-dc-17-f0-85-d3-b3')
    @commethod(3)
    def AcquireLicense(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseAcquisition(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Individualize(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CancelIndividualization(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MonitorLicenseAcquisition(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelMonitorLicenseAcquisition(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetDRMProperty(self, pwstrName: Windows.Win32.Foundation.PWSTR, dwType: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDRMProperty(self, pwstrName: Windows.Win32.Foundation.PWSTR, pdwType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMReader2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMDRMReader
    _iid_ = Guid('befe7a75-9f1d-4075-b9-d9-a3-c3-7b-da-49-a0')
    @commethod(11)
    def SetEvaluateOutputLevelLicenses(self, fEvaluate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPlayOutputLevels(self, pPlayOPL: POINTER(Windows.Win32.Media.WindowsMediaFormat.DRM_PLAY_OPL_head), pcbLength: POINTER(UInt32), pdwMinAppComplianceLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCopyOutputLevels(self, pCopyOPL: POINTER(Windows.Win32.Media.WindowsMediaFormat.DRM_COPY_OPL_head), pcbLength: POINTER(UInt32), pdwMinAppComplianceLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TryNextLicense(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMReader3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMDRMReader2
    _iid_ = Guid('e08672de-f1e7-4ff4-a0-a3-fc-4b-08-e4-ca-f8')
    @commethod(15)
    def GetInclusionList(self, ppGuids: POINTER(POINTER(Guid)), pcGuids: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMTranscryptionManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('b1a887b2-a4f0-407a-b0-2e-ef-bd-23-bb-ec-df')
    @commethod(3)
    def CreateTranscryptor(self, ppTranscryptor: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMDRMTranscryptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMTranscryptor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('69059850-6e6f-4bb2-80-6f-71-86-3d-df-c4-71')
    @commethod(3)
    def Initialize(self, bstrFileName: Windows.Win32.Foundation.BSTR, pbLicenseRequestMsg: POINTER(Byte), cbLicenseRequestMsg: UInt32, ppLicenseResponseMsg: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Seek(self, hnsTime: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Read(self, pbData: POINTER(Byte), pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMTranscryptor2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMDRMTranscryptor
    _iid_ = Guid('e0da439f-d331-496a-be-ce-18-e5-ba-c5-dd-23')
    @commethod(7)
    def SeekEx(self, cnsStartTime: UInt64, cnsDuration: UInt64, flRate: Single, fIncludeFileHeader: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ZeroAdjustTimestamps(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSeekStartTime(self, pcnsTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDuration(self, pcnsDuration: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMWriter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d6ea5dd0-12a0-43f4-90-ab-a3-fd-45-1e-6a-07')
    @commethod(3)
    def GenerateKeySeed(self, pwszKeySeed: Windows.Win32.Foundation.PWSTR, pcwchLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GenerateKeyID(self, pwszKeyID: Windows.Win32.Foundation.PWSTR, pcwchLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GenerateSigningKeyPair(self, pwszPrivKey: Windows.Win32.Foundation.PWSTR, pcwchPrivKeyLength: POINTER(UInt32), pwszPubKey: Windows.Win32.Foundation.PWSTR, pcwchPubKeyLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDRMAttribute(self, wStreamNum: UInt16, pszName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMWriter2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMDRMWriter
    _iid_ = Guid('38ee7a94-40e2-4e10-aa-3f-33-fd-32-10-ed-5b')
    @commethod(7)
    def SetWMDRMNetEncryption(self, fSamplesEncrypted: Windows.Win32.Foundation.BOOL, pbKeyID: POINTER(Byte), cbKeyID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDRMWriter3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMDRMWriter2
    _iid_ = Guid('a7184082-a4aa-4dde-ac-9c-e7-5d-bd-11-17-ce')
    @commethod(8)
    def SetProtectStreamSamples(self, pImportInitStruct: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMDRM_IMPORT_INIT_STRUCT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceRegistration(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f6211f03-8d21-4e94-93-e6-85-10-80-5f-2d-99')
    @commethod(3)
    def RegisterDevice(self, dwRegisterType: UInt32, pbCertificate: POINTER(Byte), cbCertificate: UInt32, SerialNumber: Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16, ppDevice: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterDevice(self, dwRegisterType: UInt32, pbCertificate: POINTER(Byte), cbCertificate: UInt32, SerialNumber: Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRegistrationStats(self, dwRegisterType: UInt32, pcRegisteredDevices: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFirstRegisteredDevice(self, dwRegisterType: UInt32, ppDevice: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNextRegisteredDevice(self, ppDevice: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRegisteredDeviceByID(self, dwRegisterType: UInt32, pbCertificate: POINTER(Byte), cbCertificate: UInt32, SerialNumber: Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16, ppDevice: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMGetSecureChannel(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('94bc0598-c3d2-11d3-be-df-00-c0-4f-61-29-86')
    @commethod(3)
    def GetPeerSecureChannelInterface(self, ppPeer: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMSecureChannel_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMHeaderInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bda-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetAttributeCount(self, wStreamNum: UInt16, pcAttributes: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttributeByIndex(self, wIndex: UInt16, pwStreamNum: POINTER(UInt16), pwszName: Windows.Win32.Foundation.PWSTR, pcchNameLen: POINTER(UInt16), pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributeByName(self, pwStreamNum: POINTER(UInt16), pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAttribute(self, wStreamNum: UInt16, pszName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMarkerCount(self, pcMarkers: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMarker(self, wIndex: UInt16, pwszMarkerName: Windows.Win32.Foundation.PWSTR, pcchMarkerNameLen: POINTER(UInt16), pcnsMarkerTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddMarker(self, pwszMarkerName: Windows.Win32.Foundation.PWSTR, cnsMarkerTime: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveMarker(self, wIndex: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetScriptCount(self, pcScripts: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetScript(self, wIndex: UInt16, pwszType: Windows.Win32.Foundation.PWSTR, pcchTypeLen: POINTER(UInt16), pwszCommand: Windows.Win32.Foundation.PWSTR, pcchCommandLen: POINTER(UInt16), pcnsScriptTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddScript(self, pwszType: Windows.Win32.Foundation.PWSTR, pwszCommand: Windows.Win32.Foundation.PWSTR, cnsScriptTime: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RemoveScript(self, wIndex: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IWMHeaderInfo2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMHeaderInfo
    _iid_ = Guid('15cf9781-454e-482e-b3-93-85-fa-e4-87-a8-10')
    @commethod(15)
    def GetCodecInfoCount(self, pcCodecInfos: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCodecInfo(self, wIndex: UInt32, pcchName: POINTER(UInt16), pwszName: Windows.Win32.Foundation.PWSTR, pcchDescription: POINTER(UInt16), pwszDescription: Windows.Win32.Foundation.PWSTR, pCodecType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE), pcbCodecInfo: POINTER(UInt16), pbCodecInfo: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMHeaderInfo3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMHeaderInfo2
    _iid_ = Guid('15cc68e3-27cc-4ecd-b2-22-3f-5d-02-d8-0b-d5')
    @commethod(17)
    def GetAttributeCountEx(self, wStreamNum: UInt16, pcAttributes: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetAttributeIndices(self, wStreamNum: UInt16, pwszName: Windows.Win32.Foundation.PWSTR, pwLangIndex: POINTER(UInt16), pwIndices: POINTER(UInt16), pwCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAttributeByIndexEx(self, wStreamNum: UInt16, wIndex: UInt16, pwszName: Windows.Win32.Foundation.PWSTR, pwNameLen: POINTER(UInt16), pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pwLangIndex: POINTER(UInt16), pValue: POINTER(Byte), pdwDataLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ModifyAttribute(self, wStreamNum: UInt16, wIndex: UInt16, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, wLangIndex: UInt16, pValue: POINTER(Byte), dwLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddAttribute(self, wStreamNum: UInt16, pszName: Windows.Win32.Foundation.PWSTR, pwIndex: POINTER(UInt16), Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, wLangIndex: UInt16, pValue: POINTER(Byte), dwLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DeleteAttribute(self, wStreamNum: UInt16, wIndex: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddCodecInfo(self, pwszName: Windows.Win32.Foundation.PWSTR, pwszDescription: Windows.Win32.Foundation.PWSTR, codecType: Windows.Win32.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE, cbCodecInfo: UInt16, pbCodecInfo: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMIStreamProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6816dad3-2b4b-4c8e-81-49-87-4c-34-83-a7-53')
    @commethod(3)
    def GetProperty(self, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMImageInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f0aa3b6-7267-4d89-88-f2-ba-91-5a-a5-c4-c6')
    @commethod(3)
    def GetImageCount(self, pcImages: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetImage(self, wIndex: UInt32, pcchMIMEType: POINTER(UInt16), pwszMIMEType: Windows.Win32.Foundation.PWSTR, pcchDescription: POINTER(UInt16), pwszDescription: Windows.Win32.Foundation.PWSTR, pImageType: POINTER(UInt16), pcbImageData: POINTER(UInt32), pbImageData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMIndexer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6d7cdc71-9888-11d3-8e-dc-00-c0-4f-61-09-cf')
    @commethod(3)
    def StartIndexing(self, pwszURL: Windows.Win32.Foundation.PWSTR, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMIndexer2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMIndexer
    _iid_ = Guid('b70f1e42-6255-4df0-a6-b9-02-b2-12-d9-e2-bb')
    @commethod(5)
    def Configure(self, wStreamNum: UInt16, nIndexerType: Windows.Win32.Media.WindowsMediaFormat.WMT_INDEXER_TYPE, pvInterval: c_void_p, pvIndexType: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMInputMediaProps(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps
    _iid_ = Guid('96406bd5-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(6)
    def GetConnectionName(self, pwszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGroupName(self, pwszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMLanguageList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('df683f00-2d49-4d8e-92-b7-fb-19-f6-a0-dc-57')
    @commethod(3)
    def GetLanguageCount(self, pwCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLanguageDetails(self, wIndex: UInt16, pwszLanguageString: Windows.Win32.Foundation.PWSTR, pcchLanguageStringLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddLanguageByRFC1766String(self, pwszLanguageString: Windows.Win32.Foundation.PWSTR, pwIndex: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMLicenseBackup(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('05e5ac9f-3fb6-4508-bb-43-a4-06-7b-a1-eb-e8')
    @commethod(3)
    def BackupLicenses(self, dwFlags: UInt32, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseBackup(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMLicenseRestore(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('c70b6334-a22e-4efb-a2-45-15-e6-5a-00-4a-13')
    @commethod(3)
    def RestoreLicenses(self, dwFlags: UInt32, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseRestore(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMLicenseRevocationAgent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6967f2c9-4e26-4b57-88-94-79-98-80-f7-ac-7b')
    @commethod(3)
    def GetLRBChallenge(self, pMachineID: POINTER(Byte), dwMachineIDLength: UInt32, pChallenge: POINTER(Byte), dwChallengeLength: UInt32, pChallengeOutput: POINTER(Byte), pdwChallengeOutputLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessLRB(self, pSignedLRB: POINTER(Byte), dwSignedLRBLength: UInt32, pSignedACK: POINTER(Byte), pdwSignedACKLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMMediaProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bce-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetType(self, pguidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMediaType(self, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head), pcbType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMediaType(self, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMMetadataEditor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bd9-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def Open(self, pwszFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMMetadataEditor2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMMetadataEditor
    _iid_ = Guid('203cffe3-2e18-4fdf-b5-9d-6e-71-53-05-34-cf')
    @commethod(6)
    def OpenEx(self, pwszFilename: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMMutualExclusion(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMStreamList
    _iid_ = Guid('96406bde-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(6)
    def GetType(self, pguidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetType(self, guidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMMutualExclusion2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion
    _iid_ = Guid('0302b57d-89d1-4ba2-85-c9-16-6f-2c-53-eb-91')
    @commethod(8)
    def GetName(self, pwszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetName(self, pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCount(self, pwRecordCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddRecord(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveRecord(self, wRecordNumber: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordName(self, wRecordNumber: UInt16, pwszRecordName: Windows.Win32.Foundation.PWSTR, pcchRecordName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetRecordName(self, wRecordNumber: UInt16, pwszRecordName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStreamsForRecord(self, wRecordNumber: UInt16, pwStreamNumArray: POINTER(UInt16), pcStreams: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddStreamForRecord(self, wRecordNumber: UInt16, wStreamNumber: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RemoveStreamForRecord(self, wRecordNumber: UInt16, wStreamNumber: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IWMOutputMediaProps(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps
    _iid_ = Guid('96406bd7-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(6)
    def GetStreamGroupName(self, pwszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConnectionName(self, pwszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMPacketSize(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('cdfb97ab-188f-40b3-b6-43-5b-79-03-97-5c-59')
    @commethod(3)
    def GetMaxPacketSize(self, pdwMaxPacketSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMaxPacketSize(self, dwMaxPacketSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMPacketSize2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMPacketSize
    _iid_ = Guid('8bfc2b9e-b646-4233-a8-77-1c-6a-07-96-69-dc')
    @commethod(5)
    def GetMinPacketSize(self, pdwMinPacketSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMinPacketSize(self, dwMinPacketSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMPlayerHook(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e5b7ca9a-0f1c-4f66-90-02-74-ec-50-d8-b3-04')
    @commethod(3)
    def PreDecode(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMPlayerTimestampHook(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('28580dda-d98e-48d0-b7-ae-69-e4-73-a0-28-25')
    @commethod(3)
    def MapTimestamp(self, rtIn: Int64, prtOut: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMProfile(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bdb-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetVersion(self, pdwVersion: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetName(self, pwszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetName(self, pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(self, pwszDescription: Windows.Win32.Foundation.PWSTR, pcchDescription: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDescription(self, pwszDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamCount(self, pcStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStream(self, dwStreamIndex: UInt32, ppConfig: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStreamByNumber(self, wStreamNum: UInt16, ppConfig: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveStream(self, pConfig: Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveStreamByNumber(self, wStreamNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddStream(self, pConfig: Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ReconfigStream(self, pConfig: Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateNewStream(self, guidStreamType: POINTER(Guid), ppConfig: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMutualExclusionCount(self, pcME: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetMutualExclusion(self, dwMEIndex: UInt32, ppME: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveMutualExclusion(self, pME: Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddMutualExclusion(self, pME: Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateNewMutualExclusion(self, ppME: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMProfile2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMProfile
    _iid_ = Guid('07e72d33-d94e-4be7-88-43-60-ae-5f-f7-e5-f5')
    @commethod(21)
    def GetProfileID(self, pguidID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMProfile3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMProfile2
    _iid_ = Guid('00ef96cc-a461-4546-8b-cd-c9-a2-8f-0e-06-f5')
    @commethod(22)
    def GetStorageFormat(self, pnStorageFormat: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetStorageFormat(self, nStorageFormat: Windows.Win32.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBandwidthSharingCount(self, pcBS: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetBandwidthSharing(self, dwBSIndex: UInt32, ppBS: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RemoveBandwidthSharing(self, pBS: Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def AddBandwidthSharing(self, pBS: Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreateNewBandwidthSharing(self, ppBS: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetStreamPrioritization(self, ppSP: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMStreamPrioritization_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetStreamPrioritization(self, pSP: Windows.Win32.Media.WindowsMediaFormat.IWMStreamPrioritization_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def RemoveStreamPrioritization(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateNewStreamPrioritization(self, ppSP: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMStreamPrioritization_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetExpectedPacketCount(self, msDuration: UInt64, pcPackets: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMProfileManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d16679f2-6ca0-472d-8d-31-2f-5d-55-ae-e1-55')
    @commethod(3)
    def CreateEmptyProfile(self, dwVersion: Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION, ppProfile: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadProfileByID(self, guidProfile: POINTER(Guid), ppProfile: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadProfileByData(self, pwszProfile: Windows.Win32.Foundation.PWSTR, ppProfile: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SaveProfile(self, pIWMProfile: Windows.Win32.Media.WindowsMediaFormat.IWMProfile_head, pwszProfile: Windows.Win32.Foundation.PWSTR, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSystemProfileCount(self, pcProfiles: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def LoadSystemProfile(self, dwProfileIndex: UInt32, ppProfile: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMProfileManager2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMProfileManager
    _iid_ = Guid('7a924e51-73c1-494d-80-19-23-d3-7e-d9-b8-9a')
    @commethod(9)
    def GetSystemProfileVersion(self, pdwVersion: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSystemProfileVersion(self, dwVersion: Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION) -> Windows.Win32.Foundation.HRESULT: ...
class IWMProfileManagerLanguage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('ba4dcc78-7ee0-4ab8-b2-7a-db-ce-8b-c5-14-54')
    @commethod(3)
    def GetUserLanguageID(self, wLangID: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetUserLanguageID(self, wLangID: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IWMPropertyVault(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('72995a79-5090-42a4-9c-8c-d9-d0-b6-d3-4b-e5')
    @commethod(3)
    def GetPropertyCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyByName(self, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(self, pszName: Windows.Win32.Foundation.PWSTR, pType: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), dwSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyByIndex(self, dwIndex: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pdwNameLen: POINTER(UInt32), pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPropertiesFrom(self, pIWMPropertyVault: Windows.Win32.Media.WindowsMediaFormat.IWMPropertyVault_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMProximityDetection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6a9fd8ee-b651-4bf0-b8-49-7d-4e-ce-79-a2-b1')
    @commethod(3)
    def StartDetection(self, pbRegistrationMsg: POINTER(Byte), cbRegistrationMsg: UInt32, pbLocalAddress: POINTER(Byte), cbLocalAddress: UInt32, dwExtraPortsAllowed: UInt32, ppRegistrationResponseMsg: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bd6-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def Open(self, pwszURL: Windows.Win32.Foundation.PWSTR, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMReaderCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputCount(self, pcOutputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputProps(self, dwOutputNum: UInt32, ppOutput: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetOutputProps(self, dwOutputNum: UInt32, pOutput: Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputFormatCount(self, dwOutputNumber: UInt32, pcFormats: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOutputFormat(self, dwOutputNumber: UInt32, dwFormatNumber: UInt32, ppProps: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Start(self, cnsStart: UInt64, cnsDuration: UInt64, fRate: Single, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAccelerator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bddc4d08-944d-4d52-a6-12-46-c3-fd-a0-7d-d4')
    @commethod(3)
    def GetCodecInterface(self, dwOutputNum: UInt32, riid: POINTER(Guid), ppvCodecInterface: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Notify(self, dwOutputNum: UInt32, pSubtype: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bea-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def SetUserProvidedClock(self, fUserClock: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUserProvidedClock(self, pfUserClock: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeliverTime(self, cnsTime: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetManualStreamSelection(self, fSelection: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetManualStreamSelection(self, pfSelection: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetStreamsSelected(self, cStreamCount: UInt16, pwStreamNumbers: POINTER(UInt16), pSelections: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreamSelected(self, wStreamNum: UInt16, pSelection: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetReceiveSelectionCallbacks(self, fGetCallbacks: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetReceiveSelectionCallbacks(self, pfGetCallbacks: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetReceiveStreamSamples(self, wStreamNum: UInt16, fReceiveStreamSamples: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetReceiveStreamSamples(self, wStreamNum: UInt16, pfReceiveStreamSamples: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetAllocateForOutput(self, dwOutputNum: UInt32, fAllocate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetAllocateForOutput(self, dwOutputNum: UInt32, pfAllocate: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetAllocateForStream(self, wStreamNum: UInt16, fAllocate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetAllocateForStream(self, dwSreamNum: UInt16, pfAllocate: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStatistics(self, pStatistics: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_READER_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetClientInfo(self, pClientInfo: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_READER_CLIENTINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetMaxOutputSampleSize(self, dwOutput: UInt32, pcbMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetMaxStreamSampleSize(self, wStream: UInt16, pcbMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def NotifyLateDelivery(self, cnsLateness: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced
    _iid_ = Guid('ae14a945-b90c-4d0d-91-27-80-d6-65-f7-d7-3e')
    @commethod(23)
    def SetPlayMode(self, Mode: Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetPlayMode(self, pMode: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetBufferProgress(self, pdwPercent: POINTER(UInt32), pcnsBuffering: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetDownloadProgress(self, pdwPercent: POINTER(UInt32), pqwBytesDownloaded: POINTER(UInt64), pcnsDownload: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetSaveAsProgress(self, pdwPercent: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SaveFileAs(self, pwszFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetProtocolName(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pcchProtocol: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def StartAtMarker(self, wMarkerIndex: UInt16, cnsDuration: UInt64, fRate: Single, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetOutputSetting(self, dwOutputNum: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetOutputSetting(self, dwOutputNum: UInt32, pszName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def Preroll(self, cnsStart: UInt64, cnsDuration: UInt64, fRate: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetLogClientID(self, fLogClientID: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetLogClientID(self, pfLogClientID: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def StopBuffering(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def OpenStream(self, pStream: Windows.Win32.System.Com.IStream_head, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMReaderCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced2
    _iid_ = Guid('5dc0674b-f04b-4a4e-9f-2a-b1-af-de-2c-81-00')
    @commethod(38)
    def StopNetStreaming(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def StartAtPosition(self, wStreamNum: UInt16, pvOffsetStart: c_void_p, pvDuration: c_void_p, dwOffsetFormat: Windows.Win32.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT, fRate: Single, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced4(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced3
    _iid_ = Guid('945a76a2-12ae-4d48-bd-3c-cd-1d-90-39-9b-85')
    @commethod(40)
    def GetLanguageCount(self, dwOutputNum: UInt32, pwLanguageCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetLanguage(self, dwOutputNum: UInt32, wLanguage: UInt16, pwszLanguageString: Windows.Win32.Foundation.PWSTR, pcchLanguageStringLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetMaxSpeedFactor(self, pdblFactor: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IsUsingFastCache(self, pfUsingFastCache: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def AddLogParam(self, wszNameSpace: Windows.Win32.Foundation.PWSTR, wszName: Windows.Win32.Foundation.PWSTR, wszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SendLogParams(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CanSaveFileAs(self, pfCanSave: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def CancelSaveFileAs(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetURL(self, pwszURL: Windows.Win32.Foundation.PWSTR, pcchURL: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced5(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced4
    _iid_ = Guid('24c44db0-55d1-49ae-a5-cc-f1-38-15-e3-63-63')
    @commethod(49)
    def SetPlayerHook(self, dwOutputNum: UInt32, pHook: Windows.Win32.Media.WindowsMediaFormat.IWMPlayerHook_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced6(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced5
    _iid_ = Guid('18a2e7f8-428f-4acd-8a-00-e6-46-39-bc-93-de')
    @commethod(50)
    def SetProtectStreamSamples(self, pbCertificate: POINTER(Byte), cbCertificate: UInt32, dwCertificateType: UInt32, dwFlags: UInt32, pbInitializationVector: POINTER(Byte), pcbInitializationVector: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAllocatorEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9f762fa7-a22e-428d-93-c9-ac-82-f3-aa-fe-5a')
    @commethod(3)
    def AllocateForStreamEx(self, wStreamNum: UInt16, cbBuffer: UInt32, ppBuffer: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), dwFlags: UInt32, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateForOutputEx(self, dwOutputNum: UInt32, cbBuffer: UInt32, ppBuffer: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), dwFlags: UInt32, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderCallback(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback
    _iid_ = Guid('96406bd8-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(4)
    def OnSample(self, dwOutputNum: UInt32, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderCallbackAdvanced(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406beb-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def OnStreamSample(self, wStreamNum: UInt16, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTime(self, cnsCurrentTime: UInt64, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnStreamSelection(self, wStreamCount: UInt16, pStreamNumbers: POINTER(UInt16), pSelections: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION), pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnOutputPropsChanged(self, dwOutputNum: UInt32, pMediaType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head), pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AllocateForStream(self, wStreamNum: UInt16, cbBuffer: UInt32, ppBuffer: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AllocateForOutput(self, dwOutputNum: UInt32, cbBuffer: UInt32, ppBuffer: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderNetworkConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bec-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetBufferingTime(self, pcnsBufferingTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBufferingTime(self, cnsBufferingTime: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUDPPortRanges(self, pRangeArray: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_PORT_NUMBER_RANGE_head), pcRanges: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetUDPPortRanges(self, pRangeArray: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_PORT_NUMBER_RANGE_head), cRanges: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProxySettings(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pProxySetting: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProxySettings(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, ProxySetting: Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProxyHostName(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pwszHostName: Windows.Win32.Foundation.PWSTR, pcchHostName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetProxyHostName(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pwszHostName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProxyPort(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pdwPort: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetProxyPort(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, dwPort: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetProxyExceptionList(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pwszExceptionList: Windows.Win32.Foundation.PWSTR, pcchExceptionList: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetProxyExceptionList(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pwszExceptionList: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetProxyBypassForLocal(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, pfBypassForLocal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetProxyBypassForLocal(self, pwszProtocol: Windows.Win32.Foundation.PWSTR, fBypassForLocal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetForceRerunAutoProxyDetection(self, pfForceRerunDetection: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetForceRerunAutoProxyDetection(self, fForceRerunDetection: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetEnableMulticast(self, pfEnableMulticast: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetEnableMulticast(self, fEnableMulticast: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetEnableHTTP(self, pfEnableHTTP: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetEnableHTTP(self, fEnableHTTP: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetEnableUDP(self, pfEnableUDP: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetEnableUDP(self, fEnableUDP: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetEnableTCP(self, pfEnableTCP: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetEnableTCP(self, fEnableTCP: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def ResetProtocolRollover(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetConnectionBandwidth(self, pdwConnectionBandwidth: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetConnectionBandwidth(self, dwConnectionBandwidth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetNumProtocolsSupported(self, pcProtocols: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetSupportedProtocolName(self, dwProtocolNum: UInt32, pwszProtocolName: Windows.Win32.Foundation.PWSTR, pcchProtocolName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def AddLoggingUrl(self, pwszUrl: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetLoggingUrl(self, dwIndex: UInt32, pwszUrl: Windows.Win32.Foundation.PWSTR, pcchUrl: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetLoggingUrlCount(self, pdwUrlCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ResetLoggingUrlList(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderNetworkConfig2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMReaderNetworkConfig
    _iid_ = Guid('d979a853-042b-4050-83-87-c9-39-db-22-01-3f')
    @commethod(36)
    def GetEnableContentCaching(self, pfEnableContentCaching: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetEnableContentCaching(self, fEnableContentCaching: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetEnableFastCache(self, pfEnableFastCache: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetEnableFastCache(self, fEnableFastCache: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetAcceleratedStreamingDuration(self, pcnsAccelDuration: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetAcceleratedStreamingDuration(self, cnsAccelDuration: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetAutoReconnectLimit(self, pdwAutoReconnectLimit: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetAutoReconnectLimit(self, dwAutoReconnectLimit: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetEnableResends(self, pfEnableResends: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetEnableResends(self, fEnableResends: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetEnableThinning(self, pfEnableThinning: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def SetEnableThinning(self, fEnableThinning: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetMaxNetPacketSize(self, pdwMaxNetPacketSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderPlaylistBurn(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f28c0300-9baa-4477-a8-46-17-44-d9-cb-f5-33')
    @commethod(3)
    def InitPlaylistBurn(self, cFiles: UInt32, ppwszFilenames: POINTER(Windows.Win32.Foundation.PWSTR), pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInitResults(self, cFiles: UInt32, phrStati: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndPlaylistBurn(self, hrBurnResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderStreamClock(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bed-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetTime(self, pcnsNow: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTimer(self, cnsWhen: UInt64, pvParam: c_void_p, pdwTimerId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def KillTimer(self, dwTimerId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderTimecode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f369e2f0-e081-4fe6-84-50-b8-10-b2-f4-10-d1')
    @commethod(3)
    def GetTimecodeRangeCount(self, wStreamNum: UInt16, pwRangeCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimecodeRangeBounds(self, wStreamNum: UInt16, wRangeNum: UInt16, pStartTimecode: POINTER(UInt32), pEndTimecode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMReaderTypeNegotiation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('fdbe5592-81a1-41ea-93-bd-73-5c-ad-1a-dc-05')
    @commethod(3)
    def TryOutputProps(self, dwOutputNum: UInt32, pOutput: Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWMRegisterCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('cf4b1f99-4de2-4e49-a3-63-25-27-40-d9-9b-c1')
    @commethod(3)
    def Advise(self, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMRegisteredDevice(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a4503bec-5508-4148-97-ac-bf-a7-57-60-a7-0d')
    @commethod(3)
    def GetDeviceSerialNumber(self, pSerialNumber: POINTER(Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceCertificate(self, ppCertificate: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeviceType(self, pdwType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributeCount(self, pcAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAttributeByIndex(self, dwIndex: UInt32, pbstrName: POINTER(Windows.Win32.Foundation.BSTR), pbstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAttributeByName(self, bstrName: Windows.Win32.Foundation.BSTR, pbstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAttributeByName(self, bstrName: Windows.Win32.Foundation.BSTR, bstrValue: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Approve(self, fApprove: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsValid(self, pfValid: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsApproved(self, pfApproved: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsWmdrmCompliant(self, pfCompliant: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsOpened(self, pfOpened: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Open(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSBufferAllocator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('61103ca4-2033-11d2-9e-f1-00-60-97-d2-d7-cf')
    @commethod(3)
    def AllocateBuffer(self, dwMaxBufferSize: UInt32, ppBuffer: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocatePageSizeBuffer(self, dwMaxBufferSize: UInt32, ppBuffer: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSInternalAdminNetSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('8bb23e5f-d127-4afb-8d-02-ae-5b-66-d5-4c-78')
    @commethod(3)
    def Initialize(self, pSharedNamespace: Windows.Win32.System.Com.IUnknown_head, pNamespaceNode: Windows.Win32.System.Com.IUnknown_head, pNetSourceCreator: Windows.Win32.Media.WindowsMediaFormat.INSNetSourceCreator_head, fEmbeddedInServer: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNetSourceCreator(self, ppNetSourceCreator: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSNetSourceCreator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCredentials(self, bstrRealm: Windows.Win32.Foundation.BSTR, bstrName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, fPersist: Windows.Win32.Foundation.BOOL, fConfirmedGood: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCredentials(self, bstrRealm: Windows.Win32.Foundation.BSTR, pbstrName: POINTER(Windows.Win32.Foundation.BSTR), pbstrPassword: POINTER(Windows.Win32.Foundation.BSTR), pfConfirmedGood: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteCredentials(self, bstrRealm: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCredentialFlags(self, lpdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetCredentialFlags(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindProxyForURL(self, bstrProtocol: Windows.Win32.Foundation.BSTR, bstrHost: Windows.Win32.Foundation.BSTR, pfProxyEnabled: POINTER(Windows.Win32.Foundation.BOOL), pbstrProxyServer: POINTER(Windows.Win32.Foundation.BSTR), pdwProxyPort: POINTER(UInt32), pdwProxyContext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterProxyFailure(self, hrParam: Windows.Win32.Foundation.HRESULT, dwProxyContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ShutdownProxyContext(self, dwProxyContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsUsingIE(self, dwProxyContext: UInt32, pfIsUsingIE: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSInternalAdminNetSource2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e74d58c3-cf77-4b51-af-17-74-46-87-c4-3e-ae')
    @commethod(3)
    def SetCredentialsEx(self, bstrRealm: Windows.Win32.Foundation.BSTR, bstrUrl: Windows.Win32.Foundation.BSTR, fProxy: Windows.Win32.Foundation.BOOL, bstrName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, fPersist: Windows.Win32.Foundation.BOOL, fConfirmedGood: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCredentialsEx(self, bstrRealm: Windows.Win32.Foundation.BSTR, bstrUrl: Windows.Win32.Foundation.BSTR, fProxy: Windows.Win32.Foundation.BOOL, pdwUrlPolicy: POINTER(Windows.Win32.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS), pbstrName: POINTER(Windows.Win32.Foundation.BSTR), pbstrPassword: POINTER(Windows.Win32.Foundation.BSTR), pfConfirmedGood: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteCredentialsEx(self, bstrRealm: Windows.Win32.Foundation.BSTR, bstrUrl: Windows.Win32.Foundation.BSTR, fProxy: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindProxyForURLEx(self, bstrProtocol: Windows.Win32.Foundation.BSTR, bstrHost: Windows.Win32.Foundation.BSTR, bstrUrl: Windows.Win32.Foundation.BSTR, pfProxyEnabled: POINTER(Windows.Win32.Foundation.BOOL), pbstrProxyServer: POINTER(Windows.Win32.Foundation.BSTR), pdwProxyPort: POINTER(UInt32), pdwProxyContext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSInternalAdminNetSource3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMSInternalAdminNetSource2
    _iid_ = Guid('6b63d08e-4590-44af-9e-b3-57-ff-1e-73-bf-80')
    @commethod(7)
    def GetNetSourceCreator2(self, ppNetSourceCreator: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindProxyForURLEx2(self, bstrProtocol: Windows.Win32.Foundation.BSTR, bstrHost: Windows.Win32.Foundation.BSTR, bstrUrl: Windows.Win32.Foundation.BSTR, pfProxyEnabled: POINTER(Windows.Win32.Foundation.BOOL), pbstrProxyServer: POINTER(Windows.Win32.Foundation.BSTR), pdwProxyPort: POINTER(UInt32), pqwProxyContext: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterProxyFailure2(self, hrParam: Windows.Win32.Foundation.HRESULT, qwProxyContext: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ShutdownProxyContext2(self, qwProxyContext: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsUsingIE2(self, qwProxyContext: UInt64, pfIsUsingIE: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCredentialsEx2(self, bstrRealm: Windows.Win32.Foundation.BSTR, bstrUrl: Windows.Win32.Foundation.BSTR, fProxy: Windows.Win32.Foundation.BOOL, bstrName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, fPersist: Windows.Win32.Foundation.BOOL, fConfirmedGood: Windows.Win32.Foundation.BOOL, fClearTextAuthentication: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCredentialsEx2(self, bstrRealm: Windows.Win32.Foundation.BSTR, bstrUrl: Windows.Win32.Foundation.BSTR, fProxy: Windows.Win32.Foundation.BOOL, fClearTextAuthentication: Windows.Win32.Foundation.BOOL, pdwUrlPolicy: POINTER(Windows.Win32.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS), pbstrName: POINTER(Windows.Win32.Foundation.BSTR), pbstrPassword: POINTER(Windows.Win32.Foundation.BSTR), pfConfirmedGood: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSecureChannel(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMAuthorizer
    _iid_ = Guid('2720598a-d0f2-4189-bd-10-91-c4-6e-f0-93-6f')
    @commethod(6)
    def WMSC_AddCertificate(self, pCert: Windows.Win32.Media.WindowsMediaFormat.IWMAuthorizer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WMSC_AddSignature(self, pbCertSig: POINTER(Byte), cbCertSig: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WMSC_Connect(self, pOtherSide: Windows.Win32.Media.WindowsMediaFormat.IWMSecureChannel_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WMSC_IsConnected(self, pfIsConnected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WMSC_Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WMSC_GetValidCertificate(self, ppbCertificate: POINTER(POINTER(Byte)), pdwSignature: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WMSC_Encrypt(self, pbData: POINTER(Byte), cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WMSC_Decrypt(self, pbData: POINTER(Byte), cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WMSC_Lock(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WMSC_Unlock(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def WMSC_SetSharedData(self, dwCertIndex: UInt32, pbSharedData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMStatusCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6d7cdc70-9888-11d3-8e-dc-00-c0-4f-61-09-cf')
    @commethod(3)
    def OnStatus(self, Status: Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS, hr: Windows.Win32.Foundation.HRESULT, dwType: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMStreamConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bdc-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetStreamType(self, pguidStreamType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamNumber(self, pwStreamNum: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamNumber(self, wStreamNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamName(self, pwszStreamName: Windows.Win32.Foundation.PWSTR, pcchStreamName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetStreamName(self, pwszStreamName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetConnectionName(self, pwszInputName: Windows.Win32.Foundation.PWSTR, pcchInputName: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetConnectionName(self, pwszInputName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBitrate(self, pdwBitrate: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetBitrate(self, pdwBitrate: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetBufferWindow(self, pmsBufferWindow: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetBufferWindow(self, msBufferWindow: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMStreamConfig2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig
    _iid_ = Guid('7688d8cb-fc0d-43bd-94-59-5a-8d-ec-20-0c-fa')
    @commethod(14)
    def GetTransportType(self, pnTransportType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetTransportType(self, nTransportType: Windows.Win32.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddDataUnitExtension(self, guidExtensionSystemID: Guid, cbExtensionDataSize: UInt16, pbExtensionSystemInfo: POINTER(Byte), cbExtensionSystemInfo: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDataUnitExtensionCount(self, pcDataUnitExtensions: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetDataUnitExtension(self, wDataUnitExtensionNumber: UInt16, pguidExtensionSystemID: POINTER(Guid), pcbExtensionDataSize: POINTER(UInt16), pbExtensionSystemInfo: POINTER(Byte), pcbExtensionSystemInfo: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RemoveAllDataUnitExtensions(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMStreamConfig3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig2
    _iid_ = Guid('cb164104-3aa9-45a7-9a-c9-4d-ae-e1-31-d6-e1')
    @commethod(20)
    def GetLanguage(self, pwszLanguageString: Windows.Win32.Foundation.PWSTR, pcchLanguageStringLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetLanguage(self, pwszLanguageString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWMStreamList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bdd-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetStreams(self, pwStreamNumArray: POINTER(UInt16), pcStreams: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddStream(self, wStreamNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveStream(self, wStreamNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IWMStreamPrioritization(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('8c1c6090-f9a8-4748-8e-c3-dd-11-08-ba-1e-77')
    @commethod(3)
    def GetPriorityRecords(self, pRecordArray: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_STREAM_PRIORITY_RECORD_head), pcRecords: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPriorityRecords(self, pRecordArray: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_STREAM_PRIORITY_RECORD_head), cRecords: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSyncReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9397f121-7705-4dc9-b0-49-98-b6-98-18-84-14')
    @commethod(3)
    def Open(self, pwszFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRange(self, cnsStartTime: UInt64, cnsDuration: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRangeByFrame(self, wStreamNum: UInt16, qwFrameNumber: UInt64, cFramesToRead: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNextSample(self, wStreamNum: UInt16, ppSample: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pcnsSampleTime: POINTER(UInt64), pcnsDuration: POINTER(UInt64), pdwFlags: POINTER(UInt32), pdwOutputNum: POINTER(UInt32), pwStreamNum: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetStreamsSelected(self, cStreamCount: UInt16, pwStreamNumbers: POINTER(UInt16), pSelections: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreamSelected(self, wStreamNum: UInt16, pSelection: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetReadStreamSamples(self, wStreamNum: UInt16, fCompressed: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetReadStreamSamples(self, wStreamNum: UInt16, pfCompressed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetOutputSetting(self, dwOutputNum: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetOutputSetting(self, dwOutputNum: UInt32, pszName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetOutputCount(self, pcOutputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetOutputProps(self, dwOutputNum: UInt32, ppOutput: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetOutputProps(self, dwOutputNum: UInt32, pOutput: Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetOutputFormatCount(self, dwOutputNum: UInt32, pcFormats: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetOutputFormat(self, dwOutputNum: UInt32, dwFormatNum: UInt32, ppProps: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetOutputNumberForStream(self, wStreamNum: UInt16, pdwOutputNum: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetStreamNumberForOutput(self, dwOutputNum: UInt32, pwStreamNum: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetMaxOutputSampleSize(self, dwOutput: UInt32, pcbMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetMaxStreamSampleSize(self, wStream: UInt16, pcbMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def OpenStream(self, pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSyncReader2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMSyncReader
    _iid_ = Guid('faed3d21-1b6b-4af7-8c-b6-3e-18-9b-bc-18-7b')
    @commethod(24)
    def SetRangeByTimecode(self, wStreamNum: UInt16, pStart: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_EXTENSION_DATA_head), pEnd: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_EXTENSION_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetRangeByFrameEx(self, wStreamNum: UInt16, qwFrameNumber: UInt64, cFramesToRead: Int64, pcnsStartTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetAllocateForOutput(self, dwOutputNum: UInt32, pAllocator: Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetAllocateForOutput(self, dwOutputNum: UInt32, ppAllocator: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetAllocateForStream(self, wStreamNum: UInt16, pAllocator: Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetAllocateForStream(self, dwSreamNum: UInt16, ppAllocator: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMVideoMediaProps(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps
    _iid_ = Guid('96406bcf-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(6)
    def GetMaxKeyFrameSpacing(self, pllTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMaxKeyFrameSpacing(self, llTime: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuality(self, pdwQuality: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetQuality(self, dwQuality: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWatermarkInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6f497062-f2e2-4624-8e-a7-9d-d4-0d-81-fc-8d')
    @commethod(3)
    def GetWatermarkEntryCount(self, wmetType: Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWatermarkEntry(self, wmetType: Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE, dwEntryNum: UInt32, pEntry: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406bd4-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def SetProfileByID(self, guidProfile: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProfile(self, pProfile: Windows.Win32.Media.WindowsMediaFormat.IWMProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFilename(self, pwszFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputCount(self, pcInputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInputProps(self, dwInputNum: UInt32, ppInput: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMInputMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetInputProps(self, dwInputNum: UInt32, pInput: Windows.Win32.Media.WindowsMediaFormat.IWMInputMediaProps_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInputFormatCount(self, dwInputNumber: UInt32, pcFormats: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInputFormat(self, dwInputNumber: UInt32, dwFormatNumber: UInt32, pProps: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMInputMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def BeginWriting(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndWriting(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AllocateSample(self, dwSampleSize: UInt32, ppSample: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteSample(self, dwInputNum: UInt32, cnsSampleTime: UInt64, dwFlags: UInt32, pSample: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterAdvanced(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406be3-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def GetSinkCount(self, pcSinks: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSink(self, dwSinkNum: UInt32, ppSink: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddSink(self, pSink: Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveSink(self, pSink: Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WriteStreamSample(self, wStreamNum: UInt16, cnsSampleTime: UInt64, msSampleSendTime: UInt32, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetLiveSource(self, fIsLiveSource: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsRealTime(self, pfRealTime: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetWriterTime(self, pcnsCurrentTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStatistics(self, wStreamNum: UInt16, pStats: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_WRITER_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetSyncTolerance(self, msWindow: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSyncTolerance(self, pmsWindow: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterAdvanced2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMWriterAdvanced
    _iid_ = Guid('962dc1ec-c046-4db8-9c-c7-26-ce-ae-50-08-17')
    @commethod(14)
    def GetInputSetting(self, dwInputNum: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetInputSetting(self, dwInputNum: UInt32, pszName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterAdvanced3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMWriterAdvanced2
    _iid_ = Guid('2cd6492d-7c37-4e76-9d-3b-59-26-11-83-a2-2e')
    @commethod(16)
    def GetStatisticsEx(self, wStreamNum: UInt16, pStats: POINTER(Windows.Win32.Media.WindowsMediaFormat.WM_WRITER_STATISTICS_EX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetNonBlocking(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterFileSink(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink
    _iid_ = Guid('96406be5-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(8)
    def Open(self, pwszFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterFileSink2(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMWriterFileSink
    _iid_ = Guid('14282ba7-4aef-4205-8c-e5-c2-29-03-5a-05-bc')
    @commethod(9)
    def Start(self, cnsStartTime: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Stop(self, cnsStopTime: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsStopped(self, pfStopped: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFileDuration(self, pcnsDuration: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFileSize(self, pcbFile: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsClosed(self, pfClosed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterFileSink3(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMWriterFileSink2
    _iid_ = Guid('3fea4feb-2945-47a7-a1-dd-c5-3a-8f-c4-c4-5c')
    @commethod(16)
    def SetAutoIndexing(self, fDoAutoIndexing: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetAutoIndexing(self, pfAutoIndexing: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetControlStream(self, wStreamNumber: UInt16, fShouldControlStartAndStop: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetMode(self, pdwFileSinkMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnDataUnitEx(self, pFileSinkDataUnit: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_FILESINK_DATA_UNIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetUnbufferedIO(self, fUnbufferedIO: Windows.Win32.Foundation.BOOL, fRestrictMemUsage: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetUnbufferedIO(self, pfUnbufferedIO: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CompleteOperations(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterNetworkSink(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink
    _iid_ = Guid('96406be7-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(8)
    def SetMaximumClients(self, dwMaxClients: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMaximumClients(self, pdwMaxClients: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetNetworkProtocol(self, protocol: Windows.Win32.Media.WindowsMediaFormat.WMT_NET_PROTOCOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkProtocol(self, pProtocol: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_NET_PROTOCOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHostURL(self, pwszURL: Windows.Win32.Foundation.PWSTR, pcchURL: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Open(self, pdwPortNum: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPostView(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('81e20ce4-75ef-491a-80-04-fc-53-c4-5b-dc-3e')
    @commethod(3)
    def SetPostViewCallback(self, pCallback: Windows.Win32.Media.WindowsMediaFormat.IWMWriterPostViewCallback_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetReceivePostViewSamples(self, wStreamNum: UInt16, fReceivePostViewSamples: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReceivePostViewSamples(self, wStreamNum: UInt16, pfReceivePostViewSamples: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPostViewProps(self, wStreamNumber: UInt16, ppOutput: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPostViewProps(self, wStreamNumber: UInt16, pOutput: Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPostViewFormatCount(self, wStreamNumber: UInt16, pcFormats: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPostViewFormat(self, wStreamNumber: UInt16, dwFormatNumber: UInt32, ppProps: POINTER(Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetAllocateForPostView(self, wStreamNumber: UInt16, fAllocate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetAllocateForPostView(self, wStreamNumber: UInt16, pfAllocate: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPostViewCallback(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback
    _iid_ = Guid('d9d6549d-a193-4f24-b3-08-03-12-3d-9b-7f-8d')
    @commethod(4)
    def OnPostViewSample(self, wStreamNumber: UInt16, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateForPostView(self, wStreamNum: UInt16, cbBuffer: UInt32, ppBuffer: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head), pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPreprocess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('fc54a285-38c4-45b5-aa-23-85-b9-f7-cb-42-4b')
    @commethod(3)
    def GetMaxPreprocessingPasses(self, dwInputNum: UInt32, dwFlags: UInt32, pdwMaxNumPasses: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNumPreprocessingPasses(self, dwInputNum: UInt32, dwFlags: UInt32, dwNumPasses: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginPreprocessingPass(self, dwInputNum: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PreprocessSample(self, dwInputNum: UInt32, cnsSampleTime: UInt64, dwFlags: UInt32, pSample: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EndPreprocessingPass(self, dwInputNum: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPushSink(ComPtr):
    extends: Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink
    _iid_ = Guid('dc10e6a5-072c-467d-bf-57-63-30-a9-dd-e1-2a')
    @commethod(8)
    def Connect(self, pwszURL: Windows.Win32.Foundation.PWSTR, pwszTemplateURL: Windows.Win32.Foundation.PWSTR, fAutoDestroy: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndSession(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMWriterSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96406be4-2b2b-11d3-b3-6b-00-c0-4f-61-08-ff')
    @commethod(3)
    def OnHeader(self, pHeader: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsRealTime(self, pfRealTime: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateDataUnit(self, cbDataUnit: UInt32, ppDataUnit: POINTER(Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDataUnit(self, pDataUnit: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnEndWriting(self) -> Windows.Win32.Foundation.HRESULT: ...
NETSOURCE_URLCREDPOLICY_SETTINGS = Int32
NETSOURCE_URLCREDPOLICY_SETTING_SILENTLOGONOK: NETSOURCE_URLCREDPOLICY_SETTINGS = 0
NETSOURCE_URLCREDPOLICY_SETTING_MUSTPROMPTUSER: NETSOURCE_URLCREDPOLICY_SETTINGS = 1
NETSOURCE_URLCREDPOLICY_SETTING_ANONYMOUSONLY: NETSOURCE_URLCREDPOLICY_SETTINGS = 2
WEBSTREAM_SAMPLE_TYPE = Int32
WEBSTREAM_SAMPLE_TYPE_FILE: WEBSTREAM_SAMPLE_TYPE = 1
WEBSTREAM_SAMPLE_TYPE_RENDER: WEBSTREAM_SAMPLE_TYPE = 2
class WMDRM_IMPORT_INIT_STRUCT(EasyCastStructure):
    dwVersion: UInt32
    cbEncryptedSessionKeyMessage: UInt32
    pbEncryptedSessionKeyMessage: POINTER(Byte)
    cbEncryptedKeyMessage: UInt32
    pbEncryptedKeyMessage: POINTER(Byte)
class WMMPEG2VIDEOINFO(EasyCastStructure):
    hdr: Windows.Win32.Media.WindowsMediaFormat.WMVIDEOINFOHEADER2
    dwStartTimeCode: UInt32
    cbSequenceHeader: UInt32
    dwProfile: UInt32
    dwLevel: UInt32
    dwFlags: UInt32
    dwSequenceHeader: UInt32 * 1
class WMSCRIPTFORMAT(EasyCastStructure):
    scriptType: Guid
WMT_ATTR_DATATYPE = Int32
WMT_TYPE_DWORD: WMT_ATTR_DATATYPE = 0
WMT_TYPE_STRING: WMT_ATTR_DATATYPE = 1
WMT_TYPE_BINARY: WMT_ATTR_DATATYPE = 2
WMT_TYPE_BOOL: WMT_ATTR_DATATYPE = 3
WMT_TYPE_QWORD: WMT_ATTR_DATATYPE = 4
WMT_TYPE_WORD: WMT_ATTR_DATATYPE = 5
WMT_TYPE_GUID: WMT_ATTR_DATATYPE = 6
WMT_ATTR_IMAGETYPE = Int32
WMT_IMAGETYPE_BITMAP: WMT_ATTR_IMAGETYPE = 1
WMT_IMAGETYPE_JPEG: WMT_ATTR_IMAGETYPE = 2
WMT_IMAGETYPE_GIF: WMT_ATTR_IMAGETYPE = 3
class WMT_BUFFER_SEGMENT(EasyCastStructure):
    pBuffer: Windows.Win32.Media.WindowsMediaFormat.INSSBuffer_head
    cbOffset: UInt32
    cbLength: UInt32
WMT_CODEC_INFO_TYPE = Int32
WMT_CODECINFO_AUDIO: WMT_CODEC_INFO_TYPE = 0
WMT_CODECINFO_VIDEO: WMT_CODEC_INFO_TYPE = 1
WMT_CODECINFO_UNKNOWN: WMT_CODEC_INFO_TYPE = -1
class WMT_COLORSPACEINFO_EXTENSION_DATA(EasyCastStructure):
    ucColorPrimaries: Byte
    ucColorTransferChar: Byte
    ucColorMatrixCoef: Byte
WMT_CREDENTIAL_FLAGS = Int32
WMT_CREDENTIAL_SAVE: WMT_CREDENTIAL_FLAGS = 1
WMT_CREDENTIAL_DONT_CACHE: WMT_CREDENTIAL_FLAGS = 2
WMT_CREDENTIAL_CLEAR_TEXT: WMT_CREDENTIAL_FLAGS = 4
WMT_CREDENTIAL_PROXY: WMT_CREDENTIAL_FLAGS = 8
WMT_CREDENTIAL_ENCRYPT: WMT_CREDENTIAL_FLAGS = 16
WMT_DRMLA_TRUST = Int32
WMT_DRMLA_UNTRUSTED: WMT_DRMLA_TRUST = 0
WMT_DRMLA_TRUSTED: WMT_DRMLA_TRUST = 1
WMT_DRMLA_TAMPERED: WMT_DRMLA_TRUST = 2
class WMT_FILESINK_DATA_UNIT(EasyCastStructure):
    packetHeaderBuffer: Windows.Win32.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT
    cPayloads: UInt32
    pPayloadHeaderBuffers: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT_head)
    cPayloadDataFragments: UInt32
    pPayloadDataFragments: POINTER(Windows.Win32.Media.WindowsMediaFormat.WMT_PAYLOAD_FRAGMENT_head)
WMT_FILESINK_MODE = Int32
WMT_FM_SINGLE_BUFFERS: WMT_FILESINK_MODE = 1
WMT_FM_FILESINK_DATA_UNITS: WMT_FILESINK_MODE = 2
WMT_FM_FILESINK_UNBUFFERED: WMT_FILESINK_MODE = 4
WMT_IMAGE_TYPE = Int32
WMT_IT_NONE: WMT_IMAGE_TYPE = 0
WMT_IT_BITMAP: WMT_IMAGE_TYPE = 1
WMT_IT_JPEG: WMT_IMAGE_TYPE = 2
WMT_IT_GIF: WMT_IMAGE_TYPE = 3
WMT_INDEXER_TYPE = Int32
WMT_IT_PRESENTATION_TIME: WMT_INDEXER_TYPE = 0
WMT_IT_FRAME_NUMBERS: WMT_INDEXER_TYPE = 1
WMT_IT_TIMECODE: WMT_INDEXER_TYPE = 2
WMT_INDEX_TYPE = Int32
WMT_IT_NEAREST_DATA_UNIT: WMT_INDEX_TYPE = 1
WMT_IT_NEAREST_OBJECT: WMT_INDEX_TYPE = 2
WMT_IT_NEAREST_CLEAN_POINT: WMT_INDEX_TYPE = 3
WMT_MUSICSPEECH_CLASS_MODE = Int32
WMT_MS_CLASS_MUSIC: WMT_MUSICSPEECH_CLASS_MODE = 0
WMT_MS_CLASS_SPEECH: WMT_MUSICSPEECH_CLASS_MODE = 1
WMT_MS_CLASS_MIXED: WMT_MUSICSPEECH_CLASS_MODE = 2
WMT_NET_PROTOCOL = Int32
WMT_PROTOCOL_HTTP: WMT_NET_PROTOCOL = 0
WMT_OFFSET_FORMAT = Int32
WMT_OFFSET_FORMAT_100NS: WMT_OFFSET_FORMAT = 0
WMT_OFFSET_FORMAT_FRAME_NUMBERS: WMT_OFFSET_FORMAT = 1
WMT_OFFSET_FORMAT_PLAYLIST_OFFSET: WMT_OFFSET_FORMAT = 2
WMT_OFFSET_FORMAT_TIMECODE: WMT_OFFSET_FORMAT = 3
WMT_OFFSET_FORMAT_100NS_APPROXIMATE: WMT_OFFSET_FORMAT = 4
class WMT_PAYLOAD_FRAGMENT(EasyCastStructure):
    dwPayloadIndex: UInt32
    segmentData: Windows.Win32.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT
WMT_PLAY_MODE = Int32
WMT_PLAY_MODE_AUTOSELECT: WMT_PLAY_MODE = 0
WMT_PLAY_MODE_LOCAL: WMT_PLAY_MODE = 1
WMT_PLAY_MODE_DOWNLOAD: WMT_PLAY_MODE = 2
WMT_PLAY_MODE_STREAMING: WMT_PLAY_MODE = 3
WMT_PROXY_SETTINGS = Int32
WMT_PROXY_SETTING_NONE: WMT_PROXY_SETTINGS = 0
WMT_PROXY_SETTING_MANUAL: WMT_PROXY_SETTINGS = 1
WMT_PROXY_SETTING_AUTO: WMT_PROXY_SETTINGS = 2
WMT_PROXY_SETTING_BROWSER: WMT_PROXY_SETTINGS = 3
WMT_PROXY_SETTING_MAX: WMT_PROXY_SETTINGS = 4
WMT_RIGHTS = Int32
WMT_RIGHT_PLAYBACK: WMT_RIGHTS = 1
WMT_RIGHT_COPY_TO_NON_SDMI_DEVICE: WMT_RIGHTS = 2
WMT_RIGHT_COPY_TO_CD: WMT_RIGHTS = 8
WMT_RIGHT_COPY_TO_SDMI_DEVICE: WMT_RIGHTS = 16
WMT_RIGHT_ONE_TIME: WMT_RIGHTS = 32
WMT_RIGHT_SAVE_STREAM_PROTECTED: WMT_RIGHTS = 64
WMT_RIGHT_COPY: WMT_RIGHTS = 128
WMT_RIGHT_COLLABORATIVE_PLAY: WMT_RIGHTS = 256
WMT_RIGHT_SDMI_TRIGGER: WMT_RIGHTS = 65536
WMT_RIGHT_SDMI_NOMORECOPIES: WMT_RIGHTS = 131072
WMT_STATUS = Int32
WMT_ERROR: WMT_STATUS = 0
WMT_OPENED: WMT_STATUS = 1
WMT_BUFFERING_START: WMT_STATUS = 2
WMT_BUFFERING_STOP: WMT_STATUS = 3
WMT_EOF: WMT_STATUS = 4
WMT_END_OF_FILE: WMT_STATUS = 4
WMT_END_OF_SEGMENT: WMT_STATUS = 5
WMT_END_OF_STREAMING: WMT_STATUS = 6
WMT_LOCATING: WMT_STATUS = 7
WMT_CONNECTING: WMT_STATUS = 8
WMT_NO_RIGHTS: WMT_STATUS = 9
WMT_MISSING_CODEC: WMT_STATUS = 10
WMT_STARTED: WMT_STATUS = 11
WMT_STOPPED: WMT_STATUS = 12
WMT_CLOSED: WMT_STATUS = 13
WMT_STRIDING: WMT_STATUS = 14
WMT_TIMER: WMT_STATUS = 15
WMT_INDEX_PROGRESS: WMT_STATUS = 16
WMT_SAVEAS_START: WMT_STATUS = 17
WMT_SAVEAS_STOP: WMT_STATUS = 18
WMT_NEW_SOURCEFLAGS: WMT_STATUS = 19
WMT_NEW_METADATA: WMT_STATUS = 20
WMT_BACKUPRESTORE_BEGIN: WMT_STATUS = 21
WMT_SOURCE_SWITCH: WMT_STATUS = 22
WMT_ACQUIRE_LICENSE: WMT_STATUS = 23
WMT_INDIVIDUALIZE: WMT_STATUS = 24
WMT_NEEDS_INDIVIDUALIZATION: WMT_STATUS = 25
WMT_NO_RIGHTS_EX: WMT_STATUS = 26
WMT_BACKUPRESTORE_END: WMT_STATUS = 27
WMT_BACKUPRESTORE_CONNECTING: WMT_STATUS = 28
WMT_BACKUPRESTORE_DISCONNECTING: WMT_STATUS = 29
WMT_ERROR_WITHURL: WMT_STATUS = 30
WMT_RESTRICTED_LICENSE: WMT_STATUS = 31
WMT_CLIENT_CONNECT: WMT_STATUS = 32
WMT_CLIENT_DISCONNECT: WMT_STATUS = 33
WMT_NATIVE_OUTPUT_PROPS_CHANGED: WMT_STATUS = 34
WMT_RECONNECT_START: WMT_STATUS = 35
WMT_RECONNECT_END: WMT_STATUS = 36
WMT_CLIENT_CONNECT_EX: WMT_STATUS = 37
WMT_CLIENT_DISCONNECT_EX: WMT_STATUS = 38
WMT_SET_FEC_SPAN: WMT_STATUS = 39
WMT_PREROLL_READY: WMT_STATUS = 40
WMT_PREROLL_COMPLETE: WMT_STATUS = 41
WMT_CLIENT_PROPERTIES: WMT_STATUS = 42
WMT_LICENSEURL_SIGNATURE_STATE: WMT_STATUS = 43
WMT_INIT_PLAYLIST_BURN: WMT_STATUS = 44
WMT_TRANSCRYPTOR_INIT: WMT_STATUS = 45
WMT_TRANSCRYPTOR_SEEKED: WMT_STATUS = 46
WMT_TRANSCRYPTOR_READ: WMT_STATUS = 47
WMT_TRANSCRYPTOR_CLOSED: WMT_STATUS = 48
WMT_PROXIMITY_RESULT: WMT_STATUS = 49
WMT_PROXIMITY_COMPLETED: WMT_STATUS = 50
WMT_CONTENT_ENABLER: WMT_STATUS = 51
WMT_STORAGE_FORMAT = Int32
WMT_Storage_Format_MP3: WMT_STORAGE_FORMAT = 0
WMT_Storage_Format_V1: WMT_STORAGE_FORMAT = 1
WMT_STREAM_SELECTION = Int32
WMT_OFF: WMT_STREAM_SELECTION = 0
WMT_CLEANPOINT_ONLY: WMT_STREAM_SELECTION = 1
WMT_ON: WMT_STREAM_SELECTION = 2
class WMT_TIMECODE_EXTENSION_DATA(EasyCastStructure):
    wRange: UInt16
    dwTimecode: UInt32
    dwUserbits: UInt32
    dwAmFlags: UInt32
    _pack_ = 2
WMT_TIMECODE_FRAMERATE = Int32
WMT_TIMECODE_FRAMERATE_30: WMT_TIMECODE_FRAMERATE = 0
WMT_TIMECODE_FRAMERATE_30DROP: WMT_TIMECODE_FRAMERATE = 1
WMT_TIMECODE_FRAMERATE_25: WMT_TIMECODE_FRAMERATE = 2
WMT_TIMECODE_FRAMERATE_24: WMT_TIMECODE_FRAMERATE = 3
WMT_TRANSPORT_TYPE = Int32
WMT_Transport_Type_Unreliable: WMT_TRANSPORT_TYPE = 0
WMT_Transport_Type_Reliable: WMT_TRANSPORT_TYPE = 1
WMT_VERSION = Int32
WMT_VER_4_0: WMT_VERSION = 262144
WMT_VER_7_0: WMT_VERSION = 458752
WMT_VER_8_0: WMT_VERSION = 524288
WMT_VER_9_0: WMT_VERSION = 589824
class WMT_VIDEOIMAGE_SAMPLE(EasyCastStructure):
    dwMagic: UInt32
    cbStruct: UInt32
    dwControlFlags: UInt32
    dwInputFlagsCur: UInt32
    lCurMotionXtoX: Int32
    lCurMotionYtoX: Int32
    lCurMotionXoffset: Int32
    lCurMotionXtoY: Int32
    lCurMotionYtoY: Int32
    lCurMotionYoffset: Int32
    lCurBlendCoef1: Int32
    lCurBlendCoef2: Int32
    dwInputFlagsPrev: UInt32
    lPrevMotionXtoX: Int32
    lPrevMotionYtoX: Int32
    lPrevMotionXoffset: Int32
    lPrevMotionXtoY: Int32
    lPrevMotionYtoY: Int32
    lPrevMotionYoffset: Int32
    lPrevBlendCoef1: Int32
    lPrevBlendCoef2: Int32
class WMT_VIDEOIMAGE_SAMPLE2(EasyCastStructure):
    dwMagic: UInt32
    dwStructSize: UInt32
    dwControlFlags: UInt32
    dwViewportWidth: UInt32
    dwViewportHeight: UInt32
    dwCurrImageWidth: UInt32
    dwCurrImageHeight: UInt32
    fCurrRegionX0: Single
    fCurrRegionY0: Single
    fCurrRegionWidth: Single
    fCurrRegionHeight: Single
    fCurrBlendCoef: Single
    dwPrevImageWidth: UInt32
    dwPrevImageHeight: UInt32
    fPrevRegionX0: Single
    fPrevRegionY0: Single
    fPrevRegionWidth: Single
    fPrevRegionHeight: Single
    fPrevBlendCoef: Single
    dwEffectType: UInt32
    dwNumEffectParas: UInt32
    fEffectPara0: Single
    fEffectPara1: Single
    fEffectPara2: Single
    fEffectPara3: Single
    fEffectPara4: Single
    bKeepPrevImage: Windows.Win32.Foundation.BOOL
class WMT_WATERMARK_ENTRY(EasyCastStructure):
    wmetType: Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE
    clsid: Guid
    cbDisplayName: UInt32
    pwszDisplayName: Windows.Win32.Foundation.PWSTR
WMT_WATERMARK_ENTRY_TYPE = Int32
WMT_WMETYPE_AUDIO: WMT_WATERMARK_ENTRY_TYPE = 1
WMT_WMETYPE_VIDEO: WMT_WATERMARK_ENTRY_TYPE = 2
class WMT_WEBSTREAM_FORMAT(EasyCastStructure):
    cbSize: UInt16
    cbSampleHeaderFixedData: UInt16
    wVersion: UInt16
    wReserved: UInt16
class WMT_WEBSTREAM_SAMPLE_HEADER(EasyCastStructure):
    cbLength: UInt16
    wPart: UInt16
    cTotalParts: UInt16
    wSampleType: UInt16
    wszURL: Char * 1
class WMVIDEOINFOHEADER(EasyCastStructure):
    rcSource: Windows.Win32.Foundation.RECT
    rcTarget: Windows.Win32.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    bmiHeader: Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER
class WMVIDEOINFOHEADER2(EasyCastStructure):
    rcSource: Windows.Win32.Foundation.RECT
    rcTarget: Windows.Win32.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    dwInterlaceFlags: UInt32
    dwCopyProtectFlags: UInt32
    dwPictAspectRatioX: UInt32
    dwPictAspectRatioY: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
    bmiHeader: Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER
class WM_ADDRESS_ACCESSENTRY(EasyCastStructure):
    dwIPAddress: UInt32
    dwMask: UInt32
WM_AETYPE = Int32
WM_AETYPE_INCLUDE: WM_AETYPE = 105
WM_AETYPE_EXCLUDE: WM_AETYPE = 101
class WM_CLIENT_PROPERTIES(EasyCastStructure):
    dwIPAddress: UInt32
    dwPort: UInt32
class WM_CLIENT_PROPERTIES_EX(EasyCastStructure):
    cbSize: UInt32
    pwszIPAddress: Windows.Win32.Foundation.PWSTR
    pwszPort: Windows.Win32.Foundation.PWSTR
    pwszDNSName: Windows.Win32.Foundation.PWSTR
WM_DM_INTERLACED_TYPE = Int32
WM_DM_NOTINTERLACED: WM_DM_INTERLACED_TYPE = 0
WM_DM_DEINTERLACE_NORMAL: WM_DM_INTERLACED_TYPE = 1
WM_DM_DEINTERLACE_HALFSIZE: WM_DM_INTERLACED_TYPE = 2
WM_DM_DEINTERLACE_HALFSIZEDOUBLERATE: WM_DM_INTERLACED_TYPE = 3
WM_DM_DEINTERLACE_INVERSETELECINE: WM_DM_INTERLACED_TYPE = 4
WM_DM_DEINTERLACE_VERTICALHALFSIZEDOUBLERATE: WM_DM_INTERLACED_TYPE = 5
WM_DM_IT_FIRST_FRAME_COHERENCY = Int32
WM_DM_IT_DISABLE_COHERENT_MODE: WM_DM_IT_FIRST_FRAME_COHERENCY = 0
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_TOP: WM_DM_IT_FIRST_FRAME_COHERENCY = 1
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_TOP: WM_DM_IT_FIRST_FRAME_COHERENCY = 2
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_TOP: WM_DM_IT_FIRST_FRAME_COHERENCY = 3
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_TOP: WM_DM_IT_FIRST_FRAME_COHERENCY = 4
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_TOP: WM_DM_IT_FIRST_FRAME_COHERENCY = 5
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_BOTTOM: WM_DM_IT_FIRST_FRAME_COHERENCY = 6
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_BOTTOM: WM_DM_IT_FIRST_FRAME_COHERENCY = 7
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_BOTTOM: WM_DM_IT_FIRST_FRAME_COHERENCY = 8
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_BOTTOM: WM_DM_IT_FIRST_FRAME_COHERENCY = 9
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_BOTTOM: WM_DM_IT_FIRST_FRAME_COHERENCY = 10
class WM_LEAKY_BUCKET_PAIR(EasyCastStructure):
    dwBitrate: UInt32
    msBufferWindow: UInt32
    _pack_ = 1
class WM_MEDIA_TYPE(EasyCastStructure):
    majortype: Guid
    subtype: Guid
    bFixedSizeSamples: Windows.Win32.Foundation.BOOL
    bTemporalCompression: Windows.Win32.Foundation.BOOL
    lSampleSize: UInt32
    formattype: Guid
    pUnk: Windows.Win32.System.Com.IUnknown_head
    cbFormat: UInt32
    pbFormat: POINTER(Byte)
class WM_PICTURE(EasyCastStructure):
    pwszMIMEType: Windows.Win32.Foundation.PWSTR
    bPictureType: Byte
    pwszDescription: Windows.Win32.Foundation.PWSTR
    dwDataLen: UInt32
    pbData: POINTER(Byte)
    _pack_ = 1
WM_PLAYBACK_DRC_LEVEL = Int32
WM_PLAYBACK_DRC_HIGH: WM_PLAYBACK_DRC_LEVEL = 0
WM_PLAYBACK_DRC_MEDIUM: WM_PLAYBACK_DRC_LEVEL = 1
WM_PLAYBACK_DRC_LOW: WM_PLAYBACK_DRC_LEVEL = 2
class WM_PORT_NUMBER_RANGE(EasyCastStructure):
    wPortBegin: UInt16
    wPortEnd: UInt16
class WM_READER_CLIENTINFO(EasyCastStructure):
    cbSize: UInt32
    wszLang: Windows.Win32.Foundation.PWSTR
    wszBrowserUserAgent: Windows.Win32.Foundation.PWSTR
    wszBrowserWebPage: Windows.Win32.Foundation.PWSTR
    qwReserved: UInt64
    pReserved: POINTER(Windows.Win32.Foundation.LPARAM)
    wszHostExe: Windows.Win32.Foundation.PWSTR
    qwHostVersion: UInt64
    wszPlayerUserAgent: Windows.Win32.Foundation.PWSTR
class WM_READER_STATISTICS(EasyCastStructure):
    cbSize: UInt32
    dwBandwidth: UInt32
    cPacketsReceived: UInt32
    cPacketsRecovered: UInt32
    cPacketsLost: UInt32
    wQuality: UInt16
WM_SFEX_TYPE = Int32
WM_SFEX_NOTASYNCPOINT: WM_SFEX_TYPE = 2
WM_SFEX_DATALOSS: WM_SFEX_TYPE = 4
WM_SF_TYPE = Int32
WM_SF_CLEANPOINT: WM_SF_TYPE = 1
WM_SF_DISCONTINUITY: WM_SF_TYPE = 2
WM_SF_DATALOSS: WM_SF_TYPE = 4
class WM_STREAM_PRIORITY_RECORD(EasyCastStructure):
    wStreamNumber: UInt16
    fMandatory: Windows.Win32.Foundation.BOOL
    _pack_ = 2
class WM_STREAM_TYPE_INFO(EasyCastStructure):
    guidMajorType: Guid
    cbFormat: UInt32
    _pack_ = 1
class WM_SYNCHRONISED_LYRICS(EasyCastStructure):
    bTimeStampFormat: Byte
    bContentType: Byte
    pwszContentDescriptor: Windows.Win32.Foundation.PWSTR
    dwLyricsLen: UInt32
    pbLyrics: POINTER(Byte)
    _pack_ = 1
class WM_USER_TEXT(EasyCastStructure):
    pwszDescription: Windows.Win32.Foundation.PWSTR
    pwszText: Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class WM_USER_WEB_URL(EasyCastStructure):
    pwszDescription: Windows.Win32.Foundation.PWSTR
    pwszURL: Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class WM_WRITER_STATISTICS(EasyCastStructure):
    qwSampleCount: UInt64
    qwByteCount: UInt64
    qwDroppedSampleCount: UInt64
    qwDroppedByteCount: UInt64
    dwCurrentBitrate: UInt32
    dwAverageBitrate: UInt32
    dwExpectedBitrate: UInt32
    dwCurrentSampleRate: UInt32
    dwAverageSampleRate: UInt32
    dwExpectedSampleRate: UInt32
class WM_WRITER_STATISTICS_EX(EasyCastStructure):
    dwBitratePlusOverhead: UInt32
    dwCurrentSampleDropRateInQueue: UInt32
    dwCurrentSampleDropRateInCodec: UInt32
    dwCurrentSampleDropRateInMultiplexer: UInt32
    dwTotalSampleDropsInQueue: UInt32
    dwTotalSampleDropsInCodec: UInt32
    dwTotalSampleDropsInMultiplexer: UInt32
_AM_ASFWRITERCONFIG_PARAM = Int32
AM_CONFIGASFWRITER_PARAM_AUTOINDEX: _AM_ASFWRITERCONFIG_PARAM = 1
AM_CONFIGASFWRITER_PARAM_MULTIPASS: _AM_ASFWRITERCONFIG_PARAM = 2
AM_CONFIGASFWRITER_PARAM_DONTCOMPRESS: _AM_ASFWRITERCONFIG_PARAM = 3
make_head(_module, 'AM_WMT_EVENT_DATA')
make_head(_module, 'DRM_COPY_OPL')
make_head(_module, 'DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS')
make_head(_module, 'DRM_OPL_OUTPUT_IDS')
make_head(_module, 'DRM_OUTPUT_PROTECTION')
make_head(_module, 'DRM_PLAY_OPL')
make_head(_module, 'DRM_VAL16')
make_head(_module, 'DRM_VIDEO_OUTPUT_PROTECTION_IDS')
make_head(_module, 'INSNetSourceCreator')
make_head(_module, 'INSSBuffer')
make_head(_module, 'INSSBuffer2')
make_head(_module, 'INSSBuffer3')
make_head(_module, 'INSSBuffer4')
make_head(_module, 'IWMAddressAccess')
make_head(_module, 'IWMAddressAccess2')
make_head(_module, 'IWMAuthorizer')
make_head(_module, 'IWMBackupRestoreProps')
make_head(_module, 'IWMBandwidthSharing')
make_head(_module, 'IWMClientConnections')
make_head(_module, 'IWMClientConnections2')
make_head(_module, 'IWMCodecInfo')
make_head(_module, 'IWMCodecInfo2')
make_head(_module, 'IWMCodecInfo3')
make_head(_module, 'IWMCredentialCallback')
make_head(_module, 'IWMDRMEditor')
make_head(_module, 'IWMDRMMessageParser')
make_head(_module, 'IWMDRMReader')
make_head(_module, 'IWMDRMReader2')
make_head(_module, 'IWMDRMReader3')
make_head(_module, 'IWMDRMTranscryptionManager')
make_head(_module, 'IWMDRMTranscryptor')
make_head(_module, 'IWMDRMTranscryptor2')
make_head(_module, 'IWMDRMWriter')
make_head(_module, 'IWMDRMWriter2')
make_head(_module, 'IWMDRMWriter3')
make_head(_module, 'IWMDeviceRegistration')
make_head(_module, 'IWMGetSecureChannel')
make_head(_module, 'IWMHeaderInfo')
make_head(_module, 'IWMHeaderInfo2')
make_head(_module, 'IWMHeaderInfo3')
make_head(_module, 'IWMIStreamProps')
make_head(_module, 'IWMImageInfo')
make_head(_module, 'IWMIndexer')
make_head(_module, 'IWMIndexer2')
make_head(_module, 'IWMInputMediaProps')
make_head(_module, 'IWMLanguageList')
make_head(_module, 'IWMLicenseBackup')
make_head(_module, 'IWMLicenseRestore')
make_head(_module, 'IWMLicenseRevocationAgent')
make_head(_module, 'IWMMediaProps')
make_head(_module, 'IWMMetadataEditor')
make_head(_module, 'IWMMetadataEditor2')
make_head(_module, 'IWMMutualExclusion')
make_head(_module, 'IWMMutualExclusion2')
make_head(_module, 'IWMOutputMediaProps')
make_head(_module, 'IWMPacketSize')
make_head(_module, 'IWMPacketSize2')
make_head(_module, 'IWMPlayerHook')
make_head(_module, 'IWMPlayerTimestampHook')
make_head(_module, 'IWMProfile')
make_head(_module, 'IWMProfile2')
make_head(_module, 'IWMProfile3')
make_head(_module, 'IWMProfileManager')
make_head(_module, 'IWMProfileManager2')
make_head(_module, 'IWMProfileManagerLanguage')
make_head(_module, 'IWMPropertyVault')
make_head(_module, 'IWMProximityDetection')
make_head(_module, 'IWMReader')
make_head(_module, 'IWMReaderAccelerator')
make_head(_module, 'IWMReaderAdvanced')
make_head(_module, 'IWMReaderAdvanced2')
make_head(_module, 'IWMReaderAdvanced3')
make_head(_module, 'IWMReaderAdvanced4')
make_head(_module, 'IWMReaderAdvanced5')
make_head(_module, 'IWMReaderAdvanced6')
make_head(_module, 'IWMReaderAllocatorEx')
make_head(_module, 'IWMReaderCallback')
make_head(_module, 'IWMReaderCallbackAdvanced')
make_head(_module, 'IWMReaderNetworkConfig')
make_head(_module, 'IWMReaderNetworkConfig2')
make_head(_module, 'IWMReaderPlaylistBurn')
make_head(_module, 'IWMReaderStreamClock')
make_head(_module, 'IWMReaderTimecode')
make_head(_module, 'IWMReaderTypeNegotiation')
make_head(_module, 'IWMRegisterCallback')
make_head(_module, 'IWMRegisteredDevice')
make_head(_module, 'IWMSBufferAllocator')
make_head(_module, 'IWMSInternalAdminNetSource')
make_head(_module, 'IWMSInternalAdminNetSource2')
make_head(_module, 'IWMSInternalAdminNetSource3')
make_head(_module, 'IWMSecureChannel')
make_head(_module, 'IWMStatusCallback')
make_head(_module, 'IWMStreamConfig')
make_head(_module, 'IWMStreamConfig2')
make_head(_module, 'IWMStreamConfig3')
make_head(_module, 'IWMStreamList')
make_head(_module, 'IWMStreamPrioritization')
make_head(_module, 'IWMSyncReader')
make_head(_module, 'IWMSyncReader2')
make_head(_module, 'IWMVideoMediaProps')
make_head(_module, 'IWMWatermarkInfo')
make_head(_module, 'IWMWriter')
make_head(_module, 'IWMWriterAdvanced')
make_head(_module, 'IWMWriterAdvanced2')
make_head(_module, 'IWMWriterAdvanced3')
make_head(_module, 'IWMWriterFileSink')
make_head(_module, 'IWMWriterFileSink2')
make_head(_module, 'IWMWriterFileSink3')
make_head(_module, 'IWMWriterNetworkSink')
make_head(_module, 'IWMWriterPostView')
make_head(_module, 'IWMWriterPostViewCallback')
make_head(_module, 'IWMWriterPreprocess')
make_head(_module, 'IWMWriterPushSink')
make_head(_module, 'IWMWriterSink')
make_head(_module, 'WMDRM_IMPORT_INIT_STRUCT')
make_head(_module, 'WMMPEG2VIDEOINFO')
make_head(_module, 'WMSCRIPTFORMAT')
make_head(_module, 'WMT_BUFFER_SEGMENT')
make_head(_module, 'WMT_COLORSPACEINFO_EXTENSION_DATA')
make_head(_module, 'WMT_FILESINK_DATA_UNIT')
make_head(_module, 'WMT_PAYLOAD_FRAGMENT')
make_head(_module, 'WMT_TIMECODE_EXTENSION_DATA')
make_head(_module, 'WMT_VIDEOIMAGE_SAMPLE')
make_head(_module, 'WMT_VIDEOIMAGE_SAMPLE2')
make_head(_module, 'WMT_WATERMARK_ENTRY')
make_head(_module, 'WMT_WEBSTREAM_FORMAT')
make_head(_module, 'WMT_WEBSTREAM_SAMPLE_HEADER')
make_head(_module, 'WMVIDEOINFOHEADER')
make_head(_module, 'WMVIDEOINFOHEADER2')
make_head(_module, 'WM_ADDRESS_ACCESSENTRY')
make_head(_module, 'WM_CLIENT_PROPERTIES')
make_head(_module, 'WM_CLIENT_PROPERTIES_EX')
make_head(_module, 'WM_LEAKY_BUCKET_PAIR')
make_head(_module, 'WM_MEDIA_TYPE')
make_head(_module, 'WM_PICTURE')
make_head(_module, 'WM_PORT_NUMBER_RANGE')
make_head(_module, 'WM_READER_CLIENTINFO')
make_head(_module, 'WM_READER_STATISTICS')
make_head(_module, 'WM_STREAM_PRIORITY_RECORD')
make_head(_module, 'WM_STREAM_TYPE_INFO')
make_head(_module, 'WM_SYNCHRONISED_LYRICS')
make_head(_module, 'WM_USER_TEXT')
make_head(_module, 'WM_USER_WEB_URL')
make_head(_module, 'WM_WRITER_STATISTICS')
make_head(_module, 'WM_WRITER_STATISTICS_EX')
