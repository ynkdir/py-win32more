from win32more.base import *
import win32more.Foundation
import win32more.Media.Audio
import win32more.Media.Audio.XAudio2
import win32more.System.Com

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
FXEQ_MIN_FRAMERATE = 22000
FXEQ_MAX_FRAMERATE = 48000
FXEQ_MIN_FREQUENCY_CENTER = 20
FXEQ_MAX_FREQUENCY_CENTER = 20000
FXEQ_DEFAULT_FREQUENCY_CENTER_0 = 100
FXEQ_DEFAULT_FREQUENCY_CENTER_1 = 800
FXEQ_DEFAULT_FREQUENCY_CENTER_2 = 2000
FXEQ_DEFAULT_FREQUENCY_CENTER_3 = 10000
FXEQ_MIN_GAIN = 0.126
FXEQ_MAX_GAIN = 7.94
FXEQ_DEFAULT_GAIN = 1
FXEQ_MIN_BANDWIDTH = 0.1
FXEQ_MAX_BANDWIDTH = 2
FXEQ_DEFAULT_BANDWIDTH = 1
FXMASTERINGLIMITER_MIN_RELEASE = 1
FXMASTERINGLIMITER_MAX_RELEASE = 20
FXMASTERINGLIMITER_DEFAULT_RELEASE = 6
FXMASTERINGLIMITER_MIN_LOUDNESS = 1
FXMASTERINGLIMITER_MAX_LOUDNESS = 1800
FXMASTERINGLIMITER_DEFAULT_LOUDNESS = 1000
FXREVERB_MIN_DIFFUSION = 0
FXREVERB_MAX_DIFFUSION = 1
FXREVERB_DEFAULT_DIFFUSION = 0.9
FXREVERB_MIN_ROOMSIZE = 0.0001
FXREVERB_MAX_ROOMSIZE = 1
FXREVERB_DEFAULT_ROOMSIZE = 0.6
FXLOUDNESS_DEFAULT_MOMENTARY_MS = 400
FXLOUDNESS_DEFAULT_SHORTTERM_MS = 3000
FXECHO_MIN_WETDRYMIX = 0
FXECHO_MAX_WETDRYMIX = 1
FXECHO_DEFAULT_WETDRYMIX = 0.5
FXECHO_MIN_FEEDBACK = 0
FXECHO_MAX_FEEDBACK = 1
FXECHO_DEFAULT_FEEDBACK = 0.5
FXECHO_MIN_DELAY = 1
FXECHO_MAX_DELAY = 2000
FXECHO_DEFAULT_DELAY = 500
XAUDIO2_MAX_BUFFER_BYTES = 2147483648
XAUDIO2_MAX_QUEUED_BUFFERS = 64
XAUDIO2_MAX_BUFFERS_SYSTEM = 2
XAUDIO2_MAX_AUDIO_CHANNELS = 64
XAUDIO2_MIN_SAMPLE_RATE = 1000
XAUDIO2_MAX_SAMPLE_RATE = 200000
XAUDIO2_MAX_VOLUME_LEVEL = 16777216
XAUDIO2_MAX_FREQ_RATIO = 1024
XAUDIO2_DEFAULT_FREQ_RATIO = 2
XAUDIO2_MAX_FILTER_ONEOVERQ = 1.5
XAUDIO2_MAX_FILTER_FREQUENCY = 1
XAUDIO2_MAX_LOOP_COUNT = 254
XAUDIO2_MAX_INSTANCES = 8
XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MONO = 600000
XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MULTICHANNEL = 300000
XAUDIO2_COMMIT_NOW = 0
XAUDIO2_COMMIT_ALL = 0
XAUDIO2_NO_LOOP_REGION = 0
XAUDIO2_LOOP_INFINITE = 255
XAUDIO2_DEFAULT_CHANNELS = 0
XAUDIO2_DEFAULT_SAMPLERATE = 0
XAUDIO2_DEBUG_ENGINE = 1
XAUDIO2_VOICE_NOPITCH = 2
XAUDIO2_VOICE_NOSRC = 4
XAUDIO2_VOICE_USEFILTER = 8
XAUDIO2_PLAY_TAILS = 32
XAUDIO2_END_OF_STREAM = 64
XAUDIO2_SEND_USEFILTER = 128
XAUDIO2_VOICE_NOSAMPLESPLAYED = 256
XAUDIO2_STOP_ENGINE_WHEN_IDLE = 8192
XAUDIO2_1024_QUANTUM = 32768
XAUDIO2_NO_VIRTUAL_AUDIO_CLIENT = 65536
XAUDIO2_DEFAULT_FILTER_FREQUENCY = 1
XAUDIO2_DEFAULT_FILTER_ONEOVERQ = 1
XAUDIO2_QUANTUM_NUMERATOR = 1
XAUDIO2_QUANTUM_DENOMINATOR = 100
FACILITY_XAUDIO2 = 2198
XAUDIO2_E_INVALID_CALL = -2003435519
XAUDIO2_E_XMA_DECODER_ERROR = -2003435518
XAUDIO2_E_XAPO_CREATION_FAILED = -2003435517
XAUDIO2_E_DEVICE_INVALIDATED = -2003435516
Processor1 = 1
Processor2 = 2
Processor3 = 4
Processor4 = 8
Processor5 = 16
Processor6 = 32
Processor7 = 64
Processor8 = 128
Processor9 = 256
Processor10 = 512
Processor11 = 1024
Processor12 = 2048
Processor13 = 4096
Processor14 = 8192
Processor15 = 16384
Processor16 = 32768
Processor17 = 65536
Processor18 = 131072
Processor19 = 262144
Processor20 = 524288
Processor21 = 1048576
Processor22 = 2097152
Processor23 = 4194304
Processor24 = 8388608
Processor25 = 16777216
Processor26 = 33554432
Processor27 = 67108864
Processor28 = 134217728
Processor29 = 268435456
Processor30 = 536870912
Processor31 = 1073741824
Processor32 = 2147483648
XAUDIO2_ANY_PROCESSOR = 4294967295
XAUDIO2_USE_DEFAULT_PROCESSOR = 0
XAUDIO2_DEFAULT_PROCESSOR = 1
XAUDIO2_LOG_ERRORS = 1
XAUDIO2_LOG_WARNINGS = 2
XAUDIO2_LOG_INFO = 4
XAUDIO2_LOG_DETAIL = 8
XAUDIO2_LOG_API_CALLS = 16
XAUDIO2_LOG_FUNC_CALLS = 32
XAUDIO2_LOG_TIMING = 64
XAUDIO2_LOG_LOCKS = 128
XAUDIO2_LOG_MEMORY = 256
XAUDIO2_LOG_STREAMING = 4096
XAUDIO2FX_REVERB_MIN_FRAMERATE = 20000
XAUDIO2FX_REVERB_MAX_FRAMERATE = 48000
XAUDIO2FX_REVERB_MIN_WET_DRY_MIX = 0
XAUDIO2FX_REVERB_MIN_REFLECTIONS_DELAY = 0
XAUDIO2FX_REVERB_MIN_REVERB_DELAY = 0
XAUDIO2FX_REVERB_MIN_REAR_DELAY = 0
XAUDIO2FX_REVERB_MIN_7POINT1_SIDE_DELAY = 0
XAUDIO2FX_REVERB_MIN_7POINT1_REAR_DELAY = 0
XAUDIO2FX_REVERB_MIN_POSITION = 0
XAUDIO2FX_REVERB_MIN_DIFFUSION = 0
XAUDIO2FX_REVERB_MIN_LOW_EQ_GAIN = 0
XAUDIO2FX_REVERB_MIN_LOW_EQ_CUTOFF = 0
XAUDIO2FX_REVERB_MIN_HIGH_EQ_GAIN = 0
XAUDIO2FX_REVERB_MIN_HIGH_EQ_CUTOFF = 0
XAUDIO2FX_REVERB_MIN_ROOM_FILTER_FREQ = 20
XAUDIO2FX_REVERB_MIN_ROOM_FILTER_MAIN = -100
XAUDIO2FX_REVERB_MIN_ROOM_FILTER_HF = -100
XAUDIO2FX_REVERB_MIN_REFLECTIONS_GAIN = -100
XAUDIO2FX_REVERB_MIN_REVERB_GAIN = -100
XAUDIO2FX_REVERB_MIN_DECAY_TIME = 0.1
XAUDIO2FX_REVERB_MIN_DENSITY = 0
XAUDIO2FX_REVERB_MIN_ROOM_SIZE = 0
XAUDIO2FX_REVERB_MAX_WET_DRY_MIX = 100
XAUDIO2FX_REVERB_MAX_REFLECTIONS_DELAY = 300
XAUDIO2FX_REVERB_MAX_REVERB_DELAY = 85
XAUDIO2FX_REVERB_MAX_REAR_DELAY = 5
XAUDIO2FX_REVERB_MAX_7POINT1_SIDE_DELAY = 5
XAUDIO2FX_REVERB_MAX_7POINT1_REAR_DELAY = 20
XAUDIO2FX_REVERB_MAX_POSITION = 30
XAUDIO2FX_REVERB_MAX_DIFFUSION = 15
XAUDIO2FX_REVERB_MAX_LOW_EQ_GAIN = 12
XAUDIO2FX_REVERB_MAX_LOW_EQ_CUTOFF = 9
XAUDIO2FX_REVERB_MAX_HIGH_EQ_GAIN = 8
XAUDIO2FX_REVERB_MAX_HIGH_EQ_CUTOFF = 14
XAUDIO2FX_REVERB_MAX_ROOM_FILTER_FREQ = 20000
XAUDIO2FX_REVERB_MAX_ROOM_FILTER_MAIN = 0
XAUDIO2FX_REVERB_MAX_ROOM_FILTER_HF = 0
XAUDIO2FX_REVERB_MAX_REFLECTIONS_GAIN = 20
XAUDIO2FX_REVERB_MAX_REVERB_GAIN = 20
XAUDIO2FX_REVERB_MAX_DENSITY = 100
XAUDIO2FX_REVERB_MAX_ROOM_SIZE = 100
XAUDIO2FX_REVERB_DEFAULT_WET_DRY_MIX = 100
XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_DELAY = 5
XAUDIO2FX_REVERB_DEFAULT_REVERB_DELAY = 5
XAUDIO2FX_REVERB_DEFAULT_REAR_DELAY = 5
XAUDIO2FX_REVERB_DEFAULT_7POINT1_SIDE_DELAY = 5
XAUDIO2FX_REVERB_DEFAULT_7POINT1_REAR_DELAY = 20
XAUDIO2FX_REVERB_DEFAULT_POSITION = 6
XAUDIO2FX_REVERB_DEFAULT_POSITION_MATRIX = 27
XAUDIO2FX_REVERB_DEFAULT_EARLY_DIFFUSION = 8
XAUDIO2FX_REVERB_DEFAULT_LATE_DIFFUSION = 8
XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_GAIN = 8
XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_CUTOFF = 4
XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_GAIN = 8
XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_CUTOFF = 4
XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_FREQ = 5000
XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_MAIN = 0
XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_HF = 0
XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_GAIN = 0
XAUDIO2FX_REVERB_DEFAULT_REVERB_GAIN = 0
XAUDIO2FX_REVERB_DEFAULT_DECAY_TIME = 1
XAUDIO2FX_REVERB_DEFAULT_DENSITY = 100
XAUDIO2FX_REVERB_DEFAULT_ROOM_SIZE = 100
XAUDIO2FX_REVERB_DEFAULT_DISABLE_LATE_FIELD = 0
HRTF_MAX_GAIN_LIMIT = 12
HRTF_MIN_GAIN_LIMIT = -96
HRTF_MIN_UNITY_GAIN_DISTANCE = 0.05
HRTF_DEFAULT_UNITY_GAIN_DISTANCE = 1
FACILITY_XAPO = 2199
XAPO_E_FORMAT_UNSUPPORTED = -2003369983
XAPO_MIN_CHANNELS = 1
XAPO_MAX_CHANNELS = 64
XAPO_MIN_FRAMERATE = 1000
XAPO_MAX_FRAMERATE = 200000
XAPO_REGISTRATION_STRING_LENGTH = 256
XAPO_FLAG_CHANNELS_MUST_MATCH = 1
XAPO_FLAG_FRAMERATE_MUST_MATCH = 2
XAPO_FLAG_BITSPERSAMPLE_MUST_MATCH = 4
XAPO_FLAG_BUFFERCOUNT_MUST_MATCH = 8
XAPO_FLAG_INPLACE_REQUIRED = 32
XAPO_FLAG_INPLACE_SUPPORTED = 16
SPEAKER_MONO = 4
X3DAUDIO_HANDLE_BYTESIZE = 20
X3DAUDIO_PI = 3.1415927
X3DAUDIO_2PI = 6.2831855
X3DAUDIO_SPEED_OF_SOUND = 343.5
X3DAUDIO_CALCULATE_MATRIX = 1
X3DAUDIO_CALCULATE_DELAY = 2
X3DAUDIO_CALCULATE_LPF_DIRECT = 4
X3DAUDIO_CALCULATE_LPF_REVERB = 8
X3DAUDIO_CALCULATE_REVERB = 16
X3DAUDIO_CALCULATE_DOPPLER = 32
X3DAUDIO_CALCULATE_EMITTER_ANGLE = 64
X3DAUDIO_CALCULATE_ZEROCENTER = 65536
X3DAUDIO_CALCULATE_REDIRECT_TO_LFE = 131072
def _define_XAPO_REGISTRATION_PROPERTIES_head():
    class XAPO_REGISTRATION_PROPERTIES(Structure):
        pass
    return XAPO_REGISTRATION_PROPERTIES
def _define_XAPO_REGISTRATION_PROPERTIES():
    XAPO_REGISTRATION_PROPERTIES = win32more.Media.Audio.XAudio2.XAPO_REGISTRATION_PROPERTIES_head
    XAPO_REGISTRATION_PROPERTIES._pack_ = 1
    XAPO_REGISTRATION_PROPERTIES._fields_ = [
        ("clsid", Guid),
        ("FriendlyName", Char * 256),
        ("CopyrightInfo", Char * 256),
        ("MajorVersion", UInt32),
        ("MinorVersion", UInt32),
        ("Flags", UInt32),
        ("MinInputBufferCount", UInt32),
        ("MaxInputBufferCount", UInt32),
        ("MinOutputBufferCount", UInt32),
        ("MaxOutputBufferCount", UInt32),
    ]
    return XAPO_REGISTRATION_PROPERTIES
def _define_XAPO_LOCKFORPROCESS_PARAMETERS_head():
    class XAPO_LOCKFORPROCESS_PARAMETERS(Structure):
        pass
    return XAPO_LOCKFORPROCESS_PARAMETERS
def _define_XAPO_LOCKFORPROCESS_PARAMETERS():
    XAPO_LOCKFORPROCESS_PARAMETERS = win32more.Media.Audio.XAudio2.XAPO_LOCKFORPROCESS_PARAMETERS_head
    XAPO_LOCKFORPROCESS_PARAMETERS._pack_ = 1
    XAPO_LOCKFORPROCESS_PARAMETERS._fields_ = [
        ("pFormat", POINTER(win32more.Media.Audio.WAVEFORMATEX_head)),
        ("MaxFrameCount", UInt32),
    ]
    return XAPO_LOCKFORPROCESS_PARAMETERS
XAPO_BUFFER_FLAGS = Int32
XAPO_BUFFER_SILENT = 0
XAPO_BUFFER_VALID = 1
def _define_XAPO_PROCESS_BUFFER_PARAMETERS_head():
    class XAPO_PROCESS_BUFFER_PARAMETERS(Structure):
        pass
    return XAPO_PROCESS_BUFFER_PARAMETERS
def _define_XAPO_PROCESS_BUFFER_PARAMETERS():
    XAPO_PROCESS_BUFFER_PARAMETERS = win32more.Media.Audio.XAudio2.XAPO_PROCESS_BUFFER_PARAMETERS_head
    XAPO_PROCESS_BUFFER_PARAMETERS._pack_ = 1
    XAPO_PROCESS_BUFFER_PARAMETERS._fields_ = [
        ("pBuffer", c_void_p),
        ("BufferFlags", win32more.Media.Audio.XAudio2.XAPO_BUFFER_FLAGS),
        ("ValidFrameCount", UInt32),
    ]
    return XAPO_PROCESS_BUFFER_PARAMETERS
def _define_IXAPO_head():
    class IXAPO(win32more.System.Com.IUnknown_head):
        Guid = Guid('a410b984-9839-4819-a0be-2856ae6b3adb')
    return IXAPO
def _define_IXAPO():
    IXAPO = win32more.Media.Audio.XAudio2.IXAPO_head
    IXAPO.GetRegistrationProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.XAudio2.XAPO_REGISTRATION_PROPERTIES_head)), use_last_error=False)(3, 'GetRegistrationProperties', ((1, 'ppRegistrationProperties'),)))
    IXAPO.IsInputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.WAVEFORMATEX_head),POINTER(win32more.Media.Audio.WAVEFORMATEX_head),POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)), use_last_error=False)(4, 'IsInputFormatSupported', ((1, 'pOutputFormat'),(1, 'pRequestedInputFormat'),(1, 'ppSupportedInputFormat'),)))
    IXAPO.IsOutputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.WAVEFORMATEX_head),POINTER(win32more.Media.Audio.WAVEFORMATEX_head),POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)), use_last_error=False)(5, 'IsOutputFormatSupported', ((1, 'pInputFormat'),(1, 'pRequestedOutputFormat'),(1, 'ppSupportedOutputFormat'),)))
    IXAPO.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32, use_last_error=False)(6, 'Initialize', ((1, 'pData'),(1, 'DataByteSize'),)))
    IXAPO.Reset = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(7, 'Reset', ()))
    IXAPO.LockForProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.XAudio2.XAPO_LOCKFORPROCESS_PARAMETERS),UInt32,POINTER(win32more.Media.Audio.XAudio2.XAPO_LOCKFORPROCESS_PARAMETERS), use_last_error=False)(8, 'LockForProcess', ((1, 'InputLockedParameterCount'),(1, 'pInputLockedParameters'),(1, 'OutputLockedParameterCount'),(1, 'pOutputLockedParameters'),)))
    IXAPO.UnlockForProcess = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(9, 'UnlockForProcess', ()))
    IXAPO.Process = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Media.Audio.XAudio2.XAPO_PROCESS_BUFFER_PARAMETERS),UInt32,POINTER(win32more.Media.Audio.XAudio2.XAPO_PROCESS_BUFFER_PARAMETERS),win32more.Foundation.BOOL, use_last_error=False)(10, 'Process', ((1, 'InputProcessParameterCount'),(1, 'pInputProcessParameters'),(1, 'OutputProcessParameterCount'),(1, 'pOutputProcessParameters'),(1, 'IsEnabled'),)))
    IXAPO.CalcInputFrames = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(11, 'CalcInputFrames', ((1, 'OutputFrameCount'),)))
    IXAPO.CalcOutputFrames = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(12, 'CalcOutputFrames', ((1, 'InputFrameCount'),)))
    win32more.System.Com.IUnknown
    return IXAPO
def _define_IXAPOParameters_head():
    class IXAPOParameters(win32more.System.Com.IUnknown_head):
        Guid = Guid('26d95c66-80f2-499a-ad54-5ae7f01c6d98')
    return IXAPOParameters
def _define_IXAPOParameters():
    IXAPOParameters = win32more.Media.Audio.XAudio2.IXAPOParameters_head
    IXAPOParameters.SetParameters = COMMETHOD(WINFUNCTYPE(Void,c_void_p,UInt32, use_last_error=False)(3, 'SetParameters', ((1, 'pParameters'),(1, 'ParameterByteSize'),)))
    IXAPOParameters.GetParameters = COMMETHOD(WINFUNCTYPE(Void,c_void_p,UInt32, use_last_error=False)(4, 'GetParameters', ((1, 'pParameters'),(1, 'ParameterByteSize'),)))
    win32more.System.Com.IUnknown
    return IXAPOParameters
FXEQ = Guid('f5e01117-d6c4-485a-a3f5-695196f3dbfa')
FXMasteringLimiter = Guid('c4137916-2be1-46fd-8599-441536f49856')
FXReverb = Guid('7d9aca56-cb68-4807-b632-b137352e8596')
FXEcho = Guid('5039d740-f736-449a-84d3-a56202557b87')
def _define_FXEQ_PARAMETERS_head():
    class FXEQ_PARAMETERS(Structure):
        pass
    return FXEQ_PARAMETERS
def _define_FXEQ_PARAMETERS():
    FXEQ_PARAMETERS = win32more.Media.Audio.XAudio2.FXEQ_PARAMETERS_head
    FXEQ_PARAMETERS._pack_ = 1
    FXEQ_PARAMETERS._fields_ = [
        ("FrequencyCenter0", Single),
        ("Gain0", Single),
        ("Bandwidth0", Single),
        ("FrequencyCenter1", Single),
        ("Gain1", Single),
        ("Bandwidth1", Single),
        ("FrequencyCenter2", Single),
        ("Gain2", Single),
        ("Bandwidth2", Single),
        ("FrequencyCenter3", Single),
        ("Gain3", Single),
        ("Bandwidth3", Single),
    ]
    return FXEQ_PARAMETERS
def _define_FXMASTERINGLIMITER_PARAMETERS_head():
    class FXMASTERINGLIMITER_PARAMETERS(Structure):
        pass
    return FXMASTERINGLIMITER_PARAMETERS
def _define_FXMASTERINGLIMITER_PARAMETERS():
    FXMASTERINGLIMITER_PARAMETERS = win32more.Media.Audio.XAudio2.FXMASTERINGLIMITER_PARAMETERS_head
    FXMASTERINGLIMITER_PARAMETERS._pack_ = 1
    FXMASTERINGLIMITER_PARAMETERS._fields_ = [
        ("Release", UInt32),
        ("Loudness", UInt32),
    ]
    return FXMASTERINGLIMITER_PARAMETERS
def _define_FXREVERB_PARAMETERS_head():
    class FXREVERB_PARAMETERS(Structure):
        pass
    return FXREVERB_PARAMETERS
def _define_FXREVERB_PARAMETERS():
    FXREVERB_PARAMETERS = win32more.Media.Audio.XAudio2.FXREVERB_PARAMETERS_head
    FXREVERB_PARAMETERS._pack_ = 1
    FXREVERB_PARAMETERS._fields_ = [
        ("Diffusion", Single),
        ("RoomSize", Single),
    ]
    return FXREVERB_PARAMETERS
def _define_FXECHO_INITDATA_head():
    class FXECHO_INITDATA(Structure):
        pass
    return FXECHO_INITDATA
def _define_FXECHO_INITDATA():
    FXECHO_INITDATA = win32more.Media.Audio.XAudio2.FXECHO_INITDATA_head
    FXECHO_INITDATA._pack_ = 1
    FXECHO_INITDATA._fields_ = [
        ("MaxDelay", Single),
    ]
    return FXECHO_INITDATA
def _define_FXECHO_PARAMETERS_head():
    class FXECHO_PARAMETERS(Structure):
        pass
    return FXECHO_PARAMETERS
def _define_FXECHO_PARAMETERS():
    FXECHO_PARAMETERS = win32more.Media.Audio.XAudio2.FXECHO_PARAMETERS_head
    FXECHO_PARAMETERS._pack_ = 1
    FXECHO_PARAMETERS._fields_ = [
        ("WetDryMix", Single),
        ("Feedback", Single),
        ("Delay", Single),
    ]
    return FXECHO_PARAMETERS
def _define_XAUDIO2_VOICE_DETAILS_head():
    class XAUDIO2_VOICE_DETAILS(Structure):
        pass
    return XAUDIO2_VOICE_DETAILS
def _define_XAUDIO2_VOICE_DETAILS():
    XAUDIO2_VOICE_DETAILS = win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_DETAILS_head
    XAUDIO2_VOICE_DETAILS._pack_ = 1
    XAUDIO2_VOICE_DETAILS._fields_ = [
        ("CreationFlags", UInt32),
        ("ActiveFlags", UInt32),
        ("InputChannels", UInt32),
        ("InputSampleRate", UInt32),
    ]
    return XAUDIO2_VOICE_DETAILS
def _define_XAUDIO2_SEND_DESCRIPTOR_head():
    class XAUDIO2_SEND_DESCRIPTOR(Structure):
        pass
    return XAUDIO2_SEND_DESCRIPTOR
def _define_XAUDIO2_SEND_DESCRIPTOR():
    XAUDIO2_SEND_DESCRIPTOR = win32more.Media.Audio.XAudio2.XAUDIO2_SEND_DESCRIPTOR_head
    XAUDIO2_SEND_DESCRIPTOR._pack_ = 1
    XAUDIO2_SEND_DESCRIPTOR._fields_ = [
        ("Flags", UInt32),
        ("pOutputVoice", win32more.Media.Audio.XAudio2.IXAudio2Voice_head),
    ]
    return XAUDIO2_SEND_DESCRIPTOR
def _define_XAUDIO2_VOICE_SENDS_head():
    class XAUDIO2_VOICE_SENDS(Structure):
        pass
    return XAUDIO2_VOICE_SENDS
def _define_XAUDIO2_VOICE_SENDS():
    XAUDIO2_VOICE_SENDS = win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS_head
    XAUDIO2_VOICE_SENDS._pack_ = 1
    XAUDIO2_VOICE_SENDS._fields_ = [
        ("SendCount", UInt32),
        ("pSends", POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_SEND_DESCRIPTOR_head)),
    ]
    return XAUDIO2_VOICE_SENDS
def _define_XAUDIO2_EFFECT_DESCRIPTOR_head():
    class XAUDIO2_EFFECT_DESCRIPTOR(Structure):
        pass
    return XAUDIO2_EFFECT_DESCRIPTOR
def _define_XAUDIO2_EFFECT_DESCRIPTOR():
    XAUDIO2_EFFECT_DESCRIPTOR = win32more.Media.Audio.XAudio2.XAUDIO2_EFFECT_DESCRIPTOR_head
    XAUDIO2_EFFECT_DESCRIPTOR._pack_ = 1
    XAUDIO2_EFFECT_DESCRIPTOR._fields_ = [
        ("pEffect", win32more.System.Com.IUnknown_head),
        ("InitialState", win32more.Foundation.BOOL),
        ("OutputChannels", UInt32),
    ]
    return XAUDIO2_EFFECT_DESCRIPTOR
def _define_XAUDIO2_EFFECT_CHAIN_head():
    class XAUDIO2_EFFECT_CHAIN(Structure):
        pass
    return XAUDIO2_EFFECT_CHAIN
def _define_XAUDIO2_EFFECT_CHAIN():
    XAUDIO2_EFFECT_CHAIN = win32more.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head
    XAUDIO2_EFFECT_CHAIN._pack_ = 1
    XAUDIO2_EFFECT_CHAIN._fields_ = [
        ("EffectCount", UInt32),
        ("pEffectDescriptors", POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_EFFECT_DESCRIPTOR_head)),
    ]
    return XAUDIO2_EFFECT_CHAIN
XAUDIO2_FILTER_TYPE = Int32
XAUDIO2_FILTER_TYPE_LowPassFilter = 0
XAUDIO2_FILTER_TYPE_BandPassFilter = 1
XAUDIO2_FILTER_TYPE_HighPassFilter = 2
XAUDIO2_FILTER_TYPE_NotchFilter = 3
XAUDIO2_FILTER_TYPE_LowPassOnePoleFilter = 4
XAUDIO2_FILTER_TYPE_HighPassOnePoleFilter = 5
def _define_XAUDIO2_FILTER_PARAMETERS_head():
    class XAUDIO2_FILTER_PARAMETERS(Structure):
        pass
    return XAUDIO2_FILTER_PARAMETERS
def _define_XAUDIO2_FILTER_PARAMETERS():
    XAUDIO2_FILTER_PARAMETERS = win32more.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head
    XAUDIO2_FILTER_PARAMETERS._pack_ = 1
    XAUDIO2_FILTER_PARAMETERS._fields_ = [
        ("Type", win32more.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE),
        ("Frequency", Single),
        ("OneOverQ", Single),
    ]
    return XAUDIO2_FILTER_PARAMETERS
def _define_XAUDIO2_BUFFER_head():
    class XAUDIO2_BUFFER(Structure):
        pass
    return XAUDIO2_BUFFER
def _define_XAUDIO2_BUFFER():
    XAUDIO2_BUFFER = win32more.Media.Audio.XAudio2.XAUDIO2_BUFFER_head
    XAUDIO2_BUFFER._pack_ = 1
    XAUDIO2_BUFFER._fields_ = [
        ("Flags", UInt32),
        ("AudioBytes", UInt32),
        ("pAudioData", c_char_p_no),
        ("PlayBegin", UInt32),
        ("PlayLength", UInt32),
        ("LoopBegin", UInt32),
        ("LoopLength", UInt32),
        ("LoopCount", UInt32),
        ("pContext", c_void_p),
    ]
    return XAUDIO2_BUFFER
def _define_XAUDIO2_BUFFER_WMA_head():
    class XAUDIO2_BUFFER_WMA(Structure):
        pass
    return XAUDIO2_BUFFER_WMA
def _define_XAUDIO2_BUFFER_WMA():
    XAUDIO2_BUFFER_WMA = win32more.Media.Audio.XAudio2.XAUDIO2_BUFFER_WMA_head
    XAUDIO2_BUFFER_WMA._pack_ = 1
    XAUDIO2_BUFFER_WMA._fields_ = [
        ("pDecodedPacketCumulativeBytes", POINTER(UInt32)),
        ("PacketCount", UInt32),
    ]
    return XAUDIO2_BUFFER_WMA
def _define_XAUDIO2_VOICE_STATE_head():
    class XAUDIO2_VOICE_STATE(Structure):
        pass
    return XAUDIO2_VOICE_STATE
def _define_XAUDIO2_VOICE_STATE():
    XAUDIO2_VOICE_STATE = win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_STATE_head
    XAUDIO2_VOICE_STATE._pack_ = 1
    XAUDIO2_VOICE_STATE._fields_ = [
        ("pCurrentBufferContext", c_void_p),
        ("BuffersQueued", UInt32),
        ("SamplesPlayed", UInt64),
    ]
    return XAUDIO2_VOICE_STATE
def _define_XAUDIO2_PERFORMANCE_DATA_head():
    class XAUDIO2_PERFORMANCE_DATA(Structure):
        pass
    return XAUDIO2_PERFORMANCE_DATA
def _define_XAUDIO2_PERFORMANCE_DATA():
    XAUDIO2_PERFORMANCE_DATA = win32more.Media.Audio.XAudio2.XAUDIO2_PERFORMANCE_DATA_head
    XAUDIO2_PERFORMANCE_DATA._pack_ = 1
    XAUDIO2_PERFORMANCE_DATA._fields_ = [
        ("AudioCyclesSinceLastQuery", UInt64),
        ("TotalCyclesSinceLastQuery", UInt64),
        ("MinimumCyclesPerQuantum", UInt32),
        ("MaximumCyclesPerQuantum", UInt32),
        ("MemoryUsageInBytes", UInt32),
        ("CurrentLatencyInSamples", UInt32),
        ("GlitchesSinceEngineStarted", UInt32),
        ("ActiveSourceVoiceCount", UInt32),
        ("TotalSourceVoiceCount", UInt32),
        ("ActiveSubmixVoiceCount", UInt32),
        ("ActiveResamplerCount", UInt32),
        ("ActiveMatrixMixCount", UInt32),
        ("ActiveXmaSourceVoices", UInt32),
        ("ActiveXmaStreams", UInt32),
    ]
    return XAUDIO2_PERFORMANCE_DATA
def _define_XAUDIO2_DEBUG_CONFIGURATION_head():
    class XAUDIO2_DEBUG_CONFIGURATION(Structure):
        pass
    return XAUDIO2_DEBUG_CONFIGURATION
def _define_XAUDIO2_DEBUG_CONFIGURATION():
    XAUDIO2_DEBUG_CONFIGURATION = win32more.Media.Audio.XAudio2.XAUDIO2_DEBUG_CONFIGURATION_head
    XAUDIO2_DEBUG_CONFIGURATION._pack_ = 1
    XAUDIO2_DEBUG_CONFIGURATION._fields_ = [
        ("TraceMask", UInt32),
        ("BreakMask", UInt32),
        ("LogThreadID", win32more.Foundation.BOOL),
        ("LogFileline", win32more.Foundation.BOOL),
        ("LogFunctionName", win32more.Foundation.BOOL),
        ("LogTiming", win32more.Foundation.BOOL),
    ]
    return XAUDIO2_DEBUG_CONFIGURATION
def _define_IXAudio2_head():
    class IXAudio2(win32more.System.Com.IUnknown_head):
        Guid = Guid('2b02e3cf-2e0b-4ec3-be45-1b2a3fe7210d')
    return IXAudio2
def _define_IXAudio2():
    IXAudio2 = win32more.Media.Audio.XAudio2.IXAudio2_head
    IXAudio2.RegisterForCallbacks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.XAudio2.IXAudio2EngineCallback_head, use_last_error=False)(3, 'RegisterForCallbacks', ((1, 'pCallback'),)))
    IXAudio2.UnregisterForCallbacks = COMMETHOD(WINFUNCTYPE(Void,win32more.Media.Audio.XAudio2.IXAudio2EngineCallback_head, use_last_error=False)(4, 'UnregisterForCallbacks', ((1, 'pCallback'),)))
    IXAudio2.CreateSourceVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.IXAudio2SourceVoice_head),POINTER(win32more.Media.Audio.WAVEFORMATEX_head),UInt32,Single,win32more.Media.Audio.XAudio2.IXAudio2VoiceCallback_head,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS_head),POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head), use_last_error=False)(5, 'CreateSourceVoice', ((1, 'ppSourceVoice'),(1, 'pSourceFormat'),(1, 'Flags'),(1, 'MaxFrequencyRatio'),(1, 'pCallback'),(1, 'pSendList'),(1, 'pEffectChain'),)))
    IXAudio2.CreateSubmixVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.IXAudio2SubmixVoice_head),UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS_head),POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head), use_last_error=False)(6, 'CreateSubmixVoice', ((1, 'ppSubmixVoice'),(1, 'InputChannels'),(1, 'InputSampleRate'),(1, 'Flags'),(1, 'ProcessingStage'),(1, 'pSendList'),(1, 'pEffectChain'),)))
    IXAudio2.CreateMasteringVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.IXAudio2MasteringVoice_head),UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head),win32more.Media.Audio.AUDIO_STREAM_CATEGORY, use_last_error=False)(7, 'CreateMasteringVoice', ((1, 'ppMasteringVoice'),(1, 'InputChannels'),(1, 'InputSampleRate'),(1, 'Flags'),(1, 'szDeviceId'),(1, 'pEffectChain'),(1, 'StreamCategory'),)))
    IXAudio2.StartEngine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'StartEngine', ()))
    IXAudio2.StopEngine = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(9, 'StopEngine', ()))
    IXAudio2.CommitChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'CommitChanges', ((1, 'OperationSet'),)))
    IXAudio2.GetPerformanceData = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_PERFORMANCE_DATA_head), use_last_error=False)(11, 'GetPerformanceData', ((1, 'pPerfData'),)))
    IXAudio2.SetDebugConfiguration = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_DEBUG_CONFIGURATION_head),c_void_p, use_last_error=False)(12, 'SetDebugConfiguration', ((1, 'pDebugConfiguration'),(1, 'pReserved'),)))
    win32more.System.Com.IUnknown
    return IXAudio2
def _define_IXAudio2Extension_head():
    class IXAudio2Extension(win32more.System.Com.IUnknown_head):
        Guid = Guid('84ac29bb-d619-44d2-b197-e4acf7df3ed6')
    return IXAudio2Extension
def _define_IXAudio2Extension():
    IXAudio2Extension = win32more.Media.Audio.XAudio2.IXAudio2Extension_head
    IXAudio2Extension.GetProcessingQuantum = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetProcessingQuantum', ((1, 'quantumNumerator'),(1, 'quantumDenominator'),)))
    IXAudio2Extension.GetProcessor = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt32), use_last_error=False)(4, 'GetProcessor', ((1, 'processor'),)))
    win32more.System.Com.IUnknown
    return IXAudio2Extension
def _define_IXAudio2Voice_head():
    class IXAudio2Voice(c_void_p):
        Guid = Guid(None)
    return IXAudio2Voice
def _define_IXAudio2Voice():
    IXAudio2Voice = win32more.Media.Audio.XAudio2.IXAudio2Voice_head
    IXAudio2Voice.GetVoiceDetails = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_DETAILS_head), use_last_error=False)(0, 'GetVoiceDetails', ((1, 'pVoiceDetails'),)))
    IXAudio2Voice.SetOutputVoices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS_head), use_last_error=False)(1, 'SetOutputVoices', ((1, 'pSendList'),)))
    IXAudio2Voice.SetEffectChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head), use_last_error=False)(2, 'SetEffectChain', ((1, 'pEffectChain'),)))
    IXAudio2Voice.EnableEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(3, 'EnableEffect', ((1, 'EffectIndex'),(1, 'OperationSet'),)))
    IXAudio2Voice.DisableEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'DisableEffect', ((1, 'EffectIndex'),(1, 'OperationSet'),)))
    IXAudio2Voice.GetEffectState = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'GetEffectState', ((1, 'EffectIndex'),(1, 'pEnabled'),)))
    IXAudio2Voice.SetEffectParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(6, 'SetEffectParameters', ((1, 'EffectIndex'),(1, 'pParameters'),(1, 'ParametersByteSize'),(1, 'OperationSet'),)))
    IXAudio2Voice.GetEffectParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32, use_last_error=False)(7, 'GetEffectParameters', ((1, 'EffectIndex'),(1, 'pParameters'),(1, 'ParametersByteSize'),)))
    IXAudio2Voice.SetFilterParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head),UInt32, use_last_error=False)(8, 'SetFilterParameters', ((1, 'pParameters'),(1, 'OperationSet'),)))
    IXAudio2Voice.GetFilterParameters = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head), use_last_error=False)(9, 'GetFilterParameters', ((1, 'pParameters'),)))
    IXAudio2Voice.SetOutputFilterParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.XAudio2.IXAudio2Voice_head,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head),UInt32, use_last_error=False)(10, 'SetOutputFilterParameters', ((1, 'pDestinationVoice'),(1, 'pParameters'),(1, 'OperationSet'),)))
    IXAudio2Voice.GetOutputFilterParameters = COMMETHOD(WINFUNCTYPE(Void,win32more.Media.Audio.XAudio2.IXAudio2Voice_head,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head), use_last_error=False)(11, 'GetOutputFilterParameters', ((1, 'pDestinationVoice'),(1, 'pParameters'),)))
    IXAudio2Voice.SetVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32, use_last_error=False)(12, 'SetVolume', ((1, 'Volume'),(1, 'OperationSet'),)))
    IXAudio2Voice.GetVolume = COMMETHOD(WINFUNCTYPE(Void,POINTER(Single), use_last_error=False)(13, 'GetVolume', ((1, 'pVolume'),)))
    IXAudio2Voice.SetChannelVolumes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single),UInt32, use_last_error=False)(14, 'SetChannelVolumes', ((1, 'Channels'),(1, 'pVolumes'),(1, 'OperationSet'),)))
    IXAudio2Voice.GetChannelVolumes = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(Single), use_last_error=False)(15, 'GetChannelVolumes', ((1, 'Channels'),(1, 'pVolumes'),)))
    IXAudio2Voice.SetOutputMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.XAudio2.IXAudio2Voice_head,UInt32,UInt32,POINTER(Single),UInt32, use_last_error=False)(16, 'SetOutputMatrix', ((1, 'pDestinationVoice'),(1, 'SourceChannels'),(1, 'DestinationChannels'),(1, 'pLevelMatrix'),(1, 'OperationSet'),)))
    IXAudio2Voice.GetOutputMatrix = COMMETHOD(WINFUNCTYPE(Void,win32more.Media.Audio.XAudio2.IXAudio2Voice_head,UInt32,UInt32,POINTER(Single), use_last_error=False)(17, 'GetOutputMatrix', ((1, 'pDestinationVoice'),(1, 'SourceChannels'),(1, 'DestinationChannels'),(1, 'pLevelMatrix'),)))
    IXAudio2Voice.DestroyVoice = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(18, 'DestroyVoice', ()))
    return IXAudio2Voice
def _define_IXAudio2SourceVoice_head():
    class IXAudio2SourceVoice(win32more.Media.Audio.XAudio2.IXAudio2Voice_head):
        Guid = Guid(None)
    return IXAudio2SourceVoice
def _define_IXAudio2SourceVoice():
    IXAudio2SourceVoice = win32more.Media.Audio.XAudio2.IXAudio2SourceVoice_head
    IXAudio2SourceVoice.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(19, 'Start', ((1, 'Flags'),(1, 'OperationSet'),)))
    IXAudio2SourceVoice.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(20, 'Stop', ((1, 'Flags'),(1, 'OperationSet'),)))
    IXAudio2SourceVoice.SubmitSourceBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_BUFFER_head),POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_BUFFER_WMA_head), use_last_error=False)(21, 'SubmitSourceBuffer', ((1, 'pBuffer'),(1, 'pBufferWMA'),)))
    IXAudio2SourceVoice.FlushSourceBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'FlushSourceBuffers', ()))
    IXAudio2SourceVoice.Discontinuity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Discontinuity', ()))
    IXAudio2SourceVoice.ExitLoop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(24, 'ExitLoop', ((1, 'OperationSet'),)))
    IXAudio2SourceVoice.GetState = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.XAudio2.XAUDIO2_VOICE_STATE_head),UInt32, use_last_error=False)(25, 'GetState', ((1, 'pVoiceState'),(1, 'Flags'),)))
    IXAudio2SourceVoice.SetFrequencyRatio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32, use_last_error=False)(26, 'SetFrequencyRatio', ((1, 'Ratio'),(1, 'OperationSet'),)))
    IXAudio2SourceVoice.GetFrequencyRatio = COMMETHOD(WINFUNCTYPE(Void,POINTER(Single), use_last_error=False)(27, 'GetFrequencyRatio', ((1, 'pRatio'),)))
    IXAudio2SourceVoice.SetSourceSampleRate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(28, 'SetSourceSampleRate', ((1, 'NewSourceSampleRate'),)))
    win32more.Media.Audio.XAudio2.IXAudio2Voice
    return IXAudio2SourceVoice
def _define_IXAudio2SubmixVoice_head():
    class IXAudio2SubmixVoice(win32more.Media.Audio.XAudio2.IXAudio2Voice_head):
        Guid = Guid(None)
    return IXAudio2SubmixVoice
def _define_IXAudio2SubmixVoice():
    IXAudio2SubmixVoice = win32more.Media.Audio.XAudio2.IXAudio2SubmixVoice_head
    win32more.Media.Audio.XAudio2.IXAudio2Voice
    return IXAudio2SubmixVoice
def _define_IXAudio2MasteringVoice_head():
    class IXAudio2MasteringVoice(win32more.Media.Audio.XAudio2.IXAudio2Voice_head):
        Guid = Guid(None)
    return IXAudio2MasteringVoice
def _define_IXAudio2MasteringVoice():
    IXAudio2MasteringVoice = win32more.Media.Audio.XAudio2.IXAudio2MasteringVoice_head
    IXAudio2MasteringVoice.GetChannelMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(19, 'GetChannelMask', ((1, 'pChannelmask'),)))
    win32more.Media.Audio.XAudio2.IXAudio2Voice
    return IXAudio2MasteringVoice
def _define_IXAudio2EngineCallback_head():
    class IXAudio2EngineCallback(c_void_p):
        Guid = Guid(None)
    return IXAudio2EngineCallback
def _define_IXAudio2EngineCallback():
    IXAudio2EngineCallback = win32more.Media.Audio.XAudio2.IXAudio2EngineCallback_head
    IXAudio2EngineCallback.OnProcessingPassStart = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(0, 'OnProcessingPassStart', ()))
    IXAudio2EngineCallback.OnProcessingPassEnd = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(1, 'OnProcessingPassEnd', ()))
    IXAudio2EngineCallback.OnCriticalError = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.HRESULT, use_last_error=False)(2, 'OnCriticalError', ((1, 'Error'),)))
    return IXAudio2EngineCallback
def _define_IXAudio2VoiceCallback_head():
    class IXAudio2VoiceCallback(c_void_p):
        Guid = Guid(None)
    return IXAudio2VoiceCallback
def _define_IXAudio2VoiceCallback():
    IXAudio2VoiceCallback = win32more.Media.Audio.XAudio2.IXAudio2VoiceCallback_head
    IXAudio2VoiceCallback.OnVoiceProcessingPassStart = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(0, 'OnVoiceProcessingPassStart', ((1, 'BytesRequired'),)))
    IXAudio2VoiceCallback.OnVoiceProcessingPassEnd = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(1, 'OnVoiceProcessingPassEnd', ()))
    IXAudio2VoiceCallback.OnStreamEnd = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(2, 'OnStreamEnd', ()))
    IXAudio2VoiceCallback.OnBufferStart = COMMETHOD(WINFUNCTYPE(Void,c_void_p, use_last_error=False)(3, 'OnBufferStart', ((1, 'pBufferContext'),)))
    IXAudio2VoiceCallback.OnBufferEnd = COMMETHOD(WINFUNCTYPE(Void,c_void_p, use_last_error=False)(4, 'OnBufferEnd', ((1, 'pBufferContext'),)))
    IXAudio2VoiceCallback.OnLoopEnd = COMMETHOD(WINFUNCTYPE(Void,c_void_p, use_last_error=False)(5, 'OnLoopEnd', ((1, 'pBufferContext'),)))
    IXAudio2VoiceCallback.OnVoiceError = COMMETHOD(WINFUNCTYPE(Void,c_void_p,win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnVoiceError', ((1, 'pBufferContext'),(1, 'Error'),)))
    return IXAudio2VoiceCallback
AudioVolumeMeter = Guid('4fc3b166-972a-40cf-bc37-7db03db2fba3')
AudioReverb = Guid('c2633b16-471b-4498-b8c5-4f0959e2ec09')
def _define_XAUDIO2FX_VOLUMEMETER_LEVELS_head():
    class XAUDIO2FX_VOLUMEMETER_LEVELS(Structure):
        pass
    return XAUDIO2FX_VOLUMEMETER_LEVELS
def _define_XAUDIO2FX_VOLUMEMETER_LEVELS():
    XAUDIO2FX_VOLUMEMETER_LEVELS = win32more.Media.Audio.XAudio2.XAUDIO2FX_VOLUMEMETER_LEVELS_head
    XAUDIO2FX_VOLUMEMETER_LEVELS._pack_ = 1
    XAUDIO2FX_VOLUMEMETER_LEVELS._fields_ = [
        ("pPeakLevels", POINTER(Single)),
        ("pRMSLevels", POINTER(Single)),
        ("ChannelCount", UInt32),
    ]
    return XAUDIO2FX_VOLUMEMETER_LEVELS
def _define_XAUDIO2FX_REVERB_PARAMETERS_head():
    class XAUDIO2FX_REVERB_PARAMETERS(Structure):
        pass
    return XAUDIO2FX_REVERB_PARAMETERS
def _define_XAUDIO2FX_REVERB_PARAMETERS():
    XAUDIO2FX_REVERB_PARAMETERS = win32more.Media.Audio.XAudio2.XAUDIO2FX_REVERB_PARAMETERS_head
    XAUDIO2FX_REVERB_PARAMETERS._pack_ = 1
    XAUDIO2FX_REVERB_PARAMETERS._fields_ = [
        ("WetDryMix", Single),
        ("ReflectionsDelay", UInt32),
        ("ReverbDelay", Byte),
        ("RearDelay", Byte),
        ("SideDelay", Byte),
        ("PositionLeft", Byte),
        ("PositionRight", Byte),
        ("PositionMatrixLeft", Byte),
        ("PositionMatrixRight", Byte),
        ("EarlyDiffusion", Byte),
        ("LateDiffusion", Byte),
        ("LowEQGain", Byte),
        ("LowEQCutoff", Byte),
        ("HighEQGain", Byte),
        ("HighEQCutoff", Byte),
        ("RoomFilterFreq", Single),
        ("RoomFilterMain", Single),
        ("RoomFilterHF", Single),
        ("ReflectionsGain", Single),
        ("ReverbGain", Single),
        ("DecayTime", Single),
        ("Density", Single),
        ("RoomSize", Single),
        ("DisableLateField", win32more.Foundation.BOOL),
    ]
    return XAUDIO2FX_REVERB_PARAMETERS
def _define_XAUDIO2FX_REVERB_I3DL2_PARAMETERS_head():
    class XAUDIO2FX_REVERB_I3DL2_PARAMETERS(Structure):
        pass
    return XAUDIO2FX_REVERB_I3DL2_PARAMETERS
def _define_XAUDIO2FX_REVERB_I3DL2_PARAMETERS():
    XAUDIO2FX_REVERB_I3DL2_PARAMETERS = win32more.Media.Audio.XAudio2.XAUDIO2FX_REVERB_I3DL2_PARAMETERS_head
    XAUDIO2FX_REVERB_I3DL2_PARAMETERS._pack_ = 1
    XAUDIO2FX_REVERB_I3DL2_PARAMETERS._fields_ = [
        ("WetDryMix", Single),
        ("Room", Int32),
        ("RoomHF", Int32),
        ("RoomRolloffFactor", Single),
        ("DecayTime", Single),
        ("DecayHFRatio", Single),
        ("Reflections", Int32),
        ("ReflectionsDelay", Single),
        ("Reverb", Int32),
        ("ReverbDelay", Single),
        ("Diffusion", Single),
        ("Density", Single),
        ("HFReference", Single),
    ]
    return XAUDIO2FX_REVERB_I3DL2_PARAMETERS
def _define_HrtfPosition_head():
    class HrtfPosition(Structure):
        pass
    return HrtfPosition
def _define_HrtfPosition():
    HrtfPosition = win32more.Media.Audio.XAudio2.HrtfPosition_head
    HrtfPosition._fields_ = [
        ("x", Single),
        ("y", Single),
        ("z", Single),
    ]
    return HrtfPosition
def _define_HrtfOrientation_head():
    class HrtfOrientation(Structure):
        pass
    return HrtfOrientation
def _define_HrtfOrientation():
    HrtfOrientation = win32more.Media.Audio.XAudio2.HrtfOrientation_head
    HrtfOrientation._fields_ = [
        ("element", Single * 9),
    ]
    return HrtfOrientation
HrtfDirectivityType = Int32
HrtfDirectivityType_OmniDirectional = 0
HrtfDirectivityType_Cardioid = 1
HrtfDirectivityType_Cone = 2
HrtfEnvironment = Int32
HrtfEnvironment_Small = 0
HrtfEnvironment_Medium = 1
HrtfEnvironment_Large = 2
HrtfEnvironment_Outdoors = 3
def _define_HrtfDirectivity_head():
    class HrtfDirectivity(Structure):
        pass
    return HrtfDirectivity
def _define_HrtfDirectivity():
    HrtfDirectivity = win32more.Media.Audio.XAudio2.HrtfDirectivity_head
    HrtfDirectivity._fields_ = [
        ("type", win32more.Media.Audio.XAudio2.HrtfDirectivityType),
        ("scaling", Single),
    ]
    return HrtfDirectivity
def _define_HrtfDirectivityCardioid_head():
    class HrtfDirectivityCardioid(Structure):
        pass
    return HrtfDirectivityCardioid
def _define_HrtfDirectivityCardioid():
    HrtfDirectivityCardioid = win32more.Media.Audio.XAudio2.HrtfDirectivityCardioid_head
    HrtfDirectivityCardioid._fields_ = [
        ("directivity", win32more.Media.Audio.XAudio2.HrtfDirectivity),
        ("order", Single),
    ]
    return HrtfDirectivityCardioid
def _define_HrtfDirectivityCone_head():
    class HrtfDirectivityCone(Structure):
        pass
    return HrtfDirectivityCone
def _define_HrtfDirectivityCone():
    HrtfDirectivityCone = win32more.Media.Audio.XAudio2.HrtfDirectivityCone_head
    HrtfDirectivityCone._fields_ = [
        ("directivity", win32more.Media.Audio.XAudio2.HrtfDirectivity),
        ("innerAngle", Single),
        ("outerAngle", Single),
    ]
    return HrtfDirectivityCone
HrtfDistanceDecayType = Int32
HrtfDistanceDecayType_NaturalDecay = 0
HrtfDistanceDecayType_CustomDecay = 1
def _define_HrtfDistanceDecay_head():
    class HrtfDistanceDecay(Structure):
        pass
    return HrtfDistanceDecay
def _define_HrtfDistanceDecay():
    HrtfDistanceDecay = win32more.Media.Audio.XAudio2.HrtfDistanceDecay_head
    HrtfDistanceDecay._fields_ = [
        ("type", win32more.Media.Audio.XAudio2.HrtfDistanceDecayType),
        ("maxGain", Single),
        ("minGain", Single),
        ("unityGainDistance", Single),
        ("cutoffDistance", Single),
    ]
    return HrtfDistanceDecay
def _define_HrtfApoInit_head():
    class HrtfApoInit(Structure):
        pass
    return HrtfApoInit
def _define_HrtfApoInit():
    HrtfApoInit = win32more.Media.Audio.XAudio2.HrtfApoInit_head
    HrtfApoInit._fields_ = [
        ("distanceDecay", POINTER(win32more.Media.Audio.XAudio2.HrtfDistanceDecay_head)),
        ("directivity", POINTER(win32more.Media.Audio.XAudio2.HrtfDirectivity_head)),
    ]
    return HrtfApoInit
def _define_IXAPOHrtfParameters_head():
    class IXAPOHrtfParameters(win32more.System.Com.IUnknown_head):
        Guid = Guid('15b3cd66-e9de-4464-b6e6-2bc3cf63d455')
    return IXAPOHrtfParameters
def _define_IXAPOHrtfParameters():
    IXAPOHrtfParameters = win32more.Media.Audio.XAudio2.IXAPOHrtfParameters_head
    IXAPOHrtfParameters.SetSourcePosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.HrtfPosition_head), use_last_error=False)(3, 'SetSourcePosition', ((1, 'position'),)))
    IXAPOHrtfParameters.SetSourceOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.HrtfOrientation_head), use_last_error=False)(4, 'SetSourceOrientation', ((1, 'orientation'),)))
    IXAPOHrtfParameters.SetSourceGain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(5, 'SetSourceGain', ((1, 'gain'),)))
    IXAPOHrtfParameters.SetEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.XAudio2.HrtfEnvironment, use_last_error=False)(6, 'SetEnvironment', ((1, 'environment'),)))
    win32more.System.Com.IUnknown
    return IXAPOHrtfParameters
def _define_CreateFX():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head),c_void_p,UInt32, use_last_error=False)(("CreateFX", windll["XAudio2_8"]), ((1, 'clsid'),(1, 'pEffect'),(1, 'pInitDat'),(1, 'InitDataByteSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XAudio2CreateWithVersionInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.IXAudio2_head),UInt32,UInt32,UInt32, use_last_error=False)(("XAudio2CreateWithVersionInfo", windll["XAudio2_8"]), ((1, 'ppXAudio2'),(1, 'Flags'),(1, 'XAudio2Processor'),(1, 'ntddiVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAudioVolumeMeter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("CreateAudioVolumeMeter", windll["XAudio2_8"]), ((1, 'ppApo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAudioReverb():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("CreateAudioReverb", windll["XAudio2_8"]), ((1, 'ppApo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateHrtfApo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.XAudio2.HrtfApoInit_head),POINTER(win32more.Media.Audio.XAudio2.IXAPO_head), use_last_error=False)(("CreateHrtfApo", windll["HrtfApo"]), ((1, 'init'),(1, 'xApo'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "FXEQ_MIN_FRAMERATE",
    "FXEQ_MAX_FRAMERATE",
    "FXEQ_MIN_FREQUENCY_CENTER",
    "FXEQ_MAX_FREQUENCY_CENTER",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_0",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_1",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_2",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_3",
    "FXEQ_MIN_GAIN",
    "FXEQ_MAX_GAIN",
    "FXEQ_DEFAULT_GAIN",
    "FXEQ_MIN_BANDWIDTH",
    "FXEQ_MAX_BANDWIDTH",
    "FXEQ_DEFAULT_BANDWIDTH",
    "FXMASTERINGLIMITER_MIN_RELEASE",
    "FXMASTERINGLIMITER_MAX_RELEASE",
    "FXMASTERINGLIMITER_DEFAULT_RELEASE",
    "FXMASTERINGLIMITER_MIN_LOUDNESS",
    "FXMASTERINGLIMITER_MAX_LOUDNESS",
    "FXMASTERINGLIMITER_DEFAULT_LOUDNESS",
    "FXREVERB_MIN_DIFFUSION",
    "FXREVERB_MAX_DIFFUSION",
    "FXREVERB_DEFAULT_DIFFUSION",
    "FXREVERB_MIN_ROOMSIZE",
    "FXREVERB_MAX_ROOMSIZE",
    "FXREVERB_DEFAULT_ROOMSIZE",
    "FXLOUDNESS_DEFAULT_MOMENTARY_MS",
    "FXLOUDNESS_DEFAULT_SHORTTERM_MS",
    "FXECHO_MIN_WETDRYMIX",
    "FXECHO_MAX_WETDRYMIX",
    "FXECHO_DEFAULT_WETDRYMIX",
    "FXECHO_MIN_FEEDBACK",
    "FXECHO_MAX_FEEDBACK",
    "FXECHO_DEFAULT_FEEDBACK",
    "FXECHO_MIN_DELAY",
    "FXECHO_MAX_DELAY",
    "FXECHO_DEFAULT_DELAY",
    "XAUDIO2_MAX_BUFFER_BYTES",
    "XAUDIO2_MAX_QUEUED_BUFFERS",
    "XAUDIO2_MAX_BUFFERS_SYSTEM",
    "XAUDIO2_MAX_AUDIO_CHANNELS",
    "XAUDIO2_MIN_SAMPLE_RATE",
    "XAUDIO2_MAX_SAMPLE_RATE",
    "XAUDIO2_MAX_VOLUME_LEVEL",
    "XAUDIO2_MAX_FREQ_RATIO",
    "XAUDIO2_DEFAULT_FREQ_RATIO",
    "XAUDIO2_MAX_FILTER_ONEOVERQ",
    "XAUDIO2_MAX_FILTER_FREQUENCY",
    "XAUDIO2_MAX_LOOP_COUNT",
    "XAUDIO2_MAX_INSTANCES",
    "XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MONO",
    "XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MULTICHANNEL",
    "XAUDIO2_COMMIT_NOW",
    "XAUDIO2_COMMIT_ALL",
    "XAUDIO2_NO_LOOP_REGION",
    "XAUDIO2_LOOP_INFINITE",
    "XAUDIO2_DEFAULT_CHANNELS",
    "XAUDIO2_DEFAULT_SAMPLERATE",
    "XAUDIO2_DEBUG_ENGINE",
    "XAUDIO2_VOICE_NOPITCH",
    "XAUDIO2_VOICE_NOSRC",
    "XAUDIO2_VOICE_USEFILTER",
    "XAUDIO2_PLAY_TAILS",
    "XAUDIO2_END_OF_STREAM",
    "XAUDIO2_SEND_USEFILTER",
    "XAUDIO2_VOICE_NOSAMPLESPLAYED",
    "XAUDIO2_STOP_ENGINE_WHEN_IDLE",
    "XAUDIO2_1024_QUANTUM",
    "XAUDIO2_NO_VIRTUAL_AUDIO_CLIENT",
    "XAUDIO2_DEFAULT_FILTER_FREQUENCY",
    "XAUDIO2_DEFAULT_FILTER_ONEOVERQ",
    "XAUDIO2_QUANTUM_NUMERATOR",
    "XAUDIO2_QUANTUM_DENOMINATOR",
    "FACILITY_XAUDIO2",
    "XAUDIO2_E_INVALID_CALL",
    "XAUDIO2_E_XMA_DECODER_ERROR",
    "XAUDIO2_E_XAPO_CREATION_FAILED",
    "XAUDIO2_E_DEVICE_INVALIDATED",
    "Processor1",
    "Processor2",
    "Processor3",
    "Processor4",
    "Processor5",
    "Processor6",
    "Processor7",
    "Processor8",
    "Processor9",
    "Processor10",
    "Processor11",
    "Processor12",
    "Processor13",
    "Processor14",
    "Processor15",
    "Processor16",
    "Processor17",
    "Processor18",
    "Processor19",
    "Processor20",
    "Processor21",
    "Processor22",
    "Processor23",
    "Processor24",
    "Processor25",
    "Processor26",
    "Processor27",
    "Processor28",
    "Processor29",
    "Processor30",
    "Processor31",
    "Processor32",
    "XAUDIO2_ANY_PROCESSOR",
    "XAUDIO2_USE_DEFAULT_PROCESSOR",
    "XAUDIO2_DEFAULT_PROCESSOR",
    "XAUDIO2_LOG_ERRORS",
    "XAUDIO2_LOG_WARNINGS",
    "XAUDIO2_LOG_INFO",
    "XAUDIO2_LOG_DETAIL",
    "XAUDIO2_LOG_API_CALLS",
    "XAUDIO2_LOG_FUNC_CALLS",
    "XAUDIO2_LOG_TIMING",
    "XAUDIO2_LOG_LOCKS",
    "XAUDIO2_LOG_MEMORY",
    "XAUDIO2_LOG_STREAMING",
    "XAUDIO2FX_REVERB_MIN_FRAMERATE",
    "XAUDIO2FX_REVERB_MAX_FRAMERATE",
    "XAUDIO2FX_REVERB_MIN_WET_DRY_MIX",
    "XAUDIO2FX_REVERB_MIN_REFLECTIONS_DELAY",
    "XAUDIO2FX_REVERB_MIN_REVERB_DELAY",
    "XAUDIO2FX_REVERB_MIN_REAR_DELAY",
    "XAUDIO2FX_REVERB_MIN_7POINT1_SIDE_DELAY",
    "XAUDIO2FX_REVERB_MIN_7POINT1_REAR_DELAY",
    "XAUDIO2FX_REVERB_MIN_POSITION",
    "XAUDIO2FX_REVERB_MIN_DIFFUSION",
    "XAUDIO2FX_REVERB_MIN_LOW_EQ_GAIN",
    "XAUDIO2FX_REVERB_MIN_LOW_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MIN_HIGH_EQ_GAIN",
    "XAUDIO2FX_REVERB_MIN_HIGH_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MIN_ROOM_FILTER_FREQ",
    "XAUDIO2FX_REVERB_MIN_ROOM_FILTER_MAIN",
    "XAUDIO2FX_REVERB_MIN_ROOM_FILTER_HF",
    "XAUDIO2FX_REVERB_MIN_REFLECTIONS_GAIN",
    "XAUDIO2FX_REVERB_MIN_REVERB_GAIN",
    "XAUDIO2FX_REVERB_MIN_DECAY_TIME",
    "XAUDIO2FX_REVERB_MIN_DENSITY",
    "XAUDIO2FX_REVERB_MIN_ROOM_SIZE",
    "XAUDIO2FX_REVERB_MAX_WET_DRY_MIX",
    "XAUDIO2FX_REVERB_MAX_REFLECTIONS_DELAY",
    "XAUDIO2FX_REVERB_MAX_REVERB_DELAY",
    "XAUDIO2FX_REVERB_MAX_REAR_DELAY",
    "XAUDIO2FX_REVERB_MAX_7POINT1_SIDE_DELAY",
    "XAUDIO2FX_REVERB_MAX_7POINT1_REAR_DELAY",
    "XAUDIO2FX_REVERB_MAX_POSITION",
    "XAUDIO2FX_REVERB_MAX_DIFFUSION",
    "XAUDIO2FX_REVERB_MAX_LOW_EQ_GAIN",
    "XAUDIO2FX_REVERB_MAX_LOW_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MAX_HIGH_EQ_GAIN",
    "XAUDIO2FX_REVERB_MAX_HIGH_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MAX_ROOM_FILTER_FREQ",
    "XAUDIO2FX_REVERB_MAX_ROOM_FILTER_MAIN",
    "XAUDIO2FX_REVERB_MAX_ROOM_FILTER_HF",
    "XAUDIO2FX_REVERB_MAX_REFLECTIONS_GAIN",
    "XAUDIO2FX_REVERB_MAX_REVERB_GAIN",
    "XAUDIO2FX_REVERB_MAX_DENSITY",
    "XAUDIO2FX_REVERB_MAX_ROOM_SIZE",
    "XAUDIO2FX_REVERB_DEFAULT_WET_DRY_MIX",
    "XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_REVERB_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_REAR_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_7POINT1_SIDE_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_7POINT1_REAR_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_POSITION",
    "XAUDIO2FX_REVERB_DEFAULT_POSITION_MATRIX",
    "XAUDIO2FX_REVERB_DEFAULT_EARLY_DIFFUSION",
    "XAUDIO2FX_REVERB_DEFAULT_LATE_DIFFUSION",
    "XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_FREQ",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_MAIN",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_HF",
    "XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_REVERB_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_DECAY_TIME",
    "XAUDIO2FX_REVERB_DEFAULT_DENSITY",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_SIZE",
    "XAUDIO2FX_REVERB_DEFAULT_DISABLE_LATE_FIELD",
    "HRTF_MAX_GAIN_LIMIT",
    "HRTF_MIN_GAIN_LIMIT",
    "HRTF_MIN_UNITY_GAIN_DISTANCE",
    "HRTF_DEFAULT_UNITY_GAIN_DISTANCE",
    "FACILITY_XAPO",
    "XAPO_E_FORMAT_UNSUPPORTED",
    "XAPO_MIN_CHANNELS",
    "XAPO_MAX_CHANNELS",
    "XAPO_MIN_FRAMERATE",
    "XAPO_MAX_FRAMERATE",
    "XAPO_REGISTRATION_STRING_LENGTH",
    "XAPO_FLAG_CHANNELS_MUST_MATCH",
    "XAPO_FLAG_FRAMERATE_MUST_MATCH",
    "XAPO_FLAG_BITSPERSAMPLE_MUST_MATCH",
    "XAPO_FLAG_BUFFERCOUNT_MUST_MATCH",
    "XAPO_FLAG_INPLACE_REQUIRED",
    "XAPO_FLAG_INPLACE_SUPPORTED",
    "SPEAKER_MONO",
    "X3DAUDIO_HANDLE_BYTESIZE",
    "X3DAUDIO_PI",
    "X3DAUDIO_2PI",
    "X3DAUDIO_SPEED_OF_SOUND",
    "X3DAUDIO_CALCULATE_MATRIX",
    "X3DAUDIO_CALCULATE_DELAY",
    "X3DAUDIO_CALCULATE_LPF_DIRECT",
    "X3DAUDIO_CALCULATE_LPF_REVERB",
    "X3DAUDIO_CALCULATE_REVERB",
    "X3DAUDIO_CALCULATE_DOPPLER",
    "X3DAUDIO_CALCULATE_EMITTER_ANGLE",
    "X3DAUDIO_CALCULATE_ZEROCENTER",
    "X3DAUDIO_CALCULATE_REDIRECT_TO_LFE",
    "XAPO_REGISTRATION_PROPERTIES",
    "XAPO_LOCKFORPROCESS_PARAMETERS",
    "XAPO_BUFFER_FLAGS",
    "XAPO_BUFFER_SILENT",
    "XAPO_BUFFER_VALID",
    "XAPO_PROCESS_BUFFER_PARAMETERS",
    "IXAPO",
    "IXAPOParameters",
    "FXEQ",
    "FXMasteringLimiter",
    "FXReverb",
    "FXEcho",
    "FXEQ_PARAMETERS",
    "FXMASTERINGLIMITER_PARAMETERS",
    "FXREVERB_PARAMETERS",
    "FXECHO_INITDATA",
    "FXECHO_PARAMETERS",
    "XAUDIO2_VOICE_DETAILS",
    "XAUDIO2_SEND_DESCRIPTOR",
    "XAUDIO2_VOICE_SENDS",
    "XAUDIO2_EFFECT_DESCRIPTOR",
    "XAUDIO2_EFFECT_CHAIN",
    "XAUDIO2_FILTER_TYPE",
    "XAUDIO2_FILTER_TYPE_LowPassFilter",
    "XAUDIO2_FILTER_TYPE_BandPassFilter",
    "XAUDIO2_FILTER_TYPE_HighPassFilter",
    "XAUDIO2_FILTER_TYPE_NotchFilter",
    "XAUDIO2_FILTER_TYPE_LowPassOnePoleFilter",
    "XAUDIO2_FILTER_TYPE_HighPassOnePoleFilter",
    "XAUDIO2_FILTER_PARAMETERS",
    "XAUDIO2_BUFFER",
    "XAUDIO2_BUFFER_WMA",
    "XAUDIO2_VOICE_STATE",
    "XAUDIO2_PERFORMANCE_DATA",
    "XAUDIO2_DEBUG_CONFIGURATION",
    "IXAudio2",
    "IXAudio2Extension",
    "IXAudio2Voice",
    "IXAudio2SourceVoice",
    "IXAudio2SubmixVoice",
    "IXAudio2MasteringVoice",
    "IXAudio2EngineCallback",
    "IXAudio2VoiceCallback",
    "AudioVolumeMeter",
    "AudioReverb",
    "XAUDIO2FX_VOLUMEMETER_LEVELS",
    "XAUDIO2FX_REVERB_PARAMETERS",
    "XAUDIO2FX_REVERB_I3DL2_PARAMETERS",
    "HrtfPosition",
    "HrtfOrientation",
    "HrtfDirectivityType",
    "HrtfDirectivityType_OmniDirectional",
    "HrtfDirectivityType_Cardioid",
    "HrtfDirectivityType_Cone",
    "HrtfEnvironment",
    "HrtfEnvironment_Small",
    "HrtfEnvironment_Medium",
    "HrtfEnvironment_Large",
    "HrtfEnvironment_Outdoors",
    "HrtfDirectivity",
    "HrtfDirectivityCardioid",
    "HrtfDirectivityCone",
    "HrtfDistanceDecayType",
    "HrtfDistanceDecayType_NaturalDecay",
    "HrtfDistanceDecayType_CustomDecay",
    "HrtfDistanceDecay",
    "HrtfApoInit",
    "IXAPOHrtfParameters",
    "CreateFX",
    "XAudio2CreateWithVersionInfo",
    "CreateAudioVolumeMeter",
    "CreateAudioReverb",
    "CreateHrtfApo",
]
