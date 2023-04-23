from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Audio.Apo
import Windows.Win32.Media.Audio.Endpoints
import Windows.Win32.Media.KernelStreaming
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
class AUDIO_ENDPOINT_SHARED_CREATE_PARAMS(EasyCastStructure):
    u32Size: UInt32
    u32TSSessionId: UInt32
    targetEndpointConnectorType: Windows.Win32.Media.Audio.Endpoints.EndpointConnectorType
    wfxDeviceFormat: Windows.Win32.Media.Audio.WAVEFORMATEX
def DEVPKEY_AudioEndpointPlugin_FactoryCLSID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=1)
def DEVPKEY_AudioEndpointPlugin_DataFlow():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=2)
def DEVPKEY_AudioEndpointPlugin_PnPInterface():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=3)
def DEVPKEY_AudioEndpointPlugin2_FactoryCLSID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('12d83bd7-cf12-46be-85-40-81-27-10-d3-02-1c'), pid=4)
DEVINTERFACE_AUDIOENDPOINTPLUGIN = Guid('9f2f7b66-65ac-4fa6-8a-e4-12-3c-78-b8-93-13')
EndpointConnectorType = Int32
EndpointConnectorType_eHostProcessConnector: EndpointConnectorType = 0
EndpointConnectorType_eOffloadConnector: EndpointConnectorType = 1
EndpointConnectorType_eLoopbackConnector: EndpointConnectorType = 2
EndpointConnectorType_eKeywordDetectorConnector: EndpointConnectorType = 3
EndpointConnectorType_eConnectorCount: EndpointConnectorType = 4
class IAudioEndpointFormatControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('784cfd40-9f89-456e-a1-a6-87-3b-00-6a-66-4e')
    @commethod(3)
    def ResetToDefault(self, ResetFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointLastBufferControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f8520dd3-8f9d-4437-98-61-62-f5-84-c3-3d-d6')
    @commethod(3)
    def IsLastBufferControlSupported(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def ReleaseOutputDataPointerForLastBuffer(self, pConnectionProperty: POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)) -> Void: ...
class IAudioEndpointOffloadStreamMeter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e1546dce-9dd1-418b-9a-b2-34-8c-ed-16-1c-86')
    @commethod(3)
    def GetMeterChannelCount(self, pu32ChannelCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMeteringData(self, u32ChannelCount: UInt32, pf32PeakValues: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointOffloadStreamMute(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dfe21355-5ec2-40e0-8d-6b-71-0a-c3-c0-02-49')
    @commethod(3)
    def SetMute(self, bMuted: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMute(self, pbMuted: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointOffloadStreamVolume(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('64f1dd49-71ca-4281-86-72-3a-9e-dd-d1-d0-b6')
    @commethod(3)
    def GetVolumeChannelCount(self, pu32ChannelCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetChannelVolumes(self, u32ChannelCount: UInt32, pf32Volumes: POINTER(Single), u32CurveType: Windows.Win32.Media.KernelStreaming.AUDIO_CURVE_TYPE, pCurveDuration: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelVolumes(self, u32ChannelCount: UInt32, pf32Volumes: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointVolume(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5cdf2c82-841e-4546-97-22-0c-f7-40-78-22-9a')
    @commethod(3)
    def RegisterControlChangeNotify(self, pNotify: Windows.Win32.Media.Audio.Endpoints.IAudioEndpointVolumeCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterControlChangeNotify(self, pNotify: Windows.Win32.Media.Audio.Endpoints.IAudioEndpointVolumeCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelCount(self, pnChannelCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMasterVolumeLevel(self, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMasterVolumeLevelScalar(self, fLevel: Single, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMasterVolumeLevel(self, pfLevelDB: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMasterVolumeLevelScalar(self, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetChannelVolumeLevel(self, nChannel: UInt32, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetChannelVolumeLevelScalar(self, nChannel: UInt32, fLevel: Single, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetChannelVolumeLevel(self, nChannel: UInt32, pfLevelDB: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetChannelVolumeLevelScalar(self, nChannel: UInt32, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetMute(self, bMute: Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetMute(self, pbMute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetVolumeStepInfo(self, pnStep: POINTER(UInt32), pnStepCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def VolumeStepUp(self, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def VolumeStepDown(self, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def QueryHardwareSupport(self, pdwHardwareSupportMask: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetVolumeRange(self, pflVolumeMindB: POINTER(Single), pflVolumeMaxdB: POINTER(Single), pflVolumeIncrementdB: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointVolumeCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('657804fa-d6ad-4496-8a-60-35-27-52-af-4f-89')
    @commethod(3)
    def OnNotify(self, pNotify: POINTER(Windows.Win32.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointVolumeEx(c_void_p):
    extends: Windows.Win32.Media.Audio.Endpoints.IAudioEndpointVolume
    Guid = Guid('66e11784-f695-4f28-a5-05-a7-08-00-81-a7-8f')
    @commethod(21)
    def GetVolumeRangeChannel(self, iChannel: UInt32, pflVolumeMindB: POINTER(Single), pflVolumeMaxdB: POINTER(Single), pflVolumeIncrementdB: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioLfxControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('076a6922-d802-4f83-ba-f6-40-9d-9c-a1-1b-fe')
    @commethod(3)
    def SetLocalEffectsState(self, bEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalEffectsState(self, pbEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioMeterInformation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c02216f6-8c67-4b5b-9d-00-d0-08-e7-3e-00-64')
    @commethod(3)
    def GetPeakValue(self, pfPeak: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMeteringChannelCount(self, pnChannelCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelsPeakValues(self, u32ChannelCount: UInt32, afPeakValues: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryHardwareSupport(self, pdwHardwareSupportMask: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IHardwareAudioEngineBase(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eddce3e4-f3c1-453a-b4-61-22-35-63-cb-d8-86')
    @commethod(3)
    def GetAvailableOffloadConnectorCount(self, _pwstrDeviceId: Windows.Win32.Foundation.PWSTR, _uConnectorId: UInt32, _pAvailableConnectorInstanceCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEngineFormat(self, pDevice: Windows.Win32.Media.Audio.IMMDevice_head, _bRequestDeviceFormat: Windows.Win32.Foundation.BOOL, _ppwfxFormat: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetEngineDeviceFormat(self, pDevice: Windows.Win32.Media.Audio.IMMDevice_head, _pwfxFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetGfxState(self, pDevice: Windows.Win32.Media.Audio.IMMDevice_head, _bEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGfxState(self, pDevice: Windows.Win32.Media.Audio.IMMDevice_head, _pbEnable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'AUDIO_ENDPOINT_SHARED_CREATE_PARAMS')
make_head(_module, 'DEVPKEY_AudioEndpointPlugin_FactoryCLSID')
make_head(_module, 'DEVPKEY_AudioEndpointPlugin_DataFlow')
make_head(_module, 'DEVPKEY_AudioEndpointPlugin_PnPInterface')
make_head(_module, 'DEVPKEY_AudioEndpointPlugin2_FactoryCLSID')
make_head(_module, 'IAudioEndpointFormatControl')
make_head(_module, 'IAudioEndpointLastBufferControl')
make_head(_module, 'IAudioEndpointOffloadStreamMeter')
make_head(_module, 'IAudioEndpointOffloadStreamMute')
make_head(_module, 'IAudioEndpointOffloadStreamVolume')
make_head(_module, 'IAudioEndpointVolume')
make_head(_module, 'IAudioEndpointVolumeCallback')
make_head(_module, 'IAudioEndpointVolumeEx')
make_head(_module, 'IAudioLfxControl')
make_head(_module, 'IAudioMeterInformation')
make_head(_module, 'IHardwareAudioEngineBase')
