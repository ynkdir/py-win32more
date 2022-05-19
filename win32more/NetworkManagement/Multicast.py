from win32more import *
import win32more.Foundation
import win32more.NetworkManagement.Multicast

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
MCAST_CLIENT_ID_LEN = 17
MCAST_API_CURRENT_VERSION = 1
MCAST_API_VERSION_0 = 0
MCAST_API_VERSION_1 = 1
def _define_IPNG_ADDRESS_head():
    class IPNG_ADDRESS(Union):
        pass
    return IPNG_ADDRESS
def _define_IPNG_ADDRESS():
    IPNG_ADDRESS = win32more.NetworkManagement.Multicast.IPNG_ADDRESS_head
    IPNG_ADDRESS._fields_ = [
        ("IpAddrV4", UInt32),
        ("IpAddrV6", Byte * 16),
    ]
    return IPNG_ADDRESS
def _define_MCAST_CLIENT_UID_head():
    class MCAST_CLIENT_UID(Structure):
        pass
    return MCAST_CLIENT_UID
def _define_MCAST_CLIENT_UID():
    MCAST_CLIENT_UID = win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head
    MCAST_CLIENT_UID._fields_ = [
        ("ClientUID", c_char_p_no),
        ("ClientUIDLength", UInt32),
    ]
    return MCAST_CLIENT_UID
def _define_MCAST_SCOPE_CTX_head():
    class MCAST_SCOPE_CTX(Structure):
        pass
    return MCAST_SCOPE_CTX
def _define_MCAST_SCOPE_CTX():
    MCAST_SCOPE_CTX = win32more.NetworkManagement.Multicast.MCAST_SCOPE_CTX_head
    MCAST_SCOPE_CTX._fields_ = [
        ("ScopeID", win32more.NetworkManagement.Multicast.IPNG_ADDRESS),
        ("Interface", win32more.NetworkManagement.Multicast.IPNG_ADDRESS),
        ("ServerID", win32more.NetworkManagement.Multicast.IPNG_ADDRESS),
    ]
    return MCAST_SCOPE_CTX
def _define_MCAST_SCOPE_ENTRY_head():
    class MCAST_SCOPE_ENTRY(Structure):
        pass
    return MCAST_SCOPE_ENTRY
def _define_MCAST_SCOPE_ENTRY():
    MCAST_SCOPE_ENTRY = win32more.NetworkManagement.Multicast.MCAST_SCOPE_ENTRY_head
    MCAST_SCOPE_ENTRY._fields_ = [
        ("ScopeCtx", win32more.NetworkManagement.Multicast.MCAST_SCOPE_CTX),
        ("LastAddr", win32more.NetworkManagement.Multicast.IPNG_ADDRESS),
        ("TTL", UInt32),
        ("ScopeDesc", win32more.Foundation.UNICODE_STRING),
    ]
    return MCAST_SCOPE_ENTRY
def _define_MCAST_LEASE_REQUEST_head():
    class MCAST_LEASE_REQUEST(Structure):
        pass
    return MCAST_LEASE_REQUEST
def _define_MCAST_LEASE_REQUEST():
    MCAST_LEASE_REQUEST = win32more.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head
    MCAST_LEASE_REQUEST._fields_ = [
        ("LeaseStartTime", Int32),
        ("MaxLeaseStartTime", Int32),
        ("LeaseDuration", UInt32),
        ("MinLeaseDuration", UInt32),
        ("ServerAddress", win32more.NetworkManagement.Multicast.IPNG_ADDRESS),
        ("MinAddrCount", UInt16),
        ("AddrCount", UInt16),
        ("pAddrBuf", c_char_p_no),
    ]
    return MCAST_LEASE_REQUEST
def _define_MCAST_LEASE_RESPONSE_head():
    class MCAST_LEASE_RESPONSE(Structure):
        pass
    return MCAST_LEASE_RESPONSE
def _define_MCAST_LEASE_RESPONSE():
    MCAST_LEASE_RESPONSE = win32more.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE_head
    MCAST_LEASE_RESPONSE._fields_ = [
        ("LeaseStartTime", Int32),
        ("LeaseEndTime", Int32),
        ("ServerAddress", win32more.NetworkManagement.Multicast.IPNG_ADDRESS),
        ("AddrCount", UInt16),
        ("pAddrBuf", c_char_p_no),
    ]
    return MCAST_LEASE_RESPONSE
def _define_McastApiStartup():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32), use_last_error=False)(("McastApiStartup", windll["dhcpcsvc"]), ((1, 'Version'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_McastApiCleanup():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("McastApiCleanup", windll["dhcpcsvc"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_McastGenUID():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head), use_last_error=False)(("McastGenUID", windll["dhcpcsvc"]), ((1, 'pRequestID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_McastEnumerateScopes():
    try:
        return WINFUNCTYPE(UInt32,UInt16,win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Multicast.MCAST_SCOPE_ENTRY_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("McastEnumerateScopes", windll["dhcpcsvc"]), ((1, 'AddrFamily'),(1, 'ReQuery'),(1, 'pScopeList'),(1, 'pScopeLen'),(1, 'pScopeCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_McastRequestAddress():
    try:
        return WINFUNCTYPE(UInt32,UInt16,POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head),POINTER(win32more.NetworkManagement.Multicast.MCAST_SCOPE_CTX_head),POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head),POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE_head), use_last_error=False)(("McastRequestAddress", windll["dhcpcsvc"]), ((1, 'AddrFamily'),(1, 'pRequestID'),(1, 'pScopeCtx'),(1, 'pAddrRequest'),(1, 'pAddrResponse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_McastRenewAddress():
    try:
        return WINFUNCTYPE(UInt32,UInt16,POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head),POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head),POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_RESPONSE_head), use_last_error=False)(("McastRenewAddress", windll["dhcpcsvc"]), ((1, 'AddrFamily'),(1, 'pRequestID'),(1, 'pRenewRequest'),(1, 'pRenewResponse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_McastReleaseAddress():
    try:
        return WINFUNCTYPE(UInt32,UInt16,POINTER(win32more.NetworkManagement.Multicast.MCAST_CLIENT_UID_head),POINTER(win32more.NetworkManagement.Multicast.MCAST_LEASE_REQUEST_head), use_last_error=False)(("McastReleaseAddress", windll["dhcpcsvc"]), ((1, 'AddrFamily'),(1, 'pRequestID'),(1, 'pReleaseRequest'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "MCAST_CLIENT_ID_LEN",
    "MCAST_API_CURRENT_VERSION",
    "MCAST_API_VERSION_0",
    "MCAST_API_VERSION_1",
    "IPNG_ADDRESS",
    "MCAST_CLIENT_UID",
    "MCAST_SCOPE_CTX",
    "MCAST_SCOPE_ENTRY",
    "MCAST_LEASE_REQUEST",
    "MCAST_LEASE_RESPONSE",
    "McastApiStartup",
    "McastApiCleanup",
    "McastGenUID",
    "McastEnumerateScopes",
    "McastRequestAddress",
    "McastRenewAddress",
    "McastReleaseAddress",
]
