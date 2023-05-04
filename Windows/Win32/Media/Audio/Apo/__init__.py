from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Audio.Apo
import Windows.Win32.System.Com
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class APOInitBaseStruct(EasyCastStructure):
    cbSize: UInt32
    clsid: Guid
class APOInitSystemEffects(EasyCastStructure):
    APOInit: Windows.Win32.Media.Audio.Apo.APOInitBaseStruct
    pAPOEndpointProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
    pAPOSystemEffectsProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
    pReserved: c_void_p
    pDeviceCollection: Windows.Win32.Media.Audio.IMMDeviceCollection_head
class APOInitSystemEffects2(EasyCastStructure):
    APOInit: Windows.Win32.Media.Audio.Apo.APOInitBaseStruct
    pAPOEndpointProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
    pAPOSystemEffectsProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
    pReserved: c_void_p
    pDeviceCollection: Windows.Win32.Media.Audio.IMMDeviceCollection_head
    nSoftwareIoDeviceInCollection: UInt32
    nSoftwareIoConnectorIndex: UInt32
    AudioProcessingMode: Guid
    InitializeForDiscoveryOnly: Windows.Win32.Foundation.BOOL
class APOInitSystemEffects3(EasyCastStructure):
    APOInit: Windows.Win32.Media.Audio.Apo.APOInitBaseStruct
    pAPOEndpointProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
    pServiceProvider: Windows.Win32.System.Com.IServiceProvider_head
    pDeviceCollection: Windows.Win32.Media.Audio.IMMDeviceCollection_head
    nSoftwareIoDeviceInCollection: UInt32
    nSoftwareIoConnectorIndex: UInt32
    AudioProcessingMode: Guid
    InitializeForDiscoveryOnly: Windows.Win32.Foundation.BOOL
APO_BUFFER_FLAGS = Int32
BUFFER_INVALID: APO_BUFFER_FLAGS = 0
BUFFER_VALID: APO_BUFFER_FLAGS = 1
BUFFER_SILENT: APO_BUFFER_FLAGS = 2
APO_CONNECTION_BUFFER_TYPE = Int32
APO_CONNECTION_BUFFER_TYPE_ALLOCATED: APO_CONNECTION_BUFFER_TYPE = 0
APO_CONNECTION_BUFFER_TYPE_EXTERNAL: APO_CONNECTION_BUFFER_TYPE = 1
APO_CONNECTION_BUFFER_TYPE_DEPENDANT: APO_CONNECTION_BUFFER_TYPE = 2
class APO_CONNECTION_DESCRIPTOR(EasyCastStructure):
    Type: Windows.Win32.Media.Audio.Apo.APO_CONNECTION_BUFFER_TYPE
    pBuffer: UIntPtr
    u32MaxFrameCount: UInt32
    pFormat: Windows.Win32.Media.Audio.Apo.IAudioMediaType_head
    u32Signature: UInt32
class APO_CONNECTION_PROPERTY(EasyCastStructure):
    pBuffer: UIntPtr
    u32ValidFrameCount: UInt32
    u32BufferFlags: Windows.Win32.Media.Audio.Apo.APO_BUFFER_FLAGS
    u32Signature: UInt32
class APO_CONNECTION_PROPERTY_V2(EasyCastStructure):
    property: Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY
    u64QPCTime: UInt64
APO_FLAG = Int32
APO_FLAG_NONE: APO_FLAG = 0
APO_FLAG_INPLACE: APO_FLAG = 1
APO_FLAG_SAMPLESPERFRAME_MUST_MATCH: APO_FLAG = 2
APO_FLAG_FRAMESPERSECOND_MUST_MATCH: APO_FLAG = 4
APO_FLAG_BITSPERSAMPLE_MUST_MATCH: APO_FLAG = 8
APO_FLAG_MIXER: APO_FLAG = 16
APO_FLAG_DEFAULT: APO_FLAG = 14
APO_LOG_LEVEL = Int32
APO_LOG_LEVEL_ALWAYS: APO_LOG_LEVEL = 0
APO_LOG_LEVEL_CRITICAL: APO_LOG_LEVEL = 1
APO_LOG_LEVEL_ERROR: APO_LOG_LEVEL = 2
APO_LOG_LEVEL_WARNING: APO_LOG_LEVEL = 3
APO_LOG_LEVEL_INFO: APO_LOG_LEVEL = 4
APO_LOG_LEVEL_VERBOSE: APO_LOG_LEVEL = 5
class APO_NOTIFICATION(EasyCastStructure):
    type: Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        audioEndpointVolumeChange: Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION
        audioEndpointPropertyChange: Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION
        audioSystemEffectsPropertyChange: Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION
        audioEndpointVolumeChange2: Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION2
        deviceOrientation: Windows.Win32.Media.Audio.Apo.DEVICE_ORIENTATION_TYPE
        audioMicrophoneBoostChange: Windows.Win32.Media.Audio.Apo.AUDIO_MICROPHONE_BOOST_NOTIFICATION
class APO_NOTIFICATION_DESCRIPTOR(EasyCastStructure):
    type: Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        audioEndpointVolume: Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR
        audioEndpointPropertyChange: Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
        audioSystemEffectsPropertyChange: Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
        audioMicrophoneBoost: Windows.Win32.Media.Audio.Apo.AUDIO_MICROPHONE_BOOST_APO_NOTIFICATION_DESCRIPTOR
APO_NOTIFICATION_TYPE = Int32
APO_NOTIFICATION_TYPE_NONE: APO_NOTIFICATION_TYPE = 0
APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME: APO_NOTIFICATION_TYPE = 1
APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE: APO_NOTIFICATION_TYPE = 2
APO_NOTIFICATION_TYPE_SYSTEM_EFFECTS_PROPERTY_CHANGE: APO_NOTIFICATION_TYPE = 3
APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME2: APO_NOTIFICATION_TYPE = 4
APO_NOTIFICATION_TYPE_DEVICE_ORIENTATION: APO_NOTIFICATION_TYPE = 5
APO_NOTIFICATION_TYPE_MICROPHONE_BOOST: APO_NOTIFICATION_TYPE = 6
class APO_REG_PROPERTIES(EasyCastStructure):
    clsid: Guid
    Flags: Windows.Win32.Media.Audio.Apo.APO_FLAG
    szFriendlyName: Char * 256
    szCopyrightInfo: Char * 256
    u32MajorVersion: UInt32
    u32MinorVersion: UInt32
    u32MinInputConnections: UInt32
    u32MaxInputConnections: UInt32
    u32MinOutputConnections: UInt32
    u32MaxOutputConnections: UInt32
    u32MaxInstances: UInt32
    u32NumAPOInterfaces: UInt32
    iidAPOInterfaceList: Guid * 1
class AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(EasyCastStructure):
    device: Windows.Win32.Media.Audio.IMMDevice_head
class AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION(EasyCastStructure):
    endpoint: Windows.Win32.Media.Audio.IMMDevice_head
    propertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
    propertyKey: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY
class AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR(EasyCastStructure):
    device: Windows.Win32.Media.Audio.IMMDevice_head
class AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION(EasyCastStructure):
    endpoint: Windows.Win32.Media.Audio.IMMDevice_head
    volume: POINTER(Windows.Win32.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA_head)
class AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION2(EasyCastStructure):
    endpoint: Windows.Win32.Media.Audio.IMMDevice_head
    volume: POINTER(Windows.Win32.Media.Audio.Apo.AUDIO_VOLUME_NOTIFICATION_DATA2_head)
AUDIO_FLOW_TYPE = Int32
AUDIO_FLOW_PULL: AUDIO_FLOW_TYPE = 0
AUDIO_FLOW_PUSH: AUDIO_FLOW_TYPE = 1
class AUDIO_MICROPHONE_BOOST_APO_NOTIFICATION_DESCRIPTOR(EasyCastStructure):
    device: Windows.Win32.Media.Audio.IMMDevice_head
class AUDIO_MICROPHONE_BOOST_NOTIFICATION(EasyCastStructure):
    endpoint: Windows.Win32.Media.Audio.IMMDevice_head
    eventContext: Guid
    microphoneBoostEnabled: Windows.Win32.Foundation.BOOL
    levelInDb: Single
    levelMinInDb: Single
    levelMaxInDb: Single
    levelStepInDb: Single
    muteSupported: Windows.Win32.Foundation.BOOL
    mute: Windows.Win32.Foundation.BOOL
class AUDIO_SYSTEMEFFECT(EasyCastStructure):
    id: Guid
    canSetState: Windows.Win32.Foundation.BOOL
    state: Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE
class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(EasyCastStructure):
    device: Windows.Win32.Media.Audio.IMMDevice_head
    propertyStoreContext: Guid
class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION(EasyCastStructure):
    endpoint: Windows.Win32.Media.Audio.IMMDevice_head
    propertyStoreContext: Guid
    propertyStoreType: Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE
    propertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
    propertyKey: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY
AUDIO_SYSTEMEFFECT_STATE = Int32
AUDIO_SYSTEMEFFECT_STATE_OFF: AUDIO_SYSTEMEFFECT_STATE = 0
AUDIO_SYSTEMEFFECT_STATE_ON: AUDIO_SYSTEMEFFECT_STATE = 1
class AUDIO_VOLUME_NOTIFICATION_DATA2(EasyCastStructure):
    notificationData: POINTER(Windows.Win32.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA_head)
    masterVolumeInDb: Single
    volumeMinInDb: Single
    volumeMaxInDb: Single
    volumeIncrementInDb: Single
    step: UInt32
    stepCount: UInt32
    channelVolumesInDb: Single * 1
APOERR_ALREADY_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2005073919
APOERR_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2005073918
APOERR_FORMAT_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2005073917
APOERR_INVALID_APO_CLSID: Windows.Win32.Foundation.HRESULT = -2005073916
APOERR_BUFFERS_OVERLAP: Windows.Win32.Foundation.HRESULT = -2005073915
APOERR_ALREADY_UNLOCKED: Windows.Win32.Foundation.HRESULT = -2005073914
APOERR_NUM_CONNECTIONS_INVALID: Windows.Win32.Foundation.HRESULT = -2005073913
APOERR_INVALID_OUTPUT_MAXFRAMECOUNT: Windows.Win32.Foundation.HRESULT = -2005073912
APOERR_INVALID_CONNECTION_FORMAT: Windows.Win32.Foundation.HRESULT = -2005073911
APOERR_APO_LOCKED: Windows.Win32.Foundation.HRESULT = -2005073910
APOERR_INVALID_COEFFCOUNT: Windows.Win32.Foundation.HRESULT = -2005073909
APOERR_INVALID_COEFFICIENT: Windows.Win32.Foundation.HRESULT = -2005073908
APOERR_INVALID_CURVE_PARAM: Windows.Win32.Foundation.HRESULT = -2005073907
APOERR_INVALID_INPUTID: Windows.Win32.Foundation.HRESULT = -2005073906
AUDIO_MIN_FRAMERATE: Double = 10
AUDIO_MAX_FRAMERATE: Double = 384000
AUDIO_MIN_CHANNELS: UInt32 = 1
AUDIO_MAX_CHANNELS: UInt32 = 4096
def PKEY_FX_Association():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=0)
def PKEY_FX_PreMixEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=1)
def PKEY_FX_PostMixEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=2)
def PKEY_FX_UserInterfaceClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=3)
def PKEY_FX_FriendlyName():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=4)
def PKEY_FX_StreamEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=5)
def PKEY_FX_ModeEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=6)
def PKEY_FX_EndpointEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=7)
def PKEY_FX_KeywordDetector_StreamEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=8)
def PKEY_FX_KeywordDetector_ModeEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=9)
def PKEY_FX_KeywordDetector_EndpointEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=10)
def PKEY_FX_Offload_StreamEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=11)
def PKEY_FX_Offload_ModeEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=12)
def PKEY_CompositeFX_StreamEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=13)
def PKEY_CompositeFX_ModeEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=14)
def PKEY_CompositeFX_EndpointEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=15)
def PKEY_CompositeFX_KeywordDetector_StreamEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=16)
def PKEY_CompositeFX_KeywordDetector_ModeEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=17)
def PKEY_CompositeFX_KeywordDetector_EndpointEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=18)
def PKEY_CompositeFX_Offload_StreamEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=19)
def PKEY_CompositeFX_Offload_ModeEffectClsid():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=20)
def PKEY_FX_SupportAppLauncher():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=21)
def PKEY_FX_SupportedFormats():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=22)
def PKEY_FX_Enumerator():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=23)
def PKEY_FX_VersionMajor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=24)
def PKEY_FX_VersionMinor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=25)
def PKEY_FX_Author():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=26)
def PKEY_FX_ObjectId():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=27)
def PKEY_FX_State():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=28)
def PKEY_FX_EffectPackSchema_Version():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=29)
def PKEY_FX_ApplyToBluetooth():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=30)
def PKEY_FX_ApplyToUsb():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=31)
def PKEY_FX_ApplyToRender():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=32)
def PKEY_FX_ApplyToCapture():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=33)
def PKEY_SFX_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=5)
def PKEY_MFX_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=6)
def PKEY_EFX_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=7)
def PKEY_SFX_KeywordDetector_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=8)
def PKEY_MFX_KeywordDetector_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=9)
def PKEY_EFX_KeywordDetector_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=10)
def PKEY_SFX_Offload_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=11)
def PKEY_MFX_Offload_ProcessingModes_Supported_For_Streaming():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=12)
def PKEY_APO_SWFallback_ProcessingModes():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=13)
PKEY_FX_EffectPack_Schema_V1: Guid = Guid('{7abf23d9-727e-4d0b-86a3-dd501d260001}')
SID_AudioProcessingObjectRTQueue: Guid = Guid('{458c1a1f-6899-4c12-99ac-e2e6ac253104}')
SID_AudioProcessingObjectLoggingService: Guid = Guid('{8b8008af-09f9-456e-a173-bdb58499bce7}')
AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES: UInt32 = 2
AUDIOMEDIATYPE_EQUAL_FORMAT_DATA: UInt32 = 4
AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA: UInt32 = 8
class AudioFXExtensionParams(EasyCastStructure):
    AddPageParam: Windows.Win32.Foundation.LPARAM
    pwstrEndpointID: Windows.Win32.Foundation.PWSTR
    pFxProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
DEVICE_ORIENTATION_TYPE = Int32
DEVICE_NOT_ROTATED: DEVICE_ORIENTATION_TYPE = 0
DEVICE_ROTATED_90_DEGREES_CLOCKWISE: DEVICE_ORIENTATION_TYPE = 1
DEVICE_ROTATED_180_DEGREES_CLOCKWISE: DEVICE_ORIENTATION_TYPE = 2
DEVICE_ROTATED_270_DEGREES_CLOCKWISE: DEVICE_ORIENTATION_TYPE = 3
EAudioConstriction = Int32
EAudioConstriction_eAudioConstrictionOff: EAudioConstriction = 0
EAudioConstriction_eAudioConstriction48_16: EAudioConstriction = 1
EAudioConstriction_eAudioConstriction44_16: EAudioConstriction = 2
EAudioConstriction_eAudioConstriction14_14: EAudioConstriction = 3
EAudioConstriction_eAudioConstrictionMute: EAudioConstriction = 4
@winfunctype_pointer
def FNAPONOTIFICATIONCALLBACK(pProperties: POINTER(Windows.Win32.Media.Audio.Apo.APO_REG_PROPERTIES_head), pvRefData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IApoAcousticEchoCancellation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{25385759-3236-4101-a943-25693dfb5d2d}')
class IApoAuxiliaryInputConfiguration(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ceb0aab-fa19-48ed-a857-87771ae1b768}')
    @commethod(3)
    def AddAuxiliaryInput(self, dwInputId: UInt32, cbDataSize: UInt32, pbyData: POINTER(Byte), pInputConnection: POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveAuxiliaryInput(self, dwInputId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsInputFormatSupported(self, pRequestedInputFormat: Windows.Win32.Media.Audio.Apo.IAudioMediaType_head, ppSupportedInputFormat: POINTER(Windows.Win32.Media.Audio.Apo.IAudioMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IApoAuxiliaryInputRT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f851809c-c177-49a0-b1b2-b66f017943ab}')
    @commethod(3)
    def AcceptInput(self, dwInputId: UInt32, pInputConnection: POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)) -> Void: ...
class IAudioDeviceModulesClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{98f37dac-d0b6-49f5-896a-aa4d169a4c48}')
    @commethod(3)
    def SetAudioDeviceModulesManager(self, pAudioDeviceModulesManager: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioMediaType(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e997f73-b71f-4798-873b-ed7dfcf15b4d}')
    @commethod(3)
    def IsCompressedFormat(self, pfCompressed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsEqual(self, pIAudioType: Windows.Win32.Media.Audio.Apo.IAudioMediaType_head, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAudioFormat(self) -> POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head): ...
    @commethod(6)
    def GetUncompressedAudioFormat(self, pUncompressedAudioFormat: POINTER(Windows.Win32.Media.Audio.Apo.UNCOMPRESSEDAUDIOFORMAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd7f2b29-24d0-4b5c-b177-592c39f9ca10}')
    @commethod(3)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLatency(self, pTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRegistrationProperties(self, ppRegProps: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.APO_REG_PROPERTIES_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Initialize(self, cbDataSize: UInt32, pbyData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsInputFormatSupported(self, pOppositeFormat: Windows.Win32.Media.Audio.Apo.IAudioMediaType_head, pRequestedInputFormat: Windows.Win32.Media.Audio.Apo.IAudioMediaType_head, ppSupportedInputFormat: POINTER(Windows.Win32.Media.Audio.Apo.IAudioMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsOutputFormatSupported(self, pOppositeFormat: Windows.Win32.Media.Audio.Apo.IAudioMediaType_head, pRequestedOutputFormat: Windows.Win32.Media.Audio.Apo.IAudioMediaType_head, ppSupportedOutputFormat: POINTER(Windows.Win32.Media.Audio.Apo.IAudioMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInputChannelCount(self, pu32ChannelCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectConfiguration(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e5ed805-aba6-49c3-8f9a-2b8c889c4fa8}')
    @commethod(3)
    def LockForProcess(self, u32NumInputConnections: UInt32, ppInputConnections: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head)), u32NumOutputConnections: UInt32, ppOutputConnections: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnlockForProcess(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectLoggingService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{698f0107-1745-4708-95a5-d84478a62a65}')
    @commethod(3)
    def ApoLog(self, level: Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL, format: Windows.Win32.Foundation.PWSTR) -> Void: ...
class IAudioProcessingObjectNotifications(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56b0c76f-02fd-4b21-a52e-9f8219fc86e4}')
    @commethod(3)
    def GetApoNotificationRegistrationInfo(self, apoNotifications: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR_head)), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HandleNotification(self, apoNotification: POINTER(Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_head)) -> Void: ...
class IAudioProcessingObjectNotifications2(ComPtr):
    extends: Windows.Win32.Media.Audio.Apo.IAudioProcessingObjectNotifications
    _iid_ = Guid('{ca2cfbde-a9d6-4eb0-bc95-c4d026b380f0}')
    @commethod(5)
    def GetApoNotificationRegistrationInfo2(self, maxApoNotificationTypeSupported: Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE, apoNotifications: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR_head)), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectRT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9e1d6a6d-ddbc-4e95-a4c7-ad64ba37846c}')
    @commethod(3)
    def APOProcess(self, u32NumInputConnections: UInt32, ppInputConnections: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)), u32NumOutputConnections: UInt32, ppOutputConnections: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head))) -> Void: ...
    @commethod(4)
    def CalcInputFrames(self, u32OutputFrameCount: UInt32) -> UInt32: ...
    @commethod(5)
    def CalcOutputFrames(self, u32InputFrameCount: UInt32) -> UInt32: ...
class IAudioProcessingObjectRTQueueService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{acd65e2f-955b-4b57-b9bf-ac297bb752c9}')
    @commethod(3)
    def GetRealTimeWorkQueue(self, workQueueId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectVBR(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ba1db8f-78ad-49cd-9591-f79d80a17c81}')
    @commethod(3)
    def CalcMaxInputFrames(self, u32MaxOutputFrameCount: UInt32, pu32InputFrameCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CalcMaxOutputFrames(self, u32MaxInputFrameCount: UInt32, pu32OutputFrameCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffects(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5fa00f27-add6-499a-8a9d-6b98521fa75b}')
class IAudioSystemEffects2(ComPtr):
    extends: Windows.Win32.Media.Audio.Apo.IAudioSystemEffects
    _iid_ = Guid('{bafe99d2-7436-44ce-9e0e-4d89afbfff56}')
    @commethod(3)
    def GetEffectsList(self, ppEffectsIds: POINTER(POINTER(Guid)), pcEffects: POINTER(UInt32), Event: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffects3(ComPtr):
    extends: Windows.Win32.Media.Audio.Apo.IAudioSystemEffects2
    _iid_ = Guid('{c58b31cd-fc6a-4255-bc1f-ad29bb0a4a17}')
    @commethod(4)
    def GetControllableSystemEffectsList(self, effects: POINTER(POINTER(Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_head)), numEffects: POINTER(UInt32), event: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAudioSystemEffectState(self, effectId: Guid, state: Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffectsCustomFormats(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b1176e34-bb7f-4f05-bebd-1b18a534e097}')
    @commethod(3)
    def GetFormatCount(self, pcFormats: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormat(self, nFormat: UInt32, ppFormat: POINTER(Windows.Win32.Media.Audio.Apo.IAudioMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormatRepresentation(self, nFormat: UInt32, ppwstrFormatRep: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class UNCOMPRESSEDAUDIOFORMAT(EasyCastStructure):
    guidFormatType: Guid
    dwSamplesPerFrame: UInt32
    dwBytesPerSampleContainer: UInt32
    dwValidBitsPerSample: UInt32
    fFramesPerSecond: Single
    dwChannelMask: UInt32
make_head(_module, 'APOInitBaseStruct')
make_head(_module, 'APOInitSystemEffects')
make_head(_module, 'APOInitSystemEffects2')
make_head(_module, 'APOInitSystemEffects3')
make_head(_module, 'APO_CONNECTION_DESCRIPTOR')
make_head(_module, 'APO_CONNECTION_PROPERTY')
make_head(_module, 'APO_CONNECTION_PROPERTY_V2')
make_head(_module, 'APO_NOTIFICATION')
make_head(_module, 'APO_NOTIFICATION_DESCRIPTOR')
make_head(_module, 'APO_REG_PROPERTIES')
make_head(_module, 'AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR')
make_head(_module, 'AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION')
make_head(_module, 'AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR')
make_head(_module, 'AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION')
make_head(_module, 'AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION2')
make_head(_module, 'AUDIO_MICROPHONE_BOOST_APO_NOTIFICATION_DESCRIPTOR')
make_head(_module, 'AUDIO_MICROPHONE_BOOST_NOTIFICATION')
make_head(_module, 'AUDIO_SYSTEMEFFECT')
make_head(_module, 'AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR')
make_head(_module, 'AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION')
make_head(_module, 'AUDIO_VOLUME_NOTIFICATION_DATA2')
make_head(_module, 'PKEY_FX_Association')
make_head(_module, 'PKEY_FX_PreMixEffectClsid')
make_head(_module, 'PKEY_FX_PostMixEffectClsid')
make_head(_module, 'PKEY_FX_UserInterfaceClsid')
make_head(_module, 'PKEY_FX_FriendlyName')
make_head(_module, 'PKEY_FX_StreamEffectClsid')
make_head(_module, 'PKEY_FX_ModeEffectClsid')
make_head(_module, 'PKEY_FX_EndpointEffectClsid')
make_head(_module, 'PKEY_FX_KeywordDetector_StreamEffectClsid')
make_head(_module, 'PKEY_FX_KeywordDetector_ModeEffectClsid')
make_head(_module, 'PKEY_FX_KeywordDetector_EndpointEffectClsid')
make_head(_module, 'PKEY_FX_Offload_StreamEffectClsid')
make_head(_module, 'PKEY_FX_Offload_ModeEffectClsid')
make_head(_module, 'PKEY_CompositeFX_StreamEffectClsid')
make_head(_module, 'PKEY_CompositeFX_ModeEffectClsid')
make_head(_module, 'PKEY_CompositeFX_EndpointEffectClsid')
make_head(_module, 'PKEY_CompositeFX_KeywordDetector_StreamEffectClsid')
make_head(_module, 'PKEY_CompositeFX_KeywordDetector_ModeEffectClsid')
make_head(_module, 'PKEY_CompositeFX_KeywordDetector_EndpointEffectClsid')
make_head(_module, 'PKEY_CompositeFX_Offload_StreamEffectClsid')
make_head(_module, 'PKEY_CompositeFX_Offload_ModeEffectClsid')
make_head(_module, 'PKEY_FX_SupportAppLauncher')
make_head(_module, 'PKEY_FX_SupportedFormats')
make_head(_module, 'PKEY_FX_Enumerator')
make_head(_module, 'PKEY_FX_VersionMajor')
make_head(_module, 'PKEY_FX_VersionMinor')
make_head(_module, 'PKEY_FX_Author')
make_head(_module, 'PKEY_FX_ObjectId')
make_head(_module, 'PKEY_FX_State')
make_head(_module, 'PKEY_FX_EffectPackSchema_Version')
make_head(_module, 'PKEY_FX_ApplyToBluetooth')
make_head(_module, 'PKEY_FX_ApplyToUsb')
make_head(_module, 'PKEY_FX_ApplyToRender')
make_head(_module, 'PKEY_FX_ApplyToCapture')
make_head(_module, 'PKEY_SFX_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_MFX_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_EFX_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_SFX_KeywordDetector_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_MFX_KeywordDetector_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_EFX_KeywordDetector_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_SFX_Offload_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_MFX_Offload_ProcessingModes_Supported_For_Streaming')
make_head(_module, 'PKEY_APO_SWFallback_ProcessingModes')
make_head(_module, 'AudioFXExtensionParams')
make_head(_module, 'FNAPONOTIFICATIONCALLBACK')
make_head(_module, 'IApoAcousticEchoCancellation')
make_head(_module, 'IApoAuxiliaryInputConfiguration')
make_head(_module, 'IApoAuxiliaryInputRT')
make_head(_module, 'IAudioDeviceModulesClient')
make_head(_module, 'IAudioMediaType')
make_head(_module, 'IAudioProcessingObject')
make_head(_module, 'IAudioProcessingObjectConfiguration')
make_head(_module, 'IAudioProcessingObjectLoggingService')
make_head(_module, 'IAudioProcessingObjectNotifications')
make_head(_module, 'IAudioProcessingObjectNotifications2')
make_head(_module, 'IAudioProcessingObjectRT')
make_head(_module, 'IAudioProcessingObjectRTQueueService')
make_head(_module, 'IAudioProcessingObjectVBR')
make_head(_module, 'IAudioSystemEffects')
make_head(_module, 'IAudioSystemEffects2')
make_head(_module, 'IAudioSystemEffects3')
make_head(_module, 'IAudioSystemEffectsCustomFormats')
make_head(_module, 'UNCOMPRESSEDAUDIOFORMAT')
