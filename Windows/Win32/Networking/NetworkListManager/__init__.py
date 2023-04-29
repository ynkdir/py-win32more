from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
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
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00006-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def get__NewEnum(self, ppEnumVar: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.NetworkListManager.INetworkConnection_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, ppEnumNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNetworks(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00003-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def get__NewEnum(self, ppEnumVar: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Networking.NetworkListManager.INetwork_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, ppEnumNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworks_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetwork(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00002-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetName(self, pszNetworkName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetName(self, szNetworkNewName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDescription(self, pszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDescription(self, szDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkId(self, pgdGuidNetworkId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDomainType(self, pNetworkType: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNetworkConnections(self, ppEnumNetworkConnection: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTimeCreatedAndConnected(self, pdwLowDateTimeCreated: POINTER(UInt32), pdwHighDateTimeCreated: POINTER(UInt32), pdwLowDateTimeConnected: POINTER(UInt32), pdwHighDateTimeConnected: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsConnectedToInternet(self, pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsConnected(self, pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetConnectivity(self, pConnectivity: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCategory(self, pCategory: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetCategory(self, NewCategory: Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_CATEGORY) -> Windows.Win32.Foundation.HRESULT: ...
class INetwork2(ComPtr):
    extends: Windows.Win32.Networking.NetworkListManager.INetwork
    Guid = Guid('b5550abb-3391-4310-80-4f-25-dc-c3-25-ed-81')
    @commethod(20)
    def IsDomainAuthenticatedBy(self, domainAuthenticationKind: Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_AUTHENTICATION_KIND, pValue: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00005-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetNetwork(self, ppNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.INetwork_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsConnectedToInternet(self, pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IsConnected(self, pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnectivity(self, pConnectivity: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetConnectionId(self, pgdConnectionId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAdapterId(self, pgdAdapterId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDomainType(self, pDomainType: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnection2(ComPtr):
    extends: Windows.Win32.Networking.NetworkListManager.INetworkConnection
    Guid = Guid('00e676ed-5a35-4738-92-eb-85-81-73-8d-0f-0a')
    @commethod(14)
    def IsDomainAuthenticatedBy(self, domainAuthenticationKind: Windows.Win32.Networking.NetworkListManager.NLM_DOMAIN_AUTHENTICATION_KIND, pValue: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionCost(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb0000a-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def GetCost(self, pCost: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(self, pDataPlanStatus: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionCostEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb0000b-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def ConnectionCostChanged(self, connectionId: Guid, newCost: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConnectionDataPlanStatusChanged(self, connectionId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkConnectionEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00007-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def NetworkConnectionConnectivityChanged(self, connectionId: Guid, newConnectivity: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkConnectionPropertyChanged(self, connectionId: Guid, flags: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_PROPERTY_CHANGE) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkCostManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00008-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def GetCost(self, pCost: POINTER(UInt32), pDestIPAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataPlanStatus(self, pDataPlanStatus: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_DATAPLAN_STATUS_head), pDestIPAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDestinationAddresses(self, length: UInt32, pDestIPAddrList: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head), bAppend: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkCostManagerEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00009-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def CostChanged(self, newCost: UInt32, pDestAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DataPlanStatusChanged(self, pDestAddr: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SOCKADDR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00004-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def NetworkAdded(self, networkId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NetworkDeleted(self, networkId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NetworkConnectivityChanged(self, networkId: Guid, newConnectivity: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NetworkPropertyChanged(self, networkId: Guid, flags: Windows.Win32.Networking.NetworkListManager.NLM_NETWORK_PROPERTY_CHANGE) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkListManager(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dcb00000-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(7)
    def GetNetworks(self, Flags: Windows.Win32.Networking.NetworkListManager.NLM_ENUM_NETWORK, ppEnumNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworks_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetwork(self, gdNetworkId: Guid, ppNetwork: POINTER(Windows.Win32.Networking.NetworkListManager.INetwork_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNetworkConnections(self, ppEnum: POINTER(Windows.Win32.Networking.NetworkListManager.IEnumNetworkConnections_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetNetworkConnection(self, gdNetworkConnectionId: Guid, ppNetworkConnection: POINTER(Windows.Win32.Networking.NetworkListManager.INetworkConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsConnectedToInternet(self, pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsConnected(self, pbIsConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConnectivity(self, pConnectivity: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSimulatedProfileInfo(self, pSimulatedInfo: POINTER(Windows.Win32.Networking.NetworkListManager.NLM_SIMULATED_PROFILE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearSimulatedProfileInfo(self) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkListManagerEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb00001-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
    @commethod(3)
    def ConnectivityChanged(self, newConnectivity: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTIVITY) -> Windows.Win32.Foundation.HRESULT: ...
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
    UsageData: Windows.Win32.Networking.NetworkListManager.NLM_USAGE_DATA
    DataLimitInMegabytes: UInt32
    InboundBandwidthInKbps: UInt32
    OutboundBandwidthInKbps: UInt32
    NextBillingCycle: Windows.Win32.Foundation.FILETIME
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
    cost: Windows.Win32.Networking.NetworkListManager.NLM_CONNECTION_COST
    UsageInMegabytes: UInt32
    DataLimitInMegabytes: UInt32
class NLM_SOCKADDR(EasyCastStructure):
    data: Byte * 128
class NLM_USAGE_DATA(EasyCastStructure):
    UsageInMegabytes: UInt32
    LastSyncTime: Windows.Win32.Foundation.FILETIME
NetworkListManager = Guid('dcb00c01-570f-4a9b-8d-69-19-9f-db-a5-72-3b')
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
