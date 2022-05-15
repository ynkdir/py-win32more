from win32more import *
import win32more.Media.WindowsMediaFormat
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Media.DirectShow
import win32more.System.Com

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Media.WindowsMediaFormat, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Media.WindowsMediaFormat, name)
def __dir__():
    return __all__
WMT_VIDEOIMAGE_SAMPLE_INPUT_FRAME = 1
WMT_VIDEOIMAGE_SAMPLE_OUTPUT_FRAME = 2
WMT_VIDEOIMAGE_SAMPLE_USES_CURRENT_INPUT_FRAME = 4
WMT_VIDEOIMAGE_SAMPLE_USES_PREVIOUS_INPUT_FRAME = 8
WMT_VIDEOIMAGE_SAMPLE_MOTION = 1
WMT_VIDEOIMAGE_SAMPLE_ROTATION = 2
WMT_VIDEOIMAGE_SAMPLE_BLENDING = 4
WMT_VIDEOIMAGE_SAMPLE_ADV_BLENDING = 8
WMT_VIDEOIMAGE_INTEGER_DENOMINATOR = 65536
WMT_VIDEOIMAGE_MAGIC_NUMBER = 491406834
WMT_VIDEOIMAGE_MAGIC_NUMBER_2 = 491406835
WMT_VIDEOIMAGE_TRANSITION_BOW_TIE = 11
WMT_VIDEOIMAGE_TRANSITION_CIRCLE = 12
WMT_VIDEOIMAGE_TRANSITION_CROSS_FADE = 13
WMT_VIDEOIMAGE_TRANSITION_DIAGONAL = 14
WMT_VIDEOIMAGE_TRANSITION_DIAMOND = 15
WMT_VIDEOIMAGE_TRANSITION_FADE_TO_COLOR = 16
WMT_VIDEOIMAGE_TRANSITION_FILLED_V = 17
WMT_VIDEOIMAGE_TRANSITION_FLIP = 18
WMT_VIDEOIMAGE_TRANSITION_INSET = 19
WMT_VIDEOIMAGE_TRANSITION_IRIS = 20
WMT_VIDEOIMAGE_TRANSITION_PAGE_ROLL = 21
WMT_VIDEOIMAGE_TRANSITION_RECTANGLE = 23
WMT_VIDEOIMAGE_TRANSITION_REVEAL = 24
WMT_VIDEOIMAGE_TRANSITION_SLIDE = 27
WMT_VIDEOIMAGE_TRANSITION_SPLIT = 29
WMT_VIDEOIMAGE_TRANSITION_STAR = 30
WMT_VIDEOIMAGE_TRANSITION_WHEEL = 31
WM_SampleExtension_ContentType_Size = 1
WM_SampleExtension_PixelAspectRatio_Size = 2
WM_SampleExtension_Timecode_Size = 14
WM_SampleExtension_SampleDuration_Size = 2
WM_SampleExtension_ChromaLocation_Size = 1
WM_SampleExtension_ColorSpaceInfo_Size = 3
WM_CT_REPEAT_FIRST_FIELD = 16
WM_CT_BOTTOM_FIELD_FIRST = 32
WM_CT_TOP_FIELD_FIRST = 64
WM_CT_INTERLACED = 128
WM_CL_INTERLACED420 = 0
WM_CL_PROGRESSIVE420 = 1
WM_MAX_VIDEO_STREAMS = 63
WM_MAX_STREAMS = 63
WMDRM_IMPORT_INIT_STRUCT_DEFINED = 1
DRM_OPL_TYPES = 1
g_dwWMSpecialAttributes = 20
g_wszWMDuration = 'Duration'
g_wszWMBitrate = 'Bitrate'
g_wszWMSeekable = 'Seekable'
g_wszWMStridable = 'Stridable'
g_wszWMBroadcast = 'Broadcast'
g_wszWMProtected = 'Is_Protected'
g_wszWMTrusted = 'Is_Trusted'
g_wszWMSignature_Name = 'Signature_Name'
g_wszWMHasAudio = 'HasAudio'
g_wszWMHasImage = 'HasImage'
g_wszWMHasScript = 'HasScript'
g_wszWMHasVideo = 'HasVideo'
g_wszWMCurrentBitrate = 'CurrentBitrate'
g_wszWMOptimalBitrate = 'OptimalBitrate'
g_wszWMHasAttachedImages = 'HasAttachedImages'
g_wszWMSkipBackward = 'Can_Skip_Backward'
g_wszWMSkipForward = 'Can_Skip_Forward'
g_wszWMNumberOfFrames = 'NumberOfFrames'
g_wszWMFileSize = 'FileSize'
g_wszWMHasArbitraryDataStream = 'HasArbitraryDataStream'
g_wszWMHasFileTransferStream = 'HasFileTransferStream'
g_wszWMContainerFormat = 'WM/ContainerFormat'
g_dwWMContentAttributes = 5
g_wszWMTitle = 'Title'
g_wszWMTitleSort = 'TitleSort'
g_wszWMAuthor = 'Author'
g_wszWMAuthorSort = 'AuthorSort'
g_wszWMDescription = 'Description'
g_wszWMRating = 'Rating'
g_wszWMCopyright = 'Copyright'
g_wszWMUse_DRM = 'Use_DRM'
g_wszWMDRM_Flags = 'DRM_Flags'
g_wszWMDRM_Level = 'DRM_Level'
g_wszWMUse_Advanced_DRM = 'Use_Advanced_DRM'
g_wszWMDRM_KeySeed = 'DRM_KeySeed'
g_wszWMDRM_KeyID = 'DRM_KeyID'
g_wszWMDRM_ContentID = 'DRM_ContentID'
g_wszWMDRM_SourceID = 'DRM_SourceID'
g_wszWMDRM_IndividualizedVersion = 'DRM_IndividualizedVersion'
g_wszWMDRM_LicenseAcqURL = 'DRM_LicenseAcqURL'
g_wszWMDRM_V1LicenseAcqURL = 'DRM_V1LicenseAcqURL'
g_wszWMDRM_HeaderSignPrivKey = 'DRM_HeaderSignPrivKey'
g_wszWMDRM_LASignaturePrivKey = 'DRM_LASignaturePrivKey'
g_wszWMDRM_LASignatureCert = 'DRM_LASignatureCert'
g_wszWMDRM_LASignatureLicSrvCert = 'DRM_LASignatureLicSrvCert'
g_wszWMDRM_LASignatureRootCert = 'DRM_LASignatureRootCert'
g_wszWMAlbumTitle = 'WM/AlbumTitle'
g_wszWMAlbumTitleSort = 'WM/AlbumTitleSort'
g_wszWMTrack = 'WM/Track'
g_wszWMPromotionURL = 'WM/PromotionURL'
g_wszWMAlbumCoverURL = 'WM/AlbumCoverURL'
g_wszWMGenre = 'WM/Genre'
g_wszWMYear = 'WM/Year'
g_wszWMGenreID = 'WM/GenreID'
g_wszWMMCDI = 'WM/MCDI'
g_wszWMComposer = 'WM/Composer'
g_wszWMComposerSort = 'WM/ComposerSort'
g_wszWMLyrics = 'WM/Lyrics'
g_wszWMTrackNumber = 'WM/TrackNumber'
g_wszWMToolName = 'WM/ToolName'
g_wszWMToolVersion = 'WM/ToolVersion'
g_wszWMIsVBR = 'IsVBR'
g_wszWMAlbumArtist = 'WM/AlbumArtist'
g_wszWMAlbumArtistSort = 'WM/AlbumArtistSort'
g_wszWMBannerImageType = 'BannerImageType'
g_wszWMBannerImageData = 'BannerImageData'
g_wszWMBannerImageURL = 'BannerImageURL'
g_wszWMCopyrightURL = 'CopyrightURL'
g_wszWMAspectRatioX = 'AspectRatioX'
g_wszWMAspectRatioY = 'AspectRatioY'
g_wszASFLeakyBucketPairs = 'ASFLeakyBucketPairs'
g_dwWMNSCAttributes = 5
g_wszWMNSCName = 'NSC_Name'
g_wszWMNSCAddress = 'NSC_Address'
g_wszWMNSCPhone = 'NSC_Phone'
g_wszWMNSCEmail = 'NSC_Email'
g_wszWMNSCDescription = 'NSC_Description'
g_wszWMWriter = 'WM/Writer'
g_wszWMConductor = 'WM/Conductor'
g_wszWMProducer = 'WM/Producer'
g_wszWMDirector = 'WM/Director'
g_wszWMContentGroupDescription = 'WM/ContentGroupDescription'
g_wszWMSubTitle = 'WM/SubTitle'
g_wszWMPartOfSet = 'WM/PartOfSet'
g_wszWMProtectionType = 'WM/ProtectionType'
g_wszWMVideoHeight = 'WM/VideoHeight'
g_wszWMVideoWidth = 'WM/VideoWidth'
g_wszWMVideoFrameRate = 'WM/VideoFrameRate'
g_wszWMMediaClassPrimaryID = 'WM/MediaClassPrimaryID'
g_wszWMMediaClassSecondaryID = 'WM/MediaClassSecondaryID'
g_wszWMPeriod = 'WM/Period'
g_wszWMCategory = 'WM/Category'
g_wszWMPicture = 'WM/Picture'
g_wszWMLyrics_Synchronised = 'WM/Lyrics_Synchronised'
g_wszWMOriginalLyricist = 'WM/OriginalLyricist'
g_wszWMOriginalArtist = 'WM/OriginalArtist'
g_wszWMOriginalAlbumTitle = 'WM/OriginalAlbumTitle'
g_wszWMOriginalReleaseYear = 'WM/OriginalReleaseYear'
g_wszWMOriginalFilename = 'WM/OriginalFilename'
g_wszWMPublisher = 'WM/Publisher'
g_wszWMEncodedBy = 'WM/EncodedBy'
g_wszWMEncodingSettings = 'WM/EncodingSettings'
g_wszWMEncodingTime = 'WM/EncodingTime'
g_wszWMAuthorURL = 'WM/AuthorURL'
g_wszWMUserWebURL = 'WM/UserWebURL'
g_wszWMAudioFileURL = 'WM/AudioFileURL'
g_wszWMAudioSourceURL = 'WM/AudioSourceURL'
g_wszWMLanguage = 'WM/Language'
g_wszWMParentalRating = 'WM/ParentalRating'
g_wszWMBeatsPerMinute = 'WM/BeatsPerMinute'
g_wszWMInitialKey = 'WM/InitialKey'
g_wszWMMood = 'WM/Mood'
g_wszWMText = 'WM/Text'
g_wszWMDVDID = 'WM/DVDID'
g_wszWMWMContentID = 'WM/WMContentID'
g_wszWMWMCollectionID = 'WM/WMCollectionID'
g_wszWMWMCollectionGroupID = 'WM/WMCollectionGroupID'
g_wszWMUniqueFileIdentifier = 'WM/UniqueFileIdentifier'
g_wszWMModifiedBy = 'WM/ModifiedBy'
g_wszWMRadioStationName = 'WM/RadioStationName'
g_wszWMRadioStationOwner = 'WM/RadioStationOwner'
g_wszWMPlaylistDelay = 'WM/PlaylistDelay'
g_wszWMCodec = 'WM/Codec'
g_wszWMDRM = 'WM/DRM'
g_wszWMISRC = 'WM/ISRC'
g_wszWMProvider = 'WM/Provider'
g_wszWMProviderRating = 'WM/ProviderRating'
g_wszWMProviderStyle = 'WM/ProviderStyle'
g_wszWMContentDistributor = 'WM/ContentDistributor'
g_wszWMSubscriptionContentID = 'WM/SubscriptionContentID'
g_wszWMWMADRCPeakReference = 'WM/WMADRCPeakReference'
g_wszWMWMADRCPeakTarget = 'WM/WMADRCPeakTarget'
g_wszWMWMADRCAverageReference = 'WM/WMADRCAverageReference'
g_wszWMWMADRCAverageTarget = 'WM/WMADRCAverageTarget'
g_wszWMStreamTypeInfo = 'WM/StreamTypeInfo'
g_wszWMPeakBitrate = 'WM/PeakBitrate'
g_wszWMASFPacketCount = 'WM/ASFPacketCount'
g_wszWMASFSecurityObjectsSize = 'WM/ASFSecurityObjectsSize'
g_wszWMSharedUserRating = 'WM/SharedUserRating'
g_wszWMSubTitleDescription = 'WM/SubTitleDescription'
g_wszWMMediaCredits = 'WM/MediaCredits'
g_wszWMParentalRatingReason = 'WM/ParentalRatingReason'
g_wszWMOriginalReleaseTime = 'WM/OriginalReleaseTime'
g_wszWMMediaStationCallSign = 'WM/MediaStationCallSign'
g_wszWMMediaStationName = 'WM/MediaStationName'
g_wszWMMediaNetworkAffiliation = 'WM/MediaNetworkAffiliation'
g_wszWMMediaOriginalChannel = 'WM/MediaOriginalChannel'
g_wszWMMediaOriginalBroadcastDateTime = 'WM/MediaOriginalBroadcastDateTime'
g_wszWMMediaIsStereo = 'WM/MediaIsStereo'
g_wszWMVideoClosedCaptioning = 'WM/VideoClosedCaptioning'
g_wszWMMediaIsRepeat = 'WM/MediaIsRepeat'
g_wszWMMediaIsLive = 'WM/MediaIsLive'
g_wszWMMediaIsTape = 'WM/MediaIsTape'
g_wszWMMediaIsDelay = 'WM/MediaIsDelay'
g_wszWMMediaIsSubtitled = 'WM/MediaIsSubtitled'
g_wszWMMediaIsPremiere = 'WM/MediaIsPremiere'
g_wszWMMediaIsFinale = 'WM/MediaIsFinale'
g_wszWMMediaIsSAP = 'WM/MediaIsSAP'
g_wszWMProviderCopyright = 'WM/ProviderCopyright'
g_wszWMISAN = 'WM/ISAN'
g_wszWMADID = 'WM/ADID'
g_wszWMWMShadowFileSourceFileType = 'WM/WMShadowFileSourceFileType'
g_wszWMWMShadowFileSourceDRMType = 'WM/WMShadowFileSourceDRMType'
g_wszWMWMCPDistributor = 'WM/WMCPDistributor'
g_wszWMWMCPDistributorID = 'WM/WMCPDistributorID'
g_wszWMSeasonNumber = 'WM/SeasonNumber'
g_wszWMEpisodeNumber = 'WM/EpisodeNumber'
g_wszEarlyDataDelivery = 'EarlyDataDelivery'
g_wszJustInTimeDecode = 'JustInTimeDecode'
g_wszSingleOutputBuffer = 'SingleOutputBuffer'
g_wszSoftwareScaling = 'SoftwareScaling'
g_wszDeliverOnReceive = 'DeliverOnReceive'
g_wszScrambledAudio = 'ScrambledAudio'
g_wszDedicatedDeliveryThread = 'DedicatedDeliveryThread'
g_wszEnableDiscreteOutput = 'EnableDiscreteOutput'
g_wszSpeakerConfig = 'SpeakerConfig'
g_wszDynamicRangeControl = 'DynamicRangeControl'
g_wszAllowInterlacedOutput = 'AllowInterlacedOutput'
g_wszVideoSampleDurations = 'VideoSampleDurations'
g_wszStreamLanguage = 'StreamLanguage'
g_wszEnableWMAProSPDIFOutput = 'EnableWMAProSPDIFOutput'
g_wszDeinterlaceMode = 'DeinterlaceMode'
g_wszInitialPatternForInverseTelecine = 'InitialPatternForInverseTelecine'
g_wszJPEGCompressionQuality = 'JPEGCompressionQuality'
g_wszWatermarkCLSID = 'WatermarkCLSID'
g_wszWatermarkConfig = 'WatermarkConfig'
g_wszInterlacedCoding = 'InterlacedCoding'
g_wszFixedFrameRate = 'FixedFrameRate'
g_wszOriginalSourceFormatTag = '_SOURCEFORMATTAG'
g_wszOriginalWaveFormat = '_ORIGINALWAVEFORMAT'
g_wszEDL = '_EDL'
g_wszComplexity = '_COMPLEXITYEX'
g_wszDecoderComplexityRequested = '_DECODERCOMPLEXITYPROFILE'
g_wszReloadIndexOnSeek = 'ReloadIndexOnSeek'
g_wszStreamNumIndexObjects = 'StreamNumIndexObjects'
g_wszFailSeekOnError = 'FailSeekOnError'
g_wszPermitSeeksBeyondEndOfStream = 'PermitSeeksBeyondEndOfStream'
g_wszUsePacketAtSeekPoint = 'UsePacketAtSeekPoint'
g_wszSourceBufferTime = 'SourceBufferTime'
g_wszSourceMaxBytesAtOnce = 'SourceMaxBytesAtOnce'
g_wszVBREnabled = '_VBRENABLED'
g_wszVBRQuality = '_VBRQUALITY'
g_wszVBRBitrateMax = '_RMAX'
g_wszVBRBufferWindowMax = '_BMAX'
g_wszVBRPeak = 'VBR Peak'
g_wszBufferAverage = 'Buffer Average'
g_wszComplexityMax = '_COMPLEXITYEXMAX'
g_wszComplexityOffline = '_COMPLEXITYEXOFFLINE'
g_wszComplexityLive = '_COMPLEXITYEXLIVE'
g_wszIsVBRSupported = '_ISVBRSUPPORTED'
g_wszNumPasses = '_PASSESUSED'
g_wszMusicSpeechClassMode = 'MusicSpeechClassMode'
g_wszMusicClassMode = 'MusicClassMode'
g_wszSpeechClassMode = 'SpeechClassMode'
g_wszMixedClassMode = 'MixedClassMode'
g_wszSpeechCaps = 'SpeechFormatCap'
g_wszPeakValue = 'PeakValue'
g_wszAverageLevel = 'AverageLevel'
g_wszFold6To2Channels3 = 'Fold6To2Channels3'
g_wszFoldToChannelsTemplate = 'Fold%luTo%luChannels%lu'
g_wszDeviceConformanceTemplate = 'DeviceConformanceTemplate'
g_wszEnableFrameInterpolation = 'EnableFrameInterpolation'
g_wszNeedsPreviousSample = 'NeedsPreviousSample'
g_wszWMIsCompilation = 'WM/IsCompilation'
WMMEDIASUBTYPE_Base = '00000000-0000-0010-8000-00aa00389b71'
WMMEDIATYPE_Video = '73646976-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_RGB1 = 'e436eb78-524f-11ce-9f53-0020af0ba770'
WMMEDIASUBTYPE_RGB4 = 'e436eb79-524f-11ce-9f53-0020af0ba770'
WMMEDIASUBTYPE_RGB8 = 'e436eb7a-524f-11ce-9f53-0020af0ba770'
WMMEDIASUBTYPE_RGB565 = 'e436eb7b-524f-11ce-9f53-0020af0ba770'
WMMEDIASUBTYPE_RGB555 = 'e436eb7c-524f-11ce-9f53-0020af0ba770'
WMMEDIASUBTYPE_RGB24 = 'e436eb7d-524f-11ce-9f53-0020af0ba770'
WMMEDIASUBTYPE_RGB32 = 'e436eb7e-524f-11ce-9f53-0020af0ba770'
WMMEDIASUBTYPE_I420 = '30323449-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_IYUV = '56555949-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_YV12 = '32315659-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_YUY2 = '32595559-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_P422 = '32323450-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_UYVY = '59565955-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_YVYU = '55595659-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_YVU9 = '39555659-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_VIDEOIMAGE = '1d4a45f2-e5f6-4b44-8388-f0ae5c0e0c37'
WMMEDIASUBTYPE_MP43 = '3334504d-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_MP4S = '5334504d-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_M4S2 = '3253344d-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMV1 = '31564d57-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMV2 = '32564d57-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_MSS1 = '3153534d-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_MPEG2_VIDEO = 'e06d8026-db46-11cf-b4d1-00805f6cbbea'
WMMEDIATYPE_Audio = '73647561-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_PCM = '00000001-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_DRM = '00000009-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMAudioV9 = '00000162-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMAudio_Lossless = '00000163-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_MSS2 = '3253534d-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMSP1 = '0000000a-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMSP2 = '0000000b-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMV3 = '33564d57-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMVP = '50564d57-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WVP2 = '32505657-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMVA = '41564d57-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WVC1 = '31435657-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMAudioV8 = '00000161-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMAudioV7 = '00000161-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WMAudioV2 = '00000161-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_ACELPnet = '00000130-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_MP3 = '00000055-0000-0010-8000-00aa00389b71'
WMMEDIASUBTYPE_WebStream = '776257d4-c627-41cb-8f81-7ac7ff1c40cc'
WMMEDIATYPE_Script = '73636d64-0000-0010-8000-00aa00389b71'
WMMEDIATYPE_Image = '34a50fd8-8aa5-4386-81fe-a0efe0488e31'
WMMEDIATYPE_FileTransfer = 'd9e47579-930e-4427-adfc-ad80f290e470'
WMMEDIATYPE_Text = '9bba1ea7-5ab2-4829-ba57-0940209bcf3e'
WMFORMAT_VideoInfo = '05589f80-c356-11ce-bf01-00aa0055595a'
WMFORMAT_MPEG2Video = 'e06d80e3-db46-11cf-b4d1-00805f6cbbea'
WMFORMAT_WaveFormatEx = '05589f81-c356-11ce-bf01-00aa0055595a'
WMFORMAT_Script = '5c8510f2-debe-4ca7-bba5-f07a104f8dff'
WMFORMAT_WebStream = 'da1e6b13-8359-4050-b398-388e965bf00c'
WMSCRIPTTYPE_TwoStrings = '82f38a70-c29f-11d1-97ad-00a0c95ea850'
WM_SampleExtensionGUID_OutputCleanPoint = 'f72a3c6f-6eb4-4ebc-b192-09ad9759e828'
WM_SampleExtensionGUID_Timecode = '399595ec-8667-4e2d-8fdb-98814ce76c1e'
WM_SampleExtensionGUID_ChromaLocation = '4c5acca0-9276-4b2c-9e4c-a0edefdd217e'
WM_SampleExtensionGUID_ColorSpaceInfo = 'f79ada56-30eb-4f2b-9f7a-f24b139a1157'
WM_SampleExtensionGUID_UserDataInfo = '732bb4fa-78be-4549-99bd-02db1a55b7a8'
WM_SampleExtensionGUID_FileName = 'e165ec0e-19ed-45d7-b4a7-25cbd1e28e9b'
WM_SampleExtensionGUID_ContentType = 'd590dc20-07bc-436c-9cf7-f3bbfbf1a4dc'
WM_SampleExtensionGUID_PixelAspectRatio = '1b1ee554-f9ea-4bc8-821a-376b74e4c4b8'
WM_SampleExtensionGUID_SampleDuration = 'c6bd9450-867f-4907-83a3-c77921b733ad'
WM_SampleExtensionGUID_SampleProtectionSalt = '5403deee-b9ee-438f-aa83-3804997e569d'
CLSID_WMMUTEX_Language = 'd6e22a00-35da-11d1-9034-00a0c90349be'
CLSID_WMMUTEX_Bitrate = 'd6e22a01-35da-11d1-9034-00a0c90349be'
CLSID_WMMUTEX_Presentation = 'd6e22a02-35da-11d1-9034-00a0c90349be'
CLSID_WMMUTEX_Unknown = 'd6e22a03-35da-11d1-9034-00a0c90349be'
CLSID_WMBandwidthSharing_Exclusive = 'af6060aa-5197-11d2-b6af-00c04fd908e9'
CLSID_WMBandwidthSharing_Partial = 'af6060ab-5197-11d2-b6af-00c04fd908e9'
WMT_DMOCATEGORY_AUDIO_WATERMARK = '65221c5a-fa75-4b39-b50c-06c336b6a3ef'
WMT_DMOCATEGORY_VIDEO_WATERMARK = '187cc922-8efc-4404-9daf-63f4830df1bc'
CLSID_ClientNetManager = 'cd12a3ce-9c42-11d2-beed-0060082f2054'
def _define_IAMWMBufferPass_head():
    class IAMWMBufferPass(win32more.System.Com.IUnknown_head):
        Guid = Guid('6dd816d7-e740-4123-9e24-2444412644d8')
    return IAMWMBufferPass
def _define_IAMWMBufferPass():
    IAMWMBufferPass = win32more.Media.WindowsMediaFormat.IAMWMBufferPass_head
    IAMWMBufferPass.SetNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IAMWMBufferPassCallback_head, use_last_error=False)(3, 'SetNotify', ((1, 'pCallback'),)))
    return IAMWMBufferPass
def _define_IAMWMBufferPassCallback_head():
    class IAMWMBufferPassCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('b25b8372-d2d2-44b2-8653-1b8dae332489')
    return IAMWMBufferPassCallback
def _define_IAMWMBufferPassCallback():
    IAMWMBufferPassCallback = win32more.Media.WindowsMediaFormat.IAMWMBufferPassCallback_head
    IAMWMBufferPassCallback.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.INSSBuffer3_head,win32more.Media.DirectShow.IPin_head,POINTER(Int64),POINTER(Int64), use_last_error=False)(3, 'Notify', ((1, 'pNSSBuffer3'),(1, 'pPin'),(1, 'prtStart'),(1, 'prtEnd'),)))
    return IAMWMBufferPassCallback
_AM_ASFWRITERCONFIG_PARAM = Int32
AM_CONFIGASFWRITER_PARAM_AUTOINDEX = 1
AM_CONFIGASFWRITER_PARAM_MULTIPASS = 2
AM_CONFIGASFWRITER_PARAM_DONTCOMPRESS = 3
def _define_AM_WMT_EVENT_DATA_head():
    class AM_WMT_EVENT_DATA(Structure):
        pass
    return AM_WMT_EVENT_DATA
def _define_AM_WMT_EVENT_DATA():
    AM_WMT_EVENT_DATA = win32more.Media.WindowsMediaFormat.AM_WMT_EVENT_DATA_head
    AM_WMT_EVENT_DATA._fields_ = [
        ("hrStatus", win32more.Foundation.HRESULT),
        ("pData", c_void_p),
    ]
    return AM_WMT_EVENT_DATA
def _define_INSSBuffer_head():
    class INSSBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('e1cd3524-03d7-11d2-9eed-006097d2d7cf')
    return INSSBuffer
def _define_INSSBuffer():
    INSSBuffer = win32more.Media.WindowsMediaFormat.INSSBuffer_head
    INSSBuffer.GetLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetLength', ((1, 'pdwLength'),)))
    INSSBuffer.SetLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetLength', ((1, 'dwLength'),)))
    INSSBuffer.GetMaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetMaxLength', ((1, 'pdwLength'),)))
    INSSBuffer.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no), use_last_error=False)(6, 'GetBuffer', ((1, 'ppdwBuffer'),)))
    INSSBuffer.GetBufferAndLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(7, 'GetBufferAndLength', ((1, 'ppdwBuffer'),(1, 'pdwLength'),)))
    return INSSBuffer
def _define_INSSBuffer2_head():
    class INSSBuffer2(win32more.Media.WindowsMediaFormat.INSSBuffer_head):
        Guid = Guid('4f528693-1035-43fe-b428-757561ad3a68')
    return INSSBuffer2
def _define_INSSBuffer2():
    INSSBuffer2 = win32more.Media.WindowsMediaFormat.INSSBuffer2_head
    INSSBuffer2.GetSampleProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no, use_last_error=False)(8, 'GetSampleProperties', ((1, 'cbProperties'),(1, 'pbProperties'),)))
    INSSBuffer2.SetSampleProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no, use_last_error=False)(9, 'SetSampleProperties', ((1, 'cbProperties'),(1, 'pbProperties'),)))
    return INSSBuffer2
def _define_INSSBuffer3_head():
    class INSSBuffer3(win32more.Media.WindowsMediaFormat.INSSBuffer2_head):
        Guid = Guid('c87ceaaf-75be-4bc4-84eb-ac2798507672')
    return INSSBuffer3
def _define_INSSBuffer3():
    INSSBuffer3 = win32more.Media.WindowsMediaFormat.INSSBuffer3_head
    INSSBuffer3.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,c_void_p,UInt32, use_last_error=False)(10, 'SetProperty', ((1, 'guidBufferProperty'),(1, 'pvBufferProperty'),(1, 'dwBufferPropertySize'),)))
    INSSBuffer3.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,c_void_p,POINTER(UInt32), use_last_error=False)(11, 'GetProperty', ((1, 'guidBufferProperty'),(1, 'pvBufferProperty'),(1, 'pdwBufferPropertySize'),)))
    return INSSBuffer3
def _define_INSSBuffer4_head():
    class INSSBuffer4(win32more.Media.WindowsMediaFormat.INSSBuffer3_head):
        Guid = Guid('b6b8fd5a-32e2-49d4-a910-c26cc85465ed')
    return INSSBuffer4
def _define_INSSBuffer4():
    INSSBuffer4 = win32more.Media.WindowsMediaFormat.INSSBuffer4_head
    INSSBuffer4.GetPropertyCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetPropertyCount', ((1, 'pcBufferProperties'),)))
    INSSBuffer4.GetPropertyByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),c_void_p,POINTER(UInt32), use_last_error=False)(13, 'GetPropertyByIndex', ((1, 'dwBufferPropertyIndex'),(1, 'pguidBufferProperty'),(1, 'pvBufferProperty'),(1, 'pdwBufferPropertySize'),)))
    return INSSBuffer4
def _define_IWMSBufferAllocator_head():
    class IWMSBufferAllocator(win32more.System.Com.IUnknown_head):
        Guid = Guid('61103ca4-2033-11d2-9ef1-006097d2d7cf')
    return IWMSBufferAllocator
def _define_IWMSBufferAllocator():
    IWMSBufferAllocator = win32more.Media.WindowsMediaFormat.IWMSBufferAllocator_head
    IWMSBufferAllocator.AllocateBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head), use_last_error=False)(3, 'AllocateBuffer', ((1, 'dwMaxBufferSize'),(1, 'ppBuffer'),)))
    IWMSBufferAllocator.AllocatePageSizeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head), use_last_error=False)(4, 'AllocatePageSizeBuffer', ((1, 'dwMaxBufferSize'),(1, 'ppBuffer'),)))
    return IWMSBufferAllocator
WEBSTREAM_SAMPLE_TYPE = Int32
WEBSTREAM_SAMPLE_TYPE_FILE = 1
WEBSTREAM_SAMPLE_TYPE_RENDER = 2
WM_SF_TYPE = Int32
WM_SF_CLEANPOINT = 1
WM_SF_DISCONTINUITY = 2
WM_SF_DATALOSS = 4
WM_SFEX_TYPE = Int32
WM_SFEX_NOTASYNCPOINT = 2
WM_SFEX_DATALOSS = 4
WMT_STATUS = Int32
WMT_ERROR = 0
WMT_OPENED = 1
WMT_BUFFERING_START = 2
WMT_BUFFERING_STOP = 3
WMT_EOF = 4
WMT_END_OF_FILE = 4
WMT_END_OF_SEGMENT = 5
WMT_END_OF_STREAMING = 6
WMT_LOCATING = 7
WMT_CONNECTING = 8
WMT_NO_RIGHTS = 9
WMT_MISSING_CODEC = 10
WMT_STARTED = 11
WMT_STOPPED = 12
WMT_CLOSED = 13
WMT_STRIDING = 14
WMT_TIMER = 15
WMT_INDEX_PROGRESS = 16
WMT_SAVEAS_START = 17
WMT_SAVEAS_STOP = 18
WMT_NEW_SOURCEFLAGS = 19
WMT_NEW_METADATA = 20
WMT_BACKUPRESTORE_BEGIN = 21
WMT_SOURCE_SWITCH = 22
WMT_ACQUIRE_LICENSE = 23
WMT_INDIVIDUALIZE = 24
WMT_NEEDS_INDIVIDUALIZATION = 25
WMT_NO_RIGHTS_EX = 26
WMT_BACKUPRESTORE_END = 27
WMT_BACKUPRESTORE_CONNECTING = 28
WMT_BACKUPRESTORE_DISCONNECTING = 29
WMT_ERROR_WITHURL = 30
WMT_RESTRICTED_LICENSE = 31
WMT_CLIENT_CONNECT = 32
WMT_CLIENT_DISCONNECT = 33
WMT_NATIVE_OUTPUT_PROPS_CHANGED = 34
WMT_RECONNECT_START = 35
WMT_RECONNECT_END = 36
WMT_CLIENT_CONNECT_EX = 37
WMT_CLIENT_DISCONNECT_EX = 38
WMT_SET_FEC_SPAN = 39
WMT_PREROLL_READY = 40
WMT_PREROLL_COMPLETE = 41
WMT_CLIENT_PROPERTIES = 42
WMT_LICENSEURL_SIGNATURE_STATE = 43
WMT_INIT_PLAYLIST_BURN = 44
WMT_TRANSCRYPTOR_INIT = 45
WMT_TRANSCRYPTOR_SEEKED = 46
WMT_TRANSCRYPTOR_READ = 47
WMT_TRANSCRYPTOR_CLOSED = 48
WMT_PROXIMITY_RESULT = 49
WMT_PROXIMITY_COMPLETED = 50
WMT_CONTENT_ENABLER = 51
WMT_STREAM_SELECTION = Int32
WMT_OFF = 0
WMT_CLEANPOINT_ONLY = 1
WMT_ON = 2
WMT_IMAGE_TYPE = Int32
WMT_IT_NONE = 0
WMT_IT_BITMAP = 1
WMT_IT_JPEG = 2
WMT_IT_GIF = 3
WMT_ATTR_DATATYPE = Int32
WMT_TYPE_DWORD = 0
WMT_TYPE_STRING = 1
WMT_TYPE_BINARY = 2
WMT_TYPE_BOOL = 3
WMT_TYPE_QWORD = 4
WMT_TYPE_WORD = 5
WMT_TYPE_GUID = 6
WMT_ATTR_IMAGETYPE = Int32
WMT_IMAGETYPE_BITMAP = 1
WMT_IMAGETYPE_JPEG = 2
WMT_IMAGETYPE_GIF = 3
WMT_VERSION = Int32
WMT_VER_4_0 = 262144
WMT_VER_7_0 = 458752
WMT_VER_8_0 = 524288
WMT_VER_9_0 = 589824
WMT_STORAGE_FORMAT = Int32
WMT_Storage_Format_MP3 = 0
WMT_Storage_Format_V1 = 1
WMT_DRMLA_TRUST = Int32
WMT_DRMLA_UNTRUSTED = 0
WMT_DRMLA_TRUSTED = 1
WMT_DRMLA_TAMPERED = 2
WMT_TRANSPORT_TYPE = Int32
WMT_Transport_Type_Unreliable = 0
WMT_Transport_Type_Reliable = 1
WMT_NET_PROTOCOL = Int32
WMT_PROTOCOL_HTTP = 0
WMT_PLAY_MODE = Int32
WMT_PLAY_MODE_AUTOSELECT = 0
WMT_PLAY_MODE_LOCAL = 1
WMT_PLAY_MODE_DOWNLOAD = 2
WMT_PLAY_MODE_STREAMING = 3
WMT_PROXY_SETTINGS = Int32
WMT_PROXY_SETTING_NONE = 0
WMT_PROXY_SETTING_MANUAL = 1
WMT_PROXY_SETTING_AUTO = 2
WMT_PROXY_SETTING_BROWSER = 3
WMT_PROXY_SETTING_MAX = 4
WMT_CODEC_INFO_TYPE = Int32
WMT_CODECINFO_AUDIO = 0
WMT_CODECINFO_VIDEO = 1
WMT_CODECINFO_UNKNOWN = -1
WM_DM_INTERLACED_TYPE = Int32
WM_DM_NOTINTERLACED = 0
WM_DM_DEINTERLACE_NORMAL = 1
WM_DM_DEINTERLACE_HALFSIZE = 2
WM_DM_DEINTERLACE_HALFSIZEDOUBLERATE = 3
WM_DM_DEINTERLACE_INVERSETELECINE = 4
WM_DM_DEINTERLACE_VERTICALHALFSIZEDOUBLERATE = 5
WM_DM_IT_FIRST_FRAME_COHERENCY = Int32
WM_DM_IT_DISABLE_COHERENT_MODE = 0
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_TOP = 1
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_TOP = 2
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_TOP = 3
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_TOP = 4
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_TOP = 5
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_BOTTOM = 6
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_BOTTOM = 7
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_BOTTOM = 8
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_BOTTOM = 9
WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_BOTTOM = 10
WMT_OFFSET_FORMAT = Int32
WMT_OFFSET_FORMAT_100NS = 0
WMT_OFFSET_FORMAT_FRAME_NUMBERS = 1
WMT_OFFSET_FORMAT_PLAYLIST_OFFSET = 2
WMT_OFFSET_FORMAT_TIMECODE = 3
WMT_OFFSET_FORMAT_100NS_APPROXIMATE = 4
WMT_INDEXER_TYPE = Int32
WMT_IT_PRESENTATION_TIME = 0
WMT_IT_FRAME_NUMBERS = 1
WMT_IT_TIMECODE = 2
WMT_INDEX_TYPE = Int32
WMT_IT_NEAREST_DATA_UNIT = 1
WMT_IT_NEAREST_OBJECT = 2
WMT_IT_NEAREST_CLEAN_POINT = 3
WMT_FILESINK_MODE = Int32
WMT_FM_SINGLE_BUFFERS = 1
WMT_FM_FILESINK_DATA_UNITS = 2
WMT_FM_FILESINK_UNBUFFERED = 4
WMT_MUSICSPEECH_CLASS_MODE = Int32
WMT_MS_CLASS_MUSIC = 0
WMT_MS_CLASS_SPEECH = 1
WMT_MS_CLASS_MIXED = 2
WMT_WATERMARK_ENTRY_TYPE = Int32
WMT_WMETYPE_AUDIO = 1
WMT_WMETYPE_VIDEO = 2
WM_PLAYBACK_DRC_LEVEL = Int32
WM_PLAYBACK_DRC_HIGH = 0
WM_PLAYBACK_DRC_MEDIUM = 1
WM_PLAYBACK_DRC_LOW = 2
WMT_TIMECODE_FRAMERATE = Int32
WMT_TIMECODE_FRAMERATE_30 = 0
WMT_TIMECODE_FRAMERATE_30DROP = 1
WMT_TIMECODE_FRAMERATE_25 = 2
WMT_TIMECODE_FRAMERATE_24 = 3
WMT_CREDENTIAL_FLAGS = Int32
WMT_CREDENTIAL_SAVE = 1
WMT_CREDENTIAL_DONT_CACHE = 2
WMT_CREDENTIAL_CLEAR_TEXT = 4
WMT_CREDENTIAL_PROXY = 8
WMT_CREDENTIAL_ENCRYPT = 16
WM_AETYPE = Int32
WM_AETYPE_INCLUDE = 105
WM_AETYPE_EXCLUDE = 101
WMT_RIGHTS = Int32
WMT_RIGHT_PLAYBACK = 1
WMT_RIGHT_COPY_TO_NON_SDMI_DEVICE = 2
WMT_RIGHT_COPY_TO_CD = 8
WMT_RIGHT_COPY_TO_SDMI_DEVICE = 16
WMT_RIGHT_ONE_TIME = 32
WMT_RIGHT_SAVE_STREAM_PROTECTED = 64
WMT_RIGHT_COPY = 128
WMT_RIGHT_COLLABORATIVE_PLAY = 256
WMT_RIGHT_SDMI_TRIGGER = 65536
WMT_RIGHT_SDMI_NOMORECOPIES = 131072
def _define_WM_STREAM_PRIORITY_RECORD_head():
    class WM_STREAM_PRIORITY_RECORD(Structure):
        pass
    return WM_STREAM_PRIORITY_RECORD
def _define_WM_STREAM_PRIORITY_RECORD():
    WM_STREAM_PRIORITY_RECORD = win32more.Media.WindowsMediaFormat.WM_STREAM_PRIORITY_RECORD_head
    WM_STREAM_PRIORITY_RECORD._pack_ = 2
    WM_STREAM_PRIORITY_RECORD._fields_ = [
        ("wStreamNumber", UInt16),
        ("fMandatory", win32more.Foundation.BOOL),
    ]
    return WM_STREAM_PRIORITY_RECORD
def _define_WM_WRITER_STATISTICS_head():
    class WM_WRITER_STATISTICS(Structure):
        pass
    return WM_WRITER_STATISTICS
def _define_WM_WRITER_STATISTICS():
    WM_WRITER_STATISTICS = win32more.Media.WindowsMediaFormat.WM_WRITER_STATISTICS_head
    WM_WRITER_STATISTICS._fields_ = [
        ("qwSampleCount", UInt64),
        ("qwByteCount", UInt64),
        ("qwDroppedSampleCount", UInt64),
        ("qwDroppedByteCount", UInt64),
        ("dwCurrentBitrate", UInt32),
        ("dwAverageBitrate", UInt32),
        ("dwExpectedBitrate", UInt32),
        ("dwCurrentSampleRate", UInt32),
        ("dwAverageSampleRate", UInt32),
        ("dwExpectedSampleRate", UInt32),
    ]
    return WM_WRITER_STATISTICS
def _define_WM_WRITER_STATISTICS_EX_head():
    class WM_WRITER_STATISTICS_EX(Structure):
        pass
    return WM_WRITER_STATISTICS_EX
def _define_WM_WRITER_STATISTICS_EX():
    WM_WRITER_STATISTICS_EX = win32more.Media.WindowsMediaFormat.WM_WRITER_STATISTICS_EX_head
    WM_WRITER_STATISTICS_EX._fields_ = [
        ("dwBitratePlusOverhead", UInt32),
        ("dwCurrentSampleDropRateInQueue", UInt32),
        ("dwCurrentSampleDropRateInCodec", UInt32),
        ("dwCurrentSampleDropRateInMultiplexer", UInt32),
        ("dwTotalSampleDropsInQueue", UInt32),
        ("dwTotalSampleDropsInCodec", UInt32),
        ("dwTotalSampleDropsInMultiplexer", UInt32),
    ]
    return WM_WRITER_STATISTICS_EX
def _define_WM_READER_STATISTICS_head():
    class WM_READER_STATISTICS(Structure):
        pass
    return WM_READER_STATISTICS
def _define_WM_READER_STATISTICS():
    WM_READER_STATISTICS = win32more.Media.WindowsMediaFormat.WM_READER_STATISTICS_head
    WM_READER_STATISTICS._fields_ = [
        ("cbSize", UInt32),
        ("dwBandwidth", UInt32),
        ("cPacketsReceived", UInt32),
        ("cPacketsRecovered", UInt32),
        ("cPacketsLost", UInt32),
        ("wQuality", UInt16),
    ]
    return WM_READER_STATISTICS
def _define_WM_READER_CLIENTINFO_head():
    class WM_READER_CLIENTINFO(Structure):
        pass
    return WM_READER_CLIENTINFO
def _define_WM_READER_CLIENTINFO():
    WM_READER_CLIENTINFO = win32more.Media.WindowsMediaFormat.WM_READER_CLIENTINFO_head
    WM_READER_CLIENTINFO._fields_ = [
        ("cbSize", UInt32),
        ("wszLang", win32more.Foundation.PWSTR),
        ("wszBrowserUserAgent", win32more.Foundation.PWSTR),
        ("wszBrowserWebPage", win32more.Foundation.PWSTR),
        ("qwReserved", UInt64),
        ("pReserved", POINTER(win32more.Foundation.LPARAM)),
        ("wszHostExe", win32more.Foundation.PWSTR),
        ("qwHostVersion", UInt64),
        ("wszPlayerUserAgent", win32more.Foundation.PWSTR),
    ]
    return WM_READER_CLIENTINFO
def _define_WM_CLIENT_PROPERTIES_head():
    class WM_CLIENT_PROPERTIES(Structure):
        pass
    return WM_CLIENT_PROPERTIES
def _define_WM_CLIENT_PROPERTIES():
    WM_CLIENT_PROPERTIES = win32more.Media.WindowsMediaFormat.WM_CLIENT_PROPERTIES_head
    WM_CLIENT_PROPERTIES._fields_ = [
        ("dwIPAddress", UInt32),
        ("dwPort", UInt32),
    ]
    return WM_CLIENT_PROPERTIES
def _define_WM_CLIENT_PROPERTIES_EX_head():
    class WM_CLIENT_PROPERTIES_EX(Structure):
        pass
    return WM_CLIENT_PROPERTIES_EX
def _define_WM_CLIENT_PROPERTIES_EX():
    WM_CLIENT_PROPERTIES_EX = win32more.Media.WindowsMediaFormat.WM_CLIENT_PROPERTIES_EX_head
    WM_CLIENT_PROPERTIES_EX._fields_ = [
        ("cbSize", UInt32),
        ("pwszIPAddress", win32more.Foundation.PWSTR),
        ("pwszPort", win32more.Foundation.PWSTR),
        ("pwszDNSName", win32more.Foundation.PWSTR),
    ]
    return WM_CLIENT_PROPERTIES_EX
def _define_WM_PORT_NUMBER_RANGE_head():
    class WM_PORT_NUMBER_RANGE(Structure):
        pass
    return WM_PORT_NUMBER_RANGE
def _define_WM_PORT_NUMBER_RANGE():
    WM_PORT_NUMBER_RANGE = win32more.Media.WindowsMediaFormat.WM_PORT_NUMBER_RANGE_head
    WM_PORT_NUMBER_RANGE._fields_ = [
        ("wPortBegin", UInt16),
        ("wPortEnd", UInt16),
    ]
    return WM_PORT_NUMBER_RANGE
def _define_WMT_BUFFER_SEGMENT_head():
    class WMT_BUFFER_SEGMENT(Structure):
        pass
    return WMT_BUFFER_SEGMENT
def _define_WMT_BUFFER_SEGMENT():
    WMT_BUFFER_SEGMENT = win32more.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT_head
    WMT_BUFFER_SEGMENT._fields_ = [
        ("pBuffer", win32more.Media.WindowsMediaFormat.INSSBuffer_head),
        ("cbOffset", UInt32),
        ("cbLength", UInt32),
    ]
    return WMT_BUFFER_SEGMENT
def _define_WMT_PAYLOAD_FRAGMENT_head():
    class WMT_PAYLOAD_FRAGMENT(Structure):
        pass
    return WMT_PAYLOAD_FRAGMENT
def _define_WMT_PAYLOAD_FRAGMENT():
    WMT_PAYLOAD_FRAGMENT = win32more.Media.WindowsMediaFormat.WMT_PAYLOAD_FRAGMENT_head
    WMT_PAYLOAD_FRAGMENT._fields_ = [
        ("dwPayloadIndex", UInt32),
        ("segmentData", win32more.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT),
    ]
    return WMT_PAYLOAD_FRAGMENT
def _define_WMT_FILESINK_DATA_UNIT_head():
    class WMT_FILESINK_DATA_UNIT(Structure):
        pass
    return WMT_FILESINK_DATA_UNIT
def _define_WMT_FILESINK_DATA_UNIT():
    WMT_FILESINK_DATA_UNIT = win32more.Media.WindowsMediaFormat.WMT_FILESINK_DATA_UNIT_head
    WMT_FILESINK_DATA_UNIT._fields_ = [
        ("packetHeaderBuffer", win32more.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT),
        ("cPayloads", UInt32),
        ("pPayloadHeaderBuffers", POINTER(win32more.Media.WindowsMediaFormat.WMT_BUFFER_SEGMENT_head)),
        ("cPayloadDataFragments", UInt32),
        ("pPayloadDataFragments", POINTER(win32more.Media.WindowsMediaFormat.WMT_PAYLOAD_FRAGMENT_head)),
    ]
    return WMT_FILESINK_DATA_UNIT
def _define_WMT_WEBSTREAM_FORMAT_head():
    class WMT_WEBSTREAM_FORMAT(Structure):
        pass
    return WMT_WEBSTREAM_FORMAT
def _define_WMT_WEBSTREAM_FORMAT():
    WMT_WEBSTREAM_FORMAT = win32more.Media.WindowsMediaFormat.WMT_WEBSTREAM_FORMAT_head
    WMT_WEBSTREAM_FORMAT._fields_ = [
        ("cbSize", UInt16),
        ("cbSampleHeaderFixedData", UInt16),
        ("wVersion", UInt16),
        ("wReserved", UInt16),
    ]
    return WMT_WEBSTREAM_FORMAT
def _define_WMT_WEBSTREAM_SAMPLE_HEADER_head():
    class WMT_WEBSTREAM_SAMPLE_HEADER(Structure):
        pass
    return WMT_WEBSTREAM_SAMPLE_HEADER
def _define_WMT_WEBSTREAM_SAMPLE_HEADER():
    WMT_WEBSTREAM_SAMPLE_HEADER = win32more.Media.WindowsMediaFormat.WMT_WEBSTREAM_SAMPLE_HEADER_head
    WMT_WEBSTREAM_SAMPLE_HEADER._fields_ = [
        ("cbLength", UInt16),
        ("wPart", UInt16),
        ("cTotalParts", UInt16),
        ("wSampleType", UInt16),
        ("wszURL", Char * 0),
    ]
    return WMT_WEBSTREAM_SAMPLE_HEADER
def _define_WM_ADDRESS_ACCESSENTRY_head():
    class WM_ADDRESS_ACCESSENTRY(Structure):
        pass
    return WM_ADDRESS_ACCESSENTRY
def _define_WM_ADDRESS_ACCESSENTRY():
    WM_ADDRESS_ACCESSENTRY = win32more.Media.WindowsMediaFormat.WM_ADDRESS_ACCESSENTRY_head
    WM_ADDRESS_ACCESSENTRY._fields_ = [
        ("dwIPAddress", UInt32),
        ("dwMask", UInt32),
    ]
    return WM_ADDRESS_ACCESSENTRY
def _define_WM_PICTURE_head():
    class WM_PICTURE(Structure):
        pass
    return WM_PICTURE
def _define_WM_PICTURE():
    WM_PICTURE = win32more.Media.WindowsMediaFormat.WM_PICTURE_head
    WM_PICTURE._pack_ = 1
    WM_PICTURE._fields_ = [
        ("pwszMIMEType", win32more.Foundation.PWSTR),
        ("bPictureType", Byte),
        ("pwszDescription", win32more.Foundation.PWSTR),
        ("dwDataLen", UInt32),
        ("pbData", c_char_p_no),
    ]
    return WM_PICTURE
def _define_WM_SYNCHRONISED_LYRICS_head():
    class WM_SYNCHRONISED_LYRICS(Structure):
        pass
    return WM_SYNCHRONISED_LYRICS
def _define_WM_SYNCHRONISED_LYRICS():
    WM_SYNCHRONISED_LYRICS = win32more.Media.WindowsMediaFormat.WM_SYNCHRONISED_LYRICS_head
    WM_SYNCHRONISED_LYRICS._pack_ = 1
    WM_SYNCHRONISED_LYRICS._fields_ = [
        ("bTimeStampFormat", Byte),
        ("bContentType", Byte),
        ("pwszContentDescriptor", win32more.Foundation.PWSTR),
        ("dwLyricsLen", UInt32),
        ("pbLyrics", c_char_p_no),
    ]
    return WM_SYNCHRONISED_LYRICS
def _define_WM_USER_WEB_URL_head():
    class WM_USER_WEB_URL(Structure):
        pass
    return WM_USER_WEB_URL
def _define_WM_USER_WEB_URL():
    WM_USER_WEB_URL = win32more.Media.WindowsMediaFormat.WM_USER_WEB_URL_head
    WM_USER_WEB_URL._pack_ = 1
    WM_USER_WEB_URL._fields_ = [
        ("pwszDescription", win32more.Foundation.PWSTR),
        ("pwszURL", win32more.Foundation.PWSTR),
    ]
    return WM_USER_WEB_URL
def _define_WM_USER_TEXT_head():
    class WM_USER_TEXT(Structure):
        pass
    return WM_USER_TEXT
def _define_WM_USER_TEXT():
    WM_USER_TEXT = win32more.Media.WindowsMediaFormat.WM_USER_TEXT_head
    WM_USER_TEXT._pack_ = 1
    WM_USER_TEXT._fields_ = [
        ("pwszDescription", win32more.Foundation.PWSTR),
        ("pwszText", win32more.Foundation.PWSTR),
    ]
    return WM_USER_TEXT
def _define_WM_LEAKY_BUCKET_PAIR_head():
    class WM_LEAKY_BUCKET_PAIR(Structure):
        pass
    return WM_LEAKY_BUCKET_PAIR
def _define_WM_LEAKY_BUCKET_PAIR():
    WM_LEAKY_BUCKET_PAIR = win32more.Media.WindowsMediaFormat.WM_LEAKY_BUCKET_PAIR_head
    WM_LEAKY_BUCKET_PAIR._pack_ = 1
    WM_LEAKY_BUCKET_PAIR._fields_ = [
        ("dwBitrate", UInt32),
        ("msBufferWindow", UInt32),
    ]
    return WM_LEAKY_BUCKET_PAIR
def _define_WM_STREAM_TYPE_INFO_head():
    class WM_STREAM_TYPE_INFO(Structure):
        pass
    return WM_STREAM_TYPE_INFO
def _define_WM_STREAM_TYPE_INFO():
    WM_STREAM_TYPE_INFO = win32more.Media.WindowsMediaFormat.WM_STREAM_TYPE_INFO_head
    WM_STREAM_TYPE_INFO._pack_ = 1
    WM_STREAM_TYPE_INFO._fields_ = [
        ("guidMajorType", Guid),
        ("cbFormat", UInt32),
    ]
    return WM_STREAM_TYPE_INFO
def _define_WMT_WATERMARK_ENTRY_head():
    class WMT_WATERMARK_ENTRY(Structure):
        pass
    return WMT_WATERMARK_ENTRY
def _define_WMT_WATERMARK_ENTRY():
    WMT_WATERMARK_ENTRY = win32more.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_head
    WMT_WATERMARK_ENTRY._fields_ = [
        ("wmetType", win32more.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE),
        ("clsid", Guid),
        ("cbDisplayName", UInt32),
        ("pwszDisplayName", win32more.Foundation.PWSTR),
    ]
    return WMT_WATERMARK_ENTRY
def _define_WMT_VIDEOIMAGE_SAMPLE_head():
    class WMT_VIDEOIMAGE_SAMPLE(Structure):
        pass
    return WMT_VIDEOIMAGE_SAMPLE
def _define_WMT_VIDEOIMAGE_SAMPLE():
    WMT_VIDEOIMAGE_SAMPLE = win32more.Media.WindowsMediaFormat.WMT_VIDEOIMAGE_SAMPLE_head
    WMT_VIDEOIMAGE_SAMPLE._fields_ = [
        ("dwMagic", UInt32),
        ("cbStruct", UInt32),
        ("dwControlFlags", UInt32),
        ("dwInputFlagsCur", UInt32),
        ("lCurMotionXtoX", Int32),
        ("lCurMotionYtoX", Int32),
        ("lCurMotionXoffset", Int32),
        ("lCurMotionXtoY", Int32),
        ("lCurMotionYtoY", Int32),
        ("lCurMotionYoffset", Int32),
        ("lCurBlendCoef1", Int32),
        ("lCurBlendCoef2", Int32),
        ("dwInputFlagsPrev", UInt32),
        ("lPrevMotionXtoX", Int32),
        ("lPrevMotionYtoX", Int32),
        ("lPrevMotionXoffset", Int32),
        ("lPrevMotionXtoY", Int32),
        ("lPrevMotionYtoY", Int32),
        ("lPrevMotionYoffset", Int32),
        ("lPrevBlendCoef1", Int32),
        ("lPrevBlendCoef2", Int32),
    ]
    return WMT_VIDEOIMAGE_SAMPLE
def _define_WMT_VIDEOIMAGE_SAMPLE2_head():
    class WMT_VIDEOIMAGE_SAMPLE2(Structure):
        pass
    return WMT_VIDEOIMAGE_SAMPLE2
def _define_WMT_VIDEOIMAGE_SAMPLE2():
    WMT_VIDEOIMAGE_SAMPLE2 = win32more.Media.WindowsMediaFormat.WMT_VIDEOIMAGE_SAMPLE2_head
    WMT_VIDEOIMAGE_SAMPLE2._fields_ = [
        ("dwMagic", UInt32),
        ("dwStructSize", UInt32),
        ("dwControlFlags", UInt32),
        ("dwViewportWidth", UInt32),
        ("dwViewportHeight", UInt32),
        ("dwCurrImageWidth", UInt32),
        ("dwCurrImageHeight", UInt32),
        ("fCurrRegionX0", Single),
        ("fCurrRegionY0", Single),
        ("fCurrRegionWidth", Single),
        ("fCurrRegionHeight", Single),
        ("fCurrBlendCoef", Single),
        ("dwPrevImageWidth", UInt32),
        ("dwPrevImageHeight", UInt32),
        ("fPrevRegionX0", Single),
        ("fPrevRegionY0", Single),
        ("fPrevRegionWidth", Single),
        ("fPrevRegionHeight", Single),
        ("fPrevBlendCoef", Single),
        ("dwEffectType", UInt32),
        ("dwNumEffectParas", UInt32),
        ("fEffectPara0", Single),
        ("fEffectPara1", Single),
        ("fEffectPara2", Single),
        ("fEffectPara3", Single),
        ("fEffectPara4", Single),
        ("bKeepPrevImage", win32more.Foundation.BOOL),
    ]
    return WMT_VIDEOIMAGE_SAMPLE2
def _define_WM_MEDIA_TYPE_head():
    class WM_MEDIA_TYPE(Structure):
        pass
    return WM_MEDIA_TYPE
def _define_WM_MEDIA_TYPE():
    WM_MEDIA_TYPE = win32more.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head
    WM_MEDIA_TYPE._fields_ = [
        ("majortype", Guid),
        ("subtype", Guid),
        ("bFixedSizeSamples", win32more.Foundation.BOOL),
        ("bTemporalCompression", win32more.Foundation.BOOL),
        ("lSampleSize", UInt32),
        ("formattype", Guid),
        ("pUnk", win32more.System.Com.IUnknown_head),
        ("cbFormat", UInt32),
        ("pbFormat", c_char_p_no),
    ]
    return WM_MEDIA_TYPE
def _define_WMVIDEOINFOHEADER_head():
    class WMVIDEOINFOHEADER(Structure):
        pass
    return WMVIDEOINFOHEADER
def _define_WMVIDEOINFOHEADER():
    WMVIDEOINFOHEADER = win32more.Media.WindowsMediaFormat.WMVIDEOINFOHEADER_head
    WMVIDEOINFOHEADER._fields_ = [
        ("rcSource", win32more.Foundation.RECT),
        ("rcTarget", win32more.Foundation.RECT),
        ("dwBitRate", UInt32),
        ("dwBitErrorRate", UInt32),
        ("AvgTimePerFrame", Int64),
        ("bmiHeader", win32more.Graphics.Gdi.BITMAPINFOHEADER),
    ]
    return WMVIDEOINFOHEADER
def _define_WMVIDEOINFOHEADER2_head():
    class WMVIDEOINFOHEADER2(Structure):
        pass
    return WMVIDEOINFOHEADER2
def _define_WMVIDEOINFOHEADER2():
    WMVIDEOINFOHEADER2 = win32more.Media.WindowsMediaFormat.WMVIDEOINFOHEADER2_head
    WMVIDEOINFOHEADER2._fields_ = [
        ("rcSource", win32more.Foundation.RECT),
        ("rcTarget", win32more.Foundation.RECT),
        ("dwBitRate", UInt32),
        ("dwBitErrorRate", UInt32),
        ("AvgTimePerFrame", Int64),
        ("dwInterlaceFlags", UInt32),
        ("dwCopyProtectFlags", UInt32),
        ("dwPictAspectRatioX", UInt32),
        ("dwPictAspectRatioY", UInt32),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
        ("bmiHeader", win32more.Graphics.Gdi.BITMAPINFOHEADER),
    ]
    return WMVIDEOINFOHEADER2
def _define_WMMPEG2VIDEOINFO_head():
    class WMMPEG2VIDEOINFO(Structure):
        pass
    return WMMPEG2VIDEOINFO
def _define_WMMPEG2VIDEOINFO():
    WMMPEG2VIDEOINFO = win32more.Media.WindowsMediaFormat.WMMPEG2VIDEOINFO_head
    WMMPEG2VIDEOINFO._fields_ = [
        ("hdr", win32more.Media.WindowsMediaFormat.WMVIDEOINFOHEADER2),
        ("dwStartTimeCode", UInt32),
        ("cbSequenceHeader", UInt32),
        ("dwProfile", UInt32),
        ("dwLevel", UInt32),
        ("dwFlags", UInt32),
        ("dwSequenceHeader", UInt32 * 0),
    ]
    return WMMPEG2VIDEOINFO
def _define_WMSCRIPTFORMAT_head():
    class WMSCRIPTFORMAT(Structure):
        pass
    return WMSCRIPTFORMAT
def _define_WMSCRIPTFORMAT():
    WMSCRIPTFORMAT = win32more.Media.WindowsMediaFormat.WMSCRIPTFORMAT_head
    WMSCRIPTFORMAT._fields_ = [
        ("scriptType", Guid),
    ]
    return WMSCRIPTFORMAT
def _define_WMT_COLORSPACEINFO_EXTENSION_DATA_head():
    class WMT_COLORSPACEINFO_EXTENSION_DATA(Structure):
        pass
    return WMT_COLORSPACEINFO_EXTENSION_DATA
def _define_WMT_COLORSPACEINFO_EXTENSION_DATA():
    WMT_COLORSPACEINFO_EXTENSION_DATA = win32more.Media.WindowsMediaFormat.WMT_COLORSPACEINFO_EXTENSION_DATA_head
    WMT_COLORSPACEINFO_EXTENSION_DATA._fields_ = [
        ("ucColorPrimaries", Byte),
        ("ucColorTransferChar", Byte),
        ("ucColorMatrixCoef", Byte),
    ]
    return WMT_COLORSPACEINFO_EXTENSION_DATA
def _define_WMT_TIMECODE_EXTENSION_DATA_head():
    class WMT_TIMECODE_EXTENSION_DATA(Structure):
        pass
    return WMT_TIMECODE_EXTENSION_DATA
def _define_WMT_TIMECODE_EXTENSION_DATA():
    WMT_TIMECODE_EXTENSION_DATA = win32more.Media.WindowsMediaFormat.WMT_TIMECODE_EXTENSION_DATA_head
    WMT_TIMECODE_EXTENSION_DATA._pack_ = 2
    WMT_TIMECODE_EXTENSION_DATA._fields_ = [
        ("wRange", UInt16),
        ("dwTimecode", UInt32),
        ("dwUserbits", UInt32),
        ("dwAmFlags", UInt32),
    ]
    return WMT_TIMECODE_EXTENSION_DATA
def _define_DRM_VAL16_head():
    class DRM_VAL16(Structure):
        pass
    return DRM_VAL16
def _define_DRM_VAL16():
    DRM_VAL16 = win32more.Media.WindowsMediaFormat.DRM_VAL16_head
    DRM_VAL16._fields_ = [
        ("val", Byte * 16),
    ]
    return DRM_VAL16
def _define_IWMMediaProps_head():
    class IWMMediaProps(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bce-2b2b-11d3-b36b-00c04f6108ff')
    return IWMMediaProps
def _define_IWMMediaProps():
    IWMMediaProps = win32more.Media.WindowsMediaFormat.IWMMediaProps_head
    IWMMediaProps.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetType', ((1, 'pguidType'),)))
    IWMMediaProps.GetMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head),POINTER(UInt32), use_last_error=False)(4, 'GetMediaType', ((1, 'pType'),(1, 'pcbType'),)))
    IWMMediaProps.SetMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head), use_last_error=False)(5, 'SetMediaType', ((1, 'pType'),)))
    return IWMMediaProps
def _define_IWMVideoMediaProps_head():
    class IWMVideoMediaProps(win32more.Media.WindowsMediaFormat.IWMMediaProps_head):
        Guid = Guid('96406bcf-2b2b-11d3-b36b-00c04f6108ff')
    return IWMVideoMediaProps
def _define_IWMVideoMediaProps():
    IWMVideoMediaProps = win32more.Media.WindowsMediaFormat.IWMVideoMediaProps_head
    IWMVideoMediaProps.GetMaxKeyFrameSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(6, 'GetMaxKeyFrameSpacing', ((1, 'pllTime'),)))
    IWMVideoMediaProps.SetMaxKeyFrameSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64, use_last_error=False)(7, 'SetMaxKeyFrameSpacing', ((1, 'llTime'),)))
    IWMVideoMediaProps.GetQuality = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetQuality', ((1, 'pdwQuality'),)))
    IWMVideoMediaProps.SetQuality = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetQuality', ((1, 'dwQuality'),)))
    return IWMVideoMediaProps
def _define_IWMWriter_head():
    class IWMWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bd4-2b2b-11d3-b36b-00c04f6108ff')
    return IWMWriter
def _define_IWMWriter():
    IWMWriter = win32more.Media.WindowsMediaFormat.IWMWriter_head
    IWMWriter.SetProfileByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'SetProfileByID', ((1, 'guidProfile'),)))
    IWMWriter.SetProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMProfile_head, use_last_error=False)(4, 'SetProfile', ((1, 'pProfile'),)))
    IWMWriter.SetOutputFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetOutputFilename', ((1, 'pwszFilename'),)))
    IWMWriter.GetInputCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetInputCount', ((1, 'pcInputs'),)))
    IWMWriter.GetInputProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMInputMediaProps_head), use_last_error=False)(7, 'GetInputProps', ((1, 'dwInputNum'),(1, 'ppInput'),)))
    IWMWriter.SetInputProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMInputMediaProps_head, use_last_error=False)(8, 'SetInputProps', ((1, 'dwInputNum'),(1, 'pInput'),)))
    IWMWriter.GetInputFormatCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(9, 'GetInputFormatCount', ((1, 'dwInputNumber'),(1, 'pcFormats'),)))
    IWMWriter.GetInputFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMInputMediaProps_head), use_last_error=False)(10, 'GetInputFormat', ((1, 'dwInputNumber'),(1, 'dwFormatNumber'),(1, 'pProps'),)))
    IWMWriter.BeginWriting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'BeginWriting', ()))
    IWMWriter.EndWriting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'EndWriting', ()))
    IWMWriter.AllocateSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head), use_last_error=False)(13, 'AllocateSample', ((1, 'dwSampleSize'),(1, 'ppSample'),)))
    IWMWriter.WriteSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,UInt32,win32more.Media.WindowsMediaFormat.INSSBuffer_head, use_last_error=False)(14, 'WriteSample', ((1, 'dwInputNum'),(1, 'cnsSampleTime'),(1, 'dwFlags'),(1, 'pSample'),)))
    IWMWriter.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Flush', ()))
    return IWMWriter
def _define_IWMDRMWriter_head():
    class IWMDRMWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('d6ea5dd0-12a0-43f4-90ab-a3fd451e6a07')
    return IWMDRMWriter
def _define_IWMDRMWriter():
    IWMDRMWriter = win32more.Media.WindowsMediaFormat.IWMDRMWriter_head
    IWMDRMWriter.GenerateKeySeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32), use_last_error=False)(3, 'GenerateKeySeed', ((1, 'pwszKeySeed'),(1, 'pcwchLength'),)))
    IWMDRMWriter.GenerateKeyID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32), use_last_error=False)(4, 'GenerateKeyID', ((1, 'pwszKeyID'),(1, 'pcwchLength'),)))
    IWMDRMWriter.GenerateSigningKeyPair = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32), use_last_error=False)(5, 'GenerateSigningKeyPair', ((1, 'pwszPrivKey'),(1, 'pcwchPrivKeyLength'),(1, 'pwszPubKey'),(1, 'pcwchPubKeyLength'),)))
    IWMDRMWriter.SetDRMAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt16, use_last_error=False)(6, 'SetDRMAttribute', ((1, 'wStreamNum'),(1, 'pszName'),(1, 'Type'),(1, 'pValue'),(1, 'cbLength'),)))
    return IWMDRMWriter
def _define_WMDRM_IMPORT_INIT_STRUCT_head():
    class WMDRM_IMPORT_INIT_STRUCT(Structure):
        pass
    return WMDRM_IMPORT_INIT_STRUCT
def _define_WMDRM_IMPORT_INIT_STRUCT():
    WMDRM_IMPORT_INIT_STRUCT = win32more.Media.WindowsMediaFormat.WMDRM_IMPORT_INIT_STRUCT_head
    WMDRM_IMPORT_INIT_STRUCT._fields_ = [
        ("dwVersion", UInt32),
        ("cbEncryptedSessionKeyMessage", UInt32),
        ("pbEncryptedSessionKeyMessage", c_char_p_no),
        ("cbEncryptedKeyMessage", UInt32),
        ("pbEncryptedKeyMessage", c_char_p_no),
    ]
    return WMDRM_IMPORT_INIT_STRUCT
def _define_IWMDRMWriter2_head():
    class IWMDRMWriter2(win32more.Media.WindowsMediaFormat.IWMDRMWriter_head):
        Guid = Guid('38ee7a94-40e2-4e10-aa3f-33fd3210ed5b')
    return IWMDRMWriter2
def _define_IWMDRMWriter2():
    IWMDRMWriter2 = win32more.Media.WindowsMediaFormat.IWMDRMWriter2_head
    IWMDRMWriter2.SetWMDRMNetEncryption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,c_char_p_no,UInt32, use_last_error=False)(7, 'SetWMDRMNetEncryption', ((1, 'fSamplesEncrypted'),(1, 'pbKeyID'),(1, 'cbKeyID'),)))
    return IWMDRMWriter2
def _define_IWMDRMWriter3_head():
    class IWMDRMWriter3(win32more.Media.WindowsMediaFormat.IWMDRMWriter2_head):
        Guid = Guid('a7184082-a4aa-4dde-ac9c-e75dbd1117ce')
    return IWMDRMWriter3
def _define_IWMDRMWriter3():
    IWMDRMWriter3 = win32more.Media.WindowsMediaFormat.IWMDRMWriter3_head
    IWMDRMWriter3.SetProtectStreamSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMDRM_IMPORT_INIT_STRUCT_head), use_last_error=False)(8, 'SetProtectStreamSamples', ((1, 'pImportInitStruct'),)))
    return IWMDRMWriter3
def _define_IWMInputMediaProps_head():
    class IWMInputMediaProps(win32more.Media.WindowsMediaFormat.IWMMediaProps_head):
        Guid = Guid('96406bd5-2b2b-11d3-b36b-00c04f6108ff')
    return IWMInputMediaProps
def _define_IWMInputMediaProps():
    IWMInputMediaProps = win32more.Media.WindowsMediaFormat.IWMInputMediaProps_head
    IWMInputMediaProps.GetConnectionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(6, 'GetConnectionName', ((1, 'pwszName'),(1, 'pcchName'),)))
    IWMInputMediaProps.GetGroupName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(7, 'GetGroupName', ((1, 'pwszName'),(1, 'pcchName'),)))
    return IWMInputMediaProps
def _define_IWMPropertyVault_head():
    class IWMPropertyVault(win32more.System.Com.IUnknown_head):
        Guid = Guid('72995a79-5090-42a4-9c8c-d9d0b6d34be5')
    return IWMPropertyVault
def _define_IWMPropertyVault():
    IWMPropertyVault = win32more.Media.WindowsMediaFormat.IWMPropertyVault_head
    IWMPropertyVault.GetPropertyCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetPropertyCount', ((1, 'pdwCount'),)))
    IWMPropertyVault.GetPropertyByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt32), use_last_error=False)(4, 'GetPropertyByName', ((1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pdwSize'),)))
    IWMPropertyVault.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,c_char_p_no,UInt32, use_last_error=False)(5, 'SetProperty', ((1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'dwSize'),)))
    IWMPropertyVault.GetPropertyByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32),POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt32), use_last_error=False)(6, 'GetPropertyByIndex', ((1, 'dwIndex'),(1, 'pszName'),(1, 'pdwNameLen'),(1, 'pType'),(1, 'pValue'),(1, 'pdwSize'),)))
    IWMPropertyVault.CopyPropertiesFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMPropertyVault_head, use_last_error=False)(7, 'CopyPropertiesFrom', ((1, 'pIWMPropertyVault'),)))
    IWMPropertyVault.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Clear', ()))
    return IWMPropertyVault
def _define_IWMIStreamProps_head():
    class IWMIStreamProps(win32more.System.Com.IUnknown_head):
        Guid = Guid('6816dad3-2b4b-4c8e-8149-874c3483a753')
    return IWMIStreamProps
def _define_IWMIStreamProps():
    IWMIStreamProps = win32more.Media.WindowsMediaFormat.IWMIStreamProps_head
    IWMIStreamProps.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt32), use_last_error=False)(3, 'GetProperty', ((1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pdwSize'),)))
    return IWMIStreamProps
def _define_IWMReader_head():
    class IWMReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bd6-2b2b-11d3-b36b-00c04f6108ff')
    return IWMReader
def _define_IWMReader():
    IWMReader = win32more.Media.WindowsMediaFormat.IWMReader_head
    IWMReader.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.IWMReaderCallback_head,c_void_p, use_last_error=False)(3, 'Open', ((1, 'pwszURL'),(1, 'pCallback'),(1, 'pvContext'),)))
    IWMReader.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IWMReader.GetOutputCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetOutputCount', ((1, 'pcOutputs'),)))
    IWMReader.GetOutputProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head), use_last_error=False)(6, 'GetOutputProps', ((1, 'dwOutputNum'),(1, 'ppOutput'),)))
    IWMReader.SetOutputProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head, use_last_error=False)(7, 'SetOutputProps', ((1, 'dwOutputNum'),(1, 'pOutput'),)))
    IWMReader.GetOutputFormatCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(8, 'GetOutputFormatCount', ((1, 'dwOutputNumber'),(1, 'pcFormats'),)))
    IWMReader.GetOutputFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head), use_last_error=False)(9, 'GetOutputFormat', ((1, 'dwOutputNumber'),(1, 'dwFormatNumber'),(1, 'ppProps'),)))
    IWMReader.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,Single,c_void_p, use_last_error=False)(10, 'Start', ((1, 'cnsStart'),(1, 'cnsDuration'),(1, 'fRate'),(1, 'pvContext'),)))
    IWMReader.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Stop', ()))
    IWMReader.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Pause', ()))
    IWMReader.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Resume', ()))
    return IWMReader
def _define_IWMSyncReader_head():
    class IWMSyncReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('9397f121-7705-4dc9-b049-98b698188414')
    return IWMSyncReader
def _define_IWMSyncReader():
    IWMSyncReader = win32more.Media.WindowsMediaFormat.IWMSyncReader_head
    IWMSyncReader.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Open', ((1, 'pwszFilename'),)))
    IWMSyncReader.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IWMSyncReader.SetRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,Int64, use_last_error=False)(5, 'SetRange', ((1, 'cnsStartTime'),(1, 'cnsDuration'),)))
    IWMSyncReader.SetRangeByFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt64,Int64, use_last_error=False)(6, 'SetRangeByFrame', ((1, 'wStreamNum'),(1, 'qwFrameNumber'),(1, 'cFramesToRead'),)))
    IWMSyncReader.GetNextSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),POINTER(UInt64),POINTER(UInt64),POINTER(UInt32),POINTER(UInt32),POINTER(UInt16), use_last_error=False)(7, 'GetNextSample', ((1, 'wStreamNum'),(1, 'ppSample'),(1, 'pcnsSampleTime'),(1, 'pcnsDuration'),(1, 'pdwFlags'),(1, 'pdwOutputNum'),(1, 'pwStreamNum'),)))
    IWMSyncReader.SetStreamsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16),POINTER(win32more.Media.WindowsMediaFormat.WMT_STREAM_SELECTION), use_last_error=False)(8, 'SetStreamsSelected', ((1, 'cStreamCount'),(1, 'pwStreamNumbers'),(1, 'pSelections'),)))
    IWMSyncReader.GetStreamSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.WMT_STREAM_SELECTION), use_last_error=False)(9, 'GetStreamSelected', ((1, 'wStreamNum'),(1, 'pSelection'),)))
    IWMSyncReader.SetReadStreamSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.BOOL, use_last_error=False)(10, 'SetReadStreamSamples', ((1, 'wStreamNum'),(1, 'fCompressed'),)))
    IWMSyncReader.GetReadStreamSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'GetReadStreamSamples', ((1, 'wStreamNum'),(1, 'pfCompressed'),)))
    IWMSyncReader.GetOutputSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(12, 'GetOutputSetting', ((1, 'dwOutputNum'),(1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMSyncReader.SetOutputSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt16, use_last_error=False)(13, 'SetOutputSetting', ((1, 'dwOutputNum'),(1, 'pszName'),(1, 'Type'),(1, 'pValue'),(1, 'cbLength'),)))
    IWMSyncReader.GetOutputCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'GetOutputCount', ((1, 'pcOutputs'),)))
    IWMSyncReader.GetOutputProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head), use_last_error=False)(15, 'GetOutputProps', ((1, 'dwOutputNum'),(1, 'ppOutput'),)))
    IWMSyncReader.SetOutputProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head, use_last_error=False)(16, 'SetOutputProps', ((1, 'dwOutputNum'),(1, 'pOutput'),)))
    IWMSyncReader.GetOutputFormatCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(17, 'GetOutputFormatCount', ((1, 'dwOutputNum'),(1, 'pcFormats'),)))
    IWMSyncReader.GetOutputFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head), use_last_error=False)(18, 'GetOutputFormat', ((1, 'dwOutputNum'),(1, 'dwFormatNum'),(1, 'ppProps'),)))
    IWMSyncReader.GetOutputNumberForStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt32), use_last_error=False)(19, 'GetOutputNumberForStream', ((1, 'wStreamNum'),(1, 'pdwOutputNum'),)))
    IWMSyncReader.GetStreamNumberForOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16), use_last_error=False)(20, 'GetStreamNumberForOutput', ((1, 'dwOutputNum'),(1, 'pwStreamNum'),)))
    IWMSyncReader.GetMaxOutputSampleSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(21, 'GetMaxOutputSampleSize', ((1, 'dwOutput'),(1, 'pcbMax'),)))
    IWMSyncReader.GetMaxStreamSampleSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt32), use_last_error=False)(22, 'GetMaxStreamSampleSize', ((1, 'wStream'),(1, 'pcbMax'),)))
    IWMSyncReader.OpenStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(23, 'OpenStream', ((1, 'pStream'),)))
    return IWMSyncReader
def _define_IWMSyncReader2_head():
    class IWMSyncReader2(win32more.Media.WindowsMediaFormat.IWMSyncReader_head):
        Guid = Guid('faed3d21-1b6b-4af7-8cb6-3e189bbc187b')
    return IWMSyncReader2
def _define_IWMSyncReader2():
    IWMSyncReader2 = win32more.Media.WindowsMediaFormat.IWMSyncReader2_head
    IWMSyncReader2.SetRangeByTimecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.WMT_TIMECODE_EXTENSION_DATA_head),POINTER(win32more.Media.WindowsMediaFormat.WMT_TIMECODE_EXTENSION_DATA_head), use_last_error=False)(24, 'SetRangeByTimecode', ((1, 'wStreamNum'),(1, 'pStart'),(1, 'pEnd'),)))
    IWMSyncReader2.SetRangeByFrameEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt64,Int64,POINTER(UInt64), use_last_error=False)(25, 'SetRangeByFrameEx', ((1, 'wStreamNum'),(1, 'qwFrameNumber'),(1, 'cFramesToRead'),(1, 'pcnsStartTime'),)))
    IWMSyncReader2.SetAllocateForOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head, use_last_error=False)(26, 'SetAllocateForOutput', ((1, 'dwOutputNum'),(1, 'pAllocator'),)))
    IWMSyncReader2.GetAllocateForOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head), use_last_error=False)(27, 'GetAllocateForOutput', ((1, 'dwOutputNum'),(1, 'ppAllocator'),)))
    IWMSyncReader2.SetAllocateForStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head, use_last_error=False)(28, 'SetAllocateForStream', ((1, 'wStreamNum'),(1, 'pAllocator'),)))
    IWMSyncReader2.GetAllocateForStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head), use_last_error=False)(29, 'GetAllocateForStream', ((1, 'dwSreamNum'),(1, 'ppAllocator'),)))
    return IWMSyncReader2
def _define_IWMOutputMediaProps_head():
    class IWMOutputMediaProps(win32more.Media.WindowsMediaFormat.IWMMediaProps_head):
        Guid = Guid('96406bd7-2b2b-11d3-b36b-00c04f6108ff')
    return IWMOutputMediaProps
def _define_IWMOutputMediaProps():
    IWMOutputMediaProps = win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head
    IWMOutputMediaProps.GetStreamGroupName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(6, 'GetStreamGroupName', ((1, 'pwszName'),(1, 'pcchName'),)))
    IWMOutputMediaProps.GetConnectionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(7, 'GetConnectionName', ((1, 'pwszName'),(1, 'pcchName'),)))
    return IWMOutputMediaProps
def _define_IWMStatusCallback_head():
    class IWMStatusCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d7cdc70-9888-11d3-8edc-00c04f6109cf')
    return IWMStatusCallback
def _define_IWMStatusCallback():
    IWMStatusCallback = win32more.Media.WindowsMediaFormat.IWMStatusCallback_head
    IWMStatusCallback.OnStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_STATUS,win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,c_char_p_no,c_void_p, use_last_error=False)(3, 'OnStatus', ((1, 'Status'),(1, 'hr'),(1, 'dwType'),(1, 'pValue'),(1, 'pvContext'),)))
    return IWMStatusCallback
def _define_IWMReaderCallback_head():
    class IWMReaderCallback(win32more.Media.WindowsMediaFormat.IWMStatusCallback_head):
        Guid = Guid('96406bd8-2b2b-11d3-b36b-00c04f6108ff')
    return IWMReaderCallback
def _define_IWMReaderCallback():
    IWMReaderCallback = win32more.Media.WindowsMediaFormat.IWMReaderCallback_head
    IWMReaderCallback.OnSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,UInt64,UInt32,win32more.Media.WindowsMediaFormat.INSSBuffer_head,c_void_p, use_last_error=False)(4, 'OnSample', ((1, 'dwOutputNum'),(1, 'cnsSampleTime'),(1, 'cnsSampleDuration'),(1, 'dwFlags'),(1, 'pSample'),(1, 'pvContext'),)))
    return IWMReaderCallback
def _define_IWMCredentialCallback_head():
    class IWMCredentialCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('342e0eb7-e651-450c-975b-2ace2c90c48e')
    return IWMCredentialCallback
def _define_IWMCredentialCallback():
    IWMCredentialCallback = win32more.Media.WindowsMediaFormat.IWMCredentialCallback_head
    IWMCredentialCallback.AcquireCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Char),UInt32,POINTER(Char),UInt32,win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'AcquireCredentials', ((1, 'pwszRealm'),(1, 'pwszSite'),(1, 'pwszUser'),(1, 'cchUser'),(1, 'pwszPassword'),(1, 'cchPassword'),(1, 'hrStatus'),(1, 'pdwFlags'),)))
    return IWMCredentialCallback
def _define_IWMMetadataEditor_head():
    class IWMMetadataEditor(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bd9-2b2b-11d3-b36b-00c04f6108ff')
    return IWMMetadataEditor
def _define_IWMMetadataEditor():
    IWMMetadataEditor = win32more.Media.WindowsMediaFormat.IWMMetadataEditor_head
    IWMMetadataEditor.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Open', ((1, 'pwszFilename'),)))
    IWMMetadataEditor.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IWMMetadataEditor.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Flush', ()))
    return IWMMetadataEditor
def _define_IWMMetadataEditor2_head():
    class IWMMetadataEditor2(win32more.Media.WindowsMediaFormat.IWMMetadataEditor_head):
        Guid = Guid('203cffe3-2e18-4fdf-b59d-6e71530534cf')
    return IWMMetadataEditor2
def _define_IWMMetadataEditor2():
    IWMMetadataEditor2 = win32more.Media.WindowsMediaFormat.IWMMetadataEditor2_head
    IWMMetadataEditor2.OpenEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(6, 'OpenEx', ((1, 'pwszFilename'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),)))
    return IWMMetadataEditor2
def _define_IWMDRMEditor_head():
    class IWMDRMEditor(win32more.System.Com.IUnknown_head):
        Guid = Guid('ff130ebc-a6c3-42a6-b401-c3382c3e08b3')
    return IWMDRMEditor
def _define_IWMDRMEditor():
    IWMDRMEditor = win32more.Media.WindowsMediaFormat.IWMDRMEditor_head
    IWMDRMEditor.GetDRMProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(3, 'GetDRMProperty', ((1, 'pwstrName'),(1, 'pdwType'),(1, 'pValue'),(1, 'pcbLength'),)))
    return IWMDRMEditor
def _define_IWMHeaderInfo_head():
    class IWMHeaderInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bda-2b2b-11d3-b36b-00c04f6108ff')
    return IWMHeaderInfo
def _define_IWMHeaderInfo():
    IWMHeaderInfo = win32more.Media.WindowsMediaFormat.IWMHeaderInfo_head
    IWMHeaderInfo.GetAttributeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16), use_last_error=False)(3, 'GetAttributeCount', ((1, 'wStreamNum'),(1, 'pcAttributes'),)))
    IWMHeaderInfo.GetAttributeByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16),POINTER(Char),POINTER(UInt16),POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(4, 'GetAttributeByIndex', ((1, 'wIndex'),(1, 'pwStreamNum'),(1, 'pwszName'),(1, 'pcchNameLen'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMHeaderInfo.GetAttributeByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(5, 'GetAttributeByName', ((1, 'pwStreamNum'),(1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMHeaderInfo.SetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt16, use_last_error=False)(6, 'SetAttribute', ((1, 'wStreamNum'),(1, 'pszName'),(1, 'Type'),(1, 'pValue'),(1, 'cbLength'),)))
    IWMHeaderInfo.GetMarkerCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(7, 'GetMarkerCount', ((1, 'pcMarkers'),)))
    IWMHeaderInfo.GetMarker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Char),POINTER(UInt16),POINTER(UInt64), use_last_error=False)(8, 'GetMarker', ((1, 'wIndex'),(1, 'pwszMarkerName'),(1, 'pcchMarkerNameLen'),(1, 'pcnsMarkerTime'),)))
    IWMHeaderInfo.AddMarker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt64, use_last_error=False)(9, 'AddMarker', ((1, 'pwszMarkerName'),(1, 'cnsMarkerTime'),)))
    IWMHeaderInfo.RemoveMarker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(10, 'RemoveMarker', ((1, 'wIndex'),)))
    IWMHeaderInfo.GetScriptCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(11, 'GetScriptCount', ((1, 'pcScripts'),)))
    IWMHeaderInfo.GetScript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Char),POINTER(UInt16),POINTER(Char),POINTER(UInt16),POINTER(UInt64), use_last_error=False)(12, 'GetScript', ((1, 'wIndex'),(1, 'pwszType'),(1, 'pcchTypeLen'),(1, 'pwszCommand'),(1, 'pcchCommandLen'),(1, 'pcnsScriptTime'),)))
    IWMHeaderInfo.AddScript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt64, use_last_error=False)(13, 'AddScript', ((1, 'pwszType'),(1, 'pwszCommand'),(1, 'cnsScriptTime'),)))
    IWMHeaderInfo.RemoveScript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(14, 'RemoveScript', ((1, 'wIndex'),)))
    return IWMHeaderInfo
def _define_IWMHeaderInfo2_head():
    class IWMHeaderInfo2(win32more.Media.WindowsMediaFormat.IWMHeaderInfo_head):
        Guid = Guid('15cf9781-454e-482e-b393-85fae487a810')
    return IWMHeaderInfo2
def _define_IWMHeaderInfo2():
    IWMHeaderInfo2 = win32more.Media.WindowsMediaFormat.IWMHeaderInfo2_head
    IWMHeaderInfo2.GetCodecInfoCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(15, 'GetCodecInfoCount', ((1, 'pcCodecInfos'),)))
    IWMHeaderInfo2.GetCodecInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16),POINTER(Char),POINTER(UInt16),POINTER(Char),POINTER(win32more.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE),POINTER(UInt16),POINTER(Byte), use_last_error=False)(16, 'GetCodecInfo', ((1, 'wIndex'),(1, 'pcchName'),(1, 'pwszName'),(1, 'pcchDescription'),(1, 'pwszDescription'),(1, 'pCodecType'),(1, 'pcbCodecInfo'),(1, 'pbCodecInfo'),)))
    return IWMHeaderInfo2
def _define_IWMHeaderInfo3_head():
    class IWMHeaderInfo3(win32more.Media.WindowsMediaFormat.IWMHeaderInfo2_head):
        Guid = Guid('15cc68e3-27cc-4ecd-b222-3f5d02d80bd5')
    return IWMHeaderInfo3
def _define_IWMHeaderInfo3():
    IWMHeaderInfo3 = win32more.Media.WindowsMediaFormat.IWMHeaderInfo3_head
    IWMHeaderInfo3.GetAttributeCountEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16), use_last_error=False)(17, 'GetAttributeCountEx', ((1, 'wStreamNum'),(1, 'pcAttributes'),)))
    IWMHeaderInfo3.GetAttributeIndices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16), use_last_error=False)(18, 'GetAttributeIndices', ((1, 'wStreamNum'),(1, 'pwszName'),(1, 'pwLangIndex'),(1, 'pwIndices'),(1, 'pwCount'),)))
    IWMHeaderInfo3.GetAttributeByIndexEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16,POINTER(Char),POINTER(UInt16),POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(UInt16),POINTER(Byte),POINTER(UInt32), use_last_error=False)(19, 'GetAttributeByIndexEx', ((1, 'wStreamNum'),(1, 'wIndex'),(1, 'pwszName'),(1, 'pwNameLen'),(1, 'pType'),(1, 'pwLangIndex'),(1, 'pValue'),(1, 'pdwDataLength'),)))
    IWMHeaderInfo3.ModifyAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,UInt16,POINTER(Byte),UInt32, use_last_error=False)(20, 'ModifyAttribute', ((1, 'wStreamNum'),(1, 'wIndex'),(1, 'Type'),(1, 'wLangIndex'),(1, 'pValue'),(1, 'dwLength'),)))
    IWMHeaderInfo3.AddAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR,POINTER(UInt16),win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,UInt16,POINTER(Byte),UInt32, use_last_error=False)(21, 'AddAttribute', ((1, 'wStreamNum'),(1, 'pszName'),(1, 'pwIndex'),(1, 'Type'),(1, 'wLangIndex'),(1, 'pValue'),(1, 'dwLength'),)))
    IWMHeaderInfo3.DeleteAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16, use_last_error=False)(22, 'DeleteAttribute', ((1, 'wStreamNum'),(1, 'wIndex'),)))
    IWMHeaderInfo3.AddCodecInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_CODEC_INFO_TYPE,UInt16,POINTER(Byte), use_last_error=False)(23, 'AddCodecInfo', ((1, 'pwszName'),(1, 'pwszDescription'),(1, 'codecType'),(1, 'cbCodecInfo'),(1, 'pbCodecInfo'),)))
    return IWMHeaderInfo3
def _define_IWMProfileManager_head():
    class IWMProfileManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('d16679f2-6ca0-472d-8d31-2f5d55aee155')
    return IWMProfileManager
def _define_IWMProfileManager():
    IWMProfileManager = win32more.Media.WindowsMediaFormat.IWMProfileManager_head
    IWMProfileManager.CreateEmptyProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_VERSION,POINTER(win32more.Media.WindowsMediaFormat.IWMProfile_head), use_last_error=False)(3, 'CreateEmptyProfile', ((1, 'dwVersion'),(1, 'ppProfile'),)))
    IWMProfileManager.LoadProfileByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.WindowsMediaFormat.IWMProfile_head), use_last_error=False)(4, 'LoadProfileByID', ((1, 'guidProfile'),(1, 'ppProfile'),)))
    IWMProfileManager.LoadProfileByData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.IWMProfile_head), use_last_error=False)(5, 'LoadProfileByData', ((1, 'pwszProfile'),(1, 'ppProfile'),)))
    IWMProfileManager.SaveProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMProfile_head,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(6, 'SaveProfile', ((1, 'pIWMProfile'),(1, 'pwszProfile'),(1, 'pdwLength'),)))
    IWMProfileManager.GetSystemProfileCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetSystemProfileCount', ((1, 'pcProfiles'),)))
    IWMProfileManager.LoadSystemProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMProfile_head), use_last_error=False)(8, 'LoadSystemProfile', ((1, 'dwProfileIndex'),(1, 'ppProfile'),)))
    return IWMProfileManager
def _define_IWMProfileManager2_head():
    class IWMProfileManager2(win32more.Media.WindowsMediaFormat.IWMProfileManager_head):
        Guid = Guid('7a924e51-73c1-494d-8019-23d37ed9b89a')
    return IWMProfileManager2
def _define_IWMProfileManager2():
    IWMProfileManager2 = win32more.Media.WindowsMediaFormat.IWMProfileManager2_head
    IWMProfileManager2.GetSystemProfileVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMT_VERSION), use_last_error=False)(9, 'GetSystemProfileVersion', ((1, 'pdwVersion'),)))
    IWMProfileManager2.SetSystemProfileVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_VERSION, use_last_error=False)(10, 'SetSystemProfileVersion', ((1, 'dwVersion'),)))
    return IWMProfileManager2
def _define_IWMProfileManagerLanguage_head():
    class IWMProfileManagerLanguage(win32more.System.Com.IUnknown_head):
        Guid = Guid('ba4dcc78-7ee0-4ab8-b27a-dbce8bc51454')
    return IWMProfileManagerLanguage
def _define_IWMProfileManagerLanguage():
    IWMProfileManagerLanguage = win32more.Media.WindowsMediaFormat.IWMProfileManagerLanguage_head
    IWMProfileManagerLanguage.GetUserLanguageID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(3, 'GetUserLanguageID', ((1, 'wLangID'),)))
    IWMProfileManagerLanguage.SetUserLanguageID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(4, 'SetUserLanguageID', ((1, 'wLangID'),)))
    return IWMProfileManagerLanguage
def _define_IWMProfile_head():
    class IWMProfile(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bdb-2b2b-11d3-b36b-00c04f6108ff')
    return IWMProfile
def _define_IWMProfile():
    IWMProfile = win32more.Media.WindowsMediaFormat.IWMProfile_head
    IWMProfile.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMT_VERSION), use_last_error=False)(3, 'GetVersion', ((1, 'pdwVersion'),)))
    IWMProfile.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32), use_last_error=False)(4, 'GetName', ((1, 'pwszName'),(1, 'pcchName'),)))
    IWMProfile.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetName', ((1, 'pwszName'),)))
    IWMProfile.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32), use_last_error=False)(6, 'GetDescription', ((1, 'pwszDescription'),(1, 'pcchDescription'),)))
    IWMProfile.SetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetDescription', ((1, 'pwszDescription'),)))
    IWMProfile.GetStreamCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetStreamCount', ((1, 'pcStreams'),)))
    IWMProfile.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMStreamConfig_head), use_last_error=False)(9, 'GetStream', ((1, 'dwStreamIndex'),(1, 'ppConfig'),)))
    IWMProfile.GetStreamByNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.IWMStreamConfig_head), use_last_error=False)(10, 'GetStreamByNumber', ((1, 'wStreamNum'),(1, 'ppConfig'),)))
    IWMProfile.RemoveStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMStreamConfig_head, use_last_error=False)(11, 'RemoveStream', ((1, 'pConfig'),)))
    IWMProfile.RemoveStreamByNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(12, 'RemoveStreamByNumber', ((1, 'wStreamNum'),)))
    IWMProfile.AddStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMStreamConfig_head, use_last_error=False)(13, 'AddStream', ((1, 'pConfig'),)))
    IWMProfile.ReconfigStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMStreamConfig_head, use_last_error=False)(14, 'ReconfigStream', ((1, 'pConfig'),)))
    IWMProfile.CreateNewStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.WindowsMediaFormat.IWMStreamConfig_head), use_last_error=False)(15, 'CreateNewStream', ((1, 'guidStreamType'),(1, 'ppConfig'),)))
    IWMProfile.GetMutualExclusionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(16, 'GetMutualExclusionCount', ((1, 'pcME'),)))
    IWMProfile.GetMutualExclusion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMMutualExclusion_head), use_last_error=False)(17, 'GetMutualExclusion', ((1, 'dwMEIndex'),(1, 'ppME'),)))
    IWMProfile.RemoveMutualExclusion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMMutualExclusion_head, use_last_error=False)(18, 'RemoveMutualExclusion', ((1, 'pME'),)))
    IWMProfile.AddMutualExclusion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMMutualExclusion_head, use_last_error=False)(19, 'AddMutualExclusion', ((1, 'pME'),)))
    IWMProfile.CreateNewMutualExclusion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMMutualExclusion_head), use_last_error=False)(20, 'CreateNewMutualExclusion', ((1, 'ppME'),)))
    return IWMProfile
def _define_IWMProfile2_head():
    class IWMProfile2(win32more.Media.WindowsMediaFormat.IWMProfile_head):
        Guid = Guid('07e72d33-d94e-4be7-8843-60ae5ff7e5f5')
    return IWMProfile2
def _define_IWMProfile2():
    IWMProfile2 = win32more.Media.WindowsMediaFormat.IWMProfile2_head
    IWMProfile2.GetProfileID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(21, 'GetProfileID', ((1, 'pguidID'),)))
    return IWMProfile2
def _define_IWMProfile3_head():
    class IWMProfile3(win32more.Media.WindowsMediaFormat.IWMProfile2_head):
        Guid = Guid('00ef96cc-a461-4546-8bcd-c9a28f0e06f5')
    return IWMProfile3
def _define_IWMProfile3():
    IWMProfile3 = win32more.Media.WindowsMediaFormat.IWMProfile3_head
    IWMProfile3.GetStorageFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT), use_last_error=False)(22, 'GetStorageFormat', ((1, 'pnStorageFormat'),)))
    IWMProfile3.SetStorageFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_STORAGE_FORMAT, use_last_error=False)(23, 'SetStorageFormat', ((1, 'nStorageFormat'),)))
    IWMProfile3.GetBandwidthSharingCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(24, 'GetBandwidthSharingCount', ((1, 'pcBS'),)))
    IWMProfile3.GetBandwidthSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMBandwidthSharing_head), use_last_error=False)(25, 'GetBandwidthSharing', ((1, 'dwBSIndex'),(1, 'ppBS'),)))
    IWMProfile3.RemoveBandwidthSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMBandwidthSharing_head, use_last_error=False)(26, 'RemoveBandwidthSharing', ((1, 'pBS'),)))
    IWMProfile3.AddBandwidthSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMBandwidthSharing_head, use_last_error=False)(27, 'AddBandwidthSharing', ((1, 'pBS'),)))
    IWMProfile3.CreateNewBandwidthSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMBandwidthSharing_head), use_last_error=False)(28, 'CreateNewBandwidthSharing', ((1, 'ppBS'),)))
    IWMProfile3.GetStreamPrioritization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMStreamPrioritization_head), use_last_error=False)(29, 'GetStreamPrioritization', ((1, 'ppSP'),)))
    IWMProfile3.SetStreamPrioritization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMStreamPrioritization_head, use_last_error=False)(30, 'SetStreamPrioritization', ((1, 'pSP'),)))
    IWMProfile3.RemoveStreamPrioritization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(31, 'RemoveStreamPrioritization', ()))
    IWMProfile3.CreateNewStreamPrioritization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMStreamPrioritization_head), use_last_error=False)(32, 'CreateNewStreamPrioritization', ((1, 'ppSP'),)))
    IWMProfile3.GetExpectedPacketCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt64), use_last_error=False)(33, 'GetExpectedPacketCount', ((1, 'msDuration'),(1, 'pcPackets'),)))
    return IWMProfile3
def _define_IWMStreamConfig_head():
    class IWMStreamConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bdc-2b2b-11d3-b36b-00c04f6108ff')
    return IWMStreamConfig
def _define_IWMStreamConfig():
    IWMStreamConfig = win32more.Media.WindowsMediaFormat.IWMStreamConfig_head
    IWMStreamConfig.GetStreamType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetStreamType', ((1, 'pguidStreamType'),)))
    IWMStreamConfig.GetStreamNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(4, 'GetStreamNumber', ((1, 'pwStreamNum'),)))
    IWMStreamConfig.SetStreamNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(5, 'SetStreamNumber', ((1, 'wStreamNum'),)))
    IWMStreamConfig.GetStreamName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(6, 'GetStreamName', ((1, 'pwszStreamName'),(1, 'pcchStreamName'),)))
    IWMStreamConfig.SetStreamName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetStreamName', ((1, 'pwszStreamName'),)))
    IWMStreamConfig.GetConnectionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(8, 'GetConnectionName', ((1, 'pwszInputName'),(1, 'pcchInputName'),)))
    IWMStreamConfig.SetConnectionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'SetConnectionName', ((1, 'pwszInputName'),)))
    IWMStreamConfig.GetBitrate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetBitrate', ((1, 'pdwBitrate'),)))
    IWMStreamConfig.SetBitrate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'SetBitrate', ((1, 'pdwBitrate'),)))
    IWMStreamConfig.GetBufferWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetBufferWindow', ((1, 'pmsBufferWindow'),)))
    IWMStreamConfig.SetBufferWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(13, 'SetBufferWindow', ((1, 'msBufferWindow'),)))
    return IWMStreamConfig
def _define_IWMStreamConfig2_head():
    class IWMStreamConfig2(win32more.Media.WindowsMediaFormat.IWMStreamConfig_head):
        Guid = Guid('7688d8cb-fc0d-43bd-9459-5a8dec200cfa')
    return IWMStreamConfig2
def _define_IWMStreamConfig2():
    IWMStreamConfig2 = win32more.Media.WindowsMediaFormat.IWMStreamConfig2_head
    IWMStreamConfig2.GetTransportType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE), use_last_error=False)(14, 'GetTransportType', ((1, 'pnTransportType'),)))
    IWMStreamConfig2.SetTransportType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_TRANSPORT_TYPE, use_last_error=False)(15, 'SetTransportType', ((1, 'nTransportType'),)))
    IWMStreamConfig2.AddDataUnitExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt16,POINTER(Byte),UInt32, use_last_error=False)(16, 'AddDataUnitExtension', ((1, 'guidExtensionSystemID'),(1, 'cbExtensionDataSize'),(1, 'pbExtensionSystemInfo'),(1, 'cbExtensionSystemInfo'),)))
    IWMStreamConfig2.GetDataUnitExtensionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(17, 'GetDataUnitExtensionCount', ((1, 'pcDataUnitExtensions'),)))
    IWMStreamConfig2.GetDataUnitExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Guid),POINTER(UInt16),POINTER(Byte),POINTER(UInt32), use_last_error=False)(18, 'GetDataUnitExtension', ((1, 'wDataUnitExtensionNumber'),(1, 'pguidExtensionSystemID'),(1, 'pcbExtensionDataSize'),(1, 'pbExtensionSystemInfo'),(1, 'pcbExtensionSystemInfo'),)))
    IWMStreamConfig2.RemoveAllDataUnitExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'RemoveAllDataUnitExtensions', ()))
    return IWMStreamConfig2
def _define_IWMStreamConfig3_head():
    class IWMStreamConfig3(win32more.Media.WindowsMediaFormat.IWMStreamConfig2_head):
        Guid = Guid('cb164104-3aa9-45a7-9ac9-4daee131d6e1')
    return IWMStreamConfig3
def _define_IWMStreamConfig3():
    IWMStreamConfig3 = win32more.Media.WindowsMediaFormat.IWMStreamConfig3_head
    IWMStreamConfig3.GetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(20, 'GetLanguage', ((1, 'pwszLanguageString'),(1, 'pcchLanguageStringLength'),)))
    IWMStreamConfig3.SetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(21, 'SetLanguage', ((1, 'pwszLanguageString'),)))
    return IWMStreamConfig3
def _define_IWMPacketSize_head():
    class IWMPacketSize(win32more.System.Com.IUnknown_head):
        Guid = Guid('cdfb97ab-188f-40b3-b643-5b7903975c59')
    return IWMPacketSize
def _define_IWMPacketSize():
    IWMPacketSize = win32more.Media.WindowsMediaFormat.IWMPacketSize_head
    IWMPacketSize.GetMaxPacketSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetMaxPacketSize', ((1, 'pdwMaxPacketSize'),)))
    IWMPacketSize.SetMaxPacketSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetMaxPacketSize', ((1, 'dwMaxPacketSize'),)))
    return IWMPacketSize
def _define_IWMPacketSize2_head():
    class IWMPacketSize2(win32more.Media.WindowsMediaFormat.IWMPacketSize_head):
        Guid = Guid('8bfc2b9e-b646-4233-a877-1c6a079669dc')
    return IWMPacketSize2
def _define_IWMPacketSize2():
    IWMPacketSize2 = win32more.Media.WindowsMediaFormat.IWMPacketSize2_head
    IWMPacketSize2.GetMinPacketSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetMinPacketSize', ((1, 'pdwMinPacketSize'),)))
    IWMPacketSize2.SetMinPacketSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetMinPacketSize', ((1, 'dwMinPacketSize'),)))
    return IWMPacketSize2
def _define_IWMStreamList_head():
    class IWMStreamList(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bdd-2b2b-11d3-b36b-00c04f6108ff')
    return IWMStreamList
def _define_IWMStreamList():
    IWMStreamList = win32more.Media.WindowsMediaFormat.IWMStreamList_head
    IWMStreamList.GetStreams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16), use_last_error=False)(3, 'GetStreams', ((1, 'pwStreamNumArray'),(1, 'pcStreams'),)))
    IWMStreamList.AddStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(4, 'AddStream', ((1, 'wStreamNum'),)))
    IWMStreamList.RemoveStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(5, 'RemoveStream', ((1, 'wStreamNum'),)))
    return IWMStreamList
def _define_IWMMutualExclusion_head():
    class IWMMutualExclusion(win32more.Media.WindowsMediaFormat.IWMStreamList_head):
        Guid = Guid('96406bde-2b2b-11d3-b36b-00c04f6108ff')
    return IWMMutualExclusion
def _define_IWMMutualExclusion():
    IWMMutualExclusion = win32more.Media.WindowsMediaFormat.IWMMutualExclusion_head
    IWMMutualExclusion.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'GetType', ((1, 'pguidType'),)))
    IWMMutualExclusion.SetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(7, 'SetType', ((1, 'guidType'),)))
    return IWMMutualExclusion
def _define_IWMMutualExclusion2_head():
    class IWMMutualExclusion2(win32more.Media.WindowsMediaFormat.IWMMutualExclusion_head):
        Guid = Guid('0302b57d-89d1-4ba2-85c9-166f2c53eb91')
    return IWMMutualExclusion2
def _define_IWMMutualExclusion2():
    IWMMutualExclusion2 = win32more.Media.WindowsMediaFormat.IWMMutualExclusion2_head
    IWMMutualExclusion2.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16), use_last_error=False)(8, 'GetName', ((1, 'pwszName'),(1, 'pcchName'),)))
    IWMMutualExclusion2.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'SetName', ((1, 'pwszName'),)))
    IWMMutualExclusion2.GetRecordCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(10, 'GetRecordCount', ((1, 'pwRecordCount'),)))
    IWMMutualExclusion2.AddRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'AddRecord', ()))
    IWMMutualExclusion2.RemoveRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(12, 'RemoveRecord', ((1, 'wRecordNumber'),)))
    IWMMutualExclusion2.GetRecordName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Char),POINTER(UInt16), use_last_error=False)(13, 'GetRecordName', ((1, 'wRecordNumber'),(1, 'pwszRecordName'),(1, 'pcchRecordName'),)))
    IWMMutualExclusion2.SetRecordName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR, use_last_error=False)(14, 'SetRecordName', ((1, 'wRecordNumber'),(1, 'pwszRecordName'),)))
    IWMMutualExclusion2.GetStreamsForRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16),POINTER(UInt16), use_last_error=False)(15, 'GetStreamsForRecord', ((1, 'wRecordNumber'),(1, 'pwStreamNumArray'),(1, 'pcStreams'),)))
    IWMMutualExclusion2.AddStreamForRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16, use_last_error=False)(16, 'AddStreamForRecord', ((1, 'wRecordNumber'),(1, 'wStreamNumber'),)))
    IWMMutualExclusion2.RemoveStreamForRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16, use_last_error=False)(17, 'RemoveStreamForRecord', ((1, 'wRecordNumber'),(1, 'wStreamNumber'),)))
    return IWMMutualExclusion2
def _define_IWMBandwidthSharing_head():
    class IWMBandwidthSharing(win32more.Media.WindowsMediaFormat.IWMStreamList_head):
        Guid = Guid('ad694af1-f8d9-42f8-bc47-70311b0c4f9e')
    return IWMBandwidthSharing
def _define_IWMBandwidthSharing():
    IWMBandwidthSharing = win32more.Media.WindowsMediaFormat.IWMBandwidthSharing_head
    IWMBandwidthSharing.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'GetType', ((1, 'pguidType'),)))
    IWMBandwidthSharing.SetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(7, 'SetType', ((1, 'guidType'),)))
    IWMBandwidthSharing.GetBandwidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'GetBandwidth', ((1, 'pdwBitrate'),(1, 'pmsBufferWindow'),)))
    IWMBandwidthSharing.SetBandwidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(9, 'SetBandwidth', ((1, 'dwBitrate'),(1, 'msBufferWindow'),)))
    return IWMBandwidthSharing
def _define_IWMStreamPrioritization_head():
    class IWMStreamPrioritization(win32more.System.Com.IUnknown_head):
        Guid = Guid('8c1c6090-f9a8-4748-8ec3-dd1108ba1e77')
    return IWMStreamPrioritization
def _define_IWMStreamPrioritization():
    IWMStreamPrioritization = win32more.Media.WindowsMediaFormat.IWMStreamPrioritization_head
    IWMStreamPrioritization.GetPriorityRecords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_STREAM_PRIORITY_RECORD),POINTER(UInt16), use_last_error=False)(3, 'GetPriorityRecords', ((1, 'pRecordArray'),(1, 'pcRecords'),)))
    IWMStreamPrioritization.SetPriorityRecords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_STREAM_PRIORITY_RECORD_head),UInt16, use_last_error=False)(4, 'SetPriorityRecords', ((1, 'pRecordArray'),(1, 'cRecords'),)))
    return IWMStreamPrioritization
def _define_IWMWriterAdvanced_head():
    class IWMWriterAdvanced(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406be3-2b2b-11d3-b36b-00c04f6108ff')
    return IWMWriterAdvanced
def _define_IWMWriterAdvanced():
    IWMWriterAdvanced = win32more.Media.WindowsMediaFormat.IWMWriterAdvanced_head
    IWMWriterAdvanced.GetSinkCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetSinkCount', ((1, 'pcSinks'),)))
    IWMWriterAdvanced.GetSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMWriterSink_head), use_last_error=False)(4, 'GetSink', ((1, 'dwSinkNum'),(1, 'ppSink'),)))
    IWMWriterAdvanced.AddSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMWriterSink_head, use_last_error=False)(5, 'AddSink', ((1, 'pSink'),)))
    IWMWriterAdvanced.RemoveSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMWriterSink_head, use_last_error=False)(6, 'RemoveSink', ((1, 'pSink'),)))
    IWMWriterAdvanced.WriteStreamSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt64,UInt32,UInt64,UInt32,win32more.Media.WindowsMediaFormat.INSSBuffer_head, use_last_error=False)(7, 'WriteStreamSample', ((1, 'wStreamNum'),(1, 'cnsSampleTime'),(1, 'msSampleSendTime'),(1, 'cnsSampleDuration'),(1, 'dwFlags'),(1, 'pSample'),)))
    IWMWriterAdvanced.SetLiveSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(8, 'SetLiveSource', ((1, 'fIsLiveSource'),)))
    IWMWriterAdvanced.IsRealTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'IsRealTime', ((1, 'pfRealTime'),)))
    IWMWriterAdvanced.GetWriterTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(10, 'GetWriterTime', ((1, 'pcnsCurrentTime'),)))
    IWMWriterAdvanced.GetStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.WM_WRITER_STATISTICS_head), use_last_error=False)(11, 'GetStatistics', ((1, 'wStreamNum'),(1, 'pStats'),)))
    IWMWriterAdvanced.SetSyncTolerance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'SetSyncTolerance', ((1, 'msWindow'),)))
    IWMWriterAdvanced.GetSyncTolerance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'GetSyncTolerance', ((1, 'pmsWindow'),)))
    return IWMWriterAdvanced
def _define_IWMWriterAdvanced2_head():
    class IWMWriterAdvanced2(win32more.Media.WindowsMediaFormat.IWMWriterAdvanced_head):
        Guid = Guid('962dc1ec-c046-4db8-9cc7-26ceae500817')
    return IWMWriterAdvanced2
def _define_IWMWriterAdvanced2():
    IWMWriterAdvanced2 = win32more.Media.WindowsMediaFormat.IWMWriterAdvanced2_head
    IWMWriterAdvanced2.GetInputSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(14, 'GetInputSetting', ((1, 'dwInputNum'),(1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMWriterAdvanced2.SetInputSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt16, use_last_error=False)(15, 'SetInputSetting', ((1, 'dwInputNum'),(1, 'pszName'),(1, 'Type'),(1, 'pValue'),(1, 'cbLength'),)))
    return IWMWriterAdvanced2
def _define_IWMWriterAdvanced3_head():
    class IWMWriterAdvanced3(win32more.Media.WindowsMediaFormat.IWMWriterAdvanced2_head):
        Guid = Guid('2cd6492d-7c37-4e76-9d3b-59261183a22e')
    return IWMWriterAdvanced3
def _define_IWMWriterAdvanced3():
    IWMWriterAdvanced3 = win32more.Media.WindowsMediaFormat.IWMWriterAdvanced3_head
    IWMWriterAdvanced3.GetStatisticsEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.WM_WRITER_STATISTICS_EX_head), use_last_error=False)(16, 'GetStatisticsEx', ((1, 'wStreamNum'),(1, 'pStats'),)))
    IWMWriterAdvanced3.SetNonBlocking = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'SetNonBlocking', ()))
    return IWMWriterAdvanced3
def _define_IWMWriterPreprocess_head():
    class IWMWriterPreprocess(win32more.System.Com.IUnknown_head):
        Guid = Guid('fc54a285-38c4-45b5-aa23-85b9f7cb424b')
    return IWMWriterPreprocess
def _define_IWMWriterPreprocess():
    IWMWriterPreprocess = win32more.Media.WindowsMediaFormat.IWMWriterPreprocess_head
    IWMWriterPreprocess.GetMaxPreprocessingPasses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(3, 'GetMaxPreprocessingPasses', ((1, 'dwInputNum'),(1, 'dwFlags'),(1, 'pdwMaxNumPasses'),)))
    IWMWriterPreprocess.SetNumPreprocessingPasses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(4, 'SetNumPreprocessingPasses', ((1, 'dwInputNum'),(1, 'dwFlags'),(1, 'dwNumPasses'),)))
    IWMWriterPreprocess.BeginPreprocessingPass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(5, 'BeginPreprocessingPass', ((1, 'dwInputNum'),(1, 'dwFlags'),)))
    IWMWriterPreprocess.PreprocessSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,UInt32,win32more.Media.WindowsMediaFormat.INSSBuffer_head, use_last_error=False)(6, 'PreprocessSample', ((1, 'dwInputNum'),(1, 'cnsSampleTime'),(1, 'dwFlags'),(1, 'pSample'),)))
    IWMWriterPreprocess.EndPreprocessingPass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(7, 'EndPreprocessingPass', ((1, 'dwInputNum'),(1, 'dwFlags'),)))
    return IWMWriterPreprocess
def _define_IWMWriterPostViewCallback_head():
    class IWMWriterPostViewCallback(win32more.Media.WindowsMediaFormat.IWMStatusCallback_head):
        Guid = Guid('d9d6549d-a193-4f24-b308-03123d9b7f8d')
    return IWMWriterPostViewCallback
def _define_IWMWriterPostViewCallback():
    IWMWriterPostViewCallback = win32more.Media.WindowsMediaFormat.IWMWriterPostViewCallback_head
    IWMWriterPostViewCallback.OnPostViewSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt64,UInt64,UInt32,win32more.Media.WindowsMediaFormat.INSSBuffer_head,c_void_p, use_last_error=False)(4, 'OnPostViewSample', ((1, 'wStreamNumber'),(1, 'cnsSampleTime'),(1, 'cnsSampleDuration'),(1, 'dwFlags'),(1, 'pSample'),(1, 'pvContext'),)))
    IWMWriterPostViewCallback.AllocateForPostView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),c_void_p, use_last_error=False)(5, 'AllocateForPostView', ((1, 'wStreamNum'),(1, 'cbBuffer'),(1, 'ppBuffer'),(1, 'pvContext'),)))
    return IWMWriterPostViewCallback
def _define_IWMWriterPostView_head():
    class IWMWriterPostView(win32more.System.Com.IUnknown_head):
        Guid = Guid('81e20ce4-75ef-491a-8004-fc53c45bdc3e')
    return IWMWriterPostView
def _define_IWMWriterPostView():
    IWMWriterPostView = win32more.Media.WindowsMediaFormat.IWMWriterPostView_head
    IWMWriterPostView.SetPostViewCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMWriterPostViewCallback_head,c_void_p, use_last_error=False)(3, 'SetPostViewCallback', ((1, 'pCallback'),(1, 'pvContext'),)))
    IWMWriterPostView.SetReceivePostViewSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.BOOL, use_last_error=False)(4, 'SetReceivePostViewSamples', ((1, 'wStreamNum'),(1, 'fReceivePostViewSamples'),)))
    IWMWriterPostView.GetReceivePostViewSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'GetReceivePostViewSamples', ((1, 'wStreamNum'),(1, 'pfReceivePostViewSamples'),)))
    IWMWriterPostView.GetPostViewProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.IWMMediaProps_head), use_last_error=False)(6, 'GetPostViewProps', ((1, 'wStreamNumber'),(1, 'ppOutput'),)))
    IWMWriterPostView.SetPostViewProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Media.WindowsMediaFormat.IWMMediaProps_head, use_last_error=False)(7, 'SetPostViewProps', ((1, 'wStreamNumber'),(1, 'pOutput'),)))
    IWMWriterPostView.GetPostViewFormatCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt32), use_last_error=False)(8, 'GetPostViewFormatCount', ((1, 'wStreamNumber'),(1, 'pcFormats'),)))
    IWMWriterPostView.GetPostViewFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMMediaProps_head), use_last_error=False)(9, 'GetPostViewFormat', ((1, 'wStreamNumber'),(1, 'dwFormatNumber'),(1, 'ppProps'),)))
    IWMWriterPostView.SetAllocateForPostView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.BOOL, use_last_error=False)(10, 'SetAllocateForPostView', ((1, 'wStreamNumber'),(1, 'fAllocate'),)))
    IWMWriterPostView.GetAllocateForPostView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'GetAllocateForPostView', ((1, 'wStreamNumber'),(1, 'pfAllocate'),)))
    return IWMWriterPostView
def _define_IWMWriterSink_head():
    class IWMWriterSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406be4-2b2b-11d3-b36b-00c04f6108ff')
    return IWMWriterSink
def _define_IWMWriterSink():
    IWMWriterSink = win32more.Media.WindowsMediaFormat.IWMWriterSink_head
    IWMWriterSink.OnHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.INSSBuffer_head, use_last_error=False)(3, 'OnHeader', ((1, 'pHeader'),)))
    IWMWriterSink.IsRealTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'IsRealTime', ((1, 'pfRealTime'),)))
    IWMWriterSink.AllocateDataUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head), use_last_error=False)(5, 'AllocateDataUnit', ((1, 'cbDataUnit'),(1, 'ppDataUnit'),)))
    IWMWriterSink.OnDataUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.INSSBuffer_head, use_last_error=False)(6, 'OnDataUnit', ((1, 'pDataUnit'),)))
    IWMWriterSink.OnEndWriting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'OnEndWriting', ()))
    return IWMWriterSink
def _define_IWMRegisterCallback_head():
    class IWMRegisterCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('cf4b1f99-4de2-4e49-a363-252740d99bc1')
    return IWMRegisterCallback
def _define_IWMRegisterCallback():
    IWMRegisterCallback = win32more.Media.WindowsMediaFormat.IWMRegisterCallback_head
    IWMRegisterCallback.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMStatusCallback_head,c_void_p, use_last_error=False)(3, 'Advise', ((1, 'pCallback'),(1, 'pvContext'),)))
    IWMRegisterCallback.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMStatusCallback_head,c_void_p, use_last_error=False)(4, 'Unadvise', ((1, 'pCallback'),(1, 'pvContext'),)))
    return IWMRegisterCallback
def _define_IWMWriterFileSink_head():
    class IWMWriterFileSink(win32more.Media.WindowsMediaFormat.IWMWriterSink_head):
        Guid = Guid('96406be5-2b2b-11d3-b36b-00c04f6108ff')
    return IWMWriterFileSink
def _define_IWMWriterFileSink():
    IWMWriterFileSink = win32more.Media.WindowsMediaFormat.IWMWriterFileSink_head
    IWMWriterFileSink.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'Open', ((1, 'pwszFilename'),)))
    return IWMWriterFileSink
def _define_IWMWriterFileSink2_head():
    class IWMWriterFileSink2(win32more.Media.WindowsMediaFormat.IWMWriterFileSink_head):
        Guid = Guid('14282ba7-4aef-4205-8ce5-c229035a05bc')
    return IWMWriterFileSink2
def _define_IWMWriterFileSink2():
    IWMWriterFileSink2 = win32more.Media.WindowsMediaFormat.IWMWriterFileSink2_head
    IWMWriterFileSink2.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(9, 'Start', ((1, 'cnsStartTime'),)))
    IWMWriterFileSink2.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(10, 'Stop', ((1, 'cnsStopTime'),)))
    IWMWriterFileSink2.IsStopped = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'IsStopped', ((1, 'pfStopped'),)))
    IWMWriterFileSink2.GetFileDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(12, 'GetFileDuration', ((1, 'pcnsDuration'),)))
    IWMWriterFileSink2.GetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(13, 'GetFileSize', ((1, 'pcbFile'),)))
    IWMWriterFileSink2.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Close', ()))
    IWMWriterFileSink2.IsClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'IsClosed', ((1, 'pfClosed'),)))
    return IWMWriterFileSink2
def _define_IWMWriterFileSink3_head():
    class IWMWriterFileSink3(win32more.Media.WindowsMediaFormat.IWMWriterFileSink2_head):
        Guid = Guid('3fea4feb-2945-47a7-a1dd-c53a8fc4c45c')
    return IWMWriterFileSink3
def _define_IWMWriterFileSink3():
    IWMWriterFileSink3 = win32more.Media.WindowsMediaFormat.IWMWriterFileSink3_head
    IWMWriterFileSink3.SetAutoIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(16, 'SetAutoIndexing', ((1, 'fDoAutoIndexing'),)))
    IWMWriterFileSink3.GetAutoIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'GetAutoIndexing', ((1, 'pfAutoIndexing'),)))
    IWMWriterFileSink3.SetControlStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.BOOL, use_last_error=False)(18, 'SetControlStream', ((1, 'wStreamNumber'),(1, 'fShouldControlStartAndStop'),)))
    IWMWriterFileSink3.GetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(19, 'GetMode', ((1, 'pdwFileSinkMode'),)))
    IWMWriterFileSink3.OnDataUnitEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMT_FILESINK_DATA_UNIT_head), use_last_error=False)(20, 'OnDataUnitEx', ((1, 'pFileSinkDataUnit'),)))
    IWMWriterFileSink3.SetUnbufferedIO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(21, 'SetUnbufferedIO', ((1, 'fUnbufferedIO'),(1, 'fRestrictMemUsage'),)))
    IWMWriterFileSink3.GetUnbufferedIO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(22, 'GetUnbufferedIO', ((1, 'pfUnbufferedIO'),)))
    IWMWriterFileSink3.CompleteOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'CompleteOperations', ()))
    return IWMWriterFileSink3
def _define_IWMWriterNetworkSink_head():
    class IWMWriterNetworkSink(win32more.Media.WindowsMediaFormat.IWMWriterSink_head):
        Guid = Guid('96406be7-2b2b-11d3-b36b-00c04f6108ff')
    return IWMWriterNetworkSink
def _define_IWMWriterNetworkSink():
    IWMWriterNetworkSink = win32more.Media.WindowsMediaFormat.IWMWriterNetworkSink_head
    IWMWriterNetworkSink.SetMaximumClients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'SetMaximumClients', ((1, 'dwMaxClients'),)))
    IWMWriterNetworkSink.GetMaximumClients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetMaximumClients', ((1, 'pdwMaxClients'),)))
    IWMWriterNetworkSink.SetNetworkProtocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_NET_PROTOCOL, use_last_error=False)(10, 'SetNetworkProtocol', ((1, 'protocol'),)))
    IWMWriterNetworkSink.GetNetworkProtocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMT_NET_PROTOCOL), use_last_error=False)(11, 'GetNetworkProtocol', ((1, 'pProtocol'),)))
    IWMWriterNetworkSink.GetHostURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(12, 'GetHostURL', ((1, 'pwszURL'),(1, 'pcchURL'),)))
    IWMWriterNetworkSink.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'Open', ((1, 'pdwPortNum'),)))
    IWMWriterNetworkSink.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Disconnect', ()))
    IWMWriterNetworkSink.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Close', ()))
    return IWMWriterNetworkSink
def _define_IWMClientConnections_head():
    class IWMClientConnections(win32more.System.Com.IUnknown_head):
        Guid = Guid('73c66010-a299-41df-b1f0-ccf03b09c1c6')
    return IWMClientConnections
def _define_IWMClientConnections():
    IWMClientConnections = win32more.Media.WindowsMediaFormat.IWMClientConnections_head
    IWMClientConnections.GetClientCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetClientCount', ((1, 'pcClients'),)))
    IWMClientConnections.GetClientProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.WM_CLIENT_PROPERTIES_head), use_last_error=False)(4, 'GetClientProperties', ((1, 'dwClientNum'),(1, 'pClientProperties'),)))
    return IWMClientConnections
def _define_IWMClientConnections2_head():
    class IWMClientConnections2(win32more.Media.WindowsMediaFormat.IWMClientConnections_head):
        Guid = Guid('4091571e-4701-4593-bb3d-d5f5f0c74246')
    return IWMClientConnections2
def _define_IWMClientConnections2():
    IWMClientConnections2 = win32more.Media.WindowsMediaFormat.IWMClientConnections2_head
    IWMClientConnections2.GetClientInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32), use_last_error=False)(5, 'GetClientInfo', ((1, 'dwClientNum'),(1, 'pwszNetworkAddress'),(1, 'pcchNetworkAddress'),(1, 'pwszPort'),(1, 'pcchPort'),(1, 'pwszDNSName'),(1, 'pcchDNSName'),)))
    return IWMClientConnections2
def _define_IWMReaderAdvanced_head():
    class IWMReaderAdvanced(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bea-2b2b-11d3-b36b-00c04f6108ff')
    return IWMReaderAdvanced
def _define_IWMReaderAdvanced():
    IWMReaderAdvanced = win32more.Media.WindowsMediaFormat.IWMReaderAdvanced_head
    IWMReaderAdvanced.SetUserProvidedClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(3, 'SetUserProvidedClock', ((1, 'fUserClock'),)))
    IWMReaderAdvanced.GetUserProvidedClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetUserProvidedClock', ((1, 'pfUserClock'),)))
    IWMReaderAdvanced.DeliverTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(5, 'DeliverTime', ((1, 'cnsTime'),)))
    IWMReaderAdvanced.SetManualStreamSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'SetManualStreamSelection', ((1, 'fSelection'),)))
    IWMReaderAdvanced.GetManualStreamSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'GetManualStreamSelection', ((1, 'pfSelection'),)))
    IWMReaderAdvanced.SetStreamsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16),POINTER(win32more.Media.WindowsMediaFormat.WMT_STREAM_SELECTION), use_last_error=False)(8, 'SetStreamsSelected', ((1, 'cStreamCount'),(1, 'pwStreamNumbers'),(1, 'pSelections'),)))
    IWMReaderAdvanced.GetStreamSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.WindowsMediaFormat.WMT_STREAM_SELECTION), use_last_error=False)(9, 'GetStreamSelected', ((1, 'wStreamNum'),(1, 'pSelection'),)))
    IWMReaderAdvanced.SetReceiveSelectionCallbacks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'SetReceiveSelectionCallbacks', ((1, 'fGetCallbacks'),)))
    IWMReaderAdvanced.GetReceiveSelectionCallbacks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'GetReceiveSelectionCallbacks', ((1, 'pfGetCallbacks'),)))
    IWMReaderAdvanced.SetReceiveStreamSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.BOOL, use_last_error=False)(12, 'SetReceiveStreamSamples', ((1, 'wStreamNum'),(1, 'fReceiveStreamSamples'),)))
    IWMReaderAdvanced.GetReceiveStreamSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'GetReceiveStreamSamples', ((1, 'wStreamNum'),(1, 'pfReceiveStreamSamples'),)))
    IWMReaderAdvanced.SetAllocateForOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL, use_last_error=False)(14, 'SetAllocateForOutput', ((1, 'dwOutputNum'),(1, 'fAllocate'),)))
    IWMReaderAdvanced.GetAllocateForOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'GetAllocateForOutput', ((1, 'dwOutputNum'),(1, 'pfAllocate'),)))
    IWMReaderAdvanced.SetAllocateForStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.BOOL, use_last_error=False)(16, 'SetAllocateForStream', ((1, 'wStreamNum'),(1, 'fAllocate'),)))
    IWMReaderAdvanced.GetAllocateForStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'GetAllocateForStream', ((1, 'dwSreamNum'),(1, 'pfAllocate'),)))
    IWMReaderAdvanced.GetStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_READER_STATISTICS_head), use_last_error=False)(18, 'GetStatistics', ((1, 'pStatistics'),)))
    IWMReaderAdvanced.SetClientInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_READER_CLIENTINFO_head), use_last_error=False)(19, 'SetClientInfo', ((1, 'pClientInfo'),)))
    IWMReaderAdvanced.GetMaxOutputSampleSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(20, 'GetMaxOutputSampleSize', ((1, 'dwOutput'),(1, 'pcbMax'),)))
    IWMReaderAdvanced.GetMaxStreamSampleSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt32), use_last_error=False)(21, 'GetMaxStreamSampleSize', ((1, 'wStream'),(1, 'pcbMax'),)))
    IWMReaderAdvanced.NotifyLateDelivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(22, 'NotifyLateDelivery', ((1, 'cnsLateness'),)))
    return IWMReaderAdvanced
def _define_IWMReaderAdvanced2_head():
    class IWMReaderAdvanced2(win32more.Media.WindowsMediaFormat.IWMReaderAdvanced_head):
        Guid = Guid('ae14a945-b90c-4d0d-9127-80d665f7d73e')
    return IWMReaderAdvanced2
def _define_IWMReaderAdvanced2():
    IWMReaderAdvanced2 = win32more.Media.WindowsMediaFormat.IWMReaderAdvanced2_head
    IWMReaderAdvanced2.SetPlayMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_PLAY_MODE, use_last_error=False)(23, 'SetPlayMode', ((1, 'Mode'),)))
    IWMReaderAdvanced2.GetPlayMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WMT_PLAY_MODE), use_last_error=False)(24, 'GetPlayMode', ((1, 'pMode'),)))
    IWMReaderAdvanced2.GetBufferProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt64), use_last_error=False)(25, 'GetBufferProgress', ((1, 'pdwPercent'),(1, 'pcnsBuffering'),)))
    IWMReaderAdvanced2.GetDownloadProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt64),POINTER(UInt64), use_last_error=False)(26, 'GetDownloadProgress', ((1, 'pdwPercent'),(1, 'pqwBytesDownloaded'),(1, 'pcnsDownload'),)))
    IWMReaderAdvanced2.GetSaveAsProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(27, 'GetSaveAsProgress', ((1, 'pdwPercent'),)))
    IWMReaderAdvanced2.SaveFileAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(28, 'SaveFileAs', ((1, 'pwszFilename'),)))
    IWMReaderAdvanced2.GetProtocolName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32), use_last_error=False)(29, 'GetProtocolName', ((1, 'pwszProtocol'),(1, 'pcchProtocol'),)))
    IWMReaderAdvanced2.StartAtMarker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt64,Single,c_void_p, use_last_error=False)(30, 'StartAtMarker', ((1, 'wMarkerIndex'),(1, 'cnsDuration'),(1, 'fRate'),(1, 'pvContext'),)))
    IWMReaderAdvanced2.GetOutputSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(31, 'GetOutputSetting', ((1, 'dwOutputNum'),(1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMReaderAdvanced2.SetOutputSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt16, use_last_error=False)(32, 'SetOutputSetting', ((1, 'dwOutputNum'),(1, 'pszName'),(1, 'Type'),(1, 'pValue'),(1, 'cbLength'),)))
    IWMReaderAdvanced2.Preroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,Single, use_last_error=False)(33, 'Preroll', ((1, 'cnsStart'),(1, 'cnsDuration'),(1, 'fRate'),)))
    IWMReaderAdvanced2.SetLogClientID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(34, 'SetLogClientID', ((1, 'fLogClientID'),)))
    IWMReaderAdvanced2.GetLogClientID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(35, 'GetLogClientID', ((1, 'pfLogClientID'),)))
    IWMReaderAdvanced2.StopBuffering = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(36, 'StopBuffering', ()))
    IWMReaderAdvanced2.OpenStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Media.WindowsMediaFormat.IWMReaderCallback_head,c_void_p, use_last_error=False)(37, 'OpenStream', ((1, 'pStream'),(1, 'pCallback'),(1, 'pvContext'),)))
    return IWMReaderAdvanced2
def _define_IWMReaderAdvanced3_head():
    class IWMReaderAdvanced3(win32more.Media.WindowsMediaFormat.IWMReaderAdvanced2_head):
        Guid = Guid('5dc0674b-f04b-4a4e-9f2a-b1afde2c8100')
    return IWMReaderAdvanced3
def _define_IWMReaderAdvanced3():
    IWMReaderAdvanced3 = win32more.Media.WindowsMediaFormat.IWMReaderAdvanced3_head
    IWMReaderAdvanced3.StopNetStreaming = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(38, 'StopNetStreaming', ()))
    IWMReaderAdvanced3.StartAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,c_void_p,c_void_p,win32more.Media.WindowsMediaFormat.WMT_OFFSET_FORMAT,Single,c_void_p, use_last_error=False)(39, 'StartAtPosition', ((1, 'wStreamNum'),(1, 'pvOffsetStart'),(1, 'pvDuration'),(1, 'dwOffsetFormat'),(1, 'fRate'),(1, 'pvContext'),)))
    return IWMReaderAdvanced3
def _define_IWMReaderAdvanced4_head():
    class IWMReaderAdvanced4(win32more.Media.WindowsMediaFormat.IWMReaderAdvanced3_head):
        Guid = Guid('945a76a2-12ae-4d48-bd3c-cd1d90399b85')
    return IWMReaderAdvanced4
def _define_IWMReaderAdvanced4():
    IWMReaderAdvanced4 = win32more.Media.WindowsMediaFormat.IWMReaderAdvanced4_head
    IWMReaderAdvanced4.GetLanguageCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16), use_last_error=False)(40, 'GetLanguageCount', ((1, 'dwOutputNum'),(1, 'pwLanguageCount'),)))
    IWMReaderAdvanced4.GetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Char),POINTER(UInt16), use_last_error=False)(41, 'GetLanguage', ((1, 'dwOutputNum'),(1, 'wLanguage'),(1, 'pwszLanguageString'),(1, 'pcchLanguageStringLength'),)))
    IWMReaderAdvanced4.GetMaxSpeedFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(42, 'GetMaxSpeedFactor', ((1, 'pdblFactor'),)))
    IWMReaderAdvanced4.IsUsingFastCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(43, 'IsUsingFastCache', ((1, 'pfUsingFastCache'),)))
    IWMReaderAdvanced4.AddLogParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(44, 'AddLogParam', ((1, 'wszNameSpace'),(1, 'wszName'),(1, 'wszValue'),)))
    IWMReaderAdvanced4.SendLogParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(45, 'SendLogParams', ()))
    IWMReaderAdvanced4.CanSaveFileAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(46, 'CanSaveFileAs', ((1, 'pfCanSave'),)))
    IWMReaderAdvanced4.CancelSaveFileAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(47, 'CancelSaveFileAs', ()))
    IWMReaderAdvanced4.GetURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32), use_last_error=False)(48, 'GetURL', ((1, 'pwszURL'),(1, 'pcchURL'),)))
    return IWMReaderAdvanced4
def _define_IWMReaderAdvanced5_head():
    class IWMReaderAdvanced5(win32more.Media.WindowsMediaFormat.IWMReaderAdvanced4_head):
        Guid = Guid('24c44db0-55d1-49ae-a5cc-f13815e36363')
    return IWMReaderAdvanced5
def _define_IWMReaderAdvanced5():
    IWMReaderAdvanced5 = win32more.Media.WindowsMediaFormat.IWMReaderAdvanced5_head
    IWMReaderAdvanced5.SetPlayerHook = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMPlayerHook_head, use_last_error=False)(49, 'SetPlayerHook', ((1, 'dwOutputNum'),(1, 'pHook'),)))
    return IWMReaderAdvanced5
def _define_IWMReaderAdvanced6_head():
    class IWMReaderAdvanced6(win32more.Media.WindowsMediaFormat.IWMReaderAdvanced5_head):
        Guid = Guid('18a2e7f8-428f-4acd-8a00-e64639bc93de')
    return IWMReaderAdvanced6
def _define_IWMReaderAdvanced6():
    IWMReaderAdvanced6 = win32more.Media.WindowsMediaFormat.IWMReaderAdvanced6_head
    IWMReaderAdvanced6.SetProtectStreamSamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,UInt32,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(50, 'SetProtectStreamSamples', ((1, 'pbCertificate'),(1, 'cbCertificate'),(1, 'dwCertificateType'),(1, 'dwFlags'),(1, 'pbInitializationVector'),(1, 'pcbInitializationVector'),)))
    return IWMReaderAdvanced6
def _define_IWMPlayerHook_head():
    class IWMPlayerHook(win32more.System.Com.IUnknown_head):
        Guid = Guid('e5b7ca9a-0f1c-4f66-9002-74ec50d8b304')
    return IWMPlayerHook
def _define_IWMPlayerHook():
    IWMPlayerHook = win32more.Media.WindowsMediaFormat.IWMPlayerHook_head
    IWMPlayerHook.PreDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'PreDecode', ()))
    return IWMPlayerHook
def _define_IWMReaderAllocatorEx_head():
    class IWMReaderAllocatorEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f762fa7-a22e-428d-93c9-ac82f3aafe5a')
    return IWMReaderAllocatorEx
def _define_IWMReaderAllocatorEx():
    IWMReaderAllocatorEx = win32more.Media.WindowsMediaFormat.IWMReaderAllocatorEx_head
    IWMReaderAllocatorEx.AllocateForStreamEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),UInt32,UInt64,UInt64,c_void_p, use_last_error=False)(3, 'AllocateForStreamEx', ((1, 'wStreamNum'),(1, 'cbBuffer'),(1, 'ppBuffer'),(1, 'dwFlags'),(1, 'cnsSampleTime'),(1, 'cnsSampleDuration'),(1, 'pvContext'),)))
    IWMReaderAllocatorEx.AllocateForOutputEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),UInt32,UInt64,UInt64,c_void_p, use_last_error=False)(4, 'AllocateForOutputEx', ((1, 'dwOutputNum'),(1, 'cbBuffer'),(1, 'ppBuffer'),(1, 'dwFlags'),(1, 'cnsSampleTime'),(1, 'cnsSampleDuration'),(1, 'pvContext'),)))
    return IWMReaderAllocatorEx
def _define_IWMReaderTypeNegotiation_head():
    class IWMReaderTypeNegotiation(win32more.System.Com.IUnknown_head):
        Guid = Guid('fdbe5592-81a1-41ea-93bd-735cad1adc05')
    return IWMReaderTypeNegotiation
def _define_IWMReaderTypeNegotiation():
    IWMReaderTypeNegotiation = win32more.Media.WindowsMediaFormat.IWMReaderTypeNegotiation_head
    IWMReaderTypeNegotiation.TryOutputProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMOutputMediaProps_head, use_last_error=False)(3, 'TryOutputProps', ((1, 'dwOutputNum'),(1, 'pOutput'),)))
    return IWMReaderTypeNegotiation
def _define_IWMReaderCallbackAdvanced_head():
    class IWMReaderCallbackAdvanced(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406beb-2b2b-11d3-b36b-00c04f6108ff')
    return IWMReaderCallbackAdvanced
def _define_IWMReaderCallbackAdvanced():
    IWMReaderCallbackAdvanced = win32more.Media.WindowsMediaFormat.IWMReaderCallbackAdvanced_head
    IWMReaderCallbackAdvanced.OnStreamSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt64,UInt64,UInt32,win32more.Media.WindowsMediaFormat.INSSBuffer_head,c_void_p, use_last_error=False)(3, 'OnStreamSample', ((1, 'wStreamNum'),(1, 'cnsSampleTime'),(1, 'cnsSampleDuration'),(1, 'dwFlags'),(1, 'pSample'),(1, 'pvContext'),)))
    IWMReaderCallbackAdvanced.OnTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,c_void_p, use_last_error=False)(4, 'OnTime', ((1, 'cnsCurrentTime'),(1, 'pvContext'),)))
    IWMReaderCallbackAdvanced.OnStreamSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16),POINTER(win32more.Media.WindowsMediaFormat.WMT_STREAM_SELECTION),c_void_p, use_last_error=False)(5, 'OnStreamSelection', ((1, 'wStreamCount'),(1, 'pStreamNumbers'),(1, 'pSelections'),(1, 'pvContext'),)))
    IWMReaderCallbackAdvanced.OnOutputPropsChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head),c_void_p, use_last_error=False)(6, 'OnOutputPropsChanged', ((1, 'dwOutputNum'),(1, 'pMediaType'),(1, 'pvContext'),)))
    IWMReaderCallbackAdvanced.AllocateForStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),c_void_p, use_last_error=False)(7, 'AllocateForStream', ((1, 'wStreamNum'),(1, 'cbBuffer'),(1, 'ppBuffer'),(1, 'pvContext'),)))
    IWMReaderCallbackAdvanced.AllocateForOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),c_void_p, use_last_error=False)(8, 'AllocateForOutput', ((1, 'dwOutputNum'),(1, 'cbBuffer'),(1, 'ppBuffer'),(1, 'pvContext'),)))
    return IWMReaderCallbackAdvanced
def _define_IWMDRMReader_head():
    class IWMDRMReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2827540-3ee7-432c-b14c-dc17f085d3b3')
    return IWMDRMReader
def _define_IWMDRMReader():
    IWMDRMReader = win32more.Media.WindowsMediaFormat.IWMDRMReader_head
    IWMDRMReader.AcquireLicense = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'AcquireLicense', ((1, 'dwFlags'),)))
    IWMDRMReader.CancelLicenseAcquisition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'CancelLicenseAcquisition', ()))
    IWMDRMReader.Individualize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Individualize', ((1, 'dwFlags'),)))
    IWMDRMReader.CancelIndividualization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'CancelIndividualization', ()))
    IWMDRMReader.MonitorLicenseAcquisition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'MonitorLicenseAcquisition', ()))
    IWMDRMReader.CancelMonitorLicenseAcquisition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'CancelMonitorLicenseAcquisition', ()))
    IWMDRMReader.SetDRMProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt16, use_last_error=False)(9, 'SetDRMProperty', ((1, 'pwstrName'),(1, 'dwType'),(1, 'pValue'),(1, 'cbLength'),)))
    IWMDRMReader.GetDRMProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(10, 'GetDRMProperty', ((1, 'pwstrName'),(1, 'pdwType'),(1, 'pValue'),(1, 'pcbLength'),)))
    return IWMDRMReader
def _define_DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS_head():
    class DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS(Structure):
        pass
    return DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS
def _define_DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS():
    DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS = win32more.Media.WindowsMediaFormat.DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS_head
    DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS._fields_ = [
        ("wCompressedDigitalVideo", UInt16),
        ("wUncompressedDigitalVideo", UInt16),
        ("wAnalogVideo", UInt16),
        ("wCompressedDigitalAudio", UInt16),
        ("wUncompressedDigitalAudio", UInt16),
    ]
    return DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS
def _define_DRM_OPL_OUTPUT_IDS_head():
    class DRM_OPL_OUTPUT_IDS(Structure):
        pass
    return DRM_OPL_OUTPUT_IDS
def _define_DRM_OPL_OUTPUT_IDS():
    DRM_OPL_OUTPUT_IDS = win32more.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS_head
    DRM_OPL_OUTPUT_IDS._fields_ = [
        ("cIds", UInt16),
        ("rgIds", POINTER(Guid)),
    ]
    return DRM_OPL_OUTPUT_IDS
def _define_DRM_OUTPUT_PROTECTION_head():
    class DRM_OUTPUT_PROTECTION(Structure):
        pass
    return DRM_OUTPUT_PROTECTION
def _define_DRM_OUTPUT_PROTECTION():
    DRM_OUTPUT_PROTECTION = win32more.Media.WindowsMediaFormat.DRM_OUTPUT_PROTECTION_head
    DRM_OUTPUT_PROTECTION._fields_ = [
        ("guidId", Guid),
        ("bConfigData", Byte),
    ]
    return DRM_OUTPUT_PROTECTION
def _define_DRM_VIDEO_OUTPUT_PROTECTION_IDS_head():
    class DRM_VIDEO_OUTPUT_PROTECTION_IDS(Structure):
        pass
    return DRM_VIDEO_OUTPUT_PROTECTION_IDS
def _define_DRM_VIDEO_OUTPUT_PROTECTION_IDS():
    DRM_VIDEO_OUTPUT_PROTECTION_IDS = win32more.Media.WindowsMediaFormat.DRM_VIDEO_OUTPUT_PROTECTION_IDS_head
    DRM_VIDEO_OUTPUT_PROTECTION_IDS._fields_ = [
        ("cEntries", UInt16),
        ("rgVop", POINTER(win32more.Media.WindowsMediaFormat.DRM_OUTPUT_PROTECTION_head)),
    ]
    return DRM_VIDEO_OUTPUT_PROTECTION_IDS
def _define_DRM_PLAY_OPL_head():
    class DRM_PLAY_OPL(Structure):
        pass
    return DRM_PLAY_OPL
def _define_DRM_PLAY_OPL():
    DRM_PLAY_OPL = win32more.Media.WindowsMediaFormat.DRM_PLAY_OPL_head
    DRM_PLAY_OPL._fields_ = [
        ("minOPL", win32more.Media.WindowsMediaFormat.DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS),
        ("oplIdReserved", win32more.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS),
        ("vopi", win32more.Media.WindowsMediaFormat.DRM_VIDEO_OUTPUT_PROTECTION_IDS),
    ]
    return DRM_PLAY_OPL
def _define_DRM_COPY_OPL_head():
    class DRM_COPY_OPL(Structure):
        pass
    return DRM_COPY_OPL
def _define_DRM_COPY_OPL():
    DRM_COPY_OPL = win32more.Media.WindowsMediaFormat.DRM_COPY_OPL_head
    DRM_COPY_OPL._fields_ = [
        ("wMinimumCopyLevel", UInt16),
        ("oplIdIncludes", win32more.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS),
        ("oplIdExcludes", win32more.Media.WindowsMediaFormat.DRM_OPL_OUTPUT_IDS),
    ]
    return DRM_COPY_OPL
def _define_IWMDRMReader2_head():
    class IWMDRMReader2(win32more.Media.WindowsMediaFormat.IWMDRMReader_head):
        Guid = Guid('befe7a75-9f1d-4075-b9d9-a3c37bda49a0')
    return IWMDRMReader2
def _define_IWMDRMReader2():
    IWMDRMReader2 = win32more.Media.WindowsMediaFormat.IWMDRMReader2_head
    IWMDRMReader2.SetEvaluateOutputLevelLicenses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(11, 'SetEvaluateOutputLevelLicenses', ((1, 'fEvaluate'),)))
    IWMDRMReader2.GetPlayOutputLevels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.DRM_PLAY_OPL),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(12, 'GetPlayOutputLevels', ((1, 'pPlayOPL'),(1, 'pcbLength'),(1, 'pdwMinAppComplianceLevel'),)))
    IWMDRMReader2.GetCopyOutputLevels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.DRM_COPY_OPL),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(13, 'GetCopyOutputLevels', ((1, 'pCopyOPL'),(1, 'pcbLength'),(1, 'pdwMinAppComplianceLevel'),)))
    IWMDRMReader2.TryNextLicense = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'TryNextLicense', ()))
    return IWMDRMReader2
def _define_IWMDRMReader3_head():
    class IWMDRMReader3(win32more.Media.WindowsMediaFormat.IWMDRMReader2_head):
        Guid = Guid('e08672de-f1e7-4ff4-a0a3-fc4b08e4caf8')
    return IWMDRMReader3
def _define_IWMDRMReader3():
    IWMDRMReader3 = win32more.Media.WindowsMediaFormat.IWMDRMReader3_head
    IWMDRMReader3.GetInclusionList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),POINTER(UInt32), use_last_error=False)(15, 'GetInclusionList', ((1, 'ppGuids'),(1, 'pcGuids'),)))
    return IWMDRMReader3
def _define_IWMReaderPlaylistBurn_head():
    class IWMReaderPlaylistBurn(win32more.System.Com.IUnknown_head):
        Guid = Guid('f28c0300-9baa-4477-a846-1744d9cbf533')
    return IWMReaderPlaylistBurn
def _define_IWMReaderPlaylistBurn():
    IWMReaderPlaylistBurn = win32more.Media.WindowsMediaFormat.IWMReaderPlaylistBurn_head
    IWMReaderPlaylistBurn.InitPlaylistBurn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),win32more.Media.WindowsMediaFormat.IWMStatusCallback_head,c_void_p, use_last_error=False)(3, 'InitPlaylistBurn', ((1, 'cFiles'),(1, 'ppwszFilenames'),(1, 'pCallback'),(1, 'pvContext'),)))
    IWMReaderPlaylistBurn.GetInitResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(4, 'GetInitResults', ((1, 'cFiles'),(1, 'phrStati'),)))
    IWMReaderPlaylistBurn.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Cancel', ()))
    IWMReaderPlaylistBurn.EndPlaylistBurn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(6, 'EndPlaylistBurn', ((1, 'hrBurnResult'),)))
    return IWMReaderPlaylistBurn
def _define_IWMReaderNetworkConfig_head():
    class IWMReaderNetworkConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bec-2b2b-11d3-b36b-00c04f6108ff')
    return IWMReaderNetworkConfig
def _define_IWMReaderNetworkConfig():
    IWMReaderNetworkConfig = win32more.Media.WindowsMediaFormat.IWMReaderNetworkConfig_head
    IWMReaderNetworkConfig.GetBufferingTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(3, 'GetBufferingTime', ((1, 'pcnsBufferingTime'),)))
    IWMReaderNetworkConfig.SetBufferingTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(4, 'SetBufferingTime', ((1, 'cnsBufferingTime'),)))
    IWMReaderNetworkConfig.GetUDPPortRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_PORT_NUMBER_RANGE),POINTER(UInt32), use_last_error=False)(5, 'GetUDPPortRanges', ((1, 'pRangeArray'),(1, 'pcRanges'),)))
    IWMReaderNetworkConfig.SetUDPPortRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.WM_PORT_NUMBER_RANGE),UInt32, use_last_error=False)(6, 'SetUDPPortRanges', ((1, 'pRangeArray'),(1, 'cRanges'),)))
    IWMReaderNetworkConfig.GetProxySettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS), use_last_error=False)(7, 'GetProxySettings', ((1, 'pwszProtocol'),(1, 'pProxySetting'),)))
    IWMReaderNetworkConfig.SetProxySettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_PROXY_SETTINGS, use_last_error=False)(8, 'SetProxySettings', ((1, 'pwszProtocol'),(1, 'ProxySetting'),)))
    IWMReaderNetworkConfig.GetProxyHostName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(9, 'GetProxyHostName', ((1, 'pwszProtocol'),(1, 'pwszHostName'),(1, 'pcchHostName'),)))
    IWMReaderNetworkConfig.SetProxyHostName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(10, 'SetProxyHostName', ((1, 'pwszProtocol'),(1, 'pwszHostName'),)))
    IWMReaderNetworkConfig.GetProxyPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(11, 'GetProxyPort', ((1, 'pwszProtocol'),(1, 'pdwPort'),)))
    IWMReaderNetworkConfig.SetProxyPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(12, 'SetProxyPort', ((1, 'pwszProtocol'),(1, 'dwPort'),)))
    IWMReaderNetworkConfig.GetProxyExceptionList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(13, 'GetProxyExceptionList', ((1, 'pwszProtocol'),(1, 'pwszExceptionList'),(1, 'pcchExceptionList'),)))
    IWMReaderNetworkConfig.SetProxyExceptionList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(14, 'SetProxyExceptionList', ((1, 'pwszProtocol'),(1, 'pwszExceptionList'),)))
    IWMReaderNetworkConfig.GetProxyBypassForLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'GetProxyBypassForLocal', ((1, 'pwszProtocol'),(1, 'pfBypassForLocal'),)))
    IWMReaderNetworkConfig.SetProxyBypassForLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(16, 'SetProxyBypassForLocal', ((1, 'pwszProtocol'),(1, 'fBypassForLocal'),)))
    IWMReaderNetworkConfig.GetForceRerunAutoProxyDetection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'GetForceRerunAutoProxyDetection', ((1, 'pfForceRerunDetection'),)))
    IWMReaderNetworkConfig.SetForceRerunAutoProxyDetection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(18, 'SetForceRerunAutoProxyDetection', ((1, 'fForceRerunDetection'),)))
    IWMReaderNetworkConfig.GetEnableMulticast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'GetEnableMulticast', ((1, 'pfEnableMulticast'),)))
    IWMReaderNetworkConfig.SetEnableMulticast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(20, 'SetEnableMulticast', ((1, 'fEnableMulticast'),)))
    IWMReaderNetworkConfig.GetEnableHTTP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(21, 'GetEnableHTTP', ((1, 'pfEnableHTTP'),)))
    IWMReaderNetworkConfig.SetEnableHTTP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(22, 'SetEnableHTTP', ((1, 'fEnableHTTP'),)))
    IWMReaderNetworkConfig.GetEnableUDP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(23, 'GetEnableUDP', ((1, 'pfEnableUDP'),)))
    IWMReaderNetworkConfig.SetEnableUDP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(24, 'SetEnableUDP', ((1, 'fEnableUDP'),)))
    IWMReaderNetworkConfig.GetEnableTCP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(25, 'GetEnableTCP', ((1, 'pfEnableTCP'),)))
    IWMReaderNetworkConfig.SetEnableTCP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(26, 'SetEnableTCP', ((1, 'fEnableTCP'),)))
    IWMReaderNetworkConfig.ResetProtocolRollover = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(27, 'ResetProtocolRollover', ()))
    IWMReaderNetworkConfig.GetConnectionBandwidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(28, 'GetConnectionBandwidth', ((1, 'pdwConnectionBandwidth'),)))
    IWMReaderNetworkConfig.SetConnectionBandwidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(29, 'SetConnectionBandwidth', ((1, 'dwConnectionBandwidth'),)))
    IWMReaderNetworkConfig.GetNumProtocolsSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(30, 'GetNumProtocolsSupported', ((1, 'pcProtocols'),)))
    IWMReaderNetworkConfig.GetSupportedProtocolName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(31, 'GetSupportedProtocolName', ((1, 'dwProtocolNum'),(1, 'pwszProtocolName'),(1, 'pcchProtocolName'),)))
    IWMReaderNetworkConfig.AddLoggingUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(32, 'AddLoggingUrl', ((1, 'pwszUrl'),)))
    IWMReaderNetworkConfig.GetLoggingUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(33, 'GetLoggingUrl', ((1, 'dwIndex'),(1, 'pwszUrl'),(1, 'pcchUrl'),)))
    IWMReaderNetworkConfig.GetLoggingUrlCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(34, 'GetLoggingUrlCount', ((1, 'pdwUrlCount'),)))
    IWMReaderNetworkConfig.ResetLoggingUrlList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'ResetLoggingUrlList', ()))
    return IWMReaderNetworkConfig
def _define_IWMReaderNetworkConfig2_head():
    class IWMReaderNetworkConfig2(win32more.Media.WindowsMediaFormat.IWMReaderNetworkConfig_head):
        Guid = Guid('d979a853-042b-4050-8387-c939db22013f')
    return IWMReaderNetworkConfig2
def _define_IWMReaderNetworkConfig2():
    IWMReaderNetworkConfig2 = win32more.Media.WindowsMediaFormat.IWMReaderNetworkConfig2_head
    IWMReaderNetworkConfig2.GetEnableContentCaching = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(36, 'GetEnableContentCaching', ((1, 'pfEnableContentCaching'),)))
    IWMReaderNetworkConfig2.SetEnableContentCaching = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(37, 'SetEnableContentCaching', ((1, 'fEnableContentCaching'),)))
    IWMReaderNetworkConfig2.GetEnableFastCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(38, 'GetEnableFastCache', ((1, 'pfEnableFastCache'),)))
    IWMReaderNetworkConfig2.SetEnableFastCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(39, 'SetEnableFastCache', ((1, 'fEnableFastCache'),)))
    IWMReaderNetworkConfig2.GetAcceleratedStreamingDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(40, 'GetAcceleratedStreamingDuration', ((1, 'pcnsAccelDuration'),)))
    IWMReaderNetworkConfig2.SetAcceleratedStreamingDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(41, 'SetAcceleratedStreamingDuration', ((1, 'cnsAccelDuration'),)))
    IWMReaderNetworkConfig2.GetAutoReconnectLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(42, 'GetAutoReconnectLimit', ((1, 'pdwAutoReconnectLimit'),)))
    IWMReaderNetworkConfig2.SetAutoReconnectLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(43, 'SetAutoReconnectLimit', ((1, 'dwAutoReconnectLimit'),)))
    IWMReaderNetworkConfig2.GetEnableResends = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(44, 'GetEnableResends', ((1, 'pfEnableResends'),)))
    IWMReaderNetworkConfig2.SetEnableResends = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(45, 'SetEnableResends', ((1, 'fEnableResends'),)))
    IWMReaderNetworkConfig2.GetEnableThinning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(46, 'GetEnableThinning', ((1, 'pfEnableThinning'),)))
    IWMReaderNetworkConfig2.SetEnableThinning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(47, 'SetEnableThinning', ((1, 'fEnableThinning'),)))
    IWMReaderNetworkConfig2.GetMaxNetPacketSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(48, 'GetMaxNetPacketSize', ((1, 'pdwMaxNetPacketSize'),)))
    return IWMReaderNetworkConfig2
def _define_IWMReaderStreamClock_head():
    class IWMReaderStreamClock(win32more.System.Com.IUnknown_head):
        Guid = Guid('96406bed-2b2b-11d3-b36b-00c04f6108ff')
    return IWMReaderStreamClock
def _define_IWMReaderStreamClock():
    IWMReaderStreamClock = win32more.Media.WindowsMediaFormat.IWMReaderStreamClock_head
    IWMReaderStreamClock.GetTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(3, 'GetTime', ((1, 'pcnsNow'),)))
    IWMReaderStreamClock.SetTimer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,c_void_p,POINTER(UInt32), use_last_error=False)(4, 'SetTimer', ((1, 'cnsWhen'),(1, 'pvParam'),(1, 'pdwTimerId'),)))
    IWMReaderStreamClock.KillTimer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'KillTimer', ((1, 'dwTimerId'),)))
    return IWMReaderStreamClock
def _define_IWMIndexer_head():
    class IWMIndexer(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d7cdc71-9888-11d3-8edc-00c04f6109cf')
    return IWMIndexer
def _define_IWMIndexer():
    IWMIndexer = win32more.Media.WindowsMediaFormat.IWMIndexer_head
    IWMIndexer.StartIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.IWMStatusCallback_head,c_void_p, use_last_error=False)(3, 'StartIndexing', ((1, 'pwszURL'),(1, 'pCallback'),(1, 'pvContext'),)))
    IWMIndexer.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Cancel', ()))
    return IWMIndexer
def _define_IWMIndexer2_head():
    class IWMIndexer2(win32more.Media.WindowsMediaFormat.IWMIndexer_head):
        Guid = Guid('b70f1e42-6255-4df0-a6b9-02b212d9e2bb')
    return IWMIndexer2
def _define_IWMIndexer2():
    IWMIndexer2 = win32more.Media.WindowsMediaFormat.IWMIndexer2_head
    IWMIndexer2.Configure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Media.WindowsMediaFormat.WMT_INDEXER_TYPE,c_void_p,c_void_p, use_last_error=False)(5, 'Configure', ((1, 'wStreamNum'),(1, 'nIndexerType'),(1, 'pvInterval'),(1, 'pvIndexType'),)))
    return IWMIndexer2
def _define_IWMLicenseBackup_head():
    class IWMLicenseBackup(win32more.System.Com.IUnknown_head):
        Guid = Guid('05e5ac9f-3fb6-4508-bb43-a4067ba1ebe8')
    return IWMLicenseBackup
def _define_IWMLicenseBackup():
    IWMLicenseBackup = win32more.Media.WindowsMediaFormat.IWMLicenseBackup_head
    IWMLicenseBackup.BackupLicenses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMStatusCallback_head, use_last_error=False)(3, 'BackupLicenses', ((1, 'dwFlags'),(1, 'pCallback'),)))
    IWMLicenseBackup.CancelLicenseBackup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'CancelLicenseBackup', ()))
    return IWMLicenseBackup
def _define_IWMLicenseRestore_head():
    class IWMLicenseRestore(win32more.System.Com.IUnknown_head):
        Guid = Guid('c70b6334-a22e-4efb-a245-15e65a004a13')
    return IWMLicenseRestore
def _define_IWMLicenseRestore():
    IWMLicenseRestore = win32more.Media.WindowsMediaFormat.IWMLicenseRestore_head
    IWMLicenseRestore.RestoreLicenses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.WindowsMediaFormat.IWMStatusCallback_head, use_last_error=False)(3, 'RestoreLicenses', ((1, 'dwFlags'),(1, 'pCallback'),)))
    IWMLicenseRestore.CancelLicenseRestore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'CancelLicenseRestore', ()))
    return IWMLicenseRestore
def _define_IWMBackupRestoreProps_head():
    class IWMBackupRestoreProps(win32more.System.Com.IUnknown_head):
        Guid = Guid('3c8e0da6-996f-4ff3-a1af-4838f9377e2e')
    return IWMBackupRestoreProps
def _define_IWMBackupRestoreProps():
    IWMBackupRestoreProps = win32more.Media.WindowsMediaFormat.IWMBackupRestoreProps_head
    IWMBackupRestoreProps.GetPropCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(3, 'GetPropCount', ((1, 'pcProps'),)))
    IWMBackupRestoreProps.GetPropByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Char),POINTER(UInt16),POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(4, 'GetPropByIndex', ((1, 'wIndex'),(1, 'pwszName'),(1, 'pcchNameLen'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMBackupRestoreProps.GetPropByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt16), use_last_error=False)(5, 'GetPropByName', ((1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pcbLength'),)))
    IWMBackupRestoreProps.SetProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt16, use_last_error=False)(6, 'SetProp', ((1, 'pszName'),(1, 'Type'),(1, 'pValue'),(1, 'cbLength'),)))
    IWMBackupRestoreProps.RemoveProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'RemoveProp', ((1, 'pcwszName'),)))
    IWMBackupRestoreProps.RemoveAllProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'RemoveAllProps', ()))
    return IWMBackupRestoreProps
def _define_IWMCodecInfo_head():
    class IWMCodecInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('a970f41e-34de-4a98-b3ba-e4b3ca7528f0')
    return IWMCodecInfo
def _define_IWMCodecInfo():
    IWMCodecInfo = win32more.Media.WindowsMediaFormat.IWMCodecInfo_head
    IWMCodecInfo.GetCodecInfoCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(3, 'GetCodecInfoCount', ((1, 'guidType'),(1, 'pcCodecs'),)))
    IWMCodecInfo.GetCodecFormatCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetCodecFormatCount', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'pcFormat'),)))
    IWMCodecInfo.GetCodecFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMStreamConfig_head), use_last_error=False)(5, 'GetCodecFormat', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'dwFormatIndex'),(1, 'ppIStreamConfig'),)))
    return IWMCodecInfo
def _define_IWMCodecInfo2_head():
    class IWMCodecInfo2(win32more.Media.WindowsMediaFormat.IWMCodecInfo_head):
        Guid = Guid('aa65e273-b686-4056-91ec-dd768d4df710')
    return IWMCodecInfo2
def _define_IWMCodecInfo2():
    IWMCodecInfo2 = win32more.Media.WindowsMediaFormat.IWMCodecInfo2_head
    IWMCodecInfo2.GetCodecName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(6, 'GetCodecName', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'wszName'),(1, 'pcchName'),)))
    IWMCodecInfo2.GetCodecFormatDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMStreamConfig_head),POINTER(Char),POINTER(UInt32), use_last_error=False)(7, 'GetCodecFormatDesc', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'dwFormatIndex'),(1, 'ppIStreamConfig'),(1, 'wszDesc'),(1, 'pcchDesc'),)))
    return IWMCodecInfo2
def _define_IWMCodecInfo3_head():
    class IWMCodecInfo3(win32more.Media.WindowsMediaFormat.IWMCodecInfo2_head):
        Guid = Guid('7e51f487-4d93-4f98-8ab4-27d0565adc51')
    return IWMCodecInfo3
def _define_IWMCodecInfo3():
    IWMCodecInfo3 = win32more.Media.WindowsMediaFormat.IWMCodecInfo3_head
    IWMCodecInfo3.GetCodecFormatProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt32), use_last_error=False)(8, 'GetCodecFormatProp', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'dwFormatIndex'),(1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pdwSize'),)))
    IWMCodecInfo3.GetCodecProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt32), use_last_error=False)(9, 'GetCodecProp', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pdwSize'),)))
    IWMCodecInfo3.SetCodecEnumerationSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE,POINTER(Byte),UInt32, use_last_error=False)(10, 'SetCodecEnumerationSetting', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'pszName'),(1, 'Type'),(1, 'pValue'),(1, 'dwSize'),)))
    IWMCodecInfo3.GetCodecEnumerationSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Media.WindowsMediaFormat.WMT_ATTR_DATATYPE),POINTER(Byte),POINTER(UInt32), use_last_error=False)(11, 'GetCodecEnumerationSetting', ((1, 'guidType'),(1, 'dwCodecIndex'),(1, 'pszName'),(1, 'pType'),(1, 'pValue'),(1, 'pdwSize'),)))
    return IWMCodecInfo3
def _define_IWMLanguageList_head():
    class IWMLanguageList(win32more.System.Com.IUnknown_head):
        Guid = Guid('df683f00-2d49-4d8e-92b7-fb19f6a0dc57')
    return IWMLanguageList
def _define_IWMLanguageList():
    IWMLanguageList = win32more.Media.WindowsMediaFormat.IWMLanguageList_head
    IWMLanguageList.GetLanguageCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(3, 'GetLanguageCount', ((1, 'pwCount'),)))
    IWMLanguageList.GetLanguageDetails = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Char),POINTER(UInt16), use_last_error=False)(4, 'GetLanguageDetails', ((1, 'wIndex'),(1, 'pwszLanguageString'),(1, 'pcchLanguageStringLength'),)))
    IWMLanguageList.AddLanguageByRFC1766String = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt16), use_last_error=False)(5, 'AddLanguageByRFC1766String', ((1, 'pwszLanguageString'),(1, 'pwIndex'),)))
    return IWMLanguageList
def _define_IWMWriterPushSink_head():
    class IWMWriterPushSink(win32more.Media.WindowsMediaFormat.IWMWriterSink_head):
        Guid = Guid('dc10e6a5-072c-467d-bf57-6330a9dde12a')
    return IWMWriterPushSink
def _define_IWMWriterPushSink():
    IWMWriterPushSink = win32more.Media.WindowsMediaFormat.IWMWriterPushSink_head
    IWMWriterPushSink.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(8, 'Connect', ((1, 'pwszURL'),(1, 'pwszTemplateURL'),(1, 'fAutoDestroy'),)))
    IWMWriterPushSink.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Disconnect', ()))
    IWMWriterPushSink.EndSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'EndSession', ()))
    return IWMWriterPushSink
def _define_IWMDeviceRegistration_head():
    class IWMDeviceRegistration(win32more.System.Com.IUnknown_head):
        Guid = Guid('f6211f03-8d21-4e94-93e6-8510805f2d99')
    return IWMDeviceRegistration
def _define_IWMDeviceRegistration():
    IWMDeviceRegistration = win32more.Media.WindowsMediaFormat.IWMDeviceRegistration_head
    IWMDeviceRegistration.RegisterDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,win32more.Media.WindowsMediaFormat.DRM_VAL16,POINTER(win32more.Media.WindowsMediaFormat.IWMRegisteredDevice_head), use_last_error=False)(3, 'RegisterDevice', ((1, 'dwRegisterType'),(1, 'pbCertificate'),(1, 'cbCertificate'),(1, 'SerialNumber'),(1, 'ppDevice'),)))
    IWMDeviceRegistration.UnregisterDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,win32more.Media.WindowsMediaFormat.DRM_VAL16, use_last_error=False)(4, 'UnregisterDevice', ((1, 'dwRegisterType'),(1, 'pbCertificate'),(1, 'cbCertificate'),(1, 'SerialNumber'),)))
    IWMDeviceRegistration.GetRegistrationStats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetRegistrationStats', ((1, 'dwRegisterType'),(1, 'pcRegisteredDevices'),)))
    IWMDeviceRegistration.GetFirstRegisteredDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMRegisteredDevice_head), use_last_error=False)(6, 'GetFirstRegisteredDevice', ((1, 'dwRegisterType'),(1, 'ppDevice'),)))
    IWMDeviceRegistration.GetNextRegisteredDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMRegisteredDevice_head), use_last_error=False)(7, 'GetNextRegisteredDevice', ((1, 'ppDevice'),)))
    IWMDeviceRegistration.GetRegisteredDeviceByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,win32more.Media.WindowsMediaFormat.DRM_VAL16,POINTER(win32more.Media.WindowsMediaFormat.IWMRegisteredDevice_head), use_last_error=False)(8, 'GetRegisteredDeviceByID', ((1, 'dwRegisterType'),(1, 'pbCertificate'),(1, 'cbCertificate'),(1, 'SerialNumber'),(1, 'ppDevice'),)))
    return IWMDeviceRegistration
def _define_IWMRegisteredDevice_head():
    class IWMRegisteredDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('a4503bec-5508-4148-97ac-bfa75760a70d')
    return IWMRegisteredDevice
def _define_IWMRegisteredDevice():
    IWMRegisteredDevice = win32more.Media.WindowsMediaFormat.IWMRegisteredDevice_head
    IWMRegisteredDevice.GetDeviceSerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.DRM_VAL16_head), use_last_error=False)(3, 'GetDeviceSerialNumber', ((1, 'pSerialNumber'),)))
    IWMRegisteredDevice.GetDeviceCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head), use_last_error=False)(4, 'GetDeviceCertificate', ((1, 'ppCertificate'),)))
    IWMRegisteredDevice.GetDeviceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetDeviceType', ((1, 'pdwType'),)))
    IWMRegisteredDevice.GetAttributeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetAttributeCount', ((1, 'pcAttributes'),)))
    IWMRegisteredDevice.GetAttributeByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetAttributeByIndex', ((1, 'dwIndex'),(1, 'pbstrName'),(1, 'pbstrValue'),)))
    IWMRegisteredDevice.GetAttributeByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetAttributeByName', ((1, 'bstrName'),(1, 'pbstrValue'),)))
    IWMRegisteredDevice.SetAttributeByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(9, 'SetAttributeByName', ((1, 'bstrName'),(1, 'bstrValue'),)))
    IWMRegisteredDevice.Approve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'Approve', ((1, 'fApprove'),)))
    IWMRegisteredDevice.IsValid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'IsValid', ((1, 'pfValid'),)))
    IWMRegisteredDevice.IsApproved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'IsApproved', ((1, 'pfApproved'),)))
    IWMRegisteredDevice.IsWmdrmCompliant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'IsWmdrmCompliant', ((1, 'pfCompliant'),)))
    IWMRegisteredDevice.IsOpened = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'IsOpened', ((1, 'pfOpened'),)))
    IWMRegisteredDevice.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Open', ()))
    IWMRegisteredDevice.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Close', ()))
    return IWMRegisteredDevice
def _define_IWMProximityDetection_head():
    class IWMProximityDetection(win32more.System.Com.IUnknown_head):
        Guid = Guid('6a9fd8ee-b651-4bf0-b849-7d4ece79a2b1')
    return IWMProximityDetection
def _define_IWMProximityDetection():
    IWMProximityDetection = win32more.Media.WindowsMediaFormat.IWMProximityDetection_head
    IWMProximityDetection.StartDetection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),UInt32,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),win32more.Media.WindowsMediaFormat.IWMStatusCallback_head,c_void_p, use_last_error=False)(3, 'StartDetection', ((1, 'pbRegistrationMsg'),(1, 'cbRegistrationMsg'),(1, 'pbLocalAddress'),(1, 'cbLocalAddress'),(1, 'dwExtraPortsAllowed'),(1, 'ppRegistrationResponseMsg'),(1, 'pCallback'),(1, 'pvContext'),)))
    return IWMProximityDetection
def _define_IWMDRMMessageParser_head():
    class IWMDRMMessageParser(win32more.System.Com.IUnknown_head):
        Guid = Guid('a73a0072-25a0-4c99-b4a5-ede8101a6c39')
    return IWMDRMMessageParser
def _define_IWMDRMMessageParser():
    IWMDRMMessageParser = win32more.Media.WindowsMediaFormat.IWMDRMMessageParser_head
    IWMDRMMessageParser.ParseRegistrationReqMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),POINTER(win32more.Media.WindowsMediaFormat.DRM_VAL16_head), use_last_error=False)(3, 'ParseRegistrationReqMsg', ((1, 'pbRegistrationReqMsg'),(1, 'cbRegistrationReqMsg'),(1, 'ppDeviceCert'),(1, 'pDeviceSerialNumber'),)))
    IWMDRMMessageParser.ParseLicenseRequestMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),POINTER(win32more.Media.WindowsMediaFormat.DRM_VAL16_head),POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'ParseLicenseRequestMsg', ((1, 'pbLicenseRequestMsg'),(1, 'cbLicenseRequestMsg'),(1, 'ppDeviceCert'),(1, 'pDeviceSerialNumber'),(1, 'pbstrAction'),)))
    return IWMDRMMessageParser
def _define_IWMDRMTranscryptor_head():
    class IWMDRMTranscryptor(win32more.System.Com.IUnknown_head):
        Guid = Guid('69059850-6e6f-4bb2-806f-71863ddfc471')
    return IWMDRMTranscryptor
def _define_IWMDRMTranscryptor():
    IWMDRMTranscryptor = win32more.Media.WindowsMediaFormat.IWMDRMTranscryptor_head
    IWMDRMTranscryptor.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,c_char_p_no,UInt32,POINTER(win32more.Media.WindowsMediaFormat.INSSBuffer_head),win32more.Media.WindowsMediaFormat.IWMStatusCallback_head,c_void_p, use_last_error=False)(3, 'Initialize', ((1, 'bstrFileName'),(1, 'pbLicenseRequestMsg'),(1, 'cbLicenseRequestMsg'),(1, 'ppLicenseResponseMsg'),(1, 'pCallback'),(1, 'pvContext'),)))
    IWMDRMTranscryptor.Seek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(4, 'Seek', ((1, 'hnsTime'),)))
    IWMDRMTranscryptor.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32), use_last_error=False)(5, 'Read', ((1, 'pbData'),(1, 'pcbData'),)))
    IWMDRMTranscryptor.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Close', ()))
    return IWMDRMTranscryptor
def _define_IWMDRMTranscryptor2_head():
    class IWMDRMTranscryptor2(win32more.Media.WindowsMediaFormat.IWMDRMTranscryptor_head):
        Guid = Guid('e0da439f-d331-496a-bece-18e5bac5dd23')
    return IWMDRMTranscryptor2
def _define_IWMDRMTranscryptor2():
    IWMDRMTranscryptor2 = win32more.Media.WindowsMediaFormat.IWMDRMTranscryptor2_head
    IWMDRMTranscryptor2.SeekEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,Single,win32more.Foundation.BOOL, use_last_error=False)(7, 'SeekEx', ((1, 'cnsStartTime'),(1, 'cnsDuration'),(1, 'flRate'),(1, 'fIncludeFileHeader'),)))
    IWMDRMTranscryptor2.ZeroAdjustTimestamps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(8, 'ZeroAdjustTimestamps', ((1, 'fEnable'),)))
    IWMDRMTranscryptor2.GetSeekStartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(9, 'GetSeekStartTime', ((1, 'pcnsTime'),)))
    IWMDRMTranscryptor2.GetDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(10, 'GetDuration', ((1, 'pcnsDuration'),)))
    return IWMDRMTranscryptor2
def _define_IWMDRMTranscryptionManager_head():
    class IWMDRMTranscryptionManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('b1a887b2-a4f0-407a-b02e-efbd23bbecdf')
    return IWMDRMTranscryptionManager
def _define_IWMDRMTranscryptionManager():
    IWMDRMTranscryptionManager = win32more.Media.WindowsMediaFormat.IWMDRMTranscryptionManager_head
    IWMDRMTranscryptionManager.CreateTranscryptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMDRMTranscryptor_head), use_last_error=False)(3, 'CreateTranscryptor', ((1, 'ppTranscryptor'),)))
    return IWMDRMTranscryptionManager
def _define_IWMWatermarkInfo_head():
    class IWMWatermarkInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f497062-f2e2-4624-8ea7-9dd40d81fc8d')
    return IWMWatermarkInfo
def _define_IWMWatermarkInfo():
    IWMWatermarkInfo = win32more.Media.WindowsMediaFormat.IWMWatermarkInfo_head
    IWMWatermarkInfo.GetWatermarkEntryCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE,POINTER(UInt32), use_last_error=False)(3, 'GetWatermarkEntryCount', ((1, 'wmetType'),(1, 'pdwCount'),)))
    IWMWatermarkInfo.GetWatermarkEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_TYPE,UInt32,POINTER(win32more.Media.WindowsMediaFormat.WMT_WATERMARK_ENTRY_head), use_last_error=False)(4, 'GetWatermarkEntry', ((1, 'wmetType'),(1, 'dwEntryNum'),(1, 'pEntry'),)))
    return IWMWatermarkInfo
def _define_IWMReaderAccelerator_head():
    class IWMReaderAccelerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('bddc4d08-944d-4d52-a612-46c3fda07dd4')
    return IWMReaderAccelerator
def _define_IWMReaderAccelerator():
    IWMReaderAccelerator = win32more.Media.WindowsMediaFormat.IWMReaderAccelerator_head
    IWMReaderAccelerator.GetCodecInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetCodecInterface', ((1, 'dwOutputNum'),(1, 'riid'),(1, 'ppvCodecInterface'),)))
    IWMReaderAccelerator.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.WindowsMediaFormat.WM_MEDIA_TYPE_head), use_last_error=False)(4, 'Notify', ((1, 'dwOutputNum'),(1, 'pSubtype'),)))
    return IWMReaderAccelerator
def _define_IWMReaderTimecode_head():
    class IWMReaderTimecode(win32more.System.Com.IUnknown_head):
        Guid = Guid('f369e2f0-e081-4fe6-8450-b810b2f410d1')
    return IWMReaderTimecode
def _define_IWMReaderTimecode():
    IWMReaderTimecode = win32more.Media.WindowsMediaFormat.IWMReaderTimecode_head
    IWMReaderTimecode.GetTimecodeRangeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt16), use_last_error=False)(3, 'GetTimecodeRangeCount', ((1, 'wStreamNum'),(1, 'pwRangeCount'),)))
    IWMReaderTimecode.GetTimecodeRangeBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetTimecodeRangeBounds', ((1, 'wStreamNum'),(1, 'wRangeNum'),(1, 'pStartTimecode'),(1, 'pEndTimecode'),)))
    return IWMReaderTimecode
def _define_IWMAddressAccess_head():
    class IWMAddressAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('bb3c6389-1633-4e92-af14-9f3173ba39d0')
    return IWMAddressAccess
def _define_IWMAddressAccess():
    IWMAddressAccess = win32more.Media.WindowsMediaFormat.IWMAddressAccess_head
    IWMAddressAccess.GetAccessEntryCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WM_AETYPE,POINTER(UInt32), use_last_error=False)(3, 'GetAccessEntryCount', ((1, 'aeType'),(1, 'pcEntries'),)))
    IWMAddressAccess.GetAccessEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WM_AETYPE,UInt32,POINTER(win32more.Media.WindowsMediaFormat.WM_ADDRESS_ACCESSENTRY_head), use_last_error=False)(4, 'GetAccessEntry', ((1, 'aeType'),(1, 'dwEntryNum'),(1, 'pAddrAccessEntry'),)))
    IWMAddressAccess.AddAccessEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WM_AETYPE,POINTER(win32more.Media.WindowsMediaFormat.WM_ADDRESS_ACCESSENTRY_head), use_last_error=False)(5, 'AddAccessEntry', ((1, 'aeType'),(1, 'pAddrAccessEntry'),)))
    IWMAddressAccess.RemoveAccessEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WM_AETYPE,UInt32, use_last_error=False)(6, 'RemoveAccessEntry', ((1, 'aeType'),(1, 'dwEntryNum'),)))
    return IWMAddressAccess
def _define_IWMAddressAccess2_head():
    class IWMAddressAccess2(win32more.Media.WindowsMediaFormat.IWMAddressAccess_head):
        Guid = Guid('65a83fc2-3e98-4d4d-81b5-2a742886b33d')
    return IWMAddressAccess2
def _define_IWMAddressAccess2():
    IWMAddressAccess2 = win32more.Media.WindowsMediaFormat.IWMAddressAccess2_head
    IWMAddressAccess2.GetAccessEntryEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WM_AETYPE,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetAccessEntryEx', ((1, 'aeType'),(1, 'dwEntryNum'),(1, 'pbstrAddress'),(1, 'pbstrMask'),)))
    IWMAddressAccess2.AddAccessEntryEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.WM_AETYPE,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(8, 'AddAccessEntryEx', ((1, 'aeType'),(1, 'bstrAddress'),(1, 'bstrMask'),)))
    return IWMAddressAccess2
def _define_IWMImageInfo_head():
    class IWMImageInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f0aa3b6-7267-4d89-88f2-ba915aa5c4c6')
    return IWMImageInfo
def _define_IWMImageInfo():
    IWMImageInfo = win32more.Media.WindowsMediaFormat.IWMImageInfo_head
    IWMImageInfo.GetImageCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetImageCount', ((1, 'pcImages'),)))
    IWMImageInfo.GetImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16),POINTER(Char),POINTER(UInt16),POINTER(Char),POINTER(UInt16),POINTER(UInt32),POINTER(Byte), use_last_error=False)(4, 'GetImage', ((1, 'wIndex'),(1, 'pcchMIMEType'),(1, 'pwszMIMEType'),(1, 'pcchDescription'),(1, 'pwszDescription'),(1, 'pImageType'),(1, 'pcbImageData'),(1, 'pbImageData'),)))
    return IWMImageInfo
def _define_IWMLicenseRevocationAgent_head():
    class IWMLicenseRevocationAgent(win32more.System.Com.IUnknown_head):
        Guid = Guid('6967f2c9-4e26-4b57-8894-799880f7ac7b')
    return IWMLicenseRevocationAgent
def _define_IWMLicenseRevocationAgent():
    IWMLicenseRevocationAgent = win32more.Media.WindowsMediaFormat.IWMLicenseRevocationAgent_head
    IWMLicenseRevocationAgent.GetLRBChallenge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(3, 'GetLRBChallenge', ((1, 'pMachineID'),(1, 'dwMachineIDLength'),(1, 'pChallenge'),(1, 'dwChallengeLength'),(1, 'pChallengeOutput'),(1, 'pdwChallengeOutputLength'),)))
    IWMLicenseRevocationAgent.ProcessLRB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'ProcessLRB', ((1, 'pSignedLRB'),(1, 'dwSignedLRBLength'),(1, 'pSignedACK'),(1, 'pdwSignedACKLength'),)))
    return IWMLicenseRevocationAgent
def _define_IWMAuthorizer_head():
    class IWMAuthorizer(win32more.System.Com.IUnknown_head):
        Guid = Guid('d9b67d36-a9ad-4eb4-baef-db284ef5504c')
    return IWMAuthorizer
def _define_IWMAuthorizer():
    IWMAuthorizer = win32more.Media.WindowsMediaFormat.IWMAuthorizer_head
    IWMAuthorizer.GetCertCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCertCount', ((1, 'pcCerts'),)))
    IWMAuthorizer.GetCert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_char_p_no), use_last_error=False)(4, 'GetCert', ((1, 'dwIndex'),(1, 'ppbCertData'),)))
    IWMAuthorizer.GetSharedData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,c_char_p_no,POINTER(c_char_p_no), use_last_error=False)(5, 'GetSharedData', ((1, 'dwCertIndex'),(1, 'pbSharedData'),(1, 'pbCert'),(1, 'ppbSharedData'),)))
    return IWMAuthorizer
def _define_IWMSecureChannel_head():
    class IWMSecureChannel(win32more.Media.WindowsMediaFormat.IWMAuthorizer_head):
        Guid = Guid('2720598a-d0f2-4189-bd10-91c46ef0936f')
    return IWMSecureChannel
def _define_IWMSecureChannel():
    IWMSecureChannel = win32more.Media.WindowsMediaFormat.IWMSecureChannel_head
    IWMSecureChannel.WMSC_AddCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMAuthorizer_head, use_last_error=False)(6, 'WMSC_AddCertificate', ((1, 'pCert'),)))
    IWMSecureChannel.WMSC_AddSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32, use_last_error=False)(7, 'WMSC_AddSignature', ((1, 'pbCertSig'),(1, 'cbCertSig'),)))
    IWMSecureChannel.WMSC_Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMSecureChannel_head, use_last_error=False)(8, 'WMSC_Connect', ((1, 'pOtherSide'),)))
    IWMSecureChannel.WMSC_IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'WMSC_IsConnected', ((1, 'pfIsConnected'),)))
    IWMSecureChannel.WMSC_Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'WMSC_Disconnect', ()))
    IWMSecureChannel.WMSC_GetValidCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(11, 'WMSC_GetValidCertificate', ((1, 'ppbCertificate'),(1, 'pdwSignature'),)))
    IWMSecureChannel.WMSC_Encrypt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32, use_last_error=False)(12, 'WMSC_Encrypt', ((1, 'pbData'),(1, 'cbData'),)))
    IWMSecureChannel.WMSC_Decrypt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32, use_last_error=False)(13, 'WMSC_Decrypt', ((1, 'pbData'),(1, 'cbData'),)))
    IWMSecureChannel.WMSC_Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'WMSC_Lock', ()))
    IWMSecureChannel.WMSC_Unlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'WMSC_Unlock', ()))
    IWMSecureChannel.WMSC_SetSharedData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no, use_last_error=False)(16, 'WMSC_SetSharedData', ((1, 'dwCertIndex'),(1, 'pbSharedData'),)))
    return IWMSecureChannel
def _define_IWMGetSecureChannel_head():
    class IWMGetSecureChannel(win32more.System.Com.IUnknown_head):
        Guid = Guid('94bc0598-c3d2-11d3-bedf-00c04f612986')
    return IWMGetSecureChannel
def _define_IWMGetSecureChannel():
    IWMGetSecureChannel = win32more.Media.WindowsMediaFormat.IWMGetSecureChannel_head
    IWMGetSecureChannel.GetPeerSecureChannelInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMSecureChannel_head), use_last_error=False)(3, 'GetPeerSecureChannelInterface', ((1, 'ppPeer'),)))
    return IWMGetSecureChannel
def _define_INSNetSourceCreator_head():
    class INSNetSourceCreator(win32more.System.Com.IUnknown_head):
        Guid = Guid('0c0e4080-9081-11d2-beec-0060082f2054')
    return INSNetSourceCreator
def _define_INSNetSourceCreator():
    INSNetSourceCreator = win32more.Media.WindowsMediaFormat.INSNetSourceCreator_head
    INSNetSourceCreator.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Initialize', ()))
    INSNetSourceCreator.CreateNetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head,c_char_p_no,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,UInt64, use_last_error=False)(4, 'CreateNetSource', ((1, 'pszStreamName'),(1, 'pMonitor'),(1, 'pData'),(1, 'pUserContext'),(1, 'pCallback'),(1, 'qwContext'),)))
    INSNetSourceCreator.GetNetSourceProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'GetNetSourceProperties', ((1, 'pszStreamName'),(1, 'ppPropertiesNode'),)))
    INSNetSourceCreator.GetNetSourceSharedNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'GetNetSourceSharedNamespace', ((1, 'ppSharedNamespace'),)))
    INSNetSourceCreator.GetNetSourceAdminInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetNetSourceAdminInterface', ((1, 'pszStreamName'),(1, 'pVal'),)))
    INSNetSourceCreator.GetNumProtocolsSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetNumProtocolsSupported', ((1, 'pcProtocols'),)))
    INSNetSourceCreator.GetProtocolName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt16), use_last_error=False)(9, 'GetProtocolName', ((1, 'dwProtocolNum'),(1, 'pwszProtocolName'),(1, 'pcchProtocolName'),)))
    INSNetSourceCreator.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Shutdown', ()))
    return INSNetSourceCreator
def _define_IWMPlayerTimestampHook_head():
    class IWMPlayerTimestampHook(win32more.System.Com.IUnknown_head):
        Guid = Guid('28580dda-d98e-48d0-b7ae-69e473a02825')
    return IWMPlayerTimestampHook
def _define_IWMPlayerTimestampHook():
    IWMPlayerTimestampHook = win32more.Media.WindowsMediaFormat.IWMPlayerTimestampHook_head
    IWMPlayerTimestampHook.MapTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Int64), use_last_error=False)(3, 'MapTimestamp', ((1, 'rtIn'),(1, 'prtOut'),)))
    return IWMPlayerTimestampHook
def _define_IWMCodecAMVideoAccelerator_head():
    class IWMCodecAMVideoAccelerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('d98ee251-34e0-4a2d-9312-9b4c788d9fa1')
    return IWMCodecAMVideoAccelerator
def _define_IWMCodecAMVideoAccelerator():
    IWMCodecAMVideoAccelerator = win32more.Media.WindowsMediaFormat.IWMCodecAMVideoAccelerator_head
    IWMCodecAMVideoAccelerator.SetAcceleratorInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DirectShow.IAMVideoAccelerator_head, use_last_error=False)(3, 'SetAcceleratorInterface', ((1, 'pIAMVA'),)))
    IWMCodecAMVideoAccelerator.NegotiateConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DirectShow.AM_MEDIA_TYPE_head), use_last_error=False)(4, 'NegotiateConnection', ((1, 'pMediaType'),)))
    IWMCodecAMVideoAccelerator.SetPlayerNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMPlayerTimestampHook_head, use_last_error=False)(5, 'SetPlayerNotify', ((1, 'pHook'),)))
    return IWMCodecAMVideoAccelerator
def _define_IWMCodecVideoAccelerator_head():
    class IWMCodecVideoAccelerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('990641b0-739f-4e94-a808-9888da8f75af')
    return IWMCodecVideoAccelerator
def _define_IWMCodecVideoAccelerator():
    IWMCodecVideoAccelerator = win32more.Media.WindowsMediaFormat.IWMCodecVideoAccelerator_head
    IWMCodecVideoAccelerator.NegotiateConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DirectShow.IAMVideoAccelerator_head,POINTER(win32more.Media.DirectShow.AM_MEDIA_TYPE_head), use_last_error=False)(3, 'NegotiateConnection', ((1, 'pIAMVA'),(1, 'pMediaType'),)))
    IWMCodecVideoAccelerator.SetPlayerNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.WindowsMediaFormat.IWMPlayerTimestampHook_head, use_last_error=False)(4, 'SetPlayerNotify', ((1, 'pHook'),)))
    return IWMCodecVideoAccelerator
NETSOURCE_URLCREDPOLICY_SETTINGS = Int32
NETSOURCE_URLCREDPOLICY_SETTING_SILENTLOGONOK = 0
NETSOURCE_URLCREDPOLICY_SETTING_MUSTPROMPTUSER = 1
NETSOURCE_URLCREDPOLICY_SETTING_ANONYMOUSONLY = 2
def _define_IWMSInternalAdminNetSource_head():
    class IWMSInternalAdminNetSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('8bb23e5f-d127-4afb-8d02-ae5b66d54c78')
    return IWMSInternalAdminNetSource
def _define_IWMSInternalAdminNetSource():
    IWMSInternalAdminNetSource = win32more.Media.WindowsMediaFormat.IWMSInternalAdminNetSource_head
    IWMSInternalAdminNetSource.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.Media.WindowsMediaFormat.INSNetSourceCreator_head,win32more.Foundation.BOOL, use_last_error=False)(3, 'Initialize', ((1, 'pSharedNamespace'),(1, 'pNamespaceNode'),(1, 'pNetSourceCreator'),(1, 'fEmbeddedInServer'),)))
    IWMSInternalAdminNetSource.GetNetSourceCreator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.INSNetSourceCreator_head), use_last_error=False)(4, 'GetNetSourceCreator', ((1, 'ppNetSourceCreator'),)))
    IWMSInternalAdminNetSource.SetCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(5, 'SetCredentials', ((1, 'bstrRealm'),(1, 'bstrName'),(1, 'bstrPassword'),(1, 'fPersist'),(1, 'fConfirmedGood'),)))
    IWMSInternalAdminNetSource.GetCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'GetCredentials', ((1, 'bstrRealm'),(1, 'pbstrName'),(1, 'pbstrPassword'),(1, 'pfConfirmedGood'),)))
    IWMSInternalAdminNetSource.DeleteCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'DeleteCredentials', ((1, 'bstrRealm'),)))
    IWMSInternalAdminNetSource.GetCredentialFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetCredentialFlags', ((1, 'lpdwFlags'),)))
    IWMSInternalAdminNetSource.SetCredentialFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetCredentialFlags', ((1, 'dwFlags'),)))
    IWMSInternalAdminNetSource.FindProxyForURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(10, 'FindProxyForURL', ((1, 'bstrProtocol'),(1, 'bstrHost'),(1, 'pfProxyEnabled'),(1, 'pbstrProxyServer'),(1, 'pdwProxyPort'),(1, 'pdwProxyContext'),)))
    IWMSInternalAdminNetSource.RegisterProxyFailure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'RegisterProxyFailure', ((1, 'hrParam'),(1, 'dwProxyContext'),)))
    IWMSInternalAdminNetSource.ShutdownProxyContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'ShutdownProxyContext', ((1, 'dwProxyContext'),)))
    IWMSInternalAdminNetSource.IsUsingIE = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'IsUsingIE', ((1, 'dwProxyContext'),(1, 'pfIsUsingIE'),)))
    return IWMSInternalAdminNetSource
def _define_IWMSInternalAdminNetSource2_head():
    class IWMSInternalAdminNetSource2(win32more.System.Com.IUnknown_head):
        Guid = Guid('e74d58c3-cf77-4b51-af17-744687c43eae')
    return IWMSInternalAdminNetSource2
def _define_IWMSInternalAdminNetSource2():
    IWMSInternalAdminNetSource2 = win32more.Media.WindowsMediaFormat.IWMSInternalAdminNetSource2_head
    IWMSInternalAdminNetSource2.SetCredentialsEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(3, 'SetCredentialsEx', ((1, 'bstrRealm'),(1, 'bstrUrl'),(1, 'fProxy'),(1, 'bstrName'),(1, 'bstrPassword'),(1, 'fPersist'),(1, 'fConfirmedGood'),)))
    IWMSInternalAdminNetSource2.GetCredentialsEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL,POINTER(win32more.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetCredentialsEx', ((1, 'bstrRealm'),(1, 'bstrUrl'),(1, 'fProxy'),(1, 'pdwUrlPolicy'),(1, 'pbstrName'),(1, 'pbstrPassword'),(1, 'pfConfirmedGood'),)))
    IWMSInternalAdminNetSource2.DeleteCredentialsEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL, use_last_error=False)(5, 'DeleteCredentialsEx', ((1, 'bstrRealm'),(1, 'bstrUrl'),(1, 'fProxy'),)))
    IWMSInternalAdminNetSource2.FindProxyForURLEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'FindProxyForURLEx', ((1, 'bstrProtocol'),(1, 'bstrHost'),(1, 'bstrUrl'),(1, 'pfProxyEnabled'),(1, 'pbstrProxyServer'),(1, 'pdwProxyPort'),(1, 'pdwProxyContext'),)))
    return IWMSInternalAdminNetSource2
def _define_IWMSInternalAdminNetSource3_head():
    class IWMSInternalAdminNetSource3(win32more.Media.WindowsMediaFormat.IWMSInternalAdminNetSource2_head):
        Guid = Guid('6b63d08e-4590-44af-9eb3-57ff1e73bf80')
    return IWMSInternalAdminNetSource3
def _define_IWMSInternalAdminNetSource3():
    IWMSInternalAdminNetSource3 = win32more.Media.WindowsMediaFormat.IWMSInternalAdminNetSource3_head
    IWMSInternalAdminNetSource3.GetNetSourceCreator2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'GetNetSourceCreator2', ((1, 'ppNetSourceCreator'),)))
    IWMSInternalAdminNetSource3.FindProxyForURLEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(UInt64), use_last_error=False)(8, 'FindProxyForURLEx2', ((1, 'bstrProtocol'),(1, 'bstrHost'),(1, 'bstrUrl'),(1, 'pfProxyEnabled'),(1, 'pbstrProxyServer'),(1, 'pdwProxyPort'),(1, 'pqwProxyContext'),)))
    IWMSInternalAdminNetSource3.RegisterProxyFailure2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt64, use_last_error=False)(9, 'RegisterProxyFailure2', ((1, 'hrParam'),(1, 'qwProxyContext'),)))
    IWMSInternalAdminNetSource3.ShutdownProxyContext2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(10, 'ShutdownProxyContext2', ((1, 'qwProxyContext'),)))
    IWMSInternalAdminNetSource3.IsUsingIE2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'IsUsingIE2', ((1, 'qwProxyContext'),(1, 'pfIsUsingIE'),)))
    IWMSInternalAdminNetSource3.SetCredentialsEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(12, 'SetCredentialsEx2', ((1, 'bstrRealm'),(1, 'bstrUrl'),(1, 'fProxy'),(1, 'bstrName'),(1, 'bstrPassword'),(1, 'fPersist'),(1, 'fConfirmedGood'),(1, 'fClearTextAuthentication'),)))
    IWMSInternalAdminNetSource3.GetCredentialsEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.Media.WindowsMediaFormat.NETSOURCE_URLCREDPOLICY_SETTINGS),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'GetCredentialsEx2', ((1, 'bstrRealm'),(1, 'bstrUrl'),(1, 'fProxy'),(1, 'fClearTextAuthentication'),(1, 'pdwUrlPolicy'),(1, 'pbstrName'),(1, 'pbstrPassword'),(1, 'pfConfirmedGood'),)))
    return IWMSInternalAdminNetSource3
def _define_WMIsContentProtected():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("WMIsContentProtected", windll["WMVCore"]), ((1, 'pwszFileName'),(1, 'pfIsProtected'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateWriter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Media.WindowsMediaFormat.IWMWriter_head), use_last_error=False)(("WMCreateWriter", windll["WMVCore"]), ((1, 'pUnkCert'),(1, 'ppWriter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateReader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMReader_head), use_last_error=False)(("WMCreateReader", windll["WMVCore"]), ((1, 'pUnkCert'),(1, 'dwRights'),(1, 'ppReader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateSyncReader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.Media.WindowsMediaFormat.IWMSyncReader_head), use_last_error=False)(("WMCreateSyncReader", windll["WMVCore"]), ((1, 'pUnkCert'),(1, 'dwRights'),(1, 'ppSyncReader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateEditor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMMetadataEditor_head), use_last_error=False)(("WMCreateEditor", windll["WMVCore"]), ((1, 'ppEditor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateIndexer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMIndexer_head), use_last_error=False)(("WMCreateIndexer", windll["WMVCore"]), ((1, 'ppIndexer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateBackupRestorer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Media.WindowsMediaFormat.IWMLicenseBackup_head), use_last_error=False)(("WMCreateBackupRestorer", windll["WMVCore"]), ((1, 'pCallback'),(1, 'ppBackup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateProfileManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMProfileManager_head), use_last_error=False)(("WMCreateProfileManager", windll["WMVCore"]), ((1, 'ppProfileManager'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateWriterFileSink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMWriterFileSink_head), use_last_error=False)(("WMCreateWriterFileSink", windll["WMVCore"]), ((1, 'ppSink'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateWriterNetworkSink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMWriterNetworkSink_head), use_last_error=False)(("WMCreateWriterNetworkSink", windll["WMVCore"]), ((1, 'ppSink'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WMCreateWriterPushSink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.WindowsMediaFormat.IWMWriterPushSink_head), use_last_error=False)(("WMCreateWriterPushSink", windll["WMVCore"]), ((1, 'ppSink'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WMT_VIDEOIMAGE_SAMPLE_INPUT_FRAME",
    "WMT_VIDEOIMAGE_SAMPLE_OUTPUT_FRAME",
    "WMT_VIDEOIMAGE_SAMPLE_USES_CURRENT_INPUT_FRAME",
    "WMT_VIDEOIMAGE_SAMPLE_USES_PREVIOUS_INPUT_FRAME",
    "WMT_VIDEOIMAGE_SAMPLE_MOTION",
    "WMT_VIDEOIMAGE_SAMPLE_ROTATION",
    "WMT_VIDEOIMAGE_SAMPLE_BLENDING",
    "WMT_VIDEOIMAGE_SAMPLE_ADV_BLENDING",
    "WMT_VIDEOIMAGE_INTEGER_DENOMINATOR",
    "WMT_VIDEOIMAGE_MAGIC_NUMBER",
    "WMT_VIDEOIMAGE_MAGIC_NUMBER_2",
    "WMT_VIDEOIMAGE_TRANSITION_BOW_TIE",
    "WMT_VIDEOIMAGE_TRANSITION_CIRCLE",
    "WMT_VIDEOIMAGE_TRANSITION_CROSS_FADE",
    "WMT_VIDEOIMAGE_TRANSITION_DIAGONAL",
    "WMT_VIDEOIMAGE_TRANSITION_DIAMOND",
    "WMT_VIDEOIMAGE_TRANSITION_FADE_TO_COLOR",
    "WMT_VIDEOIMAGE_TRANSITION_FILLED_V",
    "WMT_VIDEOIMAGE_TRANSITION_FLIP",
    "WMT_VIDEOIMAGE_TRANSITION_INSET",
    "WMT_VIDEOIMAGE_TRANSITION_IRIS",
    "WMT_VIDEOIMAGE_TRANSITION_PAGE_ROLL",
    "WMT_VIDEOIMAGE_TRANSITION_RECTANGLE",
    "WMT_VIDEOIMAGE_TRANSITION_REVEAL",
    "WMT_VIDEOIMAGE_TRANSITION_SLIDE",
    "WMT_VIDEOIMAGE_TRANSITION_SPLIT",
    "WMT_VIDEOIMAGE_TRANSITION_STAR",
    "WMT_VIDEOIMAGE_TRANSITION_WHEEL",
    "WM_SampleExtension_ContentType_Size",
    "WM_SampleExtension_PixelAspectRatio_Size",
    "WM_SampleExtension_Timecode_Size",
    "WM_SampleExtension_SampleDuration_Size",
    "WM_SampleExtension_ChromaLocation_Size",
    "WM_SampleExtension_ColorSpaceInfo_Size",
    "WM_CT_REPEAT_FIRST_FIELD",
    "WM_CT_BOTTOM_FIELD_FIRST",
    "WM_CT_TOP_FIELD_FIRST",
    "WM_CT_INTERLACED",
    "WM_CL_INTERLACED420",
    "WM_CL_PROGRESSIVE420",
    "WM_MAX_VIDEO_STREAMS",
    "WM_MAX_STREAMS",
    "WMDRM_IMPORT_INIT_STRUCT_DEFINED",
    "DRM_OPL_TYPES",
    "g_dwWMSpecialAttributes",
    "g_wszWMDuration",
    "g_wszWMBitrate",
    "g_wszWMSeekable",
    "g_wszWMStridable",
    "g_wszWMBroadcast",
    "g_wszWMProtected",
    "g_wszWMTrusted",
    "g_wszWMSignature_Name",
    "g_wszWMHasAudio",
    "g_wszWMHasImage",
    "g_wszWMHasScript",
    "g_wszWMHasVideo",
    "g_wszWMCurrentBitrate",
    "g_wszWMOptimalBitrate",
    "g_wszWMHasAttachedImages",
    "g_wszWMSkipBackward",
    "g_wszWMSkipForward",
    "g_wszWMNumberOfFrames",
    "g_wszWMFileSize",
    "g_wszWMHasArbitraryDataStream",
    "g_wszWMHasFileTransferStream",
    "g_wszWMContainerFormat",
    "g_dwWMContentAttributes",
    "g_wszWMTitle",
    "g_wszWMTitleSort",
    "g_wszWMAuthor",
    "g_wszWMAuthorSort",
    "g_wszWMDescription",
    "g_wszWMRating",
    "g_wszWMCopyright",
    "g_wszWMUse_DRM",
    "g_wszWMDRM_Flags",
    "g_wszWMDRM_Level",
    "g_wszWMUse_Advanced_DRM",
    "g_wszWMDRM_KeySeed",
    "g_wszWMDRM_KeyID",
    "g_wszWMDRM_ContentID",
    "g_wszWMDRM_SourceID",
    "g_wszWMDRM_IndividualizedVersion",
    "g_wszWMDRM_LicenseAcqURL",
    "g_wszWMDRM_V1LicenseAcqURL",
    "g_wszWMDRM_HeaderSignPrivKey",
    "g_wszWMDRM_LASignaturePrivKey",
    "g_wszWMDRM_LASignatureCert",
    "g_wszWMDRM_LASignatureLicSrvCert",
    "g_wszWMDRM_LASignatureRootCert",
    "g_wszWMAlbumTitle",
    "g_wszWMAlbumTitleSort",
    "g_wszWMTrack",
    "g_wszWMPromotionURL",
    "g_wszWMAlbumCoverURL",
    "g_wszWMGenre",
    "g_wszWMYear",
    "g_wszWMGenreID",
    "g_wszWMMCDI",
    "g_wszWMComposer",
    "g_wszWMComposerSort",
    "g_wszWMLyrics",
    "g_wszWMTrackNumber",
    "g_wszWMToolName",
    "g_wszWMToolVersion",
    "g_wszWMIsVBR",
    "g_wszWMAlbumArtist",
    "g_wszWMAlbumArtistSort",
    "g_wszWMBannerImageType",
    "g_wszWMBannerImageData",
    "g_wszWMBannerImageURL",
    "g_wszWMCopyrightURL",
    "g_wszWMAspectRatioX",
    "g_wszWMAspectRatioY",
    "g_wszASFLeakyBucketPairs",
    "g_dwWMNSCAttributes",
    "g_wszWMNSCName",
    "g_wszWMNSCAddress",
    "g_wszWMNSCPhone",
    "g_wszWMNSCEmail",
    "g_wszWMNSCDescription",
    "g_wszWMWriter",
    "g_wszWMConductor",
    "g_wszWMProducer",
    "g_wszWMDirector",
    "g_wszWMContentGroupDescription",
    "g_wszWMSubTitle",
    "g_wszWMPartOfSet",
    "g_wszWMProtectionType",
    "g_wszWMVideoHeight",
    "g_wszWMVideoWidth",
    "g_wszWMVideoFrameRate",
    "g_wszWMMediaClassPrimaryID",
    "g_wszWMMediaClassSecondaryID",
    "g_wszWMPeriod",
    "g_wszWMCategory",
    "g_wszWMPicture",
    "g_wszWMLyrics_Synchronised",
    "g_wszWMOriginalLyricist",
    "g_wszWMOriginalArtist",
    "g_wszWMOriginalAlbumTitle",
    "g_wszWMOriginalReleaseYear",
    "g_wszWMOriginalFilename",
    "g_wszWMPublisher",
    "g_wszWMEncodedBy",
    "g_wszWMEncodingSettings",
    "g_wszWMEncodingTime",
    "g_wszWMAuthorURL",
    "g_wszWMUserWebURL",
    "g_wszWMAudioFileURL",
    "g_wszWMAudioSourceURL",
    "g_wszWMLanguage",
    "g_wszWMParentalRating",
    "g_wszWMBeatsPerMinute",
    "g_wszWMInitialKey",
    "g_wszWMMood",
    "g_wszWMText",
    "g_wszWMDVDID",
    "g_wszWMWMContentID",
    "g_wszWMWMCollectionID",
    "g_wszWMWMCollectionGroupID",
    "g_wszWMUniqueFileIdentifier",
    "g_wszWMModifiedBy",
    "g_wszWMRadioStationName",
    "g_wszWMRadioStationOwner",
    "g_wszWMPlaylistDelay",
    "g_wszWMCodec",
    "g_wszWMDRM",
    "g_wszWMISRC",
    "g_wszWMProvider",
    "g_wszWMProviderRating",
    "g_wszWMProviderStyle",
    "g_wszWMContentDistributor",
    "g_wszWMSubscriptionContentID",
    "g_wszWMWMADRCPeakReference",
    "g_wszWMWMADRCPeakTarget",
    "g_wszWMWMADRCAverageReference",
    "g_wszWMWMADRCAverageTarget",
    "g_wszWMStreamTypeInfo",
    "g_wszWMPeakBitrate",
    "g_wszWMASFPacketCount",
    "g_wszWMASFSecurityObjectsSize",
    "g_wszWMSharedUserRating",
    "g_wszWMSubTitleDescription",
    "g_wszWMMediaCredits",
    "g_wszWMParentalRatingReason",
    "g_wszWMOriginalReleaseTime",
    "g_wszWMMediaStationCallSign",
    "g_wszWMMediaStationName",
    "g_wszWMMediaNetworkAffiliation",
    "g_wszWMMediaOriginalChannel",
    "g_wszWMMediaOriginalBroadcastDateTime",
    "g_wszWMMediaIsStereo",
    "g_wszWMVideoClosedCaptioning",
    "g_wszWMMediaIsRepeat",
    "g_wszWMMediaIsLive",
    "g_wszWMMediaIsTape",
    "g_wszWMMediaIsDelay",
    "g_wszWMMediaIsSubtitled",
    "g_wszWMMediaIsPremiere",
    "g_wszWMMediaIsFinale",
    "g_wszWMMediaIsSAP",
    "g_wszWMProviderCopyright",
    "g_wszWMISAN",
    "g_wszWMADID",
    "g_wszWMWMShadowFileSourceFileType",
    "g_wszWMWMShadowFileSourceDRMType",
    "g_wszWMWMCPDistributor",
    "g_wszWMWMCPDistributorID",
    "g_wszWMSeasonNumber",
    "g_wszWMEpisodeNumber",
    "g_wszEarlyDataDelivery",
    "g_wszJustInTimeDecode",
    "g_wszSingleOutputBuffer",
    "g_wszSoftwareScaling",
    "g_wszDeliverOnReceive",
    "g_wszScrambledAudio",
    "g_wszDedicatedDeliveryThread",
    "g_wszEnableDiscreteOutput",
    "g_wszSpeakerConfig",
    "g_wszDynamicRangeControl",
    "g_wszAllowInterlacedOutput",
    "g_wszVideoSampleDurations",
    "g_wszStreamLanguage",
    "g_wszEnableWMAProSPDIFOutput",
    "g_wszDeinterlaceMode",
    "g_wszInitialPatternForInverseTelecine",
    "g_wszJPEGCompressionQuality",
    "g_wszWatermarkCLSID",
    "g_wszWatermarkConfig",
    "g_wszInterlacedCoding",
    "g_wszFixedFrameRate",
    "g_wszOriginalSourceFormatTag",
    "g_wszOriginalWaveFormat",
    "g_wszEDL",
    "g_wszComplexity",
    "g_wszDecoderComplexityRequested",
    "g_wszReloadIndexOnSeek",
    "g_wszStreamNumIndexObjects",
    "g_wszFailSeekOnError",
    "g_wszPermitSeeksBeyondEndOfStream",
    "g_wszUsePacketAtSeekPoint",
    "g_wszSourceBufferTime",
    "g_wszSourceMaxBytesAtOnce",
    "g_wszVBREnabled",
    "g_wszVBRQuality",
    "g_wszVBRBitrateMax",
    "g_wszVBRBufferWindowMax",
    "g_wszVBRPeak",
    "g_wszBufferAverage",
    "g_wszComplexityMax",
    "g_wszComplexityOffline",
    "g_wszComplexityLive",
    "g_wszIsVBRSupported",
    "g_wszNumPasses",
    "g_wszMusicSpeechClassMode",
    "g_wszMusicClassMode",
    "g_wszSpeechClassMode",
    "g_wszMixedClassMode",
    "g_wszSpeechCaps",
    "g_wszPeakValue",
    "g_wszAverageLevel",
    "g_wszFold6To2Channels3",
    "g_wszFoldToChannelsTemplate",
    "g_wszDeviceConformanceTemplate",
    "g_wszEnableFrameInterpolation",
    "g_wszNeedsPreviousSample",
    "g_wszWMIsCompilation",
    "WMMEDIASUBTYPE_Base",
    "WMMEDIATYPE_Video",
    "WMMEDIASUBTYPE_RGB1",
    "WMMEDIASUBTYPE_RGB4",
    "WMMEDIASUBTYPE_RGB8",
    "WMMEDIASUBTYPE_RGB565",
    "WMMEDIASUBTYPE_RGB555",
    "WMMEDIASUBTYPE_RGB24",
    "WMMEDIASUBTYPE_RGB32",
    "WMMEDIASUBTYPE_I420",
    "WMMEDIASUBTYPE_IYUV",
    "WMMEDIASUBTYPE_YV12",
    "WMMEDIASUBTYPE_YUY2",
    "WMMEDIASUBTYPE_P422",
    "WMMEDIASUBTYPE_UYVY",
    "WMMEDIASUBTYPE_YVYU",
    "WMMEDIASUBTYPE_YVU9",
    "WMMEDIASUBTYPE_VIDEOIMAGE",
    "WMMEDIASUBTYPE_MP43",
    "WMMEDIASUBTYPE_MP4S",
    "WMMEDIASUBTYPE_M4S2",
    "WMMEDIASUBTYPE_WMV1",
    "WMMEDIASUBTYPE_WMV2",
    "WMMEDIASUBTYPE_MSS1",
    "WMMEDIASUBTYPE_MPEG2_VIDEO",
    "WMMEDIATYPE_Audio",
    "WMMEDIASUBTYPE_PCM",
    "WMMEDIASUBTYPE_DRM",
    "WMMEDIASUBTYPE_WMAudioV9",
    "WMMEDIASUBTYPE_WMAudio_Lossless",
    "WMMEDIASUBTYPE_MSS2",
    "WMMEDIASUBTYPE_WMSP1",
    "WMMEDIASUBTYPE_WMSP2",
    "WMMEDIASUBTYPE_WMV3",
    "WMMEDIASUBTYPE_WMVP",
    "WMMEDIASUBTYPE_WVP2",
    "WMMEDIASUBTYPE_WMVA",
    "WMMEDIASUBTYPE_WVC1",
    "WMMEDIASUBTYPE_WMAudioV8",
    "WMMEDIASUBTYPE_WMAudioV7",
    "WMMEDIASUBTYPE_WMAudioV2",
    "WMMEDIASUBTYPE_ACELPnet",
    "WMMEDIASUBTYPE_MP3",
    "WMMEDIASUBTYPE_WebStream",
    "WMMEDIATYPE_Script",
    "WMMEDIATYPE_Image",
    "WMMEDIATYPE_FileTransfer",
    "WMMEDIATYPE_Text",
    "WMFORMAT_VideoInfo",
    "WMFORMAT_MPEG2Video",
    "WMFORMAT_WaveFormatEx",
    "WMFORMAT_Script",
    "WMFORMAT_WebStream",
    "WMSCRIPTTYPE_TwoStrings",
    "WM_SampleExtensionGUID_OutputCleanPoint",
    "WM_SampleExtensionGUID_Timecode",
    "WM_SampleExtensionGUID_ChromaLocation",
    "WM_SampleExtensionGUID_ColorSpaceInfo",
    "WM_SampleExtensionGUID_UserDataInfo",
    "WM_SampleExtensionGUID_FileName",
    "WM_SampleExtensionGUID_ContentType",
    "WM_SampleExtensionGUID_PixelAspectRatio",
    "WM_SampleExtensionGUID_SampleDuration",
    "WM_SampleExtensionGUID_SampleProtectionSalt",
    "CLSID_WMMUTEX_Language",
    "CLSID_WMMUTEX_Bitrate",
    "CLSID_WMMUTEX_Presentation",
    "CLSID_WMMUTEX_Unknown",
    "CLSID_WMBandwidthSharing_Exclusive",
    "CLSID_WMBandwidthSharing_Partial",
    "WMT_DMOCATEGORY_AUDIO_WATERMARK",
    "WMT_DMOCATEGORY_VIDEO_WATERMARK",
    "CLSID_ClientNetManager",
    "IAMWMBufferPass",
    "IAMWMBufferPassCallback",
    "_AM_ASFWRITERCONFIG_PARAM",
    "AM_CONFIGASFWRITER_PARAM_AUTOINDEX",
    "AM_CONFIGASFWRITER_PARAM_MULTIPASS",
    "AM_CONFIGASFWRITER_PARAM_DONTCOMPRESS",
    "AM_WMT_EVENT_DATA",
    "INSSBuffer",
    "INSSBuffer2",
    "INSSBuffer3",
    "INSSBuffer4",
    "IWMSBufferAllocator",
    "WEBSTREAM_SAMPLE_TYPE",
    "WEBSTREAM_SAMPLE_TYPE_FILE",
    "WEBSTREAM_SAMPLE_TYPE_RENDER",
    "WM_SF_TYPE",
    "WM_SF_CLEANPOINT",
    "WM_SF_DISCONTINUITY",
    "WM_SF_DATALOSS",
    "WM_SFEX_TYPE",
    "WM_SFEX_NOTASYNCPOINT",
    "WM_SFEX_DATALOSS",
    "WMT_STATUS",
    "WMT_ERROR",
    "WMT_OPENED",
    "WMT_BUFFERING_START",
    "WMT_BUFFERING_STOP",
    "WMT_EOF",
    "WMT_END_OF_FILE",
    "WMT_END_OF_SEGMENT",
    "WMT_END_OF_STREAMING",
    "WMT_LOCATING",
    "WMT_CONNECTING",
    "WMT_NO_RIGHTS",
    "WMT_MISSING_CODEC",
    "WMT_STARTED",
    "WMT_STOPPED",
    "WMT_CLOSED",
    "WMT_STRIDING",
    "WMT_TIMER",
    "WMT_INDEX_PROGRESS",
    "WMT_SAVEAS_START",
    "WMT_SAVEAS_STOP",
    "WMT_NEW_SOURCEFLAGS",
    "WMT_NEW_METADATA",
    "WMT_BACKUPRESTORE_BEGIN",
    "WMT_SOURCE_SWITCH",
    "WMT_ACQUIRE_LICENSE",
    "WMT_INDIVIDUALIZE",
    "WMT_NEEDS_INDIVIDUALIZATION",
    "WMT_NO_RIGHTS_EX",
    "WMT_BACKUPRESTORE_END",
    "WMT_BACKUPRESTORE_CONNECTING",
    "WMT_BACKUPRESTORE_DISCONNECTING",
    "WMT_ERROR_WITHURL",
    "WMT_RESTRICTED_LICENSE",
    "WMT_CLIENT_CONNECT",
    "WMT_CLIENT_DISCONNECT",
    "WMT_NATIVE_OUTPUT_PROPS_CHANGED",
    "WMT_RECONNECT_START",
    "WMT_RECONNECT_END",
    "WMT_CLIENT_CONNECT_EX",
    "WMT_CLIENT_DISCONNECT_EX",
    "WMT_SET_FEC_SPAN",
    "WMT_PREROLL_READY",
    "WMT_PREROLL_COMPLETE",
    "WMT_CLIENT_PROPERTIES",
    "WMT_LICENSEURL_SIGNATURE_STATE",
    "WMT_INIT_PLAYLIST_BURN",
    "WMT_TRANSCRYPTOR_INIT",
    "WMT_TRANSCRYPTOR_SEEKED",
    "WMT_TRANSCRYPTOR_READ",
    "WMT_TRANSCRYPTOR_CLOSED",
    "WMT_PROXIMITY_RESULT",
    "WMT_PROXIMITY_COMPLETED",
    "WMT_CONTENT_ENABLER",
    "WMT_STREAM_SELECTION",
    "WMT_OFF",
    "WMT_CLEANPOINT_ONLY",
    "WMT_ON",
    "WMT_IMAGE_TYPE",
    "WMT_IT_NONE",
    "WMT_IT_BITMAP",
    "WMT_IT_JPEG",
    "WMT_IT_GIF",
    "WMT_ATTR_DATATYPE",
    "WMT_TYPE_DWORD",
    "WMT_TYPE_STRING",
    "WMT_TYPE_BINARY",
    "WMT_TYPE_BOOL",
    "WMT_TYPE_QWORD",
    "WMT_TYPE_WORD",
    "WMT_TYPE_GUID",
    "WMT_ATTR_IMAGETYPE",
    "WMT_IMAGETYPE_BITMAP",
    "WMT_IMAGETYPE_JPEG",
    "WMT_IMAGETYPE_GIF",
    "WMT_VERSION",
    "WMT_VER_4_0",
    "WMT_VER_7_0",
    "WMT_VER_8_0",
    "WMT_VER_9_0",
    "WMT_STORAGE_FORMAT",
    "WMT_Storage_Format_MP3",
    "WMT_Storage_Format_V1",
    "WMT_DRMLA_TRUST",
    "WMT_DRMLA_UNTRUSTED",
    "WMT_DRMLA_TRUSTED",
    "WMT_DRMLA_TAMPERED",
    "WMT_TRANSPORT_TYPE",
    "WMT_Transport_Type_Unreliable",
    "WMT_Transport_Type_Reliable",
    "WMT_NET_PROTOCOL",
    "WMT_PROTOCOL_HTTP",
    "WMT_PLAY_MODE",
    "WMT_PLAY_MODE_AUTOSELECT",
    "WMT_PLAY_MODE_LOCAL",
    "WMT_PLAY_MODE_DOWNLOAD",
    "WMT_PLAY_MODE_STREAMING",
    "WMT_PROXY_SETTINGS",
    "WMT_PROXY_SETTING_NONE",
    "WMT_PROXY_SETTING_MANUAL",
    "WMT_PROXY_SETTING_AUTO",
    "WMT_PROXY_SETTING_BROWSER",
    "WMT_PROXY_SETTING_MAX",
    "WMT_CODEC_INFO_TYPE",
    "WMT_CODECINFO_AUDIO",
    "WMT_CODECINFO_VIDEO",
    "WMT_CODECINFO_UNKNOWN",
    "WM_DM_INTERLACED_TYPE",
    "WM_DM_NOTINTERLACED",
    "WM_DM_DEINTERLACE_NORMAL",
    "WM_DM_DEINTERLACE_HALFSIZE",
    "WM_DM_DEINTERLACE_HALFSIZEDOUBLERATE",
    "WM_DM_DEINTERLACE_INVERSETELECINE",
    "WM_DM_DEINTERLACE_VERTICALHALFSIZEDOUBLERATE",
    "WM_DM_IT_FIRST_FRAME_COHERENCY",
    "WM_DM_IT_DISABLE_COHERENT_MODE",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_TOP",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_TOP",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_TOP",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_TOP",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_TOP",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_AA_BOTTOM",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BB_BOTTOM",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_BC_BOTTOM",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_CD_BOTTOM",
    "WM_DM_IT_FIRST_FRAME_IN_CLIP_IS_DD_BOTTOM",
    "WMT_OFFSET_FORMAT",
    "WMT_OFFSET_FORMAT_100NS",
    "WMT_OFFSET_FORMAT_FRAME_NUMBERS",
    "WMT_OFFSET_FORMAT_PLAYLIST_OFFSET",
    "WMT_OFFSET_FORMAT_TIMECODE",
    "WMT_OFFSET_FORMAT_100NS_APPROXIMATE",
    "WMT_INDEXER_TYPE",
    "WMT_IT_PRESENTATION_TIME",
    "WMT_IT_FRAME_NUMBERS",
    "WMT_IT_TIMECODE",
    "WMT_INDEX_TYPE",
    "WMT_IT_NEAREST_DATA_UNIT",
    "WMT_IT_NEAREST_OBJECT",
    "WMT_IT_NEAREST_CLEAN_POINT",
    "WMT_FILESINK_MODE",
    "WMT_FM_SINGLE_BUFFERS",
    "WMT_FM_FILESINK_DATA_UNITS",
    "WMT_FM_FILESINK_UNBUFFERED",
    "WMT_MUSICSPEECH_CLASS_MODE",
    "WMT_MS_CLASS_MUSIC",
    "WMT_MS_CLASS_SPEECH",
    "WMT_MS_CLASS_MIXED",
    "WMT_WATERMARK_ENTRY_TYPE",
    "WMT_WMETYPE_AUDIO",
    "WMT_WMETYPE_VIDEO",
    "WM_PLAYBACK_DRC_LEVEL",
    "WM_PLAYBACK_DRC_HIGH",
    "WM_PLAYBACK_DRC_MEDIUM",
    "WM_PLAYBACK_DRC_LOW",
    "WMT_TIMECODE_FRAMERATE",
    "WMT_TIMECODE_FRAMERATE_30",
    "WMT_TIMECODE_FRAMERATE_30DROP",
    "WMT_TIMECODE_FRAMERATE_25",
    "WMT_TIMECODE_FRAMERATE_24",
    "WMT_CREDENTIAL_FLAGS",
    "WMT_CREDENTIAL_SAVE",
    "WMT_CREDENTIAL_DONT_CACHE",
    "WMT_CREDENTIAL_CLEAR_TEXT",
    "WMT_CREDENTIAL_PROXY",
    "WMT_CREDENTIAL_ENCRYPT",
    "WM_AETYPE",
    "WM_AETYPE_INCLUDE",
    "WM_AETYPE_EXCLUDE",
    "WMT_RIGHTS",
    "WMT_RIGHT_PLAYBACK",
    "WMT_RIGHT_COPY_TO_NON_SDMI_DEVICE",
    "WMT_RIGHT_COPY_TO_CD",
    "WMT_RIGHT_COPY_TO_SDMI_DEVICE",
    "WMT_RIGHT_ONE_TIME",
    "WMT_RIGHT_SAVE_STREAM_PROTECTED",
    "WMT_RIGHT_COPY",
    "WMT_RIGHT_COLLABORATIVE_PLAY",
    "WMT_RIGHT_SDMI_TRIGGER",
    "WMT_RIGHT_SDMI_NOMORECOPIES",
    "WM_STREAM_PRIORITY_RECORD",
    "WM_WRITER_STATISTICS",
    "WM_WRITER_STATISTICS_EX",
    "WM_READER_STATISTICS",
    "WM_READER_CLIENTINFO",
    "WM_CLIENT_PROPERTIES",
    "WM_CLIENT_PROPERTIES_EX",
    "WM_PORT_NUMBER_RANGE",
    "WMT_BUFFER_SEGMENT",
    "WMT_PAYLOAD_FRAGMENT",
    "WMT_FILESINK_DATA_UNIT",
    "WMT_WEBSTREAM_FORMAT",
    "WMT_WEBSTREAM_SAMPLE_HEADER",
    "WM_ADDRESS_ACCESSENTRY",
    "WM_PICTURE",
    "WM_SYNCHRONISED_LYRICS",
    "WM_USER_WEB_URL",
    "WM_USER_TEXT",
    "WM_LEAKY_BUCKET_PAIR",
    "WM_STREAM_TYPE_INFO",
    "WMT_WATERMARK_ENTRY",
    "WMT_VIDEOIMAGE_SAMPLE",
    "WMT_VIDEOIMAGE_SAMPLE2",
    "WM_MEDIA_TYPE",
    "WMVIDEOINFOHEADER",
    "WMVIDEOINFOHEADER2",
    "WMMPEG2VIDEOINFO",
    "WMSCRIPTFORMAT",
    "WMT_COLORSPACEINFO_EXTENSION_DATA",
    "WMT_TIMECODE_EXTENSION_DATA",
    "DRM_VAL16",
    "IWMMediaProps",
    "IWMVideoMediaProps",
    "IWMWriter",
    "IWMDRMWriter",
    "WMDRM_IMPORT_INIT_STRUCT",
    "IWMDRMWriter2",
    "IWMDRMWriter3",
    "IWMInputMediaProps",
    "IWMPropertyVault",
    "IWMIStreamProps",
    "IWMReader",
    "IWMSyncReader",
    "IWMSyncReader2",
    "IWMOutputMediaProps",
    "IWMStatusCallback",
    "IWMReaderCallback",
    "IWMCredentialCallback",
    "IWMMetadataEditor",
    "IWMMetadataEditor2",
    "IWMDRMEditor",
    "IWMHeaderInfo",
    "IWMHeaderInfo2",
    "IWMHeaderInfo3",
    "IWMProfileManager",
    "IWMProfileManager2",
    "IWMProfileManagerLanguage",
    "IWMProfile",
    "IWMProfile2",
    "IWMProfile3",
    "IWMStreamConfig",
    "IWMStreamConfig2",
    "IWMStreamConfig3",
    "IWMPacketSize",
    "IWMPacketSize2",
    "IWMStreamList",
    "IWMMutualExclusion",
    "IWMMutualExclusion2",
    "IWMBandwidthSharing",
    "IWMStreamPrioritization",
    "IWMWriterAdvanced",
    "IWMWriterAdvanced2",
    "IWMWriterAdvanced3",
    "IWMWriterPreprocess",
    "IWMWriterPostViewCallback",
    "IWMWriterPostView",
    "IWMWriterSink",
    "IWMRegisterCallback",
    "IWMWriterFileSink",
    "IWMWriterFileSink2",
    "IWMWriterFileSink3",
    "IWMWriterNetworkSink",
    "IWMClientConnections",
    "IWMClientConnections2",
    "IWMReaderAdvanced",
    "IWMReaderAdvanced2",
    "IWMReaderAdvanced3",
    "IWMReaderAdvanced4",
    "IWMReaderAdvanced5",
    "IWMReaderAdvanced6",
    "IWMPlayerHook",
    "IWMReaderAllocatorEx",
    "IWMReaderTypeNegotiation",
    "IWMReaderCallbackAdvanced",
    "IWMDRMReader",
    "DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS",
    "DRM_OPL_OUTPUT_IDS",
    "DRM_OUTPUT_PROTECTION",
    "DRM_VIDEO_OUTPUT_PROTECTION_IDS",
    "DRM_PLAY_OPL",
    "DRM_COPY_OPL",
    "IWMDRMReader2",
    "IWMDRMReader3",
    "IWMReaderPlaylistBurn",
    "IWMReaderNetworkConfig",
    "IWMReaderNetworkConfig2",
    "IWMReaderStreamClock",
    "IWMIndexer",
    "IWMIndexer2",
    "IWMLicenseBackup",
    "IWMLicenseRestore",
    "IWMBackupRestoreProps",
    "IWMCodecInfo",
    "IWMCodecInfo2",
    "IWMCodecInfo3",
    "IWMLanguageList",
    "IWMWriterPushSink",
    "IWMDeviceRegistration",
    "IWMRegisteredDevice",
    "IWMProximityDetection",
    "IWMDRMMessageParser",
    "IWMDRMTranscryptor",
    "IWMDRMTranscryptor2",
    "IWMDRMTranscryptionManager",
    "IWMWatermarkInfo",
    "IWMReaderAccelerator",
    "IWMReaderTimecode",
    "IWMAddressAccess",
    "IWMAddressAccess2",
    "IWMImageInfo",
    "IWMLicenseRevocationAgent",
    "IWMAuthorizer",
    "IWMSecureChannel",
    "IWMGetSecureChannel",
    "INSNetSourceCreator",
    "IWMPlayerTimestampHook",
    "IWMCodecAMVideoAccelerator",
    "IWMCodecVideoAccelerator",
    "NETSOURCE_URLCREDPOLICY_SETTINGS",
    "NETSOURCE_URLCREDPOLICY_SETTING_SILENTLOGONOK",
    "NETSOURCE_URLCREDPOLICY_SETTING_MUSTPROMPTUSER",
    "NETSOURCE_URLCREDPOLICY_SETTING_ANONYMOUSONLY",
    "IWMSInternalAdminNetSource",
    "IWMSInternalAdminNetSource2",
    "IWMSInternalAdminNetSource3",
    "WMIsContentProtected",
    "WMCreateWriter",
    "WMCreateReader",
    "WMCreateSyncReader",
    "WMCreateEditor",
    "WMCreateIndexer",
    "WMCreateBackupRestorer",
    "WMCreateProfileManager",
    "WMCreateWriterFileSink",
    "WMCreateWriterNetworkSink",
    "WMCreateWriterPushSink",
]
