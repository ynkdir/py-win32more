from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Audio.Apo
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
class APOInitBaseStruct(Structure):
    cbSize: UInt32
    clsid: Guid
class APOInitSystemEffects(Structure):
    APOInit: win32more.Windows.Win32.Media.Audio.Apo.APOInitBaseStruct
    pAPOEndpointProperties: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    pAPOSystemEffectsProperties: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    pReserved: VoidPtr
    pDeviceCollection: win32more.Windows.Win32.Media.Audio.IMMDeviceCollection
class APOInitSystemEffects2(Structure):
    APOInit: win32more.Windows.Win32.Media.Audio.Apo.APOInitBaseStruct
    pAPOEndpointProperties: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    pAPOSystemEffectsProperties: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    pReserved: VoidPtr
    pDeviceCollection: win32more.Windows.Win32.Media.Audio.IMMDeviceCollection
    nSoftwareIoDeviceInCollection: UInt32
    nSoftwareIoConnectorIndex: UInt32
    AudioProcessingMode: Guid
    InitializeForDiscoveryOnly: win32more.Windows.Win32.Foundation.BOOL
class APOInitSystemEffects3(Structure):
    APOInit: win32more.Windows.Win32.Media.Audio.Apo.APOInitBaseStruct
    pAPOEndpointProperties: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    pServiceProvider: win32more.Windows.Win32.System.Com.IServiceProvider
    pDeviceCollection: win32more.Windows.Win32.Media.Audio.IMMDeviceCollection
    nSoftwareIoDeviceInCollection: UInt32
    nSoftwareIoConnectorIndex: UInt32
    AudioProcessingMode: Guid
    InitializeForDiscoveryOnly: win32more.Windows.Win32.Foundation.BOOL
APO_BUFFER_FLAGS = Int32
BUFFER_INVALID: win32more.Windows.Win32.Media.Audio.Apo.APO_BUFFER_FLAGS = 0
BUFFER_VALID: win32more.Windows.Win32.Media.Audio.Apo.APO_BUFFER_FLAGS = 1
BUFFER_SILENT: win32more.Windows.Win32.Media.Audio.Apo.APO_BUFFER_FLAGS = 2
APO_CONNECTION_BUFFER_TYPE = Int32
APO_CONNECTION_BUFFER_TYPE_ALLOCATED: win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_BUFFER_TYPE = 0
APO_CONNECTION_BUFFER_TYPE_EXTERNAL: win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_BUFFER_TYPE = 1
APO_CONNECTION_BUFFER_TYPE_DEPENDANT: win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_BUFFER_TYPE = 2
class APO_CONNECTION_DESCRIPTOR(Structure):
    Type: win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_BUFFER_TYPE
    pBuffer: UIntPtr
    u32MaxFrameCount: UInt32
    pFormat: win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType
    u32Signature: UInt32
class APO_CONNECTION_PROPERTY(Structure):
    pBuffer: UIntPtr
    u32ValidFrameCount: UInt32
    u32BufferFlags: win32more.Windows.Win32.Media.Audio.Apo.APO_BUFFER_FLAGS
    u32Signature: UInt32
class APO_CONNECTION_PROPERTY_V2(Structure):
    property: win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY
    u64QPCTime: UInt64
APO_FLAG = Int32
APO_FLAG_NONE: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG = 0
APO_FLAG_INPLACE: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG = 1
APO_FLAG_SAMPLESPERFRAME_MUST_MATCH: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG = 2
APO_FLAG_FRAMESPERSECOND_MUST_MATCH: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG = 4
APO_FLAG_BITSPERSAMPLE_MUST_MATCH: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG = 8
APO_FLAG_MIXER: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG = 16
APO_FLAG_DEFAULT: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG = 14
APO_LOG_LEVEL = Int32
APO_LOG_LEVEL_ALWAYS: win32more.Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL = 0
APO_LOG_LEVEL_CRITICAL: win32more.Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL = 1
APO_LOG_LEVEL_ERROR: win32more.Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL = 2
APO_LOG_LEVEL_WARNING: win32more.Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL = 3
APO_LOG_LEVEL_INFO: win32more.Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL = 4
APO_LOG_LEVEL_VERBOSE: win32more.Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL = 5
class APO_NOTIFICATION(Structure):
    type: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        audioEndpointVolumeChange: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION
        audioEndpointPropertyChange: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION
        audioSystemEffectsPropertyChange: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION
        audioEndpointVolumeChange2: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION2
        deviceOrientation: win32more.Windows.Win32.Media.Audio.Apo.DEVICE_ORIENTATION_TYPE
        audioMicrophoneBoostChange: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_MICROPHONE_BOOST_NOTIFICATION
class APO_NOTIFICATION_DESCRIPTOR(Structure):
    type: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        audioEndpointVolume: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR
        audioEndpointPropertyChange: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
        audioSystemEffectsPropertyChange: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
        audioMicrophoneBoost: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_MICROPHONE_BOOST_APO_NOTIFICATION_DESCRIPTOR
APO_NOTIFICATION_TYPE = Int32
APO_NOTIFICATION_TYPE_NONE: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE = 0
APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE = 1
APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE = 2
APO_NOTIFICATION_TYPE_SYSTEM_EFFECTS_PROPERTY_CHANGE: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE = 3
APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME2: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE = 4
APO_NOTIFICATION_TYPE_DEVICE_ORIENTATION: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE = 5
APO_NOTIFICATION_TYPE_MICROPHONE_BOOST: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE = 6
class APO_REG_PROPERTIES(Structure):
    clsid: Guid
    Flags: win32more.Windows.Win32.Media.Audio.Apo.APO_FLAG
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
class AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(Structure):
    device: win32more.Windows.Win32.Media.Audio.IMMDevice
class AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION(Structure):
    endpoint: win32more.Windows.Win32.Media.Audio.IMMDevice
    propertyStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    propertyKey: win32more.Windows.Win32.Foundation.PROPERTYKEY
class AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR(Structure):
    device: win32more.Windows.Win32.Media.Audio.IMMDevice
class AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION(Structure):
    endpoint: win32more.Windows.Win32.Media.Audio.IMMDevice
    volume: POINTER(win32more.Windows.Win32.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA)
class AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION2(Structure):
    endpoint: win32more.Windows.Win32.Media.Audio.IMMDevice
    volume: POINTER(win32more.Windows.Win32.Media.Audio.Apo.AUDIO_VOLUME_NOTIFICATION_DATA2)
AUDIO_FLOW_TYPE = Int32
AUDIO_FLOW_PULL: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_FLOW_TYPE = 0
AUDIO_FLOW_PUSH: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_FLOW_TYPE = 1
class AUDIO_MICROPHONE_BOOST_APO_NOTIFICATION_DESCRIPTOR(Structure):
    device: win32more.Windows.Win32.Media.Audio.IMMDevice
class AUDIO_MICROPHONE_BOOST_NOTIFICATION(Structure):
    endpoint: win32more.Windows.Win32.Media.Audio.IMMDevice
    eventContext: Guid
    microphoneBoostEnabled: win32more.Windows.Win32.Foundation.BOOL
    levelInDb: Single
    levelMinInDb: Single
    levelMaxInDb: Single
    levelStepInDb: Single
    muteSupported: win32more.Windows.Win32.Foundation.BOOL
    mute: win32more.Windows.Win32.Foundation.BOOL
class AUDIO_SYSTEMEFFECT(Structure):
    id: Guid
    canSetState: win32more.Windows.Win32.Foundation.BOOL
    state: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE
class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(Structure):
    device: win32more.Windows.Win32.Media.Audio.IMMDevice
    propertyStoreContext: Guid
class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION(Structure):
    endpoint: win32more.Windows.Win32.Media.Audio.IMMDevice
    propertyStoreContext: Guid
    propertyStoreType: win32more.Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE
    propertyStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    propertyKey: win32more.Windows.Win32.Foundation.PROPERTYKEY
AUDIO_SYSTEMEFFECT_STATE = Int32
AUDIO_SYSTEMEFFECT_STATE_OFF: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE = 0
AUDIO_SYSTEMEFFECT_STATE_ON: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE = 1
class AUDIO_VOLUME_NOTIFICATION_DATA2(Structure):
    notificationData: POINTER(win32more.Windows.Win32.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA)
    masterVolumeInDb: Single
    volumeMinInDb: Single
    volumeMaxInDb: Single
    volumeIncrementInDb: Single
    step: UInt32
    stepCount: UInt32
    channelVolumesInDb: Single * 1
APOERR_ALREADY_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2005073919
APOERR_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2005073918
APOERR_FORMAT_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2005073917
APOERR_INVALID_APO_CLSID: win32more.Windows.Win32.Foundation.HRESULT = -2005073916
APOERR_BUFFERS_OVERLAP: win32more.Windows.Win32.Foundation.HRESULT = -2005073915
APOERR_ALREADY_UNLOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2005073914
APOERR_NUM_CONNECTIONS_INVALID: win32more.Windows.Win32.Foundation.HRESULT = -2005073913
APOERR_INVALID_OUTPUT_MAXFRAMECOUNT: win32more.Windows.Win32.Foundation.HRESULT = -2005073912
APOERR_INVALID_CONNECTION_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2005073911
APOERR_APO_LOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2005073910
APOERR_INVALID_COEFFCOUNT: win32more.Windows.Win32.Foundation.HRESULT = -2005073909
APOERR_INVALID_COEFFICIENT: win32more.Windows.Win32.Foundation.HRESULT = -2005073908
APOERR_INVALID_CURVE_PARAM: win32more.Windows.Win32.Foundation.HRESULT = -2005073907
APOERR_INVALID_INPUTID: win32more.Windows.Win32.Foundation.HRESULT = -2005073906
AUDIO_MIN_FRAMERATE: Double = 10
AUDIO_MAX_FRAMERATE: Double = 384000
AUDIO_MIN_CHANNELS: UInt32 = 1
AUDIO_MAX_CHANNELS: UInt32 = 4096
PKEY_FX_Association: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=0)
PKEY_FX_PreMixEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=1)
PKEY_FX_PostMixEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=2)
PKEY_FX_UserInterfaceClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=3)
PKEY_FX_FriendlyName: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=4)
PKEY_FX_StreamEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=5)
PKEY_FX_ModeEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=6)
PKEY_FX_EndpointEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=7)
PKEY_FX_KeywordDetector_StreamEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=8)
PKEY_FX_KeywordDetector_ModeEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=9)
PKEY_FX_KeywordDetector_EndpointEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=10)
PKEY_FX_Offload_StreamEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=11)
PKEY_FX_Offload_ModeEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=12)
PKEY_CompositeFX_StreamEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=13)
PKEY_CompositeFX_ModeEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=14)
PKEY_CompositeFX_EndpointEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=15)
PKEY_CompositeFX_KeywordDetector_StreamEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=16)
PKEY_CompositeFX_KeywordDetector_ModeEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=17)
PKEY_CompositeFX_KeywordDetector_EndpointEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=18)
PKEY_CompositeFX_Offload_StreamEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=19)
PKEY_CompositeFX_Offload_ModeEffectClsid: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=20)
PKEY_FX_SupportAppLauncher: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=21)
PKEY_FX_SupportedFormats: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=22)
PKEY_FX_Enumerator: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=23)
PKEY_FX_VersionMajor: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=24)
PKEY_FX_VersionMinor: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=25)
PKEY_FX_Author: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=26)
PKEY_FX_ObjectId: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=27)
PKEY_FX_State: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=28)
PKEY_FX_EffectPackSchema_Version: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=29)
PKEY_FX_ApplyToBluetooth: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=30)
PKEY_FX_ApplyToUsb: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=31)
PKEY_FX_ApplyToRender: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=32)
PKEY_FX_ApplyToCapture: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d04e05a6-594b-4fb6-a80d-01af5eed7d1d}'), pid=33)
PKEY_SFX_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=5)
PKEY_MFX_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=6)
PKEY_EFX_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=7)
PKEY_SFX_KeywordDetector_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=8)
PKEY_MFX_KeywordDetector_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=9)
PKEY_EFX_KeywordDetector_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=10)
PKEY_SFX_Offload_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=11)
PKEY_MFX_Offload_ProcessingModes_Supported_For_Streaming: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=12)
PKEY_APO_SWFallback_ProcessingModes: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d3993a3f-99c2-4402-b5ec-a92a0367664b}'), pid=13)
PKEY_FX_EffectPack_Schema_V1: Guid = Guid('{7abf23d9-727e-4d0b-86a3-dd501d260001}')
SID_AudioProcessingObjectRTQueue: Guid = Guid('{458c1a1f-6899-4c12-99ac-e2e6ac253104}')
SID_AudioProcessingObjectLoggingService: Guid = Guid('{8b8008af-09f9-456e-a173-bdb58499bce7}')
AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES: UInt32 = 2
AUDIOMEDIATYPE_EQUAL_FORMAT_DATA: UInt32 = 4
AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA: UInt32 = 8
class AudioFXExtensionParams(Structure):
    AddPageParam: win32more.Windows.Win32.Foundation.LPARAM
    pwstrEndpointID: win32more.Windows.Win32.Foundation.PWSTR
    pFxProperties: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
DEVICE_ORIENTATION_TYPE = Int32
DEVICE_NOT_ROTATED: win32more.Windows.Win32.Media.Audio.Apo.DEVICE_ORIENTATION_TYPE = 0
DEVICE_ROTATED_90_DEGREES_CLOCKWISE: win32more.Windows.Win32.Media.Audio.Apo.DEVICE_ORIENTATION_TYPE = 1
DEVICE_ROTATED_180_DEGREES_CLOCKWISE: win32more.Windows.Win32.Media.Audio.Apo.DEVICE_ORIENTATION_TYPE = 2
DEVICE_ROTATED_270_DEGREES_CLOCKWISE: win32more.Windows.Win32.Media.Audio.Apo.DEVICE_ORIENTATION_TYPE = 3
EAudioConstriction = Int32
eAudioConstrictionOff: win32more.Windows.Win32.Media.Audio.Apo.EAudioConstriction = 0
eAudioConstriction48_16: win32more.Windows.Win32.Media.Audio.Apo.EAudioConstriction = 1
eAudioConstriction44_16: win32more.Windows.Win32.Media.Audio.Apo.EAudioConstriction = 2
eAudioConstriction14_14: win32more.Windows.Win32.Media.Audio.Apo.EAudioConstriction = 3
eAudioConstrictionMute: win32more.Windows.Win32.Media.Audio.Apo.EAudioConstriction = 4
@winfunctype_pointer
def FNAPONOTIFICATIONCALLBACK(pProperties: POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_REG_PROPERTIES), pvRefData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApoAcousticEchoCancellation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{25385759-3236-4101-a943-25693dfb5d2d}')
class IApoAuxiliaryInputConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ceb0aab-fa19-48ed-a857-87771ae1b768}')
    @commethod(3)
    def AddAuxiliaryInput(self, dwInputId: UInt32, cbDataSize: UInt32, pbyData: POINTER(Byte), pInputConnection: POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveAuxiliaryInput(self, dwInputId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsInputFormatSupported(self, pRequestedInputFormat: win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType, ppSupportedInputFormat: POINTER(win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApoAuxiliaryInputRT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f851809c-c177-49a0-b1b2-b66f017943ab}')
    @commethod(3)
    def AcceptInput(self, dwInputId: UInt32, pInputConnection: POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY)) -> Void: ...
class IAudioDeviceModulesClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{98f37dac-d0b6-49f5-896a-aa4d169a4c48}')
    @commethod(3)
    def SetAudioDeviceModulesManager(self, pAudioDeviceModulesManager: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioMediaType(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e997f73-b71f-4798-873b-ed7dfcf15b4d}')
    @commethod(3)
    def IsCompressedFormat(self, pfCompressed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsEqual(self, pIAudioType: win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAudioFormat(self) -> POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX): ...
    @commethod(6)
    def GetUncompressedAudioFormat(self, pUncompressedAudioFormat: POINTER(win32more.Windows.Win32.Media.Audio.Apo.UNCOMPRESSEDAUDIOFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd7f2b29-24d0-4b5c-b177-592c39f9ca10}')
    @commethod(3)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLatency(self, pTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRegistrationProperties(self, ppRegProps: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_REG_PROPERTIES))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Initialize(self, cbDataSize: UInt32, pbyData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsInputFormatSupported(self, pOppositeFormat: win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType, pRequestedInputFormat: win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType, ppSupportedInputFormat: POINTER(win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsOutputFormatSupported(self, pOppositeFormat: win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType, pRequestedOutputFormat: win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType, ppSupportedOutputFormat: POINTER(win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInputChannelCount(self, pu32ChannelCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e5ed805-aba6-49c3-8f9a-2b8c889c4fa8}')
    @commethod(3)
    def LockForProcess(self, u32NumInputConnections: UInt32, ppInputConnections: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR)), u32NumOutputConnections: UInt32, ppOutputConnections: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnlockForProcess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectLoggingService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{698f0107-1745-4708-95a5-d84478a62a65}')
    @commethod(3)
    def ApoLog(self, level: win32more.Windows.Win32.Media.Audio.Apo.APO_LOG_LEVEL, format: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
class IAudioProcessingObjectNotifications(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56b0c76f-02fd-4b21-a52e-9f8219fc86e4}')
    @commethod(3)
    def GetApoNotificationRegistrationInfo(self, apoNotifications: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HandleNotification(self, apoNotification: POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION)) -> Void: ...
class IAudioProcessingObjectNotifications2(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.Apo.IAudioProcessingObjectNotifications
    _iid_ = Guid('{ca2cfbde-a9d6-4eb0-bc95-c4d026b380f0}')
    @commethod(5)
    def GetApoNotificationRegistrationInfo2(self, maxApoNotificationTypeSupported: win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_TYPE, apoNotifications: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectRT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9e1d6a6d-ddbc-4e95-a4c7-ad64ba37846c}')
    @commethod(3)
    def APOProcess(self, u32NumInputConnections: UInt32, ppInputConnections: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY)), u32NumOutputConnections: UInt32, ppOutputConnections: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY))) -> Void: ...
    @commethod(4)
    def CalcInputFrames(self, u32OutputFrameCount: UInt32) -> UInt32: ...
    @commethod(5)
    def CalcOutputFrames(self, u32InputFrameCount: UInt32) -> UInt32: ...
class IAudioProcessingObjectRTQueueService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{acd65e2f-955b-4b57-b9bf-ac297bb752c9}')
    @commethod(3)
    def GetRealTimeWorkQueue(self, workQueueId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioProcessingObjectVBR(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ba1db8f-78ad-49cd-9591-f79d80a17c81}')
    @commethod(3)
    def CalcMaxInputFrames(self, u32MaxOutputFrameCount: UInt32, pu32InputFrameCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CalcMaxOutputFrames(self, u32MaxInputFrameCount: UInt32, pu32OutputFrameCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffects(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5fa00f27-add6-499a-8a9d-6b98521fa75b}')
class IAudioSystemEffects2(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.Apo.IAudioSystemEffects
    _iid_ = Guid('{bafe99d2-7436-44ce-9e0e-4d89afbfff56}')
    @commethod(3)
    def GetEffectsList(self, ppEffectsIds: POINTER(POINTER(Guid)), pcEffects: POINTER(UInt32), Event: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffects3(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.Apo.IAudioSystemEffects2
    _iid_ = Guid('{c58b31cd-fc6a-4255-bc1f-ad29bb0a4a17}')
    @commethod(4)
    def GetControllableSystemEffectsList(self, effects: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT)), numEffects: POINTER(UInt32), event: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAudioSystemEffectState(self, effectId: Guid, state: win32more.Windows.Win32.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffectsCustomFormats(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b1176e34-bb7f-4f05-bebd-1b18a534e097}')
    @commethod(3)
    def GetFormatCount(self, pcFormats: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormat(self, nFormat: UInt32, ppFormat: POINTER(win32more.Windows.Win32.Media.Audio.Apo.IAudioMediaType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormatRepresentation(self, nFormat: UInt32, ppwstrFormatRep: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class UNCOMPRESSEDAUDIOFORMAT(Structure):
    guidFormatType: Guid
    dwSamplesPerFrame: UInt32
    dwBytesPerSampleContainer: UInt32
    dwValidBitsPerSample: UInt32
    fFramesPerSecond: Single
    dwChannelMask: UInt32


make_ready(__name__)
