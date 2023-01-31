from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Direct3D9
import win32more.Graphics.DirectDraw
import win32more.Graphics.Gdi
import win32more.Media
import win32more.Media.Audio
import win32more.Media.Audio.DirectSound
import win32more.Media.DirectShow
import win32more.Media.KernelStreaming
import win32more.Media.MediaFoundation
import win32more.Media.WindowsMediaFormat
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Diagnostics.Etw
import win32more.System.Ole
import win32more.System.Registry
import win32more.UI.WindowsAndMessaging
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
ADVISE_TYPE = UInt32
ADVISE_NONE: ADVISE_TYPE = 0
ADVISE_CLIPPING: ADVISE_TYPE = 1
ADVISE_PALETTE: ADVISE_TYPE = 2
ADVISE_COLORKEY: ADVISE_TYPE = 4
ADVISE_POSITION: ADVISE_TYPE = 8
ADVISE_DISPLAY_CHANGE: ADVISE_TYPE = 16
class ALLOCATOR_PROPERTIES(Structure):
    cBuffers: Int32
    cbBuffer: Int32
    cbAlign: Int32
    cbPrefix: Int32
class AMCOPPCommand(Structure):
    macKDI: Guid
    guidCommandID: Guid
    dwSequence: UInt32
    cbSizeData: UInt32
    CommandData: Byte * 4056
class AMCOPPSignature(Structure):
    Signature: Byte * 256
class AMCOPPStatusInput(Structure):
    rApp: Guid
    guidStatusRequestID: Guid
    dwSequence: UInt32
    cbSizeData: UInt32
    StatusData: Byte * 4056
class AMCOPPStatusOutput(Structure):
    macKDI: Guid
    cbSizeData: UInt32
    COPPStatus: Byte * 4076
AMExtendedSeekingCapabilities = Int32
AM_EXSEEK_CANSEEK: AMExtendedSeekingCapabilities = 1
AM_EXSEEK_CANSCAN: AMExtendedSeekingCapabilities = 2
AM_EXSEEK_MARKERSEEK: AMExtendedSeekingCapabilities = 4
AM_EXSEEK_SCANWITHOUTCLOCK: AMExtendedSeekingCapabilities = 8
AM_EXSEEK_NOSTANDARDREPAINT: AMExtendedSeekingCapabilities = 16
AM_EXSEEK_BUFFERING: AMExtendedSeekingCapabilities = 32
AM_EXSEEK_SENDS_VIDEOFRAMEREADY: AMExtendedSeekingCapabilities = 64
@winfunctype_pointer
def AMGETERRORTEXTPROCA(param0: win32more.Foundation.HRESULT, param1: win32more.Foundation.PSTR, param2: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def AMGETERRORTEXTPROCW(param0: win32more.Foundation.HRESULT, param1: win32more.Foundation.PWSTR, param2: UInt32) -> win32more.Foundation.BOOL: ...
AMMSF_MMS_INIT_FLAGS = UInt32
AMMSF_NOGRAPHTHREAD: AMMSF_MMS_INIT_FLAGS = 1
AMMSF_MS_FLAGS = UInt32
AMMSF_ADDDEFAULTRENDERER: AMMSF_MS_FLAGS = 1
AMMSF_CREATEPEER: AMMSF_MS_FLAGS = 2
AMMSF_STOPIFNOSAMPLES: AMMSF_MS_FLAGS = 4
AMMSF_NOSTALL: AMMSF_MS_FLAGS = 8
AMMSF_RENDER_FLAGS = UInt32
AMMSF_RENDERTYPEMASK: AMMSF_RENDER_FLAGS = 3
AMMSF_RENDERTOEXISTING: AMMSF_RENDER_FLAGS = 0
AMMSF_RENDERALLSTREAMS: AMMSF_RENDER_FLAGS = 1
AMMSF_NORENDER: AMMSF_RENDER_FLAGS = 2
AMMSF_NOCLOCK: AMMSF_RENDER_FLAGS = 4
AMMSF_RUN: AMMSF_RENDER_FLAGS = 8
AMOVERLAYFX = Int32
AMOVERFX_NOFX: AMOVERLAYFX = 0
AMOVERFX_MIRRORLEFTRIGHT: AMOVERLAYFX = 2
AMOVERFX_MIRRORUPDOWN: AMOVERLAYFX = 4
AMOVERFX_DEINTERLACE: AMOVERLAYFX = 8
AMPROPERTY_PIN = Int32
AMPROPERTY_PIN_CATEGORY: AMPROPERTY_PIN = 0
AMPROPERTY_PIN_MEDIUM: AMPROPERTY_PIN = 1
AMPlayListEventFlags = Int32
AMPLAYLISTEVENT_RESUME: AMPlayListEventFlags = 0
AMPLAYLISTEVENT_BREAK: AMPlayListEventFlags = 1
AMPLAYLISTEVENT_NEXT: AMPlayListEventFlags = 2
AMPLAYLISTEVENT_MASK: AMPlayListEventFlags = 15
AMPLAYLISTEVENT_REFRESH: AMPlayListEventFlags = 16
AMPlayListFlags = Int32
AMPLAYLIST_STARTINSCANMODE: AMPlayListFlags = 1
AMPLAYLIST_FORCEBANNER: AMPlayListFlags = 2
AMPlayListItemFlags = Int32
AMPLAYLISTITEM_CANSKIP: AMPlayListItemFlags = 1
AMPLAYLISTITEM_CANBIND: AMPlayListItemFlags = 2
AMTVAudioEventType = Int32
AMTVAUDIO_EVENT_CHANGED: AMTVAudioEventType = 1
AMTunerEventType = Int32
AMTUNER_EVENT_CHANGED: AMTunerEventType = 1
AMTunerModeType = Int32
AMTUNER_MODE_DEFAULT: AMTunerModeType = 0
AMTUNER_MODE_TV: AMTunerModeType = 1
AMTUNER_MODE_FM_RADIO: AMTunerModeType = 2
AMTUNER_MODE_AM_RADIO: AMTunerModeType = 4
AMTUNER_MODE_DSS: AMTunerModeType = 8
AMTunerSignalStrength = Int32
AMTUNER_HASNOSIGNALSTRENGTH: AMTunerSignalStrength = -1
AMTUNER_NOSIGNAL: AMTunerSignalStrength = 0
AMTUNER_SIGNALPRESENT: AMTunerSignalStrength = 1
AMTunerSubChannel = Int32
AMTUNER_SUBCHAN_NO_TUNE: AMTunerSubChannel = -2
AMTUNER_SUBCHAN_DEFAULT: AMTunerSubChannel = -1
class AMVABUFFERINFO(Structure):
    dwTypeIndex: UInt32
    dwBufferIndex: UInt32
    dwDataOffset: UInt32
    dwDataSize: UInt32
class AMVABeginFrameInfo(Structure):
    dwDestSurfaceIndex: UInt32
    pInputData: c_void_p
    dwSizeInputData: UInt32
    pOutputData: c_void_p
    dwSizeOutputData: UInt32
class AMVACompBufferInfo(Structure):
    dwNumCompBuffers: UInt32
    dwWidthToCreate: UInt32
    dwHeightToCreate: UInt32
    dwBytesToAllocate: UInt32
    ddCompCaps: win32more.Graphics.DirectDraw.DDSCAPS2
    ddPixelFormat: win32more.Graphics.DirectDraw.DDPIXELFORMAT
class AMVAEndFrameInfo(Structure):
    dwSizeMiscData: UInt32
    pMiscData: c_void_p
class AMVAInternalMemInfo(Structure):
    dwScratchMemAlloc: UInt32
class AMVAUncompBufferInfo(Structure):
    dwMinNumSurfaces: UInt32
    dwMaxNumSurfaces: UInt32
    ddUncompPixelFormat: win32more.Graphics.DirectDraw.DDPIXELFORMAT
class AMVAUncompDataInfo(Structure):
    dwUncompWidth: UInt32
    dwUncompHeight: UInt32
    ddUncompPixelFormat: win32more.Graphics.DirectDraw.DDPIXELFORMAT
class AMVPDATAINFO(Structure):
    dwSize: UInt32
    dwMicrosecondsPerField: UInt32
    amvpDimInfo: win32more.Media.DirectShow.AMVPDIMINFO
    dwPictAspectRatioX: UInt32
    dwPictAspectRatioY: UInt32
    bEnableDoubleClock: win32more.Foundation.BOOL
    bEnableVACT: win32more.Foundation.BOOL
    bDataIsInterlaced: win32more.Foundation.BOOL
    lHalfLinesOdd: Int32
    bFieldPolarityInverted: win32more.Foundation.BOOL
    dwNumLinesInVREF: UInt32
    lHalfLinesEven: Int32
    dwReserved1: UInt32
class AMVPDIMINFO(Structure):
    dwFieldWidth: UInt32
    dwFieldHeight: UInt32
    dwVBIWidth: UInt32
    dwVBIHeight: UInt32
    rcValidRegion: win32more.Foundation.RECT
class AMVPSIZE(Structure):
    dwWidth: UInt32
    dwHeight: UInt32
AMVP_MODE = Int32
AMVP_MODE_WEAVE: AMVP_MODE = 0
AMVP_MODE_BOBINTERLEAVED: AMVP_MODE = 1
AMVP_MODE_BOBNONINTERLEAVED: AMVP_MODE = 2
AMVP_MODE_SKIPEVEN: AMVP_MODE = 3
AMVP_MODE_SKIPODD: AMVP_MODE = 4
AMVP_SELECT_FORMAT_BY = Int32
AMVP_DO_NOT_CARE: AMVP_SELECT_FORMAT_BY = 0
AMVP_BEST_BANDWIDTH: AMVP_SELECT_FORMAT_BY = 1
AMVP_INPUT_SAME_AS_OUTPUT: AMVP_SELECT_FORMAT_BY = 2
class AM_AC3_ALTERNATE_AUDIO(Structure):
    fStereo: win32more.Foundation.BOOL
    DualMode: UInt32
class AM_AC3_BIT_STREAM_MODE(Structure):
    BitStreamMode: Int32
class AM_AC3_DIALOGUE_LEVEL(Structure):
    DialogueLevel: UInt32
class AM_AC3_DOWNMIX(Structure):
    fDownMix: win32more.Foundation.BOOL
    fDolbySurround: win32more.Foundation.BOOL
class AM_AC3_ERROR_CONCEALMENT(Structure):
    fRepeatPreviousBlock: win32more.Foundation.BOOL
    fErrorInCurrentBlock: win32more.Foundation.BOOL
class AM_AC3_ROOM_TYPE(Structure):
    fLargeRoom: win32more.Foundation.BOOL
AM_ASPECT_RATIO_MODE = Int32
AM_ARMODE_STRETCHED: AM_ASPECT_RATIO_MODE = 0
AM_ARMODE_LETTER_BOX: AM_ASPECT_RATIO_MODE = 1
AM_ARMODE_CROP: AM_ASPECT_RATIO_MODE = 2
AM_ARMODE_STRETCHED_AS_PRIMARY: AM_ASPECT_RATIO_MODE = 3
class AM_COLCON(Structure):
    _bitfield1: Byte
    _bitfield2: Byte
    _bitfield3: Byte
    _bitfield4: Byte
class AM_COPY_MACROVISION(Structure):
    MACROVISIONLevel: UInt32
AM_COPY_MACROVISION_LEVEL = Int32
AM_MACROVISION_DISABLED: AM_COPY_MACROVISION_LEVEL = 0
AM_MACROVISION_LEVEL1: AM_COPY_MACROVISION_LEVEL = 1
AM_MACROVISION_LEVEL2: AM_COPY_MACROVISION_LEVEL = 2
AM_MACROVISION_LEVEL3: AM_COPY_MACROVISION_LEVEL = 3
AM_DIGITAL_CP = Int32
AM_DIGITAL_CP_OFF: AM_DIGITAL_CP = 0
AM_DIGITAL_CP_ON: AM_DIGITAL_CP = 1
AM_DIGITAL_CP_DVD_COMPLIANT: AM_DIGITAL_CP = 2
AM_DVDCOPYSTATE = Int32
AM_DVDCOPYSTATE_INITIALIZE: AM_DVDCOPYSTATE = 0
AM_DVDCOPYSTATE_INITIALIZE_TITLE: AM_DVDCOPYSTATE = 1
AM_DVDCOPYSTATE_AUTHENTICATION_NOT_REQUIRED: AM_DVDCOPYSTATE = 2
AM_DVDCOPYSTATE_AUTHENTICATION_REQUIRED: AM_DVDCOPYSTATE = 3
AM_DVDCOPYSTATE_DONE: AM_DVDCOPYSTATE = 4
class AM_DVDCOPY_BUSKEY(Structure):
    BusKey: Byte * 5
    Reserved: Byte * 1
class AM_DVDCOPY_CHLGKEY(Structure):
    ChlgKey: Byte * 10
    Reserved: Byte * 2
class AM_DVDCOPY_DISCKEY(Structure):
    DiscKey: Byte * 2048
class AM_DVDCOPY_SET_COPY_STATE(Structure):
    DVDCopyState: UInt32
class AM_DVDCOPY_TITLEKEY(Structure):
    KeyFlags: UInt32
    Reserved1: UInt32 * 2
    TitleKey: Byte * 6
    Reserved2: Byte * 2
class AM_DVD_ChangeRate(Structure):
    StartInTime: Int64
    StartOutTime: Int64
    Rate: Int32
AM_DVD_GRAPH_FLAGS = Int32
AM_DVD_HWDEC_PREFER: AM_DVD_GRAPH_FLAGS = 1
AM_DVD_HWDEC_ONLY: AM_DVD_GRAPH_FLAGS = 2
AM_DVD_SWDEC_PREFER: AM_DVD_GRAPH_FLAGS = 4
AM_DVD_SWDEC_ONLY: AM_DVD_GRAPH_FLAGS = 8
AM_DVD_NOVPE: AM_DVD_GRAPH_FLAGS = 256
AM_DVD_DO_NOT_CLEAR: AM_DVD_GRAPH_FLAGS = 512
AM_DVD_VMR9_ONLY: AM_DVD_GRAPH_FLAGS = 2048
AM_DVD_EVR_ONLY: AM_DVD_GRAPH_FLAGS = 4096
AM_DVD_EVR_QOS: AM_DVD_GRAPH_FLAGS = 8192
AM_DVD_ADAPT_GRAPH: AM_DVD_GRAPH_FLAGS = 16384
AM_DVD_MASK: AM_DVD_GRAPH_FLAGS = 65535
class AM_DVD_RENDERSTATUS(Structure):
    hrVPEStatus: win32more.Foundation.HRESULT
    bDvdVolInvalid: win32more.Foundation.BOOL
    bDvdVolUnknown: win32more.Foundation.BOOL
    bNoLine21In: win32more.Foundation.BOOL
    bNoLine21Out: win32more.Foundation.BOOL
    iNumStreams: Int32
    iNumStreamsFailed: Int32
    dwFailedStreamsFlag: UInt32
AM_DVD_STREAM_FLAGS = Int32
AM_DVD_STREAM_VIDEO: AM_DVD_STREAM_FLAGS = 1
AM_DVD_STREAM_AUDIO: AM_DVD_STREAM_FLAGS = 2
AM_DVD_STREAM_SUBPIC: AM_DVD_STREAM_FLAGS = 4
class AM_DVD_YUV(Structure):
    Reserved: Byte
    Y: Byte
    U: Byte
    V: Byte
class AM_DvdKaraokeData(Structure):
    dwDownmix: UInt32
    dwSpeakerAssignment: UInt32
class AM_ExactRateChange(Structure):
    OutputZeroTime: Int64
    Rate: Int32
AM_FILESINK_FLAGS = Int32
AM_FILE_OVERWRITE: AM_FILESINK_FLAGS = 1
AM_FILTER_FLAGS = Int32
AM_FILTER_FLAGS_REMOVABLE: AM_FILTER_FLAGS = 1
class AM_FRAMESTEP_STEP(Structure):
    dwFramesToStep: UInt32
AM_GRAPH_CONFIG_RECONNECT_FLAGS = Int32
AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT: AM_GRAPH_CONFIG_RECONNECT_FLAGS = 1
AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS: AM_GRAPH_CONFIG_RECONNECT_FLAGS = 2
AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS: AM_GRAPH_CONFIG_RECONNECT_FLAGS = 4
AM_LINE21_CCLEVEL = Int32
AM_L21_CCLEVEL_TC2: AM_LINE21_CCLEVEL = 0
AM_LINE21_CCSERVICE = Int32
AM_L21_CCSERVICE_None: AM_LINE21_CCSERVICE = 0
AM_L21_CCSERVICE_Caption1: AM_LINE21_CCSERVICE = 1
AM_L21_CCSERVICE_Caption2: AM_LINE21_CCSERVICE = 2
AM_L21_CCSERVICE_Text1: AM_LINE21_CCSERVICE = 3
AM_L21_CCSERVICE_Text2: AM_LINE21_CCSERVICE = 4
AM_L21_CCSERVICE_XDS: AM_LINE21_CCSERVICE = 5
AM_L21_CCSERVICE_DefChannel: AM_LINE21_CCSERVICE = 10
AM_L21_CCSERVICE_Invalid: AM_LINE21_CCSERVICE = 11
AM_LINE21_CCSTATE = Int32
AM_L21_CCSTATE_Off: AM_LINE21_CCSTATE = 0
AM_L21_CCSTATE_On: AM_LINE21_CCSTATE = 1
AM_LINE21_CCSTYLE = Int32
AM_L21_CCSTYLE_None: AM_LINE21_CCSTYLE = 0
AM_L21_CCSTYLE_PopOn: AM_LINE21_CCSTYLE = 1
AM_L21_CCSTYLE_PaintOn: AM_LINE21_CCSTYLE = 2
AM_L21_CCSTYLE_RollUp: AM_LINE21_CCSTYLE = 3
AM_LINE21_DRAWBGMODE = Int32
AM_L21_DRAWBGMODE_Opaque: AM_LINE21_DRAWBGMODE = 0
AM_L21_DRAWBGMODE_Transparent: AM_LINE21_DRAWBGMODE = 1
AM_MEDIAEVENT_FLAGS = Int32
AM_MEDIAEVENT_NONOTIFY: AM_MEDIAEVENT_FLAGS = 1
AM_MPEG2Level = Int32
AM_MPEG2Level_Low: AM_MPEG2Level = 1
AM_MPEG2Level_Main: AM_MPEG2Level = 2
AM_MPEG2Level_High1440: AM_MPEG2Level = 3
AM_MPEG2Level_High: AM_MPEG2Level = 4
AM_MPEG2Profile = Int32
AM_MPEG2Profile_Simple: AM_MPEG2Profile = 1
AM_MPEG2Profile_Main: AM_MPEG2Profile = 2
AM_MPEG2Profile_SNRScalable: AM_MPEG2Profile = 3
AM_MPEG2Profile_SpatiallyScalable: AM_MPEG2Profile = 4
AM_MPEG2Profile_High: AM_MPEG2Profile = 5
class AM_MPEGSTREAMTYPE(Structure):
    dwStreamId: UInt32
    dwReserved: UInt32
    mt: win32more.Media.MediaFoundation.AM_MEDIA_TYPE
    bFormat: Byte * 1
class AM_MPEGSYSTEMTYPE(Structure):
    dwBitRate: UInt32
    cStreams: UInt32
    Streams: win32more.Media.DirectShow.AM_MPEGSTREAMTYPE * 1
AM_PROPERTY_AC3 = Int32
AM_PROPERTY_AC3_ERROR_CONCEALMENT: AM_PROPERTY_AC3 = 1
AM_PROPERTY_AC3_ALTERNATE_AUDIO: AM_PROPERTY_AC3 = 2
AM_PROPERTY_AC3_DOWNMIX: AM_PROPERTY_AC3 = 3
AM_PROPERTY_AC3_BIT_STREAM_MODE: AM_PROPERTY_AC3 = 4
AM_PROPERTY_AC3_DIALOGUE_LEVEL: AM_PROPERTY_AC3 = 5
AM_PROPERTY_AC3_LANGUAGE_CODE: AM_PROPERTY_AC3 = 6
AM_PROPERTY_AC3_ROOM_TYPE: AM_PROPERTY_AC3 = 7
AM_PROPERTY_DVDCOPYPROT = Int32
AM_PROPERTY_DVDCOPY_CHLG_KEY: AM_PROPERTY_DVDCOPYPROT = 1
AM_PROPERTY_DVDCOPY_DVD_KEY1: AM_PROPERTY_DVDCOPYPROT = 2
AM_PROPERTY_DVDCOPY_DEC_KEY2: AM_PROPERTY_DVDCOPYPROT = 3
AM_PROPERTY_DVDCOPY_TITLE_KEY: AM_PROPERTY_DVDCOPYPROT = 4
AM_PROPERTY_COPY_MACROVISION: AM_PROPERTY_DVDCOPYPROT = 5
AM_PROPERTY_DVDCOPY_REGION: AM_PROPERTY_DVDCOPYPROT = 6
AM_PROPERTY_DVDCOPY_SET_COPY_STATE: AM_PROPERTY_DVDCOPYPROT = 7
AM_PROPERTY_COPY_ANALOG_COMPONENT: AM_PROPERTY_DVDCOPYPROT = 8
AM_PROPERTY_COPY_DIGITAL_CP: AM_PROPERTY_DVDCOPYPROT = 9
AM_PROPERTY_COPY_DVD_SRM: AM_PROPERTY_DVDCOPYPROT = 10
AM_PROPERTY_DVDCOPY_SUPPORTS_NEW_KEYCOUNT: AM_PROPERTY_DVDCOPYPROT = 11
AM_PROPERTY_DVDCOPY_DISC_KEY: AM_PROPERTY_DVDCOPYPROT = 128
AM_PROPERTY_DVDKARAOKE = Int32
AM_PROPERTY_DVDKARAOKE_ENABLE: AM_PROPERTY_DVDKARAOKE = 0
AM_PROPERTY_DVDKARAOKE_DATA: AM_PROPERTY_DVDKARAOKE = 1
AM_PROPERTY_DVDSUBPIC = Int32
AM_PROPERTY_DVDSUBPIC_PALETTE: AM_PROPERTY_DVDSUBPIC = 0
AM_PROPERTY_DVDSUBPIC_HLI: AM_PROPERTY_DVDSUBPIC = 1
AM_PROPERTY_DVDSUBPIC_COMPOSIT_ON: AM_PROPERTY_DVDSUBPIC = 2
AM_PROPERTY_DVD_RATE_CHANGE = Int32
AM_RATE_ChangeRate: AM_PROPERTY_DVD_RATE_CHANGE = 1
AM_RATE_FullDataRateMax: AM_PROPERTY_DVD_RATE_CHANGE = 2
AM_RATE_ReverseDecode: AM_PROPERTY_DVD_RATE_CHANGE = 3
AM_RATE_DecoderPosition: AM_PROPERTY_DVD_RATE_CHANGE = 4
AM_RATE_DecoderVersion: AM_PROPERTY_DVD_RATE_CHANGE = 5
AM_PROPERTY_FRAMESTEP = Int32
AM_PROPERTY_FRAMESTEP_STEP: AM_PROPERTY_FRAMESTEP = 1
AM_PROPERTY_FRAMESTEP_CANCEL: AM_PROPERTY_FRAMESTEP = 2
AM_PROPERTY_FRAMESTEP_CANSTEP: AM_PROPERTY_FRAMESTEP = 3
AM_PROPERTY_FRAMESTEP_CANSTEPMULTIPLE: AM_PROPERTY_FRAMESTEP = 4
class AM_PROPERTY_SPHLI(Structure):
    HLISS: UInt16
    Reserved: UInt16
    StartPTM: UInt32
    EndPTM: UInt32
    StartX: UInt16
    StartY: UInt16
    StopX: UInt16
    StopY: UInt16
    ColCon: win32more.Media.DirectShow.AM_COLCON
class AM_PROPERTY_SPPAL(Structure):
    sppal: win32more.Media.DirectShow.AM_DVD_YUV * 16
AM_PROPERTY_TS_RATE_CHANGE = Int32
AM_RATE_SimpleRateChange: AM_PROPERTY_TS_RATE_CHANGE = 1
AM_RATE_ExactRateChange: AM_PROPERTY_TS_RATE_CHANGE = 2
AM_RATE_MaxFullDataRate: AM_PROPERTY_TS_RATE_CHANGE = 3
AM_RATE_Step: AM_PROPERTY_TS_RATE_CHANGE = 4
AM_RATE_UseRateVersion: AM_PROPERTY_TS_RATE_CHANGE = 5
AM_RATE_QueryFullFrameRate: AM_PROPERTY_TS_RATE_CHANGE = 6
AM_RATE_QueryLastRateSegPTS: AM_PROPERTY_TS_RATE_CHANGE = 7
AM_RATE_CorrectTS: AM_PROPERTY_TS_RATE_CHANGE = 8
AM_RATE_ReverseMaxFullDataRate: AM_PROPERTY_TS_RATE_CHANGE = 9
AM_RATE_ResetOnTimeDisc: AM_PROPERTY_TS_RATE_CHANGE = 10
AM_RATE_QueryMapping: AM_PROPERTY_TS_RATE_CHANGE = 11
class AM_QueryRate(Structure):
    lMaxForwardFullFrame: Int32
    lMaxReverseFullFrame: Int32
class AM_SAMPLE2_PROPERTIES(Structure):
    cbData: UInt32
    dwTypeSpecificFlags: UInt32
    dwSampleFlags: UInt32
    lActual: Int32
    tStart: Int64
    tStop: Int64
    dwStreamId: UInt32
    pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)
    pbBuffer: c_char_p_no
    cbBuffer: Int32
AM_SAMPLE_PROPERTY_FLAGS = Int32
AM_SAMPLE_SPLICEPOINT: AM_SAMPLE_PROPERTY_FLAGS = 1
AM_SAMPLE_PREROLL: AM_SAMPLE_PROPERTY_FLAGS = 2
AM_SAMPLE_DATADISCONTINUITY: AM_SAMPLE_PROPERTY_FLAGS = 4
AM_SAMPLE_TYPECHANGED: AM_SAMPLE_PROPERTY_FLAGS = 8
AM_SAMPLE_TIMEVALID: AM_SAMPLE_PROPERTY_FLAGS = 16
AM_SAMPLE_TIMEDISCONTINUITY: AM_SAMPLE_PROPERTY_FLAGS = 64
AM_SAMPLE_FLUSH_ON_PAUSE: AM_SAMPLE_PROPERTY_FLAGS = 128
AM_SAMPLE_STOPVALID: AM_SAMPLE_PROPERTY_FLAGS = 256
AM_SAMPLE_ENDOFSTREAM: AM_SAMPLE_PROPERTY_FLAGS = 512
AM_STREAM_MEDIA: AM_SAMPLE_PROPERTY_FLAGS = 0
AM_STREAM_CONTROL: AM_SAMPLE_PROPERTY_FLAGS = 1
AM_SEEKING_SEEKING_CAPABILITIES = Int32
AM_SEEKING_CanSeekAbsolute: AM_SEEKING_SEEKING_CAPABILITIES = 1
AM_SEEKING_CanSeekForwards: AM_SEEKING_SEEKING_CAPABILITIES = 2
AM_SEEKING_CanSeekBackwards: AM_SEEKING_SEEKING_CAPABILITIES = 4
AM_SEEKING_CanGetCurrentPos: AM_SEEKING_SEEKING_CAPABILITIES = 8
AM_SEEKING_CanGetStopPos: AM_SEEKING_SEEKING_CAPABILITIES = 16
AM_SEEKING_CanGetDuration: AM_SEEKING_SEEKING_CAPABILITIES = 32
AM_SEEKING_CanPlayBackwards: AM_SEEKING_SEEKING_CAPABILITIES = 64
AM_SEEKING_CanDoSegments: AM_SEEKING_SEEKING_CAPABILITIES = 128
AM_SEEKING_Source: AM_SEEKING_SEEKING_CAPABILITIES = 256
AM_SEEKING_SEEKING_FLAGS = Int32
AM_SEEKING_NoPositioning: AM_SEEKING_SEEKING_FLAGS = 0
AM_SEEKING_AbsolutePositioning: AM_SEEKING_SEEKING_FLAGS = 1
AM_SEEKING_RelativePositioning: AM_SEEKING_SEEKING_FLAGS = 2
AM_SEEKING_IncrementalPositioning: AM_SEEKING_SEEKING_FLAGS = 3
AM_SEEKING_PositioningBitsMask: AM_SEEKING_SEEKING_FLAGS = 3
AM_SEEKING_SeekToKeyFrame: AM_SEEKING_SEEKING_FLAGS = 4
AM_SEEKING_ReturnTime: AM_SEEKING_SEEKING_FLAGS = 8
AM_SEEKING_Segment: AM_SEEKING_SEEKING_FLAGS = 16
AM_SEEKING_NoFlush: AM_SEEKING_SEEKING_FLAGS = 32
class AM_STREAM_INFO(Structure):
    tStart: Int64
    tStop: Int64
    dwStartCookie: UInt32
    dwStopCookie: UInt32
    dwFlags: UInt32
AM_STREAM_INFO_FLAGS = Int32
AM_STREAM_INFO_START_DEFINED: AM_STREAM_INFO_FLAGS = 1
AM_STREAM_INFO_STOP_DEFINED: AM_STREAM_INFO_FLAGS = 2
AM_STREAM_INFO_DISCARDING: AM_STREAM_INFO_FLAGS = 4
AM_STREAM_INFO_STOP_SEND_EXTRA: AM_STREAM_INFO_FLAGS = 16
class AM_SimpleRateChange(Structure):
    StartTime: Int64
    Rate: Int32
AM_WST_DRAWBGMODE = Int32
AM_WST_DRAWBGMODE_Opaque: AM_WST_DRAWBGMODE = 0
AM_WST_DRAWBGMODE_Transparent: AM_WST_DRAWBGMODE = 1
AM_WST_LEVEL = Int32
AM_WST_LEVEL_1_5: AM_WST_LEVEL = 0
class AM_WST_PAGE(Structure):
    dwPageNr: UInt32
    dwSubPageNr: UInt32
    pucPageData: c_char_p_no
AM_WST_SERVICE = Int32
AM_WST_SERVICE_None: AM_WST_SERVICE = 0
AM_WST_SERVICE_Text: AM_WST_SERVICE = 1
AM_WST_SERVICE_IDS: AM_WST_SERVICE = 2
AM_WST_SERVICE_Invalid: AM_WST_SERVICE = 3
AM_WST_STATE = Int32
AM_WST_STATE_Off: AM_WST_STATE = 0
AM_WST_STATE_On: AM_WST_STATE = 1
AM_WST_STYLE = Int32
AM_WST_STYLE_None: AM_WST_STYLE = 0
AM_WST_STYLE_Invers: AM_WST_STYLE = 1
class ANALOGVIDEOINFO(Structure):
    rcSource: win32more.Foundation.RECT
    rcTarget: win32more.Foundation.RECT
    dwActiveWidth: UInt32
    dwActiveHeight: UInt32
    AvgTimePerFrame: Int64
ANALOG_AUXIN_NETWORK_TYPE = Guid('742ef867-09e1-40a3-82-d3-96-69-ba-35-32-5f')
ANALOG_FM_NETWORK_TYPE = Guid('7728087b-2bb9-4e30-80-78-44-94-76-e5-9d-bb')
ANALOG_TV_NETWORK_TYPE = Guid('b820d87e-e0e3-478f-8a-38-4e-13-f7-b3-df-42')
ATSCChannelTuneRequest = Guid('0369b4e6-45b6-11d3-b6-50-00-c0-4f-79-49-8e')
ATSCComponentType = Guid('a8dcf3d5-0780-4ef4-8a-83-2c-ff-aa-cb-8a-ce')
ATSCComponentTypeFlags = Int32
ATSCCT_AC3: ATSCComponentTypeFlags = 1
ATSCLocator = Guid('8872ff1b-98fa-4d7a-8d-93-c9-f1-05-5f-85-bb')
ATSCTuningSpace = Guid('a2e30750-6c3d-11d3-b6-53-00-c0-4f-79-49-8e')
class ATSC_FILTER_OPTIONS(Structure):
    fSpecifyEtmId: win32more.Foundation.BOOL
    EtmId: UInt32
    _pack_ = 1
ATSC_TERRESTRIAL_TV_NETWORK_TYPE = Guid('0dad2fdd-5fd7-11d3-8f-50-00-c0-4f-79-71-e2')
class AUDIO_STREAM_CONFIG_CAPS(Structure):
    guid: Guid
    MinimumChannels: UInt32
    MaximumChannels: UInt32
    ChannelsGranularity: UInt32
    MinimumBitsPerSample: UInt32
    MaximumBitsPerSample: UInt32
    BitsPerSampleGranularity: UInt32
    MinimumSampleFrequency: UInt32
    MaximumSampleFrequency: UInt32
    SampleFrequencyGranularity: UInt32
class AVIEXTHEADER(Structure):
    fcc: UInt32
    cb: UInt32
    dwGrandFrames: UInt32
    dwFuture: UInt32 * 61
    _pack_ = 2
class AVIFIELDINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    qwBaseOffset: UInt64
    dwReserved3: UInt32
    aIndex: _avifieldindex_entry * 1
    _pack_ = 2
    class _avifieldindex_entry(Structure):
        dwOffset: UInt32
        dwSize: UInt32
        dwOffsetField2: UInt32
        _pack_ = 2
class AVIINDEXENTRY(Structure):
    ckid: UInt32
    dwFlags: UInt32
    dwChunkOffset: UInt32
    dwChunkLength: UInt32
class AVIMAINHEADER(Structure):
    fcc: UInt32
    cb: UInt32
    dwMicroSecPerFrame: UInt32
    dwMaxBytesPerSec: UInt32
    dwPaddingGranularity: UInt32
    dwFlags: UInt32
    dwTotalFrames: UInt32
    dwInitialFrames: UInt32
    dwStreams: UInt32
    dwSuggestedBufferSize: UInt32
    dwWidth: UInt32
    dwHeight: UInt32
    dwReserved: UInt32 * 4
    _pack_ = 2
class AVIMETAINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    dwReserved: UInt32 * 3
    adwIndex: UInt32 * 1
    _pack_ = 2
class AVIOLDINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    aIndex: _avioldindex_entry * 1
    _pack_ = 2
    class _avioldindex_entry(Structure):
        dwChunkId: UInt32
        dwFlags: UInt32
        dwOffset: UInt32
        dwSize: UInt32
        _pack_ = 2
class AVIPALCHANGE(Structure):
    bFirstEntry: Byte
    bNumEntries: Byte
    wFlags: UInt16
    peNew: win32more.Graphics.Gdi.PALETTEENTRY * 1
class AVISTDINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    qwBaseOffset: UInt64
    dwReserved_3: UInt32
    aIndex: win32more.Media.DirectShow.AVISTDINDEX_ENTRY * 2044
    _pack_ = 2
class AVISTDINDEX_ENTRY(Structure):
    dwOffset: UInt32
    dwSize: UInt32
    _pack_ = 2
class AVISTREAMHEADER(Structure):
    fcc: UInt32
    cb: UInt32
    fccType: UInt32
    fccHandler: UInt32
    dwFlags: UInt32
    wPriority: UInt16
    wLanguage: UInt16
    dwInitialFrames: UInt32
    dwScale: UInt32
    dwRate: UInt32
    dwStart: UInt32
    dwLength: UInt32
    dwSuggestedBufferSize: UInt32
    dwQuality: UInt32
    dwSampleSize: UInt32
    rcFrame: _rcFrame_e__Struct
    _pack_ = 2
    class _rcFrame_e__Struct(Structure):
        left: Int16
        top: Int16
        right: Int16
        bottom: Int16
class AVISUPERINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    dwReserved: UInt32 * 3
    aIndex: _avisuperindex_entry * 1022
    _pack_ = 2
    class _avisuperindex_entry(Structure):
        qwOffset: UInt64
        dwSize: UInt32
        dwDuration: UInt32
        _pack_ = 2
class AVIStreamHeader(Structure):
    fccType: UInt32
    fccHandler: UInt32
    dwFlags: UInt32
    wPriority: UInt16
    wLanguage: UInt16
    dwInitialFrames: UInt32
    dwScale: UInt32
    dwRate: UInt32
    dwStart: UInt32
    dwLength: UInt32
    dwSuggestedBufferSize: UInt32
    dwQuality: UInt32
    dwSampleSize: UInt32
    rcFrame: win32more.Foundation.RECT
class AVITCDLINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    dwReserved: UInt32 * 3
    aIndex: win32more.Media.DirectShow.AVITCDLINDEX_ENTRY * 584
    adwTrailingFill: UInt32 * 3512
    _pack_ = 2
class AVITCDLINDEX_ENTRY(Structure):
    dwTick: UInt32
    time: win32more.Media.TIMECODE
    dwSMPTEflags: UInt32
    dwUser: UInt32
    szReelId: SByte * 12
    _pack_ = 2
class AVITIMECODEINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    dwReserved: UInt32 * 3
    aIndex: win32more.Media.DirectShow.TIMECODEDATA * 1022
    _pack_ = 2
class AVITIMEDINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    qwBaseOffset: UInt64
    dwReserved_3: UInt32
    aIndex: win32more.Media.DirectShow.AVITIMEDINDEX_ENTRY * 1362
    adwTrailingFill: UInt32 * 2734
    _pack_ = 2
class AVITIMEDINDEX_ENTRY(Structure):
    dwOffset: UInt32
    dwSize: UInt32
    dwDuration: UInt32
    _pack_ = 2
AnalogAudioComponentType = Guid('28ab0005-e845-4ffa-aa-9b-f4-66-52-36-14-1c')
AnalogLocator = Guid('49638b91-48ab-48b7-a4-7a-7d-0e-75-a0-8e-de')
AnalogRadioTuningSpace = Guid('8a674b4c-1f63-11d3-b6-4c-00-c0-4f-79-49-8e')
AnalogTVTuningSpace = Guid('8a674b4d-1f63-11d3-b6-4c-00-c0-4f-79-49-8e')
AnalogVideoStandard = Int32
AnalogVideo_None: AnalogVideoStandard = 0
AnalogVideo_NTSC_M: AnalogVideoStandard = 1
AnalogVideo_NTSC_M_J: AnalogVideoStandard = 2
AnalogVideo_NTSC_433: AnalogVideoStandard = 4
AnalogVideo_PAL_B: AnalogVideoStandard = 16
AnalogVideo_PAL_D: AnalogVideoStandard = 32
AnalogVideo_PAL_G: AnalogVideoStandard = 64
AnalogVideo_PAL_H: AnalogVideoStandard = 128
AnalogVideo_PAL_I: AnalogVideoStandard = 256
AnalogVideo_PAL_M: AnalogVideoStandard = 512
AnalogVideo_PAL_N: AnalogVideoStandard = 1024
AnalogVideo_PAL_60: AnalogVideoStandard = 2048
AnalogVideo_SECAM_B: AnalogVideoStandard = 4096
AnalogVideo_SECAM_D: AnalogVideoStandard = 8192
AnalogVideo_SECAM_G: AnalogVideoStandard = 16384
AnalogVideo_SECAM_H: AnalogVideoStandard = 32768
AnalogVideo_SECAM_K: AnalogVideoStandard = 65536
AnalogVideo_SECAM_K1: AnalogVideoStandard = 131072
AnalogVideo_SECAM_L: AnalogVideoStandard = 262144
AnalogVideo_SECAM_L1: AnalogVideoStandard = 524288
AnalogVideo_PAL_N_COMBO: AnalogVideoStandard = 1048576
AnalogVideoMask_MCE_NTSC: AnalogVideoStandard = 1052167
AnalogVideoMask_MCE_PAL: AnalogVideoStandard = 496
AnalogVideoMask_MCE_SECAM: AnalogVideoStandard = 1044480
EC_SND_DEVICE_ERROR_BASE: UInt32 = 512
EC_SNDDEV_IN_ERROR: UInt32 = 512
EC_SNDDEV_OUT_ERROR: UInt32 = 513
EC_SYSTEMBASE: UInt32 = 0
EC_USER: UInt32 = 32768
EC_COMPLETE: UInt32 = 1
EC_USERABORT: UInt32 = 2
EC_ERRORABORT: UInt32 = 3
EC_TIME: UInt32 = 4
EC_REPAINT: UInt32 = 5
EC_STREAM_ERROR_STOPPED: UInt32 = 6
EC_STREAM_ERROR_STILLPLAYING: UInt32 = 7
EC_ERROR_STILLPLAYING: UInt32 = 8
EC_PALETTE_CHANGED: UInt32 = 9
EC_VIDEO_SIZE_CHANGED: UInt32 = 10
EC_QUALITY_CHANGE: UInt32 = 11
EC_SHUTTING_DOWN: UInt32 = 12
EC_CLOCK_CHANGED: UInt32 = 13
EC_PAUSED: UInt32 = 14
EC_OPENING_FILE: UInt32 = 16
EC_BUFFERING_DATA: UInt32 = 17
EC_FULLSCREEN_LOST: UInt32 = 18
EC_ACTIVATE: UInt32 = 19
EC_NEED_RESTART: UInt32 = 20
EC_WINDOW_DESTROYED: UInt32 = 21
EC_DISPLAY_CHANGED: UInt32 = 22
EC_STARVATION: UInt32 = 23
EC_OLE_EVENT: UInt32 = 24
EC_NOTIFY_WINDOW: UInt32 = 25
EC_STREAM_CONTROL_STOPPED: UInt32 = 26
EC_STREAM_CONTROL_STARTED: UInt32 = 27
EC_END_OF_SEGMENT: UInt32 = 28
EC_SEGMENT_STARTED: UInt32 = 29
EC_LENGTH_CHANGED: UInt32 = 30
EC_DEVICE_LOST: UInt32 = 31
EC_SAMPLE_NEEDED: UInt32 = 32
EC_PROCESSING_LATENCY: UInt32 = 33
EC_SAMPLE_LATENCY: UInt32 = 34
EC_SCRUB_TIME: UInt32 = 35
EC_STEP_COMPLETE: UInt32 = 36
EC_TIMECODE_AVAILABLE: UInt32 = 48
EC_EXTDEVICE_MODE_CHANGE: UInt32 = 49
EC_STATE_CHANGE: UInt32 = 50
EC_GRAPH_CHANGED: UInt32 = 80
EC_CLOCK_UNSET: UInt32 = 81
EC_VMR_RENDERDEVICE_SET: UInt32 = 83
VMR_RENDER_DEVICE_OVERLAY: UInt32 = 1
VMR_RENDER_DEVICE_VIDMEM: UInt32 = 2
VMR_RENDER_DEVICE_SYSMEM: UInt32 = 4
EC_VMR_SURFACE_FLIPPED: UInt32 = 84
EC_VMR_RECONNECTION_FAILED: UInt32 = 85
EC_PREPROCESS_COMPLETE: UInt32 = 86
EC_CODECAPI_EVENT: UInt32 = 87
EC_WMT_EVENT_BASE: UInt32 = 593
EC_WMT_INDEX_EVENT: UInt32 = 593
EC_WMT_EVENT: UInt32 = 594
EC_BUILT: UInt32 = 768
EC_UNBUILT: UInt32 = 769
EC_SKIP_FRAMES: UInt32 = 37
EC_PLEASE_REOPEN: UInt32 = 64
EC_STATUS: UInt32 = 65
EC_MARKER_HIT: UInt32 = 66
EC_LOADSTATUS: UInt32 = 67
EC_FILE_CLOSED: UInt32 = 68
EC_ERRORABORTEX: UInt32 = 69
AM_LOADSTATUS_CLOSED: UInt32 = 0
AM_LOADSTATUS_LOADINGDESCR: UInt32 = 1
AM_LOADSTATUS_LOADINGMCAST: UInt32 = 2
AM_LOADSTATUS_LOCATING: UInt32 = 3
AM_LOADSTATUS_CONNECTING: UInt32 = 4
AM_LOADSTATUS_OPENING: UInt32 = 5
AM_LOADSTATUS_OPEN: UInt32 = 6
EC_NEW_PIN: UInt32 = 32
EC_RENDER_FINISHED: UInt32 = 33
EC_EOS_SOON: UInt32 = 70
EC_CONTENTPROPERTY_CHANGED: UInt32 = 71
AM_CONTENTPROPERTY_TITLE: UInt32 = 1
AM_CONTENTPROPERTY_AUTHOR: UInt32 = 2
AM_CONTENTPROPERTY_COPYRIGHT: UInt32 = 4
AM_CONTENTPROPERTY_DESCRIPTION: UInt32 = 8
EC_BANDWIDTHCHANGE: UInt32 = 72
EC_VIDEOFRAMEREADY: UInt32 = 73
EC_DVDBASE: UInt32 = 256
EC_DVD_DOMAIN_CHANGE: UInt32 = 257
EC_DVD_TITLE_CHANGE: UInt32 = 258
EC_DVD_CHAPTER_START: UInt32 = 259
EC_DVD_AUDIO_STREAM_CHANGE: UInt32 = 260
EC_DVD_SUBPICTURE_STREAM_CHANGE: UInt32 = 261
EC_DVD_ANGLE_CHANGE: UInt32 = 262
EC_DVD_BUTTON_CHANGE: UInt32 = 263
EC_DVD_VALID_UOPS_CHANGE: UInt32 = 264
EC_DVD_STILL_ON: UInt32 = 265
EC_DVD_STILL_OFF: UInt32 = 266
EC_DVD_CURRENT_TIME: UInt32 = 267
EC_DVD_ERROR: UInt32 = 268
EC_DVD_WARNING: UInt32 = 269
EC_DVD_CHAPTER_AUTOSTOP: UInt32 = 270
EC_DVD_NO_FP_PGC: UInt32 = 271
EC_DVD_PLAYBACK_RATE_CHANGE: UInt32 = 272
EC_DVD_PARENTAL_LEVEL_CHANGE: UInt32 = 273
EC_DVD_PLAYBACK_STOPPED: UInt32 = 274
EC_DVD_ANGLES_AVAILABLE: UInt32 = 275
EC_DVD_PLAYPERIOD_AUTOSTOP: UInt32 = 276
EC_DVD_BUTTON_AUTO_ACTIVATED: UInt32 = 277
EC_DVD_CMD_START: UInt32 = 278
EC_DVD_CMD_END: UInt32 = 279
EC_DVD_DISC_EJECTED: UInt32 = 280
EC_DVD_DISC_INSERTED: UInt32 = 281
EC_DVD_CURRENT_HMSF_TIME: UInt32 = 282
EC_DVD_KARAOKE_MODE: UInt32 = 283
EC_DVD_PROGRAM_CELL_CHANGE: UInt32 = 284
EC_DVD_TITLE_SET_CHANGE: UInt32 = 285
EC_DVD_PROGRAM_CHAIN_CHANGE: UInt32 = 286
EC_DVD_VOBU_Offset: UInt32 = 287
EC_DVD_VOBU_Timestamp: UInt32 = 288
EC_DVD_GPRM_Change: UInt32 = 289
EC_DVD_SPRM_Change: UInt32 = 290
EC_DVD_BeginNavigationCommands: UInt32 = 291
EC_DVD_NavigationCommand: UInt32 = 292
AM_AC3_ALTERNATE_AUDIO_1: UInt32 = 1
AM_AC3_ALTERNATE_AUDIO_2: UInt32 = 2
AM_AC3_ALTERNATE_AUDIO_BOTH: UInt32 = 3
AM_AC3_SERVICE_MAIN_AUDIO: UInt32 = 0
AM_AC3_SERVICE_NO_DIALOG: UInt32 = 1
AM_AC3_SERVICE_VISUALLY_IMPAIRED: UInt32 = 2
AM_AC3_SERVICE_HEARING_IMPAIRED: UInt32 = 3
AM_AC3_SERVICE_DIALOG_ONLY: UInt32 = 4
AM_AC3_SERVICE_COMMENTARY: UInt32 = 5
AM_AC3_SERVICE_EMERGENCY_FLASH: UInt32 = 6
AM_AC3_SERVICE_VOICE_OVER: UInt32 = 7
AM_UseNewCSSKey: UInt32 = 1
AM_ReverseBlockStart: UInt32 = 2
AM_ReverseBlockEnd: UInt32 = 4
AM_DVD_CGMS_RESERVED_MASK: UInt32 = 120
AM_DVD_CGMS_COPY_PROTECT_MASK: UInt32 = 24
AM_DVD_CGMS_COPY_PERMITTED: UInt32 = 0
AM_DVD_CGMS_COPY_ONCE: UInt32 = 16
AM_DVD_CGMS_NO_COPY: UInt32 = 24
AM_DVD_COPYRIGHT_MASK: UInt32 = 64
AM_DVD_NOT_COPYRIGHTED: UInt32 = 0
AM_DVD_COPYRIGHTED: UInt32 = 64
AM_DVD_SECTOR_PROTECT_MASK: UInt32 = 32
AM_DVD_SECTOR_NOT_PROTECTED: UInt32 = 0
AM_DVD_SECTOR_PROTECTED: UInt32 = 32
AMINTERLACE_IsInterlaced: UInt32 = 1
AMINTERLACE_1FieldPerSample: UInt32 = 2
AMINTERLACE_Field1First: UInt32 = 4
AMINTERLACE_UNUSED: UInt32 = 8
AMINTERLACE_FieldPatternMask: UInt32 = 48
AMINTERLACE_FieldPatField1Only: UInt32 = 0
AMINTERLACE_FieldPatField2Only: UInt32 = 16
AMINTERLACE_FieldPatBothRegular: UInt32 = 32
AMINTERLACE_FieldPatBothIrregular: UInt32 = 48
AMINTERLACE_DisplayModeMask: UInt32 = 192
AMINTERLACE_DisplayModeBobOnly: UInt32 = 0
AMINTERLACE_DisplayModeWeaveOnly: UInt32 = 64
AMINTERLACE_DisplayModeBobOrWeave: UInt32 = 128
AMCOPYPROTECT_RestrictDuplication: UInt32 = 1
AMCONTROL_USED: UInt32 = 1
AMCONTROL_PAD_TO_4x3: UInt32 = 2
AMCONTROL_PAD_TO_16x9: UInt32 = 4
AMCONTROL_COLORINFO_PRESENT: UInt32 = 128
AM_VIDEO_FLAG_FIELD_MASK: Int32 = 3
AM_VIDEO_FLAG_INTERLEAVED_FRAME: Int32 = 0
AM_VIDEO_FLAG_FIELD1: Int32 = 1
AM_VIDEO_FLAG_FIELD2: Int32 = 2
AM_VIDEO_FLAG_FIELD1FIRST: Int32 = 4
AM_VIDEO_FLAG_WEAVE: Int32 = 8
AM_VIDEO_FLAG_IPB_MASK: Int32 = 48
AM_VIDEO_FLAG_I_SAMPLE: Int32 = 0
AM_VIDEO_FLAG_P_SAMPLE: Int32 = 16
AM_VIDEO_FLAG_B_SAMPLE: Int32 = 32
AM_VIDEO_FLAG_REPEAT_FIELD: Int32 = 64
AVIF_HASINDEX: UInt32 = 16
AVIF_MUSTUSEINDEX: UInt32 = 32
AVIF_ISINTERLEAVED: UInt32 = 256
AVIF_TRUSTCKTYPE: UInt32 = 2048
AVIF_WASCAPTUREFILE: UInt32 = 65536
AVIF_COPYRIGHTED: UInt32 = 131072
AVI_HEADERSIZE: UInt32 = 2048
AVISF_DISABLED: UInt32 = 1
AVISF_VIDEO_PALCHANGES: UInt32 = 65536
AVIIF_LIST: Int32 = 1
AVIIF_KEYFRAME: Int32 = 16
AVIIF_FIRSTPART: Int32 = 32
AVIIF_LASTPART: Int32 = 64
AVIIF_NOTIME: Int32 = 256
AVIIF_COMPUSE: Int32 = 268369920
AVIIF_NO_TIME: UInt32 = 256
AVIIF_COMPRESSOR: UInt32 = 268369920
TIMECODE_RATE_30DROP: UInt32 = 0
TIMECODE_SMPTE_BINARY_GROUP: UInt32 = 7
TIMECODE_SMPTE_COLOR_FRAME: UInt32 = 8
AVI_INDEX_OF_INDEXES: UInt32 = 0
AVI_INDEX_OF_CHUNKS: UInt32 = 1
AVI_INDEX_OF_TIMED_CHUNKS: UInt32 = 2
AVI_INDEX_OF_SUB_2FIELD: UInt32 = 3
AVI_INDEX_IS_DATA: UInt32 = 128
AVI_INDEX_SUB_DEFAULT: UInt32 = 0
AVI_INDEX_SUB_2FIELD: UInt32 = 1
STDINDEXSIZE: UInt32 = 16384
AVISTDINDEX_DELTAFRAME: UInt32 = 2147483648
AMVA_TYPEINDEX_OUTPUTFRAME: UInt32 = 4294967295
AMVA_QUERYRENDERSTATUSF_READ: UInt32 = 1
MIN_DIMENSION: UInt32 = 1
BDA_PLP_ID_NOT_SET: Int32 = -1
CDEF_CLASS_DEFAULT: UInt32 = 1
CDEF_BYPASS_CLASS_MANAGER: UInt32 = 2
CDEF_MERIT_ABOVE_DO_NOT_USE: UInt32 = 8
CDEF_DEVMON_CMGR_DEVICE: UInt32 = 16
CDEF_DEVMON_DMO: UInt32 = 32
CDEF_DEVMON_PNP_DEVICE: UInt32 = 64
CDEF_DEVMON_FILTER: UInt32 = 128
CDEF_DEVMON_SELECTIVE_MASK: UInt32 = 240
CHARS_IN_GUID: UInt32 = 39
MAX_PIN_NAME: UInt32 = 128
MAX_FILTER_NAME: UInt32 = 128
AM_GBF_PREVFRAMESKIPPED: UInt32 = 1
AM_GBF_NOTASYNCPOINT: UInt32 = 2
AM_GBF_NOWAIT: UInt32 = 4
AM_GBF_NODDSURFACELOCK: UInt32 = 8
AMF_AUTOMATICGAIN: Double = -1
AnalogVideo_NTSC_Mask: UInt32 = 7
AnalogVideo_PAL_Mask: UInt32 = 1052656
AnalogVideo_SECAM_Mask: UInt32 = 1044480
MPEG2_PROGRAM_STREAM_MAP: UInt32 = 0
MPEG2_PROGRAM_ELEMENTARY_STREAM: UInt32 = 1
MPEG2_PROGRAM_DIRECTORY_PES_PACKET: UInt32 = 2
MPEG2_PROGRAM_PACK_HEADER: UInt32 = 3
MPEG2_PROGRAM_PES_STREAM: UInt32 = 4
MPEG2_PROGRAM_SYSTEM_HEADER: UInt32 = 5
SUBSTREAM_FILTER_VAL_NONE: UInt32 = 268435456
AM_GETDECODERCAP_QUERY_VMR_SUPPORT: UInt32 = 1
VMR_NOTSUPPORTED: UInt32 = 0
VMR_SUPPORTED: UInt32 = 1
AM_QUERY_DECODER_VMR_SUPPORT: UInt32 = 1
AM_QUERY_DECODER_DXVA_1_SUPPORT: UInt32 = 2
AM_QUERY_DECODER_DVD_SUPPORT: UInt32 = 3
AM_QUERY_DECODER_ATSC_SD_SUPPORT: UInt32 = 4
AM_QUERY_DECODER_ATSC_HD_SUPPORT: UInt32 = 5
AM_GETDECODERCAP_QUERY_VMR9_SUPPORT: UInt32 = 6
AM_GETDECODERCAP_QUERY_EVR_SUPPORT: UInt32 = 7
DECODER_CAP_NOTSUPPORTED: UInt32 = 0
DECODER_CAP_SUPPORTED: UInt32 = 1
VMRBITMAP_DISABLE: UInt32 = 1
VMRBITMAP_HDC: UInt32 = 2
VMRBITMAP_ENTIREDDS: UInt32 = 4
VMRBITMAP_SRCCOLORKEY: UInt32 = 8
VMRBITMAP_SRCRECT: UInt32 = 16
DVD_TITLE_MENU: UInt32 = 0
DVD_STREAM_DATA_CURRENT: UInt32 = 2048
DVD_STREAM_DATA_VMGM: UInt32 = 1024
DVD_STREAM_DATA_VTSM: UInt32 = 1025
DVD_DEFAULT_AUDIO_STREAM: UInt32 = 15
DVD_AUDIO_CAPS_AC3: UInt32 = 1
DVD_AUDIO_CAPS_MPEG2: UInt32 = 2
DVD_AUDIO_CAPS_LPCM: UInt32 = 4
DVD_AUDIO_CAPS_DTS: UInt32 = 8
DVD_AUDIO_CAPS_SDDS: UInt32 = 16
MEDIATYPE_MPEG2_PACK: Guid = Guid('36523b13-8ee5-11d1-8c-a3-00-60-b0-57-66-4a')
MEDIATYPE_MPEG2_PES: Guid = Guid('e06d8020-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIATYPE_CONTROL: Guid = Guid('e06d8021-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIATYPE_MPEG2_SECTIONS: Guid = Guid('455f176c-4b06-47ce-9a-ef-8c-ae-f7-3d-f7-b5')
MEDIASUBTYPE_MPEG2_VERSIONED_TABLES: Guid = Guid('1ed988b0-3ffc-4523-87-25-34-7b-ee-c1-a8-a0')
MEDIASUBTYPE_ATSC_SI: Guid = Guid('b3c7397c-d303-414d-b3-3c-4e-d2-c9-d2-97-33')
MEDIASUBTYPE_DVB_SI: Guid = Guid('e9dd31a3-221d-4adb-85-32-9a-f3-09-c1-a4-08')
MEDIASUBTYPE_ISDB_SI: Guid = Guid('e89ad298-3601-4b06-aa-ec-9d-de-ed-cc-5b-d0')
MEDIASUBTYPE_TIF_SI: Guid = Guid('ec232eb2-cb96-4191-b2-26-0e-a1-29-f3-82-50')
MEDIASUBTYPE_MPEG2DATA: Guid = Guid('c892e55b-252d-42b5-a3-16-d9-97-e7-a5-d9-95')
MEDIASUBTYPE_MPEG2_WMDRM_TRANSPORT: Guid = Guid('18bec4ea-4676-450e-b4-78-0c-d8-4c-54-b3-27')
MEDIASUBTYPE_MPEG2_VIDEO: Guid = Guid('e06d8026-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
FORMAT_MPEG2_VIDEO: Guid = Guid('e06d80e3-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
FORMAT_VIDEOINFO2: Guid = Guid('f72a76a0-eb0a-11d0-ac-e4-00-00-c0-cc-16-ba')
MEDIASUBTYPE_MPEG2_PROGRAM: Guid = Guid('e06d8022-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_MPEG2_TRANSPORT: Guid = Guid('e06d8023-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE: Guid = Guid('138aa9a4-1ee2-4c5b-98-8e-19-ab-fd-bc-8a-11')
MEDIASUBTYPE_MPEG2_UDCR_TRANSPORT: Guid = Guid('18bec4ea-4676-450e-b4-78-0c-d8-4c-54-b3-27')
MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_RAW: Guid = Guid('0d7aed42-cb9a-11db-97-05-00-50-56-c0-00-08')
MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_PROCESSED: Guid = Guid('af748dd4-0d80-11db-97-05-00-50-56-c0-00-08')
MEDIASUBTYPE_MPEG2_AUDIO: Guid = Guid('e06d802b-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_DOLBY_AC3: Guid = Guid('e06d802c-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_DVD_SUBPICTURE: Guid = Guid('e06d802d-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_DVD_LPCM_AUDIO: Guid = Guid('e06d8032-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_DTS: Guid = Guid('e06d8033-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_SDDS: Guid = Guid('e06d8034-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIATYPE_DVD_ENCRYPTED_PACK: Guid = Guid('ed0b916a-044d-11d1-aa-78-00-c0-4f-c3-1d-60')
MEDIATYPE_DVD_NAVIGATION: Guid = Guid('e06d802e-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_DVD_NAVIGATION_PCI: Guid = Guid('e06d802f-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_DVD_NAVIGATION_DSI: Guid = Guid('e06d8030-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
MEDIASUBTYPE_DVD_NAVIGATION_PROVIDER: Guid = Guid('e06d8031-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
FORMAT_MPEG2Video: Guid = Guid('e06d80e3-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
FORMAT_DolbyAC3: Guid = Guid('e06d80e4-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
FORMAT_MPEG2Audio: Guid = Guid('e06d80e5-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
FORMAT_DVD_LPCMAudio: Guid = Guid('e06d80e6-db46-11cf-b4-d1-00-80-5f-6c-bb-ea')
FORMAT_UVCH264Video: Guid = Guid('2017be05-6629-4248-aa-ed-7e-1a-47-bc-9b-9c')
FORMAT_JPEGImage: Guid = Guid('692fa379-d3e8-4651-b5-b4-0b-94-b0-13-ee-af')
FORMAT_Image: Guid = Guid('692fa379-d3e8-4651-b5-b4-0b-94-b0-13-ee-af')
AM_KSPROPSETID_AC3: Guid = Guid('bfabe720-6e1f-11d0-bc-f2-44-45-53-54-00-00')
AM_KSPROPSETID_DvdSubPic: Guid = Guid('ac390460-43af-11d0-bd-6a-00-35-05-c1-03-a9')
AM_KSPROPSETID_CopyProt: Guid = Guid('0e8a0a40-6aef-11d0-9e-d0-00-a0-24-ca-19-b3')
AM_KSPROPSETID_TSRateChange: Guid = Guid('a503c5c0-1d1d-11d1-ad-80-44-45-53-54-00-00')
AM_KSPROPSETID_DVD_RateChange: Guid = Guid('3577eb09-9582-477f-b2-9c-b0-c4-52-a4-ff-9a')
AM_KSPROPSETID_DvdKaraoke: Guid = Guid('ae4720ae-aa71-42d8-b8-2a-ff-fd-f5-8b-76-fd')
AM_KSPROPSETID_FrameStep: Guid = Guid('c830acbd-ab07-492f-88-52-45-b6-98-7c-29-79')
AM_KSPROPSETID_MPEG4_MediaType_Attributes: Guid = Guid('ff6c4bfa-07a9-4c7b-a2-37-67-2f-9d-68-06-5f')
AM_KSCATEGORY_CAPTURE: Guid = Guid('65e8773d-8f56-11d0-a3-b9-00-a0-c9-22-31-96')
AM_KSCATEGORY_RENDER: Guid = Guid('65e8773e-8f56-11d0-a3-b9-00-a0-c9-22-31-96')
AM_KSCATEGORY_DATACOMPRESSOR: Guid = Guid('1e84c900-7e70-11d0-a5-d6-28-db-04-c1-00-00')
AM_KSCATEGORY_AUDIO: Guid = Guid('6994ad04-93ef-11d0-a3-cc-00-a0-c9-22-31-96')
AM_KSCATEGORY_VIDEO: Guid = Guid('6994ad05-93ef-11d0-a3-cc-00-a0-c9-22-31-96')
AM_KSCATEGORY_TVTUNER: Guid = Guid('a799a800-a46d-11d0-a1-8c-00-a0-24-01-dc-d4')
AM_KSCATEGORY_CROSSBAR: Guid = Guid('a799a801-a46d-11d0-a1-8c-00-a0-24-01-dc-d4')
AM_KSCATEGORY_TVAUDIO: Guid = Guid('a799a802-a46d-11d0-a1-8c-00-a0-24-01-dc-d4')
AM_KSCATEGORY_VBICODEC: Guid = Guid('07dad660-22f1-11d1-a9-f4-00-c0-4f-bb-de-8f')
AM_KSCATEGORY_VBICODEC_MI: Guid = Guid('9c24a977-0951-451a-80-06-0e-49-bd-28-cd-5f')
AM_KSCATEGORY_SPLITTER: Guid = Guid('0a4252a0-7e70-11d0-a5-d6-28-db-04-c1-00-00')
AM_INTERFACESETID_Standard: Guid = Guid('1a8766a0-62ce-11cf-a5-d6-28-db-04-c1-00-00')
PBDA_AUX_CONNECTOR_TYPE_SVideo: Guid = Guid('a0e905f4-24c9-4a54-b7-61-21-33-55-ef-c1-3a')
PBDA_AUX_CONNECTOR_TYPE_Composite: Guid = Guid('f6298b4c-c725-4d42-84-9b-41-0b-bb-14-ea-62')
CLSID_PBDA_AUX_DATA_TYPE: Guid = Guid('fd456373-3323-4090-ad-ca-8e-d4-5f-55-cf-10')
CLSID_PBDA_Encoder_DATA_TYPE: Guid = Guid('728fd6bc-5546-4716-b1-03-f8-99-f5-a1-fa-68')
PBDA_Encoder_Audio_AlgorithmType_MPEG1LayerII: UInt32 = 0
PBDA_Encoder_Audio_AlgorithmType_AC3: UInt32 = 1
PBDA_Encoder_Video_MPEG2PartII: UInt32 = 0
PBDA_Encoder_Video_MPEG4Part10: UInt32 = 1
PBDA_Encoder_Video_AVC: UInt32 = 1
PBDA_Encoder_Video_H264: UInt32 = 1
PBDA_Encoder_BitrateMode_Constant: UInt32 = 1
PBDA_Encoder_BitrateMode_Variable: UInt32 = 2
PBDA_Encoder_BitrateMode_Average: UInt32 = 3
CLSID_PBDA_FDC_DATA_TYPE: Guid = Guid('e7dbf9a0-22ab-4047-8e-67-ef-9a-d5-04-e7-29')
CLSID_PBDA_GDDS_DATA_TYPE: Guid = Guid('c80c0df3-6052-4c16-9f-56-c4-4c-21-f7-3c-45')
LIBID_QuartzNetTypeLib: Guid = Guid('56a868b1-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
LIBID_QuartzTypeLib: Guid = Guid('56a868b0-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
CLSID_AMMultiMediaStream: Guid = Guid('49c47ce5-9ba4-11d0-82-12-00-c0-4f-c3-2c-45')
CLSID_AMDirectDrawStream: Guid = Guid('49c47ce4-9ba4-11d0-82-12-00-c0-4f-c3-2c-45')
CLSID_AMAudioStream: Guid = Guid('8496e040-af4c-11d0-82-12-00-c0-4f-c3-2c-45')
CLSID_AMAudioData: Guid = Guid('f2468580-af8a-11d0-82-12-00-c0-4f-c3-2c-45')
CLSID_AMMediaTypeStream: Guid = Guid('cf0f2f7c-f7bf-11d0-90-0d-00-c0-4f-d9-18-9d')
AMDDS_NONE: UInt32 = 0
AMDDS_DCIPS: UInt32 = 1
AMDDS_PS: UInt32 = 2
AMDDS_RGBOVR: UInt32 = 4
AMDDS_YUVOVR: UInt32 = 8
AMDDS_RGBOFF: UInt32 = 16
AMDDS_YUVOFF: UInt32 = 32
AMDDS_RGBFLP: UInt32 = 64
AMDDS_YUVFLP: UInt32 = 128
AMDDS_ALL: UInt32 = 255
AMDDS_DEFAULT: UInt32 = 255
iPALETTE_COLORS: UInt32 = 256
iEGA_COLORS: UInt32 = 16
iMASK_COLORS: UInt32 = 3
iTRUECOLOR: UInt32 = 16
iRED: UInt32 = 0
iGREEN: UInt32 = 1
iBLUE: UInt32 = 2
iPALETTE: UInt32 = 8
iMAXBITS: UInt32 = 8
MAX_SIZE_MPEG1_SEQUENCE_INFO: UInt32 = 140
CLSID_DMOWrapperFilter: Guid = Guid('94297043-bd82-4dfd-b0-de-81-77-73-9c-6d-20')
CLSID_DMOFilterCategory: Guid = Guid('bcd5796c-bd52-4d30-ab-76-70-f9-75-b8-91-99')
AM_MPEG_AUDIO_DUAL_MERGE: UInt32 = 0
AM_MPEG_AUDIO_DUAL_LEFT: UInt32 = 1
AM_MPEG_AUDIO_DUAL_RIGHT: UInt32 = 2
VFW_FIRST_CODE: UInt32 = 512
MAX_ERROR_TEXT_LEN: UInt32 = 160
MPBOOL_TRUE: UInt32 = 1
MPBOOL_FALSE: UInt32 = 0
DWORD_ALLPARAMS: Int32 = -1
GUID_TIME_REFERENCE: Guid = Guid('93ad712b-daa0-4ffe-bc-81-b0-ce-50-0f-cd-d9')
GUID_TIME_MUSIC: Guid = Guid('0574c49d-5b04-4b15-a5-42-ae-28-20-30-11-7b')
GUID_TIME_SAMPLES: Guid = Guid('a8593d05-0c43-4984-9a-63-97-af-9e-02-c4-c0')
MPF_ENVLP_STANDARD: UInt32 = 0
MPF_ENVLP_BEGIN_CURRENTVAL: UInt32 = 1
MPF_ENVLP_BEGIN_NEUTRALVAL: UInt32 = 2
MPF_PUNCHIN_REFTIME: UInt32 = 0
MPF_PUNCHIN_NOW: UInt32 = 1
MPF_PUNCHIN_STOPPED: UInt32 = 2
MSPID_PrimaryVideo: Guid = Guid('a35ff56a-9fda-11d0-8f-df-00-c0-4f-d9-18-9d')
MSPID_PrimaryAudio: Guid = Guid('a35ff56b-9fda-11d0-8f-df-00-c0-4f-d9-18-9d')
VFW_E_INVALIDMEDIATYPE: win32more.Foundation.HRESULT = -2147220992
VFW_E_INVALIDSUBTYPE: win32more.Foundation.HRESULT = -2147220991
VFW_E_NEED_OWNER: win32more.Foundation.HRESULT = -2147220990
VFW_E_ENUM_OUT_OF_SYNC: win32more.Foundation.HRESULT = -2147220989
VFW_E_ALREADY_CONNECTED: win32more.Foundation.HRESULT = -2147220988
VFW_E_FILTER_ACTIVE: win32more.Foundation.HRESULT = -2147220987
VFW_E_NO_TYPES: win32more.Foundation.HRESULT = -2147220986
VFW_E_NO_ACCEPTABLE_TYPES: win32more.Foundation.HRESULT = -2147220985
VFW_E_INVALID_DIRECTION: win32more.Foundation.HRESULT = -2147220984
VFW_E_NOT_CONNECTED: win32more.Foundation.HRESULT = -2147220983
VFW_E_NO_ALLOCATOR: win32more.Foundation.HRESULT = -2147220982
VFW_E_RUNTIME_ERROR: win32more.Foundation.HRESULT = -2147220981
VFW_E_BUFFER_NOTSET: win32more.Foundation.HRESULT = -2147220980
VFW_E_BUFFER_OVERFLOW: win32more.Foundation.HRESULT = -2147220979
VFW_E_BADALIGN: win32more.Foundation.HRESULT = -2147220978
VFW_E_ALREADY_COMMITTED: win32more.Foundation.HRESULT = -2147220977
VFW_E_BUFFERS_OUTSTANDING: win32more.Foundation.HRESULT = -2147220976
VFW_E_NOT_COMMITTED: win32more.Foundation.HRESULT = -2147220975
VFW_E_SIZENOTSET: win32more.Foundation.HRESULT = -2147220974
VFW_E_NO_CLOCK: win32more.Foundation.HRESULT = -2147220973
VFW_E_NO_SINK: win32more.Foundation.HRESULT = -2147220972
VFW_E_NO_INTERFACE: win32more.Foundation.HRESULT = -2147220971
VFW_E_NOT_FOUND: win32more.Foundation.HRESULT = -2147220970
VFW_E_CANNOT_CONNECT: win32more.Foundation.HRESULT = -2147220969
VFW_E_CANNOT_RENDER: win32more.Foundation.HRESULT = -2147220968
VFW_E_CHANGING_FORMAT: win32more.Foundation.HRESULT = -2147220967
VFW_E_NO_COLOR_KEY_SET: win32more.Foundation.HRESULT = -2147220966
VFW_E_NOT_OVERLAY_CONNECTION: win32more.Foundation.HRESULT = -2147220965
VFW_E_NOT_SAMPLE_CONNECTION: win32more.Foundation.HRESULT = -2147220964
VFW_E_PALETTE_SET: win32more.Foundation.HRESULT = -2147220963
VFW_E_COLOR_KEY_SET: win32more.Foundation.HRESULT = -2147220962
VFW_E_NO_COLOR_KEY_FOUND: win32more.Foundation.HRESULT = -2147220961
VFW_E_NO_PALETTE_AVAILABLE: win32more.Foundation.HRESULT = -2147220960
VFW_E_NO_DISPLAY_PALETTE: win32more.Foundation.HRESULT = -2147220959
VFW_E_TOO_MANY_COLORS: win32more.Foundation.HRESULT = -2147220958
VFW_E_STATE_CHANGED: win32more.Foundation.HRESULT = -2147220957
VFW_E_NOT_STOPPED: win32more.Foundation.HRESULT = -2147220956
VFW_E_NOT_PAUSED: win32more.Foundation.HRESULT = -2147220955
VFW_E_NOT_RUNNING: win32more.Foundation.HRESULT = -2147220954
VFW_E_WRONG_STATE: win32more.Foundation.HRESULT = -2147220953
VFW_E_START_TIME_AFTER_END: win32more.Foundation.HRESULT = -2147220952
VFW_E_INVALID_RECT: win32more.Foundation.HRESULT = -2147220951
VFW_E_TYPE_NOT_ACCEPTED: win32more.Foundation.HRESULT = -2147220950
VFW_E_SAMPLE_REJECTED: win32more.Foundation.HRESULT = -2147220949
VFW_E_SAMPLE_REJECTED_EOS: win32more.Foundation.HRESULT = -2147220948
VFW_E_DUPLICATE_NAME: win32more.Foundation.HRESULT = -2147220947
VFW_S_DUPLICATE_NAME: win32more.Foundation.HRESULT = 262701
VFW_E_TIMEOUT: win32more.Foundation.HRESULT = -2147220946
VFW_E_INVALID_FILE_FORMAT: win32more.Foundation.HRESULT = -2147220945
VFW_E_ENUM_OUT_OF_RANGE: win32more.Foundation.HRESULT = -2147220944
VFW_E_CIRCULAR_GRAPH: win32more.Foundation.HRESULT = -2147220943
VFW_E_NOT_ALLOWED_TO_SAVE: win32more.Foundation.HRESULT = -2147220942
VFW_E_TIME_ALREADY_PASSED: win32more.Foundation.HRESULT = -2147220941
VFW_E_ALREADY_CANCELLED: win32more.Foundation.HRESULT = -2147220940
VFW_E_CORRUPT_GRAPH_FILE: win32more.Foundation.HRESULT = -2147220939
VFW_E_ADVISE_ALREADY_SET: win32more.Foundation.HRESULT = -2147220938
VFW_S_STATE_INTERMEDIATE: win32more.Foundation.HRESULT = 262711
VFW_E_NO_MODEX_AVAILABLE: win32more.Foundation.HRESULT = -2147220936
VFW_E_NO_ADVISE_SET: win32more.Foundation.HRESULT = -2147220935
VFW_E_NO_FULLSCREEN: win32more.Foundation.HRESULT = -2147220934
VFW_E_IN_FULLSCREEN_MODE: win32more.Foundation.HRESULT = -2147220933
VFW_E_UNKNOWN_FILE_TYPE: win32more.Foundation.HRESULT = -2147220928
VFW_E_CANNOT_LOAD_SOURCE_FILTER: win32more.Foundation.HRESULT = -2147220927
VFW_S_PARTIAL_RENDER: win32more.Foundation.HRESULT = 262722
VFW_E_FILE_TOO_SHORT: win32more.Foundation.HRESULT = -2147220925
VFW_E_INVALID_FILE_VERSION: win32more.Foundation.HRESULT = -2147220924
VFW_S_SOME_DATA_IGNORED: win32more.Foundation.HRESULT = 262725
VFW_S_CONNECTIONS_DEFERRED: win32more.Foundation.HRESULT = 262726
VFW_E_INVALID_CLSID: win32more.Foundation.HRESULT = -2147220921
VFW_E_INVALID_MEDIA_TYPE: win32more.Foundation.HRESULT = -2147220920
VFW_E_BAD_KEY: win32more.Foundation.HRESULT = -2147220494
VFW_S_NO_MORE_ITEMS: win32more.Foundation.HRESULT = 262403
VFW_E_SAMPLE_TIME_NOT_SET: win32more.Foundation.HRESULT = -2147220919
VFW_S_RESOURCE_NOT_NEEDED: win32more.Foundation.HRESULT = 262736
VFW_E_MEDIA_TIME_NOT_SET: win32more.Foundation.HRESULT = -2147220911
VFW_E_NO_TIME_FORMAT_SET: win32more.Foundation.HRESULT = -2147220910
VFW_E_MONO_AUDIO_HW: win32more.Foundation.HRESULT = -2147220909
VFW_S_MEDIA_TYPE_IGNORED: win32more.Foundation.HRESULT = 262740
VFW_E_NO_DECOMPRESSOR: win32more.Foundation.HRESULT = -2147220907
VFW_E_NO_AUDIO_HARDWARE: win32more.Foundation.HRESULT = -2147220906
VFW_S_VIDEO_NOT_RENDERED: win32more.Foundation.HRESULT = 262743
VFW_S_AUDIO_NOT_RENDERED: win32more.Foundation.HRESULT = 262744
VFW_E_RPZA: win32more.Foundation.HRESULT = -2147220903
VFW_S_RPZA: win32more.Foundation.HRESULT = 262746
VFW_E_PROCESSOR_NOT_SUITABLE: win32more.Foundation.HRESULT = -2147220901
VFW_E_UNSUPPORTED_AUDIO: win32more.Foundation.HRESULT = -2147220900
VFW_E_UNSUPPORTED_VIDEO: win32more.Foundation.HRESULT = -2147220899
VFW_E_MPEG_NOT_CONSTRAINED: win32more.Foundation.HRESULT = -2147220898
VFW_E_NOT_IN_GRAPH: win32more.Foundation.HRESULT = -2147220897
VFW_S_ESTIMATED: win32more.Foundation.HRESULT = 262752
VFW_E_NO_TIME_FORMAT: win32more.Foundation.HRESULT = -2147220895
VFW_E_READ_ONLY: win32more.Foundation.HRESULT = -2147220894
VFW_S_RESERVED: win32more.Foundation.HRESULT = 262755
VFW_E_BUFFER_UNDERFLOW: win32more.Foundation.HRESULT = -2147220892
VFW_E_UNSUPPORTED_STREAM: win32more.Foundation.HRESULT = -2147220891
VFW_E_NO_TRANSPORT: win32more.Foundation.HRESULT = -2147220890
VFW_S_STREAM_OFF: win32more.Foundation.HRESULT = 262759
VFW_S_CANT_CUE: win32more.Foundation.HRESULT = 262760
VFW_E_BAD_VIDEOCD: win32more.Foundation.HRESULT = -2147220887
VFW_S_NO_STOP_TIME: win32more.Foundation.HRESULT = 262768
VFW_E_OUT_OF_VIDEO_MEMORY: win32more.Foundation.HRESULT = -2147220879
VFW_E_VP_NEGOTIATION_FAILED: win32more.Foundation.HRESULT = -2147220878
VFW_E_DDRAW_CAPS_NOT_SUITABLE: win32more.Foundation.HRESULT = -2147220877
VFW_E_NO_VP_HARDWARE: win32more.Foundation.HRESULT = -2147220876
VFW_E_NO_CAPTURE_HARDWARE: win32more.Foundation.HRESULT = -2147220875
VFW_E_DVD_OPERATION_INHIBITED: win32more.Foundation.HRESULT = -2147220874
VFW_E_DVD_INVALIDDOMAIN: win32more.Foundation.HRESULT = -2147220873
VFW_E_DVD_NO_BUTTON: win32more.Foundation.HRESULT = -2147220872
VFW_E_DVD_GRAPHNOTREADY: win32more.Foundation.HRESULT = -2147220871
VFW_E_DVD_RENDERFAIL: win32more.Foundation.HRESULT = -2147220870
VFW_E_DVD_DECNOTENOUGH: win32more.Foundation.HRESULT = -2147220869
VFW_E_DDRAW_VERSION_NOT_SUITABLE: win32more.Foundation.HRESULT = -2147220868
VFW_E_COPYPROT_FAILED: win32more.Foundation.HRESULT = -2147220867
VFW_S_NOPREVIEWPIN: win32more.Foundation.HRESULT = 262782
VFW_E_TIME_EXPIRED: win32more.Foundation.HRESULT = -2147220865
VFW_S_DVD_NON_ONE_SEQUENTIAL: win32more.Foundation.HRESULT = 262784
VFW_E_DVD_WRONG_SPEED: win32more.Foundation.HRESULT = -2147220863
VFW_E_DVD_MENU_DOES_NOT_EXIST: win32more.Foundation.HRESULT = -2147220862
VFW_E_DVD_CMD_CANCELLED: win32more.Foundation.HRESULT = -2147220861
VFW_E_DVD_STATE_WRONG_VERSION: win32more.Foundation.HRESULT = -2147220860
VFW_E_DVD_STATE_CORRUPT: win32more.Foundation.HRESULT = -2147220859
VFW_E_DVD_STATE_WRONG_DISC: win32more.Foundation.HRESULT = -2147220858
VFW_E_DVD_INCOMPATIBLE_REGION: win32more.Foundation.HRESULT = -2147220857
VFW_E_DVD_NO_ATTRIBUTES: win32more.Foundation.HRESULT = -2147220856
VFW_E_DVD_NO_GOUP_PGC: win32more.Foundation.HRESULT = -2147220855
VFW_E_DVD_LOW_PARENTAL_LEVEL: win32more.Foundation.HRESULT = -2147220854
VFW_E_DVD_NOT_IN_KARAOKE_MODE: win32more.Foundation.HRESULT = -2147220853
VFW_S_DVD_CHANNEL_CONTENTS_NOT_AVAILABLE: win32more.Foundation.HRESULT = 262796
VFW_S_DVD_NOT_ACCURATE: win32more.Foundation.HRESULT = 262797
VFW_E_FRAME_STEP_UNSUPPORTED: win32more.Foundation.HRESULT = -2147220850
VFW_E_DVD_STREAM_DISABLED: win32more.Foundation.HRESULT = -2147220849
VFW_E_DVD_TITLE_UNKNOWN: win32more.Foundation.HRESULT = -2147220848
VFW_E_DVD_INVALID_DISC: win32more.Foundation.HRESULT = -2147220847
VFW_E_DVD_NO_RESUME_INFORMATION: win32more.Foundation.HRESULT = -2147220846
VFW_E_PIN_ALREADY_BLOCKED_ON_THIS_THREAD: win32more.Foundation.HRESULT = -2147220845
VFW_E_PIN_ALREADY_BLOCKED: win32more.Foundation.HRESULT = -2147220844
VFW_E_CERTIFICATION_FAILURE: win32more.Foundation.HRESULT = -2147220843
VFW_E_VMR_NOT_IN_MIXER_MODE: win32more.Foundation.HRESULT = -2147220842
VFW_E_VMR_NO_AP_SUPPLIED: win32more.Foundation.HRESULT = -2147220841
VFW_E_VMR_NO_DEINTERLACE_HW: win32more.Foundation.HRESULT = -2147220840
VFW_E_VMR_NO_PROCAMP_HW: win32more.Foundation.HRESULT = -2147220839
VFW_E_DVD_VMR9_INCOMPATIBLEDEC: win32more.Foundation.HRESULT = -2147220838
VFW_E_NO_COPP_HW: win32more.Foundation.HRESULT = -2147220837
VFW_E_DVD_NONBLOCKING: win32more.Foundation.HRESULT = -2147220836
VFW_E_DVD_TOO_MANY_RENDERERS_IN_FILTER_GRAPH: win32more.Foundation.HRESULT = -2147220835
VFW_E_DVD_NON_EVR_RENDERER_IN_FILTER_GRAPH: win32more.Foundation.HRESULT = -2147220834
VFW_E_DVD_RESOLUTION_ERROR: win32more.Foundation.HRESULT = -2147220833
E_PROP_SET_UNSUPPORTED: win32more.Foundation.HRESULT = -2147023726
E_PROP_ID_UNSUPPORTED: win32more.Foundation.HRESULT = -2147023728
VFW_E_CODECAPI_LINEAR_RANGE: win32more.Foundation.HRESULT = -2147220720
VFW_E_CODECAPI_ENUMERATED: win32more.Foundation.HRESULT = -2147220719
VFW_E_CODECAPI_NO_DEFAULT: win32more.Foundation.HRESULT = -2147220717
VFW_E_CODECAPI_NO_CURRENT_VALUE: win32more.Foundation.HRESULT = -2147220716
VFW_E_DVD_CHAPTER_DOES_NOT_EXIST: win32more.Foundation.HRESULT = -2147220715
VFW_S_DVD_RENDER_STATUS: win32more.Foundation.HRESULT = 262944
CFSTR_VFW_FILTERLIST: String = 'Video for Windows 4 Filters'
DXVA_ModeNone: Guid = Guid('1b81be00-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH261_A: Guid = Guid('1b81be01-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH261_B: Guid = Guid('1b81be02-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH263_A: Guid = Guid('1b81be03-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH263_B: Guid = Guid('1b81be04-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH263_C: Guid = Guid('1b81be05-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH263_D: Guid = Guid('1b81be06-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH263_E: Guid = Guid('1b81be07-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH263_F: Guid = Guid('1b81be08-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeMPEG1_A: Guid = Guid('1b81be09-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeMPEG1_VLD: Guid = Guid('6f3ec719-3735-42cc-80-63-65-cc-3c-b3-66-16')
DXVA_ModeMPEG2_A: Guid = Guid('1b81be0a-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeMPEG2_B: Guid = Guid('1b81be0b-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeMPEG2_C: Guid = Guid('1b81be0c-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeMPEG2_D: Guid = Guid('1b81be0d-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeMPEG2and1_VLD: Guid = Guid('86695f12-340e-4f04-9f-d3-92-53-dd-32-74-60')
DXVA_ModeH264_A: Guid = Guid('1b81be64-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH264_B: Guid = Guid('1b81be65-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH264_C: Guid = Guid('1b81be66-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH264_D: Guid = Guid('1b81be67-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH264_E: Guid = Guid('1b81be68-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH264_F: Guid = Guid('1b81be69-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeH264_VLD_WithFMOASO_NoFGT: Guid = Guid('d5f04ff9-3418-45d8-95-61-32-a7-6a-ae-2d-dd')
DXVA_ModeH264_VLD_Stereo_Progressive_NoFGT: Guid = Guid('d79be8da-0cf1-4c81-b8-2a-69-a4-e2-36-f4-3d')
DXVA_ModeH264_VLD_Stereo_NoFGT: Guid = Guid('f9aaccbb-c2b6-4cfc-87-79-57-07-b1-76-05-52')
DXVA_ModeH264_VLD_Multiview_NoFGT: Guid = Guid('705b9d82-76cf-49d6-b7-e6-ac-88-72-db-01-3c')
DXVA_ModeWMV8_A: Guid = Guid('1b81be80-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeWMV8_B: Guid = Guid('1b81be81-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeWMV9_A: Guid = Guid('1b81be90-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeWMV9_B: Guid = Guid('1b81be91-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeWMV9_C: Guid = Guid('1b81be94-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeVC1_A: Guid = Guid('1b81bea0-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeVC1_B: Guid = Guid('1b81bea1-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeVC1_C: Guid = Guid('1b81bea2-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeVC1_D: Guid = Guid('1b81bea3-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeVC1_D2010: Guid = Guid('1b81bea4-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_ModeMPEG4pt2_VLD_Simple: Guid = Guid('efd64d74-c9e8-41d7-a5-e9-e9-b0-e3-9f-a3-19')
DXVA_ModeMPEG4pt2_VLD_AdvSimple_NoGMC: Guid = Guid('ed418a9f-010d-4eda-9a-e3-9a-65-35-8d-8d-2e')
DXVA_ModeMPEG4pt2_VLD_AdvSimple_GMC: Guid = Guid('ab998b5b-4258-44a9-9f-eb-94-e5-97-a6-ba-ae')
DXVA_ModeHEVC_VLD_Main: Guid = Guid('5b11d51b-2f4c-4452-bc-c3-09-f2-a1-16-0c-c0')
DXVA_ModeHEVC_VLD_Main10: Guid = Guid('107af0e0-ef1a-4d19-ab-a8-67-a1-63-07-3d-13')
DXVA_ModeVP9_VLD_Profile0: Guid = Guid('463707f8-a1d0-4585-87-6d-83-aa-6d-60-b8-9e')
DXVA_ModeVP9_VLD_10bit_Profile2: Guid = Guid('a4c749ef-6ecf-48aa-84-48-50-a7-a1-16-5f-f7')
DXVA_ModeVP8_VLD: Guid = Guid('90b899ea-3a62-4705-88-b3-8d-f0-4b-27-44-e7')
DXVA_ModeAV1_VLD_Profile0: Guid = Guid('b8be4ccb-cf53-46ba-8d-59-d6-b8-a6-da-5d-2a')
DXVA_ModeAV1_VLD_Profile1: Guid = Guid('6936ff0f-45b1-4163-9c-c1-64-6e-f6-94-61-08')
DXVA_ModeAV1_VLD_Profile2: Guid = Guid('0c5f2aa1-e541-4089-bb-7b-98-11-0a-19-d7-c8')
DXVA_ModeAV1_VLD_12bit_Profile2: Guid = Guid('17127009-a00f-4ce1-99-4e-bf-40-81-f6-f3-f0')
DXVA_ModeAV1_VLD_12bit_Profile2_420: Guid = Guid('2d80bed6-9cac-4835-9e-91-32-7b-bc-4f-9e-e8')
DXVA_NoEncrypt: Guid = Guid('1b81bed0-a0c7-11d3-b9-84-00-c0-4f-2e-73-c5')
DXVA_RESTRICTED_MODE_UNRESTRICTED: UInt32 = 65535
DXVA_RESTRICTED_MODE_H261_A: UInt32 = 1
DXVA_RESTRICTED_MODE_H261_B: UInt32 = 2
DXVA_RESTRICTED_MODE_H263_A: UInt32 = 3
DXVA_RESTRICTED_MODE_H263_B: UInt32 = 4
DXVA_RESTRICTED_MODE_H263_C: UInt32 = 5
DXVA_RESTRICTED_MODE_H263_D: UInt32 = 6
DXVA_RESTRICTED_MODE_H263_E: UInt32 = 7
DXVA_RESTRICTED_MODE_H263_F: UInt32 = 8
DXVA_RESTRICTED_MODE_MPEG1_A: UInt32 = 9
DXVA_RESTRICTED_MODE_MPEG2_A: UInt32 = 10
DXVA_RESTRICTED_MODE_MPEG2_B: UInt32 = 11
DXVA_RESTRICTED_MODE_MPEG2_C: UInt32 = 12
DXVA_RESTRICTED_MODE_MPEG2_D: UInt32 = 13
DXVA_RESTRICTED_MODE_MPEG1_VLD: UInt32 = 16
DXVA_RESTRICTED_MODE_MPEG2and1_VLD: UInt32 = 17
DXVA_RESTRICTED_MODE_H264_A: UInt32 = 100
DXVA_RESTRICTED_MODE_H264_B: UInt32 = 101
DXVA_RESTRICTED_MODE_H264_C: UInt32 = 102
DXVA_RESTRICTED_MODE_H264_D: UInt32 = 103
DXVA_RESTRICTED_MODE_H264_E: UInt32 = 104
DXVA_RESTRICTED_MODE_H264_F: UInt32 = 105
DXVA_RESTRICTED_MODE_H264_VLD_WITHFMOASO_NOFGT: UInt32 = 112
DXVA_RESTRICTED_MODE_H264_VLD_STEREO_PROGRESSIVE_NOFGT: UInt32 = 113
DXVA_RESTRICTED_MODE_H264_VLD_STEREO_NOFGT: UInt32 = 114
DXVA_RESTRICTED_MODE_H264_VLD_MULTIVIEW_NOFGT: UInt32 = 115
DXVA_RESTRICTED_MODE_WMV8_A: UInt32 = 128
DXVA_RESTRICTED_MODE_WMV8_B: UInt32 = 129
DXVA_RESTRICTED_MODE_WMV9_A: UInt32 = 144
DXVA_RESTRICTED_MODE_WMV9_B: UInt32 = 145
DXVA_RESTRICTED_MODE_WMV9_C: UInt32 = 148
DXVA_RESTRICTED_MODE_VC1_A: UInt32 = 160
DXVA_RESTRICTED_MODE_VC1_B: UInt32 = 161
DXVA_RESTRICTED_MODE_VC1_C: UInt32 = 162
DXVA_RESTRICTED_MODE_VC1_D: UInt32 = 163
DXVA_RESTRICTED_MODE_VC1_D2010: UInt32 = 164
DXVA_RESTRICTED_MODE_MPEG4PT2_VLD_SIMPLE: UInt32 = 176
DXVA_RESTRICTED_MODE_MPEG4PT2_VLD_ADV_SIMPLE_NOGMC: UInt32 = 177
DXVA_RESTRICTED_MODE_MPEG4PT2_VLD_ADV_SIMPLE_GMC: UInt32 = 178
DXVA_RESTRICTED_MODE_WMV8_POSTPROC: UInt32 = 128
DXVA_RESTRICTED_MODE_WMV8_MOCOMP: UInt32 = 129
DXVA_RESTRICTED_MODE_WMV9_POSTPROC: UInt32 = 144
DXVA_RESTRICTED_MODE_WMV9_MOCOMP: UInt32 = 145
DXVA_RESTRICTED_MODE_WMV9_IDCT: UInt32 = 148
DXVA_RESTRICTED_MODE_VC1_POSTPROC: UInt32 = 160
DXVA_RESTRICTED_MODE_VC1_MOCOMP: UInt32 = 161
DXVA_RESTRICTED_MODE_VC1_IDCT: UInt32 = 162
DXVA_RESTRICTED_MODE_VC1_VLD: UInt32 = 163
DXVA_RESTRICTED_MODE_H264_MOCOMP_NOFGT: UInt32 = 100
DXVA_RESTRICTED_MODE_H264_MOCOMP_FGT: UInt32 = 101
DXVA_RESTRICTED_MODE_H264_IDCT_NOFGT: UInt32 = 102
DXVA_RESTRICTED_MODE_H264_IDCT_FGT: UInt32 = 103
DXVA_RESTRICTED_MODE_H264_VLD_NOFGT: UInt32 = 104
DXVA_RESTRICTED_MODE_H264_VLD_FGT: UInt32 = 105
DXVA_COMPBUFFER_TYPE_THAT_IS_NOT_USED: UInt32 = 0
DXVA_PICTURE_DECODE_BUFFER: UInt32 = 1
DXVA_MACROBLOCK_CONTROL_BUFFER: UInt32 = 2
DXVA_RESIDUAL_DIFFERENCE_BUFFER: UInt32 = 3
DXVA_DEBLOCKING_CONTROL_BUFFER: UInt32 = 4
DXVA_INVERSE_QUANTIZATION_MATRIX_BUFFER: UInt32 = 5
DXVA_SLICE_CONTROL_BUFFER: UInt32 = 6
DXVA_BITSTREAM_DATA_BUFFER: UInt32 = 7
DXVA_AYUV_BUFFER: UInt32 = 8
DXVA_IA44_SURFACE_BUFFER: UInt32 = 9
DXVA_DPXD_SURFACE_BUFFER: UInt32 = 10
DXVA_HIGHLIGHT_BUFFER: UInt32 = 11
DXVA_DCCMD_SURFACE_BUFFER: UInt32 = 12
DXVA_ALPHA_BLEND_COMBINATION_BUFFER: UInt32 = 13
DXVA_PICTURE_RESAMPLE_BUFFER: UInt32 = 14
DXVA_READ_BACK_BUFFER: UInt32 = 15
DXVA_MOTION_VECTOR_BUFFER: UInt32 = 16
DXVA_FILM_GRAIN_BUFFER: UInt32 = 17
DXVA_NUM_TYPES_COMP_BUFFERS: UInt32 = 18
DXVA_PICTURE_DECODING_FUNCTION: UInt32 = 1
DXVA_ALPHA_BLEND_DATA_LOAD_FUNCTION: UInt32 = 2
DXVA_ALPHA_BLEND_COMBINATION_FUNCTION: UInt32 = 3
DXVA_PICTURE_RESAMPLE_FUNCTION: UInt32 = 4
DXVA_DEBLOCKING_FILTER_FUNCTION: UInt32 = 5
DXVA_FILM_GRAIN_SYNTHESIS_FUNCTION: UInt32 = 6
DXVA_STATUS_REPORTING_FUNCTION: UInt32 = 7
DXVA_EXECUTE_RETURN_OK: UInt32 = 0
DXVA_EXECUTE_RETURN_DATA_ERROR_MINOR: UInt32 = 1
DXVA_EXECUTE_RETURN_DATA_ERROR_SIGNIF: UInt32 = 2
DXVA_EXECUTE_RETURN_DATA_ERROR_SEVERE: UInt32 = 3
DXVA_EXECUTE_RETURN_OTHER_ERROR_SEVERE: UInt32 = 4
DXVA_QUERYORREPLYFUNCFLAG_DECODER_PROBE_QUERY: UInt32 = 16777201
DXVA_QUERYORREPLYFUNCFLAG_DECODER_LOCK_QUERY: UInt32 = 16777205
DXVA_QUERYORREPLYFUNCFLAG_ACCEL_PROBE_OK_COPY: UInt32 = 16777208
DXVA_QUERYORREPLYFUNCFLAG_ACCEL_PROBE_OK_PLUS: UInt32 = 16777209
DXVA_QUERYORREPLYFUNCFLAG_ACCEL_LOCK_OK_COPY: UInt32 = 16777212
DXVA_QUERYORREPLYFUNCFLAG_ACCEL_PROBE_FALSE_PLUS: UInt32 = 16777211
DXVA_QUERYORREPLYFUNCFLAG_ACCEL_LOCK_FALSE_PLUS: UInt32 = 16777215
DXVA_ENCRYPTPROTOCOLFUNCFLAG_HOST: UInt32 = 16776960
DXVA_ENCRYPTPROTOCOLFUNCFLAG_ACCEL: UInt32 = 16776968
DXVA_CHROMA_FORMAT_420: UInt32 = 1
DXVA_CHROMA_FORMAT_422: UInt32 = 2
DXVA_CHROMA_FORMAT_444: UInt32 = 3
DXVA_PICTURE_STRUCTURE_TOP_FIELD: UInt32 = 1
DXVA_PICTURE_STRUCTURE_BOTTOM_FIELD: UInt32 = 2
DXVA_PICTURE_STRUCTURE_FRAME: UInt32 = 3
DXVA_BIDIRECTIONAL_AVERAGING_MPEG2_ROUND: UInt32 = 0
DXVA_BIDIRECTIONAL_AVERAGING_H263_TRUNC: UInt32 = 1
DXVA_MV_PRECISION_AND_CHROMA_RELATION_MPEG2: UInt32 = 0
DXVA_MV_PRECISION_AND_CHROMA_RELATION_H263: UInt32 = 1
DXVA_MV_PRECISION_AND_CHROMA_RELATION_H261: UInt32 = 2
DXVA_SCAN_METHOD_ZIG_ZAG: UInt32 = 0
DXVA_SCAN_METHOD_ALTERNATE_VERTICAL: UInt32 = 1
DXVA_SCAN_METHOD_ALTERNATE_HORIZONTAL: UInt32 = 2
DXVA_SCAN_METHOD_ARBITRARY: UInt32 = 3
DXVA_BITSTREAM_CONCEALMENT_NEED_UNLIKELY: UInt32 = 0
DXVA_BITSTREAM_CONCEALMENT_NEED_MILD: UInt32 = 1
DXVA_BITSTREAM_CONCEALMENT_NEED_LIKELY: UInt32 = 2
DXVA_BITSTREAM_CONCEALMENT_NEED_SEVERE: UInt32 = 3
DXVA_BITSTREAM_CONCEALMENT_METHOD_UNSPECIFIED: UInt32 = 0
DXVA_BITSTREAM_CONCEALMENT_METHOD_INTRA: UInt32 = 1
DXVA_BITSTREAM_CONCEALMENT_METHOD_FORWARD: UInt32 = 2
DXVA_BITSTREAM_CONCEALMENT_METHOD_BACKWARD: UInt32 = 3
DXVA_USUAL_BLOCK_WIDTH: UInt32 = 8
DXVA_USUAL_BLOCK_HEIGHT: UInt32 = 8
DXVA_NumMV_OBMC_off_BinPBwith4MV_off: UInt32 = 4
DXVA_NumMV_OBMC_off_BinPBwith4MV_on: UInt32 = 5
DXVA_NumMV_OBMC_on__BinPB_off: UInt32 = 10
DXVA_NumMV_OBMC_on__BinPB_on: UInt32 = 11
DXVA_CONFIG_DATA_TYPE_IA44: UInt32 = 0
DXVA_CONFIG_DATA_TYPE_AI44: UInt32 = 1
DXVA_CONFIG_DATA_TYPE_DPXD: UInt32 = 2
DXVA_CONFIG_DATA_TYPE_AYUV: UInt32 = 3
DXVA_CONFIG_BLEND_TYPE_FRONT_BUFFER: UInt32 = 0
DXVA_CONFIG_BLEND_TYPE_BACK_HARDWARE: UInt32 = 1
DXVA_ExtColorData_ShiftBase: UInt32 = 8
DXVA_DeinterlaceBobDevice: Guid = Guid('335aa36e-7884-43a4-9c-91-7f-87-fa-f3-e3-7e')
DXVA_DeinterlaceContainerDevice: Guid = Guid('0e85cb93-3046-4ff0-ae-cc-d5-8c-b5-f0-35-fd')
MAX_DEINTERLACE_SURFACES: UInt32 = 32
DXVA_DeinterlaceBltFnCode: UInt32 = 1
DXVA_DeinterlaceBltExFnCode: UInt32 = 2
MAX_DEINTERLACE_DEVICE_GUIDS: UInt32 = 32
DXVA_DeinterlaceQueryAvailableModesFnCode: UInt32 = 1
DXVA_DeinterlaceQueryModeCapsFnCode: UInt32 = 2
DXVA_ProcAmpControlDevice: Guid = Guid('9f200913-2ffd-4056-9f-1e-e1-b5-08-f2-2d-cf')
DXVA_ProcAmpControlQueryCapsFnCode: UInt32 = 3
DXVA_ProcAmpControlQueryRangeFnCode: UInt32 = 4
DXVA_ProcAmpControlBltFnCode: UInt32 = 1
DXVA_COPPDevice: Guid = Guid('d2457add-8999-45ed-8a-8a-d1-aa-04-7b-a4-d5')
DXVA_COPPGetCertificateLengthFnCode: UInt32 = 1
DXVA_COPPKeyExchangeFnCode: UInt32 = 2
DXVA_COPPSequenceStartFnCode: UInt32 = 3
DXVA_COPPCommandFnCode: UInt32 = 4
DXVA_COPPSetProtectionLevel: Guid = Guid('9bb9327c-4eb5-4727-9f-00-b4-2b-09-19-c0-da')
COPP_NoProtectionLevelAvailable: Int32 = -1
COPP_DefaultProtectionLevel: UInt32 = 0
DXVA_COPPSetSignaling: Guid = Guid('09a631a5-d684-4c60-8e-4d-d3-bb-0f-0b-e3-ee')
COPP_ImageAspectRatio_EN300294_Mask: UInt32 = 7
DXVA_COPPQueryStatusFnCode: UInt32 = 5
DXVA_COPPQueryConnectorType: Guid = Guid('81d0bfd5-6afe-48c2-99-c0-95-a0-8f-97-c5-da')
DXVA_COPPQueryProtectionType: Guid = Guid('38f2a801-9a6c-48bb-91-07-b6-69-6e-6f-17-97')
DXVA_COPPQueryLocalProtectionLevel: Guid = Guid('b2075857-3eda-4d5d-88-db-74-8f-8c-1a-05-49')
DXVA_COPPQueryGlobalProtectionLevel: Guid = Guid('1957210a-7766-452a-b9-9a-d2-7a-ed-54-f0-3a')
DXVA_COPPQueryDisplayData: Guid = Guid('d7bf1ba3-ad13-4f8e-af-98-0d-cb-3c-a2-04-cc')
DXVA_COPPQueryHDCPKeyData: Guid = Guid('0db59d74-a992-492e-a0-bd-c2-3f-da-56-4e-00')
DXVA_COPPQueryBusData: Guid = Guid('c6f4d673-6174-4184-8e-35-f6-db-52-00-bc-ba')
DXVA_COPPQuerySignaling: Guid = Guid('6629a591-3b79-4cf3-92-4a-11-e8-e7-81-16-71')
DXVA2Trace_Control: Guid = Guid('a0386e75-f70c-464c-a9-ce-33-c4-4e-09-16-23')
DXVA2Trace_DecodeDevCreated: Guid = Guid('b4de17a1-c5b2-44fe-86-d5-d9-7a-64-81-14-ff')
DXVA2Trace_DecodeDevDestroyed: Guid = Guid('853ebdf2-4160-421d-88-93-63-dc-ea-4f-18-bb')
DXVA2Trace_DecodeDevBeginFrame: Guid = Guid('9fd1acf6-44cb-4637-bc-62-2c-11-a9-60-8f-90')
DXVA2Trace_DecodeDevExecute: Guid = Guid('850aeb4c-d19a-4609-b3-b4-bc-bf-0e-22-12-1e')
DXVA2Trace_DecodeDevGetBuffer: Guid = Guid('57b128fb-72cb-4137-a5-75-d9-1f-a3-16-08-97')
DXVA2Trace_DecodeDevEndFrame: Guid = Guid('9fb3cb33-47dc-4899-98-c8-c0-c6-cd-7c-d3-cb')
DXVA2Trace_VideoProcessDevCreated: Guid = Guid('895508c6-540d-4c87-98-f8-8d-cb-f2-da-bb-2a')
DXVA2Trace_VideoProcessDevDestroyed: Guid = Guid('f97f30b1-fb49-42c7-8e-e8-88-bd-fa-92-d4-e2')
DXVA2Trace_VideoProcessBlt: Guid = Guid('69089cc0-71ab-42d0-95-3a-28-87-bf-05-a8-af')
MSTapeDeviceGUID: Guid = Guid('8c0f6af2-0edb-44c1-8a-eb-59-04-0b-d8-30-ed')
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
SID_MSVidCtl_CurrentAudioEndpoint: Guid = Guid('cf9a88f4-abcf-4ed8-9b-74-7d-b3-34-45-45-9e')
STREAMBUFFER_EC_BASE: UInt32 = 806
EVENTID_SBE2RecControlStarted: Guid = Guid('8966a89e-f83e-4c0e-bc-3b-bf-a7-64-9e-04-cb')
EVENTID_SBE2RecControlStopped: Guid = Guid('454b1ec8-0c9b-4caa-b1-a1-1e-7a-26-66-f6-c3')
SBE2_STREAM_DESC_EVENT: Guid = Guid('2313a4ed-bf2d-454f-ad-8a-d9-5b-a7-f9-1f-ee')
SBE2_V1_STREAMS_CREATION_EVENT: Guid = Guid('000fcf09-97f5-46ac-97-69-7a-83-b3-53-84-fb')
SBE2_V2_STREAMS_CREATION_EVENT: Guid = Guid('a72530a3-0344-4cab-a2-d0-fe-93-7d-bd-ca-b3')
SBE2_STREAM_DESC_VERSION: UInt32 = 1
SID_DRMSecureServiceChannel: Guid = Guid('c4c4c4c4-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CLSID_ETFilterEncProperties: Guid = Guid('c4c4c481-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CLSID_ETFilterTagProperties: Guid = Guid('c4c4c491-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CLSID_PTFilter: Guid = Guid('9cd31617-b303-4f96-83-30-2e-b1-73-ea-4d-c6')
CLSID_DTFilterEncProperties: Guid = Guid('c4c4c482-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CLSID_DTFilterTagProperties: Guid = Guid('c4c4c492-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CLSID_XDSCodecProperties: Guid = Guid('c4c4c483-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CLSID_XDSCodecTagProperties: Guid = Guid('c4c4c493-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CLSID_CPCAFiltersCategory: Guid = Guid('c4c4c4fc-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_XDSCodecNewXDSRating: Guid = Guid('c4c4c4e0-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_XDSCodecDuplicateXDSRating: Guid = Guid('c4c4c4df-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_XDSCodecNewXDSPacket: Guid = Guid('c4c4c4e1-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterRatingChange: Guid = Guid('c4c4c4e2-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterRatingsBlock: Guid = Guid('c4c4c4e3-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterRatingsUnblock: Guid = Guid('c4c4c4e4-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterXDSPacket: Guid = Guid('c4c4c4e5-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_ETFilterEncryptionOn: Guid = Guid('c4c4c4e6-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_ETFilterEncryptionOff: Guid = Guid('c4c4c4e7-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterCOPPUnblock: Guid = Guid('c4c4c4e8-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_EncDecFilterError: Guid = Guid('c4c4c4e9-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterCOPPBlock: Guid = Guid('c4c4c4ea-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_ETFilterCopyOnce: Guid = Guid('c4c4c4eb-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_ETFilterCopyNever: Guid = Guid('c4c4c4f0-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterDataFormatOK: Guid = Guid('c4c4c4ec-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_DTFilterDataFormatFailure: Guid = Guid('c4c4c4ed-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_ETDTFilterLicenseOK: Guid = Guid('c4c4c4ee-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_ETDTFilterLicenseFailure: Guid = Guid('c4c4c4ef-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
MEDIASUBTYPE_ETDTFilter_Tagged: Guid = Guid('c4c4c4d0-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
FORMATTYPE_ETDTFilter_Tagged: Guid = Guid('c4c4c4d1-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
MEDIASUBTYPE_CPFilters_Processed: Guid = Guid('46adbd28-6fd0-4796-93-b2-15-5c-51-dc-04-8d')
FORMATTYPE_CPFilters_Processed: Guid = Guid('6739b36f-1d5f-4ac2-81-92-28-bb-0e-73-d1-6a')
EVENTID_EncDecFilterEvent: Guid = Guid('4a1b465b-0fb9-4159-af-bd-e3-30-06-a0-f9-f4')
EVENTID_FormatNotSupportedEvent: Guid = Guid('24b2280a-b2aa-4777-bf-65-63-f3-5e-7b-02-4a')
EVENTID_DemultiplexerFilterDiscontinuity: Guid = Guid('16155770-aed5-475c-bb-98-95-a3-30-70-df-0c')
DSATTRIB_WMDRMProtectionInfo: Guid = Guid('40749583-6b9d-4eec-b4-3c-67-a1-80-1e-1a-9b')
DSATTRIB_BadSampleInfo: Guid = Guid('e4846dda-5838-42b4-b8-97-6f-7e-5f-aa-2f-2f')
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
CLSID_Mpeg2TableFilter: Guid = Guid('752845f1-758f-4c83-a0-43-42-70-c5-93-30-8e')
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
g_wszExcludeScriptStreamDeliverySynchronization: String = 'ExcludeScriptStreamDeliverySynchronization'
MPEG2_BASE: UInt32 = 512
MPEG2_S_MORE_DATA_AVAILABLE: win32more.Foundation.HRESULT = 262656
MPEG2_S_NO_MORE_DATA_AVAILABLE: win32more.Foundation.HRESULT = 262657
MPEG2_S_SG_INFO_FOUND: win32more.Foundation.HRESULT = 262658
MPEG2_S_SG_INFO_NOT_FOUND: win32more.Foundation.HRESULT = 262659
MPEG2_S_MPE_INFO_FOUND: win32more.Foundation.HRESULT = 262660
MPEG2_S_MPE_INFO_NOT_FOUND: win32more.Foundation.HRESULT = 262661
MPEG2_S_NEW_MODULE_VERSION: win32more.Foundation.HRESULT = 262662
MPEG2_E_UNINITIALIZED: win32more.Foundation.HRESULT = -2147220992
MPEG2_E_ALREADY_INITIALIZED: win32more.Foundation.HRESULT = -2147220991
MPEG2_E_OUT_OF_BOUNDS: win32more.Foundation.HRESULT = -2147220990
MPEG2_E_MALFORMED_TABLE: win32more.Foundation.HRESULT = -2147220989
MPEG2_E_UNDEFINED: win32more.Foundation.HRESULT = -2147220988
MPEG2_E_NOT_PRESENT: win32more.Foundation.HRESULT = -2147220987
MPEG2_E_SECTION_NOT_FOUND: win32more.Foundation.HRESULT = -2147220986
MPEG2_E_TX_STREAM_UNAVAILABLE: win32more.Foundation.HRESULT = -2147220985
MPEG2_E_SERVICE_ID_NOT_FOUND: win32more.Foundation.HRESULT = -2147220984
MPEG2_E_SERVICE_PMT_NOT_FOUND: win32more.Foundation.HRESULT = -2147220983
MPEG2_E_DSI_NOT_FOUND: win32more.Foundation.HRESULT = -2147220982
MPEG2_E_SERVER_UNAVAILABLE: win32more.Foundation.HRESULT = -2147220981
MPEG2_E_INVALID_CAROUSEL_ID: win32more.Foundation.HRESULT = -2147220980
MPEG2_E_MALFORMED_DSMCC_MESSAGE: win32more.Foundation.HRESULT = -2147220979
MPEG2_E_INVALID_SG_OBJECT_KIND: win32more.Foundation.HRESULT = -2147220978
MPEG2_E_OBJECT_NOT_FOUND: win32more.Foundation.HRESULT = -2147220977
MPEG2_E_OBJECT_KIND_NOT_A_DIRECTORY: win32more.Foundation.HRESULT = -2147220976
MPEG2_E_OBJECT_KIND_NOT_A_FILE: win32more.Foundation.HRESULT = -2147220975
MPEG2_E_FILE_OFFSET_TOO_BIG: win32more.Foundation.HRESULT = -2147220974
MPEG2_E_STREAM_STOPPED: win32more.Foundation.HRESULT = -2147220973
MPEG2_E_REGISTRY_ACCESS_FAILED: win32more.Foundation.HRESULT = -2147220972
MPEG2_E_INVALID_UDP_PORT: win32more.Foundation.HRESULT = -2147220971
MPEG2_E_DATA_SOURCE_FAILED: win32more.Foundation.HRESULT = -2147220970
MPEG2_E_DII_NOT_FOUND: win32more.Foundation.HRESULT = -2147220969
MPEG2_E_DSHOW_PIN_NOT_FOUND: win32more.Foundation.HRESULT = -2147220968
MPEG2_E_BUFFER_TOO_SMALL: win32more.Foundation.HRESULT = -2147220967
MPEG2_E_MISSING_SECTIONS: win32more.Foundation.HRESULT = -2147220966
MPEG2_E_TOO_MANY_SECTIONS: win32more.Foundation.HRESULT = -2147220965
MPEG2_E_NEXT_TABLE_OPS_NOT_AVAILABLE: win32more.Foundation.HRESULT = -2147220964
MPEG2_E_INCORRECT_DESCRIPTOR_TAG: win32more.Foundation.HRESULT = -2147220963
MSDRI_S_MMI_PENDING: win32more.Foundation.HRESULT = 2
MSDRI_S_PENDING: win32more.Foundation.HRESULT = 1
BDA_E_FAILURE: win32more.Foundation.HRESULT = -1073479679
BDA_E_NOT_IMPLEMENTED: win32more.Foundation.HRESULT = -1073479678
BDA_E_NO_SUCH_COMMAND: win32more.Foundation.HRESULT = -1073479677
BDA_E_OUT_OF_BOUNDS: win32more.Foundation.HRESULT = -1073479676
BDA_E_INVALID_SCHEMA: win32more.Foundation.HRESULT = -1073479675
BDA_E_INVALID_HANDLE: win32more.Foundation.HRESULT = -1073479674
BDA_E_INVALID_TYPE: win32more.Foundation.HRESULT = -1073479673
BDA_E_READ_ONLY: win32more.Foundation.HRESULT = -1073479672
BDA_E_ACCESS_DENIED: win32more.Foundation.HRESULT = -1073479671
BDA_E_NOT_FOUND: win32more.Foundation.HRESULT = -1073479670
BDA_E_BUFFER_TOO_SMALL: win32more.Foundation.HRESULT = -1073479669
BDA_E_OUT_OF_RESOURCES: win32more.Foundation.HRESULT = -1073479668
BDA_E_OUT_OF_MEMORY: win32more.Foundation.HRESULT = -1073479667
BDA_E_DISABLED: win32more.Foundation.HRESULT = -1073479666
BDA_E_NO_HANDLER: win32more.Foundation.HRESULT = -1073479665
BDA_E_INVALID_LANGUAGE: win32more.Foundation.HRESULT = -1073479664
BDA_E_TIMEOUT_ELAPSED: win32more.Foundation.HRESULT = -1073479663
BDA_E_NO_MORE_EVENTS: win32more.Foundation.HRESULT = -1073475583
BDA_E_NO_MORE_DATA: win32more.Foundation.HRESULT = -1073475582
BDA_E_TUNER_INITIALIZING: win32more.Foundation.HRESULT = -1073467391
BDA_E_TUNER_REQUIRED: win32more.Foundation.HRESULT = -1073467390
BDA_E_TUNER_CONFLICT: win32more.Foundation.HRESULT = -1073467389
BDA_E_INVALID_TUNE_REQUEST: win32more.Foundation.HRESULT = -1073467388
BDA_E_INVALID_ENTITLEMENT_TOKEN: win32more.Foundation.HRESULT = -1073463295
BDA_E_INVALID_CAPTURE_TOKEN: win32more.Foundation.HRESULT = -1073463294
BDA_E_WOULD_DISRUPT_STREAMING: win32more.Foundation.HRESULT = -1073463293
BDA_E_INVALID_PURCHASE_TOKEN: win32more.Foundation.HRESULT = -1073463292
BDA_E_IPNETWORK_ERROR: win32more.Foundation.HRESULT = -1073459199
BDA_E_IPNETWORK_ADDRESS_NOT_FOUND: win32more.Foundation.HRESULT = -1073459198
BDA_E_IPNETWORK_TIMEOUT: win32more.Foundation.HRESULT = -1073459197
BDA_E_IPNETWORK_UNAVAILABLE: win32more.Foundation.HRESULT = -1073459196
BDA_E_TUNE_FAILED_SDV01: win32more.Foundation.HRESULT = -1073455103
BDA_E_TUNE_FAILED_SDV02: win32more.Foundation.HRESULT = -1073455102
BDA_E_TUNE_FAILED_SDV03: win32more.Foundation.HRESULT = -1073455101
BDA_E_TUNE_FAILED_SDV04: win32more.Foundation.HRESULT = -1073455100
BDA_E_TUNE_FAILED_SDV05: win32more.Foundation.HRESULT = -1073455099
BDA_E_TUNE_FAILED_SDV06: win32more.Foundation.HRESULT = -1073455098
BDA_E_TUNE_FAILED_SDV07: win32more.Foundation.HRESULT = -1073455097
BDA_E_TUNE_FAILED_SDV08: win32more.Foundation.HRESULT = -1073455096
BDA_E_TUNE_FAILED_SDVFF: win32more.Foundation.HRESULT = -1073454849
BDA_E_WMDRM_INVALID_SIGNATURE: win32more.Foundation.HRESULT = -1073418239
BDA_E_WMDRM_INVALID_CERTIFICATE: win32more.Foundation.HRESULT = -1073418238
BDA_E_WMDRM_INVALID_VERSION: win32more.Foundation.HRESULT = -1073418236
BDA_E_WMDRM_INVALID_DATE: win32more.Foundation.HRESULT = -1073418235
BDA_E_WMDRM_INVALID_PROXIMITY: win32more.Foundation.HRESULT = -1073418234
BDA_E_WMDRM_KEY_ID_NOT_FOUND: win32more.Foundation.HRESULT = -1073418232
SPECIFYPAGES_STATISTICS: Guid = Guid('4c437b92-6e9e-11d1-a7-04-00-60-97-c4-e4-76')
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
@winfunctype('QUARTZ.dll')
def AMGetErrorTextA(hr: win32more.Foundation.HRESULT, pbuffer: win32more.Foundation.PSTR, MaxLen: UInt32) -> UInt32: ...
@winfunctype('QUARTZ.dll')
def AMGetErrorTextW(hr: win32more.Foundation.HRESULT, pbuffer: win32more.Foundation.PWSTR, MaxLen: UInt32) -> UInt32: ...
ApplicationTypeType = Int32
SCTE28_ConditionalAccess: ApplicationTypeType = 0
SCTE28_POD_Host_Binding_Information: ApplicationTypeType = 1
SCTE28_IPService: ApplicationTypeType = 2
SCTE28_NetworkInterface_SCTE55_2: ApplicationTypeType = 3
SCTE28_NetworkInterface_SCTE55_1: ApplicationTypeType = 4
SCTE28_CopyProtection: ApplicationTypeType = 5
SCTE28_Diagnostic: ApplicationTypeType = 6
SCTE28_Undesignated: ApplicationTypeType = 7
SCTE28_Reserved: ApplicationTypeType = 8
AuxInTuningSpace = Guid('f9769a06-7aca-4e39-9c-fb-97-bb-35-f0-e7-7e')
BDANETWORKTYPE_ATSC = Guid('71985f51-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
class BDANODE_DESCRIPTOR(Structure):
    ulBdaNodeType: UInt32
    guidFunction: Guid
    guidName: Guid
class BDA_BUFFER(Structure):
    lResult: Int32
    ulBufferSize: UInt32
    argbBuffer: Byte * 1
class BDA_CAS_CHECK_ENTITLEMENTTOKEN(Structure):
    lResult: Int32
    ulDescrambleStatus: UInt32
class BDA_CAS_CLOSEMMIDATA(Structure):
    ulDialogNumber: UInt32
class BDA_CAS_CLOSE_MMIDIALOG(Structure):
    lResult: Int32
    SessionResult: UInt32
class BDA_CAS_OPENMMIDATA(Structure):
    ulDialogNumber: UInt32
    ulDialogRequest: UInt32
    uuidDialogType: Guid
    usDialogDataLength: UInt16
    argbDialogData: Byte * 1
class BDA_CAS_REQUESTTUNERDATA(Structure):
    ucRequestPriority: Byte
    ucRequestReason: Byte
    ucRequestConsequences: Byte
    ulEstimatedTime: UInt32
class BDA_CA_MODULE_UI(Structure):
    ulFormat: UInt32
    ulbcDesc: UInt32
    ulDesc: UInt32 * 1
BDA_CHANGE_STATE = Int32
BDA_CHANGES_COMPLETE: BDA_CHANGE_STATE = 0
BDA_CHANGES_PENDING: BDA_CHANGE_STATE = 1
BDA_CONDITIONALACCESS_MMICLOSEREASON = Int32
CONDITIONALACCESS_UNSPECIFIED: BDA_CONDITIONALACCESS_MMICLOSEREASON = 0
CONDITIONALACCESS_CLOSED_ITSELF: BDA_CONDITIONALACCESS_MMICLOSEREASON = 1
CONDITIONALACCESS_TUNER_REQUESTED_CLOSE: BDA_CONDITIONALACCESS_MMICLOSEREASON = 2
CONDITIONALACCESS_DIALOG_TIMEOUT: BDA_CONDITIONALACCESS_MMICLOSEREASON = 3
CONDITIONALACCESS_DIALOG_FOCUS_CHANGE: BDA_CONDITIONALACCESS_MMICLOSEREASON = 4
CONDITIONALACCESS_DIALOG_USER_DISMISSED: BDA_CONDITIONALACCESS_MMICLOSEREASON = 5
CONDITIONALACCESS_DIALOG_USER_NOT_AVAILABLE: BDA_CONDITIONALACCESS_MMICLOSEREASON = 6
BDA_CONDITIONALACCESS_REQUESTTYPE = Int32
CONDITIONALACCESS_ACCESS_UNSPECIFIED: BDA_CONDITIONALACCESS_REQUESTTYPE = 0
CONDITIONALACCESS_ACCESS_NOT_POSSIBLE: BDA_CONDITIONALACCESS_REQUESTTYPE = 1
CONDITIONALACCESS_ACCESS_POSSIBLE: BDA_CONDITIONALACCESS_REQUESTTYPE = 2
CONDITIONALACCESS_ACCESS_POSSIBLE_NO_STREAMING_DISRUPTION: BDA_CONDITIONALACCESS_REQUESTTYPE = 3
BDA_CONDITIONALACCESS_SESSION_RESULT = Int32
CONDITIONALACCESS_SUCCESSFULL: BDA_CONDITIONALACCESS_SESSION_RESULT = 0
CONDITIONALACCESS_ENDED_NOCHANGE: BDA_CONDITIONALACCESS_SESSION_RESULT = 1
CONDITIONALACCESS_ABORTED: BDA_CONDITIONALACCESS_SESSION_RESULT = 2
BDA_Channel = Int32
BDA_UNDEFINED_CHANNEL: BDA_Channel = -1
BDA_Channel_Bandwidth = Int32
BDA_CHAN_BANDWITH_NOT_SET: BDA_Channel_Bandwidth = -1
BDA_CHAN_BANDWITH_NOT_DEFINED: BDA_Channel_Bandwidth = 0
BDA_Comp_Flags = Int32
BDACOMP_NOT_DEFINED: BDA_Comp_Flags = 0
BDACOMP_EXCLUDE_TS_FROM_TR: BDA_Comp_Flags = 1
BDACOMP_INCLUDE_LOCATOR_IN_TR: BDA_Comp_Flags = 2
BDACOMP_INCLUDE_COMPONENTS_IN_TR: BDA_Comp_Flags = 4
class BDA_DEBUG_DATA(Structure):
    lResult: Int32
    uuidDebugDataType: Guid
    ulDataSize: UInt32
    argbDebugData: Byte * 1
BDA_DEBUG_DATA_AVAILABLE = Guid('69c24f54-9983-497e-b4-15-28-2b-e4-c5-55-fb')
BDA_DEBUG_DATA_TYPE_STRING = Guid('a806e767-de5c-430c-80-bf-a2-1e-be-06-c7-48')
BDA_DISCOVERY_STATE = Int32
BDA_DISCOVERY_UNSPECIFIED: BDA_DISCOVERY_STATE = 0
BDA_DISCOVERY_REQUIRED: BDA_DISCOVERY_STATE = 1
BDA_DISCOVERY_COMPLETE: BDA_DISCOVERY_STATE = 2
class BDA_DISEQC_RESPONSE(Structure):
    ulRequestId: UInt32
    ulPacketLength: UInt32
    argbPacketData: Byte * 8
class BDA_DISEQC_SEND(Structure):
    ulRequestId: UInt32
    ulPacketLength: UInt32
    argbPacketData: Byte * 8
class BDA_DRM_DRMSTATUS(Structure):
    lResult: Int32
    DRMuuid: Guid
    ulDrmUuidListStringSize: UInt32
    argbDrmUuidListString: Guid * 1
class BDA_DVBT2_L1_SIGNALLING_DATA(Structure):
    L1Pre_TYPE: Byte
    L1Pre_BWT_S1_S2: Byte
    L1Pre_REPETITION_GUARD_PAPR: Byte
    L1Pre_MOD_COD_FEC: Byte
    L1Pre_POSTSIZE_INFO_PILOT: Byte * 5
    L1Pre_TX_ID_AVAIL: Byte
    L1Pre_CELL_ID: Byte * 2
    L1Pre_NETWORK_ID: Byte * 2
    L1Pre_T2SYSTEM_ID: Byte * 2
    L1Pre_NUM_T2_FRAMES: Byte
    L1Pre_NUM_DATA_REGENFLAG_L1POSTEXT: Byte * 2
    L1Pre_NUMRF_CURRENTRF_RESERVED: Byte * 2
    L1Pre_CRC32: Byte * 4
    L1PostData: Byte * 1
BDA_DigitalSignalStandard = Int32
Bda_DigitalStandard_None: BDA_DigitalSignalStandard = 0
Bda_DigitalStandard_DVB_T: BDA_DigitalSignalStandard = 1
Bda_DigitalStandard_DVB_S: BDA_DigitalSignalStandard = 2
Bda_DigitalStandard_DVB_C: BDA_DigitalSignalStandard = 4
Bda_DigitalStandard_ATSC: BDA_DigitalSignalStandard = 8
Bda_DigitalStandard_ISDB_T: BDA_DigitalSignalStandard = 16
Bda_DigitalStandard_ISDB_S: BDA_DigitalSignalStandard = 32
Bda_DigitalStandard_ISDB_C: BDA_DigitalSignalStandard = 64
BDA_DrmPairingError = Int32
BDA_DrmPairing_Succeeded: BDA_DrmPairingError = 0
BDA_DrmPairing_HardwareFailure: BDA_DrmPairingError = 1
BDA_DrmPairing_NeedRevocationData: BDA_DrmPairingError = 2
BDA_DrmPairing_NeedIndiv: BDA_DrmPairingError = 3
BDA_DrmPairing_Other: BDA_DrmPairingError = 4
BDA_DrmPairing_DrmInitFailed: BDA_DrmPairingError = 5
BDA_DrmPairing_DrmNotPaired: BDA_DrmPairingError = 6
BDA_DrmPairing_DrmRePairSoon: BDA_DrmPairingError = 7
BDA_DrmPairing_Aborted: BDA_DrmPairingError = 8
BDA_DrmPairing_NeedSDKUpdate: BDA_DrmPairingError = 9
class BDA_ETHERNET_ADDRESS(Structure):
    rgbAddress: Byte * 6
class BDA_ETHERNET_ADDRESS_LIST(Structure):
    ulcAddresses: UInt32
    rgAddressl: win32more.Media.DirectShow.BDA_ETHERNET_ADDRESS * 1
class BDA_EVENT_DATA(Structure):
    lResult: Int32
    ulEventID: UInt32
    uuidEventType: Guid
    ulEventDataLength: UInt32
    argbEventData: Byte * 1
BDA_EVENT_ID = Int32
BDA_EVENT_SIGNAL_LOSS: BDA_EVENT_ID = 0
BDA_EVENT_SIGNAL_LOCK: BDA_EVENT_ID = 1
BDA_EVENT_DATA_START: BDA_EVENT_ID = 2
BDA_EVENT_DATA_STOP: BDA_EVENT_ID = 3
BDA_EVENT_CHANNEL_ACQUIRED: BDA_EVENT_ID = 4
BDA_EVENT_CHANNEL_LOST: BDA_EVENT_ID = 5
BDA_EVENT_CHANNEL_SOURCE_CHANGED: BDA_EVENT_ID = 6
BDA_EVENT_CHANNEL_ACTIVATED: BDA_EVENT_ID = 7
BDA_EVENT_CHANNEL_DEACTIVATED: BDA_EVENT_ID = 8
BDA_EVENT_SUBCHANNEL_ACQUIRED: BDA_EVENT_ID = 9
BDA_EVENT_SUBCHANNEL_LOST: BDA_EVENT_ID = 10
BDA_EVENT_SUBCHANNEL_SOURCE_CHANGED: BDA_EVENT_ID = 11
BDA_EVENT_SUBCHANNEL_ACTIVATED: BDA_EVENT_ID = 12
BDA_EVENT_SUBCHANNEL_DEACTIVATED: BDA_EVENT_ID = 13
BDA_EVENT_ACCESS_GRANTED: BDA_EVENT_ID = 14
BDA_EVENT_ACCESS_DENIED: BDA_EVENT_ID = 15
BDA_EVENT_OFFER_EXTENDED: BDA_EVENT_ID = 16
BDA_EVENT_PURCHASE_COMPLETED: BDA_EVENT_ID = 17
BDA_EVENT_SMART_CARD_INSERTED: BDA_EVENT_ID = 18
BDA_EVENT_SMART_CARD_REMOVED: BDA_EVENT_ID = 19
BDA_Frequency = Int32
BDA_FREQUENCY_NOT_SET: BDA_Frequency = -1
BDA_FREQUENCY_NOT_DEFINED: BDA_Frequency = 0
BDA_Frequency_Multiplier = Int32
BDA_FREQUENCY_MULTIPLIER_NOT_SET: BDA_Frequency_Multiplier = -1
BDA_FREQUENCY_MULTIPLIER_NOT_DEFINED: BDA_Frequency_Multiplier = 0
class BDA_GDDS_DATA(Structure):
    lResult: Int32
    ulDataLength: UInt32
    ulPercentageProgress: UInt32
    argbData: Byte * 1
class BDA_GDDS_DATATYPE(Structure):
    lResult: Int32
    uuidDataType: Guid
class BDA_IPv4_ADDRESS(Structure):
    rgbAddress: Byte * 4
class BDA_IPv4_ADDRESS_LIST(Structure):
    ulcAddresses: UInt32
    rgAddressl: win32more.Media.DirectShow.BDA_IPv4_ADDRESS * 1
class BDA_IPv6_ADDRESS(Structure):
    rgbAddress: Byte * 6
class BDA_IPv6_ADDRESS_LIST(Structure):
    ulcAddresses: UInt32
    rgAddressl: win32more.Media.DirectShow.BDA_IPv6_ADDRESS * 1
class BDA_ISDBCAS_EMG_REQ(Structure):
    bCLA: Byte
    bINS: Byte
    bP1: Byte
    bP2: Byte
    bLC: Byte
    bCardId: Byte * 6
    bProtocol: Byte
    bCABroadcasterGroupId: Byte
    bMessageControl: Byte
    bMessageCode: Byte * 1
class BDA_ISDBCAS_REQUESTHEADER(Structure):
    bInstruction: Byte
    bReserved: Byte * 3
    ulDataLength: UInt32
    argbIsdbCommand: Byte * 1
    _pack_ = 1
class BDA_ISDBCAS_RESPONSEDATA(Structure):
    lResult: Int32
    ulRequestID: UInt32
    ulIsdbStatus: UInt32
    ulIsdbDataSize: UInt32
    argbIsdbCommandData: Byte * 1
    _pack_ = 1
BDA_LockType = Int32
Bda_LockType_None: BDA_LockType = 0
Bda_LockType_PLL: BDA_LockType = 1
Bda_LockType_DecoderDemod: BDA_LockType = 2
Bda_LockType_Complete: BDA_LockType = 128
BDA_MULTICAST_MODE = Int32
BDA_PROMISCUOUS_MULTICAST: BDA_MULTICAST_MODE = 0
BDA_FILTERED_MULTICAST: BDA_MULTICAST_MODE = 1
BDA_NO_MULTICAST: BDA_MULTICAST_MODE = 2
class BDA_MUX_PIDLISTITEM(Structure):
    usPIDNumber: UInt16
    usProgramNumber: UInt16
    ePIDType: win32more.Media.DirectShow.MUX_PID_TYPE
    _pack_ = 2
class BDA_PID_MAP(Structure):
    MediaSampleContent: win32more.Media.DirectShow.MEDIA_SAMPLE_CONTENT
    ulcPIDs: UInt32
    aulPIDs: UInt32 * 1
class BDA_PID_UNMAP(Structure):
    ulcPIDs: UInt32
    aulPIDs: UInt32 * 1
class BDA_PROGRAM_PID_LIST(Structure):
    ulProgramNumber: UInt32
    ulcPIDs: UInt32
    ulPID: UInt32 * 1
class BDA_RATING_PINRESET(Structure):
    bPinLength: Byte
    argbNewPin: Byte * 1
BDA_Range = Int32
BDA_RANGE_NOT_SET: BDA_Range = -1
BDA_RANGE_NOT_DEFINED: BDA_Range = 0
class BDA_SCAN_CAPABILTIES(Structure):
    lResult: Int32
    ul64AnalogStandardsSupported: UInt64
class BDA_SCAN_START(Structure):
    lResult: Int32
    LowerFrequency: UInt32
    HigerFrequency: UInt32
class BDA_SCAN_STATE(Structure):
    lResult: Int32
    ulSignalLock: UInt32
    ulSecondsLeft: UInt32
    ulCurrentFrequency: UInt32
BDA_SIGNAL_STATE = Int32
BDA_SIGNAL_UNAVAILABLE: BDA_SIGNAL_STATE = 0
BDA_SIGNAL_INACTIVE: BDA_SIGNAL_STATE = 1
BDA_SIGNAL_ACTIVE: BDA_SIGNAL_STATE = 2
class BDA_SIGNAL_TIMEOUTS(Structure):
    ulCarrierTimeoutMs: UInt32
    ulScanningTimeoutMs: UInt32
    ulTuningTimeoutMs: UInt32
class BDA_STRING(Structure):
    lResult: Int32
    ulStringSize: UInt32
    argbString: Byte * 1
BDA_SignalType = Int32
Bda_SignalType_Unknown: BDA_SignalType = 0
Bda_SignalType_Analog: BDA_SignalType = 1
Bda_SignalType_Digital: BDA_SignalType = 2
class BDA_TABLE_SECTION(Structure):
    ulPrimarySectionId: UInt32
    ulSecondarySectionId: UInt32
    ulcbSectionLength: UInt32
    argbSectionData: UInt32 * 1
class BDA_TEMPLATE_CONNECTION(Structure):
    FromNodeType: UInt32
    FromNodePinType: UInt32
    ToNodeType: UInt32
    ToNodePinType: UInt32
class BDA_TEMPLATE_PIN_JOINT(Structure):
    uliTemplateConnection: UInt32
    ulcInstancesMax: UInt32
class BDA_TRANSPORT_INFO(Structure):
    ulcbPhyiscalPacket: UInt32
    ulcbPhyiscalFrame: UInt32
    ulcbPhyiscalFrameAlignment: UInt32
    AvgTimePerFrame: Int64
class BDA_TS_SELECTORINFO(Structure):
    bTSInfolength: Byte
    bReserved: Byte * 2
    guidNetworkType: Guid
    bTSIDCount: Byte
    usTSID: UInt16 * 1
    _pack_ = 1
class BDA_TS_SELECTORINFO_ISDBS_EXT(Structure):
    bTMCC: Byte * 48
class BDA_TUNER_DIAGNOSTICS(Structure):
    lResult: Int32
    ulSignalLevel: UInt32
    ulSignalLevelQuality: UInt32
    ulSignalNoiseRatio: UInt32
class BDA_TUNER_TUNERSTATE(Structure):
    lResult: Int32
    ulTuneLength: UInt32
    argbTuneData: Byte * 1
class BDA_USERACTIVITY_INTERVAL(Structure):
    lResult: Int32
    ulActivityInterval: UInt32
class BDA_WMDRMTUNER_PIDPROTECTION(Structure):
    lResult: Int32
    uuidKeyID: Guid
class BDA_WMDRMTUNER_PURCHASEENTITLEMENT(Structure):
    lResult: Int32
    ulDescrambleStatus: UInt32
    ulCaptureTokenLength: UInt32
    argbCaptureTokenBuffer: Byte * 1
class BDA_WMDRM_KEYINFOLIST(Structure):
    lResult: Int32
    ulKeyuuidBufferLen: UInt32
    argKeyuuidBuffer: Guid * 1
class BDA_WMDRM_RENEWLICENSE(Structure):
    lResult: Int32
    ulDescrambleStatus: UInt32
    ulXmrLicenseOutputLength: UInt32
    argbXmrLicenceOutputBuffer: Byte * 1
class BDA_WMDRM_STATUS(Structure):
    lResult: Int32
    ulMaxCaptureTokenSize: UInt32
    uMaxStreamingPid: UInt32
    ulMaxLicense: UInt32
    ulMinSecurityLevel: UInt32
    ulRevInfoSequenceNumber: UInt32
    ulRevInfoIssuedTime: UInt64
    ulRevListVersion: UInt32
    ulRevInfoTTL: UInt32
    ulState: UInt32
BSKYB_TERRESTRIAL_TV_NETWORK_TYPE = Guid('9e9e46c6-3aba-4f08-ad-0e-cc-5a-c8-14-8c-2b')
class BadSampleInfo(Structure):
    hrReason: win32more.Foundation.HRESULT
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
BinaryConvolutionCodeRate = Int32
BDA_BCC_RATE_NOT_SET: BinaryConvolutionCodeRate = -1
BDA_BCC_RATE_NOT_DEFINED: BinaryConvolutionCodeRate = 0
BDA_BCC_RATE_1_2: BinaryConvolutionCodeRate = 1
BDA_BCC_RATE_2_3: BinaryConvolutionCodeRate = 2
BDA_BCC_RATE_3_4: BinaryConvolutionCodeRate = 3
BDA_BCC_RATE_3_5: BinaryConvolutionCodeRate = 4
BDA_BCC_RATE_4_5: BinaryConvolutionCodeRate = 5
BDA_BCC_RATE_5_6: BinaryConvolutionCodeRate = 6
BDA_BCC_RATE_5_11: BinaryConvolutionCodeRate = 7
BDA_BCC_RATE_7_8: BinaryConvolutionCodeRate = 8
BDA_BCC_RATE_1_4: BinaryConvolutionCodeRate = 9
BDA_BCC_RATE_1_3: BinaryConvolutionCodeRate = 10
BDA_BCC_RATE_2_5: BinaryConvolutionCodeRate = 11
BDA_BCC_RATE_6_7: BinaryConvolutionCodeRate = 12
BDA_BCC_RATE_8_9: BinaryConvolutionCodeRate = 13
BDA_BCC_RATE_9_10: BinaryConvolutionCodeRate = 14
BDA_BCC_RATE_MAX: BinaryConvolutionCodeRate = 15
BroadcastEventService = Guid('0b3ffb92-0919-4934-9d-5b-61-9c-71-9d-02-02')
class CAPTURE_STREAMTIME(Structure):
    StreamTime: Int64
class COLORKEY(Structure):
    KeyType: UInt32
    PaletteIndex: UInt32
    LowColorValue: win32more.Foundation.COLORREF
    HighColorValue: win32more.Foundation.COLORREF
COLORKEY_TYPE = Int32
CK_NOCOLORKEY: COLORKEY_TYPE = 0
CK_INDEX: COLORKEY_TYPE = 1
CK_RGB: COLORKEY_TYPE = 2
COMPLETION_STATUS_FLAGS = Int32
COMPSTAT_NOUPDATEOK: COMPLETION_STATUS_FLAGS = 1
COMPSTAT_WAIT: COMPLETION_STATUS_FLAGS = 2
COMPSTAT_ABORT: COMPLETION_STATUS_FLAGS = 4
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
COPP_ACP_Protection_Level = Int32
COPP_ACP_Level0: COPP_ACP_Protection_Level = 0
COPP_ACP_LevelMin: COPP_ACP_Protection_Level = 0
COPP_ACP_Level1: COPP_ACP_Protection_Level = 1
COPP_ACP_Level2: COPP_ACP_Protection_Level = 2
COPP_ACP_Level3: COPP_ACP_Protection_Level = 3
COPP_ACP_LevelMax: COPP_ACP_Protection_Level = 3
COPP_ACP_ForceDWORD: COPP_ACP_Protection_Level = 2147483647
COPP_BusType = Int32
COPP_BusType_Unknown: COPP_BusType = 0
COPP_BusType_PCI: COPP_BusType = 1
COPP_BusType_PCIX: COPP_BusType = 2
COPP_BusType_PCIExpress: COPP_BusType = 3
COPP_BusType_AGP: COPP_BusType = 4
COPP_BusType_Integrated: COPP_BusType = -2147483648
COPP_BusType_ForceDWORD: COPP_BusType = 2147483647
COPP_CGMSA_Protection_Level = Int32
COPP_CGMSA_Disabled: COPP_CGMSA_Protection_Level = 0
COPP_CGMSA_LevelMin: COPP_CGMSA_Protection_Level = 0
COPP_CGMSA_CopyFreely: COPP_CGMSA_Protection_Level = 1
COPP_CGMSA_CopyNoMore: COPP_CGMSA_Protection_Level = 2
COPP_CGMSA_CopyOneGeneration: COPP_CGMSA_Protection_Level = 3
COPP_CGMSA_CopyNever: COPP_CGMSA_Protection_Level = 4
COPP_CGMSA_RedistributionControlRequired: COPP_CGMSA_Protection_Level = 8
COPP_CGMSA_LevelMax: COPP_CGMSA_Protection_Level = 12
COPP_CGMSA_ForceDWORD: COPP_CGMSA_Protection_Level = 2147483647
COPP_ConnectorType = Int32
COPP_ConnectorType_Unknown: COPP_ConnectorType = -1
COPP_ConnectorType_VGA: COPP_ConnectorType = 0
COPP_ConnectorType_SVideo: COPP_ConnectorType = 1
COPP_ConnectorType_CompositeVideo: COPP_ConnectorType = 2
COPP_ConnectorType_ComponentVideo: COPP_ConnectorType = 3
COPP_ConnectorType_DVI: COPP_ConnectorType = 4
COPP_ConnectorType_HDMI: COPP_ConnectorType = 5
COPP_ConnectorType_LVDS: COPP_ConnectorType = 6
COPP_ConnectorType_TMDS: COPP_ConnectorType = 7
COPP_ConnectorType_D_JPN: COPP_ConnectorType = 8
COPP_ConnectorType_Internal: COPP_ConnectorType = -2147483648
COPP_ConnectorType_ForceDWORD: COPP_ConnectorType = 2147483647
COPP_HDCP_Protection_Level = Int32
COPP_HDCP_Level0: COPP_HDCP_Protection_Level = 0
COPP_HDCP_LevelMin: COPP_HDCP_Protection_Level = 0
COPP_HDCP_Level1: COPP_HDCP_Protection_Level = 1
COPP_HDCP_LevelMax: COPP_HDCP_Protection_Level = 1
COPP_HDCP_ForceDWORD: COPP_HDCP_Protection_Level = 2147483647
COPP_ImageAspectRatio_EN300294 = Int32
COPP_AspectRatio_EN300294_FullFormat4by3: COPP_ImageAspectRatio_EN300294 = 0
COPP_AspectRatio_EN300294_Box14by9Center: COPP_ImageAspectRatio_EN300294 = 1
COPP_AspectRatio_EN300294_Box14by9Top: COPP_ImageAspectRatio_EN300294 = 2
COPP_AspectRatio_EN300294_Box16by9Center: COPP_ImageAspectRatio_EN300294 = 3
COPP_AspectRatio_EN300294_Box16by9Top: COPP_ImageAspectRatio_EN300294 = 4
COPP_AspectRatio_EN300294_BoxGT16by9Center: COPP_ImageAspectRatio_EN300294 = 5
COPP_AspectRatio_EN300294_FullFormat4by3ProtectedCenter: COPP_ImageAspectRatio_EN300294 = 6
COPP_AspectRatio_EN300294_FullFormat16by9Anamorphic: COPP_ImageAspectRatio_EN300294 = 7
COPP_AspectRatio_ForceDWORD: COPP_ImageAspectRatio_EN300294 = 2147483647
COPP_StatusFlags = Int32
COPP_StatusNormal: COPP_StatusFlags = 0
COPP_LinkLost: COPP_StatusFlags = 1
COPP_RenegotiationRequired: COPP_StatusFlags = 2
COPP_StatusFlagsReserved: COPP_StatusFlags = -4
COPP_StatusHDCPFlags = Int32
COPP_HDCPRepeater: COPP_StatusHDCPFlags = 1
COPP_HDCPFlagsReserved: COPP_StatusHDCPFlags = -2
COPP_TVProtectionStandard = Int32
COPP_ProtectionStandard_Unknown: COPP_TVProtectionStandard = -2147483648
COPP_ProtectionStandard_None: COPP_TVProtectionStandard = 0
COPP_ProtectionStandard_IEC61880_525i: COPP_TVProtectionStandard = 1
COPP_ProtectionStandard_IEC61880_2_525i: COPP_TVProtectionStandard = 2
COPP_ProtectionStandard_IEC62375_625p: COPP_TVProtectionStandard = 4
COPP_ProtectionStandard_EIA608B_525: COPP_TVProtectionStandard = 8
COPP_ProtectionStandard_EN300294_625i: COPP_TVProtectionStandard = 16
COPP_ProtectionStandard_CEA805A_TypeA_525p: COPP_TVProtectionStandard = 32
COPP_ProtectionStandard_CEA805A_TypeA_750p: COPP_TVProtectionStandard = 64
COPP_ProtectionStandard_CEA805A_TypeA_1125i: COPP_TVProtectionStandard = 128
COPP_ProtectionStandard_CEA805A_TypeB_525p: COPP_TVProtectionStandard = 256
COPP_ProtectionStandard_CEA805A_TypeB_750p: COPP_TVProtectionStandard = 512
COPP_ProtectionStandard_CEA805A_TypeB_1125i: COPP_TVProtectionStandard = 1024
COPP_ProtectionStandard_ARIBTRB15_525i: COPP_TVProtectionStandard = 2048
COPP_ProtectionStandard_ARIBTRB15_525p: COPP_TVProtectionStandard = 4096
COPP_ProtectionStandard_ARIBTRB15_750p: COPP_TVProtectionStandard = 8192
COPP_ProtectionStandard_ARIBTRB15_1125i: COPP_TVProtectionStandard = 16384
COPP_ProtectionStandard_Mask: COPP_TVProtectionStandard = -2147450881
COPP_ProtectionStandard_Reserved: COPP_TVProtectionStandard = 2147450880
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
CXDSData = Guid('c4c4c4f4-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
CameraControlFlags = Int32
CameraControl_Flags_Auto: CameraControlFlags = 1
CameraControl_Flags_Manual: CameraControlFlags = 2
CameraControlProperty = Int32
CameraControl_Pan: CameraControlProperty = 0
CameraControl_Tilt: CameraControlProperty = 1
CameraControl_Roll: CameraControlProperty = 2
CameraControl_Zoom: CameraControlProperty = 3
CameraControl_Exposure: CameraControlProperty = 4
CameraControl_Iris: CameraControlProperty = 5
CameraControl_Focus: CameraControlProperty = 6
class ChannelChangeInfo(Structure):
    state: win32more.Media.DirectShow.ChannelChangeSpanningEvent_State
    TimeStamp: UInt64
ChannelChangeSpanningEvent_State = Int32
ChannelChangeSpanningEvent_Start: ChannelChangeSpanningEvent_State = 0
ChannelChangeSpanningEvent_End: ChannelChangeSpanningEvent_State = 2
ChannelIDTuneRequest = Guid('3a9428a7-31a4-45e9-9e-fb-e0-55-bf-7b-b3-db')
ChannelIDTuningSpace = Guid('cc829a2f-3365-463f-af-13-81-db-b6-f3-a5-55')
class ChannelInfo(Structure):
    lFrequency: Int32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        DVB: _DVB_e__Struct
        DC: _DC_e__Struct
        ATSC: _ATSC_e__Struct
        class _DVB_e__Struct(Structure):
            lONID: Int32
            lTSID: Int32
            lSID: Int32
        class _DC_e__Struct(Structure):
            lProgNumber: Int32
        class _ATSC_e__Struct(Structure):
            lProgNumber: Int32
ChannelTuneRequest = Guid('0369b4e5-45b6-11d3-b6-50-00-c0-4f-79-49-8e')
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
class ChannelTypeInfo(Structure):
    channelType: win32more.Media.DirectShow.ChannelType
    timeStamp: UInt64
Component = Guid('59dc47a8-116c-11d3-9d-8e-00-c0-4f-72-d9-80')
ComponentCategory = Int32
ComponentCategory_CategoryNotSet: ComponentCategory = -1
ComponentCategory_CategoryOther: ComponentCategory = 0
ComponentCategory_CategoryVideo: ComponentCategory = 1
ComponentCategory_CategoryAudio: ComponentCategory = 2
ComponentCategory_CategoryText: ComponentCategory = 3
ComponentCategory_CategorySubtitles: ComponentCategory = 4
ComponentCategory_CategoryCaptions: ComponentCategory = 5
ComponentCategory_CategorySuperimpose: ComponentCategory = 6
ComponentCategory_CategoryData: ComponentCategory = 7
ComponentCategory_CATEGORY_COUNT: ComponentCategory = 8
ComponentStatus = Int32
ComponentStatus_StatusActive: ComponentStatus = 0
ComponentStatus_StatusInactive: ComponentStatus = 1
ComponentStatus_StatusUnavailable: ComponentStatus = 2
ComponentType = Guid('823535a0-0318-11d3-9d-8e-00-c0-4f-72-d9-80')
ComponentTypes = Guid('a1a2b1c4-0e3a-11d3-9d-8e-00-c0-4f-72-d9-80')
Components = Guid('809b6661-94c4-49e6-b6-ec-3f-0f-86-22-15-aa')
CompressionCaps = Int32
CompressionCaps_CanQuality: CompressionCaps = 1
CompressionCaps_CanCrunch: CompressionCaps = 2
CompressionCaps_CanKeyFrame: CompressionCaps = 4
CompressionCaps_CanBFrame: CompressionCaps = 8
CompressionCaps_CanWindow: CompressionCaps = 16
CreatePropBagOnRegKey = Guid('8a674b49-1f63-11d3-b6-4c-00-c0-4f-79-49-8e')
DDSFF_FLAGS = UInt32
DDSFF_PROGRESSIVERENDER: DDSFF_FLAGS = 1
DECIMATION_USAGE = Int32
DECIMATION_LEGACY: DECIMATION_USAGE = 0
DECIMATION_USE_DECODER_ONLY: DECIMATION_USAGE = 1
DECIMATION_USE_VIDEOPORT_ONLY: DECIMATION_USAGE = 2
DECIMATION_USE_OVERLAY_ONLY: DECIMATION_USAGE = 3
DECIMATION_DEFAULT: DECIMATION_USAGE = 4
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
DIGITAL_CABLE_NETWORK_TYPE = Guid('143827ab-f77b-498d-81-ca-5a-00-7a-ec-28-bf')
DIRECT_TV_SATELLITE_TV_NETWORK_TYPE = Guid('93b66fb5-93d4-4323-92-1c-c1-f5-2d-f6-1d-3f')
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
class DSHOW_STREAM_DESC(Structure):
    VersionNo: UInt32
    StreamId: UInt32
    Default: win32more.Foundation.BOOL
    Creation: win32more.Foundation.BOOL
    Reserved: UInt32
class DSMCC_ELEMENT(Structure):
    pid: UInt16
    bComponentTag: Byte
    dwCarouselId: UInt32
    dwTransactionId: UInt32
    pNext: POINTER(win32more.Media.DirectShow.DSMCC_ELEMENT_head)
    _pack_ = 1
class DSMCC_FILTER_OPTIONS(Structure):
    fSpecifyProtocol: win32more.Foundation.BOOL
    Protocol: Byte
    fSpecifyType: win32more.Foundation.BOOL
    Type: Byte
    fSpecifyMessageId: win32more.Foundation.BOOL
    MessageId: UInt16
    fSpecifyTransactionId: win32more.Foundation.BOOL
    fUseTrxIdMessageIdMask: win32more.Foundation.BOOL
    TransactionId: UInt32
    fSpecifyModuleVersion: win32more.Foundation.BOOL
    ModuleVersion: Byte
    fSpecifyBlockNumber: win32more.Foundation.BOOL
    BlockNumber: UInt16
    fGetModuleCall: win32more.Foundation.BOOL
    NumberOfBlocksInModule: UInt16
    _pack_ = 1
class DSMCC_SECTION(Structure):
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
    class _Header_e__Union(Union):
        S: win32more.Media.DirectShow.MPEG_HEADER_BITS_MIDL
        W: UInt16
        _pack_ = 1
    class _Version_e__Union(Union):
        S: win32more.Media.DirectShow.MPEG_HEADER_VERSION_BITS_MIDL
        B: Byte
DTFilter = Guid('c4c4c4f2-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
DVBCLocator = Guid('c531d9fd-9685-4028-8b-68-6e-12-32-07-9f-1e')
DVBSLocator = Guid('1df7d126-4050-47f0-a7-cf-4c-4c-a9-24-13-33')
DVBSTuningSpace = Guid('b64016f3-c9a2-4066-96-f0-bd-95-63-31-47-26')
class DVBScramblingControlSpanningEvent(Structure):
    ulPID: UInt32
    fScrambled: win32more.Foundation.BOOL
DVBSystemType = Int32
DVB_Cable: DVBSystemType = 0
DVB_Terrestrial: DVBSystemType = 1
DVB_Satellite: DVBSystemType = 2
ISDB_Terrestrial: DVBSystemType = 3
ISDB_Satellite: DVBSystemType = 4
DVBTLocator = Guid('9cd64701-bdf3-4d14-8e-03-f1-29-83-d8-66-64')
DVBTLocator2 = Guid('efe3fa02-45d7-4920-be-96-53-fa-7f-35-b0-e6')
DVBTuneRequest = Guid('15d6504a-5494-499c-88-6c-97-3c-9e-53-b9-f1')
DVBTuningSpace = Guid('c6b14b32-76aa-4a86-a7-ac-5c-79-aa-f5-8d-a7')
DVB_CABLE_TV_NETWORK_TYPE = Guid('dc0c0fe7-0485-4266-b9-3f-68-fb-f8-0e-d8-34')
class DVB_EIT_FILTER_OPTIONS(Structure):
    fSpecifySegment: win32more.Foundation.BOOL
    bSegment: Byte
    _pack_ = 1
DVB_SATELLITE_TV_NETWORK_TYPE = Guid('fa4b375a-45b4-4d45-84-40-26-39-57-b1-16-23')
DVB_STRCONV_MODE = Int32
STRCONV_MODE_DVB: DVB_STRCONV_MODE = 0
STRCONV_MODE_DVB_EMPHASIS: DVB_STRCONV_MODE = 1
STRCONV_MODE_DVB_WITHOUT_EMPHASIS: DVB_STRCONV_MODE = 2
STRCONV_MODE_ISDB: DVB_STRCONV_MODE = 3
DVB_TERRESTRIAL_TV_NETWORK_TYPE = Guid('216c62df-6d7f-4e9a-85-71-05-f1-4e-db-76-6a')
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
class DVD_ATR(Structure):
    ulCAT: UInt32
    pbATRI: Byte * 768
DVD_AUDIO_APPMODE = Int32
DVD_AudioMode_None: DVD_AUDIO_APPMODE = 0
DVD_AudioMode_Karaoke: DVD_AUDIO_APPMODE = 1
DVD_AudioMode_Surround: DVD_AUDIO_APPMODE = 2
DVD_AudioMode_Other: DVD_AUDIO_APPMODE = 3
DVD_AUDIO_FORMAT = Int32
DVD_AudioFormat_AC3: DVD_AUDIO_FORMAT = 0
DVD_AudioFormat_MPEG1: DVD_AUDIO_FORMAT = 1
DVD_AudioFormat_MPEG1_DRC: DVD_AUDIO_FORMAT = 2
DVD_AudioFormat_MPEG2: DVD_AUDIO_FORMAT = 3
DVD_AudioFormat_MPEG2_DRC: DVD_AUDIO_FORMAT = 4
DVD_AudioFormat_LPCM: DVD_AUDIO_FORMAT = 5
DVD_AudioFormat_DTS: DVD_AUDIO_FORMAT = 6
DVD_AudioFormat_SDDS: DVD_AUDIO_FORMAT = 7
DVD_AudioFormat_Other: DVD_AUDIO_FORMAT = 8
DVD_AUDIO_LANG_EXT = Int32
DVD_AUD_EXT_NotSpecified: DVD_AUDIO_LANG_EXT = 0
DVD_AUD_EXT_Captions: DVD_AUDIO_LANG_EXT = 1
DVD_AUD_EXT_VisuallyImpaired: DVD_AUDIO_LANG_EXT = 2
DVD_AUD_EXT_DirectorComments1: DVD_AUDIO_LANG_EXT = 3
DVD_AUD_EXT_DirectorComments2: DVD_AUDIO_LANG_EXT = 4
class DVD_AudioAttributes(Structure):
    AppMode: win32more.Media.DirectShow.DVD_AUDIO_APPMODE
    AppModeData: Byte
    AudioFormat: win32more.Media.DirectShow.DVD_AUDIO_FORMAT
    Language: UInt32
    LanguageExtension: win32more.Media.DirectShow.DVD_AUDIO_LANG_EXT
    fHasMultichannelInfo: win32more.Foundation.BOOL
    dwFrequency: UInt32
    bQuantization: Byte
    bNumberOfChannels: Byte
    dwReserved: UInt32 * 2
DVD_CMD_FLAGS = Int32
DVD_CMD_FLAG_None: DVD_CMD_FLAGS = 0
DVD_CMD_FLAG_Flush: DVD_CMD_FLAGS = 1
DVD_CMD_FLAG_SendEvents: DVD_CMD_FLAGS = 2
DVD_CMD_FLAG_Block: DVD_CMD_FLAGS = 4
DVD_CMD_FLAG_StartWhenRendered: DVD_CMD_FLAGS = 8
DVD_CMD_FLAG_EndAfterRendered: DVD_CMD_FLAGS = 16
class DVD_DECODER_CAPS(Structure):
    dwSize: UInt32
    dwAudioCaps: UInt32
    dFwdMaxRateVideo: Double
    dFwdMaxRateAudio: Double
    dFwdMaxRateSP: Double
    dBwdMaxRateVideo: Double
    dBwdMaxRateAudio: Double
    dBwdMaxRateSP: Double
    dwRes1: UInt32
    dwRes2: UInt32
    dwRes3: UInt32
    dwRes4: UInt32
DVD_DISC_SIDE = Int32
DVD_SIDE_A: DVD_DISC_SIDE = 1
DVD_SIDE_B: DVD_DISC_SIDE = 2
DVD_DOMAIN = Int32
DVD_DOMAIN_FirstPlay: DVD_DOMAIN = 1
DVD_DOMAIN_VideoManagerMenu: DVD_DOMAIN = 2
DVD_DOMAIN_VideoTitleSetMenu: DVD_DOMAIN = 3
DVD_DOMAIN_Title: DVD_DOMAIN = 4
DVD_DOMAIN_Stop: DVD_DOMAIN = 5
DVD_ERROR = Int32
DVD_ERROR_Unexpected: DVD_ERROR = 1
DVD_ERROR_CopyProtectFail: DVD_ERROR = 2
DVD_ERROR_InvalidDVD1_0Disc: DVD_ERROR = 3
DVD_ERROR_InvalidDiscRegion: DVD_ERROR = 4
DVD_ERROR_LowParentalLevel: DVD_ERROR = 5
DVD_ERROR_MacrovisionFail: DVD_ERROR = 6
DVD_ERROR_IncompatibleSystemAndDecoderRegions: DVD_ERROR = 7
DVD_ERROR_IncompatibleDiscAndDecoderRegions: DVD_ERROR = 8
DVD_ERROR_CopyProtectOutputFail: DVD_ERROR = 9
DVD_ERROR_CopyProtectOutputNotSupported: DVD_ERROR = 10
DVD_FRAMERATE = Int32
DVD_FPS_25: DVD_FRAMERATE = 1
DVD_FPS_30NonDrop: DVD_FRAMERATE = 3
class DVD_HMSF_TIMECODE(Structure):
    bHours: Byte
    bMinutes: Byte
    bSeconds: Byte
    bFrames: Byte
DVD_KARAOKE_ASSIGNMENT = Int32
DVD_Assignment_reserved0: DVD_KARAOKE_ASSIGNMENT = 0
DVD_Assignment_reserved1: DVD_KARAOKE_ASSIGNMENT = 1
DVD_Assignment_LR: DVD_KARAOKE_ASSIGNMENT = 2
DVD_Assignment_LRM: DVD_KARAOKE_ASSIGNMENT = 3
DVD_Assignment_LR1: DVD_KARAOKE_ASSIGNMENT = 4
DVD_Assignment_LRM1: DVD_KARAOKE_ASSIGNMENT = 5
DVD_Assignment_LR12: DVD_KARAOKE_ASSIGNMENT = 6
DVD_Assignment_LRM12: DVD_KARAOKE_ASSIGNMENT = 7
DVD_KARAOKE_CONTENTS = Int32
DVD_Karaoke_GuideVocal1: DVD_KARAOKE_CONTENTS = 1
DVD_Karaoke_GuideVocal2: DVD_KARAOKE_CONTENTS = 2
DVD_Karaoke_GuideMelody1: DVD_KARAOKE_CONTENTS = 4
DVD_Karaoke_GuideMelody2: DVD_KARAOKE_CONTENTS = 8
DVD_Karaoke_GuideMelodyA: DVD_KARAOKE_CONTENTS = 16
DVD_Karaoke_GuideMelodyB: DVD_KARAOKE_CONTENTS = 32
DVD_Karaoke_SoundEffectA: DVD_KARAOKE_CONTENTS = 64
DVD_Karaoke_SoundEffectB: DVD_KARAOKE_CONTENTS = 128
DVD_KARAOKE_DOWNMIX = Int32
DVD_Mix_0to0: DVD_KARAOKE_DOWNMIX = 1
DVD_Mix_1to0: DVD_KARAOKE_DOWNMIX = 2
DVD_Mix_2to0: DVD_KARAOKE_DOWNMIX = 4
DVD_Mix_3to0: DVD_KARAOKE_DOWNMIX = 8
DVD_Mix_4to0: DVD_KARAOKE_DOWNMIX = 16
DVD_Mix_Lto0: DVD_KARAOKE_DOWNMIX = 32
DVD_Mix_Rto0: DVD_KARAOKE_DOWNMIX = 64
DVD_Mix_0to1: DVD_KARAOKE_DOWNMIX = 256
DVD_Mix_1to1: DVD_KARAOKE_DOWNMIX = 512
DVD_Mix_2to1: DVD_KARAOKE_DOWNMIX = 1024
DVD_Mix_3to1: DVD_KARAOKE_DOWNMIX = 2048
DVD_Mix_4to1: DVD_KARAOKE_DOWNMIX = 4096
DVD_Mix_Lto1: DVD_KARAOKE_DOWNMIX = 8192
DVD_Mix_Rto1: DVD_KARAOKE_DOWNMIX = 16384
class DVD_KaraokeAttributes(Structure):
    bVersion: Byte
    fMasterOfCeremoniesInGuideVocal1: win32more.Foundation.BOOL
    fDuet: win32more.Foundation.BOOL
    ChannelAssignment: win32more.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT
    wChannelContents: UInt16 * 8
DVD_MENU_ID = Int32
DVD_MENU_Title: DVD_MENU_ID = 2
DVD_MENU_Root: DVD_MENU_ID = 3
DVD_MENU_Subpicture: DVD_MENU_ID = 4
DVD_MENU_Audio: DVD_MENU_ID = 5
DVD_MENU_Angle: DVD_MENU_ID = 6
DVD_MENU_Chapter: DVD_MENU_ID = 7
class DVD_MUA_Coeff(Structure):
    log2_alpha: Double
    log2_beta: Double
class DVD_MUA_MixingInfo(Structure):
    fMixTo0: win32more.Foundation.BOOL
    fMixTo1: win32more.Foundation.BOOL
    fMix0InPhase: win32more.Foundation.BOOL
    fMix1InPhase: win32more.Foundation.BOOL
    dwSpeakerPosition: UInt32
class DVD_MenuAttributes(Structure):
    fCompatibleRegion: win32more.Foundation.BOOL * 8
    VideoAttributes: win32more.Media.DirectShow.DVD_VideoAttributes
    fAudioPresent: win32more.Foundation.BOOL
    AudioAttributes: win32more.Media.DirectShow.DVD_AudioAttributes
    fSubpicturePresent: win32more.Foundation.BOOL
    SubpictureAttributes: win32more.Media.DirectShow.DVD_SubpictureAttributes
class DVD_MultichannelAudioAttributes(Structure):
    Info: win32more.Media.DirectShow.DVD_MUA_MixingInfo * 8
    Coeff: win32more.Media.DirectShow.DVD_MUA_Coeff * 8
DVD_NavCmdType = Int32
DVD_NavCmdType_Pre: DVD_NavCmdType = 1
DVD_NavCmdType_Post: DVD_NavCmdType = 2
DVD_NavCmdType_Cell: DVD_NavCmdType = 3
DVD_NavCmdType_Button: DVD_NavCmdType = 4
DVD_OPTION_FLAG = Int32
DVD_ResetOnStop: DVD_OPTION_FLAG = 1
DVD_NotifyParentalLevelChange: DVD_OPTION_FLAG = 2
DVD_HMSF_TimeCodeEvents: DVD_OPTION_FLAG = 3
DVD_AudioDuringFFwdRew: DVD_OPTION_FLAG = 4
DVD_EnableNonblockingAPIs: DVD_OPTION_FLAG = 5
DVD_CacheSizeInMB: DVD_OPTION_FLAG = 6
DVD_EnablePortableBookmarks: DVD_OPTION_FLAG = 7
DVD_EnableExtendedCopyProtectErrors: DVD_OPTION_FLAG = 8
DVD_NotifyPositionChange: DVD_OPTION_FLAG = 9
DVD_IncreaseOutputControl: DVD_OPTION_FLAG = 10
DVD_EnableStreaming: DVD_OPTION_FLAG = 11
DVD_EnableESOutput: DVD_OPTION_FLAG = 12
DVD_EnableTitleLength: DVD_OPTION_FLAG = 13
DVD_DisableStillThrottle: DVD_OPTION_FLAG = 14
DVD_EnableLoggingEvents: DVD_OPTION_FLAG = 15
DVD_MaxReadBurstInKB: DVD_OPTION_FLAG = 16
DVD_ReadBurstPeriodInMS: DVD_OPTION_FLAG = 17
DVD_RestartDisc: DVD_OPTION_FLAG = 18
DVD_EnableCC: DVD_OPTION_FLAG = 19
DVD_PARENTAL_LEVEL = Int32
DVD_PARENTAL_LEVEL_8: DVD_PARENTAL_LEVEL = 32768
DVD_PARENTAL_LEVEL_7: DVD_PARENTAL_LEVEL = 16384
DVD_PARENTAL_LEVEL_6: DVD_PARENTAL_LEVEL = 8192
DVD_PARENTAL_LEVEL_5: DVD_PARENTAL_LEVEL = 4096
DVD_PARENTAL_LEVEL_4: DVD_PARENTAL_LEVEL = 2048
DVD_PARENTAL_LEVEL_3: DVD_PARENTAL_LEVEL = 1024
DVD_PARENTAL_LEVEL_2: DVD_PARENTAL_LEVEL = 512
DVD_PARENTAL_LEVEL_1: DVD_PARENTAL_LEVEL = 256
DVD_PB_STOPPED = Int32
DVD_PB_STOPPED_Other: DVD_PB_STOPPED = 0
DVD_PB_STOPPED_NoBranch: DVD_PB_STOPPED = 1
DVD_PB_STOPPED_NoFirstPlayDomain: DVD_PB_STOPPED = 2
DVD_PB_STOPPED_StopCommand: DVD_PB_STOPPED = 3
DVD_PB_STOPPED_Reset: DVD_PB_STOPPED = 4
DVD_PB_STOPPED_DiscEjected: DVD_PB_STOPPED = 5
DVD_PB_STOPPED_IllegalNavCommand: DVD_PB_STOPPED = 6
DVD_PB_STOPPED_PlayPeriodAutoStop: DVD_PB_STOPPED = 7
DVD_PB_STOPPED_PlayChapterAutoStop: DVD_PB_STOPPED = 8
DVD_PB_STOPPED_ParentalFailure: DVD_PB_STOPPED = 9
DVD_PB_STOPPED_RegionFailure: DVD_PB_STOPPED = 10
DVD_PB_STOPPED_MacrovisionFailure: DVD_PB_STOPPED = 11
DVD_PB_STOPPED_DiscReadError: DVD_PB_STOPPED = 12
DVD_PB_STOPPED_CopyProtectFailure: DVD_PB_STOPPED = 13
DVD_PB_STOPPED_CopyProtectOutputFailure: DVD_PB_STOPPED = 14
DVD_PB_STOPPED_CopyProtectOutputNotSupported: DVD_PB_STOPPED = 15
class DVD_PLAYBACK_LOCATION(Structure):
    TitleNum: UInt32
    ChapterNum: UInt32
    TimeCode: UInt32
class DVD_PLAYBACK_LOCATION2(Structure):
    TitleNum: UInt32
    ChapterNum: UInt32
    TimeCode: win32more.Media.DirectShow.DVD_HMSF_TIMECODE
    TimeCodeFlags: UInt32
DVD_PLAY_DIRECTION = Int32
DVD_DIR_FORWARD: DVD_PLAY_DIRECTION = 0
DVD_DIR_BACKWARD: DVD_PLAY_DIRECTION = 1
DVD_PREFERRED_DISPLAY_MODE = Int32
DISPLAY_CONTENT_DEFAULT: DVD_PREFERRED_DISPLAY_MODE = 0
DISPLAY_16x9: DVD_PREFERRED_DISPLAY_MODE = 1
DISPLAY_4x3_PANSCAN_PREFERRED: DVD_PREFERRED_DISPLAY_MODE = 2
DISPLAY_4x3_LETTERBOX_PREFERRED: DVD_PREFERRED_DISPLAY_MODE = 3
class DVD_REGION(Structure):
    CopySystem: Byte
    RegionData: Byte
    SystemRegion: Byte
    ResetCount: Byte
DVD_RELATIVE_BUTTON = Int32
DVD_Relative_Upper: DVD_RELATIVE_BUTTON = 1
DVD_Relative_Lower: DVD_RELATIVE_BUTTON = 2
DVD_Relative_Left: DVD_RELATIVE_BUTTON = 3
DVD_Relative_Right: DVD_RELATIVE_BUTTON = 4
DVD_SUBPICTURE_CODING = Int32
DVD_SPCoding_RunLength: DVD_SUBPICTURE_CODING = 0
DVD_SPCoding_Extended: DVD_SUBPICTURE_CODING = 1
DVD_SPCoding_Other: DVD_SUBPICTURE_CODING = 2
DVD_SUBPICTURE_LANG_EXT = Int32
DVD_SP_EXT_NotSpecified: DVD_SUBPICTURE_LANG_EXT = 0
DVD_SP_EXT_Caption_Normal: DVD_SUBPICTURE_LANG_EXT = 1
DVD_SP_EXT_Caption_Big: DVD_SUBPICTURE_LANG_EXT = 2
DVD_SP_EXT_Caption_Children: DVD_SUBPICTURE_LANG_EXT = 3
DVD_SP_EXT_CC_Normal: DVD_SUBPICTURE_LANG_EXT = 5
DVD_SP_EXT_CC_Big: DVD_SUBPICTURE_LANG_EXT = 6
DVD_SP_EXT_CC_Children: DVD_SUBPICTURE_LANG_EXT = 7
DVD_SP_EXT_Forced: DVD_SUBPICTURE_LANG_EXT = 9
DVD_SP_EXT_DirectorComments_Normal: DVD_SUBPICTURE_LANG_EXT = 13
DVD_SP_EXT_DirectorComments_Big: DVD_SUBPICTURE_LANG_EXT = 14
DVD_SP_EXT_DirectorComments_Children: DVD_SUBPICTURE_LANG_EXT = 15
DVD_SUBPICTURE_TYPE = Int32
DVD_SPType_NotSpecified: DVD_SUBPICTURE_TYPE = 0
DVD_SPType_Language: DVD_SUBPICTURE_TYPE = 1
DVD_SPType_Other: DVD_SUBPICTURE_TYPE = 2
class DVD_SubpictureAttributes(Structure):
    Type: win32more.Media.DirectShow.DVD_SUBPICTURE_TYPE
    CodingMode: win32more.Media.DirectShow.DVD_SUBPICTURE_CODING
    Language: UInt32
    LanguageExtension: win32more.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT
class DVD_TIMECODE(Structure):
    _bitfield: UInt32
DVD_TIMECODE_FLAGS = Int32
DVD_TC_FLAG_25fps: DVD_TIMECODE_FLAGS = 1
DVD_TC_FLAG_30fps: DVD_TIMECODE_FLAGS = 2
DVD_TC_FLAG_DropFrame: DVD_TIMECODE_FLAGS = 4
DVD_TC_FLAG_Interpolated: DVD_TIMECODE_FLAGS = 8
DVD_TITLE_APPMODE = Int32
DVD_AppMode_Not_Specified: DVD_TITLE_APPMODE = 0
DVD_AppMode_Karaoke: DVD_TITLE_APPMODE = 1
DVD_AppMode_Other: DVD_TITLE_APPMODE = 3
DVD_TextCharSet = Int32
DVD_CharSet_Unicode: DVD_TextCharSet = 0
DVD_CharSet_ISO646: DVD_TextCharSet = 1
DVD_CharSet_JIS_Roman_Kanji: DVD_TextCharSet = 2
DVD_CharSet_ISO8859_1: DVD_TextCharSet = 3
DVD_CharSet_ShiftJIS_Kanji_Roman_Katakana: DVD_TextCharSet = 4
DVD_TextStringType = Int32
DVD_Struct_Volume: DVD_TextStringType = 1
DVD_Struct_Title: DVD_TextStringType = 2
DVD_Struct_ParentalID: DVD_TextStringType = 3
DVD_Struct_PartOfTitle: DVD_TextStringType = 4
DVD_Struct_Cell: DVD_TextStringType = 5
DVD_Stream_Audio: DVD_TextStringType = 16
DVD_Stream_Subpicture: DVD_TextStringType = 17
DVD_Stream_Angle: DVD_TextStringType = 18
DVD_Channel_Audio: DVD_TextStringType = 32
DVD_General_Name: DVD_TextStringType = 48
DVD_General_Comments: DVD_TextStringType = 49
DVD_Title_Series: DVD_TextStringType = 56
DVD_Title_Movie: DVD_TextStringType = 57
DVD_Title_Video: DVD_TextStringType = 58
DVD_Title_Album: DVD_TextStringType = 59
DVD_Title_Song: DVD_TextStringType = 60
DVD_Title_Other: DVD_TextStringType = 63
DVD_Title_Sub_Series: DVD_TextStringType = 64
DVD_Title_Sub_Movie: DVD_TextStringType = 65
DVD_Title_Sub_Video: DVD_TextStringType = 66
DVD_Title_Sub_Album: DVD_TextStringType = 67
DVD_Title_Sub_Song: DVD_TextStringType = 68
DVD_Title_Sub_Other: DVD_TextStringType = 71
DVD_Title_Orig_Series: DVD_TextStringType = 72
DVD_Title_Orig_Movie: DVD_TextStringType = 73
DVD_Title_Orig_Video: DVD_TextStringType = 74
DVD_Title_Orig_Album: DVD_TextStringType = 75
DVD_Title_Orig_Song: DVD_TextStringType = 76
DVD_Title_Orig_Other: DVD_TextStringType = 79
DVD_Other_Scene: DVD_TextStringType = 80
DVD_Other_Cut: DVD_TextStringType = 81
DVD_Other_Take: DVD_TextStringType = 82
class DVD_TitleAttributes(Structure):
    Anonymous: _Anonymous_e__Union
    VideoAttributes: win32more.Media.DirectShow.DVD_VideoAttributes
    ulNumberOfAudioStreams: UInt32
    AudioAttributes: win32more.Media.DirectShow.DVD_AudioAttributes * 8
    MultichannelAudioAttributes: win32more.Media.DirectShow.DVD_MultichannelAudioAttributes * 8
    ulNumberOfSubpictureStreams: UInt32
    SubpictureAttributes: win32more.Media.DirectShow.DVD_SubpictureAttributes * 32
    class _Anonymous_e__Union(Union):
        AppMode: win32more.Media.DirectShow.DVD_TITLE_APPMODE
        TitleLength: win32more.Media.DirectShow.DVD_HMSF_TIMECODE
DVD_VIDEO_COMPRESSION = Int32
DVD_VideoCompression_Other: DVD_VIDEO_COMPRESSION = 0
DVD_VideoCompression_MPEG1: DVD_VIDEO_COMPRESSION = 1
DVD_VideoCompression_MPEG2: DVD_VIDEO_COMPRESSION = 2
class DVD_VideoAttributes(Structure):
    fPanscanPermitted: win32more.Foundation.BOOL
    fLetterboxPermitted: win32more.Foundation.BOOL
    ulAspectX: UInt32
    ulAspectY: UInt32
    ulFrameRate: UInt32
    ulFrameHeight: UInt32
    Compression: win32more.Media.DirectShow.DVD_VIDEO_COMPRESSION
    fLine21Field1InGOP: win32more.Foundation.BOOL
    fLine21Field2InGOP: win32more.Foundation.BOOL
    ulSourceResolutionX: UInt32
    ulSourceResolutionY: UInt32
    fIsSourceLetterboxed: win32more.Foundation.BOOL
    fIsFilmMode: win32more.Foundation.BOOL
DVD_WARNING = Int32
DVD_WARNING_InvalidDVD1_0Disc: DVD_WARNING = 1
DVD_WARNING_FormatNotSupported: DVD_WARNING = 2
DVD_WARNING_IllegalNavCommand: DVD_WARNING = 3
DVD_WARNING_Open: DVD_WARNING = 4
DVD_WARNING_Seek: DVD_WARNING = 5
DVD_WARNING_Read: DVD_WARNING = 6
class DVINFO(Structure):
    dwDVAAuxSrc: UInt32
    dwDVAAuxCtl: UInt32
    dwDVAAuxSrc1: UInt32
    dwDVAAuxCtl1: UInt32
    dwDVVAuxSrc: UInt32
    dwDVVAuxCtl: UInt32
    dwDVReserved: UInt32 * 2
class DVR_STREAM_DESC(Structure):
    Version: UInt32
    StreamId: UInt32
    Default: win32more.Foundation.BOOL
    Creation: win32more.Foundation.BOOL
    Reserved: UInt32
    guidSubMediaType: Guid
    guidFormatType: Guid
    MediaType: win32more.Media.MediaFoundation.AM_MEDIA_TYPE
class DXVA2SW_CALLBACKS(Structure):
    Size: UInt32
    GetVideoProcessorRenderTargetCount: win32more.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETCOUNT
    GetVideoProcessorRenderTargets: win32more.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETS
    GetVideoProcessorCaps: win32more.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORCAPS
    GetVideoProcessorSubStreamFormatCount: win32more.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATCOUNT
    GetVideoProcessorSubStreamFormats: win32more.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATS
    GetProcAmpRange: win32more.Media.DirectShow.PDXVA2SW_GETPROCAMPRANGE
    GetFilterPropertyRange: win32more.Media.DirectShow.PDXVA2SW_GETFILTERPROPERTYRANGE
    CreateVideoProcessDevice: win32more.Media.DirectShow.PDXVA2SW_CREATEVIDEOPROCESSDEVICE
    DestroyVideoProcessDevice: win32more.Media.DirectShow.PDXVA2SW_DESTROYVIDEOPROCESSDEVICE
    VideoProcessBeginFrame: win32more.Media.DirectShow.PDXVA2SW_VIDEOPROCESSBEGINFRAME
    VideoProcessEndFrame: win32more.Media.DirectShow.PDXVA2SW_VIDEOPROCESSENDFRAME
    VideoProcessSetRenderTarget: win32more.Media.DirectShow.PDXVA2SW_VIDEOPROCESSSETRENDERTARGET
    VideoProcessBlt: win32more.Media.DirectShow.PDXVA2SW_VIDEOPROCESSBLT
class DXVA2TraceVideoProcessBltData(Structure):
    wmiHeader: win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pRenderTarget: UInt64
    TargetFrameTime: UInt64
    TargetRect: win32more.Foundation.RECT
    Enter: win32more.Foundation.BOOL
class DXVA2Trace_DecodeDevBeginFrameData(Structure):
    wmiHeader: win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pRenderTarget: UInt64
    Enter: win32more.Foundation.BOOL
class DXVA2Trace_DecodeDevCreatedData(Structure):
    wmiHeader: win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pD3DDevice: UInt64
    DeviceGuid: Guid
    Width: UInt32
    Height: UInt32
    Enter: win32more.Foundation.BOOL
class DXVA2Trace_DecodeDevGetBufferData(Structure):
    wmiHeader: win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    BufferType: UInt32
    Enter: win32more.Foundation.BOOL
class DXVA2Trace_DecodeDeviceData(Structure):
    wmiHeader: win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    Enter: win32more.Foundation.BOOL
class DXVA2Trace_VideoProcessDevCreatedData(Structure):
    wmiHeader: win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pD3DDevice: UInt64
    DeviceGuid: Guid
    RTFourCC: UInt32
    Width: UInt32
    Height: UInt32
    Enter: win32more.Foundation.BOOL
class DXVA2Trace_VideoProcessDeviceData(Structure):
    wmiHeader: win32more.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    Enter: win32more.Foundation.BOOL
DXVA2_DestinationFlags = Int32
DXVA2_DestinationFlag_Background_Changed: DXVA2_DestinationFlags = 1
DXVA2_DestinationFlag_TargetRect_Changed: DXVA2_DestinationFlags = 2
DXVA2_DestinationFlag_ColorData_Changed: DXVA2_DestinationFlags = 4
DXVA2_DestinationFlag_Alpha_Changed: DXVA2_DestinationFlags = 8
DXVA2_DestinationFlag_RFF: DXVA2_DestinationFlags = 65536
DXVA2_DestinationFlag_TFF: DXVA2_DestinationFlags = 131072
DXVA2_DestinationFlag_RFF_TFF_Present: DXVA2_DestinationFlags = 262144
DXVA2_DestinationFlagMask: DXVA2_DestinationFlags = -65521
DXVA2_SampleFlags = Int32
DXVA2_SampleFlag_Palette_Changed: DXVA2_SampleFlags = 1
DXVA2_SampleFlag_SrcRect_Changed: DXVA2_SampleFlags = 2
DXVA2_SampleFlag_DstRect_Changed: DXVA2_SampleFlags = 4
DXVA2_SampleFlag_ColorData_Changed: DXVA2_SampleFlags = 8
DXVA2_SampleFlag_PlanarAlpha_Changed: DXVA2_SampleFlags = 16
DXVA2_SampleFlag_RFF: DXVA2_SampleFlags = 65536
DXVA2_SampleFlag_TFF: DXVA2_SampleFlags = 131072
DXVA2_SampleFlag_RFF_TFF_Present: DXVA2_SampleFlags = 262144
DXVA2_SampleFlagsMask: DXVA2_SampleFlags = -65505
class DXVA2_VIDEOPROCESSBLT(Structure):
    TargetFrame: Int64
    TargetRect: win32more.Foundation.RECT
    ConstrictionSize: win32more.Foundation.SIZE
    StreamingFlags: UInt32
    BackgroundColor: win32more.Media.MediaFoundation.DXVA2_AYUVSample16
    DestFormat: win32more.Media.MediaFoundation.DXVA2_ExtendedFormat
    DestFlags: UInt32
    ProcAmpValues: win32more.Media.MediaFoundation.DXVA2_ProcAmpValues
    Alpha: win32more.Media.MediaFoundation.DXVA2_Fixed32
    NoiseFilterLuma: win32more.Media.MediaFoundation.DXVA2_FilterValues
    NoiseFilterChroma: win32more.Media.MediaFoundation.DXVA2_FilterValues
    DetailFilterLuma: win32more.Media.MediaFoundation.DXVA2_FilterValues
    DetailFilterChroma: win32more.Media.MediaFoundation.DXVA2_FilterValues
    pSrcSurfaces: POINTER(win32more.Media.DirectShow.DXVA2_VIDEOSAMPLE_head)
    NumSrcSurfaces: UInt32
class DXVA2_VIDEOSAMPLE(Structure):
    Start: Int64
    End: Int64
    SampleFormat: win32more.Media.MediaFoundation.DXVA2_ExtendedFormat
    SampleFlags: UInt32
    SrcResource: c_void_p
    SrcRect: win32more.Foundation.RECT
    DstRect: win32more.Foundation.RECT
    Pal: win32more.Media.MediaFoundation.DXVA2_AYUVSample8 * 16
    PlanarAlpha: win32more.Media.MediaFoundation.DXVA2_Fixed32
class DXVA_COPPSetProtectionLevelCmdData(Structure):
    ProtType: UInt32
    ProtLevel: UInt32
    ExtendedInfoChangeMask: UInt32
    ExtendedInfoData: UInt32
class DXVA_COPPSetSignalingCmdData(Structure):
    ActiveTVProtectionStandard: UInt32
    AspectRatioChangeMask1: UInt32
    AspectRatioData1: UInt32
    AspectRatioChangeMask2: UInt32
    AspectRatioData2: UInt32
    AspectRatioChangeMask3: UInt32
    AspectRatioData3: UInt32
    ExtendedInfoChangeMask: UInt32 * 4
    ExtendedInfoData: UInt32 * 4
    Reserved: UInt32
class DXVA_COPPStatusData(Structure):
    rApp: Guid
    dwFlags: UInt32
    dwData: UInt32
    ExtendedInfoValidMask: UInt32
    ExtendedInfoData: UInt32
class DXVA_COPPStatusDisplayData(Structure):
    rApp: Guid
    dwFlags: UInt32
    DisplayWidth: UInt32
    DisplayHeight: UInt32
    Format: UInt32
    d3dFormat: UInt32
    FreqNumerator: UInt32
    FreqDenominator: UInt32
class DXVA_COPPStatusHDCPKeyData(Structure):
    rApp: Guid
    dwFlags: UInt32
    dwHDCPFlags: UInt32
    BKey: Guid
    Reserved1: Guid
    Reserved2: Guid
class DXVA_COPPStatusSignalingCmdData(Structure):
    rApp: Guid
    dwFlags: UInt32
    AvailableTVProtectionStandards: UInt32
    ActiveTVProtectionStandard: UInt32
    TVType: UInt32
    AspectRatioValidMask1: UInt32
    AspectRatioData1: UInt32
    AspectRatioValidMask2: UInt32
    AspectRatioData2: UInt32
    AspectRatioValidMask3: UInt32
    AspectRatioData3: UInt32
    ExtendedInfoValidMask: UInt32 * 4
    ExtendedInfoData: UInt32 * 4
DigitalCableLocator = Guid('03c06416-d127-407a-ab-4c-fd-d2-79-ab-be-5d')
DigitalCableTuneRequest = Guid('26ec0b63-aa90-458a-8d-f4-56-59-f2-c8-a1-8a')
DigitalCableTuningSpace = Guid('d9bb4cee-b87a-47f1-ac-92-b0-8d-9c-78-13-fc')
DigitalLocator = Guid('6e50cc0d-c19b-4bf6-81-0b-5b-d6-07-61-f5-cc')
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
class DualMonoInfo(Structure):
    LangID1: UInt16
    LangID2: UInt16
    lISOLangCode1: Int32
    lISOLangCode2: Int32
class DvbParentalRatingDescriptor(Structure):
    ulNumParams: UInt32
    pParams: win32more.Media.DirectShow.DvbParentalRatingParam * 1
class DvbParentalRatingParam(Structure):
    szCountryCode: win32more.Foundation.CHAR * 4
    bRating: Byte
class EALocationCodeType(Structure):
    LocationCodeScheme: win32more.Media.DirectShow.LocationCodeSchemeType
    state_code: Byte
    county_subdivision: Byte
    county_code: UInt16
ECHOSTAR_SATELLITE_TV_NETWORK_TYPE = Guid('c4f6b31b-c6bf-4759-88-6f-a7-38-6d-ca-27-a0')
ESEventFactory = Guid('8e8a07da-71f8-40c1-a9-29-5e-3a-86-8a-c2-c6')
ESEventService = Guid('c20447fc-ec60-475e-81-3f-d2-b0-a6-de-ce-fe')
ETFilter = Guid('c4c4c4f1-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
EVENTID_ARIBcontentSpanningEvent = Guid('3a954083-93d0-463e-90-b2-07-42-c4-96-ed-f0')
EVENTID_AudioDescriptorSpanningEvent = Guid('107bd41c-a6da-4691-83-69-11-b2-cd-aa-28-8e')
EVENTID_AudioTypeSpanningEvent = Guid('501cbfbe-b849-42ce-9b-e9-3d-b8-69-fb-82-b3')
EVENTID_BDAConditionalAccessTAG = Guid('efc3a459-ae8b-4b4a-8f-e9-79-a0-d0-97-f3-ea')
EVENTID_BDAEventingServicePendingEvent = Guid('5ca51711-5ddc-41a6-94-30-e4-1b-8b-3b-bc-5b')
EVENTID_BDA_CASBroadcastMMI = Guid('676876f0-1132-404c-a7-ca-e7-20-69-a9-d5-4f')
EVENTID_BDA_CASCloseMMI = Guid('5d0f550f-de2e-479d-83-45-ec-0e-95-57-e8-a2')
EVENTID_BDA_CASOpenMMI = Guid('85dac915-e593-410d-84-71-d6-81-21-05-f2-8e')
EVENTID_BDA_CASReleaseTuner = Guid('20c1a16b-441f-49a5-bb-5c-e9-a0-44-95-c6-c1')
EVENTID_BDA_CASRequestTuner = Guid('cf39a9d8-f5d3-4685-be-57-ed-81-db-a4-6b-27')
EVENTID_BDA_DiseqCResponseAvailable = Guid('efa628f8-1f2c-4b67-9e-a5-ac-f6-fa-9a-1f-36')
EVENTID_BDA_EncoderSignalLock = Guid('5ec90eb9-39fa-4cfc-b9-3f-00-bb-11-07-7f-5e')
EVENTID_BDA_FdcStatus = Guid('05f25366-d0eb-43d2-bc-3c-68-2b-86-3d-f1-42')
EVENTID_BDA_FdcTableSection = Guid('6a0cd757-4ce3-4e5b-94-44-71-87-b8-71-52-c5')
EVENTID_BDA_GPNVValueUpdate = Guid('ff75c68c-f416-4e7e-bf-17-6d-55-c5-df-15-75')
EVENTID_BDA_GuideDataAvailable = Guid('98db717a-478a-4cd4-92-d0-95-f6-6b-89-e5-b1')
EVENTID_BDA_GuideDataError = Guid('ac33c448-6f73-4fd7-b3-41-59-4c-36-0d-8d-74')
EVENTID_BDA_GuideServiceInformationUpdated = Guid('a1c3ea2b-175f-4458-b7-35-50-7d-22-db-23-a6')
EVENTID_BDA_IsdbCASResponse = Guid('d4cb1966-41bc-4ced-9a-20-fd-ce-ac-78-f7-0d')
EVENTID_BDA_LbigsCloseConnectionHandle = Guid('c2f08b99-65ef-4314-96-71-e9-9d-4c-ce-0b-ae')
EVENTID_BDA_LbigsOpenConnection = Guid('356207b2-6f31-4eb0-a2-71-b3-fa-6b-b7-68-0f')
EVENTID_BDA_LbigsSendData = Guid('1123277b-f1c6-4154-8b-0d-48-e6-15-70-59-aa')
EVENTID_BDA_RatingPinReset = Guid('c6e048c0-c574-4c26-bc-da-2f-4d-35-eb-5e-85')
EVENTID_BDA_TransprtStreamSelectorInfo = Guid('c40f9f85-09d0-489c-9e-9c-0a-bb-b5-69-51-b0')
EVENTID_BDA_TunerNoSignal = Guid('e29b382b-1edd-4930-bc-46-68-2f-d7-2d-2d-fb')
EVENTID_BDA_TunerSignalLock = Guid('1872e740-f573-429b-a0-0e-d9-c1-e4-08-af-09')
EVENTID_BDA_UpdateDrmStatus = Guid('65a6f681-1462-473b-88-ce-cb-73-14-27-bd-b5')
EVENTID_BDA_UpdateScanState = Guid('55702b50-7b49-42b8-a8-2f-4a-fb-69-1b-06-28')
EVENTID_CADenialCountChanged = Guid('2a65c528-2249-4070-ac-16-00-39-0c-df-b2-dd')
EVENTID_CASFailureSpanningEvent = Guid('ead831ae-5529-4d1f-af-ce-0d-8c-d1-25-7d-30')
EVENTID_CSDescriptorSpanningEvent = Guid('efe779d9-97f0-4786-80-0d-95-cf-50-5d-dc-66')
EVENTID_CandidatePostTuneData = Guid('9f02d3d0-9f06-4369-9f-1e-3a-d6-ca-19-80-7e')
EVENTID_CardStatusChanged = Guid('a265faea-f874-4b38-9f-f7-c5-3d-02-96-99-96')
EVENTID_ChannelChangeSpanningEvent = Guid('9067c5e5-4c5c-4205-86-c8-7a-fe-20-fe-1e-fa')
EVENTID_ChannelInfoSpanningEvent = Guid('41f36d80-4132-4cc2-b1-21-01-a4-32-19-d8-1b')
EVENTID_ChannelTypeSpanningEvent = Guid('72ab1d51-87d2-489b-ba-11-0e-08-dc-21-02-43')
EVENTID_CtxADescriptorSpanningEvent = Guid('3ab4a2e6-4247-4b34-89-6c-30-af-a5-d2-1c-24')
EVENTID_DFNWithNoActualAVData = Guid('f5689ffe-55f9-4bb3-96-be-ae-97-1c-63-ba-e0')
EVENTID_DRMParingStatusChanged = Guid('000906f5-f0d1-41d6-a7-df-40-28-69-76-69-f6')
EVENTID_DRMParingStepComplete = Guid('5b2ebf78-b752-4420-b4-1e-a4-72-dc-95-82-8e')
EVENTID_DVBScramblingControlSpanningEvent = Guid('4bd4e1c4-90a1-4109-82-36-27-f0-0e-7d-cc-5b')
EVENTID_DualMonoSpanningEvent = Guid('a9a29b56-a84b-488c-89-d5-0d-4e-76-57-c8-ce')
EVENTID_DvbParentalRatingDescriptor = Guid('2a67a58d-eca5-4eac-ab-cb-e7-34-d3-77-6d-0a')
EVENTID_EASMessageReceived = Guid('d10df9d5-c261-4b85-9e-8a-51-7b-32-99-ca-b2')
EVENTID_EmmMessageSpanningEvent = Guid('6bf00268-4f7e-4294-aa-87-e9-e9-53-e4-3f-14')
EVENTID_EntitlementChanged = Guid('9071ad5d-2359-4c95-86-94-af-a8-1d-70-bf-d5')
EVENTID_LanguageSpanningEvent = Guid('e292666d-9c02-448d-aa-8d-78-1a-93-fd-c3-95')
EVENTID_MMIMessage = Guid('052c29af-09a4-4b93-89-0f-bd-6a-34-89-68-a4')
EVENTID_NewSignalAcquired = Guid('c87ec52d-cd18-404a-a0-76-c0-2a-27-3d-3d-e7')
EVENTID_PBDAParentalControlEvent = Guid('f947aa85-fb52-48e8-b9-c5-e1-e1-f4-11-a5-1a')
EVENTID_PIDListSpanningEvent = Guid('47fc8f65-e2bb-4634-9c-ef-fd-bf-e6-26-1d-5c')
EVENTID_PSITable = Guid('1b9c3703-d447-4e16-97-bb-01-79-9f-c0-31-ed')
EVENTID_RRTSpanningEvent = Guid('f6cfc8f4-da93-4f2f-bf-f8-ba-1e-e6-fc-a3-a2')
EVENTID_STBChannelNumber = Guid('17c4d730-d0f0-413a-8c-99-50-04-69-de-35-ad')
EVENTID_ServiceTerminated = Guid('0a1d591c-e0d2-4f8e-89-60-23-35-be-f4-5c-cb')
EVENTID_SignalAndServiceStatusSpanningEvent = Guid('8068c5cb-3c04-492b-b4-7d-03-08-82-0d-ce-51')
EVENTID_SignalStatusChanged = Guid('6d9cfaf2-702d-4b01-8d-ff-68-92-ad-20-d1-91')
EVENTID_StreamIDSpanningEvent = Guid('caf1ab68-e153-4d41-a6-b3-a7-c9-98-db-75-ee')
EVENTID_StreamTypeSpanningEvent = Guid('82af2ebc-30a6-4264-a8-0b-ad-2e-13-72-ac-60')
EVENTID_SubtitleSpanningEvent = Guid('5dcec048-d0b9-4163-87-2c-4f-32-22-3b-e8-8a')
EVENTID_TeletextSpanningEvent = Guid('9599d950-5f33-4617-af-7c-1e-54-b5-10-da-a3')
EVENTID_TuneFailureEvent = Guid('d97287b2-2dfd-436a-94-85-99-d7-d4-ab-5a-69')
EVENTID_TuneFailureSpanningEvent = Guid('6f8aa455-5ee1-48ab-a2-7c-4c-8d-70-b9-ae-ba')
EVENTID_TuningChanged = Guid('9d7e6235-4b7d-425d-a6-d1-d7-17-c3-3b-9c-4c')
EVENTID_TuningChanging = Guid('83183c03-c09e-45c4-a7-19-80-7a-94-95-2b-f9')
EVENTTYPE_CASDescrambleFailureEvent = Guid('b2127d42-7be5-4f4b-91-30-66-79-89-9f-4f-4b')
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
EntitlementType = Int32
EntitlementType_Entitled: EntitlementType = 0
EntitlementType_NotEntitled: EntitlementType = 1
EntitlementType_TechnicalFailure: EntitlementType = 2
EvalRat = Guid('c5c5c5f1-3abc-11d6-b2-5b-00-c0-4f-a0-c0-26')
FECMethod = Int32
BDA_FEC_METHOD_NOT_SET: FECMethod = -1
BDA_FEC_METHOD_NOT_DEFINED: FECMethod = 0
BDA_FEC_VITERBI: FECMethod = 1
BDA_FEC_RS_204_188: FECMethod = 2
BDA_FEC_LDPC: FECMethod = 3
BDA_FEC_BCH: FECMethod = 4
BDA_FEC_RS_147_130: FECMethod = 5
BDA_FEC_MAX: FECMethod = 6
class FILTER_INFO(Structure):
    achName: Char * 128
    pGraph: win32more.Media.DirectShow.IFilterGraph_head
FILTER_STATE = Int32
State_Stopped: FILTER_STATE = 0
State_Paused: FILTER_STATE = 1
State_Running: FILTER_STATE = 2
FilgraphManager = Guid('e436ebb3-524f-11ce-9f-53-00-20-af-0b-a7-70')
FormatNotSupportedEvents = Int32
FORMATNOTSUPPORTED_CLEAR: FormatNotSupportedEvents = 0
FORMATNOTSUPPORTED_NOTSUPPORTED: FormatNotSupportedEvents = 1
GuardInterval = Int32
BDA_GUARD_NOT_SET: GuardInterval = -1
BDA_GUARD_NOT_DEFINED: GuardInterval = 0
BDA_GUARD_1_32: GuardInterval = 1
BDA_GUARD_1_16: GuardInterval = 2
BDA_GUARD_1_8: GuardInterval = 3
BDA_GUARD_1_4: GuardInterval = 4
BDA_GUARD_1_128: GuardInterval = 5
BDA_GUARD_19_128: GuardInterval = 6
BDA_GUARD_19_256: GuardInterval = 7
BDA_GUARD_MAX: GuardInterval = 8
class HEAACWAVEFORMAT(Structure):
    wfInfo: win32more.Media.DirectShow.HEAACWAVEINFO
    pbAudioSpecificConfig: Byte * 1
class HEAACWAVEINFO(Structure):
    wfx: win32more.Media.Audio.WAVEFORMATEX
    wPayloadType: UInt16
    wAudioProfileLevelIndication: UInt16
    wStructType: UInt16
    wReserved1: UInt16
    dwReserved2: UInt32
    _pack_ = 1
HierarchyAlpha = Int32
BDA_HALPHA_NOT_SET: HierarchyAlpha = -1
BDA_HALPHA_NOT_DEFINED: HierarchyAlpha = 0
BDA_HALPHA_1: HierarchyAlpha = 1
BDA_HALPHA_2: HierarchyAlpha = 2
BDA_HALPHA_4: HierarchyAlpha = 3
BDA_HALPHA_MAX: HierarchyAlpha = 4
class IAMAnalogVideoDecoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e13350-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def get_AvailableTVFormats(lAnalogVideoStandard: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_TVFormat(lAnalogVideoStandard: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_TVFormat(plAnalogVideoStandard: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_HorizontalLocked(plLocked: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_VCRHorizontalLocking(lVCRHorizontalLocking: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_VCRHorizontalLocking(plVCRHorizontalLocking: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_NumberOfLines(plNumberOfLines: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_OutputEnable(lOutputEnable: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_OutputEnable(plOutputEnable: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMAnalogVideoEncoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e133b0-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def get_AvailableTVFormats(lAnalogVideoStandard: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_TVFormat(lAnalogVideoStandard: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_TVFormat(plAnalogVideoStandard: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_CopyProtection(lVideoCopyProtection: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_CopyProtection(lVideoCopyProtection: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_CCEnable(lCCEnable: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_CCEnable(lCCEnable: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMAsyncReaderTimestampScaling(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('cf7b26fc-9a00-485b-81-47-3e-78-9d-5e-8f-67')
    @commethod(3)
    def GetTimestampMode(pfRaw: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTimestampMode(fRaw: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IAMAudioInputMixer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('54c39221-8380-11d0-b3-f0-00-aa-00-37-61-c5')
    @commethod(3)
    def put_Enable(fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Enable(pfEnable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_Mono(fMono: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Mono(pfMono: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_MixLevel(Level: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_MixLevel(pLevel: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Pan(Pan: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Pan(pPan: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Loudness(fLoudness: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Loudness(pfLoudness: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Treble(Treble: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Treble(pTreble: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_TrebleRange(pRange: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Bass(Bass: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Bass(pBass: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_BassRange(pRange: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
class IAMAudioRendererStats(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('22320cb2-d41a-11d2-bf-7c-d7-cb-9d-f0-bf-93')
    @commethod(3)
    def GetStatParam(dwParam: UInt32, pdwParam1: POINTER(UInt32), pdwParam2: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAMBufferNegotiation(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56ed71a0-af5f-11d0-b3-f0-00-aa-00-37-61-c5')
    @commethod(3)
    def SuggestAllocatorProperties(pprop: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllocatorProperties(pprop: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
class IAMCameraControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e13370-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def GetRange(Property: Int32, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Set(Property: Int32, lValue: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Get(Property: Int32, lValue: POINTER(Int32), Flags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMCertifiedOutputProtection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6feded3e-0ff1-4901-a2-f1-43-f7-01-2c-85-15')
    @commethod(3)
    def KeyExchange(pRandom: POINTER(Guid), VarLenCertGH: POINTER(c_char_p_no), pdwLengthCertGH: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SessionSequenceStart(pSig: POINTER(win32more.Media.DirectShow.AMCOPPSignature_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ProtectionCommand(cmd: POINTER(win32more.Media.DirectShow.AMCOPPCommand_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ProtectionStatus(pStatusInput: POINTER(win32more.Media.DirectShow.AMCOPPStatusInput_head), pStatusOutput: POINTER(win32more.Media.DirectShow.AMCOPPStatusOutput_head)) -> win32more.Foundation.HRESULT: ...
class IAMChannelInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa2aa8f2-8b62-11d0-a5-20-00-00-00-00-00-00')
    @commethod(7)
    def get_ChannelName(pbstrChannelName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ChannelDescription(pbstrChannelDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ChannelURL(pbstrChannelURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_ContactAddress(pbstrContactAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ContactPhone(pbstrContactPhone: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ContactEmail(pbstrContactEmail: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IAMClockAdjust(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4d5466b0-a49c-11d1-ab-e8-00-a0-c9-05-f3-75')
    @commethod(3)
    def SetClockDelta(rtDelta: Int64) -> win32more.Foundation.HRESULT: ...
class IAMClockSlave(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9fd52741-176d-4b36-8f-51-ca-8f-93-32-23-be')
    @commethod(3)
    def SetErrorTolerance(dwTolerance: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorTolerance(pdwTolerance: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAMCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868b9-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(lItem: Int32, ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IAMCopyCaptureFileProgress(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('670d1d20-a068-11d0-b3-f0-00-aa-00-37-61-c5')
    @commethod(3)
    def Progress(iProgress: Int32) -> win32more.Foundation.HRESULT: ...
class IAMCrossbar(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e13380-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def get_PinCounts(OutputPinCount: POINTER(Int32), InputPinCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CanRoute(OutputPinIndex: Int32, InputPinIndex: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Route(OutputPinIndex: Int32, InputPinIndex: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_IsRoutedTo(OutputPinIndex: Int32, InputPinIndex: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_CrossbarPinInfo(IsInputPin: win32more.Foundation.BOOL, PinIndex: Int32, PinIndexRelated: POINTER(Int32), PhysicalType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMDecoderCaps(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0dff467-d499-4986-97-2b-e1-d9-09-0f-a9-41')
    @commethod(3)
    def GetDecoderCaps(dwCapIndex: UInt32, lpdwCap: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAMDevMemoryAllocator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6545bf0-e76b-11d0-bd-52-00-a0-c9-11-ce-86')
    @commethod(3)
    def GetInfo(pdwcbTotalFree: POINTER(UInt32), pdwcbLargestFree: POINTER(UInt32), pdwcbTotalMemory: POINTER(UInt32), pdwcbMinimumChunk: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CheckMemory(pBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Alloc(ppBuffer: POINTER(c_char_p_no), pdwcbBuffer: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Free(pBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevMemoryObject(ppUnkInnner: POINTER(win32more.System.Com.IUnknown_head), pUnkOuter: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IAMDevMemoryControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6545bf1-e76b-11d0-bd-52-00-a0-c9-11-ce-86')
    @commethod(3)
    def QueryWriteSync() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WriteSync() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDevId(pdwDevId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAMDeviceRemoval(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f90a6130-b658-11d2-ae-49-00-00-f8-75-4b-99')
    @commethod(3)
    def DeviceInfo(pclsidInterfaceClass: POINTER(Guid), pwszSymbolicLink: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reassociate() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Disassociate() -> win32more.Foundation.HRESULT: ...
class IAMDirectSound(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('546f4260-d53e-11cf-b3-f0-00-aa-00-37-61-c5')
    @commethod(3)
    def GetDirectSoundInterface(lplpds: POINTER(win32more.Media.Audio.DirectSound.IDirectSound_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrimaryBufferInterface(lplpdsb: POINTER(win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSecondaryBufferInterface(lplpdsb: POINTER(win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseDirectSoundInterface(lpds: win32more.Media.Audio.DirectSound.IDirectSound_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ReleasePrimaryBufferInterface(lpdsb: win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ReleaseSecondaryBufferInterface(lpdsb: win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetFocusWindow(param0: win32more.Foundation.HWND, param1: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFocusWindow(param0: POINTER(win32more.Foundation.HWND), param1: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IAMDroppedFrames(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e13344-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def GetNumDropped(plDropped: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumNotDropped(plNotDropped: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDroppedInfo(lSize: Int32, plArray: POINTER(Int32), plNumCopied: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAverageFrameSize(plAverageSize: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMExtDevice(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b5730a90-1a2c-11cf-8c-23-00-aa-00-6b-68-14')
    @commethod(3)
    def GetCapability(Capability: Int32, pValue: POINTER(Int32), pdblValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_ExternalDeviceID(ppszData: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_ExternalDeviceVersion(ppszData: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_DevicePower(PowerMode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_DevicePower(pPowerMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Calibrate(hEvent: UIntPtr, Mode: Int32, pStatus: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_DevicePort(DevicePort: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_DevicePort(pDevicePort: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMExtTransport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a03cd5f0-3045-11cf-8c-44-00-aa-00-6b-68-14')
    @commethod(3)
    def GetCapability(Capability: Int32, pValue: POINTER(Int32), pdblValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_MediaState(State: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_MediaState(pState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_LocalControl(State: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_LocalControl(pState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetStatus(StatusItem: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransportBasicParameters(Param: Int32, pValue: POINTER(Int32), ppszData: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetTransportBasicParameters(Param: Int32, Value: Int32, pszData: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetTransportVideoParameters(Param: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetTransportVideoParameters(Param: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetTransportAudioParameters(Param: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetTransportAudioParameters(Param: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_Mode(Mode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Mode(pMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Rate(dblRate: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Rate(pdblRate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetChase(pEnabled: POINTER(Int32), pOffset: POINTER(Int32), phEvent: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetChase(Enable: Int32, Offset: Int32, hEvent: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetBump(pSpeed: POINTER(Int32), pDuration: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetBump(Speed: Int32, Duration: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_AntiClogControl(pEnabled: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_AntiClogControl(Enable: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetEditPropertySet(EditID: Int32, pState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def SetEditPropertySet(pEditID: POINTER(Int32), State: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetEditProperty(EditID: Int32, Param: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SetEditProperty(EditID: Int32, Param: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_EditStart(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_EditStart(Value: Int32) -> win32more.Foundation.HRESULT: ...
class IAMExtendedErrorInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa2aa8f6-8b62-11d0-a5-20-00-00-00-00-00-00')
    @commethod(7)
    def get_HasError(pHasError: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ErrorDescription(pbstrErrorDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ErrorCode(pErrorCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMExtendedSeeking(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa2aa8f9-8b62-11d0-a5-20-00-00-00-00-00-00')
    @commethod(7)
    def get_ExSeekCapabilities(pExCapabilities: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_MarkerCount(pMarkerCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentMarker(pCurrentMarker: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetMarkerTime(MarkerNum: Int32, pMarkerTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetMarkerName(MarkerNum: Int32, pbstrMarkerName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_PlaybackSpeed(Speed: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_PlaybackSpeed(pSpeed: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
class IAMFilterGraphCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868fd-0ad4-11ce-b0-a3-00-20-af-0b-a7-70')
    @commethod(3)
    def UnableToRender(pPin: win32more.Media.DirectShow.IPin_head) -> win32more.Foundation.HRESULT: ...
class IAMFilterMiscFlags(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2dd74950-a890-11d1-ab-e8-00-a0-c9-05-f3-75')
    @commethod(3)
    def GetMiscFlags() -> UInt32: ...
class IAMGraphBuilderCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4995f511-9ddb-4f12-bd-3b-f0-46-11-80-7b-79')
    @commethod(3)
    def SelectedFilter(pMon: win32more.System.Com.IMoniker_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreatedFilter(pFil: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
class IAMGraphStreams(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('632105fa-072e-11d3-8a-f9-00-c0-4f-b6-bd-3d')
    @commethod(3)
    def FindUpstreamInterface(pPin: win32more.Media.DirectShow.IPin_head, riid: POINTER(Guid), ppvInterface: POINTER(c_void_p), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SyncUsingStreamOffset(bUseStreamOffset: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxGraphLatency(rtMaxGraphLatency: Int64) -> win32more.Foundation.HRESULT: ...
class IAMLatency(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('62ea93ba-ec62-11d2-b7-70-00-c0-4f-b6-bd-3d')
    @commethod(3)
    def GetLatency(prtLatency: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IAMLine21Decoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6e8d4a21-310c-11d0-b7-9a-00-aa-00-37-67-a7')
    @commethod(3)
    def GetDecoderLevel(lpLevel: POINTER(win32more.Media.DirectShow.AM_LINE21_CCLEVEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentService(lpService: POINTER(win32more.Media.DirectShow.AM_LINE21_CCSERVICE)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetCurrentService(Service: win32more.Media.DirectShow.AM_LINE21_CCSERVICE) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceState(lpState: POINTER(win32more.Media.DirectShow.AM_LINE21_CCSTATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetServiceState(State: win32more.Media.DirectShow.AM_LINE21_CCSTATE) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputFormat(lpbmih: POINTER(win32more.Graphics.Gdi.BITMAPINFOHEADER_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputFormat(lpbmi: POINTER(win32more.Graphics.Gdi.BITMAPINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackgroundColor(pdwPhysColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetBackgroundColor(dwPhysColor: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRedrawAlways(lpbOption: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetRedrawAlways(bOption: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetDrawBackgroundMode(lpMode: POINTER(win32more.Media.DirectShow.AM_LINE21_DRAWBGMODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetDrawBackgroundMode(Mode: win32more.Media.DirectShow.AM_LINE21_DRAWBGMODE) -> win32more.Foundation.HRESULT: ...
class IAMMediaContent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa2aa8f4-8b62-11d0-a5-20-00-00-00-00-00-00')
    @commethod(7)
    def get_AuthorName(pbstrAuthorName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Title(pbstrTitle: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Rating(pbstrRating: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(pbstrDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Copyright(pbstrCopyright: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_BaseURL(pbstrBaseURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_LogoURL(pbstrLogoURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_LogoIconURL(pbstrLogoURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_WatermarkURL(pbstrWatermarkURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_MoreInfoURL(pbstrMoreInfoURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_MoreInfoBannerImage(pbstrMoreInfoBannerImage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_MoreInfoBannerURL(pbstrMoreInfoBannerURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_MoreInfoText(pbstrMoreInfoText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IAMMediaContent2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('ce8f78c1-74d9-11d2-b0-9d-00-a0-c9-a8-11-17')
    @commethod(7)
    def get_MediaParameter(EntryNum: Int32, bstrName: win32more.Foundation.BSTR, pbstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_MediaParameterName(EntryNum: Int32, Index: Int32, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_PlaylistCount(pNumberEntries: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMMediaStream(c_void_p):
    extends: win32more.Media.DirectShow.IMediaStream
    Guid = Guid('bebe595d-9a6f-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(9)
    def Initialize(pSourceObject: win32more.System.Com.IUnknown_head, dwFlags: UInt32, PurposeId: POINTER(Guid), StreamType: win32more.Media.DirectShow.STREAM_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetState(State: win32more.Media.DirectShow.FILTER_STATE) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def JoinAMMultiMediaStream(pAMMultiMediaStream: win32more.Media.DirectShow.IAMMultiMediaStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def JoinFilter(pMediaStreamFilter: win32more.Media.DirectShow.IMediaStreamFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def JoinFilterGraph(pFilterGraph: win32more.Media.DirectShow.IFilterGraph_head) -> win32more.Foundation.HRESULT: ...
class IAMMediaTypeSample(c_void_p):
    extends: win32more.Media.DirectShow.IStreamSample
    Guid = Guid('ab6b4afb-f6e4-11d0-90-0d-00-c0-4f-d9-18-9d')
    @commethod(8)
    def SetPointer(pBuffer: c_char_p_no, lSize: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPointer(ppBuffer: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSize() -> Int32: ...
    @commethod(11)
    def GetTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def IsSyncPoint() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetSyncPoint(bIsSyncPoint: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def IsPreroll() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetPreroll(bIsPreroll: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetActualDataLength() -> Int32: ...
    @commethod(18)
    def SetActualDataLength(__MIDL__IAMMediaTypeSample0000: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetMediaType(ppMediaType: POINTER(POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetMediaType(pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def IsDiscontinuity() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetDiscontinuity(bDiscontinuity: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetMediaTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SetMediaTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IAMMediaTypeStream(c_void_p):
    extends: win32more.Media.DirectShow.IMediaStream
    Guid = Guid('ab6b4afa-f6e4-11d0-90-0d-00-c0-4f-d9-18-9d')
    @commethod(9)
    def GetFormat(pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetFormat(pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSample(lSampleSize: Int32, pbBuffer: c_char_p_no, dwFlags: UInt32, pUnkOuter: win32more.System.Com.IUnknown_head, ppAMMediaTypeSample: POINTER(win32more.Media.DirectShow.IAMMediaTypeSample_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetStreamAllocatorRequirements(pProps: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetStreamAllocatorRequirements(pProps: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
class IAMMultiMediaStream(c_void_p):
    extends: win32more.Media.DirectShow.IMultiMediaStream
    Guid = Guid('bebe595c-9a6f-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(12)
    def Initialize(StreamType: win32more.Media.DirectShow.STREAM_TYPE, dwFlags: win32more.Media.DirectShow.AMMSF_MMS_INIT_FLAGS, pFilterGraph: win32more.Media.DirectShow.IGraphBuilder_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetFilterGraph(ppGraphBuilder: POINTER(win32more.Media.DirectShow.IGraphBuilder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetFilter(ppFilter: POINTER(win32more.Media.DirectShow.IMediaStreamFilter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def AddMediaStream(pStreamObject: win32more.System.Com.IUnknown_head, PurposeId: POINTER(Guid), dwFlags: win32more.Media.DirectShow.AMMSF_MS_FLAGS, ppNewStream: POINTER(win32more.Media.DirectShow.IMediaStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def OpenFile(pszFileName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def OpenMoniker(pCtx: win32more.System.Com.IBindCtx_head, pMoniker: win32more.System.Com.IMoniker_head, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Render(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IAMNetShowConfig(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa2aa8f1-8b62-11d0-a5-20-00-00-00-00-00-00')
    @commethod(7)
    def get_BufferingTime(pBufferingTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_BufferingTime(BufferingTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_UseFixedUDPPort(pUseFixedUDPPort: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_UseFixedUDPPort(UseFixedUDPPort: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_FixedUDPPort(pFixedUDPPort: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_FixedUDPPort(FixedUDPPort: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_UseHTTPProxy(pUseHTTPProxy: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_UseHTTPProxy(UseHTTPProxy: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_EnableAutoProxy(pEnableAutoProxy: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_EnableAutoProxy(EnableAutoProxy: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_HTTPProxyHost(pbstrHTTPProxyHost: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_HTTPProxyHost(bstrHTTPProxyHost: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_HTTPProxyPort(pHTTPProxyPort: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_HTTPProxyPort(HTTPProxyPort: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_EnableMulticast(pEnableMulticast: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_EnableMulticast(EnableMulticast: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_EnableUDP(pEnableUDP: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_EnableUDP(EnableUDP: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_EnableTCP(pEnableTCP: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_EnableTCP(EnableTCP: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_EnableHTTP(pEnableHTTP: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_EnableHTTP(EnableHTTP: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IAMNetShowExProps(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa2aa8f5-8b62-11d0-a5-20-00-00-00-00-00-00')
    @commethod(7)
    def get_SourceProtocol(pSourceProtocol: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Bandwidth(pBandwidth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ErrorCorrection(pbstrErrorCorrection: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_CodecCount(pCodecCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetCodecInstalled(CodecNum: Int32, pCodecInstalled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetCodecDescription(CodecNum: Int32, pbstrCodecDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCodecURL(CodecNum: Int32, pbstrCodecURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_CreationDate(pCreationDate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_SourceLink(pbstrSourceLink: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IAMNetShowPreroll(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('aae7e4e2-6388-11d1-8d-93-00-60-97-c9-a2-b2')
    @commethod(7)
    def put_Preroll(fPreroll: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Preroll(pfPreroll: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IAMNetworkStatus(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa2aa8f3-8b62-11d0-a5-20-00-00-00-00-00-00')
    @commethod(7)
    def get_ReceivedPackets(pReceivedPackets: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_RecoveredPackets(pRecoveredPackets: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_LostPackets(pLostPackets: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReceptionQuality(pReceptionQuality: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_BufferingCount(pBufferingCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsBroadcast(pIsBroadcast: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_BufferingProgress(pBufferingProgress: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMOpenProgress(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8e1c39a1-de53-11cf-aa-63-00-80-c7-44-52-8d')
    @commethod(3)
    def QueryProgress(pllTotal: POINTER(Int64), pllCurrent: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AbortOperation() -> win32more.Foundation.HRESULT: ...
class IAMOverlayFX(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('62fae250-7e65-4460-bf-c9-63-98-b3-22-07-3c')
    @commethod(3)
    def QueryOverlayFXCaps(lpdwOverlayFXCaps: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetOverlayFX(dwOverlayFX: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetOverlayFX(lpdwOverlayFX: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAMParse(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c47a3420-005c-11d2-90-38-00-a0-c9-69-72-98')
    @commethod(3)
    def GetParseTime(prtCurrent: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetParseTime(rtCurrent: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Flush() -> win32more.Foundation.HRESULT: ...
class IAMPhysicalPinInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f938c991-3029-11cf-8c-44-00-aa-00-6b-68-14')
    @commethod(3)
    def GetPhysicalType(pType: POINTER(Int32), ppszType: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IAMPlayList(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868fe-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def GetFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemCount(pdwItems: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetItem(dwItemIndex: UInt32, ppItem: POINTER(win32more.Media.DirectShow.IAMPlayListItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetNamedEvent(pwszEventName: win32more.Foundation.PWSTR, dwItemIndex: UInt32, ppItem: POINTER(win32more.Media.DirectShow.IAMPlayListItem_head), pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRepeatInfo(pdwRepeatCount: POINTER(UInt32), pdwRepeatStart: POINTER(UInt32), pdwRepeatEnd: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAMPlayListItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868ff-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def GetFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceCount(pdwSources: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSourceURL(dwSourceIndex: UInt32, pbstrURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceStart(dwSourceIndex: UInt32, prtStart: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSourceDuration(dwSourceIndex: UInt32, prtDuration: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceStartMarker(dwSourceIndex: UInt32, pdwMarker: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSourceEndMarker(dwSourceIndex: UInt32, pdwMarker: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSourceStartMarkerName(dwSourceIndex: UInt32, pbstrStartMarker: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSourceEndMarkerName(dwSourceIndex: UInt32, pbstrEndMarker: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetLinkURL(pbstrURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetScanDuration(dwSourceIndex: UInt32, prtScanDuration: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IAMPluginControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0e26a181-f40c-4635-87-86-97-62-84-b5-29-81')
    @commethod(3)
    def GetPreferredClsid(subType: POINTER(Guid), clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPreferredClsidByIndex(index: UInt32, subType: POINTER(Guid), clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetPreferredClsid(subType: POINTER(Guid), clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsDisabled(clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDisabledByIndex(index: UInt32, clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDisabled(clsid: POINTER(Guid), disabled: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def IsLegacyDisabled(dllName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IAMPushSource(c_void_p):
    extends: win32more.Media.DirectShow.IAMLatency
    Guid = Guid('f185fe76-e64e-11d2-b7-6e-00-c0-4f-b6-bd-3d')
    @commethod(4)
    def GetPushSourceFlags(pFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetPushSourceFlags(Flags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetStreamOffset(rtOffset: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetStreamOffset(prtOffset: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetMaxStreamOffset(prtMaxOffset: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetMaxStreamOffset(rtMaxOffset: Int64) -> win32more.Foundation.HRESULT: ...
class IAMRebuild(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('02ef04dd-7580-11d1-be-ce-00-c0-4f-b6-e9-37')
    @commethod(3)
    def RebuildNow() -> win32more.Foundation.HRESULT: ...
class IAMResourceControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8389d2d0-77d7-11d1-ab-e6-00-a0-c9-05-f3-75')
    @commethod(3)
    def Reserve(dwFlags: UInt32, pvReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
class IAMStats(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('bc9bcf80-dcd2-11d2-ab-f6-00-a0-c9-05-f3-75')
    @commethod(7)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetValueByIndex(lIndex: Int32, szName: POINTER(win32more.Foundation.BSTR), lCount: POINTER(Int32), dLast: POINTER(Double), dAverage: POINTER(Double), dStdDev: POINTER(Double), dMin: POINTER(Double), dMax: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetValueByName(szName: win32more.Foundation.BSTR, lIndex: POINTER(Int32), lCount: POINTER(Int32), dLast: POINTER(Double), dAverage: POINTER(Double), dStdDev: POINTER(Double), dMin: POINTER(Double), dMax: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetIndex(szName: win32more.Foundation.BSTR, lCreate: Int32, plIndex: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def AddValue(lIndex: Int32, dValue: Double) -> win32more.Foundation.HRESULT: ...
class IAMStreamConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e13340-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def SetFormat(pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormat(ppmt: POINTER(POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfCapabilities(piCount: POINTER(Int32), piSize: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamCaps(iIndex: Int32, ppmt: POINTER(POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)), pSCC: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IAMStreamControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('36b73881-c2c8-11cf-8b-46-00-80-5f-6c-ef-60')
    @commethod(3)
    def StartAt(ptStart: POINTER(Int64), dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def StopAt(ptStop: POINTER(Int64), bSendExtra: win32more.Foundation.BOOL, dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetInfo(pInfo: POINTER(win32more.Media.DirectShow.AM_STREAM_INFO_head)) -> win32more.Foundation.HRESULT: ...
class IAMStreamSelect(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c1960960-17f5-11d1-ab-e1-00-a0-c9-05-f3-75')
    @commethod(3)
    def Count(pcStreams: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Info(lIndex: Int32, ppmt: POINTER(POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)), pdwFlags: POINTER(UInt32), plcid: POINTER(UInt32), pdwGroup: POINTER(UInt32), ppszName: POINTER(win32more.Foundation.PWSTR), ppObject: POINTER(win32more.System.Com.IUnknown_head), ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Enable(lIndex: Int32, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IAMTVAudio(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('83ec1c30-23d1-11d1-99-e6-00-a0-c9-56-02-66')
    @commethod(3)
    def GetHardwareSupportedTVAudioModes(plModes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAvailableTVAudioModes(plModes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_TVAudioMode(plMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_TVAudioMode(lMode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterNotificationCallBack(pNotify: win32more.Media.DirectShow.IAMTunerNotification_head, lEvents: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def UnRegisterNotificationCallBack(pNotify: win32more.Media.DirectShow.IAMTunerNotification_head) -> win32more.Foundation.HRESULT: ...
class IAMTVAudioNotification(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('83ec1c33-23d1-11d1-99-e6-00-a0-c9-56-02-66')
    @commethod(3)
    def OnEvent(Event: win32more.Media.DirectShow.AMTVAudioEventType) -> win32more.Foundation.HRESULT: ...
class IAMTVTuner(c_void_p):
    extends: win32more.Media.DirectShow.IAMTuner
    Guid = Guid('211a8766-03ac-11d1-8d-13-00-aa-00-bd-83-39')
    @commethod(18)
    def get_AvailableTVFormats(lAnalogVideoStandard: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_TVFormat(plAnalogVideoStandard: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def AutoTune(lChannel: Int32, plFoundSignal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def StoreAutoTune() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_NumInputConnections(plNumInputConnections: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_InputType(lIndex: Int32, InputType: win32more.Media.DirectShow.TunerInputType) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_InputType(lIndex: Int32, pInputType: POINTER(win32more.Media.DirectShow.TunerInputType)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_ConnectInput(lIndex: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ConnectInput(plIndex: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_VideoFrequency(lFreq: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_AudioFrequency(lFreq: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMTimecodeDisplay(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b496ce2-811b-11cf-8c-77-00-aa-00-6b-68-14')
    @commethod(3)
    def GetTCDisplayEnable(pState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTCDisplayEnable(State: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTCDisplay(Param: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetTCDisplay(Param: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
class IAMTimecodeGenerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b496ce0-811b-11cf-8c-77-00-aa-00-6b-68-14')
    @commethod(3)
    def GetTCGMode(Param: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTCGMode(Param: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_VITCLine(Line: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_VITCLine(pLine: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetTimecode(pTimecodeSample: POINTER(win32more.Media.TIMECODE_SAMPLE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTimecode(pTimecodeSample: POINTER(win32more.Media.TIMECODE_SAMPLE_head)) -> win32more.Foundation.HRESULT: ...
class IAMTimecodeReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b496ce1-811b-11cf-8c-77-00-aa-00-6b-68-14')
    @commethod(3)
    def GetTCRMode(Param: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTCRMode(Param: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_VITCLine(Line: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_VITCLine(pLine: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTimecode(pTimecodeSample: POINTER(win32more.Media.TIMECODE_SAMPLE_head)) -> win32more.Foundation.HRESULT: ...
class IAMTuner(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('211a8761-03ac-11d1-8d-13-00-aa-00-bd-83-39')
    @commethod(3)
    def put_Channel(lChannel: Int32, lVideoSubChannel: Int32, lAudioSubChannel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Channel(plChannel: POINTER(Int32), plVideoSubChannel: POINTER(Int32), plAudioSubChannel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ChannelMinMax(lChannelMin: POINTER(Int32), lChannelMax: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_CountryCode(lCountryCode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_CountryCode(plCountryCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_TuningSpace(lTuningSpace: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_TuningSpace(plTuningSpace: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Logon(hCurrentUser: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Logout() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SignalPresent(plSignalStrength: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Mode(lMode: win32more.Media.DirectShow.AMTunerModeType) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Mode(plMode: POINTER(win32more.Media.DirectShow.AMTunerModeType)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetAvailableModes(plModes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterNotificationCallBack(pNotify: win32more.Media.DirectShow.IAMTunerNotification_head, lEvents: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def UnRegisterNotificationCallBack(pNotify: win32more.Media.DirectShow.IAMTunerNotification_head) -> win32more.Foundation.HRESULT: ...
class IAMTunerNotification(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('211a8760-03ac-11d1-8d-13-00-aa-00-bd-83-39')
    @commethod(3)
    def OnEvent(Event: win32more.Media.DirectShow.AMTunerEventType) -> win32more.Foundation.HRESULT: ...
class IAMVfwCaptureDialogs(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d8d715a0-6e5e-11d0-b3-f0-00-aa-00-37-61-c5')
    @commethod(3)
    def HasDialog(iDialog: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ShowDialog(iDialog: Int32, hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SendDriverMessage(iDialog: Int32, uMsg: Int32, dw1: Int32, dw2: Int32) -> win32more.Foundation.HRESULT: ...
class IAMVfwCompressDialogs(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d8d715a3-6e5e-11d0-b3-f0-00-aa-00-37-61-c5')
    @commethod(3)
    def ShowDialog(iDialog: Int32, hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetState(pState: c_void_p, pcbState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetState(pState: c_void_p, cbState: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SendDriverMessage(uMsg: Int32, dw1: Int32, dw2: Int32) -> win32more.Foundation.HRESULT: ...
class IAMVideoAccelerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('256a6a22-fbad-11d1-82-bf-00-a0-c9-69-6c-8f')
    @commethod(3)
    def GetVideoAcceleratorGUIDs(pdwNumGuidsSupported: POINTER(UInt32), pGuidsSupported: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetUncompFormatsSupported(pGuid: POINTER(Guid), pdwNumFormatsSupported: POINTER(UInt32), pFormatsSupported: POINTER(win32more.Graphics.DirectDraw.DDPIXELFORMAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetInternalMemInfo(pGuid: POINTER(Guid), pamvaUncompDataInfo: POINTER(win32more.Media.DirectShow.AMVAUncompDataInfo_head), pamvaInternalMemInfo: POINTER(win32more.Media.DirectShow.AMVAInternalMemInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCompBufferInfo(pGuid: POINTER(Guid), pamvaUncompDataInfo: POINTER(win32more.Media.DirectShow.AMVAUncompDataInfo_head), pdwNumTypesCompBuffers: POINTER(UInt32), pamvaCompBufferInfo: POINTER(win32more.Media.DirectShow.AMVACompBufferInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetInternalCompBufferInfo(pdwNumTypesCompBuffers: POINTER(UInt32), pamvaCompBufferInfo: POINTER(win32more.Media.DirectShow.AMVACompBufferInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def BeginFrame(amvaBeginFrameInfo: POINTER(win32more.Media.DirectShow.AMVABeginFrameInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EndFrame(pEndFrameInfo: POINTER(win32more.Media.DirectShow.AMVAEndFrameInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetBuffer(dwTypeIndex: UInt32, dwBufferIndex: UInt32, bReadOnly: win32more.Foundation.BOOL, ppBuffer: POINTER(c_void_p), lpStride: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ReleaseBuffer(dwTypeIndex: UInt32, dwBufferIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Execute(dwFunction: UInt32, lpPrivateInputData: c_void_p, cbPrivateInputData: UInt32, lpPrivateOutputDat: c_void_p, cbPrivateOutputData: UInt32, dwNumBuffers: UInt32, pamvaBufferInfo: POINTER(win32more.Media.DirectShow.AMVABUFFERINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def QueryRenderStatus(dwTypeIndex: UInt32, dwBufferIndex: UInt32, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def DisplayFrame(dwFlipToIndex: UInt32, pMediaSample: win32more.Media.DirectShow.IMediaSample_head) -> win32more.Foundation.HRESULT: ...
class IAMVideoAcceleratorNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('256a6a21-fbad-11d1-82-bf-00-a0-c9-69-6c-8f')
    @commethod(3)
    def GetUncompSurfacesInfo(pGuid: POINTER(Guid), pUncompBufferInfo: POINTER(win32more.Media.DirectShow.AMVAUncompBufferInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetUncompSurfacesInfo(dwActualUncompSurfacesAllocated: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCreateVideoAcceleratorData(pGuid: POINTER(Guid), pdwSizeMiscData: POINTER(UInt32), ppMiscData: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IAMVideoCompression(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e13343-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def put_KeyFrameRate(KeyFrameRate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_KeyFrameRate(pKeyFrameRate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_PFramesPerKeyFrame(PFramesPerKeyFrame: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_PFramesPerKeyFrame(pPFramesPerKeyFrame: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_Quality(Quality: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Quality(pQuality: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_WindowSize(WindowSize: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_WindowSize(pWindowSize: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetInfo(pszVersion: win32more.Foundation.PWSTR, pcbVersion: POINTER(Int32), pszDescription: win32more.Foundation.PWSTR, pcbDescription: POINTER(Int32), pDefaultKeyFrameRate: POINTER(Int32), pDefaultPFramesPerKey: POINTER(Int32), pDefaultQuality: POINTER(Double), pCapabilities: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def OverrideKeyFrame(FrameNumber: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def OverrideFrameSize(FrameNumber: Int32, Size: Int32) -> win32more.Foundation.HRESULT: ...
class IAMVideoControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6a2e0670-28e4-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def GetCaps(pPin: win32more.Media.DirectShow.IPin_head, pCapsFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetMode(pPin: win32more.Media.DirectShow.IPin_head, Mode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMode(pPin: win32more.Media.DirectShow.IPin_head, Mode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentActualFrameRate(pPin: win32more.Media.DirectShow.IPin_head, ActualFrameRate: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxAvailableFrameRate(pPin: win32more.Media.DirectShow.IPin_head, iIndex: Int32, Dimensions: win32more.Foundation.SIZE, MaxAvailableFrameRate: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFrameRateList(pPin: win32more.Media.DirectShow.IPin_head, iIndex: Int32, Dimensions: win32more.Foundation.SIZE, ListSize: POINTER(Int32), FrameRates: POINTER(POINTER(Int64))) -> win32more.Foundation.HRESULT: ...
class IAMVideoDecimationProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('60d32930-13da-11d3-9e-c6-c4-fc-ae-f5-c7-be')
    @commethod(3)
    def QueryDecimationUsage(lpUsage: POINTER(win32more.Media.DirectShow.DECIMATION_USAGE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetDecimationUsage(Usage: win32more.Media.DirectShow.DECIMATION_USAGE) -> win32more.Foundation.HRESULT: ...
class IAMVideoProcAmp(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6e13360-30ac-11d0-a1-8c-00-a0-c9-11-89-56')
    @commethod(3)
    def GetRange(Property: Int32, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Set(Property: Int32, lValue: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Get(Property: Int32, lValue: POINTER(Int32), Flags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IAMWMBufferPass(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6dd816d7-e740-4123-9e-24-24-44-41-26-44-d8')
    @commethod(3)
    def SetNotify(pCallback: win32more.Media.DirectShow.IAMWMBufferPassCallback_head) -> win32more.Foundation.HRESULT: ...
class IAMWMBufferPassCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b25b8372-d2d2-44b2-86-53-1b-8d-ae-33-24-89')
    @commethod(3)
    def Notify(pNSSBuffer3: win32more.Media.WindowsMediaFormat.INSSBuffer3_head, pPin: win32more.Media.DirectShow.IPin_head, prtStart: POINTER(Int64), prtEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IAMWstDecoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c056de21-75c2-11d3-a1-84-00-10-5a-ef-9f-33')
    @commethod(3)
    def GetDecoderLevel(lpLevel: POINTER(win32more.Media.DirectShow.AM_WST_LEVEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentService(lpService: POINTER(win32more.Media.DirectShow.AM_WST_SERVICE)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceState(lpState: POINTER(win32more.Media.DirectShow.AM_WST_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetServiceState(State: win32more.Media.DirectShow.AM_WST_STATE) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputFormat(lpbmih: POINTER(win32more.Graphics.Gdi.BITMAPINFOHEADER_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetOutputFormat(lpbmi: POINTER(win32more.Graphics.Gdi.BITMAPINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetBackgroundColor(pdwPhysColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetBackgroundColor(dwPhysColor: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRedrawAlways(lpbOption: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetRedrawAlways(bOption: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDrawBackgroundMode(lpMode: POINTER(win32more.Media.DirectShow.AM_WST_DRAWBGMODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetDrawBackgroundMode(Mode: win32more.Media.DirectShow.AM_WST_DRAWBGMODE) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetAnswerMode(bAnswer: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetAnswerMode(pbAnswer: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetHoldPage(bHoldPage: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetHoldPage(pbHoldPage: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetCurrentPage(pWstPage: POINTER(win32more.Media.DirectShow.AM_WST_PAGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetCurrentPage(WstPage: win32more.Media.DirectShow.AM_WST_PAGE) -> win32more.Foundation.HRESULT: ...
class IAMovieSetup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a3d8cec0-7e5a-11cf-bb-c5-00-80-5f-6c-ef-20')
    @commethod(3)
    def Register() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister() -> win32more.Foundation.HRESULT: ...
class IATSCChannelTuneRequest(c_void_p):
    extends: win32more.Media.DirectShow.IChannelTuneRequest
    Guid = Guid('0369b4e1-45b6-11d3-b6-50-00-c0-4f-79-49-8e')
    @commethod(14)
    def get_MinorChannel(MinorChannel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_MinorChannel(MinorChannel: Int32) -> win32more.Foundation.HRESULT: ...
class IATSCComponentType(c_void_p):
    extends: win32more.Media.DirectShow.IMPEG2ComponentType
    Guid = Guid('fc189e4d-7bd4-4125-b3-b3-3a-76-a3-32-cc-96')
    @commethod(28)
    def get_Flags(Flags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Flags(flags: Int32) -> win32more.Foundation.HRESULT: ...
class IATSCLocator(c_void_p):
    extends: win32more.Media.DirectShow.IDigitalLocator
    Guid = Guid('bf8d986f-8c2b-4131-94-d7-4d-3d-9f-cc-21-ef')
    @commethod(22)
    def get_PhysicalChannel(PhysicalChannel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_PhysicalChannel(PhysicalChannel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_TSID(TSID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_TSID(TSID: Int32) -> win32more.Foundation.HRESULT: ...
class IATSCLocator2(c_void_p):
    extends: win32more.Media.DirectShow.IATSCLocator
    Guid = Guid('612aa885-66cf-4090-ba-0a-56-6f-53-12-e4-ca')
    @commethod(26)
    def get_ProgramNumber(ProgramNumber: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_ProgramNumber(ProgramNumber: Int32) -> win32more.Foundation.HRESULT: ...
class IATSCTuningSpace(c_void_p):
    extends: win32more.Media.DirectShow.IAnalogTVTuningSpace
    Guid = Guid('0369b4e2-45b6-11d3-b6-50-00-c0-4f-79-49-8e')
    @commethod(34)
    def get_MinMinorChannel(MinMinorChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_MinMinorChannel(NewMinMinorChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_MaxMinorChannel(MaxMinorChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_MaxMinorChannel(NewMaxMinorChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_MinPhysicalChannel(MinPhysicalChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_MinPhysicalChannel(NewMinPhysicalChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_MaxPhysicalChannel(MaxPhysicalChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_MaxPhysicalChannel(NewMaxPhysicalChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
class IATSC_EIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d7c212d7-76a2-4b4b-aa-56-84-68-79-a8-00-96')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSourceId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetProtocolVersion(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordEventId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordStartTime(dwRecordIndex: UInt32, pmdtVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordEtmLocation(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordDuration(dwRecordIndex: UInt32, pmdVal: POINTER(win32more.Media.DirectShow.MPEG_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordTitleText(dwRecordIndex: UInt32, pdwLength: POINTER(UInt32), ppText: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
class IATSC_ETT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5a142cc9-b8cf-4a86-a0-40-e9-ca-df-3e-f3-e7')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetProtocolVersion(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEtmId(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetExtendedMessageText(pdwLength: POINTER(UInt32), ppText: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IATSC_MGT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8877dabd-c137-4073-97-e3-77-94-07-a5-d8-7a')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetProtocolVersion(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordType(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordTypePid(dwRecordIndex: UInt32, ppidVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordVersionNumber(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
class IATSC_STT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6bf42423-217d-4d6f-81-e1-3a-7b-36-0e-c8-96')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProtocolVersion(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSystemTime(pmdtSystemTime: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetGpsUtcOffset(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDaylightSavings(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
class IATSC_VCT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('26879a18-32f9-46c6-91-f0-fb-64-79-27-0e-8c')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransportStreamId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetProtocolVersion(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordName(dwRecordIndex: UInt32, pwsName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordMajorChannelNumber(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordMinorChannelNumber(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordModulationMode(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCarrierFrequency(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordTransportStreamId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordProgramNumber(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordEtmLocation(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordIsAccessControlledBitSet(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordIsHiddenBitSet(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecordIsPathSelectBitSet(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetRecordIsOutOfBandBitSet(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetRecordIsHideGuideBitSet(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetRecordServiceType(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetRecordSourceId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
class IAnalogAudioComponentType(c_void_p):
    extends: win32more.Media.DirectShow.IComponentType
    Guid = Guid('2cfeb2a8-1787-4a24-a9-41-c6-ea-ec-39-c8-42')
    @commethod(24)
    def get_AnalogAudioMode(Mode: POINTER(win32more.Media.DirectShow.TVAudioMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_AnalogAudioMode(Mode: win32more.Media.DirectShow.TVAudioMode) -> win32more.Foundation.HRESULT: ...
class IAnalogLocator(c_void_p):
    extends: win32more.Media.DirectShow.ILocator
    Guid = Guid('34d1f26b-e339-430d-ab-ce-73-8c-b4-89-84-dc')
    @commethod(22)
    def get_VideoStandard(AVS: POINTER(win32more.Media.DirectShow.AnalogVideoStandard)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_VideoStandard(AVS: win32more.Media.DirectShow.AnalogVideoStandard) -> win32more.Foundation.HRESULT: ...
class IAnalogRadioTuningSpace(c_void_p):
    extends: win32more.Media.DirectShow.ITuningSpace
    Guid = Guid('2a6e293b-2595-11d3-b6-4c-00-c0-4f-79-49-8e')
    @commethod(26)
    def get_MinFrequency(MinFrequencyVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_MinFrequency(NewMinFrequencyVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_MaxFrequency(MaxFrequencyVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_MaxFrequency(NewMaxFrequencyVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_Step(StepVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_Step(NewStepVal: Int32) -> win32more.Foundation.HRESULT: ...
class IAnalogRadioTuningSpace2(c_void_p):
    extends: win32more.Media.DirectShow.IAnalogRadioTuningSpace
    Guid = Guid('39dd45da-2da8-46ba-8a-8a-87-e2-b7-3d-98-3a')
    @commethod(32)
    def get_CountryCode(CountryCodeVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_CountryCode(NewCountryCodeVal: Int32) -> win32more.Foundation.HRESULT: ...
class IAnalogTVTuningSpace(c_void_p):
    extends: win32more.Media.DirectShow.ITuningSpace
    Guid = Guid('2a6e293c-2595-11d3-b6-4c-00-c0-4f-79-49-8e')
    @commethod(26)
    def get_MinChannel(MinChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_MinChannel(NewMinChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_MaxChannel(MaxChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_MaxChannel(NewMaxChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_InputType(InputTypeVal: POINTER(win32more.Media.DirectShow.TunerInputType)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_InputType(NewInputTypeVal: win32more.Media.DirectShow.TunerInputType) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_CountryCode(CountryCodeVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_CountryCode(NewCountryCodeVal: Int32) -> win32more.Foundation.HRESULT: ...
class IAsyncReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868aa-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def RequestAllocator(pPreferred: win32more.Media.DirectShow.IMemAllocator_head, pProps: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head), ppActual: POINTER(win32more.Media.DirectShow.IMemAllocator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Request(pSample: win32more.Media.DirectShow.IMediaSample_head, dwUser: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def WaitForNext(dwTimeout: UInt32, ppSample: POINTER(win32more.Media.DirectShow.IMediaSample_head), pdwUser: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SyncReadAligned(pSample: win32more.Media.DirectShow.IMediaSample_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SyncRead(llPosition: Int64, lLength: Int32, pBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Length(pTotal: POINTER(Int64), pAvailable: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def BeginFlush() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EndFlush() -> win32more.Foundation.HRESULT: ...
class IAtscContentAdvisoryDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ff76e60c-0283-43ea-ba-32-b4-22-23-85-47-ee')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRatingRegionCount(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordRatingRegion(bIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordRatedDimensions(bIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordRatingDimension(bIndexOuter: Byte, bIndexInner: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordRatingValue(bIndexOuter: Byte, bIndexInner: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordRatingDescriptionText(bIndex: Byte, pbLength: c_char_p_no, ppText: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IAtscPsipParser(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b2c98995-5eb2-4fb1-b4-06-f3-e8-e2-02-6a-9a')
    @commethod(3)
    def Initialize(punkMpeg2Data: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPAT(ppPAT: POINTER(win32more.Media.DirectShow.IPAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCAT(dwTimeout: UInt32, ppCAT: POINTER(win32more.Media.DirectShow.ICAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPMT(pid: UInt16, pwProgramNumber: POINTER(UInt16), ppPMT: POINTER(win32more.Media.DirectShow.IPMT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTSDT(ppTSDT: POINTER(win32more.Media.DirectShow.ITSDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetMGT(ppMGT: POINTER(win32more.Media.DirectShow.IATSC_MGT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetVCT(tableId: Byte, fGetNextTable: win32more.Foundation.BOOL, ppVCT: POINTER(win32more.Media.DirectShow.IATSC_VCT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetEIT(pid: UInt16, pwSourceId: POINTER(UInt16), dwTimeout: UInt32, ppEIT: POINTER(win32more.Media.DirectShow.IATSC_EIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetETT(pid: UInt16, wSourceId: POINTER(UInt16), pwEventId: POINTER(UInt16), ppETT: POINTER(win32more.Media.DirectShow.IATSC_ETT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetSTT(ppSTT: POINTER(win32more.Media.DirectShow.IATSC_STT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetEAS(pid: UInt16, ppEAS: POINTER(win32more.Media.DirectShow.ISCTE_EAS_head)) -> win32more.Foundation.HRESULT: ...
class IAttributeGet(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('52dbd1ec-e48f-4528-92-32-f4-42-a6-8f-0a-e1')
    @commethod(3)
    def GetCount(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttribIndexed(lIndex: Int32, pguidAttribute: POINTER(Guid), pbAttribute: c_char_p_no, pdwAttributeLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttrib(guidAttribute: Guid, pbAttribute: c_char_p_no, pdwAttributeLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAttributeSet(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('583ec3cc-4960-4857-98-2b-41-a3-3e-a0-a0-06')
    @commethod(3)
    def SetAttrib(guidAttribute: Guid, pbAttribute: c_char_p_no, dwAttributeLength: UInt32) -> win32more.Foundation.HRESULT: ...
class IAudioData(c_void_p):
    extends: win32more.Media.DirectShow.IMemoryData
    Guid = Guid('54c719c0-af60-11d0-82-12-00-c0-4f-c3-2c-45')
    @commethod(6)
    def GetFormat(pWaveFormatCurrent: POINTER(win32more.Media.Audio.WAVEFORMATEX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetFormat(lpWaveFormat: POINTER(win32more.Media.Audio.WAVEFORMATEX_head)) -> win32more.Foundation.HRESULT: ...
class IAudioMediaStream(c_void_p):
    extends: win32more.Media.DirectShow.IMediaStream
    Guid = Guid('f7537560-a3be-11d0-82-12-00-c0-4f-c3-2c-45')
    @commethod(9)
    def GetFormat(pWaveFormatCurrent: POINTER(win32more.Media.Audio.WAVEFORMATEX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetFormat(lpWaveFormat: POINTER(win32more.Media.Audio.WAVEFORMATEX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSample(pAudioData: win32more.Media.DirectShow.IAudioData_head, dwFlags: UInt32, ppSample: POINTER(win32more.Media.DirectShow.IAudioStreamSample_head)) -> win32more.Foundation.HRESULT: ...
class IAudioStreamSample(c_void_p):
    extends: win32more.Media.DirectShow.IStreamSample
    Guid = Guid('345fee00-aba5-11d0-82-12-00-c0-4f-c3-2c-45')
    @commethod(8)
    def GetAudioData(ppAudio: POINTER(win32more.Media.DirectShow.IAudioData_head)) -> win32more.Foundation.HRESULT: ...
class IAuxInTuningSpace(c_void_p):
    extends: win32more.Media.DirectShow.ITuningSpace
    Guid = Guid('e48244b8-7e17-4f76-a7-63-50-90-ff-1e-2f-30')
class IAuxInTuningSpace2(c_void_p):
    extends: win32more.Media.DirectShow.IAuxInTuningSpace
    Guid = Guid('b10931ed-8bfe-4ab0-9d-ce-e4-69-c2-9a-97-29')
    @commethod(26)
    def get_CountryCode(CountryCodeVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_CountryCode(NewCountryCodeVal: Int32) -> win32more.Foundation.HRESULT: ...
class IBDAComparable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b34505e0-2f0e-497b-80-bc-d4-3f-3b-24-ed-7f')
    @commethod(3)
    def CompareExact(CompareTo: win32more.System.Com.IDispatch_head, Result: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CompareEquivalent(CompareTo: win32more.System.Com.IDispatch_head, dwFlags: UInt32, Result: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def HashExact(Result: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def HashExactIncremental(PartialResult: Int64, Result: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def HashEquivalent(dwFlags: UInt32, Result: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def HashEquivalentIncremental(PartialResult: Int64, dwFlags: UInt32, Result: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IBDACreateTuneRequestEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0a4a1d4-2b3c-491a-ba-22-49-9f-ba-dd-4d-12')
    @commethod(3)
    def CreateTuneRequestEx(TuneRequestIID: POINTER(Guid), TuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
class IBDA_AUX(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7def4c09-6e66-4567-a8-19-f0-e1-7f-4a-81-ab')
    @commethod(3)
    def QueryCapabilities(pdwNumAuxInputsBSTR: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumCapability(dwIndex: UInt32, dwInputID: POINTER(UInt32), pConnectorType: POINTER(Guid), ConnTypeNum: POINTER(UInt32), NumVideoStds: POINTER(UInt32), AnalogStds: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class IBDA_AutoDemodulate(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ddf15b12-bd25-11d2-9c-a0-00-c0-4f-79-71-e0')
    @commethod(3)
    def put_AutoDemodulate() -> win32more.Foundation.HRESULT: ...
class IBDA_AutoDemodulateEx(c_void_p):
    extends: win32more.Media.DirectShow.IBDA_AutoDemodulate
    Guid = Guid('34518d13-1182-48e6-b2-8f-b2-49-87-78-73-26')
    @commethod(4)
    def get_SupportedDeviceNodeTypes(ulcDeviceNodeTypesMax: UInt32, pulcDeviceNodeTypes: POINTER(UInt32), pguidDeviceNodeTypes: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_SupportedVideoFormats(pulAMTunerModeType: POINTER(UInt32), pulAnalogVideoStandard: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_AuxInputCount(pulCompositeCount: POINTER(UInt32), pulSvideoCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_ConditionalAccess(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('cd51f1e0-7be9-4123-84-82-a2-a7-96-c0-a6-b0')
    @commethod(3)
    def get_SmartCardStatus(pCardStatus: POINTER(win32more.Media.DirectShow.SmartCardStatusType), pCardAssociation: POINTER(win32more.Media.DirectShow.SmartCardAssociationType), pbstrCardError: POINTER(win32more.Foundation.BSTR), pfOOBLocked: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_SmartCardInfo(pbstrCardName: POINTER(win32more.Foundation.BSTR), pbstrCardManufacturer: POINTER(win32more.Foundation.BSTR), pfDaylightSavings: POINTER(win32more.Foundation.VARIANT_BOOL), pbyRatingRegion: c_char_p_no, plTimeZoneOffsetMinutes: POINTER(Int32), pbstrLanguage: POINTER(win32more.Foundation.BSTR), pEALocationCode: POINTER(win32more.Media.DirectShow.EALocationCodeType_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_SmartCardApplications(pulcApplications: POINTER(UInt32), ulcApplicationsMax: UInt32, rgApplications: POINTER(win32more.Media.DirectShow.SmartCardApplication_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Entitlement(usVirtualChannel: UInt16, pEntitlement: POINTER(win32more.Media.DirectShow.EntitlementType)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def TuneByChannel(usVirtualChannel: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetProgram(usProgramNumber: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddProgram(usProgramNumber: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveProgram(usProgramNumber: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetModuleUI(byDialogNumber: Byte, pbstrURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def InformUIClosed(byDialogNumber: Byte, CloseReason: win32more.Media.DirectShow.UICloseReasonType) -> win32more.Foundation.HRESULT: ...
class IBDA_ConditionalAccessEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('497c3418-23cb-44ba-bb-62-76-9f-50-6f-ce-a7')
    @commethod(3)
    def CheckEntitlementToken(ulDialogRequest: UInt32, bstrLanguage: win32more.Foundation.BSTR, RequestType: win32more.Media.DirectShow.BDA_CONDITIONALACCESS_REQUESTTYPE, ulcbEntitlementTokenLen: UInt32, pbEntitlementToken: c_char_p_no, pulDescrambleStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetCaptureToken(ulcbCaptureTokenLen: UInt32, pbCaptureToken: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OpenBroadcastMmi(ulDialogRequest: UInt32, bstrLanguage: win32more.Foundation.BSTR, EventId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CloseMmiDialog(ulDialogRequest: UInt32, bstrLanguage: win32more.Foundation.BSTR, ulDialogNumber: UInt32, ReasonCode: win32more.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON, pulSessionResult: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDialogRequestNumber(pulDialogRequestNumber: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_DRIDRMService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1f9bc2a5-44a3-4c52-aa-b1-0b-bc-e5-a1-38-1d')
    @commethod(3)
    def SetDRM(bstrNewDrm: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDRMStatus(pbstrDrmUuidList: POINTER(win32more.Foundation.BSTR), DrmUuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPairingStatus(penumPairingStatus: POINTER(win32more.Media.DirectShow.BDA_DrmPairingError)) -> win32more.Foundation.HRESULT: ...
class IBDA_DRIWMDRMSession(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('05c690f8-56db-4bb2-b0-53-79-c1-20-98-bb-26')
    @commethod(3)
    def AcknowledgeLicense(hrLicenseAck: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessLicenseChallenge(dwcbLicenseMessage: UInt32, pbLicenseMessage: c_char_p_no, pdwcbLicenseResponse: POINTER(UInt32), ppbLicenseResponse: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ProcessRegistrationChallenge(dwcbRegistrationMessage: UInt32, pbRegistrationMessage: c_char_p_no, pdwcbRegistrationResponse: POINTER(UInt32), ppbRegistrationResponse: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetRevInfo(dwRevInfoLen: UInt32, pbRevInfo: c_char_p_no, pdwResponse: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetCrl(dwCrlLen: UInt32, pbCrlLen: c_char_p_no, pdwResponse: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetHMSAssociationData() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastCardeaError(pdwError: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_DRM(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f98d88b0-1992-4cd6-a6-d9-b9-af-ab-99-33-0d')
    @commethod(3)
    def GetDRMPairingStatus(pdwStatus: POINTER(UInt32), phError: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PerformDRMPairing(fSync: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IBDA_DRMService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bff6b5bb-b0ae-484c-9d-ca-73-52-8f-b0-b4-6e')
    @commethod(3)
    def SetDRM(puuidNewDrm: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDRMStatus(pbstrDrmUuidList: POINTER(win32more.Foundation.BSTR), DrmUuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IBDA_DeviceControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fd0a5af3-b41d-11d2-9c-95-00-c0-4f-79-71-e0')
    @commethod(3)
    def StartChanges() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CheckChanges() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CommitChanges() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeState(pState: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_DiagnosticProperties(c_void_p):
    extends: win32more.System.Com.StructuredStorage.IPropertyBag
    Guid = Guid('20e80cb5-c543-4c1b-8e-b3-49-e7-19-ee-e7-d4')
class IBDA_DigitalDemodulator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ef30f379-985b-4d10-b6-40-a7-9d-5e-04-e1-e0')
    @commethod(3)
    def put_ModulationType(pModulationType: POINTER(win32more.Media.DirectShow.ModulationType)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_ModulationType(pModulationType: POINTER(win32more.Media.DirectShow.ModulationType)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_InnerFECMethod(pFECMethod: POINTER(win32more.Media.DirectShow.FECMethod)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_InnerFECMethod(pFECMethod: POINTER(win32more.Media.DirectShow.FECMethod)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_InnerFECRate(pFECRate: POINTER(win32more.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_InnerFECRate(pFECRate: POINTER(win32more.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_OuterFECMethod(pFECMethod: POINTER(win32more.Media.DirectShow.FECMethod)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_OuterFECMethod(pFECMethod: POINTER(win32more.Media.DirectShow.FECMethod)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_OuterFECRate(pFECRate: POINTER(win32more.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_OuterFECRate(pFECRate: POINTER(win32more.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_SymbolRate(pSymbolRate: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_SymbolRate(pSymbolRate: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_SpectralInversion(pSpectralInversion: POINTER(win32more.Media.DirectShow.SpectralInversion)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_SpectralInversion(pSpectralInversion: POINTER(win32more.Media.DirectShow.SpectralInversion)) -> win32more.Foundation.HRESULT: ...
class IBDA_DigitalDemodulator2(c_void_p):
    extends: win32more.Media.DirectShow.IBDA_DigitalDemodulator
    Guid = Guid('525ed3ee-5cf3-4e1e-9a-06-53-68-a8-4f-9a-6e')
    @commethod(17)
    def put_GuardInterval(pGuardInterval: POINTER(win32more.Media.DirectShow.GuardInterval)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_GuardInterval(pGuardInterval: POINTER(win32more.Media.DirectShow.GuardInterval)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_TransmissionMode(pTransmissionMode: POINTER(win32more.Media.DirectShow.TransmissionMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionMode(pTransmissionMode: POINTER(win32more.Media.DirectShow.TransmissionMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_RollOff(pRollOff: POINTER(win32more.Media.DirectShow.RollOff)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_RollOff(pRollOff: POINTER(win32more.Media.DirectShow.RollOff)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_Pilot(pPilot: POINTER(win32more.Media.DirectShow.Pilot)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Pilot(pPilot: POINTER(win32more.Media.DirectShow.Pilot)) -> win32more.Foundation.HRESULT: ...
class IBDA_DigitalDemodulator3(c_void_p):
    extends: win32more.Media.DirectShow.IBDA_DigitalDemodulator2
    Guid = Guid('13f19604-7d32-4359-93-a2-a0-52-05-d9-0a-c9')
    @commethod(25)
    def put_SignalTimeouts(pSignalTimeouts: POINTER(win32more.Media.DirectShow.BDA_SIGNAL_TIMEOUTS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_SignalTimeouts(pSignalTimeouts: POINTER(win32more.Media.DirectShow.BDA_SIGNAL_TIMEOUTS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_PLPNumber(pPLPNumber: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_PLPNumber(pPLPNumber: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_DiseqCommand(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f84e2ab0-3c6b-45e3-a0-fc-86-69-d4-b8-1f-11')
    @commethod(3)
    def put_EnableDiseqCommands(bEnable: win32more.Foundation.BOOLEAN) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_DiseqLNBSource(ulLNBSource: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_DiseqUseToneBurst(bUseToneBurst: win32more.Foundation.BOOLEAN) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_DiseqRepeats(ulRepeats: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_DiseqSendCommand(ulRequestId: UInt32, ulcbCommandLen: UInt32, pbCommand: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_DiseqResponse(ulRequestId: UInt32, pulcbResponseLen: POINTER(UInt32), pbResponse: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBDA_EasMessage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d806973d-3ebe-46de-8f-bb-63-58-fe-78-42-08')
    @commethod(3)
    def get_EasMessage(ulEventID: UInt32, ppEASObject: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IBDA_Encoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3a8bad59-59fe-4559-a0-ba-39-6c-fa-a9-8a-e3')
    @commethod(3)
    def QueryCapabilities(NumAudioFmts: POINTER(UInt32), NumVideoFmts: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumAudioCapability(FmtIndex: UInt32, MethodID: POINTER(UInt32), AlgorithmType: POINTER(UInt32), SamplingRate: POINTER(UInt32), BitDepth: POINTER(UInt32), NumChannels: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumVideoCapability(FmtIndex: UInt32, MethodID: POINTER(UInt32), AlgorithmType: POINTER(UInt32), VerticalSize: POINTER(UInt32), HorizontalSize: POINTER(UInt32), AspectRatio: POINTER(UInt32), FrameRateCode: POINTER(UInt32), ProgressiveSequence: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetParameters(AudioBitrateMode: UInt32, AudioBitrate: UInt32, AudioMethodID: UInt32, AudioProgram: UInt32, VideoBitrateMode: UInt32, VideoBitrate: UInt32, VideoMethodID: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetState(AudioBitrateMax: POINTER(UInt32), AudioBitrateMin: POINTER(UInt32), AudioBitrateMode: POINTER(UInt32), AudioBitrateStepping: POINTER(UInt32), AudioBitrate: POINTER(UInt32), AudioMethodID: POINTER(UInt32), AvailableAudioPrograms: POINTER(UInt32), AudioProgram: POINTER(UInt32), VideoBitrateMax: POINTER(UInt32), VideoBitrateMin: POINTER(UInt32), VideoBitrateMode: POINTER(UInt32), VideoBitrate: POINTER(UInt32), VideoBitrateStepping: POINTER(UInt32), VideoMethodID: POINTER(UInt32), SignalSourceID: POINTER(UInt32), SignalFormat: POINTER(UInt64), SignalLock: POINTER(win32more.Foundation.BOOL), SignalLevel: POINTER(Int32), SignalToNoiseRatio: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_EthernetFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71985f43-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
    @commethod(3)
    def GetMulticastListSize(pulcbAddresses: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PutMulticastList(ulcbAddresses: UInt32, pAddressList: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMulticastList(pulcbAddresses: POINTER(UInt32), pAddressList: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def PutMulticastMode(ulModeMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetMulticastMode(pulModeMask: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_EventingService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('207c413f-00dc-4c61-ba-d6-6f-ee-1f-f0-70-64')
    @commethod(3)
    def CompleteEvent(ulEventID: UInt32, ulEventResult: UInt32) -> win32more.Foundation.HRESULT: ...
class IBDA_FDC(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('138adc7e-58ae-437f-b0-b4-c9-fe-19-d5-b4-ac')
    @commethod(3)
    def GetStatus(CurrentBitrate: POINTER(UInt32), CarrierLock: POINTER(win32more.Foundation.BOOL), CurrentFrequency: POINTER(UInt32), CurrentSpectrumInversion: POINTER(win32more.Foundation.BOOL), CurrentPIDList: POINTER(win32more.Foundation.BSTR), CurrentTIDList: POINTER(win32more.Foundation.BSTR), Overflow: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RequestTables(TableIDs: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddPid(PidsToAdd: win32more.Foundation.BSTR, RemainingFilterEntries: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemovePid(PidsToRemove: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AddTid(TidsToAdd: win32more.Foundation.BSTR, CurrentTidList: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveTid(TidsToRemove: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableSection(Pid: POINTER(UInt32), MaxBufferSize: UInt32, ActualSize: POINTER(UInt32), SecBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBDA_FrequencyFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71985f47-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
    @commethod(3)
    def put_Autotune(ulTransponder: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Autotune(pulTransponder: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_Frequency(ulFrequency: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Frequency(pulFrequency: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_Polarity(Polarity: win32more.Media.DirectShow.Polarisation) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Polarity(pPolarity: POINTER(win32more.Media.DirectShow.Polarisation)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Range(ulRange: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Range(pulRange: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Bandwidth(ulBandwidth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Bandwidth(pulBandwidth: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_FrequencyMultiplier(ulMultiplier: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_FrequencyMultiplier(pulMultiplier: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_GuideDataDeliveryService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0afcb73-23e7-4bc6-ba-fa-fd-c1-67-b4-71-9f')
    @commethod(3)
    def GetGuideDataType(pguidDataType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetGuideData(pulcbBufferLen: POINTER(UInt32), pbBuffer: c_char_p_no, pulGuideDataPercentageProgress: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RequestGuideDataUpdate() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTuneXmlFromServiceIdx(ul64ServiceIdx: UInt64, pbstrTuneXml: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetServices(pulcbBufferLen: POINTER(UInt32), pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceInfoFromTuneXml(bstrTuneXml: win32more.Foundation.BSTR, pbstrServiceDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IBDA_IPSinkControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3f4dc8e2-4050-11d3-8f-4b-00-c0-4f-79-71-e2')
    @commethod(3)
    def GetMulticastList(pulcbSize: POINTER(UInt32), pbBuffer: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterIPAddress(pulcbSize: POINTER(UInt32), pbBuffer: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IBDA_IPSinkInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a750108f-492e-4d51-95-f7-64-9b-23-ff-7a-d7')
    @commethod(3)
    def get_MulticastList(pulcbAddresses: POINTER(UInt32), ppbAddressList: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_AdapterIPAddress(pbstrBuffer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_AdapterDescription(pbstrBuffer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IBDA_IPV4Filter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71985f44-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
    @commethod(3)
    def GetMulticastListSize(pulcbAddresses: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PutMulticastList(ulcbAddresses: UInt32, pAddressList: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMulticastList(pulcbAddresses: POINTER(UInt32), pAddressList: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def PutMulticastMode(ulModeMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetMulticastMode(pulModeMask: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_IPV6Filter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e1785a74-2a23-4fb3-92-45-a8-f8-80-17-ef-33')
    @commethod(3)
    def GetMulticastListSize(pulcbAddresses: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PutMulticastList(ulcbAddresses: UInt32, pAddressList: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMulticastList(pulcbAddresses: POINTER(UInt32), pAddressList: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def PutMulticastMode(ulModeMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetMulticastMode(pulModeMask: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_ISDBConditionalAccess(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5e68c627-16c2-4e6c-b1-e2-d0-01-70-cd-aa-0f')
    @commethod(3)
    def SetIsdbCasRequest(ulRequestId: UInt32, ulcbRequestBufferLen: UInt32, pbRequestBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBDA_LNBInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('992cf102-49f9-4719-a6-64-c4-f2-3e-24-08-f4')
    @commethod(3)
    def put_LocalOscilatorFrequencyLowBand(ulLOFLow: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_LocalOscilatorFrequencyLowBand(pulLOFLow: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_LocalOscilatorFrequencyHighBand(ulLOFHigh: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_LocalOscilatorFrequencyHighBand(pulLOFHigh: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_HighLowSwitchFrequency(ulSwitchFrequency: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_HighLowSwitchFrequency(pulSwitchFrequency: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_MUX(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('942aafec-4c05-4c74-b8-eb-87-06-c2-a4-94-3f')
    @commethod(3)
    def SetPidList(ulPidListCount: UInt32, pbPidListBuffer: POINTER(win32more.Media.DirectShow.BDA_MUX_PIDLISTITEM_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPidList(pulPidListCount: POINTER(UInt32), pbPidListBuffer: POINTER(win32more.Media.DirectShow.BDA_MUX_PIDLISTITEM_head)) -> win32more.Foundation.HRESULT: ...
class IBDA_NameValueService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7f0b3150-7b81-4ad4-98-e3-7e-90-97-09-43-01')
    @commethod(3)
    def GetValueNameByIndex(ulIndex: UInt32, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(bstrName: win32more.Foundation.BSTR, bstrLanguage: win32more.Foundation.BSTR, pbstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(ulDialogRequest: UInt32, bstrLanguage: win32more.Foundation.BSTR, bstrName: win32more.Foundation.BSTR, bstrValue: win32more.Foundation.BSTR, ulReserved: UInt32) -> win32more.Foundation.HRESULT: ...
class IBDA_NetworkProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fd501041-8ebe-11ce-81-83-00-aa-00-57-7d-a2')
    @commethod(3)
    def PutSignalSource(ulSignalSource: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignalSource(pulSignalSource: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkType(pguidNetworkType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def PutTuningSpace(guidTuningSpace: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTuningSpace(pguidTuingSpace: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterDeviceFilter(pUnkFilterControl: win32more.System.Com.IUnknown_head, ppvRegisitrationContext: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def UnRegisterDeviceFilter(pvRegistrationContext: UInt32) -> win32more.Foundation.HRESULT: ...
class IBDA_NullTransform(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ddf15b0d-bd25-11d2-9c-a0-00-c0-4f-79-71-e0')
    @commethod(3)
    def Start() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Stop() -> win32more.Foundation.HRESULT: ...
class IBDA_PinControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0ded49d5-a8b7-4d5d-97-a1-12-b0-c1-95-87-4d')
    @commethod(3)
    def GetPinID(pulPinID: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPinType(pulPinType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RegistrationContext(pulRegistrationCtx: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_SignalProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2f1644b-b409-11d2-bc-69-00-a0-c9-ee-9e-16')
    @commethod(3)
    def PutNetworkType(guidNetworkType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNetworkType(pguidNetworkType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PutSignalSource(ulSignalSource: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignalSource(pulSignalSource: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def PutTuningSpace(guidTuningSpace: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTuningSpace(pguidTuingSpace: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IBDA_SignalStatistics(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1347d106-cf3a-428a-a5-cb-ac-0d-9a-2a-43-38')
    @commethod(3)
    def put_SignalStrength(lDbStrength: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_SignalStrength(plDbStrength: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_SignalQuality(lPercentQuality: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_SignalQuality(plPercentQuality: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_SignalPresent(fPresent: win32more.Foundation.BOOLEAN) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_SignalPresent(pfPresent: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_SignalLocked(fLocked: win32more.Foundation.BOOLEAN) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_SignalLocked(pfLocked: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_SampleTime(lmsSampleTime: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_SampleTime(plmsSampleTime: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IBDA_TIF_REGISTRATION(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dfef4a68-ee61-415f-9c-cb-cd-95-f2-f9-8a-3a')
    @commethod(3)
    def RegisterTIFEx(pTIFInputPin: win32more.Media.DirectShow.IPin_head, ppvRegistrationContext: POINTER(UInt32), ppMpeg2DataControl: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterTIF(pvRegistrationContext: UInt32) -> win32more.Foundation.HRESULT: ...
class IBDA_Topology(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('79b56888-7fea-4690-b4-5d-38-fd-3c-78-49-be')
    @commethod(3)
    def GetNodeTypes(pulcNodeTypes: POINTER(UInt32), ulcNodeTypesMax: UInt32, rgulNodeTypes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNodeDescriptors(ulcNodeDescriptors: POINTER(UInt32), ulcNodeDescriptorsMax: UInt32, rgNodeDescriptors: POINTER(win32more.Media.DirectShow.BDANODE_DESCRIPTOR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNodeInterfaces(ulNodeType: UInt32, pulcInterfaces: POINTER(UInt32), ulcInterfacesMax: UInt32, rgguidInterfaces: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPinTypes(pulcPinTypes: POINTER(UInt32), ulcPinTypesMax: UInt32, rgulPinTypes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTemplateConnections(pulcConnections: POINTER(UInt32), ulcConnectionsMax: UInt32, rgConnections: POINTER(win32more.Media.DirectShow.BDA_TEMPLATE_CONNECTION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreatePin(ulPinType: UInt32, pulPinId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def DeletePin(ulPinId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetMediaType(ulPinId: UInt32, pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetMedium(ulPinId: UInt32, pMedium: POINTER(win32more.Media.DirectShow.REGPINMEDIUM_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateTopology(ulInputPinId: UInt32, ulOutputPinId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetControlNode(ulInputPinId: UInt32, ulOutputPinId: UInt32, ulNodeType: UInt32, ppControlNode: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IBDA_TransportStreamInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8e882535-5f86-47ab-86-cf-c2-81-a7-2a-05-49')
    @commethod(3)
    def get_PatTableTickCount(pPatTickCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBDA_TransportStreamSelector(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1dcfafe9-b45e-41b3-bb-2a-56-1e-b1-29-ae-98')
    @commethod(3)
    def SetTSID(usTSID: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTSInformation(pulTSInformationBufferLen: POINTER(UInt32), pbTSInformationBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBDA_UserActivityService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('53b14189-e478-4b7a-a1-ff-50-6d-b4-b9-9d-fe')
    @commethod(3)
    def SetCurrentTunerUseReason(dwUseReason: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetUserActivityInterval(pdwActivityInterval: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def UserActivityDetected() -> win32more.Foundation.HRESULT: ...
class IBDA_VoidTransform(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71985f46-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
    @commethod(3)
    def Start() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Stop() -> win32more.Foundation.HRESULT: ...
class IBDA_WMDRMSession(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4be6fa3d-07cd-4139-8b-80-8c-18-ba-3a-ec-88')
    @commethod(3)
    def GetStatus(MaxCaptureToken: POINTER(UInt32), MaxStreamingPid: POINTER(UInt32), MaxLicense: POINTER(UInt32), MinSecurityLevel: POINTER(UInt32), RevInfoSequenceNumber: POINTER(UInt32), RevInfoIssuedTime: POINTER(UInt64), RevInfoTTL: POINTER(UInt32), RevListVersion: POINTER(UInt32), ulState: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetRevInfo(ulRevInfoLen: UInt32, pbRevInfo: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetCrl(ulCrlLen: UInt32, pbCrlLen: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def TransactMessage(ulcbRequest: UInt32, pbRequest: c_char_p_no, pulcbResponse: POINTER(UInt32), pbResponse: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetLicense(uuidKey: POINTER(Guid), pulPackageLen: POINTER(UInt32), pbPackage: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ReissueLicense(uuidKey: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RenewLicense(ulInXmrLicenseLen: UInt32, pbInXmrLicense: c_char_p_no, ulEntitlementTokenLen: UInt32, pbEntitlementToken: c_char_p_no, pulDescrambleStatus: POINTER(UInt32), pulOutXmrLicenseLen: POINTER(UInt32), pbOutXmrLicense: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetKeyInfo(pulKeyInfoLen: POINTER(UInt32), pbKeyInfo: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBDA_WMDRMTuner(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('86d979cf-a8a7-4f94-b5-fb-14-c0-ac-a6-8f-e6')
    @commethod(3)
    def PurchaseEntitlement(ulDialogRequest: UInt32, bstrLanguage: win32more.Foundation.BSTR, ulPurchaseTokenLen: UInt32, pbPurchaseToken: c_char_p_no, pulDescrambleStatus: POINTER(UInt32), pulCaptureTokenLen: POINTER(UInt32), pbCaptureToken: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CancelCaptureToken(ulCaptureTokenLen: UInt32, pbCaptureToken: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetPidProtection(ulPid: UInt32, uuidKey: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPidProtection(pulPid: UInt32, uuidKey: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetSyncValue(ulSyncValue: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetStartCodeProfile(pulStartCodeProfileLen: POINTER(UInt32), pbStartCodeProfile: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IBPCSatelliteTuner(c_void_p):
    extends: win32more.Media.DirectShow.IAMTuner
    Guid = Guid('211a8765-03ac-11d1-8d-13-00-aa-00-bd-83-39')
    @commethod(18)
    def get_DefaultSubChannelTypes(plDefaultVideoType: POINTER(Int32), plDefaultAudioType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_DefaultSubChannelTypes(lDefaultVideoType: Int32, lDefaultAudioType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def IsTapingPermitted() -> win32more.Foundation.HRESULT: ...
class IBaseFilter(c_void_p):
    extends: win32more.Media.DirectShow.IMediaFilter
    Guid = Guid('56a86895-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(10)
    def EnumPins(ppEnum: POINTER(win32more.Media.DirectShow.IEnumPins_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def FindPin(Id: win32more.Foundation.PWSTR, ppPin: POINTER(win32more.Media.DirectShow.IPin_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def QueryFilterInfo(pInfo: POINTER(win32more.Media.DirectShow.FILTER_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def JoinFilterGraph(pGraph: win32more.Media.DirectShow.IFilterGraph_head, pName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def QueryVendorInfo(pVendorInfo: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IBaseVideoMixer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('61ded640-e912-11ce-a0-99-00-aa-00-47-9a-58')
    @commethod(3)
    def SetLeadPin(iPin: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLeadPin(piPin: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputPinCount(piPinCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsUsingClock(pbValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetUsingClock(bValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetClockPeriod(pbValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetClockPeriod(bValue: Int32) -> win32more.Foundation.HRESULT: ...
class IBasicAudio(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868b3-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def put_Volume(lVolume: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Volume(plVolume: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Balance(lBalance: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Balance(plBalance: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IBasicVideo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868b5-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def get_AvgTimePerFrame(pAvgTimePerFrame: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_BitRate(pBitRate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_BitErrorRate(pBitErrorRate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_VideoWidth(pVideoWidth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_VideoHeight(pVideoHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_SourceLeft(SourceLeft: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_SourceLeft(pSourceLeft: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_SourceWidth(SourceWidth: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_SourceWidth(pSourceWidth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_SourceTop(SourceTop: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_SourceTop(pSourceTop: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_SourceHeight(SourceHeight: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_SourceHeight(pSourceHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_DestinationLeft(DestinationLeft: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_DestinationLeft(pDestinationLeft: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_DestinationWidth(DestinationWidth: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_DestinationWidth(pDestinationWidth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_DestinationTop(DestinationTop: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_DestinationTop(pDestinationTop: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_DestinationHeight(DestinationHeight: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_DestinationHeight(pDestinationHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SetSourcePosition(Left: Int32, Top: Int32, Width: Int32, Height: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetSourcePosition(pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SetDefaultSourcePosition() -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def SetDestinationPosition(Left: Int32, Top: Int32, Width: Int32, Height: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetDestinationPosition(pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def SetDefaultDestinationPosition() -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetVideoSize(pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetVideoPaletteEntries(StartIndex: Int32, Entries: Int32, pRetrieved: POINTER(Int32), pPalette: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetCurrentImage(pBufferSize: POINTER(Int32), pDIBImage: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def IsUsingDefaultSource() -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def IsUsingDefaultDestination() -> win32more.Foundation.HRESULT: ...
class IBasicVideo2(c_void_p):
    extends: win32more.Media.DirectShow.IBasicVideo
    Guid = Guid('329bb360-f6ea-11d1-90-38-00-a0-c9-69-72-98')
    @commethod(39)
    def GetPreferredAspectRatio(plAspectX: POINTER(Int32), plAspectY: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IBroadcastEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3b21263f-26e8-489d-aa-c4-92-4f-7e-fd-95-11')
    @commethod(3)
    def Fire(EventID: Guid) -> win32more.Foundation.HRESULT: ...
class IBroadcastEventEx(c_void_p):
    extends: win32more.Media.DirectShow.IBroadcastEvent
    Guid = Guid('3d9e3887-1929-423f-80-21-43-68-2d-e9-54-48')
    @commethod(4)
    def FireEx(EventID: Guid, Param1: UInt32, Param2: UInt32, Param3: UInt32, Param4: UInt32) -> win32more.Foundation.HRESULT: ...
class IBufferingTime(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1e00486a-78dd-11d2-8d-d3-00-60-97-c9-a2-b2')
    @commethod(3)
    def GetBufferingTime(pdwMilliseconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetBufferingTime(dwMilliseconds: UInt32) -> win32more.Foundation.HRESULT: ...
class ICAT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7c6995fb-2a31-4bd7-95-3e-b1-ad-7f-b7-d3-1c')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextTable(dwTimeout: UInt32, ppCAT: POINTER(win32more.Media.DirectShow.ICAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
class ICCSubStreamFiltering(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4b2bd7ea-8347-467b-8d-bf-62-f7-84-92-9c-c3')
    @commethod(3)
    def get_SubstreamTypes(pTypes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_SubstreamTypes(Types: Int32) -> win32more.Foundation.HRESULT: ...
class ICameraControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2ba1785d-4d1b-44ef-85-e8-c7-f1-d3-f2-01-84')
    @commethod(3)
    def get_Exposure(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_Exposure(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def getRange_Exposure(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Focus(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_Focus(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def getRange_Focus(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Iris(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Iris(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def getRange_Iris(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Zoom(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Zoom(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def getRange_Zoom(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_FocalLengths(plOcularFocalLength: POINTER(Int32), plObjectiveFocalLengthMin: POINTER(Int32), plObjectiveFocalLengthMax: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Pan(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Pan(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def getRange_Pan(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Tilt(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Tilt(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def getRange_Tilt(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_PanTilt(pPanValue: POINTER(Int32), pTiltValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_PanTilt(PanValue: Int32, TiltValue: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Roll(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_Roll(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def getRange_Roll(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_ExposureRelative(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_ExposureRelative(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def getRange_ExposureRelative(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_FocusRelative(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_FocusRelative(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def getRange_FocusRelative(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_IrisRelative(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_IrisRelative(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def getRange_IrisRelative(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_ZoomRelative(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_ZoomRelative(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def getRange_ZoomRelative(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_PanRelative(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_PanRelative(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_TiltRelative(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def put_TiltRelative(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def getRange_TiltRelative(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_PanTiltRelative(pPanValue: POINTER(Int32), pTiltValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_PanTiltRelative(PanValue: Int32, TiltValue: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def getRange_PanRelative(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get_RollRelative(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def put_RollRelative(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def getRange_RollRelative(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def get_ScanMode(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def put_ScanMode(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_PrivacyMode(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def put_PrivacyMode(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
class ICaptionServiceDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('40834007-6834-46f0-bd-45-d5-f6-a6-be-25-8c')
    @commethod(3)
    def GetNumberOfServices(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLanguageCode(bIndex: Byte, LangCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCaptionServiceNumber(bIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCCType(bIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetEasyReader(bIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetWideAspectRatio(bIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class ICaptureGraphBuilder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bf87b6e0-8c27-11d0-b3-f0-00-aa-00-37-61-c5')
    @commethod(3)
    def SetFiltergraph(pfg: win32more.Media.DirectShow.IGraphBuilder_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiltergraph(ppfg: POINTER(win32more.Media.DirectShow.IGraphBuilder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFileName(pType: POINTER(Guid), lpstrFile: win32more.Foundation.PWSTR, ppf: POINTER(win32more.Media.DirectShow.IBaseFilter_head), ppSink: POINTER(win32more.Media.DirectShow.IFileSinkFilter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FindInterface(pCategory: POINTER(Guid), pf: win32more.Media.DirectShow.IBaseFilter_head, riid: POINTER(Guid), ppint: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RenderStream(pCategory: POINTER(Guid), pSource: win32more.System.Com.IUnknown_head, pfCompressor: win32more.Media.DirectShow.IBaseFilter_head, pfRenderer: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ControlStream(pCategory: POINTER(Guid), pFilter: win32more.Media.DirectShow.IBaseFilter_head, pstart: POINTER(Int64), pstop: POINTER(Int64), wStartCookie: UInt16, wStopCookie: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AllocCapFile(lpstr: win32more.Foundation.PWSTR, dwlSize: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CopyCaptureFile(lpwstrOld: win32more.Foundation.PWSTR, lpwstrNew: win32more.Foundation.PWSTR, fAllowEscAbort: Int32, pCallback: win32more.Media.DirectShow.IAMCopyCaptureFileProgress_head) -> win32more.Foundation.HRESULT: ...
class ICaptureGraphBuilder2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('93e5a4e0-2d50-11d2-ab-fa-00-a0-c9-c6-e3-8d')
    @commethod(3)
    def SetFiltergraph(pfg: win32more.Media.DirectShow.IGraphBuilder_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiltergraph(ppfg: POINTER(win32more.Media.DirectShow.IGraphBuilder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFileName(pType: POINTER(Guid), lpstrFile: win32more.Foundation.PWSTR, ppf: POINTER(win32more.Media.DirectShow.IBaseFilter_head), ppSink: POINTER(win32more.Media.DirectShow.IFileSinkFilter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FindInterface(pCategory: POINTER(Guid), pType: POINTER(Guid), pf: win32more.Media.DirectShow.IBaseFilter_head, riid: POINTER(Guid), ppint: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RenderStream(pCategory: POINTER(Guid), pType: POINTER(Guid), pSource: win32more.System.Com.IUnknown_head, pfCompressor: win32more.Media.DirectShow.IBaseFilter_head, pfRenderer: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ControlStream(pCategory: POINTER(Guid), pType: POINTER(Guid), pFilter: win32more.Media.DirectShow.IBaseFilter_head, pstart: POINTER(Int64), pstop: POINTER(Int64), wStartCookie: UInt16, wStopCookie: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AllocCapFile(lpstr: win32more.Foundation.PWSTR, dwlSize: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CopyCaptureFile(lpwstrOld: win32more.Foundation.PWSTR, lpwstrNew: win32more.Foundation.PWSTR, fAllowEscAbort: Int32, pCallback: win32more.Media.DirectShow.IAMCopyCaptureFileProgress_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def FindPin(pSource: win32more.System.Com.IUnknown_head, pindir: win32more.Media.DirectShow.PIN_DIRECTION, pCategory: POINTER(Guid), pType: POINTER(Guid), fUnconnected: win32more.Foundation.BOOL, num: Int32, ppPin: POINTER(win32more.Media.DirectShow.IPin_head)) -> win32more.Foundation.HRESULT: ...
class IChannelIDTuneRequest(c_void_p):
    extends: win32more.Media.DirectShow.ITuneRequest
    Guid = Guid('156eff60-86f4-4e28-89-fc-10-97-99-fd-57-ee')
    @commethod(12)
    def get_ChannelID(ChannelID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_ChannelID(ChannelID: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IChannelTuneRequest(c_void_p):
    extends: win32more.Media.DirectShow.ITuneRequest
    Guid = Guid('0369b4e0-45b6-11d3-b6-50-00-c0-4f-79-49-8e')
    @commethod(12)
    def get_Channel(Channel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Channel(Channel: Int32) -> win32more.Foundation.HRESULT: ...
class IComponent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('1a5576fc-0e19-11d3-9d-8e-00-c0-4f-72-d9-80')
    @commethod(7)
    def get_Type(CT: POINTER(win32more.Media.DirectShow.IComponentType_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Type(CT: win32more.Media.DirectShow.IComponentType_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_DescLangID(LangID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_DescLangID(LangID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(Status: POINTER(win32more.Media.DirectShow.ComponentStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Status(Status: win32more.Media.DirectShow.ComponentStatus) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Description(Description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Description(Description: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(NewComponent: POINTER(win32more.Media.DirectShow.IComponent_head)) -> win32more.Foundation.HRESULT: ...
class IComponentType(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6a340dc0-0311-11d3-9d-8e-00-c0-4f-72-d9-80')
    @commethod(7)
    def get_Category(Category: POINTER(win32more.Media.DirectShow.ComponentCategory)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Category(Category: win32more.Media.DirectShow.ComponentCategory) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_MediaMajorType(MediaMajorType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_MediaMajorType(MediaMajorType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get__MediaMajorType(MediaMajorTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put__MediaMajorType(MediaMajorTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_MediaSubType(MediaSubType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_MediaSubType(MediaSubType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get__MediaSubType(MediaSubTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put__MediaSubType(MediaSubTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_MediaFormatType(MediaFormatType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_MediaFormatType(MediaFormatType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get__MediaFormatType(MediaFormatTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put__MediaFormatType(MediaFormatTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_MediaType(MediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_MediaType(MediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(NewCT: POINTER(win32more.Media.DirectShow.IComponentType_head)) -> win32more.Foundation.HRESULT: ...
class IComponentTypes(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0dc13d4a-0313-11d3-9d-8e-00-c0-4f-72-d9-80')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(ppNewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumComponentTypes(ppNewEnum: POINTER(win32more.Media.DirectShow.IEnumComponentTypes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Item(Index: win32more.System.Com.VARIANT, ComponentType: POINTER(win32more.Media.DirectShow.IComponentType_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Item(Index: win32more.System.Com.VARIANT, ComponentType: win32more.Media.DirectShow.IComponentType_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Add(ComponentType: win32more.Media.DirectShow.IComponentType_head, NewIndex: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Remove(Index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Clone(NewList: POINTER(win32more.Media.DirectShow.IComponentTypes_head)) -> win32more.Foundation.HRESULT: ...
class IComponents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('39a48091-fffe-4182-a1-61-3f-f8-02-64-0e-26')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(ppNewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumComponents(ppNewEnum: POINTER(win32more.Media.DirectShow.IEnumComponents_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Item(Index: win32more.System.Com.VARIANT, ppComponent: POINTER(win32more.Media.DirectShow.IComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Add(Component: win32more.Media.DirectShow.IComponent_head, NewIndex: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(Index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(NewList: POINTER(win32more.Media.DirectShow.IComponents_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Item(Index: win32more.System.Com.VARIANT, ppComponent: win32more.Media.DirectShow.IComponent_head) -> win32more.Foundation.HRESULT: ...
class IComponentsOld(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fcd01846-0e19-11d3-9d-8e-00-c0-4f-72-d9-80')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(ppNewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumComponents(ppNewEnum: POINTER(win32more.Media.DirectShow.IEnumComponents_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Item(Index: win32more.System.Com.VARIANT, ppComponent: POINTER(win32more.Media.DirectShow.IComponent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Add(Component: win32more.Media.DirectShow.IComponent_head, NewIndex: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(Index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(NewList: POINTER(win32more.Media.DirectShow.IComponents_head)) -> win32more.Foundation.HRESULT: ...
class IConfigAsfWriter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('45086030-f7e4-486a-b5-04-82-6b-b5-79-2a-3b')
    @commethod(3)
    def ConfigureFilterUsingProfileId(dwProfileId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentProfileId(pdwProfileId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ConfigureFilterUsingProfileGuid(guidProfile: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentProfileGuid(pProfileGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ConfigureFilterUsingProfile(pProfile: win32more.Media.WindowsMediaFormat.IWMProfile_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentProfile(ppProfile: POINTER(win32more.Media.WindowsMediaFormat.IWMProfile_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetIndexMode(bIndexFile: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetIndexMode(pbIndexFile: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IConfigAsfWriter2(c_void_p):
    extends: win32more.Media.DirectShow.IConfigAsfWriter
    Guid = Guid('7989ccaa-53f0-44f0-88-4a-f3-b0-3f-6a-e0-66')
    @commethod(11)
    def StreamNumFromPin(pPin: win32more.Media.DirectShow.IPin_head, pwStreamNum: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetParam(dwParam: UInt32, dwParam1: UInt32, dwParam2: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetParam(dwParam: UInt32, pdwParam1: POINTER(UInt32), pdwParam2: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def ResetMultiPassState() -> win32more.Foundation.HRESULT: ...
class IConfigAviMux(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5acd6aa0-f482-11ce-8b-67-00-aa-00-a3-f1-a6')
    @commethod(3)
    def SetMasterStream(iStream: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMasterStream(pStream: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputCompatibilityIndex(fOldIndex: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputCompatibilityIndex(pfOldIndex: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IConfigInterleaving(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bee3d220-157b-11d0-bd-23-00-a0-c9-11-ce-86')
    @commethod(3)
    def put_Mode(mode: win32more.Media.DirectShow.InterleavingMode) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Mode(pMode: POINTER(win32more.Media.DirectShow.InterleavingMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_Interleaving(prtInterleave: POINTER(Int64), prtPreroll: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Interleaving(prtInterleave: POINTER(Int64), prtPreroll: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class ICreateDevEnum(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('29840822-5b84-11d0-bd-3b-00-a0-c9-11-ce-86')
    @commethod(3)
    def CreateClassEnumerator(clsidDeviceClass: POINTER(Guid), ppEnumMoniker: POINTER(win32more.System.Com.IEnumMoniker_head), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class ICreatePropBagOnRegKey(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8a674b48-1f63-11d3-b6-4c-00-c0-4f-79-49-8e')
    @commethod(3)
    def Create(hkey: win32more.System.Registry.HKEY, subkey: win32more.Foundation.PWSTR, ulOptions: UInt32, samDesired: UInt32, iid: POINTER(Guid), ppBag: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDDrawExclModeVideo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('153acc21-d83b-11d1-82-bf-00-a0-c9-69-6c-8f')
    @commethod(3)
    def SetDDrawObject(pDDrawObject: win32more.Graphics.DirectDraw.IDirectDraw_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDDrawObject(ppDDrawObject: POINTER(win32more.Graphics.DirectDraw.IDirectDraw_head), pbUsingExternal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetDDrawSurface(pDDrawSurface: win32more.Graphics.DirectDraw.IDirectDrawSurface_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDDrawSurface(ppDDrawSurface: POINTER(win32more.Graphics.DirectDraw.IDirectDrawSurface_head), pbUsingExternal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetDrawParameters(prcSource: POINTER(win32more.Foundation.RECT_head), prcTarget: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetNativeVideoProps(pdwVideoWidth: POINTER(UInt32), pdwVideoHeight: POINTER(UInt32), pdwPictAspectRatioX: POINTER(UInt32), pdwPictAspectRatioY: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetCallbackInterface(pCallback: win32more.Media.DirectShow.IDDrawExclModeVideoCallback_head, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IDDrawExclModeVideoCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('913c24a0-20ab-11d2-90-38-00-a0-c9-69-72-98')
    @commethod(3)
    def OnUpdateOverlay(bBefore: win32more.Foundation.BOOL, dwFlags: UInt32, bOldVisible: win32more.Foundation.BOOL, prcOldSrc: POINTER(win32more.Foundation.RECT_head), prcOldDest: POINTER(win32more.Foundation.RECT_head), bNewVisible: win32more.Foundation.BOOL, prcNewSrc: POINTER(win32more.Foundation.RECT_head), prcNewDest: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnUpdateColorKey(pKey: POINTER(win32more.Media.DirectShow.COLORKEY_head), dwColor: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnUpdateSize(dwWidth: UInt32, dwHeight: UInt32, dwARWidth: UInt32, dwARHeight: UInt32) -> win32more.Foundation.HRESULT: ...
class IDMOWrapperFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('52d6f586-9f0f-4824-8f-c8-e3-2c-a0-49-30-c2')
    @commethod(3)
    def Init(clsidDMO: POINTER(Guid), catDMO: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IDShowPlugin(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4746b7c8-700e-11d1-be-cc-00-c0-4f-b6-e9-37')
    @commethod(3)
    def get_URL(pURL: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_UserAgent(pUserAgent: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDTFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c4c4c4b2-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
    @commethod(3)
    def get_EvalRatObjOK(pHrCoCreateRetVal: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrRating(pEnSystem: POINTER(win32more.Media.DirectShow.EnTvRat_System), pEnRating: POINTER(win32more.Media.DirectShow.EnTvRat_GenericLevel), plbfEnAttr: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_BlockedRatingAttributes(enSystem: win32more.Media.DirectShow.EnTvRat_System, enLevel: win32more.Media.DirectShow.EnTvRat_GenericLevel, plbfEnAttr: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_BlockedRatingAttributes(enSystem: win32more.Media.DirectShow.EnTvRat_System, enLevel: win32more.Media.DirectShow.EnTvRat_GenericLevel, lbfAttrs: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_BlockUnRated(pfBlockUnRatedShows: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_BlockUnRated(fBlockUnRatedShows: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_BlockUnRatedDelay(pmsecsDelayBeforeBlock: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_BlockUnRatedDelay(msecsDelayBeforeBlock: Int32) -> win32more.Foundation.HRESULT: ...
class IDTFilter2(c_void_p):
    extends: win32more.Media.DirectShow.IDTFilter
    Guid = Guid('c4c4c4b4-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
    @commethod(11)
    def get_ChallengeUrl(pbstrChallengeUrl: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetCurrLicenseExpDate(protType: POINTER(win32more.Media.DirectShow.ProtType), lpDateTime: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetLastErrorCode() -> win32more.Foundation.HRESULT: ...
class IDTFilter3(c_void_p):
    extends: win32more.Media.DirectShow.IDTFilter2
    Guid = Guid('513998cc-e929-4cdf-9f-bd-ba-d1-e0-31-48-66')
    @commethod(14)
    def GetProtectionType(pProtectionType: POINTER(win32more.Media.DirectShow.ProtType)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def LicenseHasExpirationDate(pfLicenseHasExpirationDate: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetRights(bstrRights: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IDTFilterConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c4c4c4d2-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
    @commethod(3)
    def GetSecureChannelObject(ppUnkDRMSecureChannel: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IDTFilterEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c4c4c4c2-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
class IDTFilterLicenseRenewal(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8a78b317-e405-4a43-99-4a-62-0d-8f-5c-e2-5e')
    @commethod(3)
    def GetLicenseRenewalData(ppwszFileName: POINTER(win32more.Foundation.PWSTR), ppwszExpiredKid: POINTER(win32more.Foundation.PWSTR), ppwszTunerId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IDVBCLocator(c_void_p):
    extends: win32more.Media.DirectShow.IDigitalLocator
    Guid = Guid('6e42f36e-1dd2-43c4-9f-78-69-d2-5a-e3-90-34')
class IDVBSLocator(c_void_p):
    extends: win32more.Media.DirectShow.IDigitalLocator
    Guid = Guid('3d7c353c-0d04-45f1-a7-42-f9-7c-c1-18-8d-c8')
    @commethod(22)
    def get_SignalPolarisation(PolarisationVal: POINTER(win32more.Media.DirectShow.Polarisation)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_SignalPolarisation(PolarisationVal: win32more.Media.DirectShow.Polarisation) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_WestPosition(WestLongitude: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_WestPosition(WestLongitude: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_OrbitalPosition(longitude: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_OrbitalPosition(longitude: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Azimuth(Azimuth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Azimuth(Azimuth: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_Elevation(Elevation: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_Elevation(Elevation: Int32) -> win32more.Foundation.HRESULT: ...
class IDVBSLocator2(c_void_p):
    extends: win32more.Media.DirectShow.IDVBSLocator
    Guid = Guid('6044634a-1733-4f99-b9-82-5f-b1-2a-fc-e4-f0')
    @commethod(32)
    def get_DiseqLNBSource(DiseqLNBSourceVal: POINTER(win32more.Media.DirectShow.LNB_Source)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_DiseqLNBSource(DiseqLNBSourceVal: win32more.Media.DirectShow.LNB_Source) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_LocalOscillatorOverrideLow(LocalOscillatorOverrideLowVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_LocalOscillatorOverrideLow(LocalOscillatorOverrideLowVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_LocalOscillatorOverrideHigh(LocalOscillatorOverrideHighVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_LocalOscillatorOverrideHigh(LocalOscillatorOverrideHighVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_LocalLNBSwitchOverride(LocalLNBSwitchOverrideVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_LocalLNBSwitchOverride(LocalLNBSwitchOverrideVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_LocalSpectralInversionOverride(LocalSpectralInversionOverrideVal: POINTER(win32more.Media.DirectShow.SpectralInversion)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_LocalSpectralInversionOverride(LocalSpectralInversionOverrideVal: win32more.Media.DirectShow.SpectralInversion) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_SignalRollOff(RollOffVal: POINTER(win32more.Media.DirectShow.RollOff)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_SignalRollOff(RollOffVal: win32more.Media.DirectShow.RollOff) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_SignalPilot(PilotVal: POINTER(win32more.Media.DirectShow.Pilot)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_SignalPilot(PilotVal: win32more.Media.DirectShow.Pilot) -> win32more.Foundation.HRESULT: ...
class IDVBSTuningSpace(c_void_p):
    extends: win32more.Media.DirectShow.IDVBTuningSpace2
    Guid = Guid('cdf7be60-d954-42fd-a9-72-78-97-19-58-e4-70')
    @commethod(30)
    def get_LowOscillator(LowOscillator: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_LowOscillator(LowOscillator: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_HighOscillator(HighOscillator: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_HighOscillator(HighOscillator: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_LNBSwitch(LNBSwitch: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_LNBSwitch(LNBSwitch: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_InputRange(InputRange: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_InputRange(InputRange: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_SpectralInversion(SpectralInversionVal: POINTER(win32more.Media.DirectShow.SpectralInversion)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_SpectralInversion(SpectralInversionVal: win32more.Media.DirectShow.SpectralInversion) -> win32more.Foundation.HRESULT: ...
class IDVBTLocator(c_void_p):
    extends: win32more.Media.DirectShow.IDigitalLocator
    Guid = Guid('8664da16-dda2-42ac-92-6a-c1-8f-91-27-c3-02')
    @commethod(22)
    def get_Bandwidth(BandWidthVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_Bandwidth(BandwidthVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_LPInnerFEC(FEC: POINTER(win32more.Media.DirectShow.FECMethod)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_LPInnerFEC(FEC: win32more.Media.DirectShow.FECMethod) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_LPInnerFECRate(FEC: POINTER(win32more.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_LPInnerFECRate(FEC: win32more.Media.DirectShow.BinaryConvolutionCodeRate) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_HAlpha(Alpha: POINTER(win32more.Media.DirectShow.HierarchyAlpha)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_HAlpha(Alpha: win32more.Media.DirectShow.HierarchyAlpha) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_Guard(GI: POINTER(win32more.Media.DirectShow.GuardInterval)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_Guard(GI: win32more.Media.DirectShow.GuardInterval) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_Mode(mode: POINTER(win32more.Media.DirectShow.TransmissionMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_Mode(mode: win32more.Media.DirectShow.TransmissionMode) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_OtherFrequencyInUse(OtherFrequencyInUseVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_OtherFrequencyInUse(OtherFrequencyInUseVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IDVBTLocator2(c_void_p):
    extends: win32more.Media.DirectShow.IDVBTLocator
    Guid = Guid('448a2edf-ae95-4b43-a3-cc-74-78-43-c4-53-d4')
    @commethod(36)
    def get_PhysicalLayerPipeId(PhysicalLayerPipeIdVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_PhysicalLayerPipeId(PhysicalLayerPipeIdVal: Int32) -> win32more.Foundation.HRESULT: ...
class IDVBTuneRequest(c_void_p):
    extends: win32more.Media.DirectShow.ITuneRequest
    Guid = Guid('0d6f567e-a636-42bb-83-ba-ce-4c-17-04-af-a2')
    @commethod(12)
    def get_ONID(ONID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_ONID(ONID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_TSID(TSID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_TSID(TSID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_SID(SID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_SID(SID: Int32) -> win32more.Foundation.HRESULT: ...
class IDVBTuningSpace(c_void_p):
    extends: win32more.Media.DirectShow.ITuningSpace
    Guid = Guid('ada0b268-3b19-4e5b-ac-c4-49-f8-52-be-13-ba')
    @commethod(26)
    def get_SystemType(SysType: POINTER(win32more.Media.DirectShow.DVBSystemType)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_SystemType(SysType: win32more.Media.DirectShow.DVBSystemType) -> win32more.Foundation.HRESULT: ...
class IDVBTuningSpace2(c_void_p):
    extends: win32more.Media.DirectShow.IDVBTuningSpace
    Guid = Guid('843188b4-ce62-43db-96-6b-81-45-a0-94-e0-40')
    @commethod(28)
    def get_NetworkID(NetworkID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_NetworkID(NetworkID: Int32) -> win32more.Foundation.HRESULT: ...
class IDVB_BAT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ece9bb0c-43b6-4558-a0-ec-18-12-c3-4c-d6-ca')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetBouquetId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordTransportStreamId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordOriginalNetworkId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetNextTable(ppBAT: POINTER(win32more.Media.DirectShow.IDVB_BAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
class IDVB_DIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('91bffdf9-9432-410f-86-ef-1c-22-8e-d0-ad-70')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransitionFlag(pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IDVB_EIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('442db029-02cb-4495-8b-92-1c-13-37-5b-ce-99')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransportStreamId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSegmentLastSectionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastTableId(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordEventId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordStartTime(dwRecordIndex: UInt32, pmdtVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDuration(dwRecordIndex: UInt32, pmdVal: POINTER(win32more.Media.DirectShow.MPEG_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordRunningStatus(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordFreeCAMode(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetNextTable(ppEIT: POINTER(win32more.Media.DirectShow.IDVB_EIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDVB_EIT2(c_void_p):
    extends: win32more.Media.DirectShow.IDVB_EIT
    Guid = Guid('61a389e0-9b9e-4ba0-ae-ea-5d-dd-15-98-20-ea')
    @commethod(24)
    def GetSegmentInfo(pbTid: c_char_p_no, pbSegment: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetRecordSection(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDVB_NIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c64935f4-29e4-4e22-91-1a-63-f7-f5-5c-b0-97')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordTransportStreamId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordOriginalNetworkId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetNextTable(ppNIT: POINTER(win32more.Media.DirectShow.IDVB_NIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDVB_RST(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f47dcd04-1e23-4fb7-9f-96-b4-0e-ea-d1-0b-2b')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecordTransportStreamId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordOriginalNetworkId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordServiceId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordEventId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordRunningStatus(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDVB_SDT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('02cad8d3-fe43-48e2-90-bd-45-0e-d9-a8-a5-fd')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransportStreamId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetOriginalNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordServiceId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordEITScheduleFlag(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordEITPresentFollowingFlag(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordRunningStatus(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordFreeCAMode(dwRecordIndex: UInt32, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetNextTable(ppSDT: POINTER(win32more.Media.DirectShow.IDVB_SDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDVB_SIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('68cdce53-8bea-45c2-9d-9d-ac-f5-75-a0-89-b5')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordServiceId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordRunningStatus(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetNextTable(dwTimeout: UInt32, ppSIT: POINTER(win32more.Media.DirectShow.IDVB_SIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
class IDVB_ST(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4d5b9f23-2a02-45de-bc-da-5d-5d-bf-bf-be-62')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataLength(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetData(ppData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IDVB_TDT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0780dc7d-d55c-4aef-97-e6-6b-75-90-6e-27-96')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetUTCTime(pmdtVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
class IDVB_TOT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('83295d6a-faba-4ee1-9b-15-80-67-69-69-10-ae')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetUTCTime(pmdtVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
class IDVEnc(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d18e17a0-aacb-11d0-af-b0-00-aa-00-b6-7a-42')
    @commethod(3)
    def get_IFormatResolution(VideoFormat: POINTER(Int32), DVFormat: POINTER(Int32), Resolution: POINTER(Int32), fDVInfo: Byte, sDVInfo: POINTER(win32more.Media.DirectShow.DVINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_IFormatResolution(VideoFormat: Int32, DVFormat: Int32, Resolution: Int32, fDVInfo: Byte, sDVInfo: POINTER(win32more.Media.DirectShow.DVINFO_head)) -> win32more.Foundation.HRESULT: ...
class IDVRGB219(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('58473a19-2bc8-4663-80-12-25-f8-1b-ab-dd-d1')
    @commethod(3)
    def SetRGB219(bState: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IDVSplitter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('92a3a302-da7c-4a1f-ba-7e-18-02-bb-5d-2d-02')
    @commethod(3)
    def DiscardAlternateVideoFrames(nDiscard: Int32) -> win32more.Foundation.HRESULT: ...
class IDecimateVideoImage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2e5ea3e0-e924-11d2-b6-da-00-a0-c9-95-e8-df')
    @commethod(3)
    def SetDecimationImageSize(lWidth: Int32, lHeight: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ResetDecimationImageSize() -> win32more.Foundation.HRESULT: ...
class IDeferredCommand(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868b8-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Confidence(pConfidence: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Postpone(newtime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetHResult(phrResult: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
class IDigitalCableLocator(c_void_p):
    extends: win32more.Media.DirectShow.IATSCLocator2
    Guid = Guid('48f66a11-171a-419a-95-25-be-ee-cd-51-58-4c')
class IDigitalCableTuneRequest(c_void_p):
    extends: win32more.Media.DirectShow.IATSCChannelTuneRequest
    Guid = Guid('bad7753b-6b37-4810-ae-57-3c-e0-c4-a9-e6-cb')
    @commethod(16)
    def get_MajorChannel(pMajorChannel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_MajorChannel(MajorChannel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_SourceID(pSourceID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_SourceID(SourceID: Int32) -> win32more.Foundation.HRESULT: ...
class IDigitalCableTuningSpace(c_void_p):
    extends: win32more.Media.DirectShow.IATSCTuningSpace
    Guid = Guid('013f9f9c-b449-4ec7-a6-d2-9d-4f-2f-c7-0a-e5')
    @commethod(42)
    def get_MinMajorChannel(MinMajorChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_MinMajorChannel(NewMinMajorChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_MaxMajorChannel(MaxMajorChannelVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_MaxMajorChannel(NewMaxMajorChannelVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_MinSourceID(MinSourceIDVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_MinSourceID(NewMinSourceIDVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_MaxSourceID(MaxSourceIDVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def put_MaxSourceID(NewMaxSourceIDVal: Int32) -> win32more.Foundation.HRESULT: ...
class IDigitalLocator(c_void_p):
    extends: win32more.Media.DirectShow.ILocator
    Guid = Guid('19b595d8-839a-47f0-96-df-4f-19-4f-3c-76-8c')
class IDirectDrawMediaSample(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ab6b4afe-f6e4-11d0-90-0d-00-c0-4f-d9-18-9d')
    @commethod(3)
    def GetSurfaceAndReleaseLock(ppDirectDrawSurface: POINTER(win32more.Graphics.DirectDraw.IDirectDrawSurface_head), pRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LockMediaSamplePointer() -> win32more.Foundation.HRESULT: ...
class IDirectDrawMediaSampleAllocator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ab6b4afc-f6e4-11d0-90-0d-00-c0-4f-d9-18-9d')
    @commethod(3)
    def GetDirectDraw(ppDirectDraw: POINTER(win32more.Graphics.DirectDraw.IDirectDraw_head)) -> win32more.Foundation.HRESULT: ...
class IDirectDrawMediaStream(c_void_p):
    extends: win32more.Media.DirectShow.IMediaStream
    Guid = Guid('f4104fce-9a70-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(9)
    def GetFormat(pDDSDCurrent: POINTER(win32more.Graphics.DirectDraw.DDSURFACEDESC_head), ppDirectDrawPalette: POINTER(win32more.Graphics.DirectDraw.IDirectDrawPalette_head), pDDSDDesired: POINTER(win32more.Graphics.DirectDraw.DDSURFACEDESC_head), pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetFormat(pDDSurfaceDesc: POINTER(win32more.Graphics.DirectDraw.DDSURFACEDESC_head), pDirectDrawPalette: win32more.Graphics.DirectDraw.IDirectDrawPalette_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetDirectDraw(ppDirectDraw: POINTER(win32more.Graphics.DirectDraw.IDirectDraw_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetDirectDraw(pDirectDraw: win32more.Graphics.DirectDraw.IDirectDraw_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def CreateSample(pSurface: win32more.Graphics.DirectDraw.IDirectDrawSurface_head, pRect: POINTER(win32more.Foundation.RECT_head), dwFlags: UInt32, ppSample: POINTER(win32more.Media.DirectShow.IDirectDrawStreamSample_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimePerFrame(pFrameTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IDirectDrawStreamSample(c_void_p):
    extends: win32more.Media.DirectShow.IStreamSample
    Guid = Guid('f4104fcf-9a70-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(8)
    def GetSurface(ppDirectDrawSurface: POINTER(win32more.Graphics.DirectDraw.IDirectDrawSurface_head), pRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetRect(pRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
class IDirectDrawVideo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('36d39eb0-dd75-11ce-bf-0e-00-aa-00-55-59-5a')
    @commethod(3)
    def GetSwitches(pSwitches: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetSwitches(Switches: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCaps(pCaps: POINTER(win32more.Graphics.DirectDraw.DDCAPS_DX7_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEmulatedCaps(pCaps: POINTER(win32more.Graphics.DirectDraw.DDCAPS_DX7_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSurfaceDesc(pSurfaceDesc: POINTER(win32more.Graphics.DirectDraw.DDSURFACEDESC_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFourCCCodes(pCount: POINTER(UInt32), pCodes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetDirectDraw(pDirectDraw: win32more.Graphics.DirectDraw.IDirectDraw_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDirectDraw(ppDirectDraw: POINTER(win32more.Graphics.DirectDraw.IDirectDraw_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSurfaceType(pSurfaceType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetDefault() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def UseScanLine(UseScanLine: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CanUseScanLine(UseScanLine: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def UseOverlayStretch(UseOverlayStretch: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CanUseOverlayStretch(UseOverlayStretch: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def UseWhenFullScreen(UseWhenFullScreen: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def WillUseFullScreen(UseWhenFullScreen: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IDistributorNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868af-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Stop() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Run(tStart: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetSyncSource(pClock: win32more.Media.IReferenceClock_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyGraphChange() -> win32more.Foundation.HRESULT: ...
class IDrawVideoImage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('48efb120-ab49-11d2-ae-d2-00-a0-c9-95-e8-d5')
    @commethod(3)
    def DrawVideoImageBegin() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DrawVideoImageEnd() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DrawVideoImageDraw(hdc: win32more.Graphics.Gdi.HDC, lprcSrc: POINTER(win32more.Foundation.RECT_head), lprcDst: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
class IDvbCableDeliverySystemDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dfb98e36-9e1a-4862-99-46-99-3a-4e-59-01-7b')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFrequency(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFECOuter(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetModulation(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSymbolRate(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFECInner(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbComponentDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('91e405cf-80e7-457f-90-96-1b-9d-1c-e3-21-41')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamContent(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetComponentTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetLanguageCode(pszCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTextW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDvbContentDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2e883881-a467-412a-9d-63-6f-2b-6d-a0-5b-f0')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordContentNibbles(bRecordIndex: Byte, pbValLevel1: c_char_p_no, pbValLevel2: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordUserNibbles(bRecordIndex: Byte, pbVal1: c_char_p_no, pbVal2: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbContentIdentifierDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('05e0c1ea-f661-4053-9f-bf-d9-3b-28-35-98-38')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordCrid(bRecordIndex: Byte, pbType: c_char_p_no, pbLocation: c_char_p_no, pbLength: c_char_p_no, ppbBytes: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IDvbDataBroadcastDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d1ebc1d6-8b60-4c20-9c-af-e5-93-82-e7-c4-00')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataBroadcastID(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSelectorLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelectorBytes(pbLen: c_char_p_no, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLangID(pulVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetTextLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetText(pbLen: c_char_p_no, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbDataBroadcastIDDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5f26f518-65c8-4048-91-f2-92-90-f5-9f-7b-90')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataBroadcastID(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetIDSelectorBytes(pbLen: c_char_p_no, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbDefaultAuthorityDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('05ec24d1-3a31-44e7-b4-08-67-c6-0a-35-22-76')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDefaultAuthority(pbLength: c_char_p_no, ppbBytes: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IDvbExtendedEventDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c9b22eca-85f4-499f-b1-db-ef-a9-3a-91-ee-57')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDescriptorNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastDescriptorNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetLanguageCode(pszCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordItemW(bRecordIndex: Byte, convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrDesc: POINTER(win32more.Foundation.BSTR), pbstrItem: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetConcatenatedItemW(pFollowingDescriptor: win32more.Media.DirectShow.IDvbExtendedEventDescriptor_head, convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrDesc: POINTER(win32more.Foundation.BSTR), pbstrItem: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetTextW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetConcatenatedTextW(FollowingDescriptor: win32more.Media.DirectShow.IDvbExtendedEventDescriptor_head, convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordItemRawBytes(bRecordIndex: Byte, ppbRawItem: POINTER(c_char_p_no), pbItemLength: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbFrequencyListDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1cadb613-e1dd-4512-af-a8-bb-7a-00-7e-f8-b1')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCodingType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordCentreFrequency(bRecordIndex: Byte, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDvbHDSimulcastLogicalChannelDescriptor(c_void_p):
    extends: win32more.Media.DirectShow.IDvbLogicalChannelDescriptor2
    Guid = Guid('1ea8b738-a307-4680-9e-26-d0-a9-08-c8-24-f4')
class IDvbLinkageDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1cdf8b31-994a-46fc-ac-fd-6a-6b-e8-93-4d-d5')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTSId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetONId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetServiceId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetLinkageType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrivateDataLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPrivateData(pbLen: c_char_p_no, pbData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbLogicalChannel2Descriptor(c_void_p):
    extends: win32more.Media.DirectShow.IDvbLogicalChannelDescriptor2
    Guid = Guid('f69c3747-8a30-4980-99-8c-01-fe-7f-0b-a3-5a')
    @commethod(9)
    def GetCountOfLists(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetListId(bListIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetListNameW(bListIndex: Byte, convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetListCountryCode(bListIndex: Byte, pszCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetListCountOfRecords(bChannelListIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetListRecordServiceId(bListIndex: Byte, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetListRecordLogicalChannelNumber(bListIndex: Byte, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetListRecordLogicalChannelAndVisibility(bListIndex: Byte, bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IDvbLogicalChannelDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('cf1edaff-3ffd-4cf7-82-01-35-75-6a-cb-f8-5f')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordServiceId(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordLogicalChannelNumber(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IDvbLogicalChannelDescriptor2(c_void_p):
    extends: win32more.Media.DirectShow.IDvbLogicalChannelDescriptor
    Guid = Guid('43aca974-4be8-4b98-bc-17-9e-af-d7-88-b1-d7')
    @commethod(8)
    def GetRecordLogicalChannelAndVisibility(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IDvbMultilingualServiceNameDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2d80433b-b32c-47ef-98-7f-e7-8e-bb-77-3e-34')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordLangId(bRecordIndex: Byte, ulVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordServiceProviderNameW(bRecordIndex: Byte, convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordServiceNameW(bRecordIndex: Byte, convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDvbNetworkNameDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5b2a80cf-35b9-446c-b3-e4-04-8b-76-1d-bc-51')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkName(pszName: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetNetworkNameW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDvbParentalRatingDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3ad9dde1-fb1b-4186-93-7f-22-e6-b5-a7-2a-10')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordRating(bRecordIndex: Byte, pszCountryCode: c_char_p_no, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbPrivateDataSpecifierDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5660a019-e75a-4b82-9b-4c-ed-22-56-d1-65-a2')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPrivateDataSpecifier(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDvbSatelliteDeliverySystemDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('02f2225a-805b-4ec5-a9-a6-f9-b5-91-3c-d4-70')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFrequency(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetOrbitalPosition(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetWestEastFlag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPolarization(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetModulation(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSymbolRate(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetFECInner(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbServiceAttributeDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0f37bd92-d6a1-4854-b9-50-3a-96-9d-27-f3-0e')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordServiceId(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordNumericSelectionFlag(bRecordIndex: Byte, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordVisibleServiceFlag(bRecordIndex: Byte, pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IDvbServiceDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f9c7fbcf-e2d6-464d-b3-2d-2e-f5-26-e4-92-90')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceProviderName(pszName: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetServiceProviderNameW(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceName(pszName: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetProcessedServiceName(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetServiceNameEmphasized(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDvbServiceDescriptor2(c_void_p):
    extends: win32more.Media.DirectShow.IDvbServiceDescriptor
    Guid = Guid('d6c76506-85ab-487c-9b-2b-36-41-65-11-e4-a2')
    @commethod(11)
    def GetServiceProviderNameW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetServiceNameW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDvbServiceListDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('05db0d8f-6008-491a-ac-d3-70-90-95-27-07-d0')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordServiceId(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordServiceType(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbShortEventDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b170be92-5b75-458e-9c-6e-b0-00-82-31-49-1a')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLanguageCode(pszCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEventNameW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTextW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDvbSiParser(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b758a7bd-14dc-449d-b8-28-35-90-9a-cb-3b-1e')
    @commethod(3)
    def Initialize(punkMpeg2Data: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPAT(ppPAT: POINTER(win32more.Media.DirectShow.IPAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCAT(dwTimeout: UInt32, ppCAT: POINTER(win32more.Media.DirectShow.ICAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPMT(pid: UInt16, pwProgramNumber: POINTER(UInt16), ppPMT: POINTER(win32more.Media.DirectShow.IPMT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTSDT(ppTSDT: POINTER(win32more.Media.DirectShow.ITSDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetNIT(tableId: Byte, pwNetworkId: POINTER(UInt16), ppNIT: POINTER(win32more.Media.DirectShow.IDVB_NIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSDT(tableId: Byte, pwTransportStreamId: POINTER(UInt16), ppSDT: POINTER(win32more.Media.DirectShow.IDVB_SDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetEIT(tableId: Byte, pwServiceId: POINTER(UInt16), ppEIT: POINTER(win32more.Media.DirectShow.IDVB_EIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetBAT(pwBouquetId: POINTER(UInt16), ppBAT: POINTER(win32more.Media.DirectShow.IDVB_BAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRST(dwTimeout: UInt32, ppRST: POINTER(win32more.Media.DirectShow.IDVB_RST_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetST(pid: UInt16, dwTimeout: UInt32, ppST: POINTER(win32more.Media.DirectShow.IDVB_ST_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetTDT(ppTDT: POINTER(win32more.Media.DirectShow.IDVB_TDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetTOT(ppTOT: POINTER(win32more.Media.DirectShow.IDVB_TOT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetDIT(dwTimeout: UInt32, ppDIT: POINTER(win32more.Media.DirectShow.IDVB_DIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetSIT(dwTimeout: UInt32, ppSIT: POINTER(win32more.Media.DirectShow.IDVB_SIT_head)) -> win32more.Foundation.HRESULT: ...
class IDvbSiParser2(c_void_p):
    extends: win32more.Media.DirectShow.IDvbSiParser
    Guid = Guid('0ac5525f-f816-42f4-93-ba-4c-0f-32-f4-6e-54')
    @commethod(18)
    def GetEIT2(tableId: Byte, pwServiceId: POINTER(UInt16), pbSegment: c_char_p_no, ppEIT: POINTER(win32more.Media.DirectShow.IDVB_EIT2_head)) -> win32more.Foundation.HRESULT: ...
class IDvbSubtitlingDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b25fe1d-fa23-4e50-97-84-6d-f8-b2-6f-8a-49')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordLangId(bRecordIndex: Byte, pulVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordSubtitlingType(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordCompositionPageID(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordAncillaryPageID(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IDvbTeletextDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9cd29d47-69c6-4f92-98-a9-21-0a-f1-b7-30-3a')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecordLangId(bRecordIndex: Byte, pulVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordTeletextType(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordMagazineNumber(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordPageNumber(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbTerrestrial2DeliverySystemDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('20ee9be9-cd57-49ab-8f-6e-1d-07-ae-b8-e4-82')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTagExtension(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCentreFrequency(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPLPId(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetT2SystemId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetMultipleInputMode(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetBandwidth(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetGuardInterval(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetTransmissionMode(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCellId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetOtherFrequencyFlag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetTFSFlag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvbTerrestrialDeliverySystemDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ed7e1b91-d12e-420c-b4-1d-a4-9d-84-fe-18-23')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCentreFrequency(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetBandwidth(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetConstellation(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetHierarchyInformation(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCodeRateHPStream(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCodeRateLPStream(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetGuardInterval(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetTransmissionMode(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetOtherFrequencyFlag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IDvdCmd(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5a4a97e4-94ee-4a55-97-51-74-b5-64-3a-a2-7d')
    @commethod(3)
    def WaitForStart() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WaitForEnd() -> win32more.Foundation.HRESULT: ...
class IDvdControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a70efe61-e2a3-11d0-a9-be-00-aa-00-61-be-93')
    @commethod(3)
    def TitlePlay(ulTitle: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ChapterPlay(ulTitle: UInt32, ulChapter: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def TimePlay(ulTitle: UInt32, bcdTime: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def StopForResume() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GoUp() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def TimeSearch(bcdTime: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ChapterSearch(ulChapter: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def PrevPGSearch() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def TopPGSearch() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def NextPGSearch() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ForwardScan(dwSpeed: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def BackwardScan(dwSpeed: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def MenuCall(MenuID: win32more.Media.DirectShow.DVD_MENU_ID) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Resume() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def UpperButtonSelect() -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def LowerButtonSelect() -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def LeftButtonSelect() -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def RightButtonSelect() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def ButtonActivate() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ButtonSelectAndActivate(ulButton: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def StillOff() -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def PauseOn() -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def PauseOff() -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def MenuLanguageSelect(Language: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def AudioStreamChange(ulAudio: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SubpictureStreamChange(ulSubPicture: UInt32, bDisplay: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def AngleChange(ulAngle: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def ParentalLevelSelect(ulParentalLevel: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def ParentalCountrySelect(wCountry: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def KaraokeAudioPresentationModeChange(ulMode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def VideoModePreferrence(ulPreferredDisplayMode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def SetRoot(pszPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def MouseActivate(point: win32more.Foundation.POINT) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def MouseSelect(point: win32more.Foundation.POINT) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def ChapterPlayAutoStop(ulTitle: UInt32, ulChapter: UInt32, ulChaptersToPlay: UInt32) -> win32more.Foundation.HRESULT: ...
class IDvdControl2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('33bc7430-eec0-11d2-82-01-00-a0-c9-d7-48-42')
    @commethod(3)
    def PlayTitle(ulTitle: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PlayChapterInTitle(ulTitle: UInt32, ulChapter: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PlayAtTimeInTitle(ulTitle: UInt32, pStartTime: POINTER(win32more.Media.DirectShow.DVD_HMSF_TIMECODE_head), dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Stop() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ReturnFromSubmenu(dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def PlayAtTime(pTime: POINTER(win32more.Media.DirectShow.DVD_HMSF_TIMECODE_head), dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def PlayChapter(ulChapter: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def PlayPrevChapter(dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ReplayChapter(dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def PlayNextChapter(dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def PlayForwards(dSpeed: Double, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def PlayBackwards(dSpeed: Double, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ShowMenu(MenuID: win32more.Media.DirectShow.DVD_MENU_ID, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Resume(dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SelectRelativeButton(buttonDir: win32more.Media.DirectShow.DVD_RELATIVE_BUTTON) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ActivateButton() -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SelectButton(ulButton: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SelectAndActivateButton(ulButton: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def StillOff() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Pause(bState: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SelectAudioStream(ulAudio: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SelectSubpictureStream(ulSubPicture: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetSubpictureState(bState: win32more.Foundation.BOOL, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def SelectAngle(ulAngle: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SelectParentalLevel(ulParentalLevel: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SelectParentalCountry(bCountry: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SelectKaraokeAudioPresentationMode(ulMode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SelectVideoModePreference(ulPreferredDisplayMode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def SetDVDDirectory(pszwPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def ActivateAtPosition(point: win32more.Foundation.POINT) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def SelectAtPosition(point: win32more.Foundation.POINT) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def PlayChaptersAutoStop(ulTitle: UInt32, ulChapter: UInt32, ulChaptersToPlay: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def AcceptParentalLevelChange(bAccept: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def SetOption(flag: win32more.Media.DirectShow.DVD_OPTION_FLAG, fState: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def SetState(pState: win32more.Media.DirectShow.IDvdState_head, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def PlayPeriodInTitleAutoStop(ulTitle: UInt32, pStartTime: POINTER(win32more.Media.DirectShow.DVD_HMSF_TIMECODE_head), pEndTime: POINTER(win32more.Media.DirectShow.DVD_HMSF_TIMECODE_head), dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def SetGPRM(ulIndex: UInt32, wValue: UInt16, dwFlags: UInt32, ppCmd: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def SelectDefaultMenuLanguage(Language: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def SelectDefaultAudioLanguage(Language: UInt32, audioExtension: win32more.Media.DirectShow.DVD_AUDIO_LANG_EXT) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def SelectDefaultSubpictureLanguage(Language: UInt32, subpictureExtension: win32more.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT) -> win32more.Foundation.HRESULT: ...
class IDvdGraphBuilder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fcc152b6-f372-11d0-8e-00-00-c0-4f-d7-c0-8b')
    @commethod(3)
    def GetFiltergraph(ppGB: POINTER(win32more.Media.DirectShow.IGraphBuilder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDvdInterface(riid: POINTER(Guid), ppvIF: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RenderDvdVideoVolume(lpcwszPathName: win32more.Foundation.PWSTR, dwFlags: UInt32, pStatus: POINTER(win32more.Media.DirectShow.AM_DVD_RENDERSTATUS_head)) -> win32more.Foundation.HRESULT: ...
class IDvdInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a70efe60-e2a3-11d0-a9-be-00-aa-00-61-be-93')
    @commethod(3)
    def GetCurrentDomain(pDomain: POINTER(win32more.Media.DirectShow.DVD_DOMAIN)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentLocation(pLocation: POINTER(win32more.Media.DirectShow.DVD_PLAYBACK_LOCATION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalTitleTime(pulTotalTime: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentButton(pulButtonsAvailable: POINTER(UInt32), pulCurrentButton: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentAngle(pulAnglesAvailable: POINTER(UInt32), pulCurrentAngle: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentAudio(pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentSubpicture(pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32), pIsDisabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentUOPS(pUOP: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetAllSPRMs(pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetAllGPRMs(pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetAudioLanguage(ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetSubpictureLanguage(ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetTitleAttributes(ulTitle: UInt32, pATR: POINTER(win32more.Media.DirectShow.DVD_ATR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetVMGAttributes(pATR: POINTER(win32more.Media.DirectShow.DVD_ATR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetCurrentVideoAttributes(pATR: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetCurrentAudioAttributes(pATR: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetCurrentSubpictureAttributes(pATR: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetCurrentVolumeInfo(pulNumOfVol: POINTER(UInt32), pulThisVolNum: POINTER(UInt32), pSide: POINTER(win32more.Media.DirectShow.DVD_DISC_SIDE), pulNumOfTitles: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetDVDTextInfo(pTextManager: c_char_p_no, ulBufSize: UInt32, pulActualSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetPlayerParentalLevel(pulParentalLevel: POINTER(UInt32), pulCountryCode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetNumberOfChapters(ulTitle: UInt32, pulNumberOfChapters: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetTitleParentalLevels(ulTitle: UInt32, pulParentalLevels: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetRoot(pRoot: win32more.Foundation.PSTR, ulBufSize: UInt32, pulActualSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDvdInfo2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('34151510-eec0-11d2-82-01-00-a0-c9-d7-48-42')
    @commethod(3)
    def GetCurrentDomain(pDomain: POINTER(win32more.Media.DirectShow.DVD_DOMAIN)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentLocation(pLocation: POINTER(win32more.Media.DirectShow.DVD_PLAYBACK_LOCATION2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalTitleTime(pTotalTime: POINTER(win32more.Media.DirectShow.DVD_HMSF_TIMECODE_head), ulTimeCodeFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentButton(pulButtonsAvailable: POINTER(UInt32), pulCurrentButton: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentAngle(pulAnglesAvailable: POINTER(UInt32), pulCurrentAngle: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentAudio(pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentSubpicture(pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32), pbIsDisabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentUOPS(pulUOPs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetAllSPRMs(pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetAllGPRMs(pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetAudioLanguage(ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetSubpictureLanguage(ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetTitleAttributes(ulTitle: UInt32, pMenu: POINTER(win32more.Media.DirectShow.DVD_MenuAttributes_head), pTitle: POINTER(win32more.Media.DirectShow.DVD_TitleAttributes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetVMGAttributes(pATR: POINTER(win32more.Media.DirectShow.DVD_MenuAttributes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetCurrentVideoAttributes(pATR: POINTER(win32more.Media.DirectShow.DVD_VideoAttributes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetAudioAttributes(ulStream: UInt32, pATR: POINTER(win32more.Media.DirectShow.DVD_AudioAttributes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetKaraokeAttributes(ulStream: UInt32, pAttributes: POINTER(win32more.Media.DirectShow.DVD_KaraokeAttributes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetSubpictureAttributes(ulStream: UInt32, pATR: POINTER(win32more.Media.DirectShow.DVD_SubpictureAttributes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetDVDVolumeInfo(pulNumOfVolumes: POINTER(UInt32), pulVolume: POINTER(UInt32), pSide: POINTER(win32more.Media.DirectShow.DVD_DISC_SIDE), pulNumOfTitles: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetDVDTextNumberOfLanguages(pulNumOfLangs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetDVDTextLanguageInfo(ulLangIndex: UInt32, pulNumOfStrings: POINTER(UInt32), pLangCode: POINTER(UInt32), pbCharacterSet: POINTER(win32more.Media.DirectShow.DVD_TextCharSet)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetDVDTextStringAsNative(ulLangIndex: UInt32, ulStringIndex: UInt32, pbBuffer: c_char_p_no, ulMaxBufferSize: UInt32, pulActualSize: POINTER(UInt32), pType: POINTER(win32more.Media.DirectShow.DVD_TextStringType)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetDVDTextStringAsUnicode(ulLangIndex: UInt32, ulStringIndex: UInt32, pchwBuffer: win32more.Foundation.PWSTR, ulMaxBufferSize: UInt32, pulActualSize: POINTER(UInt32), pType: POINTER(win32more.Media.DirectShow.DVD_TextStringType)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetPlayerParentalLevel(pulParentalLevel: POINTER(UInt32), pbCountryCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetNumberOfChapters(ulTitle: UInt32, pulNumOfChapters: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetTitleParentalLevels(ulTitle: UInt32, pulParentalLevels: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetDVDDirectory(pszwPath: win32more.Foundation.PWSTR, ulMaxSize: UInt32, pulActualSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def IsAudioStreamEnabled(ulStreamNum: UInt32, pbEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetDiscID(pszwPath: win32more.Foundation.PWSTR, pullDiscID: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetState(pStateData: POINTER(win32more.Media.DirectShow.IDvdState_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetMenuLanguages(pLanguages: POINTER(UInt32), ulMaxLanguages: UInt32, pulActualLanguages: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetButtonAtPosition(point: win32more.Foundation.POINT, pulButtonIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetCmdFromEvent(lParam1: IntPtr, pCmdObj: POINTER(win32more.Media.DirectShow.IDvdCmd_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetDefaultMenuLanguage(pLanguage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetDefaultAudioLanguage(pLanguage: POINTER(UInt32), pAudioExtension: POINTER(win32more.Media.DirectShow.DVD_AUDIO_LANG_EXT)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetDefaultSubpictureLanguage(pLanguage: POINTER(UInt32), pSubpictureExtension: POINTER(win32more.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetDecoderCaps(pCaps: POINTER(win32more.Media.DirectShow.DVD_DECODER_CAPS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetButtonRect(ulButton: UInt32, pRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def IsSubpictureStreamEnabled(ulStreamNum: UInt32, pbEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IDvdState(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('86303d6d-1c4a-4087-ab-42-f7-11-16-70-48-ef')
    @commethod(3)
    def GetDiscID(pullUniqueID: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentalLevel(pulParentalLevel: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IESCloseMmiEvent(c_void_p):
    extends: win32more.Media.DirectShow.IESEvent
    Guid = Guid('6b80e96f-55e2-45aa-b7-54-0c-23-c8-e7-d5-c1')
    @commethod(8)
    def GetDialogNumber(pDialogNumber: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IESEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1f0e5357-af43-44e6-85-47-65-4c-64-51-45-d2')
    @commethod(3)
    def GetEventId(pdwEventId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetEventType(pguidEventType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetCompletionStatus(dwResult: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetData(pbData: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetStringData(pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IESEventFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('506a09b8-7f86-4e04-ac-05-33-03-bf-e8-fc-49')
    @commethod(3)
    def CreateESEvent(pServiceProvider: win32more.System.Com.IUnknown_head, dwEventId: UInt32, guidEventType: Guid, dwEventDataLength: UInt32, pEventData: c_char_p_no, bstrBaseUrl: win32more.Foundation.BSTR, pInitContext: win32more.System.Com.IUnknown_head, ppESEvent: POINTER(win32more.Media.DirectShow.IESEvent_head)) -> win32more.Foundation.HRESULT: ...
class IESEventService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ed89a619-4c06-4b2f-99-eb-c7-66-9b-13-04-7c')
    @commethod(3)
    def FireESEvent(pESEvent: win32more.Media.DirectShow.IESEvent_head) -> win32more.Foundation.HRESULT: ...
class IESEventServiceConfiguration(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('33b9daae-9309-491d-a0-51-bc-ad-2a-70-cd-66')
    @commethod(3)
    def SetParent(pEventService: win32more.Media.DirectShow.IESEventService_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveParent() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetOwner(pESEvents: win32more.Media.DirectShow.IESEvents_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveOwner() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetGraph(pGraph: win32more.Media.DirectShow.IFilterGraph_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveGraph(pGraph: win32more.Media.DirectShow.IFilterGraph_head) -> win32more.Foundation.HRESULT: ...
class IESEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('abd414bf-cfe5-4e5e-af-5b-4b-4e-49-c5-bf-eb')
    @commethod(3)
    def OnESEventReceived(guidEventType: Guid, pESEvent: win32more.Media.DirectShow.IESEvent_head) -> win32more.Foundation.HRESULT: ...
class IESFileExpiryDateEvent(c_void_p):
    extends: win32more.Media.DirectShow.IESEvent
    Guid = Guid('ba9edcb6-4d36-4cfe-8c-56-87-a6-b0-ca-48-e1')
    @commethod(8)
    def GetTunerId(pguidTunerId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetExpiryDate(pqwExpiryDate: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFinalExpiryDate(pqwExpiryDate: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetMaxRenewalCount(dwMaxRenewalCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def IsEntitlementTokenPresent(pfEntTokenPresent: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def DoesExpireAfterFirstUse(pfExpireAfterFirstUse: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IESIsdbCasResponseEvent(c_void_p):
    extends: win32more.Media.DirectShow.IESEvent
    Guid = Guid('2017cb03-dc0f-4c24-83-ca-36-30-7b-2c-d1-9f')
    @commethod(8)
    def GetRequestId(pRequestId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetStatus(pStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDataLength(pRequestLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetResponseData(pbData: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IESLicenseRenewalResultEvent(c_void_p):
    extends: win32more.Media.DirectShow.IESEvent
    Guid = Guid('d5a48ef5-a81b-4df0-ac-aa-5e-35-e7-ea-45-d4')
    @commethod(8)
    def GetCallersId(pdwCallersId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFileName(pbstrFilename: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsRenewalSuccessful(pfRenewalSuccessful: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def IsCheckEntitlementCallRequired(pfCheckEntTokenCallNeeded: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetDescrambledStatus(pDescrambledStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRenewalResultCode(pdwRenewalResultCode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetCASFailureCode(pdwCASFailureCode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRenewalHResult(phr: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetEntitlementTokenLength(pdwLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetEntitlementToken(pbData: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetExpiryDate(pqwExpiryDate: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class IESOpenMmiEvent(c_void_p):
    extends: win32more.Media.DirectShow.IESEvent
    Guid = Guid('ba4b6526-1a35-4635-8b-56-3e-c6-12-74-6a-8c')
    @commethod(8)
    def GetDialogNumber(pDialogRequest: POINTER(UInt32), pDialogNumber: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDialogType(guidDialogType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDialogData(pbData: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetDialogStringData(pbstrBaseUrl: POINTER(win32more.Foundation.BSTR), pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IESRequestTunerEvent(c_void_p):
    extends: win32more.Media.DirectShow.IESEvent
    Guid = Guid('54c7a5e8-c3bb-4f51-af-14-e0-e2-c0-e3-4c-6d')
    @commethod(8)
    def GetPriority(pbyPriority: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetReason(pbyReason: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetConsequences(pbyConsequences: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetEstimatedTime(pdwEstimatedTime: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IESValueUpdatedEvent(c_void_p):
    extends: win32more.Media.DirectShow.IESEvent
    Guid = Guid('8a24c46e-bb63-4664-86-02-5d-9c-71-8c-14-6d')
    @commethod(8)
    def GetValueNames(pbstrNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IETFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c4c4c4b1-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
    @commethod(3)
    def get_EvalRatObjOK(pHrCoCreateRetVal: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrRating(pEnSystem: POINTER(win32more.Media.DirectShow.EnTvRat_System), pEnRating: POINTER(win32more.Media.DirectShow.EnTvRat_GenericLevel), plbfEnAttr: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrLicenseExpDate(protType: POINTER(win32more.Media.DirectShow.ProtType), lpDateTime: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastErrorCode() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetRecordingOn(fRecState: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IETFilterConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c4c4c4d1-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
    @commethod(3)
    def InitLicense(LicenseId: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSecureChannelObject(ppUnkDRMSecureChannel: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IETFilterEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c4c4c4c1-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
class IEncoderAPI(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('70423839-6acc-4b23-b0-79-21-db-f0-81-56-a5')
    @commethod(3)
    def IsSupported(Api: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def IsAvailable(Api: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetParameterRange(Api: POINTER(Guid), ValueMin: POINTER(win32more.System.Com.VARIANT_head), ValueMax: POINTER(win32more.System.Com.VARIANT_head), SteppingDelta: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetParameterValues(Api: POINTER(Guid), Values: POINTER(POINTER(win32more.System.Com.VARIANT_head)), ValuesCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultValue(Api: POINTER(Guid), Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetValue(Api: POINTER(Guid), Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetValue(Api: POINTER(Guid), Value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IEnumComponentTypes(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8a674b4a-1f63-11d3-b6-4c-00-c0-4f-79-49-8e')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Media.DirectShow.IComponentType_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Media.DirectShow.IEnumComponentTypes_head)) -> win32more.Foundation.HRESULT: ...
class IEnumComponents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2a6e2939-2595-11d3-b6-4c-00-c0-4f-79-49-8e')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Media.DirectShow.IComponent_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Media.DirectShow.IEnumComponents_head)) -> win32more.Foundation.HRESULT: ...
class IEnumFilters(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a86893-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Next(cFilters: UInt32, ppFilter: POINTER(win32more.Media.DirectShow.IBaseFilter_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cFilters: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Media.DirectShow.IEnumFilters_head)) -> win32more.Foundation.HRESULT: ...
class IEnumGuideDataProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ae44423b-4571-475c-ad-2c-f4-0a-77-1d-80-ef')
    @commethod(3)
    def Next(celt: UInt32, ppprop: POINTER(win32more.Media.DirectShow.IGuideDataProperty_head), pcelt: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Media.DirectShow.IEnumGuideDataProperties_head)) -> win32more.Foundation.HRESULT: ...
class IEnumMSVidGraphSegment(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3dd2903e-e0aa-11d2-b6-3a-00-c0-4f-79-49-8e')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Media.DirectShow.IMSVidGraphSegment_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Media.DirectShow.IEnumMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
class IEnumMediaTypes(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('89c31040-846b-11ce-97-d3-00-aa-00-55-59-5a')
    @commethod(3)
    def Next(cMediaTypes: UInt32, ppMediaTypes: POINTER(POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cMediaTypes: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Media.DirectShow.IEnumMediaTypes_head)) -> win32more.Foundation.HRESULT: ...
class IEnumPIDMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('afb6c2a2-2c41-11d3-8a-60-00-00-f8-1e-0e-4a')
    @commethod(3)
    def Next(cRequest: UInt32, pPIDMap: POINTER(win32more.Media.DirectShow.PID_MAP_head), pcReceived: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cRecords: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppIEnumPIDMap: POINTER(win32more.Media.DirectShow.IEnumPIDMap_head)) -> win32more.Foundation.HRESULT: ...
class IEnumPins(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a86892-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Next(cPins: UInt32, ppPins: POINTER(win32more.Media.DirectShow.IPin_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cPins: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Media.DirectShow.IEnumPins_head)) -> win32more.Foundation.HRESULT: ...
class IEnumRegFilters(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868a4-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Next(cFilters: UInt32, apRegFilter: POINTER(POINTER(win32more.Media.DirectShow.REGFILTER_head)), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cFilters: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Media.DirectShow.IEnumRegFilters_head)) -> win32more.Foundation.HRESULT: ...
class IEnumStreamBufferRecordingAttrib(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c18a9162-1e82-4142-8c-73-56-90-fa-62-fe-33')
    @commethod(3)
    def Next(cRequest: UInt32, pStreamBufferAttribute: POINTER(win32more.Media.DirectShow.STREAMBUFFER_ATTRIBUTE_head), pcReceived: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cRecords: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppIEnumStreamBufferAttrib: POINTER(win32more.Media.DirectShow.IEnumStreamBufferRecordingAttrib_head)) -> win32more.Foundation.HRESULT: ...
class IEnumStreamIdMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('945c1566-6202-46fc-96-c7-d8-7f-28-9c-65-34')
    @commethod(3)
    def Next(cRequest: UInt32, pStreamIdMap: POINTER(win32more.Media.DirectShow.STREAM_ID_MAP_head), pcReceived: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cRecords: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppIEnumStreamIdMap: POINTER(win32more.Media.DirectShow.IEnumStreamIdMap_head)) -> win32more.Foundation.HRESULT: ...
class IEnumTuneRequests(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1993299c-ced6-4788-87-a3-42-00-67-dc-e0-c7')
    @commethod(3)
    def Next(celt: UInt32, ppprop: POINTER(win32more.Media.DirectShow.ITuneRequest_head), pcelt: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Media.DirectShow.IEnumTuneRequests_head)) -> win32more.Foundation.HRESULT: ...
class IEnumTuningSpaces(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8b8eb248-fc2b-11d2-9d-8c-00-c0-4f-72-d9-80')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Media.DirectShow.ITuningSpace_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Media.DirectShow.IEnumTuningSpaces_head)) -> win32more.Foundation.HRESULT: ...
class IEvalRat(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c5c5c5b1-3abc-11d6-b2-5b-00-c0-4f-a0-c0-26')
    @commethod(7)
    def get_BlockedRatingAttributes(enSystem: win32more.Media.DirectShow.EnTvRat_System, enLevel: win32more.Media.DirectShow.EnTvRat_GenericLevel, plbfAttrs: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_BlockedRatingAttributes(enSystem: win32more.Media.DirectShow.EnTvRat_System, enLevel: win32more.Media.DirectShow.EnTvRat_GenericLevel, lbfAttrs: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_BlockUnRated(pfBlockUnRatedShows: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_BlockUnRated(fBlockUnRatedShows: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def MostRestrictiveRating(enSystem1: win32more.Media.DirectShow.EnTvRat_System, enEnLevel1: win32more.Media.DirectShow.EnTvRat_GenericLevel, lbfEnAttr1: Int32, enSystem2: win32more.Media.DirectShow.EnTvRat_System, enEnLevel2: win32more.Media.DirectShow.EnTvRat_GenericLevel, lbfEnAttr2: Int32, penSystem: POINTER(win32more.Media.DirectShow.EnTvRat_System), penEnLevel: POINTER(win32more.Media.DirectShow.EnTvRat_GenericLevel), plbfEnAttr: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def TestRating(enShowSystem: win32more.Media.DirectShow.EnTvRat_System, enShowLevel: win32more.Media.DirectShow.EnTvRat_GenericLevel, lbfEnShowAttributes: Int32) -> win32more.Foundation.HRESULT: ...
IFILTERMAPPER_MERIT = Int32
MERIT_PREFERRED: IFILTERMAPPER_MERIT = 8388608
MERIT_NORMAL: IFILTERMAPPER_MERIT = 6291456
MERIT_UNLIKELY: IFILTERMAPPER_MERIT = 4194304
MERIT_DO_NOT_USE: IFILTERMAPPER_MERIT = 2097152
MERIT_SW_COMPRESSOR: IFILTERMAPPER_MERIT = 1048576
MERIT_HW_COMPRESSOR: IFILTERMAPPER_MERIT = 1048656
class IFileSinkFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a2104830-7c70-11cf-8b-ce-00-aa-00-a3-f1-a6')
    @commethod(3)
    def SetFileName(pszFileName: win32more.Foundation.PWSTR, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurFile(ppszFileName: POINTER(win32more.Foundation.PWSTR), pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
class IFileSinkFilter2(c_void_p):
    extends: win32more.Media.DirectShow.IFileSinkFilter
    Guid = Guid('00855b90-ce1b-11d0-bd-4f-00-a0-c9-11-ce-86')
    @commethod(5)
    def SetMode(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMode(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IFileSourceFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868a6-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Load(pszFileName: win32more.Foundation.PWSTR, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurFile(ppszFileName: POINTER(win32more.Foundation.PWSTR), pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
class IFilterChain(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcfbdcf6-0dc2-45f5-9a-b2-7c-33-0e-a0-9c-29')
    @commethod(3)
    def StartChain(pStartFilter: win32more.Media.DirectShow.IBaseFilter_head, pEndFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PauseChain(pStartFilter: win32more.Media.DirectShow.IBaseFilter_head, pEndFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def StopChain(pStartFilter: win32more.Media.DirectShow.IBaseFilter_head, pEndFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveChain(pStartFilter: win32more.Media.DirectShow.IBaseFilter_head, pEndFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
class IFilterGraph(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a8689f-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def AddFilter(pFilter: win32more.Media.DirectShow.IBaseFilter_head, pName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveFilter(pFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumFilters(ppEnum: POINTER(win32more.Media.DirectShow.IEnumFilters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FindFilterByName(pName: win32more.Foundation.PWSTR, ppFilter: POINTER(win32more.Media.DirectShow.IBaseFilter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ConnectDirect(ppinOut: win32more.Media.DirectShow.IPin_head, ppinIn: win32more.Media.DirectShow.IPin_head, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Reconnect(ppin: win32more.Media.DirectShow.IPin_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Disconnect(ppin: win32more.Media.DirectShow.IPin_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetDefaultSyncSource() -> win32more.Foundation.HRESULT: ...
class IFilterGraph2(c_void_p):
    extends: win32more.Media.DirectShow.IGraphBuilder
    Guid = Guid('36b73882-c2c8-11cf-8b-46-00-80-5f-6c-ef-60')
    @commethod(18)
    def AddSourceFilterForMoniker(pMoniker: win32more.System.Com.IMoniker_head, pCtx: win32more.System.Com.IBindCtx_head, lpcwstrFilterName: win32more.Foundation.PWSTR, ppFilter: POINTER(win32more.Media.DirectShow.IBaseFilter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ReconnectEx(ppin: win32more.Media.DirectShow.IPin_head, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def RenderEx(pPinOut: win32more.Media.DirectShow.IPin_head, dwFlags: UInt32, pvContext: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IFilterGraph3(c_void_p):
    extends: win32more.Media.DirectShow.IFilterGraph2
    Guid = Guid('aaf38154-b80b-422f-91-e6-b6-64-67-50-9a-07')
    @commethod(21)
    def SetSyncSourceEx(pClockForMostOfFilterGraph: win32more.Media.IReferenceClock_head, pClockForFilter: win32more.Media.IReferenceClock_head, pFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
class IFilterInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868ba-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def FindPin(strPinID: win32more.Foundation.BSTR, ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(strName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_VendorInfo(strVendorInfo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Filter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Pins(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsFileSource(pbIsSource: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Filename(pstrFilename: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Filename(strFilename: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFilterMapper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868a3-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def RegisterFilter(clsid: Guid, Name: win32more.Foundation.PWSTR, dwMerit: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterFilterInstance(clsid: Guid, Name: win32more.Foundation.PWSTR, MRId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterPin(Filter: Guid, Name: win32more.Foundation.PWSTR, bRendered: win32more.Foundation.BOOL, bOutput: win32more.Foundation.BOOL, bZero: win32more.Foundation.BOOL, bMany: win32more.Foundation.BOOL, ConnectsToFilter: Guid, ConnectsToPin: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RegisterPinType(clsFilter: Guid, strName: win32more.Foundation.PWSTR, clsMajorType: Guid, clsSubType: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterFilter(Filter: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def UnregisterFilterInstance(MRId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterPin(Filter: Guid, Name: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EnumMatchingFilters(ppEnum: POINTER(win32more.Media.DirectShow.IEnumRegFilters_head), dwMerit: UInt32, bInputNeeded: win32more.Foundation.BOOL, clsInMaj: Guid, clsInSub: Guid, bRender: win32more.Foundation.BOOL, bOututNeeded: win32more.Foundation.BOOL, clsOutMaj: Guid, clsOutSub: Guid) -> win32more.Foundation.HRESULT: ...
class IFilterMapper2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b79bb0b0-33c1-11d1-ab-e1-00-a0-c9-05-f3-75')
    @commethod(3)
    def CreateCategory(clsidCategory: POINTER(Guid), dwCategoryMerit: UInt32, Description: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterFilter(pclsidCategory: POINTER(Guid), szInstance: win32more.Foundation.PWSTR, Filter: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterFilter(clsidFilter: POINTER(Guid), Name: win32more.Foundation.PWSTR, ppMoniker: POINTER(win32more.System.Com.IMoniker_head), pclsidCategory: POINTER(Guid), szInstance: win32more.Foundation.PWSTR, prf2: POINTER(win32more.Media.DirectShow.REGFILTER2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumMatchingFilters(ppEnum: POINTER(win32more.System.Com.IEnumMoniker_head), dwFlags: UInt32, bExactMatch: win32more.Foundation.BOOL, dwMerit: UInt32, bInputNeeded: win32more.Foundation.BOOL, cInputTypes: UInt32, pInputTypes: POINTER(Guid), pMedIn: POINTER(win32more.Media.DirectShow.REGPINMEDIUM_head), pPinCategoryIn: POINTER(Guid), bRender: win32more.Foundation.BOOL, bOutputNeeded: win32more.Foundation.BOOL, cOutputTypes: UInt32, pOutputTypes: POINTER(Guid), pMedOut: POINTER(win32more.Media.DirectShow.REGPINMEDIUM_head), pPinCategoryOut: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IFilterMapper3(c_void_p):
    extends: win32more.Media.DirectShow.IFilterMapper2
    Guid = Guid('b79bb0b1-33c1-11d1-ab-e1-00-a0-c9-05-f3-75')
    @commethod(7)
    def GetICreateDevEnum(ppEnum: POINTER(win32more.Media.DirectShow.ICreateDevEnum_head)) -> win32more.Foundation.HRESULT: ...
class IFrequencyMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('06fb45c1-693c-4ea7-b7-9f-7a-6a-54-d8-de-f2')
    @commethod(3)
    def get_FrequencyMapping(ulCount: POINTER(UInt32), ppulList: POINTER(POINTER(UInt32))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_FrequencyMapping(ulCount: UInt32, pList: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_CountryCode(pulCountryCode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_CountryCode(ulCountryCode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_DefaultFrequencyMapping(ulCountryCode: UInt32, pulCount: POINTER(UInt32), ppulList: POINTER(POINTER(UInt32))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_CountryCodeList(pulCount: POINTER(UInt32), ppulList: POINTER(POINTER(UInt32))) -> win32more.Foundation.HRESULT: ...
class IFullScreenVideo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dd1d7110-7836-11cf-bf-47-00-aa-00-55-59-5a')
    @commethod(3)
    def CountModes(pModes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetModeInfo(Mode: Int32, pWidth: POINTER(Int32), pHeight: POINTER(Int32), pDepth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentMode(pMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsModeAvailable(Mode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def IsModeEnabled(Mode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetEnabled(Mode: Int32, bEnabled: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetClipFactor(pClipFactor: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetClipFactor(ClipFactor: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetMessageDrain(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetMessageDrain(hwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetMonitor(Monitor: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetMonitor(Monitor: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def HideOnDeactivate(Hide: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def IsHideOnDeactivate() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetCaption(strCaption: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetCaption(pstrCaption: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetDefault() -> win32more.Foundation.HRESULT: ...
class IFullScreenVideoEx(c_void_p):
    extends: win32more.Media.DirectShow.IFullScreenVideo
    Guid = Guid('53479470-f1dd-11cf-bc-42-00-aa-00-ac-74-f6')
    @commethod(20)
    def SetAcceleratorTable(hwnd: win32more.Foundation.HWND, hAccel: win32more.UI.WindowsAndMessaging.HACCEL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetAcceleratorTable(phwnd: POINTER(win32more.Foundation.HWND), phAccel: POINTER(win32more.UI.WindowsAndMessaging.HACCEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def KeepPixelAspectRatio(KeepAspect: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def IsKeepPixelAspectRatio(pKeepAspect: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IGenericDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6a5918f8-a77a-4f61-ae-d0-57-02-bd-cd-a3-e6')
    @commethod(3)
    def Initialize(pbDesc: c_char_p_no, bCount: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetBody(ppbVal: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IGenericDescriptor2(c_void_p):
    extends: win32more.Media.DirectShow.IGenericDescriptor
    Guid = Guid('bf02fb7e-9792-4e10-a6-8d-03-3a-2c-c2-46-a5')
    @commethod(7)
    def Initialize(pbDesc: c_char_p_no, wCount: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetLength(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IGetCapabilitiesKey(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a8809222-07bb-48ea-95-1c-33-15-81-00-62-5b')
    @commethod(3)
    def GetCapabilitiesKey(pHKey: POINTER(win32more.System.Registry.HKEY)) -> win32more.Foundation.HRESULT: ...
class IGpnvsCommonBase(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('907e0b5c-e42d-4f04-91-f0-26-f4-01-f3-69-07')
    @commethod(3)
    def GetValueUpdateName(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IGraphBuilder(c_void_p):
    extends: win32more.Media.DirectShow.IFilterGraph
    Guid = Guid('56a868a9-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(11)
    def Connect(ppinOut: win32more.Media.DirectShow.IPin_head, ppinIn: win32more.Media.DirectShow.IPin_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Render(ppinOut: win32more.Media.DirectShow.IPin_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def RenderFile(lpcwstrFile: win32more.Foundation.PWSTR, lpcwstrPlayList: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def AddSourceFilter(lpcwstrFileName: win32more.Foundation.PWSTR, lpcwstrFilterName: win32more.Foundation.PWSTR, ppFilter: POINTER(win32more.Media.DirectShow.IBaseFilter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetLogFile(hFile: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Abort() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ShouldOperationContinue() -> win32more.Foundation.HRESULT: ...
class IGraphConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('03a1eb8e-32bf-4245-85-02-11-4d-08-a9-cb-88')
    @commethod(3)
    def Reconnect(pOutputPin: win32more.Media.DirectShow.IPin_head, pInputPin: win32more.Media.DirectShow.IPin_head, pmtFirstConnection: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), pUsingFilter: win32more.Media.DirectShow.IBaseFilter_head, hAbortEvent: win32more.Foundation.HANDLE, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reconfigure(pCallback: win32more.Media.DirectShow.IGraphConfigCallback_head, pvContext: c_void_p, dwFlags: UInt32, hAbortEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddFilterToCache(pFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumCacheFilter(pEnum: POINTER(win32more.Media.DirectShow.IEnumFilters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveFilterFromCache(pFilter: win32more.Media.DirectShow.IBaseFilter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetStartTime(prtStart: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def PushThroughData(pOutputPin: win32more.Media.DirectShow.IPin_head, pConnection: win32more.Media.DirectShow.IPinConnection_head, hEventAbort: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetFilterFlags(pFilter: win32more.Media.DirectShow.IBaseFilter_head, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetFilterFlags(pFilter: win32more.Media.DirectShow.IBaseFilter_head, pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveFilterEx(pFilter: win32more.Media.DirectShow.IBaseFilter_head, Flags: UInt32) -> win32more.Foundation.HRESULT: ...
class IGraphConfigCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ade0fd60-d19d-11d2-ab-f6-00-a0-c9-05-f3-75')
    @commethod(3)
    def Reconfigure(pvContext: c_void_p, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IGraphVersion(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868ab-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def QueryVersion(pVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IGuideData(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('61571138-5b01-43cd-ae-af-60-b7-84-a0-bf-93')
    @commethod(3)
    def GetServices(ppEnumTuneRequests: POINTER(win32more.Media.DirectShow.IEnumTuneRequests_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetServiceProperties(pTuneRequest: win32more.Media.DirectShow.ITuneRequest_head, ppEnumProperties: POINTER(win32more.Media.DirectShow.IEnumGuideDataProperties_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetGuideProgramIDs(pEnumPrograms: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetProgramProperties(varProgramDescriptionID: win32more.System.Com.VARIANT, ppEnumProperties: POINTER(win32more.Media.DirectShow.IEnumGuideDataProperties_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetScheduleEntryIDs(pEnumScheduleEntries: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetScheduleEntryProperties(varScheduleEntryDescriptionID: win32more.System.Com.VARIANT, ppEnumProperties: POINTER(win32more.Media.DirectShow.IEnumGuideDataProperties_head)) -> win32more.Foundation.HRESULT: ...
class IGuideDataEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('efda0c80-f395-42c3-9b-3c-56-b3-7d-ec-7b-b7')
    @commethod(3)
    def GuideDataAcquired() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ProgramChanged(varProgramDescriptionID: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ServiceChanged(varServiceDescriptionID: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ScheduleEntryChanged(varScheduleEntryDescriptionID: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ProgramDeleted(varProgramDescriptionID: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ServiceDeleted(varServiceDescriptionID: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ScheduleDeleted(varScheduleEntryDescriptionID: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IGuideDataLoader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4764ff7c-fa95-4525-af-4d-d3-22-36-db-9e-38')
    @commethod(3)
    def Init(pGuideStore: win32more.Media.DirectShow.IGuideData_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate() -> win32more.Foundation.HRESULT: ...
class IGuideDataProperty(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('88ec5e58-bb73-41d6-99-ce-66-c5-24-b8-b5-91')
    @commethod(3)
    def get_Name(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Language(idLang: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Value(pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IIPDVDec(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b8e8bd60-0bfe-11d0-af-91-00-aa-00-b6-7a-42')
    @commethod(3)
    def get_IPDisplay(displayPix: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_IPDisplay(displayPix: Int32) -> win32more.Foundation.HRESULT: ...
class IISDBSLocator(c_void_p):
    extends: win32more.Media.DirectShow.IDVBSLocator
    Guid = Guid('c9897087-e29c-473f-9e-4b-70-72-12-3d-ea-14')
class IISDB_BIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('537cd71e-0e46-4173-90-01-ba-04-3f-3e-49-e2')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetOriginalNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetBroadcastViewPropriety(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordBroadcasterId(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IISDB_CDT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('25fa92c2-8b80-4787-a8-41-3a-0e-8f-17-98-4b')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head, bSectionNumber: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDownloadDataId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSectionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetDataType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetSizeOfDataModule(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDataModule(pbData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IISDB_EMM(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0edb556d-43ad-4938-96-68-32-1b-2f-fe-cf-d3')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTableIdExtension(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDataBytes(pwBufferLength: POINTER(UInt16), pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSharedEmmMessage(pwLength: POINTER(UInt16), ppbMessage: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetIndividualEmmMessage(pUnknown: win32more.System.Com.IUnknown_head, pwLength: POINTER(UInt16), ppbMessage: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IISDB_LDT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('141a546b-02ff-4fb9-a3-a3-2f-07-4b-74-a9-a9')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetOriginalServiceId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransportStreamId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordDescriptionId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IISDB_NBIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1b1863ef-08f1-40b7-a5-59-3b-1e-ff-8c-af-a6')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetOriginalNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordInformationId(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordInformationType(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordDescriptionBodyLocation(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordMessageSectionNumber(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordUserDefined(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordNumberOfKeys(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordKeys(dwRecordIndex: UInt32, pbKeys: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IISDB_SDT(c_void_p):
    extends: win32more.Media.DirectShow.IDVB_SDT
    Guid = Guid('3f3dc9a2-bb32-4fb9-ae-9e-d8-56-84-89-27-a3')
    @commethod(21)
    def GetRecordEITUserDefinedFlags(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IISDB_SDTT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ee60ef2d-813a-4dc7-bf-92-ea-13-da-c8-53-13')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTableIdExt(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransportStreamId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetOriginalNetworkId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordGroup(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordTargetVersion(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordNewVersion(dwRecordIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDownloadLevel(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordVersionIndicator(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordScheduleTimeShiftInformation(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordCountOfSchedules(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordStartTimeByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, pmdtVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecordDurationByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, pmdVal: POINTER(win32more.Media.DirectShow.MPEG_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetVersionHash(pdwVersionHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IIsdbAudioComponentDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('679d2002-2425-4be4-a4-c7-d6-63-2a-57-4f-4d')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamContent(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetComponentTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSimulcastGroupTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetESMultiLingualFlag(pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetMainComponentFlag(pfVal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetQualityIndicator(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetSamplingRate(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetLanguageCode(pszCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetLanguageCode2(pszCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetTextW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IIsdbCAContractInformationDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('08e18b25-a28f-4e92-82-1e-4f-ce-d5-cc-22-91')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCASystemId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCAUnitId(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordComponentTag(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetContractVerificationInfoLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetContractVerificationInfo(bBufLength: Byte, pbBuf: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetFeeNameW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IIsdbCADescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0570aa47-52bc-42ae-8c-a5-96-9f-41-e8-1a-ea')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCASystemId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetReservedBits(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCAPID(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPrivateDataBytes(pbBufferLength: c_char_p_no, pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IIsdbCAServiceDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('39cbeb97-ff0b-42a7-9a-b9-7b-9c-fe-70-a7-7a')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCASystemId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCABroadcasterGroupId(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetMessageControl(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceIds(pbNumServiceIds: c_char_p_no, pwServiceIds: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IIsdbComponentGroupDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a494f17f-c592-47d8-89-43-64-c9-a3-4b-e7-b9')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetComponentGroupType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordGroupId(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordNumberOfCAUnit(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordCAUnitCAUnitId(bRecordIndex: Byte, bCAUnitIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordCAUnitNumberOfComponents(bRecordIndex: Byte, bCAUnitIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordCAUnitComponentTag(bRecordIndex: Byte, bCAUnitIndex: Byte, bComponentIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordTotalBitRate(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordTextW(bRecordIndex: Byte, convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IIsdbDataContentDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a428100a-e646-4bd6-aa-14-60-87-bd-c0-8c-d5')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataComponentId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEntryComponent(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSelectorLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelectorBytes(bBufLength: Byte, pbBuf: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordComponentRef(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetLanguageCode(pszCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetTextW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IIsdbDigitalCopyControlDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1a28417e-266a-4bb8-a4-bd-d7-82-bc-fb-81-61')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCopyControl(pbDigitalRecordingControlData: c_char_p_no, pbCopyControlType: c_char_p_no, pbAPSControlData: c_char_p_no, pbMaximumBitrate: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordCopyControl(bRecordIndex: Byte, pbComponentTag: c_char_p_no, pbDigitalRecordingControlData: c_char_p_no, pbCopyControlType: c_char_p_no, pbAPSControlData: c_char_p_no, pbMaximumBitrate: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IIsdbDownloadContentDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5298661e-cb88-4f5f-a1-de-5f-44-0c-18-5b-92')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(pfReboot: POINTER(win32more.Foundation.BOOL), pfAddOn: POINTER(win32more.Foundation.BOOL), pfCompatibility: POINTER(win32more.Foundation.BOOL), pfModuleInfo: POINTER(win32more.Foundation.BOOL), pfTextInfo: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentSize(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDownloadId(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTimeOutValueDII(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLeakRate(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetComponentTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetCompatiblityDescriptorLength(pwLength: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetCompatiblityDescriptor(ppbData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCountOfRecords(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordModuleId(wRecordIndex: UInt16, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordModuleSize(wRecordIndex: UInt16, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetRecordModuleInfoLength(wRecordIndex: UInt16, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetRecordModuleInfo(wRecordIndex: UInt16, ppbData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetTextLanguageCode(szCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetTextW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IIsdbEmergencyInformationDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ba6fa681-b973-4da1-92-07-ac-3e-7f-03-41-eb')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceId(bRecordIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetStartEndFlag(bRecordIndex: Byte, pVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignalLevel(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetAreaCode(bRecordIndex: Byte, ppwVal: POINTER(POINTER(UInt16)), pbNumAreaCodes: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IIsdbEventGroupDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('94b06780-2e2a-44dc-a9-66-cc-56-fd-ab-c6-c2')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetGroupType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordEvent(bRecordIndex: Byte, pwServiceId: POINTER(UInt16), pwEventId: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRefRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRefRecordEvent(bRecordIndex: Byte, pwOriginalNetworkId: POINTER(UInt16), pwTransportStreamId: POINTER(UInt16), pwServiceId: POINTER(UInt16), pwEventId: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IIsdbHierarchicalTransmissionDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b7b3ae90-ee0b-446d-87-69-f7-e2-aa-26-6a-a6')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFutureUse1(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetQualityLevel(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFutureUse2(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetReferencePid(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IIsdbLogoTransmissionDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e0103f49-4ae1-4f07-90-98-75-6d-b1-fa-88-cd')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLogoTransmissionType(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetLogoId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetLogoVersion(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetDownloadDataId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLogoCharW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrChar: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IIsdbSIParameterDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f837dc36-867c-426a-91-11-f6-20-93-95-1a-45')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetParameterVersion(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetUpdateTime(pVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordNumberOfTable(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableId(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptionLength(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetTableDescriptionBytes(bRecordIndex: Byte, pbBufferLength: c_char_p_no, pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IIsdbSeriesDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('07ef6370-1660-4f26-87-fc-61-4a-da-b2-4b-11')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSeriesId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRepeatLabel(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetProgramPattern(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetExpireDate(pfValid: POINTER(win32more.Foundation.BOOL), pmdtVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetEpisodeNumber(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetLastEpisodeNumber(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSeriesNameW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IIsdbSiParser2(c_void_p):
    extends: win32more.Media.DirectShow.IDvbSiParser2
    Guid = Guid('900e4bb7-18cd-453f-98-be-3b-e6-aa-21-17-72')
    @commethod(19)
    def GetSDT(tableId: Byte, pwTransportStreamId: POINTER(UInt16), ppSDT: POINTER(win32more.Media.DirectShow.IISDB_SDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetBIT(tableId: Byte, pwOriginalNetworkId: POINTER(UInt16), ppBIT: POINTER(win32more.Media.DirectShow.IISDB_BIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetNBIT(tableId: Byte, pwOriginalNetworkId: POINTER(UInt16), ppNBIT: POINTER(win32more.Media.DirectShow.IISDB_NBIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetLDT(tableId: Byte, pwOriginalServiceId: POINTER(UInt16), ppLDT: POINTER(win32more.Media.DirectShow.IISDB_LDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetSDTT(tableId: Byte, pwTableIdExt: POINTER(UInt16), ppSDTT: POINTER(win32more.Media.DirectShow.IISDB_SDTT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetCDT(tableId: Byte, bSectionNumber: Byte, pwDownloadDataId: POINTER(UInt16), ppCDT: POINTER(win32more.Media.DirectShow.IISDB_CDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetEMM(pid: UInt16, wTableIdExt: UInt16, ppEMM: POINTER(win32more.Media.DirectShow.IISDB_EMM_head)) -> win32more.Foundation.HRESULT: ...
class IIsdbTSInformationDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d7ad183e-38f5-4210-b5-5f-ec-8d-60-1b-bd-47')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRemoteControlKeyId(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTSNameW(convMode: win32more.Media.DirectShow.DVB_STRCONV_MODE, pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordTransmissionTypeInfo(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordNumberOfServices(bRecordIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordServiceIdByIndex(bRecordIndex: Byte, bServiceIndex: Byte, pdwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IIsdbTerrestrialDeliverySystemDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('39fae0a6-d151-44dd-a2-8a-76-5d-e5-99-16-70')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAreaCode(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetGuardInterval(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransmissionMode(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCountOfRecords(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordFrequency(bRecordIndex: Byte, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IKsNodeControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('11737c14-24a7-4bb5-81-a0-0d-00-38-13-b0-c4')
    @commethod(3)
    def put_NodeId(dwNodeId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_KsControl(pKsControl: c_void_p) -> win32more.Foundation.HRESULT: ...
class IKsTopologyInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('720d4ac0-7533-11d0-a5-d6-28-db-04-c1-00-00')
    @commethod(3)
    def get_NumCategories(pdwNumCategories: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Category(dwIndex: UInt32, pCategory: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_NumConnections(pdwNumConnections: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_ConnectionInfo(dwIndex: UInt32, pConnectionInfo: POINTER(win32more.Media.KernelStreaming.KSTOPOLOGY_CONNECTION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_NodeName(dwNodeId: UInt32, pwchNodeName: win32more.Foundation.PWSTR, dwBufSize: UInt32, pdwNameLen: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_NumNodes(pdwNumNodes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_NodeType(dwNodeId: UInt32, pNodeType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateNodeInstance(dwNodeId: UInt32, iid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ILanguageComponentType(c_void_p):
    extends: win32more.Media.DirectShow.IComponentType
    Guid = Guid('b874c8ba-0fa2-11d3-9d-8e-00-c0-4f-72-d9-80')
    @commethod(24)
    def get_LangID(LangID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_LangID(LangID: Int32) -> win32more.Foundation.HRESULT: ...
class ILocator(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('286d7f89-760c-4f89-80-c4-66-84-1d-25-07-aa')
    @commethod(7)
    def get_CarrierFrequency(Frequency: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_CarrierFrequency(Frequency: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_InnerFEC(FEC: POINTER(win32more.Media.DirectShow.FECMethod)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_InnerFEC(FEC: win32more.Media.DirectShow.FECMethod) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_InnerFECRate(FEC: POINTER(win32more.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_InnerFECRate(FEC: win32more.Media.DirectShow.BinaryConvolutionCodeRate) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_OuterFEC(FEC: POINTER(win32more.Media.DirectShow.FECMethod)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_OuterFEC(FEC: win32more.Media.DirectShow.FECMethod) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_OuterFECRate(FEC: POINTER(win32more.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_OuterFECRate(FEC: win32more.Media.DirectShow.BinaryConvolutionCodeRate) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Modulation(Modulation: POINTER(win32more.Media.DirectShow.ModulationType)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Modulation(Modulation: win32more.Media.DirectShow.ModulationType) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_SymbolRate(Rate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_SymbolRate(Rate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Clone(NewLocator: POINTER(win32more.Media.DirectShow.ILocator_head)) -> win32more.Foundation.HRESULT: ...
class IMPEG2Component(c_void_p):
    extends: win32more.Media.DirectShow.IComponent
    Guid = Guid('1493e353-1eb6-473c-80-2d-8e-6b-8e-c9-d2-a9')
    @commethod(16)
    def get_PID(PID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_PID(PID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_PCRPID(PCRPID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_PCRPID(PCRPID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_ProgramNumber(ProgramNumber: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_ProgramNumber(ProgramNumber: Int32) -> win32more.Foundation.HRESULT: ...
class IMPEG2ComponentType(c_void_p):
    extends: win32more.Media.DirectShow.ILanguageComponentType
    Guid = Guid('2c073d84-b51c-48c9-aa-9f-68-97-1e-1f-6e-38')
    @commethod(26)
    def get_StreamType(MP2StreamType: POINTER(win32more.Media.DirectShow.MPEG2StreamType)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_StreamType(MP2StreamType: win32more.Media.DirectShow.MPEG2StreamType) -> win32more.Foundation.HRESULT: ...
class IMPEG2PIDMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('afb6c2a1-2c41-11d3-8a-60-00-00-f8-1e-0e-4a')
    @commethod(3)
    def MapPID(culPID: UInt32, pulPID: POINTER(UInt32), MediaSampleContent: win32more.Media.DirectShow.MEDIA_SAMPLE_CONTENT) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnmapPID(culPID: UInt32, pulPID: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumPIDMap(pIEnumPIDMap: POINTER(win32more.Media.DirectShow.IEnumPIDMap_head)) -> win32more.Foundation.HRESULT: ...
class IMPEG2StreamIdMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d0e04c47-25b8-4369-92-5a-36-2a-01-d9-54-44')
    @commethod(3)
    def MapStreamId(ulStreamId: UInt32, MediaSampleContent: UInt32, ulSubstreamFilterValue: UInt32, iDataOffset: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnmapStreamId(culStreamId: UInt32, pulStreamId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumStreamIdMap(ppIEnumStreamIdMap: POINTER(win32more.Media.DirectShow.IEnumStreamIdMap_head)) -> win32more.Foundation.HRESULT: ...
class IMPEG2TuneRequest(c_void_p):
    extends: win32more.Media.DirectShow.ITuneRequest
    Guid = Guid('eb7d987f-8a01-42ad-b8-ae-57-4d-ee-e4-4d-1a')
    @commethod(12)
    def get_TSID(TSID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_TSID(TSID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_ProgNo(ProgNo: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_ProgNo(ProgNo: Int32) -> win32more.Foundation.HRESULT: ...
class IMPEG2TuneRequestFactory(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('14e11abd-ee37-4893-9e-a1-69-64-de-93-3e-39')
    @commethod(7)
    def CreateTuneRequest(TuningSpace: win32more.Media.DirectShow.ITuningSpace_head, TuneRequest: POINTER(win32more.Media.DirectShow.IMPEG2TuneRequest_head)) -> win32more.Foundation.HRESULT: ...
class IMPEG2TuneRequestSupport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1b9d5fc3-5bbc-4b6c-bb-18-b9-d1-0e-3e-ee-bf')
class IMPEG2_TIF_CONTROL(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f9bac2f9-4149-4916-b2-ef-fa-a2-02-32-68-62')
    @commethod(3)
    def RegisterTIF(pUnkTIF: win32more.System.Com.IUnknown_head, ppvRegistrationContext: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterTIF(pvRegistrationContext: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddPIDs(ulcPIDs: UInt32, pulPIDs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DeletePIDs(ulcPIDs: UInt32, pulPIDs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPIDCount(pulcPIDs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPIDs(pulcPIDs: POINTER(UInt32), pulPIDs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMSEventBinder(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c3a9f406-2222-436d-86-d5-ba-32-29-27-9e-fb')
    @commethod(7)
    def Bind(pEventObject: win32more.System.Com.IDispatch_head, EventName: win32more.Foundation.BSTR, EventHandler: win32more.Foundation.BSTR, CancelID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Unbind(CancelCookie: UInt32) -> win32more.Foundation.HRESULT: ...
class IMSVidAnalogTuner(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidTuner
    Guid = Guid('1c15d47e-911d-11d2-b6-32-00-c0-4f-79-49-8e')
    @commethod(22)
    def get_Channel(Channel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_Channel(Channel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_VideoFrequency(lcc: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_AudioFrequency(lcc: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_CountryCode(lcc: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_CountryCode(lcc: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_SAP(pfSapOn: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_SAP(fSapOn: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def ChannelAvailable(nChannel: Int32, SignalStrength: POINTER(Int32), fSignalPresent: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IMSVidAnalogTuner2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidAnalogTuner
    Guid = Guid('37647bf7-3dde-4cc8-a4-dc-0d-53-4d-3d-00-37')
    @commethod(31)
    def get_TVFormats(Formats: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_TunerModes(Modes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_NumAuxInputs(Inputs: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMSVidAnalogTunerEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidTunerEvent
    Guid = Guid('1c15d486-911d-11d2-b6-32-00-c0-4f-79-49-8e')
class IMSVidAudioRenderer(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDevice
    Guid = Guid('37b0353f-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
    @commethod(16)
    def put_Volume(lVol: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Volume(lVol: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Balance(lBal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Balance(lBal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMSVidAudioRendererDevices(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c5702cd4-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
    @commethod(7)
    def get_Count(lCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(pD: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(v: win32more.System.Com.VARIANT, pDB: POINTER(win32more.Media.DirectShow.IMSVidAudioRenderer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pDB: win32more.Media.DirectShow.IMSVidAudioRenderer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(v: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IMSVidAudioRendererEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDeviceEvent
    Guid = Guid('37b03541-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
class IMSVidAudioRendererEvent2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidAudioRendererEvent
    Guid = Guid('e3f55729-353b-4c43-a0-28-50-f7-9a-a9-a9-07')
    @commethod(8)
    def AVDecAudioDualMono() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AVAudioSampleRate() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def AVAudioChannelConfig() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def AVAudioChannelCount() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def AVDecCommonMeanBitRate() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AVDDSurroundMode() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def AVDecCommonInputFormat() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def AVDecCommonOutputFormat() -> win32more.Foundation.HRESULT: ...
class IMSVidClosedCaptioning(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFeature
    Guid = Guid('99652ea1-c1f7-414f-bb-7b-1c-96-7d-e7-59-83')
    @commethod(16)
    def get_Enable(On: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Enable(On: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IMSVidClosedCaptioning2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidClosedCaptioning
    Guid = Guid('e00cb864-a029-4310-99-87-a8-73-f5-88-7d-97')
    @commethod(18)
    def get_Service(On: POINTER(win32more.Media.DirectShow.MSVidCCService)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Service(On: win32more.Media.DirectShow.MSVidCCService) -> win32more.Foundation.HRESULT: ...
class IMSVidClosedCaptioning3(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidClosedCaptioning2
    Guid = Guid('c8638e8a-7625-4c51-93-66-2f-40-a9-83-1f-c0')
    @commethod(20)
    def get_TeleTextFilter(punkTTFilter: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidCompositionSegment(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidGraphSegment
    Guid = Guid('1c15d483-911d-11d2-b6-32-00-c0-4f-79-49-8e')
    @commethod(19)
    def Compose(upstream: win32more.Media.DirectShow.IMSVidGraphSegment_head, downstream: win32more.Media.DirectShow.IMSVidGraphSegment_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Up(upstream: POINTER(win32more.Media.DirectShow.IMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Down(downstream: POINTER(win32more.Media.DirectShow.IMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidCtl(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b0edf162-910a-11d2-b6-32-00-c0-4f-79-49-8e')
    @commethod(7)
    def get_AutoSize(pbool: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_AutoSize(vbool: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_BackColor(backcolor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_BackColor(backcolor: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Enabled(pbool: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Enabled(vbool: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_TabStop(pbool: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_TabStop(vbool: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Window(phwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_DisplaySize(CurrentValue: POINTER(win32more.Media.DirectShow.DisplaySizeList)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_DisplaySize(NewValue: win32more.Media.DirectShow.DisplaySizeList) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_MaintainAspectRatio(CurrentValue: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_MaintainAspectRatio(NewValue: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_ColorKey(CurrentValue: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_ColorKey(NewValue: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_InputsAvailable(CategoryGuid: win32more.Foundation.BSTR, pVal: POINTER(win32more.Media.DirectShow.IMSVidInputDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_OutputsAvailable(CategoryGuid: win32more.Foundation.BSTR, pVal: POINTER(win32more.Media.DirectShow.IMSVidOutputDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get__InputsAvailable(CategoryGuid: POINTER(Guid), pVal: POINTER(win32more.Media.DirectShow.IMSVidInputDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get__OutputsAvailable(CategoryGuid: POINTER(Guid), pVal: POINTER(win32more.Media.DirectShow.IMSVidOutputDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_VideoRenderersAvailable(pVal: POINTER(win32more.Media.DirectShow.IMSVidVideoRendererDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_AudioRenderersAvailable(pVal: POINTER(win32more.Media.DirectShow.IMSVidAudioRendererDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_FeaturesAvailable(pVal: POINTER(win32more.Media.DirectShow.IMSVidFeatures_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_InputActive(pVal: POINTER(win32more.Media.DirectShow.IMSVidInputDevice_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_InputActive(pVal: win32more.Media.DirectShow.IMSVidInputDevice_head) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_OutputsActive(pVal: POINTER(win32more.Media.DirectShow.IMSVidOutputDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_OutputsActive(pVal: win32more.Media.DirectShow.IMSVidOutputDevices_head) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_VideoRendererActive(pVal: POINTER(win32more.Media.DirectShow.IMSVidVideoRenderer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_VideoRendererActive(pVal: win32more.Media.DirectShow.IMSVidVideoRenderer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_AudioRendererActive(pVal: POINTER(win32more.Media.DirectShow.IMSVidAudioRenderer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_AudioRendererActive(pVal: win32more.Media.DirectShow.IMSVidAudioRenderer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_FeaturesActive(pVal: POINTER(win32more.Media.DirectShow.IMSVidFeatures_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_FeaturesActive(pVal: win32more.Media.DirectShow.IMSVidFeatures_head) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_State(lState: POINTER(win32more.Media.DirectShow.MSVidCtlStateList)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def View(v: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def Build() -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def Run() -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def Stop() -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def Decompose() -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def DisableVideo() -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def DisableAudio() -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def ViewNext(v: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidDataServices(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFeature
    Guid = Guid('334125c1-77e5-11d3-b6-53-00-c0-4f-79-49-8e')
class IMSVidDataServicesEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidDeviceEvent
    Guid = Guid('334125c2-77e5-11d3-b6-53-00-c0-4f-79-49-8e')
class IMSVidDevice(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('1c15d47c-911d-11d2-b6-32-00-c0-4f-79-49-8e')
    @commethod(7)
    def get_Name(Name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Status(Status: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Power(Power: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Power(Power: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Category(Guid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ClassID(Clsid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get__Category(Guid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get__ClassID(Clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def IsEqualDevice(Device: win32more.Media.DirectShow.IMSVidDevice_head, IsEqual: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IMSVidDevice2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('87bd2783-ebc0-478c-b4-a0-e8-e7-f4-3a-b7-8e')
    @commethod(3)
    def get_DevicePath(DevPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IMSVidDeviceEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('1c15d480-911d-11d2-b6-32-00-c0-4f-79-49-8e')
    @commethod(7)
    def StateChange(lpd: win32more.Media.DirectShow.IMSVidDevice_head, oldState: Int32, newState: Int32) -> win32more.Foundation.HRESULT: ...
class IMSVidEVR(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidVideoRenderer
    Guid = Guid('15e496ae-82a8-4cf9-a6-b6-c5-61-dc-60-39-8f')
    @commethod(46)
    def get_Presenter(ppAllocPresent: POINTER(win32more.Media.MediaFoundation.IMFVideoPresenter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def put_Presenter(pAllocPresent: win32more.Media.MediaFoundation.IMFVideoPresenter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def put_SuppressEffects(bSuppress: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_SuppressEffects(bSuppress: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IMSVidEVREvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDeviceEvent
    Guid = Guid('349abb10-883c-4f22-87-14-ce-ca-ee-e4-5d-62')
    @commethod(8)
    def OnUserEvent(lEventCode: Int32) -> win32more.Foundation.HRESULT: ...
class IMSVidEncoder(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFeature
    Guid = Guid('c0020fd4-bee7-43d9-a4-95-9f-21-31-17-10-3d')
    @commethod(16)
    def get_VideoEncoderInterface(ppEncInt: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_AudioEncoderInterface(ppEncInt: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidFeature(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidDevice
    Guid = Guid('37b03547-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
class IMSVidFeatureEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidDeviceEvent
    Guid = Guid('3dd2903c-e0aa-11d2-b6-3a-00-c0-4f-79-49-8e')
class IMSVidFeatures(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c5702cd5-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
    @commethod(7)
    def get_Count(lCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(pD: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(v: win32more.System.Com.VARIANT, pDB: POINTER(win32more.Media.DirectShow.IMSVidFeature_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pDB: win32more.Media.DirectShow.IMSVidFeature_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(v: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IMSVidFilePlayback(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidPlayback
    Guid = Guid('37b03539-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
    @commethod(32)
    def get_FileName(FileName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_FileName(FileName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IMSVidFilePlayback2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFilePlayback
    Guid = Guid('2f7e44af-6e52-4660-bc-08-d8-d5-42-58-7d-72')
    @commethod(34)
    def put__SourceFilter(FileName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put___SourceFilter(FileName: Guid) -> win32more.Foundation.HRESULT: ...
class IMSVidFilePlaybackEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidPlaybackEvent
    Guid = Guid('37b0353a-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
class IMSVidGenericSink(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDevice
    Guid = Guid('6c29b41d-455b-4c33-96-3a-0d-28-e5-e5-55-ea')
    @commethod(16)
    def SetSinkFilter(bstrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_SinkStreams(pStreams: POINTER(win32more.Media.DirectShow.MSVidSinkStreams)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_SinkStreams(Streams: win32more.Media.DirectShow.MSVidSinkStreams) -> win32more.Foundation.HRESULT: ...
class IMSVidGenericSink2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidGenericSink
    Guid = Guid('6b5a28f3-47f1-4092-b1-68-60-ca-be-c0-8f-1c')
    @commethod(19)
    def AddFilter(bstrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def ResetFilterList() -> win32more.Foundation.HRESULT: ...
class IMSVidGraphSegment(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('238dec54-adeb-4005-a3-49-f7-72-b9-af-eb-c4')
    @commethod(4)
    def get_Init(pInit: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_Init(pInit: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumFilters(pNewEnum: POINTER(win32more.Media.DirectShow.IEnumFilters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Container(ppCtl: POINTER(win32more.Media.DirectShow.IMSVidGraphSegmentContainer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Container(pCtl: win32more.Media.DirectShow.IMSVidGraphSegmentContainer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Type(pType: POINTER(win32more.Media.DirectShow.MSVidSegmentType)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Category(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Build() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def PostBuild() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def PreRun() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def PostRun() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def PreStop() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def PostStop() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def OnEventNotify(lEventCode: Int32, lEventParm1: IntPtr, lEventParm2: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Decompose() -> win32more.Foundation.HRESULT: ...
class IMSVidGraphSegmentContainer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3dd2903d-e0aa-11d2-b6-3a-00-c0-4f-79-49-8e')
    @commethod(3)
    def get_Graph(ppGraph: POINTER(win32more.Media.DirectShow.IGraphBuilder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Input(ppInput: POINTER(win32more.Media.DirectShow.IMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Outputs(ppOutputs: POINTER(win32more.Media.DirectShow.IEnumMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_VideoRenderer(ppVR: POINTER(win32more.Media.DirectShow.IMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_AudioRenderer(ppAR: POINTER(win32more.Media.DirectShow.IMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Features(ppFeatures: POINTER(win32more.Media.DirectShow.IEnumMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Composites(ppComposites: POINTER(win32more.Media.DirectShow.IEnumMSVidGraphSegment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_ParentContainer(ppContainer: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Decompose(pSegment: win32more.Media.DirectShow.IMSVidGraphSegment_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def IsWindowless() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetFocus() -> win32more.Foundation.HRESULT: ...
class IMSVidGraphSegmentUserInput(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('301c060e-20d9-4587-9b-03-f8-2e-d9-a9-94-3c')
    @commethod(3)
    def Click() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DblClick() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def KeyDown(KeyCode: POINTER(Int16), ShiftState: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def KeyPress(KeyAscii: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def KeyUp(KeyCode: POINTER(Int16), ShiftState: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def MouseDown(ButtonState: Int16, ShiftState: Int16, x: Int32, y: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def MouseMove(ButtonState: Int16, ShiftState: Int16, x: Int32, y: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def MouseUp(ButtonState: Int16, ShiftState: Int16, x: Int32, y: Int32) -> win32more.Foundation.HRESULT: ...
class IMSVidInputDevice(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidDevice
    Guid = Guid('37b0353d-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
    @commethod(16)
    def IsViewable(v: POINTER(win32more.System.Com.VARIANT_head), pfViewable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def View(v: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidInputDeviceEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('37b0353e-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
class IMSVidInputDevices(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c5702cd1-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
    @commethod(7)
    def get_Count(lCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(pD: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(v: win32more.System.Com.VARIANT, pDB: POINTER(win32more.Media.DirectShow.IMSVidInputDevice_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pDB: win32more.Media.DirectShow.IMSVidInputDevice_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(v: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IMSVidOutputDevice(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidDevice
    Guid = Guid('37b03546-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
class IMSVidOutputDeviceEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidDeviceEvent
    Guid = Guid('2e6a14e2-571c-11d3-b6-52-00-c0-4f-79-49-8e')
class IMSVidOutputDevices(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c5702cd2-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
    @commethod(7)
    def get_Count(lCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(pD: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(v: win32more.System.Com.VARIANT, pDB: POINTER(win32more.Media.DirectShow.IMSVidOutputDevice_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pDB: win32more.Media.DirectShow.IMSVidOutputDevice_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(v: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IMSVidPlayback(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidInputDevice
    Guid = Guid('37b03538-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
    @commethod(18)
    def get_EnableResetOnStop(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_EnableResetOnStop(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Run() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Stop() -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_CanStep(fBackwards: win32more.Foundation.VARIANT_BOOL, pfCan: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def Step(lStep: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_Rate(plRate: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Rate(plRate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_CurrentPosition(lPosition: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_CurrentPosition(lPosition: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_PositionMode(lPositionMode: win32more.Media.DirectShow.PositionModeList) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_PositionMode(lPositionMode: POINTER(win32more.Media.DirectShow.PositionModeList)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_Length(lLength: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMSVidPlaybackEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidInputDeviceEvent
    Guid = Guid('37b0353b-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
    @commethod(7)
    def EndOfMedia(lpd: win32more.Media.DirectShow.IMSVidPlayback_head) -> win32more.Foundation.HRESULT: ...
class IMSVidRect(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('7f5000a6-a440-47ca-8a-cc-c0-e7-55-31-a2-c2')
    @commethod(7)
    def get_Top(TopVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Top(TopVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Left(LeftVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Left(LeftVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Width(WidthVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Width(WidthVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Height(HeightVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Height(HeightVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_HWnd(HWndVal: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_HWnd(HWndVal: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Rect(RectVal: win32more.Media.DirectShow.IMSVidRect_head) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferRecordingControl(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('160621aa-bbbc-4326-a8-24-c3-95-ae-bc-6e-74')
    @commethod(7)
    def get_StartTime(rtStart: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_StartTime(rtStart: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StopTime(rtStop: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_StopTime(rtStop: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_RecordingStopped(phResult: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_RecordingStarted(phResult: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_RecordingType(dwType: POINTER(win32more.Media.DirectShow.RecordingType)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_RecordingAttribute(pRecordingAttribute: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSink(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDevice
    Guid = Guid('159dbb45-cd1b-4dab-83-ea-5c-b1-f4-f2-1d-07')
    @commethod(16)
    def get_ContentRecorder(pszFilename: win32more.Foundation.BSTR, pRecordingIUnknown: POINTER(win32more.Media.DirectShow.IMSVidStreamBufferRecordingControl_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ReferenceRecorder(pszFilename: win32more.Foundation.BSTR, pRecordingIUnknown: POINTER(win32more.Media.DirectShow.IMSVidStreamBufferRecordingControl_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_SinkName(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_SinkName(Name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def NameSetLock() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_SBESink(sbeConfig: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSink2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSink
    Guid = Guid('2ca9fc63-c131-4e5a-95-5a-54-4a-47-c6-71-46')
    @commethod(22)
    def UnlockProfile() -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSink3(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSink2
    Guid = Guid('4f8721d7-7d59-4d8b-99-f5-a7-77-75-58-6b-d5')
    @commethod(23)
    def SetMinSeek(pdwMin: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_AudioCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_VideoCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_CCCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_WSTCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_AudioAnalysisFilter(szCLSID: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_AudioAnalysisFilter(pszCLSID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put__AudioAnalysisFilter(guid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get__AudioAnalysisFilter(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_VideoAnalysisFilter(szCLSID: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_VideoAnalysisFilter(pszCLSID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put__VideoAnalysisFilter(guid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get__VideoAnalysisFilter(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_DataAnalysisFilter(szCLSID: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_DataAnalysisFilter(pszCLSID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def put__DataAnalysisFilter(guid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get__DataAnalysisFilter(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_LicenseErrorCode(hres: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDeviceEvent
    Guid = Guid('f798a36b-b05b-4bbe-97-03-ea-ea-7d-61-cd-51')
    @commethod(8)
    def CertificateFailure() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CertificateSuccess() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def WriteFailure() -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSinkEvent
    Guid = Guid('3d7a5166-72d7-484b-a0-6f-28-61-87-b8-0c-a1')
    @commethod(11)
    def EncryptionOn() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EncryptionOff() -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent3(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSinkEvent2
    Guid = Guid('735ad8d5-c259-48e9-81-e7-d2-79-53-66-5b-23')
    @commethod(13)
    def LicenseChange(dwProt: Int32) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSinkEvent4(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSinkEvent3
    Guid = Guid('1b01dcb0-daf0-412c-a5-d1-59-0c-7f-62-e2-b8')
    @commethod(14)
    def WriteFailureClear() -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSource(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFilePlayback
    Guid = Guid('eb0c8cf9-6950-4772-87-b1-47-d1-1c-f3-a0-2f')
    @commethod(34)
    def get_Start(lStart: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_RecordingAttribute(pRecordingAttribute: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def CurrentRatings(pEnSystem: POINTER(win32more.Media.DirectShow.EnTvRat_System), pEnRating: POINTER(win32more.Media.DirectShow.EnTvRat_GenericLevel), pBfEnAttr: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def MaxRatingsLevel(enSystem: win32more.Media.DirectShow.EnTvRat_System, enRating: win32more.Media.DirectShow.EnTvRat_GenericLevel, lbfEnAttr: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def put_BlockUnrated(bBlock: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_UnratedDelay(dwDelay: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_SBESource(sbeFilter: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSource2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSource
    Guid = Guid('e4ba9059-b1ce-40d8-b9-a0-d4-ea-4a-99-89-d3')
    @commethod(41)
    def put_RateEx(dwRate: Double, dwFramesPerSecond: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_AudioCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def get_VideoCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_CCCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_WSTCounter(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSourceEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFilePlaybackEvent
    Guid = Guid('50ce8a7d-9c28-4da8-90-42-cd-fa-71-16-f9-79')
    @commethod(8)
    def CertificateFailure() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CertificateSuccess() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RatingsBlocked() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RatingsUnblocked() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def RatingsChanged() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def TimeHole(StreamOffsetMS: Int32, SizeMS: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def StaleDataRead() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ContentBecomingStale() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def StaleFileDeleted() -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSourceEvent2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSourceEvent
    Guid = Guid('7aef50ce-8e22-4ba8-bc-06-a9-2a-45-8b-4e-f2')
    @commethod(17)
    def RateChange(qwNewRate: Double, qwOldRate: Double) -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferSourceEvent3(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidStreamBufferSourceEvent2
    Guid = Guid('ceabd6ab-9b90-4570-ad-f1-3c-e7-6e-00-a7-63')
    @commethod(18)
    def BroadcastEvent(Guid: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def BroadcastEventEx(Guid: win32more.Foundation.BSTR, Param1: UInt32, Param2: UInt32, Param3: UInt32, Param4: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def COPPBlocked() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def COPPUnblocked() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ContentPrimarilyAudio() -> win32more.Foundation.HRESULT: ...
class IMSVidStreamBufferV2SourceEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFilePlaybackEvent
    Guid = Guid('49c771f9-41b2-4cf7-9f-9a-a3-13-a8-f6-02-7e')
    @commethod(8)
    def RatingsChanged() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def TimeHole(StreamOffsetMS: Int32, SizeMS: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def StaleDataRead() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ContentBecomingStale() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def StaleFileDeleted() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def RateChange(qwNewRate: Double, qwOldRate: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def BroadcastEvent(Guid: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def BroadcastEventEx(Guid: win32more.Foundation.BSTR, Param1: UInt32, Param2: UInt32, Param3: UInt32, Param4: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ContentPrimarilyAudio() -> win32more.Foundation.HRESULT: ...
class IMSVidTuner(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidVideoInputDevice
    Guid = Guid('1c15d47d-911d-11d2-b6-32-00-c0-4f-79-49-8e')
    @commethod(18)
    def get_Tune(ppTR: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Tune(pTR: win32more.Media.DirectShow.ITuneRequest_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_TuningSpace(plTS: POINTER(win32more.Media.DirectShow.ITuningSpace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_TuningSpace(plTS: win32more.Media.DirectShow.ITuningSpace_head) -> win32more.Foundation.HRESULT: ...
class IMSVidTunerEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidInputDeviceEvent
    Guid = Guid('1c15d485-911d-11d2-b6-32-00-c0-4f-79-49-8e')
    @commethod(7)
    def TuneChanged(lpd: win32more.Media.DirectShow.IMSVidTuner_head) -> win32more.Foundation.HRESULT: ...
class IMSVidVMR9(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidVideoRenderer
    Guid = Guid('d58b0015-ebef-44bb-bb-dd-3f-36-99-d7-6e-a1')
    @commethod(46)
    def get_Allocator_ID(ID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def SetAllocator(AllocPresent: win32more.System.Com.IUnknown_head, ID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def put_SuppressEffects(bSuppress: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_SuppressEffects(bSuppress: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def get_Allocator(AllocPresent: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidVRGraphSegment(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidGraphSegment
    Guid = Guid('dd47de3f-9874-4f7b-8b-22-7c-b2-68-84-61-e7')
    @commethod(19)
    def put__VMRendererMode(dwMode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Owner(Window: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Owner(Window: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_UseOverlay(UseOverlayVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_UseOverlay(UseOverlayVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Visible(Visible: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_Visible(Visible: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ColorKey(ColorKey: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_ColorKey(ColorKey: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Source(r: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Source(r: win32more.Foundation.RECT) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_Destination(r: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_Destination(r: win32more.Foundation.RECT) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_NativeSize(sizeval: POINTER(win32more.Foundation.SIZE_head), aspectratio: POINTER(win32more.Foundation.SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_BorderColor(color: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_BorderColor(color: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_MaintainAspectRatio(fMaintain: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_MaintainAspectRatio(fMaintain: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def DisplayChange() -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def RePaint(hdc: win32more.Graphics.Gdi.HDC) -> win32more.Foundation.HRESULT: ...
class IMSVidVideoInputDevice(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidInputDevice
    Guid = Guid('1c15d47f-911d-11d2-b6-32-00-c0-4f-79-49-8e')
class IMSVidVideoRenderer(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDevice
    Guid = Guid('37b03540-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
    @commethod(16)
    def get_CustomCompositorClass(CompositorCLSID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_CustomCompositorClass(CompositorCLSID: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get__CustomCompositorClass(CompositorCLSID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put__CustomCompositorClass(CompositorCLSID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get__CustomCompositor(Compositor: POINTER(win32more.Media.DirectShow.IVMRImageCompositor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put__CustomCompositor(Compositor: win32more.Media.DirectShow.IVMRImageCompositor_head) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_MixerBitmap(MixerPictureDisp: POINTER(win32more.System.Ole.IPictureDisp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get__MixerBitmap(MixerPicture: POINTER(win32more.Media.DirectShow.IVMRMixerBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_MixerBitmap(MixerPictureDisp: win32more.System.Ole.IPictureDisp_head) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put__MixerBitmap(MixerPicture: POINTER(win32more.Media.DirectShow.VMRALPHABITMAP_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_MixerBitmapPositionRect(rDest: POINTER(win32more.Media.DirectShow.IMSVidRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_MixerBitmapPositionRect(rDest: win32more.Media.DirectShow.IMSVidRect_head) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_MixerBitmapOpacity(opacity: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_MixerBitmapOpacity(opacity: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SetupMixerBitmap(MixerPictureDisp: win32more.System.Ole.IPictureDisp_head, Opacity: Int32, rDest: win32more.Media.DirectShow.IMSVidRect_head) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_SourceSize(CurrentSize: POINTER(win32more.Media.DirectShow.SourceSizeList)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_SourceSize(NewSize: win32more.Media.DirectShow.SourceSizeList) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_OverScan(plPercent: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_OverScan(lPercent: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_AvailableSourceRect(pRect: POINTER(win32more.Media.DirectShow.IMSVidRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_MaxVidRect(ppVidRect: POINTER(win32more.Media.DirectShow.IMSVidRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_MinVidRect(ppVidRect: POINTER(win32more.Media.DirectShow.IMSVidRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_ClippedSourceRect(pRect: POINTER(win32more.Media.DirectShow.IMSVidRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_ClippedSourceRect(pRect: win32more.Media.DirectShow.IMSVidRect_head) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_UsingOverlay(UseOverlayVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_UsingOverlay(UseOverlayVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def Capture(currentImage: POINTER(win32more.System.Ole.IPictureDisp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def get_FramesPerSecond(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_DecimateInput(pDeci: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_DecimateInput(pDeci: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IMSVidVideoRenderer2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidVideoRenderer
    Guid = Guid('6bdd5c1e-2810-4159-94-bc-05-51-1a-e8-54-9b')
    @commethod(46)
    def get_Allocator(AllocPresent: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get__Allocator(AllocPresent: POINTER(win32more.Media.DirectShow.IVMRSurfaceAllocator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_Allocator_ID(ID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def SetAllocator(AllocPresent: win32more.System.Com.IUnknown_head, ID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def _SetAllocator2(AllocPresent: win32more.Media.DirectShow.IVMRSurfaceAllocator_head, ID: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def put_SuppressEffects(bSuppress: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_SuppressEffects(bSuppress: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IMSVidVideoRendererDevices(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c5702cd3-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
    @commethod(7)
    def get_Count(lCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(pD: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(v: win32more.System.Com.VARIANT, pDB: POINTER(win32more.Media.DirectShow.IMSVidVideoRenderer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(pDB: win32more.Media.DirectShow.IMSVidVideoRenderer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(v: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IMSVidVideoRendererEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDeviceEvent
    Guid = Guid('37b03545-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
    @commethod(8)
    def OverlayUnavailable() -> win32more.Foundation.HRESULT: ...
class IMSVidVideoRendererEvent2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidOutputDeviceEvent
    Guid = Guid('7145ed66-4730-4fdb-8a-53-fd-e7-50-8d-3e-5e')
    @commethod(8)
    def OverlayUnavailable() -> win32more.Foundation.HRESULT: ...
class IMSVidWebDVD(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidPlayback
    Guid = Guid('cf45f88b-ac56-4ee2-a7-3a-ed-04-e2-88-5d-3c')
    @commethod(32)
    def OnDVDEvent(lEvent: Int32, lParam1: IntPtr, lParam2: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def PlayTitle(lTitle: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def PlayChapterInTitle(lTitle: Int32, lChapter: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def PlayChapter(lChapter: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def PlayChaptersAutoStop(lTitle: Int32, lstrChapter: Int32, lChapterCount: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def PlayAtTime(strTime: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def PlayAtTimeInTitle(lTitle: Int32, strTime: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def PlayPeriodInTitleAutoStop(lTitle: Int32, strStartTime: win32more.Foundation.BSTR, strEndTime: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def ReplayChapter() -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def PlayPrevChapter() -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def PlayNextChapter() -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def StillOff() -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_AudioLanguage(lStream: Int32, fFormat: win32more.Foundation.VARIANT_BOOL, strAudioLang: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def ShowMenu(MenuID: win32more.Media.DirectShow.DVDMenuIDConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def Resume() -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def ReturnFromSubmenu() -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_ButtonsAvailable(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_CurrentButton(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def SelectAndActivateButton(lButton: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def ActivateButton() -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def SelectRightButton() -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def SelectLeftButton() -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def SelectLowerButton() -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def SelectUpperButton() -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def ActivateAtPosition(xPos: Int32, yPos: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def SelectAtPosition(xPos: Int32, yPos: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def get_ButtonAtPosition(xPos: Int32, yPos: Int32, plButton: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_NumberOfChapters(lTitle: Int32, pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def get_TotalTitleTime(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def get_TitlesAvailable(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def get_VolumesAvailable(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def get_CurrentVolume(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def get_CurrentDiscSide(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def get_CurrentDomain(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def get_CurrentChapter(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def get_CurrentTitle(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def get_CurrentTime(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def DVDTimeCode2bstr(timeCode: Int32, pTimeStr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def get_DVDDirectory(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def put_DVDDirectory(newVal: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def IsSubpictureStreamEnabled(lstream: Int32, fEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def IsAudioStreamEnabled(lstream: Int32, fEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def get_CurrentSubpictureStream(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def put_CurrentSubpictureStream(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def get_SubpictureLanguage(lStream: Int32, strLanguage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def get_CurrentAudioStream(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def put_CurrentAudioStream(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(79)
    def get_AudioStreamsAvailable(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def get_AnglesAvailable(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def get_CurrentAngle(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(82)
    def put_CurrentAngle(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(83)
    def get_SubpictureStreamsAvailable(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(84)
    def get_SubpictureOn(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(85)
    def put_SubpictureOn(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(86)
    def get_DVDUniqueID(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(87)
    def AcceptParentalLevelChange(fAccept: win32more.Foundation.VARIANT_BOOL, strUserName: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(88)
    def NotifyParentalLevelChange(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(89)
    def SelectParentalCountry(lCountry: Int32, strUserName: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(90)
    def SelectParentalLevel(lParentalLevel: Int32, strUserName: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(91)
    def get_TitleParentalLevels(lTitle: Int32, plParentalLevels: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(92)
    def get_PlayerParentalCountry(plCountryCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(93)
    def get_PlayerParentalLevel(plParentalLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(94)
    def Eject() -> win32more.Foundation.HRESULT: ...
    @commethod(95)
    def UOPValid(lUOP: Int32, pfValid: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(96)
    def get_SPRM(lIndex: Int32, psSPRM: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(97)
    def get_GPRM(lIndex: Int32, psSPRM: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(98)
    def put_GPRM(lIndex: Int32, sValue: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(99)
    def get_DVDTextStringType(lLangIndex: Int32, lStringIndex: Int32, pType: POINTER(win32more.Media.DirectShow.DVDTextStringType)) -> win32more.Foundation.HRESULT: ...
    @commethod(100)
    def get_DVDTextString(lLangIndex: Int32, lStringIndex: Int32, pstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(101)
    def get_DVDTextNumberOfStrings(lLangIndex: Int32, plNumOfStrings: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(102)
    def get_DVDTextNumberOfLanguages(plNumOfLangs: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(103)
    def get_DVDTextLanguageLCID(lLangIndex: Int32, lcid: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(104)
    def RegionChange() -> win32more.Foundation.HRESULT: ...
    @commethod(105)
    def get_DVDAdm(pVal: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(106)
    def DeleteBookmark() -> win32more.Foundation.HRESULT: ...
    @commethod(107)
    def RestoreBookmark() -> win32more.Foundation.HRESULT: ...
    @commethod(108)
    def SaveBookmark() -> win32more.Foundation.HRESULT: ...
    @commethod(109)
    def SelectDefaultAudioLanguage(lang: Int32, ext: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(110)
    def SelectDefaultSubpictureLanguage(lang: Int32, ext: win32more.Media.DirectShow.DVDSPExt) -> win32more.Foundation.HRESULT: ...
    @commethod(111)
    def get_PreferredSubpictureStream(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(112)
    def get_DefaultMenuLanguage(lang: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(113)
    def put_DefaultMenuLanguage(lang: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(114)
    def get_DefaultSubpictureLanguage(lang: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(115)
    def get_DefaultAudioLanguage(lang: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(116)
    def get_DefaultSubpictureLanguageExt(ext: POINTER(win32more.Media.DirectShow.DVDSPExt)) -> win32more.Foundation.HRESULT: ...
    @commethod(117)
    def get_DefaultAudioLanguageExt(ext: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(118)
    def get_LanguageFromLCID(lcid: Int32, lang: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(119)
    def get_KaraokeAudioPresentationMode(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(120)
    def put_KaraokeAudioPresentationMode(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(121)
    def get_KaraokeChannelContent(lStream: Int32, lChan: Int32, lContent: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(122)
    def get_KaraokeChannelAssignment(lStream: Int32, lChannelAssignment: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(123)
    def RestorePreferredSettings() -> win32more.Foundation.HRESULT: ...
    @commethod(124)
    def get_ButtonRect(lButton: Int32, pRect: POINTER(win32more.Media.DirectShow.IMSVidRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(125)
    def get_DVDScreenInMouseCoordinates(ppRect: POINTER(win32more.Media.DirectShow.IMSVidRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(126)
    def put_DVDScreenInMouseCoordinates(pRect: win32more.Media.DirectShow.IMSVidRect_head) -> win32more.Foundation.HRESULT: ...
class IMSVidWebDVD2(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidWebDVD
    Guid = Guid('7027212f-ee9a-4a7c-8b-67-f0-23-71-4c-da-ff')
    @commethod(127)
    def get_Bookmark(ppData: POINTER(c_char_p_no), pDataLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(128)
    def put_Bookmark(pData: c_char_p_no, dwDataLength: UInt32) -> win32more.Foundation.HRESULT: ...
class IMSVidWebDVDAdm(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b8be681a-eb2c-47f0-b4-15-94-d5-45-2f-0e-05')
    @commethod(7)
    def ChangePassword(strUserName: win32more.Foundation.BSTR, strOld: win32more.Foundation.BSTR, strNew: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SaveParentalLevel(level: Int32, strUserName: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SaveParentalCountry(country: Int32, strUserName: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ConfirmPassword(strUserName: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR, pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetParentalLevel(lLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetParentalCountry(lCountry: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_DefaultAudioLCID(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_DefaultAudioLCID(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_DefaultSubpictureLCID(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_DefaultSubpictureLCID(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_DefaultMenuLCID(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_DefaultMenuLCID(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_BookmarkOnStop(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_BookmarkOnStop(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IMSVidWebDVDEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidPlaybackEvent
    Guid = Guid('b4f7a674-9b83-49cb-a3-57-c6-3b-87-1b-e9-58')
    @commethod(8)
    def DVDNotify(lEventCode: Int32, lParam1: win32more.System.Com.VARIANT, lParam2: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def PlayForwards(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def PlayBackwards(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ShowMenu(MenuID: win32more.Media.DirectShow.DVDMenuIDConstants, bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Resume(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SelectOrActivateButton(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def StillOff(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def PauseOn(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ChangeCurrentAudioStream(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ChangeCurrentSubpictureStream(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ChangeCurrentAngle(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def PlayAtTimeInTitle(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def PlayAtTime(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def PlayChapterInTitle(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def PlayChapter(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def ReplayChapter(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def PlayNextChapter(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def Stop(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def ReturnFromSubmenu(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def PlayTitle(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def PlayPrevChapter(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def ChangeKaraokePresMode(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def ChangeVideoPresMode(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IMSVidXDS(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFeature
    Guid = Guid('11ebc158-e712-4d1f-8b-b3-01-ed-52-74-c4-ce')
    @commethod(16)
    def get_ChannelChangeInterface(punkCC: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSVidXDSEvent(c_void_p):
    extends: win32more.Media.DirectShow.IMSVidFeatureEvent
    Guid = Guid('6db2317d-3b23-41ec-ba-4b-70-1f-40-7e-af-3a')
    @commethod(8)
    def RatingChange(PrevRatingSystem: win32more.Media.DirectShow.EnTvRat_System, PrevLevel: win32more.Media.DirectShow.EnTvRat_GenericLevel, PrevAttributes: win32more.Media.DirectShow.BfEnTvRat_GenericAttributes, NewRatingSystem: win32more.Media.DirectShow.EnTvRat_System, NewLevel: win32more.Media.DirectShow.EnTvRat_GenericLevel, NewAttributes: win32more.Media.DirectShow.BfEnTvRat_GenericAttributes) -> win32more.Foundation.HRESULT: ...
class IMceBurnerControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5a86b91a-e71e-46c1-88-a9-9b-b3-38-71-05-52')
    @commethod(3)
    def GetBurnerNoDecryption() -> win32more.Foundation.HRESULT: ...
class IMediaControl(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868b1-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def Run() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Stop() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetState(msTimeout: Int32, pfs: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RenderFile(strFilename: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def AddSourceFilter(strFilename: win32more.Foundation.BSTR, ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_FilterCollection(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_RegFilterCollection(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def StopWhenReady() -> win32more.Foundation.HRESULT: ...
class IMediaEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868b6-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def GetEventHandle(hEvent: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetEvent(lEventCode: POINTER(Int32), lParam1: POINTER(IntPtr), lParam2: POINTER(IntPtr), msTimeout: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def WaitForCompletion(msTimeout: Int32, pEvCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CancelDefaultHandling(lEvCode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RestoreDefaultHandling(lEvCode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def FreeEventParams(lEvCode: Int32, lParam1: IntPtr, lParam2: IntPtr) -> win32more.Foundation.HRESULT: ...
class IMediaEventEx(c_void_p):
    extends: win32more.Media.DirectShow.IMediaEvent
    Guid = Guid('56a868c0-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(13)
    def SetNotifyWindow(hwnd: IntPtr, lMsg: Int32, lInstanceData: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetNotifyFlags(lNoNotifyFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetNotifyFlags(lplNoNotifyFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMediaEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868a2-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Notify(EventCode: Int32, EventParam1: IntPtr, EventParam2: IntPtr) -> win32more.Foundation.HRESULT: ...
class IMediaFilter(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('56a86899-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(4)
    def Stop() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Run(tStart: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetState(dwMilliSecsTimeout: UInt32, State: POINTER(win32more.Media.DirectShow.FILTER_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetSyncSource(pClock: win32more.Media.IReferenceClock_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSyncSource(pClock: POINTER(win32more.Media.IReferenceClock_head)) -> win32more.Foundation.HRESULT: ...
class IMediaParamInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6d6cbb60-a223-44aa-84-2f-a2-f0-67-50-be-6d')
    @commethod(3)
    def GetParamCount(pdwParams: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetParamInfo(dwParamIndex: UInt32, pInfo: POINTER(win32more.Media.DirectShow.MP_PARAMINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetParamText(dwParamIndex: UInt32, ppwchText: POINTER(POINTER(UInt16))) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetNumTimeFormats(pdwNumTimeFormats: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSupportedTimeFormat(dwFormatIndex: UInt32, pguidTimeFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentTimeFormat(pguidTimeFormat: POINTER(Guid), pTimeData: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMediaParams(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6d6cbb61-a223-44aa-84-2f-a2-f0-67-50-be-6e')
    @commethod(3)
    def GetParam(dwParamIndex: UInt32, pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetParam(dwParamIndex: UInt32, value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddEnvelope(dwParamIndex: UInt32, cSegments: UInt32, pEnvelopeSegments: POINTER(win32more.Media.DirectShow.MP_ENVELOPE_SEGMENT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FlushEnvelope(dwParamIndex: UInt32, refTimeStart: Int64, refTimeEnd: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetTimeFormat(guidTimeFormat: Guid, mpTimeData: UInt32) -> win32more.Foundation.HRESULT: ...
class IMediaPosition(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868b2-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def get_Duration(plength: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_CurrentPosition(llTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentPosition(pllTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StopTime(pllTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_StopTime(llTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_PrerollTime(pllTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_PrerollTime(llTime: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Rate(dRate: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Rate(pdRate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CanSeekForward(pCanSeekForward: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def CanSeekBackward(pCanSeekBackward: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMediaPropertyBag(c_void_p):
    extends: win32more.System.Com.StructuredStorage.IPropertyBag
    Guid = Guid('6025a880-c0d5-11d0-bd-4e-00-a0-c9-11-ce-86')
    @commethod(5)
    def EnumProperty(iProperty: UInt32, pvarPropertyName: POINTER(win32more.System.Com.VARIANT_head), pvarPropertyValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMediaSample(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a8689a-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def GetPointer(ppBuffer: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSize() -> Int32: ...
    @commethod(5)
    def GetTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def IsSyncPoint() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetSyncPoint(bIsSyncPoint: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def IsPreroll() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetPreroll(bIsPreroll: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetActualDataLength() -> Int32: ...
    @commethod(12)
    def SetActualDataLength(__MIDL__IMediaSample0000: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetMediaType(ppMediaType: POINTER(POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetMediaType(pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def IsDiscontinuity() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetDiscontinuity(bDiscontinuity: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetMediaTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetMediaTime(pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IMediaSample2(c_void_p):
    extends: win32more.Media.DirectShow.IMediaSample
    Guid = Guid('36b73884-c2c8-11cf-8b-46-00-80-5f-6c-ef-60')
    @commethod(19)
    def GetProperties(cbProperties: UInt32, pbProperties: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetProperties(cbProperties: UInt32, pbProperties: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IMediaSample2Config(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('68961e68-832b-41ea-bc-91-63-59-3f-3e-70-e3')
    @commethod(3)
    def GetSurface(ppDirect3DSurface9: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMediaSeeking(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('36b73880-c2c8-11cf-8b-46-00-80-5f-6c-ef-60')
    @commethod(3)
    def GetCapabilities(pCapabilities: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CheckCapabilities(pCapabilities: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsFormatSupported(pFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def QueryPreferredFormat(pFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTimeFormat(pFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def IsUsingTimeFormat(pFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetTimeFormat(pFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDuration(pDuration: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetStopPosition(pStop: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetCurrentPosition(pCurrent: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ConvertTimeFormat(pTarget: POINTER(Int64), pTargetFormat: POINTER(Guid), Source: Int64, pSourceFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetPositions(pCurrent: POINTER(Int64), dwCurrentFlags: UInt32, pStop: POINTER(Int64), dwStopFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetPositions(pCurrent: POINTER(Int64), pStop: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetAvailable(pEarliest: POINTER(Int64), pLatest: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetRate(dRate: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetRate(pdRate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetPreroll(pllPreroll: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IMediaStream(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b502d1bd-9a57-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(3)
    def GetMultiMediaStream(ppMultiMediaStream: POINTER(win32more.Media.DirectShow.IMultiMediaStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetInformation(pPurposeId: POINTER(Guid), pType: POINTER(win32more.Media.DirectShow.STREAM_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetSameFormat(pStreamThatHasDesiredFormat: win32more.Media.DirectShow.IMediaStream_head, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateSample(dwFlags: UInt32, ppSample: POINTER(win32more.Media.DirectShow.IStreamSample_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSharedSample(pExistingSample: win32more.Media.DirectShow.IStreamSample_head, dwFlags: UInt32, ppNewSample: POINTER(win32more.Media.DirectShow.IStreamSample_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SendEndOfStream(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IMediaStreamFilter(c_void_p):
    extends: win32more.Media.DirectShow.IBaseFilter
    Guid = Guid('bebe595e-9a6f-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(15)
    def AddMediaStream(pAMMediaStream: win32more.Media.DirectShow.IAMMediaStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetMediaStream(idPurpose: POINTER(Guid), ppMediaStream: POINTER(win32more.Media.DirectShow.IMediaStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def EnumMediaStreams(Index: Int32, ppMediaStream: POINTER(win32more.Media.DirectShow.IMediaStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SupportSeeking(bRenderer: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ReferenceTimeToStreamTime(pTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetCurrentStreamTime(pCurrentStreamTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def WaitUntil(WaitStreamTime: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Flush(bCancelEOS: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def EndOfStream() -> win32more.Foundation.HRESULT: ...
class IMediaTypeInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868bc-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def get_Type(strType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Subtype(strType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IMemAllocator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a8689c-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def SetProperties(pRequest: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head), pActual: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperties(pProps: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Commit() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Decommit() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetBuffer(ppBuffer: POINTER(win32more.Media.DirectShow.IMediaSample_head), pStartTime: POINTER(Int64), pEndTime: POINTER(Int64), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ReleaseBuffer(pBuffer: win32more.Media.DirectShow.IMediaSample_head) -> win32more.Foundation.HRESULT: ...
class IMemAllocatorCallbackTemp(c_void_p):
    extends: win32more.Media.DirectShow.IMemAllocator
    Guid = Guid('379a0cf0-c1de-11d2-ab-f5-00-a0-c9-05-f3-75')
    @commethod(9)
    def SetNotify(pNotify: win32more.Media.DirectShow.IMemAllocatorNotifyCallbackTemp_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFreeCount(plBuffersFree: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMemAllocatorNotifyCallbackTemp(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('92980b30-c1de-11d2-ab-f5-00-a0-c9-05-f3-75')
    @commethod(3)
    def NotifyRelease() -> win32more.Foundation.HRESULT: ...
class IMemInputPin(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a8689d-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def GetAllocator(ppAllocator: POINTER(win32more.Media.DirectShow.IMemAllocator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyAllocator(pAllocator: win32more.Media.DirectShow.IMemAllocator_head, bReadOnly: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAllocatorRequirements(pProps: POINTER(win32more.Media.DirectShow.ALLOCATOR_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Receive(pSample: win32more.Media.DirectShow.IMediaSample_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ReceiveMultiple(pSamples: POINTER(win32more.Media.DirectShow.IMediaSample_head), nSamples: Int32, nSamplesProcessed: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ReceiveCanBlock() -> win32more.Foundation.HRESULT: ...
class IMemoryData(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('327fc560-af60-11d0-82-12-00-c0-4f-c3-2c-45')
    @commethod(3)
    def SetBuffer(cbSize: UInt32, pbData: c_char_p_no, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetInfo(pdwLength: POINTER(UInt32), ppbData: POINTER(c_char_p_no), pcbActualData: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetActual(cbDataValid: UInt32) -> win32more.Foundation.HRESULT: ...
class IMixerOCX(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('81a3bd32-dee1-11d1-85-08-00-a0-c9-1f-9c-a0')
    @commethod(3)
    def OnDisplayChange(ulBitsPerPixel: UInt32, ulScreenWidth: UInt32, ulScreenHeight: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAspectRatio(pdwPictAspectRatioX: POINTER(UInt32), pdwPictAspectRatioY: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetVideoSize(pdwVideoWidth: POINTER(UInt32), pdwVideoHeight: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(pdwStatus: POINTER(POINTER(UInt32))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnDraw(hdcDraw: win32more.Graphics.Gdi.HDC, prcDraw: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDrawRegion(lpptTopLeftSC: POINTER(win32more.Foundation.POINT_head), prcDrawCC: POINTER(win32more.Foundation.RECT_head), lprcClip: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(pmdns: win32more.Media.DirectShow.IMixerOCXNotify_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def UnAdvise() -> win32more.Foundation.HRESULT: ...
class IMixerOCXNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('81a3bd31-dee1-11d1-85-08-00-a0-c9-1f-9c-a0')
    @commethod(3)
    def OnInvalidateRect(lpcRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnStatusChange(ulStatusFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnDataChange(ulDataFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IMixerPinConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('593cdde1-0759-11d1-9e-69-00-c0-4f-d7-c1-5b')
    @commethod(3)
    def SetRelativePosition(dwLeft: UInt32, dwTop: UInt32, dwRight: UInt32, dwBottom: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRelativePosition(pdwLeft: POINTER(UInt32), pdwTop: POINTER(UInt32), pdwRight: POINTER(UInt32), pdwBottom: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetZOrder(dwZOrder: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetZOrder(pdwZOrder: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetColorKey(pColorKey: POINTER(win32more.Media.DirectShow.COLORKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetColorKey(pColorKey: POINTER(win32more.Media.DirectShow.COLORKEY_head), pColor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetBlendingParameter(dwBlendingParameter: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetBlendingParameter(pdwBlendingParameter: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetAspectRatioMode(amAspectRatioMode: win32more.Media.DirectShow.AM_ASPECT_RATIO_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetAspectRatioMode(pamAspectRatioMode: POINTER(win32more.Media.DirectShow.AM_ASPECT_RATIO_MODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetStreamTransparent(bStreamTransparent: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetStreamTransparent(pbStreamTransparent: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IMixerPinConfig2(c_void_p):
    extends: win32more.Media.DirectShow.IMixerPinConfig
    Guid = Guid('ebf47182-8764-11d1-9e-69-00-c0-4f-d7-c1-5b')
    @commethod(15)
    def SetOverlaySurfaceColorControls(pColorControl: POINTER(win32more.Graphics.DirectDraw.DDCOLORCONTROL_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetOverlaySurfaceColorControls(pColorControl: POINTER(win32more.Graphics.DirectDraw.DDCOLORCONTROL_head)) -> win32more.Foundation.HRESULT: ...
class IMpeg2Data(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b396d40-f380-4e3c-a5-14-1a-82-bf-6e-bf-e6')
    @commethod(3)
    def GetSection(pid: UInt16, tid: Byte, pFilter: POINTER(win32more.Media.DirectShow.MPEG2_FILTER_head), dwTimeout: UInt32, ppSectionList: POINTER(win32more.Media.DirectShow.ISectionList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTable(pid: UInt16, tid: Byte, pFilter: POINTER(win32more.Media.DirectShow.MPEG2_FILTER_head), dwTimeout: UInt32, ppSectionList: POINTER(win32more.Media.DirectShow.ISectionList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamOfSections(pid: UInt16, tid: Byte, pFilter: POINTER(win32more.Media.DirectShow.MPEG2_FILTER_head), hDataReadyEvent: win32more.Foundation.HANDLE, ppMpegStream: POINTER(win32more.Media.DirectShow.IMpeg2Stream_head)) -> win32more.Foundation.HRESULT: ...
class IMpeg2Demultiplexer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('436eee9c-264f-4242-90-e1-4e-33-0c-10-75-12')
    @commethod(3)
    def CreateOutputPin(pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), pszPinName: win32more.Foundation.PWSTR, ppIPin: POINTER(win32more.Media.DirectShow.IPin_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetOutputPinMediaType(pszPinName: win32more.Foundation.PWSTR, pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteOutputPin(pszPinName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IMpeg2Stream(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('400cc286-32a0-4ce4-90-41-39-57-11-25-a6-35')
    @commethod(3)
    def Initialize(requestType: win32more.Media.DirectShow.MPEG_REQUEST_TYPE, pMpeg2Data: win32more.Media.DirectShow.IMpeg2Data_head, pContext: POINTER(win32more.Media.DirectShow.MPEG_CONTEXT_head), pid: UInt16, tid: Byte, pFilter: POINTER(win32more.Media.DirectShow.MPEG2_FILTER_head), hDataReadyEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SupplyDataBuffer(pStreamBuffer: POINTER(win32more.Media.DirectShow.MPEG_STREAM_BUFFER_head)) -> win32more.Foundation.HRESULT: ...
class IMpeg2TableFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bdcdd913-9ecd-4fb2-81-ae-ad-f7-47-ea-75-a5')
    @commethod(3)
    def AddPID(p: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddTable(p: UInt16, t: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddExtension(p: UInt16, t: Byte, e: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemovePID(p: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveTable(p: UInt16, t: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveExtension(p: UInt16, t: Byte, e: UInt16) -> win32more.Foundation.HRESULT: ...
class IMpegAudioDecoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b45dd570-3c77-11d1-ab-e1-00-a0-c9-05-f3-75')
    @commethod(3)
    def get_FrequencyDivider(pDivider: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_FrequencyDivider(Divider: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_DecoderAccuracy(pAccuracy: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_DecoderAccuracy(Accuracy: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Stereo(pStereo: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Stereo(Stereo: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_DecoderWordSize(pWordSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_DecoderWordSize(WordSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IntegerDecode(pIntDecode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_IntegerDecode(IntDecode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_DualMode(pIntDecode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_DualMode(IntDecode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_AudioFormat(lpFmt: POINTER(win32more.Media.DirectShow.MPEG1WAVEFORMAT_head)) -> win32more.Foundation.HRESULT: ...
class IMultiMediaStream(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b502d1bc-9a57-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(3)
    def GetInformation(pdwFlags: POINTER(win32more.Media.DirectShow.MMSSF_GET_INFORMATION_FLAGS), pStreamType: POINTER(win32more.Media.DirectShow.STREAM_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMediaStream(idPurpose: POINTER(Guid), ppMediaStream: POINTER(win32more.Media.DirectShow.IMediaStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumMediaStreams(Index: Int32, ppMediaStream: POINTER(win32more.Media.DirectShow.IMediaStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetState(pCurrentState: POINTER(win32more.Media.DirectShow.STREAM_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetState(NewState: win32more.Media.DirectShow.STREAM_STATE) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTime(pCurrentTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDuration(pDuration: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(SeekTime: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetEndOfStreamEventHandle(phEOS: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
class IOverlay(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868a1-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def GetPalette(pdwColors: POINTER(UInt32), ppPalette: POINTER(POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPalette(dwColors: UInt32, pPalette: POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDefaultColorKey(pColorKey: POINTER(win32more.Media.DirectShow.COLORKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetColorKey(pColorKey: POINTER(win32more.Media.DirectShow.COLORKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetColorKey(pColorKey: POINTER(win32more.Media.DirectShow.COLORKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetWindowHandle(pHwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetClipList(pSourceRect: POINTER(win32more.Foundation.RECT_head), pDestinationRect: POINTER(win32more.Foundation.RECT_head), ppRgnData: POINTER(POINTER(win32more.Graphics.Gdi.RGNDATA_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetVideoPosition(pSourceRect: POINTER(win32more.Foundation.RECT_head), pDestinationRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Advise(pOverlayNotify: win32more.Media.DirectShow.IOverlayNotify_head, dwInterests: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Unadvise() -> win32more.Foundation.HRESULT: ...
class IOverlayNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868a0-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def OnPaletteChange(dwColors: UInt32, pPalette: POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnClipChange(pSourceRect: POINTER(win32more.Foundation.RECT_head), pDestinationRect: POINTER(win32more.Foundation.RECT_head), pRgnData: POINTER(win32more.Graphics.Gdi.RGNDATA_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnColorKeyChange(pColorKey: POINTER(win32more.Media.DirectShow.COLORKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnPositionChange(pSourceRect: POINTER(win32more.Foundation.RECT_head), pDestinationRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
class IOverlayNotify2(c_void_p):
    extends: win32more.Media.DirectShow.IOverlayNotify
    Guid = Guid('680efa10-d535-11d1-87-c8-00-a0-c9-22-31-96')
    @commethod(7)
    def OnDisplayChange(hMonitor: win32more.Graphics.Gdi.HMONITOR) -> win32more.Foundation.HRESULT: ...
class IPAT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6623b511-4b5f-43c3-9a-01-e8-ff-84-18-80-60')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransportStreamId(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecordProgramNumber(dwIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordProgramMapPid(dwIndex: UInt32, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def FindRecordProgramMapPid(wProgramNumber: UInt16, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetNextTable(ppPAT: POINTER(win32more.Media.DirectShow.IPAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
class IPBDAAttributesDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('313b3620-3263-45a6-95-33-96-8b-ef-be-ac-03')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributePayload(ppbAttributeBuffer: POINTER(c_char_p_no), pdwAttributeLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IPBDAEntitlementDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('22632497-0de3-4587-aa-dc-d8-d9-90-17-e7-60')
    @commethod(3)
    def GetTag(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetToken(ppbTokenBuffer: POINTER(c_char_p_no), pdwTokenLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IPBDASiParser(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9de49a74-aba2-4a18-93-e1-21-f1-7f-95-c3-c3')
    @commethod(3)
    def Initialize(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetEIT(dwSize: UInt32, pBuffer: c_char_p_no, ppEIT: POINTER(win32more.Media.DirectShow.IPBDA_EIT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetServices(dwSize: UInt32, pBuffer: c_char_p_no, ppServices: POINTER(win32more.Media.DirectShow.IPBDA_Services_head)) -> win32more.Foundation.HRESULT: ...
class IPBDA_EIT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a35f2dea-098f-4ebd-98-4c-2b-d4-c3-c8-ce-0a')
    @commethod(3)
    def Initialize(size: UInt32, pBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTableId(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersionNumber(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceIdx(plwVal: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRecordEventId(dwRecordIndex: UInt32, plwVal: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordStartTime(dwRecordIndex: UInt32, pmdtVal: POINTER(win32more.Media.DirectShow.MPEG_DATE_AND_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRecordDuration(dwRecordIndex: UInt32, pmdVal: POINTER(win32more.Media.DirectShow.MPEG_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
class IPBDA_Services(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('944eab37-eed4-4850-af-d2-77-e7-ef-eb-44-27')
    @commethod(3)
    def Initialize(size: UInt32, pBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCountOfRecords(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecordByIndex(dwRecordIndex: UInt32, pul64ServiceIdx: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class IPMT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('01f3b398-9527-4736-94-db-51-95-87-8e-97-a8')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgramNumber(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPcrPid(pPidVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCountOfRecords(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecordStreamType(dwRecordIndex: UInt32, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRecordElementaryPid(dwRecordIndex: UInt32, pPidVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRecordCountOfDescriptors(dwRecordIndex: UInt32, pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecordDescriptorByIndex(dwRecordIndex: UInt32, dwDescIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecordDescriptorByTag(dwRecordIndex: UInt32, bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def QueryServiceGatewayInfo(ppDSMCCList: POINTER(POINTER(win32more.Media.DirectShow.DSMCC_ELEMENT_head)), puiCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def QueryMPEInfo(ppMPEList: POINTER(POINTER(win32more.Media.DirectShow.MPE_ELEMENT_head)), puiCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetNextTable(ppPMT: POINTER(win32more.Media.DirectShow.IPMT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
class IPSITables(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('919f24c5-7b14-42ac-a4-b0-2a-e0-8d-af-00-ac')
    @commethod(3)
    def GetTable(dwTSID: UInt32, dwTID_PID: UInt32, dwHashedVer: UInt32, dwPara4: UInt32, ppIUnknown: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IPTFilterLicenseRenewal(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('26d836a5-0c15-44c7-ac-59-b0-da-87-28-f2-40')
    @commethod(3)
    def RenewLicenses(wszFileName: win32more.Foundation.PWSTR, wszExpiredKid: win32more.Foundation.PWSTR, dwCallersId: UInt32, bHighPriority: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CancelLicenseRenewal() -> win32more.Foundation.HRESULT: ...
class IPersistMediaPropertyBag(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('5738e040-b67f-11d0-bd-4d-00-a0-c9-11-ce-86')
    @commethod(4)
    def InitNew() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Load(pPropBag: win32more.Media.DirectShow.IMediaPropertyBag_head, pErrorLog: win32more.System.Com.IErrorLog_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pPropBag: win32more.Media.DirectShow.IMediaPropertyBag_head, fClearDirty: win32more.Foundation.BOOL, fSaveAllProperties: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IPersistTuneXml(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('0754cd31-8d15-47a9-82-15-d2-00-64-15-72-44')
    @commethod(4)
    def InitNew() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Load(varValue: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pvarFragment: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IPersistTuneXmlUtility(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('990237ae-ac11-4614-be-8f-dd-21-7a-4c-b4-cb')
    @commethod(3)
    def Deserialize(varValue: win32more.System.Com.VARIANT, ppObject: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IPersistTuneXmlUtility2(c_void_p):
    extends: win32more.Media.DirectShow.IPersistTuneXmlUtility
    Guid = Guid('992e165f-ea24-4b2f-9a-1d-00-9d-92-12-04-51')
    @commethod(4)
    def Serialize(piTuneRequest: win32more.Media.DirectShow.ITuneRequest_head, pString: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IPin(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a86891-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Connect(pReceivePin: win32more.Media.DirectShow.IPin_head, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReceiveConnection(pConnector: win32more.Media.DirectShow.IPin_head, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnect() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ConnectedTo(pPin: POINTER(win32more.Media.DirectShow.IPin_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ConnectionMediaType(pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def QueryPinInfo(pInfo: POINTER(win32more.Media.DirectShow.PIN_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def QueryDirection(pPinDir: POINTER(win32more.Media.DirectShow.PIN_DIRECTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def QueryId(Id: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def QueryAccept(pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EnumMediaTypes(ppEnum: POINTER(win32more.Media.DirectShow.IEnumMediaTypes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def QueryInternalConnections(apPin: POINTER(win32more.Media.DirectShow.IPin_head), nPin: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EndOfStream() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def BeginFlush() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def EndFlush() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def NewSegment(tStart: Int64, tStop: Int64, dRate: Double) -> win32more.Foundation.HRESULT: ...
class IPinConnection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4a9a62d3-27d4-403d-91-e9-89-f5-40-e5-55-34')
    @commethod(3)
    def DynamicQueryAccept(pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyEndOfStream(hNotifyEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsEndPin() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DynamicDisconnect() -> win32more.Foundation.HRESULT: ...
class IPinFlowControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c56e9858-dbf3-4f6b-81-19-38-4a-f2-06-0d-eb')
    @commethod(3)
    def Block(dwBlockFlags: UInt32, hEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
class IPinInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868bd-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def get_Pin(ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ConnectedTo(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ConnectionMediaType(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_FilterInfo(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(ppUnk: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Direction(ppDirection: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_PinID(strPinID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_MediaTypes(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Connect(pPin: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ConnectDirect(pPin: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ConnectWithType(pPin: win32more.System.Com.IUnknown_head, pMediaType: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Disconnect() -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Render() -> win32more.Foundation.HRESULT: ...
class IQualProp(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1bd0ecb0-f8e2-11ce-aa-c6-00-20-af-0b-99-a3')
    @commethod(3)
    def get_FramesDroppedInRenderer(pcFrames: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_FramesDrawn(pcFramesDrawn: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_AvgFrameRate(piAvgFrameRate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Jitter(iJitter: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_AvgSyncOffset(piAvg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_DevSyncOffset(piDev: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IQualityControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868a5-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Notify(pSelf: win32more.Media.DirectShow.IBaseFilter_head, q: win32more.Media.DirectShow.Quality) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetSink(piqc: win32more.Media.DirectShow.IQualityControl_head) -> win32more.Foundation.HRESULT: ...
class IQueueCommand(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868b7-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def InvokeAtStreamTime(pCmd: POINTER(win32more.Media.DirectShow.IDeferredCommand_head), time: Double, iid: POINTER(Guid), dispidMethod: Int32, wFlags: Int16, cArgs: Int32, pDispParams: POINTER(win32more.System.Com.VARIANT_head), pvarResult: POINTER(win32more.System.Com.VARIANT_head), puArgErr: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeAtPresentationTime(pCmd: POINTER(win32more.Media.DirectShow.IDeferredCommand_head), time: Double, iid: POINTER(Guid), dispidMethod: Int32, wFlags: Int16, cArgs: Int32, pDispParams: POINTER(win32more.System.Com.VARIANT_head), pvarResult: POINTER(win32more.System.Com.VARIANT_head), puArgErr: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
class IRegFilterInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868bb-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def get_Name(strName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Filter(ppUnk: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IRegisterServiceProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7b3a2f01-0751-48dd-b5-56-00-47-85-17-1c-54')
    @commethod(3)
    def RegisterService(guidService: POINTER(Guid), pUnkObject: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IRegisterTuner(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('359b3901-572c-4854-bb-49-cd-ef-66-60-6a-25')
    @commethod(3)
    def Register(pTuner: win32more.Media.DirectShow.ITuner_head, pGraph: win32more.Media.DirectShow.IGraphBuilder_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister() -> win32more.Foundation.HRESULT: ...
class IResourceConsumer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868ad-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def AcquireResource(idResource: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseResource(idResource: Int32) -> win32more.Foundation.HRESULT: ...
class IResourceManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868ac-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Register(pName: win32more.Foundation.PWSTR, cResource: Int32, plToken: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterGroup(pName: win32more.Foundation.PWSTR, cResource: Int32, palTokens: POINTER(Int32), plToken: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RequestResource(idResource: Int32, pFocusObject: win32more.System.Com.IUnknown_head, pConsumer: win32more.Media.DirectShow.IResourceConsumer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def NotifyAcquire(idResource: Int32, pConsumer: win32more.Media.DirectShow.IResourceConsumer_head, hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyRelease(idResource: Int32, pConsumer: win32more.Media.DirectShow.IResourceConsumer_head, bStillWant: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CancelRequest(idResource: Int32, pConsumer: win32more.Media.DirectShow.IResourceConsumer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetFocus(pFocusObject: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ReleaseFocus(pFocusObject: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class ISBE2Crossbar(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('547b6d26-3226-487e-82-53-8a-a1-68-74-94-34')
    @commethod(3)
    def EnableDefaultMode(DefaultFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetInitialProfile(ppProfile: POINTER(win32more.Media.DirectShow.ISBE2MediaTypeProfile_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputProfile(pProfile: win32more.Media.DirectShow.ISBE2MediaTypeProfile_head, pcOutputPins: POINTER(UInt32), ppOutputPins: POINTER(win32more.Media.DirectShow.IPin_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumStreams(ppStreams: POINTER(win32more.Media.DirectShow.ISBE2EnumStream_head)) -> win32more.Foundation.HRESULT: ...
class ISBE2EnumStream(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f7611092-9fbc-46ec-a7-c7-54-8e-a7-8b-71-a4')
    @commethod(3)
    def Next(cRequest: UInt32, pStreamDesc: POINTER(win32more.Media.DirectShow.SBE2_STREAM_DESC_head), pcReceived: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cRecords: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppIEnumStream: POINTER(win32more.Media.DirectShow.ISBE2EnumStream_head)) -> win32more.Foundation.HRESULT: ...
class ISBE2FileScan(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3e2bf5a5-4f96-4899-a1-a3-75-e8-be-9a-5a-c0')
    @commethod(3)
    def RepairFile(filename: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class ISBE2GlobalEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('caede759-b6b1-11db-a5-78-00-18-f3-fa-24-c6')
    @commethod(3)
    def GetEvent(idEvt: POINTER(Guid), param1: UInt32, param2: UInt32, param3: UInt32, param4: UInt32, pSpanning: POINTER(win32more.Foundation.BOOL), pcb: POINTER(UInt32), pb: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class ISBE2GlobalEvent2(c_void_p):
    extends: win32more.Media.DirectShow.ISBE2GlobalEvent
    Guid = Guid('6d8309bf-00fe-4506-8b-03-f8-c6-5b-5c-9b-39')
    @commethod(4)
    def GetEventEx(idEvt: POINTER(Guid), param1: UInt32, param2: UInt32, param3: UInt32, param4: UInt32, pSpanning: POINTER(win32more.Foundation.BOOL), pcb: POINTER(UInt32), pb: c_char_p_no, pStreamTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class ISBE2MediaTypeProfile(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f238267d-4671-40d7-99-7e-25-dc-32-cf-ed-2a')
    @commethod(3)
    def GetStreamCount(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetStream(Index: UInt32, ppMediaType: POINTER(POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddStream(pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteStream(Index: UInt32) -> win32more.Foundation.HRESULT: ...
class ISBE2SpanningEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('caede760-b6b1-11db-a5-78-00-18-f3-fa-24-c6')
    @commethod(3)
    def GetEvent(idEvt: POINTER(Guid), streamId: UInt32, pcb: POINTER(UInt32), pb: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class ISBE2StreamMap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('667c7745-85b1-4c55-ae-55-4e-25-05-61-59-fc')
    @commethod(3)
    def MapStream(Stream: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnmapStream(Stream: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumMappedStreams(ppStreams: POINTER(win32more.Media.DirectShow.ISBE2EnumStream_head)) -> win32more.Foundation.HRESULT: ...
class ISCTE_EAS(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1ff544d6-161d-4fae-9f-aa-4f-9f-49-2a-e9-99')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSequencyNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetProtocolVersion(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetEASEventID(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetOriginatorCode(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetEASEventCodeLen(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetEASEventCode(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRawNatureOfActivationTextLen(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRawNatureOfActivationText(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetNatureOfActivationText(bstrIS0639code: win32more.Foundation.BSTR, pbstrString: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimeRemaining(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetStartTime(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetDuration(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetAlertPriority(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetDetailsOOBSourceID(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetDetailsMajor(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetDetailsMinor(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetDetailsAudioOOBSourceID(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetAlertText(bstrIS0639code: win32more.Foundation.BSTR, pbstrString: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetRawAlertTextLen(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetRawAlertText(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetLocationCount(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetLocationCodes(bIndex: Byte, pbState: c_char_p_no, pbCountySubdivision: c_char_p_no, pwCounty: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetExceptionCount(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetExceptionService(bIndex: Byte, pbIBRef: c_char_p_no, pwFirst: POINTER(UInt16), pwSecond: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
ISDBCAS_REQUEST_ID = Int32
ISDBCAS_REQUEST_ID_EMG: ISDBCAS_REQUEST_ID = 56
ISDBCAS_REQUEST_ID_EMD: ISDBCAS_REQUEST_ID = 58
ISDBSLocator = Guid('6504afed-a629-455c-a7-f1-04-96-4d-ea-5c-c4')
ISDB_CABLE_TV_NETWORK_TYPE = Guid('c974ddb5-41fe-4b25-97-41-92-f0-49-f1-d5-d1')
ISDB_SATELLITE_TV_NETWORK_TYPE = Guid('b0a4e6a0-6a1a-4b83-bb-5b-90-3e-1d-90-e6-b6')
ISDB_S_NETWORK_TYPE = Guid('a1e78202-1459-41b1-9c-a9-2a-92-58-7a-42-cc')
ISDB_TERRESTRIAL_TV_NETWORK_TYPE = Guid('95037f6f-3ac7-4452-b6-c4-45-a9-ce-92-92-a2')
ISDB_T_NETWORK_TYPE = Guid('fc3855a6-c901-4f2e-ab-a8-90-81-5a-fc-6c-83')
class ISIInbandEPG(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f90ad9d0-b854-4b68-9c-c1-b2-cc-96-11-9d-85')
    @commethod(3)
    def StartSIEPGScan() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def StopSIEPGScan() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsSIEPGScanRunning(bRunning: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ISIInbandEPGEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7e47913a-5a89-423d-9a-2b-e1-51-68-85-89-34')
    @commethod(3)
    def SIObjectEvent(pIDVB_EIT: win32more.Media.DirectShow.IDVB_EIT2_head, dwTable_ID: UInt32, dwService_ID: UInt32) -> win32more.Foundation.HRESULT: ...
class IScanningTuner(c_void_p):
    extends: win32more.Media.DirectShow.ITuner
    Guid = Guid('1dfd0a5c-0284-11d3-9d-8e-00-c0-4f-72-d9-80')
    @commethod(13)
    def SeekUp() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SeekDown() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ScanUp(MillisecondsPause: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ScanDown(MillisecondsPause: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def AutoProgram() -> win32more.Foundation.HRESULT: ...
class IScanningTunerEx(c_void_p):
    extends: win32more.Media.DirectShow.IScanningTuner
    Guid = Guid('04bbd195-0e2d-4593-9b-d5-4f-90-8b-c3-3c-f5')
    @commethod(18)
    def GetCurrentLocator(pILocator: POINTER(win32more.Media.DirectShow.ILocator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def PerformExhaustiveScan(dwLowerFreq: Int32, dwHigherFreq: Int32, bFineTune: win32more.Foundation.VARIANT_BOOL, hEvent: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def TerminateCurrentScan(pcurrentFreq: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def ResumeCurrentScan(hEvent: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetTunerScanningCapability(HardwareAssistedScanning: POINTER(Int32), NumStandardsSupported: POINTER(Int32), BroadcastStandards: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetTunerStatus(SecondsLeft: POINTER(Int32), CurrentLockType: POINTER(Int32), AutoDetect: POINTER(Int32), CurrentFreq: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetCurrentTunerStandardCapability(CurrentBroadcastStandard: Guid, SettlingTime: POINTER(Int32), TvStandardsSupported: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetScanSignalTypeFilter(ScanModulationTypes: Int32, AnalogVideoStandard: Int32) -> win32more.Foundation.HRESULT: ...
class ISectionList(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('afec1eb5-2a64-46c6-bf-4b-ae-3c-cb-6a-fd-b0')
    @commethod(3)
    def Initialize(requestType: win32more.Media.DirectShow.MPEG_REQUEST_TYPE, pMpeg2Data: win32more.Media.DirectShow.IMpeg2Data_head, pContext: POINTER(win32more.Media.DirectShow.MPEG_CONTEXT_head), pid: UInt16, tid: Byte, pFilter: POINTER(win32more.Media.DirectShow.MPEG2_FILTER_head), timeout: UInt32, hDoneEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeWithRawSections(pmplSections: POINTER(win32more.Media.DirectShow.MPEG_PACKET_LIST_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CancelPendingRequest() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetNumberOfSections(pCount: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSectionData(sectionNumber: UInt16, pdwRawPacketLength: POINTER(UInt32), ppSection: POINTER(POINTER(win32more.Media.DirectShow.SECTION_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetProgramIdentifier(pPid: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableIdentifier(pTableId: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class ISeekingPassThru(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('36b73883-c2c8-11cf-8b-46-00-80-5f-6c-ef-60')
    @commethod(3)
    def Init(bSupportRendering: win32more.Foundation.BOOL, pPin: win32more.Media.DirectShow.IPin_head) -> win32more.Foundation.HRESULT: ...
class ISelector(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1abdaeca-68b6-4f83-93-71-b4-13-90-7c-7b-9f')
    @commethod(3)
    def get_NumSources(pdwNumSources: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_SourceNodeId(pdwPinId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_SourceNodeId(dwPinId: UInt32) -> win32more.Foundation.HRESULT: ...
class IServiceLocationDescriptor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('58c3c827-9d91-4215-bf-f3-82-0a-49-f0-90-4c')
    @commethod(3)
    def GetPCR_PID(pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberOfElements(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetElementStreamType(bIndex: Byte, pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetElementPID(bIndex: Byte, pwVal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetElementLanguageCode(bIndex: Byte, LangCode: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class ISpecifyParticularPages(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4c437b91-6e9e-11d1-a7-04-00-60-97-c4-e4-76')
    @commethod(3)
    def GetPages(guidWhatPages: POINTER(Guid), pPages: POINTER(win32more.System.Ole.CAUUID_head)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferConfigure(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ce14dfae-4098-4af7-bb-f7-d6-51-1f-83-54-14')
    @commethod(3)
    def SetDirectory(pszDirectoryName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDirectory(ppszDirectoryName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetBackingFileCount(dwMin: UInt32, dwMax: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetBackingFileCount(pdwMin: POINTER(UInt32), pdwMax: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetBackingFileDuration(dwSeconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetBackingFileDuration(pdwSeconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferConfigure2(c_void_p):
    extends: win32more.Media.DirectShow.IStreamBufferConfigure
    Guid = Guid('53e037bf-3992-4282-ae-34-24-87-b4-da-e0-6b')
    @commethod(9)
    def SetMultiplexedPacketSize(cbBytesPerPacket: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetMultiplexedPacketSize(pcbBytesPerPacket: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetFFTransitionRates(dwMaxFullFrameRate: UInt32, dwMaxNonSkippingRate: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFFTransitionRates(pdwMaxFullFrameRate: POINTER(UInt32), pdwMaxNonSkippingRate: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferConfigure3(c_void_p):
    extends: win32more.Media.DirectShow.IStreamBufferConfigure2
    Guid = Guid('7e2d2a1e-7192-4bd7-80-c1-06-1f-d1-d1-04-02')
    @commethod(13)
    def SetStartRecConfig(fStartStopsCur: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetStartRecConfig(pfStartStopsCur: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetNamespace(pszNamespace: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetNamespace(ppszNamespace: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferDataCounters(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9d2a2563-31ab-402e-9a-6b-ad-b9-03-48-94-40')
    @commethod(3)
    def GetData(pPinData: POINTER(win32more.Media.DirectShow.SBE_PIN_DATA_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ResetData() -> win32more.Foundation.HRESULT: ...
class IStreamBufferInitialize(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9ce50f2d-6ba7-40fb-a0-34-50-b1-a6-74-ec-78')
    @commethod(3)
    def SetHKEY(hkeyRoot: win32more.System.Registry.HKEY) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetSIDs(cSIDs: UInt32, ppSID: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferMediaSeeking(c_void_p):
    extends: win32more.Media.DirectShow.IMediaSeeking
    Guid = Guid('f61f5c26-863d-4afa-b0-ba-2f-81-dc-97-85-96')
class IStreamBufferMediaSeeking2(c_void_p):
    extends: win32more.Media.DirectShow.IStreamBufferMediaSeeking
    Guid = Guid('3a439ab0-155f-470a-86-a6-9e-a5-4a-fd-6e-af')
    @commethod(20)
    def SetRateEx(dRate: Double, dwFramesPerSec: UInt32) -> win32more.Foundation.HRESULT: ...
class IStreamBufferRecComp(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9e259a9b-8815-42ae-b0-9f-22-19-70-b1-54-fd')
    @commethod(3)
    def Initialize(pszTargetFilename: win32more.Foundation.PWSTR, pszSBRecProfileRef: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Append(pszSBRecording: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AppendEx(pszSBRecording: win32more.Foundation.PWSTR, rtStart: Int64, rtStop: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentLength(pcSeconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Cancel() -> win32more.Foundation.HRESULT: ...
class IStreamBufferRecordControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ba9b6c99-f3c7-4ff2-92-db-cf-dd-48-51-bf-31')
    @commethod(3)
    def Start(prtStart: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(rtStop: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecordingStatus(phResult: POINTER(win32more.Foundation.HRESULT), pbStarted: POINTER(win32more.Foundation.BOOL), pbStopped: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferRecordingAttribute(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('16ca4e03-fe69-4705-bd-41-5b-7d-fc-0c-95-f3')
    @commethod(3)
    def SetAttribute(ulReserved: UInt32, pszAttributeName: win32more.Foundation.PWSTR, StreamBufferAttributeType: win32more.Media.DirectShow.STREAMBUFFER_ATTR_DATATYPE, pbAttribute: c_char_p_no, cbAttributeLength: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttributeCount(ulReserved: UInt32, pcAttributes: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributeByName(pszAttributeName: win32more.Foundation.PWSTR, pulReserved: POINTER(UInt32), pStreamBufferAttributeType: POINTER(win32more.Media.DirectShow.STREAMBUFFER_ATTR_DATATYPE), pbAttribute: c_char_p_no, pcbLength: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributeByIndex(wIndex: UInt16, pulReserved: POINTER(UInt32), pszAttributeName: win32more.Foundation.PWSTR, pcchNameLength: POINTER(UInt16), pStreamBufferAttributeType: POINTER(win32more.Media.DirectShow.STREAMBUFFER_ATTR_DATATYPE), pbAttribute: c_char_p_no, pcbLength: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumAttributes(ppIEnumStreamBufferAttrib: POINTER(win32more.Media.DirectShow.IEnumStreamBufferRecordingAttrib_head)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('afd1f242-7efd-45ee-ba-4e-40-7a-25-c9-a7-7a')
    @commethod(3)
    def LockProfile(pszStreamBufferFilename: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRecorder(pszFilename: win32more.Foundation.PWSTR, dwRecordType: UInt32, pRecordingIUnknown: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsProfileLocked() -> win32more.Foundation.HRESULT: ...
class IStreamBufferSink2(c_void_p):
    extends: win32more.Media.DirectShow.IStreamBufferSink
    Guid = Guid('db94a660-f4fb-4bfa-bc-c6-fe-15-9a-4e-ea-93')
    @commethod(6)
    def UnlockProfile() -> win32more.Foundation.HRESULT: ...
class IStreamBufferSink3(c_void_p):
    extends: win32more.Media.DirectShow.IStreamBufferSink2
    Guid = Guid('974723f2-887a-4452-93-66-2c-ff-30-57-bc-8f')
    @commethod(7)
    def SetAvailableFilter(prtMin: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IStreamBufferSource(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1c5bd776-6ced-4f44-81-64-5e-ab-0e-98-db-12')
    @commethod(3)
    def SetStreamSink(pIStreamBufferSink: win32more.Media.DirectShow.IStreamBufferSink_head) -> win32more.Foundation.HRESULT: ...
class IStreamBuilder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56a868bf-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def Render(ppinOut: win32more.Media.DirectShow.IPin_head, pGraph: win32more.Media.DirectShow.IGraphBuilder_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Backout(ppinOut: win32more.Media.DirectShow.IPin_head, pGraph: win32more.Media.DirectShow.IGraphBuilder_head) -> win32more.Foundation.HRESULT: ...
class IStreamSample(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b502d1be-9a57-11d0-8f-de-00-c0-4f-d9-18-9d')
    @commethod(3)
    def GetMediaStream(ppMediaStream: POINTER(win32more.Media.DirectShow.IMediaStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSampleTimes(pStartTime: POINTER(Int64), pEndTime: POINTER(Int64), pCurrentTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetSampleTimes(pStartTime: POINTER(Int64), pEndTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Update(dwFlags: UInt32, hEvent: win32more.Foundation.HANDLE, pfnAPC: win32more.Foundation.PAPCFUNC, dwAPCData: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CompletionStatus(dwFlags: UInt32, dwMilliseconds: UInt32) -> win32more.Foundation.HRESULT: ...
class ITSDT(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d19bdb43-405b-4a7c-a7-91-c8-91-10-c3-31-65')
    @commethod(3)
    def Initialize(pSectionList: win32more.Media.DirectShow.ISectionList_head, pMPEGData: win32more.Media.DirectShow.IMpeg2Data_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersionNumber(pbVal: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCountOfTableDescriptors(pdwVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTableDescriptorByIndex(dwIndex: UInt32, ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTableDescriptorByTag(bTag: Byte, pdwCookie: POINTER(UInt32), ppDescriptor: POINTER(win32more.Media.DirectShow.IGenericDescriptor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterForNextTable(hNextTableAvailable: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextTable(ppTSDT: POINTER(win32more.Media.DirectShow.ITSDT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForWhenCurrent(hNextTableIsCurrent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ConvertNextToCurrent() -> win32more.Foundation.HRESULT: ...
class ITuneRequest(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('07ddc146-fc3d-11d2-9d-8c-00-c0-4f-72-d9-80')
    @commethod(7)
    def get_TuningSpace(TuningSpace: POINTER(win32more.Media.DirectShow.ITuningSpace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Components(Components: POINTER(win32more.Media.DirectShow.IComponents_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Clone(NewTuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Locator(Locator: POINTER(win32more.Media.DirectShow.ILocator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Locator(Locator: win32more.Media.DirectShow.ILocator_head) -> win32more.Foundation.HRESULT: ...
class ITuneRequestInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a3b152df-7a90-4218-ac-54-98-30-be-e8-c0-b6')
    @commethod(3)
    def GetLocatorData(Request: win32more.Media.DirectShow.ITuneRequest_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetComponentData(CurrentRequest: win32more.Media.DirectShow.ITuneRequest_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateComponentList(CurrentRequest: win32more.Media.DirectShow.ITuneRequest_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetNextProgram(CurrentRequest: win32more.Media.DirectShow.ITuneRequest_head, TuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPreviousProgram(CurrentRequest: win32more.Media.DirectShow.ITuneRequest_head, TuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetNextLocator(CurrentRequest: win32more.Media.DirectShow.ITuneRequest_head, TuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPreviousLocator(CurrentRequest: win32more.Media.DirectShow.ITuneRequest_head, TuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
class ITuneRequestInfoEx(c_void_p):
    extends: win32more.Media.DirectShow.ITuneRequestInfo
    Guid = Guid('ee957c52-b0d0-4e78-8d-d1-b8-7a-08-bf-d8-93')
    @commethod(10)
    def CreateComponentListEx(CurrentRequest: win32more.Media.DirectShow.ITuneRequest_head, ppCurPMT: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ITuner(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('28c52640-018a-11d3-9d-8e-00-c0-4f-72-d9-80')
    @commethod(3)
    def get_TuningSpace(TuningSpace: POINTER(win32more.Media.DirectShow.ITuningSpace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_TuningSpace(TuningSpace: win32more.Media.DirectShow.ITuningSpace_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumTuningSpaces(ppEnum: POINTER(win32more.Media.DirectShow.IEnumTuningSpaces_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_TuneRequest(TuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_TuneRequest(TuneRequest: win32more.Media.DirectShow.ITuneRequest_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Validate(TuneRequest: win32more.Media.DirectShow.ITuneRequest_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_PreferredComponentTypes(ComponentTypes: POINTER(win32more.Media.DirectShow.IComponentTypes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_PreferredComponentTypes(ComponentTypes: win32more.Media.DirectShow.IComponentTypes_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_SignalStrength(Strength: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def TriggerSignalEvents(Interval: Int32) -> win32more.Foundation.HRESULT: ...
class ITunerCap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e60dfa45-8d56-4e65-a8-ab-d6-be-94-12-c2-49')
    @commethod(3)
    def get_SupportedNetworkTypes(ulcNetworkTypesMax: UInt32, pulcNetworkTypes: POINTER(UInt32), pguidNetworkTypes: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_SupportedVideoFormats(pulAMTunerModeType: POINTER(UInt32), pulAnalogVideoStandard: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_AuxInputCount(pulCompositeCount: POINTER(UInt32), pulSvideoCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITunerCapEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ed3e0c66-18c8-4ea6-93-00-f6-84-1f-dd-35-dc')
    @commethod(3)
    def get_Has608_708Caption(pbHasCaption: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class ITuningSpace(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('061c6e30-e622-11d2-94-93-00-c0-4f-72-d9-80')
    @commethod(7)
    def get_UniqueName(Name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_UniqueName(Name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_FriendlyName(Name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_FriendlyName(Name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_CLSID(SpaceCLSID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_NetworkType(NetworkTypeGuid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_NetworkType(NetworkTypeGuid: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get__NetworkType(NetworkTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put__NetworkType(NetworkTypeGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CreateTuneRequest(TuneRequest: POINTER(win32more.Media.DirectShow.ITuneRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def EnumCategoryGUIDs(ppEnum: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def EnumDeviceMonikers(ppEnum: POINTER(win32more.System.Com.IEnumMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_DefaultPreferredComponentTypes(ComponentTypes: POINTER(win32more.Media.DirectShow.IComponentTypes_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_DefaultPreferredComponentTypes(NewComponentTypes: win32more.Media.DirectShow.IComponentTypes_head) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_FrequencyMapping(pMapping: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_FrequencyMapping(Mapping: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_DefaultLocator(LocatorVal: POINTER(win32more.Media.DirectShow.ILocator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_DefaultLocator(LocatorVal: win32more.Media.DirectShow.ILocator_head) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def Clone(NewTS: POINTER(win32more.Media.DirectShow.ITuningSpace_head)) -> win32more.Foundation.HRESULT: ...
class ITuningSpaceContainer(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('5b692e84-e2f1-11d2-94-93-00-c0-4f-72-d9-80')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(NewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(varIndex: win32more.System.Com.VARIANT, TuningSpace: POINTER(win32more.Media.DirectShow.ITuningSpace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Item(varIndex: win32more.System.Com.VARIANT, TuningSpace: win32more.Media.DirectShow.ITuningSpace_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def TuningSpacesForCLSID(SpaceCLSID: win32more.Foundation.BSTR, NewColl: POINTER(win32more.Media.DirectShow.ITuningSpaces_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def _TuningSpacesForCLSID2(SpaceCLSID: POINTER(Guid), NewColl: POINTER(win32more.Media.DirectShow.ITuningSpaces_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def TuningSpacesForName(Name: win32more.Foundation.BSTR, NewColl: POINTER(win32more.Media.DirectShow.ITuningSpaces_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def FindID(TuningSpace: win32more.Media.DirectShow.ITuningSpace_head, ID: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Add(TuningSpace: win32more.Media.DirectShow.ITuningSpace_head, NewIndex: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_EnumTuningSpaces(ppEnum: POINTER(win32more.Media.DirectShow.IEnumTuningSpaces_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Remove(Index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_MaxCount(MaxCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_MaxCount(MaxCount: Int32) -> win32more.Foundation.HRESULT: ...
class ITuningSpaces(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('901284e4-33fe-4b69-8d-63-63-4a-59-6f-37-56')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(NewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(varIndex: win32more.System.Com.VARIANT, TuningSpace: POINTER(win32more.Media.DirectShow.ITuningSpace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_EnumTuningSpaces(NewEnum: POINTER(win32more.Media.DirectShow.IEnumTuningSpaces_head)) -> win32more.Foundation.HRESULT: ...
class IVMRAspectRatioControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ede80b5c-bad6-4623-b5-37-65-58-6c-9f-8d-fd')
    @commethod(3)
    def GetAspectRatioMode(lpdwARMode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetAspectRatioMode(dwARMode: UInt32) -> win32more.Foundation.HRESULT: ...
class IVMRAspectRatioControl9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00d96c29-bbde-4efc-99-01-bb-50-36-39-21-46')
    @commethod(3)
    def GetAspectRatioMode(lpdwARMode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetAspectRatioMode(dwARMode: UInt32) -> win32more.Foundation.HRESULT: ...
class IVMRDeinterlaceControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bb057577-0db8-4e6a-87-a7-1a-8c-9a-50-5a-0f')
    @commethod(3)
    def GetNumberOfDeinterlaceModes(lpVideoDescription: POINTER(win32more.Media.DirectShow.VMRVideoDesc_head), lpdwNumDeinterlaceModes: POINTER(UInt32), lpDeinterlaceModes: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeinterlaceModeCaps(lpDeinterlaceMode: POINTER(Guid), lpVideoDescription: POINTER(win32more.Media.DirectShow.VMRVideoDesc_head), lpDeinterlaceCaps: POINTER(win32more.Media.DirectShow.VMRDeinterlaceCaps_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeinterlaceMode(dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetDeinterlaceMode(dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeinterlacePrefs(lpdwDeinterlacePrefs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDeinterlacePrefs(dwDeinterlacePrefs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetActualDeinterlaceMode(dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IVMRDeinterlaceControl9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a215fb8d-13c2-4f7f-99-3c-00-3d-62-71-a4-59')
    @commethod(3)
    def GetNumberOfDeinterlaceModes(lpVideoDescription: POINTER(win32more.Media.DirectShow.VMR9VideoDesc_head), lpdwNumDeinterlaceModes: POINTER(UInt32), lpDeinterlaceModes: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeinterlaceModeCaps(lpDeinterlaceMode: POINTER(Guid), lpVideoDescription: POINTER(win32more.Media.DirectShow.VMR9VideoDesc_head), lpDeinterlaceCaps: POINTER(win32more.Media.DirectShow.VMR9DeinterlaceCaps_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeinterlaceMode(dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetDeinterlaceMode(dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeinterlacePrefs(lpdwDeinterlacePrefs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDeinterlacePrefs(dwDeinterlacePrefs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetActualDeinterlaceMode(dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IVMRFilterConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9e5530c5-7034-48b4-bb-46-0b-8a-6e-fc-8e-36')
    @commethod(3)
    def SetImageCompositor(lpVMRImgCompositor: win32more.Media.DirectShow.IVMRImageCompositor_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetNumberOfStreams(dwMaxStreams: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfStreams(pdwMaxStreams: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetRenderingPrefs(dwRenderFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRenderingPrefs(pdwRenderFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetRenderingMode(Mode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRenderingMode(pMode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVMRFilterConfig9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5a804648-4f66-4867-9c-43-4f-5c-82-2c-f1-b8')
    @commethod(3)
    def SetImageCompositor(lpVMRImgCompositor: win32more.Media.DirectShow.IVMRImageCompositor9_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetNumberOfStreams(dwMaxStreams: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfStreams(pdwMaxStreams: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetRenderingPrefs(dwRenderFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRenderingPrefs(pdwRenderFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetRenderingMode(Mode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRenderingMode(pMode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVMRImageCompositor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7a4fb5af-479f-4074-bb-40-ce-67-22-e4-3c-82')
    @commethod(3)
    def InitCompositionTarget(pD3DDevice: win32more.System.Com.IUnknown_head, pddsRenderTarget: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TermCompositionTarget(pD3DDevice: win32more.System.Com.IUnknown_head, pddsRenderTarget: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamMediaType(dwStrmID: UInt32, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), fTexture: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CompositeImage(pD3DDevice: win32more.System.Com.IUnknown_head, pddsRenderTarget: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head, pmtRenderTarget: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), rtStart: Int64, rtEnd: Int64, dwClrBkGnd: UInt32, pVideoStreamInfo: POINTER(win32more.Media.DirectShow.VMRVIDEOSTREAMINFO_head), cStreams: UInt32) -> win32more.Foundation.HRESULT: ...
class IVMRImageCompositor9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4a5c89eb-df51-4654-ac-2a-e4-8e-02-bb-ab-f6')
    @commethod(3)
    def InitCompositionDevice(pD3DDevice: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TermCompositionDevice(pD3DDevice: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamMediaType(dwStrmID: UInt32, pmt: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), fTexture: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CompositeImage(pD3DDevice: win32more.System.Com.IUnknown_head, pddsRenderTarget: win32more.Graphics.Direct3D9.IDirect3DSurface9_head, pmtRenderTarget: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head), rtStart: Int64, rtEnd: Int64, dwClrBkGnd: UInt32, pVideoStreamInfo: POINTER(win32more.Media.DirectShow.VMR9VideoStreamInfo_head), cStreams: UInt32) -> win32more.Foundation.HRESULT: ...
class IVMRImagePresenter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ce704fe7-e71e-41fb-ba-a2-c4-40-3e-11-82-f5')
    @commethod(3)
    def StartPresenting(dwUserID: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def StopPresenting(dwUserID: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PresentImage(dwUserID: UIntPtr, lpPresInfo: POINTER(win32more.Media.DirectShow.VMRPRESENTATIONINFO_head)) -> win32more.Foundation.HRESULT: ...
class IVMRImagePresenter9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('69188c61-12a3-40f0-8f-fc-34-2e-7b-43-3f-d7')
    @commethod(3)
    def StartPresenting(dwUserID: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def StopPresenting(dwUserID: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PresentImage(dwUserID: UIntPtr, lpPresInfo: POINTER(win32more.Media.DirectShow.VMR9PresentationInfo_head)) -> win32more.Foundation.HRESULT: ...
class IVMRImagePresenterConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9f3a1c85-8555-49ba-93-5f-be-5b-5b-29-d1-78')
    @commethod(3)
    def SetRenderingPrefs(dwRenderFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRenderingPrefs(dwRenderFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVMRImagePresenterConfig9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('45c15cab-6e22-420a-80-43-ae-1f-0a-c0-2c-7d')
    @commethod(3)
    def SetRenderingPrefs(dwRenderFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRenderingPrefs(dwRenderFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVMRImagePresenterExclModeConfig(c_void_p):
    extends: win32more.Media.DirectShow.IVMRImagePresenterConfig
    Guid = Guid('e6f7ce40-4673-44f1-8f-77-54-99-d6-8c-b4-ea')
    @commethod(5)
    def SetXlcModeDDObjAndPrimarySurface(lpDDObj: win32more.Graphics.DirectDraw.IDirectDraw7_head, lpPrimarySurf: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetXlcModeDDObjAndPrimarySurface(lpDDObj: POINTER(win32more.Graphics.DirectDraw.IDirectDraw7_head), lpPrimarySurf: POINTER(win32more.Graphics.DirectDraw.IDirectDrawSurface7_head)) -> win32more.Foundation.HRESULT: ...
class IVMRMixerBitmap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1e673275-0257-40aa-af-20-7c-60-8d-4a-04-28')
    @commethod(3)
    def SetAlphaBitmap(pBmpParms: POINTER(win32more.Media.DirectShow.VMRALPHABITMAP_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAlphaBitmapParameters(pBmpParms: POINTER(win32more.Media.DirectShow.VMRALPHABITMAP_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAlphaBitmapParameters(pBmpParms: POINTER(win32more.Media.DirectShow.VMRALPHABITMAP_head)) -> win32more.Foundation.HRESULT: ...
class IVMRMixerBitmap9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ced175e5-1935-4820-81-bd-ff-6a-d0-0c-91-08')
    @commethod(3)
    def SetAlphaBitmap(pBmpParms: POINTER(win32more.Media.DirectShow.VMR9AlphaBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAlphaBitmapParameters(pBmpParms: POINTER(win32more.Media.DirectShow.VMR9AlphaBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAlphaBitmapParameters(pBmpParms: POINTER(win32more.Media.DirectShow.VMR9AlphaBitmap_head)) -> win32more.Foundation.HRESULT: ...
class IVMRMixerControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1c1a17b0-bed0-415d-97-4b-dc-66-96-13-15-99')
    @commethod(3)
    def SetAlpha(dwStreamID: UInt32, Alpha: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAlpha(dwStreamID: UInt32, pAlpha: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetZOrder(dwStreamID: UInt32, dwZ: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetZOrder(dwStreamID: UInt32, pZ: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetOutputRect(dwStreamID: UInt32, pRect: POINTER(win32more.Media.DirectShow.NORMALIZEDRECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputRect(dwStreamID: UInt32, pRect: POINTER(win32more.Media.DirectShow.NORMALIZEDRECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackgroundClr(ClrBkg: win32more.Foundation.COLORREF) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackgroundClr(lpClrBkg: POINTER(win32more.Foundation.COLORREF)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetMixingPrefs(dwMixerPrefs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetMixingPrefs(pdwMixerPrefs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVMRMixerControl9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1a777eaa-47c8-4930-b2-c9-8f-ee-1c-1b-0f-3b')
    @commethod(3)
    def SetAlpha(dwStreamID: UInt32, Alpha: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAlpha(dwStreamID: UInt32, pAlpha: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetZOrder(dwStreamID: UInt32, dwZ: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetZOrder(dwStreamID: UInt32, pZ: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetOutputRect(dwStreamID: UInt32, pRect: POINTER(win32more.Media.DirectShow.VMR9NormalizedRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputRect(dwStreamID: UInt32, pRect: POINTER(win32more.Media.DirectShow.VMR9NormalizedRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackgroundClr(ClrBkg: win32more.Foundation.COLORREF) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackgroundClr(lpClrBkg: POINTER(win32more.Foundation.COLORREF)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetMixingPrefs(dwMixerPrefs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetMixingPrefs(pdwMixerPrefs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetProcAmpControl(dwStreamID: UInt32, lpClrControl: POINTER(win32more.Media.DirectShow.VMR9ProcAmpControl_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetProcAmpControl(dwStreamID: UInt32, lpClrControl: POINTER(win32more.Media.DirectShow.VMR9ProcAmpControl_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetProcAmpControlRange(dwStreamID: UInt32, lpClrControl: POINTER(win32more.Media.DirectShow.VMR9ProcAmpControlRange_head)) -> win32more.Foundation.HRESULT: ...
class IVMRMonitorConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9cf0b1b6-fbaa-4b7f-88-cf-cf-1f-13-0a-0d-ce')
    @commethod(3)
    def SetMonitor(pGUID: POINTER(win32more.Media.DirectShow.VMRGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMonitor(pGUID: POINTER(win32more.Media.DirectShow.VMRGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultMonitor(pGUID: POINTER(win32more.Media.DirectShow.VMRGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDefaultMonitor(pGUID: POINTER(win32more.Media.DirectShow.VMRGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetAvailableMonitors(pInfo: POINTER(win32more.Media.DirectShow.VMRMONITORINFO_head), dwMaxInfoArraySize: UInt32, pdwNumDevices: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVMRMonitorConfig9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('46c2e457-8ba0-4eef-b8-0b-06-80-f0-97-87-49')
    @commethod(3)
    def SetMonitor(uDev: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMonitor(puDev: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultMonitor(uDev: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDefaultMonitor(puDev: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetAvailableMonitors(pInfo: POINTER(win32more.Media.DirectShow.VMR9MonitorInfo_head), dwMaxInfoArraySize: UInt32, pdwNumDevices: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVMRSurface(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a9849bbe-9ec8-4263-b7-64-62-73-0f-0d-15-d0')
    @commethod(3)
    def IsSurfaceLocked() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LockSurface(lpSurface: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def UnlockSurface() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSurface(lplpSurface: POINTER(win32more.Graphics.DirectDraw.IDirectDrawSurface7_head)) -> win32more.Foundation.HRESULT: ...
class IVMRSurface9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dfc581a1-6e1f-4c3a-8d-0a-5e-97-92-ea-2a-fc')
    @commethod(3)
    def IsSurfaceLocked() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LockSurface(lpSurface: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def UnlockSurface() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSurface(lplpSurface: POINTER(win32more.Graphics.Direct3D9.IDirect3DSurface9_head)) -> win32more.Foundation.HRESULT: ...
class IVMRSurfaceAllocator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('31ce832e-4484-458b-8c-ca-f4-d7-e3-db-0b-52')
    @commethod(3)
    def AllocateSurface(dwUserID: UIntPtr, lpAllocInfo: POINTER(win32more.Media.DirectShow.VMRALLOCATIONINFO_head), lpdwActualBuffers: POINTER(UInt32), lplpSurface: POINTER(win32more.Graphics.DirectDraw.IDirectDrawSurface7_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FreeSurface(dwID: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareSurface(dwUserID: UIntPtr, lpSurface: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head, dwSurfaceFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AdviseNotify(lpIVMRSurfAllocNotify: win32more.Media.DirectShow.IVMRSurfaceAllocatorNotify_head) -> win32more.Foundation.HRESULT: ...
class IVMRSurfaceAllocator9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8d5148ea-3f5d-46cf-9d-f1-d1-b8-96-ee-db-1f')
    @commethod(3)
    def InitializeDevice(dwUserID: UIntPtr, lpAllocInfo: POINTER(win32more.Media.DirectShow.VMR9AllocationInfo_head), lpNumBuffers: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TerminateDevice(dwID: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSurface(dwUserID: UIntPtr, SurfaceIndex: UInt32, SurfaceFlags: UInt32, lplpSurface: POINTER(win32more.Graphics.Direct3D9.IDirect3DSurface9_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AdviseNotify(lpIVMRSurfAllocNotify: win32more.Media.DirectShow.IVMRSurfaceAllocatorNotify9_head) -> win32more.Foundation.HRESULT: ...
class IVMRSurfaceAllocatorEx9(c_void_p):
    extends: win32more.Media.DirectShow.IVMRSurfaceAllocator9
    Guid = Guid('6de9a68a-a928-4522-bf-57-65-5a-e3-86-64-56')
    @commethod(7)
    def GetSurfaceEx(dwUserID: UIntPtr, SurfaceIndex: UInt32, SurfaceFlags: UInt32, lplpSurface: POINTER(win32more.Graphics.Direct3D9.IDirect3DSurface9_head), lprcDst: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
class IVMRSurfaceAllocatorNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aada05a8-5a4e-4729-af-0b-ce-a2-7a-ed-51-e2')
    @commethod(3)
    def AdviseSurfaceAllocator(dwUserID: UIntPtr, lpIVRMSurfaceAllocator: win32more.Media.DirectShow.IVMRSurfaceAllocator_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetDDrawDevice(lpDDrawDevice: win32more.Graphics.DirectDraw.IDirectDraw7_head, hMonitor: win32more.Graphics.Gdi.HMONITOR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ChangeDDrawDevice(lpDDrawDevice: win32more.Graphics.DirectDraw.IDirectDraw7_head, hMonitor: win32more.Graphics.Gdi.HMONITOR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RestoreDDrawSurfaces() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyEvent(EventCode: Int32, Param1: IntPtr, Param2: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetBorderColor(clrBorder: win32more.Foundation.COLORREF) -> win32more.Foundation.HRESULT: ...
class IVMRSurfaceAllocatorNotify9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dca3f5df-bb3a-4d03-bd-81-84-61-4b-fb-fa-0c')
    @commethod(3)
    def AdviseSurfaceAllocator(dwUserID: UIntPtr, lpIVRMSurfaceAllocator: win32more.Media.DirectShow.IVMRSurfaceAllocator9_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetD3DDevice(lpD3DDevice: win32more.Graphics.Direct3D9.IDirect3DDevice9_head, hMonitor: win32more.Graphics.Gdi.HMONITOR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ChangeD3DDevice(lpD3DDevice: win32more.Graphics.Direct3D9.IDirect3DDevice9_head, hMonitor: win32more.Graphics.Gdi.HMONITOR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateSurfaceHelper(lpAllocInfo: POINTER(win32more.Media.DirectShow.VMR9AllocationInfo_head), lpNumBuffers: POINTER(UInt32), lplpSurface: POINTER(win32more.Graphics.Direct3D9.IDirect3DSurface9_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyEvent(EventCode: Int32, Param1: IntPtr, Param2: IntPtr) -> win32more.Foundation.HRESULT: ...
class IVMRVideoStreamControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('058d1f11-2a54-4bef-bd-54-df-70-66-26-b7-27')
    @commethod(3)
    def SetColorKey(lpClrKey: POINTER(win32more.Graphics.DirectDraw.DDCOLORKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetColorKey(lpClrKey: POINTER(win32more.Graphics.DirectDraw.DDCOLORKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamActiveState(fActive: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamActiveState(lpfActive: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IVMRVideoStreamControl9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d0cfe38b-93e7-4772-89-57-04-00-c4-9a-44-85')
    @commethod(3)
    def SetStreamActiveState(fActive: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamActiveState(lpfActive: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IVMRWindowlessControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0eb1088c-4dcd-46f0-87-8f-39-da-e8-6a-51-b7')
    @commethod(3)
    def GetNativeVideoSize(lpWidth: POINTER(Int32), lpHeight: POINTER(Int32), lpARWidth: POINTER(Int32), lpARHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinIdealVideoSize(lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxIdealVideoSize(lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetVideoPosition(lpSRCRect: POINTER(win32more.Foundation.RECT_head), lpDSTRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetVideoPosition(lpSRCRect: POINTER(win32more.Foundation.RECT_head), lpDSTRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAspectRatioMode(lpAspectRatioMode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetAspectRatioMode(AspectRatioMode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetVideoClippingWindow(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RepaintVideo(hwnd: win32more.Foundation.HWND, hdc: win32more.Graphics.Gdi.HDC) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DisplayModeChanged() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentImage(lpDib: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetBorderColor(Clr: win32more.Foundation.COLORREF) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetBorderColor(lpClr: POINTER(win32more.Foundation.COLORREF)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetColorKey(Clr: win32more.Foundation.COLORREF) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetColorKey(lpClr: POINTER(win32more.Foundation.COLORREF)) -> win32more.Foundation.HRESULT: ...
class IVMRWindowlessControl9(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8f537d09-f85e-4414-b2-3b-50-2e-54-c7-99-27')
    @commethod(3)
    def GetNativeVideoSize(lpWidth: POINTER(Int32), lpHeight: POINTER(Int32), lpARWidth: POINTER(Int32), lpARHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinIdealVideoSize(lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxIdealVideoSize(lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetVideoPosition(lpSRCRect: POINTER(win32more.Foundation.RECT_head), lpDSTRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetVideoPosition(lpSRCRect: POINTER(win32more.Foundation.RECT_head), lpDSTRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAspectRatioMode(lpAspectRatioMode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetAspectRatioMode(AspectRatioMode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetVideoClippingWindow(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RepaintVideo(hwnd: win32more.Foundation.HWND, hdc: win32more.Graphics.Gdi.HDC) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DisplayModeChanged() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentImage(lpDib: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetBorderColor(Clr: win32more.Foundation.COLORREF) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetBorderColor(lpClr: POINTER(win32more.Foundation.COLORREF)) -> win32more.Foundation.HRESULT: ...
class IVPBaseConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetConnectInfo(pdwNumConnectInfo: POINTER(UInt32), pddVPConnectInfo: POINTER(win32more.Graphics.DirectDraw.DDVIDEOPORTCONNECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetConnectInfo(dwChosenEntry: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetVPDataInfo(pamvpDataInfo: POINTER(win32more.Media.DirectShow.AMVPDATAINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxPixelRate(pamvpSize: POINTER(win32more.Media.DirectShow.AMVPSIZE_head), pdwMaxPixelsPerSecond: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def InformVPInputFormats(dwNumFormats: UInt32, pDDPixelFormats: POINTER(win32more.Graphics.DirectDraw.DDPIXELFORMAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetVideoFormats(pdwNumFormats: POINTER(UInt32), pddPixelFormats: POINTER(win32more.Graphics.DirectDraw.DDPIXELFORMAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetVideoFormat(dwChosenEntry: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetInvertPolarity() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetOverlaySurface(ppddOverlaySurface: POINTER(win32more.Graphics.DirectDraw.IDirectDrawSurface_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetDirectDrawKernelHandle(dwDDKernelHandle: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetVideoPortID(dwVideoPortID: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetDDSurfaceKernelHandles(cHandles: UInt32, rgDDKernelHandles: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetSurfaceParameters(dwPitch: UInt32, dwXOrigin: UInt32, dwYOrigin: UInt32) -> win32more.Foundation.HRESULT: ...
class IVPBaseNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def RenegotiateVPParameters() -> win32more.Foundation.HRESULT: ...
class IVPConfig(c_void_p):
    extends: win32more.Media.DirectShow.IVPBaseConfig
    Guid = Guid('bc29a660-30e3-11d0-9e-69-00-c0-4f-d7-c1-5b')
    @commethod(16)
    def IsVPDecimationAllowed(pbIsDecimationAllowed: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetScalingFactors(pamvpSize: POINTER(win32more.Media.DirectShow.AMVPSIZE_head)) -> win32more.Foundation.HRESULT: ...
class IVPManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aac18c18-e186-46d2-82-5d-a1-f8-dc-8e-39-5a')
    @commethod(3)
    def SetVideoPortIndex(dwVideoPortIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVideoPortIndex(pdwVideoPortIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVPNotify(c_void_p):
    extends: win32more.Media.DirectShow.IVPBaseNotify
    Guid = Guid('c76794a1-d6c5-11d0-9e-69-00-c0-4f-d7-c1-5b')
    @commethod(4)
    def SetDeinterlaceMode(mode: win32more.Media.DirectShow.AMVP_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeinterlaceMode(pMode: POINTER(win32more.Media.DirectShow.AMVP_MODE)) -> win32more.Foundation.HRESULT: ...
class IVPNotify2(c_void_p):
    extends: win32more.Media.DirectShow.IVPNotify
    Guid = Guid('ebf47183-8764-11d1-9e-69-00-c0-4f-d7-c1-5b')
    @commethod(6)
    def SetVPSyncMaster(bVPSyncMaster: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetVPSyncMaster(pbVPSyncMaster: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IVPVBIConfig(c_void_p):
    extends: win32more.Media.DirectShow.IVPBaseConfig
    Guid = Guid('ec529b00-1a1f-11d1-ba-d9-00-60-97-44-11-1a')
class IVPVBINotify(c_void_p):
    extends: win32more.Media.DirectShow.IVPBaseNotify
    Guid = Guid('ec529b01-1a1f-11d1-ba-d9-00-60-97-44-11-1a')
class IVideoEncoder(c_void_p):
    extends: win32more.Media.DirectShow.IEncoderAPI
    Guid = Guid('02997c3b-8e1b-460e-92-70-54-5e-0d-e9-56-3e')
class IVideoFrameStep(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e46a9787-2b71-444d-a4-b5-1f-ab-7b-70-8d-6a')
    @commethod(3)
    def Step(dwFrames: UInt32, pStepObject: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CanStep(bMultiple: Int32, pStepObject: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CancelStep() -> win32more.Foundation.HRESULT: ...
class IVideoProcAmp(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4050560e-42a7-413a-85-c2-09-26-9a-2d-0f-44')
    @commethod(3)
    def get_BacklightCompensation(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_BacklightCompensation(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def getRange_BacklightCompensation(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Brightness(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_Brightness(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def getRange_Brightness(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ColorEnable(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_ColorEnable(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def getRange_ColorEnable(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Contrast(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Contrast(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def getRange_Contrast(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Gamma(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Gamma(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def getRange_Gamma(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Saturation(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Saturation(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def getRange_Saturation(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Sharpness(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Sharpness(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def getRange_Sharpness(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_WhiteBalance(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_WhiteBalance(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def getRange_WhiteBalance(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Gain(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Gain(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def getRange_Gain(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_Hue(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_Hue(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def getRange_Hue(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_DigitalMultiplier(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_DigitalMultiplier(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def getRange_DigitalMultiplier(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_PowerlineFrequency(pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_PowerlineFrequency(Value: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def getRange_PowerlineFrequency(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_WhiteBalanceComponent(pValue1: POINTER(Int32), pValue2: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_WhiteBalanceComponent(Value1: Int32, Value2: Int32, Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def getRange_WhiteBalanceComponent(pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IVideoWindow(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('56a868b4-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(7)
    def put_Caption(strCaption: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Caption(strCaption: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_WindowStyle(WindowStyle: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_WindowStyle(WindowStyle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_WindowStyleEx(WindowStyleEx: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_WindowStyleEx(WindowStyleEx: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_AutoShow(AutoShow: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_AutoShow(AutoShow: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_WindowState(WindowState: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_WindowState(WindowState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_BackgroundPalette(BackgroundPalette: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_BackgroundPalette(pBackgroundPalette: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Visible(Visible: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Visible(pVisible: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_Left(Left: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_Left(pLeft: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_Width(Width: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Width(pWidth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_Top(Top: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Top(pTop: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_Height(Height: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Height(pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Owner(Owner: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_Owner(Owner: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_MessageDrain(Drain: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_MessageDrain(Drain: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_BorderColor(Color: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_BorderColor(Color: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_FullScreenMode(FullScreenMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_FullScreenMode(FullScreenMode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def SetWindowForeground(Focus: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def NotifyOwnerMessage(hwnd: IntPtr, uMsg: Int32, wParam: IntPtr, lParam: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def SetWindowPosition(Left: Int32, Top: Int32, Width: Int32, Height: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetWindowPosition(pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def GetMinIdealImageSize(pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def GetMaxIdealImageSize(pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def GetRestorePosition(pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def HideCursor(HideCursor: win32more.Media.DirectShow.OA_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def IsCursorHidden(CursorHidden: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IWMCodecAMVideoAccelerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d98ee251-34e0-4a2d-93-12-9b-4c-78-8d-9f-a1')
    @commethod(3)
    def SetAcceleratorInterface(pIAMVA: win32more.Media.DirectShow.IAMVideoAccelerator_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NegotiateConnection(pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetPlayerNotify(pHook: win32more.Media.WindowsMediaFormat.IWMPlayerTimestampHook_head) -> win32more.Foundation.HRESULT: ...
class IWMCodecVideoAccelerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('990641b0-739f-4e94-a8-08-98-88-da-8f-75-af')
    @commethod(3)
    def NegotiateConnection(pIAMVA: win32more.Media.DirectShow.IAMVideoAccelerator_head, pMediaType: POINTER(win32more.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPlayerNotify(pHook: win32more.Media.WindowsMediaFormat.IWMPlayerTimestampHook_head) -> win32more.Foundation.HRESULT: ...
class IXDSCodec(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c4c4c4b3-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
    @commethod(3)
    def get_XDSToRatObjOK(pHrCoCreateRetVal: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_CCSubstreamService(SubstreamMask: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_CCSubstreamService(pSubstreamMask: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetContentAdvisoryRating(pRat: POINTER(Int32), pPktSeqID: POINTER(Int32), pCallSeqID: POINTER(Int32), pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetXDSPacket(pXDSClassPkt: POINTER(Int32), pXDSTypePkt: POINTER(Int32), pBstrXDSPkt: POINTER(win32more.Foundation.BSTR), pPktSeqID: POINTER(Int32), pCallSeqID: POINTER(Int32), pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrLicenseExpDate(protType: POINTER(win32more.Media.DirectShow.ProtType), lpDateTime: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastErrorCode() -> win32more.Foundation.HRESULT: ...
class IXDSCodecConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c4c4c4d3-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
    @commethod(3)
    def GetSecureChannelObject(ppUnkDRMSecureChannel: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPauseBufferTime(dwPauseBufferTime: UInt32) -> win32more.Foundation.HRESULT: ...
class IXDSCodecEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c4c4c4c3-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
class IXDSToRat(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c5c5c5b0-3abc-11d6-b2-5b-00-c0-4f-a0-c0-26')
    @commethod(7)
    def Init() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ParseXDSBytePair(byte1: Byte, byte2: Byte, pEnSystem: POINTER(win32more.Media.DirectShow.EnTvRat_System), pEnLevel: POINTER(win32more.Media.DirectShow.EnTvRat_GenericLevel), plBfEnAttributes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
InterleavingMode = Int32
INTERLEAVE_NONE: InterleavingMode = 0
INTERLEAVE_CAPTURE: InterleavingMode = 1
INTERLEAVE_FULL: InterleavingMode = 2
INTERLEAVE_NONE_BUFFERED: InterleavingMode = 3
KSCATEGORY_BDA_IP_SINK = Guid('71985f4a-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSCATEGORY_BDA_NETWORK_EPG = Guid('71985f49-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSCATEGORY_BDA_NETWORK_PROVIDER = Guid('71985f4b-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSCATEGORY_BDA_NETWORK_TUNER = Guid('71985f48-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSCATEGORY_BDA_RECEIVER_COMPONENT = Guid('fd0a5af4-b41d-11d2-9c-95-00-c0-4f-79-71-e0')
KSCATEGORY_BDA_TRANSPORT_INFORMATION = Guid('a2e3074f-6c3d-11d3-b6-53-00-c0-4f-79-49-8e')
KSDATAFORMAT_SPECIFIER_BDA_IP = Guid('6b891420-db09-11d2-8f-32-00-c0-4f-79-71-e2')
KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT = Guid('8deda6fd-ac5f-4334-8e-cf-a4-ba-8f-a7-d0-f0')
KSDATAFORMAT_SUBTYPE_ATSC_SI = Guid('b3c7397c-d303-414d-b3-3c-4e-d2-c9-d2-97-33')
KSDATAFORMAT_SUBTYPE_BDA_IP = Guid('5a9a213c-db08-11d2-8f-32-00-c0-4f-79-71-e2')
KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL = Guid('499856e8-e85b-48ed-9b-ea-41-0d-0d-d4-ef-81')
KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT = Guid('f4aeb342-0329-4fdd-a8-fd-4a-ff-49-26-c9-78')
KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP = Guid('951727db-d2ce-4528-96-f6-33-01-fa-bb-2d-e0')
KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP = Guid('762e3f66-336f-48d1-bf-83-2b-00-35-2c-11-f0')
KSDATAFORMAT_SUBTYPE_DVB_SI = Guid('e9dd31a3-221d-4adb-85-32-9a-f3-09-c1-a4-08')
KSDATAFORMAT_SUBTYPE_ISDB_SI = Guid('4a2eeb99-6458-4538-b1-87-04-01-7c-41-41-3f')
KSDATAFORMAT_SUBTYPE_PBDA_TRANSPORT_RAW = Guid('0d7aed42-cb9a-11db-97-05-00-50-56-c0-00-08')
KSDATAFORMAT_TYPE_BDA_ANTENNA = Guid('71985f41-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSDATAFORMAT_TYPE_BDA_IF_SIGNAL = Guid('61be0b47-a5eb-499b-9a-85-5b-16-c0-7f-12-58')
KSDATAFORMAT_TYPE_BDA_IP = Guid('e25f7b8e-cccc-11d2-8f-25-00-c0-4f-79-71-e2')
KSDATAFORMAT_TYPE_BDA_IP_CONTROL = Guid('dadd5799-7d5b-4b63-80-fb-d1-44-2f-26-b6-21')
KSDATAFORMAT_TYPE_MPE = Guid('455f176c-4b06-47ce-9a-ef-8c-ae-f7-3d-f7-b5')
KSDATAFORMAT_TYPE_MPEG2_SECTIONS = Guid('455f176c-4b06-47ce-9a-ef-8c-ae-f7-3d-f7-b5')
class KSEVENTDATA_BDA_RF_TUNER_SCAN_S(Structure):
    EventData: win32more.Media.KernelStreaming.KSEVENTDATA
    StartFrequency: UInt32
    EndFrequency: UInt32
    LockRequested: win32more.Media.DirectShow.BDA_LockType
KSEVENTSETID_BdaCAEvent = Guid('488c4ccc-b768-4129-8e-b1-b0-0a-07-1f-90-68')
KSEVENTSETID_BdaDiseqCEvent = Guid('8b19bbf0-4184-43ac-ad-3c-0c-88-9b-e4-c2-12')
KSEVENTSETID_BdaEvent = Guid('ae7e55b2-96d7-4e29-90-8f-62-f9-5b-2a-16-79')
KSEVENTSETID_BdaPinEvent = Guid('104781cd-50bd-40d5-95-fb-08-7e-0e-86-a5-91')
KSEVENTSETID_BdaTunerEvent = Guid('aab59e17-01c9-4ebf-93-f2-fc-3b-79-b4-6f-91')
KSEVENT_BDA_EVENT_TYPE = Int32
KSEVENT_BDA_EVENT_PENDINGEVENT: KSEVENT_BDA_EVENT_TYPE = 0
KSEVENT_BDA_TUNER = Int32
KSEVENT_BDA_TUNER_SCAN: KSEVENT_BDA_TUNER = 0
KSMETHODSETID_BdaChangeSync = Guid('fd0a5af3-b41d-11d2-9c-95-00-c0-4f-79-71-e0')
KSMETHODSETID_BdaConditionalAccessService = Guid('10ced3b4-320b-41bf-98-24-1b-2e-68-e7-1e-b9')
KSMETHODSETID_BdaDebug = Guid('0d4a90ec-c69d-4ee2-8c-5a-fb-1f-63-a5-0d-a1')
KSMETHODSETID_BdaDeviceConfiguration = Guid('71985f45-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSMETHODSETID_BdaDrmService = Guid('bff6b5bb-b0ae-484c-9d-ca-73-52-8f-b0-b4-6e')
KSMETHODSETID_BdaEventing = Guid('f99492da-6193-4eb0-86-90-66-86-cb-ff-71-3e')
KSMETHODSETID_BdaGuideDataDeliveryService = Guid('8d9d5562-1589-417d-99-ce-ac-53-1d-da-19-f9')
KSMETHODSETID_BdaIsdbConditionalAccess = Guid('5e68c627-16c2-4e6c-b1-e2-d0-01-70-cd-aa-0f')
KSMETHODSETID_BdaMux = Guid('942aafec-4c05-4c74-b8-eb-87-06-c2-a4-94-3f')
KSMETHODSETID_BdaNameValue = Guid('36e07304-9f0d-4e88-91-18-ac-0b-a3-17-b7-f2')
KSMETHODSETID_BdaNameValueA = Guid('0c24096d-5ff5-47de-a8-56-06-2e-58-7e-37-27')
KSMETHODSETID_BdaScanning = Guid('12eb49df-6249-47f3-b1-90-e2-1e-6e-2f-8a-9c')
KSMETHODSETID_BdaTSSelector = Guid('1dcfafe9-b45e-41b3-bb-2a-56-1e-b1-29-ae-98')
KSMETHODSETID_BdaTuner = Guid('b774102f-ac07-478a-82-28-27-42-d9-61-fa-7e')
KSMETHODSETID_BdaUserActivity = Guid('eda5c834-4531-483c-be-0a-94-e6-c9-6f-f3-96')
KSMETHODSETID_BdaWmdrmSession = Guid('4be6fa3d-07cd-4139-8b-80-8c-18-ba-3a-ec-88')
KSMETHODSETID_BdaWmdrmTuner = Guid('86d979cf-a8a7-4f94-b5-fb-14-c0-ac-a6-8f-e6')
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
class KSM_BDA_BUFFER(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulBufferSize: UInt32
    argbBuffer: Byte * 1
class KSM_BDA_CAS_CAPTURETOKEN(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulTokenLength: UInt32
    argbToken: Byte * 1
class KSM_BDA_CAS_CLOSEMMIDIALOG(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: win32more.Foundation.CHAR * 12
    ulDialogNumber: UInt32
    ulReason: UInt32
class KSM_BDA_CAS_ENTITLEMENTTOKEN(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: win32more.Foundation.CHAR * 12
    ulRequestType: UInt32
    ulEntitlementTokenLen: UInt32
    argbEntitlementToken: Byte * 1
class KSM_BDA_CAS_OPENBROADCASTMMI(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: win32more.Foundation.CHAR * 12
    ulEventId: UInt32
class KSM_BDA_DEBUG_LEVEL(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ucDebugLevel: Byte
    ulDebugStringSize: UInt32
    argbDebugString: Byte * 1
class KSM_BDA_DRM_SETDRM(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    NewDRMuuid: Guid
class KSM_BDA_EVENT_COMPLETE(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulEventID: UInt32
    ulEventResult: UInt32
class KSM_BDA_GDDS_SERVICEFROMTUNEXML(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulTuneXmlLength: UInt32
    argbTuneXml: Byte * 1
class KSM_BDA_GDDS_TUNEXMLFROMIDX(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulIdx: UInt64
class KSM_BDA_GPNV_GETVALUE(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulNameLength: UInt32
    cLanguage: win32more.Foundation.CHAR * 12
    argbData: Byte * 1
class KSM_BDA_GPNV_NAMEINDEX(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulValueNameIndex: UInt32
class KSM_BDA_GPNV_SETVALUE(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulDialogRequest: UInt32
    cLanguage: win32more.Foundation.CHAR * 12
    ulNameLength: UInt32
    ulValueLength: UInt32
    argbName: Byte * 1
class KSM_BDA_ISDBCAS_REQUEST(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulRequestID: UInt32
    ulIsdbCommandSize: UInt32
    argbIsdbCommandData: Byte * 1
class KSM_BDA_PIN(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    Anonymous: _Anonymous_e__Union
    Reserved: UInt32
    class _Anonymous_e__Union(Union):
        PinId: UInt32
        PinType: UInt32
class KSM_BDA_PIN_PAIR(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(Union):
        InputPinId: UInt32
        InputPinType: UInt32
    class _Anonymous2_e__Union(Union):
        OutputPinId: UInt32
        OutputPinType: UInt32
class KSM_BDA_SCAN_CAPABILTIES(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    uuidBroadcastStandard: Guid
class KSM_BDA_SCAN_FILTER(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulScanModulationTypeSize: UInt32
    AnalogVideoStandards: UInt64
    argbScanModulationTypes: Byte * 1
class KSM_BDA_SCAN_START(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    LowerFrequency: UInt32
    HigherFrequency: UInt32
class KSM_BDA_TS_SELECTOR_SETTSID(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    usTSID: UInt16
class KSM_BDA_TUNER_TUNEREQUEST(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulTuneLength: UInt32
    argbTuneData: Byte * 1
class KSM_BDA_USERACTIVITY_USEREASON(Structure):
    Method: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulUseReason: UInt32
class KSM_BDA_WMDRMTUNER_GETPIDPROTECTION(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulPID: UInt32
class KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulDialogRequest: UInt32
    cLanguage: win32more.Foundation.CHAR * 12
    ulPurchaseTokenLength: UInt32
    argbDataBuffer: Byte * 1
class KSM_BDA_WMDRMTUNER_SETPIDPROTECTION(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulPID: UInt32
    uuidKeyID: Guid
class KSM_BDA_WMDRMTUNER_SYNCVALUE(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulSyncValue: UInt32
class KSM_BDA_WMDRM_LICENSE(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    uuidKeyID: Guid
class KSM_BDA_WMDRM_RENEWLICENSE(Structure):
    NodeMethod: win32more.Media.KernelStreaming.KSM_NODE
    ulXMRLicenseLength: UInt32
    ulEntitlementTokenLength: UInt32
    argbDataBuffer: Byte * 1
KSNODE_BDA_8PSK_DEMODULATOR = Guid('e957a0e7-dd98-4a3c-81-0b-35-25-15-7a-b6-2e')
KSNODE_BDA_8VSB_DEMODULATOR = Guid('71985f4f-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSNODE_BDA_ANALOG_DEMODULATOR = Guid('634db199-27dd-46b8-ac-fb-ec-c9-8e-61-a2-ad')
KSNODE_BDA_COFDM_DEMODULATOR = Guid('2dac6e05-edbe-4b9c-b3-87-1b-6f-ad-7d-64-95')
KSNODE_BDA_COMMON_CA_POD = Guid('d83ef8fc-f3b8-45ab-8b-71-ec-f7-c3-39-de-b4')
KSNODE_BDA_DRI_DRM = Guid('4f95ad74-cefb-42d2-94-a9-68-c5-b2-c1-aa-be')
KSNODE_BDA_IP_SINK = Guid('71985f4e-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSNODE_BDA_ISDB_S_DEMODULATOR = Guid('edde230a-9086-432d-b8-a5-66-70-26-38-07-e9')
KSNODE_BDA_ISDB_T_DEMODULATOR = Guid('fcea3ae3-2cb2-464d-8f-5d-30-5c-0b-b7-78-a2')
KSNODE_BDA_OPENCABLE_POD = Guid('345812a0-fb7c-4790-aa-7e-b1-db-88-ac-19-c9')
KSNODE_BDA_PBDA_CAS = Guid('c026869f-7129-4e71-86-96-ec-8f-75-29-9b-77')
KSNODE_BDA_PBDA_DRM = Guid('9eeebd03-eea1-450f-96-ae-63-3e-6d-e6-3c-ce')
KSNODE_BDA_PBDA_ISDBCAS = Guid('f2cf2ab3-5b9d-40ae-ab-7c-4e-7a-d0-bd-1c-52')
KSNODE_BDA_PBDA_MUX = Guid('f88c7787-6678-4f4b-a1-3e-da-09-86-1d-68-2b')
KSNODE_BDA_PBDA_TUNER = Guid('aa5e8286-593c-4979-94-94-46-a2-a9-df-e0-76')
KSNODE_BDA_PID_FILTER = Guid('f5412789-b0a0-44e1-ae-4f-ee-99-9b-1b-7f-be')
KSNODE_BDA_QAM_DEMODULATOR = Guid('71985f4d-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSNODE_BDA_QPSK_DEMODULATOR = Guid('6390c905-27c1-4d67-bd-b7-77-c5-0d-07-93-00')
KSNODE_BDA_RF_TUNER = Guid('71985f4c-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSNODE_BDA_TS_SELECTOR = Guid('5eddf185-fed1-4f45-96-85-bb-b7-3c-32-3c-fc')
KSNODE_BDA_VIDEO_ENCODER = Guid('d98429e3-65c9-4ac4-93-aa-76-67-82-83-3b-7a')
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
class KSPROPERTY_BDA_RF_TUNER_CAPS_S(Structure):
    Property: win32more.Media.KernelStreaming.KSP_NODE
    Mode: UInt32
    AnalogStandardsSupported: UInt32
    DigitalStandardsSupported: UInt32
    MinFrequency: UInt32
    MaxFrequency: UInt32
    SettlingTime: UInt32
    AnalogSensingRange: UInt32
    DigitalSensingRange: UInt32
    MilliSecondsPerMHz: UInt32
class KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S(Structure):
    Property: win32more.Media.KernelStreaming.KSP_NODE
    CurrentFrequency: UInt32
    FrequencyRangeMin: UInt32
    FrequencyRangeMax: UInt32
    MilliSecondsLeft: UInt32
class KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S(Structure):
    Property: win32more.Media.KernelStreaming.KSP_NODE
    AutoDetect: win32more.Foundation.BOOL
class KSPROPERTY_BDA_RF_TUNER_STANDARD_S(Structure):
    Property: win32more.Media.KernelStreaming.KSP_NODE
    SignalType: win32more.Media.DirectShow.BDA_SignalType
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
KSPROPERTY_IPSINK = UInt32
KSPROPERTY_IPSINK_MULTICASTLIST: KSPROPERTY_IPSINK = 0
KSPROPERTY_IPSINK_ADAPTER_DESCRIPTION: KSPROPERTY_IPSINK = 1
KSPROPERTY_IPSINK_ADAPTER_ADDRESS: KSPROPERTY_IPSINK = 2
KSPROPSETID_BdaAutodemodulate = Guid('ddf15b12-bd25-11d2-9c-a0-00-c0-4f-79-71-e0')
KSPROPSETID_BdaCA = Guid('b0693766-5278-4ec6-b9-e1-3c-e4-05-60-ef-5a')
KSPROPSETID_BdaDigitalDemodulator = Guid('ef30f379-985b-4d10-b6-40-a7-9d-5e-04-e1-e0')
KSPROPSETID_BdaDiseqCommand = Guid('f84e2ab0-3c6b-45e3-a0-fc-86-69-d4-b8-1f-11')
KSPROPSETID_BdaEthernetFilter = Guid('71985f43-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSPROPSETID_BdaFrequencyFilter = Guid('71985f47-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSPROPSETID_BdaIPv4Filter = Guid('71985f44-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
KSPROPSETID_BdaIPv6Filter = Guid('e1785a74-2a23-4fb3-92-45-a8-f8-80-17-ef-33')
KSPROPSETID_BdaLNBInfo = Guid('992cf102-49f9-4719-a6-64-c4-f2-3e-24-08-f4')
KSPROPSETID_BdaNullTransform = Guid('ddf15b0d-bd25-11d2-9c-a0-00-c0-4f-79-71-e0')
KSPROPSETID_BdaPIDFilter = Guid('d0a67d65-08df-4fec-85-33-e5-b5-50-41-0b-85')
KSPROPSETID_BdaPinControl = Guid('0ded49d5-a8b7-4d5d-97-a1-12-b0-c1-95-87-4d')
KSPROPSETID_BdaSignalStats = Guid('1347d106-cf3a-428a-a5-cb-ac-0d-9a-2a-43-38')
KSPROPSETID_BdaTableSection = Guid('516b99c5-971c-4aaf-b3-f3-d9-fd-a8-a1-5e-16')
KSPROPSETID_BdaTopology = Guid('a14ee835-0a23-11d3-9c-c7-00-c0-4f-79-71-e0')
KSPROPSETID_BdaVoidTransform = Guid('71985f46-1ca1-11d3-9c-c8-00-c0-4f-79-71-e0')
class KSP_BDA_NODE_PIN(Structure):
    Property: win32more.Media.KernelStreaming.KSIDENTIFIER
    ulNodeType: UInt32
    ulInputPinId: UInt32
    ulOutputPinId: UInt32
class KSP_NODE_ESPID(Structure):
    Property: win32more.Media.KernelStreaming.KSP_NODE
    EsPid: UInt32
class KS_BDA_FRAME_INFO(Structure):
    ExtendedHeaderSize: UInt32
    dwFrameFlags: UInt32
    ulEvent: UInt32
    ulChannelNumber: UInt32
    ulSubchannelNumber: UInt32
    ulReason: UInt32
class KS_DATARANGE_BDA_ANTENNA(Structure):
    DataRange: win32more.Media.KernelStreaming.KSDATAFORMAT
class KS_DATARANGE_BDA_TRANSPORT(Structure):
    DataRange: win32more.Media.KernelStreaming.KSDATAFORMAT
    BdaTransportInfo: win32more.Media.DirectShow.BDA_TRANSPORT_INFO
LNB_Source = Int32
BDA_LNB_SOURCE_NOT_SET: LNB_Source = -1
BDA_LNB_SOURCE_NOT_DEFINED: LNB_Source = 0
BDA_LNB_SOURCE_A: LNB_Source = 1
BDA_LNB_SOURCE_B: LNB_Source = 2
BDA_LNB_SOURCE_C: LNB_Source = 3
BDA_LNB_SOURCE_D: LNB_Source = 4
BDA_LNB_SOURCE_MAX: LNB_Source = 5
class LONG_SECTION(Structure):
    TableId: Byte
    Header: _Header_e__Union
    TableIdExtension: UInt16
    Version: _Version_e__Union
    SectionNumber: Byte
    LastSectionNumber: Byte
    RemainingData: Byte * 1
    _pack_ = 1
    class _Header_e__Union(Union):
        S: win32more.Media.DirectShow.MPEG_HEADER_BITS_MIDL
        W: UInt16
        _pack_ = 1
    class _Version_e__Union(Union):
        S: win32more.Media.DirectShow.MPEG_HEADER_VERSION_BITS_MIDL
        B: Byte
LanguageComponentType = Guid('1be49f30-0e1b-11d3-9d-8e-00-c0-4f-72-d9-80')
class LanguageInfo(Structure):
    LangID: UInt16
    lISOLangCode: Int32
LicenseEventBlockReason = Int32
LIC_BadLicense: LicenseEventBlockReason = 0
LIC_NeedIndiv: LicenseEventBlockReason = 1
LIC_Expired: LicenseEventBlockReason = 2
LIC_NeedActivation: LicenseEventBlockReason = 3
LIC_ExtenderBlocked: LicenseEventBlockReason = 4
LocationCodeSchemeType = Int32
SCTE_18: LocationCodeSchemeType = 0
Locator = Guid('0888c883-ac4f-4943-b5-16-2c-38-d9-b3-45-62')
MEDIA_SAMPLE_CONTENT = Int32
MEDIA_TRANSPORT_PACKET: MEDIA_SAMPLE_CONTENT = 0
MEDIA_ELEMENTARY_STREAM: MEDIA_SAMPLE_CONTENT = 1
MEDIA_MPEG2_PSI: MEDIA_SAMPLE_CONTENT = 2
MEDIA_TRANSPORT_PAYLOAD: MEDIA_SAMPLE_CONTENT = 3
MMSSF_GET_INFORMATION_FLAGS = UInt32
MMSSF_HASCLOCK: MMSSF_GET_INFORMATION_FLAGS = 1
MMSSF_SUPPORTSEEK: MMSSF_GET_INFORMATION_FLAGS = 2
MMSSF_ASYNCHRONOUS: MMSSF_GET_INFORMATION_FLAGS = 4
class MPEG1WAVEFORMAT(Structure):
    wfx: win32more.Media.Audio.WAVEFORMATEX
    fwHeadLayer: UInt16
    dwHeadBitrate: UInt32
    fwHeadMode: UInt16
    fwHeadModeExt: UInt16
    wHeadEmphasis: UInt16
    fwHeadFlags: UInt16
    dwPTSLow: UInt32
    dwPTSHigh: UInt32
    _pack_ = 1
MPEG2Component = Guid('055cb2d7-2969-45cd-91-4b-76-89-07-22-f1-12')
MPEG2ComponentType = Guid('418008f3-cf67-4668-96-28-10-dc-52-be-1d-08')
MPEG2StreamType = Int32
MPEG2StreamType_BDA_UNITIALIZED_MPEG2STREAMTYPE: MPEG2StreamType = -1
MPEG2StreamType_Reserved1: MPEG2StreamType = 0
MPEG2StreamType_ISO_IEC_11172_2_VIDEO: MPEG2StreamType = 1
MPEG2StreamType_ISO_IEC_13818_2_VIDEO: MPEG2StreamType = 2
MPEG2StreamType_ISO_IEC_11172_3_AUDIO: MPEG2StreamType = 3
MPEG2StreamType_ISO_IEC_13818_3_AUDIO: MPEG2StreamType = 4
MPEG2StreamType_ISO_IEC_13818_1_PRIVATE_SECTION: MPEG2StreamType = 5
MPEG2StreamType_ISO_IEC_13818_1_PES: MPEG2StreamType = 6
MPEG2StreamType_ISO_IEC_13522_MHEG: MPEG2StreamType = 7
MPEG2StreamType_ANNEX_A_DSM_CC: MPEG2StreamType = 8
MPEG2StreamType_ITU_T_REC_H_222_1: MPEG2StreamType = 9
MPEG2StreamType_ISO_IEC_13818_6_TYPE_A: MPEG2StreamType = 10
MPEG2StreamType_ISO_IEC_13818_6_TYPE_B: MPEG2StreamType = 11
MPEG2StreamType_ISO_IEC_13818_6_TYPE_C: MPEG2StreamType = 12
MPEG2StreamType_ISO_IEC_13818_6_TYPE_D: MPEG2StreamType = 13
MPEG2StreamType_ISO_IEC_13818_1_AUXILIARY: MPEG2StreamType = 14
MPEG2StreamType_ISO_IEC_13818_7_AUDIO: MPEG2StreamType = 15
MPEG2StreamType_ISO_IEC_14496_2_VISUAL: MPEG2StreamType = 16
MPEG2StreamType_ISO_IEC_14496_3_AUDIO: MPEG2StreamType = 17
MPEG2StreamType_ISO_IEC_14496_1_IN_PES: MPEG2StreamType = 18
MPEG2StreamType_ISO_IEC_14496_1_IN_SECTION: MPEG2StreamType = 19
MPEG2StreamType_ISO_IEC_13818_6_DOWNLOAD: MPEG2StreamType = 20
MPEG2StreamType_METADATA_IN_PES: MPEG2StreamType = 21
MPEG2StreamType_METADATA_IN_SECTION: MPEG2StreamType = 22
MPEG2StreamType_METADATA_IN_DATA_CAROUSEL: MPEG2StreamType = 23
MPEG2StreamType_METADATA_IN_OBJECT_CAROUSEL: MPEG2StreamType = 24
MPEG2StreamType_METADATA_IN_DOWNLOAD_PROTOCOL: MPEG2StreamType = 25
MPEG2StreamType_IRPM_STREAMM: MPEG2StreamType = 26
MPEG2StreamType_ITU_T_H264: MPEG2StreamType = 27
MPEG2StreamType_ISO_IEC_13818_1_RESERVED: MPEG2StreamType = 28
MPEG2StreamType_USER_PRIVATE: MPEG2StreamType = 16
MPEG2StreamType_HEVC_VIDEO_OR_TEMPORAL_VIDEO: MPEG2StreamType = 36
MPEG2StreamType_HEVC_TEMPORAL_VIDEO_SUBSET: MPEG2StreamType = 37
MPEG2StreamType_ISO_IEC_USER_PRIVATE: MPEG2StreamType = 128
MPEG2StreamType_DOLBY_AC3_AUDIO: MPEG2StreamType = 129
MPEG2StreamType_DOLBY_DIGITAL_PLUS_AUDIO_ATSC: MPEG2StreamType = 135
MPEG2TuneRequest = Guid('0955ac62-bf2e-4cba-a2-b9-a6-3f-77-2d-46-cf')
MPEG2TuneRequestFactory = Guid('2c63e4eb-4cea-41b8-91-9c-e9-47-ea-19-a7-7c')
class MPEG2_FILTER(Structure):
    bVersionNumber: Byte
    wFilterSize: UInt16
    fUseRawFilteringBits: win32more.Foundation.BOOL
    Filter: Byte * 16
    Mask: Byte * 16
    fSpecifyTableIdExtension: win32more.Foundation.BOOL
    TableIdExtension: UInt16
    fSpecifyVersion: win32more.Foundation.BOOL
    Version: Byte
    fSpecifySectionNumber: win32more.Foundation.BOOL
    SectionNumber: Byte
    fSpecifyCurrentNext: win32more.Foundation.BOOL
    fNext: win32more.Foundation.BOOL
    fSpecifyDsmccOptions: win32more.Foundation.BOOL
    Dsmcc: win32more.Media.DirectShow.DSMCC_FILTER_OPTIONS
    fSpecifyAtscOptions: win32more.Foundation.BOOL
    Atsc: win32more.Media.DirectShow.ATSC_FILTER_OPTIONS
    _pack_ = 1
class MPEG2_FILTER2(Structure):
    Anonymous: _Anonymous_e__Union
    fSpecifyDvbEitOptions: win32more.Foundation.BOOL
    DvbEit: win32more.Media.DirectShow.DVB_EIT_FILTER_OPTIONS
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        bVersion1Bytes: Byte * 124
        class _Anonymous_e__Struct(Structure):
            bVersionNumber: Byte
            wFilterSize: UInt16
            fUseRawFilteringBits: win32more.Foundation.BOOL
            Filter: Byte * 16
            Mask: Byte * 16
            fSpecifyTableIdExtension: win32more.Foundation.BOOL
            TableIdExtension: UInt16
            fSpecifyVersion: win32more.Foundation.BOOL
            Version: Byte
            fSpecifySectionNumber: win32more.Foundation.BOOL
            SectionNumber: Byte
            fSpecifyCurrentNext: win32more.Foundation.BOOL
            fNext: win32more.Foundation.BOOL
            fSpecifyDsmccOptions: win32more.Foundation.BOOL
            Dsmcc: win32more.Media.DirectShow.DSMCC_FILTER_OPTIONS
            fSpecifyAtscOptions: win32more.Foundation.BOOL
            Atsc: win32more.Media.DirectShow.ATSC_FILTER_OPTIONS
            _pack_ = 1
class MPEG2_TRANSPORT_STRIDE(Structure):
    dwOffset: UInt32
    dwPacketLength: UInt32
    dwStride: UInt32
class MPEGLAYER3WAVEFORMAT(Structure):
    wfx: win32more.Media.Audio.WAVEFORMATEX
    wID: UInt16
    fdwFlags: win32more.Media.DirectShow.MPEGLAYER3WAVEFORMAT_FLAGS
    nBlockSize: UInt16
    nFramesPerBlock: UInt16
    nCodecDelay: UInt16
    _pack_ = 1
MPEGLAYER3WAVEFORMAT_FLAGS = UInt32
MPEGLAYER3_FLAG_PADDING_ISO: MPEGLAYER3WAVEFORMAT_FLAGS = 0
MPEGLAYER3_FLAG_PADDING_ON: MPEGLAYER3WAVEFORMAT_FLAGS = 1
MPEGLAYER3_FLAG_PADDING_OFF: MPEGLAYER3WAVEFORMAT_FLAGS = 2
class MPEG_BCS_DEMUX(Structure):
    AVMGraphId: UInt32
    _pack_ = 1
class MPEG_CONTEXT(Structure):
    Type: win32more.Media.DirectShow.MPEG_CONTEXT_TYPE
    U: _U_e__Union
    _pack_ = 1
    class _U_e__Union(Union):
        Demux: win32more.Media.DirectShow.MPEG_BCS_DEMUX
        Winsock: win32more.Media.DirectShow.MPEG_WINSOCK
MPEG_CONTEXT_TYPE = Int32
MPEG_CONTEXT_BCS_DEMUX: MPEG_CONTEXT_TYPE = 0
MPEG_CONTEXT_WINSOCK: MPEG_CONTEXT_TYPE = 1
MPEG_CURRENT_NEXT_BIT = Int32
MPEG_SECTION_IS_NEXT: MPEG_CURRENT_NEXT_BIT = 0
MPEG_SECTION_IS_CURRENT: MPEG_CURRENT_NEXT_BIT = 1
class MPEG_DATE(Structure):
    Date: Byte
    Month: Byte
    Year: UInt16
    _pack_ = 1
class MPEG_DATE_AND_TIME(Structure):
    D: win32more.Media.DirectShow.MPEG_DATE
    T: win32more.Media.DirectShow.MPEG_TIME
    _pack_ = 1
class MPEG_HEADER_BITS(Structure):
    _bitfield: UInt16
    _pack_ = 1
class MPEG_HEADER_BITS_MIDL(Structure):
    Bits: UInt16
    _pack_ = 1
class MPEG_HEADER_VERSION_BITS(Structure):
    _bitfield: Byte
class MPEG_HEADER_VERSION_BITS_MIDL(Structure):
    Bits: Byte
class MPEG_PACKET_LIST(Structure):
    wPacketCount: UInt16
    PacketList: POINTER(win32more.Media.DirectShow.MPEG_RQST_PACKET_head) * 1
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
class MPEG_RQST_PACKET(Structure):
    dwLength: UInt32
    pSection: POINTER(win32more.Media.DirectShow.SECTION_head)
    _pack_ = 1
class MPEG_SERVICE_REQUEST(Structure):
    Type: win32more.Media.DirectShow.MPEG_REQUEST_TYPE
    Context: win32more.Media.DirectShow.MPEG_CONTEXT
    Pid: UInt16
    TableId: Byte
    Filter: win32more.Media.DirectShow.MPEG2_FILTER
    Flags: UInt32
    _pack_ = 1
class MPEG_SERVICE_RESPONSE(Structure):
    IPAddress: UInt32
    Port: UInt16
    _pack_ = 1
class MPEG_STREAM_BUFFER(Structure):
    hr: win32more.Foundation.HRESULT
    dwDataBufferSize: UInt32
    dwSizeOfDataRead: UInt32
    pDataBuffer: c_char_p_no
    _pack_ = 1
class MPEG_STREAM_FILTER(Structure):
    wPidValue: UInt16
    dwFilterSize: UInt32
    fCrcEnabled: win32more.Foundation.BOOL
    rgchFilter: Byte * 16
    rgchMask: Byte * 16
    _pack_ = 1
class MPEG_TIME(Structure):
    Hours: Byte
    Minutes: Byte
    Seconds: Byte
    _pack_ = 1
class MPEG_WINSOCK(Structure):
    AVMGraphId: UInt32
    _pack_ = 1
class MPE_ELEMENT(Structure):
    pid: UInt16
    bComponentTag: Byte
    pNext: POINTER(win32more.Media.DirectShow.MPE_ELEMENT_head)
    _pack_ = 1
MP_CURVE_TYPE = Int32
MP_CURVE_JUMP: MP_CURVE_TYPE = 1
MP_CURVE_LINEAR: MP_CURVE_TYPE = 2
MP_CURVE_SQUARE: MP_CURVE_TYPE = 4
MP_CURVE_INVSQUARE: MP_CURVE_TYPE = 8
MP_CURVE_SINE: MP_CURVE_TYPE = 16
class MP_ENVELOPE_SEGMENT(Structure):
    rtStart: Int64
    rtEnd: Int64
    valStart: Single
    valEnd: Single
    iCurve: win32more.Media.DirectShow.MP_CURVE_TYPE
    flags: UInt32
class MP_PARAMINFO(Structure):
    mpType: win32more.Media.DirectShow.MP_TYPE
    mopCaps: UInt32
    mpdMinValue: Single
    mpdMaxValue: Single
    mpdNeutralValue: Single
    szUnitText: Char * 32
    szLabel: Char * 32
MP_TYPE = Int32
MPT_INT: MP_TYPE = 0
MPT_FLOAT: MP_TYPE = 1
MPT_BOOL: MP_TYPE = 2
MPT_ENUM: MP_TYPE = 3
MPT_MAX: MP_TYPE = 4
MSEventBinder = Guid('577faa18-4518-445e-8f-70-14-73-f8-cf-4b-a4')
MSVidAnalogCaptureToCCA = Guid('942b7909-a28e-49a1-a2-07-34-eb-cb-cb-4b-3b')
MSVidAnalogCaptureToDataServices = Guid('c5702cd6-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
MSVidAnalogCaptureToOverlayMixer = Guid('e18af75a-08af-11d3-b6-4a-00-c0-4f-79-49-8e')
MSVidAnalogCaptureToStreamBufferSink = Guid('9f50e8b1-9530-4ddc-82-5e-1a-f8-1d-47-ae-d6')
MSVidAnalogCaptureToXDS = Guid('3540d440-5b1d-49cb-82-1a-e8-4b-8c-f0-65-a7')
MSVidAnalogTVToEncoder = Guid('28953661-0231-41db-89-86-21-ff-43-88-ee-9b')
MSVidAnalogTunerDevice = Guid('1c15d484-911d-11d2-b6-32-00-c0-4f-79-49-8e')
MSVidAudioRenderer = Guid('37b03544-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
MSVidAudioRendererDevices = Guid('c5702ccf-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
MSVidBDATunerDevice = Guid('a2e3074e-6c3d-11d3-b6-53-00-c0-4f-79-49-8e')
MSVidCCA = Guid('86151827-e47b-45ee-84-21-d1-0e-6e-69-09-79')
MSVidCCAToStreamBufferSink = Guid('3ef76d68-8661-4843-8b-8f-c3-71-63-d8-c9-ce')
MSVidCCService = Int32
MSVidCCService_None: MSVidCCService = 0
MSVidCCService_Caption1: MSVidCCService = 1
MSVidCCService_Caption2: MSVidCCService = 2
MSVidCCService_Text1: MSVidCCService = 3
MSVidCCService_Text2: MSVidCCService = 4
MSVidCCService_XDS: MSVidCCService = 5
MSVidCCToAR = Guid('d76334ca-d89e-4baf-86-ab-dd-b5-93-72-af-c2')
MSVidCCToVMR = Guid('c4bf2784-ae00-41ba-98-28-9c-95-3b-d3-c5-4a')
MSVidClosedCaptioning = Guid('7f9cb14d-48e4-43b6-93-46-1a-eb-c3-9c-64-d3')
MSVidClosedCaptioningSI = Guid('92ed88bf-879e-448f-b6-b6-a3-85-bc-eb-84-6d')
MSVidCtl = Guid('b0edf163-910a-11d2-b6-32-00-c0-4f-79-49-8e')
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
MSVidDataServices = Guid('334125c0-77e5-11d3-b6-53-00-c0-4f-79-49-8e')
MSVidDataServicesToStreamBufferSink = Guid('38f03426-e83b-4e68-b6-5b-dc-ae-73-30-48-38')
MSVidDataServicesToXDS = Guid('0429ec6e-1144-4bed-b8-8b-2f-b9-89-9a-4a-3d')
MSVidDevice = Guid('6e40476f-9c49-4c3e-8b-b9-85-87-95-8e-ff-74')
MSVidDevice2 = Guid('30997f7d-b3b5-4a1c-98-3a-1f-e8-09-8c-b7-7d')
MSVidDigitalCaptureToCCA = Guid('73d14237-b9db-4efa-a6-dd-84-35-04-21-fb-2f')
MSVidDigitalCaptureToITV = Guid('5d8e73f7-4989-4ac8-8a-98-39-ba-0d-32-53-02')
MSVidDigitalCaptureToStreamBufferSink = Guid('abe40035-27c3-4a2f-81-53-66-24-47-16-08-af')
MSVidEVR = Guid('c45268a2-fa81-4e19-b1-e3-72-ed-bd-60-ae-da')
MSVidEncoder = Guid('bb530c63-d9df-4b49-94-39-63-45-39-62-e5-98')
MSVidEncoderToStreamBufferSink = Guid('a0b9b497-afbc-45ad-a8-a6-9b-07-7c-40-d4-f2')
MSVidFeature = Guid('7748530b-c08a-47ea-b2-4c-be-86-95-ff-40-5f')
MSVidFeatures = Guid('c5702cd0-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
MSVidFilePlaybackDevice = Guid('37b0353c-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
MSVidFilePlaybackToAudioRenderer = Guid('cc23f537-18d4-4ece-93-bd-20-7a-84-72-69-79')
MSVidFilePlaybackToVideoRenderer = Guid('b401c5eb-8457-427f-84-ea-a4-d2-36-33-64-b0')
MSVidGenericComposite = Guid('2764bce5-cc39-11d2-b6-39-00-c0-4f-79-49-8e')
MSVidGenericSink = Guid('4a5869cf-929d-4040-ae-03-fc-af-c5-b9-cd-42')
MSVidITVCapture = Guid('5740a302-ef0b-45ce-bf-3b-44-70-a1-4a-89-80')
MSVidITVPlayback = Guid('9e797ed0-5253-4243-a9-b7-bd-06-c5-8f-8e-f3')
MSVidITVToStreamBufferSink = Guid('92b94828-1af7-4e6e-9e-bf-77-06-57-f7-7a-f5')
MSVidInputDevice = Guid('ac1972f2-138a-4ca3-90-da-ae-51-11-2e-da-28')
MSVidInputDevices = Guid('c5702ccc-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
MSVidMPEG2DecoderToClosedCaptioning = Guid('6ad28ee1-5002-4e71-aa-f7-bd-07-79-07-b1-a4')
MSVidOutput = Guid('87eb890d-03ad-4e9d-98-66-37-6e-5e-c5-72-ed')
MSVidOutputDevices = Guid('c5702ccd-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
MSVidRect = Guid('cb4276e6-7d5f-4cf1-97-27-62-9c-5e-6d-b6-ae')
MSVidSBESourceToCC = Guid('9193a8f9-0cba-400e-aa-97-eb-47-09-16-45-76')
MSVidSBESourceToGenericSink = Guid('991da7e5-953f-435b-be-5e-b9-2a-05-ed-fc-42')
MSVidSBESourceToITV = Guid('2291478c-5ee3-4bef-ab-5d-b5-ff-2c-f5-83-52')
MSVidSegmentType = Int32
MSVidSEG_SOURCE: MSVidSegmentType = 0
MSVidSEG_XFORM: MSVidSegmentType = 1
MSVidSEG_DEST: MSVidSegmentType = 2
MSVidSinkStreams = Int32
MSVidSink_Video: MSVidSinkStreams = 1
MSVidSink_Audio: MSVidSinkStreams = 2
MSVidSink_Other: MSVidSinkStreams = 4
MSVidStreamBufferRecordingControl = Guid('caafdd83-cefc-4e3d-ba-03-17-5f-17-a2-4f-91')
MSVidStreamBufferSink = Guid('9e77aac4-35e5-42a1-bd-c2-8f-3f-f3-99-84-7c')
MSVidStreamBufferSource = Guid('ad8e510d-217f-409b-80-76-29-c5-e7-3b-98-e8')
MSVidStreamBufferSourceToVideoRenderer = Guid('3c4708dc-b181-46a8-8d-a8-4a-b0-37-17-58-cd')
MSVidStreamBufferV2Source = Guid('fd351ea1-4173-4af4-82-1d-80-d4-ae-97-90-48')
MSVidVMR9 = Guid('24dc3975-09bf-4231-86-55-3e-e7-1f-43-83-7d')
MSVidVideoInputDevice = Guid('95f4820b-bb3a-4e2d-bc-64-5b-81-7b-c2-c3-0e')
MSVidVideoPlaybackDevice = Guid('1990d634-1a5e-4071-a3-4a-53-aa-ff-ce-9f-36')
MSVidVideoRenderer = Guid('37b03543-a4c8-11d2-b6-34-00-c0-4f-79-49-8e')
MSVidVideoRendererDevices = Guid('c5702cce-9b79-11d3-b6-54-00-c0-4f-79-49-8e')
MSVidWebDVD = Guid('011b3619-fe63-4814-8a-84-15-a1-94-ce-9c-e3')
MSVidWebDVDAdm = Guid('fa7c375b-66a7-4280-87-9d-fd-45-9c-84-bb-02')
MSVidWebDVDToAudioRenderer = Guid('8d04238e-9fd1-41c6-8d-e3-9e-1e-e3-09-e9-35')
MSVidWebDVDToVideoRenderer = Guid('267db0b3-55e3-4902-94-9b-df-8f-5c-ec-01-91')
MSVidXDS = Guid('0149eedf-d08f-4142-8d-73-d2-39-03-d2-1e-90')
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
MUX_PID_TYPE = Int32
PID_OTHER: MUX_PID_TYPE = -1
PID_ELEMENTARY_STREAM: MUX_PID_TYPE = 0
PID_MPEG2_SECTION_PSI_SI: MUX_PID_TYPE = 1
class MainAVIHeader(Structure):
    dwMicroSecPerFrame: UInt32
    dwMaxBytesPerSec: UInt32
    dwPaddingGranularity: UInt32
    dwFlags: UInt32
    dwTotalFrames: UInt32
    dwInitialFrames: UInt32
    dwStreams: UInt32
    dwSuggestedBufferSize: UInt32
    dwWidth: UInt32
    dwHeight: UInt32
    dwReserved: UInt32 * 4
ModulationType = Int32
BDA_MOD_NOT_SET: ModulationType = -1
BDA_MOD_NOT_DEFINED: ModulationType = 0
BDA_MOD_16QAM: ModulationType = 1
BDA_MOD_32QAM: ModulationType = 2
BDA_MOD_64QAM: ModulationType = 3
BDA_MOD_80QAM: ModulationType = 4
BDA_MOD_96QAM: ModulationType = 5
BDA_MOD_112QAM: ModulationType = 6
BDA_MOD_128QAM: ModulationType = 7
BDA_MOD_160QAM: ModulationType = 8
BDA_MOD_192QAM: ModulationType = 9
BDA_MOD_224QAM: ModulationType = 10
BDA_MOD_256QAM: ModulationType = 11
BDA_MOD_320QAM: ModulationType = 12
BDA_MOD_384QAM: ModulationType = 13
BDA_MOD_448QAM: ModulationType = 14
BDA_MOD_512QAM: ModulationType = 15
BDA_MOD_640QAM: ModulationType = 16
BDA_MOD_768QAM: ModulationType = 17
BDA_MOD_896QAM: ModulationType = 18
BDA_MOD_1024QAM: ModulationType = 19
BDA_MOD_QPSK: ModulationType = 20
BDA_MOD_BPSK: ModulationType = 21
BDA_MOD_OQPSK: ModulationType = 22
BDA_MOD_8VSB: ModulationType = 23
BDA_MOD_16VSB: ModulationType = 24
BDA_MOD_ANALOG_AMPLITUDE: ModulationType = 25
BDA_MOD_ANALOG_FREQUENCY: ModulationType = 26
BDA_MOD_8PSK: ModulationType = 27
BDA_MOD_RF: ModulationType = 28
BDA_MOD_16APSK: ModulationType = 29
BDA_MOD_32APSK: ModulationType = 30
BDA_MOD_NBC_QPSK: ModulationType = 31
BDA_MOD_NBC_8PSK: ModulationType = 32
BDA_MOD_DIRECTV: ModulationType = 33
BDA_MOD_ISDB_T_TMCC: ModulationType = 34
BDA_MOD_ISDB_S_TMCC: ModulationType = 35
BDA_MOD_MAX: ModulationType = 36
Mpeg2Data = Guid('c666e115-bb62-4027-a1-13-82-d6-43-fe-2d-99')
Mpeg2DataLib = Guid('dbaf6c1b-b6a4-4898-ae-65-20-4f-0d-95-09-a1')
Mpeg2Stream = Guid('f91d96c7-8509-4d0b-ab-26-a0-dd-10-90-4b-b7')
class Mpeg2TableSampleHdr(Structure):
    SectionCount: Byte
    Reserved: Byte * 3
    SectionOffsets: Int32 * 1
    _pack_ = 1
class NORMALIZEDRECT(Structure):
    left: Single
    top: Single
    right: Single
    bottom: Single
OA_BOOL = Int32
OATRUE: OA_BOOL = -1
OAFALSE: OA_BOOL = 0
OUTPUT_STATE = UInt32
OUTPUT_STATE_Disabled: OUTPUT_STATE = 0
OUTPUT_STATE_ReadData: OUTPUT_STATE = 1
OUTPUT_STATE_RenderData: OUTPUT_STATE = 2
class PBDAParentalControl(Structure):
    rating_system_count: UInt32
    rating_systems: POINTER(win32more.Media.DirectShow.RATING_SYSTEM_head)
    _pack_ = 1
PBDA_ALWAYS_TUNE_IN_MUX = Guid('1e1d7141-583f-4ac2-b0-19-1f-43-0e-da-0f-4c')
class PBDA_TAG_ATTRIBUTE(Structure):
    TableUUId: Guid
    TableId: Byte
    VersionNo: UInt16
    TableDataSize: UInt32
    TableData: Byte * 1
@winfunctype_pointer
def PDXVA2SW_CREATEVIDEOPROCESSDEVICE(pD3DD9: win32more.Graphics.Direct3D9.IDirect3DDevice9_head, pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: win32more.Graphics.Direct3D9.D3DFORMAT, MaxSubStreams: UInt32, phDevice: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_DESTROYVIDEOPROCESSDEVICE(hDevice: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETFILTERPROPERTYRANGE(pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: win32more.Graphics.Direct3D9.D3DFORMAT, FilterSetting: UInt32, pRange: POINTER(win32more.Media.MediaFoundation.DXVA2_ValueRange_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETPROCAMPRANGE(pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: win32more.Graphics.Direct3D9.D3DFORMAT, ProcAmpCap: UInt32, pRange: POINTER(win32more.Media.MediaFoundation.DXVA2_ValueRange_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORCAPS(pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: win32more.Graphics.Direct3D9.D3DFORMAT, pCaps: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoProcessorCaps_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETCOUNT(pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETS(pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), Count: UInt32, pFormats: POINTER(win32more.Graphics.Direct3D9.D3DFORMAT)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATCOUNT(pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: win32more.Graphics.Direct3D9.D3DFORMAT, pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATS(pVideoDesc: POINTER(win32more.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: win32more.Graphics.Direct3D9.D3DFORMAT, Count: UInt32, pFormats: POINTER(win32more.Graphics.Direct3D9.D3DFORMAT)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSBEGINFRAME(hDevice: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSBLT(hDevice: win32more.Foundation.HANDLE, pBlt: POINTER(win32more.Media.DirectShow.DXVA2_VIDEOPROCESSBLT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSENDFRAME(hDevice: win32more.Foundation.HANDLE, pHandleComplete: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSSETRENDERTARGET(hDevice: win32more.Foundation.HANDLE, pRenderTarget: win32more.Graphics.Direct3D9.IDirect3DSurface9_head) -> win32more.Foundation.HRESULT: ...
class PIC_SEQ_SAMPLE(Structure):
    _bitfield: UInt32
class PIDListSpanningEvent(Structure):
    wPIDCount: UInt16
    pulPIDs: UInt32 * 1
class PID_BITS(Structure):
    _bitfield: UInt16
    _pack_ = 1
class PID_BITS_MIDL(Structure):
    Bits: UInt16
    _pack_ = 1
class PID_MAP(Structure):
    ulPID: UInt32
    MediaSampleContent: win32more.Media.DirectShow.MEDIA_SAMPLE_CONTENT
PINNAME_BDA_ANALOG_AUDIO = Guid('d28a580a-9b1f-4b0c-9c-33-9b-f0-a8-ea-63-6b')
PINNAME_BDA_ANALOG_VIDEO = Guid('5c0c8281-5667-486c-84-82-63-e3-1f-01-a6-e9')
PINNAME_BDA_FM_RADIO = Guid('d2855fed-b2d3-4eeb-9b-d0-19-34-36-a2-f8-90')
PINNAME_BDA_IF_PIN = Guid('1a9d4a42-f3cd-48a1-9a-ea-71-de-13-3c-be-14')
PINNAME_BDA_OPENCABLE_PSIP_PIN = Guid('297bb104-e5c9-4ace-b1-23-95-c3-cb-b2-4d-4f')
PINNAME_BDA_TRANSPORT = Guid('78216a81-cfa8-493e-97-11-36-a6-1c-08-bd-9d')
PINNAME_IPSINK_INPUT = Guid('3fdffa70-ac9a-11d2-8f-17-00-c0-4f-79-71-e2')
PINNAME_MPE = Guid('c1b06d73-1dbb-11d3-8f-46-00-c0-4f-79-71-e2')
PIN_DIRECTION = Int32
PINDIR_INPUT: PIN_DIRECTION = 0
PINDIR_OUTPUT: PIN_DIRECTION = 1
class PIN_INFO(Structure):
    pFilter: win32more.Media.DirectShow.IBaseFilter_head
    dir: win32more.Media.DirectShow.PIN_DIRECTION
    achName: Char * 128
PersistTuneXmlUtility = Guid('e77026b0-b97f-4cbb-b7-fb-f4-f0-3a-d6-9f-11')
PhysicalConnectorType = Int32
PhysConn_Video_Tuner: PhysicalConnectorType = 1
PhysConn_Video_Composite: PhysicalConnectorType = 2
PhysConn_Video_SVideo: PhysicalConnectorType = 3
PhysConn_Video_RGB: PhysicalConnectorType = 4
PhysConn_Video_YRYBY: PhysicalConnectorType = 5
PhysConn_Video_SerialDigital: PhysicalConnectorType = 6
PhysConn_Video_ParallelDigital: PhysicalConnectorType = 7
PhysConn_Video_SCSI: PhysicalConnectorType = 8
PhysConn_Video_AUX: PhysicalConnectorType = 9
PhysConn_Video_1394: PhysicalConnectorType = 10
PhysConn_Video_USB: PhysicalConnectorType = 11
PhysConn_Video_VideoDecoder: PhysicalConnectorType = 12
PhysConn_Video_VideoEncoder: PhysicalConnectorType = 13
PhysConn_Video_SCART: PhysicalConnectorType = 14
PhysConn_Video_Black: PhysicalConnectorType = 15
PhysConn_Audio_Tuner: PhysicalConnectorType = 4096
PhysConn_Audio_Line: PhysicalConnectorType = 4097
PhysConn_Audio_Mic: PhysicalConnectorType = 4098
PhysConn_Audio_AESDigital: PhysicalConnectorType = 4099
PhysConn_Audio_SPDIFDigital: PhysicalConnectorType = 4100
PhysConn_Audio_SCSI: PhysicalConnectorType = 4101
PhysConn_Audio_AUX: PhysicalConnectorType = 4102
PhysConn_Audio_1394: PhysicalConnectorType = 4103
PhysConn_Audio_USB: PhysicalConnectorType = 4104
PhysConn_Audio_AudioDecoder: PhysicalConnectorType = 4105
Pilot = Int32
BDA_PILOT_NOT_SET: Pilot = -1
BDA_PILOT_NOT_DEFINED: Pilot = 0
BDA_PILOT_OFF: Pilot = 1
BDA_PILOT_ON: Pilot = 2
BDA_PILOT_MAX: Pilot = 3
Polarisation = Int32
BDA_POLARISATION_NOT_SET: Polarisation = -1
BDA_POLARISATION_NOT_DEFINED: Polarisation = 0
BDA_POLARISATION_LINEAR_H: Polarisation = 1
BDA_POLARISATION_LINEAR_V: Polarisation = 2
BDA_POLARISATION_CIRCULAR_L: Polarisation = 3
BDA_POLARISATION_CIRCULAR_R: Polarisation = 4
BDA_POLARISATION_MAX: Polarisation = 5
PositionModeList = Int32
PositionModeList_FrameMode: PositionModeList = 0
PositionModeList_TenthsSecondsMode: PositionModeList = 1
class ProgramElement(Structure):
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
class Quality(Structure):
    Type: win32more.Media.DirectShow.QualityMessageType
    Proportion: Int32
    Late: Int64
    TimeStamp: Int64
QualityMessageType = Int32
QualityMessageType_Famine: QualityMessageType = 0
QualityMessageType_Flood: QualityMessageType = 1
class RATING_ATTRIBUTE(Structure):
    rating_attribute_id: UInt32
    rating_attribute_value: UInt32
    _pack_ = 1
class RATING_INFO(Structure):
    rating_system_count: UInt32
    lpratingsystem: POINTER(win32more.Media.DirectShow.RATING_SYSTEM_head)
    _pack_ = 1
class RATING_SYSTEM(Structure):
    rating_system_id: Guid
    _bitfield: Byte
    country_code: Byte * 3
    rating_attribute_count: UInt32
    lpratingattrib: POINTER(win32more.Media.DirectShow.RATING_ATTRIBUTE_head)
    _pack_ = 1
RECORDING_TYPE = Int32
RECORDING_TYPE_CONTENT: RECORDING_TYPE = 0
RECORDING_TYPE_REFERENCE: RECORDING_TYPE = 1
class REGFILTER(Structure):
    Clsid: Guid
    Name: win32more.Foundation.PWSTR
class REGFILTER2(Structure):
    dwVersion: UInt32
    dwMerit: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            cPins: UInt32
            rgPins: POINTER(win32more.Media.DirectShow.REGFILTERPINS_head)
        class _Anonymous2_e__Struct(Structure):
            cPins2: UInt32
            rgPins2: POINTER(win32more.Media.DirectShow.REGFILTERPINS2_head)
class REGFILTERPINS(Structure):
    strName: win32more.Foundation.PWSTR
    bRendered: win32more.Foundation.BOOL
    bOutput: win32more.Foundation.BOOL
    bZero: win32more.Foundation.BOOL
    bMany: win32more.Foundation.BOOL
    clsConnectsToFilter: POINTER(Guid)
    strConnectsToPin: win32more.Foundation.PWSTR
    nMediaTypes: UInt32
    lpMediaType: POINTER(win32more.Media.DirectShow.REGPINTYPES_head)
class REGFILTERPINS2(Structure):
    dwFlags: UInt32
    cInstances: UInt32
    nMediaTypes: UInt32
    lpMediaType: POINTER(win32more.Media.DirectShow.REGPINTYPES_head)
    nMediums: UInt32
    lpMedium: POINTER(win32more.Media.DirectShow.REGPINMEDIUM_head)
    clsPinCategory: POINTER(Guid)
class REGPINMEDIUM(Structure):
    clsMedium: Guid
    dw1: UInt32
    dw2: UInt32
class REGPINTYPES(Structure):
    clsMajorType: POINTER(Guid)
    clsMinorType: POINTER(Guid)
REG_PINFLAG = UInt32
REG_PINFLAG_B_ZERO: REG_PINFLAG = 1
REG_PINFLAG_B_RENDERER: REG_PINFLAG = 2
REG_PINFLAG_B_MANY: REG_PINFLAG = 4
REG_PINFLAG_B_OUTPUT: REG_PINFLAG = 8
class RIFFCHUNK(Structure):
    fcc: UInt32
    cb: UInt32
    _pack_ = 2
class RIFFLIST(Structure):
    fcc: UInt32
    cb: UInt32
    fccListType: UInt32
    _pack_ = 2
RecordingType = Int32
CONTENT: RecordingType = 0
REFERENCE: RecordingType = 1
RevokedComponent = Int32
REVOKED_COPP: RevokedComponent = 0
REVOKED_SAC: RevokedComponent = 1
REVOKED_APP_STUB: RevokedComponent = 2
REVOKED_SECURE_PIPELINE: RevokedComponent = 3
REVOKED_MAX_TYPES: RevokedComponent = 4
RollOff = Int32
BDA_ROLL_OFF_NOT_SET: RollOff = -1
BDA_ROLL_OFF_NOT_DEFINED: RollOff = 0
BDA_ROLL_OFF_20: RollOff = 1
BDA_ROLL_OFF_25: RollOff = 2
BDA_ROLL_OFF_35: RollOff = 3
BDA_ROLL_OFF_MAX: RollOff = 4
class SAMPLE_LIVE_STREAM_TIME(Structure):
    qwStreamTime: UInt64
    qwLiveTime: UInt64
class SAMPLE_SEQ_OFFSET(Structure):
    _bitfield: UInt32
class SBE2_STREAM_DESC(Structure):
    Version: UInt32
    StreamId: UInt32
    Default: UInt32
    Reserved: UInt32
class SBE_PIN_DATA(Structure):
    cDataBytes: UInt64
    cSamplesProcessed: UInt64
    cDiscontinuities: UInt64
    cSyncPoints: UInt64
    cTimestamps: UInt64
class SECTION(Structure):
    TableId: Byte
    Header: _Header_e__Union
    SectionData: Byte * 1
    _pack_ = 1
    class _Header_e__Union(Union):
        S: win32more.Media.DirectShow.MPEG_HEADER_BITS_MIDL
        W: UInt16
        _pack_ = 1
SNDDEV_ERR = Int32
SNDDEV_ERROR_Open: SNDDEV_ERR = 1
SNDDEV_ERROR_Close: SNDDEV_ERR = 2
SNDDEV_ERROR_GetCaps: SNDDEV_ERR = 3
SNDDEV_ERROR_PrepareHeader: SNDDEV_ERR = 4
SNDDEV_ERROR_UnprepareHeader: SNDDEV_ERR = 5
SNDDEV_ERROR_Reset: SNDDEV_ERR = 6
SNDDEV_ERROR_Restart: SNDDEV_ERR = 7
SNDDEV_ERROR_GetPosition: SNDDEV_ERR = 8
SNDDEV_ERROR_Write: SNDDEV_ERR = 9
SNDDEV_ERROR_Pause: SNDDEV_ERR = 10
SNDDEV_ERROR_Stop: SNDDEV_ERR = 11
SNDDEV_ERROR_Start: SNDDEV_ERR = 12
SNDDEV_ERROR_AddBuffer: SNDDEV_ERR = 13
SNDDEV_ERROR_Query: SNDDEV_ERR = 14
SSUPDATE_TYPE = Int32
SSUPDATE_ASYNC: SSUPDATE_TYPE = 1
SSUPDATE_CONTINUOUS: SSUPDATE_TYPE = 2
class STREAMBUFFER_ATTRIBUTE(Structure):
    pszName: win32more.Foundation.PWSTR
    StreamBufferAttributeType: win32more.Media.DirectShow.STREAMBUFFER_ATTR_DATATYPE
    pbAttribute: c_char_p_no
    cbLength: UInt16
STREAMBUFFER_ATTR_DATATYPE = Int32
STREAMBUFFER_TYPE_DWORD: STREAMBUFFER_ATTR_DATATYPE = 0
STREAMBUFFER_TYPE_STRING: STREAMBUFFER_ATTR_DATATYPE = 1
STREAMBUFFER_TYPE_BINARY: STREAMBUFFER_ATTR_DATATYPE = 2
STREAMBUFFER_TYPE_BOOL: STREAMBUFFER_ATTR_DATATYPE = 3
STREAMBUFFER_TYPE_QWORD: STREAMBUFFER_ATTR_DATATYPE = 4
STREAMBUFFER_TYPE_WORD: STREAMBUFFER_ATTR_DATATYPE = 5
STREAMBUFFER_TYPE_GUID: STREAMBUFFER_ATTR_DATATYPE = 6
STREAMIF_CONSTANTS = Int32
MAX_NUMBER_OF_STREAMS: STREAMIF_CONSTANTS = 16
class STREAM_ID_MAP(Structure):
    stream_id: UInt32
    dwMediaSampleContent: UInt32
    ulSubstreamFilterValue: UInt32
    iDataOffset: Int32
STREAM_STATE = Int32
STREAMSTATE_STOP: STREAM_STATE = 0
STREAMSTATE_RUN: STREAM_STATE = 1
STREAM_TYPE = Int32
STREAMTYPE_READ: STREAM_TYPE = 0
STREAMTYPE_WRITE: STREAM_TYPE = 1
STREAMTYPE_TRANSFORM: STREAM_TYPE = 2
ScanModulationTypes = Int32
BDA_SCAN_MOD_16QAM: ScanModulationTypes = 1
BDA_SCAN_MOD_32QAM: ScanModulationTypes = 2
BDA_SCAN_MOD_64QAM: ScanModulationTypes = 4
BDA_SCAN_MOD_80QAM: ScanModulationTypes = 8
BDA_SCAN_MOD_96QAM: ScanModulationTypes = 16
BDA_SCAN_MOD_112QAM: ScanModulationTypes = 32
BDA_SCAN_MOD_128QAM: ScanModulationTypes = 64
BDA_SCAN_MOD_160QAM: ScanModulationTypes = 128
BDA_SCAN_MOD_192QAM: ScanModulationTypes = 256
BDA_SCAN_MOD_224QAM: ScanModulationTypes = 512
BDA_SCAN_MOD_256QAM: ScanModulationTypes = 1024
BDA_SCAN_MOD_320QAM: ScanModulationTypes = 2048
BDA_SCAN_MOD_384QAM: ScanModulationTypes = 4096
BDA_SCAN_MOD_448QAM: ScanModulationTypes = 8192
BDA_SCAN_MOD_512QAM: ScanModulationTypes = 16384
BDA_SCAN_MOD_640QAM: ScanModulationTypes = 32768
BDA_SCAN_MOD_768QAM: ScanModulationTypes = 65536
BDA_SCAN_MOD_896QAM: ScanModulationTypes = 131072
BDA_SCAN_MOD_1024QAM: ScanModulationTypes = 262144
BDA_SCAN_MOD_QPSK: ScanModulationTypes = 524288
BDA_SCAN_MOD_BPSK: ScanModulationTypes = 1048576
BDA_SCAN_MOD_OQPSK: ScanModulationTypes = 2097152
BDA_SCAN_MOD_8VSB: ScanModulationTypes = 4194304
BDA_SCAN_MOD_16VSB: ScanModulationTypes = 8388608
BDA_SCAN_MOD_AM_RADIO: ScanModulationTypes = 16777216
BDA_SCAN_MOD_FM_RADIO: ScanModulationTypes = 33554432
BDA_SCAN_MOD_8PSK: ScanModulationTypes = 67108864
BDA_SCAN_MOD_RF: ScanModulationTypes = 134217728
ScanModulationTypesMask_MCE_DigitalCable: ScanModulationTypes = 11
ScanModulationTypesMask_MCE_TerrestrialATSC: ScanModulationTypes = 23
ScanModulationTypesMask_MCE_AnalogTv: ScanModulationTypes = 28
ScanModulationTypesMask_MCE_All_TV: ScanModulationTypes = -1
ScanModulationTypesMask_DVBC: ScanModulationTypes = 75
BDA_SCAN_MOD_16APSK: ScanModulationTypes = 268435456
BDA_SCAN_MOD_32APSK: ScanModulationTypes = 536870912
SectionList = Guid('73da5d04-4347-45d3-a9-dc-fa-e9-dd-be-55-8d')
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
class SmartCardApplication(Structure):
    ApplicationType: win32more.Media.DirectShow.ApplicationTypeType
    ApplicationVersion: UInt16
    pbstrApplicationName: win32more.Foundation.BSTR
    pbstrApplicationURL: win32more.Foundation.BSTR
SmartCardAssociationType = Int32
SmartCardAssociationType_NotAssociated: SmartCardAssociationType = 0
SmartCardAssociationType_Associated: SmartCardAssociationType = 1
SmartCardAssociationType_AssociationUnknown: SmartCardAssociationType = 2
SmartCardStatusType = Int32
SmartCardStatusType_CardInserted: SmartCardStatusType = 0
SmartCardStatusType_CardRemoved: SmartCardStatusType = 1
SmartCardStatusType_CardError: SmartCardStatusType = 2
SmartCardStatusType_CardDataChanged: SmartCardStatusType = 3
SmartCardStatusType_CardFirmwareUpgrade: SmartCardStatusType = 4
SourceSizeList = Int32
SourceSizeList_sslFullSize: SourceSizeList = 0
SourceSizeList_sslClipByOverScan: SourceSizeList = 1
SourceSizeList_sslClipByClipRect: SourceSizeList = 2
class SpanningEventDescriptor(Structure):
    wDataLen: UInt16
    wProgNumber: UInt16
    wSID: UInt16
    bDescriptor: Byte * 1
class SpanningEventEmmMessage(Structure):
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
SpectralInversion = Int32
BDA_SPECTRAL_INVERSION_NOT_SET: SpectralInversion = -1
BDA_SPECTRAL_INVERSION_NOT_DEFINED: SpectralInversion = 0
BDA_SPECTRAL_INVERSION_AUTOMATIC: SpectralInversion = 1
BDA_SPECTRAL_INVERSION_NORMAL: SpectralInversion = 2
BDA_SPECTRAL_INVERSION_INVERTED: SpectralInversion = 3
BDA_SPECTRAL_INVERSION_MAX: SpectralInversion = 4
SystemTuningSpaces = Guid('d02aac50-027e-11d3-9d-8e-00-c0-4f-72-d9-80')
class TID_EXTENSION(Structure):
    wTidExt: UInt16
    wCount: UInt16
    _pack_ = 1
TIFLoad = Guid('14eb8748-1753-4393-95-ae-4f-7e-7a-87-aa-d6')
class TIMECODEDATA(Structure):
    time: win32more.Media.TIMECODE
    dwSMPTEflags: UInt32
    dwUser: UInt32
    _pack_ = 2
class TRANSPORT_PROPERTIES(Structure):
    PID: UInt32
    PCR: Int64
    Fields: _Fields_e__Union
    class _Fields_e__Union(Union):
        Others: _Others
        Value: Int64
        class _Others(Structure):
            _bitfield: Int64
class TRUECOLORINFO(Structure):
    dwBitMasks: UInt32 * 3
    bmiColors: win32more.Graphics.Gdi.RGBQUAD * 256
TVAudioMode = Int32
AMTVAUDIO_MODE_MONO: TVAudioMode = 1
AMTVAUDIO_MODE_STEREO: TVAudioMode = 2
AMTVAUDIO_MODE_LANG_A: TVAudioMode = 16
AMTVAUDIO_MODE_LANG_B: TVAudioMode = 32
AMTVAUDIO_MODE_LANG_C: TVAudioMode = 64
AMTVAUDIO_PRESET_STEREO: TVAudioMode = 512
AMTVAUDIO_PRESET_LANG_A: TVAudioMode = 4096
AMTVAUDIO_PRESET_LANG_B: TVAudioMode = 8192
AMTVAUDIO_PRESET_LANG_C: TVAudioMode = 16384
TransmissionMode = Int32
BDA_XMIT_MODE_NOT_SET: TransmissionMode = -1
BDA_XMIT_MODE_NOT_DEFINED: TransmissionMode = 0
BDA_XMIT_MODE_2K: TransmissionMode = 1
BDA_XMIT_MODE_8K: TransmissionMode = 2
BDA_XMIT_MODE_4K: TransmissionMode = 3
BDA_XMIT_MODE_2K_INTERLEAVED: TransmissionMode = 4
BDA_XMIT_MODE_4K_INTERLEAVED: TransmissionMode = 5
BDA_XMIT_MODE_1K: TransmissionMode = 6
BDA_XMIT_MODE_16K: TransmissionMode = 7
BDA_XMIT_MODE_32K: TransmissionMode = 8
BDA_XMIT_MODE_MAX: TransmissionMode = 9
TuneRequest = Guid('b46e0d38-ab35-4a06-a1-37-70-57-6b-01-b3-9f')
TunerInputType = Int32
TunerInputType_TunerInputCable: TunerInputType = 0
TunerInputType_TunerInputAntenna: TunerInputType = 1
TunerMarshaler = Guid('6438570b-0c08-4a25-95-04-80-12-bb-4d-50-cf')
TuningSpace = Guid('5ffdc5e6-b83a-4b55-b6-e8-c6-9e-76-5f-e9-db')
class UDCR_TAG(Structure):
    bVersion: Byte
    KID: Byte * 25
    ullBaseCounter: UInt64
    ullBaseCounterRange: UInt64
    fScrambled: win32more.Foundation.BOOL
    bStreamMark: Byte
    dwReserved1: UInt32
    dwReserved2: UInt32
UICloseReasonType = Int32
UICloseReasonType_NotReady: UICloseReasonType = 0
UICloseReasonType_UserClosed: UICloseReasonType = 1
UICloseReasonType_SystemClosed: UICloseReasonType = 2
UICloseReasonType_DeviceClosed: UICloseReasonType = 3
UICloseReasonType_ErrorClosed: UICloseReasonType = 4
VALID_UOP_FLAG = Int32
UOP_FLAG_Play_Title_Or_AtTime: VALID_UOP_FLAG = 1
UOP_FLAG_Play_Chapter: VALID_UOP_FLAG = 2
UOP_FLAG_Play_Title: VALID_UOP_FLAG = 4
UOP_FLAG_Stop: VALID_UOP_FLAG = 8
UOP_FLAG_ReturnFromSubMenu: VALID_UOP_FLAG = 16
UOP_FLAG_Play_Chapter_Or_AtTime: VALID_UOP_FLAG = 32
UOP_FLAG_PlayPrev_Or_Replay_Chapter: VALID_UOP_FLAG = 64
UOP_FLAG_PlayNext_Chapter: VALID_UOP_FLAG = 128
UOP_FLAG_Play_Forwards: VALID_UOP_FLAG = 256
UOP_FLAG_Play_Backwards: VALID_UOP_FLAG = 512
UOP_FLAG_ShowMenu_Title: VALID_UOP_FLAG = 1024
UOP_FLAG_ShowMenu_Root: VALID_UOP_FLAG = 2048
UOP_FLAG_ShowMenu_SubPic: VALID_UOP_FLAG = 4096
UOP_FLAG_ShowMenu_Audio: VALID_UOP_FLAG = 8192
UOP_FLAG_ShowMenu_Angle: VALID_UOP_FLAG = 16384
UOP_FLAG_ShowMenu_Chapter: VALID_UOP_FLAG = 32768
UOP_FLAG_Resume: VALID_UOP_FLAG = 65536
UOP_FLAG_Select_Or_Activate_Button: VALID_UOP_FLAG = 131072
UOP_FLAG_Still_Off: VALID_UOP_FLAG = 262144
UOP_FLAG_Pause_On: VALID_UOP_FLAG = 524288
UOP_FLAG_Select_Audio_Stream: VALID_UOP_FLAG = 1048576
UOP_FLAG_Select_SubPic_Stream: VALID_UOP_FLAG = 2097152
UOP_FLAG_Select_Angle: VALID_UOP_FLAG = 4194304
UOP_FLAG_Select_Karaoke_Audio_Presentation_Mode: VALID_UOP_FLAG = 8388608
UOP_FLAG_Select_Video_Mode_Preference: VALID_UOP_FLAG = 16777216
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
class VA_OPTIONAL_VIDEO_PROPERTIES(Structure):
    dwPictureHeight: UInt16
    dwPictureWidth: UInt16
    dwAspectRatioX: UInt16
    dwAspectRatioY: UInt16
    VAVideoFormat: win32more.Media.DirectShow.VA_VIDEO_FORMAT
    VAColorPrimaries: win32more.Media.DirectShow.VA_COLOR_PRIMARIES
    VATransferCharacteristics: win32more.Media.DirectShow.VA_TRANSFER_CHARACTERISTICS
    VAMatrixCoefficients: win32more.Media.DirectShow.VA_MATRIX_COEFFICIENTS
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
class VFW_FILTERLIST(Structure):
    cFilters: UInt32
    aClsId: Guid * 1
VIDEOENCODER_BITRATE_MODE = Int32
VIDEOENCODER_BITRATE_MODE_ConstantBitRate: VIDEOENCODER_BITRATE_MODE = 0
VIDEOENCODER_BITRATE_MODE_VariableBitRateAverage: VIDEOENCODER_BITRATE_MODE = 1
VIDEOENCODER_BITRATE_MODE_VariableBitRatePeak: VIDEOENCODER_BITRATE_MODE = 2
class VIDEOINFO(Structure):
    rcSource: win32more.Foundation.RECT
    rcTarget: win32more.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    bmiHeader: win32more.Graphics.Gdi.BITMAPINFOHEADER
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        bmiColors: win32more.Graphics.Gdi.RGBQUAD * 256
        dwBitMasks: UInt32 * 3
        TrueColorInfo: win32more.Media.DirectShow.TRUECOLORINFO
class VIDEO_STREAM_CONFIG_CAPS(Structure):
    guid: Guid
    VideoStandard: UInt32
    InputSize: win32more.Foundation.SIZE
    MinCroppingSize: win32more.Foundation.SIZE
    MaxCroppingSize: win32more.Foundation.SIZE
    CropGranularityX: Int32
    CropGranularityY: Int32
    CropAlignX: Int32
    CropAlignY: Int32
    MinOutputSize: win32more.Foundation.SIZE
    MaxOutputSize: win32more.Foundation.SIZE
    OutputGranularityX: Int32
    OutputGranularityY: Int32
    StretchTapsX: Int32
    StretchTapsY: Int32
    ShrinkTapsX: Int32
    ShrinkTapsY: Int32
    MinFrameInterval: Int64
    MaxFrameInterval: Int64
    MinBitsPerSecond: Int32
    MaxBitsPerSecond: Int32
class VMR9AllocationInfo(Structure):
    dwFlags: UInt32
    dwWidth: UInt32
    dwHeight: UInt32
    Format: win32more.Graphics.Direct3D9.D3DFORMAT
    Pool: win32more.Graphics.Direct3D9.D3DPOOL
    MinBuffers: UInt32
    szAspectRatio: win32more.Foundation.SIZE
    szNativeSize: win32more.Foundation.SIZE
class VMR9AlphaBitmap(Structure):
    dwFlags: UInt32
    hdc: win32more.Graphics.Gdi.HDC
    pDDS: win32more.Graphics.Direct3D9.IDirect3DSurface9_head
    rSrc: win32more.Foundation.RECT
    rDest: win32more.Media.DirectShow.VMR9NormalizedRect
    fAlpha: Single
    clrSrcKey: win32more.Foundation.COLORREF
    dwFilterMode: UInt32
VMR9AlphaBitmapFlags = Int32
VMR9AlphaBitmap_Disable: VMR9AlphaBitmapFlags = 1
VMR9AlphaBitmap_hDC: VMR9AlphaBitmapFlags = 2
VMR9AlphaBitmap_EntireDDS: VMR9AlphaBitmapFlags = 4
VMR9AlphaBitmap_SrcColorKey: VMR9AlphaBitmapFlags = 8
VMR9AlphaBitmap_SrcRect: VMR9AlphaBitmapFlags = 16
VMR9AlphaBitmap_FilterMode: VMR9AlphaBitmapFlags = 32
VMR9AspectRatioMode = Int32
VMR9ARMode_None: VMR9AspectRatioMode = 0
VMR9ARMode_LetterBox: VMR9AspectRatioMode = 1
class VMR9DeinterlaceCaps(Structure):
    dwSize: UInt32
    dwNumPreviousOutputFrames: UInt32
    dwNumForwardRefSamples: UInt32
    dwNumBackwardRefSamples: UInt32
    DeinterlaceTechnology: win32more.Media.DirectShow.VMR9DeinterlaceTech
VMR9DeinterlacePrefs = Int32
DeinterlacePref9_NextBest: VMR9DeinterlacePrefs = 1
DeinterlacePref9_BOB: VMR9DeinterlacePrefs = 2
DeinterlacePref9_Weave: VMR9DeinterlacePrefs = 4
DeinterlacePref9_Mask: VMR9DeinterlacePrefs = 7
VMR9DeinterlaceTech = Int32
DeinterlaceTech9_Unknown: VMR9DeinterlaceTech = 0
DeinterlaceTech9_BOBLineReplicate: VMR9DeinterlaceTech = 1
DeinterlaceTech9_BOBVerticalStretch: VMR9DeinterlaceTech = 2
DeinterlaceTech9_MedianFiltering: VMR9DeinterlaceTech = 4
DeinterlaceTech9_EdgeFiltering: VMR9DeinterlaceTech = 16
DeinterlaceTech9_FieldAdaptive: VMR9DeinterlaceTech = 32
DeinterlaceTech9_PixelAdaptive: VMR9DeinterlaceTech = 64
DeinterlaceTech9_MotionVectorSteered: VMR9DeinterlaceTech = 128
class VMR9Frequency(Structure):
    dwNumerator: UInt32
    dwDenominator: UInt32
VMR9MixerPrefs = Int32
MixerPref9_NoDecimation: VMR9MixerPrefs = 1
MixerPref9_DecimateOutput: VMR9MixerPrefs = 2
MixerPref9_ARAdjustXorY: VMR9MixerPrefs = 4
MixerPref9_NonSquareMixing: VMR9MixerPrefs = 8
MixerPref9_DecimateMask: VMR9MixerPrefs = 15
MixerPref9_BiLinearFiltering: VMR9MixerPrefs = 16
MixerPref9_PointFiltering: VMR9MixerPrefs = 32
MixerPref9_AnisotropicFiltering: VMR9MixerPrefs = 64
MixerPref9_PyramidalQuadFiltering: VMR9MixerPrefs = 128
MixerPref9_GaussianQuadFiltering: VMR9MixerPrefs = 256
MixerPref9_FilteringReserved: VMR9MixerPrefs = 3584
MixerPref9_FilteringMask: VMR9MixerPrefs = 4080
MixerPref9_RenderTargetRGB: VMR9MixerPrefs = 4096
MixerPref9_RenderTargetYUV: VMR9MixerPrefs = 8192
MixerPref9_RenderTargetReserved: VMR9MixerPrefs = 1032192
MixerPref9_RenderTargetMask: VMR9MixerPrefs = 1044480
MixerPref9_DynamicSwitchToBOB: VMR9MixerPrefs = 1048576
MixerPref9_DynamicDecimateBy2: VMR9MixerPrefs = 2097152
MixerPref9_DynamicReserved: VMR9MixerPrefs = 12582912
MixerPref9_DynamicMask: VMR9MixerPrefs = 15728640
VMR9Mode = Int32
VMR9Mode_Windowed: VMR9Mode = 1
VMR9Mode_Windowless: VMR9Mode = 2
VMR9Mode_Renderless: VMR9Mode = 4
VMR9Mode_Mask: VMR9Mode = 7
class VMR9MonitorInfo(Structure):
    uDevID: UInt32
    rcMonitor: win32more.Foundation.RECT
    hMon: win32more.Graphics.Gdi.HMONITOR
    dwFlags: UInt32
    szDevice: Char * 32
    szDescription: Char * 512
    liDriverVersion: win32more.Foundation.LARGE_INTEGER
    dwVendorId: UInt32
    dwDeviceId: UInt32
    dwSubSysId: UInt32
    dwRevision: UInt32
class VMR9NormalizedRect(Structure):
    left: Single
    top: Single
    right: Single
    bottom: Single
VMR9PresentationFlags = Int32
VMR9Sample_SyncPoint: VMR9PresentationFlags = 1
VMR9Sample_Preroll: VMR9PresentationFlags = 2
VMR9Sample_Discontinuity: VMR9PresentationFlags = 4
VMR9Sample_TimeValid: VMR9PresentationFlags = 8
VMR9Sample_SrcDstRectsValid: VMR9PresentationFlags = 16
class VMR9PresentationInfo(Structure):
    dwFlags: UInt32
    lpSurf: win32more.Graphics.Direct3D9.IDirect3DSurface9_head
    rtStart: Int64
    rtEnd: Int64
    szAspectRatio: win32more.Foundation.SIZE
    rcSrc: win32more.Foundation.RECT
    rcDst: win32more.Foundation.RECT
    dwReserved1: UInt32
    dwReserved2: UInt32
class VMR9ProcAmpControl(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    Brightness: Single
    Contrast: Single
    Hue: Single
    Saturation: Single
VMR9ProcAmpControlFlags = Int32
ProcAmpControl9_Brightness: VMR9ProcAmpControlFlags = 1
ProcAmpControl9_Contrast: VMR9ProcAmpControlFlags = 2
ProcAmpControl9_Hue: VMR9ProcAmpControlFlags = 4
ProcAmpControl9_Saturation: VMR9ProcAmpControlFlags = 8
ProcAmpControl9_Mask: VMR9ProcAmpControlFlags = 15
class VMR9ProcAmpControlRange(Structure):
    dwSize: UInt32
    dwProperty: win32more.Media.DirectShow.VMR9ProcAmpControlFlags
    MinValue: Single
    MaxValue: Single
    DefaultValue: Single
    StepSize: Single
VMR9RenderPrefs = Int32
RenderPrefs9_DoNotRenderBorder: VMR9RenderPrefs = 1
RenderPrefs9_Mask: VMR9RenderPrefs = 1
VMR9SurfaceAllocationFlags = Int32
VMR9AllocFlag_3DRenderTarget: VMR9SurfaceAllocationFlags = 1
VMR9AllocFlag_DXVATarget: VMR9SurfaceAllocationFlags = 2
VMR9AllocFlag_TextureSurface: VMR9SurfaceAllocationFlags = 4
VMR9AllocFlag_OffscreenSurface: VMR9SurfaceAllocationFlags = 8
VMR9AllocFlag_RGBDynamicSwitch: VMR9SurfaceAllocationFlags = 16
VMR9AllocFlag_UsageReserved: VMR9SurfaceAllocationFlags = 224
VMR9AllocFlag_UsageMask: VMR9SurfaceAllocationFlags = 255
class VMR9VideoDesc(Structure):
    dwSize: UInt32
    dwSampleWidth: UInt32
    dwSampleHeight: UInt32
    SampleFormat: win32more.Media.DirectShow.VMR9_SampleFormat
    dwFourCC: UInt32
    InputSampleFreq: win32more.Media.DirectShow.VMR9Frequency
    OutputFrameFreq: win32more.Media.DirectShow.VMR9Frequency
class VMR9VideoStreamInfo(Structure):
    pddsVideoSurface: win32more.Graphics.Direct3D9.IDirect3DSurface9_head
    dwWidth: UInt32
    dwHeight: UInt32
    dwStrmID: UInt32
    fAlpha: Single
    rNormal: win32more.Media.DirectShow.VMR9NormalizedRect
    rtStart: Int64
    rtEnd: Int64
    SampleFormat: win32more.Media.DirectShow.VMR9_SampleFormat
VMR9_SampleFormat = Int32
VMR9_SampleReserved: VMR9_SampleFormat = 1
VMR9_SampleProgressiveFrame: VMR9_SampleFormat = 2
VMR9_SampleFieldInterleavedEvenFirst: VMR9_SampleFormat = 3
VMR9_SampleFieldInterleavedOddFirst: VMR9_SampleFormat = 4
VMR9_SampleFieldSingleEven: VMR9_SampleFormat = 5
VMR9_SampleFieldSingleOdd: VMR9_SampleFormat = 6
class VMRALLOCATIONINFO(Structure):
    dwFlags: UInt32
    lpHdr: POINTER(win32more.Graphics.Gdi.BITMAPINFOHEADER_head)
    lpPixFmt: POINTER(win32more.Graphics.DirectDraw.DDPIXELFORMAT_head)
    szAspectRatio: win32more.Foundation.SIZE
    dwMinBuffers: UInt32
    dwMaxBuffers: UInt32
    dwInterlaceFlags: UInt32
    szNativeSize: win32more.Foundation.SIZE
class VMRALPHABITMAP(Structure):
    dwFlags: UInt32
    hdc: win32more.Graphics.Gdi.HDC
    pDDS: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head
    rSrc: win32more.Foundation.RECT
    rDest: win32more.Media.DirectShow.NORMALIZEDRECT
    fAlpha: Single
    clrSrcKey: win32more.Foundation.COLORREF
class VMRDeinterlaceCaps(Structure):
    dwSize: UInt32
    dwNumPreviousOutputFrames: UInt32
    dwNumForwardRefSamples: UInt32
    dwNumBackwardRefSamples: UInt32
    DeinterlaceTechnology: win32more.Media.DirectShow.VMRDeinterlaceTech
VMRDeinterlacePrefs = Int32
DeinterlacePref_NextBest: VMRDeinterlacePrefs = 1
DeinterlacePref_BOB: VMRDeinterlacePrefs = 2
DeinterlacePref_Weave: VMRDeinterlacePrefs = 4
DeinterlacePref_Mask: VMRDeinterlacePrefs = 7
VMRDeinterlaceTech = Int32
DeinterlaceTech_Unknown: VMRDeinterlaceTech = 0
DeinterlaceTech_BOBLineReplicate: VMRDeinterlaceTech = 1
DeinterlaceTech_BOBVerticalStretch: VMRDeinterlaceTech = 2
DeinterlaceTech_MedianFiltering: VMRDeinterlaceTech = 4
DeinterlaceTech_EdgeFiltering: VMRDeinterlaceTech = 16
DeinterlaceTech_FieldAdaptive: VMRDeinterlaceTech = 32
DeinterlaceTech_PixelAdaptive: VMRDeinterlaceTech = 64
DeinterlaceTech_MotionVectorSteered: VMRDeinterlaceTech = 128
class VMRFrequency(Structure):
    dwNumerator: UInt32
    dwDenominator: UInt32
class VMRGUID(Structure):
    pGUID: POINTER(Guid)
    GUID: Guid
class VMRMONITORINFO(Structure):
    guid: win32more.Media.DirectShow.VMRGUID
    rcMonitor: win32more.Foundation.RECT
    hMon: win32more.Graphics.Gdi.HMONITOR
    dwFlags: UInt32
    szDevice: Char * 32
    szDescription: Char * 256
    liDriverVersion: win32more.Foundation.LARGE_INTEGER
    dwVendorId: UInt32
    dwDeviceId: UInt32
    dwSubSysId: UInt32
    dwRevision: UInt32
VMRMixerPrefs = Int32
MixerPref_NoDecimation: VMRMixerPrefs = 1
MixerPref_DecimateOutput: VMRMixerPrefs = 2
MixerPref_ARAdjustXorY: VMRMixerPrefs = 4
MixerPref_DecimationReserved: VMRMixerPrefs = 8
MixerPref_DecimateMask: VMRMixerPrefs = 15
MixerPref_BiLinearFiltering: VMRMixerPrefs = 16
MixerPref_PointFiltering: VMRMixerPrefs = 32
MixerPref_FilteringMask: VMRMixerPrefs = 240
MixerPref_RenderTargetRGB: VMRMixerPrefs = 256
MixerPref_RenderTargetYUV: VMRMixerPrefs = 4096
MixerPref_RenderTargetYUV420: VMRMixerPrefs = 512
MixerPref_RenderTargetYUV422: VMRMixerPrefs = 1024
MixerPref_RenderTargetYUV444: VMRMixerPrefs = 2048
MixerPref_RenderTargetReserved: VMRMixerPrefs = 57344
MixerPref_RenderTargetMask: VMRMixerPrefs = 65280
MixerPref_DynamicSwitchToBOB: VMRMixerPrefs = 65536
MixerPref_DynamicDecimateBy2: VMRMixerPrefs = 131072
MixerPref_DynamicReserved: VMRMixerPrefs = 786432
MixerPref_DynamicMask: VMRMixerPrefs = 983040
VMRMode = Int32
VMRMode_Windowed: VMRMode = 1
VMRMode_Windowless: VMRMode = 2
VMRMode_Renderless: VMRMode = 4
VMRMode_Mask: VMRMode = 7
class VMRPRESENTATIONINFO(Structure):
    dwFlags: UInt32
    lpSurf: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head
    rtStart: Int64
    rtEnd: Int64
    szAspectRatio: win32more.Foundation.SIZE
    rcSrc: win32more.Foundation.RECT
    rcDst: win32more.Foundation.RECT
    dwTypeSpecificFlags: UInt32
    dwInterlaceFlags: UInt32
VMRPresentationFlags = Int32
VMRSample_SyncPoint: VMRPresentationFlags = 1
VMRSample_Preroll: VMRPresentationFlags = 2
VMRSample_Discontinuity: VMRPresentationFlags = 4
VMRSample_TimeValid: VMRPresentationFlags = 8
VMRSample_SrcDstRectsValid: VMRPresentationFlags = 16
VMRRenderPrefs = Int32
RenderPrefs_RestrictToInitialMonitor: VMRRenderPrefs = 0
RenderPrefs_ForceOffscreen: VMRRenderPrefs = 1
RenderPrefs_ForceOverlays: VMRRenderPrefs = 2
RenderPrefs_AllowOverlays: VMRRenderPrefs = 0
RenderPrefs_AllowOffscreen: VMRRenderPrefs = 0
RenderPrefs_DoNotRenderColorKeyAndBorder: VMRRenderPrefs = 8
RenderPrefs_Reserved: VMRRenderPrefs = 16
RenderPrefs_PreferAGPMemWhenMixing: VMRRenderPrefs = 32
RenderPrefs_Mask: VMRRenderPrefs = 63
VMRSurfaceAllocationFlags = Int32
AMAP_PIXELFORMAT_VALID: VMRSurfaceAllocationFlags = 1
AMAP_3D_TARGET: VMRSurfaceAllocationFlags = 2
AMAP_ALLOW_SYSMEM: VMRSurfaceAllocationFlags = 4
AMAP_FORCE_SYSMEM: VMRSurfaceAllocationFlags = 8
AMAP_DIRECTED_FLIP: VMRSurfaceAllocationFlags = 16
AMAP_DXVA_TARGET: VMRSurfaceAllocationFlags = 32
class VMRVIDEOSTREAMINFO(Structure):
    pddsVideoSurface: win32more.Graphics.DirectDraw.IDirectDrawSurface7_head
    dwWidth: UInt32
    dwHeight: UInt32
    dwStrmID: UInt32
    fAlpha: Single
    ddClrKey: win32more.Graphics.DirectDraw.DDCOLORKEY
    rNormal: win32more.Media.DirectShow.NORMALIZEDRECT
class VMRVideoDesc(Structure):
    dwSize: UInt32
    dwSampleWidth: UInt32
    dwSampleHeight: UInt32
    SingleFieldPerSample: win32more.Foundation.BOOL
    dwFourCC: UInt32
    InputSampleFreq: win32more.Media.DirectShow.VMRFrequency
    OutputFrameFreq: win32more.Media.DirectShow.VMRFrequency
VMR_ASPECT_RATIO_MODE = Int32
VMR_ARMODE_NONE: VMR_ASPECT_RATIO_MODE = 0
VMR_ARMODE_LETTER_BOX: VMR_ASPECT_RATIO_MODE = 1
VfwCaptureDialogs = Int32
VfwCaptureDialog_Source: VfwCaptureDialogs = 1
VfwCaptureDialog_Format: VfwCaptureDialogs = 2
VfwCaptureDialog_Display: VfwCaptureDialogs = 4
VfwCompressDialogs = Int32
VfwCompressDialog_Config: VfwCompressDialogs = 1
VfwCompressDialog_About: VfwCompressDialogs = 2
VfwCompressDialog_QueryConfig: VfwCompressDialogs = 4
VfwCompressDialog_QueryAbout: VfwCompressDialogs = 8
VideoControlFlags = Int32
VideoControlFlag_FlipHorizontal: VideoControlFlags = 1
VideoControlFlag_FlipVertical: VideoControlFlags = 2
VideoControlFlag_ExternalTriggerEnable: VideoControlFlags = 4
VideoControlFlag_Trigger: VideoControlFlags = 8
VideoCopyProtectionType = Int32
VideoCopyProtectionType_VideoCopyProtectionMacrovisionBasic: VideoCopyProtectionType = 0
VideoCopyProtectionType_VideoCopyProtectionMacrovisionCBI: VideoCopyProtectionType = 1
VideoProcAmpFlags = Int32
VideoProcAmp_Flags_Auto: VideoProcAmpFlags = 1
VideoProcAmp_Flags_Manual: VideoProcAmpFlags = 2
VideoProcAmpProperty = Int32
VideoProcAmp_Brightness: VideoProcAmpProperty = 0
VideoProcAmp_Contrast: VideoProcAmpProperty = 1
VideoProcAmp_Hue: VideoProcAmpProperty = 2
VideoProcAmp_Saturation: VideoProcAmpProperty = 3
VideoProcAmp_Sharpness: VideoProcAmpProperty = 4
VideoProcAmp_Gamma: VideoProcAmpProperty = 5
VideoProcAmp_ColorEnable: VideoProcAmpProperty = 6
VideoProcAmp_WhiteBalance: VideoProcAmpProperty = 7
VideoProcAmp_BacklightCompensation: VideoProcAmpProperty = 8
VideoProcAmp_Gain: VideoProcAmpProperty = 9
class WMDRMProtectionInfo(Structure):
    wszKID: UInt16 * 25
    qwCounter: UInt64
    qwIndex: UInt64
    bOffset: Byte
    _pack_ = 1
XDSCodec = Guid('c4c4c4f3-0049-4e2b-98-fb-95-37-f6-ce-51-6d')
XDSToRat = Guid('c5c5c5f0-3abc-11d6-b2-5b-00-c0-4f-a0-c0-26')
_AMRESCTL_RESERVEFLAGS = Int32
AMRESCTL_RESERVEFLAGS_RESERVE: _AMRESCTL_RESERVEFLAGS = 0
AMRESCTL_RESERVEFLAGS_UNRESERVE: _AMRESCTL_RESERVEFLAGS = 1
_AMSTREAMSELECTENABLEFLAGS = Int32
AMSTREAMSELECTENABLE_ENABLE: _AMSTREAMSELECTENABLEFLAGS = 1
AMSTREAMSELECTENABLE_ENABLEALL: _AMSTREAMSELECTENABLEFLAGS = 2
_AMSTREAMSELECTINFOFLAGS = Int32
AMSTREAMSELECTINFO_ENABLED: _AMSTREAMSELECTINFOFLAGS = 1
AMSTREAMSELECTINFO_EXCLUSIVE: _AMSTREAMSELECTINFOFLAGS = 2
_AM_AUDIO_RENDERER_STAT_PARAM = Int32
AM_AUDREND_STAT_PARAM_BREAK_COUNT: _AM_AUDIO_RENDERER_STAT_PARAM = 1
AM_AUDREND_STAT_PARAM_SLAVE_MODE: _AM_AUDIO_RENDERER_STAT_PARAM = 2
AM_AUDREND_STAT_PARAM_SILENCE_DUR: _AM_AUDIO_RENDERER_STAT_PARAM = 3
AM_AUDREND_STAT_PARAM_LAST_BUFFER_DUR: _AM_AUDIO_RENDERER_STAT_PARAM = 4
AM_AUDREND_STAT_PARAM_DISCONTINUITIES: _AM_AUDIO_RENDERER_STAT_PARAM = 5
AM_AUDREND_STAT_PARAM_SLAVE_RATE: _AM_AUDIO_RENDERER_STAT_PARAM = 6
AM_AUDREND_STAT_PARAM_SLAVE_DROPWRITE_DUR: _AM_AUDIO_RENDERER_STAT_PARAM = 7
AM_AUDREND_STAT_PARAM_SLAVE_HIGHLOWERROR: _AM_AUDIO_RENDERER_STAT_PARAM = 8
AM_AUDREND_STAT_PARAM_SLAVE_LASTHIGHLOWERROR: _AM_AUDIO_RENDERER_STAT_PARAM = 9
AM_AUDREND_STAT_PARAM_SLAVE_ACCUMERROR: _AM_AUDIO_RENDERER_STAT_PARAM = 10
AM_AUDREND_STAT_PARAM_BUFFERFULLNESS: _AM_AUDIO_RENDERER_STAT_PARAM = 11
AM_AUDREND_STAT_PARAM_JITTER: _AM_AUDIO_RENDERER_STAT_PARAM = 12
_AM_FILTER_MISC_FLAGS = Int32
AM_FILTER_MISC_FLAGS_IS_RENDERER: _AM_FILTER_MISC_FLAGS = 1
AM_FILTER_MISC_FLAGS_IS_SOURCE: _AM_FILTER_MISC_FLAGS = 2
_AM_INTF_SEARCH_FLAGS = Int32
AM_INTF_SEARCH_INPUT_PIN: _AM_INTF_SEARCH_FLAGS = 1
AM_INTF_SEARCH_OUTPUT_PIN: _AM_INTF_SEARCH_FLAGS = 2
AM_INTF_SEARCH_FILTER: _AM_INTF_SEARCH_FLAGS = 4
_AM_OVERLAY_NOTIFY_FLAGS = Int32
AM_OVERLAY_NOTIFY_VISIBLE_CHANGE: _AM_OVERLAY_NOTIFY_FLAGS = 1
AM_OVERLAY_NOTIFY_SOURCE_CHANGE: _AM_OVERLAY_NOTIFY_FLAGS = 2
AM_OVERLAY_NOTIFY_DEST_CHANGE: _AM_OVERLAY_NOTIFY_FLAGS = 4
_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS = Int32
AM_PIN_FLOW_CONTROL_BLOCK: _AM_PIN_FLOW_CONTROL_BLOCK_FLAGS = 1
_AM_PUSHSOURCE_FLAGS = Int32
AM_PUSHSOURCECAPS_INTERNAL_RM: _AM_PUSHSOURCE_FLAGS = 1
AM_PUSHSOURCECAPS_NOT_LIVE: _AM_PUSHSOURCE_FLAGS = 2
AM_PUSHSOURCECAPS_PRIVATE_CLOCK: _AM_PUSHSOURCE_FLAGS = 4
AM_PUSHSOURCEREQS_USE_STREAM_CLOCK: _AM_PUSHSOURCE_FLAGS = 65536
AM_PUSHSOURCEREQS_USE_CLOCK_CHAIN: _AM_PUSHSOURCE_FLAGS = 131072
_AM_RENSDEREXFLAGS = Int32
AM_RENDEREX_RENDERTOEXISTINGRENDERERS: _AM_RENSDEREXFLAGS = 1
_DVDECODERRESOLUTION = Int32
DVDECODERRESOLUTION_720x480: _DVDECODERRESOLUTION = 1000
DVDECODERRESOLUTION_360x240: _DVDECODERRESOLUTION = 1001
DVDECODERRESOLUTION_180x120: _DVDECODERRESOLUTION = 1002
DVDECODERRESOLUTION_88x60: _DVDECODERRESOLUTION = 1003
_DVENCODERFORMAT = Int32
DVENCODERFORMAT_DVSD: _DVENCODERFORMAT = 2007
DVENCODERFORMAT_DVHD: _DVENCODERFORMAT = 2008
DVENCODERFORMAT_DVSL: _DVENCODERFORMAT = 2009
_DVENCODERRESOLUTION = Int32
DVENCODERRESOLUTION_720x480: _DVENCODERRESOLUTION = 2012
DVENCODERRESOLUTION_360x240: _DVENCODERRESOLUTION = 2013
DVENCODERRESOLUTION_180x120: _DVENCODERRESOLUTION = 2014
DVENCODERRESOLUTION_88x60: _DVENCODERRESOLUTION = 2015
_DVENCODERVIDEOFORMAT = Int32
DVENCODERVIDEOFORMAT_NTSC: _DVENCODERVIDEOFORMAT = 2000
DVENCODERVIDEOFORMAT_PAL: _DVENCODERVIDEOFORMAT = 2001
_DVRESOLUTION = Int32
DVRESOLUTION_FULL: _DVRESOLUTION = 1000
DVRESOLUTION_HALF: _DVRESOLUTION = 1001
DVRESOLUTION_QUARTER: _DVRESOLUTION = 1002
DVRESOLUTION_DC: _DVRESOLUTION = 1003
class _IMSVidCtlEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b0edf164-910a-11d2-b6-32-00-c0-4f-79-49-8e')
_REM_FILTER_FLAGS = Int32
REMFILTERF_LEAVECONNECTED: _REM_FILTER_FLAGS = 1
make_head(_module, 'ALLOCATOR_PROPERTIES')
make_head(_module, 'AMCOPPCommand')
make_head(_module, 'AMCOPPSignature')
make_head(_module, 'AMCOPPStatusInput')
make_head(_module, 'AMCOPPStatusOutput')
make_head(_module, 'AMGETERRORTEXTPROCA')
make_head(_module, 'AMGETERRORTEXTPROCW')
make_head(_module, 'AMVABUFFERINFO')
make_head(_module, 'AMVABeginFrameInfo')
make_head(_module, 'AMVACompBufferInfo')
make_head(_module, 'AMVAEndFrameInfo')
make_head(_module, 'AMVAInternalMemInfo')
make_head(_module, 'AMVAUncompBufferInfo')
make_head(_module, 'AMVAUncompDataInfo')
make_head(_module, 'AMVPDATAINFO')
make_head(_module, 'AMVPDIMINFO')
make_head(_module, 'AMVPSIZE')
make_head(_module, 'AM_AC3_ALTERNATE_AUDIO')
make_head(_module, 'AM_AC3_BIT_STREAM_MODE')
make_head(_module, 'AM_AC3_DIALOGUE_LEVEL')
make_head(_module, 'AM_AC3_DOWNMIX')
make_head(_module, 'AM_AC3_ERROR_CONCEALMENT')
make_head(_module, 'AM_AC3_ROOM_TYPE')
make_head(_module, 'AM_COLCON')
make_head(_module, 'AM_COPY_MACROVISION')
make_head(_module, 'AM_DVDCOPY_BUSKEY')
make_head(_module, 'AM_DVDCOPY_CHLGKEY')
make_head(_module, 'AM_DVDCOPY_DISCKEY')
make_head(_module, 'AM_DVDCOPY_SET_COPY_STATE')
make_head(_module, 'AM_DVDCOPY_TITLEKEY')
make_head(_module, 'AM_DVD_ChangeRate')
make_head(_module, 'AM_DVD_RENDERSTATUS')
make_head(_module, 'AM_DVD_YUV')
make_head(_module, 'AM_DvdKaraokeData')
make_head(_module, 'AM_ExactRateChange')
make_head(_module, 'AM_FRAMESTEP_STEP')
make_head(_module, 'AM_MPEGSTREAMTYPE')
make_head(_module, 'AM_MPEGSYSTEMTYPE')
make_head(_module, 'AM_PROPERTY_SPHLI')
make_head(_module, 'AM_PROPERTY_SPPAL')
make_head(_module, 'AM_QueryRate')
make_head(_module, 'AM_SAMPLE2_PROPERTIES')
make_head(_module, 'AM_STREAM_INFO')
make_head(_module, 'AM_SimpleRateChange')
make_head(_module, 'AM_WST_PAGE')
make_head(_module, 'ANALOGVIDEOINFO')
make_head(_module, 'ATSC_FILTER_OPTIONS')
make_head(_module, 'AUDIO_STREAM_CONFIG_CAPS')
make_head(_module, 'AVIEXTHEADER')
make_head(_module, 'AVIFIELDINDEX')
make_head(_module, 'AVIINDEXENTRY')
make_head(_module, 'AVIMAINHEADER')
make_head(_module, 'AVIMETAINDEX')
make_head(_module, 'AVIOLDINDEX')
make_head(_module, 'AVIPALCHANGE')
make_head(_module, 'AVISTDINDEX')
make_head(_module, 'AVISTDINDEX_ENTRY')
make_head(_module, 'AVISTREAMHEADER')
make_head(_module, 'AVISUPERINDEX')
make_head(_module, 'AVIStreamHeader')
make_head(_module, 'AVITCDLINDEX')
make_head(_module, 'AVITCDLINDEX_ENTRY')
make_head(_module, 'AVITIMECODEINDEX')
make_head(_module, 'AVITIMEDINDEX')
make_head(_module, 'AVITIMEDINDEX_ENTRY')
make_head(_module, 'BDANODE_DESCRIPTOR')
make_head(_module, 'BDA_BUFFER')
make_head(_module, 'BDA_CAS_CHECK_ENTITLEMENTTOKEN')
make_head(_module, 'BDA_CAS_CLOSEMMIDATA')
make_head(_module, 'BDA_CAS_CLOSE_MMIDIALOG')
make_head(_module, 'BDA_CAS_OPENMMIDATA')
make_head(_module, 'BDA_CAS_REQUESTTUNERDATA')
make_head(_module, 'BDA_CA_MODULE_UI')
make_head(_module, 'BDA_DEBUG_DATA')
make_head(_module, 'BDA_DISEQC_RESPONSE')
make_head(_module, 'BDA_DISEQC_SEND')
make_head(_module, 'BDA_DRM_DRMSTATUS')
make_head(_module, 'BDA_DVBT2_L1_SIGNALLING_DATA')
make_head(_module, 'BDA_ETHERNET_ADDRESS')
make_head(_module, 'BDA_ETHERNET_ADDRESS_LIST')
make_head(_module, 'BDA_EVENT_DATA')
make_head(_module, 'BDA_GDDS_DATA')
make_head(_module, 'BDA_GDDS_DATATYPE')
make_head(_module, 'BDA_IPv4_ADDRESS')
make_head(_module, 'BDA_IPv4_ADDRESS_LIST')
make_head(_module, 'BDA_IPv6_ADDRESS')
make_head(_module, 'BDA_IPv6_ADDRESS_LIST')
make_head(_module, 'BDA_ISDBCAS_EMG_REQ')
make_head(_module, 'BDA_ISDBCAS_REQUESTHEADER')
make_head(_module, 'BDA_ISDBCAS_RESPONSEDATA')
make_head(_module, 'BDA_MUX_PIDLISTITEM')
make_head(_module, 'BDA_PID_MAP')
make_head(_module, 'BDA_PID_UNMAP')
make_head(_module, 'BDA_PROGRAM_PID_LIST')
make_head(_module, 'BDA_RATING_PINRESET')
make_head(_module, 'BDA_SCAN_CAPABILTIES')
make_head(_module, 'BDA_SCAN_START')
make_head(_module, 'BDA_SCAN_STATE')
make_head(_module, 'BDA_SIGNAL_TIMEOUTS')
make_head(_module, 'BDA_STRING')
make_head(_module, 'BDA_TABLE_SECTION')
make_head(_module, 'BDA_TEMPLATE_CONNECTION')
make_head(_module, 'BDA_TEMPLATE_PIN_JOINT')
make_head(_module, 'BDA_TRANSPORT_INFO')
make_head(_module, 'BDA_TS_SELECTORINFO')
make_head(_module, 'BDA_TS_SELECTORINFO_ISDBS_EXT')
make_head(_module, 'BDA_TUNER_DIAGNOSTICS')
make_head(_module, 'BDA_TUNER_TUNERSTATE')
make_head(_module, 'BDA_USERACTIVITY_INTERVAL')
make_head(_module, 'BDA_WMDRMTUNER_PIDPROTECTION')
make_head(_module, 'BDA_WMDRMTUNER_PURCHASEENTITLEMENT')
make_head(_module, 'BDA_WMDRM_KEYINFOLIST')
make_head(_module, 'BDA_WMDRM_RENEWLICENSE')
make_head(_module, 'BDA_WMDRM_STATUS')
make_head(_module, 'BadSampleInfo')
make_head(_module, 'CAPTURE_STREAMTIME')
make_head(_module, 'COLORKEY')
make_head(_module, 'ChannelChangeInfo')
make_head(_module, 'ChannelInfo')
make_head(_module, 'ChannelTypeInfo')
make_head(_module, 'DSHOW_STREAM_DESC')
make_head(_module, 'DSMCC_ELEMENT')
make_head(_module, 'DSMCC_FILTER_OPTIONS')
make_head(_module, 'DSMCC_SECTION')
make_head(_module, 'DVBScramblingControlSpanningEvent')
make_head(_module, 'DVB_EIT_FILTER_OPTIONS')
make_head(_module, 'DVD_ATR')
make_head(_module, 'DVD_AudioAttributes')
make_head(_module, 'DVD_DECODER_CAPS')
make_head(_module, 'DVD_HMSF_TIMECODE')
make_head(_module, 'DVD_KaraokeAttributes')
make_head(_module, 'DVD_MUA_Coeff')
make_head(_module, 'DVD_MUA_MixingInfo')
make_head(_module, 'DVD_MenuAttributes')
make_head(_module, 'DVD_MultichannelAudioAttributes')
make_head(_module, 'DVD_PLAYBACK_LOCATION')
make_head(_module, 'DVD_PLAYBACK_LOCATION2')
make_head(_module, 'DVD_REGION')
make_head(_module, 'DVD_SubpictureAttributes')
make_head(_module, 'DVD_TIMECODE')
make_head(_module, 'DVD_TitleAttributes')
make_head(_module, 'DVD_VideoAttributes')
make_head(_module, 'DVINFO')
make_head(_module, 'DVR_STREAM_DESC')
make_head(_module, 'DXVA2SW_CALLBACKS')
make_head(_module, 'DXVA2TraceVideoProcessBltData')
make_head(_module, 'DXVA2Trace_DecodeDevBeginFrameData')
make_head(_module, 'DXVA2Trace_DecodeDevCreatedData')
make_head(_module, 'DXVA2Trace_DecodeDevGetBufferData')
make_head(_module, 'DXVA2Trace_DecodeDeviceData')
make_head(_module, 'DXVA2Trace_VideoProcessDevCreatedData')
make_head(_module, 'DXVA2Trace_VideoProcessDeviceData')
make_head(_module, 'DXVA2_VIDEOPROCESSBLT')
make_head(_module, 'DXVA2_VIDEOSAMPLE')
make_head(_module, 'DXVA_COPPSetProtectionLevelCmdData')
make_head(_module, 'DXVA_COPPSetSignalingCmdData')
make_head(_module, 'DXVA_COPPStatusData')
make_head(_module, 'DXVA_COPPStatusDisplayData')
make_head(_module, 'DXVA_COPPStatusHDCPKeyData')
make_head(_module, 'DXVA_COPPStatusSignalingCmdData')
make_head(_module, 'DualMonoInfo')
make_head(_module, 'DvbParentalRatingDescriptor')
make_head(_module, 'DvbParentalRatingParam')
make_head(_module, 'EALocationCodeType')
make_head(_module, 'FILTER_INFO')
make_head(_module, 'HEAACWAVEFORMAT')
make_head(_module, 'HEAACWAVEINFO')
make_head(_module, 'IAMAnalogVideoDecoder')
make_head(_module, 'IAMAnalogVideoEncoder')
make_head(_module, 'IAMAsyncReaderTimestampScaling')
make_head(_module, 'IAMAudioInputMixer')
make_head(_module, 'IAMAudioRendererStats')
make_head(_module, 'IAMBufferNegotiation')
make_head(_module, 'IAMCameraControl')
make_head(_module, 'IAMCertifiedOutputProtection')
make_head(_module, 'IAMChannelInfo')
make_head(_module, 'IAMClockAdjust')
make_head(_module, 'IAMClockSlave')
make_head(_module, 'IAMCollection')
make_head(_module, 'IAMCopyCaptureFileProgress')
make_head(_module, 'IAMCrossbar')
make_head(_module, 'IAMDecoderCaps')
make_head(_module, 'IAMDevMemoryAllocator')
make_head(_module, 'IAMDevMemoryControl')
make_head(_module, 'IAMDeviceRemoval')
make_head(_module, 'IAMDirectSound')
make_head(_module, 'IAMDroppedFrames')
make_head(_module, 'IAMExtDevice')
make_head(_module, 'IAMExtTransport')
make_head(_module, 'IAMExtendedErrorInfo')
make_head(_module, 'IAMExtendedSeeking')
make_head(_module, 'IAMFilterGraphCallback')
make_head(_module, 'IAMFilterMiscFlags')
make_head(_module, 'IAMGraphBuilderCallback')
make_head(_module, 'IAMGraphStreams')
make_head(_module, 'IAMLatency')
make_head(_module, 'IAMLine21Decoder')
make_head(_module, 'IAMMediaContent')
make_head(_module, 'IAMMediaContent2')
make_head(_module, 'IAMMediaStream')
make_head(_module, 'IAMMediaTypeSample')
make_head(_module, 'IAMMediaTypeStream')
make_head(_module, 'IAMMultiMediaStream')
make_head(_module, 'IAMNetShowConfig')
make_head(_module, 'IAMNetShowExProps')
make_head(_module, 'IAMNetShowPreroll')
make_head(_module, 'IAMNetworkStatus')
make_head(_module, 'IAMOpenProgress')
make_head(_module, 'IAMOverlayFX')
make_head(_module, 'IAMParse')
make_head(_module, 'IAMPhysicalPinInfo')
make_head(_module, 'IAMPlayList')
make_head(_module, 'IAMPlayListItem')
make_head(_module, 'IAMPluginControl')
make_head(_module, 'IAMPushSource')
make_head(_module, 'IAMRebuild')
make_head(_module, 'IAMResourceControl')
make_head(_module, 'IAMStats')
make_head(_module, 'IAMStreamConfig')
make_head(_module, 'IAMStreamControl')
make_head(_module, 'IAMStreamSelect')
make_head(_module, 'IAMTVAudio')
make_head(_module, 'IAMTVAudioNotification')
make_head(_module, 'IAMTVTuner')
make_head(_module, 'IAMTimecodeDisplay')
make_head(_module, 'IAMTimecodeGenerator')
make_head(_module, 'IAMTimecodeReader')
make_head(_module, 'IAMTuner')
make_head(_module, 'IAMTunerNotification')
make_head(_module, 'IAMVfwCaptureDialogs')
make_head(_module, 'IAMVfwCompressDialogs')
make_head(_module, 'IAMVideoAccelerator')
make_head(_module, 'IAMVideoAcceleratorNotify')
make_head(_module, 'IAMVideoCompression')
make_head(_module, 'IAMVideoControl')
make_head(_module, 'IAMVideoDecimationProperties')
make_head(_module, 'IAMVideoProcAmp')
make_head(_module, 'IAMWMBufferPass')
make_head(_module, 'IAMWMBufferPassCallback')
make_head(_module, 'IAMWstDecoder')
make_head(_module, 'IAMovieSetup')
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
make_head(_module, 'IAsyncReader')
make_head(_module, 'IAtscContentAdvisoryDescriptor')
make_head(_module, 'IAtscPsipParser')
make_head(_module, 'IAttributeGet')
make_head(_module, 'IAttributeSet')
make_head(_module, 'IAudioData')
make_head(_module, 'IAudioMediaStream')
make_head(_module, 'IAudioStreamSample')
make_head(_module, 'IAuxInTuningSpace')
make_head(_module, 'IAuxInTuningSpace2')
make_head(_module, 'IBDAComparable')
make_head(_module, 'IBDACreateTuneRequestEx')
make_head(_module, 'IBDA_AUX')
make_head(_module, 'IBDA_AutoDemodulate')
make_head(_module, 'IBDA_AutoDemodulateEx')
make_head(_module, 'IBDA_ConditionalAccess')
make_head(_module, 'IBDA_ConditionalAccessEx')
make_head(_module, 'IBDA_DRIDRMService')
make_head(_module, 'IBDA_DRIWMDRMSession')
make_head(_module, 'IBDA_DRM')
make_head(_module, 'IBDA_DRMService')
make_head(_module, 'IBDA_DeviceControl')
make_head(_module, 'IBDA_DiagnosticProperties')
make_head(_module, 'IBDA_DigitalDemodulator')
make_head(_module, 'IBDA_DigitalDemodulator2')
make_head(_module, 'IBDA_DigitalDemodulator3')
make_head(_module, 'IBDA_DiseqCommand')
make_head(_module, 'IBDA_EasMessage')
make_head(_module, 'IBDA_Encoder')
make_head(_module, 'IBDA_EthernetFilter')
make_head(_module, 'IBDA_EventingService')
make_head(_module, 'IBDA_FDC')
make_head(_module, 'IBDA_FrequencyFilter')
make_head(_module, 'IBDA_GuideDataDeliveryService')
make_head(_module, 'IBDA_IPSinkControl')
make_head(_module, 'IBDA_IPSinkInfo')
make_head(_module, 'IBDA_IPV4Filter')
make_head(_module, 'IBDA_IPV6Filter')
make_head(_module, 'IBDA_ISDBConditionalAccess')
make_head(_module, 'IBDA_LNBInfo')
make_head(_module, 'IBDA_MUX')
make_head(_module, 'IBDA_NameValueService')
make_head(_module, 'IBDA_NetworkProvider')
make_head(_module, 'IBDA_NullTransform')
make_head(_module, 'IBDA_PinControl')
make_head(_module, 'IBDA_SignalProperties')
make_head(_module, 'IBDA_SignalStatistics')
make_head(_module, 'IBDA_TIF_REGISTRATION')
make_head(_module, 'IBDA_Topology')
make_head(_module, 'IBDA_TransportStreamInfo')
make_head(_module, 'IBDA_TransportStreamSelector')
make_head(_module, 'IBDA_UserActivityService')
make_head(_module, 'IBDA_VoidTransform')
make_head(_module, 'IBDA_WMDRMSession')
make_head(_module, 'IBDA_WMDRMTuner')
make_head(_module, 'IBPCSatelliteTuner')
make_head(_module, 'IBaseFilter')
make_head(_module, 'IBaseVideoMixer')
make_head(_module, 'IBasicAudio')
make_head(_module, 'IBasicVideo')
make_head(_module, 'IBasicVideo2')
make_head(_module, 'IBroadcastEvent')
make_head(_module, 'IBroadcastEventEx')
make_head(_module, 'IBufferingTime')
make_head(_module, 'ICAT')
make_head(_module, 'ICCSubStreamFiltering')
make_head(_module, 'ICameraControl')
make_head(_module, 'ICaptionServiceDescriptor')
make_head(_module, 'ICaptureGraphBuilder')
make_head(_module, 'ICaptureGraphBuilder2')
make_head(_module, 'IChannelIDTuneRequest')
make_head(_module, 'IChannelTuneRequest')
make_head(_module, 'IComponent')
make_head(_module, 'IComponentType')
make_head(_module, 'IComponentTypes')
make_head(_module, 'IComponents')
make_head(_module, 'IComponentsOld')
make_head(_module, 'IConfigAsfWriter')
make_head(_module, 'IConfigAsfWriter2')
make_head(_module, 'IConfigAviMux')
make_head(_module, 'IConfigInterleaving')
make_head(_module, 'ICreateDevEnum')
make_head(_module, 'ICreatePropBagOnRegKey')
make_head(_module, 'IDDrawExclModeVideo')
make_head(_module, 'IDDrawExclModeVideoCallback')
make_head(_module, 'IDMOWrapperFilter')
make_head(_module, 'IDShowPlugin')
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
make_head(_module, 'IDVEnc')
make_head(_module, 'IDVRGB219')
make_head(_module, 'IDVSplitter')
make_head(_module, 'IDecimateVideoImage')
make_head(_module, 'IDeferredCommand')
make_head(_module, 'IDigitalCableLocator')
make_head(_module, 'IDigitalCableTuneRequest')
make_head(_module, 'IDigitalCableTuningSpace')
make_head(_module, 'IDigitalLocator')
make_head(_module, 'IDirectDrawMediaSample')
make_head(_module, 'IDirectDrawMediaSampleAllocator')
make_head(_module, 'IDirectDrawMediaStream')
make_head(_module, 'IDirectDrawStreamSample')
make_head(_module, 'IDirectDrawVideo')
make_head(_module, 'IDistributorNotify')
make_head(_module, 'IDrawVideoImage')
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
make_head(_module, 'IDvdCmd')
make_head(_module, 'IDvdControl')
make_head(_module, 'IDvdControl2')
make_head(_module, 'IDvdGraphBuilder')
make_head(_module, 'IDvdInfo')
make_head(_module, 'IDvdInfo2')
make_head(_module, 'IDvdState')
make_head(_module, 'IESCloseMmiEvent')
make_head(_module, 'IESEvent')
make_head(_module, 'IESEventFactory')
make_head(_module, 'IESEventService')
make_head(_module, 'IESEventServiceConfiguration')
make_head(_module, 'IESEvents')
make_head(_module, 'IESFileExpiryDateEvent')
make_head(_module, 'IESIsdbCasResponseEvent')
make_head(_module, 'IESLicenseRenewalResultEvent')
make_head(_module, 'IESOpenMmiEvent')
make_head(_module, 'IESRequestTunerEvent')
make_head(_module, 'IESValueUpdatedEvent')
make_head(_module, 'IETFilter')
make_head(_module, 'IETFilterConfig')
make_head(_module, 'IETFilterEvents')
make_head(_module, 'IEncoderAPI')
make_head(_module, 'IEnumComponentTypes')
make_head(_module, 'IEnumComponents')
make_head(_module, 'IEnumFilters')
make_head(_module, 'IEnumGuideDataProperties')
make_head(_module, 'IEnumMSVidGraphSegment')
make_head(_module, 'IEnumMediaTypes')
make_head(_module, 'IEnumPIDMap')
make_head(_module, 'IEnumPins')
make_head(_module, 'IEnumRegFilters')
make_head(_module, 'IEnumStreamBufferRecordingAttrib')
make_head(_module, 'IEnumStreamIdMap')
make_head(_module, 'IEnumTuneRequests')
make_head(_module, 'IEnumTuningSpaces')
make_head(_module, 'IEvalRat')
make_head(_module, 'IFileSinkFilter')
make_head(_module, 'IFileSinkFilter2')
make_head(_module, 'IFileSourceFilter')
make_head(_module, 'IFilterChain')
make_head(_module, 'IFilterGraph')
make_head(_module, 'IFilterGraph2')
make_head(_module, 'IFilterGraph3')
make_head(_module, 'IFilterInfo')
make_head(_module, 'IFilterMapper')
make_head(_module, 'IFilterMapper2')
make_head(_module, 'IFilterMapper3')
make_head(_module, 'IFrequencyMap')
make_head(_module, 'IFullScreenVideo')
make_head(_module, 'IFullScreenVideoEx')
make_head(_module, 'IGenericDescriptor')
make_head(_module, 'IGenericDescriptor2')
make_head(_module, 'IGetCapabilitiesKey')
make_head(_module, 'IGpnvsCommonBase')
make_head(_module, 'IGraphBuilder')
make_head(_module, 'IGraphConfig')
make_head(_module, 'IGraphConfigCallback')
make_head(_module, 'IGraphVersion')
make_head(_module, 'IGuideData')
make_head(_module, 'IGuideDataEvent')
make_head(_module, 'IGuideDataLoader')
make_head(_module, 'IGuideDataProperty')
make_head(_module, 'IIPDVDec')
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
make_head(_module, 'IKsNodeControl')
make_head(_module, 'IKsTopologyInfo')
make_head(_module, 'ILanguageComponentType')
make_head(_module, 'ILocator')
make_head(_module, 'IMPEG2Component')
make_head(_module, 'IMPEG2ComponentType')
make_head(_module, 'IMPEG2PIDMap')
make_head(_module, 'IMPEG2StreamIdMap')
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
make_head(_module, 'IMediaControl')
make_head(_module, 'IMediaEvent')
make_head(_module, 'IMediaEventEx')
make_head(_module, 'IMediaEventSink')
make_head(_module, 'IMediaFilter')
make_head(_module, 'IMediaParamInfo')
make_head(_module, 'IMediaParams')
make_head(_module, 'IMediaPosition')
make_head(_module, 'IMediaPropertyBag')
make_head(_module, 'IMediaSample')
make_head(_module, 'IMediaSample2')
make_head(_module, 'IMediaSample2Config')
make_head(_module, 'IMediaSeeking')
make_head(_module, 'IMediaStream')
make_head(_module, 'IMediaStreamFilter')
make_head(_module, 'IMediaTypeInfo')
make_head(_module, 'IMemAllocator')
make_head(_module, 'IMemAllocatorCallbackTemp')
make_head(_module, 'IMemAllocatorNotifyCallbackTemp')
make_head(_module, 'IMemInputPin')
make_head(_module, 'IMemoryData')
make_head(_module, 'IMixerOCX')
make_head(_module, 'IMixerOCXNotify')
make_head(_module, 'IMixerPinConfig')
make_head(_module, 'IMixerPinConfig2')
make_head(_module, 'IMpeg2Data')
make_head(_module, 'IMpeg2Demultiplexer')
make_head(_module, 'IMpeg2Stream')
make_head(_module, 'IMpeg2TableFilter')
make_head(_module, 'IMpegAudioDecoder')
make_head(_module, 'IMultiMediaStream')
make_head(_module, 'IOverlay')
make_head(_module, 'IOverlayNotify')
make_head(_module, 'IOverlayNotify2')
make_head(_module, 'IPAT')
make_head(_module, 'IPBDAAttributesDescriptor')
make_head(_module, 'IPBDAEntitlementDescriptor')
make_head(_module, 'IPBDASiParser')
make_head(_module, 'IPBDA_EIT')
make_head(_module, 'IPBDA_Services')
make_head(_module, 'IPMT')
make_head(_module, 'IPSITables')
make_head(_module, 'IPTFilterLicenseRenewal')
make_head(_module, 'IPersistMediaPropertyBag')
make_head(_module, 'IPersistTuneXml')
make_head(_module, 'IPersistTuneXmlUtility')
make_head(_module, 'IPersistTuneXmlUtility2')
make_head(_module, 'IPin')
make_head(_module, 'IPinConnection')
make_head(_module, 'IPinFlowControl')
make_head(_module, 'IPinInfo')
make_head(_module, 'IQualProp')
make_head(_module, 'IQualityControl')
make_head(_module, 'IQueueCommand')
make_head(_module, 'IRegFilterInfo')
make_head(_module, 'IRegisterServiceProvider')
make_head(_module, 'IRegisterTuner')
make_head(_module, 'IResourceConsumer')
make_head(_module, 'IResourceManager')
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
make_head(_module, 'ISeekingPassThru')
make_head(_module, 'ISelector')
make_head(_module, 'IServiceLocationDescriptor')
make_head(_module, 'ISpecifyParticularPages')
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
make_head(_module, 'IStreamBuilder')
make_head(_module, 'IStreamSample')
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
make_head(_module, 'IVMRAspectRatioControl')
make_head(_module, 'IVMRAspectRatioControl9')
make_head(_module, 'IVMRDeinterlaceControl')
make_head(_module, 'IVMRDeinterlaceControl9')
make_head(_module, 'IVMRFilterConfig')
make_head(_module, 'IVMRFilterConfig9')
make_head(_module, 'IVMRImageCompositor')
make_head(_module, 'IVMRImageCompositor9')
make_head(_module, 'IVMRImagePresenter')
make_head(_module, 'IVMRImagePresenter9')
make_head(_module, 'IVMRImagePresenterConfig')
make_head(_module, 'IVMRImagePresenterConfig9')
make_head(_module, 'IVMRImagePresenterExclModeConfig')
make_head(_module, 'IVMRMixerBitmap')
make_head(_module, 'IVMRMixerBitmap9')
make_head(_module, 'IVMRMixerControl')
make_head(_module, 'IVMRMixerControl9')
make_head(_module, 'IVMRMonitorConfig')
make_head(_module, 'IVMRMonitorConfig9')
make_head(_module, 'IVMRSurface')
make_head(_module, 'IVMRSurface9')
make_head(_module, 'IVMRSurfaceAllocator')
make_head(_module, 'IVMRSurfaceAllocator9')
make_head(_module, 'IVMRSurfaceAllocatorEx9')
make_head(_module, 'IVMRSurfaceAllocatorNotify')
make_head(_module, 'IVMRSurfaceAllocatorNotify9')
make_head(_module, 'IVMRVideoStreamControl')
make_head(_module, 'IVMRVideoStreamControl9')
make_head(_module, 'IVMRWindowlessControl')
make_head(_module, 'IVMRWindowlessControl9')
make_head(_module, 'IVPBaseConfig')
make_head(_module, 'IVPBaseNotify')
make_head(_module, 'IVPConfig')
make_head(_module, 'IVPManager')
make_head(_module, 'IVPNotify')
make_head(_module, 'IVPNotify2')
make_head(_module, 'IVPVBIConfig')
make_head(_module, 'IVPVBINotify')
make_head(_module, 'IVideoEncoder')
make_head(_module, 'IVideoFrameStep')
make_head(_module, 'IVideoProcAmp')
make_head(_module, 'IVideoWindow')
make_head(_module, 'IWMCodecAMVideoAccelerator')
make_head(_module, 'IWMCodecVideoAccelerator')
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
make_head(_module, 'KS_BDA_FRAME_INFO')
make_head(_module, 'KS_DATARANGE_BDA_ANTENNA')
make_head(_module, 'KS_DATARANGE_BDA_TRANSPORT')
make_head(_module, 'LONG_SECTION')
make_head(_module, 'LanguageInfo')
make_head(_module, 'MPEG1WAVEFORMAT')
make_head(_module, 'MPEG2_FILTER')
make_head(_module, 'MPEG2_FILTER2')
make_head(_module, 'MPEG2_TRANSPORT_STRIDE')
make_head(_module, 'MPEGLAYER3WAVEFORMAT')
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
make_head(_module, 'MP_ENVELOPE_SEGMENT')
make_head(_module, 'MP_PARAMINFO')
make_head(_module, 'MainAVIHeader')
make_head(_module, 'Mpeg2TableSampleHdr')
make_head(_module, 'NORMALIZEDRECT')
make_head(_module, 'PBDAParentalControl')
make_head(_module, 'PBDA_TAG_ATTRIBUTE')
make_head(_module, 'PDXVA2SW_CREATEVIDEOPROCESSDEVICE')
make_head(_module, 'PDXVA2SW_DESTROYVIDEOPROCESSDEVICE')
make_head(_module, 'PDXVA2SW_GETFILTERPROPERTYRANGE')
make_head(_module, 'PDXVA2SW_GETPROCAMPRANGE')
make_head(_module, 'PDXVA2SW_GETVIDEOPROCESSORCAPS')
make_head(_module, 'PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETCOUNT')
make_head(_module, 'PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETS')
make_head(_module, 'PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATCOUNT')
make_head(_module, 'PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATS')
make_head(_module, 'PDXVA2SW_VIDEOPROCESSBEGINFRAME')
make_head(_module, 'PDXVA2SW_VIDEOPROCESSBLT')
make_head(_module, 'PDXVA2SW_VIDEOPROCESSENDFRAME')
make_head(_module, 'PDXVA2SW_VIDEOPROCESSSETRENDERTARGET')
make_head(_module, 'PIC_SEQ_SAMPLE')
make_head(_module, 'PIDListSpanningEvent')
make_head(_module, 'PID_BITS')
make_head(_module, 'PID_BITS_MIDL')
make_head(_module, 'PID_MAP')
make_head(_module, 'PIN_INFO')
make_head(_module, 'ProgramElement')
make_head(_module, 'Quality')
make_head(_module, 'RATING_ATTRIBUTE')
make_head(_module, 'RATING_INFO')
make_head(_module, 'RATING_SYSTEM')
make_head(_module, 'REGFILTER')
make_head(_module, 'REGFILTER2')
make_head(_module, 'REGFILTERPINS')
make_head(_module, 'REGFILTERPINS2')
make_head(_module, 'REGPINMEDIUM')
make_head(_module, 'REGPINTYPES')
make_head(_module, 'RIFFCHUNK')
make_head(_module, 'RIFFLIST')
make_head(_module, 'SAMPLE_LIVE_STREAM_TIME')
make_head(_module, 'SAMPLE_SEQ_OFFSET')
make_head(_module, 'SBE2_STREAM_DESC')
make_head(_module, 'SBE_PIN_DATA')
make_head(_module, 'SECTION')
make_head(_module, 'STREAMBUFFER_ATTRIBUTE')
make_head(_module, 'STREAM_ID_MAP')
make_head(_module, 'SmartCardApplication')
make_head(_module, 'SpanningEventDescriptor')
make_head(_module, 'SpanningEventEmmMessage')
make_head(_module, 'TID_EXTENSION')
make_head(_module, 'TIMECODEDATA')
make_head(_module, 'TRANSPORT_PROPERTIES')
make_head(_module, 'TRUECOLORINFO')
make_head(_module, 'UDCR_TAG')
make_head(_module, 'VA_OPTIONAL_VIDEO_PROPERTIES')
make_head(_module, 'VFW_FILTERLIST')
make_head(_module, 'VIDEOINFO')
make_head(_module, 'VIDEO_STREAM_CONFIG_CAPS')
make_head(_module, 'VMR9AllocationInfo')
make_head(_module, 'VMR9AlphaBitmap')
make_head(_module, 'VMR9DeinterlaceCaps')
make_head(_module, 'VMR9Frequency')
make_head(_module, 'VMR9MonitorInfo')
make_head(_module, 'VMR9NormalizedRect')
make_head(_module, 'VMR9PresentationInfo')
make_head(_module, 'VMR9ProcAmpControl')
make_head(_module, 'VMR9ProcAmpControlRange')
make_head(_module, 'VMR9VideoDesc')
make_head(_module, 'VMR9VideoStreamInfo')
make_head(_module, 'VMRALLOCATIONINFO')
make_head(_module, 'VMRALPHABITMAP')
make_head(_module, 'VMRDeinterlaceCaps')
make_head(_module, 'VMRFrequency')
make_head(_module, 'VMRGUID')
make_head(_module, 'VMRMONITORINFO')
make_head(_module, 'VMRPRESENTATIONINFO')
make_head(_module, 'VMRVIDEOSTREAMINFO')
make_head(_module, 'VMRVideoDesc')
make_head(_module, 'WMDRMProtectionInfo')
make_head(_module, '_IMSVidCtlEvents')
__all__ = [
    "ADVISE_CLIPPING",
    "ADVISE_COLORKEY",
    "ADVISE_DISPLAY_CHANGE",
    "ADVISE_NONE",
    "ADVISE_PALETTE",
    "ADVISE_POSITION",
    "ADVISE_TYPE",
    "ALLOCATOR_PROPERTIES",
    "AMAP_3D_TARGET",
    "AMAP_ALLOW_SYSMEM",
    "AMAP_DIRECTED_FLIP",
    "AMAP_DXVA_TARGET",
    "AMAP_FORCE_SYSMEM",
    "AMAP_PIXELFORMAT_VALID",
    "AMCONTROL_COLORINFO_PRESENT",
    "AMCONTROL_PAD_TO_16x9",
    "AMCONTROL_PAD_TO_4x3",
    "AMCONTROL_USED",
    "AMCOPPCommand",
    "AMCOPPSignature",
    "AMCOPPStatusInput",
    "AMCOPPStatusOutput",
    "AMCOPYPROTECT_RestrictDuplication",
    "AMDDS_ALL",
    "AMDDS_DCIPS",
    "AMDDS_DEFAULT",
    "AMDDS_NONE",
    "AMDDS_PS",
    "AMDDS_RGBFLP",
    "AMDDS_RGBOFF",
    "AMDDS_RGBOVR",
    "AMDDS_YUVFLP",
    "AMDDS_YUVOFF",
    "AMDDS_YUVOVR",
    "AMExtendedSeekingCapabilities",
    "AMF_AUTOMATICGAIN",
    "AMGETERRORTEXTPROCA",
    "AMGETERRORTEXTPROCW",
    "AMGetErrorTextA",
    "AMGetErrorTextW",
    "AMINTERLACE_1FieldPerSample",
    "AMINTERLACE_DisplayModeBobOnly",
    "AMINTERLACE_DisplayModeBobOrWeave",
    "AMINTERLACE_DisplayModeMask",
    "AMINTERLACE_DisplayModeWeaveOnly",
    "AMINTERLACE_Field1First",
    "AMINTERLACE_FieldPatBothIrregular",
    "AMINTERLACE_FieldPatBothRegular",
    "AMINTERLACE_FieldPatField1Only",
    "AMINTERLACE_FieldPatField2Only",
    "AMINTERLACE_FieldPatternMask",
    "AMINTERLACE_IsInterlaced",
    "AMINTERLACE_UNUSED",
    "AMMSF_ADDDEFAULTRENDERER",
    "AMMSF_CREATEPEER",
    "AMMSF_MMS_INIT_FLAGS",
    "AMMSF_MS_FLAGS",
    "AMMSF_NOCLOCK",
    "AMMSF_NOGRAPHTHREAD",
    "AMMSF_NORENDER",
    "AMMSF_NOSTALL",
    "AMMSF_RENDERALLSTREAMS",
    "AMMSF_RENDERTOEXISTING",
    "AMMSF_RENDERTYPEMASK",
    "AMMSF_RENDER_FLAGS",
    "AMMSF_RUN",
    "AMMSF_STOPIFNOSAMPLES",
    "AMOVERFX_DEINTERLACE",
    "AMOVERFX_MIRRORLEFTRIGHT",
    "AMOVERFX_MIRRORUPDOWN",
    "AMOVERFX_NOFX",
    "AMOVERLAYFX",
    "AMPLAYLISTEVENT_BREAK",
    "AMPLAYLISTEVENT_MASK",
    "AMPLAYLISTEVENT_NEXT",
    "AMPLAYLISTEVENT_REFRESH",
    "AMPLAYLISTEVENT_RESUME",
    "AMPLAYLISTITEM_CANBIND",
    "AMPLAYLISTITEM_CANSKIP",
    "AMPLAYLIST_FORCEBANNER",
    "AMPLAYLIST_STARTINSCANMODE",
    "AMPROPERTY_PIN",
    "AMPROPERTY_PIN_CATEGORY",
    "AMPROPERTY_PIN_MEDIUM",
    "AMPlayListEventFlags",
    "AMPlayListFlags",
    "AMPlayListItemFlags",
    "AMRESCTL_RESERVEFLAGS_RESERVE",
    "AMRESCTL_RESERVEFLAGS_UNRESERVE",
    "AMSTREAMSELECTENABLE_ENABLE",
    "AMSTREAMSELECTENABLE_ENABLEALL",
    "AMSTREAMSELECTINFO_ENABLED",
    "AMSTREAMSELECTINFO_EXCLUSIVE",
    "AMTUNER_EVENT_CHANGED",
    "AMTUNER_HASNOSIGNALSTRENGTH",
    "AMTUNER_MODE_AM_RADIO",
    "AMTUNER_MODE_DEFAULT",
    "AMTUNER_MODE_DSS",
    "AMTUNER_MODE_FM_RADIO",
    "AMTUNER_MODE_TV",
    "AMTUNER_NOSIGNAL",
    "AMTUNER_SIGNALPRESENT",
    "AMTUNER_SUBCHAN_DEFAULT",
    "AMTUNER_SUBCHAN_NO_TUNE",
    "AMTVAUDIO_EVENT_CHANGED",
    "AMTVAUDIO_MODE_LANG_A",
    "AMTVAUDIO_MODE_LANG_B",
    "AMTVAUDIO_MODE_LANG_C",
    "AMTVAUDIO_MODE_MONO",
    "AMTVAUDIO_MODE_STEREO",
    "AMTVAUDIO_PRESET_LANG_A",
    "AMTVAUDIO_PRESET_LANG_B",
    "AMTVAUDIO_PRESET_LANG_C",
    "AMTVAUDIO_PRESET_STEREO",
    "AMTVAudioEventType",
    "AMTunerEventType",
    "AMTunerModeType",
    "AMTunerSignalStrength",
    "AMTunerSubChannel",
    "AMVABUFFERINFO",
    "AMVABeginFrameInfo",
    "AMVACompBufferInfo",
    "AMVAEndFrameInfo",
    "AMVAInternalMemInfo",
    "AMVAUncompBufferInfo",
    "AMVAUncompDataInfo",
    "AMVA_QUERYRENDERSTATUSF_READ",
    "AMVA_TYPEINDEX_OUTPUTFRAME",
    "AMVPDATAINFO",
    "AMVPDIMINFO",
    "AMVPSIZE",
    "AMVP_BEST_BANDWIDTH",
    "AMVP_DO_NOT_CARE",
    "AMVP_INPUT_SAME_AS_OUTPUT",
    "AMVP_MODE",
    "AMVP_MODE_BOBINTERLEAVED",
    "AMVP_MODE_BOBNONINTERLEAVED",
    "AMVP_MODE_SKIPEVEN",
    "AMVP_MODE_SKIPODD",
    "AMVP_MODE_WEAVE",
    "AMVP_SELECT_FORMAT_BY",
    "AM_AC3_ALTERNATE_AUDIO",
    "AM_AC3_ALTERNATE_AUDIO_1",
    "AM_AC3_ALTERNATE_AUDIO_2",
    "AM_AC3_ALTERNATE_AUDIO_BOTH",
    "AM_AC3_BIT_STREAM_MODE",
    "AM_AC3_DIALOGUE_LEVEL",
    "AM_AC3_DOWNMIX",
    "AM_AC3_ERROR_CONCEALMENT",
    "AM_AC3_ROOM_TYPE",
    "AM_AC3_SERVICE_COMMENTARY",
    "AM_AC3_SERVICE_DIALOG_ONLY",
    "AM_AC3_SERVICE_EMERGENCY_FLASH",
    "AM_AC3_SERVICE_HEARING_IMPAIRED",
    "AM_AC3_SERVICE_MAIN_AUDIO",
    "AM_AC3_SERVICE_NO_DIALOG",
    "AM_AC3_SERVICE_VISUALLY_IMPAIRED",
    "AM_AC3_SERVICE_VOICE_OVER",
    "AM_ARMODE_CROP",
    "AM_ARMODE_LETTER_BOX",
    "AM_ARMODE_STRETCHED",
    "AM_ARMODE_STRETCHED_AS_PRIMARY",
    "AM_ASPECT_RATIO_MODE",
    "AM_AUDREND_STAT_PARAM_BREAK_COUNT",
    "AM_AUDREND_STAT_PARAM_BUFFERFULLNESS",
    "AM_AUDREND_STAT_PARAM_DISCONTINUITIES",
    "AM_AUDREND_STAT_PARAM_JITTER",
    "AM_AUDREND_STAT_PARAM_LAST_BUFFER_DUR",
    "AM_AUDREND_STAT_PARAM_SILENCE_DUR",
    "AM_AUDREND_STAT_PARAM_SLAVE_ACCUMERROR",
    "AM_AUDREND_STAT_PARAM_SLAVE_DROPWRITE_DUR",
    "AM_AUDREND_STAT_PARAM_SLAVE_HIGHLOWERROR",
    "AM_AUDREND_STAT_PARAM_SLAVE_LASTHIGHLOWERROR",
    "AM_AUDREND_STAT_PARAM_SLAVE_MODE",
    "AM_AUDREND_STAT_PARAM_SLAVE_RATE",
    "AM_COLCON",
    "AM_CONTENTPROPERTY_AUTHOR",
    "AM_CONTENTPROPERTY_COPYRIGHT",
    "AM_CONTENTPROPERTY_DESCRIPTION",
    "AM_CONTENTPROPERTY_TITLE",
    "AM_COPY_MACROVISION",
    "AM_COPY_MACROVISION_LEVEL",
    "AM_DIGITAL_CP",
    "AM_DIGITAL_CP_DVD_COMPLIANT",
    "AM_DIGITAL_CP_OFF",
    "AM_DIGITAL_CP_ON",
    "AM_DVDCOPYSTATE",
    "AM_DVDCOPYSTATE_AUTHENTICATION_NOT_REQUIRED",
    "AM_DVDCOPYSTATE_AUTHENTICATION_REQUIRED",
    "AM_DVDCOPYSTATE_DONE",
    "AM_DVDCOPYSTATE_INITIALIZE",
    "AM_DVDCOPYSTATE_INITIALIZE_TITLE",
    "AM_DVDCOPY_BUSKEY",
    "AM_DVDCOPY_CHLGKEY",
    "AM_DVDCOPY_DISCKEY",
    "AM_DVDCOPY_SET_COPY_STATE",
    "AM_DVDCOPY_TITLEKEY",
    "AM_DVD_ADAPT_GRAPH",
    "AM_DVD_CGMS_COPY_ONCE",
    "AM_DVD_CGMS_COPY_PERMITTED",
    "AM_DVD_CGMS_COPY_PROTECT_MASK",
    "AM_DVD_CGMS_NO_COPY",
    "AM_DVD_CGMS_RESERVED_MASK",
    "AM_DVD_COPYRIGHTED",
    "AM_DVD_COPYRIGHT_MASK",
    "AM_DVD_ChangeRate",
    "AM_DVD_DO_NOT_CLEAR",
    "AM_DVD_EVR_ONLY",
    "AM_DVD_EVR_QOS",
    "AM_DVD_GRAPH_FLAGS",
    "AM_DVD_HWDEC_ONLY",
    "AM_DVD_HWDEC_PREFER",
    "AM_DVD_MASK",
    "AM_DVD_NOT_COPYRIGHTED",
    "AM_DVD_NOVPE",
    "AM_DVD_RENDERSTATUS",
    "AM_DVD_SECTOR_NOT_PROTECTED",
    "AM_DVD_SECTOR_PROTECTED",
    "AM_DVD_SECTOR_PROTECT_MASK",
    "AM_DVD_STREAM_AUDIO",
    "AM_DVD_STREAM_FLAGS",
    "AM_DVD_STREAM_SUBPIC",
    "AM_DVD_STREAM_VIDEO",
    "AM_DVD_SWDEC_ONLY",
    "AM_DVD_SWDEC_PREFER",
    "AM_DVD_VMR9_ONLY",
    "AM_DVD_YUV",
    "AM_DvdKaraokeData",
    "AM_EXSEEK_BUFFERING",
    "AM_EXSEEK_CANSCAN",
    "AM_EXSEEK_CANSEEK",
    "AM_EXSEEK_MARKERSEEK",
    "AM_EXSEEK_NOSTANDARDREPAINT",
    "AM_EXSEEK_SCANWITHOUTCLOCK",
    "AM_EXSEEK_SENDS_VIDEOFRAMEREADY",
    "AM_ExactRateChange",
    "AM_FILESINK_FLAGS",
    "AM_FILE_OVERWRITE",
    "AM_FILTER_FLAGS",
    "AM_FILTER_FLAGS_REMOVABLE",
    "AM_FILTER_MISC_FLAGS_IS_RENDERER",
    "AM_FILTER_MISC_FLAGS_IS_SOURCE",
    "AM_FRAMESTEP_STEP",
    "AM_GBF_NODDSURFACELOCK",
    "AM_GBF_NOTASYNCPOINT",
    "AM_GBF_NOWAIT",
    "AM_GBF_PREVFRAMESKIPPED",
    "AM_GETDECODERCAP_QUERY_EVR_SUPPORT",
    "AM_GETDECODERCAP_QUERY_VMR9_SUPPORT",
    "AM_GETDECODERCAP_QUERY_VMR_SUPPORT",
    "AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS",
    "AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT",
    "AM_GRAPH_CONFIG_RECONNECT_FLAGS",
    "AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS",
    "AM_INTERFACESETID_Standard",
    "AM_INTF_SEARCH_FILTER",
    "AM_INTF_SEARCH_INPUT_PIN",
    "AM_INTF_SEARCH_OUTPUT_PIN",
    "AM_KSCATEGORY_AUDIO",
    "AM_KSCATEGORY_CAPTURE",
    "AM_KSCATEGORY_CROSSBAR",
    "AM_KSCATEGORY_DATACOMPRESSOR",
    "AM_KSCATEGORY_RENDER",
    "AM_KSCATEGORY_SPLITTER",
    "AM_KSCATEGORY_TVAUDIO",
    "AM_KSCATEGORY_TVTUNER",
    "AM_KSCATEGORY_VBICODEC",
    "AM_KSCATEGORY_VBICODEC_MI",
    "AM_KSCATEGORY_VIDEO",
    "AM_KSPROPSETID_AC3",
    "AM_KSPROPSETID_CopyProt",
    "AM_KSPROPSETID_DVD_RateChange",
    "AM_KSPROPSETID_DvdKaraoke",
    "AM_KSPROPSETID_DvdSubPic",
    "AM_KSPROPSETID_FrameStep",
    "AM_KSPROPSETID_MPEG4_MediaType_Attributes",
    "AM_KSPROPSETID_TSRateChange",
    "AM_L21_CCLEVEL_TC2",
    "AM_L21_CCSERVICE_Caption1",
    "AM_L21_CCSERVICE_Caption2",
    "AM_L21_CCSERVICE_DefChannel",
    "AM_L21_CCSERVICE_Invalid",
    "AM_L21_CCSERVICE_None",
    "AM_L21_CCSERVICE_Text1",
    "AM_L21_CCSERVICE_Text2",
    "AM_L21_CCSERVICE_XDS",
    "AM_L21_CCSTATE_Off",
    "AM_L21_CCSTATE_On",
    "AM_L21_CCSTYLE_None",
    "AM_L21_CCSTYLE_PaintOn",
    "AM_L21_CCSTYLE_PopOn",
    "AM_L21_CCSTYLE_RollUp",
    "AM_L21_DRAWBGMODE_Opaque",
    "AM_L21_DRAWBGMODE_Transparent",
    "AM_LINE21_CCLEVEL",
    "AM_LINE21_CCSERVICE",
    "AM_LINE21_CCSTATE",
    "AM_LINE21_CCSTYLE",
    "AM_LINE21_DRAWBGMODE",
    "AM_LOADSTATUS_CLOSED",
    "AM_LOADSTATUS_CONNECTING",
    "AM_LOADSTATUS_LOADINGDESCR",
    "AM_LOADSTATUS_LOADINGMCAST",
    "AM_LOADSTATUS_LOCATING",
    "AM_LOADSTATUS_OPEN",
    "AM_LOADSTATUS_OPENING",
    "AM_MACROVISION_DISABLED",
    "AM_MACROVISION_LEVEL1",
    "AM_MACROVISION_LEVEL2",
    "AM_MACROVISION_LEVEL3",
    "AM_MEDIAEVENT_FLAGS",
    "AM_MEDIAEVENT_NONOTIFY",
    "AM_MPEG2Level",
    "AM_MPEG2Level_High",
    "AM_MPEG2Level_High1440",
    "AM_MPEG2Level_Low",
    "AM_MPEG2Level_Main",
    "AM_MPEG2Profile",
    "AM_MPEG2Profile_High",
    "AM_MPEG2Profile_Main",
    "AM_MPEG2Profile_SNRScalable",
    "AM_MPEG2Profile_Simple",
    "AM_MPEG2Profile_SpatiallyScalable",
    "AM_MPEGSTREAMTYPE",
    "AM_MPEGSYSTEMTYPE",
    "AM_MPEG_AUDIO_DUAL_LEFT",
    "AM_MPEG_AUDIO_DUAL_MERGE",
    "AM_MPEG_AUDIO_DUAL_RIGHT",
    "AM_OVERLAY_NOTIFY_DEST_CHANGE",
    "AM_OVERLAY_NOTIFY_SOURCE_CHANGE",
    "AM_OVERLAY_NOTIFY_VISIBLE_CHANGE",
    "AM_PIN_FLOW_CONTROL_BLOCK",
    "AM_PROPERTY_AC3",
    "AM_PROPERTY_AC3_ALTERNATE_AUDIO",
    "AM_PROPERTY_AC3_BIT_STREAM_MODE",
    "AM_PROPERTY_AC3_DIALOGUE_LEVEL",
    "AM_PROPERTY_AC3_DOWNMIX",
    "AM_PROPERTY_AC3_ERROR_CONCEALMENT",
    "AM_PROPERTY_AC3_LANGUAGE_CODE",
    "AM_PROPERTY_AC3_ROOM_TYPE",
    "AM_PROPERTY_COPY_ANALOG_COMPONENT",
    "AM_PROPERTY_COPY_DIGITAL_CP",
    "AM_PROPERTY_COPY_DVD_SRM",
    "AM_PROPERTY_COPY_MACROVISION",
    "AM_PROPERTY_DVDCOPYPROT",
    "AM_PROPERTY_DVDCOPY_CHLG_KEY",
    "AM_PROPERTY_DVDCOPY_DEC_KEY2",
    "AM_PROPERTY_DVDCOPY_DISC_KEY",
    "AM_PROPERTY_DVDCOPY_DVD_KEY1",
    "AM_PROPERTY_DVDCOPY_REGION",
    "AM_PROPERTY_DVDCOPY_SET_COPY_STATE",
    "AM_PROPERTY_DVDCOPY_SUPPORTS_NEW_KEYCOUNT",
    "AM_PROPERTY_DVDCOPY_TITLE_KEY",
    "AM_PROPERTY_DVDKARAOKE",
    "AM_PROPERTY_DVDKARAOKE_DATA",
    "AM_PROPERTY_DVDKARAOKE_ENABLE",
    "AM_PROPERTY_DVDSUBPIC",
    "AM_PROPERTY_DVDSUBPIC_COMPOSIT_ON",
    "AM_PROPERTY_DVDSUBPIC_HLI",
    "AM_PROPERTY_DVDSUBPIC_PALETTE",
    "AM_PROPERTY_DVD_RATE_CHANGE",
    "AM_PROPERTY_FRAMESTEP",
    "AM_PROPERTY_FRAMESTEP_CANCEL",
    "AM_PROPERTY_FRAMESTEP_CANSTEP",
    "AM_PROPERTY_FRAMESTEP_CANSTEPMULTIPLE",
    "AM_PROPERTY_FRAMESTEP_STEP",
    "AM_PROPERTY_SPHLI",
    "AM_PROPERTY_SPPAL",
    "AM_PROPERTY_TS_RATE_CHANGE",
    "AM_PUSHSOURCECAPS_INTERNAL_RM",
    "AM_PUSHSOURCECAPS_NOT_LIVE",
    "AM_PUSHSOURCECAPS_PRIVATE_CLOCK",
    "AM_PUSHSOURCEREQS_USE_CLOCK_CHAIN",
    "AM_PUSHSOURCEREQS_USE_STREAM_CLOCK",
    "AM_QUERY_DECODER_ATSC_HD_SUPPORT",
    "AM_QUERY_DECODER_ATSC_SD_SUPPORT",
    "AM_QUERY_DECODER_DVD_SUPPORT",
    "AM_QUERY_DECODER_DXVA_1_SUPPORT",
    "AM_QUERY_DECODER_VMR_SUPPORT",
    "AM_QueryRate",
    "AM_RATE_ChangeRate",
    "AM_RATE_CorrectTS",
    "AM_RATE_DecoderPosition",
    "AM_RATE_DecoderVersion",
    "AM_RATE_ExactRateChange",
    "AM_RATE_FullDataRateMax",
    "AM_RATE_MaxFullDataRate",
    "AM_RATE_QueryFullFrameRate",
    "AM_RATE_QueryLastRateSegPTS",
    "AM_RATE_QueryMapping",
    "AM_RATE_ResetOnTimeDisc",
    "AM_RATE_ReverseDecode",
    "AM_RATE_ReverseMaxFullDataRate",
    "AM_RATE_SimpleRateChange",
    "AM_RATE_Step",
    "AM_RATE_UseRateVersion",
    "AM_RENDEREX_RENDERTOEXISTINGRENDERERS",
    "AM_ReverseBlockEnd",
    "AM_ReverseBlockStart",
    "AM_SAMPLE2_PROPERTIES",
    "AM_SAMPLE_DATADISCONTINUITY",
    "AM_SAMPLE_ENDOFSTREAM",
    "AM_SAMPLE_FLUSH_ON_PAUSE",
    "AM_SAMPLE_PREROLL",
    "AM_SAMPLE_PROPERTY_FLAGS",
    "AM_SAMPLE_SPLICEPOINT",
    "AM_SAMPLE_STOPVALID",
    "AM_SAMPLE_TIMEDISCONTINUITY",
    "AM_SAMPLE_TIMEVALID",
    "AM_SAMPLE_TYPECHANGED",
    "AM_SEEKING_AbsolutePositioning",
    "AM_SEEKING_CanDoSegments",
    "AM_SEEKING_CanGetCurrentPos",
    "AM_SEEKING_CanGetDuration",
    "AM_SEEKING_CanGetStopPos",
    "AM_SEEKING_CanPlayBackwards",
    "AM_SEEKING_CanSeekAbsolute",
    "AM_SEEKING_CanSeekBackwards",
    "AM_SEEKING_CanSeekForwards",
    "AM_SEEKING_IncrementalPositioning",
    "AM_SEEKING_NoFlush",
    "AM_SEEKING_NoPositioning",
    "AM_SEEKING_PositioningBitsMask",
    "AM_SEEKING_RelativePositioning",
    "AM_SEEKING_ReturnTime",
    "AM_SEEKING_SEEKING_CAPABILITIES",
    "AM_SEEKING_SEEKING_FLAGS",
    "AM_SEEKING_SeekToKeyFrame",
    "AM_SEEKING_Segment",
    "AM_SEEKING_Source",
    "AM_STREAM_CONTROL",
    "AM_STREAM_INFO",
    "AM_STREAM_INFO_DISCARDING",
    "AM_STREAM_INFO_FLAGS",
    "AM_STREAM_INFO_START_DEFINED",
    "AM_STREAM_INFO_STOP_DEFINED",
    "AM_STREAM_INFO_STOP_SEND_EXTRA",
    "AM_STREAM_MEDIA",
    "AM_SimpleRateChange",
    "AM_UseNewCSSKey",
    "AM_VIDEO_FLAG_B_SAMPLE",
    "AM_VIDEO_FLAG_FIELD1",
    "AM_VIDEO_FLAG_FIELD1FIRST",
    "AM_VIDEO_FLAG_FIELD2",
    "AM_VIDEO_FLAG_FIELD_MASK",
    "AM_VIDEO_FLAG_INTERLEAVED_FRAME",
    "AM_VIDEO_FLAG_IPB_MASK",
    "AM_VIDEO_FLAG_I_SAMPLE",
    "AM_VIDEO_FLAG_P_SAMPLE",
    "AM_VIDEO_FLAG_REPEAT_FIELD",
    "AM_VIDEO_FLAG_WEAVE",
    "AM_WST_DRAWBGMODE",
    "AM_WST_DRAWBGMODE_Opaque",
    "AM_WST_DRAWBGMODE_Transparent",
    "AM_WST_LEVEL",
    "AM_WST_LEVEL_1_5",
    "AM_WST_PAGE",
    "AM_WST_SERVICE",
    "AM_WST_SERVICE_IDS",
    "AM_WST_SERVICE_Invalid",
    "AM_WST_SERVICE_None",
    "AM_WST_SERVICE_Text",
    "AM_WST_STATE",
    "AM_WST_STATE_Off",
    "AM_WST_STATE_On",
    "AM_WST_STYLE",
    "AM_WST_STYLE_Invers",
    "AM_WST_STYLE_None",
    "ANALOGVIDEOINFO",
    "ANALOG_AUXIN_NETWORK_TYPE",
    "ANALOG_FM_NETWORK_TYPE",
    "ANALOG_TV_NETWORK_TYPE",
    "ATSCCT_AC3",
    "ATSCChannelTuneRequest",
    "ATSCComponentType",
    "ATSCComponentTypeFlags",
    "ATSCLocator",
    "ATSCTuningSpace",
    "ATSC_EIT_TID",
    "ATSC_ETM_LOCATION_IN_PTC_FOR_EVENT",
    "ATSC_ETM_LOCATION_IN_PTC_FOR_PSIP",
    "ATSC_ETM_LOCATION_NOT_PRESENT",
    "ATSC_ETM_LOCATION_RESERVED",
    "ATSC_ETT_TID",
    "ATSC_FILTER_OPTIONS",
    "ATSC_MGT_PID",
    "ATSC_MGT_TID",
    "ATSC_PIT_TID",
    "ATSC_RRT_PID",
    "ATSC_RRT_TID",
    "ATSC_STT_PID",
    "ATSC_STT_TID",
    "ATSC_TERRESTRIAL_TV_NETWORK_TYPE",
    "ATSC_VCT_CABL_TID",
    "ATSC_VCT_PID",
    "ATSC_VCT_TERR_TID",
    "AUDIO_STREAM_CONFIG_CAPS",
    "AVIEXTHEADER",
    "AVIFIELDINDEX",
    "AVIF_COPYRIGHTED",
    "AVIF_HASINDEX",
    "AVIF_ISINTERLEAVED",
    "AVIF_MUSTUSEINDEX",
    "AVIF_TRUSTCKTYPE",
    "AVIF_WASCAPTUREFILE",
    "AVIIF_COMPRESSOR",
    "AVIIF_COMPUSE",
    "AVIIF_FIRSTPART",
    "AVIIF_KEYFRAME",
    "AVIIF_LASTPART",
    "AVIIF_LIST",
    "AVIIF_NOTIME",
    "AVIIF_NO_TIME",
    "AVIINDEXENTRY",
    "AVIMAINHEADER",
    "AVIMETAINDEX",
    "AVIOLDINDEX",
    "AVIPALCHANGE",
    "AVISF_DISABLED",
    "AVISF_VIDEO_PALCHANGES",
    "AVISTDINDEX",
    "AVISTDINDEX_DELTAFRAME",
    "AVISTDINDEX_ENTRY",
    "AVISTREAMHEADER",
    "AVISUPERINDEX",
    "AVIStreamHeader",
    "AVITCDLINDEX",
    "AVITCDLINDEX_ENTRY",
    "AVITIMECODEINDEX",
    "AVITIMEDINDEX",
    "AVITIMEDINDEX_ENTRY",
    "AVI_HEADERSIZE",
    "AVI_INDEX_IS_DATA",
    "AVI_INDEX_OF_CHUNKS",
    "AVI_INDEX_OF_INDEXES",
    "AVI_INDEX_OF_SUB_2FIELD",
    "AVI_INDEX_OF_TIMED_CHUNKS",
    "AVI_INDEX_SUB_2FIELD",
    "AVI_INDEX_SUB_DEFAULT",
    "AnalogAudioComponentType",
    "AnalogLocator",
    "AnalogRadioTuningSpace",
    "AnalogTVTuningSpace",
    "AnalogVideoMask_MCE_NTSC",
    "AnalogVideoMask_MCE_PAL",
    "AnalogVideoMask_MCE_SECAM",
    "AnalogVideoStandard",
    "AnalogVideo_NTSC_433",
    "AnalogVideo_NTSC_M",
    "AnalogVideo_NTSC_M_J",
    "AnalogVideo_NTSC_Mask",
    "AnalogVideo_None",
    "AnalogVideo_PAL_60",
    "AnalogVideo_PAL_B",
    "AnalogVideo_PAL_D",
    "AnalogVideo_PAL_G",
    "AnalogVideo_PAL_H",
    "AnalogVideo_PAL_I",
    "AnalogVideo_PAL_M",
    "AnalogVideo_PAL_Mask",
    "AnalogVideo_PAL_N",
    "AnalogVideo_PAL_N_COMBO",
    "AnalogVideo_SECAM_B",
    "AnalogVideo_SECAM_D",
    "AnalogVideo_SECAM_G",
    "AnalogVideo_SECAM_H",
    "AnalogVideo_SECAM_K",
    "AnalogVideo_SECAM_K1",
    "AnalogVideo_SECAM_L",
    "AnalogVideo_SECAM_L1",
    "AnalogVideo_SECAM_Mask",
    "ApplicationTypeType",
    "AudioType_Commentary",
    "AudioType_Dialogue",
    "AudioType_Emergency",
    "AudioType_Hearing_Impaired",
    "AudioType_Music_And_Effects",
    "AudioType_Reserved",
    "AudioType_Standard",
    "AudioType_Visually_Impaired",
    "AudioType_Voiceover",
    "AuxInTuningSpace",
    "BDACOMP_EXCLUDE_TS_FROM_TR",
    "BDACOMP_INCLUDE_COMPONENTS_IN_TR",
    "BDACOMP_INCLUDE_LOCATOR_IN_TR",
    "BDACOMP_NOT_DEFINED",
    "BDANETWORKTYPE_ATSC",
    "BDANODE_DESCRIPTOR",
    "BDA_BCC_RATE_1_2",
    "BDA_BCC_RATE_1_3",
    "BDA_BCC_RATE_1_4",
    "BDA_BCC_RATE_2_3",
    "BDA_BCC_RATE_2_5",
    "BDA_BCC_RATE_3_4",
    "BDA_BCC_RATE_3_5",
    "BDA_BCC_RATE_4_5",
    "BDA_BCC_RATE_5_11",
    "BDA_BCC_RATE_5_6",
    "BDA_BCC_RATE_6_7",
    "BDA_BCC_RATE_7_8",
    "BDA_BCC_RATE_8_9",
    "BDA_BCC_RATE_9_10",
    "BDA_BCC_RATE_MAX",
    "BDA_BCC_RATE_NOT_DEFINED",
    "BDA_BCC_RATE_NOT_SET",
    "BDA_BUFFER",
    "BDA_CAS_CHECK_ENTITLEMENTTOKEN",
    "BDA_CAS_CLOSEMMIDATA",
    "BDA_CAS_CLOSE_MMIDIALOG",
    "BDA_CAS_OPENMMIDATA",
    "BDA_CAS_REQUESTTUNERDATA",
    "BDA_CA_MODULE_UI",
    "BDA_CHANGES_COMPLETE",
    "BDA_CHANGES_PENDING",
    "BDA_CHANGE_STATE",
    "BDA_CHAN_BANDWITH_NOT_DEFINED",
    "BDA_CHAN_BANDWITH_NOT_SET",
    "BDA_CONDITIONALACCESS_MMICLOSEREASON",
    "BDA_CONDITIONALACCESS_REQUESTTYPE",
    "BDA_CONDITIONALACCESS_SESSION_RESULT",
    "BDA_Channel",
    "BDA_Channel_Bandwidth",
    "BDA_Comp_Flags",
    "BDA_DEBUG_DATA",
    "BDA_DEBUG_DATA_AVAILABLE",
    "BDA_DEBUG_DATA_TYPE_STRING",
    "BDA_DISCOVERY_COMPLETE",
    "BDA_DISCOVERY_REQUIRED",
    "BDA_DISCOVERY_STATE",
    "BDA_DISCOVERY_UNSPECIFIED",
    "BDA_DISEQC_RESPONSE",
    "BDA_DISEQC_SEND",
    "BDA_DRM_DRMSTATUS",
    "BDA_DVBT2_L1_SIGNALLING_DATA",
    "BDA_DigitalSignalStandard",
    "BDA_DrmPairingError",
    "BDA_DrmPairing_Aborted",
    "BDA_DrmPairing_DrmInitFailed",
    "BDA_DrmPairing_DrmNotPaired",
    "BDA_DrmPairing_DrmRePairSoon",
    "BDA_DrmPairing_HardwareFailure",
    "BDA_DrmPairing_NeedIndiv",
    "BDA_DrmPairing_NeedRevocationData",
    "BDA_DrmPairing_NeedSDKUpdate",
    "BDA_DrmPairing_Other",
    "BDA_DrmPairing_Succeeded",
    "BDA_ETHERNET_ADDRESS",
    "BDA_ETHERNET_ADDRESS_LIST",
    "BDA_EVENT_ACCESS_DENIED",
    "BDA_EVENT_ACCESS_GRANTED",
    "BDA_EVENT_CHANNEL_ACQUIRED",
    "BDA_EVENT_CHANNEL_ACTIVATED",
    "BDA_EVENT_CHANNEL_DEACTIVATED",
    "BDA_EVENT_CHANNEL_LOST",
    "BDA_EVENT_CHANNEL_SOURCE_CHANGED",
    "BDA_EVENT_DATA",
    "BDA_EVENT_DATA_START",
    "BDA_EVENT_DATA_STOP",
    "BDA_EVENT_ID",
    "BDA_EVENT_OFFER_EXTENDED",
    "BDA_EVENT_PURCHASE_COMPLETED",
    "BDA_EVENT_SIGNAL_LOCK",
    "BDA_EVENT_SIGNAL_LOSS",
    "BDA_EVENT_SMART_CARD_INSERTED",
    "BDA_EVENT_SMART_CARD_REMOVED",
    "BDA_EVENT_SUBCHANNEL_ACQUIRED",
    "BDA_EVENT_SUBCHANNEL_ACTIVATED",
    "BDA_EVENT_SUBCHANNEL_DEACTIVATED",
    "BDA_EVENT_SUBCHANNEL_LOST",
    "BDA_EVENT_SUBCHANNEL_SOURCE_CHANGED",
    "BDA_E_ACCESS_DENIED",
    "BDA_E_BUFFER_TOO_SMALL",
    "BDA_E_DISABLED",
    "BDA_E_FAILURE",
    "BDA_E_INVALID_CAPTURE_TOKEN",
    "BDA_E_INVALID_ENTITLEMENT_TOKEN",
    "BDA_E_INVALID_HANDLE",
    "BDA_E_INVALID_LANGUAGE",
    "BDA_E_INVALID_PURCHASE_TOKEN",
    "BDA_E_INVALID_SCHEMA",
    "BDA_E_INVALID_TUNE_REQUEST",
    "BDA_E_INVALID_TYPE",
    "BDA_E_IPNETWORK_ADDRESS_NOT_FOUND",
    "BDA_E_IPNETWORK_ERROR",
    "BDA_E_IPNETWORK_TIMEOUT",
    "BDA_E_IPNETWORK_UNAVAILABLE",
    "BDA_E_NOT_FOUND",
    "BDA_E_NOT_IMPLEMENTED",
    "BDA_E_NO_HANDLER",
    "BDA_E_NO_MORE_DATA",
    "BDA_E_NO_MORE_EVENTS",
    "BDA_E_NO_SUCH_COMMAND",
    "BDA_E_OUT_OF_BOUNDS",
    "BDA_E_OUT_OF_MEMORY",
    "BDA_E_OUT_OF_RESOURCES",
    "BDA_E_READ_ONLY",
    "BDA_E_TIMEOUT_ELAPSED",
    "BDA_E_TUNER_CONFLICT",
    "BDA_E_TUNER_INITIALIZING",
    "BDA_E_TUNER_REQUIRED",
    "BDA_E_TUNE_FAILED_SDV01",
    "BDA_E_TUNE_FAILED_SDV02",
    "BDA_E_TUNE_FAILED_SDV03",
    "BDA_E_TUNE_FAILED_SDV04",
    "BDA_E_TUNE_FAILED_SDV05",
    "BDA_E_TUNE_FAILED_SDV06",
    "BDA_E_TUNE_FAILED_SDV07",
    "BDA_E_TUNE_FAILED_SDV08",
    "BDA_E_TUNE_FAILED_SDVFF",
    "BDA_E_WMDRM_INVALID_CERTIFICATE",
    "BDA_E_WMDRM_INVALID_DATE",
    "BDA_E_WMDRM_INVALID_PROXIMITY",
    "BDA_E_WMDRM_INVALID_SIGNATURE",
    "BDA_E_WMDRM_INVALID_VERSION",
    "BDA_E_WMDRM_KEY_ID_NOT_FOUND",
    "BDA_E_WOULD_DISRUPT_STREAMING",
    "BDA_FEC_BCH",
    "BDA_FEC_LDPC",
    "BDA_FEC_MAX",
    "BDA_FEC_METHOD_NOT_DEFINED",
    "BDA_FEC_METHOD_NOT_SET",
    "BDA_FEC_RS_147_130",
    "BDA_FEC_RS_204_188",
    "BDA_FEC_VITERBI",
    "BDA_FILTERED_MULTICAST",
    "BDA_FREQUENCY_MULTIPLIER_NOT_DEFINED",
    "BDA_FREQUENCY_MULTIPLIER_NOT_SET",
    "BDA_FREQUENCY_NOT_DEFINED",
    "BDA_FREQUENCY_NOT_SET",
    "BDA_Frequency",
    "BDA_Frequency_Multiplier",
    "BDA_GDDS_DATA",
    "BDA_GDDS_DATATYPE",
    "BDA_GUARD_19_128",
    "BDA_GUARD_19_256",
    "BDA_GUARD_1_128",
    "BDA_GUARD_1_16",
    "BDA_GUARD_1_32",
    "BDA_GUARD_1_4",
    "BDA_GUARD_1_8",
    "BDA_GUARD_MAX",
    "BDA_GUARD_NOT_DEFINED",
    "BDA_GUARD_NOT_SET",
    "BDA_HALPHA_1",
    "BDA_HALPHA_2",
    "BDA_HALPHA_4",
    "BDA_HALPHA_MAX",
    "BDA_HALPHA_NOT_DEFINED",
    "BDA_HALPHA_NOT_SET",
    "BDA_IPv4_ADDRESS",
    "BDA_IPv4_ADDRESS_LIST",
    "BDA_IPv6_ADDRESS",
    "BDA_IPv6_ADDRESS_LIST",
    "BDA_ISDBCAS_EMG_REQ",
    "BDA_ISDBCAS_REQUESTHEADER",
    "BDA_ISDBCAS_RESPONSEDATA",
    "BDA_LNB_SOURCE_A",
    "BDA_LNB_SOURCE_B",
    "BDA_LNB_SOURCE_C",
    "BDA_LNB_SOURCE_D",
    "BDA_LNB_SOURCE_MAX",
    "BDA_LNB_SOURCE_NOT_DEFINED",
    "BDA_LNB_SOURCE_NOT_SET",
    "BDA_LockType",
    "BDA_MOD_1024QAM",
    "BDA_MOD_112QAM",
    "BDA_MOD_128QAM",
    "BDA_MOD_160QAM",
    "BDA_MOD_16APSK",
    "BDA_MOD_16QAM",
    "BDA_MOD_16VSB",
    "BDA_MOD_192QAM",
    "BDA_MOD_224QAM",
    "BDA_MOD_256QAM",
    "BDA_MOD_320QAM",
    "BDA_MOD_32APSK",
    "BDA_MOD_32QAM",
    "BDA_MOD_384QAM",
    "BDA_MOD_448QAM",
    "BDA_MOD_512QAM",
    "BDA_MOD_640QAM",
    "BDA_MOD_64QAM",
    "BDA_MOD_768QAM",
    "BDA_MOD_80QAM",
    "BDA_MOD_896QAM",
    "BDA_MOD_8PSK",
    "BDA_MOD_8VSB",
    "BDA_MOD_96QAM",
    "BDA_MOD_ANALOG_AMPLITUDE",
    "BDA_MOD_ANALOG_FREQUENCY",
    "BDA_MOD_BPSK",
    "BDA_MOD_DIRECTV",
    "BDA_MOD_ISDB_S_TMCC",
    "BDA_MOD_ISDB_T_TMCC",
    "BDA_MOD_MAX",
    "BDA_MOD_NBC_8PSK",
    "BDA_MOD_NBC_QPSK",
    "BDA_MOD_NOT_DEFINED",
    "BDA_MOD_NOT_SET",
    "BDA_MOD_OQPSK",
    "BDA_MOD_QPSK",
    "BDA_MOD_RF",
    "BDA_MULTICAST_MODE",
    "BDA_MUX_PIDLISTITEM",
    "BDA_NO_MULTICAST",
    "BDA_PID_MAP",
    "BDA_PID_UNMAP",
    "BDA_PILOT_MAX",
    "BDA_PILOT_NOT_DEFINED",
    "BDA_PILOT_NOT_SET",
    "BDA_PILOT_OFF",
    "BDA_PILOT_ON",
    "BDA_PLP_ID_NOT_SET",
    "BDA_POLARISATION_CIRCULAR_L",
    "BDA_POLARISATION_CIRCULAR_R",
    "BDA_POLARISATION_LINEAR_H",
    "BDA_POLARISATION_LINEAR_V",
    "BDA_POLARISATION_MAX",
    "BDA_POLARISATION_NOT_DEFINED",
    "BDA_POLARISATION_NOT_SET",
    "BDA_PROGRAM_PID_LIST",
    "BDA_PROMISCUOUS_MULTICAST",
    "BDA_RANGE_NOT_DEFINED",
    "BDA_RANGE_NOT_SET",
    "BDA_RATING_PINRESET",
    "BDA_ROLL_OFF_20",
    "BDA_ROLL_OFF_25",
    "BDA_ROLL_OFF_35",
    "BDA_ROLL_OFF_MAX",
    "BDA_ROLL_OFF_NOT_DEFINED",
    "BDA_ROLL_OFF_NOT_SET",
    "BDA_Range",
    "BDA_SCAN_CAPABILTIES",
    "BDA_SCAN_MOD_1024QAM",
    "BDA_SCAN_MOD_112QAM",
    "BDA_SCAN_MOD_128QAM",
    "BDA_SCAN_MOD_160QAM",
    "BDA_SCAN_MOD_16APSK",
    "BDA_SCAN_MOD_16QAM",
    "BDA_SCAN_MOD_16VSB",
    "BDA_SCAN_MOD_192QAM",
    "BDA_SCAN_MOD_224QAM",
    "BDA_SCAN_MOD_256QAM",
    "BDA_SCAN_MOD_320QAM",
    "BDA_SCAN_MOD_32APSK",
    "BDA_SCAN_MOD_32QAM",
    "BDA_SCAN_MOD_384QAM",
    "BDA_SCAN_MOD_448QAM",
    "BDA_SCAN_MOD_512QAM",
    "BDA_SCAN_MOD_640QAM",
    "BDA_SCAN_MOD_64QAM",
    "BDA_SCAN_MOD_768QAM",
    "BDA_SCAN_MOD_80QAM",
    "BDA_SCAN_MOD_896QAM",
    "BDA_SCAN_MOD_8PSK",
    "BDA_SCAN_MOD_8VSB",
    "BDA_SCAN_MOD_96QAM",
    "BDA_SCAN_MOD_AM_RADIO",
    "BDA_SCAN_MOD_BPSK",
    "BDA_SCAN_MOD_FM_RADIO",
    "BDA_SCAN_MOD_OQPSK",
    "BDA_SCAN_MOD_QPSK",
    "BDA_SCAN_MOD_RF",
    "BDA_SCAN_START",
    "BDA_SCAN_STATE",
    "BDA_SIGNAL_ACTIVE",
    "BDA_SIGNAL_INACTIVE",
    "BDA_SIGNAL_STATE",
    "BDA_SIGNAL_TIMEOUTS",
    "BDA_SIGNAL_UNAVAILABLE",
    "BDA_SPECTRAL_INVERSION_AUTOMATIC",
    "BDA_SPECTRAL_INVERSION_INVERTED",
    "BDA_SPECTRAL_INVERSION_MAX",
    "BDA_SPECTRAL_INVERSION_NORMAL",
    "BDA_SPECTRAL_INVERSION_NOT_DEFINED",
    "BDA_SPECTRAL_INVERSION_NOT_SET",
    "BDA_STRING",
    "BDA_SignalType",
    "BDA_TABLE_SECTION",
    "BDA_TEMPLATE_CONNECTION",
    "BDA_TEMPLATE_PIN_JOINT",
    "BDA_TRANSPORT_INFO",
    "BDA_TS_SELECTORINFO",
    "BDA_TS_SELECTORINFO_ISDBS_EXT",
    "BDA_TUNER_DIAGNOSTICS",
    "BDA_TUNER_TUNERSTATE",
    "BDA_UNDEFINED_CHANNEL",
    "BDA_USERACTIVITY_INTERVAL",
    "BDA_WMDRMTUNER_PIDPROTECTION",
    "BDA_WMDRMTUNER_PURCHASEENTITLEMENT",
    "BDA_WMDRM_KEYINFOLIST",
    "BDA_WMDRM_RENEWLICENSE",
    "BDA_WMDRM_STATUS",
    "BDA_XMIT_MODE_16K",
    "BDA_XMIT_MODE_1K",
    "BDA_XMIT_MODE_2K",
    "BDA_XMIT_MODE_2K_INTERLEAVED",
    "BDA_XMIT_MODE_32K",
    "BDA_XMIT_MODE_4K",
    "BDA_XMIT_MODE_4K_INTERLEAVED",
    "BDA_XMIT_MODE_8K",
    "BDA_XMIT_MODE_MAX",
    "BDA_XMIT_MODE_NOT_DEFINED",
    "BDA_XMIT_MODE_NOT_SET",
    "BSKYB_TERRESTRIAL_TV_NETWORK_TYPE",
    "BadSampleInfo",
    "Bda_DigitalStandard_ATSC",
    "Bda_DigitalStandard_DVB_C",
    "Bda_DigitalStandard_DVB_S",
    "Bda_DigitalStandard_DVB_T",
    "Bda_DigitalStandard_ISDB_C",
    "Bda_DigitalStandard_ISDB_S",
    "Bda_DigitalStandard_ISDB_T",
    "Bda_DigitalStandard_None",
    "Bda_LockType_Complete",
    "Bda_LockType_DecoderDemod",
    "Bda_LockType_None",
    "Bda_LockType_PLL",
    "Bda_SignalType_Analog",
    "Bda_SignalType_Digital",
    "Bda_SignalType_Unknown",
    "BfEnTvRat_Attributes_CAE_TV",
    "BfEnTvRat_Attributes_CAF_TV",
    "BfEnTvRat_Attributes_MPAA",
    "BfEnTvRat_Attributes_US_TV",
    "BfEnTvRat_GenericAttributes",
    "BfEnTvRat_GenericAttributes_BfAttrNone",
    "BfEnTvRat_GenericAttributes_BfIsAttr_1",
    "BfEnTvRat_GenericAttributes_BfIsAttr_2",
    "BfEnTvRat_GenericAttributes_BfIsAttr_3",
    "BfEnTvRat_GenericAttributes_BfIsAttr_4",
    "BfEnTvRat_GenericAttributes_BfIsAttr_5",
    "BfEnTvRat_GenericAttributes_BfIsAttr_6",
    "BfEnTvRat_GenericAttributes_BfIsAttr_7",
    "BfEnTvRat_GenericAttributes_BfIsBlocked",
    "BfEnTvRat_GenericAttributes_BfValidAttrSubmask",
    "BinaryConvolutionCodeRate",
    "BroadcastEventService",
    "CAE_IsBlocked",
    "CAE_TV_14",
    "CAE_TV_18",
    "CAE_TV_C",
    "CAE_TV_C8",
    "CAE_TV_Exempt",
    "CAE_TV_G",
    "CAE_TV_PG",
    "CAE_TV_Reserved",
    "CAE_ValidAttrSubmask",
    "CAF_IsBlocked",
    "CAF_TV_13",
    "CAF_TV_16",
    "CAF_TV_18",
    "CAF_TV_8",
    "CAF_TV_Exempt",
    "CAF_TV_G",
    "CAF_TV_Reserved",
    "CAF_TV_Reserved6",
    "CAF_ValidAttrSubmask",
    "CAPTURE_STREAMTIME",
    "CDEF_BYPASS_CLASS_MANAGER",
    "CDEF_CLASS_DEFAULT",
    "CDEF_DEVMON_CMGR_DEVICE",
    "CDEF_DEVMON_DMO",
    "CDEF_DEVMON_FILTER",
    "CDEF_DEVMON_PNP_DEVICE",
    "CDEF_DEVMON_SELECTIVE_MASK",
    "CDEF_MERIT_ABOVE_DO_NOT_USE",
    "CFSTR_VFW_FILTERLIST",
    "CHARS_IN_GUID",
    "CK_INDEX",
    "CK_NOCOLORKEY",
    "CK_RGB",
    "CLSID_AMAudioData",
    "CLSID_AMAudioStream",
    "CLSID_AMDirectDrawStream",
    "CLSID_AMMediaTypeStream",
    "CLSID_AMMultiMediaStream",
    "CLSID_CPCAFiltersCategory",
    "CLSID_DMOFilterCategory",
    "CLSID_DMOWrapperFilter",
    "CLSID_DTFilterEncProperties",
    "CLSID_DTFilterTagProperties",
    "CLSID_ETFilterEncProperties",
    "CLSID_ETFilterTagProperties",
    "CLSID_Mpeg2TableFilter",
    "CLSID_PBDA_AUX_DATA_TYPE",
    "CLSID_PBDA_Encoder_DATA_TYPE",
    "CLSID_PBDA_FDC_DATA_TYPE",
    "CLSID_PBDA_GDDS_DATA_TYPE",
    "CLSID_PTFilter",
    "CLSID_XDSCodecProperties",
    "CLSID_XDSCodecTagProperties",
    "COLORKEY",
    "COLORKEY_TYPE",
    "COMPLETION_STATUS_FLAGS",
    "COMPONENT_TAG_CAPTION_MAX",
    "COMPONENT_TAG_CAPTION_MIN",
    "COMPONENT_TAG_SUPERIMPOSE_MAX",
    "COMPONENT_TAG_SUPERIMPOSE_MIN",
    "COMPSTAT_ABORT",
    "COMPSTAT_NOUPDATEOK",
    "COMPSTAT_WAIT",
    "CONDITIONALACCESS_ABORTED",
    "CONDITIONALACCESS_ACCESS_NOT_POSSIBLE",
    "CONDITIONALACCESS_ACCESS_POSSIBLE",
    "CONDITIONALACCESS_ACCESS_POSSIBLE_NO_STREAMING_DISRUPTION",
    "CONDITIONALACCESS_ACCESS_UNSPECIFIED",
    "CONDITIONALACCESS_CLOSED_ITSELF",
    "CONDITIONALACCESS_DIALOG_FOCUS_CHANGE",
    "CONDITIONALACCESS_DIALOG_TIMEOUT",
    "CONDITIONALACCESS_DIALOG_USER_DISMISSED",
    "CONDITIONALACCESS_DIALOG_USER_NOT_AVAILABLE",
    "CONDITIONALACCESS_ENDED_NOCHANGE",
    "CONDITIONALACCESS_SUCCESSFULL",
    "CONDITIONALACCESS_TUNER_REQUESTED_CLOSE",
    "CONDITIONALACCESS_UNSPECIFIED",
    "CONTENT",
    "COPPEventBlockReason",
    "COPP_ACP_ForceDWORD",
    "COPP_ACP_Level0",
    "COPP_ACP_Level1",
    "COPP_ACP_Level2",
    "COPP_ACP_Level3",
    "COPP_ACP_LevelMax",
    "COPP_ACP_LevelMin",
    "COPP_ACP_Protection_Level",
    "COPP_Activate",
    "COPP_AeroGlassOff",
    "COPP_AspectRatio_EN300294_Box14by9Center",
    "COPP_AspectRatio_EN300294_Box14by9Top",
    "COPP_AspectRatio_EN300294_Box16by9Center",
    "COPP_AspectRatio_EN300294_Box16by9Top",
    "COPP_AspectRatio_EN300294_BoxGT16by9Center",
    "COPP_AspectRatio_EN300294_FullFormat16by9Anamorphic",
    "COPP_AspectRatio_EN300294_FullFormat4by3",
    "COPP_AspectRatio_EN300294_FullFormat4by3ProtectedCenter",
    "COPP_AspectRatio_ForceDWORD",
    "COPP_BadCertificate",
    "COPP_BadDriver",
    "COPP_BusType",
    "COPP_BusType_AGP",
    "COPP_BusType_ForceDWORD",
    "COPP_BusType_Integrated",
    "COPP_BusType_PCI",
    "COPP_BusType_PCIExpress",
    "COPP_BusType_PCIX",
    "COPP_BusType_Unknown",
    "COPP_CGMSA_CopyFreely",
    "COPP_CGMSA_CopyNever",
    "COPP_CGMSA_CopyNoMore",
    "COPP_CGMSA_CopyOneGeneration",
    "COPP_CGMSA_Disabled",
    "COPP_CGMSA_ForceDWORD",
    "COPP_CGMSA_LevelMax",
    "COPP_CGMSA_LevelMin",
    "COPP_CGMSA_Protection_Level",
    "COPP_CGMSA_RedistributionControlRequired",
    "COPP_ConnectorType",
    "COPP_ConnectorType_ComponentVideo",
    "COPP_ConnectorType_CompositeVideo",
    "COPP_ConnectorType_DVI",
    "COPP_ConnectorType_D_JPN",
    "COPP_ConnectorType_ForceDWORD",
    "COPP_ConnectorType_HDMI",
    "COPP_ConnectorType_Internal",
    "COPP_ConnectorType_LVDS",
    "COPP_ConnectorType_SVideo",
    "COPP_ConnectorType_TMDS",
    "COPP_ConnectorType_Unknown",
    "COPP_ConnectorType_VGA",
    "COPP_DefaultProtectionLevel",
    "COPP_DigitalAudioUnprotected",
    "COPP_ForbiddenVideo",
    "COPP_HDCPFlagsReserved",
    "COPP_HDCPRepeater",
    "COPP_HDCP_ForceDWORD",
    "COPP_HDCP_Level0",
    "COPP_HDCP_Level1",
    "COPP_HDCP_LevelMax",
    "COPP_HDCP_LevelMin",
    "COPP_HDCP_Protection_Level",
    "COPP_ImageAspectRatio_EN300294",
    "COPP_ImageAspectRatio_EN300294_Mask",
    "COPP_InvalidBusProtection",
    "COPP_LinkLost",
    "COPP_NoCardHDCPSupport",
    "COPP_NoMonitorHDCPSupport",
    "COPP_NoProtectionLevelAvailable",
    "COPP_ProtectionStandard_ARIBTRB15_1125i",
    "COPP_ProtectionStandard_ARIBTRB15_525i",
    "COPP_ProtectionStandard_ARIBTRB15_525p",
    "COPP_ProtectionStandard_ARIBTRB15_750p",
    "COPP_ProtectionStandard_CEA805A_TypeA_1125i",
    "COPP_ProtectionStandard_CEA805A_TypeA_525p",
    "COPP_ProtectionStandard_CEA805A_TypeA_750p",
    "COPP_ProtectionStandard_CEA805A_TypeB_1125i",
    "COPP_ProtectionStandard_CEA805A_TypeB_525p",
    "COPP_ProtectionStandard_CEA805A_TypeB_750p",
    "COPP_ProtectionStandard_EIA608B_525",
    "COPP_ProtectionStandard_EN300294_625i",
    "COPP_ProtectionStandard_IEC61880_2_525i",
    "COPP_ProtectionStandard_IEC61880_525i",
    "COPP_ProtectionStandard_IEC62375_625p",
    "COPP_ProtectionStandard_Mask",
    "COPP_ProtectionStandard_None",
    "COPP_ProtectionStandard_Reserved",
    "COPP_ProtectionStandard_Unknown",
    "COPP_RenegotiationRequired",
    "COPP_RogueApp",
    "COPP_StatusFlags",
    "COPP_StatusFlagsReserved",
    "COPP_StatusHDCPFlags",
    "COPP_StatusNormal",
    "COPP_TVProtectionStandard",
    "COPP_Unknown",
    "CPEVENT_BITSHIFT_COPP",
    "CPEVENT_BITSHIFT_DOWNRES",
    "CPEVENT_BITSHIFT_LICENSE",
    "CPEVENT_BITSHIFT_NO_PLAYREADY",
    "CPEVENT_BITSHIFT_PENDING_CERTIFICATE",
    "CPEVENT_BITSHIFT_RATINGS",
    "CPEVENT_BITSHIFT_ROLLBACK",
    "CPEVENT_BITSHIFT_SAC",
    "CPEVENT_BITSHIFT_STUBLIB",
    "CPEVENT_BITSHIFT_UNTRUSTEDGRAPH",
    "CPEVENT_COPP",
    "CPEVENT_DOWNRES",
    "CPEVENT_LICENSE",
    "CPEVENT_NONE",
    "CPEVENT_PROTECTWINDOWED",
    "CPEVENT_RATINGS",
    "CPEVENT_ROLLBACK",
    "CPEVENT_SAC",
    "CPEVENT_STUBLIB",
    "CPEVENT_UNTRUSTEDGRAPH",
    "CPEventBitShift",
    "CPEvents",
    "CPRecordingStatus",
    "CRID_LOCATION",
    "CRID_LOCATION_DVB_RESERVED1",
    "CRID_LOCATION_DVB_RESERVED2",
    "CRID_LOCATION_IN_CIT",
    "CRID_LOCATION_IN_DESCRIPTOR",
    "CROSSBAR_DEFAULT_FLAGS",
    "CXDSData",
    "CameraControlFlags",
    "CameraControlProperty",
    "CameraControl_Exposure",
    "CameraControl_Flags_Auto",
    "CameraControl_Flags_Manual",
    "CameraControl_Focus",
    "CameraControl_Iris",
    "CameraControl_Pan",
    "CameraControl_Roll",
    "CameraControl_Tilt",
    "CameraControl_Zoom",
    "ChannelChangeInfo",
    "ChannelChangeSpanningEvent_End",
    "ChannelChangeSpanningEvent_Start",
    "ChannelChangeSpanningEvent_State",
    "ChannelIDTuneRequest",
    "ChannelIDTuningSpace",
    "ChannelInfo",
    "ChannelTuneRequest",
    "ChannelType",
    "ChannelTypeInfo",
    "ChannelType_ChannelTypeAudio",
    "ChannelType_ChannelTypeCaptions",
    "ChannelType_ChannelTypeData",
    "ChannelType_ChannelTypeNone",
    "ChannelType_ChannelTypeOther",
    "ChannelType_ChannelTypeSubtitles",
    "ChannelType_ChannelTypeSuperimpose",
    "ChannelType_ChannelTypeText",
    "ChannelType_ChannelTypeVideo",
    "Component",
    "ComponentCategory",
    "ComponentCategory_CATEGORY_COUNT",
    "ComponentCategory_CategoryAudio",
    "ComponentCategory_CategoryCaptions",
    "ComponentCategory_CategoryData",
    "ComponentCategory_CategoryNotSet",
    "ComponentCategory_CategoryOther",
    "ComponentCategory_CategorySubtitles",
    "ComponentCategory_CategorySuperimpose",
    "ComponentCategory_CategoryText",
    "ComponentCategory_CategoryVideo",
    "ComponentStatus",
    "ComponentStatus_StatusActive",
    "ComponentStatus_StatusInactive",
    "ComponentStatus_StatusUnavailable",
    "ComponentType",
    "ComponentTypes",
    "Components",
    "CompressionCaps",
    "CompressionCaps_CanBFrame",
    "CompressionCaps_CanCrunch",
    "CompressionCaps_CanKeyFrame",
    "CompressionCaps_CanQuality",
    "CompressionCaps_CanWindow",
    "CreatePropBagOnRegKey",
    "DDSFF_FLAGS",
    "DDSFF_PROGRESSIVERENDER",
    "DECIMATION_DEFAULT",
    "DECIMATION_LEGACY",
    "DECIMATION_USAGE",
    "DECIMATION_USE_DECODER_ONLY",
    "DECIMATION_USE_OVERLAY_ONLY",
    "DECIMATION_USE_VIDEOPORT_ONLY",
    "DECODER_CAP_NOTSUPPORTED",
    "DECODER_CAP_SUPPORTED",
    "DEF_MODE_PROFILE",
    "DEF_MODE_STREAMS",
    "DESC_LINKAGE_CA_REPLACEMENT",
    "DESC_LINKAGE_COMPLETE_NET_BOUQUET_SI",
    "DESC_LINKAGE_DATA",
    "DESC_LINKAGE_EPG",
    "DESC_LINKAGE_INFORMATION",
    "DESC_LINKAGE_REPLACEMENT",
    "DESC_LINKAGE_RESERVED0",
    "DESC_LINKAGE_RESERVED1",
    "DESC_LINKAGE_RESERVED2",
    "DESC_LINKAGE_TYPE",
    "DESC_LINKAGE_USER",
    "DIGITAL_CABLE_NETWORK_TYPE",
    "DIRECT_TV_SATELLITE_TV_NETWORK_TYPE",
    "DISPID_CHTUNER_ACTR_MINOR_CHANNEL",
    "DISPID_CHTUNER_ATVAC_CHANNEL",
    "DISPID_CHTUNER_ATVDC_CONTENT",
    "DISPID_CHTUNER_ATVDC_SYSTEM",
    "DISPID_CHTUNER_CIDTR_CHANNELID",
    "DISPID_CHTUNER_CTR_CHANNEL",
    "DISPID_CHTUNER_DCTR_MAJOR_CHANNEL",
    "DISPID_CHTUNER_DCTR_SRCID",
    "DISPID_DVBTUNER_DVBC_ATTRIBUTESVALID",
    "DISPID_DVBTUNER_DVBC_COMPONENTTYPE",
    "DISPID_DVBTUNER_DVBC_PID",
    "DISPID_DVBTUNER_DVBC_TAG",
    "DISPID_DVBTUNER_ONID",
    "DISPID_DVBTUNER_SID",
    "DISPID_DVBTUNER_TSID",
    "DISPID_MP2TUNERFACTORY_CREATETUNEREQUEST",
    "DISPID_MP2TUNER_PROGNO",
    "DISPID_MP2TUNER_TSID",
    "DISPID_TUNER",
    "DISPID_TUNER_ATSCCT_FLAGS",
    "DISPID_TUNER_CT_CATEGORY",
    "DISPID_TUNER_CT_CLONE",
    "DISPID_TUNER_CT_MEDIAFORMATTYPE",
    "DISPID_TUNER_CT_MEDIAMAJORTYPE",
    "DISPID_TUNER_CT_MEDIASUBTYPE",
    "DISPID_TUNER_CT_MEDIATYPE",
    "DISPID_TUNER_CT__MEDIAFORMATTYPE",
    "DISPID_TUNER_CT__MEDIAMAJORTYPE",
    "DISPID_TUNER_CT__MEDIASUBTYPE",
    "DISPID_TUNER_C_ANALOG_AUDIO",
    "DISPID_TUNER_C_CLONE",
    "DISPID_TUNER_C_DESCRIPTION",
    "DISPID_TUNER_C_LANGID",
    "DISPID_TUNER_C_MP2_PCRPID",
    "DISPID_TUNER_C_MP2_PID",
    "DISPID_TUNER_C_MP2_PROGNO",
    "DISPID_TUNER_C_STATUS",
    "DISPID_TUNER_C_TYPE",
    "DISPID_TUNER_LCT_LANGID",
    "DISPID_TUNER_L_ANALOG_STANDARD",
    "DISPID_TUNER_L_ATSC_MP2_PROGNO",
    "DISPID_TUNER_L_ATSC_PHYS_CHANNEL",
    "DISPID_TUNER_L_ATSC_TSID",
    "DISPID_TUNER_L_CARRFREQ",
    "DISPID_TUNER_L_CLONE",
    "DISPID_TUNER_L_DTV_O_MAJOR_CHANNEL",
    "DISPID_TUNER_L_DVBS2_DISEQ_LNB_SOURCE",
    "DISPID_TUNER_L_DVBS2_PILOT",
    "DISPID_TUNER_L_DVBS2_ROLLOFF",
    "DISPID_TUNER_L_DVBS_AZIMUTH",
    "DISPID_TUNER_L_DVBS_ELEVATION",
    "DISPID_TUNER_L_DVBS_ORBITAL",
    "DISPID_TUNER_L_DVBS_POLARISATION",
    "DISPID_TUNER_L_DVBS_WEST",
    "DISPID_TUNER_L_DVBT2_PHYSICALLAYERPIPEID",
    "DISPID_TUNER_L_DVBT_BANDWIDTH",
    "DISPID_TUNER_L_DVBT_GUARDINTERVAL",
    "DISPID_TUNER_L_DVBT_HALPHA",
    "DISPID_TUNER_L_DVBT_INUSE",
    "DISPID_TUNER_L_DVBT_LPINNERFECMETHOD",
    "DISPID_TUNER_L_DVBT_LPINNERFECRATE",
    "DISPID_TUNER_L_DVBT_TRANSMISSIONMODE",
    "DISPID_TUNER_L_INNERFECMETHOD",
    "DISPID_TUNER_L_INNERFECRATE",
    "DISPID_TUNER_L_MOD",
    "DISPID_TUNER_L_OUTERFECMETHOD",
    "DISPID_TUNER_L_OUTERFECRATE",
    "DISPID_TUNER_L_SYMRATE",
    "DISPID_TUNER_MP2CT_TYPE",
    "DISPID_TUNER_TR_CLONE",
    "DISPID_TUNER_TR_COMPONENTS",
    "DISPID_TUNER_TR_LOCATOR",
    "DISPID_TUNER_TR_TUNINGSPACE",
    "DISPID_TUNER_TS_AR_COUNTRYCODE",
    "DISPID_TUNER_TS_AR_MAXFREQUENCY",
    "DISPID_TUNER_TS_AR_MINFREQUENCY",
    "DISPID_TUNER_TS_AR_STEP",
    "DISPID_TUNER_TS_ATSC_MAXMINORCHANNEL",
    "DISPID_TUNER_TS_ATSC_MAXPHYSCHANNEL",
    "DISPID_TUNER_TS_ATSC_MINMINORCHANNEL",
    "DISPID_TUNER_TS_ATSC_MINPHYSCHANNEL",
    "DISPID_TUNER_TS_ATV_COUNTRYCODE",
    "DISPID_TUNER_TS_ATV_INPUTTYPE",
    "DISPID_TUNER_TS_ATV_MAXCHANNEL",
    "DISPID_TUNER_TS_ATV_MINCHANNEL",
    "DISPID_TUNER_TS_AUX_COUNTRYCODE",
    "DISPID_TUNER_TS_CLONE",
    "DISPID_TUNER_TS_CLSID",
    "DISPID_TUNER_TS_CREATETUNEREQUEST",
    "DISPID_TUNER_TS_DC_MAXMAJORCHANNEL",
    "DISPID_TUNER_TS_DC_MAXSOURCEID",
    "DISPID_TUNER_TS_DC_MINMAJORCHANNEL",
    "DISPID_TUNER_TS_DC_MINSOURCEID",
    "DISPID_TUNER_TS_DEFAULTPREFERREDCOMPONENTTYPES",
    "DISPID_TUNER_TS_DEFLOCATOR",
    "DISPID_TUNER_TS_DVB2_NETWORK_ID",
    "DISPID_TUNER_TS_DVBS2_HI_OSC_FREQ_OVERRIDE",
    "DISPID_TUNER_TS_DVBS2_LNB_SWITCH_FREQ_OVERRIDE",
    "DISPID_TUNER_TS_DVBS2_LOW_OSC_FREQ_OVERRIDE",
    "DISPID_TUNER_TS_DVBS2_SPECTRAL_INVERSION_OVERRIDE",
    "DISPID_TUNER_TS_DVBS_HI_OSC_FREQ",
    "DISPID_TUNER_TS_DVBS_INPUT_RANGE",
    "DISPID_TUNER_TS_DVBS_LNB_SWITCH_FREQ",
    "DISPID_TUNER_TS_DVBS_LOW_OSC_FREQ",
    "DISPID_TUNER_TS_DVBS_SPECTRAL_INVERSION",
    "DISPID_TUNER_TS_DVB_SYSTEMTYPE",
    "DISPID_TUNER_TS_ENUMCATEGORYGUIDS",
    "DISPID_TUNER_TS_ENUMDEVICEMONIKERS",
    "DISPID_TUNER_TS_FREQMAP",
    "DISPID_TUNER_TS_FRIENDLYNAME",
    "DISPID_TUNER_TS_NETWORKTYPE",
    "DISPID_TUNER_TS_UNIQUENAME",
    "DISPID_TUNER_TS__NETWORKTYPE",
    "DISPLAY_16x9",
    "DISPLAY_4x3_LETTERBOX_PREFERRED",
    "DISPLAY_4x3_PANSCAN_PREFERRED",
    "DISPLAY_CONTENT_DEFAULT",
    "DOWNRES_Always",
    "DOWNRES_InWindowOnly",
    "DOWNRES_Undefined",
    "DSATTRIB_BadSampleInfo",
    "DSATTRIB_WMDRMProtectionInfo",
    "DSHOW_STREAM_DESC",
    "DSMCC_ELEMENT",
    "DSMCC_FILTER_OPTIONS",
    "DSMCC_SECTION",
    "DTFilter",
    "DTV_CardStatus_Error",
    "DTV_CardStatus_FirmwareDownload",
    "DTV_CardStatus_Inserted",
    "DTV_CardStatus_Removed",
    "DTV_Entitlement_CanDecrypt",
    "DTV_Entitlement_NotEntitled",
    "DTV_Entitlement_TechnicalFailure",
    "DTV_MMIMessage_Close",
    "DTV_MMIMessage_Open",
    "DVBCLocator",
    "DVBSLocator",
    "DVBSTuningSpace",
    "DVBS_SCAN_TABLE_MAX_SIZE",
    "DVBScramblingControlSpanningEvent",
    "DVBSystemType",
    "DVBTLocator",
    "DVBTLocator2",
    "DVBTuneRequest",
    "DVBTuningSpace",
    "DVB_BAT_PID",
    "DVB_BAT_TID",
    "DVB_CABLE_TV_NETWORK_TYPE",
    "DVB_Cable",
    "DVB_DIT_PID",
    "DVB_DIT_TID",
    "DVB_EIT_ACTUAL_TID",
    "DVB_EIT_FILTER_OPTIONS",
    "DVB_EIT_OTHER_TID",
    "DVB_EIT_PID",
    "DVB_NIT_ACTUAL_TID",
    "DVB_NIT_OTHER_TID",
    "DVB_NIT_PID",
    "DVB_RST_PID",
    "DVB_RST_TID",
    "DVB_SATELLITE_TV_NETWORK_TYPE",
    "DVB_SDT_ACTUAL_TID",
    "DVB_SDT_OTHER_TID",
    "DVB_SDT_PID",
    "DVB_SIT_PID",
    "DVB_SIT_TID",
    "DVB_STRCONV_MODE",
    "DVB_ST_PID_16",
    "DVB_ST_PID_17",
    "DVB_ST_PID_18",
    "DVB_ST_PID_19",
    "DVB_ST_PID_20",
    "DVB_ST_TID",
    "DVB_Satellite",
    "DVB_TDT_PID",
    "DVB_TDT_TID",
    "DVB_TERRESTRIAL_TV_NETWORK_TYPE",
    "DVB_TOT_PID",
    "DVB_TOT_TID",
    "DVB_Terrestrial",
    "DVDECODERRESOLUTION_180x120",
    "DVDECODERRESOLUTION_360x240",
    "DVDECODERRESOLUTION_720x480",
    "DVDECODERRESOLUTION_88x60",
    "DVDFilterState",
    "DVDMenuIDConstants",
    "DVDSPExt",
    "DVDTextStringType",
    "DVD_ATR",
    "DVD_AUDIO_APPMODE",
    "DVD_AUDIO_CAPS_AC3",
    "DVD_AUDIO_CAPS_DTS",
    "DVD_AUDIO_CAPS_LPCM",
    "DVD_AUDIO_CAPS_MPEG2",
    "DVD_AUDIO_CAPS_SDDS",
    "DVD_AUDIO_FORMAT",
    "DVD_AUDIO_LANG_EXT",
    "DVD_AUD_EXT_Captions",
    "DVD_AUD_EXT_DirectorComments1",
    "DVD_AUD_EXT_DirectorComments2",
    "DVD_AUD_EXT_NotSpecified",
    "DVD_AUD_EXT_VisuallyImpaired",
    "DVD_AppMode_Karaoke",
    "DVD_AppMode_Not_Specified",
    "DVD_AppMode_Other",
    "DVD_Assignment_LR",
    "DVD_Assignment_LR1",
    "DVD_Assignment_LR12",
    "DVD_Assignment_LRM",
    "DVD_Assignment_LRM1",
    "DVD_Assignment_LRM12",
    "DVD_Assignment_reserved0",
    "DVD_Assignment_reserved1",
    "DVD_AudioAttributes",
    "DVD_AudioDuringFFwdRew",
    "DVD_AudioFormat_AC3",
    "DVD_AudioFormat_DTS",
    "DVD_AudioFormat_LPCM",
    "DVD_AudioFormat_MPEG1",
    "DVD_AudioFormat_MPEG1_DRC",
    "DVD_AudioFormat_MPEG2",
    "DVD_AudioFormat_MPEG2_DRC",
    "DVD_AudioFormat_Other",
    "DVD_AudioFormat_SDDS",
    "DVD_AudioMode_Karaoke",
    "DVD_AudioMode_None",
    "DVD_AudioMode_Other",
    "DVD_AudioMode_Surround",
    "DVD_CMD_FLAGS",
    "DVD_CMD_FLAG_Block",
    "DVD_CMD_FLAG_EndAfterRendered",
    "DVD_CMD_FLAG_Flush",
    "DVD_CMD_FLAG_None",
    "DVD_CMD_FLAG_SendEvents",
    "DVD_CMD_FLAG_StartWhenRendered",
    "DVD_CacheSizeInMB",
    "DVD_Channel_Audio",
    "DVD_CharSet_ISO646",
    "DVD_CharSet_ISO8859_1",
    "DVD_CharSet_JIS_Roman_Kanji",
    "DVD_CharSet_ShiftJIS_Kanji_Roman_Katakana",
    "DVD_CharSet_Unicode",
    "DVD_DECODER_CAPS",
    "DVD_DEFAULT_AUDIO_STREAM",
    "DVD_DIR_BACKWARD",
    "DVD_DIR_FORWARD",
    "DVD_DISC_SIDE",
    "DVD_DOMAIN",
    "DVD_DOMAIN_FirstPlay",
    "DVD_DOMAIN_Stop",
    "DVD_DOMAIN_Title",
    "DVD_DOMAIN_VideoManagerMenu",
    "DVD_DOMAIN_VideoTitleSetMenu",
    "DVD_DisableStillThrottle",
    "DVD_ERROR",
    "DVD_ERROR_CopyProtectFail",
    "DVD_ERROR_CopyProtectOutputFail",
    "DVD_ERROR_CopyProtectOutputNotSupported",
    "DVD_ERROR_IncompatibleDiscAndDecoderRegions",
    "DVD_ERROR_IncompatibleSystemAndDecoderRegions",
    "DVD_ERROR_InvalidDVD1_0Disc",
    "DVD_ERROR_InvalidDiscRegion",
    "DVD_ERROR_LowParentalLevel",
    "DVD_ERROR_MacrovisionFail",
    "DVD_ERROR_Unexpected",
    "DVD_EnableCC",
    "DVD_EnableESOutput",
    "DVD_EnableExtendedCopyProtectErrors",
    "DVD_EnableLoggingEvents",
    "DVD_EnableNonblockingAPIs",
    "DVD_EnablePortableBookmarks",
    "DVD_EnableStreaming",
    "DVD_EnableTitleLength",
    "DVD_FPS_25",
    "DVD_FPS_30NonDrop",
    "DVD_FRAMERATE",
    "DVD_General_Comments",
    "DVD_General_Name",
    "DVD_HMSF_TIMECODE",
    "DVD_HMSF_TimeCodeEvents",
    "DVD_IncreaseOutputControl",
    "DVD_KARAOKE_ASSIGNMENT",
    "DVD_KARAOKE_CONTENTS",
    "DVD_KARAOKE_DOWNMIX",
    "DVD_KaraokeAttributes",
    "DVD_Karaoke_GuideMelody1",
    "DVD_Karaoke_GuideMelody2",
    "DVD_Karaoke_GuideMelodyA",
    "DVD_Karaoke_GuideMelodyB",
    "DVD_Karaoke_GuideVocal1",
    "DVD_Karaoke_GuideVocal2",
    "DVD_Karaoke_SoundEffectA",
    "DVD_Karaoke_SoundEffectB",
    "DVD_MENU_Angle",
    "DVD_MENU_Audio",
    "DVD_MENU_Chapter",
    "DVD_MENU_ID",
    "DVD_MENU_Root",
    "DVD_MENU_Subpicture",
    "DVD_MENU_Title",
    "DVD_MUA_Coeff",
    "DVD_MUA_MixingInfo",
    "DVD_MaxReadBurstInKB",
    "DVD_MenuAttributes",
    "DVD_Mix_0to0",
    "DVD_Mix_0to1",
    "DVD_Mix_1to0",
    "DVD_Mix_1to1",
    "DVD_Mix_2to0",
    "DVD_Mix_2to1",
    "DVD_Mix_3to0",
    "DVD_Mix_3to1",
    "DVD_Mix_4to0",
    "DVD_Mix_4to1",
    "DVD_Mix_Lto0",
    "DVD_Mix_Lto1",
    "DVD_Mix_Rto0",
    "DVD_Mix_Rto1",
    "DVD_MultichannelAudioAttributes",
    "DVD_NavCmdType",
    "DVD_NavCmdType_Button",
    "DVD_NavCmdType_Cell",
    "DVD_NavCmdType_Post",
    "DVD_NavCmdType_Pre",
    "DVD_NotifyParentalLevelChange",
    "DVD_NotifyPositionChange",
    "DVD_OPTION_FLAG",
    "DVD_Other_Cut",
    "DVD_Other_Scene",
    "DVD_Other_Take",
    "DVD_PARENTAL_LEVEL",
    "DVD_PARENTAL_LEVEL_1",
    "DVD_PARENTAL_LEVEL_2",
    "DVD_PARENTAL_LEVEL_3",
    "DVD_PARENTAL_LEVEL_4",
    "DVD_PARENTAL_LEVEL_5",
    "DVD_PARENTAL_LEVEL_6",
    "DVD_PARENTAL_LEVEL_7",
    "DVD_PARENTAL_LEVEL_8",
    "DVD_PB_STOPPED",
    "DVD_PB_STOPPED_CopyProtectFailure",
    "DVD_PB_STOPPED_CopyProtectOutputFailure",
    "DVD_PB_STOPPED_CopyProtectOutputNotSupported",
    "DVD_PB_STOPPED_DiscEjected",
    "DVD_PB_STOPPED_DiscReadError",
    "DVD_PB_STOPPED_IllegalNavCommand",
    "DVD_PB_STOPPED_MacrovisionFailure",
    "DVD_PB_STOPPED_NoBranch",
    "DVD_PB_STOPPED_NoFirstPlayDomain",
    "DVD_PB_STOPPED_Other",
    "DVD_PB_STOPPED_ParentalFailure",
    "DVD_PB_STOPPED_PlayChapterAutoStop",
    "DVD_PB_STOPPED_PlayPeriodAutoStop",
    "DVD_PB_STOPPED_RegionFailure",
    "DVD_PB_STOPPED_Reset",
    "DVD_PB_STOPPED_StopCommand",
    "DVD_PLAYBACK_LOCATION",
    "DVD_PLAYBACK_LOCATION2",
    "DVD_PLAY_DIRECTION",
    "DVD_PREFERRED_DISPLAY_MODE",
    "DVD_REGION",
    "DVD_RELATIVE_BUTTON",
    "DVD_ReadBurstPeriodInMS",
    "DVD_Relative_Left",
    "DVD_Relative_Lower",
    "DVD_Relative_Right",
    "DVD_Relative_Upper",
    "DVD_ResetOnStop",
    "DVD_RestartDisc",
    "DVD_SIDE_A",
    "DVD_SIDE_B",
    "DVD_SPCoding_Extended",
    "DVD_SPCoding_Other",
    "DVD_SPCoding_RunLength",
    "DVD_SPType_Language",
    "DVD_SPType_NotSpecified",
    "DVD_SPType_Other",
    "DVD_SP_EXT_CC_Big",
    "DVD_SP_EXT_CC_Children",
    "DVD_SP_EXT_CC_Normal",
    "DVD_SP_EXT_Caption_Big",
    "DVD_SP_EXT_Caption_Children",
    "DVD_SP_EXT_Caption_Normal",
    "DVD_SP_EXT_DirectorComments_Big",
    "DVD_SP_EXT_DirectorComments_Children",
    "DVD_SP_EXT_DirectorComments_Normal",
    "DVD_SP_EXT_Forced",
    "DVD_SP_EXT_NotSpecified",
    "DVD_STREAM_DATA_CURRENT",
    "DVD_STREAM_DATA_VMGM",
    "DVD_STREAM_DATA_VTSM",
    "DVD_SUBPICTURE_CODING",
    "DVD_SUBPICTURE_LANG_EXT",
    "DVD_SUBPICTURE_TYPE",
    "DVD_Stream_Angle",
    "DVD_Stream_Audio",
    "DVD_Stream_Subpicture",
    "DVD_Struct_Cell",
    "DVD_Struct_ParentalID",
    "DVD_Struct_PartOfTitle",
    "DVD_Struct_Title",
    "DVD_Struct_Volume",
    "DVD_SubpictureAttributes",
    "DVD_TC_FLAG_25fps",
    "DVD_TC_FLAG_30fps",
    "DVD_TC_FLAG_DropFrame",
    "DVD_TC_FLAG_Interpolated",
    "DVD_TIMECODE",
    "DVD_TIMECODE_FLAGS",
    "DVD_TITLE_APPMODE",
    "DVD_TITLE_MENU",
    "DVD_TextCharSet",
    "DVD_TextStringType",
    "DVD_TitleAttributes",
    "DVD_Title_Album",
    "DVD_Title_Movie",
    "DVD_Title_Orig_Album",
    "DVD_Title_Orig_Movie",
    "DVD_Title_Orig_Other",
    "DVD_Title_Orig_Series",
    "DVD_Title_Orig_Song",
    "DVD_Title_Orig_Video",
    "DVD_Title_Other",
    "DVD_Title_Series",
    "DVD_Title_Song",
    "DVD_Title_Sub_Album",
    "DVD_Title_Sub_Movie",
    "DVD_Title_Sub_Other",
    "DVD_Title_Sub_Series",
    "DVD_Title_Sub_Song",
    "DVD_Title_Sub_Video",
    "DVD_Title_Video",
    "DVD_VIDEO_COMPRESSION",
    "DVD_VideoAttributes",
    "DVD_VideoCompression_MPEG1",
    "DVD_VideoCompression_MPEG2",
    "DVD_VideoCompression_Other",
    "DVD_WARNING",
    "DVD_WARNING_FormatNotSupported",
    "DVD_WARNING_IllegalNavCommand",
    "DVD_WARNING_InvalidDVD1_0Disc",
    "DVD_WARNING_Open",
    "DVD_WARNING_Read",
    "DVD_WARNING_Seek",
    "DVENCODERFORMAT_DVHD",
    "DVENCODERFORMAT_DVSD",
    "DVENCODERFORMAT_DVSL",
    "DVENCODERRESOLUTION_180x120",
    "DVENCODERRESOLUTION_360x240",
    "DVENCODERRESOLUTION_720x480",
    "DVENCODERRESOLUTION_88x60",
    "DVENCODERVIDEOFORMAT_NTSC",
    "DVENCODERVIDEOFORMAT_PAL",
    "DVINFO",
    "DVRESOLUTION_DC",
    "DVRESOLUTION_FULL",
    "DVRESOLUTION_HALF",
    "DVRESOLUTION_QUARTER",
    "DVR_STREAM_DESC",
    "DWORD_ALLPARAMS",
    "DXVA2SW_CALLBACKS",
    "DXVA2TraceVideoProcessBltData",
    "DXVA2Trace_Control",
    "DXVA2Trace_DecodeDevBeginFrame",
    "DXVA2Trace_DecodeDevBeginFrameData",
    "DXVA2Trace_DecodeDevCreated",
    "DXVA2Trace_DecodeDevCreatedData",
    "DXVA2Trace_DecodeDevDestroyed",
    "DXVA2Trace_DecodeDevEndFrame",
    "DXVA2Trace_DecodeDevExecute",
    "DXVA2Trace_DecodeDevGetBuffer",
    "DXVA2Trace_DecodeDevGetBufferData",
    "DXVA2Trace_DecodeDeviceData",
    "DXVA2Trace_VideoProcessBlt",
    "DXVA2Trace_VideoProcessDevCreated",
    "DXVA2Trace_VideoProcessDevCreatedData",
    "DXVA2Trace_VideoProcessDevDestroyed",
    "DXVA2Trace_VideoProcessDeviceData",
    "DXVA2_DestinationFlagMask",
    "DXVA2_DestinationFlag_Alpha_Changed",
    "DXVA2_DestinationFlag_Background_Changed",
    "DXVA2_DestinationFlag_ColorData_Changed",
    "DXVA2_DestinationFlag_RFF",
    "DXVA2_DestinationFlag_RFF_TFF_Present",
    "DXVA2_DestinationFlag_TFF",
    "DXVA2_DestinationFlag_TargetRect_Changed",
    "DXVA2_DestinationFlags",
    "DXVA2_SampleFlag_ColorData_Changed",
    "DXVA2_SampleFlag_DstRect_Changed",
    "DXVA2_SampleFlag_Palette_Changed",
    "DXVA2_SampleFlag_PlanarAlpha_Changed",
    "DXVA2_SampleFlag_RFF",
    "DXVA2_SampleFlag_RFF_TFF_Present",
    "DXVA2_SampleFlag_SrcRect_Changed",
    "DXVA2_SampleFlag_TFF",
    "DXVA2_SampleFlags",
    "DXVA2_SampleFlagsMask",
    "DXVA2_VIDEOPROCESSBLT",
    "DXVA2_VIDEOSAMPLE",
    "DXVA_ALPHA_BLEND_COMBINATION_BUFFER",
    "DXVA_ALPHA_BLEND_COMBINATION_FUNCTION",
    "DXVA_ALPHA_BLEND_DATA_LOAD_FUNCTION",
    "DXVA_AYUV_BUFFER",
    "DXVA_BIDIRECTIONAL_AVERAGING_H263_TRUNC",
    "DXVA_BIDIRECTIONAL_AVERAGING_MPEG2_ROUND",
    "DXVA_BITSTREAM_CONCEALMENT_METHOD_BACKWARD",
    "DXVA_BITSTREAM_CONCEALMENT_METHOD_FORWARD",
    "DXVA_BITSTREAM_CONCEALMENT_METHOD_INTRA",
    "DXVA_BITSTREAM_CONCEALMENT_METHOD_UNSPECIFIED",
    "DXVA_BITSTREAM_CONCEALMENT_NEED_LIKELY",
    "DXVA_BITSTREAM_CONCEALMENT_NEED_MILD",
    "DXVA_BITSTREAM_CONCEALMENT_NEED_SEVERE",
    "DXVA_BITSTREAM_CONCEALMENT_NEED_UNLIKELY",
    "DXVA_BITSTREAM_DATA_BUFFER",
    "DXVA_CHROMA_FORMAT_420",
    "DXVA_CHROMA_FORMAT_422",
    "DXVA_CHROMA_FORMAT_444",
    "DXVA_COMPBUFFER_TYPE_THAT_IS_NOT_USED",
    "DXVA_CONFIG_BLEND_TYPE_BACK_HARDWARE",
    "DXVA_CONFIG_BLEND_TYPE_FRONT_BUFFER",
    "DXVA_CONFIG_DATA_TYPE_AI44",
    "DXVA_CONFIG_DATA_TYPE_AYUV",
    "DXVA_CONFIG_DATA_TYPE_DPXD",
    "DXVA_CONFIG_DATA_TYPE_IA44",
    "DXVA_COPPCommandFnCode",
    "DXVA_COPPDevice",
    "DXVA_COPPGetCertificateLengthFnCode",
    "DXVA_COPPKeyExchangeFnCode",
    "DXVA_COPPQueryBusData",
    "DXVA_COPPQueryConnectorType",
    "DXVA_COPPQueryDisplayData",
    "DXVA_COPPQueryGlobalProtectionLevel",
    "DXVA_COPPQueryHDCPKeyData",
    "DXVA_COPPQueryLocalProtectionLevel",
    "DXVA_COPPQueryProtectionType",
    "DXVA_COPPQuerySignaling",
    "DXVA_COPPQueryStatusFnCode",
    "DXVA_COPPSequenceStartFnCode",
    "DXVA_COPPSetProtectionLevel",
    "DXVA_COPPSetProtectionLevelCmdData",
    "DXVA_COPPSetSignaling",
    "DXVA_COPPSetSignalingCmdData",
    "DXVA_COPPStatusData",
    "DXVA_COPPStatusDisplayData",
    "DXVA_COPPStatusHDCPKeyData",
    "DXVA_COPPStatusSignalingCmdData",
    "DXVA_DCCMD_SURFACE_BUFFER",
    "DXVA_DEBLOCKING_CONTROL_BUFFER",
    "DXVA_DEBLOCKING_FILTER_FUNCTION",
    "DXVA_DPXD_SURFACE_BUFFER",
    "DXVA_DeinterlaceBltExFnCode",
    "DXVA_DeinterlaceBltFnCode",
    "DXVA_DeinterlaceBobDevice",
    "DXVA_DeinterlaceContainerDevice",
    "DXVA_DeinterlaceQueryAvailableModesFnCode",
    "DXVA_DeinterlaceQueryModeCapsFnCode",
    "DXVA_ENCRYPTPROTOCOLFUNCFLAG_ACCEL",
    "DXVA_ENCRYPTPROTOCOLFUNCFLAG_HOST",
    "DXVA_EXECUTE_RETURN_DATA_ERROR_MINOR",
    "DXVA_EXECUTE_RETURN_DATA_ERROR_SEVERE",
    "DXVA_EXECUTE_RETURN_DATA_ERROR_SIGNIF",
    "DXVA_EXECUTE_RETURN_OK",
    "DXVA_EXECUTE_RETURN_OTHER_ERROR_SEVERE",
    "DXVA_ExtColorData_ShiftBase",
    "DXVA_FILM_GRAIN_BUFFER",
    "DXVA_FILM_GRAIN_SYNTHESIS_FUNCTION",
    "DXVA_HIGHLIGHT_BUFFER",
    "DXVA_IA44_SURFACE_BUFFER",
    "DXVA_INVERSE_QUANTIZATION_MATRIX_BUFFER",
    "DXVA_MACROBLOCK_CONTROL_BUFFER",
    "DXVA_MOTION_VECTOR_BUFFER",
    "DXVA_MV_PRECISION_AND_CHROMA_RELATION_H261",
    "DXVA_MV_PRECISION_AND_CHROMA_RELATION_H263",
    "DXVA_MV_PRECISION_AND_CHROMA_RELATION_MPEG2",
    "DXVA_ModeAV1_VLD_12bit_Profile2",
    "DXVA_ModeAV1_VLD_12bit_Profile2_420",
    "DXVA_ModeAV1_VLD_Profile0",
    "DXVA_ModeAV1_VLD_Profile1",
    "DXVA_ModeAV1_VLD_Profile2",
    "DXVA_ModeH261_A",
    "DXVA_ModeH261_B",
    "DXVA_ModeH263_A",
    "DXVA_ModeH263_B",
    "DXVA_ModeH263_C",
    "DXVA_ModeH263_D",
    "DXVA_ModeH263_E",
    "DXVA_ModeH263_F",
    "DXVA_ModeH264_A",
    "DXVA_ModeH264_B",
    "DXVA_ModeH264_C",
    "DXVA_ModeH264_D",
    "DXVA_ModeH264_E",
    "DXVA_ModeH264_F",
    "DXVA_ModeH264_VLD_Multiview_NoFGT",
    "DXVA_ModeH264_VLD_Stereo_NoFGT",
    "DXVA_ModeH264_VLD_Stereo_Progressive_NoFGT",
    "DXVA_ModeH264_VLD_WithFMOASO_NoFGT",
    "DXVA_ModeHEVC_VLD_Main",
    "DXVA_ModeHEVC_VLD_Main10",
    "DXVA_ModeMPEG1_A",
    "DXVA_ModeMPEG1_VLD",
    "DXVA_ModeMPEG2_A",
    "DXVA_ModeMPEG2_B",
    "DXVA_ModeMPEG2_C",
    "DXVA_ModeMPEG2_D",
    "DXVA_ModeMPEG2and1_VLD",
    "DXVA_ModeMPEG4pt2_VLD_AdvSimple_GMC",
    "DXVA_ModeMPEG4pt2_VLD_AdvSimple_NoGMC",
    "DXVA_ModeMPEG4pt2_VLD_Simple",
    "DXVA_ModeNone",
    "DXVA_ModeVC1_A",
    "DXVA_ModeVC1_B",
    "DXVA_ModeVC1_C",
    "DXVA_ModeVC1_D",
    "DXVA_ModeVC1_D2010",
    "DXVA_ModeVP8_VLD",
    "DXVA_ModeVP9_VLD_10bit_Profile2",
    "DXVA_ModeVP9_VLD_Profile0",
    "DXVA_ModeWMV8_A",
    "DXVA_ModeWMV8_B",
    "DXVA_ModeWMV9_A",
    "DXVA_ModeWMV9_B",
    "DXVA_ModeWMV9_C",
    "DXVA_NUM_TYPES_COMP_BUFFERS",
    "DXVA_NoEncrypt",
    "DXVA_NumMV_OBMC_off_BinPBwith4MV_off",
    "DXVA_NumMV_OBMC_off_BinPBwith4MV_on",
    "DXVA_NumMV_OBMC_on__BinPB_off",
    "DXVA_NumMV_OBMC_on__BinPB_on",
    "DXVA_PICTURE_DECODE_BUFFER",
    "DXVA_PICTURE_DECODING_FUNCTION",
    "DXVA_PICTURE_RESAMPLE_BUFFER",
    "DXVA_PICTURE_RESAMPLE_FUNCTION",
    "DXVA_PICTURE_STRUCTURE_BOTTOM_FIELD",
    "DXVA_PICTURE_STRUCTURE_FRAME",
    "DXVA_PICTURE_STRUCTURE_TOP_FIELD",
    "DXVA_ProcAmpControlBltFnCode",
    "DXVA_ProcAmpControlDevice",
    "DXVA_ProcAmpControlQueryCapsFnCode",
    "DXVA_ProcAmpControlQueryRangeFnCode",
    "DXVA_QUERYORREPLYFUNCFLAG_ACCEL_LOCK_FALSE_PLUS",
    "DXVA_QUERYORREPLYFUNCFLAG_ACCEL_LOCK_OK_COPY",
    "DXVA_QUERYORREPLYFUNCFLAG_ACCEL_PROBE_FALSE_PLUS",
    "DXVA_QUERYORREPLYFUNCFLAG_ACCEL_PROBE_OK_COPY",
    "DXVA_QUERYORREPLYFUNCFLAG_ACCEL_PROBE_OK_PLUS",
    "DXVA_QUERYORREPLYFUNCFLAG_DECODER_LOCK_QUERY",
    "DXVA_QUERYORREPLYFUNCFLAG_DECODER_PROBE_QUERY",
    "DXVA_READ_BACK_BUFFER",
    "DXVA_RESIDUAL_DIFFERENCE_BUFFER",
    "DXVA_RESTRICTED_MODE_H261_A",
    "DXVA_RESTRICTED_MODE_H261_B",
    "DXVA_RESTRICTED_MODE_H263_A",
    "DXVA_RESTRICTED_MODE_H263_B",
    "DXVA_RESTRICTED_MODE_H263_C",
    "DXVA_RESTRICTED_MODE_H263_D",
    "DXVA_RESTRICTED_MODE_H263_E",
    "DXVA_RESTRICTED_MODE_H263_F",
    "DXVA_RESTRICTED_MODE_H264_A",
    "DXVA_RESTRICTED_MODE_H264_B",
    "DXVA_RESTRICTED_MODE_H264_C",
    "DXVA_RESTRICTED_MODE_H264_D",
    "DXVA_RESTRICTED_MODE_H264_E",
    "DXVA_RESTRICTED_MODE_H264_F",
    "DXVA_RESTRICTED_MODE_H264_IDCT_FGT",
    "DXVA_RESTRICTED_MODE_H264_IDCT_NOFGT",
    "DXVA_RESTRICTED_MODE_H264_MOCOMP_FGT",
    "DXVA_RESTRICTED_MODE_H264_MOCOMP_NOFGT",
    "DXVA_RESTRICTED_MODE_H264_VLD_FGT",
    "DXVA_RESTRICTED_MODE_H264_VLD_MULTIVIEW_NOFGT",
    "DXVA_RESTRICTED_MODE_H264_VLD_NOFGT",
    "DXVA_RESTRICTED_MODE_H264_VLD_STEREO_NOFGT",
    "DXVA_RESTRICTED_MODE_H264_VLD_STEREO_PROGRESSIVE_NOFGT",
    "DXVA_RESTRICTED_MODE_H264_VLD_WITHFMOASO_NOFGT",
    "DXVA_RESTRICTED_MODE_MPEG1_A",
    "DXVA_RESTRICTED_MODE_MPEG1_VLD",
    "DXVA_RESTRICTED_MODE_MPEG2_A",
    "DXVA_RESTRICTED_MODE_MPEG2_B",
    "DXVA_RESTRICTED_MODE_MPEG2_C",
    "DXVA_RESTRICTED_MODE_MPEG2_D",
    "DXVA_RESTRICTED_MODE_MPEG2and1_VLD",
    "DXVA_RESTRICTED_MODE_MPEG4PT2_VLD_ADV_SIMPLE_GMC",
    "DXVA_RESTRICTED_MODE_MPEG4PT2_VLD_ADV_SIMPLE_NOGMC",
    "DXVA_RESTRICTED_MODE_MPEG4PT2_VLD_SIMPLE",
    "DXVA_RESTRICTED_MODE_UNRESTRICTED",
    "DXVA_RESTRICTED_MODE_VC1_A",
    "DXVA_RESTRICTED_MODE_VC1_B",
    "DXVA_RESTRICTED_MODE_VC1_C",
    "DXVA_RESTRICTED_MODE_VC1_D",
    "DXVA_RESTRICTED_MODE_VC1_D2010",
    "DXVA_RESTRICTED_MODE_VC1_IDCT",
    "DXVA_RESTRICTED_MODE_VC1_MOCOMP",
    "DXVA_RESTRICTED_MODE_VC1_POSTPROC",
    "DXVA_RESTRICTED_MODE_VC1_VLD",
    "DXVA_RESTRICTED_MODE_WMV8_A",
    "DXVA_RESTRICTED_MODE_WMV8_B",
    "DXVA_RESTRICTED_MODE_WMV8_MOCOMP",
    "DXVA_RESTRICTED_MODE_WMV8_POSTPROC",
    "DXVA_RESTRICTED_MODE_WMV9_A",
    "DXVA_RESTRICTED_MODE_WMV9_B",
    "DXVA_RESTRICTED_MODE_WMV9_C",
    "DXVA_RESTRICTED_MODE_WMV9_IDCT",
    "DXVA_RESTRICTED_MODE_WMV9_MOCOMP",
    "DXVA_RESTRICTED_MODE_WMV9_POSTPROC",
    "DXVA_SCAN_METHOD_ALTERNATE_HORIZONTAL",
    "DXVA_SCAN_METHOD_ALTERNATE_VERTICAL",
    "DXVA_SCAN_METHOD_ARBITRARY",
    "DXVA_SCAN_METHOD_ZIG_ZAG",
    "DXVA_SLICE_CONTROL_BUFFER",
    "DXVA_STATUS_REPORTING_FUNCTION",
    "DXVA_USUAL_BLOCK_HEIGHT",
    "DXVA_USUAL_BLOCK_WIDTH",
    "DeinterlacePref9_BOB",
    "DeinterlacePref9_Mask",
    "DeinterlacePref9_NextBest",
    "DeinterlacePref9_Weave",
    "DeinterlacePref_BOB",
    "DeinterlacePref_Mask",
    "DeinterlacePref_NextBest",
    "DeinterlacePref_Weave",
    "DeinterlaceTech9_BOBLineReplicate",
    "DeinterlaceTech9_BOBVerticalStretch",
    "DeinterlaceTech9_EdgeFiltering",
    "DeinterlaceTech9_FieldAdaptive",
    "DeinterlaceTech9_MedianFiltering",
    "DeinterlaceTech9_MotionVectorSteered",
    "DeinterlaceTech9_PixelAdaptive",
    "DeinterlaceTech9_Unknown",
    "DeinterlaceTech_BOBLineReplicate",
    "DeinterlaceTech_BOBVerticalStretch",
    "DeinterlaceTech_EdgeFiltering",
    "DeinterlaceTech_FieldAdaptive",
    "DeinterlaceTech_MedianFiltering",
    "DeinterlaceTech_MotionVectorSteered",
    "DeinterlaceTech_PixelAdaptive",
    "DeinterlaceTech_Unknown",
    "DigitalCableLocator",
    "DigitalCableTuneRequest",
    "DigitalCableTuningSpace",
    "DigitalLocator",
    "DisplaySizeList",
    "DisplaySizeList_dslDefaultSize",
    "DisplaySizeList_dslDoubleSourceSize",
    "DisplaySizeList_dslFullScreen",
    "DisplaySizeList_dslHalfScreen",
    "DisplaySizeList_dslHalfSourceSize",
    "DisplaySizeList_dslQuarterScreen",
    "DisplaySizeList_dslSixteenthScreen",
    "DisplaySizeList_dslSourceSize",
    "DownResEventParam",
    "DualMonoInfo",
    "DvbParentalRatingDescriptor",
    "DvbParentalRatingParam",
    "EALocationCodeType",
    "ECHOSTAR_SATELLITE_TV_NETWORK_TYPE",
    "EC_ACTIVATE",
    "EC_BANDWIDTHCHANGE",
    "EC_BUFFERING_DATA",
    "EC_BUILT",
    "EC_CLOCK_CHANGED",
    "EC_CLOCK_UNSET",
    "EC_CODECAPI_EVENT",
    "EC_COMPLETE",
    "EC_CONTENTPROPERTY_CHANGED",
    "EC_DEVICE_LOST",
    "EC_DISPLAY_CHANGED",
    "EC_DVDBASE",
    "EC_DVD_ANGLES_AVAILABLE",
    "EC_DVD_ANGLE_CHANGE",
    "EC_DVD_AUDIO_STREAM_CHANGE",
    "EC_DVD_BUTTON_AUTO_ACTIVATED",
    "EC_DVD_BUTTON_CHANGE",
    "EC_DVD_BeginNavigationCommands",
    "EC_DVD_CHAPTER_AUTOSTOP",
    "EC_DVD_CHAPTER_START",
    "EC_DVD_CMD_END",
    "EC_DVD_CMD_START",
    "EC_DVD_CURRENT_HMSF_TIME",
    "EC_DVD_CURRENT_TIME",
    "EC_DVD_DISC_EJECTED",
    "EC_DVD_DISC_INSERTED",
    "EC_DVD_DOMAIN_CHANGE",
    "EC_DVD_ERROR",
    "EC_DVD_GPRM_Change",
    "EC_DVD_KARAOKE_MODE",
    "EC_DVD_NO_FP_PGC",
    "EC_DVD_NavigationCommand",
    "EC_DVD_PARENTAL_LEVEL_CHANGE",
    "EC_DVD_PLAYBACK_RATE_CHANGE",
    "EC_DVD_PLAYBACK_STOPPED",
    "EC_DVD_PLAYPERIOD_AUTOSTOP",
    "EC_DVD_PROGRAM_CELL_CHANGE",
    "EC_DVD_PROGRAM_CHAIN_CHANGE",
    "EC_DVD_SPRM_Change",
    "EC_DVD_STILL_OFF",
    "EC_DVD_STILL_ON",
    "EC_DVD_SUBPICTURE_STREAM_CHANGE",
    "EC_DVD_TITLE_CHANGE",
    "EC_DVD_TITLE_SET_CHANGE",
    "EC_DVD_VALID_UOPS_CHANGE",
    "EC_DVD_VOBU_Offset",
    "EC_DVD_VOBU_Timestamp",
    "EC_DVD_WARNING",
    "EC_END_OF_SEGMENT",
    "EC_EOS_SOON",
    "EC_ERRORABORT",
    "EC_ERRORABORTEX",
    "EC_ERROR_STILLPLAYING",
    "EC_EXTDEVICE_MODE_CHANGE",
    "EC_FILE_CLOSED",
    "EC_FULLSCREEN_LOST",
    "EC_GRAPH_CHANGED",
    "EC_LENGTH_CHANGED",
    "EC_LOADSTATUS",
    "EC_MARKER_HIT",
    "EC_NEED_RESTART",
    "EC_NEW_PIN",
    "EC_NOTIFY_WINDOW",
    "EC_OLE_EVENT",
    "EC_OPENING_FILE",
    "EC_PALETTE_CHANGED",
    "EC_PAUSED",
    "EC_PLEASE_REOPEN",
    "EC_PREPROCESS_COMPLETE",
    "EC_PROCESSING_LATENCY",
    "EC_QUALITY_CHANGE",
    "EC_RENDER_FINISHED",
    "EC_REPAINT",
    "EC_SAMPLE_LATENCY",
    "EC_SAMPLE_NEEDED",
    "EC_SCRUB_TIME",
    "EC_SEGMENT_STARTED",
    "EC_SHUTTING_DOWN",
    "EC_SKIP_FRAMES",
    "EC_SNDDEV_IN_ERROR",
    "EC_SNDDEV_OUT_ERROR",
    "EC_SND_DEVICE_ERROR_BASE",
    "EC_STARVATION",
    "EC_STATE_CHANGE",
    "EC_STATUS",
    "EC_STEP_COMPLETE",
    "EC_STREAM_CONTROL_STARTED",
    "EC_STREAM_CONTROL_STOPPED",
    "EC_STREAM_ERROR_STILLPLAYING",
    "EC_STREAM_ERROR_STOPPED",
    "EC_SYSTEMBASE",
    "EC_TIME",
    "EC_TIMECODE_AVAILABLE",
    "EC_UNBUILT",
    "EC_USER",
    "EC_USERABORT",
    "EC_VIDEOFRAMEREADY",
    "EC_VIDEO_SIZE_CHANGED",
    "EC_VMR_RECONNECTION_FAILED",
    "EC_VMR_RENDERDEVICE_SET",
    "EC_VMR_SURFACE_FLIPPED",
    "EC_WINDOW_DESTROYED",
    "EC_WMT_EVENT",
    "EC_WMT_EVENT_BASE",
    "EC_WMT_INDEX_EVENT",
    "ENCDEC_CPEVENT",
    "ENCDEC_RECORDING_STATUS",
    "ESEventFactory",
    "ESEventService",
    "ETFilter",
    "EVENTID_ARIBcontentSpanningEvent",
    "EVENTID_AudioDescriptorSpanningEvent",
    "EVENTID_AudioTypeSpanningEvent",
    "EVENTID_BDAConditionalAccessTAG",
    "EVENTID_BDAEventingServicePendingEvent",
    "EVENTID_BDA_CASBroadcastMMI",
    "EVENTID_BDA_CASCloseMMI",
    "EVENTID_BDA_CASOpenMMI",
    "EVENTID_BDA_CASReleaseTuner",
    "EVENTID_BDA_CASRequestTuner",
    "EVENTID_BDA_DiseqCResponseAvailable",
    "EVENTID_BDA_EncoderSignalLock",
    "EVENTID_BDA_FdcStatus",
    "EVENTID_BDA_FdcTableSection",
    "EVENTID_BDA_GPNVValueUpdate",
    "EVENTID_BDA_GuideDataAvailable",
    "EVENTID_BDA_GuideDataError",
    "EVENTID_BDA_GuideServiceInformationUpdated",
    "EVENTID_BDA_IsdbCASResponse",
    "EVENTID_BDA_LbigsCloseConnectionHandle",
    "EVENTID_BDA_LbigsOpenConnection",
    "EVENTID_BDA_LbigsSendData",
    "EVENTID_BDA_RatingPinReset",
    "EVENTID_BDA_TransprtStreamSelectorInfo",
    "EVENTID_BDA_TunerNoSignal",
    "EVENTID_BDA_TunerSignalLock",
    "EVENTID_BDA_UpdateDrmStatus",
    "EVENTID_BDA_UpdateScanState",
    "EVENTID_CADenialCountChanged",
    "EVENTID_CASFailureSpanningEvent",
    "EVENTID_CSDescriptorSpanningEvent",
    "EVENTID_CandidatePostTuneData",
    "EVENTID_CardStatusChanged",
    "EVENTID_ChannelChangeSpanningEvent",
    "EVENTID_ChannelInfoSpanningEvent",
    "EVENTID_ChannelTypeSpanningEvent",
    "EVENTID_CtxADescriptorSpanningEvent",
    "EVENTID_DFNWithNoActualAVData",
    "EVENTID_DRMParingStatusChanged",
    "EVENTID_DRMParingStepComplete",
    "EVENTID_DTFilterCOPPBlock",
    "EVENTID_DTFilterCOPPUnblock",
    "EVENTID_DTFilterDataFormatFailure",
    "EVENTID_DTFilterDataFormatOK",
    "EVENTID_DTFilterRatingChange",
    "EVENTID_DTFilterRatingsBlock",
    "EVENTID_DTFilterRatingsUnblock",
    "EVENTID_DTFilterXDSPacket",
    "EVENTID_DVBScramblingControlSpanningEvent",
    "EVENTID_DemultiplexerFilterDiscontinuity",
    "EVENTID_DualMonoSpanningEvent",
    "EVENTID_DvbParentalRatingDescriptor",
    "EVENTID_EASMessageReceived",
    "EVENTID_ETDTFilterLicenseFailure",
    "EVENTID_ETDTFilterLicenseOK",
    "EVENTID_ETFilterCopyNever",
    "EVENTID_ETFilterCopyOnce",
    "EVENTID_ETFilterEncryptionOff",
    "EVENTID_ETFilterEncryptionOn",
    "EVENTID_EmmMessageSpanningEvent",
    "EVENTID_EncDecFilterError",
    "EVENTID_EncDecFilterEvent",
    "EVENTID_EntitlementChanged",
    "EVENTID_FormatNotSupportedEvent",
    "EVENTID_LanguageSpanningEvent",
    "EVENTID_MMIMessage",
    "EVENTID_NewSignalAcquired",
    "EVENTID_PBDAParentalControlEvent",
    "EVENTID_PIDListSpanningEvent",
    "EVENTID_PSITable",
    "EVENTID_RRTSpanningEvent",
    "EVENTID_SBE2RecControlStarted",
    "EVENTID_SBE2RecControlStopped",
    "EVENTID_STBChannelNumber",
    "EVENTID_ServiceTerminated",
    "EVENTID_SignalAndServiceStatusSpanningEvent",
    "EVENTID_SignalStatusChanged",
    "EVENTID_StreamIDSpanningEvent",
    "EVENTID_StreamTypeSpanningEvent",
    "EVENTID_SubtitleSpanningEvent",
    "EVENTID_TeletextSpanningEvent",
    "EVENTID_TuneFailureEvent",
    "EVENTID_TuneFailureSpanningEvent",
    "EVENTID_TuningChanged",
    "EVENTID_TuningChanging",
    "EVENTID_XDSCodecDuplicateXDSRating",
    "EVENTID_XDSCodecNewXDSPacket",
    "EVENTID_XDSCodecNewXDSRating",
    "EVENTTYPE_CASDescrambleFailureEvent",
    "E_PROP_ID_UNSUPPORTED",
    "E_PROP_SET_UNSUPPORTED",
    "EnTag_Mode",
    "EnTag_Once",
    "EnTag_Remove",
    "EnTag_Repeat",
    "EnTvRat_CAE_TV",
    "EnTvRat_CAF_TV",
    "EnTvRat_GenericLevel",
    "EnTvRat_MPAA",
    "EnTvRat_System",
    "EnTvRat_System_AgeBased",
    "EnTvRat_System_Canadian_English",
    "EnTvRat_System_Canadian_French",
    "EnTvRat_System_MPAA",
    "EnTvRat_System_PBDA",
    "EnTvRat_System_Reserved4",
    "EnTvRat_System_Reserved7",
    "EnTvRat_System_System5",
    "EnTvRat_System_System6",
    "EnTvRat_System_TvRat_SystemDontKnow",
    "EnTvRat_System_TvRat_kSystems",
    "EnTvRat_System_US_TV",
    "EnTvRat_US_TV",
    "EncDecEvents",
    "EntitlementType",
    "EntitlementType_Entitled",
    "EntitlementType_NotEntitled",
    "EntitlementType_TechnicalFailure",
    "EvalRat",
    "FECMethod",
    "FILTER_INFO",
    "FILTER_STATE",
    "FORMATNOTSUPPORTED_CLEAR",
    "FORMATNOTSUPPORTED_NOTSUPPORTED",
    "FORMATTYPE_CPFilters_Processed",
    "FORMATTYPE_ETDTFilter_Tagged",
    "FORMAT_DVD_LPCMAudio",
    "FORMAT_DolbyAC3",
    "FORMAT_Image",
    "FORMAT_JPEGImage",
    "FORMAT_MPEG2Audio",
    "FORMAT_MPEG2Video",
    "FORMAT_MPEG2_VIDEO",
    "FORMAT_UVCH264Video",
    "FORMAT_VIDEOINFO2",
    "FilgraphManager",
    "FormatNotSupportedEvents",
    "GUID_TIME_MUSIC",
    "GUID_TIME_REFERENCE",
    "GUID_TIME_SAMPLES",
    "GuardInterval",
    "HEAACWAVEFORMAT",
    "HEAACWAVEINFO",
    "HierarchyAlpha",
    "IAMAnalogVideoDecoder",
    "IAMAnalogVideoEncoder",
    "IAMAsyncReaderTimestampScaling",
    "IAMAudioInputMixer",
    "IAMAudioRendererStats",
    "IAMBufferNegotiation",
    "IAMCameraControl",
    "IAMCertifiedOutputProtection",
    "IAMChannelInfo",
    "IAMClockAdjust",
    "IAMClockSlave",
    "IAMCollection",
    "IAMCopyCaptureFileProgress",
    "IAMCrossbar",
    "IAMDecoderCaps",
    "IAMDevMemoryAllocator",
    "IAMDevMemoryControl",
    "IAMDeviceRemoval",
    "IAMDirectSound",
    "IAMDroppedFrames",
    "IAMExtDevice",
    "IAMExtTransport",
    "IAMExtendedErrorInfo",
    "IAMExtendedSeeking",
    "IAMFilterGraphCallback",
    "IAMFilterMiscFlags",
    "IAMGraphBuilderCallback",
    "IAMGraphStreams",
    "IAMLatency",
    "IAMLine21Decoder",
    "IAMMediaContent",
    "IAMMediaContent2",
    "IAMMediaStream",
    "IAMMediaTypeSample",
    "IAMMediaTypeStream",
    "IAMMultiMediaStream",
    "IAMNetShowConfig",
    "IAMNetShowExProps",
    "IAMNetShowPreroll",
    "IAMNetworkStatus",
    "IAMOpenProgress",
    "IAMOverlayFX",
    "IAMParse",
    "IAMPhysicalPinInfo",
    "IAMPlayList",
    "IAMPlayListItem",
    "IAMPluginControl",
    "IAMPushSource",
    "IAMRebuild",
    "IAMResourceControl",
    "IAMStats",
    "IAMStreamConfig",
    "IAMStreamControl",
    "IAMStreamSelect",
    "IAMTVAudio",
    "IAMTVAudioNotification",
    "IAMTVTuner",
    "IAMTimecodeDisplay",
    "IAMTimecodeGenerator",
    "IAMTimecodeReader",
    "IAMTuner",
    "IAMTunerNotification",
    "IAMVfwCaptureDialogs",
    "IAMVfwCompressDialogs",
    "IAMVideoAccelerator",
    "IAMVideoAcceleratorNotify",
    "IAMVideoCompression",
    "IAMVideoControl",
    "IAMVideoDecimationProperties",
    "IAMVideoProcAmp",
    "IAMWMBufferPass",
    "IAMWMBufferPassCallback",
    "IAMWstDecoder",
    "IAMovieSetup",
    "IATSCChannelTuneRequest",
    "IATSCComponentType",
    "IATSCLocator",
    "IATSCLocator2",
    "IATSCTuningSpace",
    "IATSC_EIT",
    "IATSC_ETT",
    "IATSC_MGT",
    "IATSC_STT",
    "IATSC_VCT",
    "IAnalogAudioComponentType",
    "IAnalogLocator",
    "IAnalogRadioTuningSpace",
    "IAnalogRadioTuningSpace2",
    "IAnalogTVTuningSpace",
    "IAsyncReader",
    "IAtscContentAdvisoryDescriptor",
    "IAtscPsipParser",
    "IAttributeGet",
    "IAttributeSet",
    "IAudioData",
    "IAudioMediaStream",
    "IAudioStreamSample",
    "IAuxInTuningSpace",
    "IAuxInTuningSpace2",
    "IBDAComparable",
    "IBDACreateTuneRequestEx",
    "IBDA_AUX",
    "IBDA_AutoDemodulate",
    "IBDA_AutoDemodulateEx",
    "IBDA_ConditionalAccess",
    "IBDA_ConditionalAccessEx",
    "IBDA_DRIDRMService",
    "IBDA_DRIWMDRMSession",
    "IBDA_DRM",
    "IBDA_DRMService",
    "IBDA_DeviceControl",
    "IBDA_DiagnosticProperties",
    "IBDA_DigitalDemodulator",
    "IBDA_DigitalDemodulator2",
    "IBDA_DigitalDemodulator3",
    "IBDA_DiseqCommand",
    "IBDA_EasMessage",
    "IBDA_Encoder",
    "IBDA_EthernetFilter",
    "IBDA_EventingService",
    "IBDA_FDC",
    "IBDA_FrequencyFilter",
    "IBDA_GuideDataDeliveryService",
    "IBDA_IPSinkControl",
    "IBDA_IPSinkInfo",
    "IBDA_IPV4Filter",
    "IBDA_IPV6Filter",
    "IBDA_ISDBConditionalAccess",
    "IBDA_LNBInfo",
    "IBDA_MUX",
    "IBDA_NameValueService",
    "IBDA_NetworkProvider",
    "IBDA_NullTransform",
    "IBDA_PinControl",
    "IBDA_SignalProperties",
    "IBDA_SignalStatistics",
    "IBDA_TIF_REGISTRATION",
    "IBDA_Topology",
    "IBDA_TransportStreamInfo",
    "IBDA_TransportStreamSelector",
    "IBDA_UserActivityService",
    "IBDA_VoidTransform",
    "IBDA_WMDRMSession",
    "IBDA_WMDRMTuner",
    "IBPCSatelliteTuner",
    "IBaseFilter",
    "IBaseVideoMixer",
    "IBasicAudio",
    "IBasicVideo",
    "IBasicVideo2",
    "IBroadcastEvent",
    "IBroadcastEventEx",
    "IBufferingTime",
    "ICAT",
    "ICCSubStreamFiltering",
    "ICameraControl",
    "ICaptionServiceDescriptor",
    "ICaptureGraphBuilder",
    "ICaptureGraphBuilder2",
    "IChannelIDTuneRequest",
    "IChannelTuneRequest",
    "IComponent",
    "IComponentType",
    "IComponentTypes",
    "IComponents",
    "IComponentsOld",
    "IConfigAsfWriter",
    "IConfigAsfWriter2",
    "IConfigAviMux",
    "IConfigInterleaving",
    "ICreateDevEnum",
    "ICreatePropBagOnRegKey",
    "IDDrawExclModeVideo",
    "IDDrawExclModeVideoCallback",
    "IDMOWrapperFilter",
    "IDShowPlugin",
    "IDTFilter",
    "IDTFilter2",
    "IDTFilter3",
    "IDTFilterConfig",
    "IDTFilterEvents",
    "IDTFilterLicenseRenewal",
    "IDVBCLocator",
    "IDVBSLocator",
    "IDVBSLocator2",
    "IDVBSTuningSpace",
    "IDVBTLocator",
    "IDVBTLocator2",
    "IDVBTuneRequest",
    "IDVBTuningSpace",
    "IDVBTuningSpace2",
    "IDVB_BAT",
    "IDVB_DIT",
    "IDVB_EIT",
    "IDVB_EIT2",
    "IDVB_NIT",
    "IDVB_RST",
    "IDVB_SDT",
    "IDVB_SIT",
    "IDVB_ST",
    "IDVB_TDT",
    "IDVB_TOT",
    "IDVEnc",
    "IDVRGB219",
    "IDVSplitter",
    "IDecimateVideoImage",
    "IDeferredCommand",
    "IDigitalCableLocator",
    "IDigitalCableTuneRequest",
    "IDigitalCableTuningSpace",
    "IDigitalLocator",
    "IDirectDrawMediaSample",
    "IDirectDrawMediaSampleAllocator",
    "IDirectDrawMediaStream",
    "IDirectDrawStreamSample",
    "IDirectDrawVideo",
    "IDistributorNotify",
    "IDrawVideoImage",
    "IDvbCableDeliverySystemDescriptor",
    "IDvbComponentDescriptor",
    "IDvbContentDescriptor",
    "IDvbContentIdentifierDescriptor",
    "IDvbDataBroadcastDescriptor",
    "IDvbDataBroadcastIDDescriptor",
    "IDvbDefaultAuthorityDescriptor",
    "IDvbExtendedEventDescriptor",
    "IDvbFrequencyListDescriptor",
    "IDvbHDSimulcastLogicalChannelDescriptor",
    "IDvbLinkageDescriptor",
    "IDvbLogicalChannel2Descriptor",
    "IDvbLogicalChannelDescriptor",
    "IDvbLogicalChannelDescriptor2",
    "IDvbMultilingualServiceNameDescriptor",
    "IDvbNetworkNameDescriptor",
    "IDvbParentalRatingDescriptor",
    "IDvbPrivateDataSpecifierDescriptor",
    "IDvbSatelliteDeliverySystemDescriptor",
    "IDvbServiceAttributeDescriptor",
    "IDvbServiceDescriptor",
    "IDvbServiceDescriptor2",
    "IDvbServiceListDescriptor",
    "IDvbShortEventDescriptor",
    "IDvbSiParser",
    "IDvbSiParser2",
    "IDvbSubtitlingDescriptor",
    "IDvbTeletextDescriptor",
    "IDvbTerrestrial2DeliverySystemDescriptor",
    "IDvbTerrestrialDeliverySystemDescriptor",
    "IDvdCmd",
    "IDvdControl",
    "IDvdControl2",
    "IDvdGraphBuilder",
    "IDvdInfo",
    "IDvdInfo2",
    "IDvdState",
    "IESCloseMmiEvent",
    "IESEvent",
    "IESEventFactory",
    "IESEventService",
    "IESEventServiceConfiguration",
    "IESEvents",
    "IESFileExpiryDateEvent",
    "IESIsdbCasResponseEvent",
    "IESLicenseRenewalResultEvent",
    "IESOpenMmiEvent",
    "IESRequestTunerEvent",
    "IESValueUpdatedEvent",
    "IETFilter",
    "IETFilterConfig",
    "IETFilterEvents",
    "IEncoderAPI",
    "IEnumComponentTypes",
    "IEnumComponents",
    "IEnumFilters",
    "IEnumGuideDataProperties",
    "IEnumMSVidGraphSegment",
    "IEnumMediaTypes",
    "IEnumPIDMap",
    "IEnumPins",
    "IEnumRegFilters",
    "IEnumStreamBufferRecordingAttrib",
    "IEnumStreamIdMap",
    "IEnumTuneRequests",
    "IEnumTuningSpaces",
    "IEvalRat",
    "IFILTERMAPPER_MERIT",
    "IFileSinkFilter",
    "IFileSinkFilter2",
    "IFileSourceFilter",
    "IFilterChain",
    "IFilterGraph",
    "IFilterGraph2",
    "IFilterGraph3",
    "IFilterInfo",
    "IFilterMapper",
    "IFilterMapper2",
    "IFilterMapper3",
    "IFrequencyMap",
    "IFullScreenVideo",
    "IFullScreenVideoEx",
    "IGenericDescriptor",
    "IGenericDescriptor2",
    "IGetCapabilitiesKey",
    "IGpnvsCommonBase",
    "IGraphBuilder",
    "IGraphConfig",
    "IGraphConfigCallback",
    "IGraphVersion",
    "IGuideData",
    "IGuideDataEvent",
    "IGuideDataLoader",
    "IGuideDataProperty",
    "IIPDVDec",
    "IISDBSLocator",
    "IISDB_BIT",
    "IISDB_CDT",
    "IISDB_EMM",
    "IISDB_LDT",
    "IISDB_NBIT",
    "IISDB_SDT",
    "IISDB_SDTT",
    "IIsdbAudioComponentDescriptor",
    "IIsdbCAContractInformationDescriptor",
    "IIsdbCADescriptor",
    "IIsdbCAServiceDescriptor",
    "IIsdbComponentGroupDescriptor",
    "IIsdbDataContentDescriptor",
    "IIsdbDigitalCopyControlDescriptor",
    "IIsdbDownloadContentDescriptor",
    "IIsdbEmergencyInformationDescriptor",
    "IIsdbEventGroupDescriptor",
    "IIsdbHierarchicalTransmissionDescriptor",
    "IIsdbLogoTransmissionDescriptor",
    "IIsdbSIParameterDescriptor",
    "IIsdbSeriesDescriptor",
    "IIsdbSiParser2",
    "IIsdbTSInformationDescriptor",
    "IIsdbTerrestrialDeliverySystemDescriptor",
    "IKsNodeControl",
    "IKsTopologyInfo",
    "ILanguageComponentType",
    "ILocator",
    "IMPEG2Component",
    "IMPEG2ComponentType",
    "IMPEG2PIDMap",
    "IMPEG2StreamIdMap",
    "IMPEG2TuneRequest",
    "IMPEG2TuneRequestFactory",
    "IMPEG2TuneRequestSupport",
    "IMPEG2_TIF_CONTROL",
    "IMSEventBinder",
    "IMSVidAnalogTuner",
    "IMSVidAnalogTuner2",
    "IMSVidAnalogTunerEvent",
    "IMSVidAudioRenderer",
    "IMSVidAudioRendererDevices",
    "IMSVidAudioRendererEvent",
    "IMSVidAudioRendererEvent2",
    "IMSVidClosedCaptioning",
    "IMSVidClosedCaptioning2",
    "IMSVidClosedCaptioning3",
    "IMSVidCompositionSegment",
    "IMSVidCtl",
    "IMSVidDataServices",
    "IMSVidDataServicesEvent",
    "IMSVidDevice",
    "IMSVidDevice2",
    "IMSVidDeviceEvent",
    "IMSVidEVR",
    "IMSVidEVREvent",
    "IMSVidEncoder",
    "IMSVidFeature",
    "IMSVidFeatureEvent",
    "IMSVidFeatures",
    "IMSVidFilePlayback",
    "IMSVidFilePlayback2",
    "IMSVidFilePlaybackEvent",
    "IMSVidGenericSink",
    "IMSVidGenericSink2",
    "IMSVidGraphSegment",
    "IMSVidGraphSegmentContainer",
    "IMSVidGraphSegmentUserInput",
    "IMSVidInputDevice",
    "IMSVidInputDeviceEvent",
    "IMSVidInputDevices",
    "IMSVidOutputDevice",
    "IMSVidOutputDeviceEvent",
    "IMSVidOutputDevices",
    "IMSVidPlayback",
    "IMSVidPlaybackEvent",
    "IMSVidRect",
    "IMSVidStreamBufferRecordingControl",
    "IMSVidStreamBufferSink",
    "IMSVidStreamBufferSink2",
    "IMSVidStreamBufferSink3",
    "IMSVidStreamBufferSinkEvent",
    "IMSVidStreamBufferSinkEvent2",
    "IMSVidStreamBufferSinkEvent3",
    "IMSVidStreamBufferSinkEvent4",
    "IMSVidStreamBufferSource",
    "IMSVidStreamBufferSource2",
    "IMSVidStreamBufferSourceEvent",
    "IMSVidStreamBufferSourceEvent2",
    "IMSVidStreamBufferSourceEvent3",
    "IMSVidStreamBufferV2SourceEvent",
    "IMSVidTuner",
    "IMSVidTunerEvent",
    "IMSVidVMR9",
    "IMSVidVRGraphSegment",
    "IMSVidVideoInputDevice",
    "IMSVidVideoRenderer",
    "IMSVidVideoRenderer2",
    "IMSVidVideoRendererDevices",
    "IMSVidVideoRendererEvent",
    "IMSVidVideoRendererEvent2",
    "IMSVidWebDVD",
    "IMSVidWebDVD2",
    "IMSVidWebDVDAdm",
    "IMSVidWebDVDEvent",
    "IMSVidXDS",
    "IMSVidXDSEvent",
    "IMceBurnerControl",
    "IMediaControl",
    "IMediaEvent",
    "IMediaEventEx",
    "IMediaEventSink",
    "IMediaFilter",
    "IMediaParamInfo",
    "IMediaParams",
    "IMediaPosition",
    "IMediaPropertyBag",
    "IMediaSample",
    "IMediaSample2",
    "IMediaSample2Config",
    "IMediaSeeking",
    "IMediaStream",
    "IMediaStreamFilter",
    "IMediaTypeInfo",
    "IMemAllocator",
    "IMemAllocatorCallbackTemp",
    "IMemAllocatorNotifyCallbackTemp",
    "IMemInputPin",
    "IMemoryData",
    "IMixerOCX",
    "IMixerOCXNotify",
    "IMixerPinConfig",
    "IMixerPinConfig2",
    "IMpeg2Data",
    "IMpeg2Demultiplexer",
    "IMpeg2Stream",
    "IMpeg2TableFilter",
    "IMpegAudioDecoder",
    "IMultiMediaStream",
    "INTERLEAVE_CAPTURE",
    "INTERLEAVE_FULL",
    "INTERLEAVE_NONE",
    "INTERLEAVE_NONE_BUFFERED",
    "IOverlay",
    "IOverlayNotify",
    "IOverlayNotify2",
    "IPAT",
    "IPBDAAttributesDescriptor",
    "IPBDAEntitlementDescriptor",
    "IPBDASiParser",
    "IPBDA_EIT",
    "IPBDA_Services",
    "IPMT",
    "IPSITables",
    "IPTFilterLicenseRenewal",
    "IPersistMediaPropertyBag",
    "IPersistTuneXml",
    "IPersistTuneXmlUtility",
    "IPersistTuneXmlUtility2",
    "IPin",
    "IPinConnection",
    "IPinFlowControl",
    "IPinInfo",
    "IQualProp",
    "IQualityControl",
    "IQueueCommand",
    "IRegFilterInfo",
    "IRegisterServiceProvider",
    "IRegisterTuner",
    "IResourceConsumer",
    "IResourceManager",
    "ISBE2Crossbar",
    "ISBE2EnumStream",
    "ISBE2FileScan",
    "ISBE2GlobalEvent",
    "ISBE2GlobalEvent2",
    "ISBE2MediaTypeProfile",
    "ISBE2SpanningEvent",
    "ISBE2StreamMap",
    "ISCTE_EAS",
    "ISDBCAS_REQUEST_ID",
    "ISDBCAS_REQUEST_ID_EMD",
    "ISDBCAS_REQUEST_ID_EMG",
    "ISDBSLocator",
    "ISDB_BIT_PID",
    "ISDB_BIT_TID",
    "ISDB_CABLE_TV_NETWORK_TYPE",
    "ISDB_CDT_PID",
    "ISDB_CDT_TID",
    "ISDB_EMM_TID",
    "ISDB_LDT_PID",
    "ISDB_LDT_TID",
    "ISDB_NBIT_MSG_TID",
    "ISDB_NBIT_PID",
    "ISDB_NBIT_REF_TID",
    "ISDB_SATELLITE_TV_NETWORK_TYPE",
    "ISDB_SDTT_ALT_PID",
    "ISDB_SDTT_PID",
    "ISDB_SDTT_TID",
    "ISDB_ST_TID",
    "ISDB_S_NETWORK_TYPE",
    "ISDB_Satellite",
    "ISDB_TERRESTRIAL_TV_NETWORK_TYPE",
    "ISDB_T_NETWORK_TYPE",
    "ISDB_Terrestrial",
    "ISIInbandEPG",
    "ISIInbandEPGEvent",
    "IScanningTuner",
    "IScanningTunerEx",
    "ISectionList",
    "ISeekingPassThru",
    "ISelector",
    "IServiceLocationDescriptor",
    "ISpecifyParticularPages",
    "IStreamBufferConfigure",
    "IStreamBufferConfigure2",
    "IStreamBufferConfigure3",
    "IStreamBufferDataCounters",
    "IStreamBufferInitialize",
    "IStreamBufferMediaSeeking",
    "IStreamBufferMediaSeeking2",
    "IStreamBufferRecComp",
    "IStreamBufferRecordControl",
    "IStreamBufferRecordingAttribute",
    "IStreamBufferSink",
    "IStreamBufferSink2",
    "IStreamBufferSink3",
    "IStreamBufferSource",
    "IStreamBuilder",
    "IStreamSample",
    "ITSDT",
    "ITuneRequest",
    "ITuneRequestInfo",
    "ITuneRequestInfoEx",
    "ITuner",
    "ITunerCap",
    "ITunerCapEx",
    "ITuningSpace",
    "ITuningSpaceContainer",
    "ITuningSpaces",
    "IVMRAspectRatioControl",
    "IVMRAspectRatioControl9",
    "IVMRDeinterlaceControl",
    "IVMRDeinterlaceControl9",
    "IVMRFilterConfig",
    "IVMRFilterConfig9",
    "IVMRImageCompositor",
    "IVMRImageCompositor9",
    "IVMRImagePresenter",
    "IVMRImagePresenter9",
    "IVMRImagePresenterConfig",
    "IVMRImagePresenterConfig9",
    "IVMRImagePresenterExclModeConfig",
    "IVMRMixerBitmap",
    "IVMRMixerBitmap9",
    "IVMRMixerControl",
    "IVMRMixerControl9",
    "IVMRMonitorConfig",
    "IVMRMonitorConfig9",
    "IVMRSurface",
    "IVMRSurface9",
    "IVMRSurfaceAllocator",
    "IVMRSurfaceAllocator9",
    "IVMRSurfaceAllocatorEx9",
    "IVMRSurfaceAllocatorNotify",
    "IVMRSurfaceAllocatorNotify9",
    "IVMRVideoStreamControl",
    "IVMRVideoStreamControl9",
    "IVMRWindowlessControl",
    "IVMRWindowlessControl9",
    "IVPBaseConfig",
    "IVPBaseNotify",
    "IVPConfig",
    "IVPManager",
    "IVPNotify",
    "IVPNotify2",
    "IVPVBIConfig",
    "IVPVBINotify",
    "IVideoEncoder",
    "IVideoFrameStep",
    "IVideoProcAmp",
    "IVideoWindow",
    "IWMCodecAMVideoAccelerator",
    "IWMCodecVideoAccelerator",
    "IXDSCodec",
    "IXDSCodecConfig",
    "IXDSCodecEvents",
    "IXDSToRat",
    "InterleavingMode",
    "KSCATEGORY_BDA_IP_SINK",
    "KSCATEGORY_BDA_NETWORK_EPG",
    "KSCATEGORY_BDA_NETWORK_PROVIDER",
    "KSCATEGORY_BDA_NETWORK_TUNER",
    "KSCATEGORY_BDA_RECEIVER_COMPONENT",
    "KSCATEGORY_BDA_TRANSPORT_INFORMATION",
    "KSDATAFORMAT_SPECIFIER_BDA_IP",
    "KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT",
    "KSDATAFORMAT_SUBTYPE_ATSC_SI",
    "KSDATAFORMAT_SUBTYPE_BDA_IP",
    "KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL",
    "KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT",
    "KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP",
    "KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP",
    "KSDATAFORMAT_SUBTYPE_DVB_SI",
    "KSDATAFORMAT_SUBTYPE_ISDB_SI",
    "KSDATAFORMAT_SUBTYPE_PBDA_TRANSPORT_RAW",
    "KSDATAFORMAT_TYPE_BDA_ANTENNA",
    "KSDATAFORMAT_TYPE_BDA_IF_SIGNAL",
    "KSDATAFORMAT_TYPE_BDA_IP",
    "KSDATAFORMAT_TYPE_BDA_IP_CONTROL",
    "KSDATAFORMAT_TYPE_MPE",
    "KSDATAFORMAT_TYPE_MPEG2_SECTIONS",
    "KSEVENTDATA_BDA_RF_TUNER_SCAN_S",
    "KSEVENTSETID_BdaCAEvent",
    "KSEVENTSETID_BdaDiseqCEvent",
    "KSEVENTSETID_BdaEvent",
    "KSEVENTSETID_BdaPinEvent",
    "KSEVENTSETID_BdaTunerEvent",
    "KSEVENT_BDA_CA_MODULE_STATUS_CHANGED",
    "KSEVENT_BDA_CA_MODULE_UI_REQUESTED",
    "KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED",
    "KSEVENT_BDA_DISEQC_DATA_RECEIVED",
    "KSEVENT_BDA_EVENT_PENDINGEVENT",
    "KSEVENT_BDA_EVENT_TYPE",
    "KSEVENT_BDA_PIN_CONNECTED",
    "KSEVENT_BDA_PIN_DISCONNECTED",
    "KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED",
    "KSEVENT_BDA_TUNER",
    "KSEVENT_BDA_TUNER_SCAN",
    "KSMETHODSETID_BdaChangeSync",
    "KSMETHODSETID_BdaConditionalAccessService",
    "KSMETHODSETID_BdaDebug",
    "KSMETHODSETID_BdaDeviceConfiguration",
    "KSMETHODSETID_BdaDrmService",
    "KSMETHODSETID_BdaEventing",
    "KSMETHODSETID_BdaGuideDataDeliveryService",
    "KSMETHODSETID_BdaIsdbConditionalAccess",
    "KSMETHODSETID_BdaMux",
    "KSMETHODSETID_BdaNameValue",
    "KSMETHODSETID_BdaNameValueA",
    "KSMETHODSETID_BdaScanning",
    "KSMETHODSETID_BdaTSSelector",
    "KSMETHODSETID_BdaTuner",
    "KSMETHODSETID_BdaUserActivity",
    "KSMETHODSETID_BdaWmdrmSession",
    "KSMETHODSETID_BdaWmdrmTuner",
    "KSMETHOD_BDA_CAS_CHECKENTITLEMENTTOKEN",
    "KSMETHOD_BDA_CAS_CLOSEMMIDIALOG",
    "KSMETHOD_BDA_CAS_OPENBROADCASTMMI",
    "KSMETHOD_BDA_CAS_SERVICE",
    "KSMETHOD_BDA_CAS_SETCAPTURETOKEN",
    "KSMETHOD_BDA_CHANGE_SYNC",
    "KSMETHOD_BDA_CHECK_CHANGES",
    "KSMETHOD_BDA_COMMIT_CHANGES",
    "KSMETHOD_BDA_CREATE_PIN_FACTORY",
    "KSMETHOD_BDA_CREATE_TOPOLOGY",
    "KSMETHOD_BDA_DEBUG_DATA",
    "KSMETHOD_BDA_DEBUG_LEVEL",
    "KSMETHOD_BDA_DEBUG_SERVICE",
    "KSMETHOD_BDA_DELETE_PIN_FACTORY",
    "KSMETHOD_BDA_DEVICE_CONFIGURATION",
    "KSMETHOD_BDA_DRM",
    "KSMETHOD_BDA_DRM_CURRENT",
    "KSMETHOD_BDA_DRM_DRMSTATUS",
    "KSMETHOD_BDA_EVENTING_SERVICE",
    "KSMETHOD_BDA_EVENT_COMPLETE",
    "KSMETHOD_BDA_EVENT_DATA",
    "KSMETHOD_BDA_GDDS_DATA",
    "KSMETHOD_BDA_GDDS_DATATYPE",
    "KSMETHOD_BDA_GDDS_DATAUPDATE",
    "KSMETHOD_BDA_GDDS_GETSERVICES",
    "KSMETHOD_BDA_GDDS_SERVICE",
    "KSMETHOD_BDA_GDDS_SERVICEFROMTUNEXML",
    "KSMETHOD_BDA_GDDS_TUNEXMLFROMIDX",
    "KSMETHOD_BDA_GET_CHANGE_STATE",
    "KSMETHOD_BDA_GPNV_GETVALUE",
    "KSMETHOD_BDA_GPNV_GETVALUEUPDATENAME",
    "KSMETHOD_BDA_GPNV_NAMEFROMINDEX",
    "KSMETHOD_BDA_GPNV_SERVICE",
    "KSMETHOD_BDA_GPNV_SETVALUE",
    "KSMETHOD_BDA_ISDBCAS_RESPONSEDATA",
    "KSMETHOD_BDA_ISDBCAS_SETREQUEST",
    "KSMETHOD_BDA_ISDB_CAS",
    "KSMETHOD_BDA_MUX_GETPIDLIST",
    "KSMETHOD_BDA_MUX_SERVICE",
    "KSMETHOD_BDA_MUX_SETPIDLIST",
    "KSMETHOD_BDA_SCANNING_STATE",
    "KSMETHOD_BDA_SCAN_CAPABILTIES",
    "KSMETHOD_BDA_SCAN_FILTER",
    "KSMETHOD_BDA_SCAN_RESUME",
    "KSMETHOD_BDA_SCAN_SERVICE",
    "KSMETHOD_BDA_SCAN_START",
    "KSMETHOD_BDA_SCAN_STOP",
    "KSMETHOD_BDA_START_CHANGES",
    "KSMETHOD_BDA_TS_SELECTOR",
    "KSMETHOD_BDA_TS_SELECTOR_GETTSINFORMATION",
    "KSMETHOD_BDA_TS_SELECTOR_SETTSID",
    "KSMETHOD_BDA_TUNER_GETTUNERSTATE",
    "KSMETHOD_BDA_TUNER_SERVICE",
    "KSMETHOD_BDA_TUNER_SETTUNER",
    "KSMETHOD_BDA_TUNER_SIGNALNOISERATIO",
    "KSMETHOD_BDA_USERACTIVITY_DETECTED",
    "KSMETHOD_BDA_USERACTIVITY_INTERVAL",
    "KSMETHOD_BDA_USERACTIVITY_SERVICE",
    "KSMETHOD_BDA_USERACTIVITY_USEREASON",
    "KSMETHOD_BDA_WMDRM",
    "KSMETHOD_BDA_WMDRMTUNER_CANCELCAPTURETOKEN",
    "KSMETHOD_BDA_WMDRMTUNER_GETPIDPROTECTION",
    "KSMETHOD_BDA_WMDRMTUNER_PURCHASE_ENTITLEMENT",
    "KSMETHOD_BDA_WMDRMTUNER_SETPIDPROTECTION",
    "KSMETHOD_BDA_WMDRMTUNER_SETSYNCVALUE",
    "KSMETHOD_BDA_WMDRMTUNER_STARTCODEPROFILE",
    "KSMETHOD_BDA_WMDRM_CRL",
    "KSMETHOD_BDA_WMDRM_KEYINFO",
    "KSMETHOD_BDA_WMDRM_LICENSE",
    "KSMETHOD_BDA_WMDRM_MESSAGE",
    "KSMETHOD_BDA_WMDRM_REISSUELICENSE",
    "KSMETHOD_BDA_WMDRM_RENEWLICENSE",
    "KSMETHOD_BDA_WMDRM_REVINFO",
    "KSMETHOD_BDA_WMDRM_STATUS",
    "KSMETHOD_BDA_WMDRM_TUNER",
    "KSM_BDA_BUFFER",
    "KSM_BDA_CAS_CAPTURETOKEN",
    "KSM_BDA_CAS_CLOSEMMIDIALOG",
    "KSM_BDA_CAS_ENTITLEMENTTOKEN",
    "KSM_BDA_CAS_OPENBROADCASTMMI",
    "KSM_BDA_DEBUG_LEVEL",
    "KSM_BDA_DRM_SETDRM",
    "KSM_BDA_EVENT_COMPLETE",
    "KSM_BDA_GDDS_SERVICEFROMTUNEXML",
    "KSM_BDA_GDDS_TUNEXMLFROMIDX",
    "KSM_BDA_GPNV_GETVALUE",
    "KSM_BDA_GPNV_NAMEINDEX",
    "KSM_BDA_GPNV_SETVALUE",
    "KSM_BDA_ISDBCAS_REQUEST",
    "KSM_BDA_PIN",
    "KSM_BDA_PIN_PAIR",
    "KSM_BDA_SCAN_CAPABILTIES",
    "KSM_BDA_SCAN_FILTER",
    "KSM_BDA_SCAN_START",
    "KSM_BDA_TS_SELECTOR_SETTSID",
    "KSM_BDA_TUNER_TUNEREQUEST",
    "KSM_BDA_USERACTIVITY_USEREASON",
    "KSM_BDA_WMDRMTUNER_GETPIDPROTECTION",
    "KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT",
    "KSM_BDA_WMDRMTUNER_SETPIDPROTECTION",
    "KSM_BDA_WMDRMTUNER_SYNCVALUE",
    "KSM_BDA_WMDRM_LICENSE",
    "KSM_BDA_WMDRM_RENEWLICENSE",
    "KSNODE_BDA_8PSK_DEMODULATOR",
    "KSNODE_BDA_8VSB_DEMODULATOR",
    "KSNODE_BDA_ANALOG_DEMODULATOR",
    "KSNODE_BDA_COFDM_DEMODULATOR",
    "KSNODE_BDA_COMMON_CA_POD",
    "KSNODE_BDA_DRI_DRM",
    "KSNODE_BDA_IP_SINK",
    "KSNODE_BDA_ISDB_S_DEMODULATOR",
    "KSNODE_BDA_ISDB_T_DEMODULATOR",
    "KSNODE_BDA_OPENCABLE_POD",
    "KSNODE_BDA_PBDA_CAS",
    "KSNODE_BDA_PBDA_DRM",
    "KSNODE_BDA_PBDA_ISDBCAS",
    "KSNODE_BDA_PBDA_MUX",
    "KSNODE_BDA_PBDA_TUNER",
    "KSNODE_BDA_PID_FILTER",
    "KSNODE_BDA_QAM_DEMODULATOR",
    "KSNODE_BDA_QPSK_DEMODULATOR",
    "KSNODE_BDA_RF_TUNER",
    "KSNODE_BDA_TS_SELECTOR",
    "KSNODE_BDA_VIDEO_ENCODER",
    "KSPROPERTY_BDA_AUTODEMODULATE",
    "KSPROPERTY_BDA_AUTODEMODULATE_START",
    "KSPROPERTY_BDA_AUTODEMODULATE_STOP",
    "KSPROPERTY_BDA_CA",
    "KSPROPERTY_BDA_CA_EVENT",
    "KSPROPERTY_BDA_CA_MODULE_STATUS",
    "KSPROPERTY_BDA_CA_MODULE_UI",
    "KSPROPERTY_BDA_CA_REMOVE_PROGRAM",
    "KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS",
    "KSPROPERTY_BDA_CA_SMART_CARD_STATUS",
    "KSPROPERTY_BDA_CONTROLLING_PIN_ID",
    "KSPROPERTY_BDA_DIGITAL_DEMODULATOR",
    "KSPROPERTY_BDA_DISEQC_COMMAND",
    "KSPROPERTY_BDA_DISEQC_ENABLE",
    "KSPROPERTY_BDA_DISEQC_EVENT",
    "KSPROPERTY_BDA_DISEQC_LNB_SOURCE",
    "KSPROPERTY_BDA_DISEQC_REPEATS",
    "KSPROPERTY_BDA_DISEQC_RESPONSE",
    "KSPROPERTY_BDA_DISEQC_SEND",
    "KSPROPERTY_BDA_DISEQC_USETONEBURST",
    "KSPROPERTY_BDA_ECM_MAP_STATUS",
    "KSPROPERTY_BDA_ETHERNET_FILTER",
    "KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST",
    "KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST_SIZE",
    "KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_MODE",
    "KSPROPERTY_BDA_FREQUENCY_FILTER",
    "KSPROPERTY_BDA_GUARD_INTERVAL",
    "KSPROPERTY_BDA_INNER_FEC_RATE",
    "KSPROPERTY_BDA_INNER_FEC_TYPE",
    "KSPROPERTY_BDA_IPv4_FILTER",
    "KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST",
    "KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST_SIZE",
    "KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_MODE",
    "KSPROPERTY_BDA_IPv6_FILTER",
    "KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST",
    "KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST_SIZE",
    "KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_MODE",
    "KSPROPERTY_BDA_LNB_INFO",
    "KSPROPERTY_BDA_LNB_LOF_HIGH_BAND",
    "KSPROPERTY_BDA_LNB_LOF_LOW_BAND",
    "KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY",
    "KSPROPERTY_BDA_MODULATION_TYPE",
    "KSPROPERTY_BDA_NODE_DESCRIPTORS",
    "KSPROPERTY_BDA_NODE_EVENTS",
    "KSPROPERTY_BDA_NODE_METHODS",
    "KSPROPERTY_BDA_NODE_PROPERTIES",
    "KSPROPERTY_BDA_NODE_TYPES",
    "KSPROPERTY_BDA_NULL_TRANSFORM",
    "KSPROPERTY_BDA_NULL_TRANSFORM_START",
    "KSPROPERTY_BDA_NULL_TRANSFORM_STOP",
    "KSPROPERTY_BDA_OUTER_FEC_RATE",
    "KSPROPERTY_BDA_OUTER_FEC_TYPE",
    "KSPROPERTY_BDA_PIDFILTER",
    "KSPROPERTY_BDA_PIDFILTER_LIST_PIDS",
    "KSPROPERTY_BDA_PIDFILTER_MAP_PIDS",
    "KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS",
    "KSPROPERTY_BDA_PILOT",
    "KSPROPERTY_BDA_PIN_CONTROL",
    "KSPROPERTY_BDA_PIN_EVENT",
    "KSPROPERTY_BDA_PIN_ID",
    "KSPROPERTY_BDA_PIN_TYPE",
    "KSPROPERTY_BDA_PIN_TYPES",
    "KSPROPERTY_BDA_PLP_NUMBER",
    "KSPROPERTY_BDA_RF_TUNER_BANDWIDTH",
    "KSPROPERTY_BDA_RF_TUNER_CAPS",
    "KSPROPERTY_BDA_RF_TUNER_CAPS_S",
    "KSPROPERTY_BDA_RF_TUNER_FREQUENCY",
    "KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER",
    "KSPROPERTY_BDA_RF_TUNER_POLARITY",
    "KSPROPERTY_BDA_RF_TUNER_RANGE",
    "KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS",
    "KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S",
    "KSPROPERTY_BDA_RF_TUNER_STANDARD",
    "KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE",
    "KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S",
    "KSPROPERTY_BDA_RF_TUNER_STANDARD_S",
    "KSPROPERTY_BDA_RF_TUNER_TRANSPONDER",
    "KSPROPERTY_BDA_ROLL_OFF",
    "KSPROPERTY_BDA_SAMPLE_TIME",
    "KSPROPERTY_BDA_SIGNALTIMEOUTS",
    "KSPROPERTY_BDA_SIGNAL_LOCKED",
    "KSPROPERTY_BDA_SIGNAL_LOCK_CAPS",
    "KSPROPERTY_BDA_SIGNAL_LOCK_TYPE",
    "KSPROPERTY_BDA_SIGNAL_PRESENT",
    "KSPROPERTY_BDA_SIGNAL_QUALITY",
    "KSPROPERTY_BDA_SIGNAL_STATS",
    "KSPROPERTY_BDA_SIGNAL_STRENGTH",
    "KSPROPERTY_BDA_SPECTRAL_INVERSION",
    "KSPROPERTY_BDA_SYMBOL_RATE",
    "KSPROPERTY_BDA_TABLE_SECTION",
    "KSPROPERTY_BDA_TEMPLATE_CONNECTIONS",
    "KSPROPERTY_BDA_TOPOLOGY",
    "KSPROPERTY_BDA_TRANSMISSION_MODE",
    "KSPROPERTY_BDA_VOID_TRANSFORM",
    "KSPROPERTY_BDA_VOID_TRANSFORM_START",
    "KSPROPERTY_BDA_VOID_TRANSFORM_STOP",
    "KSPROPERTY_IDS_BDA_TABLE",
    "KSPROPERTY_IPSINK",
    "KSPROPERTY_IPSINK_ADAPTER_ADDRESS",
    "KSPROPERTY_IPSINK_ADAPTER_DESCRIPTION",
    "KSPROPERTY_IPSINK_MULTICASTLIST",
    "KSPROPSETID_BdaAutodemodulate",
    "KSPROPSETID_BdaCA",
    "KSPROPSETID_BdaDigitalDemodulator",
    "KSPROPSETID_BdaDiseqCommand",
    "KSPROPSETID_BdaEthernetFilter",
    "KSPROPSETID_BdaFrequencyFilter",
    "KSPROPSETID_BdaIPv4Filter",
    "KSPROPSETID_BdaIPv6Filter",
    "KSPROPSETID_BdaLNBInfo",
    "KSPROPSETID_BdaNullTransform",
    "KSPROPSETID_BdaPIDFilter",
    "KSPROPSETID_BdaPinControl",
    "KSPROPSETID_BdaSignalStats",
    "KSPROPSETID_BdaTableSection",
    "KSPROPSETID_BdaTopology",
    "KSPROPSETID_BdaVoidTransform",
    "KSP_BDA_NODE_PIN",
    "KSP_NODE_ESPID",
    "KS_BDA_FRAME_INFO",
    "KS_DATARANGE_BDA_ANTENNA",
    "KS_DATARANGE_BDA_TRANSPORT",
    "LIBID_QuartzNetTypeLib",
    "LIBID_QuartzTypeLib",
    "LIC_BadLicense",
    "LIC_Expired",
    "LIC_ExtenderBlocked",
    "LIC_NeedActivation",
    "LIC_NeedIndiv",
    "LNB_Source",
    "LONG_SECTION",
    "LanguageComponentType",
    "LanguageInfo",
    "LicenseEventBlockReason",
    "LocationCodeSchemeType",
    "Locator",
    "MAX_COUNTRY_CODE_STRING",
    "MAX_DEINTERLACE_DEVICE_GUIDS",
    "MAX_DEINTERLACE_SURFACES",
    "MAX_ERROR_TEXT_LEN",
    "MAX_FILTER_NAME",
    "MAX_NUMBER_OF_STREAMS",
    "MAX_PIN_NAME",
    "MAX_SIZE_MPEG1_SEQUENCE_INFO",
    "MEDIASUBTYPE_ATSC_SI",
    "MEDIASUBTYPE_CPFilters_Processed",
    "MEDIASUBTYPE_DOLBY_AC3",
    "MEDIASUBTYPE_DTS",
    "MEDIASUBTYPE_DVB_SI",
    "MEDIASUBTYPE_DVD_LPCM_AUDIO",
    "MEDIASUBTYPE_DVD_NAVIGATION_DSI",
    "MEDIASUBTYPE_DVD_NAVIGATION_PCI",
    "MEDIASUBTYPE_DVD_NAVIGATION_PROVIDER",
    "MEDIASUBTYPE_DVD_SUBPICTURE",
    "MEDIASUBTYPE_ETDTFilter_Tagged",
    "MEDIASUBTYPE_ISDB_SI",
    "MEDIASUBTYPE_MPEG2DATA",
    "MEDIASUBTYPE_MPEG2_AUDIO",
    "MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_PROCESSED",
    "MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_RAW",
    "MEDIASUBTYPE_MPEG2_PROGRAM",
    "MEDIASUBTYPE_MPEG2_TRANSPORT",
    "MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE",
    "MEDIASUBTYPE_MPEG2_UDCR_TRANSPORT",
    "MEDIASUBTYPE_MPEG2_VERSIONED_TABLES",
    "MEDIASUBTYPE_MPEG2_VIDEO",
    "MEDIASUBTYPE_MPEG2_WMDRM_TRANSPORT",
    "MEDIASUBTYPE_SDDS",
    "MEDIASUBTYPE_TIF_SI",
    "MEDIATYPE_CONTROL",
    "MEDIATYPE_DVD_ENCRYPTED_PACK",
    "MEDIATYPE_DVD_NAVIGATION",
    "MEDIATYPE_MPEG2_PACK",
    "MEDIATYPE_MPEG2_PES",
    "MEDIATYPE_MPEG2_SECTIONS",
    "MEDIA_ELEMENTARY_STREAM",
    "MEDIA_MPEG2_PSI",
    "MEDIA_SAMPLE_CONTENT",
    "MEDIA_TRANSPORT_PACKET",
    "MEDIA_TRANSPORT_PAYLOAD",
    "MERIT_DO_NOT_USE",
    "MERIT_HW_COMPRESSOR",
    "MERIT_NORMAL",
    "MERIT_PREFERRED",
    "MERIT_SW_COMPRESSOR",
    "MERIT_UNLIKELY",
    "MIN_DIMENSION",
    "MMSSF_ASYNCHRONOUS",
    "MMSSF_GET_INFORMATION_FLAGS",
    "MMSSF_HASCLOCK",
    "MMSSF_SUPPORTSEEK",
    "MPAA_G",
    "MPAA_IsBlocked",
    "MPAA_NC17",
    "MPAA_NotApplicable",
    "MPAA_NotRated",
    "MPAA_PG",
    "MPAA_PG13",
    "MPAA_R",
    "MPAA_ValidAttrSubmask",
    "MPAA_X",
    "MPBOOL_FALSE",
    "MPBOOL_TRUE",
    "MPEG1WAVEFORMAT",
    "MPEG2Component",
    "MPEG2ComponentType",
    "MPEG2StreamType",
    "MPEG2StreamType_ANNEX_A_DSM_CC",
    "MPEG2StreamType_BDA_UNITIALIZED_MPEG2STREAMTYPE",
    "MPEG2StreamType_DOLBY_AC3_AUDIO",
    "MPEG2StreamType_DOLBY_DIGITAL_PLUS_AUDIO_ATSC",
    "MPEG2StreamType_HEVC_TEMPORAL_VIDEO_SUBSET",
    "MPEG2StreamType_HEVC_VIDEO_OR_TEMPORAL_VIDEO",
    "MPEG2StreamType_IRPM_STREAMM",
    "MPEG2StreamType_ISO_IEC_11172_2_VIDEO",
    "MPEG2StreamType_ISO_IEC_11172_3_AUDIO",
    "MPEG2StreamType_ISO_IEC_13522_MHEG",
    "MPEG2StreamType_ISO_IEC_13818_1_AUXILIARY",
    "MPEG2StreamType_ISO_IEC_13818_1_PES",
    "MPEG2StreamType_ISO_IEC_13818_1_PRIVATE_SECTION",
    "MPEG2StreamType_ISO_IEC_13818_1_RESERVED",
    "MPEG2StreamType_ISO_IEC_13818_2_VIDEO",
    "MPEG2StreamType_ISO_IEC_13818_3_AUDIO",
    "MPEG2StreamType_ISO_IEC_13818_6_DOWNLOAD",
    "MPEG2StreamType_ISO_IEC_13818_6_TYPE_A",
    "MPEG2StreamType_ISO_IEC_13818_6_TYPE_B",
    "MPEG2StreamType_ISO_IEC_13818_6_TYPE_C",
    "MPEG2StreamType_ISO_IEC_13818_6_TYPE_D",
    "MPEG2StreamType_ISO_IEC_13818_7_AUDIO",
    "MPEG2StreamType_ISO_IEC_14496_1_IN_PES",
    "MPEG2StreamType_ISO_IEC_14496_1_IN_SECTION",
    "MPEG2StreamType_ISO_IEC_14496_2_VISUAL",
    "MPEG2StreamType_ISO_IEC_14496_3_AUDIO",
    "MPEG2StreamType_ISO_IEC_USER_PRIVATE",
    "MPEG2StreamType_ITU_T_H264",
    "MPEG2StreamType_ITU_T_REC_H_222_1",
    "MPEG2StreamType_METADATA_IN_DATA_CAROUSEL",
    "MPEG2StreamType_METADATA_IN_DOWNLOAD_PROTOCOL",
    "MPEG2StreamType_METADATA_IN_OBJECT_CAROUSEL",
    "MPEG2StreamType_METADATA_IN_PES",
    "MPEG2StreamType_METADATA_IN_SECTION",
    "MPEG2StreamType_Reserved1",
    "MPEG2StreamType_USER_PRIVATE",
    "MPEG2TuneRequest",
    "MPEG2TuneRequestFactory",
    "MPEG2_BASE",
    "MPEG2_E_ALREADY_INITIALIZED",
    "MPEG2_E_BUFFER_TOO_SMALL",
    "MPEG2_E_DATA_SOURCE_FAILED",
    "MPEG2_E_DII_NOT_FOUND",
    "MPEG2_E_DSHOW_PIN_NOT_FOUND",
    "MPEG2_E_DSI_NOT_FOUND",
    "MPEG2_E_FILE_OFFSET_TOO_BIG",
    "MPEG2_E_INCORRECT_DESCRIPTOR_TAG",
    "MPEG2_E_INVALID_CAROUSEL_ID",
    "MPEG2_E_INVALID_SG_OBJECT_KIND",
    "MPEG2_E_INVALID_UDP_PORT",
    "MPEG2_E_MALFORMED_DSMCC_MESSAGE",
    "MPEG2_E_MALFORMED_TABLE",
    "MPEG2_E_MISSING_SECTIONS",
    "MPEG2_E_NEXT_TABLE_OPS_NOT_AVAILABLE",
    "MPEG2_E_NOT_PRESENT",
    "MPEG2_E_OBJECT_KIND_NOT_A_DIRECTORY",
    "MPEG2_E_OBJECT_KIND_NOT_A_FILE",
    "MPEG2_E_OBJECT_NOT_FOUND",
    "MPEG2_E_OUT_OF_BOUNDS",
    "MPEG2_E_REGISTRY_ACCESS_FAILED",
    "MPEG2_E_SECTION_NOT_FOUND",
    "MPEG2_E_SERVER_UNAVAILABLE",
    "MPEG2_E_SERVICE_ID_NOT_FOUND",
    "MPEG2_E_SERVICE_PMT_NOT_FOUND",
    "MPEG2_E_STREAM_STOPPED",
    "MPEG2_E_TOO_MANY_SECTIONS",
    "MPEG2_E_TX_STREAM_UNAVAILABLE",
    "MPEG2_E_UNDEFINED",
    "MPEG2_E_UNINITIALIZED",
    "MPEG2_FILTER",
    "MPEG2_FILTER2",
    "MPEG2_FILTER_VERSION_1_SIZE",
    "MPEG2_FILTER_VERSION_2_SIZE",
    "MPEG2_PROGRAM_DIRECTORY_PES_PACKET",
    "MPEG2_PROGRAM_ELEMENTARY_STREAM",
    "MPEG2_PROGRAM_PACK_HEADER",
    "MPEG2_PROGRAM_PES_STREAM",
    "MPEG2_PROGRAM_STREAM_MAP",
    "MPEG2_PROGRAM_SYSTEM_HEADER",
    "MPEG2_S_MORE_DATA_AVAILABLE",
    "MPEG2_S_MPE_INFO_FOUND",
    "MPEG2_S_MPE_INFO_NOT_FOUND",
    "MPEG2_S_NEW_MODULE_VERSION",
    "MPEG2_S_NO_MORE_DATA_AVAILABLE",
    "MPEG2_S_SG_INFO_FOUND",
    "MPEG2_S_SG_INFO_NOT_FOUND",
    "MPEG2_TRANSPORT_STRIDE",
    "MPEGLAYER3WAVEFORMAT",
    "MPEGLAYER3WAVEFORMAT_FLAGS",
    "MPEGLAYER3_FLAG_PADDING_ISO",
    "MPEGLAYER3_FLAG_PADDING_OFF",
    "MPEGLAYER3_FLAG_PADDING_ON",
    "MPEG_BCS_DEMUX",
    "MPEG_CAT_PID",
    "MPEG_CAT_TID",
    "MPEG_CONTEXT",
    "MPEG_CONTEXT_BCS_DEMUX",
    "MPEG_CONTEXT_TYPE",
    "MPEG_CONTEXT_WINSOCK",
    "MPEG_CURRENT_NEXT_BIT",
    "MPEG_DATE",
    "MPEG_DATE_AND_TIME",
    "MPEG_HEADER_BITS",
    "MPEG_HEADER_BITS_MIDL",
    "MPEG_HEADER_VERSION_BITS",
    "MPEG_HEADER_VERSION_BITS_MIDL",
    "MPEG_PACKET_LIST",
    "MPEG_PAT_PID",
    "MPEG_PAT_TID",
    "MPEG_PMT_TID",
    "MPEG_REQUEST_TYPE",
    "MPEG_RQST_GET_PES_STREAM",
    "MPEG_RQST_GET_SECTION",
    "MPEG_RQST_GET_SECTIONS_STREAM",
    "MPEG_RQST_GET_SECTION_ASYNC",
    "MPEG_RQST_GET_TABLE",
    "MPEG_RQST_GET_TABLE_ASYNC",
    "MPEG_RQST_GET_TS_STREAM",
    "MPEG_RQST_PACKET",
    "MPEG_RQST_START_MPE_STREAM",
    "MPEG_RQST_UNKNOWN",
    "MPEG_SECTION_IS_CURRENT",
    "MPEG_SECTION_IS_NEXT",
    "MPEG_SERVICE_REQUEST",
    "MPEG_SERVICE_RESPONSE",
    "MPEG_STREAM_BUFFER",
    "MPEG_STREAM_FILTER",
    "MPEG_TIME",
    "MPEG_TSDT_PID",
    "MPEG_TSDT_TID",
    "MPEG_WINSOCK",
    "MPE_ELEMENT",
    "MPF_ENVLP_BEGIN_CURRENTVAL",
    "MPF_ENVLP_BEGIN_NEUTRALVAL",
    "MPF_ENVLP_STANDARD",
    "MPF_PUNCHIN_NOW",
    "MPF_PUNCHIN_REFTIME",
    "MPF_PUNCHIN_STOPPED",
    "MPT_BOOL",
    "MPT_ENUM",
    "MPT_FLOAT",
    "MPT_INT",
    "MPT_MAX",
    "MP_CURVE_INVSQUARE",
    "MP_CURVE_JUMP",
    "MP_CURVE_LINEAR",
    "MP_CURVE_SINE",
    "MP_CURVE_SQUARE",
    "MP_CURVE_TYPE",
    "MP_ENVELOPE_SEGMENT",
    "MP_PARAMINFO",
    "MP_TYPE",
    "MSDRI_S_MMI_PENDING",
    "MSDRI_S_PENDING",
    "MSEventBinder",
    "MSPID_PrimaryAudio",
    "MSPID_PrimaryVideo",
    "MSTapeDeviceGUID",
    "MSVIDCTL_ALT",
    "MSVIDCTL_CTRL",
    "MSVIDCTL_LEFT_BUTTON",
    "MSVIDCTL_MIDDLE_BUTTON",
    "MSVIDCTL_RIGHT_BUTTON",
    "MSVIDCTL_SHIFT",
    "MSVIDCTL_X_BUTTON1",
    "MSVIDCTL_X_BUTTON2",
    "MSVidAnalogCaptureToCCA",
    "MSVidAnalogCaptureToDataServices",
    "MSVidAnalogCaptureToOverlayMixer",
    "MSVidAnalogCaptureToStreamBufferSink",
    "MSVidAnalogCaptureToXDS",
    "MSVidAnalogTVToEncoder",
    "MSVidAnalogTunerDevice",
    "MSVidAudioRenderer",
    "MSVidAudioRendererDevices",
    "MSVidBDATunerDevice",
    "MSVidCCA",
    "MSVidCCAToStreamBufferSink",
    "MSVidCCService",
    "MSVidCCService_Caption1",
    "MSVidCCService_Caption2",
    "MSVidCCService_None",
    "MSVidCCService_Text1",
    "MSVidCCService_Text2",
    "MSVidCCService_XDS",
    "MSVidCCToAR",
    "MSVidCCToVMR",
    "MSVidClosedCaptioning",
    "MSVidClosedCaptioningSI",
    "MSVidCtl",
    "MSVidCtlButtonstate",
    "MSVidCtlStateList",
    "MSVidDataServices",
    "MSVidDataServicesToStreamBufferSink",
    "MSVidDataServicesToXDS",
    "MSVidDevice",
    "MSVidDevice2",
    "MSVidDigitalCaptureToCCA",
    "MSVidDigitalCaptureToITV",
    "MSVidDigitalCaptureToStreamBufferSink",
    "MSVidEVR",
    "MSVidEncoder",
    "MSVidEncoderToStreamBufferSink",
    "MSVidFeature",
    "MSVidFeatures",
    "MSVidFilePlaybackDevice",
    "MSVidFilePlaybackToAudioRenderer",
    "MSVidFilePlaybackToVideoRenderer",
    "MSVidGenericComposite",
    "MSVidGenericSink",
    "MSVidITVCapture",
    "MSVidITVPlayback",
    "MSVidITVToStreamBufferSink",
    "MSVidInputDevice",
    "MSVidInputDevices",
    "MSVidMPEG2DecoderToClosedCaptioning",
    "MSVidOutput",
    "MSVidOutputDevices",
    "MSVidRect",
    "MSVidSBESourceToCC",
    "MSVidSBESourceToGenericSink",
    "MSVidSBESourceToITV",
    "MSVidSEG_DEST",
    "MSVidSEG_SOURCE",
    "MSVidSEG_XFORM",
    "MSVidSegmentType",
    "MSVidSinkStreams",
    "MSVidSink_Audio",
    "MSVidSink_Other",
    "MSVidSink_Video",
    "MSVidStreamBufferRecordingControl",
    "MSVidStreamBufferSink",
    "MSVidStreamBufferSource",
    "MSVidStreamBufferSourceToVideoRenderer",
    "MSVidStreamBufferV2Source",
    "MSVidVMR9",
    "MSVidVideoInputDevice",
    "MSVidVideoPlaybackDevice",
    "MSVidVideoRenderer",
    "MSVidVideoRendererDevices",
    "MSVidWebDVD",
    "MSVidWebDVDAdm",
    "MSVidWebDVDToAudioRenderer",
    "MSVidWebDVDToVideoRenderer",
    "MSVidXDS",
    "MSViddispidList",
    "MSViddispidList_dispidAudioRenderer",
    "MSViddispidList_dispidAudioRenderers",
    "MSViddispidList_dispidBuild",
    "MSViddispidList_dispidColorKey",
    "MSViddispidList_dispidDecompose",
    "MSViddispidList_dispidDisableAudio",
    "MSViddispidList_dispidDisableVideo",
    "MSViddispidList_dispidDisplaySize",
    "MSViddispidList_dispidFeatures",
    "MSViddispidList_dispidInput",
    "MSViddispidList_dispidInputs",
    "MSViddispidList_dispidMaintainAspectRatio",
    "MSViddispidList_dispidOutput",
    "MSViddispidList_dispidOutputs",
    "MSViddispidList_dispidPause",
    "MSViddispidList_dispidRun",
    "MSViddispidList_dispidSelectedFeatures",
    "MSViddispidList_dispidServiceP",
    "MSViddispidList_dispidStateChange",
    "MSViddispidList_dispidStop",
    "MSViddispidList_dispidVideoRenderer",
    "MSViddispidList_dispidVideoRenderers",
    "MSViddispidList_dispidView",
    "MSViddispidList_dispidViewNext",
    "MSViddispidList_dispid_Inputs",
    "MSViddispidList_dispid_Outputs",
    "MSViddispidList_dispidbind",
    "MSViddispidList_dispidgetState",
    "MSViddispidList_dispidunbind",
    "MUX_PID_TYPE",
    "MainAVIHeader",
    "MixerPref9_ARAdjustXorY",
    "MixerPref9_AnisotropicFiltering",
    "MixerPref9_BiLinearFiltering",
    "MixerPref9_DecimateMask",
    "MixerPref9_DecimateOutput",
    "MixerPref9_DynamicDecimateBy2",
    "MixerPref9_DynamicMask",
    "MixerPref9_DynamicReserved",
    "MixerPref9_DynamicSwitchToBOB",
    "MixerPref9_FilteringMask",
    "MixerPref9_FilteringReserved",
    "MixerPref9_GaussianQuadFiltering",
    "MixerPref9_NoDecimation",
    "MixerPref9_NonSquareMixing",
    "MixerPref9_PointFiltering",
    "MixerPref9_PyramidalQuadFiltering",
    "MixerPref9_RenderTargetMask",
    "MixerPref9_RenderTargetRGB",
    "MixerPref9_RenderTargetReserved",
    "MixerPref9_RenderTargetYUV",
    "MixerPref_ARAdjustXorY",
    "MixerPref_BiLinearFiltering",
    "MixerPref_DecimateMask",
    "MixerPref_DecimateOutput",
    "MixerPref_DecimationReserved",
    "MixerPref_DynamicDecimateBy2",
    "MixerPref_DynamicMask",
    "MixerPref_DynamicReserved",
    "MixerPref_DynamicSwitchToBOB",
    "MixerPref_FilteringMask",
    "MixerPref_NoDecimation",
    "MixerPref_PointFiltering",
    "MixerPref_RenderTargetMask",
    "MixerPref_RenderTargetRGB",
    "MixerPref_RenderTargetReserved",
    "MixerPref_RenderTargetYUV",
    "MixerPref_RenderTargetYUV420",
    "MixerPref_RenderTargetYUV422",
    "MixerPref_RenderTargetYUV444",
    "ModulationType",
    "Mpeg2Data",
    "Mpeg2DataLib",
    "Mpeg2Stream",
    "Mpeg2TableSampleHdr",
    "NORMALIZEDRECT",
    "OAFALSE",
    "OATRUE",
    "OA_BOOL",
    "OCUR_PAIRING_PROTOCOL_VERSION",
    "OUTPUT_STATE",
    "OUTPUT_STATE_Disabled",
    "OUTPUT_STATE_ReadData",
    "OUTPUT_STATE_RenderData",
    "PARENTAL_CONTROL_ATTRIB_DIALOGUE",
    "PARENTAL_CONTROL_ATTRIB_FANTASY",
    "PARENTAL_CONTROL_ATTRIB_LANGUAGE",
    "PARENTAL_CONTROL_ATTRIB_SEXUAL",
    "PARENTAL_CONTROL_ATTRIB_VIOLENCE",
    "PARENTAL_CONTROL_CONTENT_RATING",
    "PARENTAL_CONTROL_TIME_RANGE",
    "PARENTAL_CONTROL_VALUE_UNDEFINED",
    "PBDAParentalControl",
    "PBDA_ALWAYS_TUNE_IN_MUX",
    "PBDA_AUX_CONNECTOR_TYPE_Composite",
    "PBDA_AUX_CONNECTOR_TYPE_SVideo",
    "PBDA_Encoder_Audio_AlgorithmType_AC3",
    "PBDA_Encoder_Audio_AlgorithmType_MPEG1LayerII",
    "PBDA_Encoder_BitrateMode_Average",
    "PBDA_Encoder_BitrateMode_Constant",
    "PBDA_Encoder_BitrateMode_Variable",
    "PBDA_Encoder_Video_AVC",
    "PBDA_Encoder_Video_H264",
    "PBDA_Encoder_Video_MPEG2PartII",
    "PBDA_Encoder_Video_MPEG4Part10",
    "PBDA_PAIRING_PROTOCOL_VERSION",
    "PBDA_TAG_ATTRIBUTE",
    "PDXVA2SW_CREATEVIDEOPROCESSDEVICE",
    "PDXVA2SW_DESTROYVIDEOPROCESSDEVICE",
    "PDXVA2SW_GETFILTERPROPERTYRANGE",
    "PDXVA2SW_GETPROCAMPRANGE",
    "PDXVA2SW_GETVIDEOPROCESSORCAPS",
    "PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETCOUNT",
    "PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETS",
    "PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATCOUNT",
    "PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATS",
    "PDXVA2SW_VIDEOPROCESSBEGINFRAME",
    "PDXVA2SW_VIDEOPROCESSBLT",
    "PDXVA2SW_VIDEOPROCESSENDFRAME",
    "PDXVA2SW_VIDEOPROCESSSETRENDERTARGET",
    "PIC_SEQ_SAMPLE",
    "PIDListSpanningEvent",
    "PID_BITS",
    "PID_BITS_MIDL",
    "PID_ELEMENTARY_STREAM",
    "PID_MAP",
    "PID_MPEG2_SECTION_PSI_SI",
    "PID_OTHER",
    "PINDIR_INPUT",
    "PINDIR_OUTPUT",
    "PINNAME_BDA_ANALOG_AUDIO",
    "PINNAME_BDA_ANALOG_VIDEO",
    "PINNAME_BDA_FM_RADIO",
    "PINNAME_BDA_IF_PIN",
    "PINNAME_BDA_OPENCABLE_PSIP_PIN",
    "PINNAME_BDA_TRANSPORT",
    "PINNAME_IPSINK_INPUT",
    "PINNAME_MPE",
    "PIN_DIRECTION",
    "PIN_INFO",
    "PROT_COPY_BF",
    "PROT_COPY_CN_RECORDING_STOP",
    "PROT_COPY_FREE",
    "PROT_COPY_FREE_CIT",
    "PROT_COPY_FREE_SECURE",
    "PROT_COPY_INVALID",
    "PROT_COPY_NEVER",
    "PROT_COPY_NEVER_REALLY",
    "PROT_COPY_NO_MORE",
    "PROT_COPY_ONCE",
    "PersistTuneXmlUtility",
    "PhysConn_Audio_1394",
    "PhysConn_Audio_AESDigital",
    "PhysConn_Audio_AUX",
    "PhysConn_Audio_AudioDecoder",
    "PhysConn_Audio_Line",
    "PhysConn_Audio_Mic",
    "PhysConn_Audio_SCSI",
    "PhysConn_Audio_SPDIFDigital",
    "PhysConn_Audio_Tuner",
    "PhysConn_Audio_USB",
    "PhysConn_Video_1394",
    "PhysConn_Video_AUX",
    "PhysConn_Video_Black",
    "PhysConn_Video_Composite",
    "PhysConn_Video_ParallelDigital",
    "PhysConn_Video_RGB",
    "PhysConn_Video_SCART",
    "PhysConn_Video_SCSI",
    "PhysConn_Video_SVideo",
    "PhysConn_Video_SerialDigital",
    "PhysConn_Video_Tuner",
    "PhysConn_Video_USB",
    "PhysConn_Video_VideoDecoder",
    "PhysConn_Video_VideoEncoder",
    "PhysConn_Video_YRYBY",
    "PhysicalConnectorType",
    "Pilot",
    "Polarisation",
    "PositionModeList",
    "PositionModeList_FrameMode",
    "PositionModeList_TenthsSecondsMode",
    "ProcAmpControl9_Brightness",
    "ProcAmpControl9_Contrast",
    "ProcAmpControl9_Hue",
    "ProcAmpControl9_Mask",
    "ProcAmpControl9_Saturation",
    "ProgramElement",
    "ProtType",
    "Quality",
    "QualityMessageType",
    "QualityMessageType_Famine",
    "QualityMessageType_Flood",
    "RATING_ATTRIBUTE",
    "RATING_INFO",
    "RATING_SYSTEM",
    "RECORDING_STARTED",
    "RECORDING_STOPPED",
    "RECORDING_TYPE",
    "RECORDING_TYPE_CONTENT",
    "RECORDING_TYPE_REFERENCE",
    "REFERENCE",
    "REGFILTER",
    "REGFILTER2",
    "REGFILTERPINS",
    "REGFILTERPINS2",
    "REGPINMEDIUM",
    "REGPINTYPES",
    "REG_PINFLAG",
    "REG_PINFLAG_B_MANY",
    "REG_PINFLAG_B_OUTPUT",
    "REG_PINFLAG_B_RENDERER",
    "REG_PINFLAG_B_ZERO",
    "REMFILTERF_LEAVECONNECTED",
    "REQUIRED_PARENTAL_CONTROL_TIME_RANGE",
    "REVOKED_APP_STUB",
    "REVOKED_COPP",
    "REVOKED_MAX_TYPES",
    "REVOKED_SAC",
    "REVOKED_SECURE_PIPELINE",
    "RIFFCHUNK",
    "RIFFLIST",
    "RecordingType",
    "RenderPrefs9_DoNotRenderBorder",
    "RenderPrefs9_Mask",
    "RenderPrefs_AllowOffscreen",
    "RenderPrefs_AllowOverlays",
    "RenderPrefs_DoNotRenderColorKeyAndBorder",
    "RenderPrefs_ForceOffscreen",
    "RenderPrefs_ForceOverlays",
    "RenderPrefs_Mask",
    "RenderPrefs_PreferAGPMemWhenMixing",
    "RenderPrefs_Reserved",
    "RenderPrefs_RestrictToInitialMonitor",
    "RevokedComponent",
    "RollOff",
    "SAMPLE_LIVE_STREAM_TIME",
    "SAMPLE_SEQ_CONTENT_B_FRAME",
    "SAMPLE_SEQ_CONTENT_I_FRAME",
    "SAMPLE_SEQ_CONTENT_NONREF_FRAME",
    "SAMPLE_SEQ_CONTENT_P_FRAME",
    "SAMPLE_SEQ_CONTENT_REF_FRAME",
    "SAMPLE_SEQ_CONTENT_STANDALONE_FRAME",
    "SAMPLE_SEQ_CONTENT_UNKNOWN",
    "SAMPLE_SEQ_FRAME_START",
    "SAMPLE_SEQ_GOP_HEADER",
    "SAMPLE_SEQ_OFFSET",
    "SAMPLE_SEQ_PICTURE_HEADER",
    "SAMPLE_SEQ_SEEK_POINT",
    "SAMPLE_SEQ_SEQUENCE_HEADER",
    "SAMPLE_SEQ_SEQUENCE_START",
    "SBE2_STREAM_DESC",
    "SBE2_STREAM_DESC_EVENT",
    "SBE2_STREAM_DESC_VERSION",
    "SBE2_V1_STREAMS_CREATION_EVENT",
    "SBE2_V2_STREAMS_CREATION_EVENT",
    "SBE_PIN_DATA",
    "SCTE28_ConditionalAccess",
    "SCTE28_CopyProtection",
    "SCTE28_Diagnostic",
    "SCTE28_IPService",
    "SCTE28_NetworkInterface_SCTE55_1",
    "SCTE28_NetworkInterface_SCTE55_2",
    "SCTE28_POD_Host_Binding_Information",
    "SCTE28_Reserved",
    "SCTE28_Undesignated",
    "SCTE_18",
    "SCTE_EAS_IB_PID",
    "SCTE_EAS_OOB_PID",
    "SCTE_EAS_TID",
    "SECTION",
    "SID_DRMSecureServiceChannel",
    "SID_MSVidCtl_CurrentAudioEndpoint",
    "SNDDEV_ERR",
    "SNDDEV_ERROR_AddBuffer",
    "SNDDEV_ERROR_Close",
    "SNDDEV_ERROR_GetCaps",
    "SNDDEV_ERROR_GetPosition",
    "SNDDEV_ERROR_Open",
    "SNDDEV_ERROR_Pause",
    "SNDDEV_ERROR_PrepareHeader",
    "SNDDEV_ERROR_Query",
    "SNDDEV_ERROR_Reset",
    "SNDDEV_ERROR_Restart",
    "SNDDEV_ERROR_Start",
    "SNDDEV_ERROR_Stop",
    "SNDDEV_ERROR_UnprepareHeader",
    "SNDDEV_ERROR_Write",
    "SPECIFYPAGES_STATISTICS",
    "SSUPDATE_ASYNC",
    "SSUPDATE_CONTINUOUS",
    "SSUPDATE_TYPE",
    "STATE_PAUSE",
    "STATE_PLAY",
    "STATE_STOP",
    "STATE_UNBUILT",
    "STDINDEXSIZE",
    "STRCONV_MODE_DVB",
    "STRCONV_MODE_DVB_EMPHASIS",
    "STRCONV_MODE_DVB_WITHOUT_EMPHASIS",
    "STRCONV_MODE_ISDB",
    "STREAMBUFFER_ATTRIBUTE",
    "STREAMBUFFER_ATTR_DATATYPE",
    "STREAMBUFFER_EC_BASE",
    "STREAMBUFFER_EC_CONTENT_BECOMING_STALE",
    "STREAMBUFFER_EC_PRIMARY_AUDIO",
    "STREAMBUFFER_EC_RATE_CHANGED",
    "STREAMBUFFER_EC_RATE_CHANGING_FOR_SETPOSITIONS",
    "STREAMBUFFER_EC_READ_FAILURE",
    "STREAMBUFFER_EC_SETPOSITIONS_EVENTS_DONE",
    "STREAMBUFFER_EC_STALE_DATA_READ",
    "STREAMBUFFER_EC_STALE_FILE_DELETED",
    "STREAMBUFFER_EC_TIMEHOLE",
    "STREAMBUFFER_EC_WRITE_FAILURE",
    "STREAMBUFFER_EC_WRITE_FAILURE_CLEAR",
    "STREAMBUFFER_TYPE_BINARY",
    "STREAMBUFFER_TYPE_BOOL",
    "STREAMBUFFER_TYPE_DWORD",
    "STREAMBUFFER_TYPE_GUID",
    "STREAMBUFFER_TYPE_QWORD",
    "STREAMBUFFER_TYPE_STRING",
    "STREAMBUFFER_TYPE_WORD",
    "STREAMIF_CONSTANTS",
    "STREAMSTATE_RUN",
    "STREAMSTATE_STOP",
    "STREAMTYPE_READ",
    "STREAMTYPE_TRANSFORM",
    "STREAMTYPE_WRITE",
    "STREAM_ID_MAP",
    "STREAM_STATE",
    "STREAM_TYPE",
    "SUBSTREAM_FILTER_VAL_NONE",
    "ScanModulationTypes",
    "ScanModulationTypesMask_DVBC",
    "ScanModulationTypesMask_MCE_All_TV",
    "ScanModulationTypesMask_MCE_AnalogTv",
    "ScanModulationTypesMask_MCE_DigitalCable",
    "ScanModulationTypesMask_MCE_TerrestrialATSC",
    "SectionList",
    "SegDispidList",
    "SegDispidList_LastReservedDeviceDispid",
    "SegDispidList_dispidAllocPresentID",
    "SegDispidList_dispidAlloctor",
    "SegDispidList_dispidAuxInputs",
    "SegDispidList_dispidAvailableSourceRect",
    "SegDispidList_dispidBookmarkOnStop",
    "SegDispidList_dispidCCEnable",
    "SegDispidList_dispidCLSID",
    "SegDispidList_dispidCapture",
    "SegDispidList_dispidChangePassword",
    "SegDispidList_dispidChannelAvailable",
    "SegDispidList_dispidClip",
    "SegDispidList_dispidClippedSourceRect",
    "SegDispidList_dispidConfirmPassword",
    "SegDispidList_dispidCount",
    "SegDispidList_dispidCustomCompositorClass",
    "SegDispidList_dispidDefaultAudioLCID",
    "SegDispidList_dispidDefaultMenuLCID",
    "SegDispidList_dispidDefaultSubpictureLCID",
    "SegDispidList_dispidDevAudioFrequency",
    "SegDispidList_dispidDevAudioSubchannel",
    "SegDispidList_dispidDevBalance",
    "SegDispidList_dispidDevCanStep",
    "SegDispidList_dispidDevCountryCode",
    "SegDispidList_dispidDevFileName",
    "SegDispidList_dispidDevImageSourceHeight",
    "SegDispidList_dispidDevImageSourceWidth",
    "SegDispidList_dispidDevOverScan",
    "SegDispidList_dispidDevPause",
    "SegDispidList_dispidDevPower",
    "SegDispidList_dispidDevRun",
    "SegDispidList_dispidDevSAP",
    "SegDispidList_dispidDevStep",
    "SegDispidList_dispidDevStop",
    "SegDispidList_dispidDevVideoFrequency",
    "SegDispidList_dispidDevVideoSubchannel",
    "SegDispidList_dispidDevView",
    "SegDispidList_dispidDevVolume",
    "SegDispidList_dispidDevicePath",
    "SegDispidList_dispidDisplayChange",
    "SegDispidList_dispidGetParentalCountry",
    "SegDispidList_dispidGetParentalLevel",
    "SegDispidList_dispidKSCat",
    "SegDispidList_dispidMaxVidRect",
    "SegDispidList_dispidMediaPosition",
    "SegDispidList_dispidMessageDrain",
    "SegDispidList_dispidMinVidRect",
    "SegDispidList_dispidMixerBitmap",
    "SegDispidList_dispidMixerBitmapOpacity",
    "SegDispidList_dispidMixerBitmapRect",
    "SegDispidList_dispidModes",
    "SegDispidList_dispidName",
    "SegDispidList_dispidNameSetLock",
    "SegDispidList_dispidOwner",
    "SegDispidList_dispidRateEx",
    "SegDispidList_dispidRePaint",
    "SegDispidList_dispidRecordingAttribute",
    "SegDispidList_dispidRequestedClipRect",
    "SegDispidList_dispidSBEConfigure",
    "SegDispidList_dispidSaveParentalCountry",
    "SegDispidList_dispidSaveParentalLevel",
    "SegDispidList_dispidSegment",
    "SegDispidList_dispidService",
    "SegDispidList_dispidSetAllocator",
    "SegDispidList_dispidSetMinSeek",
    "SegDispidList_dispidSetSinkFilter",
    "SegDispidList_dispidSetupMixerBitmap",
    "SegDispidList_dispidSourceSize",
    "SegDispidList_dispidStatus",
    "SegDispidList_dispidStreamBufferContentRecording",
    "SegDispidList_dispidStreamBufferReferenceRecording",
    "SegDispidList_dispidStreamBufferSinkName",
    "SegDispidList_dispidStreamBufferSourceName",
    "SegDispidList_dispidTS",
    "SegDispidList_dispidTVFormats",
    "SegDispidList_dispidTeleTextFilter",
    "SegDispidList_dispidTune",
    "SegDispidList_dispidTuneChan",
    "SegDispidList_dispidUnlockProfile",
    "SegDispidList_dispidUserEvent",
    "SegDispidList_dispidUsingOverlay",
    "SegDispidList_dispidViewable",
    "SegDispidList_dispidVisible",
    "SegDispidList_dispid_AcceptParentalLevelChange",
    "SegDispidList_dispid_ActivateAtPosition",
    "SegDispidList_dispid_ActivateButton",
    "SegDispidList_dispid_AddFilter",
    "SegDispidList_dispid_Allocator",
    "SegDispidList_dispid_AnglesAvailable",
    "SegDispidList_dispid_AudioStreamsAvailable",
    "SegDispidList_dispid_BlockUnrated",
    "SegDispidList_dispid_Bookmark",
    "SegDispidList_dispid_ButtonAtPosition",
    "SegDispidList_dispid_ButtonRect",
    "SegDispidList_dispid_CCActive",
    "SegDispidList_dispid_CLSID",
    "SegDispidList_dispid_CurrentAngle",
    "SegDispidList_dispid_CurrentAudioStream",
    "SegDispidList_dispid_CurrentCCService",
    "SegDispidList_dispid_CurrentChapter",
    "SegDispidList_dispid_CurrentDiscSide",
    "SegDispidList_dispid_CurrentDomain",
    "SegDispidList_dispid_CurrentRatings",
    "SegDispidList_dispid_CurrentSubpictureStream",
    "SegDispidList_dispid_CurrentTime",
    "SegDispidList_dispid_CurrentTitle",
    "SegDispidList_dispid_CurrentVolume",
    "SegDispidList_dispid_CustomCompositor",
    "SegDispidList_dispid_CustomCompositorClass",
    "SegDispidList_dispid_DVDAdm",
    "SegDispidList_dispid_DVDDirectory",
    "SegDispidList_dispid_DVDScreenInMouseCoordinates",
    "SegDispidList_dispid_DVDTextLanguageLCID",
    "SegDispidList_dispid_DVDTextNumberOfLanguages",
    "SegDispidList_dispid_DVDTextNumberOfStrings",
    "SegDispidList_dispid_DVDTextString",
    "SegDispidList_dispid_DVDTextStringType",
    "SegDispidList_dispid_DVDTimeCode2bstr",
    "SegDispidList_dispid_DVDUniqueID",
    "SegDispidList_dispid_DecimateInput",
    "SegDispidList_dispid_DefaultAudioLanguage",
    "SegDispidList_dispid_DefaultAudioLanguageExt",
    "SegDispidList_dispid_DefaultMenuLanguage",
    "SegDispidList_dispid_DefaultSubpictureLanguage",
    "SegDispidList_dispid_DefaultSubpictureLanguageExt",
    "SegDispidList_dispid_DeleteBookmark",
    "SegDispidList_dispid_Eject",
    "SegDispidList_dispid_EnableResetOnStop",
    "SegDispidList_dispid_FramesPerSecond",
    "SegDispidList_dispid_GPRM",
    "SegDispidList_dispid_IsAudioStreamEnabled",
    "SegDispidList_dispid_IsEqualDevice",
    "SegDispidList_dispid_IsSubpictureStreamEnabled",
    "SegDispidList_dispid_KSCat",
    "SegDispidList_dispid_KaraokeAudioPresentationMode",
    "SegDispidList_dispid_KaraokeChannelAssignment",
    "SegDispidList_dispid_KaraokeChannelContent",
    "SegDispidList_dispid_LanguageFromLCID",
    "SegDispidList_dispid_MaxRatingsLevel",
    "SegDispidList_dispid_MixerBitmap",
    "SegDispidList_dispid_NotifyParentalLevelChange",
    "SegDispidList_dispid_NumberOfChapters",
    "SegDispidList_dispid_PlayerParentalCountry",
    "SegDispidList_dispid_PlayerParentalLevel",
    "SegDispidList_dispid_PreferredSubpictureStream",
    "SegDispidList_dispid_RecordingAttribute",
    "SegDispidList_dispid_RegionChange",
    "SegDispidList_dispid_RestoreBookmark",
    "SegDispidList_dispid_RestorePreferredSettings",
    "SegDispidList_dispid_SPRM",
    "SegDispidList_dispid_SaveBookmark",
    "SegDispidList_dispid_SelectAndActivateButton",
    "SegDispidList_dispid_SelectAtPosition",
    "SegDispidList_dispid_SelectDefaultAudioLanguage",
    "SegDispidList_dispid_SelectDefaultSubpictureLanguage",
    "SegDispidList_dispid_SelectLeftButton",
    "SegDispidList_dispid_SelectLowerButton",
    "SegDispidList_dispid_SelectParentalCountry",
    "SegDispidList_dispid_SelectParentalLevel",
    "SegDispidList_dispid_SelectRightButton",
    "SegDispidList_dispid_SelectUpperButton",
    "SegDispidList_dispid_SetAllocator",
    "SegDispidList_dispid_SinkStreams",
    "SegDispidList_dispid_SourceFilter",
    "SegDispidList_dispid_SubpictureLanguage",
    "SegDispidList_dispid_SubpictureOn",
    "SegDispidList_dispid_SubpictureStreamsAvailable",
    "SegDispidList_dispid_SuppressEffects",
    "SegDispidList_dispid_TitleParentalLevels",
    "SegDispidList_dispid_TitlesAvailable",
    "SegDispidList_dispid_TotalTitleTime",
    "SegDispidList_dispid_UOPValid",
    "SegDispidList_dispid_UnratedDelay",
    "SegDispidList_dispid_VolumesAvailable",
    "SegDispidList_dispid__SourceFilter",
    "SegDispidList_dispid_audiocounter",
    "SegDispidList_dispid_audioencoderint",
    "SegDispidList_dispid_audiolanguage",
    "SegDispidList_dispid_buttonsavailable",
    "SegDispidList_dispid_cccounter",
    "SegDispidList_dispid_channelchangeint",
    "SegDispidList_dispid_currentbutton",
    "SegDispidList_dispid_playattime",
    "SegDispidList_dispid_playattimeintitle",
    "SegDispidList_dispid_playbackwards",
    "SegDispidList_dispid_playchapter",
    "SegDispidList_dispid_playchapterintitle",
    "SegDispidList_dispid_playchaptersautostop",
    "SegDispidList_dispid_playforwards",
    "SegDispidList_dispid_playnextchapter",
    "SegDispidList_dispid_playperiodintitleautostop",
    "SegDispidList_dispid_playprevchapter",
    "SegDispidList_dispid_playtitle",
    "SegDispidList_dispid_replaychapter",
    "SegDispidList_dispid_resetFilterList",
    "SegDispidList_dispid_resume",
    "SegDispidList_dispid_returnfromsubmenu",
    "SegDispidList_dispid_showmenu",
    "SegDispidList_dispid_stilloff",
    "SegDispidList_dispid_videocounter",
    "SegDispidList_dispid_videoencoderint",
    "SegDispidList_dispid_wstcounter",
    "SegDispidList_dispidaudio_analysis",
    "SegDispidList_dispidaudioanalysis",
    "SegDispidList_dispidaudiocounter",
    "SegDispidList_dispidcccounter",
    "SegDispidList_dispiddata_analysis",
    "SegDispidList_dispiddataanalysis",
    "SegDispidList_dispidlength",
    "SegDispidList_dispidposition",
    "SegDispidList_dispidpositionmode",
    "SegDispidList_dispidrate",
    "SegDispidList_dispidrecordingstarted",
    "SegDispidList_dispidrecordingstopped",
    "SegDispidList_dispidrecordingtype",
    "SegDispidList_dispidsbesource",
    "SegDispidList_dispidstart",
    "SegDispidList_dispidstarttime",
    "SegDispidList_dispidstoptime",
    "SegDispidList_dispidvideo_analysis",
    "SegDispidList_dispidvideoanalysis",
    "SegDispidList_dispidvideocounter",
    "SegDispidList_dispidwstcounter",
    "SegEventidList",
    "SegEventidList_LastReservedDeviceEvent",
    "SegEventidList_dispidAVAudioChannelConfigEvent",
    "SegEventidList_dispidAVAudioChannelCountEvent",
    "SegEventidList_dispidAVAudioSampleRateEvent",
    "SegEventidList_dispidAVDDSurroundModeEvent",
    "SegEventidList_dispidAVDecAudioDualMonoEvent",
    "SegEventidList_dispidAVDecCommonInputFormatEvent",
    "SegEventidList_dispidAVDecCommonMeanBitRateEvent",
    "SegEventidList_dispidAVDecCommonOutputFormatEvent",
    "SegEventidList_dispidlicenseerrorcode",
    "SegEventidList_eventidBroadcastEvent",
    "SegEventidList_eventidBroadcastEventEx",
    "SegEventidList_eventidCOPPBlocked",
    "SegEventidList_eventidCOPPUnblocked",
    "SegEventidList_eventidChangeCurrentAngle",
    "SegEventidList_eventidChangeCurrentAudioStream",
    "SegEventidList_eventidChangeCurrentSubpictureStream",
    "SegEventidList_eventidChangeKaraokePresMode",
    "SegEventidList_eventidChangeVideoPresMode",
    "SegEventidList_eventidContentBecomingStale",
    "SegEventidList_eventidContentPrimarilyAudio",
    "SegEventidList_eventidDVDNotify",
    "SegEventidList_eventidEncryptionOff",
    "SegEventidList_eventidEncryptionOn",
    "SegEventidList_eventidEndOfMedia",
    "SegEventidList_eventidLicenseChange",
    "SegEventidList_eventidOnTuneChanged",
    "SegEventidList_eventidOverlayUnavailable",
    "SegEventidList_eventidPauseOn",
    "SegEventidList_eventidPlayAtTime",
    "SegEventidList_eventidPlayAtTimeInTitle",
    "SegEventidList_eventidPlayBackwards",
    "SegEventidList_eventidPlayChapter",
    "SegEventidList_eventidPlayChapterInTitle",
    "SegEventidList_eventidPlayForwards",
    "SegEventidList_eventidPlayNextChapter",
    "SegEventidList_eventidPlayPrevChapter",
    "SegEventidList_eventidPlayTitle",
    "SegEventidList_eventidRateChange",
    "SegEventidList_eventidRatingsBlocked",
    "SegEventidList_eventidRatingsChanged",
    "SegEventidList_eventidRatingsUnlocked",
    "SegEventidList_eventidReplayChapter",
    "SegEventidList_eventidResume",
    "SegEventidList_eventidReturnFromSubmenu",
    "SegEventidList_eventidSelectOrActivateButton",
    "SegEventidList_eventidShowMenu",
    "SegEventidList_eventidSinkCertificateFailure",
    "SegEventidList_eventidSinkCertificateSuccess",
    "SegEventidList_eventidSourceCertificateFailure",
    "SegEventidList_eventidSourceCertificateSuccess",
    "SegEventidList_eventidStaleDataRead",
    "SegEventidList_eventidStaleFileDeleted",
    "SegEventidList_eventidStateChange",
    "SegEventidList_eventidStillOff",
    "SegEventidList_eventidStop",
    "SegEventidList_eventidTimeHole",
    "SegEventidList_eventidWriteFailure",
    "SegEventidList_eventidWriteFailureClear",
    "SignalAndServiceStatusSpanningEvent_AllAVScrambled",
    "SignalAndServiceStatusSpanningEvent_Clear",
    "SignalAndServiceStatusSpanningEvent_NoSubscription",
    "SignalAndServiceStatusSpanningEvent_NoTVSignal",
    "SignalAndServiceStatusSpanningEvent_None",
    "SignalAndServiceStatusSpanningEvent_ServiceOffAir",
    "SignalAndServiceStatusSpanningEvent_State",
    "SignalAndServiceStatusSpanningEvent_WeakTVSignal",
    "SmartCardApplication",
    "SmartCardAssociationType",
    "SmartCardAssociationType_Associated",
    "SmartCardAssociationType_AssociationUnknown",
    "SmartCardAssociationType_NotAssociated",
    "SmartCardStatusType",
    "SmartCardStatusType_CardDataChanged",
    "SmartCardStatusType_CardError",
    "SmartCardStatusType_CardFirmwareUpgrade",
    "SmartCardStatusType_CardInserted",
    "SmartCardStatusType_CardRemoved",
    "SourceSizeList",
    "SourceSizeList_sslClipByClipRect",
    "SourceSizeList_sslClipByOverScan",
    "SourceSizeList_sslFullSize",
    "SpanningEventDescriptor",
    "SpanningEventEmmMessage",
    "SpectralInversion",
    "State_Paused",
    "State_Running",
    "State_Stopped",
    "SystemTuningSpaces",
    "TID_EXTENSION",
    "TIFLoad",
    "TIMECODEDATA",
    "TIMECODE_RATE_30DROP",
    "TIMECODE_SMPTE_BINARY_GROUP",
    "TIMECODE_SMPTE_COLOR_FRAME",
    "TRANSPORT_PROPERTIES",
    "TRUECOLORINFO",
    "TVAudioMode",
    "TransmissionMode",
    "TuneRequest",
    "TunerInputType",
    "TunerInputType_TunerInputAntenna",
    "TunerInputType_TunerInputCable",
    "TunerMarshaler",
    "TuningSpace",
    "TvRat_0",
    "TvRat_1",
    "TvRat_10",
    "TvRat_11",
    "TvRat_12",
    "TvRat_13",
    "TvRat_14",
    "TvRat_15",
    "TvRat_16",
    "TvRat_17",
    "TvRat_18",
    "TvRat_19",
    "TvRat_2",
    "TvRat_20",
    "TvRat_21",
    "TvRat_3",
    "TvRat_4",
    "TvRat_5",
    "TvRat_6",
    "TvRat_7",
    "TvRat_8",
    "TvRat_9",
    "TvRat_LevelDontKnow",
    "TvRat_Unblock",
    "TvRat_kLevels",
    "UDCR_TAG",
    "UICloseReasonType",
    "UICloseReasonType_DeviceClosed",
    "UICloseReasonType_ErrorClosed",
    "UICloseReasonType_NotReady",
    "UICloseReasonType_SystemClosed",
    "UICloseReasonType_UserClosed",
    "UOP_FLAG_Pause_On",
    "UOP_FLAG_PlayNext_Chapter",
    "UOP_FLAG_PlayPrev_Or_Replay_Chapter",
    "UOP_FLAG_Play_Backwards",
    "UOP_FLAG_Play_Chapter",
    "UOP_FLAG_Play_Chapter_Or_AtTime",
    "UOP_FLAG_Play_Forwards",
    "UOP_FLAG_Play_Title",
    "UOP_FLAG_Play_Title_Or_AtTime",
    "UOP_FLAG_Resume",
    "UOP_FLAG_ReturnFromSubMenu",
    "UOP_FLAG_Select_Angle",
    "UOP_FLAG_Select_Audio_Stream",
    "UOP_FLAG_Select_Karaoke_Audio_Presentation_Mode",
    "UOP_FLAG_Select_Or_Activate_Button",
    "UOP_FLAG_Select_SubPic_Stream",
    "UOP_FLAG_Select_Video_Mode_Preference",
    "UOP_FLAG_ShowMenu_Angle",
    "UOP_FLAG_ShowMenu_Audio",
    "UOP_FLAG_ShowMenu_Chapter",
    "UOP_FLAG_ShowMenu_Root",
    "UOP_FLAG_ShowMenu_SubPic",
    "UOP_FLAG_ShowMenu_Title",
    "UOP_FLAG_Still_Off",
    "UOP_FLAG_Stop",
    "US_TV_14",
    "US_TV_G",
    "US_TV_IsAdultLanguage",
    "US_TV_IsBlocked",
    "US_TV_IsSexualSituation",
    "US_TV_IsSexuallySuggestiveDialog",
    "US_TV_IsViolent",
    "US_TV_MA",
    "US_TV_None",
    "US_TV_None7",
    "US_TV_PG",
    "US_TV_ValidAttrSubmask",
    "US_TV_Y",
    "US_TV_Y7",
    "VALID_UOP_FLAG",
    "VA_COLOR_PRIMARIES",
    "VA_MATRIX_COEFFICIENTS",
    "VA_MATRIX_COEFF_FCC",
    "VA_MATRIX_COEFF_H264_RGB",
    "VA_MATRIX_COEFF_H264_YCgCo",
    "VA_MATRIX_COEFF_ITU_R_BT_470_SYSTEM_B_G",
    "VA_MATRIX_COEFF_ITU_R_BT_709",
    "VA_MATRIX_COEFF_SMPTE_170M",
    "VA_MATRIX_COEFF_SMPTE_240M",
    "VA_MATRIX_COEFF_UNSPECIFIED",
    "VA_OPTIONAL_VIDEO_PROPERTIES",
    "VA_PRIMARIES_H264_GENERIC_FILM",
    "VA_PRIMARIES_ITU_R_BT_470_SYSTEM_B_G",
    "VA_PRIMARIES_ITU_R_BT_470_SYSTEM_M",
    "VA_PRIMARIES_ITU_R_BT_709",
    "VA_PRIMARIES_SMPTE_170M",
    "VA_PRIMARIES_SMPTE_240M",
    "VA_PRIMARIES_UNSPECIFIED",
    "VA_TRANSFER_CHARACTERISTICS",
    "VA_TRANSFER_CHARACTERISTICS_H264_LOG_100_TO_1",
    "VA_TRANSFER_CHARACTERISTICS_H264_LOG_316_TO_1",
    "VA_TRANSFER_CHARACTERISTICS_ITU_R_BT_470_SYSTEM_B_G",
    "VA_TRANSFER_CHARACTERISTICS_ITU_R_BT_470_SYSTEM_M",
    "VA_TRANSFER_CHARACTERISTICS_ITU_R_BT_709",
    "VA_TRANSFER_CHARACTERISTICS_LINEAR",
    "VA_TRANSFER_CHARACTERISTICS_SMPTE_170M",
    "VA_TRANSFER_CHARACTERISTICS_SMPTE_240M",
    "VA_TRANSFER_CHARACTERISTICS_UNSPECIFIED",
    "VA_VIDEO_COMPONENT",
    "VA_VIDEO_FORMAT",
    "VA_VIDEO_MAC",
    "VA_VIDEO_NTSC",
    "VA_VIDEO_PAL",
    "VA_VIDEO_SECAM",
    "VA_VIDEO_UNSPECIFIED",
    "VFW_E_ADVISE_ALREADY_SET",
    "VFW_E_ALREADY_CANCELLED",
    "VFW_E_ALREADY_COMMITTED",
    "VFW_E_ALREADY_CONNECTED",
    "VFW_E_BADALIGN",
    "VFW_E_BAD_KEY",
    "VFW_E_BAD_VIDEOCD",
    "VFW_E_BUFFERS_OUTSTANDING",
    "VFW_E_BUFFER_NOTSET",
    "VFW_E_BUFFER_OVERFLOW",
    "VFW_E_BUFFER_UNDERFLOW",
    "VFW_E_CANNOT_CONNECT",
    "VFW_E_CANNOT_LOAD_SOURCE_FILTER",
    "VFW_E_CANNOT_RENDER",
    "VFW_E_CERTIFICATION_FAILURE",
    "VFW_E_CHANGING_FORMAT",
    "VFW_E_CIRCULAR_GRAPH",
    "VFW_E_CODECAPI_ENUMERATED",
    "VFW_E_CODECAPI_LINEAR_RANGE",
    "VFW_E_CODECAPI_NO_CURRENT_VALUE",
    "VFW_E_CODECAPI_NO_DEFAULT",
    "VFW_E_COLOR_KEY_SET",
    "VFW_E_COPYPROT_FAILED",
    "VFW_E_CORRUPT_GRAPH_FILE",
    "VFW_E_DDRAW_CAPS_NOT_SUITABLE",
    "VFW_E_DDRAW_VERSION_NOT_SUITABLE",
    "VFW_E_DUPLICATE_NAME",
    "VFW_E_DVD_CHAPTER_DOES_NOT_EXIST",
    "VFW_E_DVD_CMD_CANCELLED",
    "VFW_E_DVD_DECNOTENOUGH",
    "VFW_E_DVD_GRAPHNOTREADY",
    "VFW_E_DVD_INCOMPATIBLE_REGION",
    "VFW_E_DVD_INVALIDDOMAIN",
    "VFW_E_DVD_INVALID_DISC",
    "VFW_E_DVD_LOW_PARENTAL_LEVEL",
    "VFW_E_DVD_MENU_DOES_NOT_EXIST",
    "VFW_E_DVD_NONBLOCKING",
    "VFW_E_DVD_NON_EVR_RENDERER_IN_FILTER_GRAPH",
    "VFW_E_DVD_NOT_IN_KARAOKE_MODE",
    "VFW_E_DVD_NO_ATTRIBUTES",
    "VFW_E_DVD_NO_BUTTON",
    "VFW_E_DVD_NO_GOUP_PGC",
    "VFW_E_DVD_NO_RESUME_INFORMATION",
    "VFW_E_DVD_OPERATION_INHIBITED",
    "VFW_E_DVD_RENDERFAIL",
    "VFW_E_DVD_RESOLUTION_ERROR",
    "VFW_E_DVD_STATE_CORRUPT",
    "VFW_E_DVD_STATE_WRONG_DISC",
    "VFW_E_DVD_STATE_WRONG_VERSION",
    "VFW_E_DVD_STREAM_DISABLED",
    "VFW_E_DVD_TITLE_UNKNOWN",
    "VFW_E_DVD_TOO_MANY_RENDERERS_IN_FILTER_GRAPH",
    "VFW_E_DVD_VMR9_INCOMPATIBLEDEC",
    "VFW_E_DVD_WRONG_SPEED",
    "VFW_E_ENUM_OUT_OF_RANGE",
    "VFW_E_ENUM_OUT_OF_SYNC",
    "VFW_E_FILE_TOO_SHORT",
    "VFW_E_FILTER_ACTIVE",
    "VFW_E_FRAME_STEP_UNSUPPORTED",
    "VFW_E_INVALIDMEDIATYPE",
    "VFW_E_INVALIDSUBTYPE",
    "VFW_E_INVALID_CLSID",
    "VFW_E_INVALID_DIRECTION",
    "VFW_E_INVALID_FILE_FORMAT",
    "VFW_E_INVALID_FILE_VERSION",
    "VFW_E_INVALID_MEDIA_TYPE",
    "VFW_E_INVALID_RECT",
    "VFW_E_IN_FULLSCREEN_MODE",
    "VFW_E_MEDIA_TIME_NOT_SET",
    "VFW_E_MONO_AUDIO_HW",
    "VFW_E_MPEG_NOT_CONSTRAINED",
    "VFW_E_NEED_OWNER",
    "VFW_E_NOT_ALLOWED_TO_SAVE",
    "VFW_E_NOT_COMMITTED",
    "VFW_E_NOT_CONNECTED",
    "VFW_E_NOT_FOUND",
    "VFW_E_NOT_IN_GRAPH",
    "VFW_E_NOT_OVERLAY_CONNECTION",
    "VFW_E_NOT_PAUSED",
    "VFW_E_NOT_RUNNING",
    "VFW_E_NOT_SAMPLE_CONNECTION",
    "VFW_E_NOT_STOPPED",
    "VFW_E_NO_ACCEPTABLE_TYPES",
    "VFW_E_NO_ADVISE_SET",
    "VFW_E_NO_ALLOCATOR",
    "VFW_E_NO_AUDIO_HARDWARE",
    "VFW_E_NO_CAPTURE_HARDWARE",
    "VFW_E_NO_CLOCK",
    "VFW_E_NO_COLOR_KEY_FOUND",
    "VFW_E_NO_COLOR_KEY_SET",
    "VFW_E_NO_COPP_HW",
    "VFW_E_NO_DECOMPRESSOR",
    "VFW_E_NO_DISPLAY_PALETTE",
    "VFW_E_NO_FULLSCREEN",
    "VFW_E_NO_INTERFACE",
    "VFW_E_NO_MODEX_AVAILABLE",
    "VFW_E_NO_PALETTE_AVAILABLE",
    "VFW_E_NO_SINK",
    "VFW_E_NO_TIME_FORMAT",
    "VFW_E_NO_TIME_FORMAT_SET",
    "VFW_E_NO_TRANSPORT",
    "VFW_E_NO_TYPES",
    "VFW_E_NO_VP_HARDWARE",
    "VFW_E_OUT_OF_VIDEO_MEMORY",
    "VFW_E_PALETTE_SET",
    "VFW_E_PIN_ALREADY_BLOCKED",
    "VFW_E_PIN_ALREADY_BLOCKED_ON_THIS_THREAD",
    "VFW_E_PROCESSOR_NOT_SUITABLE",
    "VFW_E_READ_ONLY",
    "VFW_E_RPZA",
    "VFW_E_RUNTIME_ERROR",
    "VFW_E_SAMPLE_REJECTED",
    "VFW_E_SAMPLE_REJECTED_EOS",
    "VFW_E_SAMPLE_TIME_NOT_SET",
    "VFW_E_SIZENOTSET",
    "VFW_E_START_TIME_AFTER_END",
    "VFW_E_STATE_CHANGED",
    "VFW_E_TIMEOUT",
    "VFW_E_TIME_ALREADY_PASSED",
    "VFW_E_TIME_EXPIRED",
    "VFW_E_TOO_MANY_COLORS",
    "VFW_E_TYPE_NOT_ACCEPTED",
    "VFW_E_UNKNOWN_FILE_TYPE",
    "VFW_E_UNSUPPORTED_AUDIO",
    "VFW_E_UNSUPPORTED_STREAM",
    "VFW_E_UNSUPPORTED_VIDEO",
    "VFW_E_VMR_NOT_IN_MIXER_MODE",
    "VFW_E_VMR_NO_AP_SUPPLIED",
    "VFW_E_VMR_NO_DEINTERLACE_HW",
    "VFW_E_VMR_NO_PROCAMP_HW",
    "VFW_E_VP_NEGOTIATION_FAILED",
    "VFW_E_WRONG_STATE",
    "VFW_FILTERLIST",
    "VFW_FIRST_CODE",
    "VFW_S_AUDIO_NOT_RENDERED",
    "VFW_S_CANT_CUE",
    "VFW_S_CONNECTIONS_DEFERRED",
    "VFW_S_DUPLICATE_NAME",
    "VFW_S_DVD_CHANNEL_CONTENTS_NOT_AVAILABLE",
    "VFW_S_DVD_NON_ONE_SEQUENTIAL",
    "VFW_S_DVD_NOT_ACCURATE",
    "VFW_S_DVD_RENDER_STATUS",
    "VFW_S_ESTIMATED",
    "VFW_S_MEDIA_TYPE_IGNORED",
    "VFW_S_NOPREVIEWPIN",
    "VFW_S_NO_MORE_ITEMS",
    "VFW_S_NO_STOP_TIME",
    "VFW_S_PARTIAL_RENDER",
    "VFW_S_RESERVED",
    "VFW_S_RESOURCE_NOT_NEEDED",
    "VFW_S_RPZA",
    "VFW_S_SOME_DATA_IGNORED",
    "VFW_S_STATE_INTERMEDIATE",
    "VFW_S_STREAM_OFF",
    "VFW_S_VIDEO_NOT_RENDERED",
    "VIDEOENCODER_BITRATE_MODE",
    "VIDEOENCODER_BITRATE_MODE_ConstantBitRate",
    "VIDEOENCODER_BITRATE_MODE_VariableBitRateAverage",
    "VIDEOENCODER_BITRATE_MODE_VariableBitRatePeak",
    "VIDEOINFO",
    "VIDEO_STREAM_CONFIG_CAPS",
    "VMR9ARMode_LetterBox",
    "VMR9ARMode_None",
    "VMR9AllocFlag_3DRenderTarget",
    "VMR9AllocFlag_DXVATarget",
    "VMR9AllocFlag_OffscreenSurface",
    "VMR9AllocFlag_RGBDynamicSwitch",
    "VMR9AllocFlag_TextureSurface",
    "VMR9AllocFlag_UsageMask",
    "VMR9AllocFlag_UsageReserved",
    "VMR9AllocationInfo",
    "VMR9AlphaBitmap",
    "VMR9AlphaBitmapFlags",
    "VMR9AlphaBitmap_Disable",
    "VMR9AlphaBitmap_EntireDDS",
    "VMR9AlphaBitmap_FilterMode",
    "VMR9AlphaBitmap_SrcColorKey",
    "VMR9AlphaBitmap_SrcRect",
    "VMR9AlphaBitmap_hDC",
    "VMR9AspectRatioMode",
    "VMR9DeinterlaceCaps",
    "VMR9DeinterlacePrefs",
    "VMR9DeinterlaceTech",
    "VMR9Frequency",
    "VMR9MixerPrefs",
    "VMR9Mode",
    "VMR9Mode_Mask",
    "VMR9Mode_Renderless",
    "VMR9Mode_Windowed",
    "VMR9Mode_Windowless",
    "VMR9MonitorInfo",
    "VMR9NormalizedRect",
    "VMR9PresentationFlags",
    "VMR9PresentationInfo",
    "VMR9ProcAmpControl",
    "VMR9ProcAmpControlFlags",
    "VMR9ProcAmpControlRange",
    "VMR9RenderPrefs",
    "VMR9Sample_Discontinuity",
    "VMR9Sample_Preroll",
    "VMR9Sample_SrcDstRectsValid",
    "VMR9Sample_SyncPoint",
    "VMR9Sample_TimeValid",
    "VMR9SurfaceAllocationFlags",
    "VMR9VideoDesc",
    "VMR9VideoStreamInfo",
    "VMR9_SampleFieldInterleavedEvenFirst",
    "VMR9_SampleFieldInterleavedOddFirst",
    "VMR9_SampleFieldSingleEven",
    "VMR9_SampleFieldSingleOdd",
    "VMR9_SampleFormat",
    "VMR9_SampleProgressiveFrame",
    "VMR9_SampleReserved",
    "VMRALLOCATIONINFO",
    "VMRALPHABITMAP",
    "VMRBITMAP_DISABLE",
    "VMRBITMAP_ENTIREDDS",
    "VMRBITMAP_HDC",
    "VMRBITMAP_SRCCOLORKEY",
    "VMRBITMAP_SRCRECT",
    "VMRDeinterlaceCaps",
    "VMRDeinterlacePrefs",
    "VMRDeinterlaceTech",
    "VMRFrequency",
    "VMRGUID",
    "VMRMONITORINFO",
    "VMRMixerPrefs",
    "VMRMode",
    "VMRMode_Mask",
    "VMRMode_Renderless",
    "VMRMode_Windowed",
    "VMRMode_Windowless",
    "VMRPRESENTATIONINFO",
    "VMRPresentationFlags",
    "VMRRenderPrefs",
    "VMRSample_Discontinuity",
    "VMRSample_Preroll",
    "VMRSample_SrcDstRectsValid",
    "VMRSample_SyncPoint",
    "VMRSample_TimeValid",
    "VMRSurfaceAllocationFlags",
    "VMRVIDEOSTREAMINFO",
    "VMRVideoDesc",
    "VMR_ARMODE_LETTER_BOX",
    "VMR_ARMODE_NONE",
    "VMR_ASPECT_RATIO_MODE",
    "VMR_NOTSUPPORTED",
    "VMR_RENDER_DEVICE_OVERLAY",
    "VMR_RENDER_DEVICE_SYSMEM",
    "VMR_RENDER_DEVICE_VIDMEM",
    "VMR_SUPPORTED",
    "VfwCaptureDialog_Display",
    "VfwCaptureDialog_Format",
    "VfwCaptureDialog_Source",
    "VfwCaptureDialogs",
    "VfwCompressDialog_About",
    "VfwCompressDialog_Config",
    "VfwCompressDialog_QueryAbout",
    "VfwCompressDialog_QueryConfig",
    "VfwCompressDialogs",
    "VideoControlFlag_ExternalTriggerEnable",
    "VideoControlFlag_FlipHorizontal",
    "VideoControlFlag_FlipVertical",
    "VideoControlFlag_Trigger",
    "VideoControlFlags",
    "VideoCopyProtectionType",
    "VideoCopyProtectionType_VideoCopyProtectionMacrovisionBasic",
    "VideoCopyProtectionType_VideoCopyProtectionMacrovisionCBI",
    "VideoProcAmpFlags",
    "VideoProcAmpProperty",
    "VideoProcAmp_BacklightCompensation",
    "VideoProcAmp_Brightness",
    "VideoProcAmp_ColorEnable",
    "VideoProcAmp_Contrast",
    "VideoProcAmp_Flags_Auto",
    "VideoProcAmp_Flags_Manual",
    "VideoProcAmp_Gain",
    "VideoProcAmp_Gamma",
    "VideoProcAmp_Hue",
    "VideoProcAmp_Saturation",
    "VideoProcAmp_Sharpness",
    "VideoProcAmp_WhiteBalance",
    "WMDRMProtectionInfo",
    "XDSCodec",
    "XDSToRat",
    "_AMRESCTL_RESERVEFLAGS",
    "_AMSTREAMSELECTENABLEFLAGS",
    "_AMSTREAMSELECTINFOFLAGS",
    "_AM_AUDIO_RENDERER_STAT_PARAM",
    "_AM_FILTER_MISC_FLAGS",
    "_AM_INTF_SEARCH_FLAGS",
    "_AM_OVERLAY_NOTIFY_FLAGS",
    "_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS",
    "_AM_PUSHSOURCE_FLAGS",
    "_AM_RENSDEREXFLAGS",
    "_DVDECODERRESOLUTION",
    "_DVENCODERFORMAT",
    "_DVENCODERRESOLUTION",
    "_DVENCODERVIDEOFORMAT",
    "_DVRESOLUTION",
    "_IMSVidCtlEvents",
    "_REM_FILTER_FLAGS",
    "dvdChannel_Audio",
    "dvdGeneral_Comments",
    "dvdGeneral_Name",
    "dvdMenu_Angle",
    "dvdMenu_Audio",
    "dvdMenu_Chapter",
    "dvdMenu_Root",
    "dvdMenu_Subpicture",
    "dvdMenu_Title",
    "dvdOther_Cut",
    "dvdOther_Scene",
    "dvdOther_Take",
    "dvdSPExt_CC_Big",
    "dvdSPExt_CC_Children",
    "dvdSPExt_CC_Normal",
    "dvdSPExt_Caption_Big",
    "dvdSPExt_Caption_Children",
    "dvdSPExt_Caption_Normal",
    "dvdSPExt_DirectorComments_Big",
    "dvdSPExt_DirectorComments_Children",
    "dvdSPExt_DirectorComments_Normal",
    "dvdSPExt_Forced",
    "dvdSPExt_NotSpecified",
    "dvdState_Paused",
    "dvdState_Running",
    "dvdState_Stopped",
    "dvdState_Undefined",
    "dvdState_Unitialized",
    "dvdStream_Angle",
    "dvdStream_Audio",
    "dvdStream_Subpicture",
    "dvdStruct_Cell",
    "dvdStruct_ParentalID",
    "dvdStruct_PartOfTitle",
    "dvdStruct_Title",
    "dvdStruct_Volume",
    "dvdTitle_Album",
    "dvdTitle_Movie",
    "dvdTitle_Orig_Album",
    "dvdTitle_Orig_Movie",
    "dvdTitle_Orig_Other",
    "dvdTitle_Orig_Series",
    "dvdTitle_Orig_Song",
    "dvdTitle_Orig_Video",
    "dvdTitle_Other",
    "dvdTitle_Series",
    "dvdTitle_Song",
    "dvdTitle_Sub_Album",
    "dvdTitle_Sub_Movie",
    "dvdTitle_Sub_Other",
    "dvdTitle_Sub_Series",
    "dvdTitle_Sub_Song",
    "dvdTitle_Sub_Video",
    "dvdTitle_Video",
    "g_wszExcludeScriptStreamDeliverySynchronization",
    "g_wszStreamBufferRecordingAlbumArtist",
    "g_wszStreamBufferRecordingAlbumCoverURL",
    "g_wszStreamBufferRecordingAlbumTitle",
    "g_wszStreamBufferRecordingAspectRatioX",
    "g_wszStreamBufferRecordingAspectRatioY",
    "g_wszStreamBufferRecordingAuthor",
    "g_wszStreamBufferRecordingBannerImageData",
    "g_wszStreamBufferRecordingBannerImageType",
    "g_wszStreamBufferRecordingBannerImageURL",
    "g_wszStreamBufferRecordingBitrate",
    "g_wszStreamBufferRecordingBroadcast",
    "g_wszStreamBufferRecordingComposer",
    "g_wszStreamBufferRecordingCopyright",
    "g_wszStreamBufferRecordingCopyrightURL",
    "g_wszStreamBufferRecordingCurrentBitrate",
    "g_wszStreamBufferRecordingDRM_Flags",
    "g_wszStreamBufferRecordingDRM_Level",
    "g_wszStreamBufferRecordingDescription",
    "g_wszStreamBufferRecordingDuration",
    "g_wszStreamBufferRecordingFileSize",
    "g_wszStreamBufferRecordingGenre",
    "g_wszStreamBufferRecordingGenreID",
    "g_wszStreamBufferRecordingHasArbitraryDataStream",
    "g_wszStreamBufferRecordingHasAttachedImages",
    "g_wszStreamBufferRecordingHasAudio",
    "g_wszStreamBufferRecordingHasFileTransferStream",
    "g_wszStreamBufferRecordingHasImage",
    "g_wszStreamBufferRecordingHasScript",
    "g_wszStreamBufferRecordingHasVideo",
    "g_wszStreamBufferRecordingIsVBR",
    "g_wszStreamBufferRecordingLyrics",
    "g_wszStreamBufferRecordingMCDI",
    "g_wszStreamBufferRecordingNSCAddress",
    "g_wszStreamBufferRecordingNSCDescription",
    "g_wszStreamBufferRecordingNSCEmail",
    "g_wszStreamBufferRecordingNSCName",
    "g_wszStreamBufferRecordingNSCPhone",
    "g_wszStreamBufferRecordingNumberOfFrames",
    "g_wszStreamBufferRecordingOptimalBitrate",
    "g_wszStreamBufferRecordingPromotionURL",
    "g_wszStreamBufferRecordingProtected",
    "g_wszStreamBufferRecordingRating",
    "g_wszStreamBufferRecordingSeekable",
    "g_wszStreamBufferRecordingSignature_Name",
    "g_wszStreamBufferRecordingSkipBackward",
    "g_wszStreamBufferRecordingSkipForward",
    "g_wszStreamBufferRecordingStridable",
    "g_wszStreamBufferRecordingTitle",
    "g_wszStreamBufferRecordingToolName",
    "g_wszStreamBufferRecordingToolVersion",
    "g_wszStreamBufferRecordingTrack",
    "g_wszStreamBufferRecordingTrackNumber",
    "g_wszStreamBufferRecordingTrusted",
    "g_wszStreamBufferRecordingUse_DRM",
    "g_wszStreamBufferRecordingYear",
    "iBLUE",
    "iEGA_COLORS",
    "iGREEN",
    "iMASK_COLORS",
    "iMAXBITS",
    "iPALETTE",
    "iPALETTE_COLORS",
    "iRED",
    "iTRUECOLOR",
]
_arch_optional = [
]
