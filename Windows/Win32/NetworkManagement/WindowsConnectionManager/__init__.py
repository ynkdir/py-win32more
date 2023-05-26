from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.WindowsConnectionManager
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WCM_API_VERSION_1_0: UInt32 = 1
WCM_API_VERSION: UInt32 = 1
WCM_UNKNOWN_DATAPLAN_STATUS: UInt32 = 4294967295
WCM_MAX_PROFILE_NAME: UInt32 = 256
NET_INTERFACE_FLAG_NONE: UInt32 = 0
NET_INTERFACE_FLAG_CONNECT_IF_NEEDED: UInt32 = 1
@winfunctype('wcmapi.dll')
def WcmQueryProperty(pInterface: POINTER(Guid), strProfileName: Windows.Win32.Foundation.PWSTR, Property: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY, pReserved: VoidPtr, pdwDataSize: POINTER(UInt32), ppData: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmSetProperty(pInterface: POINTER(Guid), strProfileName: Windows.Win32.Foundation.PWSTR, Property: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROPERTY, pReserved: VoidPtr, dwDataSize: UInt32, pbData: POINTER(Byte)) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmGetProfileList(pReserved: VoidPtr, ppProfileList: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST_head))) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmSetProfileList(pProfileList: POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_PROFILE_INFO_LIST_head), dwPosition: UInt32, fIgnoreUnknownProfiles: Windows.Win32.Foundation.BOOL, pReserved: VoidPtr) -> UInt32: ...
@winfunctype('wcmapi.dll')
def WcmFreeMemory(pMemory: VoidPtr) -> Void: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandGetRoutingHint(destinationHostName: Windows.Win32.Foundation.PWSTR, interfaceIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandRegisterNotification(callback: Windows.Win32.NetworkManagement.WindowsConnectionManager.ONDEMAND_NOTIFICATION_CALLBACK, callbackContext: VoidPtr, registrationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def OnDemandUnRegisterNotification(registrationHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def GetInterfaceContextTableForHostName(HostName: Windows.Win32.Foundation.PWSTR, ProxyName: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ConnectionProfileFilterRawData: POINTER(Byte), ConnectionProfileFilterRawDataSize: UInt32, InterfaceContextTable: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OnDemandConnRouteHelper.dll')
def FreeInterfaceContextTable(InterfaceContextTable: POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_TABLE_head)) -> Void: ...
class NET_INTERFACE_CONTEXT(EasyCastStructure):
    InterfaceIndex: UInt32
    ConfigurationName: Windows.Win32.Foundation.PWSTR
class NET_INTERFACE_CONTEXT_TABLE(EasyCastStructure):
    InterfaceContextHandle: Windows.Win32.Foundation.HANDLE
    NumberOfEntries: UInt32
    InterfaceContextArray: POINTER(Windows.Win32.NetworkManagement.WindowsConnectionManager.NET_INTERFACE_CONTEXT_head)
@winfunctype_pointer
def ONDEMAND_NOTIFICATION_CALLBACK(param0: VoidPtr) -> Void: ...
class WCM_BILLING_CYCLE_INFO(EasyCastStructure):
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
class WCM_CONNECTION_COST_DATA(EasyCastStructure):
    ConnectionCost: UInt32
    CostSource: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_CONNECTION_COST_SOURCE
WCM_CONNECTION_COST_SOURCE = Int32
WCM_CONNECTION_COST_SOURCE_DEFAULT: WCM_CONNECTION_COST_SOURCE = 0
WCM_CONNECTION_COST_SOURCE_GP: WCM_CONNECTION_COST_SOURCE = 1
WCM_CONNECTION_COST_SOURCE_USER: WCM_CONNECTION_COST_SOURCE = 2
WCM_CONNECTION_COST_SOURCE_OPERATOR: WCM_CONNECTION_COST_SOURCE = 3
class WCM_DATAPLAN_STATUS(EasyCastStructure):
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
class WCM_POLICY_VALUE(EasyCastStructure):
    fValue: Windows.Win32.Foundation.BOOL
    fIsGroupPolicy: Windows.Win32.Foundation.BOOL
class WCM_PROFILE_INFO(EasyCastStructure):
    strProfileName: Char * 256
    AdapterGUID: Guid
    Media: Windows.Win32.NetworkManagement.WindowsConnectionManager.WCM_MEDIA_TYPE
class WCM_PROFILE_INFO_LIST(EasyCastStructure):
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
class WCM_TIME_INTERVAL(EasyCastStructure):
    wYear: UInt16
    wMonth: UInt16
    wDay: UInt16
    wHour: UInt16
    wMinute: UInt16
    wSecond: UInt16
    wMilliseconds: UInt16
class WCM_USAGE_DATA(EasyCastStructure):
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
