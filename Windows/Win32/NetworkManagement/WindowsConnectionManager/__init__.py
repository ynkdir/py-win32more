from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.WindowsConnectionManager
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
WCM_API_VERSION_1_0: UInt32 = 1
WCM_API_VERSION: UInt32 = 1
WCM_UNKNOWN_DATAPLAN_STATUS: UInt32 = 4294967295
WCM_MAX_PROFILE_NAME: UInt32 = 256
NET_INTERFACE_FLAG_NONE: UInt32 = 0
NET_INTERFACE_FLAG_CONNECT_IF_NEEDED: UInt32 = 1
@winfunctype('wcmapi.dll')
def WcmQueryProperty(pInterface: POINTER(Guid), strProfileName: Windows.Win32.Foundation.PWSTR, Property: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY, pReserved: c_void_p, pdwDataSize: POINTER(UInt32), ppData: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmSetProperty(pInterface: POINTER(Guid), strProfileName: Windows.Win32.Foundation.PWSTR, Property: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY, pReserved: c_void_p, dwDataSize: UInt32, pbData: c_char_p_no) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmGetProfileList(pReserved: c_void_p, ppProfileList: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST_head))) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmSetProfileList(pProfileList: POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST_head), dwPosition: UInt32, fIgnoreUnknownProfiles: Windows.Win32.Foundation.BOOL, pReserved: c_void_p) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmFreeMemory(pMemory: c_void_p) -> Void: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandGetRoutingHint(destinationHostName: Windows.Win32.Foundation.PWSTR, interfaceIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandRegisterNotification(callback: Windows.Win32.NetworkManagement.WindowsConnectionManager.ONDEMAND_NOTIFICATION_CALLBACK, callbackContext: c_void_p, registrationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandUnRegisterNotification(registrationHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def GetInterfaceContextTableForHostName(HostName: Windows.Win32.Foundation.PWSTR, ProxyName: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ConnectionProfileFilterRawData: c_char_p_no, ConnectionProfileFilterRawDataSize: UInt32, InterfaceContextTable: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def FreeInterfaceContextTable(InterfaceContextTable: POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE_head)) -> Void: ...
class NET_INTERFACE_CONTEXT(Structure):
    InterfaceIndex: UInt32
    ConfigurationName: Windows.Win32.Foundation.PWSTR
class NET_INTERFACE_CONTEXT_TABLE(Structure):
    InterfaceContextHandle: Windows.Win32.Foundation.HANDLE
    NumberOfEntries: UInt32
    InterfaceContextArray: POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_head)
@winfunctype_pointer
def ONDEMAND_NOTIFICATION_CALLBACK(param0: c_void_p) -> Void: ...
class WCM_BILLING_CYCLE_INFO(Structure):
    StartDate: Windows.Win32.Foundation.FILETIME
    Duration: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_TIME_INTERVAL
    Reset: Windows.Win32.Foundation.BOOL
WCM_CONNECTION_COST = Int32
WCM_CONNECTION_COST_UNKNOWN: WCM_CONNECTION_COST = 0
WCM_CONNECTION_COST_UNRESTRICTED: WCM_CONNECTION_COST = 1
WCM_CONNECTION_COST_FIXED: WCM_CONNECTION_COST = 2
WCM_CONNECTION_COST_VARIABLE: WCM_CONNECTION_COST = 4
WCM_CONNECTION_COST_OVERDATALIMIT: WCM_CONNECTION_COST = 65536
WCM_CONNECTION_COST_CONGESTED: WCM_CONNECTION_COST = 131072
WCM_CONNECTION_COST_ROAMING: WCM_CONNECTION_COST = 262144
WCM_CONNECTION_COST_APPROACHINGDATALIMIT: WCM_CONNECTION_COST = 524288
class WCM_CONNECTION_COST_DATA(Structure):
    ConnectionCost: UInt32
    CostSource: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE
WCM_CONNECTION_COST_SOURCE = Int32
WCM_CONNECTION_COST_SOURCE_DEFAULT: WCM_CONNECTION_COST_SOURCE = 0
WCM_CONNECTION_COST_SOURCE_GP: WCM_CONNECTION_COST_SOURCE = 1
WCM_CONNECTION_COST_SOURCE_USER: WCM_CONNECTION_COST_SOURCE = 2
WCM_CONNECTION_COST_SOURCE_OPERATOR: WCM_CONNECTION_COST_SOURCE = 3
class WCM_DATAPLAN_STATUS(Structure):
    UsageData: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_USAGE_DATA
    DataLimitInMegabytes: UInt32
    InboundBandwidthInKbps: UInt32
    OutboundBandwidthInKbps: UInt32
    BillingCycle: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_BILLING_CYCLE_INFO
    MaxTransferSizeInMegabytes: UInt32
    Reserved: UInt32
WCM_MEDIA_TYPE = Int32
wcm_media_unknown: WCM_MEDIA_TYPE = 0
wcm_media_ethernet: WCM_MEDIA_TYPE = 1
wcm_media_wlan: WCM_MEDIA_TYPE = 2
wcm_media_mbn: WCM_MEDIA_TYPE = 3
wcm_media_invalid: WCM_MEDIA_TYPE = 4
wcm_media_max: WCM_MEDIA_TYPE = 5
class WCM_POLICY_VALUE(Structure):
    fValue: Windows.Win32.Foundation.BOOL
    fIsGroupPolicy: Windows.Win32.Foundation.BOOL
class WCM_PROFILE_INFO(Structure):
    strProfileName: Char * 256
    AdapterGUID: Guid
    Media: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE
class WCM_PROFILE_INFO_LIST(Structure):
    dwNumberOfItems: UInt32
    ProfileInfo: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO * 1
WCM_PROPERTY = Int32
wcm_global_property_domain_policy: WCM_PROPERTY = 0
wcm_global_property_minimize_policy: WCM_PROPERTY = 1
wcm_global_property_roaming_policy: WCM_PROPERTY = 2
wcm_global_property_powermanagement_policy: WCM_PROPERTY = 3
wcm_intf_property_connection_cost: WCM_PROPERTY = 4
wcm_intf_property_dataplan_status: WCM_PROPERTY = 5
wcm_intf_property_hotspot_profile: WCM_PROPERTY = 6
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
    LastSyncTime: Windows.Win32.Foundation.FILETIME
make_head(_module, 'NET_INTERFACE_CONTEXT')
make_head(_module, 'NET_INTERFACE_CONTEXT_TABLE')
make_head(_module, 'ONDEMAND_NOTIFICATION_CALLBACK')
make_head(_module, 'WCM_BILLING_CYCLE_INFO')
make_head(_module, 'WCM_CONNECTION_COST_DATA')
make_head(_module, 'WCM_DATAPLAN_STATUS')
make_head(_module, 'WCM_POLICY_VALUE')
make_head(_module, 'WCM_PROFILE_INFO')
make_head(_module, 'WCM_PROFILE_INFO_LIST')
make_head(_module, 'WCM_TIME_INTERVAL')
make_head(_module, 'WCM_USAGE_DATA')
__all__ = [
    "FreeInterfaceContextTable",
    "GetInterfaceContextTableForHostName",
    "NET_INTERFACE_CONTEXT",
    "NET_INTERFACE_CONTEXT_TABLE",
    "NET_INTERFACE_FLAG_CONNECT_IF_NEEDED",
    "NET_INTERFACE_FLAG_NONE",
    "ONDEMAND_NOTIFICATION_CALLBACK",
    "OnDemandGetRoutingHint",
    "OnDemandRegisterNotification",
    "OnDemandUnRegisterNotification",
    "WCM_API_VERSION",
    "WCM_API_VERSION_1_0",
    "WCM_BILLING_CYCLE_INFO",
    "WCM_CONNECTION_COST",
    "WCM_CONNECTION_COST_APPROACHINGDATALIMIT",
    "WCM_CONNECTION_COST_CONGESTED",
    "WCM_CONNECTION_COST_DATA",
    "WCM_CONNECTION_COST_FIXED",
    "WCM_CONNECTION_COST_OVERDATALIMIT",
    "WCM_CONNECTION_COST_ROAMING",
    "WCM_CONNECTION_COST_SOURCE",
    "WCM_CONNECTION_COST_SOURCE_DEFAULT",
    "WCM_CONNECTION_COST_SOURCE_GP",
    "WCM_CONNECTION_COST_SOURCE_OPERATOR",
    "WCM_CONNECTION_COST_SOURCE_USER",
    "WCM_CONNECTION_COST_UNKNOWN",
    "WCM_CONNECTION_COST_UNRESTRICTED",
    "WCM_CONNECTION_COST_VARIABLE",
    "WCM_DATAPLAN_STATUS",
    "WCM_MAX_PROFILE_NAME",
    "WCM_MEDIA_TYPE",
    "WCM_POLICY_VALUE",
    "WCM_PROFILE_INFO",
    "WCM_PROFILE_INFO_LIST",
    "WCM_PROPERTY",
    "WCM_TIME_INTERVAL",
    "WCM_UNKNOWN_DATAPLAN_STATUS",
    "WCM_USAGE_DATA",
    "WcmFreeMemory",
    "WcmGetProfileList",
    "WcmQueryProperty",
    "WcmSetProfileList",
    "WcmSetProperty",
    "wcm_global_property_domain_policy",
    "wcm_global_property_minimize_policy",
    "wcm_global_property_powermanagement_policy",
    "wcm_global_property_roaming_policy",
    "wcm_intf_property_connection_cost",
    "wcm_intf_property_dataplan_status",
    "wcm_intf_property_hotspot_profile",
    "wcm_media_ethernet",
    "wcm_media_invalid",
    "wcm_media_max",
    "wcm_media_mbn",
    "wcm_media_unknown",
    "wcm_media_wlan",
]
_arch_optional = [
]
