from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.WiFi
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.Connectivity
import win32more.Windows.Security.Credentials
import win32more.Windows.Win32.System.WinRT
class IWiFiAdapter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAdapter'
    _iid_ = Guid('{a6c4e423-3d75-43a4-b9de-11e26b72d9b0}')
    @winrt_commethod(6)
    def get_NetworkAdapter(self) -> win32more.Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(7)
    def ScanAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_NetworkReport(self) -> win32more.Windows.Devices.WiFi.WiFiNetworkReport: ...
    @winrt_commethod(9)
    def add_AvailableNetworksChanged(self, args: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFi.WiFiAdapter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_AvailableNetworksChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def ConnectAsync(self, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_commethod(12)
    def ConnectWithPasswordCredentialAsync(self, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_commethod(13)
    def ConnectWithPasswordCredentialAndSsidAsync(self, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_commethod(14)
    def Disconnect(self) -> Void: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkReport = property(get_NetworkReport, None)
    AvailableNetworksChanged = event()
class IWiFiAdapter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAdapter2'
    _iid_ = Guid('{5bc4501d-81e4-453d-9430-1fcafbadd6b6}')
    @winrt_commethod(6)
    def GetWpsConfigurationAsync(self, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiWpsConfigurationResult]: ...
    @winrt_commethod(7)
    def ConnectWithPasswordCredentialAndSsidAndConnectionMethodAsync(self, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String, connectionMethod: win32more.Windows.Devices.WiFi.WiFiConnectionMethod) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
class IWiFiAdapterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAdapterStatics'
    _iid_ = Guid('{da25fddd-d24c-43e3-aabd-c4659f730f99}')
    @winrt_commethod(6)
    def FindAllAdaptersAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFi.WiFiAdapter]]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiAdapter]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiAccessStatus]: ...
class IWiFiAvailableNetwork(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiAvailableNetwork'
    _iid_ = Guid('{26e96246-183e-4704-9826-71b4a2f0f668}')
    @winrt_commethod(6)
    def get_Uptime(self) -> win32more.Windows.Foundation.TimeSpan: ...
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
    def get_NetworkKind(self) -> win32more.Windows.Devices.WiFi.WiFiNetworkKind: ...
    @winrt_commethod(13)
    def get_PhyKind(self) -> win32more.Windows.Devices.WiFi.WiFiPhyKind: ...
    @winrt_commethod(14)
    def get_SecuritySettings(self) -> win32more.Windows.Networking.Connectivity.NetworkSecuritySettings: ...
    @winrt_commethod(15)
    def get_BeaconInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(16)
    def get_IsWiFiDirect(self) -> Boolean: ...
    BeaconInterval = property(get_BeaconInterval, None)
    Bssid = property(get_Bssid, None)
    ChannelCenterFrequencyInKilohertz = property(get_ChannelCenterFrequencyInKilohertz, None)
    IsWiFiDirect = property(get_IsWiFiDirect, None)
    NetworkKind = property(get_NetworkKind, None)
    NetworkRssiInDecibelMilliwatts = property(get_NetworkRssiInDecibelMilliwatts, None)
    PhyKind = property(get_PhyKind, None)
    SecuritySettings = property(get_SecuritySettings, None)
    SignalBars = property(get_SignalBars, None)
    Ssid = property(get_Ssid, None)
    Uptime = property(get_Uptime, None)
class IWiFiConnectionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiConnectionResult'
    _iid_ = Guid('{143bdfd9-c37d-40be-a5c8-857bce85a931}')
    @winrt_commethod(6)
    def get_ConnectionStatus(self) -> win32more.Windows.Devices.WiFi.WiFiConnectionStatus: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
class IWiFiNetworkReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiNetworkReport'
    _iid_ = Guid('{9524ded2-5911-445e-8194-be4f1a704895}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AvailableNetworks(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFi.WiFiAvailableNetwork]: ...
    AvailableNetworks = property(get_AvailableNetworks, None)
    Timestamp = property(get_Timestamp, None)
class IWiFiOnDemandHotspotConnectTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails'
    _iid_ = Guid('{a268eb58-68f5-59cf-8d38-35bf44b097ef}')
    @winrt_commethod(6)
    def get_RequestedNetwork(self) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
    @winrt_commethod(7)
    def ReportError(self, status: win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus) -> Void: ...
    @winrt_commethod(8)
    def ConnectAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult]: ...
    @winrt_commethod(9)
    def Connect(self) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult: ...
    RequestedNetwork = property(get_RequestedNetwork, None)
class IWiFiOnDemandHotspotConnectionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectionResult'
    _iid_ = Guid('{911794a1-6c82-5de3-8a4a-f9ff22a4957a}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus: ...
    Status = property(get_Status, None)
class IWiFiOnDemandHotspotNetwork(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork'
    _iid_ = Guid('{18dc7115-a04e-507c-bbaf-b78369d29fa7}')
    @winrt_commethod(6)
    def GetProperties(self) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties: ...
    @winrt_commethod(7)
    def UpdateProperties(self, newProperties: win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties) -> Void: ...
    @winrt_commethod(8)
    def get_Id(self) -> Guid: ...
    Id = property(get_Id, None)
class IWiFiOnDemandHotspotNetworkProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties'
    _iid_ = Guid('{c810a1f2-c81d-5852-be50-e4bd4d81e98d}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Availability(self) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability: ...
    @winrt_commethod(9)
    def put_Availability(self, value: win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability) -> Void: ...
    @winrt_commethod(10)
    def get_RemainingBatteryPercent(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(11)
    def put_RemainingBatteryPercent(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(12)
    def get_CellularBars(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]: ...
    @winrt_commethod(13)
    def put_CellularBars(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]) -> Void: ...
    @winrt_commethod(14)
    def get_IsMetered(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsMetered(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Ssid(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_Ssid(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_Password(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(19)
    def put_Password(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    Availability = property(get_Availability, put_Availability)
    CellularBars = property(get_CellularBars, put_CellularBars)
    DisplayName = property(get_DisplayName, put_DisplayName)
    IsMetered = property(get_IsMetered, put_IsMetered)
    Password = property(get_Password, put_Password)
    RemainingBatteryPercent = property(get_RemainingBatteryPercent, put_RemainingBatteryPercent)
    Ssid = property(get_Ssid, put_Ssid)
class IWiFiOnDemandHotspotNetworkStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkStatics'
    _iid_ = Guid('{00f5b8ac-80e7-5054-871c-8739f374e3c9}')
    @winrt_commethod(6)
    def GetOrCreateById(self, networkId: Guid) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
class IWiFiWpsConfigurationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFi.IWiFiWpsConfigurationResult'
    _iid_ = Guid('{67b49871-17ee-42d1-b14f-5a11f1226fb5}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.WiFi.WiFiWpsConfigurationStatus: ...
    @winrt_commethod(7)
    def get_SupportedWpsKinds(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFi.WiFiWpsKind]: ...
    Status = property(get_Status, None)
    SupportedWpsKinds = property(get_SupportedWpsKinds, None)
class WiFiAccessStatus(Enum, Int32):
    Unspecified = 0
    Allowed = 1
    DeniedByUser = 2
    DeniedBySystem = 3
class WiFiAdapter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiAdapter
    _classid_ = 'Windows.Devices.WiFi.WiFiAdapter'
    @winrt_mixinmethod
    def get_NetworkAdapter(self: win32more.Windows.Devices.WiFi.IWiFiAdapter) -> win32more.Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def ScanAsync(self: win32more.Windows.Devices.WiFi.IWiFiAdapter) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_NetworkReport(self: win32more.Windows.Devices.WiFi.IWiFiAdapter) -> win32more.Windows.Devices.WiFi.WiFiNetworkReport: ...
    @winrt_mixinmethod
    def add_AvailableNetworksChanged(self: win32more.Windows.Devices.WiFi.IWiFiAdapter, args: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFi.WiFiAdapter, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableNetworksChanged(self: win32more.Windows.Devices.WiFi.IWiFiAdapter, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Devices.WiFi.IWiFiAdapter, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_mixinmethod
    def ConnectWithPasswordCredentialAsync(self: win32more.Windows.Devices.WiFi.IWiFiAdapter, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_mixinmethod
    def ConnectWithPasswordCredentialAndSsidAsync(self: win32more.Windows.Devices.WiFi.IWiFiAdapter, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_mixinmethod
    def Disconnect(self: win32more.Windows.Devices.WiFi.IWiFiAdapter) -> Void: ...
    @winrt_mixinmethod
    def GetWpsConfigurationAsync(self: win32more.Windows.Devices.WiFi.IWiFiAdapter2, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiWpsConfigurationResult]: ...
    @winrt_mixinmethod
    def ConnectWithPasswordCredentialAndSsidAndConnectionMethodAsync(self: win32more.Windows.Devices.WiFi.IWiFiAdapter2, availableNetwork: win32more.Windows.Devices.WiFi.WiFiAvailableNetwork, reconnectionKind: win32more.Windows.Devices.WiFi.WiFiReconnectionKind, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential, ssid: WinRT_String, connectionMethod: win32more.Windows.Devices.WiFi.WiFiConnectionMethod) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiConnectionResult]: ...
    @winrt_classmethod
    def FindAllAdaptersAsync(cls: win32more.Windows.Devices.WiFi.IWiFiAdapterStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFi.WiFiAdapter]]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.WiFi.IWiFiAdapterStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.WiFi.IWiFiAdapterStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiAdapter]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.WiFi.IWiFiAdapterStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiAccessStatus]: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkReport = property(get_NetworkReport, None)
    AvailableNetworksChanged = event()
class WiFiAvailableNetwork(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork
    _classid_ = 'Windows.Devices.WiFi.WiFiAvailableNetwork'
    @winrt_mixinmethod
    def get_Uptime(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Ssid(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Bssid(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ChannelCenterFrequencyInKilohertz(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Int32: ...
    @winrt_mixinmethod
    def get_NetworkRssiInDecibelMilliwatts(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Double: ...
    @winrt_mixinmethod
    def get_SignalBars(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Byte: ...
    @winrt_mixinmethod
    def get_NetworkKind(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> win32more.Windows.Devices.WiFi.WiFiNetworkKind: ...
    @winrt_mixinmethod
    def get_PhyKind(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> win32more.Windows.Devices.WiFi.WiFiPhyKind: ...
    @winrt_mixinmethod
    def get_SecuritySettings(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> win32more.Windows.Networking.Connectivity.NetworkSecuritySettings: ...
    @winrt_mixinmethod
    def get_BeaconInterval(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IsWiFiDirect(self: win32more.Windows.Devices.WiFi.IWiFiAvailableNetwork) -> Boolean: ...
    BeaconInterval = property(get_BeaconInterval, None)
    Bssid = property(get_Bssid, None)
    ChannelCenterFrequencyInKilohertz = property(get_ChannelCenterFrequencyInKilohertz, None)
    IsWiFiDirect = property(get_IsWiFiDirect, None)
    NetworkKind = property(get_NetworkKind, None)
    NetworkRssiInDecibelMilliwatts = property(get_NetworkRssiInDecibelMilliwatts, None)
    PhyKind = property(get_PhyKind, None)
    SecuritySettings = property(get_SecuritySettings, None)
    SignalBars = property(get_SignalBars, None)
    Ssid = property(get_Ssid, None)
    Uptime = property(get_Uptime, None)
class WiFiConnectionMethod(Enum, Int32):
    Default = 0
    WpsPin = 1
    WpsPushButton = 2
class WiFiConnectionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiConnectionResult
    _classid_ = 'Windows.Devices.WiFi.WiFiConnectionResult'
    @winrt_mixinmethod
    def get_ConnectionStatus(self: win32more.Windows.Devices.WiFi.IWiFiConnectionResult) -> win32more.Windows.Devices.WiFi.WiFiConnectionStatus: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
class WiFiConnectionStatus(Enum, Int32):
    UnspecifiedFailure = 0
    Success = 1
    AccessRevoked = 2
    InvalidCredential = 3
    NetworkNotAvailable = 4
    Timeout = 5
    UnsupportedAuthenticationProtocol = 6
class WiFiNetworkKind(Enum, Int32):
    Any = 0
    Infrastructure = 1
    Adhoc = 2
class WiFiNetworkReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiNetworkReport
    _classid_ = 'Windows.Devices.WiFi.WiFiNetworkReport'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.WiFi.IWiFiNetworkReport) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AvailableNetworks(self: win32more.Windows.Devices.WiFi.IWiFiNetworkReport) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFi.WiFiAvailableNetwork]: ...
    AvailableNetworks = property(get_AvailableNetworks, None)
    Timestamp = property(get_Timestamp, None)
class WiFiOnDemandHotspotAvailability(Enum, Int32):
    Available = 0
    Unavailable = 1
class WiFiOnDemandHotspotCellularBars(Enum, Int32):
    ZeroBars = 0
    OneBar = 1
    TwoBars = 2
    ThreeBars = 3
    FourBars = 4
    FiveBars = 5
class WiFiOnDemandHotspotConnectStatus(Enum, Int32):
    UnspecifiedFailure = 0
    Success = 1
    AppTimedOut = 2
    InvalidCredential = 3
    NetworkNotAvailable = 4
    UnsupportedAuthenticationProtocol = 5
    BluetoothConnectFailed = 6
    BluetoothTransmissionError = 7
    OperationCanceledByUser = 8
    EntitlementCheckFailed = 9
    NoCellularSignal = 10
    CellularDataTurnedOff = 11
    WlanConnectFailed = 12
    WlanNotVisible = 13
    AccessPointCannotConnect = 14
    CellularConnectTimedOut = 15
    RoamingNotAllowed = 16
    PairingRequired = 17
    DataLimitReached = 18
class WiFiOnDemandHotspotConnectTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotConnectTriggerDetails'
    @winrt_mixinmethod
    def get_RequestedNetwork(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails, status: win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus) -> Void: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult]: ...
    @winrt_mixinmethod
    def Connect(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectTriggerDetails) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult: ...
    RequestedNetwork = property(get_RequestedNetwork, None)
class WiFiOnDemandHotspotConnectionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectionResult
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotConnectionResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotConnectionResult) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus: ...
    Status = property(get_Status, None)
class WiFiOnDemandHotspotNetwork(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork'
    @winrt_mixinmethod
    def GetProperties(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties: ...
    @winrt_mixinmethod
    def UpdateProperties(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork, newProperties: win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetwork) -> Guid: ...
    @winrt_classmethod
    def GetOrCreateById(cls: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkStatics, networkId: Guid) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotNetwork: ...
    Id = property(get_Id, None)
class WiFiOnDemandHotspotNetworkProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties
    _classid_ = 'Windows.Devices.WiFi.WiFiOnDemandHotspotNetworkProperties'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Availability(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability: ...
    @winrt_mixinmethod
    def put_Availability(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability) -> Void: ...
    @winrt_mixinmethod
    def get_RemainingBatteryPercent(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_RemainingBatteryPercent(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_CellularBars(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> win32more.Windows.Foundation.IReference[win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]: ...
    @winrt_mixinmethod
    def put_CellularBars(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: win32more.Windows.Foundation.IReference[win32more.Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]) -> Void: ...
    @winrt_mixinmethod
    def get_IsMetered(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsMetered(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Ssid(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Ssid(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Password(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_Password(self: win32more.Windows.Devices.WiFi.IWiFiOnDemandHotspotNetworkProperties, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    Availability = property(get_Availability, put_Availability)
    CellularBars = property(get_CellularBars, put_CellularBars)
    DisplayName = property(get_DisplayName, put_DisplayName)
    IsMetered = property(get_IsMetered, put_IsMetered)
    Password = property(get_Password, put_Password)
    RemainingBatteryPercent = property(get_RemainingBatteryPercent, put_RemainingBatteryPercent)
    Ssid = property(get_Ssid, put_Ssid)
class WiFiPhyKind(Enum, Int32):
    Unknown = 0
    Fhss = 1
    Dsss = 2
    IRBaseband = 3
    Ofdm = 4
    Hrdsss = 5
    Erp = 6
    HT = 7
    Vht = 8
    Dmg = 9
    HE = 10
    Eht = 11
class WiFiReconnectionKind(Enum, Int32):
    Automatic = 0
    Manual = 1
class WiFiWpsConfigurationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFi.IWiFiWpsConfigurationResult
    _classid_ = 'Windows.Devices.WiFi.WiFiWpsConfigurationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.WiFi.IWiFiWpsConfigurationResult) -> win32more.Windows.Devices.WiFi.WiFiWpsConfigurationStatus: ...
    @winrt_mixinmethod
    def get_SupportedWpsKinds(self: win32more.Windows.Devices.WiFi.IWiFiWpsConfigurationResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFi.WiFiWpsKind]: ...
    Status = property(get_Status, None)
    SupportedWpsKinds = property(get_SupportedWpsKinds, None)
class WiFiWpsConfigurationStatus(Enum, Int32):
    UnspecifiedFailure = 0
    Success = 1
    Timeout = 2
class WiFiWpsKind(Enum, Int32):
    Unknown = 0
    Pin = 1
    PushButton = 2
    Nfc = 3
    Ethernet = 4
    Usb = 5


make_ready(__name__)
