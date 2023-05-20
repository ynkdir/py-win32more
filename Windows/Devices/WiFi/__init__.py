from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Devices.WiFi
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking.Connectivity
import Windows.Security.Credentials
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWiFiAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAdapter'
    _iid_ = Guid('{a6c4e423-3d75-43a4-b9de-11e26b72d9b0}')
    @winrt_commethod(6)
    def get_NetworkAdapter(self) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(7)
    def ScanAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_NetworkReport(self) -> Windows.Devices.WiFi.WiFiNetworkReport: ...
    @winrt_commethod(9)
    def add_AvailableNetworksChanged(self, args: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFi.WiFiAdapter, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_AvailableNetworksChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def ConnectAsync(self, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_commethod(12)
    def ConnectWithPasswordCredentialAsync(self, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_commethod(13)
    def ConnectWithPasswordCredentialAndSsidAsync(self, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_commethod(14)
    def Disconnect(self) -> Void: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkReport = property(get_NetworkReport, None)
class IWiFiAdapter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAdapter2'
    _iid_ = Guid('{5bc4501d-81e4-453d-9430-1fcafbadd6b6}')
    @winrt_commethod(6)
    def GetWpsConfigurationAsync(self, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiWpsConfigurationResult]: ...
    @winrt_commethod(7)
    def ConnectWithPasswordCredentialAndSsidAndConnectionMethodAsync(self, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String, connectionMethod: Windows.Devices.WiFi.WiFiConnectionMethod) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
class IWiFiAdapterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAdapterStatics'
    _iid_ = Guid('{da25fddd-d24c-43e3-aabd-c4659f730f99}')
    @winrt_commethod(6)
    def FindAllAdaptersAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFi.WiFiAdapter]]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiAdapter]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiAccessStatus]: ...
class IWiFiAvailableNetwork(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAvailableNetwork'
    _iid_ = Guid('{26e96246-183e-4704-9826-71b4a2f0f668}')
    @winrt_commethod(6)
    def get_Uptime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_Ssid(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Bssid(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ChannelCenterFrequencyInKilohertz(self) -> Int32: ...
    @winrt_commethod(10)
    def get_NetworkRssiInDecibelMilliwatts(self) -> Double: ...
    @winrt_commethod(11)
    def get_SignalBars(self) -> Byte: ...
    @winrt_commethod(12)
    def get_NetworkKind(self) -> Windows.Devices.WiFi.WiFiNetworkKind: ...
    @winrt_commethod(13)
    def get_PhyKind(self) -> Windows.Devices.WiFi.WiFiPhyKind: ...
    @winrt_commethod(14)
    def get_SecuritySettings(self) -> Windows.Networking.Connectivity.NetworkSecuritySettings: ...
    @winrt_commethod(15)
    def get_BeaconInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(16)
    def get_IsWiFiDirect(self) -> Boolean: ...
    Uptime = property(get_Uptime, None)
    Ssid = property(get_Ssid, None)
    Bssid = property(get_Bssid, None)
    ChannelCenterFrequencyInKilohertz = property(get_ChannelCenterFrequencyInKilohertz, None)
    NetworkRssiInDecibelMilliwatts = property(get_NetworkRssiInDecibelMilliwatts, None)
    SignalBars = property(get_SignalBars, None)
    NetworkKind = property(get_NetworkKind, None)
    PhyKind = property(get_PhyKind, None)
    SecuritySettings = property(get_SecuritySettings, None)
    BeaconInterval = property(get_BeaconInterval, None)
    IsWiFiDirect = property(get_IsWiFiDirect, None)
class IWiFiConnectionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiConnectionResult'
    _iid_ = Guid('{143bdfd9-c37d-40be-a5c8-857bce85a931}')
    @winrt_commethod(6)
    def get_ConnectionStatus(self) -> Windows.Devices.WiFi.WiFiConnectionStatus: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
class IWiFiNetworkReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiNetworkReport'
    _iid_ = Guid('{9524ded2-5911-445e-8194-be4f1a704895}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AvailableNetworks(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFi.WiFiAvailableNetwork]: ...
    Timestamp = property(get_Timestamp, None)
    AvailableNetworks = property(get_AvailableNetworks, None)
class IWiFiOnDemandHotspotConnectTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails'
    _iid_ = Guid('{a268eb58-68f5-59cf-8d38-35bf44b097ef}')
    @winrt_commethod(6)
    def get_RequestedNetwork(self) -> Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
    @winrt_commethod(7)
    def ReportError(self, status: Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus) -> Void: ...
    @winrt_commethod(8)
    def ConnectAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult]: ...
    @winrt_commethod(9)
    def Connect(self) -> Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult: ...
    RequestedNetwork = property(get_RequestedNetwork, None)
class IWiFiOnDemandHotspotConnectionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectionResult'
    _iid_ = Guid('{911794a1-6c82-5de3-8a4a-f9ff22a4957a}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus: ...
    Status = property(get_Status, None)
class IWiFiOnDemandHotspotNetwork(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork'
    _iid_ = Guid('{18dc7115-a04e-507c-bbaf-b78369d29fa7}')
    @winrt_commethod(6)
    def GetProperties(self) -> Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties: ...
    @winrt_commethod(7)
    def UpdateProperties(self, newProperties: Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties) -> Void: ...
    @winrt_commethod(8)
    def get_Id(self) -> Guid: ...
    Id = property(get_Id, None)
class IWiFiOnDemandHotspotNetworkProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties'
    _iid_ = Guid('{c810a1f2-c81d-5852-be50-e4bd4d81e98d}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Availability(self) -> Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability: ...
    @winrt_commethod(9)
    def put_Availability(self, value: Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability) -> Void: ...
    @winrt_commethod(10)
    def get_RemainingBatteryPercent(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(11)
    def put_RemainingBatteryPercent(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(12)
    def get_CellularBars(self) -> Windows.Foundation.IReference[Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]: ...
    @winrt_commethod(13)
    def put_CellularBars(self, value: Windows.Foundation.IReference[Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]) -> Void: ...
    @winrt_commethod(14)
    def get_IsMetered(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsMetered(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Ssid(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_Ssid(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_Password(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(19)
    def put_Password(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Availability = property(get_Availability, put_Availability)
    RemainingBatteryPercent = property(get_RemainingBatteryPercent, put_RemainingBatteryPercent)
    CellularBars = property(get_CellularBars, put_CellularBars)
    IsMetered = property(get_IsMetered, put_IsMetered)
    Ssid = property(get_Ssid, put_Ssid)
    Password = property(get_Password, put_Password)
class IWiFiOnDemandHotspotNetworkStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkStatics'
    _iid_ = Guid('{00f5b8ac-80e7-5054-871c-8739f374e3c9}')
    @winrt_commethod(6)
    def GetOrCreateById(self, networkId: Guid) -> Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
class IWiFiWpsConfigurationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiWpsConfigurationResult'
    _iid_ = Guid('{67b49871-17ee-42d1-b14f-5a11f1226fb5}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.WiFi.WiFiWpsConfigurationStatus: ...
    @winrt_commethod(7)
    def get_SupportedWpsKinds(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFi.WiFiWpsKind]: ...
    Status = property(get_Status, None)
    SupportedWpsKinds = property(get_SupportedWpsKinds, None)
WiFiAccessStatus = Int32
WiFiAccessStatus_Unspecified: WiFiAccessStatus = 0
WiFiAccessStatus_Allowed: WiFiAccessStatus = 1
WiFiAccessStatus_DeniedByUser: WiFiAccessStatus = 2
WiFiAccessStatus_DeniedBySystem: WiFiAccessStatus = 3
class WiFiAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiAdapter
    _classid_ = 'Windows.Devices.WiFi.WiFiAdapter'
    @winrt_mixinmethod
    def get_NetworkAdapter(self: Windows.Devices.WiFi.IWiFiAdapter) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def ScanAsync(self: Windows.Devices.WiFi.IWiFiAdapter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_NetworkReport(self: Windows.Devices.WiFi.IWiFiAdapter) -> Windows.Devices.WiFi.WiFiNetworkReport: ...
    @winrt_mixinmethod
    def add_AvailableNetworksChanged(self: Windows.Devices.WiFi.IWiFiAdapter, args: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFi.WiFiAdapter, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableNetworksChanged(self: Windows.Devices.WiFi.IWiFiAdapter, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Devices.WiFi.IWiFiAdapter, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_mixinmethod
    def ConnectWithPasswordCredentialAsync(self: Windows.Devices.WiFi.IWiFiAdapter, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_mixinmethod
    def ConnectWithPasswordCredentialAndSsidAsync(self: Windows.Devices.WiFi.IWiFiAdapter, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_mixinmethod
    def Disconnect(self: Windows.Devices.WiFi.IWiFiAdapter) -> Void: ...
    @winrt_mixinmethod
    def GetWpsConfigurationAsync(self: Windows.Devices.WiFi.IWiFiAdapter2, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiWpsConfigurationResult]: ...
    @winrt_mixinmethod
    def ConnectWithPasswordCredentialAndSsidAndConnectionMethodAsync(self: Windows.Devices.WiFi.IWiFiAdapter2, availableNetwork: Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String, connectionMethod: Windows.Devices.WiFi.WiFiConnectionMethod) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_classmethod
    def FindAllAdaptersAsync(cls: Windows.Devices.WiFi.IWiFiAdapterStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFi.WiFiAdapter]]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.WiFi.IWiFiAdapterStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.WiFi.IWiFiAdapterStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiAdapter]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Devices.WiFi.IWiFiAdapterStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiAccessStatus]: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkReport = property(get_NetworkReport, None)
class WiFiAvailableNetwork(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiAvailableNetwork
    _classid_ = 'Windows.Devices.WiFi.WiFiAvailableNetwork'
    @winrt_mixinmethod
    def get_Uptime(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Ssid(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Bssid(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChannelCenterFrequencyInKilohertz(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Int32: ...
    @winrt_mixinmethod
    def get_NetworkRssiInDecibelMilliwatts(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Double: ...
    @winrt_mixinmethod
    def get_SignalBars(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Byte: ...
    @winrt_mixinmethod
    def get_NetworkKind(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Windows.Devices.WiFi.WiFiNetworkKind: ...
    @winrt_mixinmethod
    def get_PhyKind(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Windows.Devices.WiFi.WiFiPhyKind: ...
    @winrt_mixinmethod
    def get_SecuritySettings(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Windows.Networking.Connectivity.NetworkSecuritySettings: ...
    @winrt_mixinmethod
    def get_BeaconInterval(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IsWiFiDirect(self: Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Boolean: ...
    Uptime = property(get_Uptime, None)
    Ssid = property(get_Ssid, None)
    Bssid = property(get_Bssid, None)
    ChannelCenterFrequencyInKilohertz = property(get_ChannelCenterFrequencyInKilohertz, None)
    NetworkRssiInDecibelMilliwatts = property(get_NetworkRssiInDecibelMilliwatts, None)
    SignalBars = property(get_SignalBars, None)
    NetworkKind = property(get_NetworkKind, None)
    PhyKind = property(get_PhyKind, None)
    SecuritySettings = property(get_SecuritySettings, None)
    BeaconInterval = property(get_BeaconInterval, None)
    IsWiFiDirect = property(get_IsWiFiDirect, None)
WiFiConnectionMethod = Int32
WiFiConnectionMethod_Default: WiFiConnectionMethod = 0
WiFiConnectionMethod_WpsPin: WiFiConnectionMethod = 1
WiFiConnectionMethod_WpsPushButton: WiFiConnectionMethod = 2
class WiFiConnectionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiConnectionResult
    _classid_ = 'Windows.Devices.WiFi.WiFiConnectionResult'
    @winrt_mixinmethod
    def get_ConnectionStatus(self: Windows.Devices.WiFi.IWiFiConnectionResult) -> Windows.Devices.WiFi.WiFiConnectionStatus: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
WiFiConnectionStatus = Int32
WiFiConnectionStatus_UnspecifiedFailure: WiFiConnectionStatus = 0
WiFiConnectionStatus_Success: WiFiConnectionStatus = 1
WiFiConnectionStatus_AccessRevoked: WiFiConnectionStatus = 2
WiFiConnectionStatus_InvalidCredential: WiFiConnectionStatus = 3
WiFiConnectionStatus_NetworkNotAvailable: WiFiConnectionStatus = 4
WiFiConnectionStatus_Timeout: WiFiConnectionStatus = 5
WiFiConnectionStatus_UnsupportedAuthenticationProtocol: WiFiConnectionStatus = 6
WiFiNetworkKind = Int32
WiFiNetworkKind_Any: WiFiNetworkKind = 0
WiFiNetworkKind_Infrastructure: WiFiNetworkKind = 1
WiFiNetworkKind_Adhoc: WiFiNetworkKind = 2
class WiFiNetworkReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiNetworkReport
    _classid_ = 'Windows.Devices.WiFi.WiFiNetworkReport'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.WiFi.IWiFiNetworkReport) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AvailableNetworks(self: Windows.Devices.WiFi.IWiFiNetworkReport) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFi.WiFiAvailableNetwork]: ...
    Timestamp = property(get_Timestamp, None)
    AvailableNetworks = property(get_AvailableNetworks, None)
WiFiOnDemandHotspotAvailability = Int32
WiFiOnDemandHotspotAvailability_Available: WiFiOnDemandHotspotAvailability = 0
WiFiOnDemandHotspotAvailability_Unavailable: WiFiOnDemandHotspotAvailability = 1
WiFiOnDemandHotspotCellularBars = Int32
WiFiOnDemandHotspotCellularBars_ZeroBars: WiFiOnDemandHotspotCellularBars = 0
WiFiOnDemandHotspotCellularBars_OneBar: WiFiOnDemandHotspotCellularBars = 1
WiFiOnDemandHotspotCellularBars_TwoBars: WiFiOnDemandHotspotCellularBars = 2
WiFiOnDemandHotspotCellularBars_ThreeBars: WiFiOnDemandHotspotCellularBars = 3
WiFiOnDemandHotspotCellularBars_FourBars: WiFiOnDemandHotspotCellularBars = 4
WiFiOnDemandHotspotCellularBars_FiveBars: WiFiOnDemandHotspotCellularBars = 5
WiFiOnDemandHotspotConnectStatus = Int32
WiFiOnDemandHotspotConnectStatus_UnspecifiedFailure: WiFiOnDemandHotspotConnectStatus = 0
WiFiOnDemandHotspotConnectStatus_Success: WiFiOnDemandHotspotConnectStatus = 1
WiFiOnDemandHotspotConnectStatus_AppTimedOut: WiFiOnDemandHotspotConnectStatus = 2
WiFiOnDemandHotspotConnectStatus_InvalidCredential: WiFiOnDemandHotspotConnectStatus = 3
WiFiOnDemandHotspotConnectStatus_NetworkNotAvailable: WiFiOnDemandHotspotConnectStatus = 4
WiFiOnDemandHotspotConnectStatus_UnsupportedAuthenticationProtocol: WiFiOnDemandHotspotConnectStatus = 5
WiFiOnDemandHotspotConnectStatus_BluetoothConnectFailed: WiFiOnDemandHotspotConnectStatus = 6
WiFiOnDemandHotspotConnectStatus_BluetoothTransmissionError: WiFiOnDemandHotspotConnectStatus = 7
WiFiOnDemandHotspotConnectStatus_OperationCanceledByUser: WiFiOnDemandHotspotConnectStatus = 8
WiFiOnDemandHotspotConnectStatus_EntitlementCheckFailed: WiFiOnDemandHotspotConnectStatus = 9
WiFiOnDemandHotspotConnectStatus_NoCellularSignal: WiFiOnDemandHotspotConnectStatus = 10
WiFiOnDemandHotspotConnectStatus_CellularDataTurnedOff: WiFiOnDemandHotspotConnectStatus = 11
WiFiOnDemandHotspotConnectStatus_WlanConnectFailed: WiFiOnDemandHotspotConnectStatus = 12
WiFiOnDemandHotspotConnectStatus_WlanNotVisible: WiFiOnDemandHotspotConnectStatus = 13
WiFiOnDemandHotspotConnectStatus_AccessPointCannotConnect: WiFiOnDemandHotspotConnectStatus = 14
WiFiOnDemandHotspotConnectStatus_CellularConnectTimedOut: WiFiOnDemandHotspotConnectStatus = 15
WiFiOnDemandHotspotConnectStatus_RoamingNotAllowed: WiFiOnDemandHotspotConnectStatus = 16
WiFiOnDemandHotspotConnectStatus_PairingRequired: WiFiOnDemandHotspotConnectStatus = 17
WiFiOnDemandHotspotConnectStatus_DataLimitReached: WiFiOnDemandHotspotConnectStatus = 18
class WiFiOnDemandHotspotConnectTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotConnectTriggerDetails'
    @winrt_mixinmethod
    def get_RequestedNetwork(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails) -> Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
    @winrt_mixinmethod
    def ReportError(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails, status: Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus) -> Void: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult]: ...
    @winrt_mixinmethod
    def Connect(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails) -> Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult: ...
    RequestedNetwork = property(get_RequestedNetwork, None)
class WiFiOnDemandHotspotConnectionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectionResult
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectionResult) -> Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus: ...
    Status = property(get_Status, None)
class WiFiOnDemandHotspotNetwork(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork'
    @winrt_mixinmethod
    def GetProperties(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork) -> Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties: ...
    @winrt_mixinmethod
    def UpdateProperties(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork, newProperties: Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork) -> Guid: ...
    @winrt_classmethod
    def GetOrCreateById(cls: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkStatics, networkId: Guid) -> Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
    Id = property(get_Id, None)
class WiFiOnDemandHotspotNetworkProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Availability(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability: ...
    @winrt_mixinmethod
    def put_Availability(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability) -> Void: ...
    @winrt_mixinmethod
    def get_RemainingBatteryPercent(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_RemainingBatteryPercent(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_CellularBars(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> Windows.Foundation.IReference[Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]: ...
    @winrt_mixinmethod
    def put_CellularBars(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: Windows.Foundation.IReference[Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]) -> Void: ...
    @winrt_mixinmethod
    def get_IsMetered(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsMetered(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Ssid(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Ssid(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Password(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_Password(self: Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Availability = property(get_Availability, put_Availability)
    RemainingBatteryPercent = property(get_RemainingBatteryPercent, put_RemainingBatteryPercent)
    CellularBars = property(get_CellularBars, put_CellularBars)
    IsMetered = property(get_IsMetered, put_IsMetered)
    Ssid = property(get_Ssid, put_Ssid)
    Password = property(get_Password, put_Password)
WiFiPhyKind = Int32
WiFiPhyKind_Unknown: WiFiPhyKind = 0
WiFiPhyKind_Fhss: WiFiPhyKind = 1
WiFiPhyKind_Dsss: WiFiPhyKind = 2
WiFiPhyKind_IRBaseband: WiFiPhyKind = 3
WiFiPhyKind_Ofdm: WiFiPhyKind = 4
WiFiPhyKind_Hrdsss: WiFiPhyKind = 5
WiFiPhyKind_Erp: WiFiPhyKind = 6
WiFiPhyKind_HT: WiFiPhyKind = 7
WiFiPhyKind_Vht: WiFiPhyKind = 8
WiFiPhyKind_Dmg: WiFiPhyKind = 9
WiFiPhyKind_HE: WiFiPhyKind = 10
WiFiPhyKind_Eht: WiFiPhyKind = 11
WiFiReconnectionKind = Int32
WiFiReconnectionKind_Automatic: WiFiReconnectionKind = 0
WiFiReconnectionKind_Manual: WiFiReconnectionKind = 1
class WiFiWpsConfigurationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.WiFi.IWiFiWpsConfigurationResult
    _classid_ = 'Windows.Devices.WiFi.WiFiWpsConfigurationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.WiFi.IWiFiWpsConfigurationResult) -> Windows.Devices.WiFi.WiFiWpsConfigurationStatus: ...
    @winrt_mixinmethod
    def get_SupportedWpsKinds(self: Windows.Devices.WiFi.IWiFiWpsConfigurationResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFi.WiFiWpsKind]: ...
    Status = property(get_Status, None)
    SupportedWpsKinds = property(get_SupportedWpsKinds, None)
WiFiWpsConfigurationStatus = Int32
WiFiWpsConfigurationStatus_UnspecifiedFailure: WiFiWpsConfigurationStatus = 0
WiFiWpsConfigurationStatus_Success: WiFiWpsConfigurationStatus = 1
WiFiWpsConfigurationStatus_Timeout: WiFiWpsConfigurationStatus = 2
WiFiWpsKind = Int32
WiFiWpsKind_Unknown: WiFiWpsKind = 0
WiFiWpsKind_Pin: WiFiWpsKind = 1
WiFiWpsKind_PushButton: WiFiWpsKind = 2
WiFiWpsKind_Nfc: WiFiWpsKind = 3
WiFiWpsKind_Ethernet: WiFiWpsKind = 4
WiFiWpsKind_Usb: WiFiWpsKind = 5
make_head(_module, 'IWiFiAdapter')
make_head(_module, 'IWiFiAdapter2')
make_head(_module, 'IWiFiAdapterStatics')
make_head(_module, 'IWiFiAvailableNetwork')
make_head(_module, 'IWiFiConnectionResult')
make_head(_module, 'IWiFiNetworkReport')
make_head(_module, 'IWiFiOnDemandHotspotConnectTriggerDetails')
make_head(_module, 'IWiFiOnDemandHotspotConnectionResult')
make_head(_module, 'IWiFiOnDemandHotspotNetwork')
make_head(_module, 'IWiFiOnDemandHotspotNetworkProperties')
make_head(_module, 'IWiFiOnDemandHotspotNetworkStatics')
make_head(_module, 'IWiFiWpsConfigurationResult')
make_head(_module, 'WiFiAdapter')
make_head(_module, 'WiFiAvailableNetwork')
make_head(_module, 'WiFiConnectionResult')
make_head(_module, 'WiFiNetworkReport')
make_head(_module, 'WiFiOnDemandHotspotConnectTriggerDetails')
make_head(_module, 'WiFiOnDemandHotspotConnectionResult')
make_head(_module, 'WiFiOnDemandHotspotNetwork')
make_head(_module, 'WiFiOnDemandHotspotNetworkProperties')
make_head(_module, 'WiFiWpsConfigurationResult')
