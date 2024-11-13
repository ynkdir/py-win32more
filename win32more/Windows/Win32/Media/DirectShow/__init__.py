from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D9
import win32more.Windows.Win32.Graphics.DirectDraw
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Media
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Audio.DirectSound
import win32more.Windows.Win32.Media.DirectShow
import win32more.Windows.Win32.Media.MediaFoundation
import win32more.Windows.Win32.Media.WindowsMediaFormat
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Diagnostics.Etw
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.WindowsAndMessaging
ADVISE_TYPE = Int32
ADVISE_NONE: win32more.Windows.Win32.Media.DirectShow.ADVISE_TYPE = 0
ADVISE_CLIPPING: win32more.Windows.Win32.Media.DirectShow.ADVISE_TYPE = 1
ADVISE_PALETTE: win32more.Windows.Win32.Media.DirectShow.ADVISE_TYPE = 2
ADVISE_COLORKEY: win32more.Windows.Win32.Media.DirectShow.ADVISE_TYPE = 4
ADVISE_POSITION: win32more.Windows.Win32.Media.DirectShow.ADVISE_TYPE = 8
ADVISE_DISPLAY_CHANGE: win32more.Windows.Win32.Media.DirectShow.ADVISE_TYPE = 16
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
AM_EXSEEK_CANSEEK: win32more.Windows.Win32.Media.DirectShow.AMExtendedSeekingCapabilities = 1
AM_EXSEEK_CANSCAN: win32more.Windows.Win32.Media.DirectShow.AMExtendedSeekingCapabilities = 2
AM_EXSEEK_MARKERSEEK: win32more.Windows.Win32.Media.DirectShow.AMExtendedSeekingCapabilities = 4
AM_EXSEEK_SCANWITHOUTCLOCK: win32more.Windows.Win32.Media.DirectShow.AMExtendedSeekingCapabilities = 8
AM_EXSEEK_NOSTANDARDREPAINT: win32more.Windows.Win32.Media.DirectShow.AMExtendedSeekingCapabilities = 16
AM_EXSEEK_BUFFERING: win32more.Windows.Win32.Media.DirectShow.AMExtendedSeekingCapabilities = 32
AM_EXSEEK_SENDS_VIDEOFRAMEREADY: win32more.Windows.Win32.Media.DirectShow.AMExtendedSeekingCapabilities = 64
@winfunctype_pointer
def AMGETERRORTEXTPROCA(param0: win32more.Windows.Win32.Foundation.HRESULT, param1: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def AMGETERRORTEXTPROCW(param0: win32more.Windows.Win32.Foundation.HRESULT, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
AMGETERRORTEXTPROC = UnicodeAlias('AMGETERRORTEXTPROCW')
AMMSF_MMS_INIT_FLAGS = Int32
AMMSF_NOGRAPHTHREAD: win32more.Windows.Win32.Media.DirectShow.AMMSF_MMS_INIT_FLAGS = 1
AMMSF_MS_FLAGS = Int32
AMMSF_ADDDEFAULTRENDERER: win32more.Windows.Win32.Media.DirectShow.AMMSF_MS_FLAGS = 1
AMMSF_CREATEPEER: win32more.Windows.Win32.Media.DirectShow.AMMSF_MS_FLAGS = 2
AMMSF_STOPIFNOSAMPLES: win32more.Windows.Win32.Media.DirectShow.AMMSF_MS_FLAGS = 4
AMMSF_NOSTALL: win32more.Windows.Win32.Media.DirectShow.AMMSF_MS_FLAGS = 8
AMMSF_RENDER_FLAGS = Int32
AMMSF_RENDERTYPEMASK: win32more.Windows.Win32.Media.DirectShow.AMMSF_RENDER_FLAGS = 3
AMMSF_RENDERTOEXISTING: win32more.Windows.Win32.Media.DirectShow.AMMSF_RENDER_FLAGS = 0
AMMSF_RENDERALLSTREAMS: win32more.Windows.Win32.Media.DirectShow.AMMSF_RENDER_FLAGS = 1
AMMSF_NORENDER: win32more.Windows.Win32.Media.DirectShow.AMMSF_RENDER_FLAGS = 2
AMMSF_NOCLOCK: win32more.Windows.Win32.Media.DirectShow.AMMSF_RENDER_FLAGS = 4
AMMSF_RUN: win32more.Windows.Win32.Media.DirectShow.AMMSF_RENDER_FLAGS = 8
AMOVERLAYFX = Int32
AMOVERFX_NOFX: win32more.Windows.Win32.Media.DirectShow.AMOVERLAYFX = 0
AMOVERFX_MIRRORLEFTRIGHT: win32more.Windows.Win32.Media.DirectShow.AMOVERLAYFX = 2
AMOVERFX_MIRRORUPDOWN: win32more.Windows.Win32.Media.DirectShow.AMOVERLAYFX = 4
AMOVERFX_DEINTERLACE: win32more.Windows.Win32.Media.DirectShow.AMOVERLAYFX = 8
AMPROPERTY_PIN = Int32
AMPROPERTY_PIN_CATEGORY: win32more.Windows.Win32.Media.DirectShow.AMPROPERTY_PIN = 0
AMPROPERTY_PIN_MEDIUM: win32more.Windows.Win32.Media.DirectShow.AMPROPERTY_PIN = 1
AMPlayListEventFlags = Int32
AMPLAYLISTEVENT_RESUME: win32more.Windows.Win32.Media.DirectShow.AMPlayListEventFlags = 0
AMPLAYLISTEVENT_BREAK: win32more.Windows.Win32.Media.DirectShow.AMPlayListEventFlags = 1
AMPLAYLISTEVENT_NEXT: win32more.Windows.Win32.Media.DirectShow.AMPlayListEventFlags = 2
AMPLAYLISTEVENT_MASK: win32more.Windows.Win32.Media.DirectShow.AMPlayListEventFlags = 15
AMPLAYLISTEVENT_REFRESH: win32more.Windows.Win32.Media.DirectShow.AMPlayListEventFlags = 16
AMPlayListFlags = Int32
AMPLAYLIST_STARTINSCANMODE: win32more.Windows.Win32.Media.DirectShow.AMPlayListFlags = 1
AMPLAYLIST_FORCEBANNER: win32more.Windows.Win32.Media.DirectShow.AMPlayListFlags = 2
AMPlayListItemFlags = Int32
AMPLAYLISTITEM_CANSKIP: win32more.Windows.Win32.Media.DirectShow.AMPlayListItemFlags = 1
AMPLAYLISTITEM_CANBIND: win32more.Windows.Win32.Media.DirectShow.AMPlayListItemFlags = 2
AMTVAudioEventType = Int32
AMTVAUDIO_EVENT_CHANGED: win32more.Windows.Win32.Media.DirectShow.AMTVAudioEventType = 1
AMTunerEventType = Int32
AMTUNER_EVENT_CHANGED: win32more.Windows.Win32.Media.DirectShow.AMTunerEventType = 1
AMTunerModeType = Int32
AMTUNER_MODE_DEFAULT: win32more.Windows.Win32.Media.DirectShow.AMTunerModeType = 0
AMTUNER_MODE_TV: win32more.Windows.Win32.Media.DirectShow.AMTunerModeType = 1
AMTUNER_MODE_FM_RADIO: win32more.Windows.Win32.Media.DirectShow.AMTunerModeType = 2
AMTUNER_MODE_AM_RADIO: win32more.Windows.Win32.Media.DirectShow.AMTunerModeType = 4
AMTUNER_MODE_DSS: win32more.Windows.Win32.Media.DirectShow.AMTunerModeType = 8
AMTunerSignalStrength = Int32
AMTUNER_HASNOSIGNALSTRENGTH: win32more.Windows.Win32.Media.DirectShow.AMTunerSignalStrength = -1
AMTUNER_NOSIGNAL: win32more.Windows.Win32.Media.DirectShow.AMTunerSignalStrength = 0
AMTUNER_SIGNALPRESENT: win32more.Windows.Win32.Media.DirectShow.AMTunerSignalStrength = 1
AMTunerSubChannel = Int32
AMTUNER_SUBCHAN_NO_TUNE: win32more.Windows.Win32.Media.DirectShow.AMTunerSubChannel = -2
AMTUNER_SUBCHAN_DEFAULT: win32more.Windows.Win32.Media.DirectShow.AMTunerSubChannel = -1
class AMVABUFFERINFO(Structure):
    dwTypeIndex: UInt32
    dwBufferIndex: UInt32
    dwDataOffset: UInt32
    dwDataSize: UInt32
class AMVABeginFrameInfo(Structure):
    dwDestSurfaceIndex: UInt32
    pInputData: VoidPtr
    dwSizeInputData: UInt32
    pOutputData: VoidPtr
    dwSizeOutputData: UInt32
class AMVACompBufferInfo(Structure):
    dwNumCompBuffers: UInt32
    dwWidthToCreate: UInt32
    dwHeightToCreate: UInt32
    dwBytesToAllocate: UInt32
    ddCompCaps: win32more.Windows.Win32.Graphics.DirectDraw.DDSCAPS2
    ddPixelFormat: win32more.Windows.Win32.Graphics.DirectDraw.DDPIXELFORMAT
class AMVAEndFrameInfo(Structure):
    dwSizeMiscData: UInt32
    pMiscData: VoidPtr
class AMVAInternalMemInfo(Structure):
    dwScratchMemAlloc: UInt32
class AMVAUncompBufferInfo(Structure):
    dwMinNumSurfaces: UInt32
    dwMaxNumSurfaces: UInt32
    ddUncompPixelFormat: win32more.Windows.Win32.Graphics.DirectDraw.DDPIXELFORMAT
class AMVAUncompDataInfo(Structure):
    dwUncompWidth: UInt32
    dwUncompHeight: UInt32
    ddUncompPixelFormat: win32more.Windows.Win32.Graphics.DirectDraw.DDPIXELFORMAT
class AMVPDATAINFO(Structure):
    dwSize: UInt32
    dwMicrosecondsPerField: UInt32
    amvpDimInfo: win32more.Windows.Win32.Media.DirectShow.AMVPDIMINFO
    dwPictAspectRatioX: UInt32
    dwPictAspectRatioY: UInt32
    bEnableDoubleClock: win32more.Windows.Win32.Foundation.BOOL
    bEnableVACT: win32more.Windows.Win32.Foundation.BOOL
    bDataIsInterlaced: win32more.Windows.Win32.Foundation.BOOL
    lHalfLinesOdd: Int32
    bFieldPolarityInverted: win32more.Windows.Win32.Foundation.BOOL
    dwNumLinesInVREF: UInt32
    lHalfLinesEven: Int32
    dwReserved1: UInt32
class AMVPDIMINFO(Structure):
    dwFieldWidth: UInt32
    dwFieldHeight: UInt32
    dwVBIWidth: UInt32
    dwVBIHeight: UInt32
    rcValidRegion: win32more.Windows.Win32.Foundation.RECT
class AMVPSIZE(Structure):
    dwWidth: UInt32
    dwHeight: UInt32
AMVP_MODE = Int32
AMVP_MODE_WEAVE: win32more.Windows.Win32.Media.DirectShow.AMVP_MODE = 0
AMVP_MODE_BOBINTERLEAVED: win32more.Windows.Win32.Media.DirectShow.AMVP_MODE = 1
AMVP_MODE_BOBNONINTERLEAVED: win32more.Windows.Win32.Media.DirectShow.AMVP_MODE = 2
AMVP_MODE_SKIPEVEN: win32more.Windows.Win32.Media.DirectShow.AMVP_MODE = 3
AMVP_MODE_SKIPODD: win32more.Windows.Win32.Media.DirectShow.AMVP_MODE = 4
AMVP_SELECT_FORMAT_BY = Int32
AMVP_DO_NOT_CARE: win32more.Windows.Win32.Media.DirectShow.AMVP_SELECT_FORMAT_BY = 0
AMVP_BEST_BANDWIDTH: win32more.Windows.Win32.Media.DirectShow.AMVP_SELECT_FORMAT_BY = 1
AMVP_INPUT_SAME_AS_OUTPUT: win32more.Windows.Win32.Media.DirectShow.AMVP_SELECT_FORMAT_BY = 2
class AM_AC3_ALTERNATE_AUDIO(Structure):
    fStereo: win32more.Windows.Win32.Foundation.BOOL
    DualMode: UInt32
class AM_AC3_BIT_STREAM_MODE(Structure):
    BitStreamMode: Int32
class AM_AC3_DIALOGUE_LEVEL(Structure):
    DialogueLevel: UInt32
class AM_AC3_DOWNMIX(Structure):
    fDownMix: win32more.Windows.Win32.Foundation.BOOL
    fDolbySurround: win32more.Windows.Win32.Foundation.BOOL
class AM_AC3_ERROR_CONCEALMENT(Structure):
    fRepeatPreviousBlock: win32more.Windows.Win32.Foundation.BOOL
    fErrorInCurrentBlock: win32more.Windows.Win32.Foundation.BOOL
class AM_AC3_ROOM_TYPE(Structure):
    fLargeRoom: win32more.Windows.Win32.Foundation.BOOL
AM_ASPECT_RATIO_MODE = Int32
AM_ARMODE_STRETCHED: win32more.Windows.Win32.Media.DirectShow.AM_ASPECT_RATIO_MODE = 0
AM_ARMODE_LETTER_BOX: win32more.Windows.Win32.Media.DirectShow.AM_ASPECT_RATIO_MODE = 1
AM_ARMODE_CROP: win32more.Windows.Win32.Media.DirectShow.AM_ASPECT_RATIO_MODE = 2
AM_ARMODE_STRETCHED_AS_PRIMARY: win32more.Windows.Win32.Media.DirectShow.AM_ASPECT_RATIO_MODE = 3
class AM_COLCON(Structure):
    emph1col: Annotated[Byte, 4]
    emph2col: Annotated[Byte, 4]
    backcol: Annotated[Byte, 4]
    patcol: Annotated[Byte, 4]
    emph1con: Annotated[Byte, 4]
    emph2con: Annotated[Byte, 4]
    backcon: Annotated[Byte, 4]
    patcon: Annotated[Byte, 4]
class AM_COPY_MACROVISION(Structure):
    MACROVISIONLevel: UInt32
AM_COPY_MACROVISION_LEVEL = Int32
AM_MACROVISION_DISABLED: win32more.Windows.Win32.Media.DirectShow.AM_COPY_MACROVISION_LEVEL = 0
AM_MACROVISION_LEVEL1: win32more.Windows.Win32.Media.DirectShow.AM_COPY_MACROVISION_LEVEL = 1
AM_MACROVISION_LEVEL2: win32more.Windows.Win32.Media.DirectShow.AM_COPY_MACROVISION_LEVEL = 2
AM_MACROVISION_LEVEL3: win32more.Windows.Win32.Media.DirectShow.AM_COPY_MACROVISION_LEVEL = 3
AM_DIGITAL_CP = Int32
AM_DIGITAL_CP_OFF: win32more.Windows.Win32.Media.DirectShow.AM_DIGITAL_CP = 0
AM_DIGITAL_CP_ON: win32more.Windows.Win32.Media.DirectShow.AM_DIGITAL_CP = 1
AM_DIGITAL_CP_DVD_COMPLIANT: win32more.Windows.Win32.Media.DirectShow.AM_DIGITAL_CP = 2
AM_DVDCOPYSTATE = Int32
AM_DVDCOPYSTATE_INITIALIZE: win32more.Windows.Win32.Media.DirectShow.AM_DVDCOPYSTATE = 0
AM_DVDCOPYSTATE_INITIALIZE_TITLE: win32more.Windows.Win32.Media.DirectShow.AM_DVDCOPYSTATE = 1
AM_DVDCOPYSTATE_AUTHENTICATION_NOT_REQUIRED: win32more.Windows.Win32.Media.DirectShow.AM_DVDCOPYSTATE = 2
AM_DVDCOPYSTATE_AUTHENTICATION_REQUIRED: win32more.Windows.Win32.Media.DirectShow.AM_DVDCOPYSTATE = 3
AM_DVDCOPYSTATE_DONE: win32more.Windows.Win32.Media.DirectShow.AM_DVDCOPYSTATE = 4
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
AM_DVD_HWDEC_PREFER: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 1
AM_DVD_HWDEC_ONLY: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 2
AM_DVD_SWDEC_PREFER: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 4
AM_DVD_SWDEC_ONLY: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 8
AM_DVD_NOVPE: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 256
AM_DVD_DO_NOT_CLEAR: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 512
AM_DVD_VMR9_ONLY: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 2048
AM_DVD_EVR_ONLY: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 4096
AM_DVD_EVR_QOS: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 8192
AM_DVD_ADAPT_GRAPH: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 16384
AM_DVD_MASK: win32more.Windows.Win32.Media.DirectShow.AM_DVD_GRAPH_FLAGS = 65535
class AM_DVD_RENDERSTATUS(Structure):
    hrVPEStatus: win32more.Windows.Win32.Foundation.HRESULT
    bDvdVolInvalid: win32more.Windows.Win32.Foundation.BOOL
    bDvdVolUnknown: win32more.Windows.Win32.Foundation.BOOL
    bNoLine21In: win32more.Windows.Win32.Foundation.BOOL
    bNoLine21Out: win32more.Windows.Win32.Foundation.BOOL
    iNumStreams: Int32
    iNumStreamsFailed: Int32
    dwFailedStreamsFlag: UInt32
AM_DVD_STREAM_FLAGS = Int32
AM_DVD_STREAM_VIDEO: win32more.Windows.Win32.Media.DirectShow.AM_DVD_STREAM_FLAGS = 1
AM_DVD_STREAM_AUDIO: win32more.Windows.Win32.Media.DirectShow.AM_DVD_STREAM_FLAGS = 2
AM_DVD_STREAM_SUBPIC: win32more.Windows.Win32.Media.DirectShow.AM_DVD_STREAM_FLAGS = 4
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
AM_FILE_OVERWRITE: win32more.Windows.Win32.Media.DirectShow.AM_FILESINK_FLAGS = 1
AM_FILTER_FLAGS = Int32
AM_FILTER_FLAGS_REMOVABLE: win32more.Windows.Win32.Media.DirectShow.AM_FILTER_FLAGS = 1
class AM_FRAMESTEP_STEP(Structure):
    dwFramesToStep: UInt32
AM_GRAPH_CONFIG_RECONNECT_FLAGS = Int32
AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT: win32more.Windows.Win32.Media.DirectShow.AM_GRAPH_CONFIG_RECONNECT_FLAGS = 1
AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS: win32more.Windows.Win32.Media.DirectShow.AM_GRAPH_CONFIG_RECONNECT_FLAGS = 2
AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS: win32more.Windows.Win32.Media.DirectShow.AM_GRAPH_CONFIG_RECONNECT_FLAGS = 4
AM_LINE21_CCLEVEL = Int32
AM_L21_CCLEVEL_TC2: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCLEVEL = 0
AM_LINE21_CCSERVICE = Int32
AM_L21_CCSERVICE_None: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 0
AM_L21_CCSERVICE_Caption1: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 1
AM_L21_CCSERVICE_Caption2: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 2
AM_L21_CCSERVICE_Text1: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 3
AM_L21_CCSERVICE_Text2: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 4
AM_L21_CCSERVICE_XDS: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 5
AM_L21_CCSERVICE_DefChannel: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 10
AM_L21_CCSERVICE_Invalid: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE = 11
AM_LINE21_CCSTATE = Int32
AM_L21_CCSTATE_Off: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTATE = 0
AM_L21_CCSTATE_On: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTATE = 1
AM_LINE21_CCSTYLE = Int32
AM_L21_CCSTYLE_None: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTYLE = 0
AM_L21_CCSTYLE_PopOn: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTYLE = 1
AM_L21_CCSTYLE_PaintOn: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTYLE = 2
AM_L21_CCSTYLE_RollUp: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTYLE = 3
AM_LINE21_DRAWBGMODE = Int32
AM_L21_DRAWBGMODE_Opaque: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_DRAWBGMODE = 0
AM_L21_DRAWBGMODE_Transparent: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_DRAWBGMODE = 1
AM_MEDIAEVENT_FLAGS = Int32
AM_MEDIAEVENT_NONOTIFY: win32more.Windows.Win32.Media.DirectShow.AM_MEDIAEVENT_FLAGS = 1
AM_MPEG2Level = Int32
AM_MPEG2Level_Low: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Level = 1
AM_MPEG2Level_Main: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Level = 2
AM_MPEG2Level_High1440: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Level = 3
AM_MPEG2Level_High: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Level = 4
AM_MPEG2Profile = Int32
AM_MPEG2Profile_Simple: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Profile = 1
AM_MPEG2Profile_Main: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Profile = 2
AM_MPEG2Profile_SNRScalable: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Profile = 3
AM_MPEG2Profile_SpatiallyScalable: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Profile = 4
AM_MPEG2Profile_High: win32more.Windows.Win32.Media.DirectShow.AM_MPEG2Profile = 5
class AM_MPEGSTREAMTYPE(Structure):
    dwStreamId: UInt32
    dwReserved: UInt32
    mt: win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE
    bFormat: Byte * 1
class AM_MPEGSYSTEMTYPE(Structure):
    dwBitRate: UInt32
    cStreams: UInt32
    Streams: win32more.Windows.Win32.Media.DirectShow.AM_MPEGSTREAMTYPE * 1
AM_PROPERTY_AC3 = Int32
AM_PROPERTY_AC3_ERROR_CONCEALMENT: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_AC3 = 1
AM_PROPERTY_AC3_ALTERNATE_AUDIO: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_AC3 = 2
AM_PROPERTY_AC3_DOWNMIX: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_AC3 = 3
AM_PROPERTY_AC3_BIT_STREAM_MODE: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_AC3 = 4
AM_PROPERTY_AC3_DIALOGUE_LEVEL: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_AC3 = 5
AM_PROPERTY_AC3_LANGUAGE_CODE: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_AC3 = 6
AM_PROPERTY_AC3_ROOM_TYPE: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_AC3 = 7
AM_PROPERTY_DVDCOPYPROT = Int32
AM_PROPERTY_DVDCOPY_CHLG_KEY: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 1
AM_PROPERTY_DVDCOPY_DVD_KEY1: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 2
AM_PROPERTY_DVDCOPY_DEC_KEY2: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 3
AM_PROPERTY_DVDCOPY_TITLE_KEY: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 4
AM_PROPERTY_COPY_MACROVISION: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 5
AM_PROPERTY_DVDCOPY_REGION: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 6
AM_PROPERTY_DVDCOPY_SET_COPY_STATE: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 7
AM_PROPERTY_COPY_ANALOG_COMPONENT: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 8
AM_PROPERTY_COPY_DIGITAL_CP: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 9
AM_PROPERTY_COPY_DVD_SRM: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 10
AM_PROPERTY_DVDCOPY_SUPPORTS_NEW_KEYCOUNT: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 11
AM_PROPERTY_DVDCOPY_DISC_KEY: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDCOPYPROT = 128
AM_PROPERTY_DVDKARAOKE = Int32
AM_PROPERTY_DVDKARAOKE_ENABLE: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDKARAOKE = 0
AM_PROPERTY_DVDKARAOKE_DATA: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDKARAOKE = 1
AM_PROPERTY_DVDSUBPIC = Int32
AM_PROPERTY_DVDSUBPIC_PALETTE: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDSUBPIC = 0
AM_PROPERTY_DVDSUBPIC_HLI: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDSUBPIC = 1
AM_PROPERTY_DVDSUBPIC_COMPOSIT_ON: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVDSUBPIC = 2
AM_PROPERTY_DVD_RATE_CHANGE = Int32
AM_RATE_ChangeRate: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVD_RATE_CHANGE = 1
AM_RATE_FullDataRateMax: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVD_RATE_CHANGE = 2
AM_RATE_ReverseDecode: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVD_RATE_CHANGE = 3
AM_RATE_DecoderPosition: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVD_RATE_CHANGE = 4
AM_RATE_DecoderVersion: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_DVD_RATE_CHANGE = 5
AM_PROPERTY_FRAMESTEP = Int32
AM_PROPERTY_FRAMESTEP_STEP: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_FRAMESTEP = 1
AM_PROPERTY_FRAMESTEP_CANCEL: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_FRAMESTEP = 2
AM_PROPERTY_FRAMESTEP_CANSTEP: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_FRAMESTEP = 3
AM_PROPERTY_FRAMESTEP_CANSTEPMULTIPLE: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_FRAMESTEP = 4
class AM_PROPERTY_SPHLI(Structure):
    HLISS: UInt16
    Reserved: UInt16
    StartPTM: UInt32
    EndPTM: UInt32
    StartX: UInt16
    StartY: UInt16
    StopX: UInt16
    StopY: UInt16
    ColCon: win32more.Windows.Win32.Media.DirectShow.AM_COLCON
class AM_PROPERTY_SPPAL(Structure):
    sppal: win32more.Windows.Win32.Media.DirectShow.AM_DVD_YUV * 16
AM_PROPERTY_TS_RATE_CHANGE = Int32
AM_RATE_SimpleRateChange: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 1
AM_RATE_ExactRateChange: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 2
AM_RATE_MaxFullDataRate: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 3
AM_RATE_Step: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 4
AM_RATE_UseRateVersion: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 5
AM_RATE_QueryFullFrameRate: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 6
AM_RATE_QueryLastRateSegPTS: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 7
AM_RATE_CorrectTS: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 8
AM_RATE_ReverseMaxFullDataRate: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 9
AM_RATE_ResetOnTimeDisc: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 10
AM_RATE_QueryMapping: win32more.Windows.Win32.Media.DirectShow.AM_PROPERTY_TS_RATE_CHANGE = 11
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
    pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)
    pbBuffer: POINTER(Byte)
    cbBuffer: Int32
AM_SAMPLE_PROPERTY_FLAGS = Int32
AM_SAMPLE_SPLICEPOINT: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 1
AM_SAMPLE_PREROLL: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 2
AM_SAMPLE_DATADISCONTINUITY: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 4
AM_SAMPLE_TYPECHANGED: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 8
AM_SAMPLE_TIMEVALID: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 16
AM_SAMPLE_TIMEDISCONTINUITY: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 64
AM_SAMPLE_FLUSH_ON_PAUSE: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 128
AM_SAMPLE_STOPVALID: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 256
AM_SAMPLE_ENDOFSTREAM: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 512
AM_STREAM_MEDIA: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 0
AM_STREAM_CONTROL: win32more.Windows.Win32.Media.DirectShow.AM_SAMPLE_PROPERTY_FLAGS = 1
AM_SEEKING_SEEKING_CAPABILITIES = Int32
AM_SEEKING_CanSeekAbsolute: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 1
AM_SEEKING_CanSeekForwards: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 2
AM_SEEKING_CanSeekBackwards: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 4
AM_SEEKING_CanGetCurrentPos: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 8
AM_SEEKING_CanGetStopPos: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 16
AM_SEEKING_CanGetDuration: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 32
AM_SEEKING_CanPlayBackwards: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 64
AM_SEEKING_CanDoSegments: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 128
AM_SEEKING_Source: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_CAPABILITIES = 256
AM_SEEKING_SEEKING_FLAGS = Int32
AM_SEEKING_NoPositioning: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 0
AM_SEEKING_AbsolutePositioning: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 1
AM_SEEKING_RelativePositioning: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 2
AM_SEEKING_IncrementalPositioning: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 3
AM_SEEKING_PositioningBitsMask: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 3
AM_SEEKING_SeekToKeyFrame: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 4
AM_SEEKING_ReturnTime: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 8
AM_SEEKING_Segment: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 16
AM_SEEKING_NoFlush: win32more.Windows.Win32.Media.DirectShow.AM_SEEKING_SEEKING_FLAGS = 32
class AM_STREAM_INFO(Structure):
    tStart: Int64
    tStop: Int64
    dwStartCookie: UInt32
    dwStopCookie: UInt32
    dwFlags: UInt32
AM_STREAM_INFO_FLAGS = Int32
AM_STREAM_INFO_START_DEFINED: win32more.Windows.Win32.Media.DirectShow.AM_STREAM_INFO_FLAGS = 1
AM_STREAM_INFO_STOP_DEFINED: win32more.Windows.Win32.Media.DirectShow.AM_STREAM_INFO_FLAGS = 2
AM_STREAM_INFO_DISCARDING: win32more.Windows.Win32.Media.DirectShow.AM_STREAM_INFO_FLAGS = 4
AM_STREAM_INFO_STOP_SEND_EXTRA: win32more.Windows.Win32.Media.DirectShow.AM_STREAM_INFO_FLAGS = 16
class AM_SimpleRateChange(Structure):
    StartTime: Int64
    Rate: Int32
AM_WST_DRAWBGMODE = Int32
AM_WST_DRAWBGMODE_Opaque: win32more.Windows.Win32.Media.DirectShow.AM_WST_DRAWBGMODE = 0
AM_WST_DRAWBGMODE_Transparent: win32more.Windows.Win32.Media.DirectShow.AM_WST_DRAWBGMODE = 1
AM_WST_LEVEL = Int32
AM_WST_LEVEL_1_5: win32more.Windows.Win32.Media.DirectShow.AM_WST_LEVEL = 0
class AM_WST_PAGE(Structure):
    dwPageNr: UInt32
    dwSubPageNr: UInt32
    pucPageData: POINTER(Byte)
AM_WST_SERVICE = Int32
AM_WST_SERVICE_None: win32more.Windows.Win32.Media.DirectShow.AM_WST_SERVICE = 0
AM_WST_SERVICE_Text: win32more.Windows.Win32.Media.DirectShow.AM_WST_SERVICE = 1
AM_WST_SERVICE_IDS: win32more.Windows.Win32.Media.DirectShow.AM_WST_SERVICE = 2
AM_WST_SERVICE_Invalid: win32more.Windows.Win32.Media.DirectShow.AM_WST_SERVICE = 3
AM_WST_STATE = Int32
AM_WST_STATE_Off: win32more.Windows.Win32.Media.DirectShow.AM_WST_STATE = 0
AM_WST_STATE_On: win32more.Windows.Win32.Media.DirectShow.AM_WST_STATE = 1
AM_WST_STYLE = Int32
AM_WST_STYLE_None: win32more.Windows.Win32.Media.DirectShow.AM_WST_STYLE = 0
AM_WST_STYLE_Invers: win32more.Windows.Win32.Media.DirectShow.AM_WST_STYLE = 1
class ANALOGVIDEOINFO(Structure):
    rcSource: win32more.Windows.Win32.Foundation.RECT
    rcTarget: win32more.Windows.Win32.Foundation.RECT
    dwActiveWidth: UInt32
    dwActiveHeight: UInt32
    AvgTimePerFrame: Int64
ATSCComponentTypeFlags = Int32
ATSCCT_AC3: win32more.Windows.Win32.Media.DirectShow.ATSCComponentTypeFlags = 1
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
    peNew: win32more.Windows.Win32.Graphics.Gdi.PALETTEENTRY * 1
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
    aIndex: win32more.Windows.Win32.Media.DirectShow.AVISTDINDEX_ENTRY * 2044
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
    rcFrame: win32more.Windows.Win32.Foundation.RECT
class AVITCDLINDEX(Structure):
    fcc: UInt32
    cb: UInt32
    wLongsPerEntry: UInt16
    bIndexSubType: Byte
    bIndexType: Byte
    nEntriesInUse: UInt32
    dwChunkId: UInt32
    dwReserved: UInt32 * 3
    aIndex: win32more.Windows.Win32.Media.DirectShow.AVITCDLINDEX_ENTRY * 584
    adwTrailingFill: UInt32 * 3512
    _pack_ = 2
class AVITCDLINDEX_ENTRY(Structure):
    dwTick: UInt32
    time: win32more.Windows.Win32.Media.TIMECODE
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
    aIndex: win32more.Windows.Win32.Media.DirectShow.TIMECODEDATA * 1022
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
    aIndex: win32more.Windows.Win32.Media.DirectShow.AVITIMEDINDEX_ENTRY * 1362
    adwTrailingFill: UInt32 * 2734
    _pack_ = 2
class AVITIMEDINDEX_ENTRY(Structure):
    dwOffset: UInt32
    dwSize: UInt32
    dwDuration: UInt32
    _pack_ = 2
AnalogVideoStandard = Int32
AnalogVideo_None: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 0
AnalogVideo_NTSC_M: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 1
AnalogVideo_NTSC_M_J: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 2
AnalogVideo_NTSC_433: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 4
AnalogVideo_PAL_B: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 16
AnalogVideo_PAL_D: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 32
AnalogVideo_PAL_G: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 64
AnalogVideo_PAL_H: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 128
AnalogVideo_PAL_I: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 256
AnalogVideo_PAL_M: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 512
AnalogVideo_PAL_N: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 1024
AnalogVideo_PAL_60: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 2048
AnalogVideo_SECAM_B: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 4096
AnalogVideo_SECAM_D: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 8192
AnalogVideo_SECAM_G: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 16384
AnalogVideo_SECAM_H: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 32768
AnalogVideo_SECAM_K: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 65536
AnalogVideo_SECAM_K1: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 131072
AnalogVideo_SECAM_L: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 262144
AnalogVideo_SECAM_L1: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 524288
AnalogVideo_PAL_N_COMBO: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 1048576
AnalogVideoMask_MCE_NTSC: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 1052167
AnalogVideoMask_MCE_PAL: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 496
AnalogVideoMask_MCE_SECAM: win32more.Windows.Win32.Media.DirectShow.AnalogVideoStandard = 1044480
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
MEDIATYPE_MPEG2_PACK: Guid = Guid('{36523b13-8ee5-11d1-8ca3-0060b057664a}')
MEDIATYPE_MPEG2_PES: Guid = Guid('{e06d8020-db46-11cf-b4d1-00805f6cbbea}')
MEDIATYPE_CONTROL: Guid = Guid('{e06d8021-db46-11cf-b4d1-00805f6cbbea}')
MEDIATYPE_MPEG2_SECTIONS: Guid = Guid('{455f176c-4b06-47ce-9aef-8caef73df7b5}')
MEDIASUBTYPE_MPEG2_VERSIONED_TABLES: Guid = Guid('{1ed988b0-3ffc-4523-8725-347beec1a8a0}')
MEDIASUBTYPE_ATSC_SI: Guid = Guid('{b3c7397c-d303-414d-b33c-4ed2c9d29733}')
MEDIASUBTYPE_DVB_SI: Guid = Guid('{e9dd31a3-221d-4adb-8532-9af309c1a408}')
MEDIASUBTYPE_ISDB_SI: Guid = Guid('{e89ad298-3601-4b06-aaec-9ddeedcc5bd0}')
MEDIASUBTYPE_TIF_SI: Guid = Guid('{ec232eb2-cb96-4191-b226-0ea129f38250}')
MEDIASUBTYPE_MPEG2DATA: Guid = Guid('{c892e55b-252d-42b5-a316-d997e7a5d995}')
MEDIASUBTYPE_MPEG2_WMDRM_TRANSPORT: Guid = Guid('{18bec4ea-4676-450e-b478-0cd84c54b327}')
MEDIASUBTYPE_MPEG2_VIDEO: Guid = Guid('{e06d8026-db46-11cf-b4d1-00805f6cbbea}')
FORMAT_MPEG2_VIDEO: Guid = Guid('{e06d80e3-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_MPEG2_PROGRAM: Guid = Guid('{e06d8022-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_MPEG2_TRANSPORT: Guid = Guid('{e06d8023-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE: Guid = Guid('{138aa9a4-1ee2-4c5b-988e-19abfdbc8a11}')
MEDIASUBTYPE_MPEG2_UDCR_TRANSPORT: Guid = Guid('{18bec4ea-4676-450e-b478-0cd84c54b327}')
MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_RAW: Guid = Guid('{0d7aed42-cb9a-11db-9705-005056c00008}')
MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_PROCESSED: Guid = Guid('{af748dd4-0d80-11db-9705-005056c00008}')
MEDIASUBTYPE_MPEG2_AUDIO: Guid = Guid('{e06d802b-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_DOLBY_AC3: Guid = Guid('{e06d802c-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_DVD_SUBPICTURE: Guid = Guid('{e06d802d-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_DVD_LPCM_AUDIO: Guid = Guid('{e06d8032-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_DTS: Guid = Guid('{e06d8033-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_SDDS: Guid = Guid('{e06d8034-db46-11cf-b4d1-00805f6cbbea}')
MEDIATYPE_DVD_ENCRYPTED_PACK: Guid = Guid('{ed0b916a-044d-11d1-aa78-00c04fc31d60}')
MEDIATYPE_DVD_NAVIGATION: Guid = Guid('{e06d802e-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_DVD_NAVIGATION_PCI: Guid = Guid('{e06d802f-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_DVD_NAVIGATION_DSI: Guid = Guid('{e06d8030-db46-11cf-b4d1-00805f6cbbea}')
MEDIASUBTYPE_DVD_NAVIGATION_PROVIDER: Guid = Guid('{e06d8031-db46-11cf-b4d1-00805f6cbbea}')
FORMAT_MPEG2Video: Guid = Guid('{e06d80e3-db46-11cf-b4d1-00805f6cbbea}')
FORMAT_DolbyAC3: Guid = Guid('{e06d80e4-db46-11cf-b4d1-00805f6cbbea}')
FORMAT_MPEG2Audio: Guid = Guid('{e06d80e5-db46-11cf-b4d1-00805f6cbbea}')
FORMAT_DVD_LPCMAudio: Guid = Guid('{e06d80e6-db46-11cf-b4d1-00805f6cbbea}')
FORMAT_UVCH264Video: Guid = Guid('{2017be05-6629-4248-aaed-7e1a47bc9b9c}')
FORMAT_JPEGImage: Guid = Guid('{692fa379-d3e8-4651-b5b4-0b94b013eeaf}')
FORMAT_Image: Guid = Guid('{692fa379-d3e8-4651-b5b4-0b94b013eeaf}')
AM_KSPROPSETID_AC3: Guid = Guid('{bfabe720-6e1f-11d0-bcf2-444553540000}')
AM_KSPROPSETID_DvdSubPic: Guid = Guid('{ac390460-43af-11d0-bd6a-003505c103a9}')
AM_KSPROPSETID_CopyProt: Guid = Guid('{0e8a0a40-6aef-11d0-9ed0-00a024ca19b3}')
AM_KSPROPSETID_TSRateChange: Guid = Guid('{a503c5c0-1d1d-11d1-ad80-444553540000}')
AM_KSPROPSETID_DVD_RateChange: Guid = Guid('{3577eb09-9582-477f-b29c-b0c452a4ff9a}')
AM_KSPROPSETID_DvdKaraoke: Guid = Guid('{ae4720ae-aa71-42d8-b82a-fffdf58b76fd}')
AM_KSPROPSETID_FrameStep: Guid = Guid('{c830acbd-ab07-492f-8852-45b6987c2979}')
AM_KSPROPSETID_MPEG4_MediaType_Attributes: Guid = Guid('{ff6c4bfa-07a9-4c7b-a237-672f9d68065f}')
AM_KSCATEGORY_CAPTURE: Guid = Guid('{65e8773d-8f56-11d0-a3b9-00a0c9223196}')
AM_KSCATEGORY_RENDER: Guid = Guid('{65e8773e-8f56-11d0-a3b9-00a0c9223196}')
AM_KSCATEGORY_DATACOMPRESSOR: Guid = Guid('{1e84c900-7e70-11d0-a5d6-28db04c10000}')
AM_KSCATEGORY_AUDIO: Guid = Guid('{6994ad04-93ef-11d0-a3cc-00a0c9223196}')
AM_KSCATEGORY_VIDEO: Guid = Guid('{6994ad05-93ef-11d0-a3cc-00a0c9223196}')
AM_KSCATEGORY_TVTUNER: Guid = Guid('{a799a800-a46d-11d0-a18c-00a02401dcd4}')
AM_KSCATEGORY_CROSSBAR: Guid = Guid('{a799a801-a46d-11d0-a18c-00a02401dcd4}')
AM_KSCATEGORY_TVAUDIO: Guid = Guid('{a799a802-a46d-11d0-a18c-00a02401dcd4}')
AM_KSCATEGORY_VBICODEC: Guid = Guid('{07dad660-22f1-11d1-a9f4-00c04fbbde8f}')
AM_KSCATEGORY_VBICODEC_MI: Guid = Guid('{9c24a977-0951-451a-8006-0e49bd28cd5f}')
AM_KSCATEGORY_SPLITTER: Guid = Guid('{0a4252a0-7e70-11d0-a5d6-28db04c10000}')
AM_INTERFACESETID_Standard: Guid = Guid('{1a8766a0-62ce-11cf-a5d6-28db04c10000}')
PBDA_AUX_CONNECTOR_TYPE_SVideo: Guid = Guid('{a0e905f4-24c9-4a54-b761-213355efc13a}')
PBDA_AUX_CONNECTOR_TYPE_Composite: Guid = Guid('{f6298b4c-c725-4d42-849b-410bbb14ea62}')
CLSID_PBDA_AUX_DATA_TYPE: Guid = Guid('{fd456373-3323-4090-adca-8ed45f55cf10}')
CLSID_PBDA_Encoder_DATA_TYPE: Guid = Guid('{728fd6bc-5546-4716-b103-f899f5a1fa68}')
PBDA_Encoder_Audio_AlgorithmType_MPEG1LayerII: UInt32 = 0
PBDA_Encoder_Audio_AlgorithmType_AC3: UInt32 = 1
PBDA_Encoder_Video_MPEG2PartII: UInt32 = 0
PBDA_Encoder_Video_MPEG4Part10: UInt32 = 1
PBDA_Encoder_Video_AVC: UInt32 = 1
PBDA_Encoder_Video_H264: UInt32 = 1
PBDA_Encoder_BitrateMode_Constant: UInt32 = 1
PBDA_Encoder_BitrateMode_Variable: UInt32 = 2
PBDA_Encoder_BitrateMode_Average: UInt32 = 3
CLSID_PBDA_FDC_DATA_TYPE: Guid = Guid('{e7dbf9a0-22ab-4047-8e67-ef9ad504e729}')
CLSID_PBDA_GDDS_DATA_TYPE: Guid = Guid('{c80c0df3-6052-4c16-9f56-c44c21f73c45}')
LIBID_QuartzNetTypeLib: Guid = Guid('{56a868b1-0ad4-11ce-b03a-0020af0ba770}')
LIBID_QuartzTypeLib: Guid = Guid('{56a868b0-0ad4-11ce-b03a-0020af0ba770}')
CLSID_AMMultiMediaStream: Guid = Guid('{49c47ce5-9ba4-11d0-8212-00c04fc32c45}')
CLSID_AMDirectDrawStream: Guid = Guid('{49c47ce4-9ba4-11d0-8212-00c04fc32c45}')
CLSID_AMAudioStream: Guid = Guid('{8496e040-af4c-11d0-8212-00c04fc32c45}')
CLSID_AMAudioData: Guid = Guid('{f2468580-af8a-11d0-8212-00c04fc32c45}')
CLSID_AMMediaTypeStream: Guid = Guid('{cf0f2f7c-f7bf-11d0-900d-00c04fd9189d}')
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
CLSID_DMOWrapperFilter: Guid = Guid('{94297043-bd82-4dfd-b0de-8177739c6d20}')
CLSID_DMOFilterCategory: Guid = Guid('{bcd5796c-bd52-4d30-ab76-70f975b89199}')
AM_MPEG_AUDIO_DUAL_MERGE: UInt32 = 0
AM_MPEG_AUDIO_DUAL_LEFT: UInt32 = 1
AM_MPEG_AUDIO_DUAL_RIGHT: UInt32 = 2
VFW_FIRST_CODE: UInt32 = 512
MAX_ERROR_TEXT_LEN: UInt32 = 160
MPBOOL_TRUE: UInt32 = 1
MPBOOL_FALSE: UInt32 = 0
DWORD_ALLPARAMS: Int32 = -1
GUID_TIME_REFERENCE: Guid = Guid('{93ad712b-daa0-4ffe-bc81-b0ce500fcdd9}')
GUID_TIME_MUSIC: Guid = Guid('{0574c49d-5b04-4b15-a542-ae282030117b}')
GUID_TIME_SAMPLES: Guid = Guid('{a8593d05-0c43-4984-9a63-97af9e02c4c0}')
MPF_ENVLP_STANDARD: UInt32 = 0
MPF_ENVLP_BEGIN_CURRENTVAL: UInt32 = 1
MPF_ENVLP_BEGIN_NEUTRALVAL: UInt32 = 2
MPF_PUNCHIN_REFTIME: UInt32 = 0
MPF_PUNCHIN_NOW: UInt32 = 1
MPF_PUNCHIN_STOPPED: UInt32 = 2
MSPID_PrimaryVideo: Guid = Guid('{a35ff56a-9fda-11d0-8fdf-00c04fd9189d}')
MSPID_PrimaryAudio: Guid = Guid('{a35ff56b-9fda-11d0-8fdf-00c04fd9189d}')
VFW_E_INVALIDMEDIATYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
VFW_E_INVALIDSUBTYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
VFW_E_NEED_OWNER: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
VFW_E_ENUM_OUT_OF_SYNC: win32more.Windows.Win32.Foundation.HRESULT = -2147220989
VFW_E_ALREADY_CONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220988
VFW_E_FILTER_ACTIVE: win32more.Windows.Win32.Foundation.HRESULT = -2147220987
VFW_E_NO_TYPES: win32more.Windows.Win32.Foundation.HRESULT = -2147220986
VFW_E_NO_ACCEPTABLE_TYPES: win32more.Windows.Win32.Foundation.HRESULT = -2147220985
VFW_E_INVALID_DIRECTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220984
VFW_E_NOT_CONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220983
VFW_E_NO_ALLOCATOR: win32more.Windows.Win32.Foundation.HRESULT = -2147220982
VFW_E_RUNTIME_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147220981
VFW_E_BUFFER_NOTSET: win32more.Windows.Win32.Foundation.HRESULT = -2147220980
VFW_E_BUFFER_OVERFLOW: win32more.Windows.Win32.Foundation.HRESULT = -2147220979
VFW_E_BADALIGN: win32more.Windows.Win32.Foundation.HRESULT = -2147220978
VFW_E_ALREADY_COMMITTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220977
VFW_E_BUFFERS_OUTSTANDING: win32more.Windows.Win32.Foundation.HRESULT = -2147220976
VFW_E_NOT_COMMITTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220975
VFW_E_SIZENOTSET: win32more.Windows.Win32.Foundation.HRESULT = -2147220974
VFW_E_NO_CLOCK: win32more.Windows.Win32.Foundation.HRESULT = -2147220973
VFW_E_NO_SINK: win32more.Windows.Win32.Foundation.HRESULT = -2147220972
VFW_E_NO_INTERFACE: win32more.Windows.Win32.Foundation.HRESULT = -2147220971
VFW_E_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220970
VFW_E_CANNOT_CONNECT: win32more.Windows.Win32.Foundation.HRESULT = -2147220969
VFW_E_CANNOT_RENDER: win32more.Windows.Win32.Foundation.HRESULT = -2147220968
VFW_E_CHANGING_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147220967
VFW_E_NO_COLOR_KEY_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220966
VFW_E_NOT_OVERLAY_CONNECTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220965
VFW_E_NOT_SAMPLE_CONNECTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220964
VFW_E_PALETTE_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220963
VFW_E_COLOR_KEY_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220962
VFW_E_NO_COLOR_KEY_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220961
VFW_E_NO_PALETTE_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220960
VFW_E_NO_DISPLAY_PALETTE: win32more.Windows.Win32.Foundation.HRESULT = -2147220959
VFW_E_TOO_MANY_COLORS: win32more.Windows.Win32.Foundation.HRESULT = -2147220958
VFW_E_STATE_CHANGED: win32more.Windows.Win32.Foundation.HRESULT = -2147220957
VFW_E_NOT_STOPPED: win32more.Windows.Win32.Foundation.HRESULT = -2147220956
VFW_E_NOT_PAUSED: win32more.Windows.Win32.Foundation.HRESULT = -2147220955
VFW_E_NOT_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2147220954
VFW_E_WRONG_STATE: win32more.Windows.Win32.Foundation.HRESULT = -2147220953
VFW_E_START_TIME_AFTER_END: win32more.Windows.Win32.Foundation.HRESULT = -2147220952
VFW_E_INVALID_RECT: win32more.Windows.Win32.Foundation.HRESULT = -2147220951
VFW_E_TYPE_NOT_ACCEPTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220950
VFW_E_SAMPLE_REJECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220949
VFW_E_SAMPLE_REJECTED_EOS: win32more.Windows.Win32.Foundation.HRESULT = -2147220948
VFW_E_DUPLICATE_NAME: win32more.Windows.Win32.Foundation.HRESULT = -2147220947
VFW_S_DUPLICATE_NAME: win32more.Windows.Win32.Foundation.HRESULT = 262701
VFW_E_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147220946
VFW_E_INVALID_FILE_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147220945
VFW_E_ENUM_OUT_OF_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -2147220944
VFW_E_CIRCULAR_GRAPH: win32more.Windows.Win32.Foundation.HRESULT = -2147220943
VFW_E_NOT_ALLOWED_TO_SAVE: win32more.Windows.Win32.Foundation.HRESULT = -2147220942
VFW_E_TIME_ALREADY_PASSED: win32more.Windows.Win32.Foundation.HRESULT = -2147220941
VFW_E_ALREADY_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -2147220940
VFW_E_CORRUPT_GRAPH_FILE: win32more.Windows.Win32.Foundation.HRESULT = -2147220939
VFW_E_ADVISE_ALREADY_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220938
VFW_S_STATE_INTERMEDIATE: win32more.Windows.Win32.Foundation.HRESULT = 262711
VFW_E_NO_MODEX_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220936
VFW_E_NO_ADVISE_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220935
VFW_E_NO_FULLSCREEN: win32more.Windows.Win32.Foundation.HRESULT = -2147220934
VFW_E_IN_FULLSCREEN_MODE: win32more.Windows.Win32.Foundation.HRESULT = -2147220933
VFW_E_UNKNOWN_FILE_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147220928
VFW_E_CANNOT_LOAD_SOURCE_FILTER: win32more.Windows.Win32.Foundation.HRESULT = -2147220927
VFW_S_PARTIAL_RENDER: win32more.Windows.Win32.Foundation.HRESULT = 262722
VFW_E_FILE_TOO_SHORT: win32more.Windows.Win32.Foundation.HRESULT = -2147220925
VFW_E_INVALID_FILE_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -2147220924
VFW_S_SOME_DATA_IGNORED: win32more.Windows.Win32.Foundation.HRESULT = 262725
VFW_S_CONNECTIONS_DEFERRED: win32more.Windows.Win32.Foundation.HRESULT = 262726
VFW_E_INVALID_CLSID: win32more.Windows.Win32.Foundation.HRESULT = -2147220921
VFW_E_INVALID_MEDIA_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147220920
VFW_E_BAD_KEY: win32more.Windows.Win32.Foundation.HRESULT = -2147220494
VFW_S_NO_MORE_ITEMS: win32more.Windows.Win32.Foundation.HRESULT = 262403
VFW_E_SAMPLE_TIME_NOT_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220919
VFW_S_RESOURCE_NOT_NEEDED: win32more.Windows.Win32.Foundation.HRESULT = 262736
VFW_E_MEDIA_TIME_NOT_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220911
VFW_E_NO_TIME_FORMAT_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220910
VFW_E_MONO_AUDIO_HW: win32more.Windows.Win32.Foundation.HRESULT = -2147220909
VFW_S_MEDIA_TYPE_IGNORED: win32more.Windows.Win32.Foundation.HRESULT = 262740
VFW_E_NO_DECOMPRESSOR: win32more.Windows.Win32.Foundation.HRESULT = -2147220907
VFW_E_NO_AUDIO_HARDWARE: win32more.Windows.Win32.Foundation.HRESULT = -2147220906
VFW_S_VIDEO_NOT_RENDERED: win32more.Windows.Win32.Foundation.HRESULT = 262743
VFW_S_AUDIO_NOT_RENDERED: win32more.Windows.Win32.Foundation.HRESULT = 262744
VFW_E_RPZA: win32more.Windows.Win32.Foundation.HRESULT = -2147220903
VFW_S_RPZA: win32more.Windows.Win32.Foundation.HRESULT = 262746
VFW_E_PROCESSOR_NOT_SUITABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220901
VFW_E_UNSUPPORTED_AUDIO: win32more.Windows.Win32.Foundation.HRESULT = -2147220900
VFW_E_UNSUPPORTED_VIDEO: win32more.Windows.Win32.Foundation.HRESULT = -2147220899
VFW_E_MPEG_NOT_CONSTRAINED: win32more.Windows.Win32.Foundation.HRESULT = -2147220898
VFW_E_NOT_IN_GRAPH: win32more.Windows.Win32.Foundation.HRESULT = -2147220897
VFW_S_ESTIMATED: win32more.Windows.Win32.Foundation.HRESULT = 262752
VFW_E_NO_TIME_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147220895
VFW_E_READ_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -2147220894
VFW_S_RESERVED: win32more.Windows.Win32.Foundation.HRESULT = 262755
VFW_E_BUFFER_UNDERFLOW: win32more.Windows.Win32.Foundation.HRESULT = -2147220892
VFW_E_UNSUPPORTED_STREAM: win32more.Windows.Win32.Foundation.HRESULT = -2147220891
VFW_E_NO_TRANSPORT: win32more.Windows.Win32.Foundation.HRESULT = -2147220890
VFW_S_STREAM_OFF: win32more.Windows.Win32.Foundation.HRESULT = 262759
VFW_S_CANT_CUE: win32more.Windows.Win32.Foundation.HRESULT = 262760
VFW_E_BAD_VIDEOCD: win32more.Windows.Win32.Foundation.HRESULT = -2147220887
VFW_S_NO_STOP_TIME: win32more.Windows.Win32.Foundation.HRESULT = 262768
VFW_E_OUT_OF_VIDEO_MEMORY: win32more.Windows.Win32.Foundation.HRESULT = -2147220879
VFW_E_VP_NEGOTIATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147220878
VFW_E_DDRAW_CAPS_NOT_SUITABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220877
VFW_E_NO_VP_HARDWARE: win32more.Windows.Win32.Foundation.HRESULT = -2147220876
VFW_E_NO_CAPTURE_HARDWARE: win32more.Windows.Win32.Foundation.HRESULT = -2147220875
VFW_E_DVD_OPERATION_INHIBITED: win32more.Windows.Win32.Foundation.HRESULT = -2147220874
VFW_E_DVD_INVALIDDOMAIN: win32more.Windows.Win32.Foundation.HRESULT = -2147220873
VFW_E_DVD_NO_BUTTON: win32more.Windows.Win32.Foundation.HRESULT = -2147220872
VFW_E_DVD_GRAPHNOTREADY: win32more.Windows.Win32.Foundation.HRESULT = -2147220871
VFW_E_DVD_RENDERFAIL: win32more.Windows.Win32.Foundation.HRESULT = -2147220870
VFW_E_DVD_DECNOTENOUGH: win32more.Windows.Win32.Foundation.HRESULT = -2147220869
VFW_E_DDRAW_VERSION_NOT_SUITABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220868
VFW_E_COPYPROT_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147220867
VFW_S_NOPREVIEWPIN: win32more.Windows.Win32.Foundation.HRESULT = 262782
VFW_E_TIME_EXPIRED: win32more.Windows.Win32.Foundation.HRESULT = -2147220865
VFW_S_DVD_NON_ONE_SEQUENTIAL: win32more.Windows.Win32.Foundation.HRESULT = 262784
VFW_E_DVD_WRONG_SPEED: win32more.Windows.Win32.Foundation.HRESULT = -2147220863
VFW_E_DVD_MENU_DOES_NOT_EXIST: win32more.Windows.Win32.Foundation.HRESULT = -2147220862
VFW_E_DVD_CMD_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -2147220861
VFW_E_DVD_STATE_WRONG_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -2147220860
VFW_E_DVD_STATE_CORRUPT: win32more.Windows.Win32.Foundation.HRESULT = -2147220859
VFW_E_DVD_STATE_WRONG_DISC: win32more.Windows.Win32.Foundation.HRESULT = -2147220858
VFW_E_DVD_INCOMPATIBLE_REGION: win32more.Windows.Win32.Foundation.HRESULT = -2147220857
VFW_E_DVD_NO_ATTRIBUTES: win32more.Windows.Win32.Foundation.HRESULT = -2147220856
VFW_E_DVD_NO_GOUP_PGC: win32more.Windows.Win32.Foundation.HRESULT = -2147220855
VFW_E_DVD_LOW_PARENTAL_LEVEL: win32more.Windows.Win32.Foundation.HRESULT = -2147220854
VFW_E_DVD_NOT_IN_KARAOKE_MODE: win32more.Windows.Win32.Foundation.HRESULT = -2147220853
VFW_S_DVD_CHANNEL_CONTENTS_NOT_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = 262796
VFW_S_DVD_NOT_ACCURATE: win32more.Windows.Win32.Foundation.HRESULT = 262797
VFW_E_FRAME_STEP_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220850
VFW_E_DVD_STREAM_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2147220849
VFW_E_DVD_TITLE_UNKNOWN: win32more.Windows.Win32.Foundation.HRESULT = -2147220848
VFW_E_DVD_INVALID_DISC: win32more.Windows.Win32.Foundation.HRESULT = -2147220847
VFW_E_DVD_NO_RESUME_INFORMATION: win32more.Windows.Win32.Foundation.HRESULT = -2147220846
VFW_E_PIN_ALREADY_BLOCKED_ON_THIS_THREAD: win32more.Windows.Win32.Foundation.HRESULT = -2147220845
VFW_E_PIN_ALREADY_BLOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2147220844
VFW_E_CERTIFICATION_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2147220843
VFW_E_VMR_NOT_IN_MIXER_MODE: win32more.Windows.Win32.Foundation.HRESULT = -2147220842
VFW_E_VMR_NO_AP_SUPPLIED: win32more.Windows.Win32.Foundation.HRESULT = -2147220841
VFW_E_VMR_NO_DEINTERLACE_HW: win32more.Windows.Win32.Foundation.HRESULT = -2147220840
VFW_E_VMR_NO_PROCAMP_HW: win32more.Windows.Win32.Foundation.HRESULT = -2147220839
VFW_E_DVD_VMR9_INCOMPATIBLEDEC: win32more.Windows.Win32.Foundation.HRESULT = -2147220838
VFW_E_NO_COPP_HW: win32more.Windows.Win32.Foundation.HRESULT = -2147220837
VFW_E_DVD_NONBLOCKING: win32more.Windows.Win32.Foundation.HRESULT = -2147220836
VFW_E_DVD_TOO_MANY_RENDERERS_IN_FILTER_GRAPH: win32more.Windows.Win32.Foundation.HRESULT = -2147220835
VFW_E_DVD_NON_EVR_RENDERER_IN_FILTER_GRAPH: win32more.Windows.Win32.Foundation.HRESULT = -2147220834
VFW_E_DVD_RESOLUTION_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147220833
E_PROP_SET_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147023726
E_PROP_ID_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147023728
VFW_E_CODECAPI_LINEAR_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -2147220720
VFW_E_CODECAPI_ENUMERATED: win32more.Windows.Win32.Foundation.HRESULT = -2147220719
VFW_E_CODECAPI_NO_DEFAULT: win32more.Windows.Win32.Foundation.HRESULT = -2147220717
VFW_E_CODECAPI_NO_CURRENT_VALUE: win32more.Windows.Win32.Foundation.HRESULT = -2147220716
VFW_E_DVD_CHAPTER_DOES_NOT_EXIST: win32more.Windows.Win32.Foundation.HRESULT = -2147220715
VFW_S_DVD_RENDER_STATUS: win32more.Windows.Win32.Foundation.HRESULT = 262944
CFSTR_VFW_FILTERLIST: String = 'Video for Windows 4 Filters'
DXVA_ModeNone: Guid = Guid('{1b81be00-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH261_A: Guid = Guid('{1b81be01-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH261_B: Guid = Guid('{1b81be02-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH263_A: Guid = Guid('{1b81be03-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH263_B: Guid = Guid('{1b81be04-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH263_C: Guid = Guid('{1b81be05-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH263_D: Guid = Guid('{1b81be06-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH263_E: Guid = Guid('{1b81be07-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH263_F: Guid = Guid('{1b81be08-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeMPEG1_A: Guid = Guid('{1b81be09-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeMPEG1_VLD: Guid = Guid('{6f3ec719-3735-42cc-8063-65cc3cb36616}')
DXVA_ModeMPEG2_A: Guid = Guid('{1b81be0a-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeMPEG2_B: Guid = Guid('{1b81be0b-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeMPEG2_C: Guid = Guid('{1b81be0c-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeMPEG2_D: Guid = Guid('{1b81be0d-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeMPEG2and1_VLD: Guid = Guid('{86695f12-340e-4f04-9fd3-9253dd327460}')
DXVA_ModeH264_A: Guid = Guid('{1b81be64-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH264_B: Guid = Guid('{1b81be65-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH264_C: Guid = Guid('{1b81be66-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH264_D: Guid = Guid('{1b81be67-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH264_E: Guid = Guid('{1b81be68-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH264_F: Guid = Guid('{1b81be69-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeH264_VLD_WithFMOASO_NoFGT: Guid = Guid('{d5f04ff9-3418-45d8-9561-32a76aae2ddd}')
DXVA_ModeH264_VLD_Stereo_Progressive_NoFGT: Guid = Guid('{d79be8da-0cf1-4c81-b82a-69a4e236f43d}')
DXVA_ModeH264_VLD_Stereo_NoFGT: Guid = Guid('{f9aaccbb-c2b6-4cfc-8779-5707b1760552}')
DXVA_ModeH264_VLD_Multiview_NoFGT: Guid = Guid('{705b9d82-76cf-49d6-b7e6-ac8872db013c}')
DXVA_ModeWMV8_A: Guid = Guid('{1b81be80-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeWMV8_B: Guid = Guid('{1b81be81-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeWMV9_A: Guid = Guid('{1b81be90-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeWMV9_B: Guid = Guid('{1b81be91-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeWMV9_C: Guid = Guid('{1b81be94-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeVC1_A: Guid = Guid('{1b81bea0-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeVC1_B: Guid = Guid('{1b81bea1-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeVC1_C: Guid = Guid('{1b81bea2-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeVC1_D: Guid = Guid('{1b81bea3-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeVC1_D2010: Guid = Guid('{1b81bea4-a0c7-11d3-b984-00c04f2e73c5}')
DXVA_ModeMPEG4pt2_VLD_Simple: Guid = Guid('{efd64d74-c9e8-41d7-a5e9-e9b0e39fa319}')
DXVA_ModeMPEG4pt2_VLD_AdvSimple_NoGMC: Guid = Guid('{ed418a9f-010d-4eda-9ae3-9a65358d8d2e}')
DXVA_ModeMPEG4pt2_VLD_AdvSimple_GMC: Guid = Guid('{ab998b5b-4258-44a9-9feb-94e597a6baae}')
DXVA_ModeHEVC_VLD_Main: Guid = Guid('{5b11d51b-2f4c-4452-bcc3-09f2a1160cc0}')
DXVA_ModeHEVC_VLD_Main10: Guid = Guid('{107af0e0-ef1a-4d19-aba8-67a163073d13}')
DXVA_ModeVP9_VLD_Profile0: Guid = Guid('{463707f8-a1d0-4585-876d-83aa6d60b89e}')
DXVA_ModeVP9_VLD_10bit_Profile2: Guid = Guid('{a4c749ef-6ecf-48aa-8448-50a7a1165ff7}')
DXVA_ModeVP8_VLD: Guid = Guid('{90b899ea-3a62-4705-88b3-8df04b2744e7}')
DXVA_ModeAV1_VLD_Profile0: Guid = Guid('{b8be4ccb-cf53-46ba-8d59-d6b8a6da5d2a}')
DXVA_ModeAV1_VLD_Profile1: Guid = Guid('{6936ff0f-45b1-4163-9cc1-646ef6946108}')
DXVA_ModeAV1_VLD_Profile2: Guid = Guid('{0c5f2aa1-e541-4089-bb7b-98110a19d7c8}')
DXVA_ModeAV1_VLD_12bit_Profile2: Guid = Guid('{17127009-a00f-4ce1-994e-bf4081f6f3f0}')
DXVA_ModeAV1_VLD_12bit_Profile2_420: Guid = Guid('{2d80bed6-9cac-4835-9e91-327bbc4f9ee8}')
DXVA_NoEncrypt: Guid = Guid('{1b81bed0-a0c7-11d3-b984-00c04f2e73c5}')
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
DXVA_DeinterlaceBobDevice: Guid = Guid('{335aa36e-7884-43a4-9c91-7f87faf3e37e}')
DXVA_DeinterlaceContainerDevice: Guid = Guid('{0e85cb93-3046-4ff0-aecc-d58cb5f035fd}')
MAX_DEINTERLACE_SURFACES: UInt32 = 32
DXVA_DeinterlaceBltFnCode: UInt32 = 1
DXVA_DeinterlaceBltExFnCode: UInt32 = 2
MAX_DEINTERLACE_DEVICE_GUIDS: UInt32 = 32
DXVA_DeinterlaceQueryAvailableModesFnCode: UInt32 = 1
DXVA_DeinterlaceQueryModeCapsFnCode: UInt32 = 2
DXVA_ProcAmpControlDevice: Guid = Guid('{9f200913-2ffd-4056-9f1e-e1b508f22dcf}')
DXVA_ProcAmpControlQueryCapsFnCode: UInt32 = 3
DXVA_ProcAmpControlQueryRangeFnCode: UInt32 = 4
DXVA_ProcAmpControlBltFnCode: UInt32 = 1
DXVA_COPPDevice: Guid = Guid('{d2457add-8999-45ed-8a8a-d1aa047ba4d5}')
DXVA_COPPGetCertificateLengthFnCode: UInt32 = 1
DXVA_COPPKeyExchangeFnCode: UInt32 = 2
DXVA_COPPSequenceStartFnCode: UInt32 = 3
DXVA_COPPCommandFnCode: UInt32 = 4
DXVA_COPPSetProtectionLevel: Guid = Guid('{9bb9327c-4eb5-4727-9f00-b42b0919c0da}')
COPP_NoProtectionLevelAvailable: Int32 = -1
COPP_DefaultProtectionLevel: UInt32 = 0
DXVA_COPPSetSignaling: Guid = Guid('{09a631a5-d684-4c60-8e4d-d3bb0f0be3ee}')
COPP_ImageAspectRatio_EN300294_Mask: UInt32 = 7
DXVA_COPPQueryStatusFnCode: UInt32 = 5
DXVA_COPPQueryConnectorType: Guid = Guid('{81d0bfd5-6afe-48c2-99c0-95a08f97c5da}')
DXVA_COPPQueryProtectionType: Guid = Guid('{38f2a801-9a6c-48bb-9107-b6696e6f1797}')
DXVA_COPPQueryLocalProtectionLevel: Guid = Guid('{b2075857-3eda-4d5d-88db-748f8c1a0549}')
DXVA_COPPQueryGlobalProtectionLevel: Guid = Guid('{1957210a-7766-452a-b99a-d27aed54f03a}')
DXVA_COPPQueryDisplayData: Guid = Guid('{d7bf1ba3-ad13-4f8e-af98-0dcb3ca204cc}')
DXVA_COPPQueryHDCPKeyData: Guid = Guid('{0db59d74-a992-492e-a0bd-c23fda564e00}')
DXVA_COPPQueryBusData: Guid = Guid('{c6f4d673-6174-4184-8e35-f6db5200bcba}')
DXVA_COPPQuerySignaling: Guid = Guid('{6629a591-3b79-4cf3-924a-11e8e7811671}')
DXVA2Trace_Control: Guid = Guid('{a0386e75-f70c-464c-a9ce-33c44e091623}')
DXVA2Trace_DecodeDevCreated: Guid = Guid('{b4de17a1-c5b2-44fe-86d5-d97a648114ff}')
DXVA2Trace_DecodeDevDestroyed: Guid = Guid('{853ebdf2-4160-421d-8893-63dcea4f18bb}')
DXVA2Trace_DecodeDevBeginFrame: Guid = Guid('{9fd1acf6-44cb-4637-bc62-2c11a9608f90}')
DXVA2Trace_DecodeDevExecute: Guid = Guid('{850aeb4c-d19a-4609-b3b4-bcbf0e22121e}')
DXVA2Trace_DecodeDevGetBuffer: Guid = Guid('{57b128fb-72cb-4137-a575-d91fa3160897}')
DXVA2Trace_DecodeDevEndFrame: Guid = Guid('{9fb3cb33-47dc-4899-98c8-c0c6cd7cd3cb}')
DXVA2Trace_VideoProcessDevCreated: Guid = Guid('{895508c6-540d-4c87-98f8-8dcbf2dabb2a}')
DXVA2Trace_VideoProcessDevDestroyed: Guid = Guid('{f97f30b1-fb49-42c7-8ee8-88bdfa92d4e2}')
DXVA2Trace_VideoProcessBlt: Guid = Guid('{69089cc0-71ab-42d0-953a-2887bf05a8af}')
MSTapeDeviceGUID: Guid = Guid('{8c0f6af2-0edb-44c1-8aeb-59040bd830ed}')
g_wszExcludeScriptStreamDeliverySynchronization: String = 'ExcludeScriptStreamDeliverySynchronization'
MPEG2_BASE: UInt32 = 512
MPEG2_S_MORE_DATA_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = 262656
MPEG2_S_NO_MORE_DATA_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = 262657
MPEG2_S_SG_INFO_FOUND: win32more.Windows.Win32.Foundation.HRESULT = 262658
MPEG2_S_SG_INFO_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = 262659
MPEG2_S_MPE_INFO_FOUND: win32more.Windows.Win32.Foundation.HRESULT = 262660
MPEG2_S_MPE_INFO_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = 262661
MPEG2_S_NEW_MODULE_VERSION: win32more.Windows.Win32.Foundation.HRESULT = 262662
MPEG2_E_UNINITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
MPEG2_E_ALREADY_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
MPEG2_E_OUT_OF_BOUNDS: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
MPEG2_E_MALFORMED_TABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220989
MPEG2_E_UNDEFINED: win32more.Windows.Win32.Foundation.HRESULT = -2147220988
MPEG2_E_NOT_PRESENT: win32more.Windows.Win32.Foundation.HRESULT = -2147220987
MPEG2_E_SECTION_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220986
MPEG2_E_TX_STREAM_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220985
MPEG2_E_SERVICE_ID_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220984
MPEG2_E_SERVICE_PMT_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220983
MPEG2_E_DSI_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220982
MPEG2_E_SERVER_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220981
MPEG2_E_INVALID_CAROUSEL_ID: win32more.Windows.Win32.Foundation.HRESULT = -2147220980
MPEG2_E_MALFORMED_DSMCC_MESSAGE: win32more.Windows.Win32.Foundation.HRESULT = -2147220979
MPEG2_E_INVALID_SG_OBJECT_KIND: win32more.Windows.Win32.Foundation.HRESULT = -2147220978
MPEG2_E_OBJECT_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220977
MPEG2_E_OBJECT_KIND_NOT_A_DIRECTORY: win32more.Windows.Win32.Foundation.HRESULT = -2147220976
MPEG2_E_OBJECT_KIND_NOT_A_FILE: win32more.Windows.Win32.Foundation.HRESULT = -2147220975
MPEG2_E_FILE_OFFSET_TOO_BIG: win32more.Windows.Win32.Foundation.HRESULT = -2147220974
MPEG2_E_STREAM_STOPPED: win32more.Windows.Win32.Foundation.HRESULT = -2147220973
MPEG2_E_REGISTRY_ACCESS_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147220972
MPEG2_E_INVALID_UDP_PORT: win32more.Windows.Win32.Foundation.HRESULT = -2147220971
MPEG2_E_DATA_SOURCE_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147220970
MPEG2_E_DII_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220969
MPEG2_E_DSHOW_PIN_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220968
MPEG2_E_BUFFER_TOO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = -2147220967
MPEG2_E_MISSING_SECTIONS: win32more.Windows.Win32.Foundation.HRESULT = -2147220966
MPEG2_E_TOO_MANY_SECTIONS: win32more.Windows.Win32.Foundation.HRESULT = -2147220965
MPEG2_E_NEXT_TABLE_OPS_NOT_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220964
MPEG2_E_INCORRECT_DESCRIPTOR_TAG: win32more.Windows.Win32.Foundation.HRESULT = -2147220963
MSDRI_S_MMI_PENDING: win32more.Windows.Win32.Foundation.HRESULT = 2
MSDRI_S_PENDING: win32more.Windows.Win32.Foundation.HRESULT = 1
BDA_E_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1073479679
BDA_E_NOT_IMPLEMENTED: win32more.Windows.Win32.Foundation.HRESULT = -1073479678
BDA_E_NO_SUCH_COMMAND: win32more.Windows.Win32.Foundation.HRESULT = -1073479677
BDA_E_OUT_OF_BOUNDS: win32more.Windows.Win32.Foundation.HRESULT = -1073479676
BDA_E_INVALID_SCHEMA: win32more.Windows.Win32.Foundation.HRESULT = -1073479675
BDA_E_INVALID_HANDLE: win32more.Windows.Win32.Foundation.HRESULT = -1073479674
BDA_E_INVALID_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -1073479673
BDA_E_READ_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -1073479672
BDA_E_ACCESS_DENIED: win32more.Windows.Win32.Foundation.HRESULT = -1073479671
BDA_E_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1073479670
BDA_E_BUFFER_TOO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = -1073479669
BDA_E_OUT_OF_RESOURCES: win32more.Windows.Win32.Foundation.HRESULT = -1073479668
BDA_E_OUT_OF_MEMORY: win32more.Windows.Win32.Foundation.HRESULT = -1073479667
BDA_E_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -1073479666
BDA_E_NO_HANDLER: win32more.Windows.Win32.Foundation.HRESULT = -1073479665
BDA_E_INVALID_LANGUAGE: win32more.Windows.Win32.Foundation.HRESULT = -1073479664
BDA_E_TIMEOUT_ELAPSED: win32more.Windows.Win32.Foundation.HRESULT = -1073479663
BDA_E_NO_MORE_EVENTS: win32more.Windows.Win32.Foundation.HRESULT = -1073475583
BDA_E_NO_MORE_DATA: win32more.Windows.Win32.Foundation.HRESULT = -1073475582
BDA_E_TUNER_INITIALIZING: win32more.Windows.Win32.Foundation.HRESULT = -1073467391
BDA_E_TUNER_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -1073467390
BDA_E_TUNER_CONFLICT: win32more.Windows.Win32.Foundation.HRESULT = -1073467389
BDA_E_INVALID_TUNE_REQUEST: win32more.Windows.Win32.Foundation.HRESULT = -1073467388
BDA_E_INVALID_ENTITLEMENT_TOKEN: win32more.Windows.Win32.Foundation.HRESULT = -1073463295
BDA_E_INVALID_CAPTURE_TOKEN: win32more.Windows.Win32.Foundation.HRESULT = -1073463294
BDA_E_WOULD_DISRUPT_STREAMING: win32more.Windows.Win32.Foundation.HRESULT = -1073463293
BDA_E_INVALID_PURCHASE_TOKEN: win32more.Windows.Win32.Foundation.HRESULT = -1073463292
BDA_E_IPNETWORK_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -1073459199
BDA_E_IPNETWORK_ADDRESS_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1073459198
BDA_E_IPNETWORK_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -1073459197
BDA_E_IPNETWORK_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -1073459196
BDA_E_TUNE_FAILED_SDV01: win32more.Windows.Win32.Foundation.HRESULT = -1073455103
BDA_E_TUNE_FAILED_SDV02: win32more.Windows.Win32.Foundation.HRESULT = -1073455102
BDA_E_TUNE_FAILED_SDV03: win32more.Windows.Win32.Foundation.HRESULT = -1073455101
BDA_E_TUNE_FAILED_SDV04: win32more.Windows.Win32.Foundation.HRESULT = -1073455100
BDA_E_TUNE_FAILED_SDV05: win32more.Windows.Win32.Foundation.HRESULT = -1073455099
BDA_E_TUNE_FAILED_SDV06: win32more.Windows.Win32.Foundation.HRESULT = -1073455098
BDA_E_TUNE_FAILED_SDV07: win32more.Windows.Win32.Foundation.HRESULT = -1073455097
BDA_E_TUNE_FAILED_SDV08: win32more.Windows.Win32.Foundation.HRESULT = -1073455096
BDA_E_TUNE_FAILED_SDVFF: win32more.Windows.Win32.Foundation.HRESULT = -1073454849
BDA_E_WMDRM_INVALID_SIGNATURE: win32more.Windows.Win32.Foundation.HRESULT = -1073418239
BDA_E_WMDRM_INVALID_CERTIFICATE: win32more.Windows.Win32.Foundation.HRESULT = -1073418238
BDA_E_WMDRM_INVALID_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -1073418236
BDA_E_WMDRM_INVALID_DATE: win32more.Windows.Win32.Foundation.HRESULT = -1073418235
BDA_E_WMDRM_INVALID_PROXIMITY: win32more.Windows.Win32.Foundation.HRESULT = -1073418234
BDA_E_WMDRM_KEY_ID_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1073418232
SPECIFYPAGES_STATISTICS: Guid = Guid('{4c437b92-6e9e-11d1-a704-006097c4e476}')
@winfunctype('QUARTZ.dll')
def AMGetErrorTextA(hr: win32more.Windows.Win32.Foundation.HRESULT, pbuffer: win32more.Windows.Win32.Foundation.PSTR, MaxLen: UInt32) -> UInt32: ...
@winfunctype('QUARTZ.dll')
def AMGetErrorTextW(hr: win32more.Windows.Win32.Foundation.HRESULT, pbuffer: win32more.Windows.Win32.Foundation.PWSTR, MaxLen: UInt32) -> UInt32: ...
AMGetErrorText = UnicodeAlias('AMGetErrorTextW')
ApplicationTypeType = Int32
SCTE28_ConditionalAccess: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 0
SCTE28_POD_Host_Binding_Information: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 1
SCTE28_IPService: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 2
SCTE28_NetworkInterface_SCTE55_2: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 3
SCTE28_NetworkInterface_SCTE55_1: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 4
SCTE28_CopyProtection: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 5
SCTE28_Diagnostic: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 6
SCTE28_Undesignated: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 7
SCTE28_Reserved: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType = 8
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
BDA_CHANGES_COMPLETE: win32more.Windows.Win32.Media.DirectShow.BDA_CHANGE_STATE = 0
BDA_CHANGES_PENDING: win32more.Windows.Win32.Media.DirectShow.BDA_CHANGE_STATE = 1
BDA_CONDITIONALACCESS_MMICLOSEREASON = Int32
CONDITIONALACCESS_UNSPECIFIED: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON = 0
CONDITIONALACCESS_CLOSED_ITSELF: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON = 1
CONDITIONALACCESS_TUNER_REQUESTED_CLOSE: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON = 2
CONDITIONALACCESS_DIALOG_TIMEOUT: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON = 3
CONDITIONALACCESS_DIALOG_FOCUS_CHANGE: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON = 4
CONDITIONALACCESS_DIALOG_USER_DISMISSED: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON = 5
CONDITIONALACCESS_DIALOG_USER_NOT_AVAILABLE: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON = 6
BDA_CONDITIONALACCESS_REQUESTTYPE = Int32
CONDITIONALACCESS_ACCESS_UNSPECIFIED: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_REQUESTTYPE = 0
CONDITIONALACCESS_ACCESS_NOT_POSSIBLE: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_REQUESTTYPE = 1
CONDITIONALACCESS_ACCESS_POSSIBLE: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_REQUESTTYPE = 2
CONDITIONALACCESS_ACCESS_POSSIBLE_NO_STREAMING_DISRUPTION: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_REQUESTTYPE = 3
BDA_CONDITIONALACCESS_SESSION_RESULT = Int32
CONDITIONALACCESS_SUCCESSFULL: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_SESSION_RESULT = 0
CONDITIONALACCESS_ENDED_NOCHANGE: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_SESSION_RESULT = 1
CONDITIONALACCESS_ABORTED: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_SESSION_RESULT = 2
BDA_Channel = Int32
BDA_UNDEFINED_CHANNEL: win32more.Windows.Win32.Media.DirectShow.BDA_Channel = -1
BDA_Channel_Bandwidth = Int32
BDA_CHAN_BANDWITH_NOT_SET: win32more.Windows.Win32.Media.DirectShow.BDA_Channel_Bandwidth = -1
BDA_CHAN_BANDWITH_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.BDA_Channel_Bandwidth = 0
BDA_Comp_Flags = Int32
BDACOMP_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.BDA_Comp_Flags = 0
BDACOMP_EXCLUDE_TS_FROM_TR: win32more.Windows.Win32.Media.DirectShow.BDA_Comp_Flags = 1
BDACOMP_INCLUDE_LOCATOR_IN_TR: win32more.Windows.Win32.Media.DirectShow.BDA_Comp_Flags = 2
BDACOMP_INCLUDE_COMPONENTS_IN_TR: win32more.Windows.Win32.Media.DirectShow.BDA_Comp_Flags = 4
BDA_DISCOVERY_STATE = Int32
BDA_DISCOVERY_UNSPECIFIED: win32more.Windows.Win32.Media.DirectShow.BDA_DISCOVERY_STATE = 0
BDA_DISCOVERY_REQUIRED: win32more.Windows.Win32.Media.DirectShow.BDA_DISCOVERY_STATE = 1
BDA_DISCOVERY_COMPLETE: win32more.Windows.Win32.Media.DirectShow.BDA_DISCOVERY_STATE = 2
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
BDA_DrmPairingError = Int32
BDA_DrmPairing_Succeeded: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 0
BDA_DrmPairing_HardwareFailure: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 1
BDA_DrmPairing_NeedRevocationData: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 2
BDA_DrmPairing_NeedIndiv: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 3
BDA_DrmPairing_Other: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 4
BDA_DrmPairing_DrmInitFailed: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 5
BDA_DrmPairing_DrmNotPaired: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 6
BDA_DrmPairing_DrmRePairSoon: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 7
BDA_DrmPairing_Aborted: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 8
BDA_DrmPairing_NeedSDKUpdate: win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError = 9
class BDA_ETHERNET_ADDRESS(Structure):
    rgbAddress: Byte * 6
class BDA_ETHERNET_ADDRESS_LIST(Structure):
    ulcAddresses: UInt32
    rgAddressl: win32more.Windows.Win32.Media.DirectShow.BDA_ETHERNET_ADDRESS * 1
BDA_EVENT_ID = Int32
BDA_EVENT_SIGNAL_LOSS: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 0
BDA_EVENT_SIGNAL_LOCK: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 1
BDA_EVENT_DATA_START: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 2
BDA_EVENT_DATA_STOP: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 3
BDA_EVENT_CHANNEL_ACQUIRED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 4
BDA_EVENT_CHANNEL_LOST: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 5
BDA_EVENT_CHANNEL_SOURCE_CHANGED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 6
BDA_EVENT_CHANNEL_ACTIVATED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 7
BDA_EVENT_CHANNEL_DEACTIVATED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 8
BDA_EVENT_SUBCHANNEL_ACQUIRED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 9
BDA_EVENT_SUBCHANNEL_LOST: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 10
BDA_EVENT_SUBCHANNEL_SOURCE_CHANGED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 11
BDA_EVENT_SUBCHANNEL_ACTIVATED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 12
BDA_EVENT_SUBCHANNEL_DEACTIVATED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 13
BDA_EVENT_ACCESS_GRANTED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 14
BDA_EVENT_ACCESS_DENIED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 15
BDA_EVENT_OFFER_EXTENDED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 16
BDA_EVENT_PURCHASE_COMPLETED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 17
BDA_EVENT_SMART_CARD_INSERTED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 18
BDA_EVENT_SMART_CARD_REMOVED: win32more.Windows.Win32.Media.DirectShow.BDA_EVENT_ID = 19
BDA_Frequency = Int32
BDA_FREQUENCY_NOT_SET: win32more.Windows.Win32.Media.DirectShow.BDA_Frequency = -1
BDA_FREQUENCY_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.BDA_Frequency = 0
BDA_Frequency_Multiplier = Int32
BDA_FREQUENCY_MULTIPLIER_NOT_SET: win32more.Windows.Win32.Media.DirectShow.BDA_Frequency_Multiplier = -1
BDA_FREQUENCY_MULTIPLIER_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.BDA_Frequency_Multiplier = 0
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
    rgAddressl: win32more.Windows.Win32.Media.DirectShow.BDA_IPv4_ADDRESS * 1
class BDA_IPv6_ADDRESS(Structure):
    rgbAddress: Byte * 6
class BDA_IPv6_ADDRESS_LIST(Structure):
    ulcAddresses: UInt32
    rgAddressl: win32more.Windows.Win32.Media.DirectShow.BDA_IPv6_ADDRESS * 1
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
BDA_MULTICAST_MODE = Int32
BDA_PROMISCUOUS_MULTICAST: win32more.Windows.Win32.Media.DirectShow.BDA_MULTICAST_MODE = 0
BDA_FILTERED_MULTICAST: win32more.Windows.Win32.Media.DirectShow.BDA_MULTICAST_MODE = 1
BDA_NO_MULTICAST: win32more.Windows.Win32.Media.DirectShow.BDA_MULTICAST_MODE = 2
class BDA_MUX_PIDLISTITEM(Structure):
    usPIDNumber: UInt16
    usProgramNumber: UInt16
    ePIDType: win32more.Windows.Win32.Media.DirectShow.MUX_PID_TYPE
    _pack_ = 2
class BDA_PID_MAP(Structure):
    MediaSampleContent: win32more.Windows.Win32.Media.DirectShow.MEDIA_SAMPLE_CONTENT
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
BDA_RANGE_NOT_SET: win32more.Windows.Win32.Media.DirectShow.BDA_Range = -1
BDA_RANGE_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.BDA_Range = 0
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
BDA_SIGNAL_UNAVAILABLE: win32more.Windows.Win32.Media.DirectShow.BDA_SIGNAL_STATE = 0
BDA_SIGNAL_INACTIVE: win32more.Windows.Win32.Media.DirectShow.BDA_SIGNAL_STATE = 1
BDA_SIGNAL_ACTIVE: win32more.Windows.Win32.Media.DirectShow.BDA_SIGNAL_STATE = 2
class BDA_SIGNAL_TIMEOUTS(Structure):
    ulCarrierTimeoutMs: UInt32
    ulScanningTimeoutMs: UInt32
    ulTuningTimeoutMs: UInt32
class BDA_STRING(Structure):
    lResult: Int32
    ulStringSize: UInt32
    argbString: Byte * 1
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
BinaryConvolutionCodeRate = Int32
BDA_BCC_RATE_NOT_SET: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = -1
BDA_BCC_RATE_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 0
BDA_BCC_RATE_1_2: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 1
BDA_BCC_RATE_2_3: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 2
BDA_BCC_RATE_3_4: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 3
BDA_BCC_RATE_3_5: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 4
BDA_BCC_RATE_4_5: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 5
BDA_BCC_RATE_5_6: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 6
BDA_BCC_RATE_5_11: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 7
BDA_BCC_RATE_7_8: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 8
BDA_BCC_RATE_1_4: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 9
BDA_BCC_RATE_1_3: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 10
BDA_BCC_RATE_2_5: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 11
BDA_BCC_RATE_6_7: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 12
BDA_BCC_RATE_8_9: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 13
BDA_BCC_RATE_9_10: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 14
BDA_BCC_RATE_MAX: win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate = 15
class COLORKEY(Structure):
    KeyType: UInt32
    PaletteIndex: UInt32
    LowColorValue: win32more.Windows.Win32.Foundation.COLORREF
    HighColorValue: win32more.Windows.Win32.Foundation.COLORREF
COLORKEY_TYPE = Int32
CK_NOCOLORKEY: win32more.Windows.Win32.Media.DirectShow.COLORKEY_TYPE = 0
CK_INDEX: win32more.Windows.Win32.Media.DirectShow.COLORKEY_TYPE = 1
CK_RGB: win32more.Windows.Win32.Media.DirectShow.COLORKEY_TYPE = 2
COMPLETION_STATUS_FLAGS = Int32
COMPSTAT_NOUPDATEOK: win32more.Windows.Win32.Media.DirectShow.COMPLETION_STATUS_FLAGS = 1
COMPSTAT_WAIT: win32more.Windows.Win32.Media.DirectShow.COMPLETION_STATUS_FLAGS = 2
COMPSTAT_ABORT: win32more.Windows.Win32.Media.DirectShow.COMPLETION_STATUS_FLAGS = 4
COPP_ACP_Protection_Level = Int32
COPP_ACP_Level0: win32more.Windows.Win32.Media.DirectShow.COPP_ACP_Protection_Level = 0
COPP_ACP_LevelMin: win32more.Windows.Win32.Media.DirectShow.COPP_ACP_Protection_Level = 0
COPP_ACP_Level1: win32more.Windows.Win32.Media.DirectShow.COPP_ACP_Protection_Level = 1
COPP_ACP_Level2: win32more.Windows.Win32.Media.DirectShow.COPP_ACP_Protection_Level = 2
COPP_ACP_Level3: win32more.Windows.Win32.Media.DirectShow.COPP_ACP_Protection_Level = 3
COPP_ACP_LevelMax: win32more.Windows.Win32.Media.DirectShow.COPP_ACP_Protection_Level = 3
COPP_ACP_ForceDWORD: win32more.Windows.Win32.Media.DirectShow.COPP_ACP_Protection_Level = 2147483647
COPP_BusType = Int32
COPP_BusType_Unknown: win32more.Windows.Win32.Media.DirectShow.COPP_BusType = 0
COPP_BusType_PCI: win32more.Windows.Win32.Media.DirectShow.COPP_BusType = 1
COPP_BusType_PCIX: win32more.Windows.Win32.Media.DirectShow.COPP_BusType = 2
COPP_BusType_PCIExpress: win32more.Windows.Win32.Media.DirectShow.COPP_BusType = 3
COPP_BusType_AGP: win32more.Windows.Win32.Media.DirectShow.COPP_BusType = 4
COPP_BusType_Integrated: win32more.Windows.Win32.Media.DirectShow.COPP_BusType = -2147483648
COPP_BusType_ForceDWORD: win32more.Windows.Win32.Media.DirectShow.COPP_BusType = 2147483647
COPP_CGMSA_Protection_Level = Int32
COPP_CGMSA_Disabled: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 0
COPP_CGMSA_LevelMin: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 0
COPP_CGMSA_CopyFreely: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 1
COPP_CGMSA_CopyNoMore: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 2
COPP_CGMSA_CopyOneGeneration: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 3
COPP_CGMSA_CopyNever: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 4
COPP_CGMSA_RedistributionControlRequired: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 8
COPP_CGMSA_LevelMax: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 12
COPP_CGMSA_ForceDWORD: win32more.Windows.Win32.Media.DirectShow.COPP_CGMSA_Protection_Level = 2147483647
COPP_ConnectorType = Int32
COPP_ConnectorType_Unknown: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = -1
COPP_ConnectorType_VGA: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 0
COPP_ConnectorType_SVideo: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 1
COPP_ConnectorType_CompositeVideo: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 2
COPP_ConnectorType_ComponentVideo: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 3
COPP_ConnectorType_DVI: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 4
COPP_ConnectorType_HDMI: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 5
COPP_ConnectorType_LVDS: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 6
COPP_ConnectorType_TMDS: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 7
COPP_ConnectorType_D_JPN: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 8
COPP_ConnectorType_Internal: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = -2147483648
COPP_ConnectorType_ForceDWORD: win32more.Windows.Win32.Media.DirectShow.COPP_ConnectorType = 2147483647
COPP_HDCP_Protection_Level = Int32
COPP_HDCP_Level0: win32more.Windows.Win32.Media.DirectShow.COPP_HDCP_Protection_Level = 0
COPP_HDCP_LevelMin: win32more.Windows.Win32.Media.DirectShow.COPP_HDCP_Protection_Level = 0
COPP_HDCP_Level1: win32more.Windows.Win32.Media.DirectShow.COPP_HDCP_Protection_Level = 1
COPP_HDCP_LevelMax: win32more.Windows.Win32.Media.DirectShow.COPP_HDCP_Protection_Level = 1
COPP_HDCP_ForceDWORD: win32more.Windows.Win32.Media.DirectShow.COPP_HDCP_Protection_Level = 2147483647
COPP_ImageAspectRatio_EN300294 = Int32
COPP_AspectRatio_EN300294_FullFormat4by3: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 0
COPP_AspectRatio_EN300294_Box14by9Center: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 1
COPP_AspectRatio_EN300294_Box14by9Top: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 2
COPP_AspectRatio_EN300294_Box16by9Center: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 3
COPP_AspectRatio_EN300294_Box16by9Top: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 4
COPP_AspectRatio_EN300294_BoxGT16by9Center: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 5
COPP_AspectRatio_EN300294_FullFormat4by3ProtectedCenter: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 6
COPP_AspectRatio_EN300294_FullFormat16by9Anamorphic: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 7
COPP_AspectRatio_ForceDWORD: win32more.Windows.Win32.Media.DirectShow.COPP_ImageAspectRatio_EN300294 = 2147483647
COPP_StatusFlags = Int32
COPP_StatusNormal: win32more.Windows.Win32.Media.DirectShow.COPP_StatusFlags = 0
COPP_LinkLost: win32more.Windows.Win32.Media.DirectShow.COPP_StatusFlags = 1
COPP_RenegotiationRequired: win32more.Windows.Win32.Media.DirectShow.COPP_StatusFlags = 2
COPP_StatusFlagsReserved: win32more.Windows.Win32.Media.DirectShow.COPP_StatusFlags = -4
COPP_StatusHDCPFlags = Int32
COPP_HDCPRepeater: win32more.Windows.Win32.Media.DirectShow.COPP_StatusHDCPFlags = 1
COPP_HDCPFlagsReserved: win32more.Windows.Win32.Media.DirectShow.COPP_StatusHDCPFlags = -2
COPP_TVProtectionStandard = Int32
COPP_ProtectionStandard_Unknown: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = -2147483648
COPP_ProtectionStandard_None: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 0
COPP_ProtectionStandard_IEC61880_525i: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 1
COPP_ProtectionStandard_IEC61880_2_525i: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 2
COPP_ProtectionStandard_IEC62375_625p: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 4
COPP_ProtectionStandard_EIA608B_525: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 8
COPP_ProtectionStandard_EN300294_625i: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 16
COPP_ProtectionStandard_CEA805A_TypeA_525p: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 32
COPP_ProtectionStandard_CEA805A_TypeA_750p: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 64
COPP_ProtectionStandard_CEA805A_TypeA_1125i: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 128
COPP_ProtectionStandard_CEA805A_TypeB_525p: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 256
COPP_ProtectionStandard_CEA805A_TypeB_750p: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 512
COPP_ProtectionStandard_CEA805A_TypeB_1125i: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 1024
COPP_ProtectionStandard_ARIBTRB15_525i: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 2048
COPP_ProtectionStandard_ARIBTRB15_525p: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 4096
COPP_ProtectionStandard_ARIBTRB15_750p: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 8192
COPP_ProtectionStandard_ARIBTRB15_1125i: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 16384
COPP_ProtectionStandard_Mask: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = -2147450881
COPP_ProtectionStandard_Reserved: win32more.Windows.Win32.Media.DirectShow.COPP_TVProtectionStandard = 2147450880
CameraControlFlags = Int32
CameraControl_Flags_Auto: win32more.Windows.Win32.Media.DirectShow.CameraControlFlags = 1
CameraControl_Flags_Manual: win32more.Windows.Win32.Media.DirectShow.CameraControlFlags = 2
CameraControlProperty = Int32
CameraControl_Pan: win32more.Windows.Win32.Media.DirectShow.CameraControlProperty = 0
CameraControl_Tilt: win32more.Windows.Win32.Media.DirectShow.CameraControlProperty = 1
CameraControl_Roll: win32more.Windows.Win32.Media.DirectShow.CameraControlProperty = 2
CameraControl_Zoom: win32more.Windows.Win32.Media.DirectShow.CameraControlProperty = 3
CameraControl_Exposure: win32more.Windows.Win32.Media.DirectShow.CameraControlProperty = 4
CameraControl_Iris: win32more.Windows.Win32.Media.DirectShow.CameraControlProperty = 5
CameraControl_Focus: win32more.Windows.Win32.Media.DirectShow.CameraControlProperty = 6
ComponentCategory = Int32
CategoryNotSet: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = -1
CategoryOther: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 0
CategoryVideo: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 1
CategoryAudio: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 2
CategoryText: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 3
CategorySubtitles: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 4
CategoryCaptions: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 5
CategorySuperimpose: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 6
CategoryData: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 7
CATEGORY_COUNT: win32more.Windows.Win32.Media.DirectShow.ComponentCategory = 8
ComponentStatus = Int32
StatusActive: win32more.Windows.Win32.Media.DirectShow.ComponentStatus = 0
StatusInactive: win32more.Windows.Win32.Media.DirectShow.ComponentStatus = 1
StatusUnavailable: win32more.Windows.Win32.Media.DirectShow.ComponentStatus = 2
CompressionCaps = Int32
CompressionCaps_CanQuality: win32more.Windows.Win32.Media.DirectShow.CompressionCaps = 1
CompressionCaps_CanCrunch: win32more.Windows.Win32.Media.DirectShow.CompressionCaps = 2
CompressionCaps_CanKeyFrame: win32more.Windows.Win32.Media.DirectShow.CompressionCaps = 4
CompressionCaps_CanBFrame: win32more.Windows.Win32.Media.DirectShow.CompressionCaps = 8
CompressionCaps_CanWindow: win32more.Windows.Win32.Media.DirectShow.CompressionCaps = 16
DDSFF_FLAGS = Int32
DDSFF_PROGRESSIVERENDER: win32more.Windows.Win32.Media.DirectShow.DDSFF_FLAGS = 1
DECIMATION_USAGE = Int32
DECIMATION_LEGACY: win32more.Windows.Win32.Media.DirectShow.DECIMATION_USAGE = 0
DECIMATION_USE_DECODER_ONLY: win32more.Windows.Win32.Media.DirectShow.DECIMATION_USAGE = 1
DECIMATION_USE_VIDEOPORT_ONLY: win32more.Windows.Win32.Media.DirectShow.DECIMATION_USAGE = 2
DECIMATION_USE_OVERLAY_ONLY: win32more.Windows.Win32.Media.DirectShow.DECIMATION_USAGE = 3
DECIMATION_DEFAULT: win32more.Windows.Win32.Media.DirectShow.DECIMATION_USAGE = 4
DVBSystemType = Int32
DVB_Cable: win32more.Windows.Win32.Media.DirectShow.DVBSystemType = 0
DVB_Terrestrial: win32more.Windows.Win32.Media.DirectShow.DVBSystemType = 1
DVB_Satellite: win32more.Windows.Win32.Media.DirectShow.DVBSystemType = 2
ISDB_Terrestrial: win32more.Windows.Win32.Media.DirectShow.DVBSystemType = 3
ISDB_Satellite: win32more.Windows.Win32.Media.DirectShow.DVBSystemType = 4
class DVD_ATR(Structure):
    ulCAT: UInt32
    pbATRI: Byte * 768
DVD_AUDIO_APPMODE = Int32
DVD_AudioMode_None: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_APPMODE = 0
DVD_AudioMode_Karaoke: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_APPMODE = 1
DVD_AudioMode_Surround: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_APPMODE = 2
DVD_AudioMode_Other: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_APPMODE = 3
DVD_AUDIO_FORMAT = Int32
DVD_AudioFormat_AC3: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 0
DVD_AudioFormat_MPEG1: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 1
DVD_AudioFormat_MPEG1_DRC: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 2
DVD_AudioFormat_MPEG2: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 3
DVD_AudioFormat_MPEG2_DRC: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 4
DVD_AudioFormat_LPCM: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 5
DVD_AudioFormat_DTS: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 6
DVD_AudioFormat_SDDS: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 7
DVD_AudioFormat_Other: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT = 8
DVD_AUDIO_LANG_EXT = Int32
DVD_AUD_EXT_NotSpecified: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT = 0
DVD_AUD_EXT_Captions: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT = 1
DVD_AUD_EXT_VisuallyImpaired: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT = 2
DVD_AUD_EXT_DirectorComments1: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT = 3
DVD_AUD_EXT_DirectorComments2: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT = 4
class DVD_AudioAttributes(Structure):
    AppMode: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_APPMODE
    AppModeData: Byte
    AudioFormat: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_FORMAT
    Language: UInt32
    LanguageExtension: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT
    fHasMultichannelInfo: win32more.Windows.Win32.Foundation.BOOL
    dwFrequency: UInt32
    bQuantization: Byte
    bNumberOfChannels: Byte
    dwReserved: UInt32 * 2
DVD_CMD_FLAGS = Int32
DVD_CMD_FLAG_None: win32more.Windows.Win32.Media.DirectShow.DVD_CMD_FLAGS = 0
DVD_CMD_FLAG_Flush: win32more.Windows.Win32.Media.DirectShow.DVD_CMD_FLAGS = 1
DVD_CMD_FLAG_SendEvents: win32more.Windows.Win32.Media.DirectShow.DVD_CMD_FLAGS = 2
DVD_CMD_FLAG_Block: win32more.Windows.Win32.Media.DirectShow.DVD_CMD_FLAGS = 4
DVD_CMD_FLAG_StartWhenRendered: win32more.Windows.Win32.Media.DirectShow.DVD_CMD_FLAGS = 8
DVD_CMD_FLAG_EndAfterRendered: win32more.Windows.Win32.Media.DirectShow.DVD_CMD_FLAGS = 16
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
DVD_SIDE_A: win32more.Windows.Win32.Media.DirectShow.DVD_DISC_SIDE = 1
DVD_SIDE_B: win32more.Windows.Win32.Media.DirectShow.DVD_DISC_SIDE = 2
DVD_DOMAIN = Int32
DVD_DOMAIN_FirstPlay: win32more.Windows.Win32.Media.DirectShow.DVD_DOMAIN = 1
DVD_DOMAIN_VideoManagerMenu: win32more.Windows.Win32.Media.DirectShow.DVD_DOMAIN = 2
DVD_DOMAIN_VideoTitleSetMenu: win32more.Windows.Win32.Media.DirectShow.DVD_DOMAIN = 3
DVD_DOMAIN_Title: win32more.Windows.Win32.Media.DirectShow.DVD_DOMAIN = 4
DVD_DOMAIN_Stop: win32more.Windows.Win32.Media.DirectShow.DVD_DOMAIN = 5
DVD_ERROR = Int32
DVD_ERROR_Unexpected: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 1
DVD_ERROR_CopyProtectFail: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 2
DVD_ERROR_InvalidDVD1_0Disc: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 3
DVD_ERROR_InvalidDiscRegion: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 4
DVD_ERROR_LowParentalLevel: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 5
DVD_ERROR_MacrovisionFail: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 6
DVD_ERROR_IncompatibleSystemAndDecoderRegions: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 7
DVD_ERROR_IncompatibleDiscAndDecoderRegions: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 8
DVD_ERROR_CopyProtectOutputFail: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 9
DVD_ERROR_CopyProtectOutputNotSupported: win32more.Windows.Win32.Media.DirectShow.DVD_ERROR = 10
DVD_FRAMERATE = Int32
DVD_FPS_25: win32more.Windows.Win32.Media.DirectShow.DVD_FRAMERATE = 1
DVD_FPS_30NonDrop: win32more.Windows.Win32.Media.DirectShow.DVD_FRAMERATE = 3
class DVD_HMSF_TIMECODE(Structure):
    bHours: Byte
    bMinutes: Byte
    bSeconds: Byte
    bFrames: Byte
DVD_KARAOKE_ASSIGNMENT = Int32
DVD_Assignment_reserved0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 0
DVD_Assignment_reserved1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 1
DVD_Assignment_LR: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 2
DVD_Assignment_LRM: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 3
DVD_Assignment_LR1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 4
DVD_Assignment_LRM1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 5
DVD_Assignment_LR12: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 6
DVD_Assignment_LRM12: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT = 7
DVD_KARAOKE_CONTENTS = Int32
DVD_Karaoke_GuideVocal1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 1
DVD_Karaoke_GuideVocal2: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 2
DVD_Karaoke_GuideMelody1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 4
DVD_Karaoke_GuideMelody2: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 8
DVD_Karaoke_GuideMelodyA: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 16
DVD_Karaoke_GuideMelodyB: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 32
DVD_Karaoke_SoundEffectA: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 64
DVD_Karaoke_SoundEffectB: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_CONTENTS = 128
DVD_KARAOKE_DOWNMIX = Int32
DVD_Mix_0to0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 1
DVD_Mix_1to0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 2
DVD_Mix_2to0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 4
DVD_Mix_3to0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 8
DVD_Mix_4to0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 16
DVD_Mix_Lto0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 32
DVD_Mix_Rto0: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 64
DVD_Mix_0to1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 256
DVD_Mix_1to1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 512
DVD_Mix_2to1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 1024
DVD_Mix_3to1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 2048
DVD_Mix_4to1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 4096
DVD_Mix_Lto1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 8192
DVD_Mix_Rto1: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_DOWNMIX = 16384
class DVD_KaraokeAttributes(Structure):
    bVersion: Byte
    fMasterOfCeremoniesInGuideVocal1: win32more.Windows.Win32.Foundation.BOOL
    fDuet: win32more.Windows.Win32.Foundation.BOOL
    ChannelAssignment: win32more.Windows.Win32.Media.DirectShow.DVD_KARAOKE_ASSIGNMENT
    wChannelContents: UInt16 * 8
DVD_MENU_ID = Int32
DVD_MENU_Title: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID = 2
DVD_MENU_Root: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID = 3
DVD_MENU_Subpicture: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID = 4
DVD_MENU_Audio: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID = 5
DVD_MENU_Angle: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID = 6
DVD_MENU_Chapter: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID = 7
class DVD_MUA_Coeff(Structure):
    log2_alpha: Double
    log2_beta: Double
class DVD_MUA_MixingInfo(Structure):
    fMixTo0: win32more.Windows.Win32.Foundation.BOOL
    fMixTo1: win32more.Windows.Win32.Foundation.BOOL
    fMix0InPhase: win32more.Windows.Win32.Foundation.BOOL
    fMix1InPhase: win32more.Windows.Win32.Foundation.BOOL
    dwSpeakerPosition: UInt32
class DVD_MenuAttributes(Structure):
    fCompatibleRegion: win32more.Windows.Win32.Foundation.BOOL * 8
    VideoAttributes: win32more.Windows.Win32.Media.DirectShow.DVD_VideoAttributes
    fAudioPresent: win32more.Windows.Win32.Foundation.BOOL
    AudioAttributes: win32more.Windows.Win32.Media.DirectShow.DVD_AudioAttributes
    fSubpicturePresent: win32more.Windows.Win32.Foundation.BOOL
    SubpictureAttributes: win32more.Windows.Win32.Media.DirectShow.DVD_SubpictureAttributes
class DVD_MultichannelAudioAttributes(Structure):
    Info: win32more.Windows.Win32.Media.DirectShow.DVD_MUA_MixingInfo * 8
    Coeff: win32more.Windows.Win32.Media.DirectShow.DVD_MUA_Coeff * 8
DVD_NavCmdType = Int32
DVD_NavCmdType_Pre: win32more.Windows.Win32.Media.DirectShow.DVD_NavCmdType = 1
DVD_NavCmdType_Post: win32more.Windows.Win32.Media.DirectShow.DVD_NavCmdType = 2
DVD_NavCmdType_Cell: win32more.Windows.Win32.Media.DirectShow.DVD_NavCmdType = 3
DVD_NavCmdType_Button: win32more.Windows.Win32.Media.DirectShow.DVD_NavCmdType = 4
DVD_OPTION_FLAG = Int32
DVD_ResetOnStop: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 1
DVD_NotifyParentalLevelChange: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 2
DVD_HMSF_TimeCodeEvents: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 3
DVD_AudioDuringFFwdRew: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 4
DVD_EnableNonblockingAPIs: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 5
DVD_CacheSizeInMB: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 6
DVD_EnablePortableBookmarks: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 7
DVD_EnableExtendedCopyProtectErrors: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 8
DVD_NotifyPositionChange: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 9
DVD_IncreaseOutputControl: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 10
DVD_EnableStreaming: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 11
DVD_EnableESOutput: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 12
DVD_EnableTitleLength: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 13
DVD_DisableStillThrottle: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 14
DVD_EnableLoggingEvents: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 15
DVD_MaxReadBurstInKB: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 16
DVD_ReadBurstPeriodInMS: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 17
DVD_RestartDisc: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 18
DVD_EnableCC: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG = 19
DVD_PARENTAL_LEVEL = Int32
DVD_PARENTAL_LEVEL_8: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 32768
DVD_PARENTAL_LEVEL_7: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 16384
DVD_PARENTAL_LEVEL_6: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 8192
DVD_PARENTAL_LEVEL_5: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 4096
DVD_PARENTAL_LEVEL_4: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 2048
DVD_PARENTAL_LEVEL_3: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 1024
DVD_PARENTAL_LEVEL_2: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 512
DVD_PARENTAL_LEVEL_1: win32more.Windows.Win32.Media.DirectShow.DVD_PARENTAL_LEVEL = 256
DVD_PB_STOPPED = Int32
DVD_PB_STOPPED_Other: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 0
DVD_PB_STOPPED_NoBranch: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 1
DVD_PB_STOPPED_NoFirstPlayDomain: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 2
DVD_PB_STOPPED_StopCommand: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 3
DVD_PB_STOPPED_Reset: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 4
DVD_PB_STOPPED_DiscEjected: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 5
DVD_PB_STOPPED_IllegalNavCommand: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 6
DVD_PB_STOPPED_PlayPeriodAutoStop: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 7
DVD_PB_STOPPED_PlayChapterAutoStop: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 8
DVD_PB_STOPPED_ParentalFailure: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 9
DVD_PB_STOPPED_RegionFailure: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 10
DVD_PB_STOPPED_MacrovisionFailure: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 11
DVD_PB_STOPPED_DiscReadError: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 12
DVD_PB_STOPPED_CopyProtectFailure: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 13
DVD_PB_STOPPED_CopyProtectOutputFailure: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 14
DVD_PB_STOPPED_CopyProtectOutputNotSupported: win32more.Windows.Win32.Media.DirectShow.DVD_PB_STOPPED = 15
class DVD_PLAYBACK_LOCATION(Structure):
    TitleNum: UInt32
    ChapterNum: UInt32
    TimeCode: UInt32
class DVD_PLAYBACK_LOCATION2(Structure):
    TitleNum: UInt32
    ChapterNum: UInt32
    TimeCode: win32more.Windows.Win32.Media.DirectShow.DVD_HMSF_TIMECODE
    TimeCodeFlags: UInt32
DVD_PLAY_DIRECTION = Int32
DVD_DIR_FORWARD: win32more.Windows.Win32.Media.DirectShow.DVD_PLAY_DIRECTION = 0
DVD_DIR_BACKWARD: win32more.Windows.Win32.Media.DirectShow.DVD_PLAY_DIRECTION = 1
DVD_PREFERRED_DISPLAY_MODE = Int32
DISPLAY_CONTENT_DEFAULT: win32more.Windows.Win32.Media.DirectShow.DVD_PREFERRED_DISPLAY_MODE = 0
DISPLAY_16x9: win32more.Windows.Win32.Media.DirectShow.DVD_PREFERRED_DISPLAY_MODE = 1
DISPLAY_4x3_PANSCAN_PREFERRED: win32more.Windows.Win32.Media.DirectShow.DVD_PREFERRED_DISPLAY_MODE = 2
DISPLAY_4x3_LETTERBOX_PREFERRED: win32more.Windows.Win32.Media.DirectShow.DVD_PREFERRED_DISPLAY_MODE = 3
DVD_RELATIVE_BUTTON = Int32
DVD_Relative_Upper: win32more.Windows.Win32.Media.DirectShow.DVD_RELATIVE_BUTTON = 1
DVD_Relative_Lower: win32more.Windows.Win32.Media.DirectShow.DVD_RELATIVE_BUTTON = 2
DVD_Relative_Left: win32more.Windows.Win32.Media.DirectShow.DVD_RELATIVE_BUTTON = 3
DVD_Relative_Right: win32more.Windows.Win32.Media.DirectShow.DVD_RELATIVE_BUTTON = 4
DVD_SUBPICTURE_CODING = Int32
DVD_SPCoding_RunLength: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_CODING = 0
DVD_SPCoding_Extended: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_CODING = 1
DVD_SPCoding_Other: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_CODING = 2
DVD_SUBPICTURE_LANG_EXT = Int32
DVD_SP_EXT_NotSpecified: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 0
DVD_SP_EXT_Caption_Normal: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 1
DVD_SP_EXT_Caption_Big: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 2
DVD_SP_EXT_Caption_Children: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 3
DVD_SP_EXT_CC_Normal: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 5
DVD_SP_EXT_CC_Big: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 6
DVD_SP_EXT_CC_Children: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 7
DVD_SP_EXT_Forced: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 9
DVD_SP_EXT_DirectorComments_Normal: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 13
DVD_SP_EXT_DirectorComments_Big: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 14
DVD_SP_EXT_DirectorComments_Children: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT = 15
DVD_SUBPICTURE_TYPE = Int32
DVD_SPType_NotSpecified: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_TYPE = 0
DVD_SPType_Language: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_TYPE = 1
DVD_SPType_Other: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_TYPE = 2
class DVD_SubpictureAttributes(Structure):
    Type: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_TYPE
    CodingMode: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_CODING
    Language: UInt32
    LanguageExtension: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT
class DVD_TIMECODE(Structure):
    Hours1: Annotated[UInt32, 4]
    Hours10: Annotated[UInt32, 4]
    Minutes1: Annotated[UInt32, 4]
    Minutes10: Annotated[UInt32, 4]
    Seconds1: Annotated[UInt32, 4]
    Seconds10: Annotated[UInt32, 4]
    Frames1: Annotated[UInt32, 4]
    Frames10: Annotated[UInt32, 2]
    FrameRateCode: Annotated[UInt32, 2]
DVD_TIMECODE_FLAGS = Int32
DVD_TC_FLAG_25fps: win32more.Windows.Win32.Media.DirectShow.DVD_TIMECODE_FLAGS = 1
DVD_TC_FLAG_30fps: win32more.Windows.Win32.Media.DirectShow.DVD_TIMECODE_FLAGS = 2
DVD_TC_FLAG_DropFrame: win32more.Windows.Win32.Media.DirectShow.DVD_TIMECODE_FLAGS = 4
DVD_TC_FLAG_Interpolated: win32more.Windows.Win32.Media.DirectShow.DVD_TIMECODE_FLAGS = 8
DVD_TITLE_APPMODE = Int32
DVD_AppMode_Not_Specified: win32more.Windows.Win32.Media.DirectShow.DVD_TITLE_APPMODE = 0
DVD_AppMode_Karaoke: win32more.Windows.Win32.Media.DirectShow.DVD_TITLE_APPMODE = 1
DVD_AppMode_Other: win32more.Windows.Win32.Media.DirectShow.DVD_TITLE_APPMODE = 3
DVD_TextCharSet = Int32
DVD_CharSet_Unicode: win32more.Windows.Win32.Media.DirectShow.DVD_TextCharSet = 0
DVD_CharSet_ISO646: win32more.Windows.Win32.Media.DirectShow.DVD_TextCharSet = 1
DVD_CharSet_JIS_Roman_Kanji: win32more.Windows.Win32.Media.DirectShow.DVD_TextCharSet = 2
DVD_CharSet_ISO8859_1: win32more.Windows.Win32.Media.DirectShow.DVD_TextCharSet = 3
DVD_CharSet_ShiftJIS_Kanji_Roman_Katakana: win32more.Windows.Win32.Media.DirectShow.DVD_TextCharSet = 4
DVD_TextStringType = Int32
DVD_Struct_Volume: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 1
DVD_Struct_Title: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 2
DVD_Struct_ParentalID: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 3
DVD_Struct_PartOfTitle: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 4
DVD_Struct_Cell: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 5
DVD_Stream_Audio: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 16
DVD_Stream_Subpicture: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 17
DVD_Stream_Angle: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 18
DVD_Channel_Audio: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 32
DVD_General_Name: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 48
DVD_General_Comments: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 49
DVD_Title_Series: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 56
DVD_Title_Movie: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 57
DVD_Title_Video: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 58
DVD_Title_Album: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 59
DVD_Title_Song: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 60
DVD_Title_Other: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 63
DVD_Title_Sub_Series: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 64
DVD_Title_Sub_Movie: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 65
DVD_Title_Sub_Video: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 66
DVD_Title_Sub_Album: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 67
DVD_Title_Sub_Song: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 68
DVD_Title_Sub_Other: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 71
DVD_Title_Orig_Series: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 72
DVD_Title_Orig_Movie: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 73
DVD_Title_Orig_Video: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 74
DVD_Title_Orig_Album: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 75
DVD_Title_Orig_Song: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 76
DVD_Title_Orig_Other: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 79
DVD_Other_Scene: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 80
DVD_Other_Cut: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 81
DVD_Other_Take: win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType = 82
class DVD_TitleAttributes(Structure):
    Anonymous: _Anonymous_e__Union
    VideoAttributes: win32more.Windows.Win32.Media.DirectShow.DVD_VideoAttributes
    ulNumberOfAudioStreams: UInt32
    AudioAttributes: win32more.Windows.Win32.Media.DirectShow.DVD_AudioAttributes * 8
    MultichannelAudioAttributes: win32more.Windows.Win32.Media.DirectShow.DVD_MultichannelAudioAttributes * 8
    ulNumberOfSubpictureStreams: UInt32
    SubpictureAttributes: win32more.Windows.Win32.Media.DirectShow.DVD_SubpictureAttributes * 32
    class _Anonymous_e__Union(Union):
        AppMode: win32more.Windows.Win32.Media.DirectShow.DVD_TITLE_APPMODE
        TitleLength: win32more.Windows.Win32.Media.DirectShow.DVD_HMSF_TIMECODE
DVD_VIDEO_COMPRESSION = Int32
DVD_VideoCompression_Other: win32more.Windows.Win32.Media.DirectShow.DVD_VIDEO_COMPRESSION = 0
DVD_VideoCompression_MPEG1: win32more.Windows.Win32.Media.DirectShow.DVD_VIDEO_COMPRESSION = 1
DVD_VideoCompression_MPEG2: win32more.Windows.Win32.Media.DirectShow.DVD_VIDEO_COMPRESSION = 2
class DVD_VideoAttributes(Structure):
    fPanscanPermitted: win32more.Windows.Win32.Foundation.BOOL
    fLetterboxPermitted: win32more.Windows.Win32.Foundation.BOOL
    ulAspectX: UInt32
    ulAspectY: UInt32
    ulFrameRate: UInt32
    ulFrameHeight: UInt32
    Compression: win32more.Windows.Win32.Media.DirectShow.DVD_VIDEO_COMPRESSION
    fLine21Field1InGOP: win32more.Windows.Win32.Foundation.BOOL
    fLine21Field2InGOP: win32more.Windows.Win32.Foundation.BOOL
    ulSourceResolutionX: UInt32
    ulSourceResolutionY: UInt32
    fIsSourceLetterboxed: win32more.Windows.Win32.Foundation.BOOL
    fIsFilmMode: win32more.Windows.Win32.Foundation.BOOL
DVD_WARNING = Int32
DVD_WARNING_InvalidDVD1_0Disc: win32more.Windows.Win32.Media.DirectShow.DVD_WARNING = 1
DVD_WARNING_FormatNotSupported: win32more.Windows.Win32.Media.DirectShow.DVD_WARNING = 2
DVD_WARNING_IllegalNavCommand: win32more.Windows.Win32.Media.DirectShow.DVD_WARNING = 3
DVD_WARNING_Open: win32more.Windows.Win32.Media.DirectShow.DVD_WARNING = 4
DVD_WARNING_Seek: win32more.Windows.Win32.Media.DirectShow.DVD_WARNING = 5
DVD_WARNING_Read: win32more.Windows.Win32.Media.DirectShow.DVD_WARNING = 6
class DVINFO(Structure):
    dwDVAAuxSrc: UInt32
    dwDVAAuxCtl: UInt32
    dwDVAAuxSrc1: UInt32
    dwDVAAuxCtl1: UInt32
    dwDVVAuxSrc: UInt32
    dwDVVAuxCtl: UInt32
    dwDVReserved: UInt32 * 2
class DXVA2SW_CALLBACKS(Structure):
    Size: UInt32
    GetVideoProcessorRenderTargetCount: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETCOUNT
    GetVideoProcessorRenderTargets: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETS
    GetVideoProcessorCaps: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORCAPS
    GetVideoProcessorSubStreamFormatCount: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATCOUNT
    GetVideoProcessorSubStreamFormats: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATS
    GetProcAmpRange: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_GETPROCAMPRANGE
    GetFilterPropertyRange: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_GETFILTERPROPERTYRANGE
    CreateVideoProcessDevice: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_CREATEVIDEOPROCESSDEVICE
    DestroyVideoProcessDevice: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_DESTROYVIDEOPROCESSDEVICE
    VideoProcessBeginFrame: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_VIDEOPROCESSBEGINFRAME
    VideoProcessEndFrame: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_VIDEOPROCESSENDFRAME
    VideoProcessSetRenderTarget: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_VIDEOPROCESSSETRENDERTARGET
    VideoProcessBlt: win32more.Windows.Win32.Media.DirectShow.PDXVA2SW_VIDEOPROCESSBLT
class DXVA2TraceVideoProcessBltData(Structure):
    wmiHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pRenderTarget: UInt64
    TargetFrameTime: UInt64
    TargetRect: win32more.Windows.Win32.Foundation.RECT
    Enter: win32more.Windows.Win32.Foundation.BOOL
class DXVA2Trace_DecodeDevBeginFrameData(Structure):
    wmiHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pRenderTarget: UInt64
    Enter: win32more.Windows.Win32.Foundation.BOOL
class DXVA2Trace_DecodeDevCreatedData(Structure):
    wmiHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pD3DDevice: UInt64
    DeviceGuid: Guid
    Width: UInt32
    Height: UInt32
    Enter: win32more.Windows.Win32.Foundation.BOOL
class DXVA2Trace_DecodeDevGetBufferData(Structure):
    wmiHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    BufferType: UInt32
    Enter: win32more.Windows.Win32.Foundation.BOOL
class DXVA2Trace_DecodeDeviceData(Structure):
    wmiHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    Enter: win32more.Windows.Win32.Foundation.BOOL
class DXVA2Trace_VideoProcessDevCreatedData(Structure):
    wmiHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    pD3DDevice: UInt64
    DeviceGuid: Guid
    RTFourCC: UInt32
    Width: UInt32
    Height: UInt32
    Enter: win32more.Windows.Win32.Foundation.BOOL
class DXVA2Trace_VideoProcessDeviceData(Structure):
    wmiHeader: win32more.Windows.Win32.System.Diagnostics.Etw.EVENT_TRACE_HEADER
    pObject: UInt64
    Enter: win32more.Windows.Win32.Foundation.BOOL
DXVA2_DestinationFlags = Int32
DXVA2_DestinationFlag_Background_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = 1
DXVA2_DestinationFlag_TargetRect_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = 2
DXVA2_DestinationFlag_ColorData_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = 4
DXVA2_DestinationFlag_Alpha_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = 8
DXVA2_DestinationFlag_RFF: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = 65536
DXVA2_DestinationFlag_TFF: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = 131072
DXVA2_DestinationFlag_RFF_TFF_Present: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = 262144
DXVA2_DestinationFlagMask: win32more.Windows.Win32.Media.DirectShow.DXVA2_DestinationFlags = -65521
DXVA2_SampleFlags = Int32
DXVA2_SampleFlag_Palette_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 1
DXVA2_SampleFlag_SrcRect_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 2
DXVA2_SampleFlag_DstRect_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 4
DXVA2_SampleFlag_ColorData_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 8
DXVA2_SampleFlag_PlanarAlpha_Changed: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 16
DXVA2_SampleFlag_RFF: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 65536
DXVA2_SampleFlag_TFF: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 131072
DXVA2_SampleFlag_RFF_TFF_Present: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = 262144
DXVA2_SampleFlagsMask: win32more.Windows.Win32.Media.DirectShow.DXVA2_SampleFlags = -65505
class DXVA2_VIDEOPROCESSBLT(Structure):
    TargetFrame: Int64
    TargetRect: win32more.Windows.Win32.Foundation.RECT
    ConstrictionSize: win32more.Windows.Win32.Foundation.SIZE
    StreamingFlags: UInt32
    BackgroundColor: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_AYUVSample16
    DestFormat: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_ExtendedFormat
    DestFlags: UInt32
    ProcAmpValues: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_ProcAmpValues
    Alpha: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    NoiseFilterLuma: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    NoiseFilterChroma: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    DetailFilterLuma: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    DetailFilterChroma: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    pSrcSurfaces: POINTER(win32more.Windows.Win32.Media.DirectShow.DXVA2_VIDEOSAMPLE)
    NumSrcSurfaces: UInt32
class DXVA2_VIDEOSAMPLE(Structure):
    Start: Int64
    End: Int64
    SampleFormat: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_ExtendedFormat
    SampleFlags: UInt32
    SrcResource: VoidPtr
    SrcRect: win32more.Windows.Win32.Foundation.RECT
    DstRect: win32more.Windows.Win32.Foundation.RECT
    Pal: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_AYUVSample8 * 16
    PlanarAlpha: win32more.Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
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
class EALocationCodeType(Structure):
    LocationCodeScheme: win32more.Windows.Win32.Media.DirectShow.LocationCodeSchemeType
    state_code: Byte
    county_subdivision: Byte
    county_code: UInt16
EntitlementType = Int32
Entitled: win32more.Windows.Win32.Media.DirectShow.EntitlementType = 0
NotEntitled: win32more.Windows.Win32.Media.DirectShow.EntitlementType = 1
TechnicalFailure: win32more.Windows.Win32.Media.DirectShow.EntitlementType = 2
FECMethod = Int32
BDA_FEC_METHOD_NOT_SET: win32more.Windows.Win32.Media.DirectShow.FECMethod = -1
BDA_FEC_METHOD_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.FECMethod = 0
BDA_FEC_VITERBI: win32more.Windows.Win32.Media.DirectShow.FECMethod = 1
BDA_FEC_RS_204_188: win32more.Windows.Win32.Media.DirectShow.FECMethod = 2
BDA_FEC_LDPC: win32more.Windows.Win32.Media.DirectShow.FECMethod = 3
BDA_FEC_BCH: win32more.Windows.Win32.Media.DirectShow.FECMethod = 4
BDA_FEC_RS_147_130: win32more.Windows.Win32.Media.DirectShow.FECMethod = 5
BDA_FEC_MAX: win32more.Windows.Win32.Media.DirectShow.FECMethod = 6
class FILTER_INFO(Structure):
    achName: Char * 128
    pGraph: win32more.Windows.Win32.Media.DirectShow.IFilterGraph
FILTER_STATE = Int32
State_Stopped: win32more.Windows.Win32.Media.DirectShow.FILTER_STATE = 0
State_Paused: win32more.Windows.Win32.Media.DirectShow.FILTER_STATE = 1
State_Running: win32more.Windows.Win32.Media.DirectShow.FILTER_STATE = 2
FilgraphManager = Guid('{e436ebb3-524f-11ce-9f53-0020af0ba770}')
GuardInterval = Int32
BDA_GUARD_NOT_SET: win32more.Windows.Win32.Media.DirectShow.GuardInterval = -1
BDA_GUARD_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 0
BDA_GUARD_1_32: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 1
BDA_GUARD_1_16: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 2
BDA_GUARD_1_8: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 3
BDA_GUARD_1_4: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 4
BDA_GUARD_1_128: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 5
BDA_GUARD_19_128: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 6
BDA_GUARD_19_256: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 7
BDA_GUARD_MAX: win32more.Windows.Win32.Media.DirectShow.GuardInterval = 8
class HEAACWAVEFORMAT(Structure):
    wfInfo: win32more.Windows.Win32.Media.DirectShow.HEAACWAVEINFO
    pbAudioSpecificConfig: Byte * 1
class HEAACWAVEINFO(Structure):
    wfx: win32more.Windows.Win32.Media.Audio.WAVEFORMATEX
    wPayloadType: UInt16
    wAudioProfileLevelIndication: UInt16
    wStructType: UInt16
    wReserved1: UInt16
    dwReserved2: UInt32
    _pack_ = 1
HierarchyAlpha = Int32
BDA_HALPHA_NOT_SET: win32more.Windows.Win32.Media.DirectShow.HierarchyAlpha = -1
BDA_HALPHA_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.HierarchyAlpha = 0
BDA_HALPHA_1: win32more.Windows.Win32.Media.DirectShow.HierarchyAlpha = 1
BDA_HALPHA_2: win32more.Windows.Win32.Media.DirectShow.HierarchyAlpha = 2
BDA_HALPHA_4: win32more.Windows.Win32.Media.DirectShow.HierarchyAlpha = 3
BDA_HALPHA_MAX: win32more.Windows.Win32.Media.DirectShow.HierarchyAlpha = 4
class IAMAnalogVideoDecoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e13350-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def get_AvailableTVFormats(self, lAnalogVideoStandard: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_TVFormat(self, lAnalogVideoStandard: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_TVFormat(self, plAnalogVideoStandard: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_HorizontalLocked(self, plLocked: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_VCRHorizontalLocking(self, lVCRHorizontalLocking: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_VCRHorizontalLocking(self, plVCRHorizontalLocking: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NumberOfLines(self, plNumberOfLines: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_OutputEnable(self, lOutputEnable: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_OutputEnable(self, plOutputEnable: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMAnalogVideoEncoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e133b0-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def get_AvailableTVFormats(self, lAnalogVideoStandard: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_TVFormat(self, lAnalogVideoStandard: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_TVFormat(self, plAnalogVideoStandard: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_CopyProtection(self, lVideoCopyProtection: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CopyProtection(self, lVideoCopyProtection: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_CCEnable(self, lCCEnable: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CCEnable(self, lCCEnable: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMAsyncReaderTimestampScaling(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf7b26fc-9a00-485b-8147-3e789d5e8f67}')
    @commethod(3)
    def GetTimestampMode(self, pfRaw: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTimestampMode(self, fRaw: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMAudioInputMixer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54c39221-8380-11d0-b3f0-00aa003761c5}')
    @commethod(3)
    def put_Enable(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Enable(self, pfEnable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_Mono(self, fMono: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Mono(self, pfMono: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_MixLevel(self, Level: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_MixLevel(self, pLevel: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Pan(self, Pan: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Pan(self, pPan: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Loudness(self, fLoudness: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Loudness(self, pfLoudness: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Treble(self, Treble: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Treble(self, pTreble: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_TrebleRange(self, pRange: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Bass(self, Bass: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Bass(self, pBass: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_BassRange(self, pRange: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMAudioRendererStats(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22320cb2-d41a-11d2-bf7c-d7cb9df0bf93}')
    @commethod(3)
    def GetStatParam(self, dwParam: UInt32, pdwParam1: POINTER(UInt32), pdwParam2: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMBufferNegotiation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56ed71a0-af5f-11d0-b3f0-00aa003761c5}')
    @commethod(3)
    def SuggestAllocatorProperties(self, pprop: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllocatorProperties(self, pprop: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMCameraControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e13370-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def GetRange(self, Property: Int32, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Set(self, Property: Int32, lValue: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Get(self, Property: Int32, lValue: POINTER(Int32), Flags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMCertifiedOutputProtection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6feded3e-0ff1-4901-a2f1-43f7012c8515}')
    @commethod(3)
    def KeyExchange(self, pRandom: POINTER(Guid), VarLenCertGH: POINTER(POINTER(Byte)), pdwLengthCertGH: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SessionSequenceStart(self, pSig: POINTER(win32more.Windows.Win32.Media.DirectShow.AMCOPPSignature)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ProtectionCommand(self, cmd: POINTER(win32more.Windows.Win32.Media.DirectShow.AMCOPPCommand)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProtectionStatus(self, pStatusInput: POINTER(win32more.Windows.Win32.Media.DirectShow.AMCOPPStatusInput), pStatusOutput: POINTER(win32more.Windows.Win32.Media.DirectShow.AMCOPPStatusOutput)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMChannelInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa2aa8f2-8b62-11d0-a520-000000000000}')
    @commethod(7)
    def get_ChannelName(self, pbstrChannelName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ChannelDescription(self, pbstrChannelDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ChannelURL(self, pbstrChannelURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ContactAddress(self, pbstrContactAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ContactPhone(self, pbstrContactPhone: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ContactEmail(self, pbstrContactEmail: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMClockAdjust(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4d5466b0-a49c-11d1-abe8-00a0c905f375}')
    @commethod(3)
    def SetClockDelta(self, rtDelta: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMClockSlave(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9fd52741-176d-4b36-8f51-ca8f933223be}')
    @commethod(3)
    def SetErrorTolerance(self, dwTolerance: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorTolerance(self, pdwTolerance: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868b9-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, lItem: Int32, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMCopyCaptureFileProgress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{670d1d20-a068-11d0-b3f0-00aa003761c5}')
    @commethod(3)
    def Progress(self, iProgress: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMCrossbar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e13380-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def get_PinCounts(self, OutputPinCount: POINTER(Int32), InputPinCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CanRoute(self, OutputPinIndex: Int32, InputPinIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Route(self, OutputPinIndex: Int32, InputPinIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_IsRoutedTo(self, OutputPinIndex: Int32, InputPinIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CrossbarPinInfo(self, IsInputPin: win32more.Windows.Win32.Foundation.BOOL, PinIndex: Int32, PinIndexRelated: POINTER(Int32), PhysicalType: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMDecoderCaps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0dff467-d499-4986-972b-e1d9090fa941}')
    @commethod(3)
    def GetDecoderCaps(self, dwCapIndex: UInt32, lpdwCap: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMDevMemoryAllocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6545bf0-e76b-11d0-bd52-00a0c911ce86}')
    @commethod(3)
    def GetInfo(self, pdwcbTotalFree: POINTER(UInt32), pdwcbLargestFree: POINTER(UInt32), pdwcbTotalMemory: POINTER(UInt32), pdwcbMinimumChunk: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CheckMemory(self, pBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Alloc(self, ppBuffer: POINTER(POINTER(Byte)), pdwcbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Free(self, pBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevMemoryObject(self, ppUnkInnner: POINTER(win32more.Windows.Win32.System.Com.IUnknown), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMDevMemoryControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6545bf1-e76b-11d0-bd52-00a0c911ce86}')
    @commethod(3)
    def QueryWriteSync(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteSync(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDevId(self, pdwDevId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMDeviceRemoval(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f90a6130-b658-11d2-ae49-0000f8754b99}')
    @commethod(3)
    def DeviceInfo(self, pclsidInterfaceClass: POINTER(Guid), pwszSymbolicLink: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reassociate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disassociate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMDirectSound(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{546f4260-d53e-11cf-b3f0-00aa003761c5}')
    @commethod(3)
    def GetDirectSoundInterface(self, lplpds: POINTER(win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSound)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrimaryBufferInterface(self, lplpdsb: POINTER(win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSecondaryBufferInterface(self, lplpdsb: POINTER(win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseDirectSoundInterface(self, lpds: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSound) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReleasePrimaryBufferInterface(self, lpdsb: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReleaseSecondaryBufferInterface(self, lpdsb: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetFocusWindow(self, param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFocusWindow(self, param0: POINTER(win32more.Windows.Win32.Foundation.HWND), param1: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMDroppedFrames(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e13344-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def GetNumDropped(self, plDropped: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumNotDropped(self, plNotDropped: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDroppedInfo(self, lSize: Int32, plArray: POINTER(Int32), plNumCopied: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAverageFrameSize(self, plAverageSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMExtDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b5730a90-1a2c-11cf-8c23-00aa006b6814}')
    @commethod(3)
    def GetCapability(self, Capability: Int32, pValue: POINTER(Int32), pdblValue: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ExternalDeviceID(self, ppszData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_ExternalDeviceVersion(self, ppszData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_DevicePower(self, PowerMode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_DevicePower(self, pPowerMode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Calibrate(self, hEvent: UIntPtr, Mode: Int32, pStatus: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_DevicePort(self, DevicePort: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DevicePort(self, pDevicePort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMExtTransport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a03cd5f0-3045-11cf-8c44-00aa006b6814}')
    @commethod(3)
    def GetCapability(self, Capability: Int32, pValue: POINTER(Int32), pdblValue: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_MediaState(self, State: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_MediaState(self, pState: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_LocalControl(self, State: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_LocalControl(self, pState: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStatus(self, StatusItem: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransportBasicParameters(self, Param: Int32, pValue: POINTER(Int32), ppszData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTransportBasicParameters(self, Param: Int32, Value: Int32, pszData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTransportVideoParameters(self, Param: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTransportVideoParameters(self, Param: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTransportAudioParameters(self, Param: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetTransportAudioParameters(self, Param: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Mode(self, Mode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Mode(self, pMode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Rate(self, dblRate: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Rate(self, pdblRate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetChase(self, pEnabled: POINTER(Int32), pOffset: POINTER(Int32), phEvent: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetChase(self, Enable: Int32, Offset: Int32, hEvent: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetBump(self, pSpeed: POINTER(Int32), pDuration: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetBump(self, Speed: Int32, Duration: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_AntiClogControl(self, pEnabled: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AntiClogControl(self, Enable: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetEditPropertySet(self, EditID: Int32, pState: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetEditPropertySet(self, pEditID: POINTER(Int32), State: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetEditProperty(self, EditID: Int32, Param: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetEditProperty(self, EditID: Int32, Param: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_EditStart(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_EditStart(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMExtendedErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa2aa8f6-8b62-11d0-a520-000000000000}')
    @commethod(7)
    def get_HasError(self, pHasError: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ErrorDescription(self, pbstrErrorDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ErrorCode(self, pErrorCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMExtendedSeeking(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa2aa8f9-8b62-11d0-a520-000000000000}')
    @commethod(7)
    def get_ExSeekCapabilities(self, pExCapabilities: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_MarkerCount(self, pMarkerCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentMarker(self, pCurrentMarker: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMarkerTime(self, MarkerNum: Int32, pMarkerTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMarkerName(self, MarkerNum: Int32, pbstrMarkerName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PlaybackSpeed(self, Speed: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PlaybackSpeed(self, pSpeed: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMFilterGraphCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868fd-0ad4-11ce-b0a3-0020af0ba770}')
    @commethod(3)
    def UnableToRender(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMFilterMiscFlags(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2dd74950-a890-11d1-abe8-00a0c905f375}')
    @commethod(3)
    def GetMiscFlags(self) -> UInt32: ...
class IAMGraphBuilderCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4995f511-9ddb-4f12-bd3b-f04611807b79}')
    @commethod(3)
    def SelectedFilter(self, pMon: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatedFilter(self, pFil: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMGraphStreams(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{632105fa-072e-11d3-8af9-00c04fb6bd3d}')
    @commethod(3)
    def FindUpstreamInterface(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, riid: POINTER(Guid), ppvInterface: POINTER(VoidPtr), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SyncUsingStreamOffset(self, bUseStreamOffset: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxGraphLatency(self, rtMaxGraphLatency: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMLatency(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{62ea93ba-ec62-11d2-b770-00c04fb6bd3d}')
    @commethod(3)
    def GetLatency(self, prtLatency: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMLine21Decoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e8d4a21-310c-11d0-b79a-00aa003767a7}')
    @commethod(3)
    def GetDecoderLevel(self, lpLevel: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCLEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentService(self, lpService: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCurrentService(self, Service: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSERVICE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceState(self, lpState: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetServiceState(self, State: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_CCSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputFormat(self, lpbmih: POINTER(win32more.Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputFormat(self, lpbmi: POINTER(win32more.Windows.Win32.Graphics.Gdi.BITMAPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackgroundColor(self, pdwPhysColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetBackgroundColor(self, dwPhysColor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRedrawAlways(self, lpbOption: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetRedrawAlways(self, bOption: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDrawBackgroundMode(self, lpMode: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_LINE21_DRAWBGMODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetDrawBackgroundMode(self, Mode: win32more.Windows.Win32.Media.DirectShow.AM_LINE21_DRAWBGMODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMMediaContent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa2aa8f4-8b62-11d0-a520-000000000000}')
    @commethod(7)
    def get_AuthorName(self, pbstrAuthorName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Title(self, pbstrTitle: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Rating(self, pbstrRating: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Copyright(self, pbstrCopyright: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_BaseURL(self, pbstrBaseURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_LogoURL(self, pbstrLogoURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_LogoIconURL(self, pbstrLogoURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_WatermarkURL(self, pbstrWatermarkURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_MoreInfoURL(self, pbstrMoreInfoURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MoreInfoBannerImage(self, pbstrMoreInfoBannerImage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_MoreInfoBannerURL(self, pbstrMoreInfoBannerURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_MoreInfoText(self, pbstrMoreInfoText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMMediaContent2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ce8f78c1-74d9-11d2-b09d-00a0c9a81117}')
    @commethod(7)
    def get_MediaParameter(self, EntryNum: Int32, bstrName: win32more.Windows.Win32.Foundation.BSTR, pbstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_MediaParameterName(self, EntryNum: Int32, Index: Int32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PlaylistCount(self, pNumberEntries: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMMediaStream(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMediaStream
    _iid_ = Guid('{bebe595d-9a6f-11d0-8fde-00c04fd9189d}')
    @commethod(9)
    def Initialize(self, pSourceObject: win32more.Windows.Win32.System.Com.IUnknown, dwFlags: UInt32, PurposeId: POINTER(Guid), StreamType: win32more.Windows.Win32.Media.DirectShow.STREAM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetState(self, State: win32more.Windows.Win32.Media.DirectShow.FILTER_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def JoinAMMultiMediaStream(self, pAMMultiMediaStream: win32more.Windows.Win32.Media.DirectShow.IAMMultiMediaStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def JoinFilter(self, pMediaStreamFilter: win32more.Windows.Win32.Media.DirectShow.IMediaStreamFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def JoinFilterGraph(self, pFilterGraph: win32more.Windows.Win32.Media.DirectShow.IFilterGraph) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMMediaTypeSample(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IStreamSample
    _iid_ = Guid('{ab6b4afb-f6e4-11d0-900d-00c04fd9189d}')
    @commethod(8)
    def SetPointer(self, pBuffer: POINTER(Byte), lSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPointer(self, ppBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSize(self) -> Int32: ...
    @commethod(11)
    def GetTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsSyncPoint(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSyncPoint(self, bIsSyncPoint: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsPreroll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetPreroll(self, bIsPreroll: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetActualDataLength(self) -> Int32: ...
    @commethod(18)
    def SetActualDataLength(self, __MIDL__IAMMediaTypeSample0000: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetMediaType(self, ppMediaType: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetMediaType(self, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def IsDiscontinuity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetDiscontinuity(self, bDiscontinuity: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMediaTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetMediaTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMMediaTypeStream(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMediaStream
    _iid_ = Guid('{ab6b4afa-f6e4-11d0-900d-00c04fd9189d}')
    @commethod(9)
    def GetFormat(self, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFormat(self, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSample(self, lSampleSize: Int32, pbBuffer: POINTER(Byte), dwFlags: UInt32, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, ppAMMediaTypeSample: POINTER(win32more.Windows.Win32.Media.DirectShow.IAMMediaTypeSample)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetStreamAllocatorRequirements(self, pProps: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetStreamAllocatorRequirements(self, pProps: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMMultiMediaStream(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMultiMediaStream
    _iid_ = Guid('{bebe595c-9a6f-11d0-8fde-00c04fd9189d}')
    @commethod(12)
    def Initialize(self, StreamType: win32more.Windows.Win32.Media.DirectShow.STREAM_TYPE, dwFlags: UInt32, pFilterGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFilterGraph(self, ppGraphBuilder: POINTER(win32more.Windows.Win32.Media.DirectShow.IGraphBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetFilter(self, ppFilter: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaStreamFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AddMediaStream(self, pStreamObject: win32more.Windows.Win32.System.Com.IUnknown, PurposeId: POINTER(Guid), dwFlags: UInt32, ppNewStream: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OpenFile(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OpenMoniker(self, pCtx: win32more.Windows.Win32.System.Com.IBindCtx, pMoniker: win32more.Windows.Win32.System.Com.IMoniker, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Render(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMNetShowConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa2aa8f1-8b62-11d0-a520-000000000000}')
    @commethod(7)
    def get_BufferingTime(self, pBufferingTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BufferingTime(self, BufferingTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UseFixedUDPPort(self, pUseFixedUDPPort: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_UseFixedUDPPort(self, UseFixedUDPPort: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FixedUDPPort(self, pFixedUDPPort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_FixedUDPPort(self, FixedUDPPort: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UseHTTPProxy(self, pUseHTTPProxy: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_UseHTTPProxy(self, UseHTTPProxy: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_EnableAutoProxy(self, pEnableAutoProxy: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EnableAutoProxy(self, EnableAutoProxy: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_HTTPProxyHost(self, pbstrHTTPProxyHost: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_HTTPProxyHost(self, bstrHTTPProxyHost: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_HTTPProxyPort(self, pHTTPProxyPort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_HTTPProxyPort(self, HTTPProxyPort: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_EnableMulticast(self, pEnableMulticast: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_EnableMulticast(self, EnableMulticast: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_EnableUDP(self, pEnableUDP: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_EnableUDP(self, EnableUDP: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_EnableTCP(self, pEnableTCP: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_EnableTCP(self, EnableTCP: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_EnableHTTP(self, pEnableHTTP: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_EnableHTTP(self, EnableHTTP: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMNetShowExProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa2aa8f5-8b62-11d0-a520-000000000000}')
    @commethod(7)
    def get_SourceProtocol(self, pSourceProtocol: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Bandwidth(self, pBandwidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ErrorCorrection(self, pbstrErrorCorrection: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CodecCount(self, pCodecCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCodecInstalled(self, CodecNum: Int32, pCodecInstalled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCodecDescription(self, CodecNum: Int32, pbstrCodecDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCodecURL(self, CodecNum: Int32, pbstrCodecURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CreationDate(self, pCreationDate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SourceLink(self, pbstrSourceLink: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMNetShowPreroll(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{aae7e4e2-6388-11d1-8d93-006097c9a2b2}')
    @commethod(7)
    def put_Preroll(self, fPreroll: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Preroll(self, pfPreroll: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMNetworkStatus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa2aa8f3-8b62-11d0-a520-000000000000}')
    @commethod(7)
    def get_ReceivedPackets(self, pReceivedPackets: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RecoveredPackets(self, pRecoveredPackets: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LostPackets(self, pLostPackets: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReceptionQuality(self, pReceptionQuality: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_BufferingCount(self, pBufferingCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsBroadcast(self, pIsBroadcast: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_BufferingProgress(self, pBufferingProgress: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMOpenProgress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8e1c39a1-de53-11cf-aa63-0080c744528d}')
    @commethod(3)
    def QueryProgress(self, pllTotal: POINTER(Int64), pllCurrent: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AbortOperation(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMOverlayFX(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{62fae250-7e65-4460-bfc9-6398b322073c}')
    @commethod(3)
    def QueryOverlayFXCaps(self, lpdwOverlayFXCaps: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetOverlayFX(self, dwOverlayFX: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOverlayFX(self, lpdwOverlayFX: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMParse(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c47a3420-005c-11d2-9038-00a0c9697298}')
    @commethod(3)
    def GetParseTime(self, prtCurrent: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParseTime(self, rtCurrent: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMPhysicalPinInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f938c991-3029-11cf-8c44-00aa006b6814}')
    @commethod(3)
    def GetPhysicalType(self, pType: POINTER(Int32), ppszType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMPlayList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868fe-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemCount(self, pdwItems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItem(self, dwItemIndex: UInt32, ppItem: POINTER(win32more.Windows.Win32.Media.DirectShow.IAMPlayListItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNamedEvent(self, pwszEventName: win32more.Windows.Win32.Foundation.PWSTR, dwItemIndex: UInt32, ppItem: POINTER(win32more.Windows.Win32.Media.DirectShow.IAMPlayListItem), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRepeatInfo(self, pdwRepeatCount: POINTER(UInt32), pdwRepeatStart: POINTER(UInt32), pdwRepeatEnd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMPlayListItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868ff-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceCount(self, pdwSources: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSourceURL(self, dwSourceIndex: UInt32, pbstrURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceStart(self, dwSourceIndex: UInt32, prtStart: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSourceDuration(self, dwSourceIndex: UInt32, prtDuration: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceStartMarker(self, dwSourceIndex: UInt32, pdwMarker: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSourceEndMarker(self, dwSourceIndex: UInt32, pdwMarker: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSourceStartMarkerName(self, dwSourceIndex: UInt32, pbstrStartMarker: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSourceEndMarkerName(self, dwSourceIndex: UInt32, pbstrEndMarker: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLinkURL(self, pbstrURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetScanDuration(self, dwSourceIndex: UInt32, prtScanDuration: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMPluginControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e26a181-f40c-4635-8786-976284b52981}')
    @commethod(3)
    def GetPreferredClsid(self, subType: POINTER(Guid), clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPreferredClsidByIndex(self, index: UInt32, subType: POINTER(Guid), clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPreferredClsid(self, subType: POINTER(Guid), clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsDisabled(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDisabledByIndex(self, index: UInt32, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDisabled(self, clsid: POINTER(Guid), disabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsLegacyDisabled(self, dllName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMPushSource(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IAMLatency
    _iid_ = Guid('{f185fe76-e64e-11d2-b76e-00c04fb6bd3d}')
    @commethod(4)
    def GetPushSourceFlags(self, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPushSourceFlags(self, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetStreamOffset(self, rtOffset: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStreamOffset(self, prtOffset: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMaxStreamOffset(self, prtMaxOffset: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetMaxStreamOffset(self, rtMaxOffset: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMRebuild(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02ef04dd-7580-11d1-bece-00c04fb6e937}')
    @commethod(3)
    def RebuildNow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMResourceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8389d2d0-77d7-11d1-abe6-00a0c905f375}')
    @commethod(3)
    def Reserve(self, dwFlags: UInt32, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMStats(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bc9bcf80-dcd2-11d2-abf6-00a0c905f375}')
    @commethod(7)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetValueByIndex(self, lIndex: Int32, szName: POINTER(win32more.Windows.Win32.Foundation.BSTR), lCount: POINTER(Int32), dLast: POINTER(Double), dAverage: POINTER(Double), dStdDev: POINTER(Double), dMin: POINTER(Double), dMax: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetValueByName(self, szName: win32more.Windows.Win32.Foundation.BSTR, lIndex: POINTER(Int32), lCount: POINTER(Int32), dLast: POINTER(Double), dAverage: POINTER(Double), dStdDev: POINTER(Double), dMin: POINTER(Double), dMax: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetIndex(self, szName: win32more.Windows.Win32.Foundation.BSTR, lCreate: Int32, plIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddValue(self, lIndex: Int32, dValue: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMStreamConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e13340-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def SetFormat(self, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormat(self, ppmt: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfCapabilities(self, piCount: POINTER(Int32), piSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamCaps(self, iIndex: Int32, ppmt: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)), pSCC: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMStreamControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36b73881-c2c8-11cf-8b46-00805f6cef60}')
    @commethod(3)
    def StartAt(self, ptStart: POINTER(Int64), dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopAt(self, ptStop: POINTER(Int64), bSendExtra: win32more.Windows.Win32.Foundation.BOOL, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInfo(self, pInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_STREAM_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMStreamSelect(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c1960960-17f5-11d1-abe1-00a0c905f375}')
    @commethod(3)
    def Count(self, pcStreams: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Info(self, lIndex: Int32, ppmt: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)), pdwFlags: POINTER(UInt32), plcid: POINTER(UInt32), pdwGroup: POINTER(UInt32), ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown), ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Enable(self, lIndex: Int32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTVAudio(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83ec1c30-23d1-11d1-99e6-00a0c9560266}')
    @commethod(3)
    def GetHardwareSupportedTVAudioModes(self, plModes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAvailableTVAudioModes(self, plModes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_TVAudioMode(self, plMode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_TVAudioMode(self, lMode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterNotificationCallBack(self, pNotify: win32more.Windows.Win32.Media.DirectShow.IAMTunerNotification, lEvents: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnRegisterNotificationCallBack(self, pNotify: win32more.Windows.Win32.Media.DirectShow.IAMTunerNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTVAudioNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83ec1c33-23d1-11d1-99e6-00a0c9560266}')
    @commethod(3)
    def OnEvent(self, Event: win32more.Windows.Win32.Media.DirectShow.AMTVAudioEventType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTVTuner(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IAMTuner
    _iid_ = Guid('{211a8766-03ac-11d1-8d13-00aa00bd8339}')
    @commethod(18)
    def get_AvailableTVFormats(self, lAnalogVideoStandard: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TVFormat(self, plAnalogVideoStandard: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AutoTune(self, lChannel: Int32, plFoundSignal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def StoreAutoTune(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_NumInputConnections(self, plNumInputConnections: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_InputType(self, lIndex: Int32, InputType: win32more.Windows.Win32.Media.DirectShow.TunerInputType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_InputType(self, lIndex: Int32, pInputType: POINTER(win32more.Windows.Win32.Media.DirectShow.TunerInputType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_ConnectInput(self, lIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ConnectInput(self, plIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_VideoFrequency(self, lFreq: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_AudioFrequency(self, lFreq: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTimecodeDisplay(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b496ce2-811b-11cf-8c77-00aa006b6814}')
    @commethod(3)
    def GetTCDisplayEnable(self, pState: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTCDisplayEnable(self, State: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTCDisplay(self, Param: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTCDisplay(self, Param: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTimecodeGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b496ce0-811b-11cf-8c77-00aa006b6814}')
    @commethod(3)
    def GetTCGMode(self, Param: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTCGMode(self, Param: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_VITCLine(self, Line: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_VITCLine(self, pLine: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetTimecode(self, pTimecodeSample: POINTER(win32more.Windows.Win32.Media.TIMECODE_SAMPLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTimecode(self, pTimecodeSample: POINTER(win32more.Windows.Win32.Media.TIMECODE_SAMPLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTimecodeReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b496ce1-811b-11cf-8c77-00aa006b6814}')
    @commethod(3)
    def GetTCRMode(self, Param: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTCRMode(self, Param: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_VITCLine(self, Line: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_VITCLine(self, pLine: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTimecode(self, pTimecodeSample: POINTER(win32more.Windows.Win32.Media.TIMECODE_SAMPLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTuner(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{211a8761-03ac-11d1-8d13-00aa00bd8339}')
    @commethod(3)
    def put_Channel(self, lChannel: Int32, lVideoSubChannel: Int32, lAudioSubChannel: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Channel(self, plChannel: POINTER(Int32), plVideoSubChannel: POINTER(Int32), plAudioSubChannel: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChannelMinMax(self, lChannelMin: POINTER(Int32), lChannelMax: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_CountryCode(self, lCountryCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CountryCode(self, plCountryCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TuningSpace(self, lTuningSpace: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TuningSpace(self, plTuningSpace: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Logon(self, hCurrentUser: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Logout(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SignalPresent(self, plSignalStrength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Mode(self, lMode: win32more.Windows.Win32.Media.DirectShow.AMTunerModeType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Mode(self, plMode: POINTER(win32more.Windows.Win32.Media.DirectShow.AMTunerModeType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetAvailableModes(self, plModes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterNotificationCallBack(self, pNotify: win32more.Windows.Win32.Media.DirectShow.IAMTunerNotification, lEvents: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UnRegisterNotificationCallBack(self, pNotify: win32more.Windows.Win32.Media.DirectShow.IAMTunerNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMTunerNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{211a8760-03ac-11d1-8d13-00aa00bd8339}')
    @commethod(3)
    def OnEvent(self, Event: win32more.Windows.Win32.Media.DirectShow.AMTunerEventType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVfwCaptureDialogs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d8d715a0-6e5e-11d0-b3f0-00aa003761c5}')
    @commethod(3)
    def HasDialog(self, iDialog: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowDialog(self, iDialog: Int32, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendDriverMessage(self, iDialog: Int32, uMsg: Int32, dw1: Int32, dw2: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVfwCompressDialogs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d8d715a3-6e5e-11d0-b3f0-00aa003761c5}')
    @commethod(3)
    def ShowDialog(self, iDialog: Int32, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetState(self, pState: VoidPtr, pcbState: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetState(self, pState: VoidPtr, cbState: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendDriverMessage(self, uMsg: Int32, dw1: Int32, dw2: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVideoAccelerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{256a6a22-fbad-11d1-82bf-00a0c9696c8f}')
    @commethod(3)
    def GetVideoAcceleratorGUIDs(self, pdwNumGuidsSupported: POINTER(UInt32), pGuidsSupported: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUncompFormatsSupported(self, pGuid: POINTER(Guid), pdwNumFormatsSupported: POINTER(UInt32), pFormatsSupported: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDPIXELFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInternalMemInfo(self, pGuid: POINTER(Guid), pamvaUncompDataInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVAUncompDataInfo), pamvaInternalMemInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVAInternalMemInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCompBufferInfo(self, pGuid: POINTER(Guid), pamvaUncompDataInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVAUncompDataInfo), pdwNumTypesCompBuffers: POINTER(UInt32), pamvaCompBufferInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVACompBufferInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInternalCompBufferInfo(self, pdwNumTypesCompBuffers: POINTER(UInt32), pamvaCompBufferInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVACompBufferInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginFrame(self, amvaBeginFrameInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVABeginFrameInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndFrame(self, pEndFrameInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVAEndFrameInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBuffer(self, dwTypeIndex: UInt32, dwBufferIndex: UInt32, bReadOnly: win32more.Windows.Win32.Foundation.BOOL, ppBuffer: POINTER(VoidPtr), lpStride: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ReleaseBuffer(self, dwTypeIndex: UInt32, dwBufferIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Execute(self, dwFunction: UInt32, lpPrivateInputData: VoidPtr, cbPrivateInputData: UInt32, lpPrivateOutputDat: VoidPtr, cbPrivateOutputData: UInt32, dwNumBuffers: UInt32, pamvaBufferInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVABUFFERINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def QueryRenderStatus(self, dwTypeIndex: UInt32, dwBufferIndex: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DisplayFrame(self, dwFlipToIndex: UInt32, pMediaSample: win32more.Windows.Win32.Media.DirectShow.IMediaSample) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVideoAcceleratorNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{256a6a21-fbad-11d1-82bf-00a0c9696c8f}')
    @commethod(3)
    def GetUncompSurfacesInfo(self, pGuid: POINTER(Guid), pUncompBufferInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVAUncompBufferInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetUncompSurfacesInfo(self, dwActualUncompSurfacesAllocated: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCreateVideoAcceleratorData(self, pGuid: POINTER(Guid), pdwSizeMiscData: POINTER(UInt32), ppMiscData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVideoCompression(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e13343-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def put_KeyFrameRate(self, KeyFrameRate: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_KeyFrameRate(self, pKeyFrameRate: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_PFramesPerKeyFrame(self, PFramesPerKeyFrame: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_PFramesPerKeyFrame(self, pPFramesPerKeyFrame: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_Quality(self, Quality: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Quality(self, pQuality: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_WindowSize(self, WindowSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_WindowSize(self, pWindowSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInfo(self, pszVersion: win32more.Windows.Win32.Foundation.PWSTR, pcbVersion: POINTER(Int32), pszDescription: win32more.Windows.Win32.Foundation.PWSTR, pcbDescription: POINTER(Int32), pDefaultKeyFrameRate: POINTER(Int32), pDefaultPFramesPerKey: POINTER(Int32), pDefaultQuality: POINTER(Double), pCapabilities: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OverrideKeyFrame(self, FrameNumber: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OverrideFrameSize(self, FrameNumber: Int32, Size: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVideoControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a2e0670-28e4-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def GetCaps(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, pCapsFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMode(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, Mode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMode(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, Mode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentActualFrameRate(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, ActualFrameRate: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxAvailableFrameRate(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, iIndex: Int32, Dimensions: win32more.Windows.Win32.Foundation.SIZE, MaxAvailableFrameRate: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFrameRateList(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, iIndex: Int32, Dimensions: win32more.Windows.Win32.Foundation.SIZE, ListSize: POINTER(Int32), FrameRates: POINTER(POINTER(Int64))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVideoDecimationProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{60d32930-13da-11d3-9ec6-c4fcaef5c7be}')
    @commethod(3)
    def QueryDecimationUsage(self, lpUsage: POINTER(win32more.Windows.Win32.Media.DirectShow.DECIMATION_USAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDecimationUsage(self, Usage: win32more.Windows.Win32.Media.DirectShow.DECIMATION_USAGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMVideoProcAmp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6e13360-30ac-11d0-a18c-00a0c9118956}')
    @commethod(3)
    def GetRange(self, Property: Int32, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Set(self, Property: Int32, lValue: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Get(self, Property: Int32, lValue: POINTER(Int32), Flags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMWMBufferPass(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6dd816d7-e740-4123-9e24-2444412644d8}')
    @commethod(3)
    def SetNotify(self, pCallback: win32more.Windows.Win32.Media.DirectShow.IAMWMBufferPassCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMWMBufferPassCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b25b8372-d2d2-44b2-8653-1b8dae332489}')
    @commethod(3)
    def Notify(self, pNSSBuffer3: win32more.Windows.Win32.Media.WindowsMediaFormat.INSSBuffer3, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, prtStart: POINTER(Int64), prtEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMWstDecoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c056de21-75c2-11d3-a184-00105aef9f33}')
    @commethod(3)
    def GetDecoderLevel(self, lpLevel: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_WST_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentService(self, lpService: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_WST_SERVICE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceState(self, lpState: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_WST_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetServiceState(self, State: win32more.Windows.Win32.Media.DirectShow.AM_WST_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputFormat(self, lpbmih: POINTER(win32more.Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetOutputFormat(self, lpbmi: POINTER(win32more.Windows.Win32.Graphics.Gdi.BITMAPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBackgroundColor(self, pdwPhysColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetBackgroundColor(self, dwPhysColor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRedrawAlways(self, lpbOption: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetRedrawAlways(self, bOption: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDrawBackgroundMode(self, lpMode: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_WST_DRAWBGMODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetDrawBackgroundMode(self, Mode: win32more.Windows.Win32.Media.DirectShow.AM_WST_DRAWBGMODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetAnswerMode(self, bAnswer: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAnswerMode(self, pbAnswer: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetHoldPage(self, bHoldPage: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetHoldPage(self, pbHoldPage: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCurrentPage(self, pWstPage: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_WST_PAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetCurrentPage(self, WstPage: win32more.Windows.Win32.Media.DirectShow.AM_WST_PAGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAMovieSetup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3d8cec0-7e5a-11cf-bbc5-00805f6cef20}')
    @commethod(3)
    def Register(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAsyncReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868aa-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def RequestAllocator(self, pPreferred: win32more.Windows.Win32.Media.DirectShow.IMemAllocator, pProps: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES), ppActual: POINTER(win32more.Windows.Win32.Media.DirectShow.IMemAllocator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Request(self, pSample: win32more.Windows.Win32.Media.DirectShow.IMediaSample, dwUser: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WaitForNext(self, dwTimeout: UInt32, ppSample: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaSample), pdwUser: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SyncReadAligned(self, pSample: win32more.Windows.Win32.Media.DirectShow.IMediaSample) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SyncRead(self, llPosition: Int64, lLength: Int32, pBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Length(self, pTotal: POINTER(Int64), pAvailable: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BeginFlush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndFlush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioData(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMemoryData
    _iid_ = Guid('{54c719c0-af60-11d0-8212-00c04fc32c45}')
    @commethod(6)
    def GetFormat(self, pWaveFormatCurrent: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFormat(self, lpWaveFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioMediaStream(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMediaStream
    _iid_ = Guid('{f7537560-a3be-11d0-8212-00c04fc32c45}')
    @commethod(9)
    def GetFormat(self, pWaveFormatCurrent: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFormat(self, lpWaveFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSample(self, pAudioData: win32more.Windows.Win32.Media.DirectShow.IAudioData, dwFlags: UInt32, ppSample: POINTER(win32more.Windows.Win32.Media.DirectShow.IAudioStreamSample)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioStreamSample(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IStreamSample
    _iid_ = Guid('{345fee00-aba5-11d0-8212-00c04fc32c45}')
    @commethod(8)
    def GetAudioData(self, ppAudio: POINTER(win32more.Windows.Win32.Media.DirectShow.IAudioData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_AUX(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7def4c09-6e66-4567-a819-f0e17f4a81ab}')
    @commethod(3)
    def QueryCapabilities(self, pdwNumAuxInputsBSTR: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumCapability(self, dwIndex: UInt32, dwInputID: POINTER(UInt32), pConnectorType: POINTER(Guid), ConnTypeNum: POINTER(UInt32), NumVideoStds: POINTER(UInt32), AnalogStds: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_AutoDemodulate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ddf15b12-bd25-11d2-9ca0-00c04f7971e0}')
    @commethod(3)
    def put_AutoDemodulate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_AutoDemodulateEx(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IBDA_AutoDemodulate
    _iid_ = Guid('{34518d13-1182-48e6-b28f-b24987787326}')
    @commethod(4)
    def get_SupportedDeviceNodeTypes(self, ulcDeviceNodeTypesMax: UInt32, pulcDeviceNodeTypes: POINTER(UInt32), pguidDeviceNodeTypes: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_SupportedVideoFormats(self, pulAMTunerModeType: POINTER(UInt32), pulAnalogVideoStandard: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_AuxInputCount(self, pulCompositeCount: POINTER(UInt32), pulSvideoCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_ConditionalAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cd51f1e0-7be9-4123-8482-a2a796c0a6b0}')
    @commethod(3)
    def get_SmartCardStatus(self, pCardStatus: POINTER(win32more.Windows.Win32.Media.DirectShow.SmartCardStatusType), pCardAssociation: POINTER(win32more.Windows.Win32.Media.DirectShow.SmartCardAssociationType), pbstrCardError: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfOOBLocked: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SmartCardInfo(self, pbstrCardName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrCardManufacturer: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfDaylightSavings: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), pbyRatingRegion: POINTER(Byte), plTimeZoneOffsetMinutes: POINTER(Int32), pbstrLanguage: POINTER(win32more.Windows.Win32.Foundation.BSTR), pEALocationCode: POINTER(win32more.Windows.Win32.Media.DirectShow.EALocationCodeType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_SmartCardApplications(self, pulcApplications: POINTER(UInt32), ulcApplicationsMax: UInt32, rgApplications: POINTER(win32more.Windows.Win32.Media.DirectShow.SmartCardApplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Entitlement(self, usVirtualChannel: UInt16, pEntitlement: POINTER(win32more.Windows.Win32.Media.DirectShow.EntitlementType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def TuneByChannel(self, usVirtualChannel: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProgram(self, usProgramNumber: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddProgram(self, usProgramNumber: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveProgram(self, usProgramNumber: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetModuleUI(self, byDialogNumber: Byte, pbstrURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def InformUIClosed(self, byDialogNumber: Byte, CloseReason: win32more.Windows.Win32.Media.DirectShow.UICloseReasonType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_ConditionalAccessEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{497c3418-23cb-44ba-bb62-769f506fcea7}')
    @commethod(3)
    def CheckEntitlementToken(self, ulDialogRequest: UInt32, bstrLanguage: win32more.Windows.Win32.Foundation.BSTR, RequestType: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_REQUESTTYPE, ulcbEntitlementTokenLen: UInt32, pbEntitlementToken: POINTER(Byte), pulDescrambleStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCaptureToken(self, ulcbCaptureTokenLen: UInt32, pbCaptureToken: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenBroadcastMmi(self, ulDialogRequest: UInt32, bstrLanguage: win32more.Windows.Win32.Foundation.BSTR, EventId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CloseMmiDialog(self, ulDialogRequest: UInt32, bstrLanguage: win32more.Windows.Win32.Foundation.BSTR, ulDialogNumber: UInt32, ReasonCode: win32more.Windows.Win32.Media.DirectShow.BDA_CONDITIONALACCESS_MMICLOSEREASON, pulSessionResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDialogRequestNumber(self, pulDialogRequestNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DRIDRMService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f9bc2a5-44a3-4c52-aab1-0bbce5a1381d}')
    @commethod(3)
    def SetDRM(self, bstrNewDrm: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDRMStatus(self, pbstrDrmUuidList: POINTER(win32more.Windows.Win32.Foundation.BSTR), DrmUuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPairingStatus(self, penumPairingStatus: POINTER(win32more.Windows.Win32.Media.DirectShow.BDA_DrmPairingError)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DRIWMDRMSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{05c690f8-56db-4bb2-b053-79c12098bb26}')
    @commethod(3)
    def AcknowledgeLicense(self, hrLicenseAck: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessLicenseChallenge(self, dwcbLicenseMessage: UInt32, pbLicenseMessage: POINTER(Byte), pdwcbLicenseResponse: POINTER(UInt32), ppbLicenseResponse: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ProcessRegistrationChallenge(self, dwcbRegistrationMessage: UInt32, pbRegistrationMessage: POINTER(Byte), pdwcbRegistrationResponse: POINTER(UInt32), ppbRegistrationResponse: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRevInfo(self, dwRevInfoLen: UInt32, pbRevInfo: POINTER(Byte), pdwResponse: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCrl(self, dwCrlLen: UInt32, pbCrlLen: POINTER(Byte), pdwResponse: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetHMSAssociationData(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastCardeaError(self, pdwError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DRM(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f98d88b0-1992-4cd6-a6d9-b9afab99330d}')
    @commethod(3)
    def GetDRMPairingStatus(self, pdwStatus: POINTER(UInt32), phError: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PerformDRMPairing(self, fSync: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DRMService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bff6b5bb-b0ae-484c-9dca-73528fb0b46e}')
    @commethod(3)
    def SetDRM(self, puuidNewDrm: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDRMStatus(self, pbstrDrmUuidList: POINTER(win32more.Windows.Win32.Foundation.BSTR), DrmUuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DeviceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd0a5af3-b41d-11d2-9c95-00c04f7971e0}')
    @commethod(3)
    def StartChanges(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CheckChanges(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CommitChanges(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeState(self, pState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DiagnosticProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag
    _iid_ = Guid('{20e80cb5-c543-4c1b-8eb3-49e719eee7d4}')
class IBDA_DigitalDemodulator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ef30f379-985b-4d10-b640-a79d5e04e1e0}')
    @commethod(3)
    def put_ModulationType(self, pModulationType: POINTER(win32more.Windows.Win32.Media.DirectShow.ModulationType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ModulationType(self, pModulationType: POINTER(win32more.Windows.Win32.Media.DirectShow.ModulationType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_InnerFECMethod(self, pFECMethod: POINTER(win32more.Windows.Win32.Media.DirectShow.FECMethod)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_InnerFECMethod(self, pFECMethod: POINTER(win32more.Windows.Win32.Media.DirectShow.FECMethod)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_InnerFECRate(self, pFECRate: POINTER(win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_InnerFECRate(self, pFECRate: POINTER(win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_OuterFECMethod(self, pFECMethod: POINTER(win32more.Windows.Win32.Media.DirectShow.FECMethod)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OuterFECMethod(self, pFECMethod: POINTER(win32more.Windows.Win32.Media.DirectShow.FECMethod)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_OuterFECRate(self, pFECRate: POINTER(win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_OuterFECRate(self, pFECRate: POINTER(win32more.Windows.Win32.Media.DirectShow.BinaryConvolutionCodeRate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_SymbolRate(self, pSymbolRate: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SymbolRate(self, pSymbolRate: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_SpectralInversion(self, pSpectralInversion: POINTER(win32more.Windows.Win32.Media.DirectShow.SpectralInversion)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_SpectralInversion(self, pSpectralInversion: POINTER(win32more.Windows.Win32.Media.DirectShow.SpectralInversion)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DigitalDemodulator2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IBDA_DigitalDemodulator
    _iid_ = Guid('{525ed3ee-5cf3-4e1e-9a06-5368a84f9a6e}')
    @commethod(17)
    def put_GuardInterval(self, pGuardInterval: POINTER(win32more.Windows.Win32.Media.DirectShow.GuardInterval)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_GuardInterval(self, pGuardInterval: POINTER(win32more.Windows.Win32.Media.DirectShow.GuardInterval)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_TransmissionMode(self, pTransmissionMode: POINTER(win32more.Windows.Win32.Media.DirectShow.TransmissionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TransmissionMode(self, pTransmissionMode: POINTER(win32more.Windows.Win32.Media.DirectShow.TransmissionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_RollOff(self, pRollOff: POINTER(win32more.Windows.Win32.Media.DirectShow.RollOff)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_RollOff(self, pRollOff: POINTER(win32more.Windows.Win32.Media.DirectShow.RollOff)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Pilot(self, pPilot: POINTER(win32more.Windows.Win32.Media.DirectShow.Pilot)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Pilot(self, pPilot: POINTER(win32more.Windows.Win32.Media.DirectShow.Pilot)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DigitalDemodulator3(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IBDA_DigitalDemodulator2
    _iid_ = Guid('{13f19604-7d32-4359-93a2-a05205d90ac9}')
    @commethod(25)
    def put_SignalTimeouts(self, pSignalTimeouts: POINTER(win32more.Windows.Win32.Media.DirectShow.BDA_SIGNAL_TIMEOUTS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_SignalTimeouts(self, pSignalTimeouts: POINTER(win32more.Windows.Win32.Media.DirectShow.BDA_SIGNAL_TIMEOUTS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_PLPNumber(self, pPLPNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_PLPNumber(self, pPLPNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_DiseqCommand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f84e2ab0-3c6b-45e3-a0fc-8669d4b81f11}')
    @commethod(3)
    def put_EnableDiseqCommands(self, bEnable: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_DiseqLNBSource(self, ulLNBSource: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_DiseqUseToneBurst(self, bUseToneBurst: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_DiseqRepeats(self, ulRepeats: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_DiseqSendCommand(self, ulRequestId: UInt32, ulcbCommandLen: UInt32, pbCommand: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DiseqResponse(self, ulRequestId: UInt32, pulcbResponseLen: POINTER(UInt32), pbResponse: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_EasMessage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d806973d-3ebe-46de-8fbb-6358fe784208}')
    @commethod(3)
    def get_EasMessage(self, ulEventID: UInt32, ppEASObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_Encoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a8bad59-59fe-4559-a0ba-396cfaa98ae3}')
    @commethod(3)
    def QueryCapabilities(self, NumAudioFmts: POINTER(UInt32), NumVideoFmts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumAudioCapability(self, FmtIndex: UInt32, MethodID: POINTER(UInt32), AlgorithmType: POINTER(UInt32), SamplingRate: POINTER(UInt32), BitDepth: POINTER(UInt32), NumChannels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumVideoCapability(self, FmtIndex: UInt32, MethodID: POINTER(UInt32), AlgorithmType: POINTER(UInt32), VerticalSize: POINTER(UInt32), HorizontalSize: POINTER(UInt32), AspectRatio: POINTER(UInt32), FrameRateCode: POINTER(UInt32), ProgressiveSequence: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetParameters(self, AudioBitrateMode: UInt32, AudioBitrate: UInt32, AudioMethodID: UInt32, AudioProgram: UInt32, VideoBitrateMode: UInt32, VideoBitrate: UInt32, VideoMethodID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetState(self, AudioBitrateMax: POINTER(UInt32), AudioBitrateMin: POINTER(UInt32), AudioBitrateMode: POINTER(UInt32), AudioBitrateStepping: POINTER(UInt32), AudioBitrate: POINTER(UInt32), AudioMethodID: POINTER(UInt32), AvailableAudioPrograms: POINTER(UInt32), AudioProgram: POINTER(UInt32), VideoBitrateMax: POINTER(UInt32), VideoBitrateMin: POINTER(UInt32), VideoBitrateMode: POINTER(UInt32), VideoBitrate: POINTER(UInt32), VideoBitrateStepping: POINTER(UInt32), VideoMethodID: POINTER(UInt32), SignalSourceID: POINTER(UInt32), SignalFormat: POINTER(UInt64), SignalLock: POINTER(win32more.Windows.Win32.Foundation.BOOL), SignalLevel: POINTER(Int32), SignalToNoiseRatio: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_EthernetFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71985f43-1ca1-11d3-9cc8-00c04f7971e0}')
    @commethod(3)
    def GetMulticastListSize(self, pulcbAddresses: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PutMulticastList(self, ulcbAddresses: UInt32, pAddressList: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMulticastList(self, pulcbAddresses: POINTER(UInt32), pAddressList: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PutMulticastMode(self, ulModeMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMulticastMode(self, pulModeMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_EventingService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{207c413f-00dc-4c61-bad6-6fee1ff07064}')
    @commethod(3)
    def CompleteEvent(self, ulEventID: UInt32, ulEventResult: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_FDC(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{138adc7e-58ae-437f-b0b4-c9fe19d5b4ac}')
    @commethod(3)
    def GetStatus(self, CurrentBitrate: POINTER(UInt32), CarrierLock: POINTER(win32more.Windows.Win32.Foundation.BOOL), CurrentFrequency: POINTER(UInt32), CurrentSpectrumInversion: POINTER(win32more.Windows.Win32.Foundation.BOOL), CurrentPIDList: POINTER(win32more.Windows.Win32.Foundation.BSTR), CurrentTIDList: POINTER(win32more.Windows.Win32.Foundation.BSTR), Overflow: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RequestTables(self, TableIDs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPid(self, PidsToAdd: win32more.Windows.Win32.Foundation.BSTR, RemainingFilterEntries: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemovePid(self, PidsToRemove: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddTid(self, TidsToAdd: win32more.Windows.Win32.Foundation.BSTR, CurrentTidList: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveTid(self, TidsToRemove: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTableSection(self, Pid: POINTER(UInt32), MaxBufferSize: UInt32, ActualSize: POINTER(UInt32), SecBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_FrequencyFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71985f47-1ca1-11d3-9cc8-00c04f7971e0}')
    @commethod(3)
    def put_Autotune(self, ulTransponder: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Autotune(self, pulTransponder: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_Frequency(self, ulFrequency: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Frequency(self, pulFrequency: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_Polarity(self, Polarity: win32more.Windows.Win32.Media.DirectShow.Polarisation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Polarity(self, pPolarity: POINTER(win32more.Windows.Win32.Media.DirectShow.Polarisation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Range(self, ulRange: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Range(self, pulRange: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Bandwidth(self, ulBandwidth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Bandwidth(self, pulBandwidth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_FrequencyMultiplier(self, ulMultiplier: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_FrequencyMultiplier(self, pulMultiplier: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_GuideDataDeliveryService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0afcb73-23e7-4bc6-bafa-fdc167b4719f}')
    @commethod(3)
    def GetGuideDataType(self, pguidDataType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGuideData(self, pulcbBufferLen: POINTER(UInt32), pbBuffer: POINTER(Byte), pulGuideDataPercentageProgress: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestGuideDataUpdate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTuneXmlFromServiceIdx(self, ul64ServiceIdx: UInt64, pbstrTuneXml: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetServices(self, pulcbBufferLen: POINTER(UInt32), pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetServiceInfoFromTuneXml(self, bstrTuneXml: win32more.Windows.Win32.Foundation.BSTR, pbstrServiceDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_IPSinkControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3f4dc8e2-4050-11d3-8f4b-00c04f7971e2}')
    @commethod(3)
    def GetMulticastList(self, pulcbSize: POINTER(UInt32), pbBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterIPAddress(self, pulcbSize: POINTER(UInt32), pbBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_IPSinkInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a750108f-492e-4d51-95f7-649b23ff7ad7}')
    @commethod(3)
    def get_MulticastList(self, pulcbAddresses: POINTER(UInt32), ppbAddressList: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_AdapterIPAddress(self, pbstrBuffer: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AdapterDescription(self, pbstrBuffer: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_IPV4Filter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71985f44-1ca1-11d3-9cc8-00c04f7971e0}')
    @commethod(3)
    def GetMulticastListSize(self, pulcbAddresses: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PutMulticastList(self, ulcbAddresses: UInt32, pAddressList: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMulticastList(self, pulcbAddresses: POINTER(UInt32), pAddressList: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PutMulticastMode(self, ulModeMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMulticastMode(self, pulModeMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_IPV6Filter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e1785a74-2a23-4fb3-9245-a8f88017ef33}')
    @commethod(3)
    def GetMulticastListSize(self, pulcbAddresses: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PutMulticastList(self, ulcbAddresses: UInt32, pAddressList: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMulticastList(self, pulcbAddresses: POINTER(UInt32), pAddressList: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PutMulticastMode(self, ulModeMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMulticastMode(self, pulModeMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_ISDBConditionalAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e68c627-16c2-4e6c-b1e2-d00170cdaa0f}')
    @commethod(3)
    def SetIsdbCasRequest(self, ulRequestId: UInt32, ulcbRequestBufferLen: UInt32, pbRequestBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_LNBInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{992cf102-49f9-4719-a664-c4f23e2408f4}')
    @commethod(3)
    def put_LocalOscilatorFrequencyLowBand(self, ulLOFLow: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_LocalOscilatorFrequencyLowBand(self, pulLOFLow: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_LocalOscilatorFrequencyHighBand(self, ulLOFHigh: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_LocalOscilatorFrequencyHighBand(self, pulLOFHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_HighLowSwitchFrequency(self, ulSwitchFrequency: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_HighLowSwitchFrequency(self, pulSwitchFrequency: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_MUX(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{942aafec-4c05-4c74-b8eb-8706c2a4943f}')
    @commethod(3)
    def SetPidList(self, ulPidListCount: UInt32, pbPidListBuffer: POINTER(win32more.Windows.Win32.Media.DirectShow.BDA_MUX_PIDLISTITEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPidList(self, pulPidListCount: POINTER(UInt32), pbPidListBuffer: POINTER(win32more.Windows.Win32.Media.DirectShow.BDA_MUX_PIDLISTITEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_NameValueService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7f0b3150-7b81-4ad4-98e3-7e9097094301}')
    @commethod(3)
    def GetValueNameByIndex(self, ulIndex: UInt32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrLanguage: win32more.Windows.Win32.Foundation.BSTR, pbstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, ulDialogRequest: UInt32, bstrLanguage: win32more.Windows.Win32.Foundation.BSTR, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrValue: win32more.Windows.Win32.Foundation.BSTR, ulReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_NetworkProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd501041-8ebe-11ce-8183-00aa00577da2}')
    @commethod(3)
    def PutSignalSource(self, ulSignalSource: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignalSource(self, pulSignalSource: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkType(self, pguidNetworkType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PutTuningSpace(self, guidTuningSpace: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTuningSpace(self, pguidTuingSpace: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterDeviceFilter(self, pUnkFilterControl: win32more.Windows.Win32.System.Com.IUnknown, ppvRegisitrationContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnRegisterDeviceFilter(self, pvRegistrationContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_NullTransform(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ddf15b0d-bd25-11d2-9ca0-00c04f7971e0}')
    @commethod(3)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_PinControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0ded49d5-a8b7-4d5d-97a1-12b0c195874d}')
    @commethod(3)
    def GetPinID(self, pulPinID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPinType(self, pulPinType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegistrationContext(self, pulRegistrationCtx: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_SignalProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2f1644b-b409-11d2-bc69-00a0c9ee9e16}')
    @commethod(3)
    def PutNetworkType(self, guidNetworkType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNetworkType(self, pguidNetworkType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PutSignalSource(self, ulSignalSource: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignalSource(self, pulSignalSource: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PutTuningSpace(self, guidTuningSpace: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTuningSpace(self, pguidTuingSpace: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_SignalStatistics(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1347d106-cf3a-428a-a5cb-ac0d9a2a4338}')
    @commethod(3)
    def put_SignalStrength(self, lDbStrength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SignalStrength(self, plDbStrength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_SignalQuality(self, lPercentQuality: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_SignalQuality(self, plPercentQuality: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_SignalPresent(self, fPresent: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SignalPresent(self, pfPresent: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_SignalLocked(self, fLocked: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_SignalLocked(self, pfLocked: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_SampleTime(self, lmsSampleTime: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SampleTime(self, plmsSampleTime: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_Topology(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79b56888-7fea-4690-b45d-38fd3c7849be}')
    @commethod(3)
    def GetNodeTypes(self, pulcNodeTypes: POINTER(UInt32), ulcNodeTypesMax: UInt32, rgulNodeTypes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNodeDescriptors(self, ulcNodeDescriptors: POINTER(UInt32), ulcNodeDescriptorsMax: UInt32, rgNodeDescriptors: POINTER(win32more.Windows.Win32.Media.DirectShow.BDANODE_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNodeInterfaces(self, ulNodeType: UInt32, pulcInterfaces: POINTER(UInt32), ulcInterfacesMax: UInt32, rgguidInterfaces: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPinTypes(self, pulcPinTypes: POINTER(UInt32), ulcPinTypesMax: UInt32, rgulPinTypes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTemplateConnections(self, pulcConnections: POINTER(UInt32), ulcConnectionsMax: UInt32, rgConnections: POINTER(win32more.Windows.Win32.Media.DirectShow.BDA_TEMPLATE_CONNECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreatePin(self, ulPinType: UInt32, pulPinId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeletePin(self, ulPinId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetMediaType(self, ulPinId: UInt32, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMedium(self, ulPinId: UInt32, pMedium: POINTER(win32more.Windows.Win32.Media.DirectShow.REGPINMEDIUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateTopology(self, ulInputPinId: UInt32, ulOutputPinId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetControlNode(self, ulInputPinId: UInt32, ulOutputPinId: UInt32, ulNodeType: UInt32, ppControlNode: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_TransportStreamInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8e882535-5f86-47ab-86cf-c281a72a0549}')
    @commethod(3)
    def get_PatTableTickCount(self, pPatTickCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_TransportStreamSelector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dcfafe9-b45e-41b3-bb2a-561eb129ae98}')
    @commethod(3)
    def SetTSID(self, usTSID: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTSInformation(self, pulTSInformationBufferLen: POINTER(UInt32), pbTSInformationBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_UserActivityService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53b14189-e478-4b7a-a1ff-506db4b99dfe}')
    @commethod(3)
    def SetCurrentTunerUseReason(self, dwUseReason: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUserActivityInterval(self, pdwActivityInterval: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UserActivityDetected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_VoidTransform(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71985f46-1ca1-11d3-9cc8-00c04f7971e0}')
    @commethod(3)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_WMDRMSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4be6fa3d-07cd-4139-8b80-8c18ba3aec88}')
    @commethod(3)
    def GetStatus(self, MaxCaptureToken: POINTER(UInt32), MaxStreamingPid: POINTER(UInt32), MaxLicense: POINTER(UInt32), MinSecurityLevel: POINTER(UInt32), RevInfoSequenceNumber: POINTER(UInt32), RevInfoIssuedTime: POINTER(UInt64), RevInfoTTL: POINTER(UInt32), RevListVersion: POINTER(UInt32), ulState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRevInfo(self, ulRevInfoLen: UInt32, pbRevInfo: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCrl(self, ulCrlLen: UInt32, pbCrlLen: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TransactMessage(self, ulcbRequest: UInt32, pbRequest: POINTER(Byte), pulcbResponse: POINTER(UInt32), pbResponse: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLicense(self, uuidKey: POINTER(Guid), pulPackageLen: POINTER(UInt32), pbPackage: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReissueLicense(self, uuidKey: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RenewLicense(self, ulInXmrLicenseLen: UInt32, pbInXmrLicense: POINTER(Byte), ulEntitlementTokenLen: UInt32, pbEntitlementToken: POINTER(Byte), pulDescrambleStatus: POINTER(UInt32), pulOutXmrLicenseLen: POINTER(UInt32), pbOutXmrLicense: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetKeyInfo(self, pulKeyInfoLen: POINTER(UInt32), pbKeyInfo: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBDA_WMDRMTuner(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86d979cf-a8a7-4f94-b5fb-14c0aca68fe6}')
    @commethod(3)
    def PurchaseEntitlement(self, ulDialogRequest: UInt32, bstrLanguage: win32more.Windows.Win32.Foundation.BSTR, ulPurchaseTokenLen: UInt32, pbPurchaseToken: POINTER(Byte), pulDescrambleStatus: POINTER(UInt32), pulCaptureTokenLen: POINTER(UInt32), pbCaptureToken: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelCaptureToken(self, ulCaptureTokenLen: UInt32, pbCaptureToken: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPidProtection(self, ulPid: UInt32, uuidKey: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPidProtection(self, pulPid: UInt32, uuidKey: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSyncValue(self, ulSyncValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStartCodeProfile(self, pulStartCodeProfileLen: POINTER(UInt32), pbStartCodeProfile: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBPCSatelliteTuner(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IAMTuner
    _iid_ = Guid('{211a8765-03ac-11d1-8d13-00aa00bd8339}')
    @commethod(18)
    def get_DefaultSubChannelTypes(self, plDefaultVideoType: POINTER(Int32), plDefaultAudioType: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_DefaultSubChannelTypes(self, lDefaultVideoType: Int32, lDefaultAudioType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def IsTapingPermitted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBaseFilter(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMediaFilter
    _iid_ = Guid('{56a86895-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(10)
    def EnumPins(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumPins)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindPin(self, Id: win32more.Windows.Win32.Foundation.PWSTR, ppPin: POINTER(win32more.Windows.Win32.Media.DirectShow.IPin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryFilterInfo(self, pInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.FILTER_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def JoinFilterGraph(self, pGraph: win32more.Windows.Win32.Media.DirectShow.IFilterGraph, pName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def QueryVendorInfo(self, pVendorInfo: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBaseVideoMixer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61ded640-e912-11ce-a099-00aa00479a58}')
    @commethod(3)
    def SetLeadPin(self, iPin: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLeadPin(self, piPin: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputPinCount(self, piPinCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsUsingClock(self, pbValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetUsingClock(self, bValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetClockPeriod(self, pbValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetClockPeriod(self, bValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBasicAudio(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868b3-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def put_Volume(self, lVolume: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Volume(self, plVolume: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Balance(self, lBalance: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Balance(self, plBalance: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBasicVideo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868b5-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def get_AvgTimePerFrame(self, pAvgTimePerFrame: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_BitRate(self, pBitRate: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BitErrorRate(self, pBitErrorRate: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_VideoWidth(self, pVideoWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_VideoHeight(self, pVideoHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SourceLeft(self, SourceLeft: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_SourceLeft(self, pSourceLeft: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_SourceWidth(self, SourceWidth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SourceWidth(self, pSourceWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_SourceTop(self, SourceTop: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SourceTop(self, pSourceTop: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SourceHeight(self, SourceHeight: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SourceHeight(self, pSourceHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DestinationLeft(self, DestinationLeft: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DestinationLeft(self, pDestinationLeft: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DestinationWidth(self, DestinationWidth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_DestinationWidth(self, pDestinationWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_DestinationTop(self, DestinationTop: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_DestinationTop(self, pDestinationTop: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_DestinationHeight(self, DestinationHeight: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_DestinationHeight(self, pDestinationHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetSourcePosition(self, Left: Int32, Top: Int32, Width: Int32, Height: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetSourcePosition(self, pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetDefaultSourcePosition(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetDestinationPosition(self, Left: Int32, Top: Int32, Width: Int32, Height: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetDestinationPosition(self, pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetDefaultDestinationPosition(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetVideoSize(self, pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetVideoPaletteEntries(self, StartIndex: Int32, Entries: Int32, pRetrieved: POINTER(Int32), pPalette: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetCurrentImage(self, pBufferSize: POINTER(Int32), pDIBImage: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def IsUsingDefaultSource(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def IsUsingDefaultDestination(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBasicVideo2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IBasicVideo
    _iid_ = Guid('{329bb360-f6ea-11d1-9038-00a0c9697298}')
    @commethod(39)
    def GetPreferredAspectRatio(self, plAspectX: POINTER(Int32), plAspectY: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBroadcastEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3b21263f-26e8-489d-aac4-924f7efd9511}')
    @commethod(3)
    def Fire(self, EventID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBroadcastEventEx(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IBroadcastEvent
    _iid_ = Guid('{3d9e3887-1929-423f-8021-43682de95448}')
    @commethod(4)
    def FireEx(self, EventID: Guid, Param1: UInt32, Param2: UInt32, Param3: UInt32, Param4: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBufferingTime(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1e00486a-78dd-11d2-8dd3-006097c9a2b2}')
    @commethod(3)
    def GetBufferingTime(self, pdwMilliseconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBufferingTime(self, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICCSubStreamFiltering(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b2bd7ea-8347-467b-8dbf-62f784929cc3}')
    @commethod(3)
    def get_SubstreamTypes(self, pTypes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_SubstreamTypes(self, Types: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICameraControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2ba1785d-4d1b-44ef-85e8-c7f1d3f20184}')
    @commethod(3)
    def get_Exposure(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Exposure(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def getRange_Exposure(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Focus(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_Focus(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def getRange_Focus(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Iris(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Iris(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def getRange_Iris(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Zoom(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Zoom(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def getRange_Zoom(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_FocalLengths(self, plOcularFocalLength: POINTER(Int32), plObjectiveFocalLengthMin: POINTER(Int32), plObjectiveFocalLengthMax: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Pan(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Pan(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def getRange_Pan(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Tilt(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_Tilt(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def getRange_Tilt(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_PanTilt(self, pPanValue: POINTER(Int32), pTiltValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_PanTilt(self, PanValue: Int32, TiltValue: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Roll(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Roll(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def getRange_Roll(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ExposureRelative(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ExposureRelative(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def getRange_ExposureRelative(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_FocusRelative(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_FocusRelative(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def getRange_FocusRelative(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_IrisRelative(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_IrisRelative(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def getRange_IrisRelative(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_ZoomRelative(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_ZoomRelative(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def getRange_ZoomRelative(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_PanRelative(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_PanRelative(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_TiltRelative(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_TiltRelative(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def getRange_TiltRelative(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_PanTiltRelative(self, pPanValue: POINTER(Int32), pTiltValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_PanTiltRelative(self, PanValue: Int32, TiltValue: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def getRange_PanRelative(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_RollRelative(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_RollRelative(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def getRange_RollRelative(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_ScanMode(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_ScanMode(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_PrivacyMode(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def put_PrivacyMode(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICaptureGraphBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf87b6e0-8c27-11d0-b3f0-00aa003761c5}')
    @commethod(3)
    def SetFiltergraph(self, pfg: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiltergraph(self, ppfg: POINTER(win32more.Windows.Win32.Media.DirectShow.IGraphBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFileName(self, pType: POINTER(Guid), lpstrFile: win32more.Windows.Win32.Foundation.PWSTR, ppf: POINTER(win32more.Windows.Win32.Media.DirectShow.IBaseFilter), ppSink: POINTER(win32more.Windows.Win32.Media.DirectShow.IFileSinkFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindInterface(self, pCategory: POINTER(Guid), pf: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, riid: POINTER(Guid), ppint: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RenderStream(self, pCategory: POINTER(Guid), pSource: win32more.Windows.Win32.System.Com.IUnknown, pfCompressor: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pfRenderer: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ControlStream(self, pCategory: POINTER(Guid), pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pstart: POINTER(Int64), pstop: POINTER(Int64), wStartCookie: UInt16, wStopCookie: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AllocCapFile(self, lpstr: win32more.Windows.Win32.Foundation.PWSTR, dwlSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CopyCaptureFile(self, lpwstrOld: win32more.Windows.Win32.Foundation.PWSTR, lpwstrNew: win32more.Windows.Win32.Foundation.PWSTR, fAllowEscAbort: Int32, pCallback: win32more.Windows.Win32.Media.DirectShow.IAMCopyCaptureFileProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICaptureGraphBuilder2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{93e5a4e0-2d50-11d2-abfa-00a0c9c6e38d}')
    @commethod(3)
    def SetFiltergraph(self, pfg: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFiltergraph(self, ppfg: POINTER(win32more.Windows.Win32.Media.DirectShow.IGraphBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFileName(self, pType: POINTER(Guid), lpstrFile: win32more.Windows.Win32.Foundation.PWSTR, ppf: POINTER(win32more.Windows.Win32.Media.DirectShow.IBaseFilter), ppSink: POINTER(win32more.Windows.Win32.Media.DirectShow.IFileSinkFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindInterface(self, pCategory: POINTER(Guid), pType: POINTER(Guid), pf: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, riid: POINTER(Guid), ppint: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RenderStream(self, pCategory: POINTER(Guid), pType: POINTER(Guid), pSource: win32more.Windows.Win32.System.Com.IUnknown, pfCompressor: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pfRenderer: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ControlStream(self, pCategory: POINTER(Guid), pType: POINTER(Guid), pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pstart: POINTER(Int64), pstop: POINTER(Int64), wStartCookie: UInt16, wStopCookie: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AllocCapFile(self, lpstr: win32more.Windows.Win32.Foundation.PWSTR, dwlSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CopyCaptureFile(self, lpwstrOld: win32more.Windows.Win32.Foundation.PWSTR, lpwstrNew: win32more.Windows.Win32.Foundation.PWSTR, fAllowEscAbort: Int32, pCallback: win32more.Windows.Win32.Media.DirectShow.IAMCopyCaptureFileProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindPin(self, pSource: win32more.Windows.Win32.System.Com.IUnknown, pindir: win32more.Windows.Win32.Media.DirectShow.PIN_DIRECTION, pCategory: POINTER(Guid), pType: POINTER(Guid), fUnconnected: win32more.Windows.Win32.Foundation.BOOL, num: Int32, ppPin: POINTER(win32more.Windows.Win32.Media.DirectShow.IPin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConfigAsfWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45086030-f7e4-486a-b504-826bb5792a3b}')
    @commethod(3)
    def ConfigureFilterUsingProfileId(self, dwProfileId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentProfileId(self, pdwProfileId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConfigureFilterUsingProfileGuid(self, guidProfile: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentProfileGuid(self, pProfileGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ConfigureFilterUsingProfile(self, pProfile: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentProfile(self, ppProfile: POINTER(win32more.Windows.Win32.Media.WindowsMediaFormat.IWMProfile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetIndexMode(self, bIndexFile: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetIndexMode(self, pbIndexFile: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConfigAsfWriter2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IConfigAsfWriter
    _iid_ = Guid('{7989ccaa-53f0-44f0-884a-f3b03f6ae066}')
    @commethod(11)
    def StreamNumFromPin(self, pPin: win32more.Windows.Win32.Media.DirectShow.IPin, pwStreamNum: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetParam(self, dwParam: UInt32, dwParam1: UInt32, dwParam2: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetParam(self, dwParam: UInt32, pdwParam1: POINTER(UInt32), pdwParam2: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ResetMultiPassState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConfigAviMux(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5acd6aa0-f482-11ce-8b67-00aa00a3f1a6}')
    @commethod(3)
    def SetMasterStream(self, iStream: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMasterStream(self, pStream: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputCompatibilityIndex(self, fOldIndex: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputCompatibilityIndex(self, pfOldIndex: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConfigInterleaving(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bee3d220-157b-11d0-bd23-00a0c911ce86}')
    @commethod(3)
    def put_Mode(self, mode: win32more.Windows.Win32.Media.DirectShow.InterleavingMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Mode(self, pMode: POINTER(win32more.Windows.Win32.Media.DirectShow.InterleavingMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_Interleaving(self, prtInterleave: POINTER(Int64), prtPreroll: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Interleaving(self, prtInterleave: POINTER(Int64), prtPreroll: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateDevEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{29840822-5b84-11d0-bd3b-00a0c911ce86}')
    @commethod(3)
    def CreateClassEnumerator(self, clsidDeviceClass: POINTER(Guid), ppEnumMoniker: POINTER(win32more.Windows.Win32.System.Com.IEnumMoniker), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDDrawExclModeVideo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{153acc21-d83b-11d1-82bf-00a0c9696c8f}')
    @commethod(3)
    def SetDDrawObject(self, pDDrawObject: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDDrawObject(self, ppDDrawObject: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw), pbUsingExternal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDDrawSurface(self, pDDrawSurface: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDDrawSurface(self, ppDDrawSurface: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface), pbUsingExternal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDrawParameters(self, prcSource: POINTER(win32more.Windows.Win32.Foundation.RECT), prcTarget: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNativeVideoProps(self, pdwVideoWidth: POINTER(UInt32), pdwVideoHeight: POINTER(UInt32), pdwPictAspectRatioX: POINTER(UInt32), pdwPictAspectRatioY: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetCallbackInterface(self, pCallback: win32more.Windows.Win32.Media.DirectShow.IDDrawExclModeVideoCallback, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDDrawExclModeVideoCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{913c24a0-20ab-11d2-9038-00a0c9697298}')
    @commethod(3)
    def OnUpdateOverlay(self, bBefore: win32more.Windows.Win32.Foundation.BOOL, dwFlags: UInt32, bOldVisible: win32more.Windows.Win32.Foundation.BOOL, prcOldSrc: POINTER(win32more.Windows.Win32.Foundation.RECT), prcOldDest: POINTER(win32more.Windows.Win32.Foundation.RECT), bNewVisible: win32more.Windows.Win32.Foundation.BOOL, prcNewSrc: POINTER(win32more.Windows.Win32.Foundation.RECT), prcNewDest: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnUpdateColorKey(self, pKey: POINTER(win32more.Windows.Win32.Media.DirectShow.COLORKEY), dwColor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnUpdateSize(self, dwWidth: UInt32, dwHeight: UInt32, dwARWidth: UInt32, dwARHeight: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMOWrapperFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52d6f586-9f0f-4824-8fc8-e32ca04930c2}')
    @commethod(3)
    def Init(self, clsidDMO: POINTER(Guid), catDMO: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDShowPlugin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4746b7c8-700e-11d1-becc-00c04fb6e937}')
    @commethod(3)
    def get_URL(self, pURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_UserAgent(self, pUserAgent: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDVEnc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d18e17a0-aacb-11d0-afb0-00aa00b67a42}')
    @commethod(3)
    def get_IFormatResolution(self, VideoFormat: POINTER(Int32), DVFormat: POINTER(Int32), Resolution: POINTER(Int32), fDVInfo: Byte, sDVInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.DVINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_IFormatResolution(self, VideoFormat: Int32, DVFormat: Int32, Resolution: Int32, fDVInfo: Byte, sDVInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.DVINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDVRGB219(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{58473a19-2bc8-4663-8012-25f81babddd1}')
    @commethod(3)
    def SetRGB219(self, bState: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDVSplitter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92a3a302-da7c-4a1f-ba7e-1802bb5d2d02}')
    @commethod(3)
    def DiscardAlternateVideoFrames(self, nDiscard: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDecimateVideoImage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e5ea3e0-e924-11d2-b6da-00a0c995e8df}')
    @commethod(3)
    def SetDecimationImageSize(self, lWidth: Int32, lHeight: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResetDecimationImageSize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeferredCommand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868b8-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Confidence(self, pConfidence: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Postpone(self, newtime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetHResult(self, phrResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectDrawMediaSample(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ab6b4afe-f6e4-11d0-900d-00c04fd9189d}')
    @commethod(3)
    def GetSurfaceAndReleaseLock(self, ppDirectDrawSurface: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface), pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockMediaSamplePointer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectDrawMediaSampleAllocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ab6b4afc-f6e4-11d0-900d-00c04fd9189d}')
    @commethod(3)
    def GetDirectDraw(self, ppDirectDraw: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectDrawMediaStream(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMediaStream
    _iid_ = Guid('{f4104fce-9a70-11d0-8fde-00c04fd9189d}')
    @commethod(9)
    def GetFormat(self, pDDSDCurrent: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDSURFACEDESC), ppDirectDrawPalette: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawPalette), pDDSDDesired: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDSURFACEDESC), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFormat(self, pDDSurfaceDesc: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDSURFACEDESC), pDirectDrawPalette: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawPalette) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDirectDraw(self, ppDirectDraw: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDirectDraw(self, pDirectDraw: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateSample(self, pSurface: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT), dwFlags: UInt32, ppSample: POINTER(win32more.Windows.Win32.Media.DirectShow.IDirectDrawStreamSample)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimePerFrame(self, pFrameTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectDrawStreamSample(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IStreamSample
    _iid_ = Guid('{f4104fcf-9a70-11d0-8fde-00c04fd9189d}')
    @commethod(8)
    def GetSurface(self, ppDirectDrawSurface: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface), pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetRect(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectDrawVideo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36d39eb0-dd75-11ce-bf0e-00aa0055595a}')
    @commethod(3)
    def GetSwitches(self, pSwitches: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSwitches(self, Switches: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCaps(self, pCaps: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDCAPS_DX7)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEmulatedCaps(self, pCaps: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDCAPS_DX7)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSurfaceDesc(self, pSurfaceDesc: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDSURFACEDESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFourCCCodes(self, pCount: POINTER(UInt32), pCodes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetDirectDraw(self, pDirectDraw: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDirectDraw(self, ppDirectDraw: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSurfaceType(self, pSurfaceType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDefault(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UseScanLine(self, UseScanLine: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CanUseScanLine(self, UseScanLine: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UseOverlayStretch(self, UseOverlayStretch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CanUseOverlayStretch(self, UseOverlayStretch: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UseWhenFullScreen(self, UseWhenFullScreen: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def WillUseFullScreen(self, UseWhenFullScreen: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDistributorNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868af-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Run(self, tStart: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSyncSource(self, pClock: win32more.Windows.Win32.Media.IReferenceClock) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyGraphChange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDrawVideoImage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{48efb120-ab49-11d2-aed2-00a0c995e8d5}')
    @commethod(3)
    def DrawVideoImageBegin(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DrawVideoImageEnd(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DrawVideoImageDraw(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, lprcSrc: POINTER(win32more.Windows.Win32.Foundation.RECT), lprcDst: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDvdCmd(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5a4a97e4-94ee-4a55-9751-74b5643aa27d}')
    @commethod(3)
    def WaitForStart(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WaitForEnd(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDvdControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a70efe61-e2a3-11d0-a9be-00aa0061be93}')
    @commethod(3)
    def TitlePlay(self, ulTitle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChapterPlay(self, ulTitle: UInt32, ulChapter: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TimePlay(self, ulTitle: UInt32, bcdTime: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StopForResume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GoUp(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def TimeSearch(self, bcdTime: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ChapterSearch(self, ulChapter: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PrevPGSearch(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def TopPGSearch(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def NextPGSearch(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ForwardScan(self, dwSpeed: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def BackwardScan(self, dwSpeed: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MenuCall(self, MenuID: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UpperButtonSelect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def LowerButtonSelect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def LeftButtonSelect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RightButtonSelect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ButtonActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ButtonSelectAndActivate(self, ulButton: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def StillOff(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def PauseOn(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def PauseOff(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def MenuLanguageSelect(self, Language: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def AudioStreamChange(self, ulAudio: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SubpictureStreamChange(self, ulSubPicture: UInt32, bDisplay: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def AngleChange(self, ulAngle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def ParentalLevelSelect(self, ulParentalLevel: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ParentalCountrySelect(self, wCountry: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def KaraokeAudioPresentationModeChange(self, ulMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def VideoModePreferrence(self, ulPreferredDisplayMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetRoot(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def MouseActivate(self, point: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def MouseSelect(self, point: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def ChapterPlayAutoStop(self, ulTitle: UInt32, ulChapter: UInt32, ulChaptersToPlay: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDvdControl2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33bc7430-eec0-11d2-8201-00a0c9d74842}')
    @commethod(3)
    def PlayTitle(self, ulTitle: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PlayChapterInTitle(self, ulTitle: UInt32, ulChapter: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PlayAtTimeInTitle(self, ulTitle: UInt32, pStartTime: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_HMSF_TIMECODE), dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReturnFromSubmenu(self, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PlayAtTime(self, pTime: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_HMSF_TIMECODE), dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PlayChapter(self, ulChapter: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PlayPrevChapter(self, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ReplayChapter(self, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PlayNextChapter(self, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PlayForwards(self, dSpeed: Double, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PlayBackwards(self, dSpeed: Double, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ShowMenu(self, MenuID: win32more.Windows.Win32.Media.DirectShow.DVD_MENU_ID, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Resume(self, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SelectRelativeButton(self, buttonDir: win32more.Windows.Win32.Media.DirectShow.DVD_RELATIVE_BUTTON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ActivateButton(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SelectButton(self, ulButton: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SelectAndActivateButton(self, ulButton: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def StillOff(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Pause(self, bState: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SelectAudioStream(self, ulAudio: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SelectSubpictureStream(self, ulSubPicture: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetSubpictureState(self, bState: win32more.Windows.Win32.Foundation.BOOL, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SelectAngle(self, ulAngle: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SelectParentalLevel(self, ulParentalLevel: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SelectParentalCountry(self, bCountry: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SelectKaraokeAudioPresentationMode(self, ulMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SelectVideoModePreference(self, ulPreferredDisplayMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetDVDDirectory(self, pszwPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def ActivateAtPosition(self, point: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SelectAtPosition(self, point: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def PlayChaptersAutoStop(self, ulTitle: UInt32, ulChapter: UInt32, ulChaptersToPlay: UInt32, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def AcceptParentalLevelChange(self, bAccept: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetOption(self, flag: win32more.Windows.Win32.Media.DirectShow.DVD_OPTION_FLAG, fState: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetState(self, pState: win32more.Windows.Win32.Media.DirectShow.IDvdState, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def PlayPeriodInTitleAutoStop(self, ulTitle: UInt32, pStartTime: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_HMSF_TIMECODE), pEndTime: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_HMSF_TIMECODE), dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetGPRM(self, ulIndex: UInt32, wValue: UInt16, dwFlags: UInt32, ppCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SelectDefaultMenuLanguage(self, Language: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SelectDefaultAudioLanguage(self, Language: UInt32, audioExtension: win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SelectDefaultSubpictureLanguage(self, Language: UInt32, subpictureExtension: win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDvdGraphBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fcc152b6-f372-11d0-8e00-00c04fd7c08b}')
    @commethod(3)
    def GetFiltergraph(self, ppGB: POINTER(win32more.Windows.Win32.Media.DirectShow.IGraphBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDvdInterface(self, riid: POINTER(Guid), ppvIF: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RenderDvdVideoVolume(self, lpcwszPathName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pStatus: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_DVD_RENDERSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDvdInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a70efe60-e2a3-11d0-a9be-00aa0061be93}')
    @commethod(3)
    def GetCurrentDomain(self, pDomain: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_DOMAIN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentLocation(self, pLocation: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_PLAYBACK_LOCATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalTitleTime(self, pulTotalTime: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentButton(self, pulButtonsAvailable: POINTER(UInt32), pulCurrentButton: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentAngle(self, pulAnglesAvailable: POINTER(UInt32), pulCurrentAngle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentAudio(self, pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentSubpicture(self, pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32), pIsDisabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentUOPS(self, pUOP: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetAllSPRMs(self, pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAllGPRMs(self, pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetAudioLanguage(self, ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSubpictureLanguage(self, ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTitleAttributes(self, ulTitle: UInt32, pATR: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_ATR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetVMGAttributes(self, pATR: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_ATR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCurrentVideoAttributes(self, pATR: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCurrentAudioAttributes(self, pATR: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCurrentSubpictureAttributes(self, pATR: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetCurrentVolumeInfo(self, pulNumOfVol: POINTER(UInt32), pulThisVolNum: POINTER(UInt32), pSide: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_DISC_SIDE), pulNumOfTitles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetDVDTextInfo(self, pTextManager: POINTER(Byte), ulBufSize: UInt32, pulActualSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetPlayerParentalLevel(self, pulParentalLevel: POINTER(UInt32), pulCountryCode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetNumberOfChapters(self, ulTitle: UInt32, pulNumberOfChapters: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetTitleParentalLevels(self, ulTitle: UInt32, pulParentalLevels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetRoot(self, pRoot: win32more.Windows.Win32.Foundation.PSTR, ulBufSize: UInt32, pulActualSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDvdInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{34151510-eec0-11d2-8201-00a0c9d74842}')
    @commethod(3)
    def GetCurrentDomain(self, pDomain: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_DOMAIN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentLocation(self, pLocation: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_PLAYBACK_LOCATION2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalTitleTime(self, pTotalTime: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_HMSF_TIMECODE), ulTimeCodeFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentButton(self, pulButtonsAvailable: POINTER(UInt32), pulCurrentButton: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentAngle(self, pulAnglesAvailable: POINTER(UInt32), pulCurrentAngle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentAudio(self, pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentSubpicture(self, pulStreamsAvailable: POINTER(UInt32), pulCurrentStream: POINTER(UInt32), pbIsDisabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentUOPS(self, pulUOPs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetAllSPRMs(self, pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAllGPRMs(self, pRegisterArray: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetAudioLanguage(self, ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSubpictureLanguage(self, ulStream: UInt32, pLanguage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTitleAttributes(self, ulTitle: UInt32, pMenu: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_MenuAttributes), pTitle: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_TitleAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetVMGAttributes(self, pATR: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_MenuAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCurrentVideoAttributes(self, pATR: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_VideoAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetAudioAttributes(self, ulStream: UInt32, pATR: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_AudioAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetKaraokeAttributes(self, ulStream: UInt32, pAttributes: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_KaraokeAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetSubpictureAttributes(self, ulStream: UInt32, pATR: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_SubpictureAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetDVDVolumeInfo(self, pulNumOfVolumes: POINTER(UInt32), pulVolume: POINTER(UInt32), pSide: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_DISC_SIDE), pulNumOfTitles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetDVDTextNumberOfLanguages(self, pulNumOfLangs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetDVDTextLanguageInfo(self, ulLangIndex: UInt32, pulNumOfStrings: POINTER(UInt32), pLangCode: POINTER(UInt32), pbCharacterSet: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_TextCharSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetDVDTextStringAsNative(self, ulLangIndex: UInt32, ulStringIndex: UInt32, pbBuffer: POINTER(Byte), ulMaxBufferSize: UInt32, pulActualSize: POINTER(UInt32), pType: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetDVDTextStringAsUnicode(self, ulLangIndex: UInt32, ulStringIndex: UInt32, pchwBuffer: win32more.Windows.Win32.Foundation.PWSTR, ulMaxBufferSize: UInt32, pulActualSize: POINTER(UInt32), pType: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_TextStringType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetPlayerParentalLevel(self, pulParentalLevel: POINTER(UInt32), pbCountryCode: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetNumberOfChapters(self, ulTitle: UInt32, pulNumOfChapters: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetTitleParentalLevels(self, ulTitle: UInt32, pulParentalLevels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetDVDDirectory(self, pszwPath: win32more.Windows.Win32.Foundation.PWSTR, ulMaxSize: UInt32, pulActualSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def IsAudioStreamEnabled(self, ulStreamNum: UInt32, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetDiscID(self, pszwPath: win32more.Windows.Win32.Foundation.PWSTR, pullDiscID: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetState(self, pStateData: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetMenuLanguages(self, pLanguages: POINTER(UInt32), ulMaxLanguages: UInt32, pulActualLanguages: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetButtonAtPosition(self, point: win32more.Windows.Win32.Foundation.POINT, pulButtonIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetCmdFromEvent(self, lParam1: IntPtr, pCmdObj: POINTER(win32more.Windows.Win32.Media.DirectShow.IDvdCmd)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetDefaultMenuLanguage(self, pLanguage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetDefaultAudioLanguage(self, pLanguage: POINTER(UInt32), pAudioExtension: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_AUDIO_LANG_EXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetDefaultSubpictureLanguage(self, pLanguage: POINTER(UInt32), pSubpictureExtension: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_SUBPICTURE_LANG_EXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetDecoderCaps(self, pCaps: POINTER(win32more.Windows.Win32.Media.DirectShow.DVD_DECODER_CAPS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetButtonRect(self, ulButton: UInt32, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def IsSubpictureStreamEnabled(self, ulStreamNum: UInt32, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDvdState(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86303d6d-1c4a-4087-ab42-f711167048ef}')
    @commethod(3)
    def GetDiscID(self, pullUniqueID: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentalLevel(self, pulParentalLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IESEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f0e5357-af43-44e6-8547-654c645145d2}')
    @commethod(3)
    def GetEventId(self, pdwEventId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEventType(self, pguidEventType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCompletionStatus(self, dwResult: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetData(self, pbData: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStringData(self, pbstrData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IESEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{abd414bf-cfe5-4e5e-af5b-4b4e49c5bfeb}')
    @commethod(3)
    def OnESEventReceived(self, guidEventType: Guid, pESEvent: win32more.Windows.Win32.Media.DirectShow.IESEvent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEncoderAPI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70423839-6acc-4b23-b079-21dbf08156a5}')
    @commethod(3)
    def IsSupported(self, Api: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsAvailable(self, Api: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParameterRange(self, Api: POINTER(Guid), ValueMin: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), ValueMax: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), SteppingDelta: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetParameterValues(self, Api: POINTER(Guid), Values: POINTER(POINTER(win32more.Windows.Win32.System.Variant.VARIANT)), ValuesCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultValue(self, Api: POINTER(Guid), Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetValue(self, Api: POINTER(Guid), Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValue(self, Api: POINTER(Guid), Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumFilters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a86893-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Next(self, cFilters: UInt32, ppFilter: POINTER(win32more.Windows.Win32.Media.DirectShow.IBaseFilter), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cFilters: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumFilters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumMediaTypes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{89c31040-846b-11ce-97d3-00aa0055595a}')
    @commethod(3)
    def Next(self, cMediaTypes: UInt32, ppMediaTypes: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cMediaTypes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumMediaTypes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumPIDMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{afb6c2a2-2c41-11d3-8a60-0000f81e0e4a}')
    @commethod(3)
    def Next(self, cRequest: UInt32, pPIDMap: POINTER(win32more.Windows.Win32.Media.DirectShow.PID_MAP), pcReceived: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cRecords: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppIEnumPIDMap: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumPIDMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumPins(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a86892-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Next(self, cPins: UInt32, ppPins: POINTER(win32more.Windows.Win32.Media.DirectShow.IPin), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cPins: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumPins)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumRegFilters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868a4-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Next(self, cFilters: UInt32, apRegFilter: POINTER(POINTER(win32more.Windows.Win32.Media.DirectShow.REGFILTER)), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cFilters: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumRegFilters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumStreamIdMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{945c1566-6202-46fc-96c7-d87f289c6534}')
    @commethod(3)
    def Next(self, cRequest: UInt32, pStreamIdMap: POINTER(win32more.Windows.Win32.Media.DirectShow.STREAM_ID_MAP), pcReceived: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cRecords: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppIEnumStreamIdMap: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumStreamIdMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IFILTERMAPPER_MERIT = Int32
MERIT_PREFERRED: win32more.Windows.Win32.Media.DirectShow.IFILTERMAPPER_MERIT = 8388608
MERIT_NORMAL: win32more.Windows.Win32.Media.DirectShow.IFILTERMAPPER_MERIT = 6291456
MERIT_UNLIKELY: win32more.Windows.Win32.Media.DirectShow.IFILTERMAPPER_MERIT = 4194304
MERIT_DO_NOT_USE: win32more.Windows.Win32.Media.DirectShow.IFILTERMAPPER_MERIT = 2097152
MERIT_SW_COMPRESSOR: win32more.Windows.Win32.Media.DirectShow.IFILTERMAPPER_MERIT = 1048576
MERIT_HW_COMPRESSOR: win32more.Windows.Win32.Media.DirectShow.IFILTERMAPPER_MERIT = 1048656
class IFileSinkFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a2104830-7c70-11cf-8bce-00aa00a3f1a6}')
    @commethod(3)
    def SetFileName(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurFile(self, ppszFileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSinkFilter2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IFileSinkFilter
    _iid_ = Guid('{00855b90-ce1b-11d0-bd4f-00a0c911ce86}')
    @commethod(5)
    def SetMode(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMode(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSourceFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868a6-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Load(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurFile(self, ppszFileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterChain(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcfbdcf6-0dc2-45f5-9ab2-7c330ea09c29}')
    @commethod(3)
    def StartChain(self, pStartFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pEndFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PauseChain(self, pStartFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pEndFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopChain(self, pStartFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pEndFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveChain(self, pStartFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pEndFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterGraph(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a8689f-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def AddFilter(self, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveFilter(self, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumFilters(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumFilters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindFilterByName(self, pName: win32more.Windows.Win32.Foundation.PWSTR, ppFilter: POINTER(win32more.Windows.Win32.Media.DirectShow.IBaseFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ConnectDirect(self, ppinOut: win32more.Windows.Win32.Media.DirectShow.IPin, ppinIn: win32more.Windows.Win32.Media.DirectShow.IPin, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reconnect(self, ppin: win32more.Windows.Win32.Media.DirectShow.IPin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Disconnect(self, ppin: win32more.Windows.Win32.Media.DirectShow.IPin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDefaultSyncSource(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterGraph2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder
    _iid_ = Guid('{36b73882-c2c8-11cf-8b46-00805f6cef60}')
    @commethod(18)
    def AddSourceFilterForMoniker(self, pMoniker: win32more.Windows.Win32.System.Com.IMoniker, pCtx: win32more.Windows.Win32.System.Com.IBindCtx, lpcwstrFilterName: win32more.Windows.Win32.Foundation.PWSTR, ppFilter: POINTER(win32more.Windows.Win32.Media.DirectShow.IBaseFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ReconnectEx(self, ppin: win32more.Windows.Win32.Media.DirectShow.IPin, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RenderEx(self, pPinOut: win32more.Windows.Win32.Media.DirectShow.IPin, dwFlags: UInt32, pvContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterGraph3(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IFilterGraph2
    _iid_ = Guid('{aaf38154-b80b-422f-91e6-b66467509a07}')
    @commethod(21)
    def SetSyncSourceEx(self, pClockForMostOfFilterGraph: win32more.Windows.Win32.Media.IReferenceClock, pClockForFilter: win32more.Windows.Win32.Media.IReferenceClock, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868ba-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def FindPin(self, strPinID: win32more.Windows.Win32.Foundation.BSTR, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(self, strName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_VendorInfo(self, strVendorInfo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Filter(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Pins(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsFileSource(self, pbIsSource: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Filename(self, pstrFilename: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Filename(self, strFilename: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterMapper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868a3-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def RegisterFilter(self, clsid: Guid, Name: win32more.Windows.Win32.Foundation.PWSTR, dwMerit: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterFilterInstance(self, clsid: Guid, Name: win32more.Windows.Win32.Foundation.PWSTR, MRId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterPin(self, Filter: Guid, Name: win32more.Windows.Win32.Foundation.PWSTR, bRendered: win32more.Windows.Win32.Foundation.BOOL, bOutput: win32more.Windows.Win32.Foundation.BOOL, bZero: win32more.Windows.Win32.Foundation.BOOL, bMany: win32more.Windows.Win32.Foundation.BOOL, ConnectsToFilter: Guid, ConnectsToPin: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RegisterPinType(self, clsFilter: Guid, strName: win32more.Windows.Win32.Foundation.PWSTR, clsMajorType: Guid, clsSubType: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterFilter(self, Filter: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnregisterFilterInstance(self, MRId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterPin(self, Filter: Guid, Name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumMatchingFilters(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumRegFilters), dwMerit: UInt32, bInputNeeded: win32more.Windows.Win32.Foundation.BOOL, clsInMaj: Guid, clsInSub: Guid, bRender: win32more.Windows.Win32.Foundation.BOOL, bOututNeeded: win32more.Windows.Win32.Foundation.BOOL, clsOutMaj: Guid, clsOutSub: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterMapper2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b79bb0b0-33c1-11d1-abe1-00a0c905f375}')
    @commethod(3)
    def CreateCategory(self, clsidCategory: POINTER(Guid), dwCategoryMerit: UInt32, Description: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterFilter(self, pclsidCategory: POINTER(Guid), szInstance: win32more.Windows.Win32.Foundation.PWSTR, Filter: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterFilter(self, clsidFilter: POINTER(Guid), Name: win32more.Windows.Win32.Foundation.PWSTR, ppMoniker: POINTER(win32more.Windows.Win32.System.Com.IMoniker), pclsidCategory: POINTER(Guid), szInstance: win32more.Windows.Win32.Foundation.PWSTR, prf2: POINTER(win32more.Windows.Win32.Media.DirectShow.REGFILTER2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumMatchingFilters(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumMoniker), dwFlags: UInt32, bExactMatch: win32more.Windows.Win32.Foundation.BOOL, dwMerit: UInt32, bInputNeeded: win32more.Windows.Win32.Foundation.BOOL, cInputTypes: UInt32, pInputTypes: POINTER(Guid), pMedIn: POINTER(win32more.Windows.Win32.Media.DirectShow.REGPINMEDIUM), pPinCategoryIn: POINTER(Guid), bRender: win32more.Windows.Win32.Foundation.BOOL, bOutputNeeded: win32more.Windows.Win32.Foundation.BOOL, cOutputTypes: UInt32, pOutputTypes: POINTER(Guid), pMedOut: POINTER(win32more.Windows.Win32.Media.DirectShow.REGPINMEDIUM), pPinCategoryOut: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterMapper3(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IFilterMapper2
    _iid_ = Guid('{b79bb0b1-33c1-11d1-abe1-00a0c905f375}')
    @commethod(7)
    def GetICreateDevEnum(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.ICreateDevEnum)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFrequencyMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{06fb45c1-693c-4ea7-b79f-7a6a54d8def2}')
    @commethod(3)
    def get_FrequencyMapping(self, ulCount: POINTER(UInt32), ppulList: POINTER(POINTER(UInt32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_FrequencyMapping(self, ulCount: UInt32, pList: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CountryCode(self, pulCountryCode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_CountryCode(self, ulCountryCode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_DefaultFrequencyMapping(self, ulCountryCode: UInt32, pulCount: POINTER(UInt32), ppulList: POINTER(POINTER(UInt32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CountryCodeList(self, pulCount: POINTER(UInt32), ppulList: POINTER(POINTER(UInt32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFullScreenVideo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dd1d7110-7836-11cf-bf47-00aa0055595a}')
    @commethod(3)
    def CountModes(self, pModes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetModeInfo(self, Mode: Int32, pWidth: POINTER(Int32), pHeight: POINTER(Int32), pDepth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentMode(self, pMode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsModeAvailable(self, Mode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsModeEnabled(self, Mode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetEnabled(self, Mode: Int32, bEnabled: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetClipFactor(self, pClipFactor: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetClipFactor(self, ClipFactor: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMessageDrain(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMessageDrain(self, hwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetMonitor(self, Monitor: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetMonitor(self, Monitor: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def HideOnDeactivate(self, Hide: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def IsHideOnDeactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetCaption(self, strCaption: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCaption(self, pstrCaption: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDefault(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFullScreenVideoEx(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IFullScreenVideo
    _iid_ = Guid('{53479470-f1dd-11cf-bc42-00aa00ac74f6}')
    @commethod(20)
    def SetAcceleratorTable(self, hwnd: win32more.Windows.Win32.Foundation.HWND, hAccel: win32more.Windows.Win32.UI.WindowsAndMessaging.HACCEL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetAcceleratorTable(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND), phAccel: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HACCEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def KeepPixelAspectRatio(self, KeepAspect: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsKeepPixelAspectRatio(self, pKeepAspect: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetCapabilitiesKey(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a8809222-07bb-48ea-951c-33158100625b}')
    @commethod(3)
    def GetCapabilitiesKey(self, pHKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGraphBuilder(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IFilterGraph
    _iid_ = Guid('{56a868a9-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(11)
    def Connect(self, ppinOut: win32more.Windows.Win32.Media.DirectShow.IPin, ppinIn: win32more.Windows.Win32.Media.DirectShow.IPin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Render(self, ppinOut: win32more.Windows.Win32.Media.DirectShow.IPin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RenderFile(self, lpcwstrFile: win32more.Windows.Win32.Foundation.PWSTR, lpcwstrPlayList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddSourceFilter(self, lpcwstrFileName: win32more.Windows.Win32.Foundation.PWSTR, lpcwstrFilterName: win32more.Windows.Win32.Foundation.PWSTR, ppFilter: POINTER(win32more.Windows.Win32.Media.DirectShow.IBaseFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetLogFile(self, hFile: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ShouldOperationContinue(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGraphConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03a1eb8e-32bf-4245-8502-114d08a9cb88}')
    @commethod(3)
    def Reconnect(self, pOutputPin: win32more.Windows.Win32.Media.DirectShow.IPin, pInputPin: win32more.Windows.Win32.Media.DirectShow.IPin, pmtFirstConnection: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), pUsingFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, hAbortEvent: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reconfigure(self, pCallback: win32more.Windows.Win32.Media.DirectShow.IGraphConfigCallback, pvContext: VoidPtr, dwFlags: UInt32, hAbortEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddFilterToCache(self, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumCacheFilter(self, pEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumFilters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveFilterFromCache(self, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStartTime(self, prtStart: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PushThroughData(self, pOutputPin: win32more.Windows.Win32.Media.DirectShow.IPin, pConnection: win32more.Windows.Win32.Media.DirectShow.IPinConnection, hEventAbort: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFilterFlags(self, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFilterFlags(self, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveFilterEx(self, pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGraphConfigCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ade0fd60-d19d-11d2-abf6-00a0c905f375}')
    @commethod(3)
    def Reconfigure(self, pvContext: VoidPtr, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGraphVersion(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868ab-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def QueryVersion(self, pVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIPDVDec(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b8e8bd60-0bfe-11d0-af91-00aa00b67a42}')
    @commethod(3)
    def get_IPDisplay(self, displayPix: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_IPDisplay(self, displayPix: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMPEG2PIDMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{afb6c2a1-2c41-11d3-8a60-0000f81e0e4a}')
    @commethod(3)
    def MapPID(self, culPID: UInt32, pulPID: POINTER(UInt32), MediaSampleContent: win32more.Windows.Win32.Media.DirectShow.MEDIA_SAMPLE_CONTENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnmapPID(self, culPID: UInt32, pulPID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumPIDMap(self, pIEnumPIDMap: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumPIDMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMPEG2StreamIdMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0e04c47-25b8-4369-925a-362a01d95444}')
    @commethod(3)
    def MapStreamId(self, ulStreamId: UInt32, MediaSampleContent: UInt32, ulSubstreamFilterValue: UInt32, iDataOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnmapStreamId(self, culStreamId: UInt32, pulStreamId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumStreamIdMap(self, ppIEnumStreamIdMap: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumStreamIdMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868b1-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def Run(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetState(self, msTimeout: Int32, pfs: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RenderFile(self, strFilename: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddSourceFilter(self, strFilename: win32more.Windows.Win32.Foundation.BSTR, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FilterCollection(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_RegFilterCollection(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def StopWhenReady(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868b6-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def GetEventHandle(self, hEvent: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEvent(self, lEventCode: POINTER(Int32), lParam1: POINTER(IntPtr), lParam2: POINTER(IntPtr), msTimeout: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WaitForCompletion(self, msTimeout: Int32, pEvCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelDefaultHandling(self, lEvCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RestoreDefaultHandling(self, lEvCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def FreeEventParams(self, lEvCode: Int32, lParam1: IntPtr, lParam2: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaEventEx(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMediaEvent
    _iid_ = Guid('{56a868c0-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(13)
    def SetNotifyWindow(self, hwnd: IntPtr, lMsg: Int32, lInstanceData: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetNotifyFlags(self, lNoNotifyFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetNotifyFlags(self, lplNoNotifyFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868a2-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Notify(self, EventCode: Int32, EventParam1: IntPtr, EventParam2: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{56a86899-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Run(self, tStart: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetState(self, dwMilliSecsTimeout: UInt32, State: POINTER(win32more.Windows.Win32.Media.DirectShow.FILTER_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSyncSource(self, pClock: win32more.Windows.Win32.Media.IReferenceClock) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSyncSource(self, pClock: POINTER(win32more.Windows.Win32.Media.IReferenceClock)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaParamInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d6cbb60-a223-44aa-842f-a2f06750be6d}')
    @commethod(3)
    def GetParamCount(self, pdwParams: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParamInfo(self, dwParamIndex: UInt32, pInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.MP_PARAMINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParamText(self, dwParamIndex: UInt32, ppwchText: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNumTimeFormats(self, pdwNumTimeFormats: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSupportedTimeFormat(self, dwFormatIndex: UInt32, pguidTimeFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurrentTimeFormat(self, pguidTimeFormat: POINTER(Guid), pTimeData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaParams(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d6cbb61-a223-44aa-842f-a2f06750be6e}')
    @commethod(3)
    def GetParam(self, dwParamIndex: UInt32, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParam(self, dwParamIndex: UInt32, value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddEnvelope(self, dwParamIndex: UInt32, cSegments: UInt32, pEnvelopeSegments: POINTER(win32more.Windows.Win32.Media.DirectShow.MP_ENVELOPE_SEGMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FlushEnvelope(self, dwParamIndex: UInt32, refTimeStart: Int64, refTimeEnd: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetTimeFormat(self, guidTimeFormat: Guid, mpTimeData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaPosition(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868b2-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def get_Duration(self, plength: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_CurrentPosition(self, llTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentPosition(self, pllTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StopTime(self, pllTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_StopTime(self, llTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PrerollTime(self, pllTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_PrerollTime(self, llTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Rate(self, dRate: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Rate(self, pdRate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CanSeekForward(self, pCanSeekForward: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CanSeekBackward(self, pCanSeekBackward: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaPropertyBag(ComPtr):
    extends: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag
    _iid_ = Guid('{6025a880-c0d5-11d0-bd4e-00a0c911ce86}')
    @commethod(5)
    def EnumProperty(self, iProperty: UInt32, pvarPropertyName: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarPropertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaSample(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a8689a-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def GetPointer(self, ppBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSize(self) -> Int32: ...
    @commethod(5)
    def GetTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsSyncPoint(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSyncPoint(self, bIsSyncPoint: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsPreroll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetPreroll(self, bIsPreroll: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetActualDataLength(self) -> Int32: ...
    @commethod(12)
    def SetActualDataLength(self, __MIDL__IMediaSample0000: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetMediaType(self, ppMediaType: POINTER(POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetMediaType(self, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsDiscontinuity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetDiscontinuity(self, bDiscontinuity: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetMediaTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetMediaTime(self, pTimeStart: POINTER(Int64), pTimeEnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaSample2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMediaSample
    _iid_ = Guid('{36b73884-c2c8-11cf-8b46-00805f6cef60}')
    @commethod(19)
    def GetProperties(self, cbProperties: UInt32, pbProperties: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetProperties(self, cbProperties: UInt32, pbProperties: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaSample2Config(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68961e68-832b-41ea-bc91-63593f3e70e3}')
    @commethod(3)
    def GetSurface(self, ppDirect3DSurface9: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaSeeking(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36b73880-c2c8-11cf-8b46-00805f6cef60}')
    @commethod(3)
    def GetCapabilities(self, pCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CheckCapabilities(self, pCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsFormatSupported(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryPreferredFormat(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTimeFormat(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsUsingTimeFormat(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetTimeFormat(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDuration(self, pDuration: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStopPosition(self, pStop: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCurrentPosition(self, pCurrent: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ConvertTimeFormat(self, pTarget: POINTER(Int64), pTargetFormat: POINTER(Guid), Source: Int64, pSourceFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetPositions(self, pCurrent: POINTER(Int64), dwCurrentFlags: UInt32, pStop: POINTER(Int64), dwStopFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPositions(self, pCurrent: POINTER(Int64), pStop: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAvailable(self, pEarliest: POINTER(Int64), pLatest: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetRate(self, dRate: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetRate(self, pdRate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetPreroll(self, pllPreroll: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b502d1bd-9a57-11d0-8fde-00c04fd9189d}')
    @commethod(3)
    def GetMultiMediaStream(self, ppMultiMediaStream: POINTER(win32more.Windows.Win32.Media.DirectShow.IMultiMediaStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInformation(self, pPurposeId: POINTER(Guid), pType: POINTER(win32more.Windows.Win32.Media.DirectShow.STREAM_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSameFormat(self, pStreamThatHasDesiredFormat: win32more.Windows.Win32.Media.DirectShow.IMediaStream, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateSample(self, dwFlags: UInt32, ppSample: POINTER(win32more.Windows.Win32.Media.DirectShow.IStreamSample)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSharedSample(self, pExistingSample: win32more.Windows.Win32.Media.DirectShow.IStreamSample, dwFlags: UInt32, ppNewSample: POINTER(win32more.Windows.Win32.Media.DirectShow.IStreamSample)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SendEndOfStream(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaStreamFilter(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IBaseFilter
    _iid_ = Guid('{bebe595e-9a6f-11d0-8fde-00c04fd9189d}')
    @commethod(15)
    def AddMediaStream(self, pAMMediaStream: win32more.Windows.Win32.Media.DirectShow.IAMMediaStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMediaStream(self, idPurpose: POINTER(Guid), ppMediaStream: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumMediaStreams(self, Index: Int32, ppMediaStream: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SupportSeeking(self, bRenderer: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ReferenceTimeToStreamTime(self, pTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetCurrentStreamTime(self, pCurrentStreamTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def WaitUntil(self, WaitStreamTime: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Flush(self, bCancelEOS: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def EndOfStream(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaTypeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868bc-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def get_Type(self, strType: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Subtype(self, strType: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMemAllocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a8689c-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def SetProperties(self, pRequest: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES), pActual: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperties(self, pProps: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Decommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBuffer(self, ppBuffer: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaSample), pStartTime: POINTER(Int64), pEndTime: POINTER(Int64), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReleaseBuffer(self, pBuffer: win32more.Windows.Win32.Media.DirectShow.IMediaSample) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMemAllocatorCallbackTemp(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMemAllocator
    _iid_ = Guid('{379a0cf0-c1de-11d2-abf5-00a0c905f375}')
    @commethod(9)
    def SetNotify(self, pNotify: win32more.Windows.Win32.Media.DirectShow.IMemAllocatorNotifyCallbackTemp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFreeCount(self, plBuffersFree: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMemAllocatorNotifyCallbackTemp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92980b30-c1de-11d2-abf5-00a0c905f375}')
    @commethod(3)
    def NotifyRelease(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMemInputPin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a8689d-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def GetAllocator(self, ppAllocator: POINTER(win32more.Windows.Win32.Media.DirectShow.IMemAllocator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyAllocator(self, pAllocator: win32more.Windows.Win32.Media.DirectShow.IMemAllocator, bReadOnly: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAllocatorRequirements(self, pProps: POINTER(win32more.Windows.Win32.Media.DirectShow.ALLOCATOR_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Receive(self, pSample: win32more.Windows.Win32.Media.DirectShow.IMediaSample) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReceiveMultiple(self, pSamples: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaSample), nSamples: Int32, nSamplesProcessed: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReceiveCanBlock(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMemoryData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{327fc560-af60-11d0-8212-00c04fc32c45}')
    @commethod(3)
    def SetBuffer(self, cbSize: UInt32, pbData: POINTER(Byte), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInfo(self, pdwLength: POINTER(UInt32), ppbData: POINTER(POINTER(Byte)), pcbActualData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetActual(self, cbDataValid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMixerOCX(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{81a3bd32-dee1-11d1-8508-00a0c91f9ca0}')
    @commethod(3)
    def OnDisplayChange(self, ulBitsPerPixel: UInt32, ulScreenWidth: UInt32, ulScreenHeight: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAspectRatio(self, pdwPictAspectRatioX: POINTER(UInt32), pdwPictAspectRatioY: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVideoSize(self, pdwVideoWidth: POINTER(UInt32), pdwVideoHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, pdwStatus: POINTER(POINTER(UInt32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnDraw(self, hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, prcDraw: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDrawRegion(self, lpptTopLeftSC: POINTER(win32more.Windows.Win32.Foundation.POINT), prcDrawCC: POINTER(win32more.Windows.Win32.Foundation.RECT), lprcClip: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(self, pmdns: win32more.Windows.Win32.Media.DirectShow.IMixerOCXNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnAdvise(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMixerOCXNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{81a3bd31-dee1-11d1-8508-00a0c91f9ca0}')
    @commethod(3)
    def OnInvalidateRect(self, lpcRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStatusChange(self, ulStatusFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDataChange(self, ulDataFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMixerPinConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{593cdde1-0759-11d1-9e69-00c04fd7c15b}')
    @commethod(3)
    def SetRelativePosition(self, dwLeft: UInt32, dwTop: UInt32, dwRight: UInt32, dwBottom: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRelativePosition(self, pdwLeft: POINTER(UInt32), pdwTop: POINTER(UInt32), pdwRight: POINTER(UInt32), pdwBottom: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetZOrder(self, dwZOrder: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetZOrder(self, pdwZOrder: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColorKey(self, pColorKey: POINTER(win32more.Windows.Win32.Media.DirectShow.COLORKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetColorKey(self, pColorKey: POINTER(win32more.Windows.Win32.Media.DirectShow.COLORKEY), pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBlendingParameter(self, dwBlendingParameter: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBlendingParameter(self, pdwBlendingParameter: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetAspectRatioMode(self, amAspectRatioMode: win32more.Windows.Win32.Media.DirectShow.AM_ASPECT_RATIO_MODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAspectRatioMode(self, pamAspectRatioMode: POINTER(win32more.Windows.Win32.Media.DirectShow.AM_ASPECT_RATIO_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetStreamTransparent(self, bStreamTransparent: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStreamTransparent(self, pbStreamTransparent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMixerPinConfig2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IMixerPinConfig
    _iid_ = Guid('{ebf47182-8764-11d1-9e69-00c04fd7c15b}')
    @commethod(15)
    def SetOverlaySurfaceColorControls(self, pColorControl: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDCOLORCONTROL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetOverlaySurfaceColorControls(self, pColorControl: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDCOLORCONTROL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMpeg2Demultiplexer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{436eee9c-264f-4242-90e1-4e330c107512}')
    @commethod(3)
    def CreateOutputPin(self, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), pszPinName: win32more.Windows.Win32.Foundation.PWSTR, ppIPin: POINTER(win32more.Windows.Win32.Media.DirectShow.IPin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetOutputPinMediaType(self, pszPinName: win32more.Windows.Win32.Foundation.PWSTR, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteOutputPin(self, pszPinName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMpegAudioDecoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b45dd570-3c77-11d1-abe1-00a0c905f375}')
    @commethod(3)
    def get_FrequencyDivider(self, pDivider: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_FrequencyDivider(self, Divider: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_DecoderAccuracy(self, pAccuracy: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_DecoderAccuracy(self, Accuracy: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Stereo(self, pStereo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Stereo(self, Stereo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DecoderWordSize(self, pWordSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DecoderWordSize(self, WordSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IntegerDecode(self, pIntDecode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IntegerDecode(self, IntDecode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DualMode(self, pIntDecode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_DualMode(self, IntDecode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_AudioFormat(self, lpFmt: POINTER(win32more.Windows.Win32.Media.DirectShow.MPEG1WAVEFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultiMediaStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b502d1bc-9a57-11d0-8fde-00c04fd9189d}')
    @commethod(3)
    def GetInformation(self, pdwFlags: POINTER(win32more.Windows.Win32.Media.DirectShow.MMSSF_GET_INFORMATION_FLAGS), pStreamType: POINTER(win32more.Windows.Win32.Media.DirectShow.STREAM_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMediaStream(self, idPurpose: POINTER(Guid), ppMediaStream: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumMediaStreams(self, Index: Int32, ppMediaStream: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetState(self, pCurrentState: POINTER(win32more.Windows.Win32.Media.DirectShow.STREAM_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetState(self, NewState: win32more.Windows.Win32.Media.DirectShow.STREAM_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTime(self, pCurrentTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDuration(self, pDuration: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(self, SeekTime: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEndOfStreamEventHandle(self, phEOS: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOverlay(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868a1-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def GetPalette(self, pdwColors: POINTER(UInt32), ppPalette: POINTER(POINTER(win32more.Windows.Win32.Graphics.Gdi.PALETTEENTRY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPalette(self, dwColors: UInt32, pPalette: POINTER(win32more.Windows.Win32.Graphics.Gdi.PALETTEENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDefaultColorKey(self, pColorKey: POINTER(win32more.Windows.Win32.Media.DirectShow.COLORKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColorKey(self, pColorKey: POINTER(win32more.Windows.Win32.Media.DirectShow.COLORKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColorKey(self, pColorKey: POINTER(win32more.Windows.Win32.Media.DirectShow.COLORKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWindowHandle(self, pHwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetClipList(self, pSourceRect: POINTER(win32more.Windows.Win32.Foundation.RECT), pDestinationRect: POINTER(win32more.Windows.Win32.Foundation.RECT), ppRgnData: POINTER(POINTER(win32more.Windows.Win32.Graphics.Gdi.RGNDATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetVideoPosition(self, pSourceRect: POINTER(win32more.Windows.Win32.Foundation.RECT), pDestinationRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Advise(self, pOverlayNotify: win32more.Windows.Win32.Media.DirectShow.IOverlayNotify, dwInterests: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Unadvise(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOverlayNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868a0-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def OnPaletteChange(self, dwColors: UInt32, pPalette: POINTER(win32more.Windows.Win32.Graphics.Gdi.PALETTEENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClipChange(self, pSourceRect: POINTER(win32more.Windows.Win32.Foundation.RECT), pDestinationRect: POINTER(win32more.Windows.Win32.Foundation.RECT), pRgnData: POINTER(win32more.Windows.Win32.Graphics.Gdi.RGNDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnColorKeyChange(self, pColorKey: POINTER(win32more.Windows.Win32.Media.DirectShow.COLORKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnPositionChange(self, pSourceRect: POINTER(win32more.Windows.Win32.Foundation.RECT), pDestinationRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOverlayNotify2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IOverlayNotify
    _iid_ = Guid('{680efa10-d535-11d1-87c8-00a0c9223196}')
    @commethod(7)
    def OnDisplayChange(self, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistMediaPropertyBag(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{5738e040-b67f-11d0-bd4d-00a0c911ce86}')
    @commethod(4)
    def InitNew(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pPropBag: win32more.Windows.Win32.Media.DirectShow.IMediaPropertyBag, pErrorLog: win32more.Windows.Win32.System.Com.IErrorLog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pPropBag: win32more.Windows.Win32.Media.DirectShow.IMediaPropertyBag, fClearDirty: win32more.Windows.Win32.Foundation.BOOL, fSaveAllProperties: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a86891-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Connect(self, pReceivePin: win32more.Windows.Win32.Media.DirectShow.IPin, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReceiveConnection(self, pConnector: win32more.Windows.Win32.Media.DirectShow.IPin, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConnectedTo(self, pPin: POINTER(win32more.Windows.Win32.Media.DirectShow.IPin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ConnectionMediaType(self, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryPinInfo(self, pInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.PIN_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def QueryDirection(self, pPinDir: POINTER(win32more.Windows.Win32.Media.DirectShow.PIN_DIRECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def QueryId(self, Id: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def QueryAccept(self, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumMediaTypes(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DirectShow.IEnumMediaTypes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def QueryInternalConnections(self, apPin: POINTER(win32more.Windows.Win32.Media.DirectShow.IPin), nPin: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EndOfStream(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def BeginFlush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EndFlush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def NewSegment(self, tStart: Int64, tStop: Int64, dRate: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPinConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4a9a62d3-27d4-403d-91e9-89f540e55534}')
    @commethod(3)
    def DynamicQueryAccept(self, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyEndOfStream(self, hNotifyEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsEndPin(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DynamicDisconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPinFlowControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c56e9858-dbf3-4f6b-8119-384af2060deb}')
    @commethod(3)
    def Block(self, dwBlockFlags: UInt32, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPinInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868bd-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def get_Pin(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ConnectedTo(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ConnectionMediaType(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FilterInfo(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(self, ppUnk: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Direction(self, ppDirection: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PinID(self, strPinID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_MediaTypes(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Connect(self, pPin: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ConnectDirect(self, pPin: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ConnectWithType(self, pPin: win32more.Windows.Win32.System.Com.IUnknown, pMediaType: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Render(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQualProp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1bd0ecb0-f8e2-11ce-aac6-0020af0b99a3}')
    @commethod(3)
    def get_FramesDroppedInRenderer(self, pcFrames: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_FramesDrawn(self, pcFramesDrawn: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AvgFrameRate(self, piAvgFrameRate: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Jitter(self, iJitter: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AvgSyncOffset(self, piAvg: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DevSyncOffset(self, piDev: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQualityControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868a5-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Notify(self, pSelf: win32more.Windows.Win32.Media.DirectShow.IBaseFilter, q: win32more.Windows.Win32.Media.DirectShow.Quality) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSink(self, piqc: win32more.Windows.Win32.Media.DirectShow.IQualityControl) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueueCommand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868b7-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def InvokeAtStreamTime(self, pCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDeferredCommand), time: Double, iid: POINTER(Guid), dispidMethod: Int32, wFlags: Int16, cArgs: Int32, pDispParams: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), puArgErr: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeAtPresentationTime(self, pCmd: POINTER(win32more.Windows.Win32.Media.DirectShow.IDeferredCommand), time: Double, iid: POINTER(Guid), dispidMethod: Int32, wFlags: Int16, cArgs: Int32, pDispParams: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), puArgErr: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRegFilterInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868bb-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def get_Name(self, strName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Filter(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRegisterServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7b3a2f01-0751-48dd-b556-004785171c54}')
    @commethod(3)
    def RegisterService(self, guidService: POINTER(Guid), pUnkObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceConsumer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868ad-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def AcquireResource(self, idResource: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseResource(self, idResource: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868ac-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Register(self, pName: win32more.Windows.Win32.Foundation.PWSTR, cResource: Int32, plToken: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterGroup(self, pName: win32more.Windows.Win32.Foundation.PWSTR, cResource: Int32, palTokens: POINTER(Int32), plToken: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestResource(self, idResource: Int32, pFocusObject: win32more.Windows.Win32.System.Com.IUnknown, pConsumer: win32more.Windows.Win32.Media.DirectShow.IResourceConsumer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifyAcquire(self, idResource: Int32, pConsumer: win32more.Windows.Win32.Media.DirectShow.IResourceConsumer, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyRelease(self, idResource: Int32, pConsumer: win32more.Windows.Win32.Media.DirectShow.IResourceConsumer, bStillWant: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelRequest(self, idResource: Int32, pConsumer: win32more.Windows.Win32.Media.DirectShow.IResourceConsumer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetFocus(self, pFocusObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ReleaseFocus(self, pFocusObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ISDBCAS_REQUEST_ID = Int32
ISDBCAS_REQUEST_ID_EMG: win32more.Windows.Win32.Media.DirectShow.ISDBCAS_REQUEST_ID = 56
ISDBCAS_REQUEST_ID_EMD: win32more.Windows.Win32.Media.DirectShow.ISDBCAS_REQUEST_ID = 58
class ISeekingPassThru(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36b73883-c2c8-11cf-8b46-00805f6cef60}')
    @commethod(3)
    def Init(self, bSupportRendering: win32more.Windows.Win32.Foundation.BOOL, pPin: win32more.Windows.Win32.Media.DirectShow.IPin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISelector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1abdaeca-68b6-4f83-9371-b413907c7b9f}')
    @commethod(3)
    def get_NumSources(self, pdwNumSources: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SourceNodeId(self, pdwPinId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_SourceNodeId(self, dwPinId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpecifyParticularPages(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4c437b91-6e9e-11d1-a704-006097c4e476}')
    @commethod(3)
    def GetPages(self, guidWhatPages: POINTER(Guid), pPages: POINTER(win32more.Windows.Win32.System.Ole.CAUUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStreamBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56a868bf-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(3)
    def Render(self, ppinOut: win32more.Windows.Win32.Media.DirectShow.IPin, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Backout(self, ppinOut: win32more.Windows.Win32.Media.DirectShow.IPin, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStreamSample(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b502d1be-9a57-11d0-8fde-00c04fd9189d}')
    @commethod(3)
    def GetMediaStream(self, ppMediaStream: POINTER(win32more.Windows.Win32.Media.DirectShow.IMediaStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSampleTimes(self, pStartTime: POINTER(Int64), pEndTime: POINTER(Int64), pCurrentTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSampleTimes(self, pStartTime: POINTER(Int64), pEndTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Update(self, dwFlags: UInt32, hEvent: win32more.Windows.Win32.Foundation.HANDLE, pfnAPC: win32more.Windows.Win32.Foundation.PAPCFUNC, dwAPCData: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CompletionStatus(self, dwFlags: UInt32, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRAspectRatioControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ede80b5c-bad6-4623-b537-65586c9f8dfd}')
    @commethod(3)
    def GetAspectRatioMode(self, lpdwARMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAspectRatioMode(self, dwARMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRAspectRatioControl9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00d96c29-bbde-4efc-9901-bb5036392146}')
    @commethod(3)
    def GetAspectRatioMode(self, lpdwARMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAspectRatioMode(self, dwARMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRDeinterlaceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb057577-0db8-4e6a-87a7-1a8c9a505a0f}')
    @commethod(3)
    def GetNumberOfDeinterlaceModes(self, lpVideoDescription: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRVideoDesc), lpdwNumDeinterlaceModes: POINTER(UInt32), lpDeinterlaceModes: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeinterlaceModeCaps(self, lpDeinterlaceMode: POINTER(Guid), lpVideoDescription: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRVideoDesc), lpDeinterlaceCaps: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceCaps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeinterlaceMode(self, dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDeinterlaceMode(self, dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeinterlacePrefs(self, lpdwDeinterlacePrefs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDeinterlacePrefs(self, dwDeinterlacePrefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetActualDeinterlaceMode(self, dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRDeinterlaceControl9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a215fb8d-13c2-4f7f-993c-003d6271a459}')
    @commethod(3)
    def GetNumberOfDeinterlaceModes(self, lpVideoDescription: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9VideoDesc), lpdwNumDeinterlaceModes: POINTER(UInt32), lpDeinterlaceModes: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeinterlaceModeCaps(self, lpDeinterlaceMode: POINTER(Guid), lpVideoDescription: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9VideoDesc), lpDeinterlaceCaps: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceCaps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeinterlaceMode(self, dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDeinterlaceMode(self, dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeinterlacePrefs(self, lpdwDeinterlacePrefs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDeinterlacePrefs(self, dwDeinterlacePrefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetActualDeinterlaceMode(self, dwStreamID: UInt32, lpDeinterlaceMode: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRFilterConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9e5530c5-7034-48b4-bb46-0b8a6efc8e36}')
    @commethod(3)
    def SetImageCompositor(self, lpVMRImgCompositor: win32more.Windows.Win32.Media.DirectShow.IVMRImageCompositor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNumberOfStreams(self, dwMaxStreams: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfStreams(self, pdwMaxStreams: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRenderingPrefs(self, dwRenderFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRenderingPrefs(self, pdwRenderFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetRenderingMode(self, Mode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRenderingMode(self, pMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRFilterConfig9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5a804648-4f66-4867-9c43-4f5c822cf1b8}')
    @commethod(3)
    def SetImageCompositor(self, lpVMRImgCompositor: win32more.Windows.Win32.Media.DirectShow.IVMRImageCompositor9) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetNumberOfStreams(self, dwMaxStreams: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfStreams(self, pdwMaxStreams: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRenderingPrefs(self, dwRenderFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRenderingPrefs(self, pdwRenderFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetRenderingMode(self, Mode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRenderingMode(self, pMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRImageCompositor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7a4fb5af-479f-4074-bb40-ce6722e43c82}')
    @commethod(3)
    def InitCompositionTarget(self, pD3DDevice: win32more.Windows.Win32.System.Com.IUnknown, pddsRenderTarget: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TermCompositionTarget(self, pD3DDevice: win32more.Windows.Win32.System.Com.IUnknown, pddsRenderTarget: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamMediaType(self, dwStrmID: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), fTexture: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CompositeImage(self, pD3DDevice: win32more.Windows.Win32.System.Com.IUnknown, pddsRenderTarget: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7, pmtRenderTarget: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), rtStart: Int64, rtEnd: Int64, dwClrBkGnd: UInt32, pVideoStreamInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRVIDEOSTREAMINFO), cStreams: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRImageCompositor9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4a5c89eb-df51-4654-ac2a-e48e02bbabf6}')
    @commethod(3)
    def InitCompositionDevice(self, pD3DDevice: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TermCompositionDevice(self, pD3DDevice: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamMediaType(self, dwStrmID: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), fTexture: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CompositeImage(self, pD3DDevice: win32more.Windows.Win32.System.Com.IUnknown, pddsRenderTarget: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9, pmtRenderTarget: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE), rtStart: Int64, rtEnd: Int64, dwClrBkGnd: UInt32, pVideoStreamInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9VideoStreamInfo), cStreams: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRImagePresenter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ce704fe7-e71e-41fb-baa2-c4403e1182f5}')
    @commethod(3)
    def StartPresenting(self, dwUserID: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopPresenting(self, dwUserID: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PresentImage(self, dwUserID: UIntPtr, lpPresInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRPRESENTATIONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRImagePresenter9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{69188c61-12a3-40f0-8ffc-342e7b433fd7}')
    @commethod(3)
    def StartPresenting(self, dwUserID: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopPresenting(self, dwUserID: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PresentImage(self, dwUserID: UIntPtr, lpPresInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9PresentationInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRImagePresenterConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f3a1c85-8555-49ba-935f-be5b5b29d178}')
    @commethod(3)
    def SetRenderingPrefs(self, dwRenderFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRenderingPrefs(self, dwRenderFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRImagePresenterConfig9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45c15cab-6e22-420a-8043-ae1f0ac02c7d}')
    @commethod(3)
    def SetRenderingPrefs(self, dwRenderFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRenderingPrefs(self, dwRenderFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRImagePresenterExclModeConfig(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IVMRImagePresenterConfig
    _iid_ = Guid('{e6f7ce40-4673-44f1-8f77-5499d68cb4ea}')
    @commethod(5)
    def SetXlcModeDDObjAndPrimarySurface(self, lpDDObj: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw7, lpPrimarySurf: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetXlcModeDDObjAndPrimarySurface(self, lpDDObj: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw7), lpPrimarySurf: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRMixerBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1e673275-0257-40aa-af20-7c608d4a0428}')
    @commethod(3)
    def SetAlphaBitmap(self, pBmpParms: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRALPHABITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAlphaBitmapParameters(self, pBmpParms: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRALPHABITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAlphaBitmapParameters(self, pBmpParms: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRALPHABITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRMixerBitmap9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ced175e5-1935-4820-81bd-ff6ad00c9108}')
    @commethod(3)
    def SetAlphaBitmap(self, pBmpParms: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAlphaBitmapParameters(self, pBmpParms: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAlphaBitmapParameters(self, pBmpParms: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRMixerControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1c1a17b0-bed0-415d-974b-dc6696131599}')
    @commethod(3)
    def SetAlpha(self, dwStreamID: UInt32, Alpha: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAlpha(self, dwStreamID: UInt32, pAlpha: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetZOrder(self, dwStreamID: UInt32, dwZ: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetZOrder(self, dwStreamID: UInt32, pZ: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetOutputRect(self, dwStreamID: UInt32, pRect: POINTER(win32more.Windows.Win32.Media.DirectShow.NORMALIZEDRECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputRect(self, dwStreamID: UInt32, pRect: POINTER(win32more.Windows.Win32.Media.DirectShow.NORMALIZEDRECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackgroundClr(self, ClrBkg: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackgroundClr(self, lpClrBkg: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMixingPrefs(self, dwMixerPrefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMixingPrefs(self, pdwMixerPrefs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRMixerControl9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a777eaa-47c8-4930-b2c9-8fee1c1b0f3b}')
    @commethod(3)
    def SetAlpha(self, dwStreamID: UInt32, Alpha: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAlpha(self, dwStreamID: UInt32, pAlpha: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetZOrder(self, dwStreamID: UInt32, dwZ: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetZOrder(self, dwStreamID: UInt32, pZ: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetOutputRect(self, dwStreamID: UInt32, pRect: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9NormalizedRect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputRect(self, dwStreamID: UInt32, pRect: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9NormalizedRect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackgroundClr(self, ClrBkg: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackgroundClr(self, lpClrBkg: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMixingPrefs(self, dwMixerPrefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMixingPrefs(self, pdwMixerPrefs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetProcAmpControl(self, dwStreamID: UInt32, lpClrControl: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControl)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetProcAmpControl(self, dwStreamID: UInt32, lpClrControl: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControl)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetProcAmpControlRange(self, dwStreamID: UInt32, lpClrControl: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControlRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRMonitorConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9cf0b1b6-fbaa-4b7f-88cf-cf1f130a0dce}')
    @commethod(3)
    def SetMonitor(self, pGUID: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMonitor(self, pGUID: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultMonitor(self, pGUID: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDefaultMonitor(self, pGUID: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAvailableMonitors(self, pInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRMONITORINFO), dwMaxInfoArraySize: UInt32, pdwNumDevices: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRMonitorConfig9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{46c2e457-8ba0-4eef-b80b-0680f0978749}')
    @commethod(3)
    def SetMonitor(self, uDev: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMonitor(self, puDev: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultMonitor(self, uDev: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDefaultMonitor(self, puDev: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAvailableMonitors(self, pInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9MonitorInfo), dwMaxInfoArraySize: UInt32, pdwNumDevices: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRSurface(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9849bbe-9ec8-4263-b764-62730f0d15d0}')
    @commethod(3)
    def IsSurfaceLocked(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockSurface(self, lpSurface: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UnlockSurface(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSurface(self, lplpSurface: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRSurface9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfc581a1-6e1f-4c3a-8d0a-5e9792ea2afc}')
    @commethod(3)
    def IsSurfaceLocked(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockSurface(self, lpSurface: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UnlockSurface(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSurface(self, lplpSurface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRSurfaceAllocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{31ce832e-4484-458b-8cca-f4d7e3db0b52}')
    @commethod(3)
    def AllocateSurface(self, dwUserID: UIntPtr, lpAllocInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMRALLOCATIONINFO), lpdwActualBuffers: POINTER(UInt32), lplpSurface: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FreeSurface(self, dwID: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareSurface(self, dwUserID: UIntPtr, lpSurface: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7, dwSurfaceFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AdviseNotify(self, lpIVMRSurfAllocNotify: win32more.Windows.Win32.Media.DirectShow.IVMRSurfaceAllocatorNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRSurfaceAllocator9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d5148ea-3f5d-46cf-9df1-d1b896eedb1f}')
    @commethod(3)
    def InitializeDevice(self, dwUserID: UIntPtr, lpAllocInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9AllocationInfo), lpNumBuffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TerminateDevice(self, dwID: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSurface(self, dwUserID: UIntPtr, SurfaceIndex: UInt32, SurfaceFlags: UInt32, lplpSurface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AdviseNotify(self, lpIVMRSurfAllocNotify: win32more.Windows.Win32.Media.DirectShow.IVMRSurfaceAllocatorNotify9) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRSurfaceAllocatorEx9(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IVMRSurfaceAllocator9
    _iid_ = Guid('{6de9a68a-a928-4522-bf57-655ae3866456}')
    @commethod(7)
    def GetSurfaceEx(self, dwUserID: UIntPtr, SurfaceIndex: UInt32, SurfaceFlags: UInt32, lplpSurface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9), lprcDst: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRSurfaceAllocatorNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aada05a8-5a4e-4729-af0b-cea27aed51e2}')
    @commethod(3)
    def AdviseSurfaceAllocator(self, dwUserID: UIntPtr, lpIVRMSurfaceAllocator: win32more.Windows.Win32.Media.DirectShow.IVMRSurfaceAllocator) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDDrawDevice(self, lpDDrawDevice: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw7, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChangeDDrawDevice(self, lpDDrawDevice: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDraw7, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RestoreDDrawSurfaces(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyEvent(self, EventCode: Int32, Param1: IntPtr, Param2: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetBorderColor(self, clrBorder: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRSurfaceAllocatorNotify9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dca3f5df-bb3a-4d03-bd81-84614bfbfa0c}')
    @commethod(3)
    def AdviseSurfaceAllocator(self, dwUserID: UIntPtr, lpIVRMSurfaceAllocator: win32more.Windows.Win32.Media.DirectShow.IVMRSurfaceAllocator9) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetD3DDevice(self, lpD3DDevice: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChangeD3DDevice(self, lpD3DDevice: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateSurfaceHelper(self, lpAllocInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.VMR9AllocationInfo), lpNumBuffers: POINTER(UInt32), lplpSurface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyEvent(self, EventCode: Int32, Param1: IntPtr, Param2: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRVideoStreamControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{058d1f11-2a54-4bef-bd54-df706626b727}')
    @commethod(3)
    def SetColorKey(self, lpClrKey: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDCOLORKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColorKey(self, lpClrKey: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDCOLORKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamActiveState(self, fActive: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamActiveState(self, lpfActive: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRVideoStreamControl9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0cfe38b-93e7-4772-8957-0400c49a4485}')
    @commethod(3)
    def SetStreamActiveState(self, fActive: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamActiveState(self, lpfActive: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRWindowlessControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0eb1088c-4dcd-46f0-878f-39dae86a51b7}')
    @commethod(3)
    def GetNativeVideoSize(self, lpWidth: POINTER(Int32), lpHeight: POINTER(Int32), lpARWidth: POINTER(Int32), lpARHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinIdealVideoSize(self, lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxIdealVideoSize(self, lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetVideoPosition(self, lpSRCRect: POINTER(win32more.Windows.Win32.Foundation.RECT), lpDSTRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetVideoPosition(self, lpSRCRect: POINTER(win32more.Windows.Win32.Foundation.RECT), lpDSTRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAspectRatioMode(self, lpAspectRatioMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAspectRatioMode(self, AspectRatioMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetVideoClippingWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RepaintVideo(self, hwnd: win32more.Windows.Win32.Foundation.HWND, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DisplayModeChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentImage(self, lpDib: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetBorderColor(self, Clr: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetBorderColor(self, lpClr: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetColorKey(self, Clr: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetColorKey(self, lpClr: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVMRWindowlessControl9(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8f537d09-f85e-4414-b23b-502e54c79927}')
    @commethod(3)
    def GetNativeVideoSize(self, lpWidth: POINTER(Int32), lpHeight: POINTER(Int32), lpARWidth: POINTER(Int32), lpARHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinIdealVideoSize(self, lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxIdealVideoSize(self, lpWidth: POINTER(Int32), lpHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetVideoPosition(self, lpSRCRect: POINTER(win32more.Windows.Win32.Foundation.RECT), lpDSTRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetVideoPosition(self, lpSRCRect: POINTER(win32more.Windows.Win32.Foundation.RECT), lpDSTRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAspectRatioMode(self, lpAspectRatioMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAspectRatioMode(self, AspectRatioMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetVideoClippingWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RepaintVideo(self, hwnd: win32more.Windows.Win32.Foundation.HWND, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DisplayModeChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentImage(self, lpDib: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetBorderColor(self, Clr: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetBorderColor(self, lpClr: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVPBaseConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetConnectInfo(self, pdwNumConnectInfo: POINTER(UInt32), pddVPConnectInfo: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDVIDEOPORTCONNECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetConnectInfo(self, dwChosenEntry: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVPDataInfo(self, pamvpDataInfo: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVPDATAINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxPixelRate(self, pamvpSize: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVPSIZE), pdwMaxPixelsPerSecond: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InformVPInputFormats(self, dwNumFormats: UInt32, pDDPixelFormats: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDPIXELFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVideoFormats(self, pdwNumFormats: POINTER(UInt32), pddPixelFormats: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDPIXELFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetVideoFormat(self, dwChosenEntry: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetInvertPolarity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOverlaySurface(self, ppddOverlaySurface: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDirectDrawKernelHandle(self, dwDDKernelHandle: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetVideoPortID(self, dwVideoPortID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetDDSurfaceKernelHandles(self, cHandles: UInt32, rgDDKernelHandles: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetSurfaceParameters(self, dwPitch: UInt32, dwXOrigin: UInt32, dwYOrigin: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVPBaseNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def RenegotiateVPParameters(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVPConfig(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IVPBaseConfig
    _iid_ = Guid('{bc29a660-30e3-11d0-9e69-00c04fd7c15b}')
    @commethod(16)
    def IsVPDecimationAllowed(self, pbIsDecimationAllowed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetScalingFactors(self, pamvpSize: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVPSIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVPManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aac18c18-e186-46d2-825d-a1f8dc8e395a}')
    @commethod(3)
    def SetVideoPortIndex(self, dwVideoPortIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVideoPortIndex(self, pdwVideoPortIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVPNotify(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IVPBaseNotify
    _iid_ = Guid('{c76794a1-d6c5-11d0-9e69-00c04fd7c15b}')
    @commethod(4)
    def SetDeinterlaceMode(self, mode: win32more.Windows.Win32.Media.DirectShow.AMVP_MODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDeinterlaceMode(self, pMode: POINTER(win32more.Windows.Win32.Media.DirectShow.AMVP_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVPNotify2(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IVPNotify
    _iid_ = Guid('{ebf47183-8764-11d1-9e69-00c04fd7c15b}')
    @commethod(6)
    def SetVPSyncMaster(self, bVPSyncMaster: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetVPSyncMaster(self, pbVPSyncMaster: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVPVBIConfig(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IVPBaseConfig
    _iid_ = Guid('{ec529b00-1a1f-11d1-bad9-00609744111a}')
class IVPVBINotify(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IVPBaseNotify
    _iid_ = Guid('{ec529b01-1a1f-11d1-bad9-00609744111a}')
class IVideoEncoder(ComPtr):
    extends: win32more.Windows.Win32.Media.DirectShow.IEncoderAPI
    _iid_ = Guid('{02997c3b-8e1b-460e-9270-545e0de9563e}')
class IVideoFrameStep(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e46a9787-2b71-444d-a4b5-1fab7b708d6a}')
    @commethod(3)
    def Step(self, dwFrames: UInt32, pStepObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CanStep(self, bMultiple: Int32, pStepObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelStep(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVideoProcAmp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4050560e-42a7-413a-85c2-09269a2d0f44}')
    @commethod(3)
    def get_BacklightCompensation(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_BacklightCompensation(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def getRange_BacklightCompensation(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Brightness(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_Brightness(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def getRange_Brightness(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ColorEnable(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ColorEnable(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def getRange_ColorEnable(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Contrast(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Contrast(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def getRange_Contrast(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Gamma(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Gamma(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def getRange_Gamma(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Saturation(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_Saturation(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def getRange_Saturation(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Sharpness(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Sharpness(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def getRange_Sharpness(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_WhiteBalance(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_WhiteBalance(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def getRange_WhiteBalance(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Gain(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Gain(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def getRange_Gain(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Hue(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Hue(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def getRange_Hue(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_DigitalMultiplier(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_DigitalMultiplier(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def getRange_DigitalMultiplier(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_PowerlineFrequency(self, pValue: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_PowerlineFrequency(self, Value: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def getRange_PowerlineFrequency(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_WhiteBalanceComponent(self, pValue1: POINTER(Int32), pValue2: POINTER(Int32), pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_WhiteBalanceComponent(self, Value1: Int32, Value2: Int32, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def getRange_WhiteBalanceComponent(self, pMin: POINTER(Int32), pMax: POINTER(Int32), pSteppingDelta: POINTER(Int32), pDefault: POINTER(Int32), pCapsFlag: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVideoWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{56a868b4-0ad4-11ce-b03a-0020af0ba770}')
    @commethod(7)
    def put_Caption(self, strCaption: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Caption(self, strCaption: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_WindowStyle(self, WindowStyle: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_WindowStyle(self, WindowStyle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_WindowStyleEx(self, WindowStyleEx: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_WindowStyleEx(self, WindowStyleEx: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_AutoShow(self, AutoShow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AutoShow(self, AutoShow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_WindowState(self, WindowState: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_WindowState(self, WindowState: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_BackgroundPalette(self, BackgroundPalette: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_BackgroundPalette(self, pBackgroundPalette: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_Visible(self, Visible: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Visible(self, pVisible: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Left(self, Left: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Left(self, pLeft: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Width(self, Width: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Width(self, pWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Top(self, Top: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Top(self, pTop: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_Height(self, Height: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Height(self, pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Owner(self, Owner: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Owner(self, Owner: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_MessageDrain(self, Drain: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_MessageDrain(self, Drain: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_BorderColor(self, Color: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_BorderColor(self, Color: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_FullScreenMode(self, FullScreenMode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_FullScreenMode(self, FullScreenMode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetWindowForeground(self, Focus: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def NotifyOwnerMessage(self, hwnd: IntPtr, uMsg: Int32, wParam: IntPtr, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetWindowPosition(self, Left: Int32, Top: Int32, Width: Int32, Height: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetWindowPosition(self, pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetMinIdealImageSize(self, pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetMaxIdealImageSize(self, pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetRestorePosition(self, pLeft: POINTER(Int32), pTop: POINTER(Int32), pWidth: POINTER(Int32), pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def HideCursor(self, HideCursor: win32more.Windows.Win32.Media.DirectShow.OA_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def IsCursorHidden(self, CursorHidden: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMCodecAMVideoAccelerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d98ee251-34e0-4a2d-9312-9b4c788d9fa1}')
    @commethod(3)
    def SetAcceleratorInterface(self, pIAMVA: win32more.Windows.Win32.Media.DirectShow.IAMVideoAccelerator) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NegotiateConnection(self, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPlayerNotify(self, pHook: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMPlayerTimestampHook) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMCodecVideoAccelerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{990641b0-739f-4e94-a808-9888da8f75af}')
    @commethod(3)
    def NegotiateConnection(self, pIAMVA: win32more.Windows.Win32.Media.DirectShow.IAMVideoAccelerator, pMediaType: POINTER(win32more.Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPlayerNotify(self, pHook: win32more.Windows.Win32.Media.WindowsMediaFormat.IWMPlayerTimestampHook) -> win32more.Windows.Win32.Foundation.HRESULT: ...
InterleavingMode = Int32
INTERLEAVE_NONE: win32more.Windows.Win32.Media.DirectShow.InterleavingMode = 0
INTERLEAVE_CAPTURE: win32more.Windows.Win32.Media.DirectShow.InterleavingMode = 1
INTERLEAVE_FULL: win32more.Windows.Win32.Media.DirectShow.InterleavingMode = 2
INTERLEAVE_NONE_BUFFERED: win32more.Windows.Win32.Media.DirectShow.InterleavingMode = 3
KSPROPERTY_IPSINK = Int32
KSPROPERTY_IPSINK_MULTICASTLIST: win32more.Windows.Win32.Media.DirectShow.KSPROPERTY_IPSINK = 0
KSPROPERTY_IPSINK_ADAPTER_DESCRIPTION: win32more.Windows.Win32.Media.DirectShow.KSPROPERTY_IPSINK = 1
KSPROPERTY_IPSINK_ADAPTER_ADDRESS: win32more.Windows.Win32.Media.DirectShow.KSPROPERTY_IPSINK = 2
class KS_BDA_FRAME_INFO(Structure):
    ExtendedHeaderSize: UInt32
    dwFrameFlags: UInt32
    ulEvent: UInt32
    ulChannelNumber: UInt32
    ulSubchannelNumber: UInt32
    ulReason: UInt32
LNB_Source = Int32
BDA_LNB_SOURCE_NOT_SET: win32more.Windows.Win32.Media.DirectShow.LNB_Source = -1
BDA_LNB_SOURCE_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.LNB_Source = 0
BDA_LNB_SOURCE_A: win32more.Windows.Win32.Media.DirectShow.LNB_Source = 1
BDA_LNB_SOURCE_B: win32more.Windows.Win32.Media.DirectShow.LNB_Source = 2
BDA_LNB_SOURCE_C: win32more.Windows.Win32.Media.DirectShow.LNB_Source = 3
BDA_LNB_SOURCE_D: win32more.Windows.Win32.Media.DirectShow.LNB_Source = 4
BDA_LNB_SOURCE_MAX: win32more.Windows.Win32.Media.DirectShow.LNB_Source = 5
LocationCodeSchemeType = Int32
SCTE_18: win32more.Windows.Win32.Media.DirectShow.LocationCodeSchemeType = 0
MEDIA_SAMPLE_CONTENT = Int32
MEDIA_TRANSPORT_PACKET: win32more.Windows.Win32.Media.DirectShow.MEDIA_SAMPLE_CONTENT = 0
MEDIA_ELEMENTARY_STREAM: win32more.Windows.Win32.Media.DirectShow.MEDIA_SAMPLE_CONTENT = 1
MEDIA_MPEG2_PSI: win32more.Windows.Win32.Media.DirectShow.MEDIA_SAMPLE_CONTENT = 2
MEDIA_TRANSPORT_PAYLOAD: win32more.Windows.Win32.Media.DirectShow.MEDIA_SAMPLE_CONTENT = 3
MMSSF_GET_INFORMATION_FLAGS = Int32
MMSSF_HASCLOCK: win32more.Windows.Win32.Media.DirectShow.MMSSF_GET_INFORMATION_FLAGS = 1
MMSSF_SUPPORTSEEK: win32more.Windows.Win32.Media.DirectShow.MMSSF_GET_INFORMATION_FLAGS = 2
MMSSF_ASYNCHRONOUS: win32more.Windows.Win32.Media.DirectShow.MMSSF_GET_INFORMATION_FLAGS = 4
class MPEG1WAVEFORMAT(Structure):
    wfx: win32more.Windows.Win32.Media.Audio.WAVEFORMATEX
    fwHeadLayer: UInt16
    dwHeadBitrate: UInt32
    fwHeadMode: UInt16
    fwHeadModeExt: UInt16
    wHeadEmphasis: UInt16
    fwHeadFlags: UInt16
    dwPTSLow: UInt32
    dwPTSHigh: UInt32
    _pack_ = 1
MPEG2StreamType = Int32
BDA_UNITIALIZED_MPEG2STREAMTYPE: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = -1
Reserved1: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 0
ISO_IEC_11172_2_VIDEO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 1
ISO_IEC_13818_2_VIDEO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 2
ISO_IEC_11172_3_AUDIO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 3
ISO_IEC_13818_3_AUDIO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 4
ISO_IEC_13818_1_PRIVATE_SECTION: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 5
ISO_IEC_13818_1_PES: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 6
ISO_IEC_13522_MHEG: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 7
ANNEX_A_DSM_CC: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 8
ITU_T_REC_H_222_1: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 9
ISO_IEC_13818_6_TYPE_A: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 10
ISO_IEC_13818_6_TYPE_B: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 11
ISO_IEC_13818_6_TYPE_C: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 12
ISO_IEC_13818_6_TYPE_D: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 13
ISO_IEC_13818_1_AUXILIARY: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 14
ISO_IEC_13818_7_AUDIO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 15
ISO_IEC_14496_2_VISUAL: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 16
ISO_IEC_14496_3_AUDIO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 17
ISO_IEC_14496_1_IN_PES: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 18
ISO_IEC_14496_1_IN_SECTION: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 19
ISO_IEC_13818_6_DOWNLOAD: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 20
METADATA_IN_PES: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 21
METADATA_IN_SECTION: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 22
METADATA_IN_DATA_CAROUSEL: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 23
METADATA_IN_OBJECT_CAROUSEL: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 24
METADATA_IN_DOWNLOAD_PROTOCOL: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 25
IRPM_STREAMM: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 26
ITU_T_H264: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 27
ISO_IEC_13818_1_RESERVED: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 28
USER_PRIVATE: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 16
HEVC_VIDEO_OR_TEMPORAL_VIDEO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 36
HEVC_TEMPORAL_VIDEO_SUBSET: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 37
ISO_IEC_USER_PRIVATE: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 128
DOLBY_AC3_AUDIO: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 129
DOLBY_DIGITAL_PLUS_AUDIO_ATSC: win32more.Windows.Win32.Media.DirectShow.MPEG2StreamType = 135
class MPEG2_TRANSPORT_STRIDE(Structure):
    dwOffset: UInt32
    dwPacketLength: UInt32
    dwStride: UInt32
class MPEGLAYER3WAVEFORMAT(Structure):
    wfx: win32more.Windows.Win32.Media.Audio.WAVEFORMATEX
    wID: UInt16
    fdwFlags: win32more.Windows.Win32.Media.DirectShow.MPEGLAYER3WAVEFORMAT_FLAGS
    nBlockSize: UInt16
    nFramesPerBlock: UInt16
    nCodecDelay: UInt16
    _pack_ = 1
MPEGLAYER3WAVEFORMAT_FLAGS = UInt32
MPEGLAYER3_FLAG_PADDING_ISO: win32more.Windows.Win32.Media.DirectShow.MPEGLAYER3WAVEFORMAT_FLAGS = 0
MPEGLAYER3_FLAG_PADDING_ON: win32more.Windows.Win32.Media.DirectShow.MPEGLAYER3WAVEFORMAT_FLAGS = 1
MPEGLAYER3_FLAG_PADDING_OFF: win32more.Windows.Win32.Media.DirectShow.MPEGLAYER3WAVEFORMAT_FLAGS = 2
MP_CURVE_TYPE = Int32
MP_CURVE_JUMP: win32more.Windows.Win32.Media.DirectShow.MP_CURVE_TYPE = 1
MP_CURVE_LINEAR: win32more.Windows.Win32.Media.DirectShow.MP_CURVE_TYPE = 2
MP_CURVE_SQUARE: win32more.Windows.Win32.Media.DirectShow.MP_CURVE_TYPE = 4
MP_CURVE_INVSQUARE: win32more.Windows.Win32.Media.DirectShow.MP_CURVE_TYPE = 8
MP_CURVE_SINE: win32more.Windows.Win32.Media.DirectShow.MP_CURVE_TYPE = 16
class MP_ENVELOPE_SEGMENT(Structure):
    rtStart: Int64
    rtEnd: Int64
    valStart: Single
    valEnd: Single
    iCurve: win32more.Windows.Win32.Media.DirectShow.MP_CURVE_TYPE
    flags: UInt32
class MP_PARAMINFO(Structure):
    mpType: win32more.Windows.Win32.Media.DirectShow.MP_TYPE
    mopCaps: UInt32
    mpdMinValue: Single
    mpdMaxValue: Single
    mpdNeutralValue: Single
    szUnitText: Char * 32
    szLabel: Char * 32
MP_TYPE = Int32
MPT_INT: win32more.Windows.Win32.Media.DirectShow.MP_TYPE = 0
MPT_FLOAT: win32more.Windows.Win32.Media.DirectShow.MP_TYPE = 1
MPT_BOOL: win32more.Windows.Win32.Media.DirectShow.MP_TYPE = 2
MPT_ENUM: win32more.Windows.Win32.Media.DirectShow.MP_TYPE = 3
MPT_MAX: win32more.Windows.Win32.Media.DirectShow.MP_TYPE = 4
MUX_PID_TYPE = Int32
PID_OTHER: win32more.Windows.Win32.Media.DirectShow.MUX_PID_TYPE = -1
PID_ELEMENTARY_STREAM: win32more.Windows.Win32.Media.DirectShow.MUX_PID_TYPE = 0
PID_MPEG2_SECTION_PSI_SI: win32more.Windows.Win32.Media.DirectShow.MUX_PID_TYPE = 1
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
BDA_MOD_NOT_SET: win32more.Windows.Win32.Media.DirectShow.ModulationType = -1
BDA_MOD_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.ModulationType = 0
BDA_MOD_16QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 1
BDA_MOD_32QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 2
BDA_MOD_64QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 3
BDA_MOD_80QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 4
BDA_MOD_96QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 5
BDA_MOD_112QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 6
BDA_MOD_128QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 7
BDA_MOD_160QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 8
BDA_MOD_192QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 9
BDA_MOD_224QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 10
BDA_MOD_256QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 11
BDA_MOD_320QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 12
BDA_MOD_384QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 13
BDA_MOD_448QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 14
BDA_MOD_512QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 15
BDA_MOD_640QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 16
BDA_MOD_768QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 17
BDA_MOD_896QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 18
BDA_MOD_1024QAM: win32more.Windows.Win32.Media.DirectShow.ModulationType = 19
BDA_MOD_QPSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 20
BDA_MOD_BPSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 21
BDA_MOD_OQPSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 22
BDA_MOD_8VSB: win32more.Windows.Win32.Media.DirectShow.ModulationType = 23
BDA_MOD_16VSB: win32more.Windows.Win32.Media.DirectShow.ModulationType = 24
BDA_MOD_ANALOG_AMPLITUDE: win32more.Windows.Win32.Media.DirectShow.ModulationType = 25
BDA_MOD_ANALOG_FREQUENCY: win32more.Windows.Win32.Media.DirectShow.ModulationType = 26
BDA_MOD_8PSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 27
BDA_MOD_RF: win32more.Windows.Win32.Media.DirectShow.ModulationType = 28
BDA_MOD_16APSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 29
BDA_MOD_32APSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 30
BDA_MOD_NBC_QPSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 31
BDA_MOD_NBC_8PSK: win32more.Windows.Win32.Media.DirectShow.ModulationType = 32
BDA_MOD_DIRECTV: win32more.Windows.Win32.Media.DirectShow.ModulationType = 33
BDA_MOD_ISDB_T_TMCC: win32more.Windows.Win32.Media.DirectShow.ModulationType = 34
BDA_MOD_ISDB_S_TMCC: win32more.Windows.Win32.Media.DirectShow.ModulationType = 35
BDA_MOD_MAX: win32more.Windows.Win32.Media.DirectShow.ModulationType = 36
class NORMALIZEDRECT(Structure):
    left: Single
    top: Single
    right: Single
    bottom: Single
OA_BOOL = Int32
OATRUE: win32more.Windows.Win32.Media.DirectShow.OA_BOOL = -1
OAFALSE: win32more.Windows.Win32.Media.DirectShow.OA_BOOL = 0
OUTPUT_STATE = Int32
Disabled: win32more.Windows.Win32.Media.DirectShow.OUTPUT_STATE = 0
ReadData: win32more.Windows.Win32.Media.DirectShow.OUTPUT_STATE = 1
RenderData: win32more.Windows.Win32.Media.DirectShow.OUTPUT_STATE = 2
@winfunctype_pointer
def PDXVA2SW_CREATEVIDEOPROCESSDEVICE(pD3DD9: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9, pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), RenderTargetFormat: win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT, MaxSubStreams: UInt32, phDevice: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_DESTROYVIDEOPROCESSDEVICE(hDevice: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETFILTERPROPERTYRANGE(pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), RenderTargetFormat: win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT, FilterSetting: UInt32, pRange: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETPROCAMPRANGE(pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), RenderTargetFormat: win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT, ProcAmpCap: UInt32, pRange: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORCAPS(pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), RenderTargetFormat: win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT, pCaps: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoProcessorCaps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETCOUNT(pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORRENDERTARGETS(pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), Count: UInt32, pFormats: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATCOUNT(pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), RenderTargetFormat: win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_GETVIDEOPROCESSORSUBSTREAMFORMATS(pVideoDesc: POINTER(win32more.Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc), RenderTargetFormat: win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT, Count: UInt32, pFormats: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSBEGINFRAME(hDevice: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSBLT(hDevice: win32more.Windows.Win32.Foundation.HANDLE, pBlt: POINTER(win32more.Windows.Win32.Media.DirectShow.DXVA2_VIDEOPROCESSBLT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSENDFRAME(hDevice: win32more.Windows.Win32.Foundation.HANDLE, pHandleComplete: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVA2SW_VIDEOPROCESSSETRENDERTARGET(hDevice: win32more.Windows.Win32.Foundation.HANDLE, pRenderTarget: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class PID_MAP(Structure):
    ulPID: UInt32
    MediaSampleContent: win32more.Windows.Win32.Media.DirectShow.MEDIA_SAMPLE_CONTENT
PIN_DIRECTION = Int32
PINDIR_INPUT: win32more.Windows.Win32.Media.DirectShow.PIN_DIRECTION = 0
PINDIR_OUTPUT: win32more.Windows.Win32.Media.DirectShow.PIN_DIRECTION = 1
class PIN_INFO(Structure):
    pFilter: win32more.Windows.Win32.Media.DirectShow.IBaseFilter
    dir: win32more.Windows.Win32.Media.DirectShow.PIN_DIRECTION
    achName: Char * 128
PhysicalConnectorType = Int32
PhysConn_Video_Tuner: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 1
PhysConn_Video_Composite: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 2
PhysConn_Video_SVideo: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 3
PhysConn_Video_RGB: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4
PhysConn_Video_YRYBY: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 5
PhysConn_Video_SerialDigital: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 6
PhysConn_Video_ParallelDigital: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 7
PhysConn_Video_SCSI: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 8
PhysConn_Video_AUX: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 9
PhysConn_Video_1394: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 10
PhysConn_Video_USB: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 11
PhysConn_Video_VideoDecoder: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 12
PhysConn_Video_VideoEncoder: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 13
PhysConn_Video_SCART: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 14
PhysConn_Video_Black: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 15
PhysConn_Audio_Tuner: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4096
PhysConn_Audio_Line: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4097
PhysConn_Audio_Mic: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4098
PhysConn_Audio_AESDigital: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4099
PhysConn_Audio_SPDIFDigital: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4100
PhysConn_Audio_SCSI: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4101
PhysConn_Audio_AUX: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4102
PhysConn_Audio_1394: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4103
PhysConn_Audio_USB: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4104
PhysConn_Audio_AudioDecoder: win32more.Windows.Win32.Media.DirectShow.PhysicalConnectorType = 4105
Pilot = Int32
BDA_PILOT_NOT_SET: win32more.Windows.Win32.Media.DirectShow.Pilot = -1
BDA_PILOT_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.Pilot = 0
BDA_PILOT_OFF: win32more.Windows.Win32.Media.DirectShow.Pilot = 1
BDA_PILOT_ON: win32more.Windows.Win32.Media.DirectShow.Pilot = 2
BDA_PILOT_MAX: win32more.Windows.Win32.Media.DirectShow.Pilot = 3
Polarisation = Int32
BDA_POLARISATION_NOT_SET: win32more.Windows.Win32.Media.DirectShow.Polarisation = -1
BDA_POLARISATION_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.Polarisation = 0
BDA_POLARISATION_LINEAR_H: win32more.Windows.Win32.Media.DirectShow.Polarisation = 1
BDA_POLARISATION_LINEAR_V: win32more.Windows.Win32.Media.DirectShow.Polarisation = 2
BDA_POLARISATION_CIRCULAR_L: win32more.Windows.Win32.Media.DirectShow.Polarisation = 3
BDA_POLARISATION_CIRCULAR_R: win32more.Windows.Win32.Media.DirectShow.Polarisation = 4
BDA_POLARISATION_MAX: win32more.Windows.Win32.Media.DirectShow.Polarisation = 5
class Quality(Structure):
    Type: win32more.Windows.Win32.Media.DirectShow.QualityMessageType
    Proportion: Int32
    Late: Int64
    TimeStamp: Int64
QualityMessageType = Int32
Famine: win32more.Windows.Win32.Media.DirectShow.QualityMessageType = 0
Flood: win32more.Windows.Win32.Media.DirectShow.QualityMessageType = 1
class REGFILTER(Structure):
    Clsid: Guid
    Name: win32more.Windows.Win32.Foundation.PWSTR
class REGFILTER2(Structure):
    dwVersion: UInt32
    dwMerit: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            cPins: UInt32
            rgPins: POINTER(win32more.Windows.Win32.Media.DirectShow.REGFILTERPINS)
        class _Anonymous2_e__Struct(Structure):
            cPins2: UInt32
            rgPins2: POINTER(win32more.Windows.Win32.Media.DirectShow.REGFILTERPINS2)
class REGFILTERPINS(Structure):
    strName: win32more.Windows.Win32.Foundation.PWSTR
    bRendered: win32more.Windows.Win32.Foundation.BOOL
    bOutput: win32more.Windows.Win32.Foundation.BOOL
    bZero: win32more.Windows.Win32.Foundation.BOOL
    bMany: win32more.Windows.Win32.Foundation.BOOL
    clsConnectsToFilter: POINTER(Guid)
    strConnectsToPin: win32more.Windows.Win32.Foundation.PWSTR
    nMediaTypes: UInt32
    lpMediaType: POINTER(win32more.Windows.Win32.Media.DirectShow.REGPINTYPES)
class REGFILTERPINS2(Structure):
    dwFlags: UInt32
    cInstances: UInt32
    nMediaTypes: UInt32
    lpMediaType: POINTER(win32more.Windows.Win32.Media.DirectShow.REGPINTYPES)
    nMediums: UInt32
    lpMedium: POINTER(win32more.Windows.Win32.Media.DirectShow.REGPINMEDIUM)
    clsPinCategory: POINTER(Guid)
class REGPINMEDIUM(Structure):
    clsMedium: Guid
    dw1: UInt32
    dw2: UInt32
class REGPINTYPES(Structure):
    clsMajorType: POINTER(Guid)
    clsMinorType: POINTER(Guid)
REG_PINFLAG = Int32
REG_PINFLAG_B_ZERO: win32more.Windows.Win32.Media.DirectShow.REG_PINFLAG = 1
REG_PINFLAG_B_RENDERER: win32more.Windows.Win32.Media.DirectShow.REG_PINFLAG = 2
REG_PINFLAG_B_MANY: win32more.Windows.Win32.Media.DirectShow.REG_PINFLAG = 4
REG_PINFLAG_B_OUTPUT: win32more.Windows.Win32.Media.DirectShow.REG_PINFLAG = 8
class RIFFCHUNK(Structure):
    fcc: UInt32
    cb: UInt32
    _pack_ = 2
class RIFFLIST(Structure):
    fcc: UInt32
    cb: UInt32
    fccListType: UInt32
    _pack_ = 2
RollOff = Int32
BDA_ROLL_OFF_NOT_SET: win32more.Windows.Win32.Media.DirectShow.RollOff = -1
BDA_ROLL_OFF_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.RollOff = 0
BDA_ROLL_OFF_20: win32more.Windows.Win32.Media.DirectShow.RollOff = 1
BDA_ROLL_OFF_25: win32more.Windows.Win32.Media.DirectShow.RollOff = 2
BDA_ROLL_OFF_35: win32more.Windows.Win32.Media.DirectShow.RollOff = 3
BDA_ROLL_OFF_MAX: win32more.Windows.Win32.Media.DirectShow.RollOff = 4
SNDDEV_ERR = Int32
SNDDEV_ERROR_Open: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 1
SNDDEV_ERROR_Close: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 2
SNDDEV_ERROR_GetCaps: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 3
SNDDEV_ERROR_PrepareHeader: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 4
SNDDEV_ERROR_UnprepareHeader: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 5
SNDDEV_ERROR_Reset: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 6
SNDDEV_ERROR_Restart: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 7
SNDDEV_ERROR_GetPosition: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 8
SNDDEV_ERROR_Write: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 9
SNDDEV_ERROR_Pause: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 10
SNDDEV_ERROR_Stop: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 11
SNDDEV_ERROR_Start: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 12
SNDDEV_ERROR_AddBuffer: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 13
SNDDEV_ERROR_Query: win32more.Windows.Win32.Media.DirectShow.SNDDEV_ERR = 14
SSUPDATE_TYPE = Int32
SSUPDATE_ASYNC: win32more.Windows.Win32.Media.DirectShow.SSUPDATE_TYPE = 1
SSUPDATE_CONTINUOUS: win32more.Windows.Win32.Media.DirectShow.SSUPDATE_TYPE = 2
STREAMIF_CONSTANTS = Int32
MAX_NUMBER_OF_STREAMS: win32more.Windows.Win32.Media.DirectShow.STREAMIF_CONSTANTS = 16
class STREAM_ID_MAP(Structure):
    stream_id: UInt32
    dwMediaSampleContent: UInt32
    ulSubstreamFilterValue: UInt32
    iDataOffset: Int32
STREAM_STATE = Int32
STREAMSTATE_STOP: win32more.Windows.Win32.Media.DirectShow.STREAM_STATE = 0
STREAMSTATE_RUN: win32more.Windows.Win32.Media.DirectShow.STREAM_STATE = 1
STREAM_TYPE = Int32
STREAMTYPE_READ: win32more.Windows.Win32.Media.DirectShow.STREAM_TYPE = 0
STREAMTYPE_WRITE: win32more.Windows.Win32.Media.DirectShow.STREAM_TYPE = 1
STREAMTYPE_TRANSFORM: win32more.Windows.Win32.Media.DirectShow.STREAM_TYPE = 2
ScanModulationTypes = Int32
BDA_SCAN_MOD_16QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 1
BDA_SCAN_MOD_32QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 2
BDA_SCAN_MOD_64QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 4
BDA_SCAN_MOD_80QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 8
BDA_SCAN_MOD_96QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 16
BDA_SCAN_MOD_112QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 32
BDA_SCAN_MOD_128QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 64
BDA_SCAN_MOD_160QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 128
BDA_SCAN_MOD_192QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 256
BDA_SCAN_MOD_224QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 512
BDA_SCAN_MOD_256QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 1024
BDA_SCAN_MOD_320QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 2048
BDA_SCAN_MOD_384QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 4096
BDA_SCAN_MOD_448QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 8192
BDA_SCAN_MOD_512QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 16384
BDA_SCAN_MOD_640QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 32768
BDA_SCAN_MOD_768QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 65536
BDA_SCAN_MOD_896QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 131072
BDA_SCAN_MOD_1024QAM: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 262144
BDA_SCAN_MOD_QPSK: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 524288
BDA_SCAN_MOD_BPSK: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 1048576
BDA_SCAN_MOD_OQPSK: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 2097152
BDA_SCAN_MOD_8VSB: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 4194304
BDA_SCAN_MOD_16VSB: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 8388608
BDA_SCAN_MOD_AM_RADIO: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 16777216
BDA_SCAN_MOD_FM_RADIO: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 33554432
BDA_SCAN_MOD_8PSK: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 67108864
BDA_SCAN_MOD_RF: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 134217728
ScanModulationTypesMask_MCE_DigitalCable: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 11
ScanModulationTypesMask_MCE_TerrestrialATSC: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 23
ScanModulationTypesMask_MCE_AnalogTv: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 28
ScanModulationTypesMask_MCE_All_TV: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = -1
ScanModulationTypesMask_DVBC: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 75
BDA_SCAN_MOD_16APSK: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 268435456
BDA_SCAN_MOD_32APSK: win32more.Windows.Win32.Media.DirectShow.ScanModulationTypes = 536870912
class SmartCardApplication(Structure):
    ApplicationType: win32more.Windows.Win32.Media.DirectShow.ApplicationTypeType
    ApplicationVersion: UInt16
    pbstrApplicationName: win32more.Windows.Win32.Foundation.BSTR
    pbstrApplicationURL: win32more.Windows.Win32.Foundation.BSTR
SmartCardAssociationType = Int32
NotAssociated: win32more.Windows.Win32.Media.DirectShow.SmartCardAssociationType = 0
Associated: win32more.Windows.Win32.Media.DirectShow.SmartCardAssociationType = 1
AssociationUnknown: win32more.Windows.Win32.Media.DirectShow.SmartCardAssociationType = 2
SmartCardStatusType = Int32
CardInserted: win32more.Windows.Win32.Media.DirectShow.SmartCardStatusType = 0
CardRemoved: win32more.Windows.Win32.Media.DirectShow.SmartCardStatusType = 1
CardError: win32more.Windows.Win32.Media.DirectShow.SmartCardStatusType = 2
CardDataChanged: win32more.Windows.Win32.Media.DirectShow.SmartCardStatusType = 3
CardFirmwareUpgrade: win32more.Windows.Win32.Media.DirectShow.SmartCardStatusType = 4
SpectralInversion = Int32
BDA_SPECTRAL_INVERSION_NOT_SET: win32more.Windows.Win32.Media.DirectShow.SpectralInversion = -1
BDA_SPECTRAL_INVERSION_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.SpectralInversion = 0
BDA_SPECTRAL_INVERSION_AUTOMATIC: win32more.Windows.Win32.Media.DirectShow.SpectralInversion = 1
BDA_SPECTRAL_INVERSION_NORMAL: win32more.Windows.Win32.Media.DirectShow.SpectralInversion = 2
BDA_SPECTRAL_INVERSION_INVERTED: win32more.Windows.Win32.Media.DirectShow.SpectralInversion = 3
BDA_SPECTRAL_INVERSION_MAX: win32more.Windows.Win32.Media.DirectShow.SpectralInversion = 4
class TIMECODEDATA(Structure):
    time: win32more.Windows.Win32.Media.TIMECODE
    dwSMPTEflags: UInt32
    dwUser: UInt32
    _pack_ = 2
class TRUECOLORINFO(Structure):
    dwBitMasks: UInt32 * 3
    bmiColors: win32more.Windows.Win32.Graphics.Gdi.RGBQUAD * 256
TVAudioMode = Int32
AMTVAUDIO_MODE_MONO: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 1
AMTVAUDIO_MODE_STEREO: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 2
AMTVAUDIO_MODE_LANG_A: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 16
AMTVAUDIO_MODE_LANG_B: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 32
AMTVAUDIO_MODE_LANG_C: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 64
AMTVAUDIO_PRESET_STEREO: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 512
AMTVAUDIO_PRESET_LANG_A: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 4096
AMTVAUDIO_PRESET_LANG_B: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 8192
AMTVAUDIO_PRESET_LANG_C: win32more.Windows.Win32.Media.DirectShow.TVAudioMode = 16384
TransmissionMode = Int32
BDA_XMIT_MODE_NOT_SET: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = -1
BDA_XMIT_MODE_NOT_DEFINED: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 0
BDA_XMIT_MODE_2K: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 1
BDA_XMIT_MODE_8K: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 2
BDA_XMIT_MODE_4K: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 3
BDA_XMIT_MODE_2K_INTERLEAVED: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 4
BDA_XMIT_MODE_4K_INTERLEAVED: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 5
BDA_XMIT_MODE_1K: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 6
BDA_XMIT_MODE_16K: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 7
BDA_XMIT_MODE_32K: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 8
BDA_XMIT_MODE_MAX: win32more.Windows.Win32.Media.DirectShow.TransmissionMode = 9
TunerInputType = Int32
TunerInputCable: win32more.Windows.Win32.Media.DirectShow.TunerInputType = 0
TunerInputAntenna: win32more.Windows.Win32.Media.DirectShow.TunerInputType = 1
UICloseReasonType = Int32
NotReady: win32more.Windows.Win32.Media.DirectShow.UICloseReasonType = 0
UserClosed: win32more.Windows.Win32.Media.DirectShow.UICloseReasonType = 1
SystemClosed: win32more.Windows.Win32.Media.DirectShow.UICloseReasonType = 2
DeviceClosed: win32more.Windows.Win32.Media.DirectShow.UICloseReasonType = 3
ErrorClosed: win32more.Windows.Win32.Media.DirectShow.UICloseReasonType = 4
VALID_UOP_FLAG = Int32
UOP_FLAG_Play_Title_Or_AtTime: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 1
UOP_FLAG_Play_Chapter: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 2
UOP_FLAG_Play_Title: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 4
UOP_FLAG_Stop: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 8
UOP_FLAG_ReturnFromSubMenu: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 16
UOP_FLAG_Play_Chapter_Or_AtTime: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 32
UOP_FLAG_PlayPrev_Or_Replay_Chapter: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 64
UOP_FLAG_PlayNext_Chapter: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 128
UOP_FLAG_Play_Forwards: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 256
UOP_FLAG_Play_Backwards: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 512
UOP_FLAG_ShowMenu_Title: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 1024
UOP_FLAG_ShowMenu_Root: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 2048
UOP_FLAG_ShowMenu_SubPic: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 4096
UOP_FLAG_ShowMenu_Audio: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 8192
UOP_FLAG_ShowMenu_Angle: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 16384
UOP_FLAG_ShowMenu_Chapter: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 32768
UOP_FLAG_Resume: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 65536
UOP_FLAG_Select_Or_Activate_Button: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 131072
UOP_FLAG_Still_Off: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 262144
UOP_FLAG_Pause_On: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 524288
UOP_FLAG_Select_Audio_Stream: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 1048576
UOP_FLAG_Select_SubPic_Stream: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 2097152
UOP_FLAG_Select_Angle: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 4194304
UOP_FLAG_Select_Karaoke_Audio_Presentation_Mode: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 8388608
UOP_FLAG_Select_Video_Mode_Preference: win32more.Windows.Win32.Media.DirectShow.VALID_UOP_FLAG = 16777216
class VFW_FILTERLIST(Structure):
    cFilters: UInt32
    aClsId: Guid * 1
VIDEOENCODER_BITRATE_MODE = Int32
ConstantBitRate: win32more.Windows.Win32.Media.DirectShow.VIDEOENCODER_BITRATE_MODE = 0
VariableBitRateAverage: win32more.Windows.Win32.Media.DirectShow.VIDEOENCODER_BITRATE_MODE = 1
VariableBitRatePeak: win32more.Windows.Win32.Media.DirectShow.VIDEOENCODER_BITRATE_MODE = 2
class VIDEOINFO(Structure):
    rcSource: win32more.Windows.Win32.Foundation.RECT
    rcTarget: win32more.Windows.Win32.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    bmiHeader: win32more.Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        bmiColors: win32more.Windows.Win32.Graphics.Gdi.RGBQUAD * 256
        dwBitMasks: UInt32 * 3
        TrueColorInfo: win32more.Windows.Win32.Media.DirectShow.TRUECOLORINFO
class VIDEO_STREAM_CONFIG_CAPS(Structure):
    guid: Guid
    VideoStandard: UInt32
    InputSize: win32more.Windows.Win32.Foundation.SIZE
    MinCroppingSize: win32more.Windows.Win32.Foundation.SIZE
    MaxCroppingSize: win32more.Windows.Win32.Foundation.SIZE
    CropGranularityX: Int32
    CropGranularityY: Int32
    CropAlignX: Int32
    CropAlignY: Int32
    MinOutputSize: win32more.Windows.Win32.Foundation.SIZE
    MaxOutputSize: win32more.Windows.Win32.Foundation.SIZE
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
    Format: win32more.Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    Pool: win32more.Windows.Win32.Graphics.Direct3D9.D3DPOOL
    MinBuffers: UInt32
    szAspectRatio: win32more.Windows.Win32.Foundation.SIZE
    szNativeSize: win32more.Windows.Win32.Foundation.SIZE
class VMR9AlphaBitmap(Structure):
    dwFlags: UInt32
    hdc: win32more.Windows.Win32.Graphics.Gdi.HDC
    pDDS: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9
    rSrc: win32more.Windows.Win32.Foundation.RECT
    rDest: win32more.Windows.Win32.Media.DirectShow.VMR9NormalizedRect
    fAlpha: Single
    clrSrcKey: win32more.Windows.Win32.Foundation.COLORREF
    dwFilterMode: UInt32
VMR9AlphaBitmapFlags = Int32
VMR9AlphaBitmap_Disable: win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmapFlags = 1
VMR9AlphaBitmap_hDC: win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmapFlags = 2
VMR9AlphaBitmap_EntireDDS: win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmapFlags = 4
VMR9AlphaBitmap_SrcColorKey: win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmapFlags = 8
VMR9AlphaBitmap_SrcRect: win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmapFlags = 16
VMR9AlphaBitmap_FilterMode: win32more.Windows.Win32.Media.DirectShow.VMR9AlphaBitmapFlags = 32
VMR9AspectRatioMode = Int32
VMR9ARMode_None: win32more.Windows.Win32.Media.DirectShow.VMR9AspectRatioMode = 0
VMR9ARMode_LetterBox: win32more.Windows.Win32.Media.DirectShow.VMR9AspectRatioMode = 1
class VMR9DeinterlaceCaps(Structure):
    dwSize: UInt32
    dwNumPreviousOutputFrames: UInt32
    dwNumForwardRefSamples: UInt32
    dwNumBackwardRefSamples: UInt32
    DeinterlaceTechnology: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech
VMR9DeinterlacePrefs = Int32
DeinterlacePref9_NextBest: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlacePrefs = 1
DeinterlacePref9_BOB: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlacePrefs = 2
DeinterlacePref9_Weave: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlacePrefs = 4
DeinterlacePref9_Mask: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlacePrefs = 7
VMR9DeinterlaceTech = Int32
DeinterlaceTech9_Unknown: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 0
DeinterlaceTech9_BOBLineReplicate: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 1
DeinterlaceTech9_BOBVerticalStretch: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 2
DeinterlaceTech9_MedianFiltering: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 4
DeinterlaceTech9_EdgeFiltering: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 16
DeinterlaceTech9_FieldAdaptive: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 32
DeinterlaceTech9_PixelAdaptive: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 64
DeinterlaceTech9_MotionVectorSteered: win32more.Windows.Win32.Media.DirectShow.VMR9DeinterlaceTech = 128
class VMR9Frequency(Structure):
    dwNumerator: UInt32
    dwDenominator: UInt32
VMR9MixerPrefs = Int32
MixerPref9_NoDecimation: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 1
MixerPref9_DecimateOutput: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 2
MixerPref9_ARAdjustXorY: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 4
MixerPref9_NonSquareMixing: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 8
MixerPref9_DecimateMask: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 15
MixerPref9_BiLinearFiltering: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 16
MixerPref9_PointFiltering: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 32
MixerPref9_AnisotropicFiltering: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 64
MixerPref9_PyramidalQuadFiltering: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 128
MixerPref9_GaussianQuadFiltering: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 256
MixerPref9_FilteringReserved: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 3584
MixerPref9_FilteringMask: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 4080
MixerPref9_RenderTargetRGB: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 4096
MixerPref9_RenderTargetYUV: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 8192
MixerPref9_RenderTargetReserved: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 1032192
MixerPref9_RenderTargetMask: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 1044480
MixerPref9_DynamicSwitchToBOB: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 1048576
MixerPref9_DynamicDecimateBy2: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 2097152
MixerPref9_DynamicReserved: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 12582912
MixerPref9_DynamicMask: win32more.Windows.Win32.Media.DirectShow.VMR9MixerPrefs = 15728640
VMR9Mode = Int32
VMR9Mode_Windowed: win32more.Windows.Win32.Media.DirectShow.VMR9Mode = 1
VMR9Mode_Windowless: win32more.Windows.Win32.Media.DirectShow.VMR9Mode = 2
VMR9Mode_Renderless: win32more.Windows.Win32.Media.DirectShow.VMR9Mode = 4
VMR9Mode_Mask: win32more.Windows.Win32.Media.DirectShow.VMR9Mode = 7
class VMR9MonitorInfo(Structure):
    uDevID: UInt32
    rcMonitor: win32more.Windows.Win32.Foundation.RECT
    hMon: win32more.Windows.Win32.Graphics.Gdi.HMONITOR
    dwFlags: UInt32
    szDevice: Char * 32
    szDescription: Char * 512
    liDriverVersion: Int64
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
VMR9Sample_SyncPoint: win32more.Windows.Win32.Media.DirectShow.VMR9PresentationFlags = 1
VMR9Sample_Preroll: win32more.Windows.Win32.Media.DirectShow.VMR9PresentationFlags = 2
VMR9Sample_Discontinuity: win32more.Windows.Win32.Media.DirectShow.VMR9PresentationFlags = 4
VMR9Sample_TimeValid: win32more.Windows.Win32.Media.DirectShow.VMR9PresentationFlags = 8
VMR9Sample_SrcDstRectsValid: win32more.Windows.Win32.Media.DirectShow.VMR9PresentationFlags = 16
class VMR9PresentationInfo(Structure):
    dwFlags: UInt32
    lpSurf: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9
    rtStart: Int64
    rtEnd: Int64
    szAspectRatio: win32more.Windows.Win32.Foundation.SIZE
    rcSrc: win32more.Windows.Win32.Foundation.RECT
    rcDst: win32more.Windows.Win32.Foundation.RECT
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
ProcAmpControl9_Brightness: win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControlFlags = 1
ProcAmpControl9_Contrast: win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControlFlags = 2
ProcAmpControl9_Hue: win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControlFlags = 4
ProcAmpControl9_Saturation: win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControlFlags = 8
ProcAmpControl9_Mask: win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControlFlags = 15
class VMR9ProcAmpControlRange(Structure):
    dwSize: UInt32
    dwProperty: win32more.Windows.Win32.Media.DirectShow.VMR9ProcAmpControlFlags
    MinValue: Single
    MaxValue: Single
    DefaultValue: Single
    StepSize: Single
VMR9RenderPrefs = Int32
RenderPrefs9_DoNotRenderBorder: win32more.Windows.Win32.Media.DirectShow.VMR9RenderPrefs = 1
RenderPrefs9_Mask: win32more.Windows.Win32.Media.DirectShow.VMR9RenderPrefs = 1
VMR9SurfaceAllocationFlags = Int32
VMR9AllocFlag_3DRenderTarget: win32more.Windows.Win32.Media.DirectShow.VMR9SurfaceAllocationFlags = 1
VMR9AllocFlag_DXVATarget: win32more.Windows.Win32.Media.DirectShow.VMR9SurfaceAllocationFlags = 2
VMR9AllocFlag_TextureSurface: win32more.Windows.Win32.Media.DirectShow.VMR9SurfaceAllocationFlags = 4
VMR9AllocFlag_OffscreenSurface: win32more.Windows.Win32.Media.DirectShow.VMR9SurfaceAllocationFlags = 8
VMR9AllocFlag_RGBDynamicSwitch: win32more.Windows.Win32.Media.DirectShow.VMR9SurfaceAllocationFlags = 16
VMR9AllocFlag_UsageReserved: win32more.Windows.Win32.Media.DirectShow.VMR9SurfaceAllocationFlags = 224
VMR9AllocFlag_UsageMask: win32more.Windows.Win32.Media.DirectShow.VMR9SurfaceAllocationFlags = 255
class VMR9VideoDesc(Structure):
    dwSize: UInt32
    dwSampleWidth: UInt32
    dwSampleHeight: UInt32
    SampleFormat: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat
    dwFourCC: UInt32
    InputSampleFreq: win32more.Windows.Win32.Media.DirectShow.VMR9Frequency
    OutputFrameFreq: win32more.Windows.Win32.Media.DirectShow.VMR9Frequency
class VMR9VideoStreamInfo(Structure):
    pddsVideoSurface: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9
    dwWidth: UInt32
    dwHeight: UInt32
    dwStrmID: UInt32
    fAlpha: Single
    rNormal: win32more.Windows.Win32.Media.DirectShow.VMR9NormalizedRect
    rtStart: Int64
    rtEnd: Int64
    SampleFormat: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat
VMR9_SampleFormat = Int32
VMR9_SampleReserved: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat = 1
VMR9_SampleProgressiveFrame: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat = 2
VMR9_SampleFieldInterleavedEvenFirst: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat = 3
VMR9_SampleFieldInterleavedOddFirst: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat = 4
VMR9_SampleFieldSingleEven: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat = 5
VMR9_SampleFieldSingleOdd: win32more.Windows.Win32.Media.DirectShow.VMR9_SampleFormat = 6
class VMRALLOCATIONINFO(Structure):
    dwFlags: UInt32
    lpHdr: POINTER(win32more.Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER)
    lpPixFmt: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.DDPIXELFORMAT)
    szAspectRatio: win32more.Windows.Win32.Foundation.SIZE
    dwMinBuffers: UInt32
    dwMaxBuffers: UInt32
    dwInterlaceFlags: UInt32
    szNativeSize: win32more.Windows.Win32.Foundation.SIZE
class VMRALPHABITMAP(Structure):
    dwFlags: UInt32
    hdc: win32more.Windows.Win32.Graphics.Gdi.HDC
    pDDS: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7
    rSrc: win32more.Windows.Win32.Foundation.RECT
    rDest: win32more.Windows.Win32.Media.DirectShow.NORMALIZEDRECT
    fAlpha: Single
    clrSrcKey: win32more.Windows.Win32.Foundation.COLORREF
class VMRDeinterlaceCaps(Structure):
    dwSize: UInt32
    dwNumPreviousOutputFrames: UInt32
    dwNumForwardRefSamples: UInt32
    dwNumBackwardRefSamples: UInt32
    DeinterlaceTechnology: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech
VMRDeinterlacePrefs = Int32
DeinterlacePref_NextBest: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlacePrefs = 1
DeinterlacePref_BOB: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlacePrefs = 2
DeinterlacePref_Weave: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlacePrefs = 4
DeinterlacePref_Mask: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlacePrefs = 7
VMRDeinterlaceTech = Int32
DeinterlaceTech_Unknown: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 0
DeinterlaceTech_BOBLineReplicate: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 1
DeinterlaceTech_BOBVerticalStretch: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 2
DeinterlaceTech_MedianFiltering: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 4
DeinterlaceTech_EdgeFiltering: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 16
DeinterlaceTech_FieldAdaptive: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 32
DeinterlaceTech_PixelAdaptive: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 64
DeinterlaceTech_MotionVectorSteered: win32more.Windows.Win32.Media.DirectShow.VMRDeinterlaceTech = 128
class VMRFrequency(Structure):
    dwNumerator: UInt32
    dwDenominator: UInt32
class VMRGUID(Structure):
    pGUID: POINTER(Guid)
    GUID: Guid
class VMRMONITORINFO(Structure):
    guid: win32more.Windows.Win32.Media.DirectShow.VMRGUID
    rcMonitor: win32more.Windows.Win32.Foundation.RECT
    hMon: win32more.Windows.Win32.Graphics.Gdi.HMONITOR
    dwFlags: UInt32
    szDevice: Char * 32
    szDescription: Char * 256
    liDriverVersion: Int64
    dwVendorId: UInt32
    dwDeviceId: UInt32
    dwSubSysId: UInt32
    dwRevision: UInt32
VMRMixerPrefs = Int32
MixerPref_NoDecimation: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 1
MixerPref_DecimateOutput: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 2
MixerPref_ARAdjustXorY: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 4
MixerPref_DecimationReserved: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 8
MixerPref_DecimateMask: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 15
MixerPref_BiLinearFiltering: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 16
MixerPref_PointFiltering: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 32
MixerPref_FilteringMask: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 240
MixerPref_RenderTargetRGB: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 256
MixerPref_RenderTargetYUV: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 4096
MixerPref_RenderTargetYUV420: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 512
MixerPref_RenderTargetYUV422: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 1024
MixerPref_RenderTargetYUV444: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 2048
MixerPref_RenderTargetReserved: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 57344
MixerPref_RenderTargetMask: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 65280
MixerPref_DynamicSwitchToBOB: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 65536
MixerPref_DynamicDecimateBy2: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 131072
MixerPref_DynamicReserved: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 786432
MixerPref_DynamicMask: win32more.Windows.Win32.Media.DirectShow.VMRMixerPrefs = 983040
VMRMode = Int32
VMRMode_Windowed: win32more.Windows.Win32.Media.DirectShow.VMRMode = 1
VMRMode_Windowless: win32more.Windows.Win32.Media.DirectShow.VMRMode = 2
VMRMode_Renderless: win32more.Windows.Win32.Media.DirectShow.VMRMode = 4
VMRMode_Mask: win32more.Windows.Win32.Media.DirectShow.VMRMode = 7
class VMRPRESENTATIONINFO(Structure):
    dwFlags: UInt32
    lpSurf: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7
    rtStart: Int64
    rtEnd: Int64
    szAspectRatio: win32more.Windows.Win32.Foundation.SIZE
    rcSrc: win32more.Windows.Win32.Foundation.RECT
    rcDst: win32more.Windows.Win32.Foundation.RECT
    dwTypeSpecificFlags: UInt32
    dwInterlaceFlags: UInt32
VMRPresentationFlags = Int32
VMRSample_SyncPoint: win32more.Windows.Win32.Media.DirectShow.VMRPresentationFlags = 1
VMRSample_Preroll: win32more.Windows.Win32.Media.DirectShow.VMRPresentationFlags = 2
VMRSample_Discontinuity: win32more.Windows.Win32.Media.DirectShow.VMRPresentationFlags = 4
VMRSample_TimeValid: win32more.Windows.Win32.Media.DirectShow.VMRPresentationFlags = 8
VMRSample_SrcDstRectsValid: win32more.Windows.Win32.Media.DirectShow.VMRPresentationFlags = 16
VMRRenderPrefs = Int32
RenderPrefs_RestrictToInitialMonitor: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 0
RenderPrefs_ForceOffscreen: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 1
RenderPrefs_ForceOverlays: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 2
RenderPrefs_AllowOverlays: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 0
RenderPrefs_AllowOffscreen: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 0
RenderPrefs_DoNotRenderColorKeyAndBorder: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 8
RenderPrefs_Reserved: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 16
RenderPrefs_PreferAGPMemWhenMixing: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 32
RenderPrefs_Mask: win32more.Windows.Win32.Media.DirectShow.VMRRenderPrefs = 63
VMRSurfaceAllocationFlags = Int32
AMAP_PIXELFORMAT_VALID: win32more.Windows.Win32.Media.DirectShow.VMRSurfaceAllocationFlags = 1
AMAP_3D_TARGET: win32more.Windows.Win32.Media.DirectShow.VMRSurfaceAllocationFlags = 2
AMAP_ALLOW_SYSMEM: win32more.Windows.Win32.Media.DirectShow.VMRSurfaceAllocationFlags = 4
AMAP_FORCE_SYSMEM: win32more.Windows.Win32.Media.DirectShow.VMRSurfaceAllocationFlags = 8
AMAP_DIRECTED_FLIP: win32more.Windows.Win32.Media.DirectShow.VMRSurfaceAllocationFlags = 16
AMAP_DXVA_TARGET: win32more.Windows.Win32.Media.DirectShow.VMRSurfaceAllocationFlags = 32
class VMRVIDEOSTREAMINFO(Structure):
    pddsVideoSurface: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7
    dwWidth: UInt32
    dwHeight: UInt32
    dwStrmID: UInt32
    fAlpha: Single
    ddClrKey: win32more.Windows.Win32.Graphics.DirectDraw.DDCOLORKEY
    rNormal: win32more.Windows.Win32.Media.DirectShow.NORMALIZEDRECT
class VMRVideoDesc(Structure):
    dwSize: UInt32
    dwSampleWidth: UInt32
    dwSampleHeight: UInt32
    SingleFieldPerSample: win32more.Windows.Win32.Foundation.BOOL
    dwFourCC: UInt32
    InputSampleFreq: win32more.Windows.Win32.Media.DirectShow.VMRFrequency
    OutputFrameFreq: win32more.Windows.Win32.Media.DirectShow.VMRFrequency
VMR_ASPECT_RATIO_MODE = Int32
VMR_ARMODE_NONE: win32more.Windows.Win32.Media.DirectShow.VMR_ASPECT_RATIO_MODE = 0
VMR_ARMODE_LETTER_BOX: win32more.Windows.Win32.Media.DirectShow.VMR_ASPECT_RATIO_MODE = 1
VfwCaptureDialogs = Int32
VfwCaptureDialog_Source: win32more.Windows.Win32.Media.DirectShow.VfwCaptureDialogs = 1
VfwCaptureDialog_Format: win32more.Windows.Win32.Media.DirectShow.VfwCaptureDialogs = 2
VfwCaptureDialog_Display: win32more.Windows.Win32.Media.DirectShow.VfwCaptureDialogs = 4
VfwCompressDialogs = Int32
VfwCompressDialog_Config: win32more.Windows.Win32.Media.DirectShow.VfwCompressDialogs = 1
VfwCompressDialog_About: win32more.Windows.Win32.Media.DirectShow.VfwCompressDialogs = 2
VfwCompressDialog_QueryConfig: win32more.Windows.Win32.Media.DirectShow.VfwCompressDialogs = 4
VfwCompressDialog_QueryAbout: win32more.Windows.Win32.Media.DirectShow.VfwCompressDialogs = 8
VideoControlFlags = Int32
VideoControlFlag_FlipHorizontal: win32more.Windows.Win32.Media.DirectShow.VideoControlFlags = 1
VideoControlFlag_FlipVertical: win32more.Windows.Win32.Media.DirectShow.VideoControlFlags = 2
VideoControlFlag_ExternalTriggerEnable: win32more.Windows.Win32.Media.DirectShow.VideoControlFlags = 4
VideoControlFlag_Trigger: win32more.Windows.Win32.Media.DirectShow.VideoControlFlags = 8
VideoCopyProtectionType = Int32
VideoCopyProtectionMacrovisionBasic: win32more.Windows.Win32.Media.DirectShow.VideoCopyProtectionType = 0
VideoCopyProtectionMacrovisionCBI: win32more.Windows.Win32.Media.DirectShow.VideoCopyProtectionType = 1
VideoProcAmpFlags = Int32
VideoProcAmp_Flags_Auto: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpFlags = 1
VideoProcAmp_Flags_Manual: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpFlags = 2
VideoProcAmpProperty = Int32
VideoProcAmp_Brightness: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 0
VideoProcAmp_Contrast: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 1
VideoProcAmp_Hue: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 2
VideoProcAmp_Saturation: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 3
VideoProcAmp_Sharpness: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 4
VideoProcAmp_Gamma: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 5
VideoProcAmp_ColorEnable: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 6
VideoProcAmp_WhiteBalance: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 7
VideoProcAmp_BacklightCompensation: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 8
VideoProcAmp_Gain: win32more.Windows.Win32.Media.DirectShow.VideoProcAmpProperty = 9
_AMRESCTL_RESERVEFLAGS = Int32
AMRESCTL_RESERVEFLAGS_RESERVE: win32more.Windows.Win32.Media.DirectShow._AMRESCTL_RESERVEFLAGS = 0
AMRESCTL_RESERVEFLAGS_UNRESERVE: win32more.Windows.Win32.Media.DirectShow._AMRESCTL_RESERVEFLAGS = 1
_AMSTREAMSELECTENABLEFLAGS = Int32
AMSTREAMSELECTENABLE_ENABLE: win32more.Windows.Win32.Media.DirectShow._AMSTREAMSELECTENABLEFLAGS = 1
AMSTREAMSELECTENABLE_ENABLEALL: win32more.Windows.Win32.Media.DirectShow._AMSTREAMSELECTENABLEFLAGS = 2
_AMSTREAMSELECTINFOFLAGS = Int32
AMSTREAMSELECTINFO_ENABLED: win32more.Windows.Win32.Media.DirectShow._AMSTREAMSELECTINFOFLAGS = 1
AMSTREAMSELECTINFO_EXCLUSIVE: win32more.Windows.Win32.Media.DirectShow._AMSTREAMSELECTINFOFLAGS = 2
_AM_AUDIO_RENDERER_STAT_PARAM = Int32
AM_AUDREND_STAT_PARAM_BREAK_COUNT: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 1
AM_AUDREND_STAT_PARAM_SLAVE_MODE: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 2
AM_AUDREND_STAT_PARAM_SILENCE_DUR: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 3
AM_AUDREND_STAT_PARAM_LAST_BUFFER_DUR: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 4
AM_AUDREND_STAT_PARAM_DISCONTINUITIES: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 5
AM_AUDREND_STAT_PARAM_SLAVE_RATE: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 6
AM_AUDREND_STAT_PARAM_SLAVE_DROPWRITE_DUR: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 7
AM_AUDREND_STAT_PARAM_SLAVE_HIGHLOWERROR: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 8
AM_AUDREND_STAT_PARAM_SLAVE_LASTHIGHLOWERROR: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 9
AM_AUDREND_STAT_PARAM_SLAVE_ACCUMERROR: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 10
AM_AUDREND_STAT_PARAM_BUFFERFULLNESS: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 11
AM_AUDREND_STAT_PARAM_JITTER: win32more.Windows.Win32.Media.DirectShow._AM_AUDIO_RENDERER_STAT_PARAM = 12
_AM_FILTER_MISC_FLAGS = Int32
AM_FILTER_MISC_FLAGS_IS_RENDERER: win32more.Windows.Win32.Media.DirectShow._AM_FILTER_MISC_FLAGS = 1
AM_FILTER_MISC_FLAGS_IS_SOURCE: win32more.Windows.Win32.Media.DirectShow._AM_FILTER_MISC_FLAGS = 2
_AM_INTF_SEARCH_FLAGS = Int32
AM_INTF_SEARCH_INPUT_PIN: win32more.Windows.Win32.Media.DirectShow._AM_INTF_SEARCH_FLAGS = 1
AM_INTF_SEARCH_OUTPUT_PIN: win32more.Windows.Win32.Media.DirectShow._AM_INTF_SEARCH_FLAGS = 2
AM_INTF_SEARCH_FILTER: win32more.Windows.Win32.Media.DirectShow._AM_INTF_SEARCH_FLAGS = 4
_AM_OVERLAY_NOTIFY_FLAGS = Int32
AM_OVERLAY_NOTIFY_VISIBLE_CHANGE: win32more.Windows.Win32.Media.DirectShow._AM_OVERLAY_NOTIFY_FLAGS = 1
AM_OVERLAY_NOTIFY_SOURCE_CHANGE: win32more.Windows.Win32.Media.DirectShow._AM_OVERLAY_NOTIFY_FLAGS = 2
AM_OVERLAY_NOTIFY_DEST_CHANGE: win32more.Windows.Win32.Media.DirectShow._AM_OVERLAY_NOTIFY_FLAGS = 4
_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS = Int32
AM_PIN_FLOW_CONTROL_BLOCK: win32more.Windows.Win32.Media.DirectShow._AM_PIN_FLOW_CONTROL_BLOCK_FLAGS = 1
_AM_PUSHSOURCE_FLAGS = Int32
AM_PUSHSOURCECAPS_INTERNAL_RM: win32more.Windows.Win32.Media.DirectShow._AM_PUSHSOURCE_FLAGS = 1
AM_PUSHSOURCECAPS_NOT_LIVE: win32more.Windows.Win32.Media.DirectShow._AM_PUSHSOURCE_FLAGS = 2
AM_PUSHSOURCECAPS_PRIVATE_CLOCK: win32more.Windows.Win32.Media.DirectShow._AM_PUSHSOURCE_FLAGS = 4
AM_PUSHSOURCEREQS_USE_STREAM_CLOCK: win32more.Windows.Win32.Media.DirectShow._AM_PUSHSOURCE_FLAGS = 65536
AM_PUSHSOURCEREQS_USE_CLOCK_CHAIN: win32more.Windows.Win32.Media.DirectShow._AM_PUSHSOURCE_FLAGS = 131072
_AM_RENSDEREXFLAGS = Int32
AM_RENDEREX_RENDERTOEXISTINGRENDERERS: win32more.Windows.Win32.Media.DirectShow._AM_RENSDEREXFLAGS = 1
_DVDECODERRESOLUTION = Int32
DVDECODERRESOLUTION_720x480: win32more.Windows.Win32.Media.DirectShow._DVDECODERRESOLUTION = 1000
DVDECODERRESOLUTION_360x240: win32more.Windows.Win32.Media.DirectShow._DVDECODERRESOLUTION = 1001
DVDECODERRESOLUTION_180x120: win32more.Windows.Win32.Media.DirectShow._DVDECODERRESOLUTION = 1002
DVDECODERRESOLUTION_88x60: win32more.Windows.Win32.Media.DirectShow._DVDECODERRESOLUTION = 1003
_DVENCODERFORMAT = Int32
DVENCODERFORMAT_DVSD: win32more.Windows.Win32.Media.DirectShow._DVENCODERFORMAT = 2007
DVENCODERFORMAT_DVHD: win32more.Windows.Win32.Media.DirectShow._DVENCODERFORMAT = 2008
DVENCODERFORMAT_DVSL: win32more.Windows.Win32.Media.DirectShow._DVENCODERFORMAT = 2009
_DVENCODERRESOLUTION = Int32
DVENCODERRESOLUTION_720x480: win32more.Windows.Win32.Media.DirectShow._DVENCODERRESOLUTION = 2012
DVENCODERRESOLUTION_360x240: win32more.Windows.Win32.Media.DirectShow._DVENCODERRESOLUTION = 2013
DVENCODERRESOLUTION_180x120: win32more.Windows.Win32.Media.DirectShow._DVENCODERRESOLUTION = 2014
DVENCODERRESOLUTION_88x60: win32more.Windows.Win32.Media.DirectShow._DVENCODERRESOLUTION = 2015
_DVENCODERVIDEOFORMAT = Int32
DVENCODERVIDEOFORMAT_NTSC: win32more.Windows.Win32.Media.DirectShow._DVENCODERVIDEOFORMAT = 2000
DVENCODERVIDEOFORMAT_PAL: win32more.Windows.Win32.Media.DirectShow._DVENCODERVIDEOFORMAT = 2001
_DVRESOLUTION = Int32
DVRESOLUTION_FULL: win32more.Windows.Win32.Media.DirectShow._DVRESOLUTION = 1000
DVRESOLUTION_HALF: win32more.Windows.Win32.Media.DirectShow._DVRESOLUTION = 1001
DVRESOLUTION_QUARTER: win32more.Windows.Win32.Media.DirectShow._DVRESOLUTION = 1002
DVRESOLUTION_DC: win32more.Windows.Win32.Media.DirectShow._DVRESOLUTION = 1003
_REM_FILTER_FLAGS = Int32
REMFILTERF_LEAVECONNECTED: win32more.Windows.Win32.Media.DirectShow._REM_FILTER_FLAGS = 1


make_ready(__name__)
