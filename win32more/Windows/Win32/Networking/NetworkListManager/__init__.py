from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.NetworkListManager
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Ole
NA_DomainAuthenticationFailed: String = 'NA_DomainAuthenticationFailed'
NA_NetworkClass: String = 'NA_NetworkClass'
NA_NameSetByPolicy: String = 'NA_NameSetByPolicy'
NA_IconSetByPolicy: String = 'NA_IconSetByPolicy'
NA_DescriptionSetByPolicy: String = 'NA_DescriptionSetByPolicy'
NA_CategorySetByPolicy: String = 'NA_CategorySetByPolicy'
NA_NameReadOnly: String = 'NA_NameReadOnly'
NA_IconReadOnly: String = 'NA_IconReadOnly'
NA_DescriptionReadOnly: String = 'NA_DescriptionReadOnly'
NA_CategoryReadOnly: String = 'NA_CategoryReadOnly'
NA_AllowMerge: String = 'NA_AllowMerge'
NA_InternetConnectivityV4: String = 'NA_InternetConnectivityV4'
NA_InternetConnectivityV6: String = 'NA_InternetConnectivityV6'
NLM_MAX_ADDRESS_LIST_SIZE: UInt32 = 10
NLM_UNKNOWN_DATAPLAN_STATUS: UInt32 = 4294967295
class IEnumNetworkConnections(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcb00006-570f-4a9b-8d69-199fdba5723b}')
    @commethod(7)
    def get__NewEnum(self, ppEnumVar: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetworkConnection), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, ppEnumNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetworks(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcb00003-570f-4a9b-8d69-199fdba5723b}')
    @commethod(7)
    def get__NewEnum(self, ppEnumVar: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetwork), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, ppEnumNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworks)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetwork(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcb00002-570f-4a9b-8d69-199fdba5723b}')
    @commethod(7)
    def GetName(self, pszNetworkName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetName(self, szNetworkNewName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDescription(self, pszDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDescription(self, szDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkId(self, pgdGuidNetworkId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDomainType(self, pNetworkType: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNetworkConnections(self, ppEnumNetworkConnection: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimeCreatedAndConnected(self, pdwLowDateTimeCreated: POINTER(UInt32), pdwHighDateTimeCreated: POINTER(UInt32), pdwLowDateTimeConnected: POINTER(UInt32), pdwHighDateTimeConnected: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsConnectedToInternet(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsConnected(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetConnectivity(self, pConnectivity: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCategory(self, pCategory: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetCategory(self, NewCategory: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetwork2(ComPtr):
    extends: win32more.Windows.Win32.Networking.NetworkListManager.INetwork
    _iid_ = Guid('{b5550abb-3391-4310-804f-25dcc325ed81}')
    @commethod(20)
    def IsDomainAuthenticatedBy(self, domainAuthenticationKind: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_AUTHENTICATION_KIND, pValue: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcb00005-570f-4a9b-8d69-199fdba5723b}')
    @commethod(7)
    def GetNetwork(self, ppNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetwork)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsConnectedToInternet(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IsConnected(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnectivity(self, pConnectivity: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetConnectionId(self, pgdConnectionId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAdapterId(self, pgdAdapterId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDomainType(self, pDomainType: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkConnection2(ComPtr):
    extends: win32more.Windows.Win32.Networking.NetworkListManager.INetworkConnection
    _iid_ = Guid('{00e676ed-5a35-4738-92eb-8581738d0f0a}')
    @commethod(14)
    def IsDomainAuthenticatedBy(self, domainAuthenticationKind: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_AUTHENTICATION_KIND, pValue: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionCost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb0000a-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def GetCost(self, pCost: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(self, pDataPlanStatus: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionCostEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb0000b-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def ConnectionCostChanged(self, connectionId: Guid, newCost: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConnectionDataPlanStatusChanged(self, connectionId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb00007-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def NetworkConnectionConnectivityChanged(self, connectionId: Guid, newConnectivity: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkConnectionPropertyChanged(self, connectionId: Guid, flags: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_PROPERTY_CHANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkCostManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb00008-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def GetCost(self, pCost: POINTER(UInt32), pDestIPAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(self, pDataPlanStatus: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS), pDestIPAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDestinationAddresses(self, length: UInt32, pDestIPAddrList: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR), bAppend: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkCostManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb00009-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def CostChanged(self, newCost: UInt32, pDestAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DataPlanStatusChanged(self, pDestAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb00004-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def NetworkAdded(self, networkId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkDeleted(self, networkId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NetworkConnectivityChanged(self, networkId: Guid, newConnectivity: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NetworkPropertyChanged(self, networkId: Guid, flags: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkListManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcb00000-570f-4a9b-8d69-199fdba5723b}')
    @commethod(7)
    def GetNetworks(self, Flags: win32more.Windows.Win32.Networking.NetworkListManager.NLM_ENUM_NETWORK, ppEnumNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworks)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetwork(self, gdNetworkId: Guid, ppNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetwork)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNetworkConnections(self, ppEnum: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetNetworkConnection(self, gdNetworkConnectionId: Guid, ppNetworkConnection: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetworkConnection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsConnectedToInternet(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsConnected(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConnectivity(self, pConnectivity: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSimulatedProfileInfo(self, pSimulatedInfo: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SIMULATED_PROFILE_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearSimulatedProfileInfo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkListManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb00001-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def ConnectivityChanged(self, newConnectivity: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
NLM_CONNECTION_COST = Int32
NLM_CONNECTION_COST_UNKNOWN: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 0
NLM_CONNECTION_COST_UNRESTRICTED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 1
NLM_CONNECTION_COST_FIXED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 2
NLM_CONNECTION_COST_VARIABLE: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 4
NLM_CONNECTION_COST_OVERDATALIMIT: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 65536
NLM_CONNECTION_COST_CONGESTED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 131072
NLM_CONNECTION_COST_ROAMING: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 262144
NLM_CONNECTION_COST_APPROACHINGDATALIMIT: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST = 524288
NLM_CONNECTION_PROPERTY_CHANGE = Int32
NLM_CONNECTION_PROPERTY_CHANGE_AUTHENTICATION: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_PROPERTY_CHANGE = 1
NLM_CONNECTIVITY = Int32
NLM_CONNECTIVITY_DISCONNECTED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 0
NLM_CONNECTIVITY_IPV4_NOTRAFFIC: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 1
NLM_CONNECTIVITY_IPV6_NOTRAFFIC: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 2
NLM_CONNECTIVITY_IPV4_SUBNET: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 16
NLM_CONNECTIVITY_IPV4_LOCALNETWORK: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 32
NLM_CONNECTIVITY_IPV4_INTERNET: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 64
NLM_CONNECTIVITY_IPV6_SUBNET: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 256
NLM_CONNECTIVITY_IPV6_LOCALNETWORK: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 512
NLM_CONNECTIVITY_IPV6_INTERNET: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY = 1024
class NLM_DATAPLAN_STATUS(Structure):
    InterfaceGuid: Guid
    UsageData: win32more.Windows.Win32.Networking.NetworkListManager.NLM_USAGE_DATA
    DataLimitInMegabytes: UInt32
    InboundBandwidthInKbps: UInt32
    OutboundBandwidthInKbps: UInt32
    NextBillingCycle: win32more.Windows.Win32.Foundation.FILETIME
    MaxTransferSizeInMegabytes: UInt32
    Reserved: UInt32
NLM_DOMAIN_AUTHENTICATION_KIND = Int32
NLM_DOMAIN_AUTHENTICATION_KIND_NONE: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_AUTHENTICATION_KIND = 0
NLM_DOMAIN_AUTHENTICATION_KIND_LDAP: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_AUTHENTICATION_KIND = 1
NLM_DOMAIN_AUTHENTICATION_KIND_TLS: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_AUTHENTICATION_KIND = 2
NLM_DOMAIN_TYPE = Int32
NLM_DOMAIN_TYPE_NON_DOMAIN_NETWORK: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE = 0
NLM_DOMAIN_TYPE_DOMAIN_NETWORK: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE = 1
NLM_DOMAIN_TYPE_DOMAIN_AUTHENTICATED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE = 2
NLM_ENUM_NETWORK = Int32
NLM_ENUM_NETWORK_CONNECTED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_ENUM_NETWORK = 1
NLM_ENUM_NETWORK_DISCONNECTED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_ENUM_NETWORK = 2
NLM_ENUM_NETWORK_ALL: win32more.Windows.Win32.Networking.NetworkListManager.NLM_ENUM_NETWORK = 3
NLM_INTERNET_CONNECTIVITY = Int32
NLM_INTERNET_CONNECTIVITY_WEBHIJACK: win32more.Windows.Win32.Networking.NetworkListManager.NLM_INTERNET_CONNECTIVITY = 1
NLM_INTERNET_CONNECTIVITY_PROXIED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_INTERNET_CONNECTIVITY = 2
NLM_INTERNET_CONNECTIVITY_CORPORATE: win32more.Windows.Win32.Networking.NetworkListManager.NLM_INTERNET_CONNECTIVITY = 4
NLM_NETWORK_CATEGORY = Int32
NLM_NETWORK_CATEGORY_PUBLIC: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY = 0
NLM_NETWORK_CATEGORY_PRIVATE: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY = 1
NLM_NETWORK_CATEGORY_DOMAIN_AUTHENTICATED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY = 2
NLM_NETWORK_CLASS = Int32
NLM_NETWORK_IDENTIFYING: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CLASS = 1
NLM_NETWORK_IDENTIFIED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CLASS = 2
NLM_NETWORK_UNIDENTIFIED: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CLASS = 3
NLM_NETWORK_PROPERTY_CHANGE = Int32
NLM_NETWORK_PROPERTY_CHANGE_CONNECTION: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE = 1
NLM_NETWORK_PROPERTY_CHANGE_DESCRIPTION: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE = 2
NLM_NETWORK_PROPERTY_CHANGE_NAME: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE = 4
NLM_NETWORK_PROPERTY_CHANGE_ICON: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE = 8
NLM_NETWORK_PROPERTY_CHANGE_CATEGORY_VALUE: win32more.Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE = 16
class NLM_SIMULATED_PROFILE_INFO(Structure):
    ProfileName: Char * 256
    cost: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST
    UsageInMegabytes: UInt32
    DataLimitInMegabytes: UInt32
class NLM_SOCKADDR(Structure):
    data: Byte * 128
class NLM_USAGE_DATA(Structure):
    UsageInMegabytes: UInt32
    LastSyncTime: win32more.Windows.Win32.Foundation.FILETIME
NetworkListManager = Guid('{dcb00c01-570f-4a9b-8d69-199fdba5723b}')


make_ready(__name__)
