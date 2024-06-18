from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Media.WindowsMediaFormat
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
class AM_WMT_EVENT_DATA(Structure):
    hrStatus: win32more.Windows.Win32.Foundation.HRESULT
    pData: VoidPtr
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
WMMEDIASUBTYPE_Base: Guid = Guid('{00000000-0000-0010-8000-00aa00389b71}')
WMMEDIATYPE_Video: Guid = Guid('{73646976-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_RGB1: Guid = Guid('{e436eb78-524f-11ce-9f53-0020af0ba770}')
WMMEDIASUBTYPE_RGB4: Guid = Guid('{e436eb79-524f-11ce-9f53-0020af0ba770}')
WMMEDIASUBTYPE_RGB8: Guid = Guid('{e436eb7a-524f-11ce-9f53-0020af0ba770}')
WMMEDIASUBTYPE_RGB565: Guid = Guid('{e436eb7b-524f-11ce-9f53-0020af0ba770}')
WMMEDIASUBTYPE_RGB555: Guid = Guid('{e436eb7c-524f-11ce-9f53-0020af0ba770}')
WMMEDIASUBTYPE_RGB24: Guid = Guid('{e436eb7d-524f-11ce-9f53-0020af0ba770}')
WMMEDIASUBTYPE_RGB32: Guid = Guid('{e436eb7e-524f-11ce-9f53-0020af0ba770}')
WMMEDIASUBTYPE_I420: Guid = Guid('{30323449-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_IYUV: Guid = Guid('{56555949-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_YV12: Guid = Guid('{32315659-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_YUY2: Guid = Guid('{32595559-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_P422: Guid = Guid('{32323450-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_UYVY: Guid = Guid('{59565955-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_YVYU: Guid = Guid('{55595659-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_YVU9: Guid = Guid('{39555659-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_VIDEOIMAGE: Guid = Guid('{1d4a45f2-e5f6-4b44-8388-f0ae5c0e0c37}')
WMMEDIASUBTYPE_MP43: Guid = Guid('{3334504d-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_MP4S: Guid = Guid('{5334504d-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_M4S2: Guid = Guid('{3253344d-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMV1: Guid = Guid('{31564d57-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMV2: Guid = Guid('{32564d57-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_MSS1: Guid = Guid('{3153534d-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_MPEG2_VIDEO: Guid = Guid('{e06d8026-db46-11cf-b4d1-00805f6cbbea}')
WMMEDIATYPE_Audio: Guid = Guid('{73647561-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_PCM: Guid = Guid('{00000001-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_DRM: Guid = Guid('{00000009-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMAudioV9: Guid = Guid('{00000162-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMAudio_Lossless: Guid = Guid('{00000163-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_MSS2: Guid = Guid('{3253534d-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMSP1: Guid = Guid('{0000000a-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMSP2: Guid = Guid('{0000000b-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMV3: Guid = Guid('{33564d57-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMVP: Guid = Guid('{50564d57-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WVP2: Guid = Guid('{32505657-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMVA: Guid = Guid('{41564d57-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WVC1: Guid = Guid('{31435657-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMAudioV8: Guid = Guid('{00000161-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMAudioV7: Guid = Guid('{00000161-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WMAudioV2: Guid = Guid('{00000161-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_ACELPnet: Guid = Guid('{00000130-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_MP3: Guid = Guid('{00000055-0000-0010-8000-00aa00389b71}')
WMMEDIASUBTYPE_WebStream: Guid = Guid('{776257d4-c627-41cb-8f81-7ac7ff1c40cc}')
WMMEDIATYPE_Script: Guid = Guid('{73636d64-0000-0010-8000-00aa00389b71}')
WMMEDIATYPE_Image: Guid = Guid('{34a50fd8-8aa5-4386-81fe-a0efe0488e31}')
WMMEDIATYPE_FileTransfer: Guid = Guid('{d9e47579-930e-4427-adfc-ad80f290e470}')
WMMEDIATYPE_Text: Guid = Guid('{9bba1ea7-5ab2-4829-ba57-0940209bcf3e}')
WMFORMAT_VideoInfo: Guid = Guid('{05589f80-c356-11ce-bf01-00aa0055595a}')
WMFORMAT_MPEG2Video: Guid = Guid('{e06d80e3-db46-11cf-b4d1-00805f6cbbea}')
WMFORMAT_WaveFormatEx: Guid = Guid('{05589f81-c356-11ce-bf01-00aa0055595a}')
WMFORMAT_Script: Guid = Guid('{5c8510f2-debe-4ca7-bba5-f07a104f8dff}')
WMFORMAT_WebStream: Guid = Guid('{da1e6b13-8359-4050-b398-388e965bf00c}')
WMSCRIPTTYPE_TwoStrings: Guid = Guid('{82f38a70-c29f-11d1-97ad-00a0c95ea850}')
WM_SampleExtensionGUID_OutputCleanPoint: Guid = Guid('{f72a3c6f-6eb4-4ebc-b192-09ad9759e828}')
WM_SampleExtensionGUID_Timecode: Guid = Guid('{399595ec-8667-4e2d-8fdb-98814ce76c1e}')
WM_SampleExtensionGUID_ChromaLocation: Guid = Guid('{4c5acca0-9276-4b2c-9e4c-a0edefdd217e}')
WM_SampleExtensionGUID_ColorSpaceInfo: Guid = Guid('{f79ada56-30eb-4f2b-9f7a-f24b139a1157}')
WM_SampleExtensionGUID_UserDataInfo: Guid = Guid('{732bb4fa-78be-4549-99bd-02db1a55b7a8}')
WM_SampleExtensionGUID_FileName: Guid = Guid('{e165ec0e-19ed-45d7-b4a7-25cbd1e28e9b}')
WM_SampleExtensionGUID_ContentType: Guid = Guid('{d590dc20-07bc-436c-9cf7-f3bbfbf1a4dc}')
WM_SampleExtensionGUID_PixelAspectRatio: Guid = Guid('{1b1ee554-f9ea-4bc8-821a-376b74e4c4b8}')
WM_SampleExtensionGUID_SampleDuration: Guid = Guid('{c6bd9450-867f-4907-83a3-c77921b733ad}')
WM_SampleExtensionGUID_SampleProtectionSalt: Guid = Guid('{5403deee-b9ee-438f-aa83-3804997e569d}')
CLSID_WMMUTEX_Language: Guid = Guid('{d6e22a00-35da-11d1-9034-00a0c90349be}')
CLSID_WMMUTEX_Bitrate: Guid = Guid('{d6e22a01-35da-11d1-9034-00a0c90349be}')
CLSID_WMMUTEX_Presentation: Guid = Guid('{d6e22a02-35da-11d1-9034-00a0c90349be}')
CLSID_WMMUTEX_Unknown: Guid = Guid('{d6e22a03-35da-11d1-9034-00a0c90349be}')
CLSID_WMBandwidthSharing_Exclusive: Guid = Guid('{af6060aa-5197-11d2-b6af-00c04fd908e9}')
CLSID_WMBandwidthSharing_Partial: Guid = Guid('{af6060ab-5197-11d2-b6af-00c04fd908e9}')
WMT_DMOCATEGORY_AUDIO_WATERMARK: Guid = Guid('{65221c5a-fa75-4b39-b50c-06c336b6a3ef}')
WMT_DMOCATEGORY_VIDEO_WATERMARK: Guid = Guid('{187cc922-8efc-4404-9daf-63f4830df1bc}')
CLSID_ClientNetManager: Guid = Guid('{cd12a3ce-9c42-11d2-beed-0060082f2054}')
@winfunctype('WMVCore.dll')
def WMIsContentProtected(pwszFileName: win32more.Windows.Win32.Foundation.PWSTR, pfIsProtected: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriter(pUnkCert: win32more.Windows.Win32.System.Com.IUnknown, ppWriter: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateReader(pUnkCert: win32more.Windows.Win32.System.Com.IUnknown, dwRights: UInt32, ppReader: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateSyncReader(pUnkCert: win32more.Windows.Win32.System.Com.IUnknown, dwRights: UInt32, ppSyncReader: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMSyncReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateEditor(ppEditor: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMetadataEditor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateIndexer(ppIndexer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMIndexer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateBackupRestorer(pCallback: win32more.Windows.Win32.System.Com.IUnknown, ppBackup: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMLicenseBackup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateProfileManager(ppProfileManager: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfileManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriterFileSink(ppSink: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterFileSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriterNetworkSink(ppSink: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterNetworkSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WMVCore.dll')
def WMCreateWriterPushSink(ppSink: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterPushSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DRM_COPY_OPL(Structure):
    wMinimumCopyLevel: UInt16
    oplIdIncludes: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS
    oplIdExcludes: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS
class DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS(Structure):
    wCompressedDigitalVideo: UInt16
    wUncompressedDigitalVideo: UInt16
    wAnalogVideo: UInt16
    wCompressedDigitalAudio: UInt16
    wUncompressedDigitalAudio: UInt16
class DRM_OPL_OUTPUT_IDS(Structure):
    cIds: UInt16
    rgIds: POINTER(Guid)
class DRM_OUTPUT_PROTECTION(Structure):
    guidId: Guid
    bConfigData: Byte
class DRM_PLAY_OPL(Structure):
    minOPL: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS
    oplIdReserved: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS
    vopi: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_VIDEO_OUTPUT_PROTECTION_IDS
class DRM_VAL16(Structure):
    val: Byte * 16
class DRM_VIDEO_OUTPUT_PROTECTION_IDS(Structure):
    cEntries: UInt16
    rgVop: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_OUTPUT_PROTECTION)
class INSNetSourceCreator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c0e4080-9081-11d2-beec-0060082f2054}')
    @commethod(3)
    def Initialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateNetSource(self, pszStreamName: win32more.Windows.Win32.Foundation.PWSTR, pMonitor: win32more.Windows.Win32.System.Com.IUnknown, pData: POINTER(Byte), pUserContext: win32more.Windows.Win32.System.Com.IUnknown, pCallback: win32more.Windows.Win32.System.Com.IUnknown, qwContext: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetSourceProperties(self, pszStreamName: win32more.Windows.Win32.Foundation.PWSTR, ppPropertiesNode: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNetSourceSharedNamespace(self, ppSharedNamespace: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNetSourceAdminInterface(self, pszStreamName: win32more.Windows.Win32.Foundation.PWSTR, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNumProtocolsSupported(self, pcProtocols: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProtocolName(self, dwProtocolNum: UInt32, pwszProtocolName: win32more.Windows.Win32.Foundation.PWSTR, pcchProtocolName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Shutdown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e1cd3524-03d7-11d2-9eed-006097d2d7cf}')
    @commethod(3)
    def GetLength(self, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLength(self, dwLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxLength(self, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBuffer(self, ppdwBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBufferAndLength(self, ppdwBuffer: POINTER(POINTER(Byte)), pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer
    _iid_ = Guid('{4f528693-1035-43fe-b428-757561ad3a68}')
    @commethod(8)
    def GetSampleProperties(self, cbProperties: UInt32, pbProperties: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSampleProperties(self, cbProperties: UInt32, pbProperties: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer2
    _iid_ = Guid('{c87ceaaf-75be-4bc4-84eb-ac2798507672}')
    @commethod(10)
    def SetProperty(self, guidBufferProperty: Guid, pvBufferProperty: VoidPtr, dwBufferPropertySize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProperty(self, guidBufferProperty: Guid, pvBufferProperty: VoidPtr, pdwBufferPropertySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INSSBuffer4(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer3
    _iid_ = Guid('{b6b8fd5a-32e2-49d4-a910-c26cc85465ed}')
    @commethod(12)
    def GetPropertyCount(self, pcBufferProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPropertyByIndex(self, dwBufferPropertyIndex: UInt32, pguidBufferProperty: POINTER(Guid), pvBufferProperty: VoidPtr, pdwBufferPropertySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMAddressAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb3c6389-1633-4e92-af14-9f3173ba39d0}')
    @commethod(3)
    def GetAccessEntryCount(self, aeType: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, pcEntries: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAccessEntry(self, aeType: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, dwEntryNum: UInt32, pAddrAccessEntry: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_ADDRESS_ACCESSENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddAccessEntry(self, aeType: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, pAddrAccessEntry: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_ADDRESS_ACCESSENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAccessEntry(self, aeType: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, dwEntryNum: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMAddressAccess2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMAddressAccess
    _iid_ = Guid('{65a83fc2-3e98-4d4d-81b5-2a742886b33d}')
    @commethod(7)
    def GetAccessEntryEx(self, aeType: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, dwEntryNum: UInt32, pbstrAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrMask: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddAccessEntryEx(self, aeType: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE, bstrAddress: win32more.Windows.Win32.Foundation.BSTR, bstrMask: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMAuthorizer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d9b67d36-a9ad-4eb4-baef-db284ef5504c}')
    @commethod(3)
    def GetCertCount(self, pcCerts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCert(self, dwIndex: UInt32, ppbCertData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSharedData(self, dwCertIndex: UInt32, pbSharedData: POINTER(Byte), pbCert: POINTER(Byte), ppbSharedData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMBackupRestoreProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c8e0da6-996f-4ff3-a1af-4838f9377e2e}')
    @commethod(3)
    def GetPropCount(self, pcProps: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropByIndex(self, wIndex: UInt16, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchNameLen: POINTER(UInt16), pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropByName(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProp(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveProp(self, pcwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAllProps(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMBandwidthSharing(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamList
    _iid_ = Guid('{ad694af1-f8d9-42f8-bc47-70311b0c4f9e}')
    @commethod(6)
    def GetType(self, pguidType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetType(self, guidType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBandwidth(self, pdwBitrate: POINTER(UInt32), pmsBufferWindow: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBandwidth(self, dwBitrate: UInt32, msBufferWindow: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMClientConnections(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73c66010-a299-41df-b1f0-ccf03b09c1c6}')
    @commethod(3)
    def GetClientCount(self, pcClients: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClientProperties(self, dwClientNum: UInt32, pClientProperties: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_CLIENT_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMClientConnections2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMClientConnections
    _iid_ = Guid('{4091571e-4701-4593-bb3d-d5f5f0c74246}')
    @commethod(5)
    def GetClientInfo(self, dwClientNum: UInt32, pwszNetworkAddress: win32more.Windows.Win32.Foundation.PWSTR, pcchNetworkAddress: POINTER(UInt32), pwszPort: win32more.Windows.Win32.Foundation.PWSTR, pcchPort: POINTER(UInt32), pwszDNSName: win32more.Windows.Win32.Foundation.PWSTR, pcchDNSName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMCodecInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a970f41e-34de-4a98-b3ba-e4b3ca7528f0}')
    @commethod(3)
    def GetCodecInfoCount(self, guidType: POINTER(Guid), pcCodecs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCodecFormatCount(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pcFormat: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCodecFormat(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, dwFormatIndex: UInt32, ppIStreamConfig: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMCodecInfo2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMCodecInfo
    _iid_ = Guid('{aa65e273-b686-4056-91ec-dd768d4df710}')
    @commethod(6)
    def GetCodecName(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, wszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCodecFormatDesc(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, dwFormatIndex: UInt32, ppIStreamConfig: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig), wszDesc: win32more.Windows.Win32.Foundation.PWSTR, pcchDesc: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMCodecInfo3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMCodecInfo2
    _iid_ = Guid('{7e51f487-4d93-4f98-8ab4-27d0565adc51}')
    @commethod(8)
    def GetCodecFormatProp(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, dwFormatIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCodecProp(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCodecEnumerationSetting(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), dwSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCodecEnumerationSetting(self, guidType: POINTER(Guid), dwCodecIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMCredentialCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{342e0eb7-e651-450c-975b-2ace2c90c48e}')
    @commethod(3)
    def AcquireCredentials(self, pwszRealm: win32more.Windows.Win32.Foundation.PWSTR, pwszSite: win32more.Windows.Win32.Foundation.PWSTR, pwszUser: win32more.Windows.Win32.Foundation.PWSTR, cchUser: UInt32, pwszPassword: win32more.Windows.Win32.Foundation.PWSTR, cchPassword: UInt32, hrStatus: win32more.Windows.Win32.Foundation.HRESULT, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMEditor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ff130ebc-a6c3-42a6-b401-c3382c3e08b3}')
    @commethod(3)
    def GetDRMProperty(self, pwstrName: win32more.Windows.Win32.Foundation.PWSTR, pdwType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMMessageParser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a73a0072-25a0-4c99-b4a5-ede8101a6c39}')
    @commethod(3)
    def ParseRegistrationReqMsg(self, pbRegistrationReqMsg: POINTER(Byte), cbRegistrationReqMsg: UInt32, ppDeviceCert: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pDeviceSerialNumber: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ParseLicenseRequestMsg(self, pbLicenseRequestMsg: POINTER(Byte), cbLicenseRequestMsg: UInt32, ppDeviceCert: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pDeviceSerialNumber: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16), pbstrAction: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2827540-3ee7-432c-b14c-dc17f085d3b3}')
    @commethod(3)
    def AcquireLicense(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseAcquisition(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Individualize(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CancelIndividualization(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MonitorLicenseAcquisition(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelMonitorLicenseAcquisition(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetDRMProperty(self, pwstrName: win32more.Windows.Win32.Foundation.PWSTR, dwType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDRMProperty(self, pwstrName: win32more.Windows.Win32.Foundation.PWSTR, pdwType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMReader2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMDRMReader
    _iid_ = Guid('{befe7a75-9f1d-4075-b9d9-a3c37bda49a0}')
    @commethod(11)
    def SetEvaluateOutputLevelLicenses(self, fEvaluate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPlayOutputLevels(self, pPlayOPL: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_PLAY_OPL), pcbLength: POINTER(UInt32), pdwMinAppComplianceLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCopyOutputLevels(self, pCopyOPL: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_COPY_OPL), pcbLength: POINTER(UInt32), pdwMinAppComplianceLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TryNextLicense(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMReader3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMDRMReader2
    _iid_ = Guid('{e08672de-f1e7-4ff4-a0a3-fc4b08e4caf8}')
    @commethod(15)
    def GetInclusionList(self, ppGuids: POINTER(POINTER(Guid)), pcGuids: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMTranscryptionManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b1a887b2-a4f0-407a-b02e-efbd23bbecdf}')
    @commethod(3)
    def CreateTranscryptor(self, ppTranscryptor: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMDRMTranscryptor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMTranscryptor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{69059850-6e6f-4bb2-806f-71863ddfc471}')
    @commethod(3)
    def Initialize(self, bstrFileName: win32more.Windows.Win32.Foundation.BSTR, pbLicenseRequestMsg: POINTER(Byte), cbLicenseRequestMsg: UInt32, ppLicenseResponseMsg: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Seek(self, hnsTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Read(self, pbData: POINTER(Byte), pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMTranscryptor2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMDRMTranscryptor
    _iid_ = Guid('{e0da439f-d331-496a-bece-18e5bac5dd23}')
    @commethod(7)
    def SeekEx(self, cnsStartTime: UInt64, cnsDuration: UInt64, flRate: Single, fIncludeFileHeader: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ZeroAdjustTimestamps(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSeekStartTime(self, pcnsTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDuration(self, pcnsDuration: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6ea5dd0-12a0-43f4-90ab-a3fd451e6a07}')
    @commethod(3)
    def GenerateKeySeed(self, pwszKeySeed: win32more.Windows.Win32.Foundation.PWSTR, pcwchLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GenerateKeyID(self, pwszKeyID: win32more.Windows.Win32.Foundation.PWSTR, pcwchLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GenerateSigningKeyPair(self, pwszPrivKey: win32more.Windows.Win32.Foundation.PWSTR, pcwchPrivKeyLength: POINTER(UInt32), pwszPubKey: win32more.Windows.Win32.Foundation.PWSTR, pcwchPubKeyLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDRMAttribute(self, wStreamNum: UInt16, pszName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMWriter2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMDRMWriter
    _iid_ = Guid('{38ee7a94-40e2-4e10-aa3f-33fd3210ed5b}')
    @commethod(7)
    def SetWMDRMNetEncryption(self, fSamplesEncrypted: win32more.Windows.Win32.Foundation.BOOL, pbKeyID: POINTER(Byte), cbKeyID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDRMWriter3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMDRMWriter2
    _iid_ = Guid('{a7184082-a4aa-4dde-ac9c-e75dbd1117ce}')
    @commethod(8)
    def SetProtectStreamSamples(self, pImportInitStruct: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMDRM_IMPORT_INIT_STRUCT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f6211f03-8d21-4e94-93e6-8510805f2d99}')
    @commethod(3)
    def RegisterDevice(self, dwRegisterType: UInt32, pbCertificate: POINTER(Byte), cbCertificate: UInt32, SerialNumber: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16, ppDevice: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterDevice(self, dwRegisterType: UInt32, pbCertificate: POINTER(Byte), cbCertificate: UInt32, SerialNumber: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRegistrationStats(self, dwRegisterType: UInt32, pcRegisteredDevices: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFirstRegisteredDevice(self, dwRegisterType: UInt32, ppDevice: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNextRegisteredDevice(self, ppDevice: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRegisteredDeviceByID(self, dwRegisterType: UInt32, pbCertificate: POINTER(Byte), cbCertificate: UInt32, SerialNumber: win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16, ppDevice: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMRegisteredDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMGetSecureChannel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{94bc0598-c3d2-11d3-bedf-00c04f612986}')
    @commethod(3)
    def GetPeerSecureChannelInterface(self, ppPeer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMSecureChannel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMHeaderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bda-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetAttributeCount(self, wStreamNum: UInt16, pcAttributes: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttributeByIndex(self, wIndex: UInt16, pwStreamNum: POINTER(UInt16), pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchNameLen: POINTER(UInt16), pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributeByName(self, pwStreamNum: POINTER(UInt16), pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAttribute(self, wStreamNum: UInt16, pszName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMarkerCount(self, pcMarkers: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMarker(self, wIndex: UInt16, pwszMarkerName: win32more.Windows.Win32.Foundation.PWSTR, pcchMarkerNameLen: POINTER(UInt16), pcnsMarkerTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddMarker(self, pwszMarkerName: win32more.Windows.Win32.Foundation.PWSTR, cnsMarkerTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveMarker(self, wIndex: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetScriptCount(self, pcScripts: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetScript(self, wIndex: UInt16, pwszType: win32more.Windows.Win32.Foundation.PWSTR, pcchTypeLen: POINTER(UInt16), pwszCommand: win32more.Windows.Win32.Foundation.PWSTR, pcchCommandLen: POINTER(UInt16), pcnsScriptTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddScript(self, pwszType: win32more.Windows.Win32.Foundation.PWSTR, pwszCommand: win32more.Windows.Win32.Foundation.PWSTR, cnsScriptTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RemoveScript(self, wIndex: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMHeaderInfo2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMHeaderInfo
    _iid_ = Guid('{15cf9781-454e-482e-b393-85fae487a810}')
    @commethod(15)
    def GetCodecInfoCount(self, pcCodecInfos: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCodecInfo(self, wIndex: UInt32, pcchName: POINTER(UInt16), pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchDescription: POINTER(UInt16), pwszDescription: win32more.Windows.Win32.Foundation.PWSTR, pCodecType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE), pcbCodecInfo: POINTER(UInt16), pbCodecInfo: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMHeaderInfo3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMHeaderInfo2
    _iid_ = Guid('{15cc68e3-27cc-4ecd-b222-3f5d02d80bd5}')
    @commethod(17)
    def GetAttributeCountEx(self, wStreamNum: UInt16, pcAttributes: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetAttributeIndices(self, wStreamNum: UInt16, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pwLangIndex: POINTER(UInt16), pwIndices: POINTER(UInt16), pwCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAttributeByIndexEx(self, wStreamNum: UInt16, wIndex: UInt16, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pwNameLen: POINTER(UInt16), pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pwLangIndex: POINTER(UInt16), pValue: POINTER(Byte), pdwDataLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ModifyAttribute(self, wStreamNum: UInt16, wIndex: UInt16, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, wLangIndex: UInt16, pValue: POINTER(Byte), dwLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddAttribute(self, wStreamNum: UInt16, pszName: win32more.Windows.Win32.Foundation.PWSTR, pwIndex: POINTER(UInt16), Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, wLangIndex: UInt16, pValue: POINTER(Byte), dwLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DeleteAttribute(self, wStreamNum: UInt16, wIndex: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddCodecInfo(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pwszDescription: win32more.Windows.Win32.Foundation.PWSTR, codecType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE, cbCodecInfo: UInt16, pbCodecInfo: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMIStreamProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6816dad3-2b4b-4c8e-8149-874c3483a753}')
    @commethod(3)
    def GetProperty(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMImageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f0aa3b6-7267-4d89-88f2-ba915aa5c4c6}')
    @commethod(3)
    def GetImageCount(self, pcImages: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetImage(self, wIndex: UInt32, pcchMIMEType: POINTER(UInt16), pwszMIMEType: win32more.Windows.Win32.Foundation.PWSTR, pcchDescription: POINTER(UInt16), pwszDescription: win32more.Windows.Win32.Foundation.PWSTR, pImageType: POINTER(UInt16), pcbImageData: POINTER(UInt32), pbImageData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMIndexer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d7cdc71-9888-11d3-8edc-00c04f6109cf}')
    @commethod(3)
    def StartIndexing(self, pwszURL: win32more.Windows.Win32.Foundation.PWSTR, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMIndexer2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMIndexer
    _iid_ = Guid('{b70f1e42-6255-4df0-a6b9-02b212d9e2bb}')
    @commethod(5)
    def Configure(self, wStreamNum: UInt16, nIndexerType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_INDEXER_TYPE, pvInterval: VoidPtr, pvIndexType: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMInputMediaProps(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps
    _iid_ = Guid('{96406bd5-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(6)
    def GetConnectionName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGroupName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMLanguageList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df683f00-2d49-4d8e-92b7-fb19f6a0dc57}')
    @commethod(3)
    def GetLanguageCount(self, pwCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLanguageDetails(self, wIndex: UInt16, pwszLanguageString: win32more.Windows.Win32.Foundation.PWSTR, pcchLanguageStringLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddLanguageByRFC1766String(self, pwszLanguageString: win32more.Windows.Win32.Foundation.PWSTR, pwIndex: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMLicenseBackup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{05e5ac9f-3fb6-4508-bb43-a4067ba1ebe8}')
    @commethod(3)
    def BackupLicenses(self, dwFlags: UInt32, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseBackup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMLicenseRestore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c70b6334-a22e-4efb-a245-15e65a004a13}')
    @commethod(3)
    def RestoreLicenses(self, dwFlags: UInt32, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseRestore(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMLicenseRevocationAgent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6967f2c9-4e26-4b57-8894-799880f7ac7b}')
    @commethod(3)
    def GetLRBChallenge(self, pMachineID: POINTER(Byte), dwMachineIDLength: UInt32, pChallenge: POINTER(Byte), dwChallengeLength: UInt32, pChallengeOutput: POINTER(Byte), pdwChallengeOutputLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessLRB(self, pSignedLRB: POINTER(Byte), dwSignedLRBLength: UInt32, pSignedACK: POINTER(Byte), pdwSignedACKLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMMediaProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bce-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetType(self, pguidType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMediaType(self, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE), pcbType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMediaType(self, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMMetadataEditor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bd9-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def Open(self, pwszFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMMetadataEditor2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMetadataEditor
    _iid_ = Guid('{203cffe3-2e18-4fdf-b59d-6e71530534cf}')
    @commethod(6)
    def OpenEx(self, pwszFilename: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMMutualExclusion(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamList
    _iid_ = Guid('{96406bde-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(6)
    def GetType(self, pguidType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetType(self, guidType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMMutualExclusion2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion
    _iid_ = Guid('{0302b57d-89d1-4ba2-85c9-166f2c53eb91}')
    @commethod(8)
    def GetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCount(self, pwRecordCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddRecord(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveRecord(self, wRecordNumber: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordName(self, wRecordNumber: UInt16, pwszRecordName: win32more.Windows.Win32.Foundation.PWSTR, pcchRecordName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetRecordName(self, wRecordNumber: UInt16, pwszRecordName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStreamsForRecord(self, wRecordNumber: UInt16, pwStreamNumArray: POINTER(UInt16), pcStreams: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddStreamForRecord(self, wRecordNumber: UInt16, wStreamNumber: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RemoveStreamForRecord(self, wRecordNumber: UInt16, wStreamNumber: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMOutputMediaProps(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps
    _iid_ = Guid('{96406bd7-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(6)
    def GetStreamGroupName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConnectionName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMPacketSize(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cdfb97ab-188f-40b3-b643-5b7903975c59}')
    @commethod(3)
    def GetMaxPacketSize(self, pdwMaxPacketSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMaxPacketSize(self, dwMaxPacketSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMPacketSize2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMPacketSize
    _iid_ = Guid('{8bfc2b9e-b646-4233-a877-1c6a079669dc}')
    @commethod(5)
    def GetMinPacketSize(self, pdwMinPacketSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMinPacketSize(self, dwMinPacketSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMPlayerHook(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e5b7ca9a-0f1c-4f66-9002-74ec50d8b304}')
    @commethod(3)
    def PreDecode(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMPlayerTimestampHook(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{28580dda-d98e-48d0-b7ae-69e473a02825}')
    @commethod(3)
    def MapTimestamp(self, rtIn: Int64, prtOut: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMProfile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bdb-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetVersion(self, pdwVersion: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(self, pwszDescription: win32more.Windows.Win32.Foundation.PWSTR, pcchDescription: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDescription(self, pwszDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamCount(self, pcStreams: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStream(self, dwStreamIndex: UInt32, ppConfig: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStreamByNumber(self, wStreamNum: UInt16, ppConfig: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveStream(self, pConfig: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveStreamByNumber(self, wStreamNum: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddStream(self, pConfig: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ReconfigStream(self, pConfig: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateNewStream(self, guidStreamType: POINTER(Guid), ppConfig: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMutualExclusionCount(self, pcME: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetMutualExclusion(self, dwMEIndex: UInt32, ppME: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveMutualExclusion(self, pME: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddMutualExclusion(self, pME: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateNewMutualExclusion(self, ppME: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMutualExclusion)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMProfile2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile
    _iid_ = Guid('{07e72d33-d94e-4be7-8843-60ae5ff7e5f5}')
    @commethod(21)
    def GetProfileID(self, pguidID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMProfile3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile2
    _iid_ = Guid('{00ef96cc-a461-4546-8bcd-c9a28f0e06f5}')
    @commethod(22)
    def GetStorageFormat(self, pnStorageFormat: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetStorageFormat(self, nStorageFormat: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBandwidthSharingCount(self, pcBS: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetBandwidthSharing(self, dwBSIndex: UInt32, ppBS: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RemoveBandwidthSharing(self, pBS: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def AddBandwidthSharing(self, pBS: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreateNewBandwidthSharing(self, ppBS: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMBandwidthSharing)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetStreamPrioritization(self, ppSP: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamPrioritization)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetStreamPrioritization(self, pSP: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamPrioritization) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def RemoveStreamPrioritization(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateNewStreamPrioritization(self, ppSP: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamPrioritization)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetExpectedPacketCount(self, msDuration: UInt64, pcPackets: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMProfileManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d16679f2-6ca0-472d-8d31-2f5d55aee155}')
    @commethod(3)
    def CreateEmptyProfile(self, dwVersion: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION, ppProfile: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadProfileByID(self, guidProfile: POINTER(Guid), ppProfile: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadProfileByData(self, pwszProfile: win32more.Windows.Win32.Foundation.PWSTR, ppProfile: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SaveProfile(self, pIWMProfile: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile, pwszProfile: win32more.Windows.Win32.Foundation.PWSTR, pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSystemProfileCount(self, pcProfiles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def LoadSystemProfile(self, dwProfileIndex: UInt32, ppProfile: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMProfileManager2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfileManager
    _iid_ = Guid('{7a924e51-73c1-494d-8019-23d37ed9b89a}')
    @commethod(9)
    def GetSystemProfileVersion(self, pdwVersion: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSystemProfileVersion(self, dwVersion: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMProfileManagerLanguage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba4dcc78-7ee0-4ab8-b27a-dbce8bc51454}')
    @commethod(3)
    def GetUserLanguageID(self, wLangID: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetUserLanguageID(self, wLangID: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMPropertyVault(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{72995a79-5090-42a4-9c8c-d9d0b6d34be5}')
    @commethod(3)
    def GetPropertyCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyByName(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), dwSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyByIndex(self, dwIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pdwNameLen: POINTER(UInt32), pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPropertiesFrom(self, pIWMPropertyVault: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMPropertyVault) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMProximityDetection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a9fd8ee-b651-4bf0-b849-7d4ece79a2b1}')
    @commethod(3)
    def StartDetection(self, pbRegistrationMsg: POINTER(Byte), cbRegistrationMsg: UInt32, pbLocalAddress: POINTER(Byte), cbLocalAddress: UInt32, dwExtraPortsAllowed: UInt32, ppRegistrationResponseMsg: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bd6-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def Open(self, pwszURL: win32more.Windows.Win32.Foundation.PWSTR, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputCount(self, pcOutputs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputProps(self, dwOutputNum: UInt32, ppOutput: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetOutputProps(self, dwOutputNum: UInt32, pOutput: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputFormatCount(self, dwOutputNumber: UInt32, pcFormats: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOutputFormat(self, dwOutputNumber: UInt32, dwFormatNumber: UInt32, ppProps: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Start(self, cnsStart: UInt64, cnsDuration: UInt64, fRate: Single, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAccelerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bddc4d08-944d-4d52-a612-46c3fda07dd4}')
    @commethod(3)
    def GetCodecInterface(self, dwOutputNum: UInt32, riid: POINTER(Guid), ppvCodecInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Notify(self, dwOutputNum: UInt32, pSubtype: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bea-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def SetUserProvidedClock(self, fUserClock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUserProvidedClock(self, pfUserClock: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeliverTime(self, cnsTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetManualStreamSelection(self, fSelection: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetManualStreamSelection(self, pfSelection: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetStreamsSelected(self, cStreamCount: UInt16, pwStreamNumbers: POINTER(UInt16), pSelections: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreamSelected(self, wStreamNum: UInt16, pSelection: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetReceiveSelectionCallbacks(self, fGetCallbacks: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetReceiveSelectionCallbacks(self, pfGetCallbacks: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetReceiveStreamSamples(self, wStreamNum: UInt16, fReceiveStreamSamples: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetReceiveStreamSamples(self, wStreamNum: UInt16, pfReceiveStreamSamples: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetAllocateForOutput(self, dwOutputNum: UInt32, fAllocate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetAllocateForOutput(self, dwOutputNum: UInt32, pfAllocate: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetAllocateForStream(self, wStreamNum: UInt16, fAllocate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetAllocateForStream(self, dwSreamNum: UInt16, pfAllocate: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStatistics(self, pStatistics: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_READER_STATISTICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetClientInfo(self, pClientInfo: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_READER_CLIENTINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetMaxOutputSampleSize(self, dwOutput: UInt32, pcbMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetMaxStreamSampleSize(self, wStream: UInt16, pcbMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def NotifyLateDelivery(self, cnsLateness: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced
    _iid_ = Guid('{ae14a945-b90c-4d0d-9127-80d665f7d73e}')
    @commethod(23)
    def SetPlayMode(self, Mode: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetPlayMode(self, pMode: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetBufferProgress(self, pdwPercent: POINTER(UInt32), pcnsBuffering: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetDownloadProgress(self, pdwPercent: POINTER(UInt32), pqwBytesDownloaded: POINTER(UInt64), pcnsDownload: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetSaveAsProgress(self, pdwPercent: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SaveFileAs(self, pwszFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetProtocolName(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pcchProtocol: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def StartAtMarker(self, wMarkerIndex: UInt16, cnsDuration: UInt64, fRate: Single, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetOutputSetting(self, dwOutputNum: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetOutputSetting(self, dwOutputNum: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def Preroll(self, cnsStart: UInt64, cnsDuration: UInt64, fRate: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetLogClientID(self, fLogClientID: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetLogClientID(self, pfLogClientID: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def StopBuffering(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def OpenStream(self, pStream: win32more.Windows.Win32.System.Com.IStream, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced2
    _iid_ = Guid('{5dc0674b-f04b-4a4e-9f2a-b1afde2c8100}')
    @commethod(38)
    def StopNetStreaming(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def StartAtPosition(self, wStreamNum: UInt16, pvOffsetStart: VoidPtr, pvDuration: VoidPtr, dwOffsetFormat: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT, fRate: Single, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced4(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced3
    _iid_ = Guid('{945a76a2-12ae-4d48-bd3c-cd1d90399b85}')
    @commethod(40)
    def GetLanguageCount(self, dwOutputNum: UInt32, pwLanguageCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetLanguage(self, dwOutputNum: UInt32, wLanguage: UInt16, pwszLanguageString: win32more.Windows.Win32.Foundation.PWSTR, pcchLanguageStringLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetMaxSpeedFactor(self, pdblFactor: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IsUsingFastCache(self, pfUsingFastCache: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def AddLogParam(self, wszNameSpace: win32more.Windows.Win32.Foundation.PWSTR, wszName: win32more.Windows.Win32.Foundation.PWSTR, wszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SendLogParams(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CanSaveFileAs(self, pfCanSave: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def CancelSaveFileAs(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetURL(self, pwszURL: win32more.Windows.Win32.Foundation.PWSTR, pcchURL: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced5(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced4
    _iid_ = Guid('{24c44db0-55d1-49ae-a5cc-f13815e36363}')
    @commethod(49)
    def SetPlayerHook(self, dwOutputNum: UInt32, pHook: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMPlayerHook) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAdvanced6(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAdvanced5
    _iid_ = Guid('{18a2e7f8-428f-4acd-8a00-e64639bc93de}')
    @commethod(50)
    def SetProtectStreamSamples(self, pbCertificate: POINTER(Byte), cbCertificate: UInt32, dwCertificateType: UInt32, dwFlags: UInt32, pbInitializationVector: POINTER(Byte), pcbInitializationVector: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderAllocatorEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f762fa7-a22e-428d-93c9-ac82f3aafe5a}')
    @commethod(3)
    def AllocateForStreamEx(self, wStreamNum: UInt16, cbBuffer: UInt32, ppBuffer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), dwFlags: UInt32, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateForOutputEx(self, dwOutputNum: UInt32, cbBuffer: UInt32, ppBuffer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), dwFlags: UInt32, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderCallback(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback
    _iid_ = Guid('{96406bd8-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(4)
    def OnSample(self, dwOutputNum: UInt32, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderCallbackAdvanced(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406beb-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def OnStreamSample(self, wStreamNum: UInt16, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTime(self, cnsCurrentTime: UInt64, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnStreamSelection(self, wStreamCount: UInt16, pStreamNumbers: POINTER(UInt16), pSelections: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION), pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnOutputPropsChanged(self, dwOutputNum: UInt32, pMediaType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_MEDIA_TYPE), pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AllocateForStream(self, wStreamNum: UInt16, cbBuffer: UInt32, ppBuffer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AllocateForOutput(self, dwOutputNum: UInt32, cbBuffer: UInt32, ppBuffer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderNetworkConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bec-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetBufferingTime(self, pcnsBufferingTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBufferingTime(self, cnsBufferingTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUDPPortRanges(self, pRangeArray: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_PORT_NUMBER_RANGE), pcRanges: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetUDPPortRanges(self, pRangeArray: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_PORT_NUMBER_RANGE), cRanges: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProxySettings(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pProxySetting: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProxySettings(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, ProxySetting: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProxyHostName(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pwszHostName: win32more.Windows.Win32.Foundation.PWSTR, pcchHostName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetProxyHostName(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pwszHostName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProxyPort(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pdwPort: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetProxyPort(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, dwPort: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetProxyExceptionList(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pwszExceptionList: win32more.Windows.Win32.Foundation.PWSTR, pcchExceptionList: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetProxyExceptionList(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pwszExceptionList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetProxyBypassForLocal(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, pfBypassForLocal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetProxyBypassForLocal(self, pwszProtocol: win32more.Windows.Win32.Foundation.PWSTR, fBypassForLocal: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetForceRerunAutoProxyDetection(self, pfForceRerunDetection: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetForceRerunAutoProxyDetection(self, fForceRerunDetection: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetEnableMulticast(self, pfEnableMulticast: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetEnableMulticast(self, fEnableMulticast: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetEnableHTTP(self, pfEnableHTTP: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetEnableHTTP(self, fEnableHTTP: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetEnableUDP(self, pfEnableUDP: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetEnableUDP(self, fEnableUDP: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetEnableTCP(self, pfEnableTCP: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetEnableTCP(self, fEnableTCP: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def ResetProtocolRollover(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetConnectionBandwidth(self, pdwConnectionBandwidth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetConnectionBandwidth(self, dwConnectionBandwidth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetNumProtocolsSupported(self, pcProtocols: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetSupportedProtocolName(self, dwProtocolNum: UInt32, pwszProtocolName: win32more.Windows.Win32.Foundation.PWSTR, pcchProtocolName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def AddLoggingUrl(self, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetLoggingUrl(self, dwIndex: UInt32, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, pcchUrl: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetLoggingUrlCount(self, pdwUrlCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ResetLoggingUrlList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderNetworkConfig2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderNetworkConfig
    _iid_ = Guid('{d979a853-042b-4050-8387-c939db22013f}')
    @commethod(36)
    def GetEnableContentCaching(self, pfEnableContentCaching: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetEnableContentCaching(self, fEnableContentCaching: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetEnableFastCache(self, pfEnableFastCache: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetEnableFastCache(self, fEnableFastCache: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetAcceleratedStreamingDuration(self, pcnsAccelDuration: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetAcceleratedStreamingDuration(self, cnsAccelDuration: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetAutoReconnectLimit(self, pdwAutoReconnectLimit: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetAutoReconnectLimit(self, dwAutoReconnectLimit: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetEnableResends(self, pfEnableResends: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetEnableResends(self, fEnableResends: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetEnableThinning(self, pfEnableThinning: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def SetEnableThinning(self, fEnableThinning: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetMaxNetPacketSize(self, pdwMaxNetPacketSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderPlaylistBurn(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f28c0300-9baa-4477-a846-1744d9cbf533}')
    @commethod(3)
    def InitPlaylistBurn(self, cFiles: UInt32, ppwszFilenames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInitResults(self, cFiles: UInt32, phrStati: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndPlaylistBurn(self, hrBurnResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderStreamClock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bed-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetTime(self, pcnsNow: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTimer(self, cnsWhen: UInt64, pvParam: VoidPtr, pdwTimerId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def KillTimer(self, dwTimerId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderTimecode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f369e2f0-e081-4fe6-8450-b810b2f410d1}')
    @commethod(3)
    def GetTimecodeRangeCount(self, wStreamNum: UInt16, pwRangeCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimecodeRangeBounds(self, wStreamNum: UInt16, wRangeNum: UInt16, pStartTimecode: POINTER(UInt32), pEndTimecode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMReaderTypeNegotiation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fdbe5592-81a1-41ea-93bd-735cad1adc05}')
    @commethod(3)
    def TryOutputProps(self, dwOutputNum: UInt32, pOutput: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMRegisterCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf4b1f99-4de2-4e49-a363-252740d99bc1}')
    @commethod(3)
    def Advise(self, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMRegisteredDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a4503bec-5508-4148-97ac-bfa75760a70d}')
    @commethod(3)
    def GetDeviceSerialNumber(self, pSerialNumber: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.DRM_VAL16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceCertificate(self, ppCertificate: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeviceType(self, pdwType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributeCount(self, pcAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAttributeByIndex(self, dwIndex: UInt32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAttributeByName(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pbstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAttributeByName(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrValue: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Approve(self, fApprove: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsValid(self, pfValid: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsApproved(self, pfApproved: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsWmdrmCompliant(self, pfCompliant: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsOpened(self, pfOpened: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Open(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMSBufferAllocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61103ca4-2033-11d2-9ef1-006097d2d7cf}')
    @commethod(3)
    def AllocateBuffer(self, dwMaxBufferSize: UInt32, ppBuffer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocatePageSizeBuffer(self, dwMaxBufferSize: UInt32, ppBuffer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMSInternalAdminNetSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8bb23e5f-d127-4afb-8d02-ae5b66d54c78}')
    @commethod(3)
    def Initialize(self, pSharedNamespace: win32more.Windows.Win32.System.Com.IUnknown, pNamespaceNode: win32more.Windows.Win32.System.Com.IUnknown, pNetSourceCreator: win32more.Windows.Win32.Media.WindowsMediaFormat.INSNetSourceCreator, fEmbeddedInServer: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNetSourceCreator(self, ppNetSourceCreator: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSNetSourceCreator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCredentials(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, fPersist: win32more.Windows.Win32.Foundation.BOOL, fConfirmedGood: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCredentials(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrPassword: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfConfirmedGood: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteCredentials(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCredentialFlags(self, lpdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetCredentialFlags(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindProxyForURL(self, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR, bstrHost: win32more.Windows.Win32.Foundation.BSTR, pfProxyEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbstrProxyServer: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwProxyPort: POINTER(UInt32), pdwProxyContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterProxyFailure(self, hrParam: win32more.Windows.Win32.Foundation.HRESULT, dwProxyContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ShutdownProxyContext(self, dwProxyContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsUsingIE(self, dwProxyContext: UInt32, pfIsUsingIE: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMSInternalAdminNetSource2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e74d58c3-cf77-4b51-af17-744687c43eae}')
    @commethod(3)
    def SetCredentialsEx(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, fProxy: win32more.Windows.Win32.Foundation.BOOL, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, fPersist: win32more.Windows.Win32.Foundation.BOOL, fConfirmedGood: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCredentialsEx(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, fProxy: win32more.Windows.Win32.Foundation.BOOL, pdwUrlPolicy: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS), pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrPassword: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfConfirmedGood: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteCredentialsEx(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, fProxy: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindProxyForURLEx(self, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR, bstrHost: win32more.Windows.Win32.Foundation.BSTR, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, pfProxyEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbstrProxyServer: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwProxyPort: POINTER(UInt32), pdwProxyContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMSInternalAdminNetSource3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMSInternalAdminNetSource2
    _iid_ = Guid('{6b63d08e-4590-44af-9eb3-57ff1e73bf80}')
    @commethod(7)
    def GetNetSourceCreator2(self, ppNetSourceCreator: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindProxyForURLEx2(self, bstrProtocol: win32more.Windows.Win32.Foundation.BSTR, bstrHost: win32more.Windows.Win32.Foundation.BSTR, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, pfProxyEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbstrProxyServer: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwProxyPort: POINTER(UInt32), pqwProxyContext: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterProxyFailure2(self, hrParam: win32more.Windows.Win32.Foundation.HRESULT, qwProxyContext: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ShutdownProxyContext2(self, qwProxyContext: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsUsingIE2(self, qwProxyContext: UInt64, pfIsUsingIE: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCredentialsEx2(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, fProxy: win32more.Windows.Win32.Foundation.BOOL, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, fPersist: win32more.Windows.Win32.Foundation.BOOL, fConfirmedGood: win32more.Windows.Win32.Foundation.BOOL, fClearTextAuthentication: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCredentialsEx2(self, bstrRealm: win32more.Windows.Win32.Foundation.BSTR, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, fProxy: win32more.Windows.Win32.Foundation.BOOL, fClearTextAuthentication: win32more.Windows.Win32.Foundation.BOOL, pdwUrlPolicy: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS), pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrPassword: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfConfirmedGood: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMSecureChannel(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMAuthorizer
    _iid_ = Guid('{2720598a-d0f2-4189-bd10-91c46ef0936f}')
    @commethod(6)
    def WMSC_AddCertificate(self, pCert: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMAuthorizer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WMSC_AddSignature(self, pbCertSig: POINTER(Byte), cbCertSig: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WMSC_Connect(self, pOtherSide: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMSecureChannel) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WMSC_IsConnected(self, pfIsConnected: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WMSC_Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WMSC_GetValidCertificate(self, ppbCertificate: POINTER(POINTER(Byte)), pdwSignature: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WMSC_Encrypt(self, pbData: POINTER(Byte), cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WMSC_Decrypt(self, pbData: POINTER(Byte), cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WMSC_Lock(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WMSC_Unlock(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def WMSC_SetSharedData(self, dwCertIndex: UInt32, pbSharedData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMStatusCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d7cdc70-9888-11d3-8edc-00c04f6109cf}')
    @commethod(3)
    def OnStatus(self, Status: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS, hr: win32more.Windows.Win32.Foundation.HRESULT, dwType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMStreamConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bdc-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetStreamType(self, pguidStreamType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamNumber(self, pwStreamNum: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamNumber(self, wStreamNum: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamName(self, pwszStreamName: win32more.Windows.Win32.Foundation.PWSTR, pcchStreamName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetStreamName(self, pwszStreamName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetConnectionName(self, pwszInputName: win32more.Windows.Win32.Foundation.PWSTR, pcchInputName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetConnectionName(self, pwszInputName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBitrate(self, pdwBitrate: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetBitrate(self, pdwBitrate: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetBufferWindow(self, pmsBufferWindow: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetBufferWindow(self, msBufferWindow: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMStreamConfig2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig
    _iid_ = Guid('{7688d8cb-fc0d-43bd-9459-5a8dec200cfa}')
    @commethod(14)
    def GetTransportType(self, pnTransportType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetTransportType(self, nTransportType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddDataUnitExtension(self, guidExtensionSystemID: Guid, cbExtensionDataSize: UInt16, pbExtensionSystemInfo: POINTER(Byte), cbExtensionSystemInfo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDataUnitExtensionCount(self, pcDataUnitExtensions: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetDataUnitExtension(self, wDataUnitExtensionNumber: UInt16, pguidExtensionSystemID: POINTER(Guid), pcbExtensionDataSize: POINTER(UInt16), pbExtensionSystemInfo: POINTER(Byte), pcbExtensionSystemInfo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RemoveAllDataUnitExtensions(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMStreamConfig3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStreamConfig2
    _iid_ = Guid('{cb164104-3aa9-45a7-9ac9-4daee131d6e1}')
    @commethod(20)
    def GetLanguage(self, pwszLanguageString: win32more.Windows.Win32.Foundation.PWSTR, pcchLanguageStringLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetLanguage(self, pwszLanguageString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMStreamList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bdd-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetStreams(self, pwStreamNumArray: POINTER(UInt16), pcStreams: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddStream(self, wStreamNum: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveStream(self, wStreamNum: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMStreamPrioritization(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8c1c6090-f9a8-4748-8ec3-dd1108ba1e77}')
    @commethod(3)
    def GetPriorityRecords(self, pRecordArray: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_STREAM_PRIORITY_RECORD), pcRecords: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPriorityRecords(self, pRecordArray: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_STREAM_PRIORITY_RECORD), cRecords: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMSyncReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9397f121-7705-4dc9-b049-98b698188414}')
    @commethod(3)
    def Open(self, pwszFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRange(self, cnsStartTime: UInt64, cnsDuration: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRangeByFrame(self, wStreamNum: UInt16, qwFrameNumber: UInt64, cFramesToRead: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNextSample(self, wStreamNum: UInt16, ppSample: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pcnsSampleTime: POINTER(UInt64), pcnsDuration: POINTER(UInt64), pdwFlags: POINTER(UInt32), pdwOutputNum: POINTER(UInt32), pwStreamNum: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetStreamsSelected(self, cStreamCount: UInt16, pwStreamNumbers: POINTER(UInt16), pSelections: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreamSelected(self, wStreamNum: UInt16, pSelection: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetReadStreamSamples(self, wStreamNum: UInt16, fCompressed: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetReadStreamSamples(self, wStreamNum: UInt16, pfCompressed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetOutputSetting(self, dwOutputNum: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetOutputSetting(self, dwOutputNum: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetOutputCount(self, pcOutputs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetOutputProps(self, dwOutputNum: UInt32, ppOutput: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetOutputProps(self, dwOutputNum: UInt32, pOutput: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetOutputFormatCount(self, dwOutputNum: UInt32, pcFormats: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetOutputFormat(self, dwOutputNum: UInt32, dwFormatNum: UInt32, ppProps: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMOutputMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetOutputNumberForStream(self, wStreamNum: UInt16, pdwOutputNum: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetStreamNumberForOutput(self, dwOutputNum: UInt32, pwStreamNum: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetMaxOutputSampleSize(self, dwOutput: UInt32, pcbMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetMaxStreamSampleSize(self, wStream: UInt16, pcbMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def OpenStream(self, pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMSyncReader2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMSyncReader
    _iid_ = Guid('{faed3d21-1b6b-4af7-8cb6-3e189bbc187b}')
    @commethod(24)
    def SetRangeByTimecode(self, wStreamNum: UInt16, pStart: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_EXTENSION_DATA), pEnd: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_EXTENSION_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetRangeByFrameEx(self, wStreamNum: UInt16, qwFrameNumber: UInt64, cFramesToRead: Int64, pcnsStartTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetAllocateForOutput(self, dwOutputNum: UInt32, pAllocator: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetAllocateForOutput(self, dwOutputNum: UInt32, ppAllocator: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetAllocateForStream(self, wStreamNum: UInt16, pAllocator: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetAllocateForStream(self, dwSreamNum: UInt16, ppAllocator: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMReaderAllocatorEx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMVideoMediaProps(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps
    _iid_ = Guid('{96406bcf-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(6)
    def GetMaxKeyFrameSpacing(self, pllTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMaxKeyFrameSpacing(self, llTime: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuality(self, pdwQuality: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetQuality(self, dwQuality: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWatermarkInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6f497062-f2e2-4624-8ea7-9dd40d81fc8d}')
    @commethod(3)
    def GetWatermarkEntryCount(self, wmetType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWatermarkEntry(self, wmetType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE, dwEntryNum: UInt32, pEntry: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406bd4-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def SetProfileByID(self, guidProfile: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProfile(self, pProfile: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFilename(self, pwszFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputCount(self, pcInputs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInputProps(self, dwInputNum: UInt32, ppInput: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMInputMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetInputProps(self, dwInputNum: UInt32, pInput: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMInputMediaProps) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInputFormatCount(self, dwInputNumber: UInt32, pcFormats: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInputFormat(self, dwInputNumber: UInt32, dwFormatNumber: UInt32, pProps: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMInputMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def BeginWriting(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndWriting(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AllocateSample(self, dwSampleSize: UInt32, ppSample: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteSample(self, dwInputNum: UInt32, cnsSampleTime: UInt64, dwFlags: UInt32, pSample: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterAdvanced(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406be3-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def GetSinkCount(self, pcSinks: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSink(self, dwSinkNum: UInt32, ppSink: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddSink(self, pSink: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveSink(self, pSink: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WriteStreamSample(self, wStreamNum: UInt16, cnsSampleTime: UInt64, msSampleSendTime: UInt32, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetLiveSource(self, fIsLiveSource: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsRealTime(self, pfRealTime: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetWriterTime(self, pcnsCurrentTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStatistics(self, wStreamNum: UInt16, pStats: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_WRITER_STATISTICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetSyncTolerance(self, msWindow: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSyncTolerance(self, pmsWindow: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterAdvanced2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterAdvanced
    _iid_ = Guid('{962dc1ec-c046-4db8-9cc7-26ceae500817}')
    @commethod(14)
    def GetInputSetting(self, dwInputNum: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE), pValue: POINTER(Byte), pcbLength: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetInputSetting(self, dwInputNum: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE, pValue: POINTER(Byte), cbLength: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterAdvanced3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterAdvanced2
    _iid_ = Guid('{2cd6492d-7c37-4e76-9d3b-59261183a22e}')
    @commethod(16)
    def GetStatisticsEx(self, wStreamNum: UInt16, pStats: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WM_WRITER_STATISTICS_EX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetNonBlocking(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterFileSink(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink
    _iid_ = Guid('{96406be5-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(8)
    def Open(self, pwszFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterFileSink2(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterFileSink
    _iid_ = Guid('{14282ba7-4aef-4205-8ce5-c229035a05bc}')
    @commethod(9)
    def Start(self, cnsStartTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Stop(self, cnsStopTime: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsStopped(self, pfStopped: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFileDuration(self, pcnsDuration: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFileSize(self, pcbFile: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsClosed(self, pfClosed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterFileSink3(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterFileSink2
    _iid_ = Guid('{3fea4feb-2945-47a7-a1dd-c53a8fc4c45c}')
    @commethod(16)
    def SetAutoIndexing(self, fDoAutoIndexing: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetAutoIndexing(self, pfAutoIndexing: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetControlStream(self, wStreamNumber: UInt16, fShouldControlStartAndStop: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetMode(self, pdwFileSinkMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnDataUnitEx(self, pFileSinkDataUnit: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_FILESINK_DATA_UNIT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetUnbufferedIO(self, fUnbufferedIO: win32more.Windows.Win32.Foundation.BOOL, fRestrictMemUsage: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetUnbufferedIO(self, pfUnbufferedIO: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CompleteOperations(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterNetworkSink(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink
    _iid_ = Guid('{96406be7-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(8)
    def SetMaximumClients(self, dwMaxClients: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMaximumClients(self, pdwMaxClients: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetNetworkProtocol(self, protocol: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_NET_PROTOCOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkProtocol(self, pProtocol: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_NET_PROTOCOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHostURL(self, pwszURL: win32more.Windows.Win32.Foundation.PWSTR, pcchURL: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Open(self, pdwPortNum: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPostView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{81e20ce4-75ef-491a-8004-fc53c45bdc3e}')
    @commethod(3)
    def SetPostViewCallback(self, pCallback: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterPostViewCallback, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetReceivePostViewSamples(self, wStreamNum: UInt16, fReceivePostViewSamples: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReceivePostViewSamples(self, wStreamNum: UInt16, pfReceivePostViewSamples: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPostViewProps(self, wStreamNumber: UInt16, ppOutput: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPostViewProps(self, wStreamNumber: UInt16, pOutput: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPostViewFormatCount(self, wStreamNumber: UInt16, pcFormats: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPostViewFormat(self, wStreamNumber: UInt16, dwFormatNumber: UInt32, ppProps: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMMediaProps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetAllocateForPostView(self, wStreamNumber: UInt16, fAllocate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetAllocateForPostView(self, wStreamNumber: UInt16, pfAllocate: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPostViewCallback(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMStatusCallback
    _iid_ = Guid('{d9d6549d-a193-4f24-b308-03123d9b7f8d}')
    @commethod(4)
    def OnPostViewSample(self, wStreamNumber: UInt16, cnsSampleTime: UInt64, cnsSampleDuration: UInt64, dwFlags: UInt32, pSample: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateForPostView(self, wStreamNum: UInt16, cbBuffer: UInt32, ppBuffer: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer), pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPreprocess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc54a285-38c4-45b5-aa23-85b9f7cb424b}')
    @commethod(3)
    def GetMaxPreprocessingPasses(self, dwInputNum: UInt32, dwFlags: UInt32, pdwMaxNumPasses: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNumPreprocessingPasses(self, dwInputNum: UInt32, dwFlags: UInt32, dwNumPasses: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginPreprocessingPass(self, dwInputNum: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PreprocessSample(self, dwInputNum: UInt32, cnsSampleTime: UInt64, dwFlags: UInt32, pSample: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EndPreprocessingPass(self, dwInputNum: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterPushSink(ComPtr):
    extends: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMWriterSink
    _iid_ = Guid('{dc10e6a5-072c-467d-bf57-6330a9dde12a}')
    @commethod(8)
    def Connect(self, pwszURL: win32more.Windows.Win32.Foundation.PWSTR, pwszTemplateURL: win32more.Windows.Win32.Foundation.PWSTR, fAutoDestroy: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndSession(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMWriterSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96406be4-2b2b-11d3-b36b-00c04f6108ff}')
    @commethod(3)
    def OnHeader(self, pHeader: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsRealTime(self, pfRealTime: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateDataUnit(self, cbDataUnit: UInt32, ppDataUnit: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDataUnit(self, pDataUnit: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnEndWriting(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
NETSOURCE_URLCREDPOLICY_SETTINGS = Int32
NETSOURCE_URLCREDPOLICY_SETTING_SILENTLOGONOK: win32more.Windows.Win32.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS = 0
NETSOURCE_URLCREDPOLICY_SETTING_MUSTPROMPTUSER: win32more.Windows.Win32.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS = 1
NETSOURCE_URLCREDPOLICY_SETTING_ANONYMOUSONLY: win32more.Windows.Win32.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS = 2
WEBSTREAM_SAMPLE_TYPE = Int32
WEBSTREAM_SAMPLE_TYPE_FILE: win32more.Windows.Win32.Media.WindowsMediaFormat.WEBSTREAM_SAMPLE_TYPE = 1
WEBSTREAM_SAMPLE_TYPE_RENDER: win32more.Windows.Win32.Media.WindowsMediaFormat.WEBSTREAM_SAMPLE_TYPE = 2
class WMDRM_IMPORT_INIT_STRUCT(Structure):
    dwVersion: UInt32
    cbEncryptedSessionKeyMessage: UInt32
    pbEncryptedSessionKeyMessage: POINTER(Byte)
    cbEncryptedKeyMessage: UInt32
    pbEncryptedKeyMessage: POINTER(Byte)
class WMMPEG2VIDEOINFO(Structure):
    hdr: win32more.Windows.Win32.Media.WindowsMediaFormat.WMVIDEOINFOHEADER2
    dwStartTimeCode: UInt32
    cbSequenceHeader: UInt32
    dwProfile: UInt32
    dwLevel: UInt32
    dwFlags: UInt32
    dwSequenceHeader: UInt32 * 1
class WMSCRIPTFORMAT(Structure):
    scriptType: Guid
WMT_ATTR_DATATYPE = Int32
WMT_TYPE_DWORD: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE = 0
WMT_TYPE_STRING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE = 1
WMT_TYPE_BINARY: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE = 2
WMT_TYPE_BOOL: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE = 3
WMT_TYPE_QWORD: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE = 4
WMT_TYPE_WORD: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE = 5
WMT_TYPE_GUID: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE = 6
WMT_ATTR_IMAGETYPE = Int32
WMT_IMAGETYPE_BITMAP: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_IMAGETYPE = 1
WMT_IMAGETYPE_JPEG: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_IMAGETYPE = 2
WMT_IMAGETYPE_GIF: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_ATTR_IMAGETYPE = 3
class WMT_BUFFER_SEGMENT(Structure):
    pBuffer: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer
    cbOffset: UInt32
    cbLength: UInt32
WMT_CODEC_INFO_TYPE = Int32
WMT_CODECINFO_AUDIO: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE = 0
WMT_CODECINFO_VIDEO: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE = 1
WMT_CODECINFO_UNKNOWN: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE = -1
class WMT_COLORSPACEINFO_EXTENSION_DATA(Structure):
    ucColorPrimaries: Byte
    ucColorTransferChar: Byte
    ucColorMatrixCoef: Byte
WMT_CREDENTIAL_FLAGS = Int32
WMT_CREDENTIAL_SAVE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CREDENTIAL_FLAGS = 1
WMT_CREDENTIAL_DONT_CACHE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CREDENTIAL_FLAGS = 2
WMT_CREDENTIAL_CLEAR_TEXT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CREDENTIAL_FLAGS = 4
WMT_CREDENTIAL_PROXY: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CREDENTIAL_FLAGS = 8
WMT_CREDENTIAL_ENCRYPT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_CREDENTIAL_FLAGS = 16
WMT_DRMLA_TRUST = Int32
WMT_DRMLA_UNTRUSTED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_DRMLA_TRUST = 0
WMT_DRMLA_TRUSTED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_DRMLA_TRUST = 1
WMT_DRMLA_TAMPERED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_DRMLA_TRUST = 2
class WMT_FILESINK_DATA_UNIT(Structure):
    packetHeaderBuffer: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT
    cPayloads: UInt32
    pPayloadHeaderBuffers: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT)
    cPayloadDataFragments: UInt32
    pPayloadDataFragments: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PAYLOAD_FRAGMENT)
WMT_FILESINK_MODE = Int32
WMT_FM_SINGLE_BUFFERS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_FILESINK_MODE = 1
WMT_FM_FILESINK_DATA_UNITS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_FILESINK_MODE = 2
WMT_FM_FILESINK_UNBUFFERED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_FILESINK_MODE = 4
WMT_IMAGE_TYPE = Int32
WMT_IT_NONE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_IMAGE_TYPE = 0
WMT_IT_BITMAP: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_IMAGE_TYPE = 1
WMT_IT_JPEG: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_IMAGE_TYPE = 2
WMT_IT_GIF: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_IMAGE_TYPE = 3
WMT_INDEXER_TYPE = Int32
WMT_IT_PRESENTATION_TIME: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_INDEXER_TYPE = 0
WMT_IT_FRAME_NUMBERS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_INDEXER_TYPE = 1
WMT_IT_TIMECODE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_INDEXER_TYPE = 2
WMT_INDEX_TYPE = Int32
WMT_IT_NEAREST_DATA_UNIT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_INDEX_TYPE = 1
WMT_IT_NEAREST_OBJECT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_INDEX_TYPE = 2
WMT_IT_NEAREST_CLEAN_POINT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_INDEX_TYPE = 3
WMT_MUSICSPEECH_CLASS_MODE = Int32
WMT_MS_CLASS_MUSIC: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_MUSICSPEECH_CLASS_MODE = 0
WMT_MS_CLASS_SPEECH: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_MUSICSPEECH_CLASS_MODE = 1
WMT_MS_CLASS_MIXED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_MUSICSPEECH_CLASS_MODE = 2
WMT_NET_PROTOCOL = Int32
WMT_PROTOCOL_HTTP: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_NET_PROTOCOL = 0
WMT_OFFSET_FORMAT = Int32
WMT_OFFSET_FORMAT_100NS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT = 0
WMT_OFFSET_FORMAT_FRAME_NUMBERS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT = 1
WMT_OFFSET_FORMAT_PLAYLIST_OFFSET: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT = 2
WMT_OFFSET_FORMAT_TIMECODE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT = 3
WMT_OFFSET_FORMAT_100NS_APPROXIMATE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT = 4
class WMT_PAYLOAD_FRAGMENT(Structure):
    dwPayloadIndex: UInt32
    segmentData: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT
WMT_PLAY_MODE = Int32
WMT_PLAY_MODE_AUTOSELECT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE = 0
WMT_PLAY_MODE_LOCAL: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE = 1
WMT_PLAY_MODE_DOWNLOAD: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE = 2
WMT_PLAY_MODE_STREAMING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PLAY_MODE = 3
WMT_PROXY_SETTINGS = Int32
WMT_PROXY_SETTING_NONE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS = 0
WMT_PROXY_SETTING_MANUAL: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS = 1
WMT_PROXY_SETTING_AUTO: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS = 2
WMT_PROXY_SETTING_BROWSER: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS = 3
WMT_PROXY_SETTING_MAX: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS = 4
WMT_RIGHTS = Int32
WMT_RIGHT_PLAYBACK: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 1
WMT_RIGHT_COPY_TO_NON_SDMI_DEVICE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 2
WMT_RIGHT_COPY_TO_CD: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 8
WMT_RIGHT_COPY_TO_SDMI_DEVICE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 16
WMT_RIGHT_ONE_TIME: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 32
WMT_RIGHT_SAVE_STREAM_PROTECTED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 64
WMT_RIGHT_COPY: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 128
WMT_RIGHT_COLLABORATIVE_PLAY: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 256
WMT_RIGHT_SDMI_TRIGGER: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 65536
WMT_RIGHT_SDMI_NOMORECOPIES: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_RIGHTS = 131072
WMT_STATUS = Int32
WMT_ERROR: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 0
WMT_OPENED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 1
WMT_BUFFERING_START: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 2
WMT_BUFFERING_STOP: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 3
WMT_EOF: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 4
WMT_END_OF_FILE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 4
WMT_END_OF_SEGMENT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 5
WMT_END_OF_STREAMING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 6
WMT_LOCATING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 7
WMT_CONNECTING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 8
WMT_NO_RIGHTS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 9
WMT_MISSING_CODEC: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 10
WMT_STARTED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 11
WMT_STOPPED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 12
WMT_CLOSED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 13
WMT_STRIDING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 14
WMT_TIMER: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 15
WMT_INDEX_PROGRESS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 16
WMT_SAVEAS_START: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 17
WMT_SAVEAS_STOP: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 18
WMT_NEW_SOURCEFLAGS: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 19
WMT_NEW_METADATA: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 20
WMT_BACKUPRESTORE_BEGIN: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 21
WMT_SOURCE_SWITCH: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 22
WMT_ACQUIRE_LICENSE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 23
WMT_INDIVIDUALIZE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 24
WMT_NEEDS_INDIVIDUALIZATION: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 25
WMT_NO_RIGHTS_EX: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 26
WMT_BACKUPRESTORE_END: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 27
WMT_BACKUPRESTORE_CONNECTING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 28
WMT_BACKUPRESTORE_DISCONNECTING: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 29
WMT_ERROR_WITHURL: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 30
WMT_RESTRICTED_LICENSE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 31
WMT_CLIENT_CONNECT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 32
WMT_CLIENT_DISCONNECT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 33
WMT_NATIVE_OUTPUT_PROPS_CHANGED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 34
WMT_RECONNECT_START: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 35
WMT_RECONNECT_END: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 36
WMT_CLIENT_CONNECT_EX: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 37
WMT_CLIENT_DISCONNECT_EX: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 38
WMT_SET_FEC_SPAN: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 39
WMT_PREROLL_READY: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 40
WMT_PREROLL_COMPLETE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 41
WMT_CLIENT_PROPERTIES: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 42
WMT_LICENSEURL_SIGNATURE_STATE: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 43
WMT_INIT_PLAYLIST_BURN: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 44
WMT_TRANSCRYPTOR_INIT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 45
WMT_TRANSCRYPTOR_SEEKED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 46
WMT_TRANSCRYPTOR_READ: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 47
WMT_TRANSCRYPTOR_CLOSED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 48
WMT_PROXIMITY_RESULT: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 49
WMT_PROXIMITY_COMPLETED: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 50
WMT_CONTENT_ENABLER: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STATUS = 51
WMT_STORAGE_FORMAT = Int32
WMT_Storage_Format_MP3: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT = 0
WMT_Storage_Format_V1: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT = 1
WMT_STREAM_SELECTION = Int32
WMT_OFF: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION = 0
WMT_CLEANPOINT_ONLY: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION = 1
WMT_ON: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_STREAM_SELECTION = 2
class WMT_TIMECODE_EXTENSION_DATA(Structure):
    wRange: UInt16
    dwTimecode: UInt32
    dwUserbits: UInt32
    dwAmFlags: UInt32
    _pack_ = 2
WMT_TIMECODE_FRAMERATE = Int32
WMT_TIMECODE_FRAMERATE_30: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_FRAMERATE = 0
WMT_TIMECODE_FRAMERATE_30DROP: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_FRAMERATE = 1
WMT_TIMECODE_FRAMERATE_25: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_FRAMERATE = 2
WMT_TIMECODE_FRAMERATE_24: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TIMECODE_FRAMERATE = 3
WMT_TRANSPORT_TYPE = Int32
WMT_Transport_Type_Unreliable: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE = 0
WMT_Transport_Type_Reliable: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE = 1
WMT_VERSION = Int32
WMT_VER_4_0: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION = 262144
WMT_VER_7_0: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION = 458752
WMT_VER_8_0: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION = 524288
WMT_VER_9_0: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_VERSION = 589824
class WMT_VIDEOIMAGE_SAMPLE(Structure):
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
class WMT_VIDEOIMAGE_SAMPLE2(Structure):
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
    bKeepPrevImage: win32more.Windows.Win32.Foundation.BOOL
class WMT_WATERMARK_ENTRY(Structure):
    wmetType: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE
    clsid: Guid
    cbDisplayName: UInt32
    pwszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
WMT_WATERMARK_ENTRY_TYPE = Int32
WMT_WMETYPE_AUDIO: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE = 1
WMT_WMETYPE_VIDEO: win32more.Windows.Win32.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE = 2
class WMT_WEBSTREAM_FORMAT(Structure):
    cbSize: UInt16
    cbSampleHeaderFixedData: UInt16
    wVersion: UInt16
    wReserved: UInt16
class WMT_WEBSTREAM_SAMPLE_HEADER(Structure):
    cbLength: UInt16
    wPart: UInt16
    cTotalParts: UInt16
    wSampleType: UInt16
    wszURL: Char * 1
class WMVIDEOINFOHEADER(Structure):
    rcSource: win32more.Windows.Win32.Foundation.RECT
    rcTarget: win32more.Windows.Win32.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    bmiHeader: win32more.Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER
class WMVIDEOINFOHEADER2(Structure):
    rcSource: win32more.Windows.Win32.Foundation.RECT
    rcTarget: win32more.Windows.Win32.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    dwInterlaceFlags: UInt32
    dwCopyProtectFlags: UInt32
    dwPictAspectRatioX: UInt32
    dwPictAspectRatioY: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
    bmiHeader: win32more.Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER
class WM_ADDRESS_ACCESSENTRY(Structure):
    dwIPAddress: UInt32
    dwMask: UInt32
WM_AETYPE = Int32
WM_AETYPE_INCLUDE: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE = 105
WM_AETYPE_EXCLUDE: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_AETYPE = 101
class WM_CLIENT_PROPERTIES(Structure):
    dwIPAddress: UInt32
    dwPort: UInt32
class WM_CLIENT_PROPERTIES_EX(Structure):
    cbSize: UInt32
    pwszIPAddress: win32more.Windows.Win32.Foundation.PWSTR
    pwszPort: win32more.Windows.Win32.Foundation.PWSTR
    pwszDNSName: win32more.Windows.Win32.Foundation.PWSTR
WM_DM_INTERLACED_TYPE = Int32
WM_DM_NOTINTERLACED: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_INTERLACED_TYPE = 0
WM_DM_DEINTERLACE_NORMAL: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_INTERLACED_TYPE = 1
WM_DM_DEINTERLACE_HALFSIZE: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_INTERLACED_TYPE = 2
WM_DM_DEINTERLACE_HALFSIZEDOUBLERATE: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_INTERLACED_TYPE = 3
WM_DM_DEINTERLACE_INVERSETELECINE: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_INTERLACED_TYPE = 4
WM_DM_DEINTERLACE_VERTICALHALFSIZEDOUBLERATE: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_INTERLACED_TYPE = 5
WM_DM_IT_FIRST_FRAME_COHERENCY = Int32
WM_DM_IT_DISABLE_COHERENT_MODE: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 0
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_TOP: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 1
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_TOP: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 2
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_TOP: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 3
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_TOP: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 4
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_TOP: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 5
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_BOTTOM: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 6
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_BOTTOM: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 7
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_BOTTOM: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 8
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_BOTTOM: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 9
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_BOTTOM: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_DM_IT_FIRST_FRAME_COHERENCY = 10
class WM_LEAKY_BUCKET_PAIR(Structure):
    dwBitrate: UInt32
    msBufferWindow: UInt32
    _pack_ = 1
class WM_MEDIA_TYPE(Structure):
    majortype: Guid
    subtype: Guid
    bFixedSizeSamples: win32more.Windows.Win32.Foundation.BOOL
    bTemporalCompression: win32more.Windows.Win32.Foundation.BOOL
    lSampleSize: UInt32
    formattype: Guid
    pUnk: win32more.Windows.Win32.System.Com.IUnknown
    cbFormat: UInt32
    pbFormat: POINTER(Byte)
class WM_PICTURE(Structure):
    pwszMIMEType: win32more.Windows.Win32.Foundation.PWSTR
    bPictureType: Byte
    pwszDescription: win32more.Windows.Win32.Foundation.PWSTR
    dwDataLen: UInt32
    pbData: POINTER(Byte)
    _pack_ = 1
WM_PLAYBACK_DRC_LEVEL = Int32
WM_PLAYBACK_DRC_HIGH: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_PLAYBACK_DRC_LEVEL = 0
WM_PLAYBACK_DRC_MEDIUM: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_PLAYBACK_DRC_LEVEL = 1
WM_PLAYBACK_DRC_LOW: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_PLAYBACK_DRC_LEVEL = 2
class WM_PORT_NUMBER_RANGE(Structure):
    wPortBegin: UInt16
    wPortEnd: UInt16
class WM_READER_CLIENTINFO(Structure):
    cbSize: UInt32
    wszLang: win32more.Windows.Win32.Foundation.PWSTR
    wszBrowserUserAgent: win32more.Windows.Win32.Foundation.PWSTR
    wszBrowserWebPage: win32more.Windows.Win32.Foundation.PWSTR
    qwReserved: UInt64
    pReserved: POINTER(win32more.Windows.Win32.Foundation.LPARAM)
    wszHostExe: win32more.Windows.Win32.Foundation.PWSTR
    qwHostVersion: UInt64
    wszPlayerUserAgent: win32more.Windows.Win32.Foundation.PWSTR
class WM_READER_STATISTICS(Structure):
    cbSize: UInt32
    dwBandwidth: UInt32
    cPacketsReceived: UInt32
    cPacketsRecovered: UInt32
    cPacketsLost: UInt32
    wQuality: UInt16
WM_SFEX_TYPE = Int32
WM_SFEX_NOTASYNCPOINT: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_SFEX_TYPE = 2
WM_SFEX_DATALOSS: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_SFEX_TYPE = 4
WM_SF_TYPE = Int32
WM_SF_CLEANPOINT: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_SF_TYPE = 1
WM_SF_DISCONTINUITY: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_SF_TYPE = 2
WM_SF_DATALOSS: win32more.Windows.Win32.Media.WindowsMediaFormat.WM_SF_TYPE = 4
class WM_STREAM_PRIORITY_RECORD(Structure):
    wStreamNumber: UInt16
    fMandatory: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 2
class WM_STREAM_TYPE_INFO(Structure):
    guidMajorType: Guid
    cbFormat: UInt32
    _pack_ = 1
class WM_SYNCHRONISED_LYRICS(Structure):
    bTimeStampFormat: Byte
    bContentType: Byte
    pwszContentDescriptor: win32more.Windows.Win32.Foundation.PWSTR
    dwLyricsLen: UInt32
    pbLyrics: POINTER(Byte)
    _pack_ = 1
class WM_USER_TEXT(Structure):
    pwszDescription: win32more.Windows.Win32.Foundation.PWSTR
    pwszText: win32more.Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class WM_USER_WEB_URL(Structure):
    pwszDescription: win32more.Windows.Win32.Foundation.PWSTR
    pwszURL: win32more.Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class WM_WRITER_STATISTICS(Structure):
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
class WM_WRITER_STATISTICS_EX(Structure):
    dwBitratePlusOverhead: UInt32
    dwCurrentSampleDropRateInQueue: UInt32
    dwCurrentSampleDropRateInCodec: UInt32
    dwCurrentSampleDropRateInMultiplexer: UInt32
    dwTotalSampleDropsInQueue: UInt32
    dwTotalSampleDropsInCodec: UInt32
    dwTotalSampleDropsInMultiplexer: UInt32
_AM_ASFWRITERCONFIG_PARAM = Int32
AM_CONFIGASFWRITER_PARAM_AUTOINDEX: win32more.Windows.Win32.Media.WindowsMediaFormat._AM_ASFWRITERCONFIG_PARAM = 1
AM_CONFIGASFWRITER_PARAM_MULTIPASS: win32more.Windows.Win32.Media.WindowsMediaFormat._AM_ASFWRITERCONFIG_PARAM = 2
AM_CONFIGASFWRITER_PARAM_DONTCOMPRESS: win32more.Windows.Win32.Media.WindowsMediaFormat._AM_ASFWRITERCONFIG_PARAM = 3


make_ready(__name__)
