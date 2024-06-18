from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager
WCM_API_VERSION_1_0: UInt32 = 1
WCM_API_VERSION: UInt32 = 1
WCM_UNKNOWN_DATAPLAN_STATUS: UInt32 = 4294967295
WCM_MAX_PROFILE_NAME: UInt32 = 256
NET_INTERFACE_FLAG_NONE: UInt32 = 0
NET_INTERFACE_FLAG_CONNECT_IF_NEEDED: UInt32 = 1
@winfunctype('wcmapi.dll')
def WcmQueryProperty(pInterface: POINTER(Guid), strProfileName: win32more.Windows.Win32.Foundation.PWSTR, Property: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY, pReserved: VoidPtr, pdwDataSize: POINTER(UInt32), ppData: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmSetProperty(pInterface: POINTER(Guid), strProfileName: win32more.Windows.Win32.Foundation.PWSTR, Property: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY, pReserved: VoidPtr, dwDataSize: UInt32, pbData: POINTER(Byte)) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmGetProfileList(pReserved: VoidPtr, ppProfileList: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST))) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmSetProfileList(pProfileList: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST), dwPosition: UInt32, fIgnoreUnknownProfiles: win32more.Windows.Win32.Foundation.BOOL, pReserved: VoidPtr) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmFreeMemory(pMemory: VoidPtr) -> Void: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandGetRoutingHint(destinationHostName: win32more.Windows.Win32.Foundation.PWSTR, interfaceIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandRegisterNotification(callback: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.ONDEMAND_NOTIFICATION_CALLBACK, callbackContext: VoidPtr, registrationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandUnRegisterNotification(registrationHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def GetInterfaceContextTableForHostName(HostName: win32more.Windows.Win32.Foundation.PWSTR, ProxyName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, ConnectionProfileFilterRawData: POINTER(Byte), ConnectionProfileFilterRawDataSize: UInt32, InterfaceContextTable: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def FreeInterfaceContextTable(InterfaceContextTable: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE)) -> Void: ...
class NET_INTERFACE_CONTEXT(Structure):
    InterfaceIndex: UInt32
    ConfigurationName: win32more.Windows.Win32.Foundation.PWSTR
class NET_INTERFACE_CONTEXT_TABLE(Structure):
    InterfaceContextHandle: win32more.Windows.Win32.Foundation.HANDLE
    NumberOfEntries: UInt32
    InterfaceContextArray: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT)
@winfunctype_pointer
def ONDEMAND_NOTIFICATION_CALLBACK(param0: VoidPtr) -> Void: ...
class WCM_BILLING_CYCLE_INFO(Structure):
    StartDate: win32more.Windows.Win32.Foundation.FILETIME
    Duration: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_TIME_INTERVAL
    Reset: win32more.Windows.Win32.Foundation.BOOL
WCM_CONNECTION_COST = Int32
WCM_CONNECTION_COST_UNKNOWN: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 0
WCM_CONNECTION_COST_UNRESTRICTED: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 1
WCM_CONNECTION_COST_FIXED: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 2
WCM_CONNECTION_COST_VARIABLE: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 4
WCM_CONNECTION_COST_OVERDATALIMIT: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 65536
WCM_CONNECTION_COST_CONGESTED: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 131072
WCM_CONNECTION_COST_ROAMING: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 262144
WCM_CONNECTION_COST_APPROACHINGDATALIMIT: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST = 524288
class WCM_CONNECTION_COST_DATA(Structure):
    ConnectionCost: UInt32
    CostSource: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE
WCM_CONNECTION_COST_SOURCE = Int32
WCM_CONNECTION_COST_SOURCE_DEFAULT: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE = 0
WCM_CONNECTION_COST_SOURCE_GP: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE = 1
WCM_CONNECTION_COST_SOURCE_USER: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE = 2
WCM_CONNECTION_COST_SOURCE_OPERATOR: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE = 3
class WCM_DATAPLAN_STATUS(Structure):
    UsageData: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_USAGE_DATA
    DataLimitInMegabytes: UInt32
    InboundBandwidthInKbps: UInt32
    OutboundBandwidthInKbps: UInt32
    BillingCycle: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_BILLING_CYCLE_INFO
    MaxTransferSizeInMegabytes: UInt32
    Reserved: UInt32
WCM_MEDIA_TYPE = Int32
wcm_media_unknown: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE = 0
wcm_media_ethernet: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE = 1
wcm_media_wlan: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE = 2
wcm_media_mbn: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE = 3
wcm_media_invalid: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE = 4
wcm_media_max: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE = 5
class WCM_POLICY_VALUE(Structure):
    fValue: win32more.Windows.Win32.Foundation.BOOL
    fIsGroupPolicy: win32more.Windows.Win32.Foundation.BOOL
class WCM_PROFILE_INFO(Structure):
    strProfileName: Char * 256
    AdapterGUID: Guid
    Media: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE
class WCM_PROFILE_INFO_LIST(Structure):
    dwNumberOfItems: UInt32
    ProfileInfo: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO * 1
WCM_PROPERTY = Int32
wcm_global_property_domain_policy: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY = 0
wcm_global_property_minimize_policy: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY = 1
wcm_global_property_roaming_policy: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY = 2
wcm_global_property_powermanagement_policy: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY = 3
wcm_intf_property_connection_cost: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY = 4
wcm_intf_property_dataplan_status: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY = 5
wcm_intf_property_hotspot_profile: win32more.Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY = 6
class WCM_TIME_INTERVAL(Structure):
    wYear: UInt16
    wMonth: UInt16
    wDay: UInt16
    wHour: UInt16
    wMinute: UInt16
    wSecond: UInt16
    wMilliseconds: UInt16
class WCM_USAGE_DATA(Structure):
    UsageInMegabytes: UInt32
    LastSyncTime: win32more.Windows.Win32.Foundation.FILETIME


make_ready(__name__)
