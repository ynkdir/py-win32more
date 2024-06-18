from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Audio.DirectMusic
import win32more.Windows.Win32.Media.Audio.DirectSound
import win32more.Windows.Win32.Media.Multimedia
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.IO
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
CLSID_DirectMusic: Guid = Guid('{636b9f10-0c7d-11d1-95b2-0020afdc7421}')
CLSID_DirectMusicCollection: Guid = Guid('{480ff4b0-28b2-11d1-bef7-00c04fbf8fef}')
CLSID_DirectMusicSynth: Guid = Guid('{58c2b4d0-46e7-11d1-89ac-00a0c9054129}')
GUID_DMUS_PROP_GM_Hardware: Guid = Guid('{178f2f24-c364-11d1-a760-0000f875ac12}')
GUID_DMUS_PROP_GS_Hardware: Guid = Guid('{178f2f25-c364-11d1-a760-0000f875ac12}')
GUID_DMUS_PROP_XG_Hardware: Guid = Guid('{178f2f26-c364-11d1-a760-0000f875ac12}')
GUID_DMUS_PROP_XG_Capable: Guid = Guid('{6496aba1-61b0-11d2-afa6-00aa0024d8b6}')
GUID_DMUS_PROP_GS_Capable: Guid = Guid('{6496aba2-61b0-11d2-afa6-00aa0024d8b6}')
GUID_DMUS_PROP_DLS1: Guid = Guid('{178f2f27-c364-11d1-a760-0000f875ac12}')
GUID_DMUS_PROP_DLS2: Guid = Guid('{f14599e5-4689-11d2-afa6-00aa0024d8b6}')
GUID_DMUS_PROP_INSTRUMENT2: Guid = Guid('{865fd372-9f67-11d2-872a-00600893b1bd}')
GUID_DMUS_PROP_SynthSink_DSOUND: Guid = Guid('{0aa97844-c877-11d1-870c-00600893b1bd}')
GUID_DMUS_PROP_SynthSink_WAVE: Guid = Guid('{0aa97845-c877-11d1-870c-00600893b1bd}')
GUID_DMUS_PROP_SampleMemorySize: Guid = Guid('{178f2f28-c364-11d1-a760-0000f875ac12}')
GUID_DMUS_PROP_SamplePlaybackRate: Guid = Guid('{2a91f713-a4bf-11d2-bbdf-00600833dbd8}')
GUID_DMUS_PROP_WriteLatency: Guid = Guid('{268a0fa0-60f2-11d2-afa6-00aa0024d8b6}')
GUID_DMUS_PROP_WritePeriod: Guid = Guid('{268a0fa1-60f2-11d2-afa6-00aa0024d8b6}')
GUID_DMUS_PROP_MemorySize: Guid = Guid('{178f2f28-c364-11d1-a760-0000f875ac12}')
GUID_DMUS_PROP_WavesReverb: Guid = Guid('{04cb5622-32e5-11d2-afa6-00aa0024d8b6}')
GUID_DMUS_PROP_Effects: Guid = Guid('{cda8d611-684a-11d2-871e-00600893b1bd}')
GUID_DMUS_PROP_LegacyCaps: Guid = Guid('{cfa7cdc2-00a1-11d2-aad5-0000f875ac12}')
GUID_DMUS_PROP_Volume: Guid = Guid('{fedfae25-e46e-11d1-aace-0000f875ac12}')
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
DLSID_GMInHardware: Guid = Guid('{178f2f24-c364-11d1-a760-0000f875ac12}')
DLSID_GSInHardware: Guid = Guid('{178f2f25-c364-11d1-a760-0000f875ac12}')
DLSID_XGInHardware: Guid = Guid('{178f2f26-c364-11d1-a760-0000f875ac12}')
DLSID_SupportsDLS1: Guid = Guid('{178f2f27-c364-11d1-a760-0000f875ac12}')
DLSID_SupportsDLS2: Guid = Guid('{f14599e5-4689-11d2-afa6-00aa0024d8b6}')
DLSID_SampleMemorySize: Guid = Guid('{178f2f28-c364-11d1-a760-0000f875ac12}')
DLSID_ManufacturersID: Guid = Guid('{b03e1181-8095-11d2-a1ef-00600833dbd8}')
DLSID_ProductID: Guid = Guid('{b03e1182-8095-11d2-a1ef-00600833dbd8}')
DLSID_SamplePlaybackRate: Guid = Guid('{2a91f713-a4bf-11d2-bbdf-00600833dbd8}')
REGSTR_PATH_SOFTWARESYNTHS: String = 'Software\\Microsoft\\DirectMusic\\SoftwareSynths'
REFRESH_F_LASTBUFFER: UInt32 = 1
CLSID_DirectMusicSynthSink: Guid = Guid('{aec17ce3-a514-11d1-afa6-00aa0024d8b6}')
GUID_DMUS_PROP_SetSynthSink: Guid = Guid('{0a3a5ba5-37b6-11d2-b9f9-0000f875ac12}')
GUID_DMUS_PROP_SinkUsesDSound: Guid = Guid('{be208857-8952-11d2-ba1c-0000f875ac12}')
CLSID_DirectSoundPrivate: Guid = Guid('{11ab3ec0-25ec-11d1-a4d8-00c04fc28aca}')
DSPROPSETID_DirectSoundDevice: Guid = Guid('{84624f82-25ec-11d1-a4d8-00c04fc28aca}')
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
DIRECTSOUNDDEVICE_DATAFLOW_RENDER: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW = 0
DIRECTSOUNDDEVICE_DATAFLOW_CAPTURE: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW = 1
DIRECTSOUNDDEVICE_TYPE = Int32
DIRECTSOUNDDEVICE_TYPE_EMULATED: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE = 0
DIRECTSOUNDDEVICE_TYPE_VXD: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE = 1
DIRECTSOUNDDEVICE_TYPE_WDM: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE = 2
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
    LFO: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_LFOPARAMS
    VolEG: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_VEGPARAMS
    PitchEG: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_PEGPARAMS
    Misc: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_MSCPARAMS
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
    ctType: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKTYPE
    guidClock: Guid
    wszDescription: Char * 128
class DMUS_CLOCKINFO8(Structure):
    dwSize: UInt32
    ctType: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKTYPE
    guidClock: Guid
    wszDescription: Char * 128
    dwFlags: UInt32
DMUS_CLOCKTYPE = Int32
DMUS_CLOCK_SYSTEM: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKTYPE = 0
DMUS_CLOCK_WAVE: win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKTYPE = 1
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
    fShare: win32more.Windows.Win32.Foundation.BOOL
class DMUS_PORTPARAMS8(Structure):
    dwSize: UInt32
    dwValidParams: UInt32
    dwVoices: UInt32
    dwChannelGroups: UInt32
    dwAudioChannels: UInt32
    dwSampleRate: UInt32
    dwEffectFlags: UInt32
    fShare: win32more.Windows.Win32.Foundation.BOOL
    dwFeatures: UInt32
class DMUS_REGION(Structure):
    RangeKey: win32more.Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
    RangeVelocity: win32more.Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
    fusOptions: UInt16
    usKeyGroup: UInt16
    ulRegionArtIdx: UInt32
    ulNextRegionIdx: UInt32
    ulFirstExtCkIdx: UInt32
    WaveLink: win32more.Windows.Win32.Media.Audio.DirectMusic.WAVELINK
    WSMP: win32more.Windows.Win32.Media.Audio.DirectMusic.WSMPL
    WLOOP: win32more.Windows.Win32.Media.Audio.DirectMusic.WLOOP * 1
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
    bExists: win32more.Windows.Win32.Foundation.BOOL
    spPosition: UInt64
class DMUS_WAVE(Structure):
    ulFirstExtCkIdx: UInt32
    ulCopyrightIdx: UInt32
    ulWaveDataIdx: UInt32
    WaveformatEx: win32more.Windows.Win32.Media.Audio.WAVEFORMATEX
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
DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 1
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 2
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 3
DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 4
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 5
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 6
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 7
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W: win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE = 8
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA(Structure):
    DeviceId: Guid
    DescriptionA: win32more.Windows.Win32.Foundation.CHAR * 256
    DescriptionW: Char * 256
    ModuleA: win32more.Windows.Win32.Foundation.CHAR * 260
    ModuleW: Char * 260
    Type: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    WaveDeviceId: UInt32
    Devnode: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA(Structure):
    Type: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
    Description: win32more.Windows.Win32.Foundation.PSTR
    Module: win32more.Windows.Win32.Foundation.PSTR
    Interface: win32more.Windows.Win32.Foundation.PSTR
    WaveDeviceId: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA(Structure):
    Type: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE
    DataFlow: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
    Description: win32more.Windows.Win32.Foundation.PWSTR
    Module: win32more.Windows.Win32.Foundation.PWSTR
    Interface: win32more.Windows.Win32.Foundation.PWSTR
    WaveDeviceId: UInt32
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA(Structure):
    Callback: win32more.Windows.Win32.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1
    Context: VoidPtr
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA(Structure):
    Callback: win32more.Windows.Win32.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA
    Context: VoidPtr
class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA(Structure):
    Callback: win32more.Windows.Win32.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW
    Context: VoidPtr
class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA(Structure):
    DeviceName: win32more.Windows.Win32.Foundation.PSTR
    DataFlow: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA(Structure):
    DeviceName: win32more.Windows.Win32.Foundation.PWSTR
    DataFlow: win32more.Windows.Win32.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW
    DeviceId: Guid
class DVAudInfo(Structure):
    bAudStyle: Byte * 2
    bAudQu: Byte * 2
    bNumAudPin: Byte
    wAvgSamplesPerPinPerFrm: UInt16 * 2
    wBlkMode: UInt16
    wDIFMode: UInt16
    wBlkDiv: UInt16
class IDirectMusic(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6536115a-7b2d-11d2-ba18-0000f875ac12}')
    @commethod(3)
    def EnumPort(self, dwIndex: UInt32, pPortCaps: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTCAPS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateMusicBuffer(self, pBufferDesc: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_BUFFERDESC), ppBuffer: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicBuffer), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreatePort(self, rclsidPort: POINTER(Guid), pPortParams: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTPARAMS8), ppPort: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicPort), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumMasterClock(self, dwIndex: UInt32, lpClockInfo: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_CLOCKINFO8)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMasterClock(self, pguidClock: POINTER(Guid), ppReferenceClock: POINTER(win32more.Windows.Win32.Media.IReferenceClock)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetMasterClock(self, rguidClock: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Activate(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDefaultPort(self, pguidPort: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDirectSound(self, pDirectSound: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSound, hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusic8(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusic
    _iid_ = Guid('{2d3629f7-813d-4939-8508-f05c6b75fd97}')
    @commethod(12)
    def SetExternalMasterClock(self, pClock: win32more.Windows.Win32.Media.IReferenceClock) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2ac2878-b39b-11d1-8704-00600893b1bd}')
    @commethod(3)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TotalTime(self, prtTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PackStructured(self, rt: Int64, dwChannelGroup: UInt32, dwChannelMessage: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PackUnstructured(self, rt: Int64, dwChannelGroup: UInt32, cb: UInt32, lpb: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResetReadPtr(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNextEvent(self, prt: POINTER(Int64), pdwChannelGroup: POINTER(UInt32), pdwLength: POINTER(UInt32), ppData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRawBufferPtr(self, ppData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStartTime(self, prt: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetUsedBytes(self, pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMaxBytes(self, pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetBufferFormat(self, pGuidFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetStartTime(self, rt: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetUsedBytes(self, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2ac287c-b39b-11d1-8704-00600893b1bd}')
    @commethod(3)
    def GetInstrument(self, dwPatch: UInt32, ppInstrument: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicInstrument)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumInstrument(self, dwIndex: UInt32, pdwPatch: POINTER(UInt32), pwszName: win32more.Windows.Win32.Foundation.PWSTR, dwNameLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicDownload(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2ac287b-b39b-11d1-8704-00600893b1bd}')
    @commethod(3)
    def GetBuffer(self, ppvBuffer: POINTER(VoidPtr), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicDownloadedInstrument(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2ac287e-b39b-11d1-8704-00600893b1bd}')
class IDirectMusicInstrument(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2ac287d-b39b-11d1-8704-00600893b1bd}')
    @commethod(3)
    def GetPatch(self, pdwPatch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPatch(self, dwPatch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicPort(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08f2d8c9-37c2-11d2-b9f9-0000f875ac12}')
    @commethod(3)
    def PlayBuffer(self, pBuffer: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetReadNotificationHandle(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Read(self, pBuffer: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DownloadInstrument(self, pInstrument: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicInstrument, ppDownloadedInstrument: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument), pNoteRanges: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_NOTERANGE), dwNumNoteRanges: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnloadInstrument(self, pDownloadedInstrument: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLatencyClock(self, ppClock: POINTER(win32more.Windows.Win32.Media.IReferenceClock)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRunningStats(self, pStats: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_SYNTHSTATS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Compact(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCaps(self, pPortCaps: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTCAPS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeviceIoControl(self, dwIoControlCode: UInt32, lpInBuffer: VoidPtr, nInBufferSize: UInt32, lpOutBuffer: VoidPtr, nOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetNumChannelGroups(self, dwChannelGroups: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNumChannelGroups(self, pdwChannelGroups: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Activate(self, fActive: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, dwPriority: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, pdwPriority: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetDirectSound(self, pDirectSound: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSound, pDirectSoundBuffer: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFormat(self, pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pdwWaveFormatExSize: POINTER(UInt32), pdwBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicPortDownload(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2ac287a-b39b-11d1-8704-00600893b1bd}')
    @commethod(3)
    def GetBuffer(self, dwDLId: UInt32, ppIDMDownload: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateBuffer(self, dwSize: UInt32, ppIDMDownload: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDLId(self, pdwStartDLId: POINTER(UInt32), dwCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAppend(self, pdwAppend: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Download(self, pIDMDownload: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Unload(self, pIDMDownload: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicDownload) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicSynth(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09823661-5c85-11d2-afa6-00aa0024d8b6}')
    @commethod(3)
    def Open(self, pPortParams: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTPARAMS8)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNumChannelGroups(self, dwGroups: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Download(self, phDownload: POINTER(win32more.Windows.Win32.Foundation.HANDLE), pvData: VoidPtr, pbFree: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Unload(self, hDownload: win32more.Windows.Win32.Foundation.HANDLE, lpFreeHandle: IntPtr, hUserData: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PlayBuffer(self, rt: Int64, pbBuffer: POINTER(Byte), cbBuffer: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRunningStats(self, pStats: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_SYNTHSTATS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPortCaps(self, pCaps: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_PORTCAPS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMasterClock(self, pClock: win32more.Windows.Win32.Media.IReferenceClock) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLatencyClock(self, ppClock: POINTER(win32more.Windows.Win32.Media.IReferenceClock)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Activate(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSynthSink(self, pSynthSink: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicSynthSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Render(self, pBuffer: POINTER(Int16), dwLength: UInt32, llPosition: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, dwPriority: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetChannelPriority(self, dwChannelGroup: UInt32, dwChannel: UInt32, pdwPriority: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFormat(self, pWaveFormatEx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pdwWaveFormatExSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAppend(self, pdwAppend: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicSynth8(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicSynth
    _iid_ = Guid('{53cab625-2711-4c9f-9de7-1b7f925f6fc8}')
    @commethod(20)
    def PlayVoice(self, rt: Int64, dwVoiceId: UInt32, dwChannelGroup: UInt32, dwChannel: UInt32, dwDLId: UInt32, prPitch: Int32, vrVolume: Int32, stVoiceStart: UInt64, stLoopStart: UInt64, stLoopEnd: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def StopVoice(self, rt: Int64, dwVoiceId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetVoiceState(self, dwVoice: POINTER(UInt32), cbVoice: UInt32, dwVoiceState: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DMUS_VOICE_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Refresh(self, dwDownloadID: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def AssignChannelToBuses(self, dwChannelGroup: UInt32, dwChannel: UInt32, pdwBuses: POINTER(UInt32), cBuses: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicSynthSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09823663-5c85-11d2-afa6-00aa0024d8b6}')
    @commethod(3)
    def Init(self, pSynth: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicSynth) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMasterClock(self, pClock: win32more.Windows.Win32.Media.IReferenceClock) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatencyClock(self, ppClock: POINTER(win32more.Windows.Win32.Media.IReferenceClock)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SampleToRefTime(self, llSampleTime: Int64, prfTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RefTimeToSample(self, rfTime: Int64, pllSampleTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetDirectSound(self, pDirectSound: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSound, pDirectSoundBuffer: win32more.Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDesiredBufferSize(self, pdwBufferSizeInSamples: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirectMusicThru(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ced153e7-3606-11d2-b9f9-0000f875ac12}')
    @commethod(3)
    def ThruChannel(self, dwSourceChannelGroup: UInt32, dwSourceChannel: UInt32, dwDestinationChannelGroup: UInt32, dwDestinationChannel: UInt32, pDestinationPort: win32more.Windows.Win32.Media.Audio.DirectMusic.IDirectMusicPort) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INSTHEADER(Structure):
    cRegions: UInt32
    Locale: win32more.Windows.Win32.Media.Audio.DirectMusic.MIDILOCALE
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1(param0: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA), param1: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA(param0: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA), param1: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW(param0: POINTER(win32more.Windows.Win32.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA), param1: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK = UnicodeAlias('LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW')
class MDEVICECAPSEX(Structure):
    cbSize: UInt32
    pCaps: VoidPtr
    _pack_ = 1
class MIDILOCALE(Structure):
    ulBank: UInt32
    ulInstrument: UInt32
class MIDIOPENDESC(Structure):
    hMidi: win32more.Windows.Win32.Media.Audio.HMIDI
    dwCallback: UIntPtr
    dwInstance: UIntPtr
    dnDevNode: UIntPtr
    cIds: UInt32
    rgIds: win32more.Windows.Win32.Media.Multimedia.MIDIOPENSTRMID * 1
    _pack_ = 1
class POOLCUE(Structure):
    ulOffset: UInt32
class POOLTABLE(Structure):
    cbSize: UInt32
    cCues: UInt32
class RGNHEADER(Structure):
    RangeKey: win32more.Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
    RangeVelocity: win32more.Windows.Win32.Media.Audio.DirectMusic.RGNRANGE
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


make_ready(__name__)
