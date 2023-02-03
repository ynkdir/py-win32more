from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Audio.XAudio2
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
FXEQ_MIN_FRAMERATE: UInt32 = 22000
FXEQ_MAX_FRAMERATE: UInt32 = 48000
FXEQ_MIN_FREQUENCY_CENTER: Single = 20
FXEQ_MAX_FREQUENCY_CENTER: Single = 20000
FXEQ_DEFAULT_FREQUENCY_CENTER_0: Single = 100
FXEQ_DEFAULT_FREQUENCY_CENTER_1: Single = 800
FXEQ_DEFAULT_FREQUENCY_CENTER_2: Single = 2000
FXEQ_DEFAULT_FREQUENCY_CENTER_3: Single = 10000
FXEQ_MIN_GAIN: Single = 0.126
FXEQ_MAX_GAIN: Single = 7.94
FXEQ_DEFAULT_GAIN: Single = 1
FXEQ_MIN_BANDWIDTH: Single = 0.1
FXEQ_MAX_BANDWIDTH: Single = 2
FXEQ_DEFAULT_BANDWIDTH: Single = 1
FXMASTERINGLIMITER_MIN_RELEASE: UInt32 = 1
FXMASTERINGLIMITER_MAX_RELEASE: UInt32 = 20
FXMASTERINGLIMITER_DEFAULT_RELEASE: UInt32 = 6
FXMASTERINGLIMITER_MIN_LOUDNESS: UInt32 = 1
FXMASTERINGLIMITER_MAX_LOUDNESS: UInt32 = 1800
FXMASTERINGLIMITER_DEFAULT_LOUDNESS: UInt32 = 1000
FXREVERB_MIN_DIFFUSION: Single = 0
FXREVERB_MAX_DIFFUSION: Single = 1
FXREVERB_DEFAULT_DIFFUSION: Single = 0.9
FXREVERB_MIN_ROOMSIZE: Single = 0.0001
FXREVERB_MAX_ROOMSIZE: Single = 1
FXREVERB_DEFAULT_ROOMSIZE: Single = 0.6
FXLOUDNESS_DEFAULT_MOMENTARY_MS: UInt32 = 400
FXLOUDNESS_DEFAULT_SHORTTERM_MS: UInt32 = 3000
FXECHO_MIN_WETDRYMIX: Single = 0
FXECHO_MAX_WETDRYMIX: Single = 1
FXECHO_DEFAULT_WETDRYMIX: Single = 0.5
FXECHO_MIN_FEEDBACK: Single = 0
FXECHO_MAX_FEEDBACK: Single = 1
FXECHO_DEFAULT_FEEDBACK: Single = 0.5
FXECHO_MIN_DELAY: Single = 1
FXECHO_MAX_DELAY: Single = 2000
FXECHO_DEFAULT_DELAY: Single = 500
XAUDIO2_DLL_A: String = 'xaudio2_9.dll'
XAUDIO2_DLL_W: String = 'xaudio2_9.dll'
XAUDIO2D_DLL_A: String = 'xaudio2_9d.dll'
XAUDIO2D_DLL_W: String = 'xaudio2_9d.dll'
XAUDIO2_DLL: String = 'xaudio2_9.dll'
XAUDIO2D_DLL: String = 'xaudio2_9d.dll'
XAUDIO2_MAX_BUFFER_BYTES: UInt32 = 2147483648
XAUDIO2_MAX_QUEUED_BUFFERS: UInt32 = 64
XAUDIO2_MAX_BUFFERS_SYSTEM: UInt32 = 2
XAUDIO2_MAX_AUDIO_CHANNELS: UInt32 = 64
XAUDIO2_MIN_SAMPLE_RATE: UInt32 = 1000
XAUDIO2_MAX_SAMPLE_RATE: UInt32 = 200000
XAUDIO2_MAX_VOLUME_LEVEL: Single = 16777216
XAUDIO2_MAX_FREQ_RATIO: Single = 1024
XAUDIO2_DEFAULT_FREQ_RATIO: Single = 2
XAUDIO2_MAX_FILTER_ONEOVERQ: Single = 1.5
XAUDIO2_MAX_FILTER_FREQUENCY: Single = 1
XAUDIO2_MAX_LOOP_COUNT: UInt32 = 254
XAUDIO2_MAX_INSTANCES: UInt32 = 8
XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MONO: UInt32 = 600000
XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MULTICHANNEL: UInt32 = 300000
XAUDIO2_COMMIT_NOW: UInt32 = 0
XAUDIO2_COMMIT_ALL: UInt32 = 0
XAUDIO2_NO_LOOP_REGION: UInt32 = 0
XAUDIO2_LOOP_INFINITE: UInt32 = 255
XAUDIO2_DEFAULT_CHANNELS: UInt32 = 0
XAUDIO2_DEFAULT_SAMPLERATE: UInt32 = 0
XAUDIO2_DEBUG_ENGINE: UInt32 = 1
XAUDIO2_VOICE_NOPITCH: UInt32 = 2
XAUDIO2_VOICE_NOSRC: UInt32 = 4
XAUDIO2_VOICE_USEFILTER: UInt32 = 8
XAUDIO2_PLAY_TAILS: UInt32 = 32
XAUDIO2_END_OF_STREAM: UInt32 = 64
XAUDIO2_SEND_USEFILTER: UInt32 = 128
XAUDIO2_VOICE_NOSAMPLESPLAYED: UInt32 = 256
XAUDIO2_STOP_ENGINE_WHEN_IDLE: UInt32 = 8192
XAUDIO2_1024_QUANTUM: UInt32 = 32768
XAUDIO2_NO_VIRTUAL_AUDIO_CLIENT: UInt32 = 65536
XAUDIO2_DEFAULT_FILTER_FREQUENCY: Single = 1
XAUDIO2_DEFAULT_FILTER_ONEOVERQ: Single = 1
XAUDIO2_QUANTUM_NUMERATOR: UInt32 = 1
XAUDIO2_QUANTUM_DENOMINATOR: UInt32 = 100
FACILITY_XAUDIO2: UInt32 = 2198
XAUDIO2_E_INVALID_CALL: Windows.Win32.Foundation.HRESULT = -2003435519
XAUDIO2_E_XMA_DECODER_ERROR: Windows.Win32.Foundation.HRESULT = -2003435518
XAUDIO2_E_XAPO_CREATION_FAILED: Windows.Win32.Foundation.HRESULT = -2003435517
XAUDIO2_E_DEVICE_INVALIDATED: Windows.Win32.Foundation.HRESULT = -2003435516
Processor1: UInt32 = 1
Processor2: UInt32 = 2
Processor3: UInt32 = 4
Processor4: UInt32 = 8
Processor5: UInt32 = 16
Processor6: UInt32 = 32
Processor7: UInt32 = 64
Processor8: UInt32 = 128
Processor9: UInt32 = 256
Processor10: UInt32 = 512
Processor11: UInt32 = 1024
Processor12: UInt32 = 2048
Processor13: UInt32 = 4096
Processor14: UInt32 = 8192
Processor15: UInt32 = 16384
Processor16: UInt32 = 32768
Processor17: UInt32 = 65536
Processor18: UInt32 = 131072
Processor19: UInt32 = 262144
Processor20: UInt32 = 524288
Processor21: UInt32 = 1048576
Processor22: UInt32 = 2097152
Processor23: UInt32 = 4194304
Processor24: UInt32 = 8388608
Processor25: UInt32 = 16777216
Processor26: UInt32 = 33554432
Processor27: UInt32 = 67108864
Processor28: UInt32 = 134217728
Processor29: UInt32 = 268435456
Processor30: UInt32 = 536870912
Processor31: UInt32 = 1073741824
Processor32: UInt32 = 2147483648
XAUDIO2_ANY_PROCESSOR: UInt32 = 4294967295
XAUDIO2_USE_DEFAULT_PROCESSOR: UInt32 = 0
XAUDIO2_DEFAULT_PROCESSOR: UInt32 = 1
XAUDIO2_LOG_ERRORS: UInt32 = 1
XAUDIO2_LOG_WARNINGS: UInt32 = 2
XAUDIO2_LOG_INFO: UInt32 = 4
XAUDIO2_LOG_DETAIL: UInt32 = 8
XAUDIO2_LOG_API_CALLS: UInt32 = 16
XAUDIO2_LOG_FUNC_CALLS: UInt32 = 32
XAUDIO2_LOG_TIMING: UInt32 = 64
XAUDIO2_LOG_LOCKS: UInt32 = 128
XAUDIO2_LOG_MEMORY: UInt32 = 256
XAUDIO2_LOG_STREAMING: UInt32 = 4096
XAUDIO2FX_REVERB_MIN_FRAMERATE: UInt32 = 20000
XAUDIO2FX_REVERB_MAX_FRAMERATE: UInt32 = 48000
XAUDIO2FX_REVERB_MIN_WET_DRY_MIX: Single = 0
XAUDIO2FX_REVERB_MIN_REFLECTIONS_DELAY: UInt32 = 0
XAUDIO2FX_REVERB_MIN_REVERB_DELAY: UInt32 = 0
XAUDIO2FX_REVERB_MIN_REAR_DELAY: UInt32 = 0
XAUDIO2FX_REVERB_MIN_7POINT1_SIDE_DELAY: UInt32 = 0
XAUDIO2FX_REVERB_MIN_7POINT1_REAR_DELAY: UInt32 = 0
XAUDIO2FX_REVERB_MIN_POSITION: UInt32 = 0
XAUDIO2FX_REVERB_MIN_DIFFUSION: UInt32 = 0
XAUDIO2FX_REVERB_MIN_LOW_EQ_GAIN: UInt32 = 0
XAUDIO2FX_REVERB_MIN_LOW_EQ_CUTOFF: UInt32 = 0
XAUDIO2FX_REVERB_MIN_HIGH_EQ_GAIN: UInt32 = 0
XAUDIO2FX_REVERB_MIN_HIGH_EQ_CUTOFF: UInt32 = 0
XAUDIO2FX_REVERB_MIN_ROOM_FILTER_FREQ: Single = 20
XAUDIO2FX_REVERB_MIN_ROOM_FILTER_MAIN: Single = -100
XAUDIO2FX_REVERB_MIN_ROOM_FILTER_HF: Single = -100
XAUDIO2FX_REVERB_MIN_REFLECTIONS_GAIN: Single = -100
XAUDIO2FX_REVERB_MIN_REVERB_GAIN: Single = -100
XAUDIO2FX_REVERB_MIN_DECAY_TIME: Single = 0.1
XAUDIO2FX_REVERB_MIN_DENSITY: Single = 0
XAUDIO2FX_REVERB_MIN_ROOM_SIZE: Single = 0
XAUDIO2FX_REVERB_MAX_WET_DRY_MIX: Single = 100
XAUDIO2FX_REVERB_MAX_REFLECTIONS_DELAY: UInt32 = 300
XAUDIO2FX_REVERB_MAX_REVERB_DELAY: UInt32 = 85
XAUDIO2FX_REVERB_MAX_REAR_DELAY: UInt32 = 5
XAUDIO2FX_REVERB_MAX_7POINT1_SIDE_DELAY: UInt32 = 5
XAUDIO2FX_REVERB_MAX_7POINT1_REAR_DELAY: UInt32 = 20
XAUDIO2FX_REVERB_MAX_POSITION: UInt32 = 30
XAUDIO2FX_REVERB_MAX_DIFFUSION: UInt32 = 15
XAUDIO2FX_REVERB_MAX_LOW_EQ_GAIN: UInt32 = 12
XAUDIO2FX_REVERB_MAX_LOW_EQ_CUTOFF: UInt32 = 9
XAUDIO2FX_REVERB_MAX_HIGH_EQ_GAIN: UInt32 = 8
XAUDIO2FX_REVERB_MAX_HIGH_EQ_CUTOFF: UInt32 = 14
XAUDIO2FX_REVERB_MAX_ROOM_FILTER_FREQ: Single = 20000
XAUDIO2FX_REVERB_MAX_ROOM_FILTER_MAIN: Single = 0
XAUDIO2FX_REVERB_MAX_ROOM_FILTER_HF: Single = 0
XAUDIO2FX_REVERB_MAX_REFLECTIONS_GAIN: Single = 20
XAUDIO2FX_REVERB_MAX_REVERB_GAIN: Single = 20
XAUDIO2FX_REVERB_MAX_DENSITY: Single = 100
XAUDIO2FX_REVERB_MAX_ROOM_SIZE: Single = 100
XAUDIO2FX_REVERB_DEFAULT_WET_DRY_MIX: Single = 100
XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_DELAY: UInt32 = 5
XAUDIO2FX_REVERB_DEFAULT_REVERB_DELAY: UInt32 = 5
XAUDIO2FX_REVERB_DEFAULT_REAR_DELAY: UInt32 = 5
XAUDIO2FX_REVERB_DEFAULT_7POINT1_SIDE_DELAY: UInt32 = 5
XAUDIO2FX_REVERB_DEFAULT_7POINT1_REAR_DELAY: UInt32 = 20
XAUDIO2FX_REVERB_DEFAULT_POSITION: UInt32 = 6
XAUDIO2FX_REVERB_DEFAULT_POSITION_MATRIX: UInt32 = 27
XAUDIO2FX_REVERB_DEFAULT_EARLY_DIFFUSION: UInt32 = 8
XAUDIO2FX_REVERB_DEFAULT_LATE_DIFFUSION: UInt32 = 8
XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_GAIN: UInt32 = 8
XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_CUTOFF: UInt32 = 4
XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_GAIN: UInt32 = 8
XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_CUTOFF: UInt32 = 4
XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_FREQ: Single = 5000
XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_MAIN: Single = 0
XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_HF: Single = 0
XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_GAIN: Single = 0
XAUDIO2FX_REVERB_DEFAULT_REVERB_GAIN: Single = 0
XAUDIO2FX_REVERB_DEFAULT_DECAY_TIME: Single = 1
XAUDIO2FX_REVERB_DEFAULT_DENSITY: Single = 100
XAUDIO2FX_REVERB_DEFAULT_ROOM_SIZE: Single = 100
XAUDIO2FX_REVERB_DEFAULT_DISABLE_LATE_FIELD: UInt32 = 0
HRTF_MAX_GAIN_LIMIT: Single = 12
HRTF_MIN_GAIN_LIMIT: Single = -96
HRTF_MIN_UNITY_GAIN_DISTANCE: Single = 0.05
HRTF_DEFAULT_UNITY_GAIN_DISTANCE: Single = 1
FACILITY_XAPO: UInt32 = 2199
XAPO_E_FORMAT_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -2003369983
XAPO_MIN_CHANNELS: UInt32 = 1
XAPO_MAX_CHANNELS: UInt32 = 64
XAPO_MIN_FRAMERATE: UInt32 = 1000
XAPO_MAX_FRAMERATE: UInt32 = 200000
XAPO_REGISTRATION_STRING_LENGTH: UInt32 = 256
XAPO_FLAG_CHANNELS_MUST_MATCH: UInt32 = 1
XAPO_FLAG_FRAMERATE_MUST_MATCH: UInt32 = 2
XAPO_FLAG_BITSPERSAMPLE_MUST_MATCH: UInt32 = 4
XAPO_FLAG_BUFFERCOUNT_MUST_MATCH: UInt32 = 8
XAPO_FLAG_INPLACE_REQUIRED: UInt32 = 32
XAPO_FLAG_INPLACE_SUPPORTED: UInt32 = 16
SPEAKER_MONO: UInt32 = 4
X3DAUDIO_HANDLE_BYTESIZE: UInt32 = 20
X3DAUDIO_PI: Single = 3.1415927
X3DAUDIO_2PI: Single = 6.2831855
X3DAUDIO_SPEED_OF_SOUND: Single = 343.5
X3DAUDIO_CALCULATE_MATRIX: UInt32 = 1
X3DAUDIO_CALCULATE_DELAY: UInt32 = 2
X3DAUDIO_CALCULATE_LPF_DIRECT: UInt32 = 4
X3DAUDIO_CALCULATE_LPF_REVERB: UInt32 = 8
X3DAUDIO_CALCULATE_REVERB: UInt32 = 16
X3DAUDIO_CALCULATE_DOPPLER: UInt32 = 32
X3DAUDIO_CALCULATE_EMITTER_ANGLE: UInt32 = 64
X3DAUDIO_CALCULATE_ZEROCENTER: UInt32 = 65536
X3DAUDIO_CALCULATE_REDIRECT_TO_LFE: UInt32 = 131072
@cfunctype('XAudio2_8.dll')
def CreateFX(clsid: POINTER(Guid), pEffect: POINTER(Windows.Win32.System.Com.IUnknown_head), pInitDat: c_void_p, InitDataByteSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XAudio2_8.dll')
def XAudio2CreateWithVersionInfo(ppXAudio2: POINTER(Windows.Win32.Media.Audio.XAudio2.IXAudio2_head), Flags: UInt32, XAudio2Processor: UInt32, ntddiVersion: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XAudio2_8.dll')
def CreateAudioVolumeMeter(ppApo: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XAudio2_8.dll')
def CreateAudioReverb(ppApo: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('HrtfApo.dll')
def CreateHrtfApo(init: POINTER(Windows.Win32.Media.Audio.XAudio2.HrtfApoInit_head), xApo: POINTER(Windows.Win32.Media.Audio.XAudio2.IXAPO_head)) -> Windows.Win32.Foundation.HRESULT: ...
AudioReverb = Guid('c2633b16-471b-4498-b8-c5-4f-09-59-e2-ec-09')
AudioVolumeMeter = Guid('4fc3b166-972a-40cf-bc-37-7d-b0-3d-b2-fb-a3')
class FXECHO_INITDATA(Structure):
    MaxDelay: Single
    _pack_ = 1
class FXECHO_PARAMETERS(Structure):
    WetDryMix: Single
    Feedback: Single
    Delay: Single
    _pack_ = 1
FXEQ = Guid('f5e01117-d6c4-485a-a3-f5-69-51-96-f3-db-fa')
class FXEQ_PARAMETERS(Structure):
    FrequencyCenter0: Single
    Gain0: Single
    Bandwidth0: Single
    FrequencyCenter1: Single
    Gain1: Single
    Bandwidth1: Single
    FrequencyCenter2: Single
    Gain2: Single
    Bandwidth2: Single
    FrequencyCenter3: Single
    Gain3: Single
    Bandwidth3: Single
    _pack_ = 1
FXEcho = Guid('5039d740-f736-449a-84-d3-a5-62-02-55-7b-87')
class FXMASTERINGLIMITER_PARAMETERS(Structure):
    Release: UInt32
    Loudness: UInt32
    _pack_ = 1
FXMasteringLimiter = Guid('c4137916-2be1-46fd-85-99-44-15-36-f4-98-56')
class FXREVERB_PARAMETERS(Structure):
    Diffusion: Single
    RoomSize: Single
    _pack_ = 1
FXReverb = Guid('7d9aca56-cb68-4807-b6-32-b1-37-35-2e-85-96')
class HrtfApoInit(Structure):
    distanceDecay: POINTER(Windows.Win32.Media.Audio.XAudio2.HrtfDistanceDecay_head)
    directivity: POINTER(Windows.Win32.Media.Audio.XAudio2.HrtfDirectivity_head)
class HrtfDirectivity(Structure):
    type: Windows.Win32.Media.Audio.XAudio2.HrtfDirectivityType
    scaling: Single
class HrtfDirectivityCardioid(Structure):
    directivity: Windows.Win32.Media.Audio.XAudio2.HrtfDirectivity
    order: Single
class HrtfDirectivityCone(Structure):
    directivity: Windows.Win32.Media.Audio.XAudio2.HrtfDirectivity
    innerAngle: Single
    outerAngle: Single
HrtfDirectivityType = Int32
HrtfDirectivityType_OmniDirectional: HrtfDirectivityType = 0
HrtfDirectivityType_Cardioid: HrtfDirectivityType = 1
HrtfDirectivityType_Cone: HrtfDirectivityType = 2
class HrtfDistanceDecay(Structure):
    type: Windows.Win32.Media.Audio.XAudio2.HrtfDistanceDecayType
    maxGain: Single
    minGain: Single
    unityGainDistance: Single
    cutoffDistance: Single
HrtfDistanceDecayType = Int32
HrtfDistanceDecayType_NaturalDecay: HrtfDistanceDecayType = 0
HrtfDistanceDecayType_CustomDecay: HrtfDistanceDecayType = 1
HrtfEnvironment = Int32
HrtfEnvironment_Small: HrtfEnvironment = 0
HrtfEnvironment_Medium: HrtfEnvironment = 1
HrtfEnvironment_Large: HrtfEnvironment = 2
HrtfEnvironment_Outdoors: HrtfEnvironment = 3
class HrtfOrientation(Structure):
    element: Single * 9
class HrtfPosition(Structure):
    x: Single
    y: Single
    z: Single
class IXAPO(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a410b984-9839-4819-a0-be-28-56-ae-6b-3a-db')
    @commethod(3)
    def GetRegistrationProperties(ppRegistrationProperties: POINTER(POINTER(Windows.Win32.Media.Audio.XAudio2.XAPO_REGISTRATION_PROPERTIES_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsInputFormatSupported(pOutputFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pRequestedInputFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), ppSupportedInputFormat: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsOutputFormatSupported(pInputFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pRequestedOutputFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), ppSupportedOutputFormat: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Initialize(pData: c_void_p, DataByteSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Reset() -> Void: ...
    @commethod(8)
    def LockForProcess(InputLockedParameterCount: UInt32, pInputLockedParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAPO_LOCKFORPROCESS_PARAMETERS_head), OutputLockedParameterCount: UInt32, pOutputLockedParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAPO_LOCKFORPROCESS_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnlockForProcess() -> Void: ...
    @commethod(10)
    def Process(InputProcessParameterCount: UInt32, pInputProcessParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAPO_PROCESS_BUFFER_PARAMETERS_head), OutputProcessParameterCount: UInt32, pOutputProcessParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAPO_PROCESS_BUFFER_PARAMETERS_head), IsEnabled: Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(11)
    def CalcInputFrames(OutputFrameCount: UInt32) -> UInt32: ...
    @commethod(12)
    def CalcOutputFrames(InputFrameCount: UInt32) -> UInt32: ...
class IXAPOHrtfParameters(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('15b3cd66-e9de-4464-b6-e6-2b-c3-cf-63-d4-55')
    @commethod(3)
    def SetSourcePosition(position: POINTER(Windows.Win32.Media.Audio.XAudio2.HrtfPosition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSourceOrientation(orientation: POINTER(Windows.Win32.Media.Audio.XAudio2.HrtfOrientation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSourceGain(gain: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetEnvironment(environment: Windows.Win32.Media.Audio.XAudio2.HrtfEnvironment) -> Windows.Win32.Foundation.HRESULT: ...
class IXAPOParameters(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('26d95c66-80f2-499a-ad-54-5a-e7-f0-1c-6d-98')
    @commethod(3)
    def SetParameters(pParameters: c_void_p, ParameterByteSize: UInt32) -> Void: ...
    @commethod(4)
    def GetParameters(pParameters: c_void_p, ParameterByteSize: UInt32) -> Void: ...
class IXAudio2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2b02e3cf-2e0b-4ec3-be-45-1b-2a-3f-e7-21-0d')
    @commethod(3)
    def RegisterForCallbacks(pCallback: Windows.Win32.Media.Audio.XAudio2.IXAudio2EngineCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterForCallbacks(pCallback: Windows.Win32.Media.Audio.XAudio2.IXAudio2EngineCallback_head) -> Void: ...
    @commethod(5)
    def CreateSourceVoice(ppSourceVoice: POINTER(Windows.Win32.Media.Audio.XAudio2.IXAudio2SourceVoice_head), pSourceFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), Flags: UInt32, MaxFrequencyRatio: Single, pCallback: Windows.Win32.Media.Audio.XAudio2.IXAudio2VoiceCallback_head, pSendList: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS_head), pEffectChain: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSubmixVoice(ppSubmixVoice: POINTER(Windows.Win32.Media.Audio.XAudio2.IXAudio2SubmixVoice_head), InputChannels: UInt32, InputSampleRate: UInt32, Flags: UInt32, ProcessingStage: UInt32, pSendList: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS_head), pEffectChain: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateMasteringVoice(ppMasteringVoice: POINTER(Windows.Win32.Media.Audio.XAudio2.IXAudio2MasteringVoice_head), InputChannels: UInt32, InputSampleRate: UInt32, Flags: UInt32, szDeviceId: Windows.Win32.Foundation.PWSTR, pEffectChain: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head), StreamCategory: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StartEngine() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StopEngine() -> Void: ...
    @commethod(10)
    def CommitChanges(OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPerformanceData(pPerfData: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_PERFORMANCE_DATA_head)) -> Void: ...
    @commethod(12)
    def SetDebugConfiguration(pDebugConfiguration: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_DEBUG_CONFIGURATION_head), pReserved: c_void_p) -> Void: ...
class IXAudio2EngineCallback(c_void_p):
    extends: None
    @commethod(0)
    def OnProcessingPassStart() -> Void: ...
    @commethod(1)
    def OnProcessingPassEnd() -> Void: ...
    @commethod(2)
    def OnCriticalError(Error: Windows.Win32.Foundation.HRESULT) -> Void: ...
class IXAudio2Extension(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('84ac29bb-d619-44d2-b1-97-e4-ac-f7-df-3e-d6')
    @commethod(3)
    def GetProcessingQuantum(quantumNumerator: POINTER(UInt32), quantumDenominator: POINTER(UInt32)) -> Void: ...
    @commethod(4)
    def GetProcessor(processor: POINTER(UInt32)) -> Void: ...
class IXAudio2MasteringVoice(c_void_p):
    extends: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice
    @commethod(19)
    def GetChannelMask(pChannelmask: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IXAudio2SourceVoice(c_void_p):
    extends: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice
    @commethod(19)
    def Start(Flags: UInt32, OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Stop(Flags: UInt32, OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SubmitSourceBuffer(pBuffer: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_BUFFER_head), pBufferWMA: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_BUFFER_WMA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FlushSourceBuffers() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Discontinuity() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ExitLoop(OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetState(pVoiceState: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_STATE_head), Flags: UInt32) -> Void: ...
    @commethod(26)
    def SetFrequencyRatio(Ratio: Single, OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetFrequencyRatio(pRatio: POINTER(Single)) -> Void: ...
    @commethod(28)
    def SetSourceSampleRate(NewSourceSampleRate: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IXAudio2SubmixVoice(c_void_p):
    extends: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice
class IXAudio2Voice(c_void_p):
    extends: None
    @commethod(0)
    def GetVoiceDetails(pVoiceDetails: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_DETAILS_head)) -> Void: ...
    @commethod(1)
    def SetOutputVoices(pSendList: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(2)
    def SetEffectChain(pEffectChain: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(3)
    def EnableEffect(EffectIndex: UInt32, OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisableEffect(EffectIndex: UInt32, OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEffectState(EffectIndex: UInt32, pEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Void: ...
    @commethod(6)
    def SetEffectParameters(EffectIndex: UInt32, pParameters: c_void_p, ParametersByteSize: UInt32, OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEffectParameters(EffectIndex: UInt32, pParameters: c_void_p, ParametersByteSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFilterParameters(pParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head), OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilterParameters(pParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head)) -> Void: ...
    @commethod(10)
    def SetOutputFilterParameters(pDestinationVoice: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice_head, pParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head), OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputFilterParameters(pDestinationVoice: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice_head, pParameters: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS_head)) -> Void: ...
    @commethod(12)
    def SetVolume(Volume: Single, OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetVolume(pVolume: POINTER(Single)) -> Void: ...
    @commethod(14)
    def SetChannelVolumes(Channels: UInt32, pVolumes: POINTER(Single), OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetChannelVolumes(Channels: UInt32, pVolumes: POINTER(Single)) -> Void: ...
    @commethod(16)
    def SetOutputMatrix(pDestinationVoice: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice_head, SourceChannels: UInt32, DestinationChannels: UInt32, pLevelMatrix: POINTER(Single), OperationSet: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetOutputMatrix(pDestinationVoice: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice_head, SourceChannels: UInt32, DestinationChannels: UInt32, pLevelMatrix: POINTER(Single)) -> Void: ...
    @commethod(18)
    def DestroyVoice() -> Void: ...
class IXAudio2VoiceCallback(c_void_p):
    extends: None
    @commethod(0)
    def OnVoiceProcessingPassStart(BytesRequired: UInt32) -> Void: ...
    @commethod(1)
    def OnVoiceProcessingPassEnd() -> Void: ...
    @commethod(2)
    def OnStreamEnd() -> Void: ...
    @commethod(3)
    def OnBufferStart(pBufferContext: c_void_p) -> Void: ...
    @commethod(4)
    def OnBufferEnd(pBufferContext: c_void_p) -> Void: ...
    @commethod(5)
    def OnLoopEnd(pBufferContext: c_void_p) -> Void: ...
    @commethod(6)
    def OnVoiceError(pBufferContext: c_void_p, Error: Windows.Win32.Foundation.HRESULT) -> Void: ...
XAPO_BUFFER_FLAGS = Int32
XAPO_BUFFER_SILENT: XAPO_BUFFER_FLAGS = 0
XAPO_BUFFER_VALID: XAPO_BUFFER_FLAGS = 1
class XAPO_LOCKFORPROCESS_PARAMETERS(Structure):
    pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    MaxFrameCount: UInt32
    _pack_ = 1
class XAPO_PROCESS_BUFFER_PARAMETERS(Structure):
    pBuffer: c_void_p
    BufferFlags: Windows.Win32.Media.Audio.XAudio2.XAPO_BUFFER_FLAGS
    ValidFrameCount: UInt32
    _pack_ = 1
class XAPO_REGISTRATION_PROPERTIES(Structure):
    clsid: Guid
    FriendlyName: Char * 256
    CopyrightInfo: Char * 256
    MajorVersion: UInt32
    MinorVersion: UInt32
    Flags: UInt32
    MinInputBufferCount: UInt32
    MaxInputBufferCount: UInt32
    MinOutputBufferCount: UInt32
    MaxOutputBufferCount: UInt32
    _pack_ = 1
class XAUDIO2FX_REVERB_I3DL2_PARAMETERS(Structure):
    WetDryMix: Single
    Room: Int32
    RoomHF: Int32
    RoomRolloffFactor: Single
    DecayTime: Single
    DecayHFRatio: Single
    Reflections: Int32
    ReflectionsDelay: Single
    Reverb: Int32
    ReverbDelay: Single
    Diffusion: Single
    Density: Single
    HFReference: Single
    _pack_ = 1
class XAUDIO2FX_REVERB_PARAMETERS(Structure):
    WetDryMix: Single
    ReflectionsDelay: UInt32
    ReverbDelay: Byte
    RearDelay: Byte
    SideDelay: Byte
    PositionLeft: Byte
    PositionRight: Byte
    PositionMatrixLeft: Byte
    PositionMatrixRight: Byte
    EarlyDiffusion: Byte
    LateDiffusion: Byte
    LowEQGain: Byte
    LowEQCutoff: Byte
    HighEQGain: Byte
    HighEQCutoff: Byte
    RoomFilterFreq: Single
    RoomFilterMain: Single
    RoomFilterHF: Single
    ReflectionsGain: Single
    ReverbGain: Single
    DecayTime: Single
    Density: Single
    RoomSize: Single
    DisableLateField: Windows.Win32.Foundation.BOOL
    _pack_ = 1
class XAUDIO2FX_VOLUMEMETER_LEVELS(Structure):
    pPeakLevels: POINTER(Single)
    pRMSLevels: POINTER(Single)
    ChannelCount: UInt32
    _pack_ = 1
class XAUDIO2_BUFFER(Structure):
    Flags: UInt32
    AudioBytes: UInt32
    pAudioData: c_char_p_no
    PlayBegin: UInt32
    PlayLength: UInt32
    LoopBegin: UInt32
    LoopLength: UInt32
    LoopCount: UInt32
    pContext: c_void_p
    _pack_ = 1
class XAUDIO2_BUFFER_WMA(Structure):
    pDecodedPacketCumulativeBytes: POINTER(UInt32)
    PacketCount: UInt32
    _pack_ = 1
class XAUDIO2_DEBUG_CONFIGURATION(Structure):
    TraceMask: UInt32
    BreakMask: UInt32
    LogThreadID: Windows.Win32.Foundation.BOOL
    LogFileline: Windows.Win32.Foundation.BOOL
    LogFunctionName: Windows.Win32.Foundation.BOOL
    LogTiming: Windows.Win32.Foundation.BOOL
    _pack_ = 1
class XAUDIO2_EFFECT_CHAIN(Structure):
    EffectCount: UInt32
    pEffectDescriptors: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_DESCRIPTOR_head)
    _pack_ = 1
class XAUDIO2_EFFECT_DESCRIPTOR(Structure):
    pEffect: Windows.Win32.System.Com.IUnknown_head
    InitialState: Windows.Win32.Foundation.BOOL
    OutputChannels: UInt32
    _pack_ = 1
class XAUDIO2_FILTER_PARAMETERS(Structure):
    Type: Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE
    Frequency: Single
    OneOverQ: Single
    _pack_ = 1
XAUDIO2_FILTER_TYPE = Int32
XAUDIO2_FILTER_TYPE_LowPassFilter: XAUDIO2_FILTER_TYPE = 0
XAUDIO2_FILTER_TYPE_BandPassFilter: XAUDIO2_FILTER_TYPE = 1
XAUDIO2_FILTER_TYPE_HighPassFilter: XAUDIO2_FILTER_TYPE = 2
XAUDIO2_FILTER_TYPE_NotchFilter: XAUDIO2_FILTER_TYPE = 3
XAUDIO2_FILTER_TYPE_LowPassOnePoleFilter: XAUDIO2_FILTER_TYPE = 4
XAUDIO2_FILTER_TYPE_HighPassOnePoleFilter: XAUDIO2_FILTER_TYPE = 5
class XAUDIO2_PERFORMANCE_DATA(Structure):
    AudioCyclesSinceLastQuery: UInt64
    TotalCyclesSinceLastQuery: UInt64
    MinimumCyclesPerQuantum: UInt32
    MaximumCyclesPerQuantum: UInt32
    MemoryUsageInBytes: UInt32
    CurrentLatencyInSamples: UInt32
    GlitchesSinceEngineStarted: UInt32
    ActiveSourceVoiceCount: UInt32
    TotalSourceVoiceCount: UInt32
    ActiveSubmixVoiceCount: UInt32
    ActiveResamplerCount: UInt32
    ActiveMatrixMixCount: UInt32
    ActiveXmaSourceVoices: UInt32
    ActiveXmaStreams: UInt32
    _pack_ = 1
class XAUDIO2_SEND_DESCRIPTOR(Structure):
    Flags: UInt32
    pOutputVoice: Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice_head
    _pack_ = 1
class XAUDIO2_VOICE_DETAILS(Structure):
    CreationFlags: UInt32
    ActiveFlags: UInt32
    InputChannels: UInt32
    InputSampleRate: UInt32
    _pack_ = 1
class XAUDIO2_VOICE_SENDS(Structure):
    SendCount: UInt32
    pSends: POINTER(Windows.Win32.Media.Audio.XAudio2.XAUDIO2_SEND_DESCRIPTOR_head)
    _pack_ = 1
class XAUDIO2_VOICE_STATE(Structure):
    pCurrentBufferContext: c_void_p
    BuffersQueued: UInt32
    SamplesPlayed: UInt64
    _pack_ = 1
make_head(_module, 'FXECHO_INITDATA')
make_head(_module, 'FXECHO_PARAMETERS')
make_head(_module, 'FXEQ_PARAMETERS')
make_head(_module, 'FXMASTERINGLIMITER_PARAMETERS')
make_head(_module, 'FXREVERB_PARAMETERS')
make_head(_module, 'HrtfApoInit')
make_head(_module, 'HrtfDirectivity')
make_head(_module, 'HrtfDirectivityCardioid')
make_head(_module, 'HrtfDirectivityCone')
make_head(_module, 'HrtfDistanceDecay')
make_head(_module, 'HrtfOrientation')
make_head(_module, 'HrtfPosition')
make_head(_module, 'IXAPO')
make_head(_module, 'IXAPOHrtfParameters')
make_head(_module, 'IXAPOParameters')
make_head(_module, 'IXAudio2')
make_head(_module, 'IXAudio2EngineCallback')
make_head(_module, 'IXAudio2Extension')
make_head(_module, 'IXAudio2MasteringVoice')
make_head(_module, 'IXAudio2SourceVoice')
make_head(_module, 'IXAudio2SubmixVoice')
make_head(_module, 'IXAudio2Voice')
make_head(_module, 'IXAudio2VoiceCallback')
make_head(_module, 'XAPO_LOCKFORPROCESS_PARAMETERS')
make_head(_module, 'XAPO_PROCESS_BUFFER_PARAMETERS')
make_head(_module, 'XAPO_REGISTRATION_PROPERTIES')
make_head(_module, 'XAUDIO2FX_REVERB_I3DL2_PARAMETERS')
make_head(_module, 'XAUDIO2FX_REVERB_PARAMETERS')
make_head(_module, 'XAUDIO2FX_VOLUMEMETER_LEVELS')
make_head(_module, 'XAUDIO2_BUFFER')
make_head(_module, 'XAUDIO2_BUFFER_WMA')
make_head(_module, 'XAUDIO2_DEBUG_CONFIGURATION')
make_head(_module, 'XAUDIO2_EFFECT_CHAIN')
make_head(_module, 'XAUDIO2_EFFECT_DESCRIPTOR')
make_head(_module, 'XAUDIO2_FILTER_PARAMETERS')
make_head(_module, 'XAUDIO2_PERFORMANCE_DATA')
make_head(_module, 'XAUDIO2_SEND_DESCRIPTOR')
make_head(_module, 'XAUDIO2_VOICE_DETAILS')
make_head(_module, 'XAUDIO2_VOICE_SENDS')
make_head(_module, 'XAUDIO2_VOICE_STATE')
__all__ = [
    "AudioReverb",
    "AudioVolumeMeter",
    "CreateAudioReverb",
    "CreateAudioVolumeMeter",
    "CreateFX",
    "CreateHrtfApo",
    "FACILITY_XAPO",
    "FACILITY_XAUDIO2",
    "FXECHO_DEFAULT_DELAY",
    "FXECHO_DEFAULT_FEEDBACK",
    "FXECHO_DEFAULT_WETDRYMIX",
    "FXECHO_INITDATA",
    "FXECHO_MAX_DELAY",
    "FXECHO_MAX_FEEDBACK",
    "FXECHO_MAX_WETDRYMIX",
    "FXECHO_MIN_DELAY",
    "FXECHO_MIN_FEEDBACK",
    "FXECHO_MIN_WETDRYMIX",
    "FXECHO_PARAMETERS",
    "FXEQ",
    "FXEQ_DEFAULT_BANDWIDTH",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_0",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_1",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_2",
    "FXEQ_DEFAULT_FREQUENCY_CENTER_3",
    "FXEQ_DEFAULT_GAIN",
    "FXEQ_MAX_BANDWIDTH",
    "FXEQ_MAX_FRAMERATE",
    "FXEQ_MAX_FREQUENCY_CENTER",
    "FXEQ_MAX_GAIN",
    "FXEQ_MIN_BANDWIDTH",
    "FXEQ_MIN_FRAMERATE",
    "FXEQ_MIN_FREQUENCY_CENTER",
    "FXEQ_MIN_GAIN",
    "FXEQ_PARAMETERS",
    "FXEcho",
    "FXLOUDNESS_DEFAULT_MOMENTARY_MS",
    "FXLOUDNESS_DEFAULT_SHORTTERM_MS",
    "FXMASTERINGLIMITER_DEFAULT_LOUDNESS",
    "FXMASTERINGLIMITER_DEFAULT_RELEASE",
    "FXMASTERINGLIMITER_MAX_LOUDNESS",
    "FXMASTERINGLIMITER_MAX_RELEASE",
    "FXMASTERINGLIMITER_MIN_LOUDNESS",
    "FXMASTERINGLIMITER_MIN_RELEASE",
    "FXMASTERINGLIMITER_PARAMETERS",
    "FXMasteringLimiter",
    "FXREVERB_DEFAULT_DIFFUSION",
    "FXREVERB_DEFAULT_ROOMSIZE",
    "FXREVERB_MAX_DIFFUSION",
    "FXREVERB_MAX_ROOMSIZE",
    "FXREVERB_MIN_DIFFUSION",
    "FXREVERB_MIN_ROOMSIZE",
    "FXREVERB_PARAMETERS",
    "FXReverb",
    "HRTF_DEFAULT_UNITY_GAIN_DISTANCE",
    "HRTF_MAX_GAIN_LIMIT",
    "HRTF_MIN_GAIN_LIMIT",
    "HRTF_MIN_UNITY_GAIN_DISTANCE",
    "HrtfApoInit",
    "HrtfDirectivity",
    "HrtfDirectivityCardioid",
    "HrtfDirectivityCone",
    "HrtfDirectivityType",
    "HrtfDirectivityType_Cardioid",
    "HrtfDirectivityType_Cone",
    "HrtfDirectivityType_OmniDirectional",
    "HrtfDistanceDecay",
    "HrtfDistanceDecayType",
    "HrtfDistanceDecayType_CustomDecay",
    "HrtfDistanceDecayType_NaturalDecay",
    "HrtfEnvironment",
    "HrtfEnvironment_Large",
    "HrtfEnvironment_Medium",
    "HrtfEnvironment_Outdoors",
    "HrtfEnvironment_Small",
    "HrtfOrientation",
    "HrtfPosition",
    "IXAPO",
    "IXAPOHrtfParameters",
    "IXAPOParameters",
    "IXAudio2",
    "IXAudio2EngineCallback",
    "IXAudio2Extension",
    "IXAudio2MasteringVoice",
    "IXAudio2SourceVoice",
    "IXAudio2SubmixVoice",
    "IXAudio2Voice",
    "IXAudio2VoiceCallback",
    "Processor1",
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
    "Processor2",
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
    "Processor3",
    "Processor30",
    "Processor31",
    "Processor32",
    "Processor4",
    "Processor5",
    "Processor6",
    "Processor7",
    "Processor8",
    "Processor9",
    "SPEAKER_MONO",
    "X3DAUDIO_2PI",
    "X3DAUDIO_CALCULATE_DELAY",
    "X3DAUDIO_CALCULATE_DOPPLER",
    "X3DAUDIO_CALCULATE_EMITTER_ANGLE",
    "X3DAUDIO_CALCULATE_LPF_DIRECT",
    "X3DAUDIO_CALCULATE_LPF_REVERB",
    "X3DAUDIO_CALCULATE_MATRIX",
    "X3DAUDIO_CALCULATE_REDIRECT_TO_LFE",
    "X3DAUDIO_CALCULATE_REVERB",
    "X3DAUDIO_CALCULATE_ZEROCENTER",
    "X3DAUDIO_HANDLE_BYTESIZE",
    "X3DAUDIO_PI",
    "X3DAUDIO_SPEED_OF_SOUND",
    "XAPO_BUFFER_FLAGS",
    "XAPO_BUFFER_SILENT",
    "XAPO_BUFFER_VALID",
    "XAPO_E_FORMAT_UNSUPPORTED",
    "XAPO_FLAG_BITSPERSAMPLE_MUST_MATCH",
    "XAPO_FLAG_BUFFERCOUNT_MUST_MATCH",
    "XAPO_FLAG_CHANNELS_MUST_MATCH",
    "XAPO_FLAG_FRAMERATE_MUST_MATCH",
    "XAPO_FLAG_INPLACE_REQUIRED",
    "XAPO_FLAG_INPLACE_SUPPORTED",
    "XAPO_LOCKFORPROCESS_PARAMETERS",
    "XAPO_MAX_CHANNELS",
    "XAPO_MAX_FRAMERATE",
    "XAPO_MIN_CHANNELS",
    "XAPO_MIN_FRAMERATE",
    "XAPO_PROCESS_BUFFER_PARAMETERS",
    "XAPO_REGISTRATION_PROPERTIES",
    "XAPO_REGISTRATION_STRING_LENGTH",
    "XAUDIO2D_DLL",
    "XAUDIO2D_DLL_A",
    "XAUDIO2D_DLL_W",
    "XAUDIO2FX_REVERB_DEFAULT_7POINT1_REAR_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_7POINT1_SIDE_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_DECAY_TIME",
    "XAUDIO2FX_REVERB_DEFAULT_DENSITY",
    "XAUDIO2FX_REVERB_DEFAULT_DISABLE_LATE_FIELD",
    "XAUDIO2FX_REVERB_DEFAULT_EARLY_DIFFUSION",
    "XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_DEFAULT_HIGH_EQ_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_LATE_DIFFUSION",
    "XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_DEFAULT_LOW_EQ_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_POSITION",
    "XAUDIO2FX_REVERB_DEFAULT_POSITION_MATRIX",
    "XAUDIO2FX_REVERB_DEFAULT_REAR_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_REFLECTIONS_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_REVERB_DELAY",
    "XAUDIO2FX_REVERB_DEFAULT_REVERB_GAIN",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_FREQ",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_HF",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_FILTER_MAIN",
    "XAUDIO2FX_REVERB_DEFAULT_ROOM_SIZE",
    "XAUDIO2FX_REVERB_DEFAULT_WET_DRY_MIX",
    "XAUDIO2FX_REVERB_I3DL2_PARAMETERS",
    "XAUDIO2FX_REVERB_MAX_7POINT1_REAR_DELAY",
    "XAUDIO2FX_REVERB_MAX_7POINT1_SIDE_DELAY",
    "XAUDIO2FX_REVERB_MAX_DENSITY",
    "XAUDIO2FX_REVERB_MAX_DIFFUSION",
    "XAUDIO2FX_REVERB_MAX_FRAMERATE",
    "XAUDIO2FX_REVERB_MAX_HIGH_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MAX_HIGH_EQ_GAIN",
    "XAUDIO2FX_REVERB_MAX_LOW_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MAX_LOW_EQ_GAIN",
    "XAUDIO2FX_REVERB_MAX_POSITION",
    "XAUDIO2FX_REVERB_MAX_REAR_DELAY",
    "XAUDIO2FX_REVERB_MAX_REFLECTIONS_DELAY",
    "XAUDIO2FX_REVERB_MAX_REFLECTIONS_GAIN",
    "XAUDIO2FX_REVERB_MAX_REVERB_DELAY",
    "XAUDIO2FX_REVERB_MAX_REVERB_GAIN",
    "XAUDIO2FX_REVERB_MAX_ROOM_FILTER_FREQ",
    "XAUDIO2FX_REVERB_MAX_ROOM_FILTER_HF",
    "XAUDIO2FX_REVERB_MAX_ROOM_FILTER_MAIN",
    "XAUDIO2FX_REVERB_MAX_ROOM_SIZE",
    "XAUDIO2FX_REVERB_MAX_WET_DRY_MIX",
    "XAUDIO2FX_REVERB_MIN_7POINT1_REAR_DELAY",
    "XAUDIO2FX_REVERB_MIN_7POINT1_SIDE_DELAY",
    "XAUDIO2FX_REVERB_MIN_DECAY_TIME",
    "XAUDIO2FX_REVERB_MIN_DENSITY",
    "XAUDIO2FX_REVERB_MIN_DIFFUSION",
    "XAUDIO2FX_REVERB_MIN_FRAMERATE",
    "XAUDIO2FX_REVERB_MIN_HIGH_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MIN_HIGH_EQ_GAIN",
    "XAUDIO2FX_REVERB_MIN_LOW_EQ_CUTOFF",
    "XAUDIO2FX_REVERB_MIN_LOW_EQ_GAIN",
    "XAUDIO2FX_REVERB_MIN_POSITION",
    "XAUDIO2FX_REVERB_MIN_REAR_DELAY",
    "XAUDIO2FX_REVERB_MIN_REFLECTIONS_DELAY",
    "XAUDIO2FX_REVERB_MIN_REFLECTIONS_GAIN",
    "XAUDIO2FX_REVERB_MIN_REVERB_DELAY",
    "XAUDIO2FX_REVERB_MIN_REVERB_GAIN",
    "XAUDIO2FX_REVERB_MIN_ROOM_FILTER_FREQ",
    "XAUDIO2FX_REVERB_MIN_ROOM_FILTER_HF",
    "XAUDIO2FX_REVERB_MIN_ROOM_FILTER_MAIN",
    "XAUDIO2FX_REVERB_MIN_ROOM_SIZE",
    "XAUDIO2FX_REVERB_MIN_WET_DRY_MIX",
    "XAUDIO2FX_REVERB_PARAMETERS",
    "XAUDIO2FX_VOLUMEMETER_LEVELS",
    "XAUDIO2_1024_QUANTUM",
    "XAUDIO2_ANY_PROCESSOR",
    "XAUDIO2_BUFFER",
    "XAUDIO2_BUFFER_WMA",
    "XAUDIO2_COMMIT_ALL",
    "XAUDIO2_COMMIT_NOW",
    "XAUDIO2_DEBUG_CONFIGURATION",
    "XAUDIO2_DEBUG_ENGINE",
    "XAUDIO2_DEFAULT_CHANNELS",
    "XAUDIO2_DEFAULT_FILTER_FREQUENCY",
    "XAUDIO2_DEFAULT_FILTER_ONEOVERQ",
    "XAUDIO2_DEFAULT_FREQ_RATIO",
    "XAUDIO2_DEFAULT_PROCESSOR",
    "XAUDIO2_DEFAULT_SAMPLERATE",
    "XAUDIO2_DLL",
    "XAUDIO2_DLL_A",
    "XAUDIO2_DLL_W",
    "XAUDIO2_EFFECT_CHAIN",
    "XAUDIO2_EFFECT_DESCRIPTOR",
    "XAUDIO2_END_OF_STREAM",
    "XAUDIO2_E_DEVICE_INVALIDATED",
    "XAUDIO2_E_INVALID_CALL",
    "XAUDIO2_E_XAPO_CREATION_FAILED",
    "XAUDIO2_E_XMA_DECODER_ERROR",
    "XAUDIO2_FILTER_PARAMETERS",
    "XAUDIO2_FILTER_TYPE",
    "XAUDIO2_FILTER_TYPE_BandPassFilter",
    "XAUDIO2_FILTER_TYPE_HighPassFilter",
    "XAUDIO2_FILTER_TYPE_HighPassOnePoleFilter",
    "XAUDIO2_FILTER_TYPE_LowPassFilter",
    "XAUDIO2_FILTER_TYPE_LowPassOnePoleFilter",
    "XAUDIO2_FILTER_TYPE_NotchFilter",
    "XAUDIO2_LOG_API_CALLS",
    "XAUDIO2_LOG_DETAIL",
    "XAUDIO2_LOG_ERRORS",
    "XAUDIO2_LOG_FUNC_CALLS",
    "XAUDIO2_LOG_INFO",
    "XAUDIO2_LOG_LOCKS",
    "XAUDIO2_LOG_MEMORY",
    "XAUDIO2_LOG_STREAMING",
    "XAUDIO2_LOG_TIMING",
    "XAUDIO2_LOG_WARNINGS",
    "XAUDIO2_LOOP_INFINITE",
    "XAUDIO2_MAX_AUDIO_CHANNELS",
    "XAUDIO2_MAX_BUFFERS_SYSTEM",
    "XAUDIO2_MAX_BUFFER_BYTES",
    "XAUDIO2_MAX_FILTER_FREQUENCY",
    "XAUDIO2_MAX_FILTER_ONEOVERQ",
    "XAUDIO2_MAX_FREQ_RATIO",
    "XAUDIO2_MAX_INSTANCES",
    "XAUDIO2_MAX_LOOP_COUNT",
    "XAUDIO2_MAX_QUEUED_BUFFERS",
    "XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MONO",
    "XAUDIO2_MAX_RATIO_TIMES_RATE_XMA_MULTICHANNEL",
    "XAUDIO2_MAX_SAMPLE_RATE",
    "XAUDIO2_MAX_VOLUME_LEVEL",
    "XAUDIO2_MIN_SAMPLE_RATE",
    "XAUDIO2_NO_LOOP_REGION",
    "XAUDIO2_NO_VIRTUAL_AUDIO_CLIENT",
    "XAUDIO2_PERFORMANCE_DATA",
    "XAUDIO2_PLAY_TAILS",
    "XAUDIO2_QUANTUM_DENOMINATOR",
    "XAUDIO2_QUANTUM_NUMERATOR",
    "XAUDIO2_SEND_DESCRIPTOR",
    "XAUDIO2_SEND_USEFILTER",
    "XAUDIO2_STOP_ENGINE_WHEN_IDLE",
    "XAUDIO2_USE_DEFAULT_PROCESSOR",
    "XAUDIO2_VOICE_DETAILS",
    "XAUDIO2_VOICE_NOPITCH",
    "XAUDIO2_VOICE_NOSAMPLESPLAYED",
    "XAUDIO2_VOICE_NOSRC",
    "XAUDIO2_VOICE_SENDS",
    "XAUDIO2_VOICE_STATE",
    "XAUDIO2_VOICE_USEFILTER",
    "XAudio2CreateWithVersionInfo",
]
_arch_optional = [
]
