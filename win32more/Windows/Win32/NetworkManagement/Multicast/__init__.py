from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.Multicast
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
MCAST_CLIENT_ID_LEN: UInt32 = 17
MCAST_API_CURRENT_VERSION: Int32 = 1
MCAST_API_VERSION_0: Int32 = 0
MCAST_API_VERSION_1: Int32 = 1
@winfunctype('dhcpcsvc.dll')
def McastApiStartup(Version: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastApiCleanup() -> Void: ...
@winfunctype('dhcpcsvc.dll')
def McastGenUID(pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastEnumerateScopes(AddrFamily: UInt16, ReQuery: win32more.Windows.Win32.Foundation.BOOL, pScopeList: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_SCOPE_ENTRY_head), pScopeLen: POINTER(UInt32), pScopeCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastRequestAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID_head), pScopeCtx: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_SCOPE_CTX_head), pAddrRequest: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head), pAddrResponse: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastRenewAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID_head), pRenewRequest: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head), pRenewResponse: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def McastReleaseAddress(AddrFamily: UInt16, pRequestID: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_CLIENT_UID_head), pReleaseRequest: POINTER(win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head)) -> UInt32: ...
class IPNG_ADDRESS(EasyCastUnion):
    IpAddrV4: UInt32
    IpAddrV6: Byte * 16
class MCAST_CLIENT_UID(EasyCastStructure):
    ClientUID: POINTER(Byte)
    ClientUIDLength: UInt32
class MCAST_LEASE_REQUEST(EasyCastStructure):
    LeaseStartTime: Int32
    MaxLeaseStartTime: Int32
    LeaseDuration: UInt32
    MinLeaseDuration: UInt32
    ServerAddress: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    MinAddrCount: UInt16
    AddrCount: UInt16
    pAddrBuf: POINTER(Byte)
class MCAST_LEASE_RESPONSE(EasyCastStructure):
    LeaseStartTime: Int32
    LeaseEndTime: Int32
    ServerAddress: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    AddrCount: UInt16
    pAddrBuf: POINTER(Byte)
class MCAST_SCOPE_CTX(EasyCastStructure):
    ScopeID: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    Interface: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    ServerID: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
class MCAST_SCOPE_ENTRY(EasyCastStructure):
    ScopeCtx: win32more.Windows.Win32.NetworkManagement.Multicast.MCAST_SCOPE_CTX
    LastAddr: win32more.Windows.Win32.NetworkManagement.Multicast.IPNG_ADDRESS
    TTL: UInt32
    ScopeDesc: win32more.Windows.Win32.Foundation.UNICODE_STRING
make_head(_module, 'IPNG_ADDRESS')
make_head(_module, 'MCAST_CLIENT_UID')
make_head(_module, 'MCAST_LEASE_REQUEST')
make_head(_module, 'MCAST_LEASE_RESPONSE')
make_head(_module, 'MCAST_SCOPE_CTX')
make_head(_module, 'MCAST_SCOPE_ENTRY')
