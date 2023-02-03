from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.WindowsNetworkVirtualization
import Windows.Win32.Networking.WinSock
import Windows.Win32.System.IO
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
WNV_API_MAJOR_VERSION_1: UInt32 = 1
WNV_API_MINOR_VERSION_0: UInt32 = 0
@winfunctype('wnvapi.dll')
def WnvOpen() -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('wnvapi.dll')
def WnvRequestNotification(WnvHandle: Windows.Win32.Foundation.HANDLE, NotificationParam: POINTER(Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_PARAM_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), BytesTransferred: POINTER(UInt32)) -> UInt32: ...
WNV_CA_NOTIFICATION_TYPE = Int32
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressAdded: WNV_CA_NOTIFICATION_TYPE = 0
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressDeleted: WNV_CA_NOTIFICATION_TYPE = 1
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMoved: WNV_CA_NOTIFICATION_TYPE = 2
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMax: WNV_CA_NOTIFICATION_TYPE = 3
class WNV_CUSTOMER_ADDRESS_CHANGE_PARAM(Structure):
    MACAddress: Windows.Win32.Networking.WinSock.DL_EUI48
    CAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    CA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    VirtualSubnetId: UInt32
    PAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    NotificationReason: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE
class WNV_IP_ADDRESS(Structure):
    IP: _IP_e__Union
    class _IP_e__Union(Union):
        v4: Windows.Win32.Networking.WinSock.IN_ADDR
        v6: Windows.Win32.Networking.WinSock.IN6_ADDR
        Addr: Byte * 16
class WNV_NOTIFICATION_PARAM(Structure):
    Header: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_HEADER
    NotificationType: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE
    PendingNotifications: UInt32
    Buffer: c_char_p_no
WNV_NOTIFICATION_TYPE = Int32
WNV_NOTIFICATION_TYPE_WnvPolicyMismatchType: WNV_NOTIFICATION_TYPE = 0
WNV_NOTIFICATION_TYPE_WnvRedirectType: WNV_NOTIFICATION_TYPE = 1
WNV_NOTIFICATION_TYPE_WnvObjectChangeType: WNV_NOTIFICATION_TYPE = 2
WNV_NOTIFICATION_TYPE_WnvNotificationTypeMax: WNV_NOTIFICATION_TYPE = 3
class WNV_OBJECT_CHANGE_PARAM(Structure):
    ObjectType: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_TYPE
    ObjectParam: _ObjectParam_e__Union
    class _ObjectParam_e__Union(Union):
        ProviderAddressChange: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_PROVIDER_ADDRESS_CHANGE_PARAM
        CustomerAddressChange: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CUSTOMER_ADDRESS_CHANGE_PARAM
class WNV_OBJECT_HEADER(Structure):
    MajorVersion: Byte
    MinorVersion: Byte
    Size: UInt32
WNV_OBJECT_TYPE = Int32
WNV_OBJECT_TYPE_WnvProviderAddressType: WNV_OBJECT_TYPE = 0
WNV_OBJECT_TYPE_WnvCustomerAddressType: WNV_OBJECT_TYPE = 1
WNV_OBJECT_TYPE_WnvObjectTypeMax: WNV_OBJECT_TYPE = 2
class WNV_POLICY_MISMATCH_PARAM(Structure):
    CAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    VirtualSubnetId: UInt32
    CA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    PA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
class WNV_PROVIDER_ADDRESS_CHANGE_PARAM(Structure):
    PAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    AddressState: Windows.Win32.Networking.WinSock.NL_DAD_STATE
class WNV_REDIRECT_PARAM(Structure):
    CAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    NewPAFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    VirtualSubnetId: UInt32
    CA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    PA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    NewPA: Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
make_head(_module, 'WNV_CUSTOMER_ADDRESS_CHANGE_PARAM')
make_head(_module, 'WNV_IP_ADDRESS')
make_head(_module, 'WNV_NOTIFICATION_PARAM')
make_head(_module, 'WNV_OBJECT_CHANGE_PARAM')
make_head(_module, 'WNV_OBJECT_HEADER')
make_head(_module, 'WNV_POLICY_MISMATCH_PARAM')
make_head(_module, 'WNV_PROVIDER_ADDRESS_CHANGE_PARAM')
make_head(_module, 'WNV_REDIRECT_PARAM')
__all__ = [
    "WNV_API_MAJOR_VERSION_1",
    "WNV_API_MINOR_VERSION_0",
    "WNV_CA_NOTIFICATION_TYPE",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressAdded",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressDeleted",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMax",
    "WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMoved",
    "WNV_CUSTOMER_ADDRESS_CHANGE_PARAM",
    "WNV_IP_ADDRESS",
    "WNV_NOTIFICATION_PARAM",
    "WNV_NOTIFICATION_TYPE",
    "WNV_NOTIFICATION_TYPE_WnvNotificationTypeMax",
    "WNV_NOTIFICATION_TYPE_WnvObjectChangeType",
    "WNV_NOTIFICATION_TYPE_WnvPolicyMismatchType",
    "WNV_NOTIFICATION_TYPE_WnvRedirectType",
    "WNV_OBJECT_CHANGE_PARAM",
    "WNV_OBJECT_HEADER",
    "WNV_OBJECT_TYPE",
    "WNV_OBJECT_TYPE_WnvCustomerAddressType",
    "WNV_OBJECT_TYPE_WnvObjectTypeMax",
    "WNV_OBJECT_TYPE_WnvProviderAddressType",
    "WNV_POLICY_MISMATCH_PARAM",
    "WNV_PROVIDER_ADDRESS_CHANGE_PARAM",
    "WNV_REDIRECT_PARAM",
    "WnvOpen",
    "WnvRequestNotification",
]
_arch_optional = [
]
