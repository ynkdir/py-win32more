from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Media
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Audio.DirectMusic
import Windows.Win32.Media.Audio.DirectSound
import Windows.Win32.Media.Multimedia
import Windows.Win32.System.Com
import Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
class CONNECTION(EasyCastStructure):
    usSource: UInt16
    usControl: UInt16
    usDestination: UInt16
    usTransform: UInt16
    lScale: Int32
class CONNECTIONLIST(EasyCastStructure):
    cbSize: UInt32
    cConnections: UInt32
DIRECTSOUNDDEVICE_DATAFLOW = Int32
DIRECTSOUNDDEVICE_DATAFLOW_RENDER: DIRECTSOUNDDEVICE_DATAFLOW = 0
DIRECTSOUNDDEVICE_DATAFLOW_CAPTURE: DIRECTSOUNDDEVICE_DATAFLOW = 1
DIRECTSOUNDDEVICE_TYPE = Int32
DIRECTSOUNDDEVICE_TYPE_EMULATED: DIRECTSOUNDDEVICE_TYPE = 0
DIRECTSOUNDDEVICE_TYPE_VXD: DIRECTSOUNDDEVICE_TYPE = 1
DIRECTSOUNDDEVICE_TYPE_WDM: DIRECTSOUNDDEVICE_TYPE = 2
class DLSHEADER(EasyCastStructure):
    cInstruments: UInt32
class DLSID(EasyCastStructure):
    ulData1: UInt32
    usData2: UInt16
    usData3: UInt16
    abData4: Byte * 8
class DLSVERSION(EasyCastStructure):
    dwVersionMS: UInt32
    dwVersionLS: UInt32
class DMUS_ARTICPARAMS(EasyCastStructure):
    LFO: Windows.Win32.Media.Audio.DirectMusic.DMUS_LFOPARAMS
    VolEG: Windows.Win32.Media.Audio.DirectMusic.DMUS_VEGPARAMS
    PitchEG: Windows.Win32.Media.Audio.DirectMusic.DMUS_PEGPARAMS
    Misc: Windows.Win32.Media.Audio.DirectMusic.DMUS_MSCPARAMS
class DMUS_ARTICULATION(EasyCastStructure):
    ulArt1Idx: UInt32
    ulFirstExtCkIdx: UInt32
class DMUS_ARTICULATION2(EasyCastStructure):
    ulArtIdx: UInt32
    ulFirstExtCkIdx: UInt32
    ulNextArtIdx: UInt32
class DMUS_BUFFERDESC(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    guidBufferFormat: Guid
    cbBuffer: UInt32
class DMUS_CLOCKINFO7(EasyCastStructure):
    dwSize: UInt32
    ctType: Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKTYPE
    guidClock: Guid
    wszDescription: Char * 128
class DMUS_CLOCKINFO8(EasyCastStructure):
    dwSize: UInt32
    ctType: Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKTYPE
    guidClock: Guid
    wszDescription: Char * 128
    dwFlags: UInt32
DMUS_CLOCKTYPE = Int32
DMUS_CLOCK_SYSTEM: DMUS_CLOCKTYPE = 0
DMUS_CLOCK_WAVE: DMUS_CLOCKTYPE = 1
class DMUS_COPYRIGHT(EasyCastStructure):
    cbSize: UInt32
    byCopyright: Byte * 4
class DMUS_DOWNLOADINFO(EasyCastStructure):
    dwDLType: UInt32
    dwDLId: UInt32
    dwNumOffsetTableEntries: UInt32
    cbSize: UInt32
class DMUS_EVENTHEADER(EasyCastStructure):
    cbEvent: UInt32
    dwChannelGroup: UInt32
    rtDelta: Int64
    dwFlags: UInt32
    _pack_ = 4
class DMUS_EXTENSIONCHUNK(EasyCastStructure):
    cbSize: UInt32
    ulNextExtCkIdx: UInt32
    ExtCkID: UInt32
    byExtCk: Byte * 4
class DMUS_INSTRUMENT(EasyCastStructure):
    ulPatch: UInt32
    ulFirstRegionIdx: UInt32
    ulGlobalArtIdx: UInt32
    ulFirstExtCkIdx: UInt32
    ulCopyrightIdx: UInt32
    ulFlags: UInt32
class DMUS_LFOPARAMS(EasyCastStructure):
    pcFrequency: Int32
    tcDelay: Int32
    gcVolumeScale: Int32
    pcPitchScale: Int32
    gcMWToVolume: Int32
    pcMWToPitch: Int32
class DMUS_MSCPARAMS(EasyCastStructure):
    ptDefaultPan: Int32
class DMUS_NOTERANGE(EasyCastStructure):
    dwLowNote: UInt32
    dwHighNote: UInt32
class DMUS_OFFSETTABLE(EasyCastStructure):
    ulOffsetTable: UInt32 * 1
class DMUS_PEGPARAMS(EasyCastStructure):
    tcAttack: Int32
    tcDecay: Int32
    ptSustain: Int32
    tcRelease: Int32
    tcVel2Attack: Int32
    tcKey2Decay: Int32
    pcRange: Int32
class DMUS_PORTCAPS(EasyCastStructure):
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
class DMUS_PORTPARAMS7(EasyCastStructure):
    dwSize: UInt32
    dwValidParams: UInt32
    dwVoices: UInt32
    dwChannelGroups: UInt32
    dwAudioChannels: UInt32
    dwSampleRate: UInt32
    dwEffectFlags: UInt32
    fShare: Windows.Win32.Foundation.BOOL
class DMUS_PORTPARAMS8(EasyCastStructure):
    dwSize: UInt32
    dwValidParams: UInt32
    dwVoices: UInt32
    dwChannelGroups: UInt32
    dwAudioChannels: UInt32
    dwSampleRate: UInt32
    dwEffectFlags: UInt32
    fShare: Windows.Win32.Foundation.BOOL
    dwFeatures: UInt32
class DMUS_REGION(EasyCastStructure):
    RangeKey: Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
    RangeVelocity: Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
    fusOptions: UInt16
    usKeyGroup: UInt16
    ulRegionArtIdx: UInt32
    ulNextRegionIdx: UInt32
    ulFirstExtCkIdx: UInt32
    WaveLink: Windows.Win32.Media.Audio.DirectMusic.WAVELINK
    WSMP: Windows.Win32.Media.Audio.DirectMusic.WSMPL
    WLOOP: Windows.Win32.Media.Audio.DirectMusic.WLOOP * 1
class DMUS_SYNTHSTATS(EasyCastStructure):
    dwSize: UInt32
    dwValidStats: UInt32
    dwVoices: UInt32
    dwTotalCPU: UInt32
    dwCPUPerVoice: UInt32
    dwLostNotes: UInt32
    dwFreeMemory: UInt32
    lPeakVolume: Int32
class DMUS_SYNTHSTATS8(EasyCastStructure):
    dwSize: UInt32
    dwValidStats: UInt32
    dwVoices: UInt32
    dwTotalCPU: UInt32
    dwCPUPerVoice: UInt32
    dwLostNotes: UInt32
    dwFreeMemory: UInt32
    lPeakVolume: Int32
    dwSynthMemUse: UInt32
class DMUS_VEGPARAMS(EasyCastStructure):
    tcAttack: Int32
    tcDecay: Int32
    ptSustain: Int32
    tcRelease: Int32
    tcVel2Attack: Int32
    tcKey2Decay: Int32
class DMUS_VOICE_STATE(EasyCastStructure):
    bExists: Windows.Win32.Foundation.BOOL
    spPosition: UInt64
class DMUS_WAVE(EasyCastStructure):
    ulFirstExtCkIdx: UInt32
    ulCopyrightIdx: UInt32
    ulWaveDataIdx: UInt32
    WaveformatEx: Windows.Win32.Media.Audio.WAVEFORMATEX
class DMUS_WAVEARTDL(EasyCastStructure):
    ulDownloadIdIdx: UInt32
    ulBus: UInt32
    ulBuffers: UInt32
    ulMasterDLId: UInt32
    usOptions: UInt16
class DMUS_WAVEDATA(EasyCastStructure):
    cbSize: UInt32
    byData: Byte * 4
class DMUS_WAVEDL(EasyCastStructure):
    cbWaveData: UInt32
class DMUS_WAVES_REVERB_PARAMS(EasyCastStructure):
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
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA(EasyCastStructure):
    DeviceId: Guid
    DescriptionA: Windows.Win32.Foundation.CHAR * 256
    DescriptionW: Char * 256
    ModuleA: Windows.Win32.Foundation.CHAR * 260
    ModuleW: Char * 260
    Type: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    WaveDeviceId: UInt32
    Devnode: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA(EasyCastStructure):
    Type: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
    Description: Windows.Win32.Foundation.PSTR
    Module: Windows.Win32.Foundation.PSTR
    Interface: Windows.Win32.Foundation.PSTR
    WaveDeviceId: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA(EasyCastStructure):
    Type: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
    Description: Windows.Win32.Foundation.PWSTR
    Module: Windows.Win32.Foundation.PWSTR
    Interface: Windows.Win32.Foundation.PWSTR
    WaveDeviceId: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA(EasyCastStructure):
    Callback: Windows.Win32.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1
    Context: c_void_p
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA(EasyCastStructure):
    Callback: Windows.Win32.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA
    Context: c_void_p
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA(EasyCastStructure):
    Callback: Windows.Win32.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW
    Context: c_void_p
class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA(EasyCastStructure):
    DeviceName: Windows.Win32.Foundation.PSTR
    DataFlow: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA(EasyCastStructure):
    DeviceName: Windows.Win32.Foundation.PWSTR
    DataFlow: Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
class DVAudInfo(EasyCastStructure):
    bAudStyle: Byte * 2
    bAudQu: Byte * 2
    bNumAudPin: Byte
    wAvgSamplesPerPinPerFrm: UInt16 * 2
    wBlkMode: UInt16
    wDIFMode: UInt16
    wBlkDiv: UInt16
class IDirectMusic(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6536115a-7b2d-11d2-ba-18-00-00-f8-75-ac-12')
    @commethod(3)
    def EnumPort(self, dwIndex: UInt32, pPortCaps: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateMusicBuffer(self, pBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_BUFFERDESC_head), ppBuffer: POINTER(Windows.Win32.Media.Audio.DirectMusic.IDirectMusicBuffer_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreatePort(self, rclsidPort: POINTER(Guid), pPortParams: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTPARAMS8_head), ppPort: POINTER(Windows.Win32.Media.Audio.DirectMusic.IDirectMusicPort_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumMasterClock(self, dwIndex: UInt32, lpClockInfo: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKINFO8_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMasterClock(self, pguidClock: POINTER(Guid), ppReferenceClock: POINTER(Windows.Win32.Media.IReferenceClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetMasterClock(self, rguidClock: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Activate(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDefaultPort(self, pguidPort: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDirectSound(self, pDirectSound: Windows.Win32.Media.Audio.DirectSound.IDirectSound_head, hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusic8(c_void_p):
    extends: Windows.Win32.Media.Audio.DirectMusic.IDirectMusic
    Guid = Guid('2d3629f7-813d-4939-85-08-f0-5c-6b-75-fd-97')
    @commethod(12)
    def SetExternalMasterClock(self, pClock: Windows.Win32.Media.IReferenceClock_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2ac2878-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TotalTime(self, prtTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PackStructured(self, rt: Int64, dwChannelGroup: UInt32, dwChannelMessage: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PackUnstructured(self, rt: Int64, dwChannelGroup: UInt32, cb: UInt32, lpb: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResetReadPtr(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNextEvent(self, prt: POINTER(Int64), pdwChannelGroup: POINTER(UInt32), pdwLength: POINTER(UInt32), ppData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRawBufferPtr(self, ppData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStartTime(self, prt: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetUsedBytes(self, pcb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMaxBytes(self, pcb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetBufferFormat(self, pGuidFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetStartTime(self, rt: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetUsedBytes(self, cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2ac287c-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetInstrument(self, dwPatch: UInt32, ppInstrument: POINTER(Windows.Win32.Media.Audio.DirectMusic.IDirectMusicInstrument_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumInstrument(self, dwIndex: UInt32, pdwPatch: POINTER(UInt32), pwszName: Windows.Win32.Foundation.PWSTR, dwNameLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicDownload(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2ac287b-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetBuffer(self, ppvBuffer: POINTER(c_void_p), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicDownloadedInstrument(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2ac287e-b39b-11d1-87-04-00-60-08-93-b1-bd')
class IDirectMusicInstrument(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2ac287d-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetPatch(self, pdwPatch: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPatch(self, dwPatch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicPort(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('08f2d8c9-37c2-11d2-b9-f9-00-00-f8-75-ac-12')
    @commethod(3)
    def PlayBuffer(self, pBuffer: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetReadNotificationHandle(self, hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Read(self, pBuffer: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DownloadInstrument(self, pInstrument: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicInstrument_head, ppDownloadedInstrument: POINTER(Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument_head), pNoteRanges: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_NOTERANGE_head), dwNumNoteRanges: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnloadInstrument(self, pDownloadedInstrument: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLatencyClock(self, ppClock: POINTER(Windows.Win32.Media.IReferenceClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRunningStats(self, pStats: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_SYNTHSTATS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Compact(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCaps(self, pPortCaps: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeviceIoControl(self, dwIoControlCode: UInt32, lpInBuffer: c_void_p, nInBufferSize: UInt32, lpOutBuffer: c_void_p, nOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetNumChannelGroups(self, dwChannelGroups: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNumChannelGroups(self, pdwChannelGroups: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Activate(self, fActive: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, dwPriority: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, pdwPriority: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetDirectSound(self, pDirectSound: Windows.Win32.Media.Audio.DirectSound.IDirectSound_head, pDirectSoundBuffer: Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFormat(self, pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pdwWaveFormatExSize: POINTER(UInt32), pdwBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicPortDownload(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2ac287a-b39b-11d1-87-04-00-60-08-93-b1-bd')
    @commethod(3)
    def GetBuffer(self, dwDLId: UInt32, ppIDMDownload: POINTER(Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateBuffer(self, dwSize: UInt32, ppIDMDownload: POINTER(Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDLId(self, pdwStartDLId: POINTER(UInt32), dwCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAppend(self, pdwAppend: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Download(self, pIDMDownload: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Unload(self, pIDMDownload: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicSynth(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('09823661-5c85-11d2-af-a6-00-aa-00-24-d8-b6')
    @commethod(3)
    def Open(self, pPortParams: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTPARAMS8_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNumChannelGroups(self, dwGroups: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Download(self, phDownload: POINTER(Windows.Win32.Foundation.HANDLE), pvData: c_void_p, pbFree: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Unload(self, hDownload: Windows.Win32.Foundation.HANDLE, lpFreeHandle: IntPtr, hUserData: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PlayBuffer(self, rt: Int64, pbBuffer: POINTER(Byte), cbBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRunningStats(self, pStats: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_SYNTHSTATS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPortCaps(self, pCaps: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMasterClock(self, pClock: Windows.Win32.Media.IReferenceClock_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLatencyClock(self, ppClock: POINTER(Windows.Win32.Media.IReferenceClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Activate(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSynthSink(self, pSynthSink: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicSynthSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Render(self, pBuffer: POINTER(Int16), dwLength: UInt32, llPosition: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, dwPriority: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, pdwPriority: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFormat(self, pWaveFormatEx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pdwWaveFormatExSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAppend(self, pdwAppend: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicSynth8(c_void_p):
    extends: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicSynth
    Guid = Guid('53cab625-2711-4c9f-9d-e7-1b-7f-92-5f-6f-c8')
    @commethod(20)
    def PlayVoice(self, rt: Int64, dwVoiceId: UInt32, dwChannelGroup: UInt32, dwChannel: UInt32, dwDLId: UInt32, prPitch: Int32, vrVolume: Int32, stVoiceStart: UInt64, stLoopStart: UInt64, stLoopEnd: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def StopVoice(self, rt: Int64, dwVoiceId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetVoiceState(self, dwVoice: POINTER(UInt32), cbVoice: UInt32, dwVoiceState: POINTER(Windows.Win32.Media.Audio.DirectMusic.DMUS_VOICE_STATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Refresh(self, dwDownloadID: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def AssignChannelToBuses(self, dwChannelGroup: UInt32, dwChannel: UInt32, pdwBuses: POINTER(UInt32), cBuses: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicSynthSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('09823663-5c85-11d2-af-a6-00-aa-00-24-d8-b6')
    @commethod(3)
    def Init(self, pSynth: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicSynth_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMasterClock(self, pClock: Windows.Win32.Media.IReferenceClock_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatencyClock(self, ppClock: POINTER(Windows.Win32.Media.IReferenceClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SampleToRefTime(self, llSampleTime: Int64, prfTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RefTimeToSample(self, rfTime: Int64, pllSampleTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetDirectSound(self, pDirectSound: Windows.Win32.Media.Audio.DirectSound.IDirectSound_head, pDirectSoundBuffer: Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDesiredBufferSize(self, pdwBufferSizeInSamples: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicThru(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ced153e7-3606-11d2-b9-f9-00-00-f8-75-ac-12')
    @commethod(3)
    def ThruChannel(self, dwSourceChannelGroup: UInt32, dwSourceChannel: UInt32, dwDestinationChannelGroup: UInt32, dwDestinationChannel: UInt32, pDestinationPort: Windows.Win32.Media.Audio.DirectMusic.IDirectMusicPort_head) -> Windows.Win32.Foundation.HRESULT: ...
class INSTHEADER(EasyCastStructure):
    cRegions: UInt32
    Locale: Windows.Win32.Media.Audio.DirectMusic.MIDILOCALE
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1(param0: POINTER(Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA_head), param1: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA(param0: POINTER(Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA_head), param1: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW(param0: POINTER(Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA_head), param1: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
class MDEVICECAPSEX(EasyCastStructure):
    cbSize: UInt32
    pCaps: c_void_p
    _pack_ = 1
class MIDILOCALE(EasyCastStructure):
    ulBank: UInt32
    ulInstrument: UInt32
class MIDIOPENDESC(EasyCastStructure):
    hMidi: Windows.Win32.Media.Audio.HMIDI
    dwCallback: UIntPtr
    dwInstance: UIntPtr
    dnDevNode: UIntPtr
    cIds: UInt32
    rgIds: Windows.Win32.Media.Multimedia.MIDIOPENSTRMID * 1
    _pack_ = 1
class POOLCUE(EasyCastStructure):
    ulOffset: UInt32
class POOLTABLE(EasyCastStructure):
    cbSize: UInt32
    cCues: UInt32
class RGNHEADER(EasyCastStructure):
    RangeKey: Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
    RangeVelocity: Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
    fusOptions: UInt16
    usKeyGroup: UInt16
class RGNRANGE(EasyCastStructure):
    usLow: UInt16
    usHigh: UInt16
class WAVELINK(EasyCastStructure):
    fusOptions: UInt16
    usPhaseGroup: UInt16
    ulChannel: UInt32
    ulTableIndex: UInt32
class WLOOP(EasyCastStructure):
    cbSize: UInt32
    ulType: UInt32
    ulStart: UInt32
    ulLength: UInt32
class WSMPL(EasyCastStructure):
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
