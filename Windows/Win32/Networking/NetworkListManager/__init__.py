from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Networking.NetworkListManager
import Windows.Win32.System.Com
import Windows.Win32.System.Ole
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
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00006-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def get__NewEnum(ppEnumVar: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.NetworkListManager.INetworkConnection_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(ppEnumNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNetworks(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00003-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def get__NewEnum(ppEnumVar: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.NetworkListManager.INetwork_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(ppEnumNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworks_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetwork(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00002-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetName(pszNetworkName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetName(szNetworkNewName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDescription(pszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDescription(szDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkId(pgdGuidNetworkId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDomainType(pNetworkType: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNetworkConnections(ppEnumNetworkConnection: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimeCreatedAndConnected(pdwLowDateTimeCreated: POINTER(UInt32), pdwHighDateTimeCreated: POINTER(UInt32), pdwLowDateTimeConnected: POINTER(UInt32), pdwHighDateTimeConnected: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsConnectedToInternet(pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsConnected(pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetConnectivity(pConnectivity: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCategory(pCategory: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetCategory(NewCategory: Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00005-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetNetwork(ppNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.INetwork_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsConnectedToInternet(pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IsConnected(pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnectivity(pConnectivity: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetConnectionId(pgdConnectionId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAdapterId(pgdAdapterId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDomainType(pDomainType: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionCost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb0000a-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def GetCost(pCost: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(pDataPlanStatus: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionCostEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb0000b-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def ConnectionCostChanged(connectionId: Guid, newCost: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConnectionDataPlanStatusChanged(connectionId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00007-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def NetworkConnectionConnectivityChanged(connectionId: Guid, newConnectivity: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkConnectionPropertyChanged(connectionId: Guid, flags: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_PROPERTY_CHANGE) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkCostManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00008-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def GetCost(pCost: POINTER(UInt32), pDestIPAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(pDataPlanStatus: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head), pDestIPAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDestinationAddresses(length: UInt32, pDestIPAddrList: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head), bAppend: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkCostManagerEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00009-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def CostChanged(newCost: UInt32, pDestAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DataPlanStatusChanged(pDestAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00004-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def NetworkAdded(networkId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkDeleted(networkId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NetworkConnectivityChanged(networkId: Guid, newConnectivity: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NetworkPropertyChanged(networkId: Guid, flags: Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkListManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00000-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetNetworks(Flags: Windows.Win32.Networking.NetworkListManager.NLM_ENUM_NETWORK, ppEnumNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworks_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetwork(gdNetworkId: Guid, ppNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.INetwork_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNetworkConnections(ppEnum: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetNetworkConnection(gdNetworkConnectionId: Guid, ppNetworkConnection: POINTER(Windows.Win32.Networking.NetworkListManager.INetworkConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsConnectedToInternet(pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsConnected(pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConnectivity(pConnectivity: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSimulatedProfileInfo(pSimulatedInfo: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SIMULATED_PROFILE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearSimulatedProfileInfo() -> Windows.Win32.Foundation.HRESULT: ...
class INetworkListManagerEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00001-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def ConnectivityChanged(newConnectivity: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> Windows.Win32.Foundation.HRESULT: ...
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
    UsageData: Windows.Win32.Networking.NetworkListManager.NLM_USAGE_DATA
    DataLimitInMegabytes: UInt32
    InboundBandwidthInKbps: UInt32
    OutboundBandwidthInKbps: UInt32
    NextBillingCycle: Windows.Win32.Foundation.FILETIME
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
    cost: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST
    UsageInMegabytes: UInt32
    DataLimitInMegabytes: UInt32
class NLM_SOCKADDR(Structure):
    data: Byte * 128
class NLM_USAGE_DATA(Structure):
    UsageInMegabytes: UInt32
    LastSyncTime: Windows.Win32.Foundation.FILETIME
NetworkListManager = Guid('dcb00c01-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
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
_arch_optional = [
]
