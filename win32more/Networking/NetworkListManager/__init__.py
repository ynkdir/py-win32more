from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Networking.NetworkListManager
import win32more.System.Com
import win32more.System.Ole
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
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
class IEnumNetworkConnections(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('dcb00006-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def get__NewEnum(ppEnumVar: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Networking.NetworkListManager.INetworkConnection_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(ppEnumNetwork: POINTER(win32more.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> win32more.Foundation.HRESULT: ...
class IEnumNetworks(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('dcb00003-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def get__NewEnum(ppEnumVar: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Networking.NetworkListManager.INetwork_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(ppEnumNetwork: POINTER(win32more.Networking.NetworkListManager.IEnumNetworks_head)) -> win32more.Foundation.HRESULT: ...
class INetwork(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('dcb00002-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetName(pszNetworkName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetName(szNetworkNewName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDescription(pszDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetDescription(szDescription: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkId(pgdGuidNetworkId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetDomainType(pNetworkType: POINTER(win32more.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetNetworkConnections(ppEnumNetworkConnection: POINTER(win32more.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimeCreatedAndConnected(pdwLowDateTimeCreated: POINTER(UInt32), pdwHighDateTimeCreated: POINTER(UInt32), pdwLowDateTimeConnected: POINTER(UInt32), pdwHighDateTimeConnected: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsConnectedToInternet(pbIsConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsConnected(pbIsConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetConnectivity(pConnectivity: POINTER(win32more.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetCategory(pCategory: POINTER(win32more.Networking.NetworkListManager.NLM_NETWORK_CATEGORY)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetCategory(NewCategory: win32more.Networking.NetworkListManager.NLM_NETWORK_CATEGORY) -> win32more.Foundation.HRESULT: ...
class INetworkConnection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('dcb00005-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetNetwork(ppNetwork: POINTER(win32more.Networking.NetworkListManager.INetwork_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsConnectedToInternet(pbIsConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_IsConnected(pbIsConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnectivity(pConnectivity: POINTER(win32more.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetConnectionId(pgdConnectionId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetAdapterId(pgdAdapterId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDomainType(pDomainType: POINTER(win32more.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> win32more.Foundation.HRESULT: ...
class INetworkConnectionCost(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcb0000a-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def GetCost(pCost: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(pDataPlanStatus: POINTER(win32more.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head)) -> win32more.Foundation.HRESULT: ...
class INetworkConnectionCostEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcb0000b-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def ConnectionCostChanged(connectionId: Guid, newCost: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ConnectionDataPlanStatusChanged(connectionId: Guid) -> win32more.Foundation.HRESULT: ...
class INetworkConnectionEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcb00007-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def NetworkConnectionConnectivityChanged(connectionId: Guid, newConnectivity: win32more.Networking.NetworkListManager.NLM_CONNECTIVITY) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkConnectionPropertyChanged(connectionId: Guid, flags: win32more.Networking.NetworkListManager.NLM_CONNECTION_PROPERTY_CHANGE) -> win32more.Foundation.HRESULT: ...
class INetworkCostManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcb00008-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def GetCost(pCost: POINTER(UInt32), pDestIPAddr: POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(pDataPlanStatus: POINTER(win32more.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head), pDestIPAddr: POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetDestinationAddresses(length: UInt32, pDestIPAddrList: POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head), bAppend: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class INetworkCostManagerEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcb00009-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def CostChanged(newCost: UInt32, pDestAddr: POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DataPlanStatusChanged(pDestAddr: POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> win32more.Foundation.HRESULT: ...
class INetworkEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcb00004-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def NetworkAdded(networkId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkDeleted(networkId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def NetworkConnectivityChanged(networkId: Guid, newConnectivity: win32more.Networking.NetworkListManager.NLM_CONNECTIVITY) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def NetworkPropertyChanged(networkId: Guid, flags: win32more.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE) -> win32more.Foundation.HRESULT: ...
class INetworkListManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('dcb00000-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetNetworks(Flags: win32more.Networking.NetworkListManager.NLM_ENUM_NETWORK, ppEnumNetwork: POINTER(win32more.Networking.NetworkListManager.IEnumNetworks_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetwork(gdNetworkId: Guid, ppNetwork: POINTER(win32more.Networking.NetworkListManager.INetwork_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetNetworkConnections(ppEnum: POINTER(win32more.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetNetworkConnection(gdNetworkConnectionId: Guid, ppNetworkConnection: POINTER(win32more.Networking.NetworkListManager.INetworkConnection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsConnectedToInternet(pbIsConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsConnected(pbIsConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetConnectivity(pConnectivity: POINTER(win32more.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetSimulatedProfileInfo(pSimulatedInfo: POINTER(win32more.Networking.NetworkListManager.NLM_SIMULATED_PROFILE_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ClearSimulatedProfileInfo() -> win32more.Foundation.HRESULT: ...
class INetworkListManagerEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcb00001-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def ConnectivityChanged(newConnectivity: win32more.Networking.NetworkListManager.NLM_CONNECTIVITY) -> win32more.Foundation.HRESULT: ...
NetworkListManager = Guid('dcb00c01-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
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
class NLM_DATAPLAN_STATUS(Structure):
    InterfaceGuid: Guid
    UsageData: win32more.Networking.NetworkListManager.NLM_USAGE_DATA
    DataLimitInMegabytes: UInt32
    InboundBandwidthInKbps: UInt32
    OutboundBandwidthInKbps: UInt32
    NextBillingCycle: win32more.Foundation.FILETIME
    MaxTransferSizeInMegabytes: UInt32
    Reserved: UInt32
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
class NLM_SIMULATED_PROFILE_INFO(Structure):
    ProfileName: Char * 256
    cost: win32more.Networking.NetworkListManager.NLM_CONNECTION_COST
    UsageInMegabytes: UInt32
    DataLimitInMegabytes: UInt32
class NLM_SOCKADDR(Structure):
    data: Byte * 128
class NLM_USAGE_DATA(Structure):
    UsageInMegabytes: UInt32
    LastSyncTime: win32more.Foundation.FILETIME
make_head(_module, 'IEnumNetworkConnections')
make_head(_module, 'IEnumNetworks')
make_head(_module, 'INetwork')
make_head(_module, 'INetworkConnection')
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
__all__ = [
    "IEnumNetworkConnections",
    "IEnumNetworks",
    "INetwork",
    "INetworkConnection",
    "INetworkConnectionCost",
    "INetworkConnectionCostEvents",
    "INetworkConnectionEvents",
    "INetworkCostManager",
    "INetworkCostManagerEvents",
    "INetworkEvents",
    "INetworkListManager",
    "INetworkListManagerEvents",
    "NA_AllowMerge",
    "NA_CategoryReadOnly",
    "NA_CategorySetByPolicy",
    "NA_DescriptionReadOnly",
    "NA_DescriptionSetByPolicy",
    "NA_DomainAuthenticationFailed",
    "NA_IconReadOnly",
    "NA_IconSetByPolicy",
    "NA_InternetConnectivityV4",
    "NA_InternetConnectivityV6",
    "NA_NameReadOnly",
    "NA_NameSetByPolicy",
    "NA_NetworkClass",
    "NLM_CONNECTION_COST",
    "NLM_CONNECTION_COST_APPROACHINGDATALIMIT",
    "NLM_CONNECTION_COST_CONGESTED",
    "NLM_CONNECTION_COST_FIXED",
    "NLM_CONNECTION_COST_OVERDATALIMIT",
    "NLM_CONNECTION_COST_ROAMING",
    "NLM_CONNECTION_COST_UNKNOWN",
    "NLM_CONNECTION_COST_UNRESTRICTED",
    "NLM_CONNECTION_COST_VARIABLE",
    "NLM_CONNECTION_PROPERTY_CHANGE",
    "NLM_CONNECTION_PROPERTY_CHANGE_AUTHENTICATION",
    "NLM_CONNECTIVITY",
    "NLM_CONNECTIVITY_DISCONNECTED",
    "NLM_CONNECTIVITY_IPV4_INTERNET",
    "NLM_CONNECTIVITY_IPV4_LOCALNETWORK",
    "NLM_CONNECTIVITY_IPV4_NOTRAFFIC",
    "NLM_CONNECTIVITY_IPV4_SUBNET",
    "NLM_CONNECTIVITY_IPV6_INTERNET",
    "NLM_CONNECTIVITY_IPV6_LOCALNETWORK",
    "NLM_CONNECTIVITY_IPV6_NOTRAFFIC",
    "NLM_CONNECTIVITY_IPV6_SUBNET",
    "NLM_DATAPLAN_STATUS",
    "NLM_DOMAIN_TYPE",
    "NLM_DOMAIN_TYPE_DOMAIN_AUTHENTICATED",
    "NLM_DOMAIN_TYPE_DOMAIN_NETWORK",
    "NLM_DOMAIN_TYPE_NON_DOMAIN_NETWORK",
    "NLM_ENUM_NETWORK",
    "NLM_ENUM_NETWORK_ALL",
    "NLM_ENUM_NETWORK_CONNECTED",
    "NLM_ENUM_NETWORK_DISCONNECTED",
    "NLM_INTERNET_CONNECTIVITY",
    "NLM_INTERNET_CONNECTIVITY_CORPORATE",
    "NLM_INTERNET_CONNECTIVITY_PROXIED",
    "NLM_INTERNET_CONNECTIVITY_WEBHIJACK",
    "NLM_MAX_ADDRESS_LIST_SIZE",
    "NLM_NETWORK_CATEGORY",
    "NLM_NETWORK_CATEGORY_DOMAIN_AUTHENTICATED",
    "NLM_NETWORK_CATEGORY_PRIVATE",
    "NLM_NETWORK_CATEGORY_PUBLIC",
    "NLM_NETWORK_CLASS",
    "NLM_NETWORK_IDENTIFIED",
    "NLM_NETWORK_IDENTIFYING",
    "NLM_NETWORK_PROPERTY_CHANGE",
    "NLM_NETWORK_PROPERTY_CHANGE_CATEGORY_VALUE",
    "NLM_NETWORK_PROPERTY_CHANGE_CONNECTION",
    "NLM_NETWORK_PROPERTY_CHANGE_DESCRIPTION",
    "NLM_NETWORK_PROPERTY_CHANGE_ICON",
    "NLM_NETWORK_PROPERTY_CHANGE_NAME",
    "NLM_NETWORK_UNIDENTIFIED",
    "NLM_SIMULATED_PROFILE_INFO",
    "NLM_SOCKADDR",
    "NLM_UNKNOWN_DATAPLAN_STATUS",
    "NLM_USAGE_DATA",
    "NetworkListManager",
]
