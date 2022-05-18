from win32more import *
import win32more.Foundation
import win32more.Media.Audio
import win32more.Media.Audio.Apo
import win32more.System.Com
import win32more.UI.Shell.PropertiesSystem

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
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
SID_AudioProcessingObjectRTQueue = '458c1a1f-6899-4c12-99ac-e2e6ac253104'
SID_AudioProcessingObjectLoggingService = '8b8008af-09f9-456e-a173-bdb58499bce7'
AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES = 2
AUDIOMEDIATYPE_EQUAL_FORMAT_DATA = 4
AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA = 8
def _define_UNCOMPRESSEDAUDIOFORMAT_head():
    class UNCOMPRESSEDAUDIOFORMAT(Structure):
        pass
    return UNCOMPRESSEDAUDIOFORMAT
def _define_UNCOMPRESSEDAUDIOFORMAT():
    UNCOMPRESSEDAUDIOFORMAT = win32more.Media.Audio.Apo.UNCOMPRESSEDAUDIOFORMAT_head
    UNCOMPRESSEDAUDIOFORMAT._fields_ = [
        ("guidFormatType", Guid),
        ("dwSamplesPerFrame", UInt32),
        ("dwBytesPerSampleContainer", UInt32),
        ("dwValidBitsPerSample", UInt32),
        ("fFramesPerSecond", Single),
        ("dwChannelMask", UInt32),
    ]
    return UNCOMPRESSEDAUDIOFORMAT
def _define_IAudioMediaType_head():
    class IAudioMediaType(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e997f73-b71f-4798-873b-ed7dfcf15b4d')
    return IAudioMediaType
def _define_IAudioMediaType():
    IAudioMediaType = win32more.Media.Audio.Apo.IAudioMediaType_head
    IAudioMediaType.IsCompressedFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'IsCompressedFormat', ((1, 'pfCompressed'),)))
    IAudioMediaType.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(UInt32), use_last_error=False)(4, 'IsEqual', ((1, 'pIAudioType'),(1, 'pdwFlags'),)))
    IAudioMediaType.GetAudioFormat = COMMETHOD(WINFUNCTYPE(POINTER(win32more.Media.Audio.WAVEFORMATEX_head), use_last_error=False)(5, 'GetAudioFormat', ()))
    IAudioMediaType.GetUncompressedAudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.Apo.UNCOMPRESSEDAUDIOFORMAT_head), use_last_error=False)(6, 'GetUncompressedAudioFormat', ((1, 'pUncompressedAudioFormat'),)))
    return IAudioMediaType
APO_BUFFER_FLAGS = Int32
BUFFER_INVALID = 0
BUFFER_VALID = 1
BUFFER_SILENT = 2
def _define_APO_CONNECTION_PROPERTY_head():
    class APO_CONNECTION_PROPERTY(Structure):
        pass
    return APO_CONNECTION_PROPERTY
def _define_APO_CONNECTION_PROPERTY():
    APO_CONNECTION_PROPERTY = win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head
    APO_CONNECTION_PROPERTY._fields_ = [
        ("pBuffer", UIntPtr),
        ("u32ValidFrameCount", UInt32),
        ("u32BufferFlags", win32more.Media.Audio.Apo.APO_BUFFER_FLAGS),
        ("u32Signature", UInt32),
    ]
    return APO_CONNECTION_PROPERTY
def _define_APO_CONNECTION_PROPERTY_V2_head():
    class APO_CONNECTION_PROPERTY_V2(Structure):
        pass
    return APO_CONNECTION_PROPERTY_V2
def _define_APO_CONNECTION_PROPERTY_V2():
    APO_CONNECTION_PROPERTY_V2 = win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_V2_head
    APO_CONNECTION_PROPERTY_V2._fields_ = [
        ("property", win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY),
        ("u64QPCTime", UInt64),
    ]
    return APO_CONNECTION_PROPERTY_V2
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
        ("Type", win32more.Media.Audio.Apo.APO_CONNECTION_BUFFER_TYPE),
        ("pBuffer", UIntPtr),
        ("u32MaxFrameCount", UInt32),
        ("pFormat", win32more.Media.Audio.Apo.IAudioMediaType_head),
        ("u32Signature", UInt32),
    ]
    return APO_CONNECTION_DESCRIPTOR
APO_FLAG = Int32
APO_FLAG_NONE = 0
APO_FLAG_INPLACE = 1
APO_FLAG_SAMPLESPERFRAME_MUST_MATCH = 2
APO_FLAG_FRAMESPERSECOND_MUST_MATCH = 4
APO_FLAG_BITSPERSAMPLE_MUST_MATCH = 8
APO_FLAG_MIXER = 16
APO_FLAG_DEFAULT = 14
def _define_APO_REG_PROPERTIES_head():
    class APO_REG_PROPERTIES(Structure):
        pass
    return APO_REG_PROPERTIES
def _define_APO_REG_PROPERTIES():
    APO_REG_PROPERTIES = win32more.Media.Audio.Apo.APO_REG_PROPERTIES_head
    APO_REG_PROPERTIES._fields_ = [
        ("clsid", Guid),
        ("Flags", win32more.Media.Audio.Apo.APO_FLAG),
        ("szFriendlyName", Char * 256),
        ("szCopyrightInfo", Char * 256),
        ("u32MajorVersion", UInt32),
        ("u32MinorVersion", UInt32),
        ("u32MinInputConnections", UInt32),
        ("u32MaxInputConnections", UInt32),
        ("u32MinOutputConnections", UInt32),
        ("u32MaxOutputConnections", UInt32),
        ("u32MaxInstances", UInt32),
        ("u32NumAPOInterfaces", UInt32),
        ("iidAPOInterfaceList", Guid * 0),
    ]
    return APO_REG_PROPERTIES
def _define_APOInitBaseStruct_head():
    class APOInitBaseStruct(Structure):
        pass
    return APOInitBaseStruct
def _define_APOInitBaseStruct():
    APOInitBaseStruct = win32more.Media.Audio.Apo.APOInitBaseStruct_head
    APOInitBaseStruct._fields_ = [
        ("cbSize", UInt32),
        ("clsid", Guid),
    ]
    return APOInitBaseStruct
AUDIO_FLOW_TYPE = Int32
AUDIO_FLOW_PULL = 0
AUDIO_FLOW_PUSH = 1
EAudioConstriction = Int32
EAudioConstriction_eAudioConstrictionOff = 0
EAudioConstriction_eAudioConstriction48_16 = 1
EAudioConstriction_eAudioConstriction44_16 = 2
EAudioConstriction_eAudioConstriction14_14 = 3
EAudioConstriction_eAudioConstrictionMute = 4
def _define_IAudioProcessingObjectRT_head():
    class IAudioProcessingObjectRT(win32more.System.Com.IUnknown_head):
        Guid = Guid('9e1d6a6d-ddbc-4e95-a4c7-ad64ba37846c')
    return IAudioProcessingObjectRT
def _define_IAudioProcessingObjectRT():
    IAudioProcessingObjectRT = win32more.Media.Audio.Apo.IAudioProcessingObjectRT_head
    IAudioProcessingObjectRT.APOProcess = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)),UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)), use_last_error=False)(3, 'APOProcess', ((1, 'u32NumInputConnections'),(1, 'ppInputConnections'),(1, 'u32NumOutputConnections'),(1, 'ppOutputConnections'),)))
    IAudioProcessingObjectRT.CalcInputFrames = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(4, 'CalcInputFrames', ((1, 'u32OutputFrameCount'),)))
    IAudioProcessingObjectRT.CalcOutputFrames = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(5, 'CalcOutputFrames', ((1, 'u32InputFrameCount'),)))
    return IAudioProcessingObjectRT
def _define_IAudioProcessingObjectVBR_head():
    class IAudioProcessingObjectVBR(win32more.System.Com.IUnknown_head):
        Guid = Guid('7ba1db8f-78ad-49cd-9591-f79d80a17c81')
    return IAudioProcessingObjectVBR
def _define_IAudioProcessingObjectVBR():
    IAudioProcessingObjectVBR = win32more.Media.Audio.Apo.IAudioProcessingObjectVBR_head
    IAudioProcessingObjectVBR.CalcMaxInputFrames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(3, 'CalcMaxInputFrames', ((1, 'u32MaxOutputFrameCount'),(1, 'pu32InputFrameCount'),)))
    IAudioProcessingObjectVBR.CalcMaxOutputFrames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'CalcMaxOutputFrames', ((1, 'u32MaxInputFrameCount'),(1, 'pu32OutputFrameCount'),)))
    return IAudioProcessingObjectVBR
def _define_IAudioProcessingObjectConfiguration_head():
    class IAudioProcessingObjectConfiguration(win32more.System.Com.IUnknown_head):
        Guid = Guid('0e5ed805-aba6-49c3-8f9a-2b8c889c4fa8')
    return IAudioProcessingObjectConfiguration
def _define_IAudioProcessingObjectConfiguration():
    IAudioProcessingObjectConfiguration = win32more.Media.Audio.Apo.IAudioProcessingObjectConfiguration_head
    IAudioProcessingObjectConfiguration.LockForProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head)),UInt32,POINTER(POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head)), use_last_error=False)(3, 'LockForProcess', ((1, 'u32NumInputConnections'),(1, 'ppInputConnections'),(1, 'u32NumOutputConnections'),(1, 'ppOutputConnections'),)))
    IAudioProcessingObjectConfiguration.UnlockForProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'UnlockForProcess', ()))
    return IAudioProcessingObjectConfiguration
def _define_IAudioProcessingObject_head():
    class IAudioProcessingObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd7f2b29-24d0-4b5c-b177-592c39f9ca10')
    return IAudioProcessingObject
def _define_IAudioProcessingObject():
    IAudioProcessingObject = win32more.Media.Audio.Apo.IAudioProcessingObject_head
    IAudioProcessingObject.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Reset', ()))
    IAudioProcessingObject.GetLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(4, 'GetLatency', ((1, 'pTime'),)))
    IAudioProcessingObject.GetRegistrationProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.Apo.APO_REG_PROPERTIES_head)), use_last_error=False)(5, 'GetRegistrationProperties', ((1, 'ppRegProps'),)))
    IAudioProcessingObject.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte), use_last_error=False)(6, 'Initialize', ((1, 'cbDataSize'),(1, 'pbyData'),)))
    IAudioProcessingObject.IsInputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head), use_last_error=False)(7, 'IsInputFormatSupported', ((1, 'pOppositeFormat'),(1, 'pRequestedInputFormat'),(1, 'ppSupportedInputFormat'),)))
    IAudioProcessingObject.IsOutputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head), use_last_error=False)(8, 'IsOutputFormatSupported', ((1, 'pOppositeFormat'),(1, 'pRequestedOutputFormat'),(1, 'ppSupportedOutputFormat'),)))
    IAudioProcessingObject.GetInputChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetInputChannelCount', ((1, 'pu32ChannelCount'),)))
    return IAudioProcessingObject
def _define_IAudioDeviceModulesClient_head():
    class IAudioDeviceModulesClient(win32more.System.Com.IUnknown_head):
        Guid = Guid('98f37dac-d0b6-49f5-896a-aa4d169a4c48')
    return IAudioDeviceModulesClient
def _define_IAudioDeviceModulesClient():
    IAudioDeviceModulesClient = win32more.Media.Audio.Apo.IAudioDeviceModulesClient_head
    IAudioDeviceModulesClient.SetAudioDeviceModulesManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetAudioDeviceModulesManager', ((1, 'pAudioDeviceModulesManager'),)))
    return IAudioDeviceModulesClient
def _define_FNAPONOTIFICATIONCALLBACK():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.Apo.APO_REG_PROPERTIES_head),c_void_p, use_last_error=False)
def _define_IAudioSystemEffects_head():
    class IAudioSystemEffects(win32more.System.Com.IUnknown_head):
        Guid = Guid('5fa00f27-add6-499a-8a9d-6b98521fa75b')
    return IAudioSystemEffects
def _define_IAudioSystemEffects():
    IAudioSystemEffects = win32more.Media.Audio.Apo.IAudioSystemEffects_head
    return IAudioSystemEffects
def _define_IAudioSystemEffects2_head():
    class IAudioSystemEffects2(win32more.Media.Audio.Apo.IAudioSystemEffects_head):
        Guid = Guid('bafe99d2-7436-44ce-9e0e-4d89afbfff56')
    return IAudioSystemEffects2
def _define_IAudioSystemEffects2():
    IAudioSystemEffects2 = win32more.Media.Audio.Apo.IAudioSystemEffects2_head
    IAudioSystemEffects2.GetEffectsList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),POINTER(UInt32),win32more.Foundation.HANDLE, use_last_error=False)(3, 'GetEffectsList', ((1, 'ppEffectsIds'),(1, 'pcEffects'),(1, 'Event'),)))
    return IAudioSystemEffects2
def _define_IAudioSystemEffectsCustomFormats_head():
    class IAudioSystemEffectsCustomFormats(win32more.System.Com.IUnknown_head):
        Guid = Guid('b1176e34-bb7f-4f05-bebd-1b18a534e097')
    return IAudioSystemEffectsCustomFormats
def _define_IAudioSystemEffectsCustomFormats():
    IAudioSystemEffectsCustomFormats = win32more.Media.Audio.Apo.IAudioSystemEffectsCustomFormats_head
    IAudioSystemEffectsCustomFormats.GetFormatCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetFormatCount', ((1, 'pcFormats'),)))
    IAudioSystemEffectsCustomFormats.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head), use_last_error=False)(4, 'GetFormat', ((1, 'nFormat'),(1, 'ppFormat'),)))
    IAudioSystemEffectsCustomFormats.GetFormatRepresentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetFormatRepresentation', ((1, 'nFormat'),(1, 'ppwstrFormatRep'),)))
    return IAudioSystemEffectsCustomFormats
def _define_IApoAuxiliaryInputConfiguration_head():
    class IApoAuxiliaryInputConfiguration(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ceb0aab-fa19-48ed-a857-87771ae1b768')
    return IApoAuxiliaryInputConfiguration
def _define_IApoAuxiliaryInputConfiguration():
    IApoAuxiliaryInputConfiguration = win32more.Media.Audio.Apo.IApoAuxiliaryInputConfiguration_head
    IApoAuxiliaryInputConfiguration.AddAuxiliaryInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_DESCRIPTOR_head), use_last_error=False)(3, 'AddAuxiliaryInput', ((1, 'dwInputId'),(1, 'cbDataSize'),(1, 'pbyData'),(1, 'pInputConnection'),)))
    IApoAuxiliaryInputConfiguration.RemoveAuxiliaryInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'RemoveAuxiliaryInput', ((1, 'dwInputId'),)))
    IApoAuxiliaryInputConfiguration.IsInputFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Apo.IAudioMediaType_head,POINTER(win32more.Media.Audio.Apo.IAudioMediaType_head), use_last_error=False)(5, 'IsInputFormatSupported', ((1, 'pRequestedInputFormat'),(1, 'ppSupportedInputFormat'),)))
    return IApoAuxiliaryInputConfiguration
def _define_IApoAuxiliaryInputRT_head():
    class IApoAuxiliaryInputRT(win32more.System.Com.IUnknown_head):
        Guid = Guid('f851809c-c177-49a0-b1b2-b66f017943ab')
    return IApoAuxiliaryInputRT
def _define_IApoAuxiliaryInputRT():
    IApoAuxiliaryInputRT = win32more.Media.Audio.Apo.IApoAuxiliaryInputRT_head
    IApoAuxiliaryInputRT.AcceptInput = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head), use_last_error=False)(3, 'AcceptInput', ((1, 'dwInputId'),(1, 'pInputConnection'),)))
    return IApoAuxiliaryInputRT
def _define_IApoAcousticEchoCancellation_head():
    class IApoAcousticEchoCancellation(win32more.System.Com.IUnknown_head):
        Guid = Guid('25385759-3236-4101-a943-25693dfb5d2d')
    return IApoAcousticEchoCancellation
def _define_IApoAcousticEchoCancellation():
    IApoAcousticEchoCancellation = win32more.Media.Audio.Apo.IApoAcousticEchoCancellation_head
    return IApoAcousticEchoCancellation
def _define_APOInitSystemEffects_head():
    class APOInitSystemEffects(Structure):
        pass
    return APOInitSystemEffects
def _define_APOInitSystemEffects():
    APOInitSystemEffects = win32more.Media.Audio.Apo.APOInitSystemEffects_head
    APOInitSystemEffects._fields_ = [
        ("APOInit", win32more.Media.Audio.Apo.APOInitBaseStruct),
        ("pAPOEndpointProperties", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ("pAPOSystemEffectsProperties", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ("pReserved", c_void_p),
        ("pDeviceCollection", win32more.Media.Audio.IMMDeviceCollection_head),
    ]
    return APOInitSystemEffects
def _define_APOInitSystemEffects2_head():
    class APOInitSystemEffects2(Structure):
        pass
    return APOInitSystemEffects2
def _define_APOInitSystemEffects2():
    APOInitSystemEffects2 = win32more.Media.Audio.Apo.APOInitSystemEffects2_head
    APOInitSystemEffects2._fields_ = [
        ("APOInit", win32more.Media.Audio.Apo.APOInitBaseStruct),
        ("pAPOEndpointProperties", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ("pAPOSystemEffectsProperties", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ("pReserved", c_void_p),
        ("pDeviceCollection", win32more.Media.Audio.IMMDeviceCollection_head),
        ("nSoftwareIoDeviceInCollection", UInt32),
        ("nSoftwareIoConnectorIndex", UInt32),
        ("AudioProcessingMode", Guid),
        ("InitializeForDiscoveryOnly", win32more.Foundation.BOOL),
    ]
    return APOInitSystemEffects2
def _define_AudioFXExtensionParams_head():
    class AudioFXExtensionParams(Structure):
        pass
    return AudioFXExtensionParams
def _define_AudioFXExtensionParams():
    AudioFXExtensionParams = win32more.Media.Audio.Apo.AudioFXExtensionParams_head
    AudioFXExtensionParams._fields_ = [
        ("AddPageParam", win32more.Foundation.LPARAM),
        ("pwstrEndpointID", win32more.Foundation.PWSTR),
        ("pFxProperties", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
    ]
    return AudioFXExtensionParams
AUDIO_SYSTEMEFFECT_STATE = Int32
AUDIO_SYSTEMEFFECT_STATE_OFF = 0
AUDIO_SYSTEMEFFECT_STATE_ON = 1
def _define_AUDIO_SYSTEMEFFECT_head():
    class AUDIO_SYSTEMEFFECT(Structure):
        pass
    return AUDIO_SYSTEMEFFECT
def _define_AUDIO_SYSTEMEFFECT():
    AUDIO_SYSTEMEFFECT = win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_head
    AUDIO_SYSTEMEFFECT._fields_ = [
        ("id", Guid),
        ("canSetState", win32more.Foundation.BOOL),
        ("state", win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE),
    ]
    return AUDIO_SYSTEMEFFECT
def _define_IAudioSystemEffects3_head():
    class IAudioSystemEffects3(win32more.Media.Audio.Apo.IAudioSystemEffects2_head):
        Guid = Guid('c58b31cd-fc6a-4255-bc1f-ad29bb0a4a17')
    return IAudioSystemEffects3
def _define_IAudioSystemEffects3():
    IAudioSystemEffects3 = win32more.Media.Audio.Apo.IAudioSystemEffects3_head
    IAudioSystemEffects3.GetControllableSystemEffectsList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_head)),POINTER(UInt32),win32more.Foundation.HANDLE, use_last_error=False)(4, 'GetControllableSystemEffectsList', ((1, 'effects'),(1, 'numEffects'),(1, 'event'),)))
    IAudioSystemEffects3.SetAudioSystemEffectState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECT_STATE, use_last_error=False)(5, 'SetAudioSystemEffectState', ((1, 'effectId'),(1, 'state'),)))
    return IAudioSystemEffects3
def _define_APOInitSystemEffects3_head():
    class APOInitSystemEffects3(Structure):
        pass
    return APOInitSystemEffects3
def _define_APOInitSystemEffects3():
    APOInitSystemEffects3 = win32more.Media.Audio.Apo.APOInitSystemEffects3_head
    APOInitSystemEffects3._fields_ = [
        ("APOInit", win32more.Media.Audio.Apo.APOInitBaseStruct),
        ("pAPOEndpointProperties", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ("pServiceProvider", win32more.System.Com.IServiceProvider_head),
        ("pDeviceCollection", win32more.Media.Audio.IMMDeviceCollection_head),
        ("nSoftwareIoDeviceInCollection", UInt32),
        ("nSoftwareIoConnectorIndex", UInt32),
        ("AudioProcessingMode", Guid),
        ("InitializeForDiscoveryOnly", win32more.Foundation.BOOL),
    ]
    return APOInitSystemEffects3
def _define_IAudioProcessingObjectRTQueueService_head():
    class IAudioProcessingObjectRTQueueService(win32more.System.Com.IUnknown_head):
        Guid = Guid('acd65e2f-955b-4b57-b9bf-ac297bb752c9')
    return IAudioProcessingObjectRTQueueService
def _define_IAudioProcessingObjectRTQueueService():
    IAudioProcessingObjectRTQueueService = win32more.Media.Audio.Apo.IAudioProcessingObjectRTQueueService_head
    IAudioProcessingObjectRTQueueService.GetRealTimeWorkQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetRealTimeWorkQueue', ((1, 'workQueueId'),)))
    return IAudioProcessingObjectRTQueueService
APO_LOG_LEVEL = Int32
APO_LOG_LEVEL_ALWAYS = 0
APO_LOG_LEVEL_CRITICAL = 1
APO_LOG_LEVEL_ERROR = 2
APO_LOG_LEVEL_WARNING = 3
APO_LOG_LEVEL_INFO = 4
APO_LOG_LEVEL_VERBOSE = 5
def _define_IAudioProcessingObjectLoggingService_head():
    class IAudioProcessingObjectLoggingService(win32more.System.Com.IUnknown_head):
        Guid = Guid('698f0107-1745-4708-95a5-d84478a62a65')
    return IAudioProcessingObjectLoggingService
def _define_IAudioProcessingObjectLoggingService():
    IAudioProcessingObjectLoggingService = win32more.Media.Audio.Apo.IAudioProcessingObjectLoggingService_head
    IAudioProcessingObjectLoggingService.ApoLog = COMMETHOD(WINFUNCTYPE(Void,win32more.Media.Audio.Apo.APO_LOG_LEVEL,win32more.Foundation.PWSTR, use_last_error=False)(3, 'ApoLog', ((1, 'level'),(1, 'format'),)))
    return IAudioProcessingObjectLoggingService
APO_NOTIFICATION_TYPE = Int32
APO_NOTIFICATION_TYPE_NONE = 0
APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME = 1
APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE = 2
APO_NOTIFICATION_TYPE_SYSTEM_EFFECTS_PROPERTY_CHANGE = 3
def _define_AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION_head():
    class AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION(Structure):
        pass
    return AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION
def _define_AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION():
    AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION_head
    AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION._fields_ = [
        ("endpoint", win32more.Media.Audio.IMMDevice_head),
        ("volume", POINTER(win32more.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA_head)),
    ]
    return AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION_head():
    class AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION(Structure):
        pass
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION():
    AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION_head
    AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION._fields_ = [
        ("endpoint", win32more.Media.Audio.IMMDevice_head),
        ("propertyStore", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ("propertyKey", win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
    ]
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION_head():
    class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION(Structure):
        pass
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION():
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION = win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION_head
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION._fields_ = [
        ("endpoint", win32more.Media.Audio.IMMDevice_head),
        ("propertyStoreContext", Guid),
        ("propertyStoreType", win32more.Media.Audio.__MIDL___MIDL_itf_mmdeviceapi_0000_0008_0002),
        ("propertyStore", win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),
        ("propertyKey", win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
    ]
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION
def _define_APO_NOTIFICATION_head():
    class APO_NOTIFICATION(Structure):
        pass
    return APO_NOTIFICATION
def _define_APO_NOTIFICATION():
    APO_NOTIFICATION = win32more.Media.Audio.Apo.APO_NOTIFICATION_head
    class APO_NOTIFICATION__Anonymous_e__Union(Union):
        pass
    APO_NOTIFICATION__Anonymous_e__Union._fields_ = [
        ("audioEndpointVolumeChange", win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION),
        ("audioEndpointPropertyChange", win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION),
        ("audioSystemEffectsPropertyChange", win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION),
    ]
    APO_NOTIFICATION._anonymous_ = [
        'Anonymous',
    ]
    APO_NOTIFICATION._fields_ = [
        ("type", win32more.Media.Audio.Apo.APO_NOTIFICATION_TYPE),
        ("Anonymous", APO_NOTIFICATION__Anonymous_e__Union),
    ]
    return APO_NOTIFICATION
def _define_AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR_head():
    class AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR():
    AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR_head
    AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ("device", win32more.Media.Audio.IMMDevice_head),
    ]
    return AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head():
    class AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR():
    AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head
    AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ("device", win32more.Media.Audio.IMMDevice_head),
    ]
    return AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head():
    class AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR():
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR_head
    AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ("device", win32more.Media.Audio.IMMDevice_head),
        ("propertyStoreContext", Guid),
    ]
    return AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR
def _define_APO_NOTIFICATION_DESCRIPTOR_head():
    class APO_NOTIFICATION_DESCRIPTOR(Structure):
        pass
    return APO_NOTIFICATION_DESCRIPTOR
def _define_APO_NOTIFICATION_DESCRIPTOR():
    APO_NOTIFICATION_DESCRIPTOR = win32more.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR_head
    class APO_NOTIFICATION_DESCRIPTOR__Anonymous_e__Union(Union):
        pass
    APO_NOTIFICATION_DESCRIPTOR__Anonymous_e__Union._fields_ = [
        ("audioEndpointVolume", win32more.Media.Audio.Apo.AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR),
        ("audioEndpointPropertyChange", win32more.Media.Audio.Apo.AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR),
        ("audioSystemEffectsPropertyChange", win32more.Media.Audio.Apo.AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR),
    ]
    APO_NOTIFICATION_DESCRIPTOR._anonymous_ = [
        'Anonymous',
    ]
    APO_NOTIFICATION_DESCRIPTOR._fields_ = [
        ("type", win32more.Media.Audio.Apo.APO_NOTIFICATION_TYPE),
        ("Anonymous", APO_NOTIFICATION_DESCRIPTOR__Anonymous_e__Union),
    ]
    return APO_NOTIFICATION_DESCRIPTOR
def _define_IAudioProcessingObjectNotifications_head():
    class IAudioProcessingObjectNotifications(win32more.System.Com.IUnknown_head):
        Guid = Guid('56b0c76f-02fd-4b21-a52e-9f8219fc86e4')
    return IAudioProcessingObjectNotifications
def _define_IAudioProcessingObjectNotifications():
    IAudioProcessingObjectNotifications = win32more.Media.Audio.Apo.IAudioProcessingObjectNotifications_head
    IAudioProcessingObjectNotifications.GetApoNotificationRegistrationInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.Apo.APO_NOTIFICATION_DESCRIPTOR_head)),POINTER(UInt32), use_last_error=False)(3, 'GetApoNotificationRegistrationInfo', ((1, 'apoNotifications'),(1, 'count'),)))
    IAudioProcessingObjectNotifications.HandleNotification = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.Apo.APO_NOTIFICATION_head), use_last_error=False)(4, 'HandleNotification', ((1, 'apoNotification'),)))
    return IAudioProcessingObjectNotifications
__all__ = [
    "APOERR_ALREADY_INITIALIZED",
    "APOERR_NOT_INITIALIZED",
    "APOERR_FORMAT_NOT_SUPPORTED",
    "APOERR_INVALID_APO_CLSID",
    "APOERR_BUFFERS_OVERLAP",
    "APOERR_ALREADY_UNLOCKED",
    "APOERR_NUM_CONNECTIONS_INVALID",
    "APOERR_INVALID_OUTPUT_MAXFRAMECOUNT",
    "APOERR_INVALID_CONNECTION_FORMAT",
    "APOERR_APO_LOCKED",
    "APOERR_INVALID_COEFFCOUNT",
    "APOERR_INVALID_COEFFICIENT",
    "APOERR_INVALID_CURVE_PARAM",
    "APOERR_INVALID_INPUTID",
    "AUDIO_MIN_FRAMERATE",
    "AUDIO_MAX_FRAMERATE",
    "AUDIO_MIN_CHANNELS",
    "AUDIO_MAX_CHANNELS",
    "SID_AudioProcessingObjectRTQueue",
    "SID_AudioProcessingObjectLoggingService",
    "AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES",
    "AUDIOMEDIATYPE_EQUAL_FORMAT_DATA",
    "AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA",
    "UNCOMPRESSEDAUDIOFORMAT",
    "IAudioMediaType",
    "APO_BUFFER_FLAGS",
    "BUFFER_INVALID",
    "BUFFER_VALID",
    "BUFFER_SILENT",
    "APO_CONNECTION_PROPERTY",
    "APO_CONNECTION_PROPERTY_V2",
    "APO_CONNECTION_BUFFER_TYPE",
    "APO_CONNECTION_BUFFER_TYPE_ALLOCATED",
    "APO_CONNECTION_BUFFER_TYPE_EXTERNAL",
    "APO_CONNECTION_BUFFER_TYPE_DEPENDANT",
    "APO_CONNECTION_DESCRIPTOR",
    "APO_FLAG",
    "APO_FLAG_NONE",
    "APO_FLAG_INPLACE",
    "APO_FLAG_SAMPLESPERFRAME_MUST_MATCH",
    "APO_FLAG_FRAMESPERSECOND_MUST_MATCH",
    "APO_FLAG_BITSPERSAMPLE_MUST_MATCH",
    "APO_FLAG_MIXER",
    "APO_FLAG_DEFAULT",
    "APO_REG_PROPERTIES",
    "APOInitBaseStruct",
    "AUDIO_FLOW_TYPE",
    "AUDIO_FLOW_PULL",
    "AUDIO_FLOW_PUSH",
    "EAudioConstriction",
    "EAudioConstriction_eAudioConstrictionOff",
    "EAudioConstriction_eAudioConstriction48_16",
    "EAudioConstriction_eAudioConstriction44_16",
    "EAudioConstriction_eAudioConstriction14_14",
    "EAudioConstriction_eAudioConstrictionMute",
    "IAudioProcessingObjectRT",
    "IAudioProcessingObjectVBR",
    "IAudioProcessingObjectConfiguration",
    "IAudioProcessingObject",
    "IAudioDeviceModulesClient",
    "FNAPONOTIFICATIONCALLBACK",
    "IAudioSystemEffects",
    "IAudioSystemEffects2",
    "IAudioSystemEffectsCustomFormats",
    "IApoAuxiliaryInputConfiguration",
    "IApoAuxiliaryInputRT",
    "IApoAcousticEchoCancellation",
    "APOInitSystemEffects",
    "APOInitSystemEffects2",
    "AudioFXExtensionParams",
    "AUDIO_SYSTEMEFFECT_STATE",
    "AUDIO_SYSTEMEFFECT_STATE_OFF",
    "AUDIO_SYSTEMEFFECT_STATE_ON",
    "AUDIO_SYSTEMEFFECT",
    "IAudioSystemEffects3",
    "APOInitSystemEffects3",
    "IAudioProcessingObjectRTQueueService",
    "APO_LOG_LEVEL",
    "APO_LOG_LEVEL_ALWAYS",
    "APO_LOG_LEVEL_CRITICAL",
    "APO_LOG_LEVEL_ERROR",
    "APO_LOG_LEVEL_WARNING",
    "APO_LOG_LEVEL_INFO",
    "APO_LOG_LEVEL_VERBOSE",
    "IAudioProcessingObjectLoggingService",
    "APO_NOTIFICATION_TYPE",
    "APO_NOTIFICATION_TYPE_NONE",
    "APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME",
    "APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE",
    "APO_NOTIFICATION_TYPE_SYSTEM_EFFECTS_PROPERTY_CHANGE",
    "AUDIO_ENDPOINT_VOLUME_CHANGE_NOTIFICATION",
    "AUDIO_ENDPOINT_PROPERTY_CHANGE_NOTIFICATION",
    "AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_NOTIFICATION",
    "APO_NOTIFICATION",
    "AUDIO_ENDPOINT_VOLUME_APO_NOTIFICATION_DESCRIPTOR",
    "AUDIO_ENDPOINT_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR",
    "AUDIO_SYSTEMEFFECTS_PROPERTY_CHANGE_APO_NOTIFICATION_DESCRIPTOR",
    "APO_NOTIFICATION_DESCRIPTOR",
    "IAudioProcessingObjectNotifications",
]
