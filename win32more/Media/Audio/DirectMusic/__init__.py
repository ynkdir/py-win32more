from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Media
import win32more.Media.Audio
import win32more.Media.Audio.DirectMusic
import win32more.Media.Audio.DirectSound
import win32more.Media.Multimedia
import win32more.System.Com
import win32more.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
DMUS_MAX_DESCRIPTION: UInt32 = 128
DMUS_MAX_DRIVER: UInt32 = 128
DMUS_EFFECT_NONE: UInt32 = 0
DMUS_EFFECT_REVERB: UInt32 = 1
DMUS_EFFECT_CHORUS: UInt32 = 2
DMUS_EFFECT_DELAY: UInt32 = 4
DMUS_PC_INPUTCLASS: UInt32 = 0
DMUS_PC_OUTPUTCLASS: UInt32 = 1
DMUS_PC_DLS: UInt32 = 1
DMUS_PC_EXTERNAL: UInt32 = 2
DMUS_PC_SOFTWARESYNTH: UInt32 = 4
DMUS_PC_MEMORYSIZEFIXED: UInt32 = 8
DMUS_PC_GMINHARDWARE: UInt32 = 16
DMUS_PC_GSINHARDWARE: UInt32 = 32
DMUS_PC_XGINHARDWARE: UInt32 = 64
DMUS_PC_DIRECTSOUND: UInt32 = 128
DMUS_PC_SHAREABLE: UInt32 = 256
DMUS_PC_DLS2: UInt32 = 512
DMUS_PC_AUDIOPATH: UInt32 = 1024
DMUS_PC_WAVE: UInt32 = 2048
DMUS_PC_SYSTEMMEMORY: UInt32 = 2147483647
DMUS_PORT_WINMM_DRIVER: UInt32 = 0
DMUS_PORT_USER_MODE_SYNTH: UInt32 = 1
DMUS_PORT_KERNEL_MODE: UInt32 = 2
DMUS_PORTPARAMS_VOICES: UInt32 = 1
DMUS_PORTPARAMS_CHANNELGROUPS: UInt32 = 2
DMUS_PORTPARAMS_AUDIOCHANNELS: UInt32 = 4
DMUS_PORTPARAMS_SAMPLERATE: UInt32 = 8
DMUS_PORTPARAMS_EFFECTS: UInt32 = 32
DMUS_PORTPARAMS_SHARE: UInt32 = 64
DMUS_PORTPARAMS_FEATURES: UInt32 = 128
DMUS_PORT_FEATURE_AUDIOPATH: UInt32 = 1
DMUS_PORT_FEATURE_STREAMING: UInt32 = 2
DMUS_SYNTHSTATS_VOICES: UInt32 = 1
DMUS_SYNTHSTATS_TOTAL_CPU: UInt32 = 2
DMUS_SYNTHSTATS_CPU_PER_VOICE: UInt32 = 4
DMUS_SYNTHSTATS_LOST_NOTES: UInt32 = 8
DMUS_SYNTHSTATS_PEAK_VOLUME: UInt32 = 16
DMUS_SYNTHSTATS_FREE_MEMORY: UInt32 = 32
DMUS_SYNTHSTATS_SYSTEMMEMORY: UInt32 = 2147483647
DMUS_CLOCKF_GLOBAL: UInt32 = 1
DSBUSID_FIRST_SPKR_LOC: UInt32 = 0
DSBUSID_FRONT_LEFT: UInt32 = 0
DSBUSID_LEFT: UInt32 = 0
DSBUSID_FRONT_RIGHT: UInt32 = 1
DSBUSID_RIGHT: UInt32 = 1
DSBUSID_FRONT_CENTER: UInt32 = 2
DSBUSID_LOW_FREQUENCY: UInt32 = 3
DSBUSID_BACK_LEFT: UInt32 = 4
DSBUSID_BACK_RIGHT: UInt32 = 5
DSBUSID_FRONT_LEFT_OF_CENTER: UInt32 = 6
DSBUSID_FRONT_RIGHT_OF_CENTER: UInt32 = 7
DSBUSID_BACK_CENTER: UInt32 = 8
DSBUSID_SIDE_LEFT: UInt32 = 9
DSBUSID_SIDE_RIGHT: UInt32 = 10
DSBUSID_TOP_CENTER: UInt32 = 11
DSBUSID_TOP_FRONT_LEFT: UInt32 = 12
DSBUSID_TOP_FRONT_CENTER: UInt32 = 13
DSBUSID_TOP_FRONT_RIGHT: UInt32 = 14
DSBUSID_TOP_BACK_LEFT: UInt32 = 15
DSBUSID_TOP_BACK_CENTER: UInt32 = 16
DSBUSID_TOP_BACK_RIGHT: UInt32 = 17
DSBUSID_LAST_SPKR_LOC: UInt32 = 17
DSBUSID_REVERB_SEND: UInt32 = 64
DSBUSID_CHORUS_SEND: UInt32 = 65
DSBUSID_DYNAMIC_0: UInt32 = 512
DSBUSID_NULL: UInt32 = 4294967295
DAUD_CRITICAL_VOICE_PRIORITY: UInt32 = 4026531840
DAUD_HIGH_VOICE_PRIORITY: UInt32 = 3221225472
DAUD_STANDARD_VOICE_PRIORITY: UInt32 = 2147483648
DAUD_LOW_VOICE_PRIORITY: UInt32 = 1073741824
DAUD_PERSIST_VOICE_PRIORITY: UInt32 = 268435456
DAUD_CHAN1_VOICE_PRIORITY_OFFSET: UInt32 = 14
DAUD_CHAN2_VOICE_PRIORITY_OFFSET: UInt32 = 13
DAUD_CHAN3_VOICE_PRIORITY_OFFSET: UInt32 = 12
DAUD_CHAN4_VOICE_PRIORITY_OFFSET: UInt32 = 11
DAUD_CHAN5_VOICE_PRIORITY_OFFSET: UInt32 = 10
DAUD_CHAN6_VOICE_PRIORITY_OFFSET: UInt32 = 9
DAUD_CHAN7_VOICE_PRIORITY_OFFSET: UInt32 = 8
DAUD_CHAN8_VOICE_PRIORITY_OFFSET: UInt32 = 7
DAUD_CHAN9_VOICE_PRIORITY_OFFSET: UInt32 = 6
DAUD_CHAN10_VOICE_PRIORITY_OFFSET: UInt32 = 15
DAUD_CHAN11_VOICE_PRIORITY_OFFSET: UInt32 = 5
DAUD_CHAN12_VOICE_PRIORITY_OFFSET: UInt32 = 4
DAUD_CHAN13_VOICE_PRIORITY_OFFSET: UInt32 = 3
DAUD_CHAN14_VOICE_PRIORITY_OFFSET: UInt32 = 2
DAUD_CHAN15_VOICE_PRIORITY_OFFSET: UInt32 = 1
DAUD_CHAN16_VOICE_PRIORITY_OFFSET: UInt32 = 0
CLSID_DirectMusic: Guid = Guid('636b9f10-0c7d-11d1-95-b2-00-20-af-dc-74-21')
CLSID_DirectMusicCollection: Guid = Guid('480ff4b0-28b2-11d1-be-f7-00-c0-4f-bf-8f-ef')
CLSID_DirectMusicSynth: Guid = Guid('58c2b4d0-46e7-11d1-89-ac-00-a0-c9-05-41-29')
GUID_DMUS_PROP_GM_Hardware: Guid = Guid('178f2f24-c364-11d1-a7-60-00-00-f8-75-ac-12')
GUID_DMUS_PROP_GS_Hardware: Guid = Guid('178f2f25-c364-11d1-a7-60-00-00-f8-75-ac-12')
GUID_DMUS_PROP_XG_Hardware: Guid = Guid('178f2f26-c364-11d1-a7-60-00-00-f8-75-ac-12')
GUID_DMUS_PROP_XG_Capable: Guid = Guid('6496aba1-61b0-11d2-af-a6-00-aa-00-24-d8-b6')
GUID_DMUS_PROP_GS_Capable: Guid = Guid('6496aba2-61b0-11d2-af-a6-00-aa-00-24-d8-b6')
GUID_DMUS_PROP_DLS1: Guid = Guid('178f2f27-c364-11d1-a7-60-00-00-f8-75-ac-12')
GUID_DMUS_PROP_DLS2: Guid = Guid('f14599e5-4689-11d2-af-a6-00-aa-00-24-d8-b6')
GUID_DMUS_PROP_INSTRUMENT2: Guid = Guid('865fd372-9f67-11d2-87-2a-00-60-08-93-b1-bd')
GUID_DMUS_PROP_SynthSink_DSOUND: Guid = Guid('0aa97844-c877-11d1-87-0c-00-60-08-93-b1-bd')
GUID_DMUS_PROP_SynthSink_WAVE: Guid = Guid('0aa97845-c877-11d1-87-0c-00-60-08-93-b1-bd')
GUID_DMUS_PROP_SampleMemorySize: Guid = Guid('178f2f28-c364-11d1-a7-60-00-00-f8-75-ac-12')
GUID_DMUS_PROP_SamplePlaybackRate: Guid = Guid('2a91f713-a4bf-11d2-bb-df-00-60-08-33-db-d8')
GUID_DMUS_PROP_WriteLatency: Guid = Guid('268a0fa0-60f2-11d2-af-a6-00-aa-00-24-d8-b6')
GUID_DMUS_PROP_WritePeriod: Guid = Guid('268a0fa1-60f2-11d2-af-a6-00-aa-00-24-d8-b6')
GUID_DMUS_PROP_MemorySize: Guid = Guid('178f2f28-c364-11d1-a7-60-00-00-f8-75-ac-12')
GUID_DMUS_PROP_WavesReverb: Guid = Guid('04cb5622-32e5-11d2-af-a6-00-aa-00-24-d8-b6')
GUID_DMUS_PROP_Effects: Guid = Guid('cda8d611-684a-11d2-87-1e-00-60-08-93-b1-bd')
GUID_DMUS_PROP_LegacyCaps: Guid = Guid('cfa7cdc2-00a1-11d2-aa-d5-00-00-f8-75-ac-12')
GUID_DMUS_PROP_Volume: Guid = Guid('fedfae25-e46e-11d1-aa-ce-00-00-f8-75-ac-12')
DMUS_VOLUME_MAX: UInt32 = 2000
DMUS_VOLUME_MIN: Int32 = -20000
DMUS_EVENT_STRUCTURED: UInt32 = 1
DMUS_DOWNLOADINFO_INSTRUMENT: UInt32 = 1
DMUS_DOWNLOADINFO_WAVE: UInt32 = 2
DMUS_DOWNLOADINFO_INSTRUMENT2: UInt32 = 3
DMUS_DOWNLOADINFO_WAVEARTICULATION: UInt32 = 4
DMUS_DOWNLOADINFO_STREAMINGWAVE: UInt32 = 5
DMUS_DOWNLOADINFO_ONESHOTWAVE: UInt32 = 6
DMUS_DEFAULT_SIZE_OFFSETTABLE: UInt32 = 1
DMUS_INSTRUMENT_GM_INSTRUMENT: UInt32 = 1
DMUS_MIN_DATA_SIZE: UInt32 = 4
CONN_SRC_NONE: UInt32 = 0
CONN_SRC_LFO: UInt32 = 1
CONN_SRC_KEYONVELOCITY: UInt32 = 2
CONN_SRC_KEYNUMBER: UInt32 = 3
CONN_SRC_EG1: UInt32 = 4
CONN_SRC_EG2: UInt32 = 5
CONN_SRC_PITCHWHEEL: UInt32 = 6
CONN_SRC_CC1: UInt32 = 129
CONN_SRC_CC7: UInt32 = 135
CONN_SRC_CC10: UInt32 = 138
CONN_SRC_CC11: UInt32 = 139
CONN_DST_NONE: UInt32 = 0
CONN_DST_ATTENUATION: UInt32 = 1
CONN_DST_PITCH: UInt32 = 3
CONN_DST_PAN: UInt32 = 4
CONN_DST_LFO_FREQUENCY: UInt32 = 260
CONN_DST_LFO_STARTDELAY: UInt32 = 261
CONN_DST_EG1_ATTACKTIME: UInt32 = 518
CONN_DST_EG1_DECAYTIME: UInt32 = 519
CONN_DST_EG1_RELEASETIME: UInt32 = 521
CONN_DST_EG1_SUSTAINLEVEL: UInt32 = 522
CONN_DST_EG2_ATTACKTIME: UInt32 = 778
CONN_DST_EG2_DECAYTIME: UInt32 = 779
CONN_DST_EG2_RELEASETIME: UInt32 = 781
CONN_DST_EG2_SUSTAINLEVEL: UInt32 = 782
CONN_TRN_NONE: UInt32 = 0
CONN_TRN_CONCAVE: UInt32 = 1
F_INSTRUMENT_DRUMS: UInt32 = 2147483648
F_RGN_OPTION_SELFNONEXCLUSIVE: UInt32 = 1
WAVELINK_CHANNEL_LEFT: Int32 = 1
WAVELINK_CHANNEL_RIGHT: Int32 = 2
F_WAVELINK_PHASE_MASTER: UInt32 = 1
POOL_CUE_NULL: Int32 = -1
F_WSMP_NO_TRUNCATION: Int32 = 1
F_WSMP_NO_COMPRESSION: Int32 = 2
WLOOP_TYPE_FORWARD: UInt32 = 0
CONN_SRC_POLYPRESSURE: UInt32 = 7
CONN_SRC_CHANNELPRESSURE: UInt32 = 8
CONN_SRC_VIBRATO: UInt32 = 9
CONN_SRC_MONOPRESSURE: UInt32 = 10
CONN_SRC_CC91: UInt32 = 219
CONN_SRC_CC93: UInt32 = 221
CONN_DST_GAIN: UInt32 = 1
CONN_DST_KEYNUMBER: UInt32 = 5
CONN_DST_LEFT: UInt32 = 16
CONN_DST_RIGHT: UInt32 = 17
CONN_DST_CENTER: UInt32 = 18
CONN_DST_LEFTREAR: UInt32 = 19
CONN_DST_RIGHTREAR: UInt32 = 20
CONN_DST_LFE_CHANNEL: UInt32 = 21
CONN_DST_CHORUS: UInt32 = 128
CONN_DST_REVERB: UInt32 = 129
CONN_DST_VIB_FREQUENCY: UInt32 = 276
CONN_DST_VIB_STARTDELAY: UInt32 = 277
CONN_DST_EG1_DELAYTIME: UInt32 = 523
CONN_DST_EG1_HOLDTIME: UInt32 = 524
CONN_DST_EG1_SHUTDOWNTIME: UInt32 = 525
CONN_DST_EG2_DELAYTIME: UInt32 = 783
CONN_DST_EG2_HOLDTIME: UInt32 = 784
CONN_DST_FILTER_CUTOFF: UInt32 = 1280
CONN_DST_FILTER_Q: UInt32 = 1281
CONN_TRN_CONVEX: UInt32 = 2
CONN_TRN_SWITCH: UInt32 = 3
DLS_CDL_AND: UInt32 = 1
DLS_CDL_OR: UInt32 = 2
DLS_CDL_XOR: UInt32 = 3
DLS_CDL_ADD: UInt32 = 4
DLS_CDL_SUBTRACT: UInt32 = 5
DLS_CDL_MULTIPLY: UInt32 = 6
DLS_CDL_DIVIDE: UInt32 = 7
DLS_CDL_LOGICAL_AND: UInt32 = 8
DLS_CDL_LOGICAL_OR: UInt32 = 9
DLS_CDL_LT: UInt32 = 10
DLS_CDL_LE: UInt32 = 11
DLS_CDL_GT: UInt32 = 12
DLS_CDL_GE: UInt32 = 13
DLS_CDL_EQ: UInt32 = 14
DLS_CDL_NOT: UInt32 = 15
DLS_CDL_CONST: UInt32 = 16
DLS_CDL_QUERY: UInt32 = 17
DLS_CDL_QUERYSUPPORTED: UInt32 = 18
WLOOP_TYPE_RELEASE: UInt32 = 2
F_WAVELINK_MULTICHANNEL: UInt32 = 2
DLSID_GMInHardware: Guid = Guid('178f2f24-c364-11d1-a7-60-00-00-f8-75-ac-12')
DLSID_GSInHardware: Guid = Guid('178f2f25-c364-11d1-a7-60-00-00-f8-75-ac-12')
DLSID_XGInHardware: Guid = Guid('178f2f26-c364-11d1-a7-60-00-00-f8-75-ac-12')
DLSID_SupportsDLS1: Guid = Guid('178f2f27-c364-11d1-a7-60-00-00-f8-75-ac-12')
DLSID_SupportsDLS2: Guid = Guid('f14599e5-4689-11d2-af-a6-00-aa-00-24-d8-b6')
DLSID_SampleMemorySize: Guid = Guid('178f2f28-c364-11d1-a7-60-00-00-f8-75-ac-12')
DLSID_ManufacturersID: Guid = Guid('b03e1181-8095-11d2-a1-ef-00-60-08-33-db-d8')
DLSID_ProductID: Guid = Guid('b03e1182-8095-11d2-a1-ef-00-60-08-33-db-d8')
DLSID_SamplePlaybackRate: Guid = Guid('2a91f713-a4bf-11d2-bb-df-00-60-08-33-db-d8')
REGSTR_PATH_SOFTWARESYNTHS: String = 'Software\\Microsoft\\DirectMusic\\SoftwareSynths'
REFRESH_F_LASTBUFFER: UInt32 = 1
CLSID_DirectMusicSynthSink: Guid = Guid('aec17ce3-a514-11d1-af-a6-00-aa-00-24-d8-b6')
GUID_DMUS_PROP_SetSynthSink: Guid = Guid('0a3a5ba5-37b6-11d2-b9-f9-00-00-f8-75-ac-12')
GUID_DMUS_PROP_SinkUsesDSound: Guid = Guid('be208857-8952-11d2-ba-1c-00-00-f8-75-ac-12')
CLSID_DirectSoundPrivate: Guid = Guid('11ab3ec0-25ec-11d1-a4-d8-00-c0-4f-c2-8a-ca')
DSPROPSETID_DirectSoundDevice: Guid = Guid('84624f82-25ec-11d1-a4-d8-00-c0-4f-c2-8a-ca')
DV_DVSD_NTSC_FRAMESIZE: Int32 = 120000
DV_DVSD_PAL_FRAMESIZE: Int32 = 144000
DV_SMCHN: UInt32 = 57344
DV_AUDIOMODE: UInt32 = 3840
DV_AUDIOSMP: UInt32 = 939524096
DV_AUDIOQU: UInt32 = 117440512
DV_NTSCPAL: UInt32 = 2097152
DV_STYPE: UInt32 = 2031616
DV_NTSC: UInt32 = 0
DV_PAL: UInt32 = 1
DV_SD: UInt32 = 0
DV_HD: UInt32 = 1
DV_SL: UInt32 = 2
DV_CAP_AUD16Bits: UInt32 = 0
DV_CAP_AUD12Bits: UInt32 = 1
SIZE_DVINFO: UInt32 = 32
class CONNECTION(Structure):
    usSource: UInt16
    usControl: UInt16
    usDestination: UInt16
    usTransform: UInt16
    lScale: Int32
class CONNECTIONLIST(Structure):
    cbSize: UInt32
    cConnections: UInt32
DIRECTSOUNDDEVICE_DATAFLOW = Int32
DIRECTSOUNDDEVICE_DATAFLOW_RENDER: DIRECTSOUNDDEVICE_DATAFLOW = 0
DIRECTSOUNDDEVICE_DATAFLOW_CAPTURE: DIRECTSOUNDDEVICE_DATAFLOW = 1
DIRECTSOUNDDEVICE_TYPE = Int32
DIRECTSOUNDDEVICE_TYPE_EMULATED: DIRECTSOUNDDEVICE_TYPE = 0
DIRECTSOUNDDEVICE_TYPE_VXD: DIRECTSOUNDDEVICE_TYPE = 1
DIRECTSOUNDDEVICE_TYPE_WDM: DIRECTSOUNDDEVICE_TYPE = 2
class DLSHEADER(Structure):
    cInstruments: UInt32
class DLSID(Structure):
    ulData1: UInt32
    usData2: UInt16
    usData3: UInt16
    abData4: Byte * 8
class DLSVERSION(Structure):
    dwVersionMS: UInt32
    dwVersionLS: UInt32
class DMUS_ARTICPARAMS(Structure):
    LFO: win32more.Media.Audio.DirectMusic.DMUS_LFOPARAMS
    VolEG: win32more.Media.Audio.DirectMusic.DMUS_VEGPARAMS
    PitchEG: win32more.Media.Audio.DirectMusic.DMUS_PEGPARAMS
    Misc: win32more.Media.Audio.DirectMusic.DMUS_MSCPARAMS
class DMUS_ARTICULATION(Structure):
    ulArt1Idx: UInt32
    ulFirstExtCkIdx: UInt32
class DMUS_ARTICULATION2(Structure):
    ulArtIdx: UInt32
    ulFirstExtCkIdx: UInt32
    ulNextArtIdx: UInt32
class DMUS_BUFFERDESC(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    guidBufferFormat: Guid
    cbBuffer: UInt32
class DMUS_CLOCKINFO7(Structure):
    dwSize: UInt32
    ctType: win32more.Media.Audio.DirectMusic.DMUS_CLOCKTYPE
    guidClock: Guid
    wszDescription: Char * 128
class DMUS_CLOCKINFO8(Structure):
    dwSize: UInt32
    ctType: win32more.Media.Audio.DirectMusic.DMUS_CLOCKTYPE
    guidClock: Guid
    wszDescription: Char * 128
    dwFlags: UInt32
DMUS_CLOCKTYPE = Int32
DMUS_CLOCK_SYSTEM: DMUS_CLOCKTYPE = 0
DMUS_CLOCK_WAVE: DMUS_CLOCKTYPE = 1
class DMUS_COPYRIGHT(Structure):
    cbSize: UInt32
    byCopyright: Byte * 4
class DMUS_DOWNLOADINFO(Structure):
    dwDLType: UInt32
    dwDLId: UInt32
    dwNumOffsetTableEntries: UInt32
    cbSize: UInt32
class DMUS_EVENTHEADER(Structure):
    cbEvent: UInt32
    dwChannelGroup: UInt32
    rtDelta: Int64
    dwFlags: UInt32
    _pack_ = 4
class DMUS_EXTENSIONCHUNK(Structure):
    cbSize: UInt32
    ulNextExtCkIdx: UInt32
    ExtCkID: UInt32
    byExtCk: Byte * 4
class DMUS_INSTRUMENT(Structure):
    ulPatch: UInt32
    ulFirstRegionIdx: UInt32
    ulGlobalArtIdx: UInt32
    ulFirstExtCkIdx: UInt32
    ulCopyrightIdx: UInt32
    ulFlags: UInt32
class DMUS_LFOPARAMS(Structure):
    pcFrequency: Int32
    tcDelay: Int32
    gcVolumeScale: Int32
    pcPitchScale: Int32
    gcMWToVolume: Int32
    pcMWToPitch: Int32
class DMUS_MSCPARAMS(Structure):
    ptDefaultPan: Int32
class DMUS_NOTERANGE(Structure):
    dwLowNote: UInt32
    dwHighNote: UInt32
class DMUS_OFFSETTABLE(Structure):
    ulOffsetTable: UInt32 * 1
class DMUS_PEGPARAMS(Structure):
    tcAttack: Int32
    tcDecay: Int32
    ptSustain: Int32
    tcRelease: Int32
    tcVel2Attack: Int32
    tcKey2Decay: Int32
    pcRange: Int32
class DMUS_PORTCAPS(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    guidPort: Guid
    dwClass: UInt32
    dwType: UInt32
    dwMemorySize: UInt32
    dwMaxChannelGroups: UInt32
    dwMaxVoices: UInt32
    dwMaxAudioChannels: UInt32
    dwEffectFlags: UInt32
    wszDescription: Char * 128
class DMUS_PORTPARAMS7(Structure):
    dwSize: UInt32
    dwValidParams: UInt32
    dwVoices: UInt32
    dwChannelGroups: UInt32
    dwAudioChannels: UInt32
    dwSampleRate: UInt32
    dwEffectFlags: UInt32
    fShare: win32more.Foundation.BOOL
class DMUS_PORTPARAMS8(Structure):
    dwSize: UInt32
    dwValidParams: UInt32
    dwVoices: UInt32
    dwChannelGroups: UInt32
    dwAudioChannels: UInt32
    dwSampleRate: UInt32
    dwEffectFlags: UInt32
    fShare: win32more.Foundation.BOOL
    dwFeatures: UInt32
class DMUS_REGION(Structure):
    RangeKey: win32more.Media.Audio.DirectMusic.RGNRANGE
    RangeVelocity: win32more.Media.Audio.DirectMusic.RGNRANGE
    fusOptions: UInt16
    usKeyGroup: UInt16
    ulRegionArtIdx: UInt32
    ulNextRegionIdx: UInt32
    ulFirstExtCkIdx: UInt32
    WaveLink: win32more.Media.Audio.DirectMusic.WAVELINK
    WSMP: win32more.Media.Audio.DirectMusic.WSMPL
    WLOOP: win32more.Media.Audio.DirectMusic.WLOOP * 1
class DMUS_SYNTHSTATS(Structure):
    dwSize: UInt32
    dwValidStats: UInt32
    dwVoices: UInt32
    dwTotalCPU: UInt32
    dwCPUPerVoice: UInt32
    dwLostNotes: UInt32
    dwFreeMemory: UInt32
    lPeakVolume: Int32
class DMUS_SYNTHSTATS8(Structure):
    dwSize: UInt32
    dwValidStats: UInt32
    dwVoices: UInt32
    dwTotalCPU: UInt32
    dwCPUPerVoice: UInt32
    dwLostNotes: UInt32
    dwFreeMemory: UInt32
    lPeakVolume: Int32
    dwSynthMemUse: UInt32
class DMUS_VEGPARAMS(Structure):
    tcAttack: Int32
    tcDecay: Int32
    ptSustain: Int32
    tcRelease: Int32
    tcVel2Attack: Int32
    tcKey2Decay: Int32
class DMUS_VOICE_STATE(Structure):
    bExists: win32more.Foundation.BOOL
    spPosition: UInt64
class DMUS_WAVE(Structure):
    ulFirstExtCkIdx: UInt32
    ulCopyrightIdx: UInt32
    ulWaveDataIdx: UInt32
    WaveformatEx: win32more.Media.Audio.WAVEFORMATEX
class DMUS_WAVEARTDL(Structure):
    ulDownloadIdIdx: UInt32
    ulBus: UInt32
    ulBuffers: UInt32
    ulMasterDLId: UInt32
    usOptions: UInt16
class DMUS_WAVEDATA(Structure):
    cbSize: UInt32
    byData: Byte * 4
class DMUS_WAVEDL(Structure):
    cbWaveData: UInt32
class DMUS_WAVES_REVERB_PARAMS(Structure):
    fInGain: Single
    fReverbMix: Single
    fReverbTime: Single
    fHighFreqRTRatio: Single
DSPROPERTY_DIRECTSOUNDDEVICE = Int32
DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A: DSPROPERTY_DIRECTSOUNDDEVICE = 1
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1: DSPROPERTY_DIRECTSOUNDDEVICE = 2
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1: DSPROPERTY_DIRECTSOUNDDEVICE = 3
DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W: DSPROPERTY_DIRECTSOUNDDEVICE = 4
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A: DSPROPERTY_DIRECTSOUNDDEVICE = 5
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W: DSPROPERTY_DIRECTSOUNDDEVICE = 6
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A: DSPROPERTY_DIRECTSOUNDDEVICE = 7
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W: DSPROPERTY_DIRECTSOUNDDEVICE = 8
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA(Structure):
    DeviceId: Guid
    DescriptionA: win32more.Foundation.CHAR * 256
    DescriptionW: Char * 256
    ModuleA: win32more.Foundation.CHAR * 260
    ModuleW: Char * 260
    Type: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    WaveDeviceId: UInt32
    Devnode: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA(Structure):
    Type: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
    Description: win32more.Foundation.PSTR
    Module: win32more.Foundation.PSTR
    Interface: win32more.Foundation.PSTR
    WaveDeviceId: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA(Structure):
    Type: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
    Description: win32more.Foundation.PWSTR
    Module: win32more.Foundation.PWSTR
    Interface: win32more.Foundation.PWSTR
    WaveDeviceId: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA(Structure):
    Callback: win32more.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1
    Context: c_void_p
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA(Structure):
    Callback: win32more.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA
    Context: c_void_p
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA(Structure):
    Callback: win32more.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW
    Context: c_void_p
class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA(Structure):
    DeviceName: win32more.Foundation.PSTR
    DataFlow: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA(Structure):
    DeviceName: win32more.Foundation.PWSTR
    DataFlow: win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
class DVAudInfo(Structure):
    bAudStyle: Byte * 2
    bAudQu: Byte * 2
    bNumAudPin: Byte
    wAvgSamplesPerPinPerFrm: UInt16 * 2
    wBlkMode: UInt16
    wDIFMode: UInt16
    wBlkDiv: UInt16
class IDirectMusic(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6536115a-7b2d-11d2-ba-18-00-00-f8-75-ac-12')
    @commethod(3)
    def EnumPort(dwIndex: UInt32, pPortCaps: POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTCAPS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateMusicBuffer(pBufferDesc: POINTER(win32more.Media.Audio.DirectMusic.DMUS_BUFFERDESC_head), ppBuffer: POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicBuffer_head), pUnkOuter: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreatePort(rclsidPort: POINTER(Guid), pPortParams: POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTPARAMS8_head), ppPort: POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicPort_head), pUnkOuter: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumMasterClock(dwIndex: UInt32, lpClockInfo: POINTER(win32more.Media.Audio.DirectMusic.DMUS_CLOCKINFO8_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetMasterClock(pguidClock: POINTER(Guid), ppReferenceClock: POINTER(win32more.Media.IReferenceClock_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetMasterClock(rguidClock: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Activate(fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDefaultPort(pguidPort: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetDirectSound(pDirectSound: win32more.Media.Audio.DirectSound.IDirectSound_head, hWnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
class IDirectMusic8(c_void_p):
    extends: win32more.Media.Audio.DirectMusic.IDirectMusic
    Guid = Guid('2d3629f7-813d-4939-85-08-f0-5c-6b-75-fd-97')
    @commethod(12)
    def SetExternalMasterClock(pClock: win32more.Media.IReferenceClock_head) -> win32more.Foundation.HRESULT: ...
class IDirectMusicBuffer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2ac2878-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def Flush() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TotalTime(prtTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PackStructured(rt: Int64, dwChannelGroup: UInt32, dwChannelMessage: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def PackUnstructured(rt: Int64, dwChannelGroup: UInt32, cb: UInt32, lpb: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ResetReadPtr() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetNextEvent(prt: POINTER(Int64), pdwChannelGroup: POINTER(UInt32), pdwLength: POINTER(UInt32), ppData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRawBufferPtr(ppData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetStartTime(prt: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetUsedBytes(pcb: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetMaxBytes(pcb: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetBufferFormat(pGuidFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetStartTime(rt: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetUsedBytes(cb: UInt32) -> win32more.Foundation.HRESULT: ...
class IDirectMusicCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2ac287c-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetInstrument(dwPatch: UInt32, ppInstrument: POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicInstrument_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumInstrument(dwIndex: UInt32, pdwPatch: POINTER(UInt32), pwszName: win32more.Foundation.PWSTR, dwNameLen: UInt32) -> win32more.Foundation.HRESULT: ...
class IDirectMusicDownload(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2ac287b-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetBuffer(ppvBuffer: POINTER(c_void_p), pdwSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDirectMusicDownloadedInstrument(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2ac287e-b39b-11d1-87-04-00-60-08-93-b1-bd')
class IDirectMusicInstrument(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2ac287d-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetPatch(pdwPatch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPatch(dwPatch: UInt32) -> win32more.Foundation.HRESULT: ...
class IDirectMusicPort(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('08f2d8c9-37c2-11d2-b9-f9-00-00-f8-75-ac-12')
    @commethod(3)
    def PlayBuffer(pBuffer: win32more.Media.Audio.DirectMusic.IDirectMusicBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetReadNotificationHandle(hEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Read(pBuffer: win32more.Media.Audio.DirectMusic.IDirectMusicBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DownloadInstrument(pInstrument: win32more.Media.Audio.DirectMusic.IDirectMusicInstrument_head, ppDownloadedInstrument: POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument_head), pNoteRanges: POINTER(win32more.Media.Audio.DirectMusic.DMUS_NOTERANGE_head), dwNumNoteRanges: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def UnloadInstrument(pDownloadedInstrument: win32more.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetLatencyClock(ppClock: POINTER(win32more.Media.IReferenceClock_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRunningStats(pStats: POINTER(win32more.Media.Audio.DirectMusic.DMUS_SYNTHSTATS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Compact() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetCaps(pPortCaps: POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTCAPS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DeviceIoControl(dwIoControlCode: UInt32, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetNumChannelGroups(dwChannelGroups: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetNumChannelGroups(pdwChannelGroups: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Activate(fActive: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetChannelPriority(dwChannelGroup: UInt32, dwChannel: UInt32, dwPriority: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetChannelPriority(dwChannelGroup: UInt32, dwChannel: UInt32, pdwPriority: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetDirectSound(pDirectSound: win32more.Media.Audio.DirectSound.IDirectSound_head, pDirectSoundBuffer: win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetFormat(pWaveFormatEx: POINTER(win32more.Media.Audio.WAVEFORMATEX_head), pdwWaveFormatExSize: POINTER(UInt32), pdwBufferSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDirectMusicPortDownload(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2ac287a-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetBuffer(dwDLId: UInt32, ppIDMDownload: POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateBuffer(dwSize: UInt32, ppIDMDownload: POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDLId(pdwStartDLId: POINTER(UInt32), dwCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAppend(pdwAppend: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Download(pIDMDownload: win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Unload(pIDMDownload: win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head) -> win32more.Foundation.HRESULT: ...
class IDirectMusicSynth(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('09823661-5c85-11d2-af-a6-00-aa-00-24-d8-b6')
    @commethod(3)
    def Open(pPortParams: POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTPARAMS8_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetNumChannelGroups(dwGroups: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Download(phDownload: POINTER(win32more.Foundation.HANDLE), pvData: c_void_p, pbFree: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Unload(hDownload: win32more.Foundation.HANDLE, lpFreeHandle: IntPtr, hUserData: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def PlayBuffer(rt: Int64, pbBuffer: c_char_p_no, cbBuffer: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRunningStats(pStats: POINTER(win32more.Media.Audio.DirectMusic.DMUS_SYNTHSTATS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPortCaps(pCaps: POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTCAPS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetMasterClock(pClock: win32more.Media.IReferenceClock_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetLatencyClock(ppClock: POINTER(win32more.Media.IReferenceClock_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Activate(fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetSynthSink(pSynthSink: win32more.Media.Audio.DirectMusic.IDirectMusicSynthSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Render(pBuffer: POINTER(Int16), dwLength: UInt32, llPosition: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetChannelPriority(dwChannelGroup: UInt32, dwChannel: UInt32, dwPriority: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetChannelPriority(dwChannelGroup: UInt32, dwChannel: UInt32, pdwPriority: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetFormat(pWaveFormatEx: POINTER(win32more.Media.Audio.WAVEFORMATEX_head), pdwWaveFormatExSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetAppend(pdwAppend: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDirectMusicSynth8(c_void_p):
    extends: win32more.Media.Audio.DirectMusic.IDirectMusicSynth
    Guid = Guid('53cab625-2711-4c9f-9d-e7-1b-7f-92-5f-6f-c8')
    @commethod(20)
    def PlayVoice(rt: Int64, dwVoiceId: UInt32, dwChannelGroup: UInt32, dwChannel: UInt32, dwDLId: UInt32, prPitch: Int32, vrVolume: Int32, stVoiceStart: UInt64, stLoopStart: UInt64, stLoopEnd: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def StopVoice(rt: Int64, dwVoiceId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetVoiceState(dwVoice: POINTER(UInt32), cbVoice: UInt32, dwVoiceState: POINTER(win32more.Media.Audio.DirectMusic.DMUS_VOICE_STATE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Refresh(dwDownloadID: UInt32, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def AssignChannelToBuses(dwChannelGroup: UInt32, dwChannel: UInt32, pdwBuses: POINTER(UInt32), cBuses: UInt32) -> win32more.Foundation.HRESULT: ...
class IDirectMusicSynthSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('09823663-5c85-11d2-af-a6-00-aa-00-24-d8-b6')
    @commethod(3)
    def Init(pSynth: win32more.Media.Audio.DirectMusic.IDirectMusicSynth_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetMasterClock(pClock: win32more.Media.IReferenceClock_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatencyClock(ppClock: POINTER(win32more.Media.IReferenceClock_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SampleToRefTime(llSampleTime: Int64, prfTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RefTimeToSample(rfTime: Int64, pllSampleTime: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetDirectSound(pDirectSound: win32more.Media.Audio.DirectSound.IDirectSound_head, pDirectSoundBuffer: win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDesiredBufferSize(pdwBufferSizeInSamples: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IDirectMusicThru(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ced153e7-3606-11d2-b9-f9-00-00-f8-75-ac-12')
    @commethod(3)
    def ThruChannel(dwSourceChannelGroup: UInt32, dwSourceChannel: UInt32, dwDestinationChannelGroup: UInt32, dwDestinationChannel: UInt32, pDestinationPort: win32more.Media.Audio.DirectMusic.IDirectMusicPort_head) -> win32more.Foundation.HRESULT: ...
class INSTHEADER(Structure):
    cRegions: UInt32
    Locale: win32more.Media.Audio.DirectMusic.MIDILOCALE
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1(param0: POINTER(win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA_head), param1: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA(param0: POINTER(win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA_head), param1: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW(param0: POINTER(win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA_head), param1: c_void_p) -> win32more.Foundation.BOOL: ...
class MDEVICECAPSEX(Structure):
    cbSize: UInt32
    pCaps: c_void_p
    _pack_ = 1
class MIDILOCALE(Structure):
    ulBank: UInt32
    ulInstrument: UInt32
class MIDIOPENDESC(Structure):
    hMidi: win32more.Media.Audio.HMIDI
    dwCallback: UIntPtr
    dwInstance: UIntPtr
    dnDevNode: UIntPtr
    cIds: UInt32
    rgIds: win32more.Media.Multimedia.MIDIOPENSTRMID * 1
    _pack_ = 1
class POOLCUE(Structure):
    ulOffset: UInt32
class POOLTABLE(Structure):
    cbSize: UInt32
    cCues: UInt32
class RGNHEADER(Structure):
    RangeKey: win32more.Media.Audio.DirectMusic.RGNRANGE
    RangeVelocity: win32more.Media.Audio.DirectMusic.RGNRANGE
    fusOptions: UInt16
    usKeyGroup: UInt16
class RGNRANGE(Structure):
    usLow: UInt16
    usHigh: UInt16
class WAVELINK(Structure):
    fusOptions: UInt16
    usPhaseGroup: UInt16
    ulChannel: UInt32
    ulTableIndex: UInt32
class WLOOP(Structure):
    cbSize: UInt32
    ulType: UInt32
    ulStart: UInt32
    ulLength: UInt32
class WSMPL(Structure):
    cbSize: UInt32
    usUnityNote: UInt16
    sFineTune: Int16
    lAttenuation: Int32
    fulOptions: UInt32
    cSampleLoops: UInt32
make_head(_module, 'CONNECTION')
make_head(_module, 'CONNECTIONLIST')
make_head(_module, 'DLSHEADER')
make_head(_module, 'DLSID')
make_head(_module, 'DLSVERSION')
make_head(_module, 'DMUS_ARTICPARAMS')
make_head(_module, 'DMUS_ARTICULATION')
make_head(_module, 'DMUS_ARTICULATION2')
make_head(_module, 'DMUS_BUFFERDESC')
make_head(_module, 'DMUS_CLOCKINFO7')
make_head(_module, 'DMUS_CLOCKINFO8')
make_head(_module, 'DMUS_COPYRIGHT')
make_head(_module, 'DMUS_DOWNLOADINFO')
make_head(_module, 'DMUS_EVENTHEADER')
make_head(_module, 'DMUS_EXTENSIONCHUNK')
make_head(_module, 'DMUS_INSTRUMENT')
make_head(_module, 'DMUS_LFOPARAMS')
make_head(_module, 'DMUS_MSCPARAMS')
make_head(_module, 'DMUS_NOTERANGE')
make_head(_module, 'DMUS_OFFSETTABLE')
make_head(_module, 'DMUS_PEGPARAMS')
make_head(_module, 'DMUS_PORTCAPS')
make_head(_module, 'DMUS_PORTPARAMS7')
make_head(_module, 'DMUS_PORTPARAMS8')
make_head(_module, 'DMUS_REGION')
make_head(_module, 'DMUS_SYNTHSTATS')
make_head(_module, 'DMUS_SYNTHSTATS8')
make_head(_module, 'DMUS_VEGPARAMS')
make_head(_module, 'DMUS_VOICE_STATE')
make_head(_module, 'DMUS_WAVE')
make_head(_module, 'DMUS_WAVEARTDL')
make_head(_module, 'DMUS_WAVEDATA')
make_head(_module, 'DMUS_WAVEDL')
make_head(_module, 'DMUS_WAVES_REVERB_PARAMS')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA')
make_head(_module, 'DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA')
make_head(_module, 'DVAudInfo')
make_head(_module, 'IDirectMusic')
make_head(_module, 'IDirectMusic8')
make_head(_module, 'IDirectMusicBuffer')
make_head(_module, 'IDirectMusicCollection')
make_head(_module, 'IDirectMusicDownload')
make_head(_module, 'IDirectMusicDownloadedInstrument')
make_head(_module, 'IDirectMusicInstrument')
make_head(_module, 'IDirectMusicPort')
make_head(_module, 'IDirectMusicPortDownload')
make_head(_module, 'IDirectMusicSynth')
make_head(_module, 'IDirectMusicSynth8')
make_head(_module, 'IDirectMusicSynthSink')
make_head(_module, 'IDirectMusicThru')
make_head(_module, 'INSTHEADER')
make_head(_module, 'LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1')
make_head(_module, 'LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA')
make_head(_module, 'LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW')
make_head(_module, 'MDEVICECAPSEX')
make_head(_module, 'MIDILOCALE')
make_head(_module, 'MIDIOPENDESC')
make_head(_module, 'POOLCUE')
make_head(_module, 'POOLTABLE')
make_head(_module, 'RGNHEADER')
make_head(_module, 'RGNRANGE')
make_head(_module, 'WAVELINK')
make_head(_module, 'WLOOP')
make_head(_module, 'WSMPL')
__all__ = [
    "CLSID_DirectMusic",
    "CLSID_DirectMusicCollection",
    "CLSID_DirectMusicSynth",
    "CLSID_DirectMusicSynthSink",
    "CLSID_DirectSoundPrivate",
    "CONNECTION",
    "CONNECTIONLIST",
    "CONN_DST_ATTENUATION",
    "CONN_DST_CENTER",
    "CONN_DST_CHORUS",
    "CONN_DST_EG1_ATTACKTIME",
    "CONN_DST_EG1_DECAYTIME",
    "CONN_DST_EG1_DELAYTIME",
    "CONN_DST_EG1_HOLDTIME",
    "CONN_DST_EG1_RELEASETIME",
    "CONN_DST_EG1_SHUTDOWNTIME",
    "CONN_DST_EG1_SUSTAINLEVEL",
    "CONN_DST_EG2_ATTACKTIME",
    "CONN_DST_EG2_DECAYTIME",
    "CONN_DST_EG2_DELAYTIME",
    "CONN_DST_EG2_HOLDTIME",
    "CONN_DST_EG2_RELEASETIME",
    "CONN_DST_EG2_SUSTAINLEVEL",
    "CONN_DST_FILTER_CUTOFF",
    "CONN_DST_FILTER_Q",
    "CONN_DST_GAIN",
    "CONN_DST_KEYNUMBER",
    "CONN_DST_LEFT",
    "CONN_DST_LEFTREAR",
    "CONN_DST_LFE_CHANNEL",
    "CONN_DST_LFO_FREQUENCY",
    "CONN_DST_LFO_STARTDELAY",
    "CONN_DST_NONE",
    "CONN_DST_PAN",
    "CONN_DST_PITCH",
    "CONN_DST_REVERB",
    "CONN_DST_RIGHT",
    "CONN_DST_RIGHTREAR",
    "CONN_DST_VIB_FREQUENCY",
    "CONN_DST_VIB_STARTDELAY",
    "CONN_SRC_CC1",
    "CONN_SRC_CC10",
    "CONN_SRC_CC11",
    "CONN_SRC_CC7",
    "CONN_SRC_CC91",
    "CONN_SRC_CC93",
    "CONN_SRC_CHANNELPRESSURE",
    "CONN_SRC_EG1",
    "CONN_SRC_EG2",
    "CONN_SRC_KEYNUMBER",
    "CONN_SRC_KEYONVELOCITY",
    "CONN_SRC_LFO",
    "CONN_SRC_MONOPRESSURE",
    "CONN_SRC_NONE",
    "CONN_SRC_PITCHWHEEL",
    "CONN_SRC_POLYPRESSURE",
    "CONN_SRC_VIBRATO",
    "CONN_TRN_CONCAVE",
    "CONN_TRN_CONVEX",
    "CONN_TRN_NONE",
    "CONN_TRN_SWITCH",
    "DAUD_CHAN10_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN11_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN12_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN13_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN14_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN15_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN16_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN1_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN2_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN3_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN4_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN5_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN6_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN7_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN8_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN9_VOICE_PRIORITY_OFFSET",
    "DAUD_CRITICAL_VOICE_PRIORITY",
    "DAUD_HIGH_VOICE_PRIORITY",
    "DAUD_LOW_VOICE_PRIORITY",
    "DAUD_PERSIST_VOICE_PRIORITY",
    "DAUD_STANDARD_VOICE_PRIORITY",
    "DIRECTSOUNDDEVICE_DATAFLOW",
    "DIRECTSOUNDDEVICE_DATAFLOW_CAPTURE",
    "DIRECTSOUNDDEVICE_DATAFLOW_RENDER",
    "DIRECTSOUNDDEVICE_TYPE",
    "DIRECTSOUNDDEVICE_TYPE_EMULATED",
    "DIRECTSOUNDDEVICE_TYPE_VXD",
    "DIRECTSOUNDDEVICE_TYPE_WDM",
    "DLSHEADER",
    "DLSID",
    "DLSID_GMInHardware",
    "DLSID_GSInHardware",
    "DLSID_ManufacturersID",
    "DLSID_ProductID",
    "DLSID_SampleMemorySize",
    "DLSID_SamplePlaybackRate",
    "DLSID_SupportsDLS1",
    "DLSID_SupportsDLS2",
    "DLSID_XGInHardware",
    "DLSVERSION",
    "DLS_CDL_ADD",
    "DLS_CDL_AND",
    "DLS_CDL_CONST",
    "DLS_CDL_DIVIDE",
    "DLS_CDL_EQ",
    "DLS_CDL_GE",
    "DLS_CDL_GT",
    "DLS_CDL_LE",
    "DLS_CDL_LOGICAL_AND",
    "DLS_CDL_LOGICAL_OR",
    "DLS_CDL_LT",
    "DLS_CDL_MULTIPLY",
    "DLS_CDL_NOT",
    "DLS_CDL_OR",
    "DLS_CDL_QUERY",
    "DLS_CDL_QUERYSUPPORTED",
    "DLS_CDL_SUBTRACT",
    "DLS_CDL_XOR",
    "DMUS_ARTICPARAMS",
    "DMUS_ARTICULATION",
    "DMUS_ARTICULATION2",
    "DMUS_BUFFERDESC",
    "DMUS_CLOCKF_GLOBAL",
    "DMUS_CLOCKINFO7",
    "DMUS_CLOCKINFO8",
    "DMUS_CLOCKTYPE",
    "DMUS_CLOCK_SYSTEM",
    "DMUS_CLOCK_WAVE",
    "DMUS_COPYRIGHT",
    "DMUS_DEFAULT_SIZE_OFFSETTABLE",
    "DMUS_DOWNLOADINFO",
    "DMUS_DOWNLOADINFO_INSTRUMENT",
    "DMUS_DOWNLOADINFO_INSTRUMENT2",
    "DMUS_DOWNLOADINFO_ONESHOTWAVE",
    "DMUS_DOWNLOADINFO_STREAMINGWAVE",
    "DMUS_DOWNLOADINFO_WAVE",
    "DMUS_DOWNLOADINFO_WAVEARTICULATION",
    "DMUS_EFFECT_CHORUS",
    "DMUS_EFFECT_DELAY",
    "DMUS_EFFECT_NONE",
    "DMUS_EFFECT_REVERB",
    "DMUS_EVENTHEADER",
    "DMUS_EVENT_STRUCTURED",
    "DMUS_EXTENSIONCHUNK",
    "DMUS_INSTRUMENT",
    "DMUS_INSTRUMENT_GM_INSTRUMENT",
    "DMUS_LFOPARAMS",
    "DMUS_MAX_DESCRIPTION",
    "DMUS_MAX_DRIVER",
    "DMUS_MIN_DATA_SIZE",
    "DMUS_MSCPARAMS",
    "DMUS_NOTERANGE",
    "DMUS_OFFSETTABLE",
    "DMUS_PC_AUDIOPATH",
    "DMUS_PC_DIRECTSOUND",
    "DMUS_PC_DLS",
    "DMUS_PC_DLS2",
    "DMUS_PC_EXTERNAL",
    "DMUS_PC_GMINHARDWARE",
    "DMUS_PC_GSINHARDWARE",
    "DMUS_PC_INPUTCLASS",
    "DMUS_PC_MEMORYSIZEFIXED",
    "DMUS_PC_OUTPUTCLASS",
    "DMUS_PC_SHAREABLE",
    "DMUS_PC_SOFTWARESYNTH",
    "DMUS_PC_SYSTEMMEMORY",
    "DMUS_PC_WAVE",
    "DMUS_PC_XGINHARDWARE",
    "DMUS_PEGPARAMS",
    "DMUS_PORTCAPS",
    "DMUS_PORTPARAMS7",
    "DMUS_PORTPARAMS8",
    "DMUS_PORTPARAMS_AUDIOCHANNELS",
    "DMUS_PORTPARAMS_CHANNELGROUPS",
    "DMUS_PORTPARAMS_EFFECTS",
    "DMUS_PORTPARAMS_FEATURES",
    "DMUS_PORTPARAMS_SAMPLERATE",
    "DMUS_PORTPARAMS_SHARE",
    "DMUS_PORTPARAMS_VOICES",
    "DMUS_PORT_FEATURE_AUDIOPATH",
    "DMUS_PORT_FEATURE_STREAMING",
    "DMUS_PORT_KERNEL_MODE",
    "DMUS_PORT_USER_MODE_SYNTH",
    "DMUS_PORT_WINMM_DRIVER",
    "DMUS_REGION",
    "DMUS_SYNTHSTATS",
    "DMUS_SYNTHSTATS8",
    "DMUS_SYNTHSTATS_CPU_PER_VOICE",
    "DMUS_SYNTHSTATS_FREE_MEMORY",
    "DMUS_SYNTHSTATS_LOST_NOTES",
    "DMUS_SYNTHSTATS_PEAK_VOLUME",
    "DMUS_SYNTHSTATS_SYSTEMMEMORY",
    "DMUS_SYNTHSTATS_TOTAL_CPU",
    "DMUS_SYNTHSTATS_VOICES",
    "DMUS_VEGPARAMS",
    "DMUS_VOICE_STATE",
    "DMUS_VOLUME_MAX",
    "DMUS_VOLUME_MIN",
    "DMUS_WAVE",
    "DMUS_WAVEARTDL",
    "DMUS_WAVEDATA",
    "DMUS_WAVEDL",
    "DMUS_WAVES_REVERB_PARAMS",
    "DSBUSID_BACK_CENTER",
    "DSBUSID_BACK_LEFT",
    "DSBUSID_BACK_RIGHT",
    "DSBUSID_CHORUS_SEND",
    "DSBUSID_DYNAMIC_0",
    "DSBUSID_FIRST_SPKR_LOC",
    "DSBUSID_FRONT_CENTER",
    "DSBUSID_FRONT_LEFT",
    "DSBUSID_FRONT_LEFT_OF_CENTER",
    "DSBUSID_FRONT_RIGHT",
    "DSBUSID_FRONT_RIGHT_OF_CENTER",
    "DSBUSID_LAST_SPKR_LOC",
    "DSBUSID_LEFT",
    "DSBUSID_LOW_FREQUENCY",
    "DSBUSID_NULL",
    "DSBUSID_REVERB_SEND",
    "DSBUSID_RIGHT",
    "DSBUSID_SIDE_LEFT",
    "DSBUSID_SIDE_RIGHT",
    "DSBUSID_TOP_BACK_CENTER",
    "DSBUSID_TOP_BACK_LEFT",
    "DSBUSID_TOP_BACK_RIGHT",
    "DSBUSID_TOP_CENTER",
    "DSBUSID_TOP_FRONT_CENTER",
    "DSBUSID_TOP_FRONT_LEFT",
    "DSBUSID_TOP_FRONT_RIGHT",
    "DSPROPERTY_DIRECTSOUNDDEVICE",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA",
    "DSPROPSETID_DirectSoundDevice",
    "DVAudInfo",
    "DV_AUDIOMODE",
    "DV_AUDIOQU",
    "DV_AUDIOSMP",
    "DV_CAP_AUD12Bits",
    "DV_CAP_AUD16Bits",
    "DV_DVSD_NTSC_FRAMESIZE",
    "DV_DVSD_PAL_FRAMESIZE",
    "DV_HD",
    "DV_NTSC",
    "DV_NTSCPAL",
    "DV_PAL",
    "DV_SD",
    "DV_SL",
    "DV_SMCHN",
    "DV_STYPE",
    "F_INSTRUMENT_DRUMS",
    "F_RGN_OPTION_SELFNONEXCLUSIVE",
    "F_WAVELINK_MULTICHANNEL",
    "F_WAVELINK_PHASE_MASTER",
    "F_WSMP_NO_COMPRESSION",
    "F_WSMP_NO_TRUNCATION",
    "GUID_DMUS_PROP_DLS1",
    "GUID_DMUS_PROP_DLS2",
    "GUID_DMUS_PROP_Effects",
    "GUID_DMUS_PROP_GM_Hardware",
    "GUID_DMUS_PROP_GS_Capable",
    "GUID_DMUS_PROP_GS_Hardware",
    "GUID_DMUS_PROP_INSTRUMENT2",
    "GUID_DMUS_PROP_LegacyCaps",
    "GUID_DMUS_PROP_MemorySize",
    "GUID_DMUS_PROP_SampleMemorySize",
    "GUID_DMUS_PROP_SamplePlaybackRate",
    "GUID_DMUS_PROP_SetSynthSink",
    "GUID_DMUS_PROP_SinkUsesDSound",
    "GUID_DMUS_PROP_SynthSink_DSOUND",
    "GUID_DMUS_PROP_SynthSink_WAVE",
    "GUID_DMUS_PROP_Volume",
    "GUID_DMUS_PROP_WavesReverb",
    "GUID_DMUS_PROP_WriteLatency",
    "GUID_DMUS_PROP_WritePeriod",
    "GUID_DMUS_PROP_XG_Capable",
    "GUID_DMUS_PROP_XG_Hardware",
    "IDirectMusic",
    "IDirectMusic8",
    "IDirectMusicBuffer",
    "IDirectMusicCollection",
    "IDirectMusicDownload",
    "IDirectMusicDownloadedInstrument",
    "IDirectMusicInstrument",
    "IDirectMusicPort",
    "IDirectMusicPortDownload",
    "IDirectMusicSynth",
    "IDirectMusicSynth8",
    "IDirectMusicSynthSink",
    "IDirectMusicThru",
    "INSTHEADER",
    "LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1",
    "LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA",
    "LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW",
    "MDEVICECAPSEX",
    "MIDILOCALE",
    "MIDIOPENDESC",
    "POOLCUE",
    "POOLTABLE",
    "POOL_CUE_NULL",
    "REFRESH_F_LASTBUFFER",
    "REGSTR_PATH_SOFTWARESYNTHS",
    "RGNHEADER",
    "RGNRANGE",
    "SIZE_DVINFO",
    "WAVELINK",
    "WAVELINK_CHANNEL_LEFT",
    "WAVELINK_CHANNEL_RIGHT",
    "WLOOP",
    "WLOOP_TYPE_FORWARD",
    "WLOOP_TYPE_RELEASE",
    "WSMPL",
]
