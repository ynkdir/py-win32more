from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.NetworkManagement.WindowsConnectionManager
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WCM_API_VERSION_1_0 = 1
WCM_API_VERSION = 1
WCM_UNKNOWN_DATAPLAN_STATUS = 4294967295
WCM_MAX_PROFILE_NAME = 256
NET_INTERFACE_FLAG_NONE = 0
NET_INTERFACE_FLAG_CONNECT_IF_NEEDED = 1
def _define_WcmQueryProperty():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),win32more.Foundation.PWSTR,win32more.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY,c_void_p,POINTER(UInt32),POINTER(c_char_p_no))(('WcmQueryProperty', windll['wcmapi.dll']), ((1, 'pInterface'),(1, 'strProfileName'),(1, 'Property'),(1, 'pReserved'),(1, 'pdwDataSize'),(1, 'ppData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcmSetProperty():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),win32more.Foundation.PWSTR,win32more.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY,c_void_p,UInt32,c_char_p_no)(('WcmSetProperty', windll['wcmapi.dll']), ((1, 'pInterface'),(1, 'strProfileName'),(1, 'Property'),(1, 'pReserved'),(1, 'dwDataSize'),(1, 'pbData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcmGetProfileList():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(POINTER(win32more.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST_head)))(('WcmGetProfileList', windll['wcmapi.dll']), ((1, 'pReserved'),(1, 'ppProfileList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcmSetProfileList():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST_head),UInt32,win32more.Foundation.BOOL,c_void_p)(('WcmSetProfileList', windll['wcmapi.dll']), ((1, 'pProfileList'),(1, 'dwPosition'),(1, 'fIgnoreUnknownProfiles'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcmFreeMemory():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('WcmFreeMemory', windll['wcmapi.dll']), ((1, 'pMemory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OnDemandGetRoutingHint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32))(('OnDemandGetRoutingHint', windll['OnDemandConnRouteHelper.dll']), ((1, 'destinationHostName'),(1, 'interfaceIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OnDemandRegisterNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsConnectionManager.ONDEMAND_NOTIFICATION_CALLBACK,c_void_p,POINTER(win32more.Foundation.HANDLE))(('OnDemandRegisterNotification', windll['OnDemandConnRouteHelper.dll']), ((1, 'callback'),(1, 'callbackContext'),(1, 'registrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OnDemandUnRegisterNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('OnDemandUnRegisterNotification', windll['OnDemandConnRouteHelper.dll']), ((1, 'registrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInterfaceContextTableForHostName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,UInt32,POINTER(POINTER(win32more.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE_head)))(('GetInterfaceContextTableForHostName', windll['OnDemandConnRouteHelper.dll']), ((1, 'HostName'),(1, 'ProxyName'),(1, 'Flags'),(1, 'ConnectionProfileFilterRawData'),(1, 'ConnectionProfileFilterRawDataSize'),(1, 'InterfaceContextTable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeInterfaceContextTable():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE_head))(('FreeInterfaceContextTable', windll['OnDemandConnRouteHelper.dll']), ((1, 'InterfaceContextTable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NET_INTERFACE_CONTEXT_head():
    class NET_INTERFACE_CONTEXT(Structure):
        pass
    return NET_INTERFACE_CONTEXT
def _define_NET_INTERFACE_CONTEXT():
    NET_INTERFACE_CONTEXT = win32more.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_head
    NET_INTERFACE_CONTEXT._fields_ = [
        ('InterfaceIndex', UInt32),
        ('ConfigurationName', win32more.Foundation.PWSTR),
    ]
    return NET_INTERFACE_CONTEXT
def _define_NET_INTERFACE_CONTEXT_TABLE_head():
    class NET_INTERFACE_CONTEXT_TABLE(Structure):
        pass
    return NET_INTERFACE_CONTEXT_TABLE
def _define_NET_INTERFACE_CONTEXT_TABLE():
    NET_INTERFACE_CONTEXT_TABLE = win32more.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE_head
    NET_INTERFACE_CONTEXT_TABLE._fields_ = [
        ('InterfaceContextHandle', win32more.Foundation.HANDLE),
        ('NumberOfEntries', UInt32),
        ('InterfaceContextArray', POINTER(win32more.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_head)),
    ]
    return NET_INTERFACE_CONTEXT_TABLE
def _define_ONDEMAND_NOTIFICATION_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
def _define_WCM_BILLING_CYCLE_INFO_head():
    class WCM_BILLING_CYCLE_INFO(Structure):
        pass
    return WCM_BILLING_CYCLE_INFO
def _define_WCM_BILLING_CYCLE_INFO():
    WCM_BILLING_CYCLE_INFO = win32more.NetworkManagement.WindowsConnectionManager.WCM_BILLING_CYCLE_INFO_head
    WCM_BILLING_CYCLE_INFO._fields_ = [
        ('StartDate', win32more.Foundation.FILETIME),
        ('Duration', win32more.NetworkManagement.WindowsConnectionManager.WCM_TIME_INTERVAL),
        ('Reset', win32more.Foundation.BOOL),
    ]
    return WCM_BILLING_CYCLE_INFO
WCM_CONNECTION_COST = Int32
WCM_CONNECTION_COST_UNKNOWN = 0
WCM_CONNECTION_COST_UNRESTRICTED = 1
WCM_CONNECTION_COST_FIXED = 2
WCM_CONNECTION_COST_VARIABLE = 4
WCM_CONNECTION_COST_OVERDATALIMIT = 65536
WCM_CONNECTION_COST_CONGESTED = 131072
WCM_CONNECTION_COST_ROAMING = 262144
WCM_CONNECTION_COST_APPROACHINGDATALIMIT = 524288
def _define_WCM_CONNECTION_COST_DATA_head():
    class WCM_CONNECTION_COST_DATA(Structure):
        pass
    return WCM_CONNECTION_COST_DATA
def _define_WCM_CONNECTION_COST_DATA():
    WCM_CONNECTION_COST_DATA = win32more.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_DATA_head
    WCM_CONNECTION_COST_DATA._fields_ = [
        ('ConnectionCost', UInt32),
        ('CostSource', win32more.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE),
    ]
    return WCM_CONNECTION_COST_DATA
WCM_CONNECTION_COST_SOURCE = Int32
WCM_CONNECTION_COST_SOURCE_DEFAULT = 0
WCM_CONNECTION_COST_SOURCE_GP = 1
WCM_CONNECTION_COST_SOURCE_USER = 2
WCM_CONNECTION_COST_SOURCE_OPERATOR = 3
def _define_WCM_DATAPLAN_STATUS_head():
    class WCM_DATAPLAN_STATUS(Structure):
        pass
    return WCM_DATAPLAN_STATUS
def _define_WCM_DATAPLAN_STATUS():
    WCM_DATAPLAN_STATUS = win32more.NetworkManagement.WindowsConnectionManager.WCM_DATAPLAN_STATUS_head
    WCM_DATAPLAN_STATUS._fields_ = [
        ('UsageData', win32more.NetworkManagement.WindowsConnectionManager.WCM_USAGE_DATA),
        ('DataLimitInMegabytes', UInt32),
        ('InboundBandwidthInKbps', UInt32),
        ('OutboundBandwidthInKbps', UInt32),
        ('BillingCycle', win32more.NetworkManagement.WindowsConnectionManager.WCM_BILLING_CYCLE_INFO),
        ('MaxTransferSizeInMegabytes', UInt32),
        ('Reserved', UInt32),
    ]
    return WCM_DATAPLAN_STATUS
WCM_MEDIA_TYPE = Int32
wcm_media_unknown = 0
wcm_media_ethernet = 1
wcm_media_wlan = 2
wcm_media_mbn = 3
wcm_media_invalid = 4
wcm_media_max = 5
def _define_WCM_POLICY_VALUE_head():
    class WCM_POLICY_VALUE(Structure):
        pass
    return WCM_POLICY_VALUE
def _define_WCM_POLICY_VALUE():
    WCM_POLICY_VALUE = win32more.NetworkManagement.WindowsConnectionManager.WCM_POLICY_VALUE_head
    WCM_POLICY_VALUE._fields_ = [
        ('fValue', win32more.Foundation.BOOL),
        ('fIsGroupPolicy', win32more.Foundation.BOOL),
    ]
    return WCM_POLICY_VALUE
def _define_WCM_PROFILE_INFO_head():
    class WCM_PROFILE_INFO(Structure):
        pass
    return WCM_PROFILE_INFO
def _define_WCM_PROFILE_INFO():
    WCM_PROFILE_INFO = win32more.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_head
    WCM_PROFILE_INFO._fields_ = [
        ('strProfileName', Char * 256),
        ('AdapterGUID', Guid),
        ('Media', win32more.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE),
    ]
    return WCM_PROFILE_INFO
def _define_WCM_PROFILE_INFO_LIST_head():
    class WCM_PROFILE_INFO_LIST(Structure):
        pass
    return WCM_PROFILE_INFO_LIST
def _define_WCM_PROFILE_INFO_LIST():
    WCM_PROFILE_INFO_LIST = win32more.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST_head
    WCM_PROFILE_INFO_LIST._fields_ = [
        ('dwNumberOfItems', UInt32),
        ('ProfileInfo', win32more.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO * 1),
    ]
    return WCM_PROFILE_INFO_LIST
WCM_PROPERTY = Int32
wcm_global_property_domain_policy = 0
wcm_global_property_minimize_policy = 1
wcm_global_property_roaming_policy = 2
wcm_global_property_powermanagement_policy = 3
wcm_intf_property_connection_cost = 4
wcm_intf_property_dataplan_status = 5
wcm_intf_property_hotspot_profile = 6
def _define_WCM_TIME_INTERVAL_head():
    class WCM_TIME_INTERVAL(Structure):
        pass
    return WCM_TIME_INTERVAL
def _define_WCM_TIME_INTERVAL():
    WCM_TIME_INTERVAL = win32more.NetworkManagement.WindowsConnectionManager.WCM_TIME_INTERVAL_head
    WCM_TIME_INTERVAL._fields_ = [
        ('wYear', UInt16),
        ('wMonth', UInt16),
        ('wDay', UInt16),
        ('wHour', UInt16),
        ('wMinute', UInt16),
        ('wSecond', UInt16),
        ('wMilliseconds', UInt16),
    ]
    return WCM_TIME_INTERVAL
def _define_WCM_USAGE_DATA_head():
    class WCM_USAGE_DATA(Structure):
        pass
    return WCM_USAGE_DATA
def _define_WCM_USAGE_DATA():
    WCM_USAGE_DATA = win32more.NetworkManagement.WindowsConnectionManager.WCM_USAGE_DATA_head
    WCM_USAGE_DATA._fields_ = [
        ('UsageInMegabytes', UInt32),
        ('LastSyncTime', win32more.Foundation.FILETIME),
    ]
    return WCM_USAGE_DATA
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
