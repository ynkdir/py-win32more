from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Media.Audio
import win32more.Media.Audio.Apo
import win32more.Media.Audio.Endpoints
import win32more.Media.KernelStreaming
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
def _define_DEVPKEY_AudioEndpointPlugin_FactoryCLSID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=1)
def _define_DEVPKEY_AudioEndpointPlugin_DataFlow():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=2)
def _define_DEVPKEY_AudioEndpointPlugin_PnPInterface():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=3)
def _define_DEVPKEY_AudioEndpointPlugin2_FactoryCLSID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=4)
def _define_AUDIO_ENDPOINT_SHARED_CREATE_PARAMS_head():
    class AUDIO_ENDPOINT_SHARED_CREATE_PARAMS(Structure):
        pass
    return AUDIO_ENDPOINT_SHARED_CREATE_PARAMS
def _define_AUDIO_ENDPOINT_SHARED_CREATE_PARAMS():
    AUDIO_ENDPOINT_SHARED_CREATE_PARAMS = win32more.Media.Audio.Endpoints.AUDIO_ENDPOINT_SHARED_CREATE_PARAMS_head
    AUDIO_ENDPOINT_SHARED_CREATE_PARAMS._fields_ = [
        ('u32Size', UInt32),
        ('u32TSSessionId', UInt32),
        ('targetEndpointConnectorType', win32more.Media.Audio.Endpoints.EndpointConnectorType),
        ('wfxDeviceFormat', win32more.Media.Audio.WAVEFORMATEX),
    ]
    return AUDIO_ENDPOINT_SHARED_CREATE_PARAMS
DEVINTERFACE_AUDIOENDPOINTPLUGIN = Guid('9f2f7b66-65ac-4fa6-8a-e4-12-3c-78-b8-93-13')
EndpointConnectorType = Int32
EndpointConnectorType_eHostProcessConnector = 0
EndpointConnectorType_eOffloadConnector = 1
EndpointConnectorType_eLoopbackConnector = 2
EndpointConnectorType_eKeywordDetectorConnector = 3
EndpointConnectorType_eConnectorCount = 4
def _define_IAudioEndpointFormatControl_head():
    class IAudioEndpointFormatControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('784cfd40-9f89-456e-a1-a6-87-3b-00-6a-66-4e')
    return IAudioEndpointFormatControl
def _define_IAudioEndpointFormatControl():
    IAudioEndpointFormatControl = win32more.Media.Audio.Endpoints.IAudioEndpointFormatControl_head
    IAudioEndpointFormatControl.ResetToDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'ResetToDefault', ((1, 'ResetFlags'),)))
    win32more.System.Com.IUnknown
    return IAudioEndpointFormatControl
def _define_IAudioEndpointLastBufferControl_head():
    class IAudioEndpointLastBufferControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('f8520dd3-8f9d-4437-98-61-62-f5-84-c3-3d-d6')
    return IAudioEndpointLastBufferControl
def _define_IAudioEndpointLastBufferControl():
    IAudioEndpointLastBufferControl = win32more.Media.Audio.Endpoints.IAudioEndpointLastBufferControl_head
    IAudioEndpointLastBufferControl.IsLastBufferControlSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(3, 'IsLastBufferControlSupported', ()))
    IAudioEndpointLastBufferControl.ReleaseOutputDataPointerForLastBuffer = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head))(4, 'ReleaseOutputDataPointerForLastBuffer', ((1, 'pConnectionProperty'),)))
    win32more.System.Com.IUnknown
    return IAudioEndpointLastBufferControl
def _define_IAudioEndpointOffloadStreamMeter_head():
    class IAudioEndpointOffloadStreamMeter(win32more.System.Com.IUnknown_head):
        Guid = Guid('e1546dce-9dd1-418b-9a-b2-34-8c-ed-16-1c-86')
    return IAudioEndpointOffloadStreamMeter
def _define_IAudioEndpointOffloadStreamMeter():
    IAudioEndpointOffloadStreamMeter = win32more.Media.Audio.Endpoints.IAudioEndpointOffloadStreamMeter_head
    IAudioEndpointOffloadStreamMeter.GetMeterChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetMeterChannelCount', ((1, 'pu32ChannelCount'),)))
    IAudioEndpointOffloadStreamMeter.GetMeteringData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single))(4, 'GetMeteringData', ((1, 'u32ChannelCount'),(1, 'pf32PeakValues'),)))
    win32more.System.Com.IUnknown
    return IAudioEndpointOffloadStreamMeter
def _define_IAudioEndpointOffloadStreamMute_head():
    class IAudioEndpointOffloadStreamMute(win32more.System.Com.IUnknown_head):
        Guid = Guid('dfe21355-5ec2-40e0-8d-6b-71-0a-c3-c0-02-49')
    return IAudioEndpointOffloadStreamMute
def _define_IAudioEndpointOffloadStreamMute():
    IAudioEndpointOffloadStreamMute = win32more.Media.Audio.Endpoints.IAudioEndpointOffloadStreamMute_head
    IAudioEndpointOffloadStreamMute.SetMute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte)(3, 'SetMute', ((1, 'bMuted'),)))
    IAudioEndpointOffloadStreamMute.GetMute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no)(4, 'GetMute', ((1, 'pbMuted'),)))
    win32more.System.Com.IUnknown
    return IAudioEndpointOffloadStreamMute
def _define_IAudioEndpointOffloadStreamVolume_head():
    class IAudioEndpointOffloadStreamVolume(win32more.System.Com.IUnknown_head):
        Guid = Guid('64f1dd49-71ca-4281-86-72-3a-9e-dd-d1-d0-b6')
    return IAudioEndpointOffloadStreamVolume
def _define_IAudioEndpointOffloadStreamVolume():
    IAudioEndpointOffloadStreamVolume = win32more.Media.Audio.Endpoints.IAudioEndpointOffloadStreamVolume_head
    IAudioEndpointOffloadStreamVolume.GetVolumeChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetVolumeChannelCount', ((1, 'pu32ChannelCount'),)))
    IAudioEndpointOffloadStreamVolume.SetChannelVolumes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single),win32more.Media.KernelStreaming.AUDIO_CURVE_TYPE,POINTER(Int64))(4, 'SetChannelVolumes', ((1, 'u32ChannelCount'),(1, 'pf32Volumes'),(1, 'u32CurveType'),(1, 'pCurveDuration'),)))
    IAudioEndpointOffloadStreamVolume.GetChannelVolumes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single))(5, 'GetChannelVolumes', ((1, 'u32ChannelCount'),(1, 'pf32Volumes'),)))
    win32more.System.Com.IUnknown
    return IAudioEndpointOffloadStreamVolume
def _define_IAudioEndpointVolume_head():
    class IAudioEndpointVolume(win32more.System.Com.IUnknown_head):
        Guid = Guid('5cdf2c82-841e-4546-97-22-0c-f7-40-78-22-9a')
    return IAudioEndpointVolume
def _define_IAudioEndpointVolume():
    IAudioEndpointVolume = win32more.Media.Audio.Endpoints.IAudioEndpointVolume_head
    IAudioEndpointVolume.RegisterControlChangeNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Endpoints.IAudioEndpointVolumeCallback_head)(3, 'RegisterControlChangeNotify', ((1, 'pNotify'),)))
    IAudioEndpointVolume.UnregisterControlChangeNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.Endpoints.IAudioEndpointVolumeCallback_head)(4, 'UnregisterControlChangeNotify', ((1, 'pNotify'),)))
    IAudioEndpointVolume.GetChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetChannelCount', ((1, 'pnChannelCount'),)))
    IAudioEndpointVolume.SetMasterVolumeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Guid))(6, 'SetMasterVolumeLevel', ((1, 'fLevelDB'),(1, 'pguidEventContext'),)))
    IAudioEndpointVolume.SetMasterVolumeLevelScalar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Guid))(7, 'SetMasterVolumeLevelScalar', ((1, 'fLevel'),(1, 'pguidEventContext'),)))
    IAudioEndpointVolume.GetMasterVolumeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(8, 'GetMasterVolumeLevel', ((1, 'pfLevelDB'),)))
    IAudioEndpointVolume.GetMasterVolumeLevelScalar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(9, 'GetMasterVolumeLevelScalar', ((1, 'pfLevel'),)))
    IAudioEndpointVolume.SetChannelVolumeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,POINTER(Guid))(10, 'SetChannelVolumeLevel', ((1, 'nChannel'),(1, 'fLevelDB'),(1, 'pguidEventContext'),)))
    IAudioEndpointVolume.SetChannelVolumeLevelScalar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,POINTER(Guid))(11, 'SetChannelVolumeLevelScalar', ((1, 'nChannel'),(1, 'fLevel'),(1, 'pguidEventContext'),)))
    IAudioEndpointVolume.GetChannelVolumeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single))(12, 'GetChannelVolumeLevel', ((1, 'nChannel'),(1, 'pfLevelDB'),)))
    IAudioEndpointVolume.GetChannelVolumeLevelScalar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single))(13, 'GetChannelVolumeLevelScalar', ((1, 'nChannel'),(1, 'pfLevel'),)))
    IAudioEndpointVolume.SetMute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(Guid))(14, 'SetMute', ((1, 'bMute'),(1, 'pguidEventContext'),)))
    IAudioEndpointVolume.GetMute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(15, 'GetMute', ((1, 'pbMute'),)))
    IAudioEndpointVolume.GetVolumeStepInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(16, 'GetVolumeStepInfo', ((1, 'pnStep'),(1, 'pnStepCount'),)))
    IAudioEndpointVolume.VolumeStepUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(17, 'VolumeStepUp', ((1, 'pguidEventContext'),)))
    IAudioEndpointVolume.VolumeStepDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(18, 'VolumeStepDown', ((1, 'pguidEventContext'),)))
    IAudioEndpointVolume.QueryHardwareSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(19, 'QueryHardwareSupport', ((1, 'pdwHardwareSupportMask'),)))
    IAudioEndpointVolume.GetVolumeRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),POINTER(Single),POINTER(Single))(20, 'GetVolumeRange', ((1, 'pflVolumeMindB'),(1, 'pflVolumeMaxdB'),(1, 'pflVolumeIncrementdB'),)))
    win32more.System.Com.IUnknown
    return IAudioEndpointVolume
def _define_IAudioEndpointVolumeCallback_head():
    class IAudioEndpointVolumeCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('657804fa-d6ad-4496-8a-60-35-27-52-af-4f-89')
    return IAudioEndpointVolumeCallback
def _define_IAudioEndpointVolumeCallback():
    IAudioEndpointVolumeCallback = win32more.Media.Audio.Endpoints.IAudioEndpointVolumeCallback_head
    IAudioEndpointVolumeCallback.OnNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA_head))(3, 'OnNotify', ((1, 'pNotify'),)))
    win32more.System.Com.IUnknown
    return IAudioEndpointVolumeCallback
def _define_IAudioEndpointVolumeEx_head():
    class IAudioEndpointVolumeEx(win32more.Media.Audio.Endpoints.IAudioEndpointVolume_head):
        Guid = Guid('66e11784-f695-4f28-a5-05-a7-08-00-81-a7-8f')
    return IAudioEndpointVolumeEx
def _define_IAudioEndpointVolumeEx():
    IAudioEndpointVolumeEx = win32more.Media.Audio.Endpoints.IAudioEndpointVolumeEx_head
    IAudioEndpointVolumeEx.GetVolumeRangeChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single),POINTER(Single),POINTER(Single))(21, 'GetVolumeRangeChannel', ((1, 'iChannel'),(1, 'pflVolumeMindB'),(1, 'pflVolumeMaxdB'),(1, 'pflVolumeIncrementdB'),)))
    win32more.Media.Audio.Endpoints.IAudioEndpointVolume
    return IAudioEndpointVolumeEx
def _define_IAudioLfxControl_head():
    class IAudioLfxControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('076a6922-d802-4f83-ba-f6-40-9d-9c-a1-1b-fe')
    return IAudioLfxControl
def _define_IAudioLfxControl():
    IAudioLfxControl = win32more.Media.Audio.Endpoints.IAudioLfxControl_head
    IAudioLfxControl.SetLocalEffectsState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(3, 'SetLocalEffectsState', ((1, 'bEnabled'),)))
    IAudioLfxControl.GetLocalEffectsState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(4, 'GetLocalEffectsState', ((1, 'pbEnabled'),)))
    win32more.System.Com.IUnknown
    return IAudioLfxControl
def _define_IAudioMeterInformation_head():
    class IAudioMeterInformation(win32more.System.Com.IUnknown_head):
        Guid = Guid('c02216f6-8c67-4b5b-9d-00-d0-08-e7-3e-00-64')
    return IAudioMeterInformation
def _define_IAudioMeterInformation():
    IAudioMeterInformation = win32more.Media.Audio.Endpoints.IAudioMeterInformation_head
    IAudioMeterInformation.GetPeakValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(3, 'GetPeakValue', ((1, 'pfPeak'),)))
    IAudioMeterInformation.GetMeteringChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetMeteringChannelCount', ((1, 'pnChannelCount'),)))
    IAudioMeterInformation.GetChannelsPeakValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single))(5, 'GetChannelsPeakValues', ((1, 'u32ChannelCount'),(1, 'afPeakValues'),)))
    IAudioMeterInformation.QueryHardwareSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'QueryHardwareSupport', ((1, 'pdwHardwareSupportMask'),)))
    win32more.System.Com.IUnknown
    return IAudioMeterInformation
def _define_IHardwareAudioEngineBase_head():
    class IHardwareAudioEngineBase(win32more.System.Com.IUnknown_head):
        Guid = Guid('eddce3e4-f3c1-453a-b4-61-22-35-63-cb-d8-86')
    return IHardwareAudioEngineBase
def _define_IHardwareAudioEngineBase():
    IHardwareAudioEngineBase = win32more.Media.Audio.Endpoints.IHardwareAudioEngineBase_head
    IHardwareAudioEngineBase.GetAvailableOffloadConnectorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(3, 'GetAvailableOffloadConnectorCount', ((1, '_pwstrDeviceId'),(1, '_uConnectorId'),(1, '_pAvailableConnectorInstanceCount'),)))
    IHardwareAudioEngineBase.GetEngineFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.IMMDevice_head,win32more.Foundation.BOOL,POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)))(4, 'GetEngineFormat', ((1, 'pDevice'),(1, '_bRequestDeviceFormat'),(1, '_ppwfxFormat'),)))
    IHardwareAudioEngineBase.SetEngineDeviceFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.IMMDevice_head,POINTER(win32more.Media.Audio.WAVEFORMATEX_head))(5, 'SetEngineDeviceFormat', ((1, 'pDevice'),(1, '_pwfxFormat'),)))
    IHardwareAudioEngineBase.SetGfxState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.IMMDevice_head,win32more.Foundation.BOOL)(6, 'SetGfxState', ((1, 'pDevice'),(1, '_bEnable'),)))
    IHardwareAudioEngineBase.GetGfxState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Audio.IMMDevice_head,POINTER(win32more.Foundation.BOOL))(7, 'GetGfxState', ((1, 'pDevice'),(1, '_pbEnable'),)))
    win32more.System.Com.IUnknown
    return IHardwareAudioEngineBase
__all__ = [
    "AUDIO_ENDPOINT_SHARED_CREATE_PARAMS",
    "DEVINTERFACE_AUDIOENDPOINTPLUGIN",
    "DEVPKEY_AudioEndpointPlugin2_FactoryCLSID",
    "DEVPKEY_AudioEndpointPlugin_DataFlow",
    "DEVPKEY_AudioEndpointPlugin_FactoryCLSID",
    "DEVPKEY_AudioEndpointPlugin_PnPInterface",
    "EndpointConnectorType",
    "EndpointConnectorType_eConnectorCount",
    "EndpointConnectorType_eHostProcessConnector",
    "EndpointConnectorType_eKeywordDetectorConnector",
    "EndpointConnectorType_eLoopbackConnector",
    "EndpointConnectorType_eOffloadConnector",
    "IAudioEndpointFormatControl",
    "IAudioEndpointLastBufferControl",
    "IAudioEndpointOffloadStreamMeter",
    "IAudioEndpointOffloadStreamMute",
    "IAudioEndpointOffloadStreamVolume",
    "IAudioEndpointVolume",
    "IAudioEndpointVolumeCallback",
    "IAudioEndpointVolumeEx",
    "IAudioLfxControl",
    "IAudioMeterInformation",
    "IHardwareAudioEngineBase",
]
