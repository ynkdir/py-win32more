from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.System.IO
WNV_API_MAJOR_VERSION_1: UInt32 = 1
WNV_API_MINOR_VERSION_0: UInt32 = 0
@winfunctype('wnvapi.dll')
def WnvOpen() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('wnvapi.dll')
def WnvRequestNotification(WnvHandle: win32more.Windows.Win32.Foundation.HANDLE, NotificationParam: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_PARAM), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), BytesTransferred: POINTER(UInt32)) -> UInt32: ...
WNV_CA_NOTIFICATION_TYPE = Int32
WnvCustomerAddressAdded: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE = 0
WnvCustomerAddressDeleted: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE = 1
WnvCustomerAddressMoved: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE = 2
WnvCustomerAddressMax: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE = 3
class WNV_CUSTOMER_ADDRESS_CHANGE_PARAM(Structure):
    MACAddress: win32more.Windows.Win32.Networking.WinSock.DL_EUI48
    CAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    CA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    VirtualSubnetId: UInt32
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    NotificationReason: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE
class WNV_IP_ADDRESS(Structure):
    IP: _IP_e__Union
    class _IP_e__Union(Union):
        v4: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        v6: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
        Addr: Byte * 16
class WNV_NOTIFICATION_PARAM(Structure):
    Header: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_HEADER
    NotificationType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE
    PendingNotifications: UInt32
    Buffer: POINTER(Byte)
WNV_NOTIFICATION_TYPE = Int32
WnvPolicyMismatchType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE = 0
WnvRedirectType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE = 1
WnvObjectChangeType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE = 2
WnvNotificationTypeMax: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE = 3
class WNV_OBJECT_CHANGE_PARAM(Structure):
    ObjectType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_TYPE
    ObjectParam: _ObjectParam_e__Union
    class _ObjectParam_e__Union(Union):
        ProviderAddressChange: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_PROVIDER_ADDRESS_CHANGE_PARAM
        CustomerAddressChange: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CUSTOMER_ADDRESS_CHANGE_PARAM
class WNV_OBJECT_HEADER(Structure):
    MajorVersion: Byte
    MinorVersion: Byte
    Size: UInt32
WNV_OBJECT_TYPE = Int32
WnvProviderAddressType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_TYPE = 0
WnvCustomerAddressType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_TYPE = 1
WnvObjectTypeMax: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_TYPE = 2
class WNV_POLICY_MISMATCH_PARAM(Structure):
    CAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    VirtualSubnetId: UInt32
    CA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
class WNV_PROVIDER_ADDRESS_CHANGE_PARAM(Structure):
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    AddressState: win32more.Windows.Win32.Networking.WinSock.NL_DAD_STATE
class WNV_REDIRECT_PARAM(Structure):
    CAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    NewPAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    VirtualSubnetId: UInt32
    CA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    NewPA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS


make_ready(__name__)
