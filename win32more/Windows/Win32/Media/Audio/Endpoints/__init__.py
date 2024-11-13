from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Audio.Apo
import win32more.Windows.Win32.Media.Audio.Endpoints
import win32more.Windows.Win32.Media.KernelStreaming
import win32more.Windows.Win32.System.Com
class AUDIO_ENDPOINT_SHARED_CREATE_PARAMS(Structure):
    u32Size: UInt32
    u32TSSessionId: UInt32
    targetEndpointConnectorType: win32more.Windows.Win32.Media.Audio.Endpoints.EndpointConnectorType
    wfxDeviceFormat: win32more.Windows.Win32.Media.Audio.WAVEFORMATEX
DEVPKEY_AudioEndpointPlugin_FactoryCLSID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{12d83bd7-cf12-46be-8540-812710d3021c}'), pid=1)
DEVPKEY_AudioEndpointPlugin_DataFlow: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{12d83bd7-cf12-46be-8540-812710d3021c}'), pid=2)
DEVPKEY_AudioEndpointPlugin_PnPInterface: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{12d83bd7-cf12-46be-8540-812710d3021c}'), pid=3)
DEVPKEY_AudioEndpointPlugin2_FactoryCLSID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{12d83bd7-cf12-46be-8540-812710d3021c}'), pid=4)
DEVINTERFACE_AUDIOENDPOINTPLUGIN = Guid('{9f2f7b66-65ac-4fa6-8ae4-123c78b89313}')
EndpointConnectorType = Int32
eHostProcessConnector: win32more.Windows.Win32.Media.Audio.Endpoints.EndpointConnectorType = 0
eOffloadConnector: win32more.Windows.Win32.Media.Audio.Endpoints.EndpointConnectorType = 1
eLoopbackConnector: win32more.Windows.Win32.Media.Audio.Endpoints.EndpointConnectorType = 2
eKeywordDetectorConnector: win32more.Windows.Win32.Media.Audio.Endpoints.EndpointConnectorType = 3
eConnectorCount: win32more.Windows.Win32.Media.Audio.Endpoints.EndpointConnectorType = 4
class IAudioEndpointFormatControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{784cfd40-9f89-456e-a1a6-873b006a664e}')
    @commethod(3)
    def ResetToDefault(self, ResetFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointLastBufferControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f8520dd3-8f9d-4437-9861-62f584c33dd6}')
    @commethod(3)
    def IsLastBufferControlSupported(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def ReleaseOutputDataPointerForLastBuffer(self, pConnectionProperty: POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY)) -> Void: ...
class IAudioEndpointOffloadStreamMeter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e1546dce-9dd1-418b-9ab2-348ced161c86}')
    @commethod(3)
    def GetMeterChannelCount(self, pu32ChannelCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMeteringData(self, u32ChannelCount: UInt32, pf32PeakValues: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointOffloadStreamMute(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfe21355-5ec2-40e0-8d6b-710ac3c00249}')
    @commethod(3)
    def SetMute(self, bMuted: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMute(self, pbMuted: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointOffloadStreamVolume(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64f1dd49-71ca-4281-8672-3a9eddd1d0b6}')
    @commethod(3)
    def GetVolumeChannelCount(self, pu32ChannelCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetChannelVolumes(self, u32ChannelCount: UInt32, pf32Volumes: POINTER(Single), u32CurveType: win32more.Windows.Win32.Media.KernelStreaming.AUDIO_CURVE_TYPE, pCurveDuration: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelVolumes(self, u32ChannelCount: UInt32, pf32Volumes: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointVolume(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5cdf2c82-841e-4546-9722-0cf74078229a}')
    @commethod(3)
    def RegisterControlChangeNotify(self, pNotify: win32more.Windows.Win32.Media.Audio.Endpoints.IAudioEndpointVolumeCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterControlChangeNotify(self, pNotify: win32more.Windows.Win32.Media.Audio.Endpoints.IAudioEndpointVolumeCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelCount(self, pnChannelCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMasterVolumeLevel(self, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMasterVolumeLevelScalar(self, fLevel: Single, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMasterVolumeLevel(self, pfLevelDB: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMasterVolumeLevelScalar(self, pfLevel: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetChannelVolumeLevel(self, nChannel: UInt32, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetChannelVolumeLevelScalar(self, nChannel: UInt32, fLevel: Single, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetChannelVolumeLevel(self, nChannel: UInt32, pfLevelDB: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetChannelVolumeLevelScalar(self, nChannel: UInt32, pfLevel: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetMute(self, bMute: win32more.Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetMute(self, pbMute: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetVolumeStepInfo(self, pnStep: POINTER(UInt32), pnStepCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def VolumeStepUp(self, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def VolumeStepDown(self, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def QueryHardwareSupport(self, pdwHardwareSupportMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetVolumeRange(self, pflVolumeMindB: POINTER(Single), pflVolumeMaxdB: POINTER(Single), pflVolumeIncrementdB: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointVolumeCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{657804fa-d6ad-4496-8a60-352752af4f89}')
    @commethod(3)
    def OnNotify(self, pNotify: POINTER(win32more.Windows.Win32.Media.Audio.AUDIO_VOLUME_NOTIFICATION_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointVolumeEx(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.Endpoints.IAudioEndpointVolume
    _iid_ = Guid('{66e11784-f695-4f28-a505-a7080081a78f}')
    @commethod(21)
    def GetVolumeRangeChannel(self, iChannel: UInt32, pflVolumeMindB: POINTER(Single), pflVolumeMaxdB: POINTER(Single), pflVolumeIncrementdB: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioLfxControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{076a6922-d802-4f83-baf6-409d9ca11bfe}')
    @commethod(3)
    def SetLocalEffectsState(self, bEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalEffectsState(self, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioMeterInformation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c02216f6-8c67-4b5b-9d00-d008e73e0064}')
    @commethod(3)
    def GetPeakValue(self, pfPeak: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMeteringChannelCount(self, pnChannelCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelsPeakValues(self, u32ChannelCount: UInt32, afPeakValues: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryHardwareSupport(self, pdwHardwareSupportMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHardwareAudioEngineBase(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eddce3e4-f3c1-453a-b461-223563cbd886}')
    @commethod(3)
    def GetAvailableOffloadConnectorCount(self, _pwstrDeviceId: win32more.Windows.Win32.Foundation.PWSTR, _uConnectorId: UInt32, _pAvailableConnectorInstanceCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEngineFormat(self, pDevice: win32more.Windows.Win32.Media.Audio.IMMDevice, _bRequestDeviceFormat: win32more.Windows.Win32.Foundation.BOOL, _ppwfxFormat: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetEngineDeviceFormat(self, pDevice: win32more.Windows.Win32.Media.Audio.IMMDevice, _pwfxFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetGfxState(self, pDevice: win32more.Windows.Win32.Media.Audio.IMMDevice, _bEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGfxState(self, pDevice: win32more.Windows.Win32.Media.Audio.IMMDevice, _pbEnable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
