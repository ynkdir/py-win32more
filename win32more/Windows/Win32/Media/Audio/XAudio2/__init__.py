from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Audio.XAudio2
import win32more.Windows.Win32.System.Com
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
XAUDIO2_E_INVALID_CALL: win32more.Windows.Win32.Foundation.HRESULT = -2003435519
XAUDIO2_E_XMA_DECODER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2003435518
XAUDIO2_E_XAPO_CREATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2003435517
XAUDIO2_E_DEVICE_INVALIDATED: win32more.Windows.Win32.Foundation.HRESULT = -2003435516
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
XAPO_E_FORMAT_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2003369983
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
def CreateFX(clsid: POINTER(Guid), pEffect: POINTER(win32more.Windows.Win32.System.Com.IUnknown), pInitDat: VoidPtr, InitDataByteSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XAudio2_8.dll')
def XAudio2CreateWithVersionInfo(ppXAudio2: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2), Flags: UInt32, XAudio2Processor: UInt32, ntddiVersion: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XAudio2_8.dll')
def CreateAudioVolumeMeter(ppApo: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XAudio2_8.dll')
def CreateAudioReverb(ppApo: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('HrtfApo.dll')
def CreateHrtfApo(init: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.HrtfApoInit), xApo: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.IXAPO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
AudioReverb = Guid('{c2633b16-471b-4498-b8c5-4f0959e2ec09}')
AudioVolumeMeter = Guid('{4fc3b166-972a-40cf-bc37-7db03db2fba3}')
class FXECHO_INITDATA(Structure):
    MaxDelay: Single
    _pack_ = 1
class FXECHO_PARAMETERS(Structure):
    WetDryMix: Single
    Feedback: Single
    Delay: Single
    _pack_ = 1
FXEQ = Guid('{f5e01117-d6c4-485a-a3f5-695196f3dbfa}')
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
FXEcho = Guid('{5039d740-f736-449a-84d3-a56202557b87}')
class FXMASTERINGLIMITER_PARAMETERS(Structure):
    Release: UInt32
    Loudness: UInt32
    _pack_ = 1
FXMasteringLimiter = Guid('{c4137916-2be1-46fd-8599-441536f49856}')
class FXREVERB_PARAMETERS(Structure):
    Diffusion: Single
    RoomSize: Single
    _pack_ = 1
FXReverb = Guid('{7d9aca56-cb68-4807-b632-b137352e8596}')
class HrtfApoInit(Structure):
    distanceDecay: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDistanceDecay)
    directivity: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDirectivity)
class HrtfDirectivity(Structure):
    type: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDirectivityType
    scaling: Single
class HrtfDirectivityCardioid(Structure):
    directivity: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDirectivity
    order: Single
class HrtfDirectivityCone(Structure):
    directivity: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDirectivity
    innerAngle: Single
    outerAngle: Single
HrtfDirectivityType = Int32
OmniDirectional: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDirectivityType = 0
Cardioid: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDirectivityType = 1
Cone: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDirectivityType = 2
class HrtfDistanceDecay(Structure):
    type: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDistanceDecayType
    maxGain: Single
    minGain: Single
    unityGainDistance: Single
    cutoffDistance: Single
HrtfDistanceDecayType = Int32
NaturalDecay: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDistanceDecayType = 0
CustomDecay: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfDistanceDecayType = 1
HrtfEnvironment = Int32
Small: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfEnvironment = 0
Medium: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfEnvironment = 1
Large: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfEnvironment = 2
Outdoors: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfEnvironment = 3
class HrtfOrientation(Structure):
    element: Single * 9
class HrtfPosition(Structure):
    x: Single
    y: Single
    z: Single
class IXAPO(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a410b984-9839-4819-a0be-2856ae6b3adb}')
    @commethod(3)
    def GetRegistrationProperties(self, ppRegistrationProperties: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_REGISTRATION_PROPERTIES))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsInputFormatSupported(self, pOutputFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pRequestedInputFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), ppSupportedInputFormat: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsOutputFormatSupported(self, pInputFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pRequestedOutputFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), ppSupportedOutputFormat: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Initialize(self, pData: VoidPtr, DataByteSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Reset(self) -> Void: ...
    @commethod(8)
    def LockForProcess(self, InputLockedParameterCount: UInt32, pInputLockedParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_LOCKFORPROCESS_PARAMETERS), OutputLockedParameterCount: UInt32, pOutputLockedParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_LOCKFORPROCESS_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnlockForProcess(self) -> Void: ...
    @commethod(10)
    def Process(self, InputProcessParameterCount: UInt32, pInputProcessParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_PROCESS_BUFFER_PARAMETERS), OutputProcessParameterCount: UInt32, pOutputProcessParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_PROCESS_BUFFER_PARAMETERS), IsEnabled: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(11)
    def CalcInputFrames(self, OutputFrameCount: UInt32) -> UInt32: ...
    @commethod(12)
    def CalcOutputFrames(self, InputFrameCount: UInt32) -> UInt32: ...
class IXAPOHrtfParameters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{15b3cd66-e9de-4464-b6e6-2bc3cf63d455}')
    @commethod(3)
    def SetSourcePosition(self, position: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.HrtfPosition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSourceOrientation(self, orientation: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.HrtfOrientation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSourceGain(self, gain: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetEnvironment(self, environment: win32more.Windows.Win32.Media.Audio.XAudio2.HrtfEnvironment) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXAPOParameters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26d95c66-80f2-499a-ad54-5ae7f01c6d98}')
    @commethod(3)
    def SetParameters(self, pParameters: VoidPtr, ParameterByteSize: UInt32) -> Void: ...
    @commethod(4)
    def GetParameters(self, pParameters: VoidPtr, ParameterByteSize: UInt32) -> Void: ...
class IXAudio2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2b02e3cf-2e0b-4ec3-be45-1b2a3fe7210d}')
    @commethod(3)
    def RegisterForCallbacks(self, pCallback: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2EngineCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterForCallbacks(self, pCallback: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2EngineCallback) -> Void: ...
    @commethod(5)
    def CreateSourceVoice(self, ppSourceVoice: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2SourceVoice), pSourceFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), Flags: UInt32, MaxFrequencyRatio: Single, pCallback: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2VoiceCallback, pSendList: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS), pEffectChain: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSubmixVoice(self, ppSubmixVoice: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2SubmixVoice), InputChannels: UInt32, InputSampleRate: UInt32, Flags: UInt32, ProcessingStage: UInt32, pSendList: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS), pEffectChain: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateMasteringVoice(self, ppMasteringVoice: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2MasteringVoice), InputChannels: UInt32, InputSampleRate: UInt32, Flags: UInt32, szDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pEffectChain: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN), StreamCategory: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StartEngine(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StopEngine(self) -> Void: ...
    @commethod(10)
    def CommitChanges(self, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPerformanceData(self, pPerfData: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_PERFORMANCE_DATA)) -> Void: ...
    @commethod(12)
    def SetDebugConfiguration(self, pDebugConfiguration: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_DEBUG_CONFIGURATION), pReserved: VoidPtr) -> Void: ...
class IXAudio2EngineCallback(ComPtr):
    extends: None
    @commethod(0)
    def OnProcessingPassStart(self) -> Void: ...
    @commethod(1)
    def OnProcessingPassEnd(self) -> Void: ...
    @commethod(2)
    def OnCriticalError(self, Error: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
class IXAudio2Extension(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{84ac29bb-d619-44d2-b197-e4acf7df3ed6}')
    @commethod(3)
    def GetProcessingQuantum(self, quantumNumerator: POINTER(UInt32), quantumDenominator: POINTER(UInt32)) -> Void: ...
    @commethod(4)
    def GetProcessor(self, processor: POINTER(UInt32)) -> Void: ...
class IXAudio2MasteringVoice(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice
    @commethod(19)
    def GetChannelMask(self, pChannelmask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXAudio2SourceVoice(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice
    @commethod(19)
    def Start(self, Flags: UInt32, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Stop(self, Flags: UInt32, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SubmitSourceBuffer(self, pBuffer: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_BUFFER), pBufferWMA: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_BUFFER_WMA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FlushSourceBuffers(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Discontinuity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ExitLoop(self, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetState(self, pVoiceState: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_STATE), Flags: UInt32) -> Void: ...
    @commethod(26)
    def SetFrequencyRatio(self, Ratio: Single, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetFrequencyRatio(self, pRatio: POINTER(Single)) -> Void: ...
    @commethod(28)
    def SetSourceSampleRate(self, NewSourceSampleRate: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXAudio2SubmixVoice(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice
class IXAudio2Voice(ComPtr):
    extends: None
    @commethod(0)
    def GetVoiceDetails(self, pVoiceDetails: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_DETAILS)) -> Void: ...
    @commethod(1)
    def SetOutputVoices(self, pSendList: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_VOICE_SENDS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(2)
    def SetEffectChain(self, pEffectChain: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_CHAIN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(3)
    def EnableEffect(self, EffectIndex: UInt32, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisableEffect(self, EffectIndex: UInt32, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEffectState(self, EffectIndex: UInt32, pEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> Void: ...
    @commethod(6)
    def SetEffectParameters(self, EffectIndex: UInt32, pParameters: VoidPtr, ParametersByteSize: UInt32, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEffectParameters(self, EffectIndex: UInt32, pParameters: VoidPtr, ParametersByteSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFilterParameters(self, pParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS), OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilterParameters(self, pParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS)) -> Void: ...
    @commethod(10)
    def SetOutputFilterParameters(self, pDestinationVoice: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice, pParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS), OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputFilterParameters(self, pDestinationVoice: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice, pParameters: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_PARAMETERS)) -> Void: ...
    @commethod(12)
    def SetVolume(self, Volume: Single, OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetVolume(self, pVolume: POINTER(Single)) -> Void: ...
    @commethod(14)
    def SetChannelVolumes(self, Channels: UInt32, pVolumes: POINTER(Single), OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetChannelVolumes(self, Channels: UInt32, pVolumes: POINTER(Single)) -> Void: ...
    @commethod(16)
    def SetOutputMatrix(self, pDestinationVoice: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice, SourceChannels: UInt32, DestinationChannels: UInt32, pLevelMatrix: POINTER(Single), OperationSet: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetOutputMatrix(self, pDestinationVoice: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice, SourceChannels: UInt32, DestinationChannels: UInt32, pLevelMatrix: POINTER(Single)) -> Void: ...
    @commethod(18)
    def DestroyVoice(self) -> Void: ...
class IXAudio2VoiceCallback(ComPtr):
    extends: None
    @commethod(0)
    def OnVoiceProcessingPassStart(self, BytesRequired: UInt32) -> Void: ...
    @commethod(1)
    def OnVoiceProcessingPassEnd(self) -> Void: ...
    @commethod(2)
    def OnStreamEnd(self) -> Void: ...
    @commethod(3)
    def OnBufferStart(self, pBufferContext: VoidPtr) -> Void: ...
    @commethod(4)
    def OnBufferEnd(self, pBufferContext: VoidPtr) -> Void: ...
    @commethod(5)
    def OnLoopEnd(self, pBufferContext: VoidPtr) -> Void: ...
    @commethod(6)
    def OnVoiceError(self, pBufferContext: VoidPtr, Error: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
XAPO_BUFFER_FLAGS = Int32
XAPO_BUFFER_SILENT: win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_BUFFER_FLAGS = 0
XAPO_BUFFER_VALID: win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_BUFFER_FLAGS = 1
class XAPO_LOCKFORPROCESS_PARAMETERS(Structure):
    pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    MaxFrameCount: UInt32
    _pack_ = 1
class XAPO_PROCESS_BUFFER_PARAMETERS(Structure):
    pBuffer: VoidPtr
    BufferFlags: win32more.Windows.Win32.Media.Audio.XAudio2.XAPO_BUFFER_FLAGS
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
    DisableLateField: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
class XAUDIO2FX_VOLUMEMETER_LEVELS(Structure):
    pPeakLevels: POINTER(Single)
    pRMSLevels: POINTER(Single)
    ChannelCount: UInt32
    _pack_ = 1
class XAUDIO2_BUFFER(Structure):
    Flags: UInt32
    AudioBytes: UInt32
    pAudioData: POINTER(Byte)
    PlayBegin: UInt32
    PlayLength: UInt32
    LoopBegin: UInt32
    LoopLength: UInt32
    LoopCount: UInt32
    pContext: VoidPtr
    _pack_ = 1
class XAUDIO2_BUFFER_WMA(Structure):
    pDecodedPacketCumulativeBytes: POINTER(UInt32)
    PacketCount: UInt32
    _pack_ = 1
class XAUDIO2_DEBUG_CONFIGURATION(Structure):
    TraceMask: UInt32
    BreakMask: UInt32
    LogThreadID: win32more.Windows.Win32.Foundation.BOOL
    LogFileline: win32more.Windows.Win32.Foundation.BOOL
    LogFunctionName: win32more.Windows.Win32.Foundation.BOOL
    LogTiming: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
class XAUDIO2_EFFECT_CHAIN(Structure):
    EffectCount: UInt32
    pEffectDescriptors: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_EFFECT_DESCRIPTOR)
    _pack_ = 1
class XAUDIO2_EFFECT_DESCRIPTOR(Structure):
    pEffect: win32more.Windows.Win32.System.Com.IUnknown
    InitialState: win32more.Windows.Win32.Foundation.BOOL
    OutputChannels: UInt32
    _pack_ = 1
class XAUDIO2_FILTER_PARAMETERS(Structure):
    Type: win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE
    Frequency: Single
    OneOverQ: Single
    _pack_ = 1
XAUDIO2_FILTER_TYPE = Int32
LowPassFilter: win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE = 0
BandPassFilter: win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE = 1
HighPassFilter: win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE = 2
NotchFilter: win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE = 3
LowPassOnePoleFilter: win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE = 4
HighPassOnePoleFilter: win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_FILTER_TYPE = 5
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
    pOutputVoice: win32more.Windows.Win32.Media.Audio.XAudio2.IXAudio2Voice
    _pack_ = 1
class XAUDIO2_VOICE_DETAILS(Structure):
    CreationFlags: UInt32
    ActiveFlags: UInt32
    InputChannels: UInt32
    InputSampleRate: UInt32
    _pack_ = 1
class XAUDIO2_VOICE_SENDS(Structure):
    SendCount: UInt32
    pSends: POINTER(win32more.Windows.Win32.Media.Audio.XAudio2.XAUDIO2_SEND_DESCRIPTOR)
    _pack_ = 1
class XAUDIO2_VOICE_STATE(Structure):
    pCurrentBufferContext: VoidPtr
    BuffersQueued: UInt32
    SamplesPlayed: UInt64
    _pack_ = 1


make_ready(__name__)
