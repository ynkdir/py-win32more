from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Media.Audio
import win32more.Media.Audio.Apo
import win32more.System.Com
import win32more.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
APOERR_ALREADY_INITIALIZED = -2005073919
APOERR_NOT_INITIALIZED = -2005073918
APOERR_FORMAT_NOT_SUPPORTED = -2005073917
APOERR_INVALID_APO_CLSID = -2005073916
APOERR_BUFFERS_OVERLAP = -2005073915
APOERR_ALREADY_UNLOCKED = -2005073914
APOERR_NUM_CONNECTIONS_INVALID = -2005073913
APOERR_INVALID_OUTPUT_MAXFRAMECOUNT = -2005073912
APOERR_INVALID_CONNECTION_FORMAT = -2005073911
APOERR_APO_LOCKED = -2005073910
APOERR_INVALID_COEFFCOUNT = -2005073909
APOERR_INVALID_COEFFICIENT = -2005073908
APOERR_INVALID_CURVE_PARAM = -2005073907
APOERR_INVALID_INPUTID = -2005073906
AUDIO_MIN_FRAMERATE = 10
AUDIO_MAX_FRAMERATE = 384000
AUDIO_MIN_CHANNELS = 1
AUDIO_MAX_CHANNELS = 4096
def _define_PKEY_FX_Association():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=0)
def _define_PKEY_FX_PreMixEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=1)
def _define_PKEY_FX_PostMixEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=2)
def _define_PKEY_FX_UserInterfaceClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=3)
def _define_PKEY_FX_FriendlyName():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=4)
def _define_PKEY_FX_StreamEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=5)
def _define_PKEY_FX_ModeEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=6)
def _define_PKEY_FX_EndpointEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=7)
def _define_PKEY_FX_KeywordDetector_StreamEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=8)
def _define_PKEY_FX_KeywordDetector_ModeEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=9)
def _define_PKEY_FX_KeywordDetector_EndpointEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=10)
def _define_PKEY_FX_Offload_StreamEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=11)
def _define_PKEY_FX_Offload_ModeEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=12)
def _define_PKEY_CompositeFX_StreamEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=13)
def _define_PKEY_CompositeFX_ModeEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=14)
def _define_PKEY_CompositeFX_EndpointEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=15)
def _define_PKEY_CompositeFX_KeywordDetector_StreamEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=16)
def _define_PKEY_CompositeFX_KeywordDetector_ModeEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=17)
def _define_PKEY_CompositeFX_KeywordDetector_EndpointEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=18)
def _define_PKEY_CompositeFX_Offload_StreamEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=19)
def _define_PKEY_CompositeFX_Offload_ModeEffectClsid():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d04e05a6-594b-4fb6-a8-0d-01-af-5e-ed-7d-1d'), pid=20)
def _define_PKEY_SFX_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=5)
def _define_PKEY_MFX_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=6)
def _define_PKEY_EFX_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=7)
def _define_PKEY_SFX_KeywordDetector_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=8)
def _define_PKEY_MFX_KeywordDetector_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=9)
def _define_PKEY_EFX_KeywordDetector_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=10)
def _define_PKEY_SFX_Offload_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=11)
def _define_PKEY_MFX_Offload_ProcessingModes_Supported_For_Streaming():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=12)
def _define_PKEY_APO_SWFallback_ProcessingModes():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d3993a3f-99c2-4402-b5-ec-a9-2a-03-67-66-4b'), pid=13)
def _define_SID_AudioProcessingObjectRTQueue():
    return Guid('458c1a1f-6899-4c12-99-ac-e2-e6-ac-25-31-04')
def _define_SID_AudioProcessingObjectLoggingService():
    return Guid('8b8008af-09f9-456e-a1-73-bd-b5-84-99-bc-e7')
AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES = 2
AUDIOMEDIATYPE_EQUAL_FORMAT_DATA = 4
AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA = 8
APO_BUFFER_FLAGS = Int32
BUFFER_INVALID = 0
BUFFER_VALID = 1
BUFFER_SILENT = 2
APO_CONNECTION_BUFFER_TYPE = Int32
APO_CONNECTION_BUFFER_TYPE_ALLOCATED = 0
APO_CONNECTION_BUFFER_TYPE_EXTERNAL = 1
APO_CONNECTION_BUFFER_TYPE_DEPENDANT = 2
def _define_APO_CONNECTION_DESCRIPTOR_head():
    class APO_CONNECTION_DESCRIPTOR(Structure):
        pass
    return APO_CONNECTION_DESCRIPTOR
def _define_APO_CONNECTION_DESCRIPTOR():
    APO_CONNECTION_DESCRIPTOR = win32more.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head
    APO_CONNECTION_DESCRIPTOR._fields_ = [
        ('Type', win32more.Media.Audio.Apo.APO_CONNECTION_BUFFER_TYPE),
        ('pBuffer', UIntPtr),
        ('u32MaxFrameCount', UInt32),
        ('pFormat', win32more.Media.Audio.Apo.IAudioMediaType_head),
        ('u32Signature', UInt32),
    ]
    return APO_CONNECTION_DESCRIPTOR
def _define_APO_CONNECTION_PROPERTY_head():
    class APO_CONNECTION_PROPERTY(Structure):
        pass
    return APO_CONNECTION_PROPERTY
def _define_APO_CONNECTION_PROPERTY():
    APO_CONNECTION_PROPERTY = win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head
    APO_CONNECTION_PROPERTY._fields_ = [
        ('pBuffer', UIntPtr),
        ('u32ValidFrameCount', UInt32),
        ('u32BufferFlags', win32more.Media.Audio.Apo.APO_BUFFER_FLAGS),
        ('u32Signature', UInt32),
    ]
    return APO_CONNECTION_PROPERTY
def _define_APO_CONNECTION_PROPERTY_V2_head():
    class APO_CONNECTION_PROPERTY_V2(Structure):
        pass
    return APO_CONNECTION_PROPERTY_V2
def _define_APO_CONNECTION_PROPERTY_V2():
    APO_CONNECTION_PROPERTY_V2 = win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_V2_head
    APO_CONNECTION_PROPERTY_V2._fields_ = [
        ('property', win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY),
        ('u64QPCTime', UInt64),
    ]
    return APO_CONNECTION_PROPERTY_V2
APO_FLAG = Int32
APO_FLAG_NONE = 0
APO_FLAG_INPLACE = 1
APO_FLAG_SAMPLESPERFRAME_MUST_MATCH = 2
APO_FLAG_FRAMESPERSECOND_MUST_MATCH = 4
APO_FLAG_BITSPERSAMPLE_MUST_MATCH = 8
APO_FLAG_MIXER = 16
APO_FLAG_DEFAULT = 14
APO_LOG_LEVEL = Int32
APO_LOG_LEVEL_ALWAYS = 0
APO_LOG_LEVEL_CRITICAL = 1
APO_LOG_LEVEL_ERROR = 2
APO_LOG_LEVEL_WARNING = 3
APO_LOG_LEVEL_INFO = 4
APO_LOG_LEVEL_VERBOSE = 5
def _define_APO_NOTIFICATION_head():
    class APO_NOTIFICATION(Structure):
        pass
    return APO_NOTIFICATION
def _define_APO_NOTIFICATION():
    APO_NOTIFICATION = win32more.Media.Audio.Apo.APO_NOTIFICATION_head
    class APO_NOTIFICATION__Anonymous_e__Union(Union):
        pass
    APO_NOTIFICATION__Anonymous_e__Union._fields_ = [
        ('audioEndpointVolumeChange', win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION),
        ('audioEndpointPropertyChange', win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION),
        ('audioSystemEffectsPropertyChange', win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION),
    ]
    APO_NOTIFICATION._anonymous_ = [
        'Anonymous',
    ]
    APO_NOTIFICATION._fields_ = [
        ('type', win32more.Media.Audio.Apo.APO_NOTIFICATION_TYPE),
        ('Anonymous', APO_NOTIFICATION__Anonymous_e__Union),
    ]
    return APO_NOTIFICATION
def _define_APO_NOTIFICATION_DESCRIPTOR_head():
    class APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return APO_NOTIFICATION_DESCRIPTOR
def _define_APO_NOTIFICATION_DESCRIPTOR():
    APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR_head
    class APO_NOTIFICATION_DESCRIPTOR__Anonymous_e__Union(Union):
        pass
    APO_NOTIFICATION_DESCRIPTOR__Anonymous_e__Union._fields_ = [
        ('audioEndpointVolume', win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR),
        ('audioEndpointPropertyChange', win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR),
        ('audioSystemEffectsPropertyChange', win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR),
    ]
    APO_NOTIFICATION_DESCRIPTOR._anonymous_ = [
        'Anonymous',
    ]
    APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ('type', win32more.Media.Audio.Apo.APO_NOTIFICATION_TYPE),
        ('Anonymous', APO_NOTIFICATION_DESCRIPTOR__Anonymous_e__Union),
    ]
    return APO_NOTIFICATION_DESCRIPTOR
APO_NOTIFICATION_TYPE = Int32
APO_NOTIFICATION_TYPE_NONE = 0
APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME = 1
APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE = 2
APO_NOTIFICATION_TYPE_SYSTEM_EFFECTS_PROPERTY_CHANGE = 3
def _define_APO_REG_PROPERTIES_head():
    class APO_REG_PROPERTIES(Structure):
        pass
    return APO_REG_PROPERTIES
def _define_APO_REG_PROPERTIES():
    APO_REG_PROPERTIES = win32more.Media.Audio.Apo.APO_REG_PROPERTIES_head
    APO_REG_PROPERTIES._fields_ = [
        ('clsid', Guid),
        ('Flags', win32more.Media.Audio.Apo.APO_FLAG),
        ('szFriendlyName', Char * 256),
        ('szCopyrightInfo', Char * 256),
        ('u32MajorVersion', UInt32),
        ('u32MinorVersion', UInt32),
        ('u32MinInputConnections', UInt32),
        ('u32MaxInputConnections', UInt32),
        ('u32MinOutputConnections', UInt32),
        ('u32MaxOutputConnections', UInt32),
        ('u32MaxInstances', UInt32),
        ('u32NumAPOInterfaces', UInt32),
        ('iidAPOInterfaceList', Guid * 1),
    ]
    return APO_REG_PROPERTIES
def _define_APOInitBaseStruct_head():
    class APOInitBaseStruct(Structure):
        pass
    return APOInitBaseStruct
def _define_APOInitBaseStruct():
    APOInitBaseStruct = win32more.Media.Audio.Apo.APOInitBaseStruct_head
    APOInitBaseStruct._fields_ = [
        ('cbSize', UInt32),
        ('clsid', Guid),
    ]
    return APOInitBaseStruct
def _define_APOInitSystemEffects_head():
    class APOInitSystemEffects(Structure):
        pass
    return APOInitSystemEffects
def _define_APOInitSystemEffects():
    APOInitSystemEffects = win32more.Media.Audio.Apo.APOInitSystemEffects_head
    APOInitSystemEffects._fields_ = [
        ('APOInit', win32more.Media.Audio.Apo.APOInitBaseStruct),
        ('pAPOEndpointProperties', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ('pAPOSystemEffectsProperties', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ('pReserved', c_void_p),
        ('pDeviceCollection', win32more.Media.Audio.IMMDeviceCollection_head),
    ]
    return APOInitSystemEffects
def _define_APOInitSystemEffects2_head():
    class APOInitSystemEffects2(Structure):
        pass
    return APOInitSystemEffects2
def _define_APOInitSystemEffects2():
    APOInitSystemEffects2 = win32more.Media.Audio.Apo.APOInitSystemEffects2_head
    APOInitSystemEffects2._fields_ = [
        ('APOInit', win32more.Media.Audio.Apo.APOInitBaseStruct),
        ('pAPOEndpointProperties', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ('pAPOSystemEffectsProperties', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ('pReserved', c_void_p),
        ('pDeviceCollection', win32more.Media.Audio.IMMDeviceCollection_head),
        ('nSoftwareIoDeviceInCollection', UInt32),
        ('nSoftwareIoConnectorIndex', UInt32),
        ('AudioProcessingMode', Guid),
        ('InitializeForDiscoveryOnly', win32more.Foundation.BOOL),
    ]
    return APOInitSystemEffects2
def _define_APOInitSystemEffects3_head():
    class APOInitSystemEffects3(Structure):
        pass
    return APOInitSystemEffects3
def _define_APOInitSystemEffects3():
    APOInitSystemEffects3 = win32more.Media.Audio.Apo.APOInitSystemEffects3_head
    APOInitSystemEffects3._fields_ = [
        ('APOInit', win32more.Media.Audio.Apo.APOInitBaseStruct),
        ('pAPOEndpointProperties', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ('pServiceProvider', win32more.System.Com.IServiceProvider_head),
        ('pDeviceCollection', win32more.Media.Audio.IMMDeviceCollection_head),
        ('nSoftwareIoDeviceInCollection', UInt32),
        ('nSoftwareIoConnectorIndex', UInt32),
        ('AudioProcessingMode', Guid),
        ('InitializeForDiscoveryOnly', win32more.Foundation.BOOL),
    ]
    return APOInitSystemEffects3
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head():
    class AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR():
    AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head
    AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ('device', win32more.Media.Audio.IMMDevice_head),
    ]
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION_head():
    class AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION(Structure):
        pass
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION():
    AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION_head
    AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION._fields_ = [
        ('endpoint', win32more.Media.Audio.IMMDevice_head),
        ('propertyStore', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ('propertyKey', win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
    ]
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION
def _define_AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR_head():
    class AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR():
    AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR_head
    AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ('device', win32more.Media.Audio.IMMDevice_head),
    ]
    return AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION_head():
    class AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION(Structure):
        pass
    return AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION
def _define_AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION():
    AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION_head
    AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION._fields_ = [
        ('endpoint', win32more.Media.Audio.IMMDevice_head),
        ('volume', POINTER(win32more.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA_head)),
    ]
    return AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION
AUDIO_FLOW_TYPE = Int32
AUDIO_FLOW_PULL = 0
AUDIO_FLOW_PUSH = 1
def _define_AUDIO_SYSTEMEFFECT_head():
    class AUDIO_SYSTEMEFFECT(Structure):
        pass
    return AUDIO_SYSTEMEFFECT
def _define_AUDIO_SYSTEMEFFECT():
    AUDIO_SYSTEMEFFECT = win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_head
    AUDIO_SYSTEMEFFECT._fields_ = [
        ('id', Guid),
        ('canSetState', win32more.Foundation.BOOL),
        ('state', win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE),
    ]
    return AUDIO_SYSTEMEFFECT
AUDIO_SYSTEMEFFECT_STATE = Int32
AUDIO_SYSTEMEFFECT_STATE_OFF = 0
AUDIO_SYSTEMEFFECT_STATE_ON = 1
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head():
    class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR():
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ('device', win32more.Media.Audio.IMMDevice_head),
        ('propertyStoreContext', Guid),
    ]
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION_head():
    class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION(Structure):
        pass
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION():
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION = win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION_head
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION._fields_ = [
        ('endpoint', win32more.Media.Audio.IMMDevice_head),
        ('propertyStoreContext', Guid),
        ('propertyStoreType', win32more.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE),
        ('propertyStore', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ('propertyKey', win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
    ]
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION
def _define_AudioFXExtensionParams_head():
    class AudioFXExtensionParams(Structure):
        pass
    return AudioFXExtensionParams
def _define_AudioFXExtensionParams():
    AudioFXExtensionParams = win32more.Media.Audio.Apo.AudioFXExtensionParams_head
    AudioFXExtensionParams._fields_ = [
        ('AddPageParam', win32more.Foundation.LPARAM),
        ('pwstrEndpointID', win32more.Foundation.PWSTR),
        ('pFxProperties', win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
    ]
    return AudioFXExtensionParams
EAudioConstriction = Int32
EAudioConstriction_eAudioConstrictionOff = 0
EAudioConstriction_eAudioConstriction48_16 = 1
EAudioConstriction_eAudioConstriction44_16 = 2
EAudioConstriction_eAudioConstriction14_14 = 3
EAudioConstriction_eAudioConstrictionMute = 4
def _define_FNAPONOTIFICATIONCALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.Apo.APO_REG_PROPERTIES_head),c_void_p)
def _define_IApoAcousticEchoCancellation_head():
    class IApoAcousticEchoCancellation(win32more.System.Com.IUnknown_head):
        Guid = Guid('25385759-3236-4101-a9-43-25-69-3d-fb-5d-2d')
    return IApoAcousticEchoCancellation
def _define_IApoAcousticEchoCancellation():
    IApoAcousticEchoCancellation = win32more.Media.Audio.Apo.IApoAcousticEchoCancellation_head
    win32more.System.Com.IUnknown
    return IApoAcousticEchoCancellation
def _define_IApoAuxiliaryInputConfiguration_head():
    class IApoAuxiliaryInputConfiguration(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ceb0aab-fa19-48ed-a8-57-87-77-1a-e1-b7-68')
    return IApoAuxiliaryInputConfiguration
def _define_IApoAuxiliaryInputConfiguration():
    IApoAuxiliaryInputConfiguration = win32more.Media.Audio.Apo.IApoAuxiliaryInputConfiguration_head
    IApoAuxiliaryInputConfiguration.AddAuxiliaryInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_char_p_no,POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head))(3, 'AddAuxiliaryInput', ((1, 'dwInputId'),(1, 'cbDataSize'),(1, 'pbyData'),(1, 'pInputConnection'),)))
    IApoAuxiliaryInputConfiguration.RemoveAuxiliaryInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'RemoveAuxiliaryInput', ((1, 'dwInputId'),)))
    IApoAuxiliaryInputConfiguration.IsInputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head))(5, 'IsInputFormatSupported', ((1, 'pRequestedInputFormat'),(1, 'ppSupportedInputFormat'),)))
    win32more.System.Com.IUnknown
    return IApoAuxiliaryInputConfiguration
def _define_IApoAuxiliaryInputRT_head():
    class IApoAuxiliaryInputRT(win32more.System.Com.IUnknown_head):
        Guid = Guid('f851809c-c177-49a0-b1-b2-b6-6f-01-79-43-ab')
    return IApoAuxiliaryInputRT
def _define_IApoAuxiliaryInputRT():
    IApoAuxiliaryInputRT = win32more.Media.Audio.Apo.IApoAuxiliaryInputRT_head
    IApoAuxiliaryInputRT.AcceptInput = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head))(3, 'AcceptInput', ((1, 'dwInputId'),(1, 'pInputConnection'),)))
    win32more.System.Com.IUnknown
    return IApoAuxiliaryInputRT
def _define_IAudioDeviceModulesClient_head():
    class IAudioDeviceModulesClient(win32more.System.Com.IUnknown_head):
        Guid = Guid('98f37dac-d0b6-49f5-89-6a-aa-4d-16-9a-4c-48')
    return IAudioDeviceModulesClient
def _define_IAudioDeviceModulesClient():
    IAudioDeviceModulesClient = win32more.Media.Audio.Apo.IAudioDeviceModulesClient_head
    IAudioDeviceModulesClient.SetAudioDeviceModulesManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'SetAudioDeviceModulesManager', ((1, 'pAudioDeviceModulesManager'),)))
    win32more.System.Com.IUnknown
    return IAudioDeviceModulesClient
def _define_IAudioMediaType_head():
    class IAudioMediaType(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e997f73-b71f-4798-87-3b-ed-7d-fc-f1-5b-4d')
    return IAudioMediaType
def _define_IAudioMediaType():
    IAudioMediaType = win32more.Media.Audio.Apo.IAudioMediaType_head
    IAudioMediaType.IsCompressedFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'IsCompressedFormat', ((1, 'pfCompressed'),)))
    IAudioMediaType.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(UInt32))(4, 'IsEqual', ((1, 'pIAudioType'),(1, 'pdwFlags'),)))
    IAudioMediaType.GetAudioFormat = COMMETHOD(WINFUNCTYPE(POINTER(win32more.Media.Audio.WAVEFORMATEX_head),)(5, 'GetAudioFormat', ()))
    IAudioMediaType.GetUncompressedAudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.Apo.UNCOMPRESSEDAUDIOFORMAT_head))(6, 'GetUncompressedAudioFormat', ((1, 'pUncompressedAudioFormat'),)))
    win32more.System.Com.IUnknown
    return IAudioMediaType
def _define_IAudioProcessingObject_head():
    class IAudioProcessingObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd7f2b29-24d0-4b5c-b1-77-59-2c-39-f9-ca-10')
    return IAudioProcessingObject
def _define_IAudioProcessingObject():
    IAudioProcessingObject = win32more.Media.Audio.Apo.IAudioProcessingObject_head
    IAudioProcessingObject.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Reset', ()))
    IAudioProcessingObject.GetLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(4, 'GetLatency', ((1, 'pTime'),)))
    IAudioProcessingObject.GetRegistrationProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.Apo.APO_REG_PROPERTIES_head)))(5, 'GetRegistrationProperties', ((1, 'ppRegProps'),)))
    IAudioProcessingObject.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no)(6, 'Initialize', ((1, 'cbDataSize'),(1, 'pbyData'),)))
    IAudioProcessingObject.IsInputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head))(7, 'IsInputFormatSupported', ((1, 'pOppositeFormat'),(1, 'pRequestedInputFormat'),(1, 'ppSupportedInputFormat'),)))
    IAudioProcessingObject.IsOutputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head))(8, 'IsOutputFormatSupported', ((1, 'pOppositeFormat'),(1, 'pRequestedOutputFormat'),(1, 'ppSupportedOutputFormat'),)))
    IAudioProcessingObject.GetInputChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetInputChannelCount', ((1, 'pu32ChannelCount'),)))
    win32more.System.Com.IUnknown
    return IAudioProcessingObject
def _define_IAudioProcessingObjectConfiguration_head():
    class IAudioProcessingObjectConfiguration(win32more.System.Com.IUnknown_head):
        Guid = Guid('0e5ed805-aba6-49c3-8f-9a-2b-8c-88-9c-4f-a8')
    return IAudioProcessingObjectConfiguration
def _define_IAudioProcessingObjectConfiguration():
    IAudioProcessingObjectConfiguration = win32more.Media.Audio.Apo.IAudioProcessingObjectConfiguration_head
    IAudioProcessingObjectConfiguration.LockForProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head)),UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head)))(3, 'LockForProcess', ((1, 'u32NumInputConnections'),(1, 'ppInputConnections'),(1, 'u32NumOutputConnections'),(1, 'ppOutputConnections'),)))
    IAudioProcessingObjectConfiguration.UnlockForProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'UnlockForProcess', ()))
    win32more.System.Com.IUnknown
    return IAudioProcessingObjectConfiguration
def _define_IAudioProcessingObjectLoggingService_head():
    class IAudioProcessingObjectLoggingService(win32more.System.Com.IUnknown_head):
        Guid = Guid('698f0107-1745-4708-95-a5-d8-44-78-a6-2a-65')
    return IAudioProcessingObjectLoggingService
def _define_IAudioProcessingObjectLoggingService():
    IAudioProcessingObjectLoggingService = win32more.Media.Audio.Apo.IAudioProcessingObjectLoggingService_head
    IAudioProcessingObjectLoggingService.ApoLog = COMMETHOD(WINFUNCTYPE(Void,win32more.Media.Audio.Apo.APO_LOG_LEVEL,win32more.Foundation.PWSTR)(3, 'ApoLog', ((1, 'level'),(1, 'format'),)))
    win32more.System.Com.IUnknown
    return IAudioProcessingObjectLoggingService
def _define_IAudioProcessingObjectNotifications_head():
    class IAudioProcessingObjectNotifications(win32more.System.Com.IUnknown_head):
        Guid = Guid('56b0c76f-02fd-4b21-a5-2e-9f-82-19-fc-86-e4')
    return IAudioProcessingObjectNotifications
def _define_IAudioProcessingObjectNotifications():
    IAudioProcessingObjectNotifications = win32more.Media.Audio.Apo.IAudioProcessingObjectNotifications_head
    IAudioProcessingObjectNotifications.GetApoNotificationRegistrationInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR_head)),POINTER(UInt32))(3, 'GetApoNotificationRegistrationInfo', ((1, 'apoNotifications'),(1, 'count'),)))
    IAudioProcessingObjectNotifications.HandleNotification = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.Apo.APO_NOTIFICATION_head))(4, 'HandleNotification', ((1, 'apoNotification'),)))
    win32more.System.Com.IUnknown
    return IAudioProcessingObjectNotifications
def _define_IAudioProcessingObjectRT_head():
    class IAudioProcessingObjectRT(win32more.System.Com.IUnknown_head):
        Guid = Guid('9e1d6a6d-ddbc-4e95-a4-c7-ad-64-ba-37-84-6c')
    return IAudioProcessingObjectRT
def _define_IAudioProcessingObjectRT():
    IAudioProcessingObjectRT = win32more.Media.Audio.Apo.IAudioProcessingObjectRT_head
    IAudioProcessingObjectRT.APOProcess = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)),UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)))(3, 'APOProcess', ((1, 'u32NumInputConnections'),(1, 'ppInputConnections'),(1, 'u32NumOutputConnections'),(1, 'ppOutputConnections'),)))
    IAudioProcessingObjectRT.CalcInputFrames = COMMETHOD(WINFUNCTYPE(UInt32,UInt32)(4, 'CalcInputFrames', ((1, 'u32OutputFrameCount'),)))
    IAudioProcessingObjectRT.CalcOutputFrames = COMMETHOD(WINFUNCTYPE(UInt32,UInt32)(5, 'CalcOutputFrames', ((1, 'u32InputFrameCount'),)))
    win32more.System.Com.IUnknown
    return IAudioProcessingObjectRT
def _define_IAudioProcessingObjectRTQueueService_head():
    class IAudioProcessingObjectRTQueueService(win32more.System.Com.IUnknown_head):
        Guid = Guid('acd65e2f-955b-4b57-b9-bf-ac-29-7b-b7-52-c9')
    return IAudioProcessingObjectRTQueueService
def _define_IAudioProcessingObjectRTQueueService():
    IAudioProcessingObjectRTQueueService = win32more.Media.Audio.Apo.IAudioProcessingObjectRTQueueService_head
    IAudioProcessingObjectRTQueueService.GetRealTimeWorkQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetRealTimeWorkQueue', ((1, 'workQueueId'),)))
    win32more.System.Com.IUnknown
    return IAudioProcessingObjectRTQueueService
def _define_IAudioProcessingObjectVBR_head():
    class IAudioProcessingObjectVBR(win32more.System.Com.IUnknown_head):
        Guid = Guid('7ba1db8f-78ad-49cd-95-91-f7-9d-80-a1-7c-81')
    return IAudioProcessingObjectVBR
def _define_IAudioProcessingObjectVBR():
    IAudioProcessingObjectVBR = win32more.Media.Audio.Apo.IAudioProcessingObjectVBR_head
    IAudioProcessingObjectVBR.CalcMaxInputFrames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(3, 'CalcMaxInputFrames', ((1, 'u32MaxOutputFrameCount'),(1, 'pu32InputFrameCount'),)))
    IAudioProcessingObjectVBR.CalcMaxOutputFrames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(4, 'CalcMaxOutputFrames', ((1, 'u32MaxInputFrameCount'),(1, 'pu32OutputFrameCount'),)))
    win32more.System.Com.IUnknown
    return IAudioProcessingObjectVBR
def _define_IAudioSystemEffects_head():
    class IAudioSystemEffects(win32more.System.Com.IUnknown_head):
        Guid = Guid('5fa00f27-add6-499a-8a-9d-6b-98-52-1f-a7-5b')
    return IAudioSystemEffects
def _define_IAudioSystemEffects():
    IAudioSystemEffects = win32more.Media.Audio.Apo.IAudioSystemEffects_head
    win32more.System.Com.IUnknown
    return IAudioSystemEffects
def _define_IAudioSystemEffects2_head():
    class IAudioSystemEffects2(win32more.Media.Audio.Apo.IAudioSystemEffects_head):
        Guid = Guid('bafe99d2-7436-44ce-9e-0e-4d-89-af-bf-ff-56')
    return IAudioSystemEffects2
def _define_IAudioSystemEffects2():
    IAudioSystemEffects2 = win32more.Media.Audio.Apo.IAudioSystemEffects2_head
    IAudioSystemEffects2.GetEffectsList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),POINTER(UInt32),win32more.Foundation.HANDLE)(3, 'GetEffectsList', ((1, 'ppEffectsIds'),(1, 'pcEffects'),(1, 'Event'),)))
    win32more.Media.Audio.Apo.IAudioSystemEffects
    return IAudioSystemEffects2
def _define_IAudioSystemEffects3_head():
    class IAudioSystemEffects3(win32more.Media.Audio.Apo.IAudioSystemEffects2_head):
        Guid = Guid('c58b31cd-fc6a-4255-bc-1f-ad-29-bb-0a-4a-17')
    return IAudioSystemEffects3
def _define_IAudioSystemEffects3():
    IAudioSystemEffects3 = win32more.Media.Audio.Apo.IAudioSystemEffects3_head
    IAudioSystemEffects3.GetControllableSystemEffectsList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_head)),POINTER(UInt32),win32more.Foundation.HANDLE)(4, 'GetControllableSystemEffectsList', ((1, 'effects'),(1, 'numEffects'),(1, 'event'),)))
    IAudioSystemEffects3.SetAudioSystemEffectState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE)(5, 'SetAudioSystemEffectState', ((1, 'effectId'),(1, 'state'),)))
    win32more.Media.Audio.Apo.IAudioSystemEffects2
    return IAudioSystemEffects3
def _define_IAudioSystemEffectsCustomFormats_head():
    class IAudioSystemEffectsCustomFormats(win32more.System.Com.IUnknown_head):
        Guid = Guid('b1176e34-bb7f-4f05-be-bd-1b-18-a5-34-e0-97')
    return IAudioSystemEffectsCustomFormats
def _define_IAudioSystemEffectsCustomFormats():
    IAudioSystemEffectsCustomFormats = win32more.Media.Audio.Apo.IAudioSystemEffectsCustomFormats_head
    IAudioSystemEffectsCustomFormats.GetFormatCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetFormatCount', ((1, 'pcFormats'),)))
    IAudioSystemEffectsCustomFormats.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head))(4, 'GetFormat', ((1, 'nFormat'),(1, 'ppFormat'),)))
    IAudioSystemEffectsCustomFormats.GetFormatRepresentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR))(5, 'GetFormatRepresentation', ((1, 'nFormat'),(1, 'ppwstrFormatRep'),)))
    win32more.System.Com.IUnknown
    return IAudioSystemEffectsCustomFormats
def _define_UNCOMPRESSEDAUDIOFORMAT_head():
    class UNCOMPRESSEDAUDIOFORMAT(Structure):
        pass
    return UNCOMPRESSEDAUDIOFORMAT
def _define_UNCOMPRESSEDAUDIOFORMAT():
    UNCOMPRESSEDAUDIOFORMAT = win32more.Media.Audio.Apo.UNCOMPRESSEDAUDIOFORMAT_head
    UNCOMPRESSEDAUDIOFORMAT._fields_ = [
        ('guidFormatType', Guid),
        ('dwSamplesPerFrame', UInt32),
        ('dwBytesPerSampleContainer', UInt32),
        ('dwValidBitsPerSample', UInt32),
        ('fFramesPerSecond', Single),
        ('dwChannelMask', UInt32),
    ]
    return UNCOMPRESSEDAUDIOFORMAT
__all__ = [
    "APOERR_ALREADY_INITIALIZED",
    "APOERR_ALREADY_UNLOCKED",
    "APOERR_APO_LOCKED",
    "APOERR_BUFFERS_OVERLAP",
    "APOERR_FORMAT_NOT_SUPPORTED",
    "APOERR_INVALID_APO_CLSID",
    "APOERR_INVALID_COEFFCOUNT",
    "APOERR_INVALID_COEFFICIENT",
    "APOERR_INVALID_CONNECTION_FORMAT",
    "APOERR_INVALID_CURVE_PARAM",
    "APOERR_INVALID_INPUTID",
    "APOERR_INVALID_OUTPUT_MAXFRAMECOUNT",
    "APOERR_NOT_INITIALIZED",
    "APOERR_NUM_CONNECTIONS_INVALID",
    "APOInitBaseStruct",
    "APOInitSystemEffects",
    "APOInitSystemEffects2",
    "APOInitSystemEffects3",
    "APO_BUFFER_FLAGS",
    "APO_CONNECTION_BUFFER_TYPE",
    "APO_CONNECTION_BUFFER_TYPE_ALLOCATED",
    "APO_CONNECTION_BUFFER_TYPE_DEPENDANT",
    "APO_CONNECTION_BUFFER_TYPE_EXTERNAL",
    "APO_CONNECTION_DESCRIPTOR",
    "APO_CONNECTION_PROPERTY",
    "APO_CONNECTION_PROPERTY_V2",
    "APO_FLAG",
    "APO_FLAG_BITSPERSAMPLE_MUST_MATCH",
    "APO_FLAG_DEFAULT",
    "APO_FLAG_FRAMESPERSECOND_MUST_MATCH",
    "APO_FLAG_INPLACE",
    "APO_FLAG_MIXER",
    "APO_FLAG_NONE",
    "APO_FLAG_SAMPLESPERFRAME_MUST_MATCH",
    "APO_LOG_LEVEL",
    "APO_LOG_LEVEL_ALWAYS",
    "APO_LOG_LEVEL_CRITICAL",
    "APO_LOG_LEVEL_ERROR",
    "APO_LOG_LEVEL_INFO",
    "APO_LOG_LEVEL_VERBOSE",
    "APO_LOG_LEVEL_WARNING",
    "APO_NOTIFICATION",
    "APO_NOTIFICATION_DESCRIPTOR",
    "APO_NOTIFICATION_TYPE",
    "APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE",
    "APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME",
    "APO_NOTIFICATION_TYPE_NONE",
    "APO_NOTIFICATION_TYPE_SYSTEM_EFFECTS_PROPERTY_CHANGE",
    "APO_REG_PROPERTIES",
    "AUDIOMEDIATYPE_EQUAL_FORMAT_DATA",
    "AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES",
    "AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA",
    "AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR",
    "AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION",
    "AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR",
    "AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION",
    "AUDIO_FLOW_PULL",
    "AUDIO_FLOW_PUSH",
    "AUDIO_FLOW_TYPE",
    "AUDIO_MAX_CHANNELS",
    "AUDIO_MAX_FRAMERATE",
    "AUDIO_MIN_CHANNELS",
    "AUDIO_MIN_FRAMERATE",
    "AUDIO_SYSTEMEFFECT",
    "AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR",
    "AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION",
    "AUDIO_SYSTEMEFFECT_STATE",
    "AUDIO_SYSTEMEFFECT_STATE_OFF",
    "AUDIO_SYSTEMEFFECT_STATE_ON",
    "AudioFXExtensionParams",
    "BUFFER_INVALID",
    "BUFFER_SILENT",
    "BUFFER_VALID",
    "EAudioConstriction",
    "EAudioConstriction_eAudioConstriction14_14",
    "EAudioConstriction_eAudioConstriction44_16",
    "EAudioConstriction_eAudioConstriction48_16",
    "EAudioConstriction_eAudioConstrictionMute",
    "EAudioConstriction_eAudioConstrictionOff",
    "FNAPONOTIFICATIONCALLBACK",
    "IApoAcousticEchoCancellation",
    "IApoAuxiliaryInputConfiguration",
    "IApoAuxiliaryInputRT",
    "IAudioDeviceModulesClient",
    "IAudioMediaType",
    "IAudioProcessingObject",
    "IAudioProcessingObjectConfiguration",
    "IAudioProcessingObjectLoggingService",
    "IAudioProcessingObjectNotifications",
    "IAudioProcessingObjectRT",
    "IAudioProcessingObjectRTQueueService",
    "IAudioProcessingObjectVBR",
    "IAudioSystemEffects",
    "IAudioSystemEffects2",
    "IAudioSystemEffects3",
    "IAudioSystemEffectsCustomFormats",
    "PKEY_APO_SWFallback_ProcessingModes",
    "PKEY_CompositeFX_EndpointEffectClsid",
    "PKEY_CompositeFX_KeywordDetector_EndpointEffectClsid",
    "PKEY_CompositeFX_KeywordDetector_ModeEffectClsid",
    "PKEY_CompositeFX_KeywordDetector_StreamEffectClsid",
    "PKEY_CompositeFX_ModeEffectClsid",
    "PKEY_CompositeFX_Offload_ModeEffectClsid",
    "PKEY_CompositeFX_Offload_StreamEffectClsid",
    "PKEY_CompositeFX_StreamEffectClsid",
    "PKEY_EFX_KeywordDetector_ProcessingModes_Supported_For_Streaming",
    "PKEY_EFX_ProcessingModes_Supported_For_Streaming",
    "PKEY_FX_Association",
    "PKEY_FX_EndpointEffectClsid",
    "PKEY_FX_FriendlyName",
    "PKEY_FX_KeywordDetector_EndpointEffectClsid",
    "PKEY_FX_KeywordDetector_ModeEffectClsid",
    "PKEY_FX_KeywordDetector_StreamEffectClsid",
    "PKEY_FX_ModeEffectClsid",
    "PKEY_FX_Offload_ModeEffectClsid",
    "PKEY_FX_Offload_StreamEffectClsid",
    "PKEY_FX_PostMixEffectClsid",
    "PKEY_FX_PreMixEffectClsid",
    "PKEY_FX_StreamEffectClsid",
    "PKEY_FX_UserInterfaceClsid",
    "PKEY_MFX_KeywordDetector_ProcessingModes_Supported_For_Streaming",
    "PKEY_MFX_Offload_ProcessingModes_Supported_For_Streaming",
    "PKEY_MFX_ProcessingModes_Supported_For_Streaming",
    "PKEY_SFX_KeywordDetector_ProcessingModes_Supported_For_Streaming",
    "PKEY_SFX_Offload_ProcessingModes_Supported_For_Streaming",
    "PKEY_SFX_ProcessingModes_Supported_For_Streaming",
    "SID_AudioProcessingObjectLoggingService",
    "SID_AudioProcessingObjectRTQueue",
    "UNCOMPRESSEDAUDIOFORMAT",
]
