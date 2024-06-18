from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.Multicast
MCAST_CLIENT_ID_LEN: UInt32 = 17
MCAST_API_CURRENT_VERSION: Int32 = 1
MCAST_API_VERSION_0: Int32 = 0
MCAST_API_VERSION_1: Int32 = 1
@winfunctype('dhcpcsvc.dll')
def McastApiStartup(Version: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastApiCleanup() -> Void: ...
@winfunctype('dhcpcsvc.dll')
def McastGenUID(pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastEnumerateScopes(AddrFamily: UInt16, ReQuery: win32more.Windows.Win32.Foundation.BOOL, pScopeList: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_SCOPE_ENTRY), pScopeLen: POINTER(UInt32), pScopeCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastRequestAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID), pScopeCtx: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_SCOPE_CTX), pAddrRequest: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_REQUEST), pAddrResponse: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastRenewAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID), pRenewRequest: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_REQUEST), pRenewResponse: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastReleaseAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID), pReleaseRequest: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_REQUEST)) -> UInt32: ...
class IPNG_ADDRESS(Union):
    IpAddrV4: UInt32
    IpAddrV6: Byte * 16
class MCAST_CLIENT_UID(Structure):
    ClientUID: POINTER(Byte)
    ClientUIDLength: UInt32
class MCAST_LEASE_REQUEST(Structure):
    LeaseStartTime: Int32
    MaxLeaseStartTime: Int32
    LeaseDuration: UInt32
    MinLeaseDuration: UInt32
    ServerAddress: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    MinAddrCount: UInt16
    AddrCount: UInt16
    pAddrBuf: POINTER(Byte)
class MCAST_LEASE_RESPONSE(Structure):
    LeaseStartTime: Int32
    LeaseEndTime: Int32
    ServerAddress: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    AddrCount: UInt16
    pAddrBuf: POINTER(Byte)
class MCAST_SCOPE_CTX(Structure):
    ScopeID: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    Interface: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    ServerID: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
class MCAST_SCOPE_ENTRY(Structure):
    ScopeCtx: win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_SCOPE_CTX
    LastAddr: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    TTL: UInt32
    ScopeDesc: win32more.Windows.Win32.Foundation.UNICODE_STRING


make_ready(__name__)
