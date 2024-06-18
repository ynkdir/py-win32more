from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.MobileBroadband
import win32more.Windows.Win32.System.Com
class IDummyMBNUCMExt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcbbbab6-ffff-4bbb-aaee-338e368af6fa}')
class IMbnConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-200d-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def get_ConnectionID(self, ConnectionID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_InterfaceID(self, InterfaceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Connect(self, connectionMode: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONNECTION_MODE, strProfile: win32more.Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Disconnect(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConnectionState(self, ConnectionState: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE), ProfileName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVoiceCallState(self, voiceCallState: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CALL_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetActivationNetworkError(self, networkError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-200b-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetProvisionedContexts(self, provisionedContexts: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProvisionedContext(self, provisionedContexts: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT, providerID: win32more.Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionContextEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-200c-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnProvisionedContextListChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetProvisionedContextComplete(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionContext, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-200e-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnConnectComplete(self, newConnection: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDisconnectComplete(self, newConnection: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnConnectStateChange(self, newConnection: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnVoiceCallStateChange(self, newConnection: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-201d-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetConnection(self, connectionID: win32more.Windows.Win32.Foundation.PWSTR, mbnConnection: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnections(self, mbnConnections: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-201e-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnConnectionArrival(self, newConnection: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnConnectionRemoval(self, oldConnection: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2010-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetProfileXmlData(self, profileData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateProfile(self, strProfile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfileEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2011-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnProfileUpdate(self, newProfile: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfileManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-200f-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetConnectionProfiles(self, mbnInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface, connectionProfiles: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnectionProfile(self, mbnInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface, profileName: win32more.Windows.Win32.Foundation.PWSTR, connectionProfile: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateConnectionProfile(self, xmlProfile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnConnectionProfileManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-201f-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnConnectionProfileArrival(self, newConnectionProfile: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnConnectionProfileRemoval(self, oldConnectionProfile: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnectionProfile) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b3bb9a71-dc70-4be9-a4da-7886ae8b191b}')
    @commethod(3)
    def QuerySupportedCommands(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenCommandSession(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CloseCommandSession(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetCommand(self, commandID: UInt32, deviceServiceData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryCommand(self, commandID: UInt32, deviceServiceData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenDataSession(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CloseDataSession(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WriteData(self, deviceServiceData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InterfaceID(self, InterfaceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DeviceServiceID(self, DeviceServiceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_IsCommandSessionOpen(self, value: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsDataSessionOpen(self, value: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServiceStateEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d3ff196-89ee-49d8-8b60-33ffddffc58d}')
    @commethod(3)
    def OnSessionsStateChange(self, interfaceID: win32more.Windows.Win32.Foundation.BSTR, stateChange: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICE_SESSIONS_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServicesContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc5ac347-1592-4068-80bb-6a57580150d8}')
    @commethod(3)
    def EnumerateDeviceServices(self, deviceServices: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceService(self, deviceServiceID: win32more.Windows.Win32.Foundation.BSTR, mbnDeviceService: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_MaxCommandSize(self, maxCommandSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_MaxDataSize(self, maxDataSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServicesEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0a900c19-6824-4e97-b76e-cf239d0ca642}')
    @commethod(3)
    def OnQuerySupportedCommandsComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, commandIDList: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnOpenCommandSessionComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnCloseCommandSessionComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSetCommandComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, responseID: UInt32, deviceServiceData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnQueryCommandComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, responseID: UInt32, deviceServiceData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnEventNotification(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, eventID: UInt32, deviceServiceData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnOpenDataSessionComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnCloseDataSessionComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnWriteDataComplete(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, status: win32more.Windows.Win32.Foundation.HRESULT, requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnReadData(self, deviceService: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceService, deviceServiceData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnInterfaceStateChange(self, interfaceID: win32more.Windows.Win32.Foundation.BSTR, stateChange: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICES_INTERFACE_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnDeviceServicesManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20a26258-6811-4478-ac1d-13324e45e41c}')
    @commethod(3)
    def GetDeviceServicesContext(self, networkInterfaceID: win32more.Windows.Win32.Foundation.BSTR, mbnDevicesContext: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnDeviceServicesContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnInterface(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2001-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def get_InterfaceID(self, InterfaceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInterfaceCapability(self, interfaceCaps: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSubscriberInformation(self, subscriberInformation: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSubscriberInformation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReadyState(self, readyState: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InEmergencyMode(self, emergencyMode: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetHomeProvider(self, homeProvider: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPreferredProviders(self, preferredProviders: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetPreferredProviders(self, preferredProviders: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetVisibleProviders(self, age: POINTER(UInt32), visibleProviders: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ScanNetwork(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConnection(self, mbnConnection: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnConnection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnInterfaceEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2002-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnInterfaceCapabilityAvailable(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSubscriberInformationChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnReadyStateChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnEmergencyModeChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnHomeProviderAvailable(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnPreferredProvidersChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSetPreferredProvidersComplete(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnScanNetworkComplete(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnInterfaceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-201b-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetInterface(self, interfaceID: win32more.Windows.Win32.Foundation.PWSTR, mbnInterface: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInterfaces(self, mbnInterfaces: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnInterfaceManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-201c-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnInterfaceArrival(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnInterfaceRemoval(self, oldInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnInterface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnMultiCarrier(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2020-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def SetHomeProvider(self, homeProvider: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER2), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPreferredProviders(self, preferredMulticarrierProviders: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVisibleProviders(self, age: POINTER(UInt32), visibleProviders: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSupportedCellularClasses(self, cellularClasses: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentCellularClass(self, currentCellularClass: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ScanNetwork(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnMultiCarrierEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcdddab6-2021-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnSetHomeProviderComplete(self, mbnInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnCurrentCellularClassChange(self, mbnInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnPreferredProvidersChange(self, mbnInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnScanNetworkComplete(self, mbnInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnInterfaceCapabilityChange(self, mbnInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnMultiCarrier) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnPin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2007-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def get_PinType(self, PinType: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_PinFormat(self, PinFormat: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_FORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PinLengthMin(self, PinLengthMin: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_PinLengthMax(self, PinLengthMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_PinMode(self, PinMode: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Enable(self, pin: win32more.Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Disable(self, pin: win32more.Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Enter(self, pin: win32more.Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Change(self, pin: win32more.Windows.Win32.Foundation.PWSTR, newPin: win32more.Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Unblock(self, puk: win32more.Windows.Win32.Foundation.PWSTR, newPin: win32more.Windows.Win32.Foundation.PWSTR, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPinManager(self, pinManager: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPinManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnPinEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2008-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnEnableComplete(self, pin: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin, pinInfo: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO), requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDisableComplete(self, pin: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin, pinInfo: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO), requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEnterComplete(self, Pin: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin, pinInfo: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO), requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnChangeComplete(self, Pin: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin, pinInfo: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO), requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUnblockComplete(self, Pin: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin, pinInfo: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO), requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnPinManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2005-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetPinList(self, pinList: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPin(self, pinType: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE, pin: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPinState(self, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnPinManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2006-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnPinListAvailable(self, pinManager: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPinManager) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnGetPinStateComplete(self, pinManager: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnPinManager, pinInfo: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_INFO, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnRadio(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dccccab6-201f-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def get_SoftwareRadioState(self, SoftwareRadioState: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_HardwareRadioState(self, HardwareRadioState: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSoftwareRadioState(self, radioState: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnRadioEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcdddab6-201f-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnRadioStateChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnRadio) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetSoftwareRadioStateComplete(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnRadio, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2009-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetRegisterState(self, registerState: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRegisterMode(self, registerMode: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProviderID(self, providerID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProviderName(self, providerName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRoamingText(self, roamingText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAvailableDataClasses(self, availableDataClasses: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentDataClass(self, currentDataClass: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRegistrationNetworkError(self, registrationNetworkError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPacketAttachNetworkError(self, packetAttachNetworkError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetRegisterMode(self, registerMode: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE, providerID: win32more.Windows.Win32.Foundation.PWSTR, dataClass: UInt32, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnRegistrationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-200a-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnRegisterModeAvailable(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnRegisterStateChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnPacketServiceStateChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSetRegisterModeComplete(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnRegistration, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnServiceActivation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2017-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def Activate(self, vendorSpecificData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnServiceActivationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2018-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnActivationComplete(self, serviceActivation: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnServiceActivation, vendorSpecificData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT, networkError: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSignal(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2003-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetSignalStrength(self, signalStrength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignalError(self, signalError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSignalEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2004-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnSignalStateChange(self, newInterface: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSignal) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSms(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2015-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def GetSmsConfiguration(self, smsConfiguration: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSmsConfiguration)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSmsConfiguration(self, smsConfiguration: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSmsConfiguration, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SmsSendPdu(self, pduData: win32more.Windows.Win32.Foundation.PWSTR, size: Byte, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SmsSendCdma(self, address: win32more.Windows.Win32.Foundation.PWSTR, encoding: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING, language: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG, sizeInCharacters: UInt32, message: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SmsSendCdmaPdu(self, message: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SmsRead(self, smsFilter: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FILTER), smsFormat: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT, requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SmsDelete(self, smsFilter: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FILTER), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSmsStatus(self, smsStatusInfo: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2012-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def get_ServiceCenterAddress(self, scAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_ServiceCenterAddress(self, scAddress: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_MaxMessageIndex(self, index: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CdmaShortMsgSize(self, shortMsgSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_SmsFormat(self, smsFormat: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SmsFormat(self, smsFormat: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2016-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnSmsConfigurationChange(self, sms: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetSmsConfigurationComplete(self, sms: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnSmsSendComplete(self, sms: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSmsReadComplete(self, sms: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms, smsFormat: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT, readMsgs: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), moreMsgs: win32more.Windows.Win32.Foundation.VARIANT_BOOL, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnSmsNewClass0Message(self, sms: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms, smsFormat: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT, readMsgs: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnSmsDeleteComplete(self, sms: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms, requestID: UInt32, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSmsStatusChange(self, sms: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnSms) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsReadMsgPdu(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2013-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def get_Index(self, Index: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Status(self, Status: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PduData(self, PduData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Message(self, Message: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSmsReadMsgTextCdma(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2014-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def get_Index(self, Index: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Status(self, Status: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Address(self, Address: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Timestamp(self, Timestamp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_EncodingID(self, EncodingID: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LanguageID(self, LanguageID: POINTER(win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SizeInCharacters(self, SizeInCharacters: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Message(self, Message: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnSubscriberInformation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{459ecc43-bcf5-11dc-a8a8-001321f1405f}')
    @commethod(3)
    def get_SubscriberID(self, SubscriberID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SimIccID(self, SimIccID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_TelephoneNumbers(self, TelephoneNumbers: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnVendorSpecificEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-201a-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def OnEventNotification(self, vendorOperation: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnVendorSpecificOperation, vendorSpecificData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSetVendorSpecificComplete(self, vendorOperation: win32more.Windows.Win32.NetworkManagement.MobileBroadband.IMbnVendorSpecificOperation, vendorSpecificData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMbnVendorSpecificOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcbbbab6-2019-4bbb-aaee-338e368af6fa}')
    @commethod(3)
    def SetVendorSpecific(self, vendorSpecificData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), requestID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MBN_ACTIVATION_STATE = Int32
MBN_ACTIVATION_STATE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE = 0
MBN_ACTIVATION_STATE_ACTIVATED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE = 1
MBN_ACTIVATION_STATE_ACTIVATING: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE = 2
MBN_ACTIVATION_STATE_DEACTIVATED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE = 3
MBN_ACTIVATION_STATE_DEACTIVATING: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE = 4
MBN_AUTH_PROTOCOL = Int32
MBN_AUTH_PROTOCOL_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_AUTH_PROTOCOL = 0
MBN_AUTH_PROTOCOL_PAP: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_AUTH_PROTOCOL = 1
MBN_AUTH_PROTOCOL_CHAP: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_AUTH_PROTOCOL = 2
MBN_AUTH_PROTOCOL_MSCHAPV2: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_AUTH_PROTOCOL = 3
MBN_BAND_CLASS = Int32
MBN_BAND_CLASS_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 0
MBN_BAND_CLASS_0: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 1
MBN_BAND_CLASS_I: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 2
MBN_BAND_CLASS_II: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 4
MBN_BAND_CLASS_III: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 8
MBN_BAND_CLASS_IV: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 16
MBN_BAND_CLASS_V: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 32
MBN_BAND_CLASS_VI: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 64
MBN_BAND_CLASS_VII: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 128
MBN_BAND_CLASS_VIII: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 256
MBN_BAND_CLASS_IX: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 512
MBN_BAND_CLASS_X: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 1024
MBN_BAND_CLASS_XI: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 2048
MBN_BAND_CLASS_XII: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 4096
MBN_BAND_CLASS_XIII: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 8192
MBN_BAND_CLASS_XIV: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 16384
MBN_BAND_CLASS_XV: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 32768
MBN_BAND_CLASS_XVI: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 65536
MBN_BAND_CLASS_XVII: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = 131072
MBN_BAND_CLASS_CUSTOM: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS = -2147483648
MBN_CELLULAR_CLASS = Int32
MBN_CELLULAR_CLASS_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS = 0
MBN_CELLULAR_CLASS_GSM: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS = 1
MBN_CELLULAR_CLASS_CDMA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS = 2
MBN_COMPRESSION = Int32
MBN_COMPRESSION_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_COMPRESSION = 0
MBN_COMPRESSION_ENABLE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_COMPRESSION = 1
MBN_CONNECTION_MODE = Int32
MBN_CONNECTION_MODE_PROFILE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONNECTION_MODE = 0
MBN_CONNECTION_MODE_TMP_PROFILE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONNECTION_MODE = 1
class MBN_CONTEXT(Structure):
    contextID: UInt32
    contextType: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE
    accessString: win32more.Windows.Win32.Foundation.BSTR
    userName: win32more.Windows.Win32.Foundation.BSTR
    password: win32more.Windows.Win32.Foundation.BSTR
    compression: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_COMPRESSION
    authType: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_AUTH_PROTOCOL
MBN_CONTEXT_CONSTANTS = Int32
MBN_ACCESSSTRING_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_CONSTANTS = 100
MBN_USERNAME_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_CONSTANTS = 255
MBN_PASSWORD_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_CONSTANTS = 255
MBN_CONTEXT_ID_APPEND: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_CONSTANTS = -1
MBN_CONTEXT_TYPE = Int32
MBN_CONTEXT_TYPE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE = 0
MBN_CONTEXT_TYPE_INTERNET: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE = 1
MBN_CONTEXT_TYPE_VPN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE = 2
MBN_CONTEXT_TYPE_VOICE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE = 3
MBN_CONTEXT_TYPE_VIDEO_SHARE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE = 4
MBN_CONTEXT_TYPE_CUSTOM: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE = 5
MBN_CONTEXT_TYPE_PURCHASE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE = 6
MBN_CTRL_CAPS = Int32
MBN_CTRL_CAPS_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 0
MBN_CTRL_CAPS_REG_MANUAL: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 1
MBN_CTRL_CAPS_HW_RADIO_SWITCH: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 2
MBN_CTRL_CAPS_CDMA_MOBILE_IP: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 4
MBN_CTRL_CAPS_CDMA_SIMPLE_IP: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 8
MBN_CTRL_CAPS_PROTECT_UNIQUEID: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 16
MBN_CTRL_CAPS_MODEL_MULTI_CARRIER: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 32
MBN_CTRL_CAPS_USSD: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 64
MBN_CTRL_CAPS_MULTI_MODE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS = 128
MBN_DATA_CLASS = Int32
MBN_DATA_CLASS_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 0
MBN_DATA_CLASS_GPRS: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 1
MBN_DATA_CLASS_EDGE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 2
MBN_DATA_CLASS_UMTS: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 4
MBN_DATA_CLASS_HSDPA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 8
MBN_DATA_CLASS_HSUPA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 16
MBN_DATA_CLASS_LTE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 32
MBN_DATA_CLASS_5G_NSA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 64
MBN_DATA_CLASS_5G_SA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 128
MBN_DATA_CLASS_1XRTT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 65536
MBN_DATA_CLASS_1XEVDO: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 131072
MBN_DATA_CLASS_1XEVDO_REVA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 262144
MBN_DATA_CLASS_1XEVDV: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 524288
MBN_DATA_CLASS_3XRTT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 1048576
MBN_DATA_CLASS_1XEVDO_REVB: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 2097152
MBN_DATA_CLASS_UMB: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = 4194304
MBN_DATA_CLASS_CUSTOM: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS = -2147483648
class MBN_DEVICE_SERVICE(Structure):
    deviceServiceID: win32more.Windows.Win32.Foundation.BSTR
    dataWriteSupported: win32more.Windows.Win32.Foundation.VARIANT_BOOL
    dataReadSupported: win32more.Windows.Win32.Foundation.VARIANT_BOOL
MBN_DEVICE_SERVICES_INTERFACE_STATE = Int32
MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_ARRIVAL: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICES_INTERFACE_STATE = 0
MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_REMOVAL: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICES_INTERFACE_STATE = 1
MBN_DEVICE_SERVICE_SESSIONS_STATE = Int32
MBN_DEVICE_SERVICE_SESSIONS_RESTORED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICE_SESSIONS_STATE = 0
class MBN_INTERFACE_CAPS(Structure):
    cellularClass: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS
    voiceClass: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CLASS
    dataClass: UInt32
    customDataClass: win32more.Windows.Win32.Foundation.BSTR
    gsmBandClass: UInt32
    cdmaBandClass: UInt32
    customBandClass: win32more.Windows.Win32.Foundation.BSTR
    smsCaps: UInt32
    controlCaps: UInt32
    deviceID: win32more.Windows.Win32.Foundation.BSTR
    manufacturer: win32more.Windows.Win32.Foundation.BSTR
    model: win32more.Windows.Win32.Foundation.BSTR
    firmwareInfo: win32more.Windows.Win32.Foundation.BSTR
MBN_INTERFACE_CAPS_CONSTANTS = Int32
MBN_DEVICEID_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_CONSTANTS = 18
MBN_MANUFACTURER_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_CONSTANTS = 32
MBN_MODEL_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_CONSTANTS = 32
MBN_FIRMWARE_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_CONSTANTS = 32
MBN_MSG_STATUS = Int32
MBN_MSG_STATUS_NEW: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS = 0
MBN_MSG_STATUS_OLD: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS = 1
MBN_MSG_STATUS_DRAFT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS = 2
MBN_MSG_STATUS_SENT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_MSG_STATUS = 3
MBN_PIN_CONSTANTS = Int32
MBN_ATTEMPTS_REMAINING_UNKNOWN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_CONSTANTS = -1
MBN_PIN_LENGTH_UNKNOWN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_CONSTANTS = -1
MBN_PIN_FORMAT = Int32
MBN_PIN_FORMAT_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_FORMAT = 0
MBN_PIN_FORMAT_NUMERIC: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_FORMAT = 1
MBN_PIN_FORMAT_ALPHANUMERIC: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_FORMAT = 2
class MBN_PIN_INFO(Structure):
    pinState: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_STATE
    pinType: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE
    attemptsRemaining: UInt32
MBN_PIN_MODE = Int32
MBN_PIN_MODE_ENABLED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_MODE = 1
MBN_PIN_MODE_DISABLED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_MODE = 2
MBN_PIN_STATE = Int32
MBN_PIN_STATE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_STATE = 0
MBN_PIN_STATE_ENTER: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_STATE = 1
MBN_PIN_STATE_UNBLOCK: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_STATE = 2
MBN_PIN_TYPE = Int32
MBN_PIN_TYPE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 0
MBN_PIN_TYPE_CUSTOM: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 1
MBN_PIN_TYPE_PIN1: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 2
MBN_PIN_TYPE_PIN2: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 3
MBN_PIN_TYPE_DEVICE_SIM_PIN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 4
MBN_PIN_TYPE_DEVICE_FIRST_SIM_PIN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 5
MBN_PIN_TYPE_NETWORK_PIN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 6
MBN_PIN_TYPE_NETWORK_SUBSET_PIN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 7
MBN_PIN_TYPE_SVC_PROVIDER_PIN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 8
MBN_PIN_TYPE_CORPORATE_PIN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 9
MBN_PIN_TYPE_SUBSIDY_LOCK: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_TYPE = 10
class MBN_PROVIDER(Structure):
    providerID: win32more.Windows.Win32.Foundation.BSTR
    providerState: UInt32
    providerName: win32more.Windows.Win32.Foundation.BSTR
    dataClass: UInt32
class MBN_PROVIDER2(Structure):
    provider: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER
    cellularClass: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS
    signalStrength: UInt32
    signalError: UInt32
MBN_PROVIDER_CONSTANTS = Int32
MBN_PROVIDERNAME_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_CONSTANTS = 20
MBN_PROVIDERID_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_CONSTANTS = 6
MBN_PROVIDER_STATE = Int32
MBN_PROVIDER_STATE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE = 0
MBN_PROVIDER_STATE_HOME: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE = 1
MBN_PROVIDER_STATE_FORBIDDEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE = 2
MBN_PROVIDER_STATE_PREFERRED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE = 4
MBN_PROVIDER_STATE_VISIBLE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE = 8
MBN_PROVIDER_STATE_REGISTERED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE = 16
MBN_PROVIDER_STATE_PREFERRED_MULTICARRIER: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE = 32
MBN_RADIO = Int32
MBN_RADIO_OFF: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO = 0
MBN_RADIO_ON: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_RADIO = 1
MBN_READY_STATE = Int32
MBN_READY_STATE_OFF: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 0
MBN_READY_STATE_INITIALIZED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 1
MBN_READY_STATE_SIM_NOT_INSERTED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 2
MBN_READY_STATE_BAD_SIM: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 3
MBN_READY_STATE_FAILURE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 4
MBN_READY_STATE_NOT_ACTIVATED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 5
MBN_READY_STATE_DEVICE_LOCKED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 6
MBN_READY_STATE_DEVICE_BLOCKED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 7
MBN_READY_STATE_NO_ESIM_PROFILE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_READY_STATE = 8
MBN_REGISTER_MODE = Int32
MBN_REGISTER_MODE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE = 0
MBN_REGISTER_MODE_AUTOMATIC: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE = 1
MBN_REGISTER_MODE_MANUAL: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE = 2
MBN_REGISTER_STATE = Int32
MBN_REGISTER_STATE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE = 0
MBN_REGISTER_STATE_DEREGISTERED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE = 1
MBN_REGISTER_STATE_SEARCHING: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE = 2
MBN_REGISTER_STATE_HOME: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE = 3
MBN_REGISTER_STATE_ROAMING: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE = 4
MBN_REGISTER_STATE_PARTNER: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE = 5
MBN_REGISTER_STATE_DENIED: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE = 6
MBN_REGISTRATION_CONSTANTS = Int32
MBN_ROAMTEXT_LEN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTRATION_CONSTANTS = 64
MBN_CDMA_DEFAULT_PROVIDER_ID: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTRATION_CONSTANTS = 0
MBN_SIGNAL_CONSTANTS = Int32
MBN_RSSI_DEFAULT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SIGNAL_CONSTANTS = -1
MBN_RSSI_DISABLE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SIGNAL_CONSTANTS = 0
MBN_RSSI_UNKNOWN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SIGNAL_CONSTANTS = 99
MBN_ERROR_RATE_UNKNOWN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SIGNAL_CONSTANTS = 99
MBN_SMS_CAPS = Int32
MBN_SMS_CAPS_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CAPS = 0
MBN_SMS_CAPS_PDU_RECEIVE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CAPS = 1
MBN_SMS_CAPS_PDU_SEND: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CAPS = 2
MBN_SMS_CAPS_TEXT_RECEIVE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CAPS = 4
MBN_SMS_CAPS_TEXT_SEND: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CAPS = 8
MBN_SMS_CDMA_ENCODING = Int32
MBN_SMS_CDMA_ENCODING_OCTET: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 0
MBN_SMS_CDMA_ENCODING_EPM: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 1
MBN_SMS_CDMA_ENCODING_7BIT_ASCII: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 2
MBN_SMS_CDMA_ENCODING_IA5: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 3
MBN_SMS_CDMA_ENCODING_UNICODE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 4
MBN_SMS_CDMA_ENCODING_SHIFT_JIS: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 5
MBN_SMS_CDMA_ENCODING_KOREAN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 6
MBN_SMS_CDMA_ENCODING_LATIN_HEBREW: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 7
MBN_SMS_CDMA_ENCODING_LATIN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 8
MBN_SMS_CDMA_ENCODING_GSM_7BIT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING = 9
MBN_SMS_CDMA_LANG = Int32
MBN_SMS_CDMA_LANG_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 0
MBN_SMS_CDMA_LANG_ENGLISH: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 1
MBN_SMS_CDMA_LANG_FRENCH: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 2
MBN_SMS_CDMA_LANG_SPANISH: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 3
MBN_SMS_CDMA_LANG_JAPANESE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 4
MBN_SMS_CDMA_LANG_KOREAN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 5
MBN_SMS_CDMA_LANG_CHINESE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 6
MBN_SMS_CDMA_LANG_HEBREW: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG = 7
class MBN_SMS_FILTER(Structure):
    flag: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG
    messageIndex: UInt32
MBN_SMS_FLAG = Int32
MBN_SMS_FLAG_ALL: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG = 0
MBN_SMS_FLAG_INDEX: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG = 1
MBN_SMS_FLAG_NEW: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG = 2
MBN_SMS_FLAG_OLD: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG = 3
MBN_SMS_FLAG_SENT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG = 4
MBN_SMS_FLAG_DRAFT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FLAG = 5
MBN_SMS_FORMAT = Int32
MBN_SMS_FORMAT_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT = 0
MBN_SMS_FORMAT_PDU: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT = 1
MBN_SMS_FORMAT_TEXT: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT = 2
MBN_SMS_STATUS_FLAG = Int32
MBN_SMS_FLAG_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_FLAG = 0
MBN_SMS_FLAG_MESSAGE_STORE_FULL: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_FLAG = 1
MBN_SMS_FLAG_NEW_MESSAGE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_FLAG = 2
class MBN_SMS_STATUS_INFO(Structure):
    flag: UInt32
    messageIndex: UInt32
MBN_VOICE_CALL_STATE = Int32
MBN_VOICE_CALL_STATE_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CALL_STATE = 0
MBN_VOICE_CALL_STATE_IN_PROGRESS: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CALL_STATE = 1
MBN_VOICE_CALL_STATE_HANGUP: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CALL_STATE = 2
MBN_VOICE_CLASS = Int32
MBN_VOICE_CLASS_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CLASS = 0
MBN_VOICE_CLASS_NO_VOICE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CLASS = 1
MBN_VOICE_CLASS_SEPARATE_VOICE_DATA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CLASS = 2
MBN_VOICE_CLASS_SIMULTANEOUS_VOICE_DATA: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_VOICE_CLASS = 3
MbnConnectionManager = Guid('{bdfee05c-4418-11dd-90ed-001c257ccff1}')
MbnConnectionProfileManager = Guid('{bdfee05a-4418-11dd-90ed-001c257ccff1}')
MbnDeviceServicesManager = Guid('{2269daa3-2a9f-4165-a501-ce00a6f7a75b}')
MbnInterfaceManager = Guid('{bdfee05b-4418-11dd-90ed-001c257ccff1}')
WWAEXT_SMS_CONSTANTS = Int32
MBN_MESSAGE_INDEX_NONE: win32more.Windows.Win32.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS = 0
MBN_CDMA_SHORT_MSG_SIZE_UNKNOWN: win32more.Windows.Win32.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS = 0
MBN_CDMA_SHORT_MSG_SIZE_MAX: win32more.Windows.Win32.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS = 160
class __DummyPinType__(Structure):
    pinType: UInt32
class __mbnapi_ReferenceRemainingTypes__(Structure):
    bandClass: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_BAND_CLASS
    contextConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CONTEXT_CONSTANTS
    ctrlCaps: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS
    dataClass: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_DATA_CLASS
    interfaceCapsConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_CONSTANTS
    pinConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PIN_CONSTANTS
    providerConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_CONSTANTS
    providerState: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE
    registrationConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_REGISTRATION_CONSTANTS
    signalConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SIGNAL_CONSTANTS
    smsCaps: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_CAPS
    smsConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS
    wwaextSmsConstants: win32more.Windows.Win32.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS
    smsStatusFlag: win32more.Windows.Win32.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_FLAG


make_ready(__name__)
