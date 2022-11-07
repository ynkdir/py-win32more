from win32more import *
import win32more.Foundation
import win32more.Networking.NetworkListManager
import win32more.System.Com
import win32more.System.Ole

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
NLM_MAX_ADDRESS_LIST_SIZE = 10
NLM_UNKNOWN_DATAPLAN_STATUS = 4294967295
NetworkListManager = Guid('dcb00c01-570f-4a9b-8d69-199fdba5723b')
NLM_CONNECTION_COST = Int32
NLM_CONNECTION_COST_UNKNOWN = 0
NLM_CONNECTION_COST_UNRESTRICTED = 1
NLM_CONNECTION_COST_FIXED = 2
NLM_CONNECTION_COST_VARIABLE = 4
NLM_CONNECTION_COST_OVERDATALIMIT = 65536
NLM_CONNECTION_COST_CONGESTED = 131072
NLM_CONNECTION_COST_ROAMING = 262144
NLM_CONNECTION_COST_APPROACHINGDATALIMIT = 524288
def _define_NLM_USAGE_DATA_head():
    class NLM_USAGE_DATA(Structure):
        pass
    return NLM_USAGE_DATA
def _define_NLM_USAGE_DATA():
    NLM_USAGE_DATA = win32more.Networking.NetworkListManager.NLM_USAGE_DATA_head
    NLM_USAGE_DATA._fields_ = [
        ("UsageInMegabytes", UInt32),
        ("LastSyncTime", win32more.Foundation.FILETIME),
    ]
    return NLM_USAGE_DATA
def _define_NLM_DATAPLAN_STATUS_head():
    class NLM_DATAPLAN_STATUS(Structure):
        pass
    return NLM_DATAPLAN_STATUS
def _define_NLM_DATAPLAN_STATUS():
    NLM_DATAPLAN_STATUS = win32more.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head
    NLM_DATAPLAN_STATUS._fields_ = [
        ("InterfaceGuid", Guid),
        ("UsageData", win32more.Networking.NetworkListManager.NLM_USAGE_DATA),
        ("DataLimitInMegabytes", UInt32),
        ("InboundBandwidthInKbps", UInt32),
        ("OutboundBandwidthInKbps", UInt32),
        ("NextBillingCycle", win32more.Foundation.FILETIME),
        ("MaxTransferSizeInMegabytes", UInt32),
        ("Reserved", UInt32),
    ]
    return NLM_DATAPLAN_STATUS
def _define_NLM_SOCKADDR_head():
    class NLM_SOCKADDR(Structure):
        pass
    return NLM_SOCKADDR
def _define_NLM_SOCKADDR():
    NLM_SOCKADDR = win32more.Networking.NetworkListManager.NLM_SOCKADDR_head
    NLM_SOCKADDR._fields_ = [
        ("data", Byte * 128),
    ]
    return NLM_SOCKADDR
NLM_NETWORK_CLASS = Int32
NLM_NETWORK_IDENTIFYING = 1
NLM_NETWORK_IDENTIFIED = 2
NLM_NETWORK_UNIDENTIFIED = 3
def _define_NLM_SIMULATED_PROFILE_INFO_head():
    class NLM_SIMULATED_PROFILE_INFO(Structure):
        pass
    return NLM_SIMULATED_PROFILE_INFO
def _define_NLM_SIMULATED_PROFILE_INFO():
    NLM_SIMULATED_PROFILE_INFO = win32more.Networking.NetworkListManager.NLM_SIMULATED_PROFILE_INFO_head
    NLM_SIMULATED_PROFILE_INFO._fields_ = [
        ("ProfileName", Char * 256),
        ("cost", win32more.Networking.NetworkListManager.NLM_CONNECTION_COST),
        ("UsageInMegabytes", UInt32),
        ("DataLimitInMegabytes", UInt32),
    ]
    return NLM_SIMULATED_PROFILE_INFO
NLM_INTERNET_CONNECTIVITY = Int32
NLM_INTERNET_CONNECTIVITY_WEBHIJACK = 1
NLM_INTERNET_CONNECTIVITY_PROXIED = 2
NLM_INTERNET_CONNECTIVITY_CORPORATE = 4
NLM_CONNECTIVITY = Int32
NLM_CONNECTIVITY_DISCONNECTED = 0
NLM_CONNECTIVITY_IPV4_NOTRAFFIC = 1
NLM_CONNECTIVITY_IPV6_NOTRAFFIC = 2
NLM_CONNECTIVITY_IPV4_SUBNET = 16
NLM_CONNECTIVITY_IPV4_LOCALNETWORK = 32
NLM_CONNECTIVITY_IPV4_INTERNET = 64
NLM_CONNECTIVITY_IPV6_SUBNET = 256
NLM_CONNECTIVITY_IPV6_LOCALNETWORK = 512
NLM_CONNECTIVITY_IPV6_INTERNET = 1024
NLM_DOMAIN_TYPE = Int32
NLM_DOMAIN_TYPE_NON_DOMAIN_NETWORK = 0
NLM_DOMAIN_TYPE_DOMAIN_NETWORK = 1
NLM_DOMAIN_TYPE_DOMAIN_AUTHENTICATED = 2
NLM_ENUM_NETWORK = Int32
NLM_ENUM_NETWORK_CONNECTED = 1
NLM_ENUM_NETWORK_DISCONNECTED = 2
NLM_ENUM_NETWORK_ALL = 3
def _define_INetworkListManager_head():
    class INetworkListManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcb00000-570f-4a9b-8d69-199fdba5723b')
    return INetworkListManager
def _define_INetworkListManager():
    INetworkListManager = win32more.Networking.NetworkListManager.INetworkListManager_head
    INetworkListManager.GetNetworks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.NetworkListManager.NLM_ENUM_NETWORK,POINTER(win32more.Networking.NetworkListManager.IEnumNetworks_head), use_last_error=False)(7, 'GetNetworks', ((1, 'Flags'),(1, 'ppEnumNetwork'),)))
    INetworkListManager.GetNetwork = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Networking.NetworkListManager.INetwork_head), use_last_error=False)(8, 'GetNetwork', ((1, 'gdNetworkId'),(1, 'ppNetwork'),)))
    INetworkListManager.GetNetworkConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.IEnumNetworkConnections_head), use_last_error=False)(9, 'GetNetworkConnections', ((1, 'ppEnum'),)))
    INetworkListManager.GetNetworkConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Networking.NetworkListManager.INetworkConnection_head), use_last_error=False)(10, 'GetNetworkConnection', ((1, 'gdNetworkConnectionId'),(1, 'ppNetworkConnection'),)))
    INetworkListManager.get_IsConnectedToInternet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsConnectedToInternet', ((1, 'pbIsConnected'),)))
    INetworkListManager.get_IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_IsConnected', ((1, 'pbIsConnected'),)))
    INetworkListManager.GetConnectivity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_CONNECTIVITY), use_last_error=False)(13, 'GetConnectivity', ((1, 'pConnectivity'),)))
    INetworkListManager.SetSimulatedProfileInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_SIMULATED_PROFILE_INFO_head), use_last_error=False)(14, 'SetSimulatedProfileInfo', ((1, 'pSimulatedInfo'),)))
    INetworkListManager.ClearSimulatedProfileInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'ClearSimulatedProfileInfo', ()))
    win32more.System.Com.IDispatch
    return INetworkListManager
def _define_INetworkListManagerEvents_head():
    class INetworkListManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcb00001-570f-4a9b-8d69-199fdba5723b')
    return INetworkListManagerEvents
def _define_INetworkListManagerEvents():
    INetworkListManagerEvents = win32more.Networking.NetworkListManager.INetworkListManagerEvents_head
    INetworkListManagerEvents.ConnectivityChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.NetworkListManager.NLM_CONNECTIVITY, use_last_error=False)(3, 'ConnectivityChanged', ((1, 'newConnectivity'),)))
    win32more.System.Com.IUnknown
    return INetworkListManagerEvents
NLM_NETWORK_CATEGORY = Int32
NLM_NETWORK_CATEGORY_PUBLIC = 0
NLM_NETWORK_CATEGORY_PRIVATE = 1
NLM_NETWORK_CATEGORY_DOMAIN_AUTHENTICATED = 2
def _define_INetwork_head():
    class INetwork(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcb00002-570f-4a9b-8d69-199fdba5723b')
    return INetwork
def _define_INetwork():
    INetwork = win32more.Networking.NetworkListManager.INetwork_head
    INetwork.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetName', ((1, 'pszNetworkName'),)))
    INetwork.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'SetName', ((1, 'szNetworkNewName'),)))
    INetwork.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetDescription', ((1, 'pszDescription'),)))
    INetwork.SetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'SetDescription', ((1, 'szDescription'),)))
    INetwork.GetNetworkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(11, 'GetNetworkId', ((1, 'pgdGuidNetworkId'),)))
    INetwork.GetDomainType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_DOMAIN_TYPE), use_last_error=False)(12, 'GetDomainType', ((1, 'pNetworkType'),)))
    INetwork.GetNetworkConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.IEnumNetworkConnections_head), use_last_error=False)(13, 'GetNetworkConnections', ((1, 'ppEnumNetworkConnection'),)))
    INetwork.GetTimeCreatedAndConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(14, 'GetTimeCreatedAndConnected', ((1, 'pdwLowDateTimeCreated'),(1, 'pdwHighDateTimeCreated'),(1, 'pdwLowDateTimeConnected'),(1, 'pdwHighDateTimeConnected'),)))
    INetwork.get_IsConnectedToInternet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_IsConnectedToInternet', ((1, 'pbIsConnected'),)))
    INetwork.get_IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_IsConnected', ((1, 'pbIsConnected'),)))
    INetwork.GetConnectivity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_CONNECTIVITY), use_last_error=False)(17, 'GetConnectivity', ((1, 'pConnectivity'),)))
    INetwork.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_NETWORK_CATEGORY), use_last_error=False)(18, 'GetCategory', ((1, 'pCategory'),)))
    INetwork.SetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.NetworkListManager.NLM_NETWORK_CATEGORY, use_last_error=False)(19, 'SetCategory', ((1, 'NewCategory'),)))
    win32more.System.Com.IDispatch
    return INetwork
def _define_IEnumNetworks_head():
    class IEnumNetworks(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcb00003-570f-4a9b-8d69-199fdba5723b')
    return IEnumNetworks
def _define_IEnumNetworks():
    IEnumNetworks = win32more.Networking.NetworkListManager.IEnumNetworks_head
    IEnumNetworks.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppEnumVar'),)))
    IEnumNetworks.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.NetworkListManager.INetwork_head),POINTER(UInt32), use_last_error=False)(8, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumNetworks.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'Skip', ((1, 'celt'),)))
    IEnumNetworks.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Reset', ()))
    IEnumNetworks.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.IEnumNetworks_head), use_last_error=False)(11, 'Clone', ((1, 'ppEnumNetwork'),)))
    win32more.System.Com.IDispatch
    return IEnumNetworks
NLM_NETWORK_PROPERTY_CHANGE = Int32
NLM_NETWORK_PROPERTY_CHANGE_CONNECTION = 1
NLM_NETWORK_PROPERTY_CHANGE_DESCRIPTION = 2
NLM_NETWORK_PROPERTY_CHANGE_NAME = 4
NLM_NETWORK_PROPERTY_CHANGE_ICON = 8
NLM_NETWORK_PROPERTY_CHANGE_CATEGORY_VALUE = 16
def _define_INetworkEvents_head():
    class INetworkEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcb00004-570f-4a9b-8d69-199fdba5723b')
    return INetworkEvents
def _define_INetworkEvents():
    INetworkEvents = win32more.Networking.NetworkListManager.INetworkEvents_head
    INetworkEvents.NetworkAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(3, 'NetworkAdded', ((1, 'networkId'),)))
    INetworkEvents.NetworkDeleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(4, 'NetworkDeleted', ((1, 'networkId'),)))
    INetworkEvents.NetworkConnectivityChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Networking.NetworkListManager.NLM_CONNECTIVITY, use_last_error=False)(5, 'NetworkConnectivityChanged', ((1, 'networkId'),(1, 'newConnectivity'),)))
    INetworkEvents.NetworkPropertyChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE, use_last_error=False)(6, 'NetworkPropertyChanged', ((1, 'networkId'),(1, 'flags'),)))
    win32more.System.Com.IUnknown
    return INetworkEvents
def _define_INetworkConnection_head():
    class INetworkConnection(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcb00005-570f-4a9b-8d69-199fdba5723b')
    return INetworkConnection
def _define_INetworkConnection():
    INetworkConnection = win32more.Networking.NetworkListManager.INetworkConnection_head
    INetworkConnection.GetNetwork = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.INetwork_head), use_last_error=False)(7, 'GetNetwork', ((1, 'ppNetwork'),)))
    INetworkConnection.get_IsConnectedToInternet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_IsConnectedToInternet', ((1, 'pbIsConnected'),)))
    INetworkConnection.get_IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_IsConnected', ((1, 'pbIsConnected'),)))
    INetworkConnection.GetConnectivity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_CONNECTIVITY), use_last_error=False)(10, 'GetConnectivity', ((1, 'pConnectivity'),)))
    INetworkConnection.GetConnectionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(11, 'GetConnectionId', ((1, 'pgdConnectionId'),)))
    INetworkConnection.GetAdapterId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(12, 'GetAdapterId', ((1, 'pgdAdapterId'),)))
    INetworkConnection.GetDomainType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_DOMAIN_TYPE), use_last_error=False)(13, 'GetDomainType', ((1, 'pDomainType'),)))
    win32more.System.Com.IDispatch
    return INetworkConnection
def _define_IEnumNetworkConnections_head():
    class IEnumNetworkConnections(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcb00006-570f-4a9b-8d69-199fdba5723b')
    return IEnumNetworkConnections
def _define_IEnumNetworkConnections():
    IEnumNetworkConnections = win32more.Networking.NetworkListManager.IEnumNetworkConnections_head
    IEnumNetworkConnections.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppEnumVar'),)))
    IEnumNetworkConnections.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.NetworkListManager.INetworkConnection_head),POINTER(UInt32), use_last_error=False)(8, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumNetworkConnections.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'Skip', ((1, 'celt'),)))
    IEnumNetworkConnections.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Reset', ()))
    IEnumNetworkConnections.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.IEnumNetworkConnections_head), use_last_error=False)(11, 'Clone', ((1, 'ppEnumNetwork'),)))
    win32more.System.Com.IDispatch
    return IEnumNetworkConnections
NLM_CONNECTION_PROPERTY_CHANGE = Int32
NLM_CONNECTION_PROPERTY_CHANGE_AUTHENTICATION = 1
def _define_INetworkConnectionEvents_head():
    class INetworkConnectionEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcb00007-570f-4a9b-8d69-199fdba5723b')
    return INetworkConnectionEvents
def _define_INetworkConnectionEvents():
    INetworkConnectionEvents = win32more.Networking.NetworkListManager.INetworkConnectionEvents_head
    INetworkConnectionEvents.NetworkConnectionConnectivityChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Networking.NetworkListManager.NLM_CONNECTIVITY, use_last_error=False)(3, 'NetworkConnectionConnectivityChanged', ((1, 'connectionId'),(1, 'newConnectivity'),)))
    INetworkConnectionEvents.NetworkConnectionPropertyChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Networking.NetworkListManager.NLM_CONNECTION_PROPERTY_CHANGE, use_last_error=False)(4, 'NetworkConnectionPropertyChanged', ((1, 'connectionId'),(1, 'flags'),)))
    win32more.System.Com.IUnknown
    return INetworkConnectionEvents
def _define_INetworkCostManager_head():
    class INetworkCostManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcb00008-570f-4a9b-8d69-199fdba5723b')
    return INetworkCostManager
def _define_INetworkCostManager():
    INetworkCostManager = win32more.Networking.NetworkListManager.INetworkCostManager_head
    INetworkCostManager.GetCost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head), use_last_error=False)(3, 'GetCost', ((1, 'pCost'),(1, 'pDestIPAddr'),)))
    INetworkCostManager.GetDataPlanStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head),POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head), use_last_error=False)(4, 'GetDataPlanStatus', ((1, 'pDataPlanStatus'),(1, 'pDestIPAddr'),)))
    INetworkCostManager.SetDestinationAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR),Int16, use_last_error=False)(5, 'SetDestinationAddresses', ((1, 'length'),(1, 'pDestIPAddrList'),(1, 'bAppend'),)))
    win32more.System.Com.IUnknown
    return INetworkCostManager
def _define_INetworkCostManagerEvents_head():
    class INetworkCostManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcb00009-570f-4a9b-8d69-199fdba5723b')
    return INetworkCostManagerEvents
def _define_INetworkCostManagerEvents():
    INetworkCostManagerEvents = win32more.Networking.NetworkListManager.INetworkCostManagerEvents_head
    INetworkCostManagerEvents.CostChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head), use_last_error=False)(3, 'CostChanged', ((1, 'newCost'),(1, 'pDestAddr'),)))
    INetworkCostManagerEvents.DataPlanStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_SOCKADDR_head), use_last_error=False)(4, 'DataPlanStatusChanged', ((1, 'pDestAddr'),)))
    win32more.System.Com.IUnknown
    return INetworkCostManagerEvents
def _define_INetworkConnectionCost_head():
    class INetworkConnectionCost(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcb0000a-570f-4a9b-8d69-199fdba5723b')
    return INetworkConnectionCost
def _define_INetworkConnectionCost():
    INetworkConnectionCost = win32more.Networking.NetworkListManager.INetworkConnectionCost_head
    INetworkConnectionCost.GetCost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCost', ((1, 'pCost'),)))
    INetworkConnectionCost.GetDataPlanStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head), use_last_error=False)(4, 'GetDataPlanStatus', ((1, 'pDataPlanStatus'),)))
    win32more.System.Com.IUnknown
    return INetworkConnectionCost
def _define_INetworkConnectionCostEvents_head():
    class INetworkConnectionCostEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcb0000b-570f-4a9b-8d69-199fdba5723b')
    return INetworkConnectionCostEvents
def _define_INetworkConnectionCostEvents():
    INetworkConnectionCostEvents = win32more.Networking.NetworkListManager.INetworkConnectionCostEvents_head
    INetworkConnectionCostEvents.ConnectionCostChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32, use_last_error=False)(3, 'ConnectionCostChanged', ((1, 'connectionId'),(1, 'newCost'),)))
    INetworkConnectionCostEvents.ConnectionDataPlanStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(4, 'ConnectionDataPlanStatusChanged', ((1, 'connectionId'),)))
    win32more.System.Com.IUnknown
    return INetworkConnectionCostEvents
__all__ = [
    "NLM_MAX_ADDRESS_LIST_SIZE",
    "NLM_UNKNOWN_DATAPLAN_STATUS",
    "NetworkListManager",
    "NLM_CONNECTION_COST",
    "NLM_CONNECTION_COST_UNKNOWN",
    "NLM_CONNECTION_COST_UNRESTRICTED",
    "NLM_CONNECTION_COST_FIXED",
    "NLM_CONNECTION_COST_VARIABLE",
    "NLM_CONNECTION_COST_OVERDATALIMIT",
    "NLM_CONNECTION_COST_CONGESTED",
    "NLM_CONNECTION_COST_ROAMING",
    "NLM_CONNECTION_COST_APPROACHINGDATALIMIT",
    "NLM_USAGE_DATA",
    "NLM_DATAPLAN_STATUS",
    "NLM_SOCKADDR",
    "NLM_NETWORK_CLASS",
    "NLM_NETWORK_IDENTIFYING",
    "NLM_NETWORK_IDENTIFIED",
    "NLM_NETWORK_UNIDENTIFIED",
    "NLM_SIMULATED_PROFILE_INFO",
    "NLM_INTERNET_CONNECTIVITY",
    "NLM_INTERNET_CONNECTIVITY_WEBHIJACK",
    "NLM_INTERNET_CONNECTIVITY_PROXIED",
    "NLM_INTERNET_CONNECTIVITY_CORPORATE",
    "NLM_CONNECTIVITY",
    "NLM_CONNECTIVITY_DISCONNECTED",
    "NLM_CONNECTIVITY_IPV4_NOTRAFFIC",
    "NLM_CONNECTIVITY_IPV6_NOTRAFFIC",
    "NLM_CONNECTIVITY_IPV4_SUBNET",
    "NLM_CONNECTIVITY_IPV4_LOCALNETWORK",
    "NLM_CONNECTIVITY_IPV4_INTERNET",
    "NLM_CONNECTIVITY_IPV6_SUBNET",
    "NLM_CONNECTIVITY_IPV6_LOCALNETWORK",
    "NLM_CONNECTIVITY_IPV6_INTERNET",
    "NLM_DOMAIN_TYPE",
    "NLM_DOMAIN_TYPE_NON_DOMAIN_NETWORK",
    "NLM_DOMAIN_TYPE_DOMAIN_NETWORK",
    "NLM_DOMAIN_TYPE_DOMAIN_AUTHENTICATED",
    "NLM_ENUM_NETWORK",
    "NLM_ENUM_NETWORK_CONNECTED",
    "NLM_ENUM_NETWORK_DISCONNECTED",
    "NLM_ENUM_NETWORK_ALL",
    "INetworkListManager",
    "INetworkListManagerEvents",
    "NLM_NETWORK_CATEGORY",
    "NLM_NETWORK_CATEGORY_PUBLIC",
    "NLM_NETWORK_CATEGORY_PRIVATE",
    "NLM_NETWORK_CATEGORY_DOMAIN_AUTHENTICATED",
    "INetwork",
    "IEnumNetworks",
    "NLM_NETWORK_PROPERTY_CHANGE",
    "NLM_NETWORK_PROPERTY_CHANGE_CONNECTION",
    "NLM_NETWORK_PROPERTY_CHANGE_DESCRIPTION",
    "NLM_NETWORK_PROPERTY_CHANGE_NAME",
    "NLM_NETWORK_PROPERTY_CHANGE_ICON",
    "NLM_NETWORK_PROPERTY_CHANGE_CATEGORY_VALUE",
    "INetworkEvents",
    "INetworkConnection",
    "IEnumNetworkConnections",
    "NLM_CONNECTION_PROPERTY_CHANGE",
    "NLM_CONNECTION_PROPERTY_CHANGE_AUTHENTICATION",
    "INetworkConnectionEvents",
    "INetworkCostManager",
    "INetworkCostManagerEvents",
    "INetworkConnectionCost",
    "INetworkConnectionCostEvents",
]
