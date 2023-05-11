from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Connectivity
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AttributedNetworkUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IAttributedNetworkUsage
    _classid_ = 'Windows.Networking.Connectivity.AttributedNetworkUsage'
    @winrt_mixinmethod
    def get_BytesSent(self: Windows.Networking.Connectivity.IAttributedNetworkUsage) -> UInt64: ...
    @winrt_mixinmethod
    def get_BytesReceived(self: Windows.Networking.Connectivity.IAttributedNetworkUsage) -> UInt64: ...
    @winrt_mixinmethod
    def get_AttributionId(self: Windows.Networking.Connectivity.IAttributedNetworkUsage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AttributionName(self: Windows.Networking.Connectivity.IAttributedNetworkUsage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AttributionThumbnail(self: Windows.Networking.Connectivity.IAttributedNetworkUsage) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
    AttributionId = property(get_AttributionId, None)
    AttributionName = property(get_AttributionName, None)
    AttributionThumbnail = property(get_AttributionThumbnail, None)
CellularApnAuthenticationType = Int32
CellularApnAuthenticationType_None: CellularApnAuthenticationType = 0
CellularApnAuthenticationType_Pap: CellularApnAuthenticationType = 1
CellularApnAuthenticationType_Chap: CellularApnAuthenticationType = 2
CellularApnAuthenticationType_Mschapv2: CellularApnAuthenticationType = 3
class CellularApnContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.ICellularApnContext
    _classid_ = 'Windows.Networking.Connectivity.CellularApnContext'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Connectivity.CellularApnContext: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.Connectivity.ICellularApnContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProviderId(self: Windows.Networking.Connectivity.ICellularApnContext, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AccessPointName(self: Windows.Networking.Connectivity.ICellularApnContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AccessPointName(self: Windows.Networking.Connectivity.ICellularApnContext, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserName(self: Windows.Networking.Connectivity.ICellularApnContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserName(self: Windows.Networking.Connectivity.ICellularApnContext, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Password(self: Windows.Networking.Connectivity.ICellularApnContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Password(self: Windows.Networking.Connectivity.ICellularApnContext, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsCompressionEnabled(self: Windows.Networking.Connectivity.ICellularApnContext) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCompressionEnabled(self: Windows.Networking.Connectivity.ICellularApnContext, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AuthenticationType(self: Windows.Networking.Connectivity.ICellularApnContext) -> Windows.Networking.Connectivity.CellularApnAuthenticationType: ...
    @winrt_mixinmethod
    def put_AuthenticationType(self: Windows.Networking.Connectivity.ICellularApnContext, value: Windows.Networking.Connectivity.CellularApnAuthenticationType) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileName(self: Windows.Networking.Connectivity.ICellularApnContext2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProfileName(self: Windows.Networking.Connectivity.ICellularApnContext2, value: WinRT_String) -> Void: ...
    ProviderId = property(get_ProviderId, put_ProviderId)
    AccessPointName = property(get_AccessPointName, put_AccessPointName)
    UserName = property(get_UserName, put_UserName)
    Password = property(get_Password, put_Password)
    IsCompressionEnabled = property(get_IsCompressionEnabled, put_IsCompressionEnabled)
    AuthenticationType = property(get_AuthenticationType, put_AuthenticationType)
    ProfileName = property(get_ProfileName, put_ProfileName)
class ConnectionCost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IConnectionCost
    _classid_ = 'Windows.Networking.Connectivity.ConnectionCost'
    @winrt_mixinmethod
    def get_NetworkCostType(self: Windows.Networking.Connectivity.IConnectionCost) -> Windows.Networking.Connectivity.NetworkCostType: ...
    @winrt_mixinmethod
    def get_Roaming(self: Windows.Networking.Connectivity.IConnectionCost) -> Boolean: ...
    @winrt_mixinmethod
    def get_OverDataLimit(self: Windows.Networking.Connectivity.IConnectionCost) -> Boolean: ...
    @winrt_mixinmethod
    def get_ApproachingDataLimit(self: Windows.Networking.Connectivity.IConnectionCost) -> Boolean: ...
    @winrt_mixinmethod
    def get_BackgroundDataUsageRestricted(self: Windows.Networking.Connectivity.IConnectionCost2) -> Boolean: ...
    NetworkCostType = property(get_NetworkCostType, None)
    Roaming = property(get_Roaming, None)
    OverDataLimit = property(get_OverDataLimit, None)
    ApproachingDataLimit = property(get_ApproachingDataLimit, None)
    BackgroundDataUsageRestricted = property(get_BackgroundDataUsageRestricted, None)
class ConnectionProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IConnectionProfile
    _classid_ = 'Windows.Networking.Connectivity.ConnectionProfile'
    @winrt_mixinmethod
    def get_ProfileName(self: Windows.Networking.Connectivity.IConnectionProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNetworkConnectivityLevel(self: Windows.Networking.Connectivity.IConnectionProfile) -> Windows.Networking.Connectivity.NetworkConnectivityLevel: ...
    @winrt_mixinmethod
    def GetNetworkNames(self: Windows.Networking.Connectivity.IConnectionProfile) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def GetConnectionCost(self: Windows.Networking.Connectivity.IConnectionProfile) -> Windows.Networking.Connectivity.ConnectionCost: ...
    @winrt_mixinmethod
    def GetDataPlanStatus(self: Windows.Networking.Connectivity.IConnectionProfile) -> Windows.Networking.Connectivity.DataPlanStatus: ...
    @winrt_mixinmethod
    def get_NetworkAdapter(self: Windows.Networking.Connectivity.IConnectionProfile) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def GetLocalUsage(self: Windows.Networking.Connectivity.IConnectionProfile, StartTime: Windows.Foundation.DateTime, EndTime: Windows.Foundation.DateTime) -> Windows.Networking.Connectivity.DataUsage: ...
    @winrt_mixinmethod
    def GetLocalUsagePerRoamingStates(self: Windows.Networking.Connectivity.IConnectionProfile, StartTime: Windows.Foundation.DateTime, EndTime: Windows.Foundation.DateTime, States: Windows.Networking.Connectivity.RoamingStates) -> Windows.Networking.Connectivity.DataUsage: ...
    @winrt_mixinmethod
    def get_NetworkSecuritySettings(self: Windows.Networking.Connectivity.IConnectionProfile) -> Windows.Networking.Connectivity.NetworkSecuritySettings: ...
    @winrt_mixinmethod
    def get_IsWwanConnectionProfile(self: Windows.Networking.Connectivity.IConnectionProfile2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsWlanConnectionProfile(self: Windows.Networking.Connectivity.IConnectionProfile2) -> Boolean: ...
    @winrt_mixinmethod
    def get_WwanConnectionProfileDetails(self: Windows.Networking.Connectivity.IConnectionProfile2) -> Windows.Networking.Connectivity.WwanConnectionProfileDetails: ...
    @winrt_mixinmethod
    def get_WlanConnectionProfileDetails(self: Windows.Networking.Connectivity.IConnectionProfile2) -> Windows.Networking.Connectivity.WlanConnectionProfileDetails: ...
    @winrt_mixinmethod
    def get_ServiceProviderGuid(self: Windows.Networking.Connectivity.IConnectionProfile2) -> Windows.Foundation.IReference[Guid]: ...
    @winrt_mixinmethod
    def GetSignalBars(self: Windows.Networking.Connectivity.IConnectionProfile2) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def GetDomainConnectivityLevel(self: Windows.Networking.Connectivity.IConnectionProfile2) -> Windows.Networking.Connectivity.DomainConnectivityLevel: ...
    @winrt_mixinmethod
    def GetNetworkUsageAsync(self: Windows.Networking.Connectivity.IConnectionProfile2, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, granularity: Windows.Networking.Connectivity.DataUsageGranularity, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.NetworkUsage]]: ...
    @winrt_mixinmethod
    def GetConnectivityIntervalsAsync(self: Windows.Networking.Connectivity.IConnectionProfile2, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectivityInterval]]: ...
    @winrt_mixinmethod
    def GetAttributedNetworkUsageAsync(self: Windows.Networking.Connectivity.IConnectionProfile3, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.AttributedNetworkUsage]]: ...
    @winrt_mixinmethod
    def GetProviderNetworkUsageAsync(self: Windows.Networking.Connectivity.IConnectionProfile4, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ProviderNetworkUsage]]: ...
    @winrt_mixinmethod
    def get_CanDelete(self: Windows.Networking.Connectivity.IConnectionProfile5) -> Boolean: ...
    @winrt_mixinmethod
    def TryDeleteAsync(self: Windows.Networking.Connectivity.IConnectionProfile5) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ConnectionProfileDeleteStatus]: ...
    @winrt_mixinmethod
    def IsDomainAuthenticatedBy(self: Windows.Networking.Connectivity.IConnectionProfile6, kind: Windows.Networking.Connectivity.DomainAuthenticationKind) -> Boolean: ...
    ProfileName = property(get_ProfileName, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkSecuritySettings = property(get_NetworkSecuritySettings, None)
    IsWwanConnectionProfile = property(get_IsWwanConnectionProfile, None)
    IsWlanConnectionProfile = property(get_IsWlanConnectionProfile, None)
    WwanConnectionProfileDetails = property(get_WwanConnectionProfileDetails, None)
    WlanConnectionProfileDetails = property(get_WlanConnectionProfileDetails, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
    CanDelete = property(get_CanDelete, None)
ConnectionProfileDeleteStatus = Int32
ConnectionProfileDeleteStatus_Success: ConnectionProfileDeleteStatus = 0
ConnectionProfileDeleteStatus_DeniedByUser: ConnectionProfileDeleteStatus = 1
ConnectionProfileDeleteStatus_DeniedBySystem: ConnectionProfileDeleteStatus = 2
ConnectionProfileDeleteStatus_UnknownError: ConnectionProfileDeleteStatus = 3
class ConnectionProfileFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IConnectionProfileFilter
    _classid_ = 'Windows.Networking.Connectivity.ConnectionProfileFilter'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Connectivity.ConnectionProfileFilter: ...
    @winrt_mixinmethod
    def put_IsConnected(self: Windows.Networking.Connectivity.IConnectionProfileFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsConnected(self: Windows.Networking.Connectivity.IConnectionProfileFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsWwanConnectionProfile(self: Windows.Networking.Connectivity.IConnectionProfileFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsWwanConnectionProfile(self: Windows.Networking.Connectivity.IConnectionProfileFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsWlanConnectionProfile(self: Windows.Networking.Connectivity.IConnectionProfileFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsWlanConnectionProfile(self: Windows.Networking.Connectivity.IConnectionProfileFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_NetworkCostType(self: Windows.Networking.Connectivity.IConnectionProfileFilter, value: Windows.Networking.Connectivity.NetworkCostType) -> Void: ...
    @winrt_mixinmethod
    def get_NetworkCostType(self: Windows.Networking.Connectivity.IConnectionProfileFilter) -> Windows.Networking.Connectivity.NetworkCostType: ...
    @winrt_mixinmethod
    def put_ServiceProviderGuid(self: Windows.Networking.Connectivity.IConnectionProfileFilter, value: Windows.Foundation.IReference[Guid]) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceProviderGuid(self: Windows.Networking.Connectivity.IConnectionProfileFilter) -> Windows.Foundation.IReference[Guid]: ...
    @winrt_mixinmethod
    def put_IsRoaming(self: Windows.Networking.Connectivity.IConnectionProfileFilter2, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_IsRoaming(self: Windows.Networking.Connectivity.IConnectionProfileFilter2) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_IsOverDataLimit(self: Windows.Networking.Connectivity.IConnectionProfileFilter2, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_IsOverDataLimit(self: Windows.Networking.Connectivity.IConnectionProfileFilter2) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_IsBackgroundDataUsageRestricted(self: Windows.Networking.Connectivity.IConnectionProfileFilter2, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_IsBackgroundDataUsageRestricted(self: Windows.Networking.Connectivity.IConnectionProfileFilter2) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Networking.Connectivity.IConnectionProfileFilter2) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_PurposeGuid(self: Windows.Networking.Connectivity.IConnectionProfileFilter3, value: Windows.Foundation.IReference[Guid]) -> Void: ...
    @winrt_mixinmethod
    def get_PurposeGuid(self: Windows.Networking.Connectivity.IConnectionProfileFilter3) -> Windows.Foundation.IReference[Guid]: ...
    IsConnected = property(get_IsConnected, put_IsConnected)
    IsWwanConnectionProfile = property(get_IsWwanConnectionProfile, put_IsWwanConnectionProfile)
    IsWlanConnectionProfile = property(get_IsWlanConnectionProfile, put_IsWlanConnectionProfile)
    NetworkCostType = property(get_NetworkCostType, put_NetworkCostType)
    ServiceProviderGuid = property(get_ServiceProviderGuid, put_ServiceProviderGuid)
    IsRoaming = property(get_IsRoaming, put_IsRoaming)
    IsOverDataLimit = property(get_IsOverDataLimit, put_IsOverDataLimit)
    IsBackgroundDataUsageRestricted = property(get_IsBackgroundDataUsageRestricted, put_IsBackgroundDataUsageRestricted)
    RawData = property(get_RawData, None)
    PurposeGuid = property(get_PurposeGuid, put_PurposeGuid)
class ConnectionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IConnectionSession
    _classid_ = 'Windows.Networking.Connectivity.ConnectionSession'
    @winrt_mixinmethod
    def get_ConnectionProfile(self: Windows.Networking.Connectivity.IConnectionSession) -> Windows.Networking.Connectivity.ConnectionProfile: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    ConnectionProfile = property(get_ConnectionProfile, None)
class ConnectivityInterval(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IConnectivityInterval
    _classid_ = 'Windows.Networking.Connectivity.ConnectivityInterval'
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Networking.Connectivity.IConnectivityInterval) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ConnectionDuration(self: Windows.Networking.Connectivity.IConnectivityInterval) -> Windows.Foundation.TimeSpan: ...
    StartTime = property(get_StartTime, None)
    ConnectionDuration = property(get_ConnectionDuration, None)
class ConnectivityManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.ConnectivityManager'
    @winrt_classmethod
    def AcquireConnectionAsync(cls: Windows.Networking.Connectivity.IConnectivityManagerStatics, cellularApnContext: Windows.Networking.Connectivity.CellularApnContext) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ConnectionSession]: ...
    @winrt_classmethod
    def AddHttpRoutePolicy(cls: Windows.Networking.Connectivity.IConnectivityManagerStatics, routePolicy: Windows.Networking.Connectivity.RoutePolicy) -> Void: ...
    @winrt_classmethod
    def RemoveHttpRoutePolicy(cls: Windows.Networking.Connectivity.IConnectivityManagerStatics, routePolicy: Windows.Networking.Connectivity.RoutePolicy) -> Void: ...
class DataPlanStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IDataPlanStatus
    _classid_ = 'Windows.Networking.Connectivity.DataPlanStatus'
    @winrt_mixinmethod
    def get_DataPlanUsage(self: Windows.Networking.Connectivity.IDataPlanStatus) -> Windows.Networking.Connectivity.DataPlanUsage: ...
    @winrt_mixinmethod
    def get_DataLimitInMegabytes(self: Windows.Networking.Connectivity.IDataPlanStatus) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_InboundBitsPerSecond(self: Windows.Networking.Connectivity.IDataPlanStatus) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_OutboundBitsPerSecond(self: Windows.Networking.Connectivity.IDataPlanStatus) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_mixinmethod
    def get_NextBillingCycle(self: Windows.Networking.Connectivity.IDataPlanStatus) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_MaxTransferSizeInMegabytes(self: Windows.Networking.Connectivity.IDataPlanStatus) -> Windows.Foundation.IReference[UInt32]: ...
    DataPlanUsage = property(get_DataPlanUsage, None)
    DataLimitInMegabytes = property(get_DataLimitInMegabytes, None)
    InboundBitsPerSecond = property(get_InboundBitsPerSecond, None)
    OutboundBitsPerSecond = property(get_OutboundBitsPerSecond, None)
    NextBillingCycle = property(get_NextBillingCycle, None)
    MaxTransferSizeInMegabytes = property(get_MaxTransferSizeInMegabytes, None)
class DataPlanUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IDataPlanUsage
    _classid_ = 'Windows.Networking.Connectivity.DataPlanUsage'
    @winrt_mixinmethod
    def get_MegabytesUsed(self: Windows.Networking.Connectivity.IDataPlanUsage) -> UInt32: ...
    @winrt_mixinmethod
    def get_LastSyncTime(self: Windows.Networking.Connectivity.IDataPlanUsage) -> Windows.Foundation.DateTime: ...
    MegabytesUsed = property(get_MegabytesUsed, None)
    LastSyncTime = property(get_LastSyncTime, None)
class DataUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IDataUsage
    _classid_ = 'Windows.Networking.Connectivity.DataUsage'
    @winrt_mixinmethod
    def get_BytesSent(self: Windows.Networking.Connectivity.IDataUsage) -> UInt64: ...
    @winrt_mixinmethod
    def get_BytesReceived(self: Windows.Networking.Connectivity.IDataUsage) -> UInt64: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
DataUsageGranularity = Int32
DataUsageGranularity_PerMinute: DataUsageGranularity = 0
DataUsageGranularity_PerHour: DataUsageGranularity = 1
DataUsageGranularity_PerDay: DataUsageGranularity = 2
DataUsageGranularity_Total: DataUsageGranularity = 3
DomainAuthenticationKind = Int32
DomainAuthenticationKind_None: DomainAuthenticationKind = 0
DomainAuthenticationKind_Ldap: DomainAuthenticationKind = 1
DomainAuthenticationKind_Tls: DomainAuthenticationKind = 2
DomainConnectivityLevel = Int32
DomainConnectivityLevel_None: DomainConnectivityLevel = 0
DomainConnectivityLevel_Unauthenticated: DomainConnectivityLevel = 1
DomainConnectivityLevel_Authenticated: DomainConnectivityLevel = 2
class IAttributedNetworkUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IAttributedNetworkUsage'
    _iid_ = Guid('{f769b039-eca2-45eb-ade1-b0368b756c49}')
    @winrt_commethod(6)
    def get_BytesSent(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_BytesReceived(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_AttributionId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_AttributionName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AttributionThumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
    AttributionId = property(get_AttributionId, None)
    AttributionName = property(get_AttributionName, None)
    AttributionThumbnail = property(get_AttributionThumbnail, None)
class ICellularApnContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.ICellularApnContext'
    _iid_ = Guid('{6fa529f4-effd-4542-9ab2-705bbf94943a}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ProviderId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AccessPointName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_AccessPointName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_UserName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_UserName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Password(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_Password(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_IsCompressionEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsCompressionEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_AuthenticationType(self) -> Windows.Networking.Connectivity.CellularApnAuthenticationType: ...
    @winrt_commethod(17)
    def put_AuthenticationType(self, value: Windows.Networking.Connectivity.CellularApnAuthenticationType) -> Void: ...
    ProviderId = property(get_ProviderId, put_ProviderId)
    AccessPointName = property(get_AccessPointName, put_AccessPointName)
    UserName = property(get_UserName, put_UserName)
    Password = property(get_Password, put_Password)
    IsCompressionEnabled = property(get_IsCompressionEnabled, put_IsCompressionEnabled)
    AuthenticationType = property(get_AuthenticationType, put_AuthenticationType)
class ICellularApnContext2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.ICellularApnContext2'
    _iid_ = Guid('{76b0eb1a-ac49-4350-b1e5-dc4763bc69c7}')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ProfileName(self, value: WinRT_String) -> Void: ...
    ProfileName = property(get_ProfileName, put_ProfileName)
class IConnectionCost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionCost'
    _iid_ = Guid('{bad7d829-3416-4b10-a202-bac0b075bdae}')
    @winrt_commethod(6)
    def get_NetworkCostType(self) -> Windows.Networking.Connectivity.NetworkCostType: ...
    @winrt_commethod(7)
    def get_Roaming(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_OverDataLimit(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ApproachingDataLimit(self) -> Boolean: ...
    NetworkCostType = property(get_NetworkCostType, None)
    Roaming = property(get_Roaming, None)
    OverDataLimit = property(get_OverDataLimit, None)
    ApproachingDataLimit = property(get_ApproachingDataLimit, None)
class IConnectionCost2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionCost2'
    _iid_ = Guid('{8e113a05-e209-4549-bb25-5e0db691cb05}')
    @winrt_commethod(6)
    def get_BackgroundDataUsageRestricted(self) -> Boolean: ...
    BackgroundDataUsageRestricted = property(get_BackgroundDataUsageRestricted, None)
class IConnectionProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfile'
    _iid_ = Guid('{71ba143c-598e-49d0-84eb-8febaedcc195}')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetNetworkConnectivityLevel(self) -> Windows.Networking.Connectivity.NetworkConnectivityLevel: ...
    @winrt_commethod(8)
    def GetNetworkNames(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def GetConnectionCost(self) -> Windows.Networking.Connectivity.ConnectionCost: ...
    @winrt_commethod(10)
    def GetDataPlanStatus(self) -> Windows.Networking.Connectivity.DataPlanStatus: ...
    @winrt_commethod(11)
    def get_NetworkAdapter(self) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(12)
    def GetLocalUsage(self, StartTime: Windows.Foundation.DateTime, EndTime: Windows.Foundation.DateTime) -> Windows.Networking.Connectivity.DataUsage: ...
    @winrt_commethod(13)
    def GetLocalUsagePerRoamingStates(self, StartTime: Windows.Foundation.DateTime, EndTime: Windows.Foundation.DateTime, States: Windows.Networking.Connectivity.RoamingStates) -> Windows.Networking.Connectivity.DataUsage: ...
    @winrt_commethod(14)
    def get_NetworkSecuritySettings(self) -> Windows.Networking.Connectivity.NetworkSecuritySettings: ...
    ProfileName = property(get_ProfileName, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkSecuritySettings = property(get_NetworkSecuritySettings, None)
class IConnectionProfile2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfile2'
    _iid_ = Guid('{e2045145-4c9f-400c-9150-7ec7d6e2888a}')
    @winrt_commethod(6)
    def get_IsWwanConnectionProfile(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsWlanConnectionProfile(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_WwanConnectionProfileDetails(self) -> Windows.Networking.Connectivity.WwanConnectionProfileDetails: ...
    @winrt_commethod(9)
    def get_WlanConnectionProfileDetails(self) -> Windows.Networking.Connectivity.WlanConnectionProfileDetails: ...
    @winrt_commethod(10)
    def get_ServiceProviderGuid(self) -> Windows.Foundation.IReference[Guid]: ...
    @winrt_commethod(11)
    def GetSignalBars(self) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(12)
    def GetDomainConnectivityLevel(self) -> Windows.Networking.Connectivity.DomainConnectivityLevel: ...
    @winrt_commethod(13)
    def GetNetworkUsageAsync(self, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, granularity: Windows.Networking.Connectivity.DataUsageGranularity, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.NetworkUsage]]: ...
    @winrt_commethod(14)
    def GetConnectivityIntervalsAsync(self, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectivityInterval]]: ...
    IsWwanConnectionProfile = property(get_IsWwanConnectionProfile, None)
    IsWlanConnectionProfile = property(get_IsWlanConnectionProfile, None)
    WwanConnectionProfileDetails = property(get_WwanConnectionProfileDetails, None)
    WlanConnectionProfileDetails = property(get_WlanConnectionProfileDetails, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
class IConnectionProfile3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfile3'
    _iid_ = Guid('{578c2528-4cd9-4161-8045-201cfd5b115c}')
    @winrt_commethod(6)
    def GetAttributedNetworkUsageAsync(self, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.AttributedNetworkUsage]]: ...
class IConnectionProfile4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfile4'
    _iid_ = Guid('{7a2d42cd-81e0-4ae6-abed-ab9ca13eb714}')
    @winrt_commethod(6)
    def GetProviderNetworkUsageAsync(self, startTime: Windows.Foundation.DateTime, endTime: Windows.Foundation.DateTime, states: Windows.Networking.Connectivity.NetworkUsageStates) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ProviderNetworkUsage]]: ...
class IConnectionProfile5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfile5'
    _iid_ = Guid('{85361ec7-9c73-4be0-8f14-578eec71ee0e}')
    @winrt_commethod(6)
    def get_CanDelete(self) -> Boolean: ...
    @winrt_commethod(7)
    def TryDeleteAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ConnectionProfileDeleteStatus]: ...
    CanDelete = property(get_CanDelete, None)
class IConnectionProfile6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfile6'
    _iid_ = Guid('{dc27dfe2-7a6f-5d0e-9589-2fe2e5b6f9aa}')
    @winrt_commethod(6)
    def IsDomainAuthenticatedBy(self, kind: Windows.Networking.Connectivity.DomainAuthenticationKind) -> Boolean: ...
class IConnectionProfileFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfileFilter'
    _iid_ = Guid('{204c7cc8-bd2d-4e8d-a4b3-455ec337388a}')
    @winrt_commethod(6)
    def put_IsConnected(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsConnected(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsWwanConnectionProfile(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsWwanConnectionProfile(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsWlanConnectionProfile(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsWlanConnectionProfile(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_NetworkCostType(self, value: Windows.Networking.Connectivity.NetworkCostType) -> Void: ...
    @winrt_commethod(13)
    def get_NetworkCostType(self) -> Windows.Networking.Connectivity.NetworkCostType: ...
    @winrt_commethod(14)
    def put_ServiceProviderGuid(self, value: Windows.Foundation.IReference[Guid]) -> Void: ...
    @winrt_commethod(15)
    def get_ServiceProviderGuid(self) -> Windows.Foundation.IReference[Guid]: ...
    IsConnected = property(get_IsConnected, put_IsConnected)
    IsWwanConnectionProfile = property(get_IsWwanConnectionProfile, put_IsWwanConnectionProfile)
    IsWlanConnectionProfile = property(get_IsWlanConnectionProfile, put_IsWlanConnectionProfile)
    NetworkCostType = property(get_NetworkCostType, put_NetworkCostType)
    ServiceProviderGuid = property(get_ServiceProviderGuid, put_ServiceProviderGuid)
class IConnectionProfileFilter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfileFilter2'
    _iid_ = Guid('{cd068ee1-c3fc-4fad-9ddc-593faa4b7885}')
    @winrt_commethod(6)
    def put_IsRoaming(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(7)
    def get_IsRoaming(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(8)
    def put_IsOverDataLimit(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(9)
    def get_IsOverDataLimit(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(10)
    def put_IsBackgroundDataUsageRestricted(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(11)
    def get_IsBackgroundDataUsageRestricted(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(12)
    def get_RawData(self) -> Windows.Storage.Streams.IBuffer: ...
    IsRoaming = property(get_IsRoaming, put_IsRoaming)
    IsOverDataLimit = property(get_IsOverDataLimit, put_IsOverDataLimit)
    IsBackgroundDataUsageRestricted = property(get_IsBackgroundDataUsageRestricted, put_IsBackgroundDataUsageRestricted)
    RawData = property(get_RawData, None)
class IConnectionProfileFilter3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionProfileFilter3'
    _iid_ = Guid('{0aaa09c0-5014-447c-8809-aee4cb0af94a}')
    @winrt_commethod(6)
    def put_PurposeGuid(self, value: Windows.Foundation.IReference[Guid]) -> Void: ...
    @winrt_commethod(7)
    def get_PurposeGuid(self) -> Windows.Foundation.IReference[Guid]: ...
    PurposeGuid = property(get_PurposeGuid, put_PurposeGuid)
class IConnectionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectionSession'
    _iid_ = Guid('{ff905d4c-f83b-41b0-8a0c-1462d9c56b73}')
    @winrt_commethod(6)
    def get_ConnectionProfile(self) -> Windows.Networking.Connectivity.ConnectionProfile: ...
    ConnectionProfile = property(get_ConnectionProfile, None)
class IConnectivityInterval(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectivityInterval'
    _iid_ = Guid('{4faa3fff-6746-4824-a964-eed8e87f8709}')
    @winrt_commethod(6)
    def get_StartTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_ConnectionDuration(self) -> Windows.Foundation.TimeSpan: ...
    StartTime = property(get_StartTime, None)
    ConnectionDuration = property(get_ConnectionDuration, None)
class IConnectivityManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IConnectivityManagerStatics'
    _iid_ = Guid('{5120d4b1-4fb1-48b0-afc9-42e0092a8164}')
    @winrt_commethod(6)
    def AcquireConnectionAsync(self, cellularApnContext: Windows.Networking.Connectivity.CellularApnContext) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ConnectionSession]: ...
    @winrt_commethod(7)
    def AddHttpRoutePolicy(self, routePolicy: Windows.Networking.Connectivity.RoutePolicy) -> Void: ...
    @winrt_commethod(8)
    def RemoveHttpRoutePolicy(self, routePolicy: Windows.Networking.Connectivity.RoutePolicy) -> Void: ...
class IDataPlanStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IDataPlanStatus'
    _iid_ = Guid('{977a8b8c-3885-40f3-8851-42cd2bd568bb}')
    @winrt_commethod(6)
    def get_DataPlanUsage(self) -> Windows.Networking.Connectivity.DataPlanUsage: ...
    @winrt_commethod(7)
    def get_DataLimitInMegabytes(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def get_InboundBitsPerSecond(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(9)
    def get_OutboundBitsPerSecond(self) -> Windows.Foundation.IReference[UInt64]: ...
    @winrt_commethod(10)
    def get_NextBillingCycle(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def get_MaxTransferSizeInMegabytes(self) -> Windows.Foundation.IReference[UInt32]: ...
    DataPlanUsage = property(get_DataPlanUsage, None)
    DataLimitInMegabytes = property(get_DataLimitInMegabytes, None)
    InboundBitsPerSecond = property(get_InboundBitsPerSecond, None)
    OutboundBitsPerSecond = property(get_OutboundBitsPerSecond, None)
    NextBillingCycle = property(get_NextBillingCycle, None)
    MaxTransferSizeInMegabytes = property(get_MaxTransferSizeInMegabytes, None)
class IDataPlanUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IDataPlanUsage'
    _iid_ = Guid('{b921492d-3b44-47ff-b361-be59e69ed1b0}')
    @winrt_commethod(6)
    def get_MegabytesUsed(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_LastSyncTime(self) -> Windows.Foundation.DateTime: ...
    MegabytesUsed = property(get_MegabytesUsed, None)
    LastSyncTime = property(get_LastSyncTime, None)
class IDataUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IDataUsage'
    _iid_ = Guid('{c1431dd3-b146-4d39-b959-0c69b096c512}')
    @winrt_commethod(6)
    def get_BytesSent(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_BytesReceived(self) -> UInt64: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
class IIPInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IIPInformation'
    _iid_ = Guid('{d85145e0-138f-47d7-9b3a-36bb488cef33}')
    @winrt_commethod(6)
    def get_NetworkAdapter(self) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(7)
    def get_PrefixLength(self) -> Windows.Foundation.IReference[Byte]: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    PrefixLength = property(get_PrefixLength, None)
class ILanIdentifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.ILanIdentifier'
    _iid_ = Guid('{48aa53aa-1108-4546-a6cb-9a74da4b7ba0}')
    @winrt_commethod(6)
    def get_InfrastructureId(self) -> Windows.Networking.Connectivity.LanIdentifierData: ...
    @winrt_commethod(7)
    def get_PortId(self) -> Windows.Networking.Connectivity.LanIdentifierData: ...
    @winrt_commethod(8)
    def get_NetworkAdapterId(self) -> Guid: ...
    InfrastructureId = property(get_InfrastructureId, None)
    PortId = property(get_PortId, None)
    NetworkAdapterId = property(get_NetworkAdapterId, None)
class ILanIdentifierData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.ILanIdentifierData'
    _iid_ = Guid('{a74e83c3-d639-45be-a36a-c4e4aeaf6d9b}')
    @winrt_commethod(6)
    def get_Type(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Foundation.Collections.IVectorView[Byte]: ...
    Type = property(get_Type, None)
    Value = property(get_Value, None)
class INetworkAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkAdapter'
    _iid_ = Guid('{3b542e03-5388-496c-a8a3-affd39aec2e6}')
    @winrt_commethod(6)
    def get_OutboundMaxBitsPerSecond(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_InboundMaxBitsPerSecond(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_IanaInterfaceType(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_NetworkItem(self) -> Windows.Networking.Connectivity.NetworkItem: ...
    @winrt_commethod(10)
    def get_NetworkAdapterId(self) -> Guid: ...
    @winrt_commethod(11)
    def GetConnectedProfileAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ConnectionProfile]: ...
    OutboundMaxBitsPerSecond = property(get_OutboundMaxBitsPerSecond, None)
    InboundMaxBitsPerSecond = property(get_InboundMaxBitsPerSecond, None)
    IanaInterfaceType = property(get_IanaInterfaceType, None)
    NetworkItem = property(get_NetworkItem, None)
    NetworkAdapterId = property(get_NetworkAdapterId, None)
class INetworkInformationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkInformationStatics'
    _iid_ = Guid('{5074f851-950d-4165-9c15-365619481eea}')
    @winrt_commethod(6)
    def GetConnectionProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectionProfile]: ...
    @winrt_commethod(7)
    def GetInternetConnectionProfile(self) -> Windows.Networking.Connectivity.ConnectionProfile: ...
    @winrt_commethod(8)
    def GetLanIdentifiers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.LanIdentifier]: ...
    @winrt_commethod(9)
    def GetHostNames(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    @winrt_commethod(10)
    def GetProxyConfigurationAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ProxyConfiguration]: ...
    @winrt_commethod(11)
    def GetSortedEndpointPairs(self, destinationList: Windows.Foundation.Collections.IIterable[Windows.Networking.EndpointPair], sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    @winrt_commethod(12)
    def add_NetworkStatusChanged(self, networkStatusHandler: Windows.Networking.Connectivity.NetworkStatusChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_NetworkStatusChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class INetworkInformationStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkInformationStatics2'
    _iid_ = Guid('{459ced14-2832-49b6-ba6e-e265f04786a8}')
    @winrt_commethod(6)
    def FindConnectionProfilesAsync(self, pProfileFilter: Windows.Networking.Connectivity.ConnectionProfileFilter) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectionProfile]]: ...
class INetworkItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkItem'
    _iid_ = Guid('{01bc4d39-f5e0-4567-a28c-42080c831b2b}')
    @winrt_commethod(6)
    def get_NetworkId(self) -> Guid: ...
    @winrt_commethod(7)
    def GetNetworkTypes(self) -> Windows.Networking.Connectivity.NetworkTypes: ...
    NetworkId = property(get_NetworkId, None)
class INetworkSecuritySettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkSecuritySettings'
    _iid_ = Guid('{7ca07e8d-917b-4b5f-b84d-28f7a5ac5402}')
    @winrt_commethod(6)
    def get_NetworkAuthenticationType(self) -> Windows.Networking.Connectivity.NetworkAuthenticationType: ...
    @winrt_commethod(7)
    def get_NetworkEncryptionType(self) -> Windows.Networking.Connectivity.NetworkEncryptionType: ...
    NetworkAuthenticationType = property(get_NetworkAuthenticationType, None)
    NetworkEncryptionType = property(get_NetworkEncryptionType, None)
class INetworkStateChangeEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkStateChangeEventDetails'
    _iid_ = Guid('{1f0cf333-d7a6-44dd-a4e9-687c476b903d}')
    @winrt_commethod(6)
    def get_HasNewInternetConnectionProfile(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HasNewConnectionCost(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_HasNewNetworkConnectivityLevel(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_HasNewDomainConnectivityLevel(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_HasNewHostNameList(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_HasNewWwanRegistrationState(self) -> Boolean: ...
    HasNewInternetConnectionProfile = property(get_HasNewInternetConnectionProfile, None)
    HasNewConnectionCost = property(get_HasNewConnectionCost, None)
    HasNewNetworkConnectivityLevel = property(get_HasNewNetworkConnectivityLevel, None)
    HasNewDomainConnectivityLevel = property(get_HasNewDomainConnectivityLevel, None)
    HasNewHostNameList = property(get_HasNewHostNameList, None)
    HasNewWwanRegistrationState = property(get_HasNewWwanRegistrationState, None)
class INetworkStateChangeEventDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkStateChangeEventDetails2'
    _iid_ = Guid('{d643c0e8-30d3-4f6a-ad47-6a1873ceb3c1}')
    @winrt_commethod(6)
    def get_HasNewTetheringOperationalState(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HasNewTetheringClientCount(self) -> Boolean: ...
    HasNewTetheringOperationalState = property(get_HasNewTetheringOperationalState, None)
    HasNewTetheringClientCount = property(get_HasNewTetheringClientCount, None)
class INetworkUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.INetworkUsage'
    _iid_ = Guid('{49da8fce-9985-4927-bf5b-072b5c65f8d9}')
    @winrt_commethod(6)
    def get_BytesSent(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_BytesReceived(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_ConnectionDuration(self) -> Windows.Foundation.TimeSpan: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
    ConnectionDuration = property(get_ConnectionDuration, None)
class IPInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IIPInformation
    _classid_ = 'Windows.Networking.Connectivity.IPInformation'
    @winrt_mixinmethod
    def get_NetworkAdapter(self: Windows.Networking.Connectivity.IIPInformation) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def get_PrefixLength(self: Windows.Networking.Connectivity.IIPInformation) -> Windows.Foundation.IReference[Byte]: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    PrefixLength = property(get_PrefixLength, None)
class IProviderNetworkUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IProviderNetworkUsage'
    _iid_ = Guid('{5ec69e04-7931-48c8-b8f3-46300fa42728}')
    @winrt_commethod(6)
    def get_BytesSent(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_BytesReceived(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_ProviderId(self) -> WinRT_String: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
    ProviderId = property(get_ProviderId, None)
class IProxyConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IProxyConfiguration'
    _iid_ = Guid('{ef3a60b4-9004-4dd6-b7d8-b3e502f4aad0}')
    @winrt_commethod(6)
    def get_ProxyUris(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def get_CanConnectDirectly(self) -> Boolean: ...
    ProxyUris = property(get_ProxyUris, None)
    CanConnectDirectly = property(get_CanConnectDirectly, None)
class IRoutePolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IRoutePolicy'
    _iid_ = Guid('{11abc4ac-0fc7-42e4-8742-569923b1ca11}')
    @winrt_commethod(6)
    def get_ConnectionProfile(self) -> Windows.Networking.Connectivity.ConnectionProfile: ...
    @winrt_commethod(7)
    def get_HostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def get_HostNameType(self) -> Windows.Networking.DomainNameType: ...
    ConnectionProfile = property(get_ConnectionProfile, None)
    HostName = property(get_HostName, None)
    HostNameType = property(get_HostNameType, None)
class IRoutePolicyFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IRoutePolicyFactory'
    _iid_ = Guid('{36027933-a18e-4db5-a697-f58fa7364e44}')
    @winrt_commethod(6)
    def CreateRoutePolicy(self, connectionProfile: Windows.Networking.Connectivity.ConnectionProfile, hostName: Windows.Networking.HostName, type: Windows.Networking.DomainNameType) -> Windows.Networking.Connectivity.RoutePolicy: ...
class IWlanConnectionProfileDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IWlanConnectionProfileDetails'
    _iid_ = Guid('{562098cb-b35a-4bf1-a884-b7557e88ff86}')
    @winrt_commethod(6)
    def GetConnectedSsid(self) -> WinRT_String: ...
class IWwanConnectionProfileDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IWwanConnectionProfileDetails'
    _iid_ = Guid('{0e4da8fe-835f-4df3-82fd-df556ebc09ef}')
    @winrt_commethod(6)
    def get_HomeProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AccessPointName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetNetworkRegistrationState(self) -> Windows.Networking.Connectivity.WwanNetworkRegistrationState: ...
    @winrt_commethod(9)
    def GetCurrentDataClass(self) -> Windows.Networking.Connectivity.WwanDataClass: ...
    HomeProviderId = property(get_HomeProviderId, None)
    AccessPointName = property(get_AccessPointName, None)
class IWwanConnectionProfileDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.IWwanConnectionProfileDetails2'
    _iid_ = Guid('{7a754ede-a1ed-48b2-8e92-b460033d52e2}')
    @winrt_commethod(6)
    def get_IPKind(self) -> Windows.Networking.Connectivity.WwanNetworkIPKind: ...
    @winrt_commethod(7)
    def get_PurposeGuids(self) -> Windows.Foundation.Collections.IVectorView[Guid]: ...
    IPKind = property(get_IPKind, None)
    PurposeGuids = property(get_PurposeGuids, None)
class LanIdentifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.ILanIdentifier
    _classid_ = 'Windows.Networking.Connectivity.LanIdentifier'
    @winrt_mixinmethod
    def get_InfrastructureId(self: Windows.Networking.Connectivity.ILanIdentifier) -> Windows.Networking.Connectivity.LanIdentifierData: ...
    @winrt_mixinmethod
    def get_PortId(self: Windows.Networking.Connectivity.ILanIdentifier) -> Windows.Networking.Connectivity.LanIdentifierData: ...
    @winrt_mixinmethod
    def get_NetworkAdapterId(self: Windows.Networking.Connectivity.ILanIdentifier) -> Guid: ...
    InfrastructureId = property(get_InfrastructureId, None)
    PortId = property(get_PortId, None)
    NetworkAdapterId = property(get_NetworkAdapterId, None)
class LanIdentifierData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.ILanIdentifierData
    _classid_ = 'Windows.Networking.Connectivity.LanIdentifierData'
    @winrt_mixinmethod
    def get_Type(self: Windows.Networking.Connectivity.ILanIdentifierData) -> UInt32: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Networking.Connectivity.ILanIdentifierData) -> Windows.Foundation.Collections.IVectorView[Byte]: ...
    Type = property(get_Type, None)
    Value = property(get_Value, None)
class NetworkAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.INetworkAdapter
    _classid_ = 'Windows.Networking.Connectivity.NetworkAdapter'
    @winrt_mixinmethod
    def get_OutboundMaxBitsPerSecond(self: Windows.Networking.Connectivity.INetworkAdapter) -> UInt64: ...
    @winrt_mixinmethod
    def get_InboundMaxBitsPerSecond(self: Windows.Networking.Connectivity.INetworkAdapter) -> UInt64: ...
    @winrt_mixinmethod
    def get_IanaInterfaceType(self: Windows.Networking.Connectivity.INetworkAdapter) -> UInt32: ...
    @winrt_mixinmethod
    def get_NetworkItem(self: Windows.Networking.Connectivity.INetworkAdapter) -> Windows.Networking.Connectivity.NetworkItem: ...
    @winrt_mixinmethod
    def get_NetworkAdapterId(self: Windows.Networking.Connectivity.INetworkAdapter) -> Guid: ...
    @winrt_mixinmethod
    def GetConnectedProfileAsync(self: Windows.Networking.Connectivity.INetworkAdapter) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ConnectionProfile]: ...
    OutboundMaxBitsPerSecond = property(get_OutboundMaxBitsPerSecond, None)
    InboundMaxBitsPerSecond = property(get_InboundMaxBitsPerSecond, None)
    IanaInterfaceType = property(get_IanaInterfaceType, None)
    NetworkItem = property(get_NetworkItem, None)
    NetworkAdapterId = property(get_NetworkAdapterId, None)
NetworkAuthenticationType = Int32
NetworkAuthenticationType_None: NetworkAuthenticationType = 0
NetworkAuthenticationType_Unknown: NetworkAuthenticationType = 1
NetworkAuthenticationType_Open80211: NetworkAuthenticationType = 2
NetworkAuthenticationType_SharedKey80211: NetworkAuthenticationType = 3
NetworkAuthenticationType_Wpa: NetworkAuthenticationType = 4
NetworkAuthenticationType_WpaPsk: NetworkAuthenticationType = 5
NetworkAuthenticationType_WpaNone: NetworkAuthenticationType = 6
NetworkAuthenticationType_Rsna: NetworkAuthenticationType = 7
NetworkAuthenticationType_RsnaPsk: NetworkAuthenticationType = 8
NetworkAuthenticationType_Ihv: NetworkAuthenticationType = 9
NetworkAuthenticationType_Wpa3: NetworkAuthenticationType = 10
NetworkAuthenticationType_Wpa3Enterprise192Bits: NetworkAuthenticationType = 10
NetworkAuthenticationType_Wpa3Sae: NetworkAuthenticationType = 11
NetworkAuthenticationType_Owe: NetworkAuthenticationType = 12
NetworkAuthenticationType_Wpa3Enterprise: NetworkAuthenticationType = 13
NetworkConnectivityLevel = Int32
NetworkConnectivityLevel_None: NetworkConnectivityLevel = 0
NetworkConnectivityLevel_LocalAccess: NetworkConnectivityLevel = 1
NetworkConnectivityLevel_ConstrainedInternetAccess: NetworkConnectivityLevel = 2
NetworkConnectivityLevel_InternetAccess: NetworkConnectivityLevel = 3
NetworkCostType = Int32
NetworkCostType_Unknown: NetworkCostType = 0
NetworkCostType_Unrestricted: NetworkCostType = 1
NetworkCostType_Fixed: NetworkCostType = 2
NetworkCostType_Variable: NetworkCostType = 3
NetworkEncryptionType = Int32
NetworkEncryptionType_None: NetworkEncryptionType = 0
NetworkEncryptionType_Unknown: NetworkEncryptionType = 1
NetworkEncryptionType_Wep: NetworkEncryptionType = 2
NetworkEncryptionType_Wep40: NetworkEncryptionType = 3
NetworkEncryptionType_Wep104: NetworkEncryptionType = 4
NetworkEncryptionType_Tkip: NetworkEncryptionType = 5
NetworkEncryptionType_Ccmp: NetworkEncryptionType = 6
NetworkEncryptionType_WpaUseGroup: NetworkEncryptionType = 7
NetworkEncryptionType_RsnUseGroup: NetworkEncryptionType = 8
NetworkEncryptionType_Ihv: NetworkEncryptionType = 9
NetworkEncryptionType_Gcmp: NetworkEncryptionType = 10
NetworkEncryptionType_Gcmp256: NetworkEncryptionType = 11
class NetworkInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Connectivity.NetworkInformation'
    @winrt_classmethod
    def FindConnectionProfilesAsync(cls: Windows.Networking.Connectivity.INetworkInformationStatics2, pProfileFilter: Windows.Networking.Connectivity.ConnectionProfileFilter) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectionProfile]]: ...
    @winrt_classmethod
    def GetConnectionProfiles(cls: Windows.Networking.Connectivity.INetworkInformationStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectionProfile]: ...
    @winrt_classmethod
    def GetInternetConnectionProfile(cls: Windows.Networking.Connectivity.INetworkInformationStatics) -> Windows.Networking.Connectivity.ConnectionProfile: ...
    @winrt_classmethod
    def GetLanIdentifiers(cls: Windows.Networking.Connectivity.INetworkInformationStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.LanIdentifier]: ...
    @winrt_classmethod
    def GetHostNames(cls: Windows.Networking.Connectivity.INetworkInformationStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    @winrt_classmethod
    def GetProxyConfigurationAsync(cls: Windows.Networking.Connectivity.INetworkInformationStatics, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Connectivity.ProxyConfiguration]: ...
    @winrt_classmethod
    def GetSortedEndpointPairs(cls: Windows.Networking.Connectivity.INetworkInformationStatics, destinationList: Windows.Foundation.Collections.IIterable[Windows.Networking.EndpointPair], sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    @winrt_classmethod
    def add_NetworkStatusChanged(cls: Windows.Networking.Connectivity.INetworkInformationStatics, networkStatusHandler: Windows.Networking.Connectivity.NetworkStatusChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_NetworkStatusChanged(cls: Windows.Networking.Connectivity.INetworkInformationStatics, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class NetworkItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.INetworkItem
    _classid_ = 'Windows.Networking.Connectivity.NetworkItem'
    @winrt_mixinmethod
    def get_NetworkId(self: Windows.Networking.Connectivity.INetworkItem) -> Guid: ...
    @winrt_mixinmethod
    def GetNetworkTypes(self: Windows.Networking.Connectivity.INetworkItem) -> Windows.Networking.Connectivity.NetworkTypes: ...
    NetworkId = property(get_NetworkId, None)
class NetworkSecuritySettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.INetworkSecuritySettings
    _classid_ = 'Windows.Networking.Connectivity.NetworkSecuritySettings'
    @winrt_mixinmethod
    def get_NetworkAuthenticationType(self: Windows.Networking.Connectivity.INetworkSecuritySettings) -> Windows.Networking.Connectivity.NetworkAuthenticationType: ...
    @winrt_mixinmethod
    def get_NetworkEncryptionType(self: Windows.Networking.Connectivity.INetworkSecuritySettings) -> Windows.Networking.Connectivity.NetworkEncryptionType: ...
    NetworkAuthenticationType = property(get_NetworkAuthenticationType, None)
    NetworkEncryptionType = property(get_NetworkEncryptionType, None)
class NetworkStateChangeEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.INetworkStateChangeEventDetails
    _classid_ = 'Windows.Networking.Connectivity.NetworkStateChangeEventDetails'
    @winrt_mixinmethod
    def get_HasNewInternetConnectionProfile(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNewConnectionCost(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNewNetworkConnectivityLevel(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNewDomainConnectivityLevel(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNewHostNameList(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNewWwanRegistrationState(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNewTetheringOperationalState(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNewTetheringClientCount(self: Windows.Networking.Connectivity.INetworkStateChangeEventDetails2) -> Boolean: ...
    HasNewInternetConnectionProfile = property(get_HasNewInternetConnectionProfile, None)
    HasNewConnectionCost = property(get_HasNewConnectionCost, None)
    HasNewNetworkConnectivityLevel = property(get_HasNewNetworkConnectivityLevel, None)
    HasNewDomainConnectivityLevel = property(get_HasNewDomainConnectivityLevel, None)
    HasNewHostNameList = property(get_HasNewHostNameList, None)
    HasNewWwanRegistrationState = property(get_HasNewWwanRegistrationState, None)
    HasNewTetheringOperationalState = property(get_HasNewTetheringOperationalState, None)
    HasNewTetheringClientCount = property(get_HasNewTetheringClientCount, None)
class NetworkStatusChangedEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.Networking.Connectivity.NetworkStatusChangedEventHandler'
    _iid_ = Guid('{71ba143f-598e-49d0-84eb-8febaedcc195}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
NetworkTypes = UInt32
NetworkTypes_None: NetworkTypes = 0
NetworkTypes_Internet: NetworkTypes = 1
NetworkTypes_PrivateNetwork: NetworkTypes = 2
class NetworkUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.INetworkUsage
    _classid_ = 'Windows.Networking.Connectivity.NetworkUsage'
    @winrt_mixinmethod
    def get_BytesSent(self: Windows.Networking.Connectivity.INetworkUsage) -> UInt64: ...
    @winrt_mixinmethod
    def get_BytesReceived(self: Windows.Networking.Connectivity.INetworkUsage) -> UInt64: ...
    @winrt_mixinmethod
    def get_ConnectionDuration(self: Windows.Networking.Connectivity.INetworkUsage) -> Windows.Foundation.TimeSpan: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
    ConnectionDuration = property(get_ConnectionDuration, None)
class NetworkUsageStates(EasyCastStructure):
    Roaming: Windows.Networking.Connectivity.TriStates
    Shared: Windows.Networking.Connectivity.TriStates
class ProviderNetworkUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IProviderNetworkUsage
    _classid_ = 'Windows.Networking.Connectivity.ProviderNetworkUsage'
    @winrt_mixinmethod
    def get_BytesSent(self: Windows.Networking.Connectivity.IProviderNetworkUsage) -> UInt64: ...
    @winrt_mixinmethod
    def get_BytesReceived(self: Windows.Networking.Connectivity.IProviderNetworkUsage) -> UInt64: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.Connectivity.IProviderNetworkUsage) -> WinRT_String: ...
    BytesSent = property(get_BytesSent, None)
    BytesReceived = property(get_BytesReceived, None)
    ProviderId = property(get_ProviderId, None)
class ProxyConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IProxyConfiguration
    _classid_ = 'Windows.Networking.Connectivity.ProxyConfiguration'
    @winrt_mixinmethod
    def get_ProxyUris(self: Windows.Networking.Connectivity.IProxyConfiguration) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_CanConnectDirectly(self: Windows.Networking.Connectivity.IProxyConfiguration) -> Boolean: ...
    ProxyUris = property(get_ProxyUris, None)
    CanConnectDirectly = property(get_CanConnectDirectly, None)
RoamingStates = UInt32
RoamingStates_None: RoamingStates = 0
RoamingStates_NotRoaming: RoamingStates = 1
RoamingStates_Roaming: RoamingStates = 2
class RoutePolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IRoutePolicy
    _classid_ = 'Windows.Networking.Connectivity.RoutePolicy'
    @winrt_factorymethod
    def CreateRoutePolicy(cls: Windows.Networking.Connectivity.IRoutePolicyFactory, connectionProfile: Windows.Networking.Connectivity.ConnectionProfile, hostName: Windows.Networking.HostName, type: Windows.Networking.DomainNameType) -> Windows.Networking.Connectivity.RoutePolicy: ...
    @winrt_mixinmethod
    def get_ConnectionProfile(self: Windows.Networking.Connectivity.IRoutePolicy) -> Windows.Networking.Connectivity.ConnectionProfile: ...
    @winrt_mixinmethod
    def get_HostName(self: Windows.Networking.Connectivity.IRoutePolicy) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_HostNameType(self: Windows.Networking.Connectivity.IRoutePolicy) -> Windows.Networking.DomainNameType: ...
    ConnectionProfile = property(get_ConnectionProfile, None)
    HostName = property(get_HostName, None)
    HostNameType = property(get_HostNameType, None)
TriStates = Int32
TriStates_DoNotCare: TriStates = 0
TriStates_No: TriStates = 1
TriStates_Yes: TriStates = 2
class WlanConnectionProfileDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IWlanConnectionProfileDetails
    _classid_ = 'Windows.Networking.Connectivity.WlanConnectionProfileDetails'
    @winrt_mixinmethod
    def GetConnectedSsid(self: Windows.Networking.Connectivity.IWlanConnectionProfileDetails) -> WinRT_String: ...
class WwanConnectionProfileDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Connectivity.IWwanConnectionProfileDetails
    _classid_ = 'Windows.Networking.Connectivity.WwanConnectionProfileDetails'
    @winrt_mixinmethod
    def get_HomeProviderId(self: Windows.Networking.Connectivity.IWwanConnectionProfileDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessPointName(self: Windows.Networking.Connectivity.IWwanConnectionProfileDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNetworkRegistrationState(self: Windows.Networking.Connectivity.IWwanConnectionProfileDetails) -> Windows.Networking.Connectivity.WwanNetworkRegistrationState: ...
    @winrt_mixinmethod
    def GetCurrentDataClass(self: Windows.Networking.Connectivity.IWwanConnectionProfileDetails) -> Windows.Networking.Connectivity.WwanDataClass: ...
    @winrt_mixinmethod
    def get_IPKind(self: Windows.Networking.Connectivity.IWwanConnectionProfileDetails2) -> Windows.Networking.Connectivity.WwanNetworkIPKind: ...
    @winrt_mixinmethod
    def get_PurposeGuids(self: Windows.Networking.Connectivity.IWwanConnectionProfileDetails2) -> Windows.Foundation.Collections.IVectorView[Guid]: ...
    HomeProviderId = property(get_HomeProviderId, None)
    AccessPointName = property(get_AccessPointName, None)
    IPKind = property(get_IPKind, None)
    PurposeGuids = property(get_PurposeGuids, None)
WwanContract: UInt32 = 131072
WwanDataClass = UInt32
WwanDataClass_None: WwanDataClass = 0
WwanDataClass_Gprs: WwanDataClass = 1
WwanDataClass_Edge: WwanDataClass = 2
WwanDataClass_Umts: WwanDataClass = 4
WwanDataClass_Hsdpa: WwanDataClass = 8
WwanDataClass_Hsupa: WwanDataClass = 16
WwanDataClass_LteAdvanced: WwanDataClass = 32
WwanDataClass_Cdma1xRtt: WwanDataClass = 65536
WwanDataClass_Cdma1xEvdo: WwanDataClass = 131072
WwanDataClass_Cdma1xEvdoRevA: WwanDataClass = 262144
WwanDataClass_Cdma1xEvdv: WwanDataClass = 524288
WwanDataClass_Cdma3xRtt: WwanDataClass = 1048576
WwanDataClass_Cdma1xEvdoRevB: WwanDataClass = 2097152
WwanDataClass_CdmaUmb: WwanDataClass = 4194304
WwanDataClass_Custom: WwanDataClass = 2147483648
WwanNetworkIPKind = Int32
WwanNetworkIPKind_None: WwanNetworkIPKind = 0
WwanNetworkIPKind_Ipv4: WwanNetworkIPKind = 1
WwanNetworkIPKind_Ipv6: WwanNetworkIPKind = 2
WwanNetworkIPKind_Ipv4v6: WwanNetworkIPKind = 3
WwanNetworkIPKind_Ipv4v6v4Xlat: WwanNetworkIPKind = 4
WwanNetworkRegistrationState = Int32
WwanNetworkRegistrationState_None: WwanNetworkRegistrationState = 0
WwanNetworkRegistrationState_Deregistered: WwanNetworkRegistrationState = 1
WwanNetworkRegistrationState_Searching: WwanNetworkRegistrationState = 2
WwanNetworkRegistrationState_Home: WwanNetworkRegistrationState = 3
WwanNetworkRegistrationState_Roaming: WwanNetworkRegistrationState = 4
WwanNetworkRegistrationState_Partner: WwanNetworkRegistrationState = 5
WwanNetworkRegistrationState_Denied: WwanNetworkRegistrationState = 6
make_head(_module, 'AttributedNetworkUsage')
make_head(_module, 'CellularApnContext')
make_head(_module, 'ConnectionCost')
make_head(_module, 'ConnectionProfile')
make_head(_module, 'ConnectionProfileFilter')
make_head(_module, 'ConnectionSession')
make_head(_module, 'ConnectivityInterval')
make_head(_module, 'ConnectivityManager')
make_head(_module, 'DataPlanStatus')
make_head(_module, 'DataPlanUsage')
make_head(_module, 'DataUsage')
make_head(_module, 'IAttributedNetworkUsage')
make_head(_module, 'ICellularApnContext')
make_head(_module, 'ICellularApnContext2')
make_head(_module, 'IConnectionCost')
make_head(_module, 'IConnectionCost2')
make_head(_module, 'IConnectionProfile')
make_head(_module, 'IConnectionProfile2')
make_head(_module, 'IConnectionProfile3')
make_head(_module, 'IConnectionProfile4')
make_head(_module, 'IConnectionProfile5')
make_head(_module, 'IConnectionProfile6')
make_head(_module, 'IConnectionProfileFilter')
make_head(_module, 'IConnectionProfileFilter2')
make_head(_module, 'IConnectionProfileFilter3')
make_head(_module, 'IConnectionSession')
make_head(_module, 'IConnectivityInterval')
make_head(_module, 'IConnectivityManagerStatics')
make_head(_module, 'IDataPlanStatus')
make_head(_module, 'IDataPlanUsage')
make_head(_module, 'IDataUsage')
make_head(_module, 'IIPInformation')
make_head(_module, 'ILanIdentifier')
make_head(_module, 'ILanIdentifierData')
make_head(_module, 'INetworkAdapter')
make_head(_module, 'INetworkInformationStatics')
make_head(_module, 'INetworkInformationStatics2')
make_head(_module, 'INetworkItem')
make_head(_module, 'INetworkSecuritySettings')
make_head(_module, 'INetworkStateChangeEventDetails')
make_head(_module, 'INetworkStateChangeEventDetails2')
make_head(_module, 'INetworkUsage')
make_head(_module, 'IPInformation')
make_head(_module, 'IProviderNetworkUsage')
make_head(_module, 'IProxyConfiguration')
make_head(_module, 'IRoutePolicy')
make_head(_module, 'IRoutePolicyFactory')
make_head(_module, 'IWlanConnectionProfileDetails')
make_head(_module, 'IWwanConnectionProfileDetails')
make_head(_module, 'IWwanConnectionProfileDetails2')
make_head(_module, 'LanIdentifier')
make_head(_module, 'LanIdentifierData')
make_head(_module, 'NetworkAdapter')
make_head(_module, 'NetworkInformation')
make_head(_module, 'NetworkItem')
make_head(_module, 'NetworkSecuritySettings')
make_head(_module, 'NetworkStateChangeEventDetails')
make_head(_module, 'NetworkStatusChangedEventHandler')
make_head(_module, 'NetworkUsage')
make_head(_module, 'NetworkUsageStates')
make_head(_module, 'ProviderNetworkUsage')
make_head(_module, 'ProxyConfiguration')
make_head(_module, 'RoutePolicy')
make_head(_module, 'WlanConnectionProfileDetails')
make_head(_module, 'WwanConnectionProfileDetails')
