from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.NetworkListManager
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Ole
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    def get__NewEnum(self, ppEnumVar: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetworkConnection_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, ppEnumNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNetworks(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dcb00003-570f-4a9b-8d69-199fdba5723b}')
    @commethod(7)
    def get__NewEnum(self, ppEnumVar: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetwork_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, ppEnumNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworks_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetNetworkConnections(self, ppEnumNetworkConnection: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetNetwork(self, ppNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetwork_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetDataPlanStatus(self, pDataPlanStatus: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetCost(self, pCost: POINTER(UInt32), pDestIPAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(self, pDataPlanStatus: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head), pDestIPAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDestinationAddresses(self, length: UInt32, pDestIPAddrList: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head), bAppend: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkCostManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb00009-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def CostChanged(self, newCost: UInt32, pDestAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DataPlanStatusChanged(self, pDestAddr: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetNetworks(self, Flags: win32more.Windows.Win32.Networking.NetworkListManager.NLM_ENUM_NETWORK, ppEnumNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworks_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetwork(self, gdNetworkId: Guid, ppNetwork: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetwork_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNetworkConnections(self, ppEnum: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetNetworkConnection(self, gdNetworkConnectionId: Guid, ppNetworkConnection: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.INetworkConnection_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsConnectedToInternet(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsConnected(self, pbIsConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConnectivity(self, pConnectivity: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSimulatedProfileInfo(self, pSimulatedInfo: POINTER(win32more.Windows.Win32.Networking.NetworkListManager.NLM_SIMULATED_PROFILE_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearSimulatedProfileInfo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkListManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb00001-570f-4a9b-8d69-199fdba5723b}')
    @commethod(3)
    def ConnectivityChanged(self, newConnectivity: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
NLM_CONNECTION_COST = Int32
NLM_CONNECTION_COST_UNKNOWN: NLM_CONNECTION_COST = 0
NLM_CONNECTION_COST_UNRESTRICTED: NLM_CONNECTION_COST = 1
NLM_CONNECTION_COST_FIXED: NLM_CONNECTION_COST = 2
NLM_CONNECTION_COST_VARIABLE: NLM_CONNECTION_COST = 4
NLM_CONNECTION_COST_OVERDATALIMIT: NLM_CONNECTION_COST = 65536
NLM_CONNECTION_COST_CONGESTED: NLM_CONNECTION_COST = 131072
NLM_CONNECTION_COST_ROAMING: NLM_CONNECTION_COST = 262144
NLM_CONNECTION_COST_APPROACHINGDATALIMIT: NLM_CONNECTION_COST = 524288
NLM_CONNECTION_PROPERTY_CHANGE = Int32
NLM_CONNECTION_PROPERTY_CHANGE_AUTHENTICATION: NLM_CONNECTION_PROPERTY_CHANGE = 1
NLM_CONNECTIVITY = Int32
NLM_CONNECTIVITY_DISCONNECTED: NLM_CONNECTIVITY = 0
NLM_CONNECTIVITY_IPV4_NOTRAFFIC: NLM_CONNECTIVITY = 1
NLM_CONNECTIVITY_IPV6_NOTRAFFIC: NLM_CONNECTIVITY = 2
NLM_CONNECTIVITY_IPV4_SUBNET: NLM_CONNECTIVITY = 16
NLM_CONNECTIVITY_IPV4_LOCALNETWORK: NLM_CONNECTIVITY = 32
NLM_CONNECTIVITY_IPV4_INTERNET: NLM_CONNECTIVITY = 64
NLM_CONNECTIVITY_IPV6_SUBNET: NLM_CONNECTIVITY = 256
NLM_CONNECTIVITY_IPV6_LOCALNETWORK: NLM_CONNECTIVITY = 512
NLM_CONNECTIVITY_IPV6_INTERNET: NLM_CONNECTIVITY = 1024
class NLM_DATAPLAN_STATUS(EasyCastStructure):
    InterfaceGuid: Guid
    UsageData: win32more.Windows.Win32.Networking.NetworkListManager.NLM_USAGE_DATA
    DataLimitInMegabytes: UInt32
    InboundBandwidthInKbps: UInt32
    OutboundBandwidthInKbps: UInt32
    NextBillingCycle: win32more.Windows.Win32.Foundation.FILETIME
    MaxTransferSizeInMegabytes: UInt32
    Reserved: UInt32
NLM_DOMAIN_AUTHENTICATION_KIND = Int32
NLM_DOMAIN_AUTHENTICATION_KIND_NONE: NLM_DOMAIN_AUTHENTICATION_KIND = 0
NLM_DOMAIN_AUTHENTICATION_KIND_LDAP: NLM_DOMAIN_AUTHENTICATION_KIND = 1
NLM_DOMAIN_AUTHENTICATION_KIND_TLS: NLM_DOMAIN_AUTHENTICATION_KIND = 2
NLM_DOMAIN_TYPE = Int32
NLM_DOMAIN_TYPE_NON_DOMAIN_NETWORK: NLM_DOMAIN_TYPE = 0
NLM_DOMAIN_TYPE_DOMAIN_NETWORK: NLM_DOMAIN_TYPE = 1
NLM_DOMAIN_TYPE_DOMAIN_AUTHENTICATED: NLM_DOMAIN_TYPE = 2
NLM_ENUM_NETWORK = Int32
NLM_ENUM_NETWORK_CONNECTED: NLM_ENUM_NETWORK = 1
NLM_ENUM_NETWORK_DISCONNECTED: NLM_ENUM_NETWORK = 2
NLM_ENUM_NETWORK_ALL: NLM_ENUM_NETWORK = 3
NLM_INTERNET_CONNECTIVITY = Int32
NLM_INTERNET_CONNECTIVITY_WEBHIJACK: NLM_INTERNET_CONNECTIVITY = 1
NLM_INTERNET_CONNECTIVITY_PROXIED: NLM_INTERNET_CONNECTIVITY = 2
NLM_INTERNET_CONNECTIVITY_CORPORATE: NLM_INTERNET_CONNECTIVITY = 4
NLM_NETWORK_CATEGORY = Int32
NLM_NETWORK_CATEGORY_PUBLIC: NLM_NETWORK_CATEGORY = 0
NLM_NETWORK_CATEGORY_PRIVATE: NLM_NETWORK_CATEGORY = 1
NLM_NETWORK_CATEGORY_DOMAIN_AUTHENTICATED: NLM_NETWORK_CATEGORY = 2
NLM_NETWORK_CLASS = Int32
NLM_NETWORK_IDENTIFYING: NLM_NETWORK_CLASS = 1
NLM_NETWORK_IDENTIFIED: NLM_NETWORK_CLASS = 2
NLM_NETWORK_UNIDENTIFIED: NLM_NETWORK_CLASS = 3
NLM_NETWORK_PROPERTY_CHANGE = Int32
NLM_NETWORK_PROPERTY_CHANGE_CONNECTION: NLM_NETWORK_PROPERTY_CHANGE = 1
NLM_NETWORK_PROPERTY_CHANGE_DESCRIPTION: NLM_NETWORK_PROPERTY_CHANGE = 2
NLM_NETWORK_PROPERTY_CHANGE_NAME: NLM_NETWORK_PROPERTY_CHANGE = 4
NLM_NETWORK_PROPERTY_CHANGE_ICON: NLM_NETWORK_PROPERTY_CHANGE = 8
NLM_NETWORK_PROPERTY_CHANGE_CATEGORY_VALUE: NLM_NETWORK_PROPERTY_CHANGE = 16
class NLM_SIMULATED_PROFILE_INFO(EasyCastStructure):
    ProfileName: Char * 256
    cost: win32more.Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST
    UsageInMegabytes: UInt32
    DataLimitInMegabytes: UInt32
class NLM_SOCKADDR(EasyCastStructure):
    data: Byte * 128
class NLM_USAGE_DATA(EasyCastStructure):
    UsageInMegabytes: UInt32
    LastSyncTime: win32more.Windows.Win32.Foundation.FILETIME
NetworkListManager = Guid('{dcb00c01-570f-4a9b-8d69-199fdba5723b}')
make_head(_module, 'IEnumNetworkConnections')
make_head(_module, 'IEnumNetworks')
make_head(_module, 'INetwork')
make_head(_module, 'INetwork2')
make_head(_module, 'INetworkConnection')
make_head(_module, 'INetworkConnection2')
make_head(_module, 'INetworkConnectionCost')
make_head(_module, 'INetworkConnectionCostEvents')
make_head(_module, 'INetworkConnectionEvents')
make_head(_module, 'INetworkCostManager')
make_head(_module, 'INetworkCostManagerEvents')
make_head(_module, 'INetworkEvents')
make_head(_module, 'INetworkListManager')
make_head(_module, 'INetworkListManagerEvents')
make_head(_module, 'NLM_DATAPLAN_STATUS')
make_head(_module, 'NLM_SIMULATED_PROFILE_INFO')
make_head(_module, 'NLM_SOCKADDR')
make_head(_module, 'NLM_USAGE_DATA')