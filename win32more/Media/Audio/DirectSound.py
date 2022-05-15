from win32more import *
import win32more.Media.Audio.DirectSound
import win32more.Foundation
import win32more.Graphics.Direct3D
import win32more.Media.Audio
import win32more.System.Com

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Media.Audio.DirectSound, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Media.Audio.DirectSound, name)
def __dir__():
    return __all__
DIRECTSOUND_VERSION = 1792
_FACDS = 2168
CLSID_DirectSound = '47d4d946-62e8-11cf-93bc-444553540000'
CLSID_DirectSound8 = '3901cc3f-84b5-4fa4-ba35-aa8172b8a09b'
CLSID_DirectSoundCapture = 'b0210780-89cd-11d0-af08-00a0c925cd16'
CLSID_DirectSoundCapture8 = 'e4bcac13-7f99-4908-9a8e-74e3bf24b6e1'
CLSID_DirectSoundFullDuplex = 'fea4300c-7959-4147-b26a-2377b9e7a91d'
DSDEVID_DefaultPlayback = 'def00000-9c6d-47ed-aaf1-4dda8f2b5c03'
DSDEVID_DefaultCapture = 'def00001-9c6d-47ed-aaf1-4dda8f2b5c03'
DSDEVID_DefaultVoicePlayback = 'def00002-9c6d-47ed-aaf1-4dda8f2b5c03'
DSDEVID_DefaultVoiceCapture = 'def00003-9c6d-47ed-aaf1-4dda8f2b5c03'
DSFX_LOCHARDWARE = 1
DSFX_LOCSOFTWARE = 2
DSCFX_LOCHARDWARE = 1
DSCFX_LOCSOFTWARE = 2
DSCFXR_LOCHARDWARE = 16
DSCFXR_LOCSOFTWARE = 32
GUID_All_Objects = 'aa114de5-c262-4169-a1c8-23d698cc73b5'
KSPROPERTY_SUPPORT_GET = 1
KSPROPERTY_SUPPORT_SET = 2
DSFXGARGLE_WAVE_TRIANGLE = 0
DSFXGARGLE_WAVE_SQUARE = 1
DSFXGARGLE_RATEHZ_MIN = 1
DSFXGARGLE_RATEHZ_MAX = 1000
DSFXCHORUS_WAVE_TRIANGLE = 0
DSFXCHORUS_WAVE_SIN = 1
DSFXCHORUS_WETDRYMIX_MIN = 0
DSFXCHORUS_WETDRYMIX_MAX = 100
DSFXCHORUS_DEPTH_MIN = 0
DSFXCHORUS_DEPTH_MAX = 100
DSFXCHORUS_FEEDBACK_MIN = -99
DSFXCHORUS_FEEDBACK_MAX = 99
DSFXCHORUS_FREQUENCY_MIN = 0
DSFXCHORUS_FREQUENCY_MAX = 10
DSFXCHORUS_DELAY_MIN = 0
DSFXCHORUS_DELAY_MAX = 20
DSFXCHORUS_PHASE_MIN = 0
DSFXCHORUS_PHASE_MAX = 4
DSFXCHORUS_PHASE_NEG_180 = 0
DSFXCHORUS_PHASE_NEG_90 = 1
DSFXCHORUS_PHASE_ZERO = 2
DSFXCHORUS_PHASE_90 = 3
DSFXCHORUS_PHASE_180 = 4
DSFXFLANGER_WAVE_TRIANGLE = 0
DSFXFLANGER_WAVE_SIN = 1
DSFXFLANGER_WETDRYMIX_MIN = 0
DSFXFLANGER_WETDRYMIX_MAX = 100
DSFXFLANGER_FREQUENCY_MIN = 0
DSFXFLANGER_FREQUENCY_MAX = 10
DSFXFLANGER_DEPTH_MIN = 0
DSFXFLANGER_DEPTH_MAX = 100
DSFXFLANGER_PHASE_MIN = 0
DSFXFLANGER_PHASE_MAX = 4
DSFXFLANGER_FEEDBACK_MIN = -99
DSFXFLANGER_FEEDBACK_MAX = 99
DSFXFLANGER_DELAY_MIN = 0
DSFXFLANGER_DELAY_MAX = 4
DSFXFLANGER_PHASE_NEG_180 = 0
DSFXFLANGER_PHASE_NEG_90 = 1
DSFXFLANGER_PHASE_ZERO = 2
DSFXFLANGER_PHASE_90 = 3
DSFXFLANGER_PHASE_180 = 4
DSFXECHO_WETDRYMIX_MIN = 0
DSFXECHO_WETDRYMIX_MAX = 100
DSFXECHO_FEEDBACK_MIN = 0
DSFXECHO_FEEDBACK_MAX = 100
DSFXECHO_LEFTDELAY_MIN = 1
DSFXECHO_LEFTDELAY_MAX = 2000
DSFXECHO_RIGHTDELAY_MIN = 1
DSFXECHO_RIGHTDELAY_MAX = 2000
DSFXECHO_PANDELAY_MIN = 0
DSFXECHO_PANDELAY_MAX = 1
DSFXDISTORTION_GAIN_MIN = -60
DSFXDISTORTION_GAIN_MAX = 0
DSFXDISTORTION_EDGE_MIN = 0
DSFXDISTORTION_EDGE_MAX = 100
DSFXDISTORTION_POSTEQCENTERFREQUENCY_MIN = 100
DSFXDISTORTION_POSTEQCENTERFREQUENCY_MAX = 8000
DSFXDISTORTION_POSTEQBANDWIDTH_MIN = 100
DSFXDISTORTION_POSTEQBANDWIDTH_MAX = 8000
DSFXDISTORTION_PRELOWPASSCUTOFF_MIN = 100
DSFXDISTORTION_PRELOWPASSCUTOFF_MAX = 8000
DSFXCOMPRESSOR_GAIN_MIN = -60
DSFXCOMPRESSOR_GAIN_MAX = 60
DSFXCOMPRESSOR_ATTACK_MIN = 0.01
DSFXCOMPRESSOR_ATTACK_MAX = 500
DSFXCOMPRESSOR_RELEASE_MIN = 50
DSFXCOMPRESSOR_RELEASE_MAX = 3000
DSFXCOMPRESSOR_THRESHOLD_MIN = -60
DSFXCOMPRESSOR_THRESHOLD_MAX = 0
DSFXCOMPRESSOR_RATIO_MIN = 1
DSFXCOMPRESSOR_RATIO_MAX = 100
DSFXCOMPRESSOR_PREDELAY_MIN = 0
DSFXCOMPRESSOR_PREDELAY_MAX = 4
DSFXPARAMEQ_CENTER_MIN = 80
DSFXPARAMEQ_CENTER_MAX = 16000
DSFXPARAMEQ_BANDWIDTH_MIN = 1
DSFXPARAMEQ_BANDWIDTH_MAX = 36
DSFXPARAMEQ_GAIN_MIN = -15
DSFXPARAMEQ_GAIN_MAX = 15
DSFX_I3DL2REVERB_ROOM_MIN = -10000
DSFX_I3DL2REVERB_ROOM_MAX = 0
DSFX_I3DL2REVERB_ROOM_DEFAULT = -1000
DSFX_I3DL2REVERB_ROOMHF_MIN = -10000
DSFX_I3DL2REVERB_ROOMHF_MAX = 0
DSFX_I3DL2REVERB_ROOMHF_DEFAULT = -100
DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MIN = 0
DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MAX = 10
DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_DEFAULT = 0
DSFX_I3DL2REVERB_DECAYTIME_MIN = 0.1
DSFX_I3DL2REVERB_DECAYTIME_MAX = 20
DSFX_I3DL2REVERB_DECAYTIME_DEFAULT = 1.49
DSFX_I3DL2REVERB_DECAYHFRATIO_MIN = 0.1
DSFX_I3DL2REVERB_DECAYHFRATIO_MAX = 2
DSFX_I3DL2REVERB_DECAYHFRATIO_DEFAULT = 0.83
DSFX_I3DL2REVERB_REFLECTIONS_MIN = -10000
DSFX_I3DL2REVERB_REFLECTIONS_MAX = 1000
DSFX_I3DL2REVERB_REFLECTIONS_DEFAULT = -2602
DSFX_I3DL2REVERB_REFLECTIONSDELAY_MIN = 0
DSFX_I3DL2REVERB_REFLECTIONSDELAY_MAX = 0.3
DSFX_I3DL2REVERB_REFLECTIONSDELAY_DEFAULT = 0.007
DSFX_I3DL2REVERB_REVERB_MIN = -10000
DSFX_I3DL2REVERB_REVERB_MAX = 2000
DSFX_I3DL2REVERB_REVERB_DEFAULT = 200
DSFX_I3DL2REVERB_REVERBDELAY_MIN = 0
DSFX_I3DL2REVERB_REVERBDELAY_MAX = 0.1
DSFX_I3DL2REVERB_REVERBDELAY_DEFAULT = 0.011
DSFX_I3DL2REVERB_DIFFUSION_MIN = 0
DSFX_I3DL2REVERB_DIFFUSION_MAX = 100
DSFX_I3DL2REVERB_DIFFUSION_DEFAULT = 100
DSFX_I3DL2REVERB_DENSITY_MIN = 0
DSFX_I3DL2REVERB_DENSITY_MAX = 100
DSFX_I3DL2REVERB_DENSITY_DEFAULT = 100
DSFX_I3DL2REVERB_HFREFERENCE_MIN = 20
DSFX_I3DL2REVERB_HFREFERENCE_MAX = 20000
DSFX_I3DL2REVERB_HFREFERENCE_DEFAULT = 5000
DSFX_I3DL2REVERB_QUALITY_MIN = 0
DSFX_I3DL2REVERB_QUALITY_MAX = 3
DSFX_I3DL2REVERB_QUALITY_DEFAULT = 2
DSFX_WAVESREVERB_INGAIN_MIN = -96
DSFX_WAVESREVERB_INGAIN_MAX = 0
DSFX_WAVESREVERB_INGAIN_DEFAULT = 0
DSFX_WAVESREVERB_REVERBMIX_MIN = -96
DSFX_WAVESREVERB_REVERBMIX_MAX = 0
DSFX_WAVESREVERB_REVERBMIX_DEFAULT = 0
DSFX_WAVESREVERB_REVERBTIME_MIN = 0.001
DSFX_WAVESREVERB_REVERBTIME_MAX = 3000
DSFX_WAVESREVERB_REVERBTIME_DEFAULT = 1000
DSFX_WAVESREVERB_HIGHFREQRTRATIO_MIN = 0.001
DSFX_WAVESREVERB_HIGHFREQRTRATIO_MAX = 0.999
DSFX_WAVESREVERB_HIGHFREQRTRATIO_DEFAULT = 0.001
DSCFX_AEC_MODE_PASS_THROUGH = 0
DSCFX_AEC_MODE_HALF_DUPLEX = 1
DSCFX_AEC_MODE_FULL_DUPLEX = 2
DSCFX_AEC_STATUS_HISTORY_UNINITIALIZED = 0
DSCFX_AEC_STATUS_HISTORY_CONTINUOUSLY_CONVERGED = 1
DSCFX_AEC_STATUS_HISTORY_PREVIOUSLY_DIVERGED = 2
DSCFX_AEC_STATUS_CURRENTLY_CONVERGED = 8
DS_NO_VIRTUALIZATION = 142082058
DSCAPS_PRIMARYMONO = 1
DSCAPS_PRIMARYSTEREO = 2
DSCAPS_PRIMARY8BIT = 4
DSCAPS_PRIMARY16BIT = 8
DSCAPS_CONTINUOUSRATE = 16
DSCAPS_EMULDRIVER = 32
DSCAPS_CERTIFIED = 64
DSCAPS_SECONDARYMONO = 256
DSCAPS_SECONDARYSTEREO = 512
DSCAPS_SECONDARY8BIT = 1024
DSCAPS_SECONDARY16BIT = 2048
DSSCL_NORMAL = 1
DSSCL_PRIORITY = 2
DSSCL_EXCLUSIVE = 3
DSSCL_WRITEPRIMARY = 4
DSSPEAKER_DIRECTOUT = 0
DSSPEAKER_HEADPHONE = 1
DSSPEAKER_MONO = 2
DSSPEAKER_QUAD = 3
DSSPEAKER_STEREO = 4
DSSPEAKER_SURROUND = 5
DSSPEAKER_5POINT1 = 6
DSSPEAKER_7POINT1 = 7
DSSPEAKER_7POINT1_SURROUND = 8
DSSPEAKER_5POINT1_SURROUND = 9
DSSPEAKER_7POINT1_WIDE = 7
DSSPEAKER_5POINT1_BACK = 6
DSSPEAKER_GEOMETRY_MIN = 5
DSSPEAKER_GEOMETRY_NARROW = 10
DSSPEAKER_GEOMETRY_WIDE = 20
DSSPEAKER_GEOMETRY_MAX = 180
DSBCAPS_PRIMARYBUFFER = 1
DSBCAPS_STATIC = 2
DSBCAPS_LOCHARDWARE = 4
DSBCAPS_LOCSOFTWARE = 8
DSBCAPS_CTRL3D = 16
DSBCAPS_CTRLFREQUENCY = 32
DSBCAPS_CTRLPAN = 64
DSBCAPS_CTRLVOLUME = 128
DSBCAPS_CTRLPOSITIONNOTIFY = 256
DSBCAPS_CTRLFX = 512
DSBCAPS_STICKYFOCUS = 16384
DSBCAPS_GLOBALFOCUS = 32768
DSBCAPS_GETCURRENTPOSITION2 = 65536
DSBCAPS_MUTE3DATMAXDISTANCE = 131072
DSBCAPS_LOCDEFER = 262144
DSBCAPS_TRUEPLAYPOSITION = 524288
DSBPLAY_LOOPING = 1
DSBPLAY_LOCHARDWARE = 2
DSBPLAY_LOCSOFTWARE = 4
DSBPLAY_TERMINATEBY_TIME = 8
DSBPLAY_TERMINATEBY_DISTANCE = 16
DSBPLAY_TERMINATEBY_PRIORITY = 32
DSBSTATUS_PLAYING = 1
DSBSTATUS_BUFFERLOST = 2
DSBSTATUS_LOOPING = 4
DSBSTATUS_LOCHARDWARE = 8
DSBSTATUS_LOCSOFTWARE = 16
DSBSTATUS_TERMINATED = 32
DSBLOCK_FROMWRITECURSOR = 1
DSBLOCK_ENTIREBUFFER = 2
DSBFREQUENCY_ORIGINAL = 0
DSBFREQUENCY_MIN = 100
DSBFREQUENCY_MAX = 200000
DSBPAN_LEFT = -10000
DSBPAN_CENTER = 0
DSBPAN_RIGHT = 10000
DSBVOLUME_MIN = -10000
DSBVOLUME_MAX = 0
DSBSIZE_MIN = 4
DSBSIZE_MAX = 268435455
DSBSIZE_FX_MIN = 150
DSBNOTIFICATIONS_MAX = 100000
DS3DMODE_NORMAL = 0
DS3DMODE_HEADRELATIVE = 1
DS3DMODE_DISABLE = 2
DS3D_IMMEDIATE = 0
DS3D_DEFERRED = 1
DS3D_DEFAULTDISTANCEFACTOR = 1
DS3D_MINROLLOFFFACTOR = 0
DS3D_MAXROLLOFFFACTOR = 10
DS3D_DEFAULTROLLOFFFACTOR = 1
DS3D_MINDOPPLERFACTOR = 0
DS3D_MAXDOPPLERFACTOR = 10
DS3D_DEFAULTDOPPLERFACTOR = 1
DS3D_DEFAULTMINDISTANCE = 1
DS3D_DEFAULTMAXDISTANCE = 1000000000.0
DS3D_MINCONEANGLE = 0
DS3D_MAXCONEANGLE = 360
DS3D_DEFAULTCONEANGLE = 360
DS3D_DEFAULTCONEOUTSIDEVOLUME = 0
DSCCAPS_EMULDRIVER = 32
DSCCAPS_CERTIFIED = 64
DSCCAPS_MULTIPLECAPTURE = 1
DSCBCAPS_WAVEMAPPED = 2147483648
DSCBCAPS_CTRLFX = 512
DSCBLOCK_ENTIREBUFFER = 1
DSCBSTATUS_CAPTURING = 1
DSCBSTATUS_LOOPING = 2
DSCBSTART_LOOPING = 1
DSBPN_OFFSETSTOP = 4294967295
DS_CERTIFIED = 0
DS_UNCERTIFIED = 1
DS3DALG_NO_VIRTUALIZATION = 'c241333f-1c1b-11d2-94f5-00c04fc28aca'
DS3DALG_HRTF_FULL = 'c2413340-1c1b-11d2-94f5-00c04fc28aca'
DS3DALG_HRTF_LIGHT = 'c2413342-1c1b-11d2-94f5-00c04fc28aca'
GUID_DSFX_STANDARD_GARGLE = 'dafd8210-5711-4b91-9fe3-f75b7ae279bf'
GUID_DSFX_STANDARD_CHORUS = 'efe6629c-81f7-4281-bd91-c9d604a95af6'
GUID_DSFX_STANDARD_FLANGER = 'efca3d92-dfd8-4672-a603-7420894bad98'
GUID_DSFX_STANDARD_ECHO = 'ef3e932c-d40b-4f51-8ccf-3f98f1b29d5d'
GUID_DSFX_STANDARD_DISTORTION = 'ef114c90-cd1d-484e-96e5-09cfaf912a21'
GUID_DSFX_STANDARD_COMPRESSOR = 'ef011f79-4000-406d-87af-bffb3fc39d57'
GUID_DSFX_STANDARD_PARAMEQ = '120ced89-3bf4-4173-a132-3cb406cf3231'
GUID_DSFX_STANDARD_I3DL2REVERB = 'ef985e71-d5c7-42d4-ba4d-2d073e2e96f4'
GUID_DSFX_WAVES_REVERB = '87fc0268-9a55-4360-95aa-004a1d9de26c'
GUID_DSCFX_CLASS_AEC = 'bf963d80-c559-11d0-8a2b-00a0c9255ac1'
GUID_DSCFX_MS_AEC = 'cdebb919-379a-488a-8765-f53cfd36de40'
GUID_DSCFX_SYSTEM_AEC = '1c22c56d-9879-4f5b-a389-27996ddc2810'
GUID_DSCFX_CLASS_NS = 'e07f903f-62fd-4e60-8cdd-dea7236665b5'
GUID_DSCFX_MS_NS = '11c5c73b-66e9-4ba1-a0ba-e814c6eed92d'
GUID_DSCFX_SYSTEM_NS = '5ab0882e-7274-4516-877d-4eee99ba4fd0'
DSFXR_PRESENT = 0
DSFXR_LOCHARDWARE = 1
DSFXR_LOCSOFTWARE = 2
DSFXR_UNALLOCATED = 3
DSFXR_FAILED = 4
DSFXR_UNKNOWN = 5
DSFXR_SENDLOOP = 6
DSFX_I3DL2_MATERIAL_PRESET_SINGLEWINDOW = 0
DSFX_I3DL2_MATERIAL_PRESET_DOUBLEWINDOW = 1
DSFX_I3DL2_MATERIAL_PRESET_THINDOOR = 2
DSFX_I3DL2_MATERIAL_PRESET_THICKDOOR = 3
DSFX_I3DL2_MATERIAL_PRESET_WOODWALL = 4
DSFX_I3DL2_MATERIAL_PRESET_BRICKWALL = 5
DSFX_I3DL2_MATERIAL_PRESET_STONEWALL = 6
DSFX_I3DL2_MATERIAL_PRESET_CURTAIN = 7
DSFX_I3DL2_ENVIRONMENT_PRESET_DEFAULT = 0
DSFX_I3DL2_ENVIRONMENT_PRESET_GENERIC = 1
DSFX_I3DL2_ENVIRONMENT_PRESET_PADDEDCELL = 2
DSFX_I3DL2_ENVIRONMENT_PRESET_ROOM = 3
DSFX_I3DL2_ENVIRONMENT_PRESET_BATHROOM = 4
DSFX_I3DL2_ENVIRONMENT_PRESET_LIVINGROOM = 5
DSFX_I3DL2_ENVIRONMENT_PRESET_STONEROOM = 6
DSFX_I3DL2_ENVIRONMENT_PRESET_AUDITORIUM = 7
DSFX_I3DL2_ENVIRONMENT_PRESET_CONCERTHALL = 8
DSFX_I3DL2_ENVIRONMENT_PRESET_CAVE = 9
DSFX_I3DL2_ENVIRONMENT_PRESET_ARENA = 10
DSFX_I3DL2_ENVIRONMENT_PRESET_HANGAR = 11
DSFX_I3DL2_ENVIRONMENT_PRESET_CARPETEDHALLWAY = 12
DSFX_I3DL2_ENVIRONMENT_PRESET_HALLWAY = 13
DSFX_I3DL2_ENVIRONMENT_PRESET_STONECORRIDOR = 14
DSFX_I3DL2_ENVIRONMENT_PRESET_ALLEY = 15
DSFX_I3DL2_ENVIRONMENT_PRESET_FOREST = 16
DSFX_I3DL2_ENVIRONMENT_PRESET_CITY = 17
DSFX_I3DL2_ENVIRONMENT_PRESET_MOUNTAINS = 18
DSFX_I3DL2_ENVIRONMENT_PRESET_QUARRY = 19
DSFX_I3DL2_ENVIRONMENT_PRESET_PLAIN = 20
DSFX_I3DL2_ENVIRONMENT_PRESET_PARKINGLOT = 21
DSFX_I3DL2_ENVIRONMENT_PRESET_SEWERPIPE = 22
DSFX_I3DL2_ENVIRONMENT_PRESET_UNDERWATER = 23
DSFX_I3DL2_ENVIRONMENT_PRESET_SMALLROOM = 24
DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMROOM = 25
DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEROOM = 26
DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMHALL = 27
DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEHALL = 28
DSFX_I3DL2_ENVIRONMENT_PRESET_PLATE = 29
def _define_DSCAPS_head():
    class DSCAPS(Structure):
        pass
    return DSCAPS
def _define_DSCAPS():
    DSCAPS = win32more.Media.Audio.DirectSound.DSCAPS_head
    DSCAPS._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwMinSecondarySampleRate", UInt32),
        ("dwMaxSecondarySampleRate", UInt32),
        ("dwPrimaryBuffers", UInt32),
        ("dwMaxHwMixingAllBuffers", UInt32),
        ("dwMaxHwMixingStaticBuffers", UInt32),
        ("dwMaxHwMixingStreamingBuffers", UInt32),
        ("dwFreeHwMixingAllBuffers", UInt32),
        ("dwFreeHwMixingStaticBuffers", UInt32),
        ("dwFreeHwMixingStreamingBuffers", UInt32),
        ("dwMaxHw3DAllBuffers", UInt32),
        ("dwMaxHw3DStaticBuffers", UInt32),
        ("dwMaxHw3DStreamingBuffers", UInt32),
        ("dwFreeHw3DAllBuffers", UInt32),
        ("dwFreeHw3DStaticBuffers", UInt32),
        ("dwFreeHw3DStreamingBuffers", UInt32),
        ("dwTotalHwMemBytes", UInt32),
        ("dwFreeHwMemBytes", UInt32),
        ("dwMaxContigFreeHwMemBytes", UInt32),
        ("dwUnlockTransferRateHwBuffers", UInt32),
        ("dwPlayCpuOverheadSwBuffers", UInt32),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
    ]
    return DSCAPS
def _define_DSBCAPS_head():
    class DSBCAPS(Structure):
        pass
    return DSBCAPS
def _define_DSBCAPS():
    DSBCAPS = win32more.Media.Audio.DirectSound.DSBCAPS_head
    DSBCAPS._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwBufferBytes", UInt32),
        ("dwUnlockTransferRate", UInt32),
        ("dwPlayCpuOverhead", UInt32),
    ]
    return DSBCAPS
def _define_DSEFFECTDESC_head():
    class DSEFFECTDESC(Structure):
        pass
    return DSEFFECTDESC
def _define_DSEFFECTDESC():
    DSEFFECTDESC = win32more.Media.Audio.DirectSound.DSEFFECTDESC_head
    DSEFFECTDESC._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("guidDSFXClass", Guid),
        ("dwReserved1", UIntPtr),
        ("dwReserved2", UIntPtr),
    ]
    return DSEFFECTDESC
def _define_DSCEFFECTDESC_head():
    class DSCEFFECTDESC(Structure):
        pass
    return DSCEFFECTDESC
def _define_DSCEFFECTDESC():
    DSCEFFECTDESC = win32more.Media.Audio.DirectSound.DSCEFFECTDESC_head
    DSCEFFECTDESC._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("guidDSCFXClass", Guid),
        ("guidDSCFXInstance", Guid),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
    ]
    return DSCEFFECTDESC
def _define_DSBUFFERDESC_head():
    class DSBUFFERDESC(Structure):
        pass
    return DSBUFFERDESC
def _define_DSBUFFERDESC():
    DSBUFFERDESC = win32more.Media.Audio.DirectSound.DSBUFFERDESC_head
    DSBUFFERDESC._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwBufferBytes", UInt32),
        ("dwReserved", UInt32),
        ("lpwfxFormat", POINTER(win32more.Media.Audio.WAVEFORMATEX_head)),
        ("guid3DAlgorithm", Guid),
    ]
    return DSBUFFERDESC
def _define_DSBUFFERDESC1_head():
    class DSBUFFERDESC1(Structure):
        pass
    return DSBUFFERDESC1
def _define_DSBUFFERDESC1():
    DSBUFFERDESC1 = win32more.Media.Audio.DirectSound.DSBUFFERDESC1_head
    DSBUFFERDESC1._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwBufferBytes", UInt32),
        ("dwReserved", UInt32),
        ("lpwfxFormat", POINTER(win32more.Media.Audio.WAVEFORMATEX_head)),
    ]
    return DSBUFFERDESC1
def _define_DS3DBUFFER_head():
    class DS3DBUFFER(Structure):
        pass
    return DS3DBUFFER
def _define_DS3DBUFFER():
    DS3DBUFFER = win32more.Media.Audio.DirectSound.DS3DBUFFER_head
    DS3DBUFFER._fields_ = [
        ("dwSize", UInt32),
        ("vPosition", win32more.Graphics.Direct3D.D3DVECTOR),
        ("vVelocity", win32more.Graphics.Direct3D.D3DVECTOR),
        ("dwInsideConeAngle", UInt32),
        ("dwOutsideConeAngle", UInt32),
        ("vConeOrientation", win32more.Graphics.Direct3D.D3DVECTOR),
        ("lConeOutsideVolume", Int32),
        ("flMinDistance", Single),
        ("flMaxDistance", Single),
        ("dwMode", UInt32),
    ]
    return DS3DBUFFER
def _define_DS3DLISTENER_head():
    class DS3DLISTENER(Structure):
        pass
    return DS3DLISTENER
def _define_DS3DLISTENER():
    DS3DLISTENER = win32more.Media.Audio.DirectSound.DS3DLISTENER_head
    DS3DLISTENER._fields_ = [
        ("dwSize", UInt32),
        ("vPosition", win32more.Graphics.Direct3D.D3DVECTOR),
        ("vVelocity", win32more.Graphics.Direct3D.D3DVECTOR),
        ("vOrientFront", win32more.Graphics.Direct3D.D3DVECTOR),
        ("vOrientTop", win32more.Graphics.Direct3D.D3DVECTOR),
        ("flDistanceFactor", Single),
        ("flRolloffFactor", Single),
        ("flDopplerFactor", Single),
    ]
    return DS3DLISTENER
def _define_DSCCAPS_head():
    class DSCCAPS(Structure):
        pass
    return DSCCAPS
def _define_DSCCAPS():
    DSCCAPS = win32more.Media.Audio.DirectSound.DSCCAPS_head
    DSCCAPS._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwFormats", UInt32),
        ("dwChannels", UInt32),
    ]
    return DSCCAPS
def _define_DSCBUFFERDESC1_head():
    class DSCBUFFERDESC1(Structure):
        pass
    return DSCBUFFERDESC1
def _define_DSCBUFFERDESC1():
    DSCBUFFERDESC1 = win32more.Media.Audio.DirectSound.DSCBUFFERDESC1_head
    DSCBUFFERDESC1._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwBufferBytes", UInt32),
        ("dwReserved", UInt32),
        ("lpwfxFormat", POINTER(win32more.Media.Audio.WAVEFORMATEX_head)),
    ]
    return DSCBUFFERDESC1
def _define_DSCBUFFERDESC_head():
    class DSCBUFFERDESC(Structure):
        pass
    return DSCBUFFERDESC
def _define_DSCBUFFERDESC():
    DSCBUFFERDESC = win32more.Media.Audio.DirectSound.DSCBUFFERDESC_head
    DSCBUFFERDESC._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwBufferBytes", UInt32),
        ("dwReserved", UInt32),
        ("lpwfxFormat", POINTER(win32more.Media.Audio.WAVEFORMATEX_head)),
        ("dwFXCount", UInt32),
        ("lpDSCFXDesc", POINTER(win32more.Media.Audio.DirectSound.DSCEFFECTDESC_head)),
    ]
    return DSCBUFFERDESC
def _define_DSCBCAPS_head():
    class DSCBCAPS(Structure):
        pass
    return DSCBCAPS
def _define_DSCBCAPS():
    DSCBCAPS = win32more.Media.Audio.DirectSound.DSCBCAPS_head
    DSCBCAPS._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwBufferBytes", UInt32),
        ("dwReserved", UInt32),
    ]
    return DSCBCAPS
def _define_DSBPOSITIONNOTIFY_head():
    class DSBPOSITIONNOTIFY(Structure):
        pass
    return DSBPOSITIONNOTIFY
def _define_DSBPOSITIONNOTIFY():
    DSBPOSITIONNOTIFY = win32more.Media.Audio.DirectSound.DSBPOSITIONNOTIFY_head
    DSBPOSITIONNOTIFY._fields_ = [
        ("dwOffset", UInt32),
        ("hEventNotify", win32more.Foundation.HANDLE),
    ]
    return DSBPOSITIONNOTIFY
def _define_LPDSENUMCALLBACKA():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p, use_last_error=False)
def _define_LPDSENUMCALLBACKW():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)
def _define_IDirectSound_head():
    class IDirectSound(win32more.System.Com.IUnknown_head):
        Guid = Guid('279afa83-4981-11ce-a521-0020af0be560')
    return IDirectSound
def _define_IDirectSound():
    IDirectSound = win32more.Media.Audio.DirectSound.IDirectSound_head
    IDirectSound.CreateSoundBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSBUFFERDESC_head),POINTER(win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head),win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'CreateSoundBuffer', ((1, 'pcDSBufferDesc'),(1, 'ppDSBuffer'),(1, 'pUnkOuter'),)))
    IDirectSound.GetCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCAPS_head), use_last_error=False)(4, 'GetCaps', ((1, 'pDSCaps'),)))
    IDirectSound.DuplicateSoundBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head,POINTER(win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head), use_last_error=False)(5, 'DuplicateSoundBuffer', ((1, 'pDSBufferOriginal'),(1, 'ppDSBufferDuplicate'),)))
    IDirectSound.SetCooperativeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(6, 'SetCooperativeLevel', ((1, 'hwnd'),(1, 'dwLevel'),)))
    IDirectSound.Compact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Compact', ()))
    IDirectSound.GetSpeakerConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetSpeakerConfig', ((1, 'pdwSpeakerConfig'),)))
    IDirectSound.SetSpeakerConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetSpeakerConfig', ((1, 'dwSpeakerConfig'),)))
    IDirectSound.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(10, 'Initialize', ((1, 'pcGuidDevice'),)))
    return IDirectSound
def _define_IDirectSound8_head():
    class IDirectSound8(win32more.Media.Audio.DirectSound.IDirectSound_head):
        Guid = Guid('c50a7e93-f395-4834-9ef6-7fa99de50966')
    return IDirectSound8
def _define_IDirectSound8():
    IDirectSound8 = win32more.Media.Audio.DirectSound.IDirectSound8_head
    IDirectSound8.VerifyCertification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'VerifyCertification', ((1, 'pdwCertified'),)))
    return IDirectSound8
def _define_IDirectSoundBuffer_head():
    class IDirectSoundBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('279afa85-4981-11ce-a521-0020af0be560')
    return IDirectSoundBuffer
def _define_IDirectSoundBuffer():
    IDirectSoundBuffer = win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head
    IDirectSoundBuffer.GetCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSBCAPS_head), use_last_error=False)(3, 'GetCaps', ((1, 'pDSBufferCaps'),)))
    IDirectSoundBuffer.GetCurrentPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetCurrentPosition', ((1, 'pdwCurrentPlayCursor'),(1, 'pdwCurrentWriteCursor'),)))
    IDirectSoundBuffer.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.WAVEFORMATEX_head),UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetFormat', ((1, 'pwfxFormat'),(1, 'dwSizeAllocated'),(1, 'pdwSizeWritten'),)))
    IDirectSoundBuffer.GetVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'GetVolume', ((1, 'plVolume'),)))
    IDirectSoundBuffer.GetPan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'GetPan', ((1, 'plPan'),)))
    IDirectSoundBuffer.GetFrequency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetFrequency', ((1, 'pdwFrequency'),)))
    IDirectSoundBuffer.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetStatus', ((1, 'pdwStatus'),)))
    IDirectSoundBuffer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.IDirectSound_head,POINTER(win32more.Media.Audio.DirectSound.DSBUFFERDESC_head), use_last_error=False)(10, 'Initialize', ((1, 'pDirectSound'),(1, 'pcDSBufferDesc'),)))
    IDirectSoundBuffer.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(c_void_p),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32),UInt32, use_last_error=False)(11, 'Lock', ((1, 'dwOffset'),(1, 'dwBytes'),(1, 'ppvAudioPtr1'),(1, 'pdwAudioBytes1'),(1, 'ppvAudioPtr2'),(1, 'pdwAudioBytes2'),(1, 'dwFlags'),)))
    IDirectSoundBuffer.Play = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(12, 'Play', ((1, 'dwReserved1'),(1, 'dwPriority'),(1, 'dwFlags'),)))
    IDirectSoundBuffer.SetCurrentPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(13, 'SetCurrentPosition', ((1, 'dwNewPosition'),)))
    IDirectSoundBuffer.SetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.WAVEFORMATEX_head), use_last_error=False)(14, 'SetFormat', ((1, 'pcfxFormat'),)))
    IDirectSoundBuffer.SetVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'SetVolume', ((1, 'lVolume'),)))
    IDirectSoundBuffer.SetPan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'SetPan', ((1, 'lPan'),)))
    IDirectSoundBuffer.SetFrequency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(17, 'SetFrequency', ((1, 'dwFrequency'),)))
    IDirectSoundBuffer.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'Stop', ()))
    IDirectSoundBuffer.Unlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(19, 'Unlock', ((1, 'pvAudioPtr1'),(1, 'dwAudioBytes1'),(1, 'pvAudioPtr2'),(1, 'dwAudioBytes2'),)))
    IDirectSoundBuffer.Restore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'Restore', ()))
    return IDirectSoundBuffer
def _define_IDirectSoundBuffer8_head():
    class IDirectSoundBuffer8(win32more.Media.Audio.DirectSound.IDirectSoundBuffer_head):
        Guid = Guid('6825a449-7524-4d82-920f-50e36ab3ab1e')
    return IDirectSoundBuffer8
def _define_IDirectSoundBuffer8():
    IDirectSoundBuffer8 = win32more.Media.Audio.DirectSound.IDirectSoundBuffer8_head
    IDirectSoundBuffer8.SetFX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.DirectSound.DSEFFECTDESC),POINTER(UInt32), use_last_error=False)(21, 'SetFX', ((1, 'dwEffectsCount'),(1, 'pDSFXDesc'),(1, 'pdwResultCodes'),)))
    IDirectSoundBuffer8.AcquireResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(22, 'AcquireResources', ((1, 'dwFlags'),(1, 'dwEffectsCount'),(1, 'pdwResultCodes'),)))
    IDirectSoundBuffer8.GetObjectInPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(23, 'GetObjectInPath', ((1, 'rguidObject'),(1, 'dwIndex'),(1, 'rguidInterface'),(1, 'ppObject'),)))
    return IDirectSoundBuffer8
def _define_IDirectSound3DListener_head():
    class IDirectSound3DListener(win32more.System.Com.IUnknown_head):
        Guid = Guid('279afa84-4981-11ce-a521-0020af0be560')
    return IDirectSound3DListener
def _define_IDirectSound3DListener():
    IDirectSound3DListener = win32more.Media.Audio.DirectSound.IDirectSound3DListener_head
    IDirectSound3DListener.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DS3DLISTENER_head), use_last_error=False)(3, 'GetAllParameters', ((1, 'pListener'),)))
    IDirectSound3DListener.GetDistanceFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(4, 'GetDistanceFactor', ((1, 'pflDistanceFactor'),)))
    IDirectSound3DListener.GetDopplerFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(5, 'GetDopplerFactor', ((1, 'pflDopplerFactor'),)))
    IDirectSound3DListener.GetOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3DVECTOR_head),POINTER(win32more.Graphics.Direct3D.D3DVECTOR_head), use_last_error=False)(6, 'GetOrientation', ((1, 'pvOrientFront'),(1, 'pvOrientTop'),)))
    IDirectSound3DListener.GetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3DVECTOR_head), use_last_error=False)(7, 'GetPosition', ((1, 'pvPosition'),)))
    IDirectSound3DListener.GetRolloffFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(8, 'GetRolloffFactor', ((1, 'pflRolloffFactor'),)))
    IDirectSound3DListener.GetVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3DVECTOR_head), use_last_error=False)(9, 'GetVelocity', ((1, 'pvVelocity'),)))
    IDirectSound3DListener.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DS3DLISTENER_head),UInt32, use_last_error=False)(10, 'SetAllParameters', ((1, 'pcListener'),(1, 'dwApply'),)))
    IDirectSound3DListener.SetDistanceFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32, use_last_error=False)(11, 'SetDistanceFactor', ((1, 'flDistanceFactor'),(1, 'dwApply'),)))
    IDirectSound3DListener.SetDopplerFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32, use_last_error=False)(12, 'SetDopplerFactor', ((1, 'flDopplerFactor'),(1, 'dwApply'),)))
    IDirectSound3DListener.SetOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,Single,Single,UInt32, use_last_error=False)(13, 'SetOrientation', ((1, 'xFront'),(1, 'yFront'),(1, 'zFront'),(1, 'xTop'),(1, 'yTop'),(1, 'zTop'),(1, 'dwApply'),)))
    IDirectSound3DListener.SetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,UInt32, use_last_error=False)(14, 'SetPosition', ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'dwApply'),)))
    IDirectSound3DListener.SetRolloffFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32, use_last_error=False)(15, 'SetRolloffFactor', ((1, 'flRolloffFactor'),(1, 'dwApply'),)))
    IDirectSound3DListener.SetVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,UInt32, use_last_error=False)(16, 'SetVelocity', ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'dwApply'),)))
    IDirectSound3DListener.CommitDeferredSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'CommitDeferredSettings', ()))
    return IDirectSound3DListener
def _define_IDirectSound3DBuffer_head():
    class IDirectSound3DBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('279afa86-4981-11ce-a521-0020af0be560')
    return IDirectSound3DBuffer
def _define_IDirectSound3DBuffer():
    IDirectSound3DBuffer = win32more.Media.Audio.DirectSound.IDirectSound3DBuffer_head
    IDirectSound3DBuffer.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DS3DBUFFER_head), use_last_error=False)(3, 'GetAllParameters', ((1, 'pDs3dBuffer'),)))
    IDirectSound3DBuffer.GetConeAngles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetConeAngles', ((1, 'pdwInsideConeAngle'),(1, 'pdwOutsideConeAngle'),)))
    IDirectSound3DBuffer.GetConeOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3DVECTOR_head), use_last_error=False)(5, 'GetConeOrientation', ((1, 'pvOrientation'),)))
    IDirectSound3DBuffer.GetConeOutsideVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'GetConeOutsideVolume', ((1, 'plConeOutsideVolume'),)))
    IDirectSound3DBuffer.GetMaxDistance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(7, 'GetMaxDistance', ((1, 'pflMaxDistance'),)))
    IDirectSound3DBuffer.GetMinDistance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(8, 'GetMinDistance', ((1, 'pflMinDistance'),)))
    IDirectSound3DBuffer.GetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetMode', ((1, 'pdwMode'),)))
    IDirectSound3DBuffer.GetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3DVECTOR_head), use_last_error=False)(10, 'GetPosition', ((1, 'pvPosition'),)))
    IDirectSound3DBuffer.GetVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3DVECTOR_head), use_last_error=False)(11, 'GetVelocity', ((1, 'pvVelocity'),)))
    IDirectSound3DBuffer.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DS3DBUFFER_head),UInt32, use_last_error=False)(12, 'SetAllParameters', ((1, 'pcDs3dBuffer'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetConeAngles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(13, 'SetConeAngles', ((1, 'dwInsideConeAngle'),(1, 'dwOutsideConeAngle'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetConeOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,UInt32, use_last_error=False)(14, 'SetConeOrientation', ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetConeOutsideVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32, use_last_error=False)(15, 'SetConeOutsideVolume', ((1, 'lConeOutsideVolume'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetMaxDistance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32, use_last_error=False)(16, 'SetMaxDistance', ((1, 'flMaxDistance'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetMinDistance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32, use_last_error=False)(17, 'SetMinDistance', ((1, 'flMinDistance'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(18, 'SetMode', ((1, 'dwMode'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,UInt32, use_last_error=False)(19, 'SetPosition', ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'dwApply'),)))
    IDirectSound3DBuffer.SetVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,UInt32, use_last_error=False)(20, 'SetVelocity', ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'dwApply'),)))
    return IDirectSound3DBuffer
def _define_IDirectSoundCapture_head():
    class IDirectSoundCapture(win32more.System.Com.IUnknown_head):
        Guid = Guid('b0210781-89cd-11d0-af08-00a0c925cd16')
    return IDirectSoundCapture
def _define_IDirectSoundCapture():
    IDirectSoundCapture = win32more.Media.Audio.DirectSound.IDirectSoundCapture_head
    IDirectSoundCapture.CreateCaptureBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCBUFFERDESC_head),POINTER(win32more.Media.Audio.DirectSound.IDirectSoundCaptureBuffer_head),win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'CreateCaptureBuffer', ((1, 'pcDSCBufferDesc'),(1, 'ppDSCBuffer'),(1, 'pUnkOuter'),)))
    IDirectSoundCapture.GetCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCCAPS_head), use_last_error=False)(4, 'GetCaps', ((1, 'pDSCCaps'),)))
    IDirectSoundCapture.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'Initialize', ((1, 'pcGuidDevice'),)))
    return IDirectSoundCapture
def _define_IDirectSoundCaptureBuffer_head():
    class IDirectSoundCaptureBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('b0210782-89cd-11d0-af08-00a0c925cd16')
    return IDirectSoundCaptureBuffer
def _define_IDirectSoundCaptureBuffer():
    IDirectSoundCaptureBuffer = win32more.Media.Audio.DirectSound.IDirectSoundCaptureBuffer_head
    IDirectSoundCaptureBuffer.GetCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCBCAPS_head), use_last_error=False)(3, 'GetCaps', ((1, 'pDSCBCaps'),)))
    IDirectSoundCaptureBuffer.GetCurrentPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetCurrentPosition', ((1, 'pdwCapturePosition'),(1, 'pdwReadPosition'),)))
    IDirectSoundCaptureBuffer.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.WAVEFORMATEX_head),UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetFormat', ((1, 'pwfxFormat'),(1, 'dwSizeAllocated'),(1, 'pdwSizeWritten'),)))
    IDirectSoundCaptureBuffer.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetStatus', ((1, 'pdwStatus'),)))
    IDirectSoundCaptureBuffer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.IDirectSoundCapture_head,POINTER(win32more.Media.Audio.DirectSound.DSCBUFFERDESC_head), use_last_error=False)(7, 'Initialize', ((1, 'pDirectSoundCapture'),(1, 'pcDSCBufferDesc'),)))
    IDirectSoundCaptureBuffer.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(c_void_p),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32),UInt32, use_last_error=False)(8, 'Lock', ((1, 'dwOffset'),(1, 'dwBytes'),(1, 'ppvAudioPtr1'),(1, 'pdwAudioBytes1'),(1, 'ppvAudioPtr2'),(1, 'pdwAudioBytes2'),(1, 'dwFlags'),)))
    IDirectSoundCaptureBuffer.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'Start', ((1, 'dwFlags'),)))
    IDirectSoundCaptureBuffer.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Stop', ()))
    IDirectSoundCaptureBuffer.Unlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(11, 'Unlock', ((1, 'pvAudioPtr1'),(1, 'dwAudioBytes1'),(1, 'pvAudioPtr2'),(1, 'dwAudioBytes2'),)))
    return IDirectSoundCaptureBuffer
def _define_IDirectSoundCaptureBuffer8_head():
    class IDirectSoundCaptureBuffer8(win32more.Media.Audio.DirectSound.IDirectSoundCaptureBuffer_head):
        Guid = Guid('00990df4-0dbb-4872-833e-6d303e80aeb6')
    return IDirectSoundCaptureBuffer8
def _define_IDirectSoundCaptureBuffer8():
    IDirectSoundCaptureBuffer8 = win32more.Media.Audio.DirectSound.IDirectSoundCaptureBuffer8_head
    IDirectSoundCaptureBuffer8.GetObjectInPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(12, 'GetObjectInPath', ((1, 'rguidObject'),(1, 'dwIndex'),(1, 'rguidInterface'),(1, 'ppObject'),)))
    IDirectSoundCaptureBuffer8.GetFXStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(13, 'GetFXStatus', ((1, 'dwEffectsCount'),(1, 'pdwFXStatus'),)))
    return IDirectSoundCaptureBuffer8
def _define_IDirectSoundNotify_head():
    class IDirectSoundNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('b0210783-89cd-11d0-af08-00a0c925cd16')
    return IDirectSoundNotify
def _define_IDirectSoundNotify():
    IDirectSoundNotify = win32more.Media.Audio.DirectSound.IDirectSoundNotify_head
    IDirectSoundNotify.SetNotificationPositions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.DirectSound.DSBPOSITIONNOTIFY), use_last_error=False)(3, 'SetNotificationPositions', ((1, 'dwPositionNotifies'),(1, 'pcPositionNotifies'),)))
    return IDirectSoundNotify
def _define_DSFXGargle_head():
    class DSFXGargle(Structure):
        pass
    return DSFXGargle
def _define_DSFXGargle():
    DSFXGargle = win32more.Media.Audio.DirectSound.DSFXGargle_head
    DSFXGargle._fields_ = [
        ("dwRateHz", UInt32),
        ("dwWaveShape", UInt32),
    ]
    return DSFXGargle
def _define_IDirectSoundFXGargle_head():
    class IDirectSoundFXGargle(win32more.System.Com.IUnknown_head):
        Guid = Guid('d616f352-d622-11ce-aac5-0020af0b99a3')
    return IDirectSoundFXGargle
def _define_IDirectSoundFXGargle():
    IDirectSoundFXGargle = win32more.Media.Audio.DirectSound.IDirectSoundFXGargle_head
    IDirectSoundFXGargle.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXGargle_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxGargle'),)))
    IDirectSoundFXGargle.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXGargle_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxGargle'),)))
    return IDirectSoundFXGargle
def _define_DSFXChorus_head():
    class DSFXChorus(Structure):
        pass
    return DSFXChorus
def _define_DSFXChorus():
    DSFXChorus = win32more.Media.Audio.DirectSound.DSFXChorus_head
    DSFXChorus._fields_ = [
        ("fWetDryMix", Single),
        ("fDepth", Single),
        ("fFeedback", Single),
        ("fFrequency", Single),
        ("lWaveform", Int32),
        ("fDelay", Single),
        ("lPhase", Int32),
    ]
    return DSFXChorus
def _define_IDirectSoundFXChorus_head():
    class IDirectSoundFXChorus(win32more.System.Com.IUnknown_head):
        Guid = Guid('880842e3-145f-43e6-a934-a71806e50547')
    return IDirectSoundFXChorus
def _define_IDirectSoundFXChorus():
    IDirectSoundFXChorus = win32more.Media.Audio.DirectSound.IDirectSoundFXChorus_head
    IDirectSoundFXChorus.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXChorus_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxChorus'),)))
    IDirectSoundFXChorus.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXChorus_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxChorus'),)))
    return IDirectSoundFXChorus
def _define_DSFXFlanger_head():
    class DSFXFlanger(Structure):
        pass
    return DSFXFlanger
def _define_DSFXFlanger():
    DSFXFlanger = win32more.Media.Audio.DirectSound.DSFXFlanger_head
    DSFXFlanger._fields_ = [
        ("fWetDryMix", Single),
        ("fDepth", Single),
        ("fFeedback", Single),
        ("fFrequency", Single),
        ("lWaveform", Int32),
        ("fDelay", Single),
        ("lPhase", Int32),
    ]
    return DSFXFlanger
def _define_IDirectSoundFXFlanger_head():
    class IDirectSoundFXFlanger(win32more.System.Com.IUnknown_head):
        Guid = Guid('903e9878-2c92-4072-9b2c-ea68f5396783')
    return IDirectSoundFXFlanger
def _define_IDirectSoundFXFlanger():
    IDirectSoundFXFlanger = win32more.Media.Audio.DirectSound.IDirectSoundFXFlanger_head
    IDirectSoundFXFlanger.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXFlanger_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxFlanger'),)))
    IDirectSoundFXFlanger.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXFlanger_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxFlanger'),)))
    return IDirectSoundFXFlanger
def _define_DSFXEcho_head():
    class DSFXEcho(Structure):
        pass
    return DSFXEcho
def _define_DSFXEcho():
    DSFXEcho = win32more.Media.Audio.DirectSound.DSFXEcho_head
    DSFXEcho._fields_ = [
        ("fWetDryMix", Single),
        ("fFeedback", Single),
        ("fLeftDelay", Single),
        ("fRightDelay", Single),
        ("lPanDelay", Int32),
    ]
    return DSFXEcho
def _define_IDirectSoundFXEcho_head():
    class IDirectSoundFXEcho(win32more.System.Com.IUnknown_head):
        Guid = Guid('8bd28edf-50db-4e92-a2bd-445488d1ed42')
    return IDirectSoundFXEcho
def _define_IDirectSoundFXEcho():
    IDirectSoundFXEcho = win32more.Media.Audio.DirectSound.IDirectSoundFXEcho_head
    IDirectSoundFXEcho.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXEcho_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxEcho'),)))
    IDirectSoundFXEcho.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXEcho_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxEcho'),)))
    return IDirectSoundFXEcho
def _define_DSFXDistortion_head():
    class DSFXDistortion(Structure):
        pass
    return DSFXDistortion
def _define_DSFXDistortion():
    DSFXDistortion = win32more.Media.Audio.DirectSound.DSFXDistortion_head
    DSFXDistortion._fields_ = [
        ("fGain", Single),
        ("fEdge", Single),
        ("fPostEQCenterFrequency", Single),
        ("fPostEQBandwidth", Single),
        ("fPreLowpassCutoff", Single),
    ]
    return DSFXDistortion
def _define_IDirectSoundFXDistortion_head():
    class IDirectSoundFXDistortion(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ecf4326-455f-4d8b-bda9-8d5d3e9e3e0b')
    return IDirectSoundFXDistortion
def _define_IDirectSoundFXDistortion():
    IDirectSoundFXDistortion = win32more.Media.Audio.DirectSound.IDirectSoundFXDistortion_head
    IDirectSoundFXDistortion.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXDistortion_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxDistortion'),)))
    IDirectSoundFXDistortion.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXDistortion_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxDistortion'),)))
    return IDirectSoundFXDistortion
def _define_DSFXCompressor_head():
    class DSFXCompressor(Structure):
        pass
    return DSFXCompressor
def _define_DSFXCompressor():
    DSFXCompressor = win32more.Media.Audio.DirectSound.DSFXCompressor_head
    DSFXCompressor._fields_ = [
        ("fGain", Single),
        ("fAttack", Single),
        ("fRelease", Single),
        ("fThreshold", Single),
        ("fRatio", Single),
        ("fPredelay", Single),
    ]
    return DSFXCompressor
def _define_IDirectSoundFXCompressor_head():
    class IDirectSoundFXCompressor(win32more.System.Com.IUnknown_head):
        Guid = Guid('4bbd1154-62f6-4e2c-a15c-d3b6c417f7a0')
    return IDirectSoundFXCompressor
def _define_IDirectSoundFXCompressor():
    IDirectSoundFXCompressor = win32more.Media.Audio.DirectSound.IDirectSoundFXCompressor_head
    IDirectSoundFXCompressor.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXCompressor_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxCompressor'),)))
    IDirectSoundFXCompressor.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXCompressor_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxCompressor'),)))
    return IDirectSoundFXCompressor
def _define_DSFXParamEq_head():
    class DSFXParamEq(Structure):
        pass
    return DSFXParamEq
def _define_DSFXParamEq():
    DSFXParamEq = win32more.Media.Audio.DirectSound.DSFXParamEq_head
    DSFXParamEq._fields_ = [
        ("fCenter", Single),
        ("fBandwidth", Single),
        ("fGain", Single),
    ]
    return DSFXParamEq
def _define_IDirectSoundFXParamEq_head():
    class IDirectSoundFXParamEq(win32more.System.Com.IUnknown_head):
        Guid = Guid('c03ca9fe-fe90-4204-8078-82334cd177da')
    return IDirectSoundFXParamEq
def _define_IDirectSoundFXParamEq():
    IDirectSoundFXParamEq = win32more.Media.Audio.DirectSound.IDirectSoundFXParamEq_head
    IDirectSoundFXParamEq.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXParamEq_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxParamEq'),)))
    IDirectSoundFXParamEq.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXParamEq_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxParamEq'),)))
    return IDirectSoundFXParamEq
def _define_DSFXI3DL2Reverb_head():
    class DSFXI3DL2Reverb(Structure):
        pass
    return DSFXI3DL2Reverb
def _define_DSFXI3DL2Reverb():
    DSFXI3DL2Reverb = win32more.Media.Audio.DirectSound.DSFXI3DL2Reverb_head
    DSFXI3DL2Reverb._fields_ = [
        ("lRoom", Int32),
        ("lRoomHF", Int32),
        ("flRoomRolloffFactor", Single),
        ("flDecayTime", Single),
        ("flDecayHFRatio", Single),
        ("lReflections", Int32),
        ("flReflectionsDelay", Single),
        ("lReverb", Int32),
        ("flReverbDelay", Single),
        ("flDiffusion", Single),
        ("flDensity", Single),
        ("flHFReference", Single),
    ]
    return DSFXI3DL2Reverb
def _define_IDirectSoundFXI3DL2Reverb_head():
    class IDirectSoundFXI3DL2Reverb(win32more.System.Com.IUnknown_head):
        Guid = Guid('4b166a6a-0d66-43f3-80e3-ee6280dee1a4')
    return IDirectSoundFXI3DL2Reverb
def _define_IDirectSoundFXI3DL2Reverb():
    IDirectSoundFXI3DL2Reverb = win32more.Media.Audio.DirectSound.IDirectSoundFXI3DL2Reverb_head
    IDirectSoundFXI3DL2Reverb.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXI3DL2Reverb_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxI3DL2Reverb'),)))
    IDirectSoundFXI3DL2Reverb.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXI3DL2Reverb_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxI3DL2Reverb'),)))
    IDirectSoundFXI3DL2Reverb.SetPreset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetPreset', ((1, 'dwPreset'),)))
    IDirectSoundFXI3DL2Reverb.GetPreset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetPreset', ((1, 'pdwPreset'),)))
    IDirectSoundFXI3DL2Reverb.SetQuality = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'SetQuality', ((1, 'lQuality'),)))
    IDirectSoundFXI3DL2Reverb.GetQuality = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetQuality', ((1, 'plQuality'),)))
    return IDirectSoundFXI3DL2Reverb
def _define_DSFXWavesReverb_head():
    class DSFXWavesReverb(Structure):
        pass
    return DSFXWavesReverb
def _define_DSFXWavesReverb():
    DSFXWavesReverb = win32more.Media.Audio.DirectSound.DSFXWavesReverb_head
    DSFXWavesReverb._fields_ = [
        ("fInGain", Single),
        ("fReverbMix", Single),
        ("fReverbTime", Single),
        ("fHighFreqRTRatio", Single),
    ]
    return DSFXWavesReverb
def _define_IDirectSoundFXWavesReverb_head():
    class IDirectSoundFXWavesReverb(win32more.System.Com.IUnknown_head):
        Guid = Guid('46858c3a-0dc6-45e3-b760-d4eef16cb325')
    return IDirectSoundFXWavesReverb
def _define_IDirectSoundFXWavesReverb():
    IDirectSoundFXWavesReverb = win32more.Media.Audio.DirectSound.IDirectSoundFXWavesReverb_head
    IDirectSoundFXWavesReverb.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXWavesReverb_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDsFxWavesReverb'),)))
    IDirectSoundFXWavesReverb.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSFXWavesReverb_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDsFxWavesReverb'),)))
    return IDirectSoundFXWavesReverb
def _define_DSCFXAec_head():
    class DSCFXAec(Structure):
        pass
    return DSCFXAec
def _define_DSCFXAec():
    DSCFXAec = win32more.Media.Audio.DirectSound.DSCFXAec_head
    DSCFXAec._fields_ = [
        ("fEnable", win32more.Foundation.BOOL),
        ("fNoiseFill", win32more.Foundation.BOOL),
        ("dwMode", UInt32),
    ]
    return DSCFXAec
def _define_IDirectSoundCaptureFXAec_head():
    class IDirectSoundCaptureFXAec(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad74143d-903d-4ab7-8066-28d363036d65')
    return IDirectSoundCaptureFXAec
def _define_IDirectSoundCaptureFXAec():
    IDirectSoundCaptureFXAec = win32more.Media.Audio.DirectSound.IDirectSoundCaptureFXAec_head
    IDirectSoundCaptureFXAec.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCFXAec_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pDscFxAec'),)))
    IDirectSoundCaptureFXAec.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCFXAec_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDscFxAec'),)))
    IDirectSoundCaptureFXAec.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetStatus', ((1, 'pdwStatus'),)))
    IDirectSoundCaptureFXAec.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Reset', ()))
    return IDirectSoundCaptureFXAec
def _define_DSCFXNoiseSuppress_head():
    class DSCFXNoiseSuppress(Structure):
        pass
    return DSCFXNoiseSuppress
def _define_DSCFXNoiseSuppress():
    DSCFXNoiseSuppress = win32more.Media.Audio.DirectSound.DSCFXNoiseSuppress_head
    DSCFXNoiseSuppress._fields_ = [
        ("fEnable", win32more.Foundation.BOOL),
    ]
    return DSCFXNoiseSuppress
def _define_IDirectSoundCaptureFXNoiseSuppress_head():
    class IDirectSoundCaptureFXNoiseSuppress(win32more.System.Com.IUnknown_head):
        Guid = Guid('ed311e41-fbae-4175-9625-cd0854f693ca')
    return IDirectSoundCaptureFXNoiseSuppress
def _define_IDirectSoundCaptureFXNoiseSuppress():
    IDirectSoundCaptureFXNoiseSuppress = win32more.Media.Audio.DirectSound.IDirectSoundCaptureFXNoiseSuppress_head
    IDirectSoundCaptureFXNoiseSuppress.SetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCFXNoiseSuppress_head), use_last_error=False)(3, 'SetAllParameters', ((1, 'pcDscFxNoiseSuppress'),)))
    IDirectSoundCaptureFXNoiseSuppress.GetAllParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.DirectSound.DSCFXNoiseSuppress_head), use_last_error=False)(4, 'GetAllParameters', ((1, 'pDscFxNoiseSuppress'),)))
    IDirectSoundCaptureFXNoiseSuppress.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    return IDirectSoundCaptureFXNoiseSuppress
def _define_IDirectSoundFullDuplex_head():
    class IDirectSoundFullDuplex(win32more.System.Com.IUnknown_head):
        Guid = Guid('edcb4c7a-daab-4216-a42e-6c50596ddc1d')
    return IDirectSoundFullDuplex
def _define_IDirectSoundFullDuplex():
    IDirectSoundFullDuplex = win32more.Media.Audio.DirectSound.IDirectSoundFullDuplex_head
    IDirectSoundFullDuplex.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Media.Audio.DirectSound.DSCBUFFERDESC_head),POINTER(win32more.Media.Audio.DirectSound.DSBUFFERDESC_head),win32more.Foundation.HWND,UInt32,POINTER(win32more.Media.Audio.DirectSound.IDirectSoundCaptureBuffer8_head),POINTER(win32more.Media.Audio.DirectSound.IDirectSoundBuffer8_head), use_last_error=False)(3, 'Initialize', ((1, 'pCaptureGuid'),(1, 'pRenderGuid'),(1, 'lpDscBufferDesc'),(1, 'lpDsBufferDesc'),(1, 'hWnd'),(1, 'dwLevel'),(1, 'lplpDirectSoundCaptureBuffer8'),(1, 'lplpDirectSoundBuffer8'),)))
    return IDirectSoundFullDuplex
def _define_DirectSoundCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.DirectSound.IDirectSound_head),win32more.System.Com.IUnknown_head, use_last_error=False)(("DirectSoundCreate", windll["DSOUND"]), ((1, 'pcGuidDevice'),(1, 'ppDS'),(1, 'pUnkOuter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundEnumerateA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.LPDSENUMCALLBACKA,c_void_p, use_last_error=False)(("DirectSoundEnumerateA", windll["DSOUND"]), ((1, 'pDSEnumCallback'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundEnumerateW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.LPDSENUMCALLBACKW,c_void_p, use_last_error=False)(("DirectSoundEnumerateW", windll["DSOUND"]), ((1, 'pDSEnumCallback'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundEnumerate():
    return win32more.Media.Audio.DirectSound.DirectSoundEnumerateW
def _define_DirectSoundCaptureCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.DirectSound.IDirectSoundCapture_head),win32more.System.Com.IUnknown_head, use_last_error=False)(("DirectSoundCaptureCreate", windll["DSOUND"]), ((1, 'pcGuidDevice'),(1, 'ppDSC'),(1, 'pUnkOuter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundCaptureEnumerateA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.LPDSENUMCALLBACKA,c_void_p, use_last_error=False)(("DirectSoundCaptureEnumerateA", windll["DSOUND"]), ((1, 'pDSEnumCallback'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundCaptureEnumerateW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.DirectSound.LPDSENUMCALLBACKW,c_void_p, use_last_error=False)(("DirectSoundCaptureEnumerateW", windll["DSOUND"]), ((1, 'pDSEnumCallback'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundCaptureEnumerate():
    return win32more.Media.Audio.DirectSound.DirectSoundCaptureEnumerateW
def _define_DirectSoundCreate8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.DirectSound.IDirectSound8_head),win32more.System.Com.IUnknown_head, use_last_error=False)(("DirectSoundCreate8", windll["DSOUND"]), ((1, 'pcGuidDevice'),(1, 'ppDS8'),(1, 'pUnkOuter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundCaptureCreate8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.DirectSound.IDirectSoundCapture_head),win32more.System.Com.IUnknown_head, use_last_error=False)(("DirectSoundCaptureCreate8", windll["DSOUND"]), ((1, 'pcGuidDevice'),(1, 'ppDSC8'),(1, 'pUnkOuter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DirectSoundFullDuplexCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Media.Audio.DirectSound.DSCBUFFERDESC_head),POINTER(win32more.Media.Audio.DirectSound.DSBUFFERDESC_head),win32more.Foundation.HWND,UInt32,POINTER(win32more.Media.Audio.DirectSound.IDirectSoundFullDuplex_head),POINTER(win32more.Media.Audio.DirectSound.IDirectSoundCaptureBuffer8_head),POINTER(win32more.Media.Audio.DirectSound.IDirectSoundBuffer8_head),win32more.System.Com.IUnknown_head, use_last_error=False)(("DirectSoundFullDuplexCreate", windll["DSOUND"]), ((1, 'pcGuidCaptureDevice'),(1, 'pcGuidRenderDevice'),(1, 'pcDSCBufferDesc'),(1, 'pcDSBufferDesc'),(1, 'hWnd'),(1, 'dwLevel'),(1, 'ppDSFD'),(1, 'ppDSCBuffer8'),(1, 'ppDSBuffer8'),(1, 'pUnkOuter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDeviceID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(("GetDeviceID", windll["DSOUND"]), ((1, 'pGuidSrc'),(1, 'pGuidDest'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DIRECTSOUND_VERSION",
    "_FACDS",
    "CLSID_DirectSound",
    "CLSID_DirectSound8",
    "CLSID_DirectSoundCapture",
    "CLSID_DirectSoundCapture8",
    "CLSID_DirectSoundFullDuplex",
    "DSDEVID_DefaultPlayback",
    "DSDEVID_DefaultCapture",
    "DSDEVID_DefaultVoicePlayback",
    "DSDEVID_DefaultVoiceCapture",
    "DSFX_LOCHARDWARE",
    "DSFX_LOCSOFTWARE",
    "DSCFX_LOCHARDWARE",
    "DSCFX_LOCSOFTWARE",
    "DSCFXR_LOCHARDWARE",
    "DSCFXR_LOCSOFTWARE",
    "GUID_All_Objects",
    "KSPROPERTY_SUPPORT_GET",
    "KSPROPERTY_SUPPORT_SET",
    "DSFXGARGLE_WAVE_TRIANGLE",
    "DSFXGARGLE_WAVE_SQUARE",
    "DSFXGARGLE_RATEHZ_MIN",
    "DSFXGARGLE_RATEHZ_MAX",
    "DSFXCHORUS_WAVE_TRIANGLE",
    "DSFXCHORUS_WAVE_SIN",
    "DSFXCHORUS_WETDRYMIX_MIN",
    "DSFXCHORUS_WETDRYMIX_MAX",
    "DSFXCHORUS_DEPTH_MIN",
    "DSFXCHORUS_DEPTH_MAX",
    "DSFXCHORUS_FEEDBACK_MIN",
    "DSFXCHORUS_FEEDBACK_MAX",
    "DSFXCHORUS_FREQUENCY_MIN",
    "DSFXCHORUS_FREQUENCY_MAX",
    "DSFXCHORUS_DELAY_MIN",
    "DSFXCHORUS_DELAY_MAX",
    "DSFXCHORUS_PHASE_MIN",
    "DSFXCHORUS_PHASE_MAX",
    "DSFXCHORUS_PHASE_NEG_180",
    "DSFXCHORUS_PHASE_NEG_90",
    "DSFXCHORUS_PHASE_ZERO",
    "DSFXCHORUS_PHASE_90",
    "DSFXCHORUS_PHASE_180",
    "DSFXFLANGER_WAVE_TRIANGLE",
    "DSFXFLANGER_WAVE_SIN",
    "DSFXFLANGER_WETDRYMIX_MIN",
    "DSFXFLANGER_WETDRYMIX_MAX",
    "DSFXFLANGER_FREQUENCY_MIN",
    "DSFXFLANGER_FREQUENCY_MAX",
    "DSFXFLANGER_DEPTH_MIN",
    "DSFXFLANGER_DEPTH_MAX",
    "DSFXFLANGER_PHASE_MIN",
    "DSFXFLANGER_PHASE_MAX",
    "DSFXFLANGER_FEEDBACK_MIN",
    "DSFXFLANGER_FEEDBACK_MAX",
    "DSFXFLANGER_DELAY_MIN",
    "DSFXFLANGER_DELAY_MAX",
    "DSFXFLANGER_PHASE_NEG_180",
    "DSFXFLANGER_PHASE_NEG_90",
    "DSFXFLANGER_PHASE_ZERO",
    "DSFXFLANGER_PHASE_90",
    "DSFXFLANGER_PHASE_180",
    "DSFXECHO_WETDRYMIX_MIN",
    "DSFXECHO_WETDRYMIX_MAX",
    "DSFXECHO_FEEDBACK_MIN",
    "DSFXECHO_FEEDBACK_MAX",
    "DSFXECHO_LEFTDELAY_MIN",
    "DSFXECHO_LEFTDELAY_MAX",
    "DSFXECHO_RIGHTDELAY_MIN",
    "DSFXECHO_RIGHTDELAY_MAX",
    "DSFXECHO_PANDELAY_MIN",
    "DSFXECHO_PANDELAY_MAX",
    "DSFXDISTORTION_GAIN_MIN",
    "DSFXDISTORTION_GAIN_MAX",
    "DSFXDISTORTION_EDGE_MIN",
    "DSFXDISTORTION_EDGE_MAX",
    "DSFXDISTORTION_POSTEQCENTERFREQUENCY_MIN",
    "DSFXDISTORTION_POSTEQCENTERFREQUENCY_MAX",
    "DSFXDISTORTION_POSTEQBANDWIDTH_MIN",
    "DSFXDISTORTION_POSTEQBANDWIDTH_MAX",
    "DSFXDISTORTION_PRELOWPASSCUTOFF_MIN",
    "DSFXDISTORTION_PRELOWPASSCUTOFF_MAX",
    "DSFXCOMPRESSOR_GAIN_MIN",
    "DSFXCOMPRESSOR_GAIN_MAX",
    "DSFXCOMPRESSOR_ATTACK_MIN",
    "DSFXCOMPRESSOR_ATTACK_MAX",
    "DSFXCOMPRESSOR_RELEASE_MIN",
    "DSFXCOMPRESSOR_RELEASE_MAX",
    "DSFXCOMPRESSOR_THRESHOLD_MIN",
    "DSFXCOMPRESSOR_THRESHOLD_MAX",
    "DSFXCOMPRESSOR_RATIO_MIN",
    "DSFXCOMPRESSOR_RATIO_MAX",
    "DSFXCOMPRESSOR_PREDELAY_MIN",
    "DSFXCOMPRESSOR_PREDELAY_MAX",
    "DSFXPARAMEQ_CENTER_MIN",
    "DSFXPARAMEQ_CENTER_MAX",
    "DSFXPARAMEQ_BANDWIDTH_MIN",
    "DSFXPARAMEQ_BANDWIDTH_MAX",
    "DSFXPARAMEQ_GAIN_MIN",
    "DSFXPARAMEQ_GAIN_MAX",
    "DSFX_I3DL2REVERB_ROOM_MIN",
    "DSFX_I3DL2REVERB_ROOM_MAX",
    "DSFX_I3DL2REVERB_ROOM_DEFAULT",
    "DSFX_I3DL2REVERB_ROOMHF_MIN",
    "DSFX_I3DL2REVERB_ROOMHF_MAX",
    "DSFX_I3DL2REVERB_ROOMHF_DEFAULT",
    "DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MIN",
    "DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MAX",
    "DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_DEFAULT",
    "DSFX_I3DL2REVERB_DECAYTIME_MIN",
    "DSFX_I3DL2REVERB_DECAYTIME_MAX",
    "DSFX_I3DL2REVERB_DECAYTIME_DEFAULT",
    "DSFX_I3DL2REVERB_DECAYHFRATIO_MIN",
    "DSFX_I3DL2REVERB_DECAYHFRATIO_MAX",
    "DSFX_I3DL2REVERB_DECAYHFRATIO_DEFAULT",
    "DSFX_I3DL2REVERB_REFLECTIONS_MIN",
    "DSFX_I3DL2REVERB_REFLECTIONS_MAX",
    "DSFX_I3DL2REVERB_REFLECTIONS_DEFAULT",
    "DSFX_I3DL2REVERB_REFLECTIONSDELAY_MIN",
    "DSFX_I3DL2REVERB_REFLECTIONSDELAY_MAX",
    "DSFX_I3DL2REVERB_REFLECTIONSDELAY_DEFAULT",
    "DSFX_I3DL2REVERB_REVERB_MIN",
    "DSFX_I3DL2REVERB_REVERB_MAX",
    "DSFX_I3DL2REVERB_REVERB_DEFAULT",
    "DSFX_I3DL2REVERB_REVERBDELAY_MIN",
    "DSFX_I3DL2REVERB_REVERBDELAY_MAX",
    "DSFX_I3DL2REVERB_REVERBDELAY_DEFAULT",
    "DSFX_I3DL2REVERB_DIFFUSION_MIN",
    "DSFX_I3DL2REVERB_DIFFUSION_MAX",
    "DSFX_I3DL2REVERB_DIFFUSION_DEFAULT",
    "DSFX_I3DL2REVERB_DENSITY_MIN",
    "DSFX_I3DL2REVERB_DENSITY_MAX",
    "DSFX_I3DL2REVERB_DENSITY_DEFAULT",
    "DSFX_I3DL2REVERB_HFREFERENCE_MIN",
    "DSFX_I3DL2REVERB_HFREFERENCE_MAX",
    "DSFX_I3DL2REVERB_HFREFERENCE_DEFAULT",
    "DSFX_I3DL2REVERB_QUALITY_MIN",
    "DSFX_I3DL2REVERB_QUALITY_MAX",
    "DSFX_I3DL2REVERB_QUALITY_DEFAULT",
    "DSFX_WAVESREVERB_INGAIN_MIN",
    "DSFX_WAVESREVERB_INGAIN_MAX",
    "DSFX_WAVESREVERB_INGAIN_DEFAULT",
    "DSFX_WAVESREVERB_REVERBMIX_MIN",
    "DSFX_WAVESREVERB_REVERBMIX_MAX",
    "DSFX_WAVESREVERB_REVERBMIX_DEFAULT",
    "DSFX_WAVESREVERB_REVERBTIME_MIN",
    "DSFX_WAVESREVERB_REVERBTIME_MAX",
    "DSFX_WAVESREVERB_REVERBTIME_DEFAULT",
    "DSFX_WAVESREVERB_HIGHFREQRTRATIO_MIN",
    "DSFX_WAVESREVERB_HIGHFREQRTRATIO_MAX",
    "DSFX_WAVESREVERB_HIGHFREQRTRATIO_DEFAULT",
    "DSCFX_AEC_MODE_PASS_THROUGH",
    "DSCFX_AEC_MODE_HALF_DUPLEX",
    "DSCFX_AEC_MODE_FULL_DUPLEX",
    "DSCFX_AEC_STATUS_HISTORY_UNINITIALIZED",
    "DSCFX_AEC_STATUS_HISTORY_CONTINUOUSLY_CONVERGED",
    "DSCFX_AEC_STATUS_HISTORY_PREVIOUSLY_DIVERGED",
    "DSCFX_AEC_STATUS_CURRENTLY_CONVERGED",
    "DS_NO_VIRTUALIZATION",
    "DSCAPS_PRIMARYMONO",
    "DSCAPS_PRIMARYSTEREO",
    "DSCAPS_PRIMARY8BIT",
    "DSCAPS_PRIMARY16BIT",
    "DSCAPS_CONTINUOUSRATE",
    "DSCAPS_EMULDRIVER",
    "DSCAPS_CERTIFIED",
    "DSCAPS_SECONDARYMONO",
    "DSCAPS_SECONDARYSTEREO",
    "DSCAPS_SECONDARY8BIT",
    "DSCAPS_SECONDARY16BIT",
    "DSSCL_NORMAL",
    "DSSCL_PRIORITY",
    "DSSCL_EXCLUSIVE",
    "DSSCL_WRITEPRIMARY",
    "DSSPEAKER_DIRECTOUT",
    "DSSPEAKER_HEADPHONE",
    "DSSPEAKER_MONO",
    "DSSPEAKER_QUAD",
    "DSSPEAKER_STEREO",
    "DSSPEAKER_SURROUND",
    "DSSPEAKER_5POINT1",
    "DSSPEAKER_7POINT1",
    "DSSPEAKER_7POINT1_SURROUND",
    "DSSPEAKER_5POINT1_SURROUND",
    "DSSPEAKER_7POINT1_WIDE",
    "DSSPEAKER_5POINT1_BACK",
    "DSSPEAKER_GEOMETRY_MIN",
    "DSSPEAKER_GEOMETRY_NARROW",
    "DSSPEAKER_GEOMETRY_WIDE",
    "DSSPEAKER_GEOMETRY_MAX",
    "DSBCAPS_PRIMARYBUFFER",
    "DSBCAPS_STATIC",
    "DSBCAPS_LOCHARDWARE",
    "DSBCAPS_LOCSOFTWARE",
    "DSBCAPS_CTRL3D",
    "DSBCAPS_CTRLFREQUENCY",
    "DSBCAPS_CTRLPAN",
    "DSBCAPS_CTRLVOLUME",
    "DSBCAPS_CTRLPOSITIONNOTIFY",
    "DSBCAPS_CTRLFX",
    "DSBCAPS_STICKYFOCUS",
    "DSBCAPS_GLOBALFOCUS",
    "DSBCAPS_GETCURRENTPOSITION2",
    "DSBCAPS_MUTE3DATMAXDISTANCE",
    "DSBCAPS_LOCDEFER",
    "DSBCAPS_TRUEPLAYPOSITION",
    "DSBPLAY_LOOPING",
    "DSBPLAY_LOCHARDWARE",
    "DSBPLAY_LOCSOFTWARE",
    "DSBPLAY_TERMINATEBY_TIME",
    "DSBPLAY_TERMINATEBY_DISTANCE",
    "DSBPLAY_TERMINATEBY_PRIORITY",
    "DSBSTATUS_PLAYING",
    "DSBSTATUS_BUFFERLOST",
    "DSBSTATUS_LOOPING",
    "DSBSTATUS_LOCHARDWARE",
    "DSBSTATUS_LOCSOFTWARE",
    "DSBSTATUS_TERMINATED",
    "DSBLOCK_FROMWRITECURSOR",
    "DSBLOCK_ENTIREBUFFER",
    "DSBFREQUENCY_ORIGINAL",
    "DSBFREQUENCY_MIN",
    "DSBFREQUENCY_MAX",
    "DSBPAN_LEFT",
    "DSBPAN_CENTER",
    "DSBPAN_RIGHT",
    "DSBVOLUME_MIN",
    "DSBVOLUME_MAX",
    "DSBSIZE_MIN",
    "DSBSIZE_MAX",
    "DSBSIZE_FX_MIN",
    "DSBNOTIFICATIONS_MAX",
    "DS3DMODE_NORMAL",
    "DS3DMODE_HEADRELATIVE",
    "DS3DMODE_DISABLE",
    "DS3D_IMMEDIATE",
    "DS3D_DEFERRED",
    "DS3D_DEFAULTDISTANCEFACTOR",
    "DS3D_MINROLLOFFFACTOR",
    "DS3D_MAXROLLOFFFACTOR",
    "DS3D_DEFAULTROLLOFFFACTOR",
    "DS3D_MINDOPPLERFACTOR",
    "DS3D_MAXDOPPLERFACTOR",
    "DS3D_DEFAULTDOPPLERFACTOR",
    "DS3D_DEFAULTMINDISTANCE",
    "DS3D_DEFAULTMAXDISTANCE",
    "DS3D_MINCONEANGLE",
    "DS3D_MAXCONEANGLE",
    "DS3D_DEFAULTCONEANGLE",
    "DS3D_DEFAULTCONEOUTSIDEVOLUME",
    "DSCCAPS_EMULDRIVER",
    "DSCCAPS_CERTIFIED",
    "DSCCAPS_MULTIPLECAPTURE",
    "DSCBCAPS_WAVEMAPPED",
    "DSCBCAPS_CTRLFX",
    "DSCBLOCK_ENTIREBUFFER",
    "DSCBSTATUS_CAPTURING",
    "DSCBSTATUS_LOOPING",
    "DSCBSTART_LOOPING",
    "DSBPN_OFFSETSTOP",
    "DS_CERTIFIED",
    "DS_UNCERTIFIED",
    "DS3DALG_NO_VIRTUALIZATION",
    "DS3DALG_HRTF_FULL",
    "DS3DALG_HRTF_LIGHT",
    "GUID_DSFX_STANDARD_GARGLE",
    "GUID_DSFX_STANDARD_CHORUS",
    "GUID_DSFX_STANDARD_FLANGER",
    "GUID_DSFX_STANDARD_ECHO",
    "GUID_DSFX_STANDARD_DISTORTION",
    "GUID_DSFX_STANDARD_COMPRESSOR",
    "GUID_DSFX_STANDARD_PARAMEQ",
    "GUID_DSFX_STANDARD_I3DL2REVERB",
    "GUID_DSFX_WAVES_REVERB",
    "GUID_DSCFX_CLASS_AEC",
    "GUID_DSCFX_MS_AEC",
    "GUID_DSCFX_SYSTEM_AEC",
    "GUID_DSCFX_CLASS_NS",
    "GUID_DSCFX_MS_NS",
    "GUID_DSCFX_SYSTEM_NS",
    "DSFXR_PRESENT",
    "DSFXR_LOCHARDWARE",
    "DSFXR_LOCSOFTWARE",
    "DSFXR_UNALLOCATED",
    "DSFXR_FAILED",
    "DSFXR_UNKNOWN",
    "DSFXR_SENDLOOP",
    "DSFX_I3DL2_MATERIAL_PRESET_SINGLEWINDOW",
    "DSFX_I3DL2_MATERIAL_PRESET_DOUBLEWINDOW",
    "DSFX_I3DL2_MATERIAL_PRESET_THINDOOR",
    "DSFX_I3DL2_MATERIAL_PRESET_THICKDOOR",
    "DSFX_I3DL2_MATERIAL_PRESET_WOODWALL",
    "DSFX_I3DL2_MATERIAL_PRESET_BRICKWALL",
    "DSFX_I3DL2_MATERIAL_PRESET_STONEWALL",
    "DSFX_I3DL2_MATERIAL_PRESET_CURTAIN",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_DEFAULT",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_GENERIC",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PADDEDCELL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_ROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_BATHROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_LIVINGROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_STONEROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_AUDITORIUM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CONCERTHALL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CAVE",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_ARENA",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_HANGAR",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CARPETEDHALLWAY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_HALLWAY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_STONECORRIDOR",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_ALLEY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_FOREST",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CITY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_MOUNTAINS",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_QUARRY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PLAIN",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PARKINGLOT",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_SEWERPIPE",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_UNDERWATER",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_SMALLROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMHALL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEHALL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PLATE",
    "DSCAPS",
    "DSBCAPS",
    "DSEFFECTDESC",
    "DSCEFFECTDESC",
    "DSBUFFERDESC",
    "DSBUFFERDESC1",
    "DS3DBUFFER",
    "DS3DLISTENER",
    "DSCCAPS",
    "DSCBUFFERDESC1",
    "DSCBUFFERDESC",
    "DSCBCAPS",
    "DSBPOSITIONNOTIFY",
    "LPDSENUMCALLBACKA",
    "LPDSENUMCALLBACKW",
    "IDirectSound",
    "IDirectSound8",
    "IDirectSoundBuffer",
    "IDirectSoundBuffer8",
    "IDirectSound3DListener",
    "IDirectSound3DBuffer",
    "IDirectSoundCapture",
    "IDirectSoundCaptureBuffer",
    "IDirectSoundCaptureBuffer8",
    "IDirectSoundNotify",
    "DSFXGargle",
    "IDirectSoundFXGargle",
    "DSFXChorus",
    "IDirectSoundFXChorus",
    "DSFXFlanger",
    "IDirectSoundFXFlanger",
    "DSFXEcho",
    "IDirectSoundFXEcho",
    "DSFXDistortion",
    "IDirectSoundFXDistortion",
    "DSFXCompressor",
    "IDirectSoundFXCompressor",
    "DSFXParamEq",
    "IDirectSoundFXParamEq",
    "DSFXI3DL2Reverb",
    "IDirectSoundFXI3DL2Reverb",
    "DSFXWavesReverb",
    "IDirectSoundFXWavesReverb",
    "DSCFXAec",
    "IDirectSoundCaptureFXAec",
    "DSCFXNoiseSuppress",
    "IDirectSoundCaptureFXNoiseSuppress",
    "IDirectSoundFullDuplex",
    "DirectSoundCreate",
    "DirectSoundEnumerateA",
    "DirectSoundEnumerateW",
    "DirectSoundEnumerate",
    "DirectSoundCaptureCreate",
    "DirectSoundCaptureEnumerateA",
    "DirectSoundCaptureEnumerateW",
    "DirectSoundCaptureEnumerate",
    "DirectSoundCreate8",
    "DirectSoundCaptureCreate8",
    "DirectSoundFullDuplexCreate",
    "GetDeviceID",
]
