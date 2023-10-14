from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
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
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressAdded: WNV_CA_NOTIFICATION_TYPE = 0
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressDeleted: WNV_CA_NOTIFICATION_TYPE = 1
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMoved: WNV_CA_NOTIFICATION_TYPE = 2
WNV_CA_NOTIFICATION_TYPE_WnvCustomerAddressMax: WNV_CA_NOTIFICATION_TYPE = 3
class WNV_CUSTOMER_ADDRESS_CHANGE_PARAM(EasyCastStructure):
    MACAddress: win32more.Windows.Win32.Networking.WinSock.DL_EUI48
    CAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    CA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    VirtualSubnetId: UInt32
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    NotificationReason: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CA_NOTIFICATION_TYPE
class WNV_IP_ADDRESS(EasyCastStructure):
    IP: _IP_e__Union
    class _IP_e__Union(EasyCastUnion):
        v4: win32more.Windows.Win32.Networking.WinSock.IN_ADDR
        v6: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
        Addr: Byte * 16
class WNV_NOTIFICATION_PARAM(EasyCastStructure):
    Header: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_HEADER
    NotificationType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_NOTIFICATION_TYPE
    PendingNotifications: UInt32
    Buffer: POINTER(Byte)
WNV_NOTIFICATION_TYPE = Int32
WNV_NOTIFICATION_TYPE_WnvPolicyMismatchType: WNV_NOTIFICATION_TYPE = 0
WNV_NOTIFICATION_TYPE_WnvRedirectType: WNV_NOTIFICATION_TYPE = 1
WNV_NOTIFICATION_TYPE_WnvObjectChangeType: WNV_NOTIFICATION_TYPE = 2
WNV_NOTIFICATION_TYPE_WnvNotificationTypeMax: WNV_NOTIFICATION_TYPE = 3
class WNV_OBJECT_CHANGE_PARAM(EasyCastStructure):
    ObjectType: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_OBJECT_TYPE
    ObjectParam: _ObjectParam_e__Union
    class _ObjectParam_e__Union(EasyCastUnion):
        ProviderAddressChange: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_PROVIDER_ADDRESS_CHANGE_PARAM
        CustomerAddressChange: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_CUSTOMER_ADDRESS_CHANGE_PARAM
class WNV_OBJECT_HEADER(EasyCastStructure):
    MajorVersion: Byte
    MinorVersion: Byte
    Size: UInt32
WNV_OBJECT_TYPE = Int32
WNV_OBJECT_TYPE_WnvProviderAddressType: WNV_OBJECT_TYPE = 0
WNV_OBJECT_TYPE_WnvCustomerAddressType: WNV_OBJECT_TYPE = 1
WNV_OBJECT_TYPE_WnvObjectTypeMax: WNV_OBJECT_TYPE = 2
class WNV_POLICY_MISMATCH_PARAM(EasyCastStructure):
    CAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    VirtualSubnetId: UInt32
    CA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
class WNV_PROVIDER_ADDRESS_CHANGE_PARAM(EasyCastStructure):
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    AddressState: win32more.Windows.Win32.Networking.WinSock.NL_DAD_STATE
class WNV_REDIRECT_PARAM(EasyCastStructure):
    CAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    PAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    NewPAFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    VirtualSubnetId: UInt32
    CA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    PA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
    NewPA: win32more.Windows.Win32.NetworkManagement.WindowsNetworkVirtualization.WNV_IP_ADDRESS
make_ready(__name__)
