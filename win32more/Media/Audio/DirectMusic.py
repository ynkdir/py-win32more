from win32more import *
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
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
DMUS_MAX_DESCRIPTION = 128
DMUS_MAX_DRIVER = 128
DMUS_EFFECT_NONE = 0
DMUS_EFFECT_REVERB = 1
DMUS_EFFECT_CHORUS = 2
DMUS_EFFECT_DELAY = 4
DMUS_PC_INPUTCLASS = 0
DMUS_PC_OUTPUTCLASS = 1
DMUS_PC_DLS = 1
DMUS_PC_EXTERNAL = 2
DMUS_PC_SOFTWARESYNTH = 4
DMUS_PC_MEMORYSIZEFIXED = 8
DMUS_PC_GMINHARDWARE = 16
DMUS_PC_GSINHARDWARE = 32
DMUS_PC_XGINHARDWARE = 64
DMUS_PC_DIRECTSOUND = 128
DMUS_PC_SHAREABLE = 256
DMUS_PC_DLS2 = 512
DMUS_PC_AUDIOPATH = 1024
DMUS_PC_WAVE = 2048
DMUS_PC_SYSTEMMEMORY = 2147483647
DMUS_PORT_WINMM_DRIVER = 0
DMUS_PORT_USER_MODE_SYNTH = 1
DMUS_PORT_KERNEL_MODE = 2
DMUS_PORTPARAMS_VOICES = 1
DMUS_PORTPARAMS_CHANNELGROUPS = 2
DMUS_PORTPARAMS_AUDIOCHANNELS = 4
DMUS_PORTPARAMS_SAMPLERATE = 8
DMUS_PORTPARAMS_EFFECTS = 32
DMUS_PORTPARAMS_SHARE = 64
DMUS_PORTPARAMS_FEATURES = 128
DMUS_PORT_FEATURE_AUDIOPATH = 1
DMUS_PORT_FEATURE_STREAMING = 2
DMUS_SYNTHSTATS_VOICES = 1
DMUS_SYNTHSTATS_TOTAL_CPU = 2
DMUS_SYNTHSTATS_CPU_PER_VOICE = 4
DMUS_SYNTHSTATS_LOST_NOTES = 8
DMUS_SYNTHSTATS_PEAK_VOLUME = 16
DMUS_SYNTHSTATS_FREE_MEMORY = 32
DMUS_SYNTHSTATS_SYSTEMMEMORY = 2147483647
DMUS_CLOCKF_GLOBAL = 1
DSBUSID_FIRST_SPKR_LOC = 0
DSBUSID_FRONT_LEFT = 0
DSBUSID_LEFT = 0
DSBUSID_FRONT_RIGHT = 1
DSBUSID_RIGHT = 1
DSBUSID_FRONT_CENTER = 2
DSBUSID_LOW_FREQUENCY = 3
DSBUSID_BACK_LEFT = 4
DSBUSID_BACK_RIGHT = 5
DSBUSID_FRONT_LEFT_OF_CENTER = 6
DSBUSID_FRONT_RIGHT_OF_CENTER = 7
DSBUSID_BACK_CENTER = 8
DSBUSID_SIDE_LEFT = 9
DSBUSID_SIDE_RIGHT = 10
DSBUSID_TOP_CENTER = 11
DSBUSID_TOP_FRONT_LEFT = 12
DSBUSID_TOP_FRONT_CENTER = 13
DSBUSID_TOP_FRONT_RIGHT = 14
DSBUSID_TOP_BACK_LEFT = 15
DSBUSID_TOP_BACK_CENTER = 16
DSBUSID_TOP_BACK_RIGHT = 17
DSBUSID_LAST_SPKR_LOC = 17
DSBUSID_REVERB_SEND = 64
DSBUSID_CHORUS_SEND = 65
DSBUSID_DYNAMIC_0 = 512
DSBUSID_NULL = 4294967295
DAUD_CRITICAL_VOICE_PRIORITY = 4026531840
DAUD_HIGH_VOICE_PRIORITY = 3221225472
DAUD_STANDARD_VOICE_PRIORITY = 2147483648
DAUD_LOW_VOICE_PRIORITY = 1073741824
DAUD_PERSIST_VOICE_PRIORITY = 268435456
DAUD_CHAN1_VOICE_PRIORITY_OFFSET = 14
DAUD_CHAN2_VOICE_PRIORITY_OFFSET = 13
DAUD_CHAN3_VOICE_PRIORITY_OFFSET = 12
DAUD_CHAN4_VOICE_PRIORITY_OFFSET = 11
DAUD_CHAN5_VOICE_PRIORITY_OFFSET = 10
DAUD_CHAN6_VOICE_PRIORITY_OFFSET = 9
DAUD_CHAN7_VOICE_PRIORITY_OFFSET = 8
DAUD_CHAN8_VOICE_PRIORITY_OFFSET = 7
DAUD_CHAN9_VOICE_PRIORITY_OFFSET = 6
DAUD_CHAN10_VOICE_PRIORITY_OFFSET = 15
DAUD_CHAN11_VOICE_PRIORITY_OFFSET = 5
DAUD_CHAN12_VOICE_PRIORITY_OFFSET = 4
DAUD_CHAN13_VOICE_PRIORITY_OFFSET = 3
DAUD_CHAN14_VOICE_PRIORITY_OFFSET = 2
DAUD_CHAN15_VOICE_PRIORITY_OFFSET = 1
DAUD_CHAN16_VOICE_PRIORITY_OFFSET = 0
CLSID_DirectMusic = '636b9f10-0c7d-11d1-95b2-0020afdc7421'
CLSID_DirectMusicCollection = '480ff4b0-28b2-11d1-bef7-00c04fbf8fef'
CLSID_DirectMusicSynth = '58c2b4d0-46e7-11d1-89ac-00a0c9054129'
GUID_DMUS_PROP_GM_Hardware = '178f2f24-c364-11d1-a760-0000f875ac12'
GUID_DMUS_PROP_GS_Hardware = '178f2f25-c364-11d1-a760-0000f875ac12'
GUID_DMUS_PROP_XG_Hardware = '178f2f26-c364-11d1-a760-0000f875ac12'
GUID_DMUS_PROP_XG_Capable = '6496aba1-61b0-11d2-afa6-00aa0024d8b6'
GUID_DMUS_PROP_GS_Capable = '6496aba2-61b0-11d2-afa6-00aa0024d8b6'
GUID_DMUS_PROP_DLS1 = '178f2f27-c364-11d1-a760-0000f875ac12'
GUID_DMUS_PROP_DLS2 = 'f14599e5-4689-11d2-afa6-00aa0024d8b6'
GUID_DMUS_PROP_INSTRUMENT2 = '865fd372-9f67-11d2-872a-00600893b1bd'
GUID_DMUS_PROP_SynthSink_DSOUND = '0aa97844-c877-11d1-870c-00600893b1bd'
GUID_DMUS_PROP_SynthSink_WAVE = '0aa97845-c877-11d1-870c-00600893b1bd'
GUID_DMUS_PROP_SampleMemorySize = '178f2f28-c364-11d1-a760-0000f875ac12'
GUID_DMUS_PROP_SamplePlaybackRate = '2a91f713-a4bf-11d2-bbdf-00600833dbd8'
GUID_DMUS_PROP_WriteLatency = '268a0fa0-60f2-11d2-afa6-00aa0024d8b6'
GUID_DMUS_PROP_WritePeriod = '268a0fa1-60f2-11d2-afa6-00aa0024d8b6'
GUID_DMUS_PROP_MemorySize = '178f2f28-c364-11d1-a760-0000f875ac12'
GUID_DMUS_PROP_WavesReverb = '04cb5622-32e5-11d2-afa6-00aa0024d8b6'
GUID_DMUS_PROP_Effects = 'cda8d611-684a-11d2-871e-00600893b1bd'
GUID_DMUS_PROP_LegacyCaps = 'cfa7cdc2-00a1-11d2-aad5-0000f875ac12'
GUID_DMUS_PROP_Volume = 'fedfae25-e46e-11d1-aace-0000f875ac12'
DMUS_VOLUME_MAX = 2000
DMUS_VOLUME_MIN = -20000
DMUS_EVENT_STRUCTURED = 1
DMUS_DOWNLOADINFO_INSTRUMENT = 1
DMUS_DOWNLOADINFO_WAVE = 2
DMUS_DOWNLOADINFO_INSTRUMENT2 = 3
DMUS_DOWNLOADINFO_WAVEARTICULATION = 4
DMUS_DOWNLOADINFO_STREAMINGWAVE = 5
DMUS_DOWNLOADINFO_ONESHOTWAVE = 6
DMUS_DEFAULT_SIZE_OFFSETTABLE = 1
DMUS_INSTRUMENT_GM_INSTRUMENT = 1
DMUS_MIN_DATA_SIZE = 4
CONN_SRC_NONE = 0
CONN_SRC_LFO = 1
CONN_SRC_KEYONVELOCITY = 2
CONN_SRC_KEYNUMBER = 3
CONN_SRC_EG1 = 4
CONN_SRC_EG2 = 5
CONN_SRC_PITCHWHEEL = 6
CONN_SRC_CC1 = 129
CONN_SRC_CC7 = 135
CONN_SRC_CC10 = 138
CONN_SRC_CC11 = 139
CONN_DST_NONE = 0
CONN_DST_ATTENUATION = 1
CONN_DST_PITCH = 3
CONN_DST_PAN = 4
CONN_DST_LFO_FREQUENCY = 260
CONN_DST_LFO_STARTDELAY = 261
CONN_DST_EG1_ATTACKTIME = 518
CONN_DST_EG1_DECAYTIME = 519
CONN_DST_EG1_RELEASETIME = 521
CONN_DST_EG1_SUSTAINLEVEL = 522
CONN_DST_EG2_ATTACKTIME = 778
CONN_DST_EG2_DECAYTIME = 779
CONN_DST_EG2_RELEASETIME = 781
CONN_DST_EG2_SUSTAINLEVEL = 782
CONN_TRN_NONE = 0
CONN_TRN_CONCAVE = 1
F_INSTRUMENT_DRUMS = 2147483648
F_RGN_OPTION_SELFNONEXCLUSIVE = 1
WAVELINK_CHANNEL_LEFT = 1
WAVELINK_CHANNEL_RIGHT = 2
F_WAVELINK_PHASE_MASTER = 1
POOL_CUE_NULL = -1
F_WSMP_NO_TRUNCATION = 1
F_WSMP_NO_COMPRESSION = 2
WLOOP_TYPE_FORWARD = 0
CONN_SRC_POLYPRESSURE = 7
CONN_SRC_CHANNELPRESSURE = 8
CONN_SRC_VIBRATO = 9
CONN_SRC_MONOPRESSURE = 10
CONN_SRC_CC91 = 219
CONN_SRC_CC93 = 221
CONN_DST_GAIN = 1
CONN_DST_KEYNUMBER = 5
CONN_DST_LEFT = 16
CONN_DST_RIGHT = 17
CONN_DST_CENTER = 18
CONN_DST_LEFTREAR = 19
CONN_DST_RIGHTREAR = 20
CONN_DST_LFE_CHANNEL = 21
CONN_DST_CHORUS = 128
CONN_DST_REVERB = 129
CONN_DST_VIB_FREQUENCY = 276
CONN_DST_VIB_STARTDELAY = 277
CONN_DST_EG1_DELAYTIME = 523
CONN_DST_EG1_HOLDTIME = 524
CONN_DST_EG1_SHUTDOWNTIME = 525
CONN_DST_EG2_DELAYTIME = 783
CONN_DST_EG2_HOLDTIME = 784
CONN_DST_FILTER_CUTOFF = 1280
CONN_DST_FILTER_Q = 1281
CONN_TRN_CONVEX = 2
CONN_TRN_SWITCH = 3
DLS_CDL_AND = 1
DLS_CDL_OR = 2
DLS_CDL_XOR = 3
DLS_CDL_ADD = 4
DLS_CDL_SUBTRACT = 5
DLS_CDL_MULTIPLY = 6
DLS_CDL_DIVIDE = 7
DLS_CDL_LOGICAL_AND = 8
DLS_CDL_LOGICAL_OR = 9
DLS_CDL_LT = 10
DLS_CDL_LE = 11
DLS_CDL_GT = 12
DLS_CDL_GE = 13
DLS_CDL_EQ = 14
DLS_CDL_NOT = 15
DLS_CDL_CONST = 16
DLS_CDL_QUERY = 17
DLS_CDL_QUERYSUPPORTED = 18
WLOOP_TYPE_RELEASE = 2
F_WAVELINK_MULTICHANNEL = 2
DLSID_GMInHardware = '178f2f24-c364-11d1-a760-0000f875ac12'
DLSID_GSInHardware = '178f2f25-c364-11d1-a760-0000f875ac12'
DLSID_XGInHardware = '178f2f26-c364-11d1-a760-0000f875ac12'
DLSID_SupportsDLS1 = '178f2f27-c364-11d1-a760-0000f875ac12'
DLSID_SupportsDLS2 = 'f14599e5-4689-11d2-afa6-00aa0024d8b6'
DLSID_SampleMemorySize = '178f2f28-c364-11d1-a760-0000f875ac12'
DLSID_ManufacturersID = 'b03e1181-8095-11d2-a1ef-00600833dbd8'
DLSID_ProductID = 'b03e1182-8095-11d2-a1ef-00600833dbd8'
DLSID_SamplePlaybackRate = '2a91f713-a4bf-11d2-bbdf-00600833dbd8'
REFRESH_F_LASTBUFFER = 1
CLSID_DirectMusicSynthSink = 'aec17ce3-a514-11d1-afa6-00aa0024d8b6'
GUID_DMUS_PROP_SetSynthSink = '0a3a5ba5-37b6-11d2-b9f9-0000f875ac12'
GUID_DMUS_PROP_SinkUsesDSound = 'be208857-8952-11d2-ba1c-0000f875ac12'
CLSID_DirectSoundPrivate = '11ab3ec0-25ec-11d1-a4d8-00c04fc28aca'
DSPROPSETID_DirectSoundDevice = '84624f82-25ec-11d1-a4d8-00c04fc28aca'
DV_DVSD_NTSC_FRAMESIZE = 120000
DV_DVSD_PAL_FRAMESIZE = 144000
DV_SMCHN = 57344
DV_AUDIOMODE = 3840
DV_AUDIOSMP = 939524096
DV_AUDIOQU = 117440512
DV_NTSCPAL = 2097152
DV_STYPE = 2031616
DV_NTSC = 0
DV_PAL = 1
DV_SD = 0
DV_HD = 1
DV_SL = 2
DV_CAP_AUD16Bits = 0
DV_CAP_AUD12Bits = 1
SIZE_DVINFO = 32
def _define_DLSID_head():
    class DLSID(Structure):
        pass
    return DLSID
def _define_DLSID():
    DLSID = win32more.Media.Audio.DirectMusic.DLSID_head
    DLSID._fields_ = [
        ("ulData1", UInt32),
        ("usData2", UInt16),
        ("usData3", UInt16),
        ("abData4", Byte * 8),
    ]
    return DLSID
def _define_DLSVERSION_head():
    class DLSVERSION(Structure):
        pass
    return DLSVERSION
def _define_DLSVERSION():
    DLSVERSION = win32more.Media.Audio.DirectMusic.DLSVERSION_head
    DLSVERSION._fields_ = [
        ("dwVersionMS", UInt32),
        ("dwVersionLS", UInt32),
    ]
    return DLSVERSION
def _define_CONNECTION_head():
    class CONNECTION(Structure):
        pass
    return CONNECTION
def _define_CONNECTION():
    CONNECTION = win32more.Media.Audio.DirectMusic.CONNECTION_head
    CONNECTION._fields_ = [
        ("usSource", UInt16),
        ("usControl", UInt16),
        ("usDestination", UInt16),
        ("usTransform", UInt16),
        ("lScale", Int32),
    ]
    return CONNECTION
def _define_CONNECTIONLIST_head():
    class CONNECTIONLIST(Structure):
        pass
    return CONNECTIONLIST
def _define_CONNECTIONLIST():
    CONNECTIONLIST = win32more.Media.Audio.DirectMusic.CONNECTIONLIST_head
    CONNECTIONLIST._fields_ = [
        ("cbSize", UInt32),
        ("cConnections", UInt32),
    ]
    return CONNECTIONLIST
def _define_RGNRANGE_head():
    class RGNRANGE(Structure):
        pass
    return RGNRANGE
def _define_RGNRANGE():
    RGNRANGE = win32more.Media.Audio.DirectMusic.RGNRANGE_head
    RGNRANGE._fields_ = [
        ("usLow", UInt16),
        ("usHigh", UInt16),
    ]
    return RGNRANGE
def _define_MIDILOCALE_head():
    class MIDILOCALE(Structure):
        pass
    return MIDILOCALE
def _define_MIDILOCALE():
    MIDILOCALE = win32more.Media.Audio.DirectMusic.MIDILOCALE_head
    MIDILOCALE._fields_ = [
        ("ulBank", UInt32),
        ("ulInstrument", UInt32),
    ]
    return MIDILOCALE
def _define_RGNHEADER_head():
    class RGNHEADER(Structure):
        pass
    return RGNHEADER
def _define_RGNHEADER():
    RGNHEADER = win32more.Media.Audio.DirectMusic.RGNHEADER_head
    RGNHEADER._fields_ = [
        ("RangeKey", win32more.Media.Audio.DirectMusic.RGNRANGE),
        ("RangeVelocity", win32more.Media.Audio.DirectMusic.RGNRANGE),
        ("fusOptions", UInt16),
        ("usKeyGroup", UInt16),
    ]
    return RGNHEADER
def _define_INSTHEADER_head():
    class INSTHEADER(Structure):
        pass
    return INSTHEADER
def _define_INSTHEADER():
    INSTHEADER = win32more.Media.Audio.DirectMusic.INSTHEADER_head
    INSTHEADER._fields_ = [
        ("cRegions", UInt32),
        ("Locale", win32more.Media.Audio.DirectMusic.MIDILOCALE),
    ]
    return INSTHEADER
def _define_DLSHEADER_head():
    class DLSHEADER(Structure):
        pass
    return DLSHEADER
def _define_DLSHEADER():
    DLSHEADER = win32more.Media.Audio.DirectMusic.DLSHEADER_head
    DLSHEADER._fields_ = [
        ("cInstruments", UInt32),
    ]
    return DLSHEADER
def _define_WAVELINK_head():
    class WAVELINK(Structure):
        pass
    return WAVELINK
def _define_WAVELINK():
    WAVELINK = win32more.Media.Audio.DirectMusic.WAVELINK_head
    WAVELINK._fields_ = [
        ("fusOptions", UInt16),
        ("usPhaseGroup", UInt16),
        ("ulChannel", UInt32),
        ("ulTableIndex", UInt32),
    ]
    return WAVELINK
def _define_POOLCUE_head():
    class POOLCUE(Structure):
        pass
    return POOLCUE
def _define_POOLCUE():
    POOLCUE = win32more.Media.Audio.DirectMusic.POOLCUE_head
    POOLCUE._fields_ = [
        ("ulOffset", UInt32),
    ]
    return POOLCUE
def _define_POOLTABLE_head():
    class POOLTABLE(Structure):
        pass
    return POOLTABLE
def _define_POOLTABLE():
    POOLTABLE = win32more.Media.Audio.DirectMusic.POOLTABLE_head
    POOLTABLE._fields_ = [
        ("cbSize", UInt32),
        ("cCues", UInt32),
    ]
    return POOLTABLE
def _define__rwsmp_head():
    class _rwsmp(Structure):
        pass
    return _rwsmp
def _define__rwsmp():
    _rwsmp = win32more.Media.Audio.DirectMusic._rwsmp_head
    _rwsmp._fields_ = [
        ("cbSize", UInt32),
        ("usUnityNote", UInt16),
        ("sFineTune", Int16),
        ("lAttenuation", Int32),
        ("fulOptions", UInt32),
        ("cSampleLoops", UInt32),
    ]
    return _rwsmp
def _define__rloop_head():
    class _rloop(Structure):
        pass
    return _rloop
def _define__rloop():
    _rloop = win32more.Media.Audio.DirectMusic._rloop_head
    _rloop._fields_ = [
        ("cbSize", UInt32),
        ("ulType", UInt32),
        ("ulStart", UInt32),
        ("ulLength", UInt32),
    ]
    return _rloop
def _define_DMUS_DOWNLOADINFO_head():
    class DMUS_DOWNLOADINFO(Structure):
        pass
    return DMUS_DOWNLOADINFO
def _define_DMUS_DOWNLOADINFO():
    DMUS_DOWNLOADINFO = win32more.Media.Audio.DirectMusic.DMUS_DOWNLOADINFO_head
    DMUS_DOWNLOADINFO._fields_ = [
        ("dwDLType", UInt32),
        ("dwDLId", UInt32),
        ("dwNumOffsetTableEntries", UInt32),
        ("cbSize", UInt32),
    ]
    return DMUS_DOWNLOADINFO
def _define_DMUS_OFFSETTABLE_head():
    class DMUS_OFFSETTABLE(Structure):
        pass
    return DMUS_OFFSETTABLE
def _define_DMUS_OFFSETTABLE():
    DMUS_OFFSETTABLE = win32more.Media.Audio.DirectMusic.DMUS_OFFSETTABLE_head
    DMUS_OFFSETTABLE._fields_ = [
        ("ulOffsetTable", UInt32 * 0),
    ]
    return DMUS_OFFSETTABLE
def _define_DMUS_INSTRUMENT_head():
    class DMUS_INSTRUMENT(Structure):
        pass
    return DMUS_INSTRUMENT
def _define_DMUS_INSTRUMENT():
    DMUS_INSTRUMENT = win32more.Media.Audio.DirectMusic.DMUS_INSTRUMENT_head
    DMUS_INSTRUMENT._fields_ = [
        ("ulPatch", UInt32),
        ("ulFirstRegionIdx", UInt32),
        ("ulGlobalArtIdx", UInt32),
        ("ulFirstExtCkIdx", UInt32),
        ("ulCopyrightIdx", UInt32),
        ("ulFlags", UInt32),
    ]
    return DMUS_INSTRUMENT
def _define_DMUS_REGION_head():
    class DMUS_REGION(Structure):
        pass
    return DMUS_REGION
def _define_DMUS_REGION():
    DMUS_REGION = win32more.Media.Audio.DirectMusic.DMUS_REGION_head
    DMUS_REGION._fields_ = [
        ("RangeKey", win32more.Media.Audio.DirectMusic.RGNRANGE),
        ("RangeVelocity", win32more.Media.Audio.DirectMusic.RGNRANGE),
        ("fusOptions", UInt16),
        ("usKeyGroup", UInt16),
        ("ulRegionArtIdx", UInt32),
        ("ulNextRegionIdx", UInt32),
        ("ulFirstExtCkIdx", UInt32),
        ("WaveLink", win32more.Media.Audio.DirectMusic.WAVELINK),
        ("WSMP", win32more.Media.Audio.DirectMusic._rwsmp),
        ("WLOOP", win32more.Media.Audio.DirectMusic._rloop * 0),
    ]
    return DMUS_REGION
def _define_DMUS_LFOPARAMS_head():
    class DMUS_LFOPARAMS(Structure):
        pass
    return DMUS_LFOPARAMS
def _define_DMUS_LFOPARAMS():
    DMUS_LFOPARAMS = win32more.Media.Audio.DirectMusic.DMUS_LFOPARAMS_head
    DMUS_LFOPARAMS._fields_ = [
        ("pcFrequency", Int32),
        ("tcDelay", Int32),
        ("gcVolumeScale", Int32),
        ("pcPitchScale", Int32),
        ("gcMWToVolume", Int32),
        ("pcMWToPitch", Int32),
    ]
    return DMUS_LFOPARAMS
def _define_DMUS_VEGPARAMS_head():
    class DMUS_VEGPARAMS(Structure):
        pass
    return DMUS_VEGPARAMS
def _define_DMUS_VEGPARAMS():
    DMUS_VEGPARAMS = win32more.Media.Audio.DirectMusic.DMUS_VEGPARAMS_head
    DMUS_VEGPARAMS._fields_ = [
        ("tcAttack", Int32),
        ("tcDecay", Int32),
        ("ptSustain", Int32),
        ("tcRelease", Int32),
        ("tcVel2Attack", Int32),
        ("tcKey2Decay", Int32),
    ]
    return DMUS_VEGPARAMS
def _define_DMUS_PEGPARAMS_head():
    class DMUS_PEGPARAMS(Structure):
        pass
    return DMUS_PEGPARAMS
def _define_DMUS_PEGPARAMS():
    DMUS_PEGPARAMS = win32more.Media.Audio.DirectMusic.DMUS_PEGPARAMS_head
    DMUS_PEGPARAMS._fields_ = [
        ("tcAttack", Int32),
        ("tcDecay", Int32),
        ("ptSustain", Int32),
        ("tcRelease", Int32),
        ("tcVel2Attack", Int32),
        ("tcKey2Decay", Int32),
        ("pcRange", Int32),
    ]
    return DMUS_PEGPARAMS
def _define_DMUS_MSCPARAMS_head():
    class DMUS_MSCPARAMS(Structure):
        pass
    return DMUS_MSCPARAMS
def _define_DMUS_MSCPARAMS():
    DMUS_MSCPARAMS = win32more.Media.Audio.DirectMusic.DMUS_MSCPARAMS_head
    DMUS_MSCPARAMS._fields_ = [
        ("ptDefaultPan", Int32),
    ]
    return DMUS_MSCPARAMS
def _define_DMUS_ARTICPARAMS_head():
    class DMUS_ARTICPARAMS(Structure):
        pass
    return DMUS_ARTICPARAMS
def _define_DMUS_ARTICPARAMS():
    DMUS_ARTICPARAMS = win32more.Media.Audio.DirectMusic.DMUS_ARTICPARAMS_head
    DMUS_ARTICPARAMS._fields_ = [
        ("LFO", win32more.Media.Audio.DirectMusic.DMUS_LFOPARAMS),
        ("VolEG", win32more.Media.Audio.DirectMusic.DMUS_VEGPARAMS),
        ("PitchEG", win32more.Media.Audio.DirectMusic.DMUS_PEGPARAMS),
        ("Misc", win32more.Media.Audio.DirectMusic.DMUS_MSCPARAMS),
    ]
    return DMUS_ARTICPARAMS
def _define_DMUS_ARTICULATION_head():
    class DMUS_ARTICULATION(Structure):
        pass
    return DMUS_ARTICULATION
def _define_DMUS_ARTICULATION():
    DMUS_ARTICULATION = win32more.Media.Audio.DirectMusic.DMUS_ARTICULATION_head
    DMUS_ARTICULATION._fields_ = [
        ("ulArt1Idx", UInt32),
        ("ulFirstExtCkIdx", UInt32),
    ]
    return DMUS_ARTICULATION
def _define_DMUS_ARTICULATION2_head():
    class DMUS_ARTICULATION2(Structure):
        pass
    return DMUS_ARTICULATION2
def _define_DMUS_ARTICULATION2():
    DMUS_ARTICULATION2 = win32more.Media.Audio.DirectMusic.DMUS_ARTICULATION2_head
    DMUS_ARTICULATION2._fields_ = [
        ("ulArtIdx", UInt32),
        ("ulFirstExtCkIdx", UInt32),
        ("ulNextArtIdx", UInt32),
    ]
    return DMUS_ARTICULATION2
def _define_DMUS_EXTENSIONCHUNK_head():
    class DMUS_EXTENSIONCHUNK(Structure):
        pass
    return DMUS_EXTENSIONCHUNK
def _define_DMUS_EXTENSIONCHUNK():
    DMUS_EXTENSIONCHUNK = win32more.Media.Audio.DirectMusic.DMUS_EXTENSIONCHUNK_head
    DMUS_EXTENSIONCHUNK._fields_ = [
        ("cbSize", UInt32),
        ("ulNextExtCkIdx", UInt32),
        ("ExtCkID", UInt32),
        ("byExtCk", Byte * 4),
    ]
    return DMUS_EXTENSIONCHUNK
def _define_DMUS_COPYRIGHT_head():
    class DMUS_COPYRIGHT(Structure):
        pass
    return DMUS_COPYRIGHT
def _define_DMUS_COPYRIGHT():
    DMUS_COPYRIGHT = win32more.Media.Audio.DirectMusic.DMUS_COPYRIGHT_head
    DMUS_COPYRIGHT._fields_ = [
        ("cbSize", UInt32),
        ("byCopyright", Byte * 4),
    ]
    return DMUS_COPYRIGHT
def _define_DMUS_WAVEDATA_head():
    class DMUS_WAVEDATA(Structure):
        pass
    return DMUS_WAVEDATA
def _define_DMUS_WAVEDATA():
    DMUS_WAVEDATA = win32more.Media.Audio.DirectMusic.DMUS_WAVEDATA_head
    DMUS_WAVEDATA._fields_ = [
        ("cbSize", UInt32),
        ("byData", Byte * 4),
    ]
    return DMUS_WAVEDATA
def _define_DMUS_WAVE_head():
    class DMUS_WAVE(Structure):
        pass
    return DMUS_WAVE
def _define_DMUS_WAVE():
    DMUS_WAVE = win32more.Media.Audio.DirectMusic.DMUS_WAVE_head
    DMUS_WAVE._fields_ = [
        ("ulFirstExtCkIdx", UInt32),
        ("ulCopyrightIdx", UInt32),
        ("ulWaveDataIdx", UInt32),
        ("WaveformatEx", win32more.Media.Audio.WAVEFORMATEX),
    ]
    return DMUS_WAVE
def _define_DMUS_NOTERANGE_head():
    class DMUS_NOTERANGE(Structure):
        pass
    return DMUS_NOTERANGE
def _define_DMUS_NOTERANGE():
    DMUS_NOTERANGE = win32more.Media.Audio.DirectMusic.DMUS_NOTERANGE_head
    DMUS_NOTERANGE._fields_ = [
        ("dwLowNote", UInt32),
        ("dwHighNote", UInt32),
    ]
    return DMUS_NOTERANGE
def _define_DMUS_WAVEARTDL_head():
    class DMUS_WAVEARTDL(Structure):
        pass
    return DMUS_WAVEARTDL
def _define_DMUS_WAVEARTDL():
    DMUS_WAVEARTDL = win32more.Media.Audio.DirectMusic.DMUS_WAVEARTDL_head
    DMUS_WAVEARTDL._fields_ = [
        ("ulDownloadIdIdx", UInt32),
        ("ulBus", UInt32),
        ("ulBuffers", UInt32),
        ("ulMasterDLId", UInt32),
        ("usOptions", UInt16),
    ]
    return DMUS_WAVEARTDL
def _define_DMUS_WAVEDL_head():
    class DMUS_WAVEDL(Structure):
        pass
    return DMUS_WAVEDL
def _define_DMUS_WAVEDL():
    DMUS_WAVEDL = win32more.Media.Audio.DirectMusic.DMUS_WAVEDL_head
    DMUS_WAVEDL._fields_ = [
        ("cbWaveData", UInt32),
    ]
    return DMUS_WAVEDL
def _define_DMUS_EVENTHEADER_head():
    class DMUS_EVENTHEADER(Structure):
        pass
    return DMUS_EVENTHEADER
def _define_DMUS_EVENTHEADER():
    DMUS_EVENTHEADER = win32more.Media.Audio.DirectMusic.DMUS_EVENTHEADER_head
    DMUS_EVENTHEADER._pack_ = 4
    DMUS_EVENTHEADER._fields_ = [
        ("cbEvent", UInt32),
        ("dwChannelGroup", UInt32),
        ("rtDelta", Int64),
        ("dwFlags", UInt32),
    ]
    return DMUS_EVENTHEADER
def _define_DMUS_BUFFERDESC_head():
    class DMUS_BUFFERDESC(Structure):
        pass
    return DMUS_BUFFERDESC
def _define_DMUS_BUFFERDESC():
    DMUS_BUFFERDESC = win32more.Media.Audio.DirectMusic.DMUS_BUFFERDESC_head
    DMUS_BUFFERDESC._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("guidBufferFormat", Guid),
        ("cbBuffer", UInt32),
    ]
    return DMUS_BUFFERDESC
def _define_DMUS_PORTCAPS_head():
    class DMUS_PORTCAPS(Structure):
        pass
    return DMUS_PORTCAPS
def _define_DMUS_PORTCAPS():
    DMUS_PORTCAPS = win32more.Media.Audio.DirectMusic.DMUS_PORTCAPS_head
    DMUS_PORTCAPS._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("guidPort", Guid),
        ("dwClass", UInt32),
        ("dwType", UInt32),
        ("dwMemorySize", UInt32),
        ("dwMaxChannelGroups", UInt32),
        ("dwMaxVoices", UInt32),
        ("dwMaxAudioChannels", UInt32),
        ("dwEffectFlags", UInt32),
        ("wszDescription", Char * 128),
    ]
    return DMUS_PORTCAPS
def _define__DMUS_PORTPARAMS_head():
    class _DMUS_PORTPARAMS(Structure):
        pass
    return _DMUS_PORTPARAMS
def _define__DMUS_PORTPARAMS():
    _DMUS_PORTPARAMS = win32more.Media.Audio.DirectMusic._DMUS_PORTPARAMS_head
    _DMUS_PORTPARAMS._fields_ = [
        ("dwSize", UInt32),
        ("dwValidParams", UInt32),
        ("dwVoices", UInt32),
        ("dwChannelGroups", UInt32),
        ("dwAudioChannels", UInt32),
        ("dwSampleRate", UInt32),
        ("dwEffectFlags", UInt32),
        ("fShare", win32more.Foundation.BOOL),
    ]
    return _DMUS_PORTPARAMS
def _define_DMUS_PORTPARAMS8_head():
    class DMUS_PORTPARAMS8(Structure):
        pass
    return DMUS_PORTPARAMS8
def _define_DMUS_PORTPARAMS8():
    DMUS_PORTPARAMS8 = win32more.Media.Audio.DirectMusic.DMUS_PORTPARAMS8_head
    DMUS_PORTPARAMS8._fields_ = [
        ("dwSize", UInt32),
        ("dwValidParams", UInt32),
        ("dwVoices", UInt32),
        ("dwChannelGroups", UInt32),
        ("dwAudioChannels", UInt32),
        ("dwSampleRate", UInt32),
        ("dwEffectFlags", UInt32),
        ("fShare", win32more.Foundation.BOOL),
        ("dwFeatures", UInt32),
    ]
    return DMUS_PORTPARAMS8
def _define_DMUS_SYNTHSTATS_head():
    class DMUS_SYNTHSTATS(Structure):
        pass
    return DMUS_SYNTHSTATS
def _define_DMUS_SYNTHSTATS():
    DMUS_SYNTHSTATS = win32more.Media.Audio.DirectMusic.DMUS_SYNTHSTATS_head
    DMUS_SYNTHSTATS._fields_ = [
        ("dwSize", UInt32),
        ("dwValidStats", UInt32),
        ("dwVoices", UInt32),
        ("dwTotalCPU", UInt32),
        ("dwCPUPerVoice", UInt32),
        ("dwLostNotes", UInt32),
        ("dwFreeMemory", UInt32),
        ("lPeakVolume", Int32),
    ]
    return DMUS_SYNTHSTATS
def _define_DMUS_SYNTHSTATS8_head():
    class DMUS_SYNTHSTATS8(Structure):
        pass
    return DMUS_SYNTHSTATS8
def _define_DMUS_SYNTHSTATS8():
    DMUS_SYNTHSTATS8 = win32more.Media.Audio.DirectMusic.DMUS_SYNTHSTATS8_head
    DMUS_SYNTHSTATS8._fields_ = [
        ("dwSize", UInt32),
        ("dwValidStats", UInt32),
        ("dwVoices", UInt32),
        ("dwTotalCPU", UInt32),
        ("dwCPUPerVoice", UInt32),
        ("dwLostNotes", UInt32),
        ("dwFreeMemory", UInt32),
        ("lPeakVolume", Int32),
        ("dwSynthMemUse", UInt32),
    ]
    return DMUS_SYNTHSTATS8
def _define_DMUS_WAVES_REVERB_PARAMS_head():
    class DMUS_WAVES_REVERB_PARAMS(Structure):
        pass
    return DMUS_WAVES_REVERB_PARAMS
def _define_DMUS_WAVES_REVERB_PARAMS():
    DMUS_WAVES_REVERB_PARAMS = win32more.Media.Audio.DirectMusic.DMUS_WAVES_REVERB_PARAMS_head
    DMUS_WAVES_REVERB_PARAMS._fields_ = [
        ("fInGain", Single),
        ("fReverbMix", Single),
        ("fReverbTime", Single),
        ("fHighFreqRTRatio", Single),
    ]
    return DMUS_WAVES_REVERB_PARAMS
DMUS_CLOCKTYPE = Int32
DMUS_CLOCK_SYSTEM = 0
DMUS_CLOCK_WAVE = 1
def _define_DMUS_CLOCKINFO7_head():
    class DMUS_CLOCKINFO7(Structure):
        pass
    return DMUS_CLOCKINFO7
def _define_DMUS_CLOCKINFO7():
    DMUS_CLOCKINFO7 = win32more.Media.Audio.DirectMusic.DMUS_CLOCKINFO7_head
    DMUS_CLOCKINFO7._fields_ = [
        ("dwSize", UInt32),
        ("ctType", win32more.Media.Audio.DirectMusic.DMUS_CLOCKTYPE),
        ("guidClock", Guid),
        ("wszDescription", Char * 128),
    ]
    return DMUS_CLOCKINFO7
def _define_DMUS_CLOCKINFO8_head():
    class DMUS_CLOCKINFO8(Structure):
        pass
    return DMUS_CLOCKINFO8
def _define_DMUS_CLOCKINFO8():
    DMUS_CLOCKINFO8 = win32more.Media.Audio.DirectMusic.DMUS_CLOCKINFO8_head
    DMUS_CLOCKINFO8._fields_ = [
        ("dwSize", UInt32),
        ("ctType", win32more.Media.Audio.DirectMusic.DMUS_CLOCKTYPE),
        ("guidClock", Guid),
        ("wszDescription", Char * 128),
        ("dwFlags", UInt32),
    ]
    return DMUS_CLOCKINFO8
def _define_IDirectMusic_head():
    class IDirectMusic(win32more.System.Com.IUnknown_head):
        Guid = Guid('6536115a-7b2d-11d2-ba18-0000f875ac12')
    return IDirectMusic
def _define_IDirectMusic():
    IDirectMusic = win32more.Media.Audio.DirectMusic.IDirectMusic_head
    IDirectMusic.EnumPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTCAPS_head), use_last_error=False)(3, 'EnumPort', ((1, 'dwIndex'),(1, 'pPortCaps'),)))
    IDirectMusic.CreateMusicBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectMusic.DMUS_BUFFERDESC_head),POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicBuffer_head),win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'CreateMusicBuffer', ((1, 'pBufferDesc'),(1, 'ppBuffer'),(1, 'pUnkOuter'),)))
    IDirectMusic.CreatePort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTPARAMS8_head),POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicPort_head),win32more.System.Com.IUnknown_head, use_last_error=False)(5, 'CreatePort', ((1, 'rclsidPort'),(1, 'pPortParams'),(1, 'ppPort'),(1, 'pUnkOuter'),)))
    IDirectMusic.EnumMasterClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.DirectMusic.DMUS_CLOCKINFO8_head), use_last_error=False)(6, 'EnumMasterClock', ((1, 'dwIndex'),(1, 'lpClockInfo'),)))
    IDirectMusic.GetMasterClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.IReferenceClock_head), use_last_error=False)(7, 'GetMasterClock', ((1, 'pguidClock'),(1, 'ppReferenceClock'),)))
    IDirectMusic.SetMasterClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(8, 'SetMasterClock', ((1, 'rguidClock'),)))
    IDirectMusic.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'Activate', ((1, 'fEnable'),)))
    IDirectMusic.GetDefaultPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(10, 'GetDefaultPort', ((1, 'pguidPort'),)))
    IDirectMusic.SetDirectSound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.IDirectSound_head,win32more.Foundation.HWND, use_last_error=False)(11, 'SetDirectSound', ((1, 'pDirectSound'),(1, 'hWnd'),)))
    win32more.System.Com.IUnknown
    return IDirectMusic
def _define_IDirectMusic8_head():
    class IDirectMusic8(win32more.Media.Audio.DirectMusic.IDirectMusic_head):
        Guid = Guid('2d3629f7-813d-4939-8508-f05c6b75fd97')
    return IDirectMusic8
def _define_IDirectMusic8():
    IDirectMusic8 = win32more.Media.Audio.DirectMusic.IDirectMusic8_head
    IDirectMusic8.SetExternalMasterClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.IReferenceClock_head, use_last_error=False)(12, 'SetExternalMasterClock', ((1, 'pClock'),)))
    win32more.Media.Audio.DirectMusic.IDirectMusic
    return IDirectMusic8
def _define_IDirectMusicBuffer_head():
    class IDirectMusicBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2ac2878-b39b-11d1-8704-00600893b1bd')
    return IDirectMusicBuffer
def _define_IDirectMusicBuffer():
    IDirectMusicBuffer = win32more.Media.Audio.DirectMusic.IDirectMusicBuffer_head
    IDirectMusicBuffer.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Flush', ()))
    IDirectMusicBuffer.TotalTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(4, 'TotalTime', ((1, 'prtTime'),)))
    IDirectMusicBuffer.PackStructured = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,UInt32,UInt32, use_last_error=False)(5, 'PackStructured', ((1, 'rt'),(1, 'dwChannelGroup'),(1, 'dwChannelMessage'),)))
    IDirectMusicBuffer.PackUnstructured = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,UInt32,UInt32,c_char_p_no, use_last_error=False)(6, 'PackUnstructured', ((1, 'rt'),(1, 'dwChannelGroup'),(1, 'cb'),(1, 'lpb'),)))
    IDirectMusicBuffer.ResetReadPtr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'ResetReadPtr', ()))
    IDirectMusicBuffer.GetNextEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64),POINTER(UInt32),POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(8, 'GetNextEvent', ((1, 'prt'),(1, 'pdwChannelGroup'),(1, 'pdwLength'),(1, 'ppData'),)))
    IDirectMusicBuffer.GetRawBufferPtr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no), use_last_error=False)(9, 'GetRawBufferPtr', ((1, 'ppData'),)))
    IDirectMusicBuffer.GetStartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(10, 'GetStartTime', ((1, 'prt'),)))
    IDirectMusicBuffer.GetUsedBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetUsedBytes', ((1, 'pcb'),)))
    IDirectMusicBuffer.GetMaxBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetMaxBytes', ((1, 'pcb'),)))
    IDirectMusicBuffer.GetBufferFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(13, 'GetBufferFormat', ((1, 'pGuidFormat'),)))
    IDirectMusicBuffer.SetStartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64, use_last_error=False)(14, 'SetStartTime', ((1, 'rt'),)))
    IDirectMusicBuffer.SetUsedBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(15, 'SetUsedBytes', ((1, 'cb'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicBuffer
def _define_IDirectMusicInstrument_head():
    class IDirectMusicInstrument(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2ac287d-b39b-11d1-8704-00600893b1bd')
    return IDirectMusicInstrument
def _define_IDirectMusicInstrument():
    IDirectMusicInstrument = win32more.Media.Audio.DirectMusic.IDirectMusicInstrument_head
    IDirectMusicInstrument.GetPatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetPatch', ((1, 'pdwPatch'),)))
    IDirectMusicInstrument.SetPatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetPatch', ((1, 'dwPatch'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicInstrument
def _define_IDirectMusicDownloadedInstrument_head():
    class IDirectMusicDownloadedInstrument(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2ac287e-b39b-11d1-8704-00600893b1bd')
    return IDirectMusicDownloadedInstrument
def _define_IDirectMusicDownloadedInstrument():
    IDirectMusicDownloadedInstrument = win32more.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument_head
    win32more.System.Com.IUnknown
    return IDirectMusicDownloadedInstrument
def _define_IDirectMusicCollection_head():
    class IDirectMusicCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2ac287c-b39b-11d1-8704-00600893b1bd')
    return IDirectMusicCollection
def _define_IDirectMusicCollection():
    IDirectMusicCollection = win32more.Media.Audio.DirectMusic.IDirectMusicCollection_head
    IDirectMusicCollection.GetInstrument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicInstrument_head), use_last_error=False)(3, 'GetInstrument', ((1, 'dwPatch'),(1, 'ppInstrument'),)))
    IDirectMusicCollection.EnumInstrument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,UInt32, use_last_error=False)(4, 'EnumInstrument', ((1, 'dwIndex'),(1, 'pdwPatch'),(1, 'pwszName'),(1, 'dwNameLen'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicCollection
def _define_IDirectMusicDownload_head():
    class IDirectMusicDownload(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2ac287b-b39b-11d1-8704-00600893b1bd')
    return IDirectMusicDownload
def _define_IDirectMusicDownload():
    IDirectMusicDownload = win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head
    IDirectMusicDownload.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(3, 'GetBuffer', ((1, 'ppvBuffer'),(1, 'pdwSize'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicDownload
def _define_IDirectMusicPortDownload_head():
    class IDirectMusicPortDownload(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2ac287a-b39b-11d1-8704-00600893b1bd')
    return IDirectMusicPortDownload
def _define_IDirectMusicPortDownload():
    IDirectMusicPortDownload = win32more.Media.Audio.DirectMusic.IDirectMusicPortDownload_head
    IDirectMusicPortDownload.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head), use_last_error=False)(3, 'GetBuffer', ((1, 'dwDLId'),(1, 'ppIDMDownload'),)))
    IDirectMusicPortDownload.AllocateBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head), use_last_error=False)(4, 'AllocateBuffer', ((1, 'dwSize'),(1, 'ppIDMDownload'),)))
    IDirectMusicPortDownload.GetDLId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32, use_last_error=False)(5, 'GetDLId', ((1, 'pdwStartDLId'),(1, 'dwCount'),)))
    IDirectMusicPortDownload.GetAppend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetAppend', ((1, 'pdwAppend'),)))
    IDirectMusicPortDownload.Download = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head, use_last_error=False)(7, 'Download', ((1, 'pIDMDownload'),)))
    IDirectMusicPortDownload.Unload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicDownload_head, use_last_error=False)(8, 'Unload', ((1, 'pIDMDownload'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicPortDownload
def _define_IDirectMusicPort_head():
    class IDirectMusicPort(win32more.System.Com.IUnknown_head):
        Guid = Guid('08f2d8c9-37c2-11d2-b9f9-0000f875ac12')
    return IDirectMusicPort
def _define_IDirectMusicPort():
    IDirectMusicPort = win32more.Media.Audio.DirectMusic.IDirectMusicPort_head
    IDirectMusicPort.PlayBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicBuffer_head, use_last_error=False)(3, 'PlayBuffer', ((1, 'pBuffer'),)))
    IDirectMusicPort.SetReadNotificationHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(4, 'SetReadNotificationHandle', ((1, 'hEvent'),)))
    IDirectMusicPort.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicBuffer_head, use_last_error=False)(5, 'Read', ((1, 'pBuffer'),)))
    IDirectMusicPort.DownloadInstrument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicInstrument_head,POINTER(win32more.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument_head),POINTER(win32more.Media.Audio.DirectMusic.DMUS_NOTERANGE_head),UInt32, use_last_error=False)(6, 'DownloadInstrument', ((1, 'pInstrument'),(1, 'ppDownloadedInstrument'),(1, 'pNoteRanges'),(1, 'dwNumNoteRanges'),)))
    IDirectMusicPort.UnloadInstrument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicDownloadedInstrument_head, use_last_error=False)(7, 'UnloadInstrument', ((1, 'pDownloadedInstrument'),)))
    IDirectMusicPort.GetLatencyClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.IReferenceClock_head), use_last_error=False)(8, 'GetLatencyClock', ((1, 'ppClock'),)))
    IDirectMusicPort.GetRunningStats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectMusic.DMUS_SYNTHSTATS_head), use_last_error=False)(9, 'GetRunningStats', ((1, 'pStats'),)))
    IDirectMusicPort.Compact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Compact', ()))
    IDirectMusicPort.GetCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTCAPS_head), use_last_error=False)(11, 'GetCaps', ((1, 'pPortCaps'),)))
    IDirectMusicPort.DeviceIoControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(12, 'DeviceIoControl', ((1, 'dwIoControlCode'),(1, 'lpInBuffer'),(1, 'nInBufferSize'),(1, 'lpOutBuffer'),(1, 'nOutBufferSize'),(1, 'lpBytesReturned'),(1, 'lpOverlapped'),)))
    IDirectMusicPort.SetNumChannelGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(13, 'SetNumChannelGroups', ((1, 'dwChannelGroups'),)))
    IDirectMusicPort.GetNumChannelGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'GetNumChannelGroups', ((1, 'pdwChannelGroups'),)))
    IDirectMusicPort.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(15, 'Activate', ((1, 'fActive'),)))
    IDirectMusicPort.SetChannelPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(16, 'SetChannelPriority', ((1, 'dwChannelGroup'),(1, 'dwChannel'),(1, 'dwPriority'),)))
    IDirectMusicPort.GetChannelPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(17, 'GetChannelPriority', ((1, 'dwChannelGroup'),(1, 'dwChannel'),(1, 'pdwPriority'),)))
    IDirectMusicPort.SetDirectSound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.IDirectSound_head,win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head, use_last_error=False)(18, 'SetDirectSound', ((1, 'pDirectSound'),(1, 'pDirectSoundBuffer'),)))
    IDirectMusicPort.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.WAVEFORMATEX_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(19, 'GetFormat', ((1, 'pWaveFormatEx'),(1, 'pdwWaveFormatExSize'),(1, 'pdwBufferSize'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicPort
def _define_IDirectMusicThru_head():
    class IDirectMusicThru(win32more.System.Com.IUnknown_head):
        Guid = Guid('ced153e7-3606-11d2-b9f9-0000f875ac12')
    return IDirectMusicThru
def _define_IDirectMusicThru():
    IDirectMusicThru = win32more.Media.Audio.DirectMusic.IDirectMusicThru_head
    IDirectMusicThru.ThruChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,UInt32,win32more.Media.Audio.DirectMusic.IDirectMusicPort_head, use_last_error=False)(3, 'ThruChannel', ((1, 'dwSourceChannelGroup'),(1, 'dwSourceChannel'),(1, 'dwDestinationChannelGroup'),(1, 'dwDestinationChannel'),(1, 'pDestinationPort'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicThru
def _define_DMUS_VOICE_STATE_head():
    class DMUS_VOICE_STATE(Structure):
        pass
    return DMUS_VOICE_STATE
def _define_DMUS_VOICE_STATE():
    DMUS_VOICE_STATE = win32more.Media.Audio.DirectMusic.DMUS_VOICE_STATE_head
    DMUS_VOICE_STATE._fields_ = [
        ("bExists", win32more.Foundation.BOOL),
        ("spPosition", UInt64),
    ]
    return DMUS_VOICE_STATE
def _define_IDirectMusicSynth_head():
    class IDirectMusicSynth(win32more.System.Com.IUnknown_head):
        Guid = Guid('09823661-5c85-11d2-afa6-00aa0024d8b6')
    return IDirectMusicSynth
def _define_IDirectMusicSynth():
    IDirectMusicSynth = win32more.Media.Audio.DirectMusic.IDirectMusicSynth_head
    IDirectMusicSynth.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTPARAMS8_head), use_last_error=False)(3, 'Open', ((1, 'pPortParams'),)))
    IDirectMusicSynth.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IDirectMusicSynth.SetNumChannelGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetNumChannelGroups', ((1, 'dwGroups'),)))
    IDirectMusicSynth.Download = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE),c_void_p,POINTER(Int32), use_last_error=False)(6, 'Download', ((1, 'phDownload'),(1, 'pvData'),(1, 'pbFree'),)))
    IDirectMusicSynth.Unload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,IntPtr,win32more.Foundation.HANDLE, use_last_error=False)(7, 'Unload', ((1, 'hDownload'),(1, 'lpFreeHandle'),(1, 'hUserData'),)))
    IDirectMusicSynth.PlayBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,c_char_p_no,UInt32, use_last_error=False)(8, 'PlayBuffer', ((1, 'rt'),(1, 'pbBuffer'),(1, 'cbBuffer'),)))
    IDirectMusicSynth.GetRunningStats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectMusic.DMUS_SYNTHSTATS_head), use_last_error=False)(9, 'GetRunningStats', ((1, 'pStats'),)))
    IDirectMusicSynth.GetPortCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectMusic.DMUS_PORTCAPS_head), use_last_error=False)(10, 'GetPortCaps', ((1, 'pCaps'),)))
    IDirectMusicSynth.SetMasterClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.IReferenceClock_head, use_last_error=False)(11, 'SetMasterClock', ((1, 'pClock'),)))
    IDirectMusicSynth.GetLatencyClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.IReferenceClock_head), use_last_error=False)(12, 'GetLatencyClock', ((1, 'ppClock'),)))
    IDirectMusicSynth.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'Activate', ((1, 'fEnable'),)))
    IDirectMusicSynth.SetSynthSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicSynthSink_head, use_last_error=False)(14, 'SetSynthSink', ((1, 'pSynthSink'),)))
    IDirectMusicSynth.Render = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16),UInt32,Int64, use_last_error=False)(15, 'Render', ((1, 'pBuffer'),(1, 'dwLength'),(1, 'llPosition'),)))
    IDirectMusicSynth.SetChannelPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(16, 'SetChannelPriority', ((1, 'dwChannelGroup'),(1, 'dwChannel'),(1, 'dwPriority'),)))
    IDirectMusicSynth.GetChannelPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(17, 'GetChannelPriority', ((1, 'dwChannelGroup'),(1, 'dwChannel'),(1, 'pdwPriority'),)))
    IDirectMusicSynth.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.WAVEFORMATEX_head),POINTER(UInt32), use_last_error=False)(18, 'GetFormat', ((1, 'pWaveFormatEx'),(1, 'pdwWaveFormatExSize'),)))
    IDirectMusicSynth.GetAppend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(19, 'GetAppend', ((1, 'pdwAppend'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicSynth
def _define_IDirectMusicSynth8_head():
    class IDirectMusicSynth8(win32more.Media.Audio.DirectMusic.IDirectMusicSynth_head):
        Guid = Guid('53cab625-2711-4c9f-9de7-1b7f925f6fc8')
    return IDirectMusicSynth8
def _define_IDirectMusicSynth8():
    IDirectMusicSynth8 = win32more.Media.Audio.DirectMusic.IDirectMusicSynth8_head
    IDirectMusicSynth8.PlayVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,UInt32,UInt32,UInt32,UInt32,Int32,Int32,UInt64,UInt64,UInt64, use_last_error=False)(20, 'PlayVoice', ((1, 'rt'),(1, 'dwVoiceId'),(1, 'dwChannelGroup'),(1, 'dwChannel'),(1, 'dwDLId'),(1, 'prPitch'),(1, 'vrVolume'),(1, 'stVoiceStart'),(1, 'stLoopStart'),(1, 'stLoopEnd'),)))
    IDirectMusicSynth8.StopVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,UInt32, use_last_error=False)(21, 'StopVoice', ((1, 'rt'),(1, 'dwVoiceId'),)))
    IDirectMusicSynth8.GetVoiceState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.Media.Audio.DirectMusic.DMUS_VOICE_STATE_head), use_last_error=False)(22, 'GetVoiceState', ((1, 'dwVoice'),(1, 'cbVoice'),(1, 'dwVoiceState'),)))
    IDirectMusicSynth8.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(23, 'Refresh', ((1, 'dwDownloadID'),(1, 'dwFlags'),)))
    IDirectMusicSynth8.AssignChannelToBuses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(24, 'AssignChannelToBuses', ((1, 'dwChannelGroup'),(1, 'dwChannel'),(1, 'pdwBuses'),(1, 'cBuses'),)))
    win32more.Media.Audio.DirectMusic.IDirectMusicSynth
    return IDirectMusicSynth8
def _define_IDirectMusicSynthSink_head():
    class IDirectMusicSynthSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('09823663-5c85-11d2-afa6-00aa0024d8b6')
    return IDirectMusicSynthSink
def _define_IDirectMusicSynthSink():
    IDirectMusicSynthSink = win32more.Media.Audio.DirectMusic.IDirectMusicSynthSink_head
    IDirectMusicSynthSink.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectMusic.IDirectMusicSynth_head, use_last_error=False)(3, 'Init', ((1, 'pSynth'),)))
    IDirectMusicSynthSink.SetMasterClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.IReferenceClock_head, use_last_error=False)(4, 'SetMasterClock', ((1, 'pClock'),)))
    IDirectMusicSynthSink.GetLatencyClock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.IReferenceClock_head), use_last_error=False)(5, 'GetLatencyClock', ((1, 'ppClock'),)))
    IDirectMusicSynthSink.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'Activate', ((1, 'fEnable'),)))
    IDirectMusicSynthSink.SampleToRefTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Int64), use_last_error=False)(7, 'SampleToRefTime', ((1, 'llSampleTime'),(1, 'prfTime'),)))
    IDirectMusicSynthSink.RefTimeToSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Int64), use_last_error=False)(8, 'RefTimeToSample', ((1, 'rfTime'),(1, 'pllSampleTime'),)))
    IDirectMusicSynthSink.SetDirectSound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.IDirectSound_head,win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head, use_last_error=False)(9, 'SetDirectSound', ((1, 'pDirectSound'),(1, 'pDirectSoundBuffer'),)))
    IDirectMusicSynthSink.GetDesiredBufferSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetDesiredBufferSize', ((1, 'pdwBufferSizeInSamples'),)))
    win32more.System.Com.IUnknown
    return IDirectMusicSynthSink
DSPROPERTY_DIRECTSOUNDDEVICE = Int32
DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A = 1
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1 = 2
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1 = 3
DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W = 4
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A = 5
DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W = 6
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A = 7
DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W = 8
DIRECTSOUNDDEVICE_TYPE = Int32
DIRECTSOUNDDEVICE_TYPE_EMULATED = 0
DIRECTSOUNDDEVICE_TYPE_VXD = 1
DIRECTSOUNDDEVICE_TYPE_WDM = 2
DIRECTSOUNDDEVICE_DATAFLOW = Int32
DIRECTSOUNDDEVICE_DATAFLOW_RENDER = 0
DIRECTSOUNDDEVICE_DATAFLOW_CAPTURE = 1
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA._fields_ = [
        ("DeviceName", win32more.Foundation.PSTR),
        ("DataFlow", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW),
        ("DeviceId", Guid),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA._fields_ = [
        ("DeviceName", win32more.Foundation.PWSTR),
        ("DataFlow", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW),
        ("DeviceId", Guid),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA._fields_ = [
        ("DeviceId", Guid),
        ("DescriptionA", win32more.Foundation.CHAR * 256),
        ("DescriptionW", Char * 256),
        ("ModuleA", win32more.Foundation.CHAR * 260),
        ("ModuleW", Char * 260),
        ("Type", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE),
        ("DataFlow", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW),
        ("WaveDeviceId", UInt32),
        ("Devnode", UInt32),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA._fields_ = [
        ("Type", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE),
        ("DataFlow", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW),
        ("DeviceId", Guid),
        ("Description", win32more.Foundation.PSTR),
        ("Module", win32more.Foundation.PSTR),
        ("Interface", win32more.Foundation.PSTR),
        ("WaveDeviceId", UInt32),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA._fields_ = [
        ("Type", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_TYPE),
        ("DataFlow", win32more.Media.Audio.DirectMusic.DIRECTSOUNDDEVICE_DATAFLOW),
        ("DeviceId", Guid),
        ("Description", win32more.Foundation.PWSTR),
        ("Module", win32more.Foundation.PWSTR),
        ("Interface", win32more.Foundation.PWSTR),
        ("WaveDeviceId", UInt32),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA
def _define_LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA_head),c_void_p, use_last_error=False)
def _define_LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA_head),c_void_p, use_last_error=False)
def _define_LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA_head),c_void_p, use_last_error=False)
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA._fields_ = [
        ("Callback", win32more.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1),
        ("Context", c_void_p),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA._fields_ = [
        ("Callback", win32more.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA),
        ("Context", c_void_p),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA_head():
    class DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA(Structure):
        pass
    return DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA
def _define_DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA():
    DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA = win32more.Media.Audio.DirectMusic.DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA_head
    DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA._fields_ = [
        ("Callback", win32more.Media.Audio.DirectMusic.LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW),
        ("Context", c_void_p),
    ]
    return DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA
def _define_Tag_DVAudInfo_head():
    class Tag_DVAudInfo(Structure):
        pass
    return Tag_DVAudInfo
def _define_Tag_DVAudInfo():
    Tag_DVAudInfo = win32more.Media.Audio.DirectMusic.Tag_DVAudInfo_head
    Tag_DVAudInfo._fields_ = [
        ("bAudStyle", Byte * 2),
        ("bAudQu", Byte * 2),
        ("bNumAudPin", Byte),
        ("wAvgSamplesPerPinPerFrm", UInt16 * 2),
        ("wBlkMode", UInt16),
        ("wDIFMode", UInt16),
        ("wBlkDiv", UInt16),
    ]
    return Tag_DVAudInfo
def _define_MDEVICECAPSEX_head():
    class MDEVICECAPSEX(Structure):
        pass
    return MDEVICECAPSEX
def _define_MDEVICECAPSEX():
    MDEVICECAPSEX = win32more.Media.Audio.DirectMusic.MDEVICECAPSEX_head
    MDEVICECAPSEX._pack_ = 1
    MDEVICECAPSEX._fields_ = [
        ("cbSize", UInt32),
        ("pCaps", c_void_p),
    ]
    return MDEVICECAPSEX
def _define_MIDIOPENDESC_head():
    class MIDIOPENDESC(Structure):
        pass
    return MIDIOPENDESC
def _define_MIDIOPENDESC():
    MIDIOPENDESC = win32more.Media.Audio.DirectMusic.MIDIOPENDESC_head
    MIDIOPENDESC._pack_ = 1
    MIDIOPENDESC._fields_ = [
        ("hMidi", win32more.Media.Audio.HMIDI),
        ("dwCallback", UIntPtr),
        ("dwInstance", UIntPtr),
        ("dnDevNode", UIntPtr),
        ("cIds", UInt32),
        ("rgIds", win32more.Media.Multimedia.MIDIOPENSTRMID * 0),
    ]
    return MIDIOPENDESC
__all__ = [
    "DMUS_MAX_DESCRIPTION",
    "DMUS_MAX_DRIVER",
    "DMUS_EFFECT_NONE",
    "DMUS_EFFECT_REVERB",
    "DMUS_EFFECT_CHORUS",
    "DMUS_EFFECT_DELAY",
    "DMUS_PC_INPUTCLASS",
    "DMUS_PC_OUTPUTCLASS",
    "DMUS_PC_DLS",
    "DMUS_PC_EXTERNAL",
    "DMUS_PC_SOFTWARESYNTH",
    "DMUS_PC_MEMORYSIZEFIXED",
    "DMUS_PC_GMINHARDWARE",
    "DMUS_PC_GSINHARDWARE",
    "DMUS_PC_XGINHARDWARE",
    "DMUS_PC_DIRECTSOUND",
    "DMUS_PC_SHAREABLE",
    "DMUS_PC_DLS2",
    "DMUS_PC_AUDIOPATH",
    "DMUS_PC_WAVE",
    "DMUS_PC_SYSTEMMEMORY",
    "DMUS_PORT_WINMM_DRIVER",
    "DMUS_PORT_USER_MODE_SYNTH",
    "DMUS_PORT_KERNEL_MODE",
    "DMUS_PORTPARAMS_VOICES",
    "DMUS_PORTPARAMS_CHANNELGROUPS",
    "DMUS_PORTPARAMS_AUDIOCHANNELS",
    "DMUS_PORTPARAMS_SAMPLERATE",
    "DMUS_PORTPARAMS_EFFECTS",
    "DMUS_PORTPARAMS_SHARE",
    "DMUS_PORTPARAMS_FEATURES",
    "DMUS_PORT_FEATURE_AUDIOPATH",
    "DMUS_PORT_FEATURE_STREAMING",
    "DMUS_SYNTHSTATS_VOICES",
    "DMUS_SYNTHSTATS_TOTAL_CPU",
    "DMUS_SYNTHSTATS_CPU_PER_VOICE",
    "DMUS_SYNTHSTATS_LOST_NOTES",
    "DMUS_SYNTHSTATS_PEAK_VOLUME",
    "DMUS_SYNTHSTATS_FREE_MEMORY",
    "DMUS_SYNTHSTATS_SYSTEMMEMORY",
    "DMUS_CLOCKF_GLOBAL",
    "DSBUSID_FIRST_SPKR_LOC",
    "DSBUSID_FRONT_LEFT",
    "DSBUSID_LEFT",
    "DSBUSID_FRONT_RIGHT",
    "DSBUSID_RIGHT",
    "DSBUSID_FRONT_CENTER",
    "DSBUSID_LOW_FREQUENCY",
    "DSBUSID_BACK_LEFT",
    "DSBUSID_BACK_RIGHT",
    "DSBUSID_FRONT_LEFT_OF_CENTER",
    "DSBUSID_FRONT_RIGHT_OF_CENTER",
    "DSBUSID_BACK_CENTER",
    "DSBUSID_SIDE_LEFT",
    "DSBUSID_SIDE_RIGHT",
    "DSBUSID_TOP_CENTER",
    "DSBUSID_TOP_FRONT_LEFT",
    "DSBUSID_TOP_FRONT_CENTER",
    "DSBUSID_TOP_FRONT_RIGHT",
    "DSBUSID_TOP_BACK_LEFT",
    "DSBUSID_TOP_BACK_CENTER",
    "DSBUSID_TOP_BACK_RIGHT",
    "DSBUSID_LAST_SPKR_LOC",
    "DSBUSID_REVERB_SEND",
    "DSBUSID_CHORUS_SEND",
    "DSBUSID_DYNAMIC_0",
    "DSBUSID_NULL",
    "DAUD_CRITICAL_VOICE_PRIORITY",
    "DAUD_HIGH_VOICE_PRIORITY",
    "DAUD_STANDARD_VOICE_PRIORITY",
    "DAUD_LOW_VOICE_PRIORITY",
    "DAUD_PERSIST_VOICE_PRIORITY",
    "DAUD_CHAN1_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN2_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN3_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN4_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN5_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN6_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN7_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN8_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN9_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN10_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN11_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN12_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN13_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN14_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN15_VOICE_PRIORITY_OFFSET",
    "DAUD_CHAN16_VOICE_PRIORITY_OFFSET",
    "CLSID_DirectMusic",
    "CLSID_DirectMusicCollection",
    "CLSID_DirectMusicSynth",
    "GUID_DMUS_PROP_GM_Hardware",
    "GUID_DMUS_PROP_GS_Hardware",
    "GUID_DMUS_PROP_XG_Hardware",
    "GUID_DMUS_PROP_XG_Capable",
    "GUID_DMUS_PROP_GS_Capable",
    "GUID_DMUS_PROP_DLS1",
    "GUID_DMUS_PROP_DLS2",
    "GUID_DMUS_PROP_INSTRUMENT2",
    "GUID_DMUS_PROP_SynthSink_DSOUND",
    "GUID_DMUS_PROP_SynthSink_WAVE",
    "GUID_DMUS_PROP_SampleMemorySize",
    "GUID_DMUS_PROP_SamplePlaybackRate",
    "GUID_DMUS_PROP_WriteLatency",
    "GUID_DMUS_PROP_WritePeriod",
    "GUID_DMUS_PROP_MemorySize",
    "GUID_DMUS_PROP_WavesReverb",
    "GUID_DMUS_PROP_Effects",
    "GUID_DMUS_PROP_LegacyCaps",
    "GUID_DMUS_PROP_Volume",
    "DMUS_VOLUME_MAX",
    "DMUS_VOLUME_MIN",
    "DMUS_EVENT_STRUCTURED",
    "DMUS_DOWNLOADINFO_INSTRUMENT",
    "DMUS_DOWNLOADINFO_WAVE",
    "DMUS_DOWNLOADINFO_INSTRUMENT2",
    "DMUS_DOWNLOADINFO_WAVEARTICULATION",
    "DMUS_DOWNLOADINFO_STREAMINGWAVE",
    "DMUS_DOWNLOADINFO_ONESHOTWAVE",
    "DMUS_DEFAULT_SIZE_OFFSETTABLE",
    "DMUS_INSTRUMENT_GM_INSTRUMENT",
    "DMUS_MIN_DATA_SIZE",
    "CONN_SRC_NONE",
    "CONN_SRC_LFO",
    "CONN_SRC_KEYONVELOCITY",
    "CONN_SRC_KEYNUMBER",
    "CONN_SRC_EG1",
    "CONN_SRC_EG2",
    "CONN_SRC_PITCHWHEEL",
    "CONN_SRC_CC1",
    "CONN_SRC_CC7",
    "CONN_SRC_CC10",
    "CONN_SRC_CC11",
    "CONN_DST_NONE",
    "CONN_DST_ATTENUATION",
    "CONN_DST_PITCH",
    "CONN_DST_PAN",
    "CONN_DST_LFO_FREQUENCY",
    "CONN_DST_LFO_STARTDELAY",
    "CONN_DST_EG1_ATTACKTIME",
    "CONN_DST_EG1_DECAYTIME",
    "CONN_DST_EG1_RELEASETIME",
    "CONN_DST_EG1_SUSTAINLEVEL",
    "CONN_DST_EG2_ATTACKTIME",
    "CONN_DST_EG2_DECAYTIME",
    "CONN_DST_EG2_RELEASETIME",
    "CONN_DST_EG2_SUSTAINLEVEL",
    "CONN_TRN_NONE",
    "CONN_TRN_CONCAVE",
    "F_INSTRUMENT_DRUMS",
    "F_RGN_OPTION_SELFNONEXCLUSIVE",
    "WAVELINK_CHANNEL_LEFT",
    "WAVELINK_CHANNEL_RIGHT",
    "F_WAVELINK_PHASE_MASTER",
    "POOL_CUE_NULL",
    "F_WSMP_NO_TRUNCATION",
    "F_WSMP_NO_COMPRESSION",
    "WLOOP_TYPE_FORWARD",
    "CONN_SRC_POLYPRESSURE",
    "CONN_SRC_CHANNELPRESSURE",
    "CONN_SRC_VIBRATO",
    "CONN_SRC_MONOPRESSURE",
    "CONN_SRC_CC91",
    "CONN_SRC_CC93",
    "CONN_DST_GAIN",
    "CONN_DST_KEYNUMBER",
    "CONN_DST_LEFT",
    "CONN_DST_RIGHT",
    "CONN_DST_CENTER",
    "CONN_DST_LEFTREAR",
    "CONN_DST_RIGHTREAR",
    "CONN_DST_LFE_CHANNEL",
    "CONN_DST_CHORUS",
    "CONN_DST_REVERB",
    "CONN_DST_VIB_FREQUENCY",
    "CONN_DST_VIB_STARTDELAY",
    "CONN_DST_EG1_DELAYTIME",
    "CONN_DST_EG1_HOLDTIME",
    "CONN_DST_EG1_SHUTDOWNTIME",
    "CONN_DST_EG2_DELAYTIME",
    "CONN_DST_EG2_HOLDTIME",
    "CONN_DST_FILTER_CUTOFF",
    "CONN_DST_FILTER_Q",
    "CONN_TRN_CONVEX",
    "CONN_TRN_SWITCH",
    "DLS_CDL_AND",
    "DLS_CDL_OR",
    "DLS_CDL_XOR",
    "DLS_CDL_ADD",
    "DLS_CDL_SUBTRACT",
    "DLS_CDL_MULTIPLY",
    "DLS_CDL_DIVIDE",
    "DLS_CDL_LOGICAL_AND",
    "DLS_CDL_LOGICAL_OR",
    "DLS_CDL_LT",
    "DLS_CDL_LE",
    "DLS_CDL_GT",
    "DLS_CDL_GE",
    "DLS_CDL_EQ",
    "DLS_CDL_NOT",
    "DLS_CDL_CONST",
    "DLS_CDL_QUERY",
    "DLS_CDL_QUERYSUPPORTED",
    "WLOOP_TYPE_RELEASE",
    "F_WAVELINK_MULTICHANNEL",
    "DLSID_GMInHardware",
    "DLSID_GSInHardware",
    "DLSID_XGInHardware",
    "DLSID_SupportsDLS1",
    "DLSID_SupportsDLS2",
    "DLSID_SampleMemorySize",
    "DLSID_ManufacturersID",
    "DLSID_ProductID",
    "DLSID_SamplePlaybackRate",
    "REFRESH_F_LASTBUFFER",
    "CLSID_DirectMusicSynthSink",
    "GUID_DMUS_PROP_SetSynthSink",
    "GUID_DMUS_PROP_SinkUsesDSound",
    "CLSID_DirectSoundPrivate",
    "DSPROPSETID_DirectSoundDevice",
    "DV_DVSD_NTSC_FRAMESIZE",
    "DV_DVSD_PAL_FRAMESIZE",
    "DV_SMCHN",
    "DV_AUDIOMODE",
    "DV_AUDIOSMP",
    "DV_AUDIOQU",
    "DV_NTSCPAL",
    "DV_STYPE",
    "DV_NTSC",
    "DV_PAL",
    "DV_SD",
    "DV_HD",
    "DV_SL",
    "DV_CAP_AUD16Bits",
    "DV_CAP_AUD12Bits",
    "SIZE_DVINFO",
    "DLSID",
    "DLSVERSION",
    "CONNECTION",
    "CONNECTIONLIST",
    "RGNRANGE",
    "MIDILOCALE",
    "RGNHEADER",
    "INSTHEADER",
    "DLSHEADER",
    "WAVELINK",
    "POOLCUE",
    "POOLTABLE",
    "_rwsmp",
    "_rloop",
    "DMUS_DOWNLOADINFO",
    "DMUS_OFFSETTABLE",
    "DMUS_INSTRUMENT",
    "DMUS_REGION",
    "DMUS_LFOPARAMS",
    "DMUS_VEGPARAMS",
    "DMUS_PEGPARAMS",
    "DMUS_MSCPARAMS",
    "DMUS_ARTICPARAMS",
    "DMUS_ARTICULATION",
    "DMUS_ARTICULATION2",
    "DMUS_EXTENSIONCHUNK",
    "DMUS_COPYRIGHT",
    "DMUS_WAVEDATA",
    "DMUS_WAVE",
    "DMUS_NOTERANGE",
    "DMUS_WAVEARTDL",
    "DMUS_WAVEDL",
    "DMUS_EVENTHEADER",
    "DMUS_BUFFERDESC",
    "DMUS_PORTCAPS",
    "_DMUS_PORTPARAMS",
    "DMUS_PORTPARAMS8",
    "DMUS_SYNTHSTATS",
    "DMUS_SYNTHSTATS8",
    "DMUS_WAVES_REVERB_PARAMS",
    "DMUS_CLOCKTYPE",
    "DMUS_CLOCK_SYSTEM",
    "DMUS_CLOCK_WAVE",
    "DMUS_CLOCKINFO7",
    "DMUS_CLOCKINFO8",
    "IDirectMusic",
    "IDirectMusic8",
    "IDirectMusicBuffer",
    "IDirectMusicInstrument",
    "IDirectMusicDownloadedInstrument",
    "IDirectMusicCollection",
    "IDirectMusicDownload",
    "IDirectMusicPortDownload",
    "IDirectMusicPort",
    "IDirectMusicThru",
    "DMUS_VOICE_STATE",
    "IDirectMusicSynth",
    "IDirectMusicSynth8",
    "IDirectMusicSynthSink",
    "DSPROPERTY_DIRECTSOUNDDEVICE",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W",
    "DIRECTSOUNDDEVICE_TYPE",
    "DIRECTSOUNDDEVICE_TYPE_EMULATED",
    "DIRECTSOUNDDEVICE_TYPE_VXD",
    "DIRECTSOUNDDEVICE_TYPE_WDM",
    "DIRECTSOUNDDEVICE_DATAFLOW",
    "DIRECTSOUNDDEVICE_DATAFLOW_RENDER",
    "DIRECTSOUNDDEVICE_DATAFLOW_CAPTURE",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_A_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_WAVEDEVICEMAPPING_W_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_1_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_A_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_DESCRIPTION_W_DATA",
    "LPFNDIRECTSOUNDDEVICEENUMERATECALLBACK1",
    "LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKA",
    "LPFNDIRECTSOUNDDEVICEENUMERATECALLBACKW",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_1_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_A_DATA",
    "DSPROPERTY_DIRECTSOUNDDEVICE_ENUMERATE_W_DATA",
    "Tag_DVAudInfo",
    "MDEVICECAPSEX",
    "MIDIOPENDESC",
]
