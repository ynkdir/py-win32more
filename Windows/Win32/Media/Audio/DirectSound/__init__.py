from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Audio.DirectSound
import Windows.Win32.System.Com
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
DIRECTSOUND_VERSION: UInt32 = 1792
_FACDS: UInt32 = 2168
CLSID_DirectSound: Guid = Guid('47d4d946-62e8-11cf-93-bc-44-45-53-54-00-00')
CLSID_DirectSound8: Guid = Guid('3901cc3f-84b5-4fa4-ba-35-aa-81-72-b8-a0-9b')
CLSID_DirectSoundCapture: Guid = Guid('b0210780-89cd-11d0-af-08-00-a0-c9-25-cd-16')
CLSID_DirectSoundCapture8: Guid = Guid('e4bcac13-7f99-4908-9a-8e-74-e3-bf-24-b6-e1')
CLSID_DirectSoundFullDuplex: Guid = Guid('fea4300c-7959-4147-b2-6a-23-77-b9-e7-a9-1d')
DSDEVID_DefaultPlayback: Guid = Guid('def00000-9c6d-47ed-aa-f1-4d-da-8f-2b-5c-03')
DSDEVID_DefaultCapture: Guid = Guid('def00001-9c6d-47ed-aa-f1-4d-da-8f-2b-5c-03')
DSDEVID_DefaultVoicePlayback: Guid = Guid('def00002-9c6d-47ed-aa-f1-4d-da-8f-2b-5c-03')
DSDEVID_DefaultVoiceCapture: Guid = Guid('def00003-9c6d-47ed-aa-f1-4d-da-8f-2b-5c-03')
DSFX_LOCHARDWARE: UInt32 = 1
DSFX_LOCSOFTWARE: UInt32 = 2
DSCFX_LOCHARDWARE: UInt32 = 1
DSCFX_LOCSOFTWARE: UInt32 = 2
DSCFXR_LOCHARDWARE: UInt32 = 16
DSCFXR_LOCSOFTWARE: UInt32 = 32
GUID_All_Objects: Guid = Guid('aa114de5-c262-4169-a1-c8-23-d6-98-cc-73-b5')
KSPROPERTY_SUPPORT_GET: UInt32 = 1
KSPROPERTY_SUPPORT_SET: UInt32 = 2
DSFXGARGLE_WAVE_TRIANGLE: UInt32 = 0
DSFXGARGLE_WAVE_SQUARE: UInt32 = 1
DSFXGARGLE_RATEHZ_MIN: UInt32 = 1
DSFXGARGLE_RATEHZ_MAX: UInt32 = 1000
DSFXCHORUS_WAVE_TRIANGLE: UInt32 = 0
DSFXCHORUS_WAVE_SIN: UInt32 = 1
DSFXCHORUS_WETDRYMIX_MIN: Single = 0
DSFXCHORUS_WETDRYMIX_MAX: Single = 100
DSFXCHORUS_DEPTH_MIN: Single = 0
DSFXCHORUS_DEPTH_MAX: Single = 100
DSFXCHORUS_FEEDBACK_MIN: Single = -99
DSFXCHORUS_FEEDBACK_MAX: Single = 99
DSFXCHORUS_FREQUENCY_MIN: Single = 0
DSFXCHORUS_FREQUENCY_MAX: Single = 10
DSFXCHORUS_DELAY_MIN: Single = 0
DSFXCHORUS_DELAY_MAX: Single = 20
DSFXCHORUS_PHASE_MIN: UInt32 = 0
DSFXCHORUS_PHASE_MAX: UInt32 = 4
DSFXCHORUS_PHASE_NEG_180: UInt32 = 0
DSFXCHORUS_PHASE_NEG_90: UInt32 = 1
DSFXCHORUS_PHASE_ZERO: UInt32 = 2
DSFXCHORUS_PHASE_90: UInt32 = 3
DSFXCHORUS_PHASE_180: UInt32 = 4
DSFXFLANGER_WAVE_TRIANGLE: UInt32 = 0
DSFXFLANGER_WAVE_SIN: UInt32 = 1
DSFXFLANGER_WETDRYMIX_MIN: Single = 0
DSFXFLANGER_WETDRYMIX_MAX: Single = 100
DSFXFLANGER_FREQUENCY_MIN: Single = 0
DSFXFLANGER_FREQUENCY_MAX: Single = 10
DSFXFLANGER_DEPTH_MIN: Single = 0
DSFXFLANGER_DEPTH_MAX: Single = 100
DSFXFLANGER_PHASE_MIN: UInt32 = 0
DSFXFLANGER_PHASE_MAX: UInt32 = 4
DSFXFLANGER_FEEDBACK_MIN: Single = -99
DSFXFLANGER_FEEDBACK_MAX: Single = 99
DSFXFLANGER_DELAY_MIN: Single = 0
DSFXFLANGER_DELAY_MAX: Single = 4
DSFXFLANGER_PHASE_NEG_180: UInt32 = 0
DSFXFLANGER_PHASE_NEG_90: UInt32 = 1
DSFXFLANGER_PHASE_ZERO: UInt32 = 2
DSFXFLANGER_PHASE_90: UInt32 = 3
DSFXFLANGER_PHASE_180: UInt32 = 4
DSFXECHO_WETDRYMIX_MIN: Single = 0
DSFXECHO_WETDRYMIX_MAX: Single = 100
DSFXECHO_FEEDBACK_MIN: Single = 0
DSFXECHO_FEEDBACK_MAX: Single = 100
DSFXECHO_LEFTDELAY_MIN: Single = 1
DSFXECHO_LEFTDELAY_MAX: Single = 2000
DSFXECHO_RIGHTDELAY_MIN: Single = 1
DSFXECHO_RIGHTDELAY_MAX: Single = 2000
DSFXECHO_PANDELAY_MIN: UInt32 = 0
DSFXECHO_PANDELAY_MAX: UInt32 = 1
DSFXDISTORTION_GAIN_MIN: Single = -60
DSFXDISTORTION_GAIN_MAX: Single = 0
DSFXDISTORTION_EDGE_MIN: Single = 0
DSFXDISTORTION_EDGE_MAX: Single = 100
DSFXDISTORTION_POSTEQCENTERFREQUENCY_MIN: Single = 100
DSFXDISTORTION_POSTEQCENTERFREQUENCY_MAX: Single = 8000
DSFXDISTORTION_POSTEQBANDWIDTH_MIN: Single = 100
DSFXDISTORTION_POSTEQBANDWIDTH_MAX: Single = 8000
DSFXDISTORTION_PRELOWPASSCUTOFF_MIN: Single = 100
DSFXDISTORTION_PRELOWPASSCUTOFF_MAX: Single = 8000
DSFXCOMPRESSOR_GAIN_MIN: Single = -60
DSFXCOMPRESSOR_GAIN_MAX: Single = 60
DSFXCOMPRESSOR_ATTACK_MIN: Single = 0.01
DSFXCOMPRESSOR_ATTACK_MAX: Single = 500
DSFXCOMPRESSOR_RELEASE_MIN: Single = 50
DSFXCOMPRESSOR_RELEASE_MAX: Single = 3000
DSFXCOMPRESSOR_THRESHOLD_MIN: Single = -60
DSFXCOMPRESSOR_THRESHOLD_MAX: Single = 0
DSFXCOMPRESSOR_RATIO_MIN: Single = 1
DSFXCOMPRESSOR_RATIO_MAX: Single = 100
DSFXCOMPRESSOR_PREDELAY_MIN: Single = 0
DSFXCOMPRESSOR_PREDELAY_MAX: Single = 4
DSFXPARAMEQ_CENTER_MIN: Single = 80
DSFXPARAMEQ_CENTER_MAX: Single = 16000
DSFXPARAMEQ_BANDWIDTH_MIN: Single = 1
DSFXPARAMEQ_BANDWIDTH_MAX: Single = 36
DSFXPARAMEQ_GAIN_MIN: Single = -15
DSFXPARAMEQ_GAIN_MAX: Single = 15
DSFX_I3DL2REVERB_ROOM_MIN: Int32 = -10000
DSFX_I3DL2REVERB_ROOM_MAX: UInt32 = 0
DSFX_I3DL2REVERB_ROOM_DEFAULT: Int32 = -1000
DSFX_I3DL2REVERB_ROOMHF_MIN: Int32 = -10000
DSFX_I3DL2REVERB_ROOMHF_MAX: UInt32 = 0
DSFX_I3DL2REVERB_ROOMHF_DEFAULT: Int32 = -100
DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MIN: Single = 0
DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MAX: Single = 10
DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_DEFAULT: Single = 0
DSFX_I3DL2REVERB_DECAYTIME_MIN: Single = 0.1
DSFX_I3DL2REVERB_DECAYTIME_MAX: Single = 20
DSFX_I3DL2REVERB_DECAYTIME_DEFAULT: Single = 1.49
DSFX_I3DL2REVERB_DECAYHFRATIO_MIN: Single = 0.1
DSFX_I3DL2REVERB_DECAYHFRATIO_MAX: Single = 2
DSFX_I3DL2REVERB_DECAYHFRATIO_DEFAULT: Single = 0.83
DSFX_I3DL2REVERB_REFLECTIONS_MIN: Int32 = -10000
DSFX_I3DL2REVERB_REFLECTIONS_MAX: UInt32 = 1000
DSFX_I3DL2REVERB_REFLECTIONS_DEFAULT: Int32 = -2602
DSFX_I3DL2REVERB_REFLECTIONSDELAY_MIN: Single = 0
DSFX_I3DL2REVERB_REFLECTIONSDELAY_MAX: Single = 0.3
DSFX_I3DL2REVERB_REFLECTIONSDELAY_DEFAULT: Single = 0.007
DSFX_I3DL2REVERB_REVERB_MIN: Int32 = -10000
DSFX_I3DL2REVERB_REVERB_MAX: UInt32 = 2000
DSFX_I3DL2REVERB_REVERB_DEFAULT: UInt32 = 200
DSFX_I3DL2REVERB_REVERBDELAY_MIN: Single = 0
DSFX_I3DL2REVERB_REVERBDELAY_MAX: Single = 0.1
DSFX_I3DL2REVERB_REVERBDELAY_DEFAULT: Single = 0.011
DSFX_I3DL2REVERB_DIFFUSION_MIN: Single = 0
DSFX_I3DL2REVERB_DIFFUSION_MAX: Single = 100
DSFX_I3DL2REVERB_DIFFUSION_DEFAULT: Single = 100
DSFX_I3DL2REVERB_DENSITY_MIN: Single = 0
DSFX_I3DL2REVERB_DENSITY_MAX: Single = 100
DSFX_I3DL2REVERB_DENSITY_DEFAULT: Single = 100
DSFX_I3DL2REVERB_HFREFERENCE_MIN: Single = 20
DSFX_I3DL2REVERB_HFREFERENCE_MAX: Single = 20000
DSFX_I3DL2REVERB_HFREFERENCE_DEFAULT: Single = 5000
DSFX_I3DL2REVERB_QUALITY_MIN: UInt32 = 0
DSFX_I3DL2REVERB_QUALITY_MAX: UInt32 = 3
DSFX_I3DL2REVERB_QUALITY_DEFAULT: UInt32 = 2
DSFX_WAVESREVERB_INGAIN_MIN: Single = -96
DSFX_WAVESREVERB_INGAIN_MAX: Single = 0
DSFX_WAVESREVERB_INGAIN_DEFAULT: Single = 0
DSFX_WAVESREVERB_REVERBMIX_MIN: Single = -96
DSFX_WAVESREVERB_REVERBMIX_MAX: Single = 0
DSFX_WAVESREVERB_REVERBMIX_DEFAULT: Single = 0
DSFX_WAVESREVERB_REVERBTIME_MIN: Single = 0.001
DSFX_WAVESREVERB_REVERBTIME_MAX: Single = 3000
DSFX_WAVESREVERB_REVERBTIME_DEFAULT: Single = 1000
DSFX_WAVESREVERB_HIGHFREQRTRATIO_MIN: Single = 0.001
DSFX_WAVESREVERB_HIGHFREQRTRATIO_MAX: Single = 0.999
DSFX_WAVESREVERB_HIGHFREQRTRATIO_DEFAULT: Single = 0.001
DSCFX_AEC_MODE_PASS_THROUGH: UInt32 = 0
DSCFX_AEC_MODE_HALF_DUPLEX: UInt32 = 1
DSCFX_AEC_MODE_FULL_DUPLEX: UInt32 = 2
DSCFX_AEC_STATUS_HISTORY_UNINITIALIZED: UInt32 = 0
DSCFX_AEC_STATUS_HISTORY_CONTINUOUSLY_CONVERGED: UInt32 = 1
DSCFX_AEC_STATUS_HISTORY_PREVIOUSLY_DIVERGED: UInt32 = 2
DSCFX_AEC_STATUS_CURRENTLY_CONVERGED: UInt32 = 8
DS_NO_VIRTUALIZATION: Windows.Win32.Foundation.HRESULT = 142082058
DSCAPS_PRIMARYMONO: UInt32 = 1
DSCAPS_PRIMARYSTEREO: UInt32 = 2
DSCAPS_PRIMARY8BIT: UInt32 = 4
DSCAPS_PRIMARY16BIT: UInt32 = 8
DSCAPS_CONTINUOUSRATE: UInt32 = 16
DSCAPS_EMULDRIVER: UInt32 = 32
DSCAPS_CERTIFIED: UInt32 = 64
DSCAPS_SECONDARYMONO: UInt32 = 256
DSCAPS_SECONDARYSTEREO: UInt32 = 512
DSCAPS_SECONDARY8BIT: UInt32 = 1024
DSCAPS_SECONDARY16BIT: UInt32 = 2048
DSSCL_NORMAL: UInt32 = 1
DSSCL_PRIORITY: UInt32 = 2
DSSCL_EXCLUSIVE: UInt32 = 3
DSSCL_WRITEPRIMARY: UInt32 = 4
DSSPEAKER_DIRECTOUT: UInt32 = 0
DSSPEAKER_HEADPHONE: UInt32 = 1
DSSPEAKER_MONO: UInt32 = 2
DSSPEAKER_QUAD: UInt32 = 3
DSSPEAKER_STEREO: UInt32 = 4
DSSPEAKER_SURROUND: UInt32 = 5
DSSPEAKER_5POINT1: UInt32 = 6
DSSPEAKER_7POINT1: UInt32 = 7
DSSPEAKER_7POINT1_SURROUND: UInt32 = 8
DSSPEAKER_5POINT1_SURROUND: UInt32 = 9
DSSPEAKER_7POINT1_WIDE: UInt32 = 7
DSSPEAKER_5POINT1_BACK: UInt32 = 6
DSSPEAKER_GEOMETRY_MIN: UInt32 = 5
DSSPEAKER_GEOMETRY_NARROW: UInt32 = 10
DSSPEAKER_GEOMETRY_WIDE: UInt32 = 20
DSSPEAKER_GEOMETRY_MAX: UInt32 = 180
DSBCAPS_PRIMARYBUFFER: UInt32 = 1
DSBCAPS_STATIC: UInt32 = 2
DSBCAPS_LOCHARDWARE: UInt32 = 4
DSBCAPS_LOCSOFTWARE: UInt32 = 8
DSBCAPS_CTRL3D: UInt32 = 16
DSBCAPS_CTRLFREQUENCY: UInt32 = 32
DSBCAPS_CTRLPAN: UInt32 = 64
DSBCAPS_CTRLVOLUME: UInt32 = 128
DSBCAPS_CTRLPOSITIONNOTIFY: UInt32 = 256
DSBCAPS_CTRLFX: UInt32 = 512
DSBCAPS_STICKYFOCUS: UInt32 = 16384
DSBCAPS_GLOBALFOCUS: UInt32 = 32768
DSBCAPS_GETCURRENTPOSITION2: UInt32 = 65536
DSBCAPS_MUTE3DATMAXDISTANCE: UInt32 = 131072
DSBCAPS_LOCDEFER: UInt32 = 262144
DSBCAPS_TRUEPLAYPOSITION: UInt32 = 524288
DSBPLAY_LOOPING: UInt32 = 1
DSBPLAY_LOCHARDWARE: UInt32 = 2
DSBPLAY_LOCSOFTWARE: UInt32 = 4
DSBPLAY_TERMINATEBY_TIME: UInt32 = 8
DSBPLAY_TERMINATEBY_DISTANCE: UInt64 = 16
DSBPLAY_TERMINATEBY_PRIORITY: UInt64 = 32
DSBSTATUS_PLAYING: UInt32 = 1
DSBSTATUS_BUFFERLOST: UInt32 = 2
DSBSTATUS_LOOPING: UInt32 = 4
DSBSTATUS_LOCHARDWARE: UInt32 = 8
DSBSTATUS_LOCSOFTWARE: UInt32 = 16
DSBSTATUS_TERMINATED: UInt32 = 32
DSBLOCK_FROMWRITECURSOR: UInt32 = 1
DSBLOCK_ENTIREBUFFER: UInt32 = 2
DSBFREQUENCY_ORIGINAL: UInt32 = 0
DSBFREQUENCY_MIN: UInt32 = 100
DSBFREQUENCY_MAX: UInt32 = 200000
DSBPAN_LEFT: Int32 = -10000
DSBPAN_CENTER: UInt32 = 0
DSBPAN_RIGHT: UInt32 = 10000
DSBVOLUME_MIN: Int32 = -10000
DSBVOLUME_MAX: UInt32 = 0
DSBSIZE_MIN: UInt32 = 4
DSBSIZE_MAX: UInt32 = 268435455
DSBSIZE_FX_MIN: UInt32 = 150
DSBNOTIFICATIONS_MAX: UInt32 = 100000
DS3DMODE_NORMAL: UInt32 = 0
DS3DMODE_HEADRELATIVE: UInt32 = 1
DS3DMODE_DISABLE: UInt32 = 2
DS3D_IMMEDIATE: UInt32 = 0
DS3D_DEFERRED: UInt32 = 1
DS3D_DEFAULTDISTANCEFACTOR: Single = 1
DS3D_MINROLLOFFFACTOR: Single = 0
DS3D_MAXROLLOFFFACTOR: Single = 10
DS3D_DEFAULTROLLOFFFACTOR: Single = 1
DS3D_MINDOPPLERFACTOR: Single = 0
DS3D_MAXDOPPLERFACTOR: Single = 10
DS3D_DEFAULTDOPPLERFACTOR: Single = 1
DS3D_DEFAULTMINDISTANCE: Single = 1
DS3D_DEFAULTMAXDISTANCE: Single = 1000000000.0
DS3D_MINCONEANGLE: UInt32 = 0
DS3D_MAXCONEANGLE: UInt32 = 360
DS3D_DEFAULTCONEANGLE: UInt32 = 360
DS3D_DEFAULTCONEOUTSIDEVOLUME: UInt32 = 0
DSCCAPS_EMULDRIVER: UInt32 = 32
DSCCAPS_CERTIFIED: UInt32 = 64
DSCCAPS_MULTIPLECAPTURE: UInt32 = 1
DSCBCAPS_WAVEMAPPED: UInt32 = 2147483648
DSCBCAPS_CTRLFX: UInt32 = 512
DSCBLOCK_ENTIREBUFFER: UInt32 = 1
DSCBSTATUS_CAPTURING: UInt32 = 1
DSCBSTATUS_LOOPING: UInt32 = 2
DSCBSTART_LOOPING: UInt32 = 1
DSBPN_OFFSETSTOP: UInt32 = 4294967295
DS_CERTIFIED: UInt32 = 0
DS_UNCERTIFIED: UInt32 = 1
DS3DALG_NO_VIRTUALIZATION: Guid = Guid('c241333f-1c1b-11d2-94-f5-00-c0-4f-c2-8a-ca')
DS3DALG_HRTF_FULL: Guid = Guid('c2413340-1c1b-11d2-94-f5-00-c0-4f-c2-8a-ca')
DS3DALG_HRTF_LIGHT: Guid = Guid('c2413342-1c1b-11d2-94-f5-00-c0-4f-c2-8a-ca')
GUID_DSFX_STANDARD_GARGLE: Guid = Guid('dafd8210-5711-4b91-9f-e3-f7-5b-7a-e2-79-bf')
GUID_DSFX_STANDARD_CHORUS: Guid = Guid('efe6629c-81f7-4281-bd-91-c9-d6-04-a9-5a-f6')
GUID_DSFX_STANDARD_FLANGER: Guid = Guid('efca3d92-dfd8-4672-a6-03-74-20-89-4b-ad-98')
GUID_DSFX_STANDARD_ECHO: Guid = Guid('ef3e932c-d40b-4f51-8c-cf-3f-98-f1-b2-9d-5d')
GUID_DSFX_STANDARD_DISTORTION: Guid = Guid('ef114c90-cd1d-484e-96-e5-09-cf-af-91-2a-21')
GUID_DSFX_STANDARD_COMPRESSOR: Guid = Guid('ef011f79-4000-406d-87-af-bf-fb-3f-c3-9d-57')
GUID_DSFX_STANDARD_PARAMEQ: Guid = Guid('120ced89-3bf4-4173-a1-32-3c-b4-06-cf-32-31')
GUID_DSFX_STANDARD_I3DL2REVERB: Guid = Guid('ef985e71-d5c7-42d4-ba-4d-2d-07-3e-2e-96-f4')
GUID_DSFX_WAVES_REVERB: Guid = Guid('87fc0268-9a55-4360-95-aa-00-4a-1d-9d-e2-6c')
GUID_DSCFX_CLASS_AEC: Guid = Guid('bf963d80-c559-11d0-8a-2b-00-a0-c9-25-5a-c1')
GUID_DSCFX_MS_AEC: Guid = Guid('cdebb919-379a-488a-87-65-f5-3c-fd-36-de-40')
GUID_DSCFX_SYSTEM_AEC: Guid = Guid('1c22c56d-9879-4f5b-a3-89-27-99-6d-dc-28-10')
GUID_DSCFX_CLASS_NS: Guid = Guid('e07f903f-62fd-4e60-8c-dd-de-a7-23-66-65-b5')
GUID_DSCFX_MS_NS: Guid = Guid('11c5c73b-66e9-4ba1-a0-ba-e8-14-c6-ee-d9-2d')
GUID_DSCFX_SYSTEM_NS: Guid = Guid('5ab0882e-7274-4516-87-7d-4e-ee-99-ba-4f-d0')
DSFXR_PRESENT: Int32 = 0
DSFXR_LOCHARDWARE: Int32 = 1
DSFXR_LOCSOFTWARE: Int32 = 2
DSFXR_UNALLOCATED: Int32 = 3
DSFXR_FAILED: Int32 = 4
DSFXR_UNKNOWN: Int32 = 5
DSFXR_SENDLOOP: Int32 = 6
DSFX_I3DL2_MATERIAL_PRESET_SINGLEWINDOW: Int32 = 0
DSFX_I3DL2_MATERIAL_PRESET_DOUBLEWINDOW: Int32 = 1
DSFX_I3DL2_MATERIAL_PRESET_THINDOOR: Int32 = 2
DSFX_I3DL2_MATERIAL_PRESET_THICKDOOR: Int32 = 3
DSFX_I3DL2_MATERIAL_PRESET_WOODWALL: Int32 = 4
DSFX_I3DL2_MATERIAL_PRESET_BRICKWALL: Int32 = 5
DSFX_I3DL2_MATERIAL_PRESET_STONEWALL: Int32 = 6
DSFX_I3DL2_MATERIAL_PRESET_CURTAIN: Int32 = 7
DSFX_I3DL2_ENVIRONMENT_PRESET_DEFAULT: Int32 = 0
DSFX_I3DL2_ENVIRONMENT_PRESET_GENERIC: Int32 = 1
DSFX_I3DL2_ENVIRONMENT_PRESET_PADDEDCELL: Int32 = 2
DSFX_I3DL2_ENVIRONMENT_PRESET_ROOM: Int32 = 3
DSFX_I3DL2_ENVIRONMENT_PRESET_BATHROOM: Int32 = 4
DSFX_I3DL2_ENVIRONMENT_PRESET_LIVINGROOM: Int32 = 5
DSFX_I3DL2_ENVIRONMENT_PRESET_STONEROOM: Int32 = 6
DSFX_I3DL2_ENVIRONMENT_PRESET_AUDITORIUM: Int32 = 7
DSFX_I3DL2_ENVIRONMENT_PRESET_CONCERTHALL: Int32 = 8
DSFX_I3DL2_ENVIRONMENT_PRESET_CAVE: Int32 = 9
DSFX_I3DL2_ENVIRONMENT_PRESET_ARENA: Int32 = 10
DSFX_I3DL2_ENVIRONMENT_PRESET_HANGAR: Int32 = 11
DSFX_I3DL2_ENVIRONMENT_PRESET_CARPETEDHALLWAY: Int32 = 12
DSFX_I3DL2_ENVIRONMENT_PRESET_HALLWAY: Int32 = 13
DSFX_I3DL2_ENVIRONMENT_PRESET_STONECORRIDOR: Int32 = 14
DSFX_I3DL2_ENVIRONMENT_PRESET_ALLEY: Int32 = 15
DSFX_I3DL2_ENVIRONMENT_PRESET_FOREST: Int32 = 16
DSFX_I3DL2_ENVIRONMENT_PRESET_CITY: Int32 = 17
DSFX_I3DL2_ENVIRONMENT_PRESET_MOUNTAINS: Int32 = 18
DSFX_I3DL2_ENVIRONMENT_PRESET_QUARRY: Int32 = 19
DSFX_I3DL2_ENVIRONMENT_PRESET_PLAIN: Int32 = 20
DSFX_I3DL2_ENVIRONMENT_PRESET_PARKINGLOT: Int32 = 21
DSFX_I3DL2_ENVIRONMENT_PRESET_SEWERPIPE: Int32 = 22
DSFX_I3DL2_ENVIRONMENT_PRESET_UNDERWATER: Int32 = 23
DSFX_I3DL2_ENVIRONMENT_PRESET_SMALLROOM: Int32 = 24
DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMROOM: Int32 = 25
DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEROOM: Int32 = 26
DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMHALL: Int32 = 27
DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEHALL: Int32 = 28
DSFX_I3DL2_ENVIRONMENT_PRESET_PLATE: Int32 = 29
@winfunctype('DSOUND.dll')
def DirectSoundCreate(pcGuidDevice: POINTER(Guid), ppDS: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSound_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundEnumerateA(pDSEnumCallback: Windows.Win32.Media.Audio.DirectSound.LPDSENUMCALLBACKA, pContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundEnumerateW(pDSEnumCallback: Windows.Win32.Media.Audio.DirectSound.LPDSENUMCALLBACKW, pContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundCaptureCreate(pcGuidDevice: POINTER(Guid), ppDSC: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundCapture_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundCaptureEnumerateA(pDSEnumCallback: Windows.Win32.Media.Audio.DirectSound.LPDSENUMCALLBACKA, pContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundCaptureEnumerateW(pDSEnumCallback: Windows.Win32.Media.Audio.DirectSound.LPDSENUMCALLBACKW, pContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundCreate8(pcGuidDevice: POINTER(Guid), ppDS8: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSound8_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundCaptureCreate8(pcGuidDevice: POINTER(Guid), ppDSC8: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundCapture_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def DirectSoundFullDuplexCreate(pcGuidCaptureDevice: POINTER(Guid), pcGuidRenderDevice: POINTER(Guid), pcDSCBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCBUFFERDESC_head), pcDSBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSBUFFERDESC_head), hWnd: Windows.Win32.Foundation.HWND, dwLevel: UInt32, ppDSFD: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundFullDuplex_head), ppDSCBuffer8: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundCaptureBuffer8_head), ppDSBuffer8: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer8_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSOUND.dll')
def GetDeviceID(pGuidSrc: POINTER(Guid), pGuidDest: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class DS3DBUFFER(Structure):
    dwSize: UInt32
    vPosition: Windows.Win32.Graphics.Direct3D.D3DVECTOR
    vVelocity: Windows.Win32.Graphics.Direct3D.D3DVECTOR
    dwInsideConeAngle: UInt32
    dwOutsideConeAngle: UInt32
    vConeOrientation: Windows.Win32.Graphics.Direct3D.D3DVECTOR
    lConeOutsideVolume: Int32
    flMinDistance: Single
    flMaxDistance: Single
    dwMode: UInt32
class DS3DLISTENER(Structure):
    dwSize: UInt32
    vPosition: Windows.Win32.Graphics.Direct3D.D3DVECTOR
    vVelocity: Windows.Win32.Graphics.Direct3D.D3DVECTOR
    vOrientFront: Windows.Win32.Graphics.Direct3D.D3DVECTOR
    vOrientTop: Windows.Win32.Graphics.Direct3D.D3DVECTOR
    flDistanceFactor: Single
    flRolloffFactor: Single
    flDopplerFactor: Single
class DSBCAPS(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwBufferBytes: UInt32
    dwUnlockTransferRate: UInt32
    dwPlayCpuOverhead: UInt32
class DSBPOSITIONNOTIFY(Structure):
    dwOffset: UInt32
    hEventNotify: Windows.Win32.Foundation.HANDLE
class DSBUFFERDESC(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwBufferBytes: UInt32
    dwReserved: UInt32
    lpwfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    guid3DAlgorithm: Guid
class DSBUFFERDESC1(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwBufferBytes: UInt32
    dwReserved: UInt32
    lpwfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
class DSCAPS(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwMinSecondarySampleRate: UInt32
    dwMaxSecondarySampleRate: UInt32
    dwPrimaryBuffers: UInt32
    dwMaxHwMixingAllBuffers: UInt32
    dwMaxHwMixingStaticBuffers: UInt32
    dwMaxHwMixingStreamingBuffers: UInt32
    dwFreeHwMixingAllBuffers: UInt32
    dwFreeHwMixingStaticBuffers: UInt32
    dwFreeHwMixingStreamingBuffers: UInt32
    dwMaxHw3DAllBuffers: UInt32
    dwMaxHw3DStaticBuffers: UInt32
    dwMaxHw3DStreamingBuffers: UInt32
    dwFreeHw3DAllBuffers: UInt32
    dwFreeHw3DStaticBuffers: UInt32
    dwFreeHw3DStreamingBuffers: UInt32
    dwTotalHwMemBytes: UInt32
    dwFreeHwMemBytes: UInt32
    dwMaxContigFreeHwMemBytes: UInt32
    dwUnlockTransferRateHwBuffers: UInt32
    dwPlayCpuOverheadSwBuffers: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
class DSCBCAPS(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwBufferBytes: UInt32
    dwReserved: UInt32
class DSCBUFFERDESC(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwBufferBytes: UInt32
    dwReserved: UInt32
    lpwfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    dwFXCount: UInt32
    lpDSCFXDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCEFFECTDESC_head)
class DSCBUFFERDESC1(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwBufferBytes: UInt32
    dwReserved: UInt32
    lpwfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
class DSCCAPS(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwFormats: UInt32
    dwChannels: UInt32
class DSCEFFECTDESC(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    guidDSCFXClass: Guid
    guidDSCFXInstance: Guid
    dwReserved1: UInt32
    dwReserved2: UInt32
class DSCFXAec(Structure):
    fEnable: Windows.Win32.Foundation.BOOL
    fNoiseFill: Windows.Win32.Foundation.BOOL
    dwMode: UInt32
class DSCFXNoiseSuppress(Structure):
    fEnable: Windows.Win32.Foundation.BOOL
class DSEFFECTDESC(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    guidDSFXClass: Guid
    dwReserved1: UIntPtr
    dwReserved2: UIntPtr
class DSFXChorus(Structure):
    fWetDryMix: Single
    fDepth: Single
    fFeedback: Single
    fFrequency: Single
    lWaveform: Int32
    fDelay: Single
    lPhase: Int32
class DSFXCompressor(Structure):
    fGain: Single
    fAttack: Single
    fRelease: Single
    fThreshold: Single
    fRatio: Single
    fPredelay: Single
class DSFXDistortion(Structure):
    fGain: Single
    fEdge: Single
    fPostEQCenterFrequency: Single
    fPostEQBandwidth: Single
    fPreLowpassCutoff: Single
class DSFXEcho(Structure):
    fWetDryMix: Single
    fFeedback: Single
    fLeftDelay: Single
    fRightDelay: Single
    lPanDelay: Int32
class DSFXFlanger(Structure):
    fWetDryMix: Single
    fDepth: Single
    fFeedback: Single
    fFrequency: Single
    lWaveform: Int32
    fDelay: Single
    lPhase: Int32
class DSFXGargle(Structure):
    dwRateHz: UInt32
    dwWaveShape: UInt32
class DSFXI3DL2Reverb(Structure):
    lRoom: Int32
    lRoomHF: Int32
    flRoomRolloffFactor: Single
    flDecayTime: Single
    flDecayHFRatio: Single
    lReflections: Int32
    flReflectionsDelay: Single
    lReverb: Int32
    flReverbDelay: Single
    flDiffusion: Single
    flDensity: Single
    flHFReference: Single
class DSFXParamEq(Structure):
    fCenter: Single
    fBandwidth: Single
    fGain: Single
class DSFXWavesReverb(Structure):
    fInGain: Single
    fReverbMix: Single
    fReverbTime: Single
    fHighFreqRTRatio: Single
class IDirectSound(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('279afa83-4981-11ce-a5-21-00-20-af-0b-e5-60')
    @commethod(3)
    def CreateSoundBuffer(pcDSBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSBUFFERDESC_head), ppDSBuffer: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCaps(pDSCaps: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DuplicateSoundBuffer(pDSBufferOriginal: Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer_head, ppDSBufferDuplicate: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetCooperativeLevel(hwnd: Windows.Win32.Foundation.HWND, dwLevel: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Compact() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSpeakerConfig(pdwSpeakerConfig: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSpeakerConfig(dwSpeakerConfig: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Initialize(pcGuidDevice: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSound3DBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('279afa86-4981-11ce-a5-21-00-20-af-0b-e5-60')
    @commethod(3)
    def GetAllParameters(pDs3dBuffer: POINTER(Windows.Win32.Media.Audio.DirectSound.DS3DBUFFER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConeAngles(pdwInsideConeAngle: POINTER(UInt32), pdwOutsideConeAngle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetConeOrientation(pvOrientation: POINTER(Windows.Win32.Graphics.Direct3D.D3DVECTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetConeOutsideVolume(plConeOutsideVolume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxDistance(pflMaxDistance: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMinDistance(pflMinDistance: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMode(pdwMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPosition(pvPosition: POINTER(Windows.Win32.Graphics.Direct3D.D3DVECTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetVelocity(pvVelocity: POINTER(Windows.Win32.Graphics.Direct3D.D3DVECTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetAllParameters(pcDs3dBuffer: POINTER(Windows.Win32.Media.Audio.DirectSound.DS3DBUFFER_head), dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetConeAngles(dwInsideConeAngle: UInt32, dwOutsideConeAngle: UInt32, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetConeOrientation(x: Single, y: Single, z: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetConeOutsideVolume(lConeOutsideVolume: Int32, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetMaxDistance(flMaxDistance: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetMinDistance(flMinDistance: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetMode(dwMode: UInt32, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetPosition(x: Single, y: Single, z: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetVelocity(x: Single, y: Single, z: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSound3DListener(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('279afa84-4981-11ce-a5-21-00-20-af-0b-e5-60')
    @commethod(3)
    def GetAllParameters(pListener: POINTER(Windows.Win32.Media.Audio.DirectSound.DS3DLISTENER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDistanceFactor(pflDistanceFactor: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDopplerFactor(pflDopplerFactor: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOrientation(pvOrientFront: POINTER(Windows.Win32.Graphics.Direct3D.D3DVECTOR_head), pvOrientTop: POINTER(Windows.Win32.Graphics.Direct3D.D3DVECTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPosition(pvPosition: POINTER(Windows.Win32.Graphics.Direct3D.D3DVECTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRolloffFactor(pflRolloffFactor: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetVelocity(pvVelocity: POINTER(Windows.Win32.Graphics.Direct3D.D3DVECTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetAllParameters(pcListener: POINTER(Windows.Win32.Media.Audio.DirectSound.DS3DLISTENER_head), dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDistanceFactor(flDistanceFactor: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDopplerFactor(flDopplerFactor: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetOrientation(xFront: Single, yFront: Single, zFront: Single, xTop: Single, yTop: Single, zTop: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetPosition(x: Single, y: Single, z: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetRolloffFactor(flRolloffFactor: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetVelocity(x: Single, y: Single, z: Single, dwApply: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CommitDeferredSettings() -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSound8(c_void_p):
    extends: Windows.Win32.Media.Audio.DirectSound.IDirectSound
    Guid = Guid('c50a7e93-f395-4834-9e-f6-7f-a9-9d-e5-09-66')
    @commethod(11)
    def VerifyCertification(pdwCertified: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('279afa85-4981-11ce-a5-21-00-20-af-0b-e5-60')
    @commethod(3)
    def GetCaps(pDSBufferCaps: POINTER(Windows.Win32.Media.Audio.DirectSound.DSBCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentPosition(pdwCurrentPlayCursor: POINTER(UInt32), pdwCurrentWriteCursor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormat(pwfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), dwSizeAllocated: UInt32, pdwSizeWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVolume(plVolume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPan(plPan: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFrequency(pdwFrequency: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStatus(pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Initialize(pDirectSound: Windows.Win32.Media.Audio.DirectSound.IDirectSound_head, pcDSBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSBUFFERDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Lock(dwOffset: UInt32, dwBytes: UInt32, ppvAudioPtr1: POINTER(c_void_p), pdwAudioBytes1: POINTER(UInt32), ppvAudioPtr2: POINTER(c_void_p), pdwAudioBytes2: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Play(dwReserved1: UInt32, dwPriority: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetCurrentPosition(dwNewPosition: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetFormat(pcfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetVolume(lVolume: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetPan(lPan: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetFrequency(dwFrequency: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Unlock(pvAudioPtr1: c_void_p, dwAudioBytes1: UInt32, pvAudioPtr2: c_void_p, dwAudioBytes2: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Restore() -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundBuffer8(c_void_p):
    extends: Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer
    Guid = Guid('6825a449-7524-4d82-92-0f-50-e3-6a-b3-ab-1e')
    @commethod(21)
    def SetFX(dwEffectsCount: UInt32, pDSFXDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSEFFECTDESC_head), pdwResultCodes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AcquireResources(dwFlags: UInt32, dwEffectsCount: UInt32, pdwResultCodes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetObjectInPath(rguidObject: POINTER(Guid), dwIndex: UInt32, rguidInterface: POINTER(Guid), ppObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundCapture(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b0210781-89cd-11d0-af-08-00-a0-c9-25-cd-16')
    @commethod(3)
    def CreateCaptureBuffer(pcDSCBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCBUFFERDESC_head), ppDSCBuffer: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundCaptureBuffer_head), pUnkOuter: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCaps(pDSCCaps: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Initialize(pcGuidDevice: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundCaptureBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b0210782-89cd-11d0-af-08-00-a0-c9-25-cd-16')
    @commethod(3)
    def GetCaps(pDSCBCaps: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCBCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentPosition(pdwCapturePosition: POINTER(UInt32), pdwReadPosition: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormat(pwfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), dwSizeAllocated: UInt32, pdwSizeWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Initialize(pDirectSoundCapture: Windows.Win32.Media.Audio.DirectSound.IDirectSoundCapture_head, pcDSCBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCBUFFERDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Lock(dwOffset: UInt32, dwBytes: UInt32, ppvAudioPtr1: POINTER(c_void_p), pdwAudioBytes1: POINTER(UInt32), ppvAudioPtr2: POINTER(c_void_p), pdwAudioBytes2: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Start(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Unlock(pvAudioPtr1: c_void_p, dwAudioBytes1: UInt32, pvAudioPtr2: c_void_p, dwAudioBytes2: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundCaptureBuffer8(c_void_p):
    extends: Windows.Win32.Media.Audio.DirectSound.IDirectSoundCaptureBuffer
    Guid = Guid('00990df4-0dbb-4872-83-3e-6d-30-3e-80-ae-b6')
    @commethod(12)
    def GetObjectInPath(rguidObject: POINTER(Guid), dwIndex: UInt32, rguidInterface: POINTER(Guid), ppObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFXStatus(dwEffectsCount: UInt32, pdwFXStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundCaptureFXAec(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ad74143d-903d-4ab7-80-66-28-d3-63-03-6d-65')
    @commethod(3)
    def SetAllParameters(pDscFxAec: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCFXAec_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDscFxAec: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCFXAec_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundCaptureFXNoiseSuppress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ed311e41-fbae-4175-96-25-cd-08-54-f6-93-ca')
    @commethod(3)
    def SetAllParameters(pcDscFxNoiseSuppress: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCFXNoiseSuppress_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDscFxNoiseSuppress: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCFXNoiseSuppress_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXChorus(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('880842e3-145f-43e6-a9-34-a7-18-06-e5-05-47')
    @commethod(3)
    def SetAllParameters(pcDsFxChorus: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXChorus_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxChorus: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXChorus_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXCompressor(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4bbd1154-62f6-4e2c-a1-5c-d3-b6-c4-17-f7-a0')
    @commethod(3)
    def SetAllParameters(pcDsFxCompressor: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXCompressor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxCompressor: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXCompressor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXDistortion(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8ecf4326-455f-4d8b-bd-a9-8d-5d-3e-9e-3e-0b')
    @commethod(3)
    def SetAllParameters(pcDsFxDistortion: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXDistortion_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxDistortion: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXDistortion_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXEcho(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8bd28edf-50db-4e92-a2-bd-44-54-88-d1-ed-42')
    @commethod(3)
    def SetAllParameters(pcDsFxEcho: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXEcho_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxEcho: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXEcho_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXFlanger(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('903e9878-2c92-4072-9b-2c-ea-68-f5-39-67-83')
    @commethod(3)
    def SetAllParameters(pcDsFxFlanger: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXFlanger_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxFlanger: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXFlanger_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXGargle(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d616f352-d622-11ce-aa-c5-00-20-af-0b-99-a3')
    @commethod(3)
    def SetAllParameters(pcDsFxGargle: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXGargle_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxGargle: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXGargle_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXI3DL2Reverb(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4b166a6a-0d66-43f3-80-e3-ee-62-80-de-e1-a4')
    @commethod(3)
    def SetAllParameters(pcDsFxI3DL2Reverb: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXI3DL2Reverb_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxI3DL2Reverb: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXI3DL2Reverb_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPreset(dwPreset: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPreset(pdwPreset: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetQuality(lQuality: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuality(plQuality: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXParamEq(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c03ca9fe-fe90-4204-80-78-82-33-4c-d1-77-da')
    @commethod(3)
    def SetAllParameters(pcDsFxParamEq: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXParamEq_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxParamEq: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXParamEq_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFXWavesReverb(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('46858c3a-0dc6-45e3-b7-60-d4-ee-f1-6c-b3-25')
    @commethod(3)
    def SetAllParameters(pcDsFxWavesReverb: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXWavesReverb_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllParameters(pDsFxWavesReverb: POINTER(Windows.Win32.Media.Audio.DirectSound.DSFXWavesReverb_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundFullDuplex(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('edcb4c7a-daab-4216-a4-2e-6c-50-59-6d-dc-1d')
    @commethod(3)
    def Initialize(pCaptureGuid: POINTER(Guid), pRenderGuid: POINTER(Guid), lpDscBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSCBUFFERDESC_head), lpDsBufferDesc: POINTER(Windows.Win32.Media.Audio.DirectSound.DSBUFFERDESC_head), hWnd: Windows.Win32.Foundation.HWND, dwLevel: UInt32, lplpDirectSoundCaptureBuffer8: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundCaptureBuffer8_head), lplpDirectSoundBuffer8: POINTER(Windows.Win32.Media.Audio.DirectSound.IDirectSoundBuffer8_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectSoundNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b0210783-89cd-11d0-af-08-00-a0-c9-25-cd-16')
    @commethod(3)
    def SetNotificationPositions(dwPositionNotifies: UInt32, pcPositionNotifies: POINTER(Windows.Win32.Media.Audio.DirectSound.DSBPOSITIONNOTIFY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPDSENUMCALLBACKA(param0: POINTER(Guid), param1: Windows.Win32.Foundation.PSTR, param2: Windows.Win32.Foundation.PSTR, param3: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPDSENUMCALLBACKW(param0: POINTER(Guid), param1: Windows.Win32.Foundation.PWSTR, param2: Windows.Win32.Foundation.PWSTR, param3: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
make_head(_module, 'DS3DBUFFER')
make_head(_module, 'DS3DLISTENER')
make_head(_module, 'DSBCAPS')
make_head(_module, 'DSBPOSITIONNOTIFY')
make_head(_module, 'DSBUFFERDESC')
make_head(_module, 'DSBUFFERDESC1')
make_head(_module, 'DSCAPS')
make_head(_module, 'DSCBCAPS')
make_head(_module, 'DSCBUFFERDESC')
make_head(_module, 'DSCBUFFERDESC1')
make_head(_module, 'DSCCAPS')
make_head(_module, 'DSCEFFECTDESC')
make_head(_module, 'DSCFXAec')
make_head(_module, 'DSCFXNoiseSuppress')
make_head(_module, 'DSEFFECTDESC')
make_head(_module, 'DSFXChorus')
make_head(_module, 'DSFXCompressor')
make_head(_module, 'DSFXDistortion')
make_head(_module, 'DSFXEcho')
make_head(_module, 'DSFXFlanger')
make_head(_module, 'DSFXGargle')
make_head(_module, 'DSFXI3DL2Reverb')
make_head(_module, 'DSFXParamEq')
make_head(_module, 'DSFXWavesReverb')
make_head(_module, 'IDirectSound')
make_head(_module, 'IDirectSound3DBuffer')
make_head(_module, 'IDirectSound3DListener')
make_head(_module, 'IDirectSound8')
make_head(_module, 'IDirectSoundBuffer')
make_head(_module, 'IDirectSoundBuffer8')
make_head(_module, 'IDirectSoundCapture')
make_head(_module, 'IDirectSoundCaptureBuffer')
make_head(_module, 'IDirectSoundCaptureBuffer8')
make_head(_module, 'IDirectSoundCaptureFXAec')
make_head(_module, 'IDirectSoundCaptureFXNoiseSuppress')
make_head(_module, 'IDirectSoundFXChorus')
make_head(_module, 'IDirectSoundFXCompressor')
make_head(_module, 'IDirectSoundFXDistortion')
make_head(_module, 'IDirectSoundFXEcho')
make_head(_module, 'IDirectSoundFXFlanger')
make_head(_module, 'IDirectSoundFXGargle')
make_head(_module, 'IDirectSoundFXI3DL2Reverb')
make_head(_module, 'IDirectSoundFXParamEq')
make_head(_module, 'IDirectSoundFXWavesReverb')
make_head(_module, 'IDirectSoundFullDuplex')
make_head(_module, 'IDirectSoundNotify')
make_head(_module, 'LPDSENUMCALLBACKA')
make_head(_module, 'LPDSENUMCALLBACKW')
__all__ = [
    "CLSID_DirectSound",
    "CLSID_DirectSound8",
    "CLSID_DirectSoundCapture",
    "CLSID_DirectSoundCapture8",
    "CLSID_DirectSoundFullDuplex",
    "DIRECTSOUND_VERSION",
    "DS3DALG_HRTF_FULL",
    "DS3DALG_HRTF_LIGHT",
    "DS3DALG_NO_VIRTUALIZATION",
    "DS3DBUFFER",
    "DS3DLISTENER",
    "DS3DMODE_DISABLE",
    "DS3DMODE_HEADRELATIVE",
    "DS3DMODE_NORMAL",
    "DS3D_DEFAULTCONEANGLE",
    "DS3D_DEFAULTCONEOUTSIDEVOLUME",
    "DS3D_DEFAULTDISTANCEFACTOR",
    "DS3D_DEFAULTDOPPLERFACTOR",
    "DS3D_DEFAULTMAXDISTANCE",
    "DS3D_DEFAULTMINDISTANCE",
    "DS3D_DEFAULTROLLOFFFACTOR",
    "DS3D_DEFERRED",
    "DS3D_IMMEDIATE",
    "DS3D_MAXCONEANGLE",
    "DS3D_MAXDOPPLERFACTOR",
    "DS3D_MAXROLLOFFFACTOR",
    "DS3D_MINCONEANGLE",
    "DS3D_MINDOPPLERFACTOR",
    "DS3D_MINROLLOFFFACTOR",
    "DSBCAPS",
    "DSBCAPS_CTRL3D",
    "DSBCAPS_CTRLFREQUENCY",
    "DSBCAPS_CTRLFX",
    "DSBCAPS_CTRLPAN",
    "DSBCAPS_CTRLPOSITIONNOTIFY",
    "DSBCAPS_CTRLVOLUME",
    "DSBCAPS_GETCURRENTPOSITION2",
    "DSBCAPS_GLOBALFOCUS",
    "DSBCAPS_LOCDEFER",
    "DSBCAPS_LOCHARDWARE",
    "DSBCAPS_LOCSOFTWARE",
    "DSBCAPS_MUTE3DATMAXDISTANCE",
    "DSBCAPS_PRIMARYBUFFER",
    "DSBCAPS_STATIC",
    "DSBCAPS_STICKYFOCUS",
    "DSBCAPS_TRUEPLAYPOSITION",
    "DSBFREQUENCY_MAX",
    "DSBFREQUENCY_MIN",
    "DSBFREQUENCY_ORIGINAL",
    "DSBLOCK_ENTIREBUFFER",
    "DSBLOCK_FROMWRITECURSOR",
    "DSBNOTIFICATIONS_MAX",
    "DSBPAN_CENTER",
    "DSBPAN_LEFT",
    "DSBPAN_RIGHT",
    "DSBPLAY_LOCHARDWARE",
    "DSBPLAY_LOCSOFTWARE",
    "DSBPLAY_LOOPING",
    "DSBPLAY_TERMINATEBY_DISTANCE",
    "DSBPLAY_TERMINATEBY_PRIORITY",
    "DSBPLAY_TERMINATEBY_TIME",
    "DSBPN_OFFSETSTOP",
    "DSBPOSITIONNOTIFY",
    "DSBSIZE_FX_MIN",
    "DSBSIZE_MAX",
    "DSBSIZE_MIN",
    "DSBSTATUS_BUFFERLOST",
    "DSBSTATUS_LOCHARDWARE",
    "DSBSTATUS_LOCSOFTWARE",
    "DSBSTATUS_LOOPING",
    "DSBSTATUS_PLAYING",
    "DSBSTATUS_TERMINATED",
    "DSBUFFERDESC",
    "DSBUFFERDESC1",
    "DSBVOLUME_MAX",
    "DSBVOLUME_MIN",
    "DSCAPS",
    "DSCAPS_CERTIFIED",
    "DSCAPS_CONTINUOUSRATE",
    "DSCAPS_EMULDRIVER",
    "DSCAPS_PRIMARY16BIT",
    "DSCAPS_PRIMARY8BIT",
    "DSCAPS_PRIMARYMONO",
    "DSCAPS_PRIMARYSTEREO",
    "DSCAPS_SECONDARY16BIT",
    "DSCAPS_SECONDARY8BIT",
    "DSCAPS_SECONDARYMONO",
    "DSCAPS_SECONDARYSTEREO",
    "DSCBCAPS",
    "DSCBCAPS_CTRLFX",
    "DSCBCAPS_WAVEMAPPED",
    "DSCBLOCK_ENTIREBUFFER",
    "DSCBSTART_LOOPING",
    "DSCBSTATUS_CAPTURING",
    "DSCBSTATUS_LOOPING",
    "DSCBUFFERDESC",
    "DSCBUFFERDESC1",
    "DSCCAPS",
    "DSCCAPS_CERTIFIED",
    "DSCCAPS_EMULDRIVER",
    "DSCCAPS_MULTIPLECAPTURE",
    "DSCEFFECTDESC",
    "DSCFXAec",
    "DSCFXNoiseSuppress",
    "DSCFXR_LOCHARDWARE",
    "DSCFXR_LOCSOFTWARE",
    "DSCFX_AEC_MODE_FULL_DUPLEX",
    "DSCFX_AEC_MODE_HALF_DUPLEX",
    "DSCFX_AEC_MODE_PASS_THROUGH",
    "DSCFX_AEC_STATUS_CURRENTLY_CONVERGED",
    "DSCFX_AEC_STATUS_HISTORY_CONTINUOUSLY_CONVERGED",
    "DSCFX_AEC_STATUS_HISTORY_PREVIOUSLY_DIVERGED",
    "DSCFX_AEC_STATUS_HISTORY_UNINITIALIZED",
    "DSCFX_LOCHARDWARE",
    "DSCFX_LOCSOFTWARE",
    "DSDEVID_DefaultCapture",
    "DSDEVID_DefaultPlayback",
    "DSDEVID_DefaultVoiceCapture",
    "DSDEVID_DefaultVoicePlayback",
    "DSEFFECTDESC",
    "DSFXCHORUS_DELAY_MAX",
    "DSFXCHORUS_DELAY_MIN",
    "DSFXCHORUS_DEPTH_MAX",
    "DSFXCHORUS_DEPTH_MIN",
    "DSFXCHORUS_FEEDBACK_MAX",
    "DSFXCHORUS_FEEDBACK_MIN",
    "DSFXCHORUS_FREQUENCY_MAX",
    "DSFXCHORUS_FREQUENCY_MIN",
    "DSFXCHORUS_PHASE_180",
    "DSFXCHORUS_PHASE_90",
    "DSFXCHORUS_PHASE_MAX",
    "DSFXCHORUS_PHASE_MIN",
    "DSFXCHORUS_PHASE_NEG_180",
    "DSFXCHORUS_PHASE_NEG_90",
    "DSFXCHORUS_PHASE_ZERO",
    "DSFXCHORUS_WAVE_SIN",
    "DSFXCHORUS_WAVE_TRIANGLE",
    "DSFXCHORUS_WETDRYMIX_MAX",
    "DSFXCHORUS_WETDRYMIX_MIN",
    "DSFXCOMPRESSOR_ATTACK_MAX",
    "DSFXCOMPRESSOR_ATTACK_MIN",
    "DSFXCOMPRESSOR_GAIN_MAX",
    "DSFXCOMPRESSOR_GAIN_MIN",
    "DSFXCOMPRESSOR_PREDELAY_MAX",
    "DSFXCOMPRESSOR_PREDELAY_MIN",
    "DSFXCOMPRESSOR_RATIO_MAX",
    "DSFXCOMPRESSOR_RATIO_MIN",
    "DSFXCOMPRESSOR_RELEASE_MAX",
    "DSFXCOMPRESSOR_RELEASE_MIN",
    "DSFXCOMPRESSOR_THRESHOLD_MAX",
    "DSFXCOMPRESSOR_THRESHOLD_MIN",
    "DSFXChorus",
    "DSFXCompressor",
    "DSFXDISTORTION_EDGE_MAX",
    "DSFXDISTORTION_EDGE_MIN",
    "DSFXDISTORTION_GAIN_MAX",
    "DSFXDISTORTION_GAIN_MIN",
    "DSFXDISTORTION_POSTEQBANDWIDTH_MAX",
    "DSFXDISTORTION_POSTEQBANDWIDTH_MIN",
    "DSFXDISTORTION_POSTEQCENTERFREQUENCY_MAX",
    "DSFXDISTORTION_POSTEQCENTERFREQUENCY_MIN",
    "DSFXDISTORTION_PRELOWPASSCUTOFF_MAX",
    "DSFXDISTORTION_PRELOWPASSCUTOFF_MIN",
    "DSFXDistortion",
    "DSFXECHO_FEEDBACK_MAX",
    "DSFXECHO_FEEDBACK_MIN",
    "DSFXECHO_LEFTDELAY_MAX",
    "DSFXECHO_LEFTDELAY_MIN",
    "DSFXECHO_PANDELAY_MAX",
    "DSFXECHO_PANDELAY_MIN",
    "DSFXECHO_RIGHTDELAY_MAX",
    "DSFXECHO_RIGHTDELAY_MIN",
    "DSFXECHO_WETDRYMIX_MAX",
    "DSFXECHO_WETDRYMIX_MIN",
    "DSFXEcho",
    "DSFXFLANGER_DELAY_MAX",
    "DSFXFLANGER_DELAY_MIN",
    "DSFXFLANGER_DEPTH_MAX",
    "DSFXFLANGER_DEPTH_MIN",
    "DSFXFLANGER_FEEDBACK_MAX",
    "DSFXFLANGER_FEEDBACK_MIN",
    "DSFXFLANGER_FREQUENCY_MAX",
    "DSFXFLANGER_FREQUENCY_MIN",
    "DSFXFLANGER_PHASE_180",
    "DSFXFLANGER_PHASE_90",
    "DSFXFLANGER_PHASE_MAX",
    "DSFXFLANGER_PHASE_MIN",
    "DSFXFLANGER_PHASE_NEG_180",
    "DSFXFLANGER_PHASE_NEG_90",
    "DSFXFLANGER_PHASE_ZERO",
    "DSFXFLANGER_WAVE_SIN",
    "DSFXFLANGER_WAVE_TRIANGLE",
    "DSFXFLANGER_WETDRYMIX_MAX",
    "DSFXFLANGER_WETDRYMIX_MIN",
    "DSFXFlanger",
    "DSFXGARGLE_RATEHZ_MAX",
    "DSFXGARGLE_RATEHZ_MIN",
    "DSFXGARGLE_WAVE_SQUARE",
    "DSFXGARGLE_WAVE_TRIANGLE",
    "DSFXGargle",
    "DSFXI3DL2Reverb",
    "DSFXPARAMEQ_BANDWIDTH_MAX",
    "DSFXPARAMEQ_BANDWIDTH_MIN",
    "DSFXPARAMEQ_CENTER_MAX",
    "DSFXPARAMEQ_CENTER_MIN",
    "DSFXPARAMEQ_GAIN_MAX",
    "DSFXPARAMEQ_GAIN_MIN",
    "DSFXParamEq",
    "DSFXR_FAILED",
    "DSFXR_LOCHARDWARE",
    "DSFXR_LOCSOFTWARE",
    "DSFXR_PRESENT",
    "DSFXR_SENDLOOP",
    "DSFXR_UNALLOCATED",
    "DSFXR_UNKNOWN",
    "DSFXWavesReverb",
    "DSFX_I3DL2REVERB_DECAYHFRATIO_DEFAULT",
    "DSFX_I3DL2REVERB_DECAYHFRATIO_MAX",
    "DSFX_I3DL2REVERB_DECAYHFRATIO_MIN",
    "DSFX_I3DL2REVERB_DECAYTIME_DEFAULT",
    "DSFX_I3DL2REVERB_DECAYTIME_MAX",
    "DSFX_I3DL2REVERB_DECAYTIME_MIN",
    "DSFX_I3DL2REVERB_DENSITY_DEFAULT",
    "DSFX_I3DL2REVERB_DENSITY_MAX",
    "DSFX_I3DL2REVERB_DENSITY_MIN",
    "DSFX_I3DL2REVERB_DIFFUSION_DEFAULT",
    "DSFX_I3DL2REVERB_DIFFUSION_MAX",
    "DSFX_I3DL2REVERB_DIFFUSION_MIN",
    "DSFX_I3DL2REVERB_HFREFERENCE_DEFAULT",
    "DSFX_I3DL2REVERB_HFREFERENCE_MAX",
    "DSFX_I3DL2REVERB_HFREFERENCE_MIN",
    "DSFX_I3DL2REVERB_QUALITY_DEFAULT",
    "DSFX_I3DL2REVERB_QUALITY_MAX",
    "DSFX_I3DL2REVERB_QUALITY_MIN",
    "DSFX_I3DL2REVERB_REFLECTIONSDELAY_DEFAULT",
    "DSFX_I3DL2REVERB_REFLECTIONSDELAY_MAX",
    "DSFX_I3DL2REVERB_REFLECTIONSDELAY_MIN",
    "DSFX_I3DL2REVERB_REFLECTIONS_DEFAULT",
    "DSFX_I3DL2REVERB_REFLECTIONS_MAX",
    "DSFX_I3DL2REVERB_REFLECTIONS_MIN",
    "DSFX_I3DL2REVERB_REVERBDELAY_DEFAULT",
    "DSFX_I3DL2REVERB_REVERBDELAY_MAX",
    "DSFX_I3DL2REVERB_REVERBDELAY_MIN",
    "DSFX_I3DL2REVERB_REVERB_DEFAULT",
    "DSFX_I3DL2REVERB_REVERB_MAX",
    "DSFX_I3DL2REVERB_REVERB_MIN",
    "DSFX_I3DL2REVERB_ROOMHF_DEFAULT",
    "DSFX_I3DL2REVERB_ROOMHF_MAX",
    "DSFX_I3DL2REVERB_ROOMHF_MIN",
    "DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_DEFAULT",
    "DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MAX",
    "DSFX_I3DL2REVERB_ROOMROLLOFFFACTOR_MIN",
    "DSFX_I3DL2REVERB_ROOM_DEFAULT",
    "DSFX_I3DL2REVERB_ROOM_MAX",
    "DSFX_I3DL2REVERB_ROOM_MIN",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_ALLEY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_ARENA",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_AUDITORIUM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_BATHROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CARPETEDHALLWAY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CAVE",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CITY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_CONCERTHALL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_DEFAULT",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_FOREST",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_GENERIC",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_HALLWAY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_HANGAR",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEHALL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_LARGEROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_LIVINGROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMHALL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_MEDIUMROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_MOUNTAINS",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PADDEDCELL",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PARKINGLOT",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PLAIN",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_PLATE",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_QUARRY",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_ROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_SEWERPIPE",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_SMALLROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_STONECORRIDOR",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_STONEROOM",
    "DSFX_I3DL2_ENVIRONMENT_PRESET_UNDERWATER",
    "DSFX_I3DL2_MATERIAL_PRESET_BRICKWALL",
    "DSFX_I3DL2_MATERIAL_PRESET_CURTAIN",
    "DSFX_I3DL2_MATERIAL_PRESET_DOUBLEWINDOW",
    "DSFX_I3DL2_MATERIAL_PRESET_SINGLEWINDOW",
    "DSFX_I3DL2_MATERIAL_PRESET_STONEWALL",
    "DSFX_I3DL2_MATERIAL_PRESET_THICKDOOR",
    "DSFX_I3DL2_MATERIAL_PRESET_THINDOOR",
    "DSFX_I3DL2_MATERIAL_PRESET_WOODWALL",
    "DSFX_LOCHARDWARE",
    "DSFX_LOCSOFTWARE",
    "DSFX_WAVESREVERB_HIGHFREQRTRATIO_DEFAULT",
    "DSFX_WAVESREVERB_HIGHFREQRTRATIO_MAX",
    "DSFX_WAVESREVERB_HIGHFREQRTRATIO_MIN",
    "DSFX_WAVESREVERB_INGAIN_DEFAULT",
    "DSFX_WAVESREVERB_INGAIN_MAX",
    "DSFX_WAVESREVERB_INGAIN_MIN",
    "DSFX_WAVESREVERB_REVERBMIX_DEFAULT",
    "DSFX_WAVESREVERB_REVERBMIX_MAX",
    "DSFX_WAVESREVERB_REVERBMIX_MIN",
    "DSFX_WAVESREVERB_REVERBTIME_DEFAULT",
    "DSFX_WAVESREVERB_REVERBTIME_MAX",
    "DSFX_WAVESREVERB_REVERBTIME_MIN",
    "DSSCL_EXCLUSIVE",
    "DSSCL_NORMAL",
    "DSSCL_PRIORITY",
    "DSSCL_WRITEPRIMARY",
    "DSSPEAKER_5POINT1",
    "DSSPEAKER_5POINT1_BACK",
    "DSSPEAKER_5POINT1_SURROUND",
    "DSSPEAKER_7POINT1",
    "DSSPEAKER_7POINT1_SURROUND",
    "DSSPEAKER_7POINT1_WIDE",
    "DSSPEAKER_DIRECTOUT",
    "DSSPEAKER_GEOMETRY_MAX",
    "DSSPEAKER_GEOMETRY_MIN",
    "DSSPEAKER_GEOMETRY_NARROW",
    "DSSPEAKER_GEOMETRY_WIDE",
    "DSSPEAKER_HEADPHONE",
    "DSSPEAKER_MONO",
    "DSSPEAKER_QUAD",
    "DSSPEAKER_STEREO",
    "DSSPEAKER_SURROUND",
    "DS_CERTIFIED",
    "DS_NO_VIRTUALIZATION",
    "DS_UNCERTIFIED",
    "DirectSoundCaptureCreate",
    "DirectSoundCaptureCreate8",
    "DirectSoundCaptureEnumerateA",
    "DirectSoundCaptureEnumerateW",
    "DirectSoundCreate",
    "DirectSoundCreate8",
    "DirectSoundEnumerateA",
    "DirectSoundEnumerateW",
    "DirectSoundFullDuplexCreate",
    "GUID_All_Objects",
    "GUID_DSCFX_CLASS_AEC",
    "GUID_DSCFX_CLASS_NS",
    "GUID_DSCFX_MS_AEC",
    "GUID_DSCFX_MS_NS",
    "GUID_DSCFX_SYSTEM_AEC",
    "GUID_DSCFX_SYSTEM_NS",
    "GUID_DSFX_STANDARD_CHORUS",
    "GUID_DSFX_STANDARD_COMPRESSOR",
    "GUID_DSFX_STANDARD_DISTORTION",
    "GUID_DSFX_STANDARD_ECHO",
    "GUID_DSFX_STANDARD_FLANGER",
    "GUID_DSFX_STANDARD_GARGLE",
    "GUID_DSFX_STANDARD_I3DL2REVERB",
    "GUID_DSFX_STANDARD_PARAMEQ",
    "GUID_DSFX_WAVES_REVERB",
    "GetDeviceID",
    "IDirectSound",
    "IDirectSound3DBuffer",
    "IDirectSound3DListener",
    "IDirectSound8",
    "IDirectSoundBuffer",
    "IDirectSoundBuffer8",
    "IDirectSoundCapture",
    "IDirectSoundCaptureBuffer",
    "IDirectSoundCaptureBuffer8",
    "IDirectSoundCaptureFXAec",
    "IDirectSoundCaptureFXNoiseSuppress",
    "IDirectSoundFXChorus",
    "IDirectSoundFXCompressor",
    "IDirectSoundFXDistortion",
    "IDirectSoundFXEcho",
    "IDirectSoundFXFlanger",
    "IDirectSoundFXGargle",
    "IDirectSoundFXI3DL2Reverb",
    "IDirectSoundFXParamEq",
    "IDirectSoundFXWavesReverb",
    "IDirectSoundFullDuplex",
    "IDirectSoundNotify",
    "KSPROPERTY_SUPPORT_GET",
    "KSPROPERTY_SUPPORT_SET",
    "LPDSENUMCALLBACKA",
    "LPDSENUMCALLBACKW",
    "_FACDS",
]
_arch_optional = [
]
