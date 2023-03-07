from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.MobileBroadband
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
class IDummyMBNUCMExt(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcbbbab6-ffff-4bbb-aa-ee-33-8e-36-8a-f6-fa')
class IMbnConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-200d-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def get_ConnectionID(ConnectionID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_InterfaceID(InterfaceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Connect(connectionMode: Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONNECTION_MODE, strProfile: Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Disconnect(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConnectionState(ConnectionState: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE), ProfileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVoiceCallState(voiceCallState: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CALL_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetActivationNetworkError(networkError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-200b-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetProvisionedContexts(provisionedContexts: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProvisionedContext(provisionedContexts: Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT, providerID: Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionContextEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-200c-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnProvisionedContextListChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetProvisionedContextComplete(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionContext_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-200e-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnConnectComplete(newConnection: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDisconnectComplete(newConnection: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnConnectStateChange(newConnection: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnVoiceCallStateChange(newConnection: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-201d-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetConnection(connectionID: Windows.Win32.Foundation.PWSTR, mbnConnection: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnections(mbnConnections: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionManagerEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-201e-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnConnectionArrival(newConnection: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnConnectionRemoval(oldConnection: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfile(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2010-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetProfileXmlData(profileData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateProfile(strProfile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete() -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfileEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2011-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnProfileUpdate(newProfile: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfileManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-200f-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetConnectionProfiles(mbnInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head, connectionProfiles: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnectionProfile(mbnInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head, profileName: Windows.Win32.Foundation.PWSTR, connectionProfile: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateConnectionProfile(xmlProfile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfileManagerEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-201f-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnConnectionProfileArrival(newConnectionProfile: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnConnectionProfileRemoval(oldConnectionProfile: Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b3bb9a71-dc70-4be9-a4-da-78-86-ae-8b-19-1b')
    @commethod(3)
    def QuerySupportedCommands(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenCommandSession(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CloseCommandSession(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetCommand(commandID: UInt32, deviceServiceData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryCommand(commandID: UInt32, deviceServiceData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenDataSession(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CloseDataSession(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WriteData(deviceServiceData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InterfaceID(InterfaceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DeviceServiceID(DeviceServiceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_IsCommandSessionOpen(value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsDataSessionOpen(value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServiceStateEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5d3ff196-89ee-49d8-8b-60-33-ff-dd-ff-c5-8d')
    @commethod(3)
    def OnSessionsStateChange(interfaceID: Windows.Win32.Foundation.BSTR, stateChange: Windows.Win32.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICE_SESSIONS_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServicesContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fc5ac347-1592-4068-80-bb-6a-57-58-01-50-d8')
    @commethod(3)
    def EnumerateDeviceServices(deviceServices: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceService(deviceServiceID: Windows.Win32.Foundation.BSTR, mbnDeviceService: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_MaxCommandSize(maxCommandSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_MaxDataSize(maxDataSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServicesEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0a900c19-6824-4e97-b7-6e-cf-23-9d-0c-a6-42')
    @commethod(3)
    def OnQuerySupportedCommandsComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, commandIDList: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnOpenCommandSessionComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnCloseCommandSessionComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSetCommandComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, responseID: UInt32, deviceServiceData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnQueryCommandComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, responseID: UInt32, deviceServiceData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnEventNotification(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, eventID: UInt32, deviceServiceData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnOpenDataSessionComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnCloseDataSessionComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnWriteDataComplete(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, status: Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnReadData(deviceService: Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService_head, deviceServiceData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnInterfaceStateChange(interfaceID: Windows.Win32.Foundation.BSTR, stateChange: Windows.Win32.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICES_INTERFACE_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServicesManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('20a26258-6811-4478-ac-1d-13-32-4e-45-e4-1c')
    @commethod(3)
    def GetDeviceServicesContext(networkInterfaceID: Windows.Win32.Foundation.BSTR, mbnDevicesContext: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceServicesContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnInterface(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2001-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def get_InterfaceID(InterfaceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInterfaceCapability(interfaceCaps: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSubscriberInformation(subscriberInformation: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnSubscriberInformation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReadyState(readyState: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InEmergencyMode(emergencyMode: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetHomeProvider(homeProvider: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPreferredProviders(preferredProviders: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetPreferredProviders(preferredProviders: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetVisibleProviders(age: POINTER(UInt32), visibleProviders: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ScanNetwork(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConnection(mbnConnection: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnInterfaceEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2002-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnInterfaceCapabilityAvailable(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSubscriberInformationChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnReadyStateChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnEmergencyModeChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnHomeProviderAvailable(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnPreferredProvidersChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSetPreferredProvidersComplete(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnScanNetworkComplete(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnInterfaceManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-201b-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetInterface(interfaceID: Windows.Win32.Foundation.PWSTR, mbnInterface: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInterfaces(mbnInterfaces: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnInterfaceManagerEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-201c-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnInterfaceArrival(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnInterfaceRemoval(oldInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnMultiCarrier(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2020-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def SetHomeProvider(homeProvider: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER2_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPreferredProviders(preferredMulticarrierProviders: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVisibleProviders(age: POINTER(UInt32), visibleProviders: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSupportedCellularClasses(cellularClasses: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentCellularClass(currentCellularClass: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ScanNetwork(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnMultiCarrierEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcdddab6-2021-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnSetHomeProviderComplete(mbnInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnCurrentCellularClassChange(mbnInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnPreferredProvidersChange(mbnInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnScanNetworkComplete(mbnInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnInterfaceCapabilityChange(mbnInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnPin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2007-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def get_PinType(PinType: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_PinFormat(PinFormat: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_FORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PinLengthMin(PinLengthMin: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_PinLengthMax(PinLengthMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_PinMode(PinMode: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Enable(pin: Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Disable(pin: Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Enter(pin: Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Change(pin: Windows.Win32.Foundation.PWSTR, newPin: Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Unblock(puk: Windows.Win32.Foundation.PWSTR, newPin: Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPinManager(pinManager: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnPinManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnPinEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2008-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnEnableComplete(pin: Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin_head, pinInfo: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head), requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDisableComplete(pin: Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin_head, pinInfo: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head), requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEnterComplete(Pin: Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin_head, pinInfo: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head), requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnChangeComplete(Pin: Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin_head, pinInfo: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head), requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUnblockComplete(Pin: Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin_head, pinInfo: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head), requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnPinManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2005-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetPinList(pinList: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPin(pinType: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE, pin: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPinState(requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnPinManagerEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2006-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnPinListAvailable(pinManager: Windows.Win32.NetworkManagement.MobileBroadband.IMbnPinManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnGetPinStateComplete(pinManager: Windows.Win32.NetworkManagement.MobileBroadband.IMbnPinManager_head, pinInfo: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnRadio(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dccccab6-201f-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def get_SoftwareRadioState(SoftwareRadioState: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_HardwareRadioState(HardwareRadioState: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSoftwareRadioState(radioState: Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnRadioEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcdddab6-201f-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnRadioStateChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnRadio_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetSoftwareRadioStateComplete(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnRadio_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnRegistration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2009-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetRegisterState(registerState: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRegisterMode(registerMode: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProviderID(providerID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProviderName(providerName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRoamingText(roamingText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAvailableDataClasses(availableDataClasses: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentDataClass(currentDataClass: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRegistrationNetworkError(registrationNetworkError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPacketAttachNetworkError(packetAttachNetworkError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetRegisterMode(registerMode: Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE, providerID: Windows.Win32.Foundation.PWSTR, dataClass: UInt32, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnRegistrationEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-200a-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnRegisterModeAvailable(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnRegisterStateChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnPacketServiceStateChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSetRegisterModeComplete(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnServiceActivation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2017-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def Activate(vendorSpecificData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnServiceActivationEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2018-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnActivationComplete(serviceActivation: Windows.Win32.NetworkManagement.MobileBroadband.IMbnServiceActivation_head, vendorSpecificData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: UInt32, status: Windows.Win32.Foundation.HRESULT, networkError: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSignal(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2003-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetSignalStrength(signalStrength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignalError(signalError: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSignalEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2004-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnSignalStateChange(newInterface: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSignal_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSms(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2015-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def GetSmsConfiguration(smsConfiguration: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.IMbnSmsConfiguration_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSmsConfiguration(smsConfiguration: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSmsConfiguration_head, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SmsSendPdu(pduData: Windows.Win32.Foundation.PWSTR, size: Byte, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SmsSendCdma(address: Windows.Win32.Foundation.PWSTR, encoding: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING, language: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG, sizeInCharacters: UInt32, message: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SmsSendCdmaPdu(message: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SmsRead(smsFilter: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FILTER_head), smsFormat: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT, requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SmsDelete(smsFilter: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FILTER_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSmsStatus(smsStatusInfo: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsConfiguration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2012-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def get_ServiceCenterAddress(scAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_ServiceCenterAddress(scAddress: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_MaxMessageIndex(index: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CdmaShortMsgSize(shortMsgSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_SmsFormat(smsFormat: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SmsFormat(smsFormat: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2016-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnSmsConfigurationChange(sms: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetSmsConfigurationComplete(sms: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnSmsSendComplete(sms: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSmsReadComplete(sms: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms_head, smsFormat: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT, readMsgs: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), moreMsgs: Windows.Win32.Foundation.VARIANT_BOOL, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnSmsNewClass0Message(sms: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms_head, smsFormat: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT, readMsgs: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnSmsDeleteComplete(sms: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms_head, requestID: UInt32, status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSmsStatusChange(sms: Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsReadMsgPdu(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2013-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def get_Index(Index: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Status(Status: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PduData(PduData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Message(Message: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsReadMsgTextCdma(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2014-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def get_Index(Index: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Status(Status: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Address(Address: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Timestamp(Timestamp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_EncodingID(EncodingID: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LanguageID(LanguageID: POINTER(Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SizeInCharacters(SizeInCharacters: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Message(Message: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnSubscriberInformation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('459ecc43-bcf5-11dc-a8-a8-00-13-21-f1-40-5f')
    @commethod(3)
    def get_SubscriberID(SubscriberID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SimIccID(SimIccID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_TelephoneNumbers(TelephoneNumbers: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnVendorSpecificEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-201a-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def OnEventNotification(vendorOperation: Windows.Win32.NetworkManagement.MobileBroadband.IMbnVendorSpecificOperation_head, vendorSpecificData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetVendorSpecificComplete(vendorOperation: Windows.Win32.NetworkManagement.MobileBroadband.IMbnVendorSpecificOperation_head, vendorSpecificData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMbnVendorSpecificOperation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcbbbab6-2019-4bbb-aa-ee-33-8e-36-8a-f6-fa')
    @commethod(3)
    def SetVendorSpecific(vendorSpecificData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), requestID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
MBN_ACTIVATION_STATE = Int32
MBN_ACTIVATION_STATE_NONE: MBN_ACTIVATION_STATE = 0
MBN_ACTIVATION_STATE_ACTIVATED: MBN_ACTIVATION_STATE = 1
MBN_ACTIVATION_STATE_ACTIVATING: MBN_ACTIVATION_STATE = 2
MBN_ACTIVATION_STATE_DEACTIVATED: MBN_ACTIVATION_STATE = 3
MBN_ACTIVATION_STATE_DEACTIVATING: MBN_ACTIVATION_STATE = 4
MBN_AUTH_PROTOCOL = Int32
MBN_AUTH_PROTOCOL_NONE: MBN_AUTH_PROTOCOL = 0
MBN_AUTH_PROTOCOL_PAP: MBN_AUTH_PROTOCOL = 1
MBN_AUTH_PROTOCOL_CHAP: MBN_AUTH_PROTOCOL = 2
MBN_AUTH_PROTOCOL_MSCHAPV2: MBN_AUTH_PROTOCOL = 3
MBN_BAND_CLASS = Int32
MBN_BAND_CLASS_NONE: MBN_BAND_CLASS = 0
MBN_BAND_CLASS_0: MBN_BAND_CLASS = 1
MBN_BAND_CLASS_I: MBN_BAND_CLASS = 2
MBN_BAND_CLASS_II: MBN_BAND_CLASS = 4
MBN_BAND_CLASS_III: MBN_BAND_CLASS = 8
MBN_BAND_CLASS_IV: MBN_BAND_CLASS = 16
MBN_BAND_CLASS_V: MBN_BAND_CLASS = 32
MBN_BAND_CLASS_VI: MBN_BAND_CLASS = 64
MBN_BAND_CLASS_VII: MBN_BAND_CLASS = 128
MBN_BAND_CLASS_VIII: MBN_BAND_CLASS = 256
MBN_BAND_CLASS_IX: MBN_BAND_CLASS = 512
MBN_BAND_CLASS_X: MBN_BAND_CLASS = 1024
MBN_BAND_CLASS_XI: MBN_BAND_CLASS = 2048
MBN_BAND_CLASS_XII: MBN_BAND_CLASS = 4096
MBN_BAND_CLASS_XIII: MBN_BAND_CLASS = 8192
MBN_BAND_CLASS_XIV: MBN_BAND_CLASS = 16384
MBN_BAND_CLASS_XV: MBN_BAND_CLASS = 32768
MBN_BAND_CLASS_XVI: MBN_BAND_CLASS = 65536
MBN_BAND_CLASS_XVII: MBN_BAND_CLASS = 131072
MBN_BAND_CLASS_CUSTOM: MBN_BAND_CLASS = -2147483648
MBN_CELLULAR_CLASS = Int32
MBN_CELLULAR_CLASS_NONE: MBN_CELLULAR_CLASS = 0
MBN_CELLULAR_CLASS_GSM: MBN_CELLULAR_CLASS = 1
MBN_CELLULAR_CLASS_CDMA: MBN_CELLULAR_CLASS = 2
MBN_COMPRESSION = Int32
MBN_COMPRESSION_NONE: MBN_COMPRESSION = 0
MBN_COMPRESSION_ENABLE: MBN_COMPRESSION = 1
MBN_CONNECTION_MODE = Int32
MBN_CONNECTION_MODE_PROFILE: MBN_CONNECTION_MODE = 0
MBN_CONNECTION_MODE_TMP_PROFILE: MBN_CONNECTION_MODE = 1
class MBN_CONTEXT(Structure):
    contextID: UInt32
    contextType: Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE
    accessString: Windows.Win32.Foundation.BSTR
    userName: Windows.Win32.Foundation.BSTR
    password: Windows.Win32.Foundation.BSTR
    compression: Windows.Win32.NetworkManagement.MobileBroadband.MBN_COMPRESSION
    authType: Windows.Win32.NetworkManagement.MobileBroadband.MBN_AUTH_PROTOCOL
MBN_CONTEXT_CONSTANTS = Int32
MBN_ACCESSSTRING_LEN: MBN_CONTEXT_CONSTANTS = 100
MBN_USERNAME_LEN: MBN_CONTEXT_CONSTANTS = 255
MBN_PASSWORD_LEN: MBN_CONTEXT_CONSTANTS = 255
MBN_CONTEXT_ID_APPEND: MBN_CONTEXT_CONSTANTS = -1
MBN_CONTEXT_TYPE = Int32
MBN_CONTEXT_TYPE_NONE: MBN_CONTEXT_TYPE = 0
MBN_CONTEXT_TYPE_INTERNET: MBN_CONTEXT_TYPE = 1
MBN_CONTEXT_TYPE_VPN: MBN_CONTEXT_TYPE = 2
MBN_CONTEXT_TYPE_VOICE: MBN_CONTEXT_TYPE = 3
MBN_CONTEXT_TYPE_VIDEO_SHARE: MBN_CONTEXT_TYPE = 4
MBN_CONTEXT_TYPE_CUSTOM: MBN_CONTEXT_TYPE = 5
MBN_CONTEXT_TYPE_PURCHASE: MBN_CONTEXT_TYPE = 6
MBN_CTRL_CAPS = Int32
MBN_CTRL_CAPS_NONE: MBN_CTRL_CAPS = 0
MBN_CTRL_CAPS_REG_MANUAL: MBN_CTRL_CAPS = 1
MBN_CTRL_CAPS_HW_RADIO_SWITCH: MBN_CTRL_CAPS = 2
MBN_CTRL_CAPS_CDMA_MOBILE_IP: MBN_CTRL_CAPS = 4
MBN_CTRL_CAPS_CDMA_SIMPLE_IP: MBN_CTRL_CAPS = 8
MBN_CTRL_CAPS_PROTECT_UNIQUEID: MBN_CTRL_CAPS = 16
MBN_CTRL_CAPS_MODEL_MULTI_CARRIER: MBN_CTRL_CAPS = 32
MBN_CTRL_CAPS_USSD: MBN_CTRL_CAPS = 64
MBN_CTRL_CAPS_MULTI_MODE: MBN_CTRL_CAPS = 128
MBN_DATA_CLASS = Int32
MBN_DATA_CLASS_NONE: MBN_DATA_CLASS = 0
MBN_DATA_CLASS_GPRS: MBN_DATA_CLASS = 1
MBN_DATA_CLASS_EDGE: MBN_DATA_CLASS = 2
MBN_DATA_CLASS_UMTS: MBN_DATA_CLASS = 4
MBN_DATA_CLASS_HSDPA: MBN_DATA_CLASS = 8
MBN_DATA_CLASS_HSUPA: MBN_DATA_CLASS = 16
MBN_DATA_CLASS_LTE: MBN_DATA_CLASS = 32
MBN_DATA_CLASS_5G_NSA: MBN_DATA_CLASS = 64
MBN_DATA_CLASS_5G_SA: MBN_DATA_CLASS = 128
MBN_DATA_CLASS_1XRTT: MBN_DATA_CLASS = 65536
MBN_DATA_CLASS_1XEVDO: MBN_DATA_CLASS = 131072
MBN_DATA_CLASS_1XEVDO_REVA: MBN_DATA_CLASS = 262144
MBN_DATA_CLASS_1XEVDV: MBN_DATA_CLASS = 524288
MBN_DATA_CLASS_3XRTT: MBN_DATA_CLASS = 1048576
MBN_DATA_CLASS_1XEVDO_REVB: MBN_DATA_CLASS = 2097152
MBN_DATA_CLASS_UMB: MBN_DATA_CLASS = 4194304
MBN_DATA_CLASS_CUSTOM: MBN_DATA_CLASS = -2147483648
class MBN_DEVICE_SERVICE(Structure):
    deviceServiceID: Windows.Win32.Foundation.BSTR
    dataWriteSupported: Windows.Win32.Foundation.VARIANT_BOOL
    dataReadSupported: Windows.Win32.Foundation.VARIANT_BOOL
MBN_DEVICE_SERVICES_INTERFACE_STATE = Int32
MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_ARRIVAL: MBN_DEVICE_SERVICES_INTERFACE_STATE = 0
MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_REMOVAL: MBN_DEVICE_SERVICES_INTERFACE_STATE = 1
MBN_DEVICE_SERVICE_SESSIONS_STATE = Int32
MBN_DEVICE_SERVICE_SESSIONS_RESTORED: MBN_DEVICE_SERVICE_SESSIONS_STATE = 0
class MBN_INTERFACE_CAPS(Structure):
    cellularClass: Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS
    voiceClass: Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CLASS
    dataClass: UInt32
    customDataClass: Windows.Win32.Foundation.BSTR
    gsmBandClass: UInt32
    cdmaBandClass: UInt32
    customBandClass: Windows.Win32.Foundation.BSTR
    smsCaps: UInt32
    controlCaps: UInt32
    deviceID: Windows.Win32.Foundation.BSTR
    manufacturer: Windows.Win32.Foundation.BSTR
    model: Windows.Win32.Foundation.BSTR
    firmwareInfo: Windows.Win32.Foundation.BSTR
MBN_INTERFACE_CAPS_CONSTANTS = Int32
MBN_DEVICEID_LEN: MBN_INTERFACE_CAPS_CONSTANTS = 18
MBN_MANUFACTURER_LEN: MBN_INTERFACE_CAPS_CONSTANTS = 32
MBN_MODEL_LEN: MBN_INTERFACE_CAPS_CONSTANTS = 32
MBN_FIRMWARE_LEN: MBN_INTERFACE_CAPS_CONSTANTS = 32
MBN_MSG_STATUS = Int32
MBN_MSG_STATUS_NEW: MBN_MSG_STATUS = 0
MBN_MSG_STATUS_OLD: MBN_MSG_STATUS = 1
MBN_MSG_STATUS_DRAFT: MBN_MSG_STATUS = 2
MBN_MSG_STATUS_SENT: MBN_MSG_STATUS = 3
MBN_PIN_CONSTANTS = Int32
MBN_ATTEMPTS_REMAINING_UNKNOWN: MBN_PIN_CONSTANTS = -1
MBN_PIN_LENGTH_UNKNOWN: MBN_PIN_CONSTANTS = -1
MBN_PIN_FORMAT = Int32
MBN_PIN_FORMAT_NONE: MBN_PIN_FORMAT = 0
MBN_PIN_FORMAT_NUMERIC: MBN_PIN_FORMAT = 1
MBN_PIN_FORMAT_ALPHANUMERIC: MBN_PIN_FORMAT = 2
class MBN_PIN_INFO(Structure):
    pinState: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_STATE
    pinType: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE
    attemptsRemaining: UInt32
MBN_PIN_MODE = Int32
MBN_PIN_MODE_ENABLED: MBN_PIN_MODE = 1
MBN_PIN_MODE_DISABLED: MBN_PIN_MODE = 2
MBN_PIN_STATE = Int32
MBN_PIN_STATE_NONE: MBN_PIN_STATE = 0
MBN_PIN_STATE_ENTER: MBN_PIN_STATE = 1
MBN_PIN_STATE_UNBLOCK: MBN_PIN_STATE = 2
MBN_PIN_TYPE = Int32
MBN_PIN_TYPE_NONE: MBN_PIN_TYPE = 0
MBN_PIN_TYPE_CUSTOM: MBN_PIN_TYPE = 1
MBN_PIN_TYPE_PIN1: MBN_PIN_TYPE = 2
MBN_PIN_TYPE_PIN2: MBN_PIN_TYPE = 3
MBN_PIN_TYPE_DEVICE_SIM_PIN: MBN_PIN_TYPE = 4
MBN_PIN_TYPE_DEVICE_FIRST_SIM_PIN: MBN_PIN_TYPE = 5
MBN_PIN_TYPE_NETWORK_PIN: MBN_PIN_TYPE = 6
MBN_PIN_TYPE_NETWORK_SUBSET_PIN: MBN_PIN_TYPE = 7
MBN_PIN_TYPE_SVC_PROVIDER_PIN: MBN_PIN_TYPE = 8
MBN_PIN_TYPE_CORPORATE_PIN: MBN_PIN_TYPE = 9
MBN_PIN_TYPE_SUBSIDY_LOCK: MBN_PIN_TYPE = 10
class MBN_PROVIDER(Structure):
    providerID: Windows.Win32.Foundation.BSTR
    providerState: UInt32
    providerName: Windows.Win32.Foundation.BSTR
    dataClass: UInt32
class MBN_PROVIDER2(Structure):
    provider: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER
    cellularClass: Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS
    signalStrength: UInt32
    signalError: UInt32
MBN_PROVIDER_CONSTANTS = Int32
MBN_PROVIDERNAME_LEN: MBN_PROVIDER_CONSTANTS = 20
MBN_PROVIDERID_LEN: MBN_PROVIDER_CONSTANTS = 6
MBN_PROVIDER_STATE = Int32
MBN_PROVIDER_STATE_NONE: MBN_PROVIDER_STATE = 0
MBN_PROVIDER_STATE_HOME: MBN_PROVIDER_STATE = 1
MBN_PROVIDER_STATE_FORBIDDEN: MBN_PROVIDER_STATE = 2
MBN_PROVIDER_STATE_PREFERRED: MBN_PROVIDER_STATE = 4
MBN_PROVIDER_STATE_VISIBLE: MBN_PROVIDER_STATE = 8
MBN_PROVIDER_STATE_REGISTERED: MBN_PROVIDER_STATE = 16
MBN_PROVIDER_STATE_PREFERRED_MULTICARRIER: MBN_PROVIDER_STATE = 32
MBN_RADIO = Int32
MBN_RADIO_OFF: MBN_RADIO = 0
MBN_RADIO_ON: MBN_RADIO = 1
MBN_READY_STATE = Int32
MBN_READY_STATE_OFF: MBN_READY_STATE = 0
MBN_READY_STATE_INITIALIZED: MBN_READY_STATE = 1
MBN_READY_STATE_SIM_NOT_INSERTED: MBN_READY_STATE = 2
MBN_READY_STATE_BAD_SIM: MBN_READY_STATE = 3
MBN_READY_STATE_FAILURE: MBN_READY_STATE = 4
MBN_READY_STATE_NOT_ACTIVATED: MBN_READY_STATE = 5
MBN_READY_STATE_DEVICE_LOCKED: MBN_READY_STATE = 6
MBN_READY_STATE_DEVICE_BLOCKED: MBN_READY_STATE = 7
MBN_READY_STATE_NO_ESIM_PROFILE: MBN_READY_STATE = 8
MBN_REGISTER_MODE = Int32
MBN_REGISTER_MODE_NONE: MBN_REGISTER_MODE = 0
MBN_REGISTER_MODE_AUTOMATIC: MBN_REGISTER_MODE = 1
MBN_REGISTER_MODE_MANUAL: MBN_REGISTER_MODE = 2
MBN_REGISTER_STATE = Int32
MBN_REGISTER_STATE_NONE: MBN_REGISTER_STATE = 0
MBN_REGISTER_STATE_DEREGISTERED: MBN_REGISTER_STATE = 1
MBN_REGISTER_STATE_SEARCHING: MBN_REGISTER_STATE = 2
MBN_REGISTER_STATE_HOME: MBN_REGISTER_STATE = 3
MBN_REGISTER_STATE_ROAMING: MBN_REGISTER_STATE = 4
MBN_REGISTER_STATE_PARTNER: MBN_REGISTER_STATE = 5
MBN_REGISTER_STATE_DENIED: MBN_REGISTER_STATE = 6
MBN_REGISTRATION_CONSTANTS = Int32
MBN_ROAMTEXT_LEN: MBN_REGISTRATION_CONSTANTS = 64
MBN_CDMA_DEFAULT_PROVIDER_ID: MBN_REGISTRATION_CONSTANTS = 0
MBN_SIGNAL_CONSTANTS = Int32
MBN_RSSI_DEFAULT: MBN_SIGNAL_CONSTANTS = -1
MBN_RSSI_DISABLE: MBN_SIGNAL_CONSTANTS = 0
MBN_RSSI_UNKNOWN: MBN_SIGNAL_CONSTANTS = 99
MBN_ERROR_RATE_UNKNOWN: MBN_SIGNAL_CONSTANTS = 99
MBN_SMS_CAPS = Int32
MBN_SMS_CAPS_NONE: MBN_SMS_CAPS = 0
MBN_SMS_CAPS_PDU_RECEIVE: MBN_SMS_CAPS = 1
MBN_SMS_CAPS_PDU_SEND: MBN_SMS_CAPS = 2
MBN_SMS_CAPS_TEXT_RECEIVE: MBN_SMS_CAPS = 4
MBN_SMS_CAPS_TEXT_SEND: MBN_SMS_CAPS = 8
MBN_SMS_CDMA_ENCODING = Int32
MBN_SMS_CDMA_ENCODING_OCTET: MBN_SMS_CDMA_ENCODING = 0
MBN_SMS_CDMA_ENCODING_EPM: MBN_SMS_CDMA_ENCODING = 1
MBN_SMS_CDMA_ENCODING_7BIT_ASCII: MBN_SMS_CDMA_ENCODING = 2
MBN_SMS_CDMA_ENCODING_IA5: MBN_SMS_CDMA_ENCODING = 3
MBN_SMS_CDMA_ENCODING_UNICODE: MBN_SMS_CDMA_ENCODING = 4
MBN_SMS_CDMA_ENCODING_SHIFT_JIS: MBN_SMS_CDMA_ENCODING = 5
MBN_SMS_CDMA_ENCODING_KOREAN: MBN_SMS_CDMA_ENCODING = 6
MBN_SMS_CDMA_ENCODING_LATIN_HEBREW: MBN_SMS_CDMA_ENCODING = 7
MBN_SMS_CDMA_ENCODING_LATIN: MBN_SMS_CDMA_ENCODING = 8
MBN_SMS_CDMA_ENCODING_GSM_7BIT: MBN_SMS_CDMA_ENCODING = 9
MBN_SMS_CDMA_LANG = Int32
MBN_SMS_CDMA_LANG_NONE: MBN_SMS_CDMA_LANG = 0
MBN_SMS_CDMA_LANG_ENGLISH: MBN_SMS_CDMA_LANG = 1
MBN_SMS_CDMA_LANG_FRENCH: MBN_SMS_CDMA_LANG = 2
MBN_SMS_CDMA_LANG_SPANISH: MBN_SMS_CDMA_LANG = 3
MBN_SMS_CDMA_LANG_JAPANESE: MBN_SMS_CDMA_LANG = 4
MBN_SMS_CDMA_LANG_KOREAN: MBN_SMS_CDMA_LANG = 5
MBN_SMS_CDMA_LANG_CHINESE: MBN_SMS_CDMA_LANG = 6
MBN_SMS_CDMA_LANG_HEBREW: MBN_SMS_CDMA_LANG = 7
class MBN_SMS_FILTER(Structure):
    flag: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG
    messageIndex: UInt32
MBN_SMS_FLAG = Int32
MBN_SMS_FLAG_ALL: MBN_SMS_FLAG = 0
MBN_SMS_FLAG_INDEX: MBN_SMS_FLAG = 1
MBN_SMS_FLAG_NEW: MBN_SMS_FLAG = 2
MBN_SMS_FLAG_OLD: MBN_SMS_FLAG = 3
MBN_SMS_FLAG_SENT: MBN_SMS_FLAG = 4
MBN_SMS_FLAG_DRAFT: MBN_SMS_FLAG = 5
MBN_SMS_FORMAT = Int32
MBN_SMS_FORMAT_NONE: MBN_SMS_FORMAT = 0
MBN_SMS_FORMAT_PDU: MBN_SMS_FORMAT = 1
MBN_SMS_FORMAT_TEXT: MBN_SMS_FORMAT = 2
MBN_SMS_STATUS_FLAG = Int32
MBN_SMS_FLAG_NONE: MBN_SMS_STATUS_FLAG = 0
MBN_SMS_FLAG_MESSAGE_STORE_FULL: MBN_SMS_STATUS_FLAG = 1
MBN_SMS_FLAG_NEW_MESSAGE: MBN_SMS_STATUS_FLAG = 2
class MBN_SMS_STATUS_INFO(Structure):
    flag: UInt32
    messageIndex: UInt32
MBN_VOICE_CALL_STATE = Int32
MBN_VOICE_CALL_STATE_NONE: MBN_VOICE_CALL_STATE = 0
MBN_VOICE_CALL_STATE_IN_PROGRESS: MBN_VOICE_CALL_STATE = 1
MBN_VOICE_CALL_STATE_HANGUP: MBN_VOICE_CALL_STATE = 2
MBN_VOICE_CLASS = Int32
MBN_VOICE_CLASS_NONE: MBN_VOICE_CLASS = 0
MBN_VOICE_CLASS_NO_VOICE: MBN_VOICE_CLASS = 1
MBN_VOICE_CLASS_SEPARATE_VOICE_DATA: MBN_VOICE_CLASS = 2
MBN_VOICE_CLASS_SIMULTANEOUS_VOICE_DATA: MBN_VOICE_CLASS = 3
MbnConnectionManager = Guid('bdfee05c-4418-11dd-90-ed-00-1c-25-7c-cf-f1')
MbnConnectionProfileManager = Guid('bdfee05a-4418-11dd-90-ed-00-1c-25-7c-cf-f1')
MbnDeviceServicesManager = Guid('2269daa3-2a9f-4165-a5-01-ce-00-a6-f7-a7-5b')
MbnInterfaceManager = Guid('bdfee05b-4418-11dd-90-ed-00-1c-25-7c-cf-f1')
WWAEXT_SMS_CONSTANTS = Int32
MBN_MESSAGE_INDEX_NONE: WWAEXT_SMS_CONSTANTS = 0
MBN_CDMA_SHORT_MSG_SIZE_UNKNOWN: WWAEXT_SMS_CONSTANTS = 0
MBN_CDMA_SHORT_MSG_SIZE_MAX: WWAEXT_SMS_CONSTANTS = 160
class __DummyPinType__(Structure):
    pinType: UInt32
class __mbnapi_ReferenceRemainingTypes__(Structure):
    bandClass: Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS
    contextConstants: Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_CONSTANTS
    ctrlCaps: Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS
    dataClass: Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS
    interfaceCapsConstants: Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_CONSTANTS
    pinConstants: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_CONSTANTS
    providerConstants: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_CONSTANTS
    providerState: Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE
    registrationConstants: Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTRATION_CONSTANTS
    signalConstants: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SIGNAL_CONSTANTS
    smsCaps: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CAPS
    smsConstants: Windows.Win32.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS
    wwaextSmsConstants: Windows.Win32.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS
    smsStatusFlag: Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_FLAG
make_head(_module, 'IDummyMBNUCMExt')
make_head(_module, 'IMbnConnection')
make_head(_module, 'IMbnConnectionContext')
make_head(_module, 'IMbnConnectionContextEvents')
make_head(_module, 'IMbnConnectionEvents')
make_head(_module, 'IMbnConnectionManager')
make_head(_module, 'IMbnConnectionManagerEvents')
make_head(_module, 'IMbnConnectionProfile')
make_head(_module, 'IMbnConnectionProfileEvents')
make_head(_module, 'IMbnConnectionProfileManager')
make_head(_module, 'IMbnConnectionProfileManagerEvents')
make_head(_module, 'IMbnDeviceService')
make_head(_module, 'IMbnDeviceServiceStateEvents')
make_head(_module, 'IMbnDeviceServicesContext')
make_head(_module, 'IMbnDeviceServicesEvents')
make_head(_module, 'IMbnDeviceServicesManager')
make_head(_module, 'IMbnInterface')
make_head(_module, 'IMbnInterfaceEvents')
make_head(_module, 'IMbnInterfaceManager')
make_head(_module, 'IMbnInterfaceManagerEvents')
make_head(_module, 'IMbnMultiCarrier')
make_head(_module, 'IMbnMultiCarrierEvents')
make_head(_module, 'IMbnPin')
make_head(_module, 'IMbnPinEvents')
make_head(_module, 'IMbnPinManager')
make_head(_module, 'IMbnPinManagerEvents')
make_head(_module, 'IMbnRadio')
make_head(_module, 'IMbnRadioEvents')
make_head(_module, 'IMbnRegistration')
make_head(_module, 'IMbnRegistrationEvents')
make_head(_module, 'IMbnServiceActivation')
make_head(_module, 'IMbnServiceActivationEvents')
make_head(_module, 'IMbnSignal')
make_head(_module, 'IMbnSignalEvents')
make_head(_module, 'IMbnSms')
make_head(_module, 'IMbnSmsConfiguration')
make_head(_module, 'IMbnSmsEvents')
make_head(_module, 'IMbnSmsReadMsgPdu')
make_head(_module, 'IMbnSmsReadMsgTextCdma')
make_head(_module, 'IMbnSubscriberInformation')
make_head(_module, 'IMbnVendorSpecificEvents')
make_head(_module, 'IMbnVendorSpecificOperation')
make_head(_module, 'MBN_CONTEXT')
make_head(_module, 'MBN_DEVICE_SERVICE')
make_head(_module, 'MBN_INTERFACE_CAPS')
make_head(_module, 'MBN_PIN_INFO')
make_head(_module, 'MBN_PROVIDER')
make_head(_module, 'MBN_PROVIDER2')
make_head(_module, 'MBN_SMS_FILTER')
make_head(_module, 'MBN_SMS_STATUS_INFO')
make_head(_module, '__DummyPinType__')
make_head(_module, '__mbnapi_ReferenceRemainingTypes__')
__all__ = [
    "IDummyMBNUCMExt",
    "IMbnConnection",
    "IMbnConnectionContext",
    "IMbnConnectionContextEvents",
    "IMbnConnectionEvents",
    "IMbnConnectionManager",
    "IMbnConnectionManagerEvents",
    "IMbnConnectionProfile",
    "IMbnConnectionProfileEvents",
    "IMbnConnectionProfileManager",
    "IMbnConnectionProfileManagerEvents",
    "IMbnDeviceService",
    "IMbnDeviceServiceStateEvents",
    "IMbnDeviceServicesContext",
    "IMbnDeviceServicesEvents",
    "IMbnDeviceServicesManager",
    "IMbnInterface",
    "IMbnInterfaceEvents",
    "IMbnInterfaceManager",
    "IMbnInterfaceManagerEvents",
    "IMbnMultiCarrier",
    "IMbnMultiCarrierEvents",
    "IMbnPin",
    "IMbnPinEvents",
    "IMbnPinManager",
    "IMbnPinManagerEvents",
    "IMbnRadio",
    "IMbnRadioEvents",
    "IMbnRegistration",
    "IMbnRegistrationEvents",
    "IMbnServiceActivation",
    "IMbnServiceActivationEvents",
    "IMbnSignal",
    "IMbnSignalEvents",
    "IMbnSms",
    "IMbnSmsConfiguration",
    "IMbnSmsEvents",
    "IMbnSmsReadMsgPdu",
    "IMbnSmsReadMsgTextCdma",
    "IMbnSubscriberInformation",
    "IMbnVendorSpecificEvents",
    "IMbnVendorSpecificOperation",
    "MBN_ACCESSSTRING_LEN",
    "MBN_ACTIVATION_STATE",
    "MBN_ACTIVATION_STATE_ACTIVATED",
    "MBN_ACTIVATION_STATE_ACTIVATING",
    "MBN_ACTIVATION_STATE_DEACTIVATED",
    "MBN_ACTIVATION_STATE_DEACTIVATING",
    "MBN_ACTIVATION_STATE_NONE",
    "MBN_ATTEMPTS_REMAINING_UNKNOWN",
    "MBN_AUTH_PROTOCOL",
    "MBN_AUTH_PROTOCOL_CHAP",
    "MBN_AUTH_PROTOCOL_MSCHAPV2",
    "MBN_AUTH_PROTOCOL_NONE",
    "MBN_AUTH_PROTOCOL_PAP",
    "MBN_BAND_CLASS",
    "MBN_BAND_CLASS_0",
    "MBN_BAND_CLASS_CUSTOM",
    "MBN_BAND_CLASS_I",
    "MBN_BAND_CLASS_II",
    "MBN_BAND_CLASS_III",
    "MBN_BAND_CLASS_IV",
    "MBN_BAND_CLASS_IX",
    "MBN_BAND_CLASS_NONE",
    "MBN_BAND_CLASS_V",
    "MBN_BAND_CLASS_VI",
    "MBN_BAND_CLASS_VII",
    "MBN_BAND_CLASS_VIII",
    "MBN_BAND_CLASS_X",
    "MBN_BAND_CLASS_XI",
    "MBN_BAND_CLASS_XII",
    "MBN_BAND_CLASS_XIII",
    "MBN_BAND_CLASS_XIV",
    "MBN_BAND_CLASS_XV",
    "MBN_BAND_CLASS_XVI",
    "MBN_BAND_CLASS_XVII",
    "MBN_CDMA_DEFAULT_PROVIDER_ID",
    "MBN_CDMA_SHORT_MSG_SIZE_MAX",
    "MBN_CDMA_SHORT_MSG_SIZE_UNKNOWN",
    "MBN_CELLULAR_CLASS",
    "MBN_CELLULAR_CLASS_CDMA",
    "MBN_CELLULAR_CLASS_GSM",
    "MBN_CELLULAR_CLASS_NONE",
    "MBN_COMPRESSION",
    "MBN_COMPRESSION_ENABLE",
    "MBN_COMPRESSION_NONE",
    "MBN_CONNECTION_MODE",
    "MBN_CONNECTION_MODE_PROFILE",
    "MBN_CONNECTION_MODE_TMP_PROFILE",
    "MBN_CONTEXT",
    "MBN_CONTEXT_CONSTANTS",
    "MBN_CONTEXT_ID_APPEND",
    "MBN_CONTEXT_TYPE",
    "MBN_CONTEXT_TYPE_CUSTOM",
    "MBN_CONTEXT_TYPE_INTERNET",
    "MBN_CONTEXT_TYPE_NONE",
    "MBN_CONTEXT_TYPE_PURCHASE",
    "MBN_CONTEXT_TYPE_VIDEO_SHARE",
    "MBN_CONTEXT_TYPE_VOICE",
    "MBN_CONTEXT_TYPE_VPN",
    "MBN_CTRL_CAPS",
    "MBN_CTRL_CAPS_CDMA_MOBILE_IP",
    "MBN_CTRL_CAPS_CDMA_SIMPLE_IP",
    "MBN_CTRL_CAPS_HW_RADIO_SWITCH",
    "MBN_CTRL_CAPS_MODEL_MULTI_CARRIER",
    "MBN_CTRL_CAPS_MULTI_MODE",
    "MBN_CTRL_CAPS_NONE",
    "MBN_CTRL_CAPS_PROTECT_UNIQUEID",
    "MBN_CTRL_CAPS_REG_MANUAL",
    "MBN_CTRL_CAPS_USSD",
    "MBN_DATA_CLASS",
    "MBN_DATA_CLASS_1XEVDO",
    "MBN_DATA_CLASS_1XEVDO_REVA",
    "MBN_DATA_CLASS_1XEVDO_REVB",
    "MBN_DATA_CLASS_1XEVDV",
    "MBN_DATA_CLASS_1XRTT",
    "MBN_DATA_CLASS_3XRTT",
    "MBN_DATA_CLASS_5G_NSA",
    "MBN_DATA_CLASS_5G_SA",
    "MBN_DATA_CLASS_CUSTOM",
    "MBN_DATA_CLASS_EDGE",
    "MBN_DATA_CLASS_GPRS",
    "MBN_DATA_CLASS_HSDPA",
    "MBN_DATA_CLASS_HSUPA",
    "MBN_DATA_CLASS_LTE",
    "MBN_DATA_CLASS_NONE",
    "MBN_DATA_CLASS_UMB",
    "MBN_DATA_CLASS_UMTS",
    "MBN_DEVICEID_LEN",
    "MBN_DEVICE_SERVICE",
    "MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_ARRIVAL",
    "MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_REMOVAL",
    "MBN_DEVICE_SERVICES_INTERFACE_STATE",
    "MBN_DEVICE_SERVICE_SESSIONS_RESTORED",
    "MBN_DEVICE_SERVICE_SESSIONS_STATE",
    "MBN_ERROR_RATE_UNKNOWN",
    "MBN_FIRMWARE_LEN",
    "MBN_INTERFACE_CAPS",
    "MBN_INTERFACE_CAPS_CONSTANTS",
    "MBN_MANUFACTURER_LEN",
    "MBN_MESSAGE_INDEX_NONE",
    "MBN_MODEL_LEN",
    "MBN_MSG_STATUS",
    "MBN_MSG_STATUS_DRAFT",
    "MBN_MSG_STATUS_NEW",
    "MBN_MSG_STATUS_OLD",
    "MBN_MSG_STATUS_SENT",
    "MBN_PASSWORD_LEN",
    "MBN_PIN_CONSTANTS",
    "MBN_PIN_FORMAT",
    "MBN_PIN_FORMAT_ALPHANUMERIC",
    "MBN_PIN_FORMAT_NONE",
    "MBN_PIN_FORMAT_NUMERIC",
    "MBN_PIN_INFO",
    "MBN_PIN_LENGTH_UNKNOWN",
    "MBN_PIN_MODE",
    "MBN_PIN_MODE_DISABLED",
    "MBN_PIN_MODE_ENABLED",
    "MBN_PIN_STATE",
    "MBN_PIN_STATE_ENTER",
    "MBN_PIN_STATE_NONE",
    "MBN_PIN_STATE_UNBLOCK",
    "MBN_PIN_TYPE",
    "MBN_PIN_TYPE_CORPORATE_PIN",
    "MBN_PIN_TYPE_CUSTOM",
    "MBN_PIN_TYPE_DEVICE_FIRST_SIM_PIN",
    "MBN_PIN_TYPE_DEVICE_SIM_PIN",
    "MBN_PIN_TYPE_NETWORK_PIN",
    "MBN_PIN_TYPE_NETWORK_SUBSET_PIN",
    "MBN_PIN_TYPE_NONE",
    "MBN_PIN_TYPE_PIN1",
    "MBN_PIN_TYPE_PIN2",
    "MBN_PIN_TYPE_SUBSIDY_LOCK",
    "MBN_PIN_TYPE_SVC_PROVIDER_PIN",
    "MBN_PROVIDER",
    "MBN_PROVIDER2",
    "MBN_PROVIDERID_LEN",
    "MBN_PROVIDERNAME_LEN",
    "MBN_PROVIDER_CONSTANTS",
    "MBN_PROVIDER_STATE",
    "MBN_PROVIDER_STATE_FORBIDDEN",
    "MBN_PROVIDER_STATE_HOME",
    "MBN_PROVIDER_STATE_NONE",
    "MBN_PROVIDER_STATE_PREFERRED",
    "MBN_PROVIDER_STATE_PREFERRED_MULTICARRIER",
    "MBN_PROVIDER_STATE_REGISTERED",
    "MBN_PROVIDER_STATE_VISIBLE",
    "MBN_RADIO",
    "MBN_RADIO_OFF",
    "MBN_RADIO_ON",
    "MBN_READY_STATE",
    "MBN_READY_STATE_BAD_SIM",
    "MBN_READY_STATE_DEVICE_BLOCKED",
    "MBN_READY_STATE_DEVICE_LOCKED",
    "MBN_READY_STATE_FAILURE",
    "MBN_READY_STATE_INITIALIZED",
    "MBN_READY_STATE_NOT_ACTIVATED",
    "MBN_READY_STATE_NO_ESIM_PROFILE",
    "MBN_READY_STATE_OFF",
    "MBN_READY_STATE_SIM_NOT_INSERTED",
    "MBN_REGISTER_MODE",
    "MBN_REGISTER_MODE_AUTOMATIC",
    "MBN_REGISTER_MODE_MANUAL",
    "MBN_REGISTER_MODE_NONE",
    "MBN_REGISTER_STATE",
    "MBN_REGISTER_STATE_DENIED",
    "MBN_REGISTER_STATE_DEREGISTERED",
    "MBN_REGISTER_STATE_HOME",
    "MBN_REGISTER_STATE_NONE",
    "MBN_REGISTER_STATE_PARTNER",
    "MBN_REGISTER_STATE_ROAMING",
    "MBN_REGISTER_STATE_SEARCHING",
    "MBN_REGISTRATION_CONSTANTS",
    "MBN_ROAMTEXT_LEN",
    "MBN_RSSI_DEFAULT",
    "MBN_RSSI_DISABLE",
    "MBN_RSSI_UNKNOWN",
    "MBN_SIGNAL_CONSTANTS",
    "MBN_SMS_CAPS",
    "MBN_SMS_CAPS_NONE",
    "MBN_SMS_CAPS_PDU_RECEIVE",
    "MBN_SMS_CAPS_PDU_SEND",
    "MBN_SMS_CAPS_TEXT_RECEIVE",
    "MBN_SMS_CAPS_TEXT_SEND",
    "MBN_SMS_CDMA_ENCODING",
    "MBN_SMS_CDMA_ENCODING_7BIT_ASCII",
    "MBN_SMS_CDMA_ENCODING_EPM",
    "MBN_SMS_CDMA_ENCODING_GSM_7BIT",
    "MBN_SMS_CDMA_ENCODING_IA5",
    "MBN_SMS_CDMA_ENCODING_KOREAN",
    "MBN_SMS_CDMA_ENCODING_LATIN",
    "MBN_SMS_CDMA_ENCODING_LATIN_HEBREW",
    "MBN_SMS_CDMA_ENCODING_OCTET",
    "MBN_SMS_CDMA_ENCODING_SHIFT_JIS",
    "MBN_SMS_CDMA_ENCODING_UNICODE",
    "MBN_SMS_CDMA_LANG",
    "MBN_SMS_CDMA_LANG_CHINESE",
    "MBN_SMS_CDMA_LANG_ENGLISH",
    "MBN_SMS_CDMA_LANG_FRENCH",
    "MBN_SMS_CDMA_LANG_HEBREW",
    "MBN_SMS_CDMA_LANG_JAPANESE",
    "MBN_SMS_CDMA_LANG_KOREAN",
    "MBN_SMS_CDMA_LANG_NONE",
    "MBN_SMS_CDMA_LANG_SPANISH",
    "MBN_SMS_FILTER",
    "MBN_SMS_FLAG",
    "MBN_SMS_FLAG_ALL",
    "MBN_SMS_FLAG_DRAFT",
    "MBN_SMS_FLAG_INDEX",
    "MBN_SMS_FLAG_MESSAGE_STORE_FULL",
    "MBN_SMS_FLAG_NEW",
    "MBN_SMS_FLAG_NEW_MESSAGE",
    "MBN_SMS_FLAG_NONE",
    "MBN_SMS_FLAG_OLD",
    "MBN_SMS_FLAG_SENT",
    "MBN_SMS_FORMAT",
    "MBN_SMS_FORMAT_NONE",
    "MBN_SMS_FORMAT_PDU",
    "MBN_SMS_FORMAT_TEXT",
    "MBN_SMS_STATUS_FLAG",
    "MBN_SMS_STATUS_INFO",
    "MBN_USERNAME_LEN",
    "MBN_VOICE_CALL_STATE",
    "MBN_VOICE_CALL_STATE_HANGUP",
    "MBN_VOICE_CALL_STATE_IN_PROGRESS",
    "MBN_VOICE_CALL_STATE_NONE",
    "MBN_VOICE_CLASS",
    "MBN_VOICE_CLASS_NONE",
    "MBN_VOICE_CLASS_NO_VOICE",
    "MBN_VOICE_CLASS_SEPARATE_VOICE_DATA",
    "MBN_VOICE_CLASS_SIMULTANEOUS_VOICE_DATA",
    "MbnConnectionManager",
    "MbnConnectionProfileManager",
    "MbnDeviceServicesManager",
    "MbnInterfaceManager",
    "WWAEXT_SMS_CONSTANTS",
    "__DummyPinType__",
    "__mbnapi_ReferenceRemainingTypes__",
]
_arch_optional = [
]