from win32more.base import *
import win32more.Foundation
import win32more.NetworkManagement.WindowsFilteringPlatform
import win32more.NetworkManagement.WindowsNetworkVirtualization
import win32more.Networking.WinSock
import win32more.System.IO

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
WNV_API_MAJOR_VERSION_1 = 1
WNV_API_MINOR_VERSION_0 = 0
WNV_NOTIFICATION_TYPE = Int32
WNV_NOTIFICATION_TYPE_WnvPolicyMismatchType = 0
WNV_NOTIFICATION_TYPE_WnvRedirectType = 1
WNV_NOTIFICATION_TYPE_WnvObjectChangeType = 2
WNV_NOTIFICATION_TYPE_WnvNotificationTypeMax = 3
WNV_OBJECT_TYPE = Int32
WNV_OBJECT_TYPE_WnvProviderAddressType = 0
WNV_OBJECT_TYPE_WnvCustomerAddressType = 1
WNV_OBJECT_TYPE_WnvObjectTypeMax = 2
WNV_CA_NOTIFICATION_TYPE = Int32
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressAdded = 0
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressDeleted = 1
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMoved = 2
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMax = 3
def _define_WNV_OBJECT_HEADER_head():
    class WNV_OBJECT_HEADER(Structure):
        pass
    return WNV_OBJECT_HEADER
def _define_WNV_OBJECT_HEADER():
    WNV_OBJECT_HEADER = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_HEADER_head
    WNV_OBJECT_HEADER._fields_ = [
        ("MajorVersion", Byte),
        ("MinorVersion", Byte),
        ("Size", UInt32),
    ]
    return WNV_OBJECT_HEADER
def _define_WNV_NOTIFICATION_PARAM_head():
    class WNV_NOTIFICATION_PARAM(Structure):
        pass
    return WNV_NOTIFICATION_PARAM
def _define_WNV_NOTIFICATION_PARAM():
    WNV_NOTIFICATION_PARAM = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_PARAM_head
    WNV_NOTIFICATION_PARAM._fields_ = [
        ("Header", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_HEADER),
        ("NotificationType", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE),
        ("PendingNotifications", UInt32),
        ("Buffer", c_char_p_no),
    ]
    return WNV_NOTIFICATION_PARAM
def _define_WNV_IP_ADDRESS_head():
    class WNV_IP_ADDRESS(Structure):
        pass
    return WNV_IP_ADDRESS
def _define_WNV_IP_ADDRESS():
    WNV_IP_ADDRESS = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS_head
    class WNV_IP_ADDRESS__IP_e__Union(Union):
        pass
    WNV_IP_ADDRESS__IP_e__Union._fields_ = [
        ("v4", win32more.Networking.WinSock.IN_ADDR),
        ("v6", win32more.Networking.WinSock.IN6_ADDR),
        ("Addr", Byte * 16),
    ]
    WNV_IP_ADDRESS._fields_ = [
        ("IP", WNV_IP_ADDRESS__IP_e__Union),
    ]
    return WNV_IP_ADDRESS
def _define_WNV_POLICY_MISMATCH_PARAM_head():
    class WNV_POLICY_MISMATCH_PARAM(Structure):
        pass
    return WNV_POLICY_MISMATCH_PARAM
def _define_WNV_POLICY_MISMATCH_PARAM():
    WNV_POLICY_MISMATCH_PARAM = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_POLICY_MISMATCH_PARAM_head
    WNV_POLICY_MISMATCH_PARAM._fields_ = [
        ("CAFamily", UInt16),
        ("PAFamily", UInt16),
        ("VirtualSubnetId", UInt32),
        ("CA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
        ("PA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
    ]
    return WNV_POLICY_MISMATCH_PARAM
def _define_WNV_PROVIDER_ADDRESS_CHANGE_PARAM_head():
    class WNV_PROVIDER_ADDRESS_CHANGE_PARAM(Structure):
        pass
    return WNV_PROVIDER_ADDRESS_CHANGE_PARAM
def _define_WNV_PROVIDER_ADDRESS_CHANGE_PARAM():
    WNV_PROVIDER_ADDRESS_CHANGE_PARAM = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_PROVIDER_ADDRESS_CHANGE_PARAM_head
    WNV_PROVIDER_ADDRESS_CHANGE_PARAM._fields_ = [
        ("PAFamily", UInt16),
        ("PA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
        ("AddressState", win32more.Networking.WinSock.NL_DAD_STATE),
    ]
    return WNV_PROVIDER_ADDRESS_CHANGE_PARAM
def _define_WNV_CUSTOMER_ADDRESS_CHANGE_PARAM_head():
    class WNV_CUSTOMER_ADDRESS_CHANGE_PARAM(Structure):
        pass
    return WNV_CUSTOMER_ADDRESS_CHANGE_PARAM
def _define_WNV_CUSTOMER_ADDRESS_CHANGE_PARAM():
    WNV_CUSTOMER_ADDRESS_CHANGE_PARAM = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_CUSTOMER_ADDRESS_CHANGE_PARAM_head
    WNV_CUSTOMER_ADDRESS_CHANGE_PARAM._fields_ = [
        ("MACAddress", win32more.NetworkManagement.WindowsFilteringPlatform.DL_EUI48),
        ("CAFamily", UInt16),
        ("CA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
        ("VirtualSubnetId", UInt32),
        ("PAFamily", UInt16),
        ("PA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
        ("NotificationReason", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE),
    ]
    return WNV_CUSTOMER_ADDRESS_CHANGE_PARAM
def _define_WNV_OBJECT_CHANGE_PARAM_head():
    class WNV_OBJECT_CHANGE_PARAM(Structure):
        pass
    return WNV_OBJECT_CHANGE_PARAM
def _define_WNV_OBJECT_CHANGE_PARAM():
    WNV_OBJECT_CHANGE_PARAM = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_CHANGE_PARAM_head
    class WNV_OBJECT_CHANGE_PARAM__ObjectParam_e__Union(Union):
        pass
    WNV_OBJECT_CHANGE_PARAM__ObjectParam_e__Union._fields_ = [
        ("ProviderAddressChange", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_PROVIDER_ADDRESS_CHANGE_PARAM),
        ("CustomerAddressChange", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_CUSTOMER_ADDRESS_CHANGE_PARAM),
    ]
    WNV_OBJECT_CHANGE_PARAM._fields_ = [
        ("ObjectType", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_TYPE),
        ("ObjectParam", WNV_OBJECT_CHANGE_PARAM__ObjectParam_e__Union),
    ]
    return WNV_OBJECT_CHANGE_PARAM
def _define_WNV_REDIRECT_PARAM_head():
    class WNV_REDIRECT_PARAM(Structure):
        pass
    return WNV_REDIRECT_PARAM
def _define_WNV_REDIRECT_PARAM():
    WNV_REDIRECT_PARAM = win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_REDIRECT_PARAM_head
    WNV_REDIRECT_PARAM._fields_ = [
        ("CAFamily", UInt16),
        ("PAFamily", UInt16),
        ("NewPAFamily", UInt16),
        ("VirtualSubnetId", UInt32),
        ("CA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
        ("PA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
        ("NewPA", win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS),
    ]
    return WNV_REDIRECT_PARAM
def _define_WnvOpen():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(("WnvOpen", windll["wnvapi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WnvRequestNotification():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_PARAM_head),POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32), use_last_error=False)(("WnvRequestNotification", windll["wnvapi"]), ((1, 'WnvHandle'),(1, 'NotificationParam'),(1, 'Overlapped'),(1, 'BytesTransferred'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WNV_API_MAJOR_VERSION_1",
    "WNV_API_MINOR_VERSION_0",
    "WNV_NOTIFICATION_TYPE",
    "WNV_NOTIFICATION_TYPE_WnvPolicyMismatchType",
    "WNV_NOTIFICATION_TYPE_WnvRedirectType",
    "WNV_NOTIFICATION_TYPE_WnvObjectChangeType",
    "WNV_NOTIFICATION_TYPE_WnvNotificationTypeMax",
    "WNV_OBJECT_TYPE",
    "WNV_OBJECT_TYPE_WnvProviderAddressType",
    "WNV_OBJECT_TYPE_WnvCustomerAddressType",
    "WNV_OBJECT_TYPE_WnvObjectTypeMax",
    "WNV_CA_NOTIFICATION_TYPE",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressAdded",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressDeleted",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMoved",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMax",
    "WNV_OBJECT_HEADER",
    "WNV_NOTIFICATION_PARAM",
    "WNV_IP_ADDRESS",
    "WNV_POLICY_MISMATCH_PARAM",
    "WNV_PROVIDER_ADDRESS_CHANGE_PARAM",
    "WNV_CUSTOMER_ADDRESS_CHANGE_PARAM",
    "WNV_OBJECT_CHANGE_PARAM",
    "WNV_REDIRECT_PARAM",
    "WnvOpen",
    "WnvRequestNotification",
]
