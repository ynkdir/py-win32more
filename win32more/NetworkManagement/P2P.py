from win32more.base import *
import win32more.Foundation
import win32more.NetworkManagement.P2P
import win32more.Networking.WinSock
import win32more.Security.Cryptography
import win32more.System.Com
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
NS_PNRPNAME = 38
NS_PNRPCLOUD = 39
PNRPINFO_HINT = 1
NS_PROVIDER_PNRPNAME = '03fe89cd-766d-4976-b9c1-bb9bc42c7b4d'
NS_PROVIDER_PNRPCLOUD = '03fe89ce-766d-4976-b9c1-bb9bc42c7b4d'
SVCID_PNRPCLOUD = 'c2239ce6-00c0-4fbf-bad6-18139385a49a'
SVCID_PNRPNAME_V1 = 'c2239ce5-00c0-4fbf-bad6-18139385a49a'
SVCID_PNRPNAME_V2 = 'c2239ce7-00c0-4fbf-bad6-18139385a49a'
PNRP_MAX_ENDPOINT_ADDRESSES = 10
PNRP_MAX_EXTENDED_PAYLOAD_BYTES = 4096
WSA_PNRP_ERROR_BASE = 11500
WSA_PNRP_CLOUD_NOT_FOUND = 11501
WSA_PNRP_CLOUD_DISABLED = 11502
WSA_PNRP_INVALID_IDENTITY = 11503
WSA_PNRP_TOO_MUCH_LOAD = 11504
WSA_PNRP_CLOUD_IS_SEARCH_ONLY = 11505
WSA_PNRP_CLIENT_INVALID_COMPARTMENT_ID = 11506
WSA_PNRP_DUPLICATE_PEER_NAME = 11508
WSA_PNRP_CLOUD_IS_DEAD = 11509
PEER_E_CLOUD_NOT_FOUND = -2147013395
PEER_E_CLOUD_DISABLED = -2147013394
PEER_E_INVALID_IDENTITY = -2147013393
PEER_E_TOO_MUCH_LOAD = -2147013392
PEER_E_CLOUD_IS_SEARCH_ONLY = -2147013391
PEER_E_CLIENT_INVALID_COMPARTMENT_ID = -2147013390
PEER_E_DUPLICATE_PEER_NAME = -2147013388
PEER_E_CLOUD_IS_DEAD = -2147013387
PEER_E_NOT_FOUND = -2147023728
PEER_E_DISK_FULL = -2147024784
PEER_E_ALREADY_EXISTS = -2147024713
PEER_GROUP_ROLE_ADMIN = '04387127-aa56-450a-8ce5-4f565c6790f4'
PEER_GROUP_ROLE_MEMBER = 'f12dc4c7-0857-4ca0-93fc-b1bb19a3d8c2'
PEER_GROUP_ROLE_INVITING_MEMBER = '4370fd89-dc18-4cfb-8dbf-9853a8a9f905'
PEER_COLLAB_OBJECTID_USER_PICTURE = 'dd15f41f-fc4e-4922-b035-4c06a754d01d'
FACILITY_DRT = 98
DRT_E_TIMEOUT = -2141057023
DRT_E_INVALID_KEY_SIZE = -2141057022
DRT_E_INVALID_CERT_CHAIN = -2141057020
DRT_E_INVALID_MESSAGE = -2141057019
DRT_E_NO_MORE = -2141057018
DRT_E_INVALID_MAX_ADDRESSES = -2141057017
DRT_E_SEARCH_IN_PROGRESS = -2141057016
DRT_E_INVALID_KEY = -2141057015
DRT_S_RETRY = 6426640
DRT_E_INVALID_MAX_ENDPOINTS = -2141057007
DRT_E_INVALID_SEARCH_RANGE = -2141057006
DRT_E_INVALID_PORT = -2141052928
DRT_E_INVALID_TRANSPORT_PROVIDER = -2141052927
DRT_E_INVALID_SECURITY_PROVIDER = -2141052926
DRT_E_STILL_IN_USE = -2141052925
DRT_E_INVALID_BOOTSTRAP_PROVIDER = -2141052924
DRT_E_INVALID_ADDRESS = -2141052923
DRT_E_INVALID_SCOPE = -2141052922
DRT_E_TRANSPORT_SHUTTING_DOWN = -2141052921
DRT_E_NO_ADDRESSES_AVAILABLE = -2141052920
DRT_E_DUPLICATE_KEY = -2141052919
DRT_E_TRANSPORTPROVIDER_IN_USE = -2141052918
DRT_E_TRANSPORTPROVIDER_NOT_ATTACHED = -2141052917
DRT_E_SECURITYPROVIDER_IN_USE = -2141052916
DRT_E_SECURITYPROVIDER_NOT_ATTACHED = -2141052915
DRT_E_BOOTSTRAPPROVIDER_IN_USE = -2141052914
DRT_E_BOOTSTRAPPROVIDER_NOT_ATTACHED = -2141052913
DRT_E_TRANSPORT_ALREADY_BOUND = -2141052671
DRT_E_TRANSPORT_NOT_BOUND = -2141052670
DRT_E_TRANSPORT_UNEXPECTED = -2141052669
DRT_E_TRANSPORT_INVALID_ARGUMENT = -2141052668
DRT_E_TRANSPORT_NO_DEST_ADDRESSES = -2141052667
DRT_E_TRANSPORT_EXECUTING_CALLBACK = -2141052666
DRT_E_TRANSPORT_ALREADY_EXISTS_FOR_SCOPE = -2141052665
DRT_E_INVALID_SETTINGS = -2141052664
DRT_E_INVALID_SEARCH_INFO = -2141052663
DRT_E_FAULTED = -2141052662
DRT_E_TRANSPORT_STILL_BOUND = -2141052661
DRT_E_INSUFFICIENT_BUFFER = -2141052660
DRT_E_INVALID_INSTANCE_PREFIX = -2141052659
DRT_E_INVALID_SECURITY_MODE = -2141052658
DRT_E_CAPABILITY_MISMATCH = -2141052657
DRT_PAYLOAD_REVOKED = 1
DRT_MIN_ROUTING_ADDRESSES = 1
DRT_MAX_ROUTING_ADDRESSES = 20
DRT_MAX_PAYLOAD_SIZE = 5120
DRT_MAX_INSTANCE_PREFIX_LEN = 128
DRT_LINK_LOCAL_ISATAP_SCOPEID = 4294967295
PEERDIST_PUBLICATION_OPTIONS_VERSION_1 = 1
PEERDIST_PUBLICATION_OPTIONS_VERSION = 2
PEERDIST_PUBLICATION_OPTIONS_VERSION_2 = 2
PEERDIST_READ_TIMEOUT_LOCAL_CACHE_ONLY = 0
PEERDIST_READ_TIMEOUT_DEFAULT = 4294967294
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = UInt32
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_1 = 1
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_2 = 2
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION = 2
PNRP_SCOPE = Int32
PNRP_SCOPE_ANY = 0
PNRP_GLOBAL_SCOPE = 1
PNRP_SITE_LOCAL_SCOPE = 2
PNRP_LINK_LOCAL_SCOPE = 3
PNRP_CLOUD_STATE = Int32
PNRP_CLOUD_STATE_VIRTUAL = 0
PNRP_CLOUD_STATE_SYNCHRONISING = 1
PNRP_CLOUD_STATE_ACTIVE = 2
PNRP_CLOUD_STATE_DEAD = 3
PNRP_CLOUD_STATE_DISABLED = 4
PNRP_CLOUD_STATE_NO_NET = 5
PNRP_CLOUD_STATE_ALONE = 6
PNRP_CLOUD_FLAGS = Int32
PNRP_CLOUD_NO_FLAGS = 0
PNRP_CLOUD_NAME_LOCAL = 1
PNRP_CLOUD_RESOLVE_ONLY = 2
PNRP_CLOUD_FULL_PARTICIPANT = 4
PNRP_REGISTERED_ID_STATE = Int32
PNRP_REGISTERED_ID_STATE_OK = 1
PNRP_REGISTERED_ID_STATE_PROBLEM = 2
PNRP_RESOLVE_CRITERIA = Int32
PNRP_RESOLVE_CRITERIA_DEFAULT = 0
PNRP_RESOLVE_CRITERIA_REMOTE_PEER_NAME = 1
PNRP_RESOLVE_CRITERIA_NEAREST_REMOTE_PEER_NAME = 2
PNRP_RESOLVE_CRITERIA_NON_CURRENT_PROCESS_PEER_NAME = 3
PNRP_RESOLVE_CRITERIA_NEAREST_NON_CURRENT_PROCESS_PEER_NAME = 4
PNRP_RESOLVE_CRITERIA_ANY_PEER_NAME = 5
PNRP_RESOLVE_CRITERIA_NEAREST_PEER_NAME = 6
def _define_PNRP_CLOUD_ID_head():
    class PNRP_CLOUD_ID(Structure):
        pass
    return PNRP_CLOUD_ID
def _define_PNRP_CLOUD_ID():
    PNRP_CLOUD_ID = win32more.NetworkManagement.P2P.PNRP_CLOUD_ID_head
    PNRP_CLOUD_ID._fields_ = [
        ("AddressFamily", Int32),
        ("Scope", win32more.NetworkManagement.P2P.PNRP_SCOPE),
        ("ScopeId", UInt32),
    ]
    return PNRP_CLOUD_ID
PNRP_EXTENDED_PAYLOAD_TYPE = Int32
PNRP_EXTENDED_PAYLOAD_TYPE_NONE = 0
PNRP_EXTENDED_PAYLOAD_TYPE_BINARY = 1
PNRP_EXTENDED_PAYLOAD_TYPE_STRING = 2
def _define_PNRPINFO_V1_head():
    class PNRPINFO_V1(Structure):
        pass
    return PNRPINFO_V1
def _define_PNRPINFO_V1():
    PNRPINFO_V1 = win32more.NetworkManagement.P2P.PNRPINFO_V1_head
    PNRPINFO_V1._fields_ = [
        ("dwSize", UInt32),
        ("lpwszIdentity", win32more.Foundation.PWSTR),
        ("nMaxResolve", UInt32),
        ("dwTimeout", UInt32),
        ("dwLifetime", UInt32),
        ("enResolveCriteria", win32more.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA),
        ("dwFlags", UInt32),
        ("saHint", win32more.Networking.WinSock.SOCKET_ADDRESS),
        ("enNameState", win32more.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE),
    ]
    return PNRPINFO_V1
def _define_PNRPINFO_V2_head():
    class PNRPINFO_V2(Structure):
        pass
    return PNRPINFO_V2
def _define_PNRPINFO_V2():
    PNRPINFO_V2 = win32more.NetworkManagement.P2P.PNRPINFO_V2_head
    class PNRPINFO_V2__Anonymous_e__Union(Union):
        pass
    PNRPINFO_V2__Anonymous_e__Union._fields_ = [
        ("blobPayload", win32more.System.Com.BLOB),
        ("pwszPayload", win32more.Foundation.PWSTR),
    ]
    PNRPINFO_V2._anonymous_ = [
        'Anonymous',
    ]
    PNRPINFO_V2._fields_ = [
        ("dwSize", UInt32),
        ("lpwszIdentity", win32more.Foundation.PWSTR),
        ("nMaxResolve", UInt32),
        ("dwTimeout", UInt32),
        ("dwLifetime", UInt32),
        ("enResolveCriteria", win32more.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA),
        ("dwFlags", UInt32),
        ("saHint", win32more.Networking.WinSock.SOCKET_ADDRESS),
        ("enNameState", win32more.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE),
        ("enExtendedPayloadType", win32more.NetworkManagement.P2P.PNRP_EXTENDED_PAYLOAD_TYPE),
        ("Anonymous", PNRPINFO_V2__Anonymous_e__Union),
    ]
    return PNRPINFO_V2
def _define_PNRPCLOUDINFO_head():
    class PNRPCLOUDINFO(Structure):
        pass
    return PNRPCLOUDINFO
def _define_PNRPCLOUDINFO():
    PNRPCLOUDINFO = win32more.NetworkManagement.P2P.PNRPCLOUDINFO_head
    PNRPCLOUDINFO._fields_ = [
        ("dwSize", UInt32),
        ("Cloud", win32more.NetworkManagement.P2P.PNRP_CLOUD_ID),
        ("enCloudState", win32more.NetworkManagement.P2P.PNRP_CLOUD_STATE),
        ("enCloudFlags", win32more.NetworkManagement.P2P.PNRP_CLOUD_FLAGS),
    ]
    return PNRPCLOUDINFO
PEER_RECORD_CHANGE_TYPE = Int32
PEER_RECORD_ADDED = 1
PEER_RECORD_UPDATED = 2
PEER_RECORD_DELETED = 3
PEER_RECORD_EXPIRED = 4
PEER_CONNECTION_STATUS = Int32
PEER_CONNECTED = 1
PEER_DISCONNECTED = 2
PEER_CONNECTION_FAILED = 3
PEER_CONNECTION_FLAGS = Int32
PEER_CONNECTION_NEIGHBOR = 1
PEER_CONNECTION_DIRECT = 2
PEER_RECORD_FLAGS = Int32
PEER_RECORD_FLAG_AUTOREFRESH = 1
PEER_RECORD_FLAG_DELETED = 2
def _define_PEER_VERSION_DATA_head():
    class PEER_VERSION_DATA(Structure):
        pass
    return PEER_VERSION_DATA
def _define_PEER_VERSION_DATA():
    PEER_VERSION_DATA = win32more.NetworkManagement.P2P.PEER_VERSION_DATA_head
    PEER_VERSION_DATA._fields_ = [
        ("wVersion", UInt16),
        ("wHighestVersion", UInt16),
    ]
    return PEER_VERSION_DATA
def _define_PEER_DATA_head():
    class PEER_DATA(Structure):
        pass
    return PEER_DATA
def _define_PEER_DATA():
    PEER_DATA = win32more.NetworkManagement.P2P.PEER_DATA_head
    PEER_DATA._fields_ = [
        ("cbData", UInt32),
        ("pbData", c_char_p_no),
    ]
    return PEER_DATA
def _define_PEER_RECORD_head():
    class PEER_RECORD(Structure):
        pass
    return PEER_RECORD
def _define_PEER_RECORD():
    PEER_RECORD = win32more.NetworkManagement.P2P.PEER_RECORD_head
    PEER_RECORD._fields_ = [
        ("dwSize", UInt32),
        ("type", Guid),
        ("id", Guid),
        ("dwVersion", UInt32),
        ("dwFlags", UInt32),
        ("pwzCreatorId", win32more.Foundation.PWSTR),
        ("pwzModifiedById", win32more.Foundation.PWSTR),
        ("pwzAttributes", win32more.Foundation.PWSTR),
        ("ftCreation", win32more.Foundation.FILETIME),
        ("ftExpiration", win32more.Foundation.FILETIME),
        ("ftLastModified", win32more.Foundation.FILETIME),
        ("securityData", win32more.NetworkManagement.P2P.PEER_DATA),
        ("data", win32more.NetworkManagement.P2P.PEER_DATA),
    ]
    return PEER_RECORD
def _define_PEER_ADDRESS_head():
    class PEER_ADDRESS(Structure):
        pass
    return PEER_ADDRESS
def _define_PEER_ADDRESS():
    PEER_ADDRESS = win32more.NetworkManagement.P2P.PEER_ADDRESS_head
    PEER_ADDRESS._fields_ = [
        ("dwSize", UInt32),
        ("sin6", win32more.Networking.WinSock.SOCKADDR_IN6),
    ]
    return PEER_ADDRESS
def _define_PEER_CONNECTION_INFO_head():
    class PEER_CONNECTION_INFO(Structure):
        pass
    return PEER_CONNECTION_INFO
def _define_PEER_CONNECTION_INFO():
    PEER_CONNECTION_INFO = win32more.NetworkManagement.P2P.PEER_CONNECTION_INFO_head
    PEER_CONNECTION_INFO._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("ullConnectionId", UInt64),
        ("ullNodeId", UInt64),
        ("pwzPeerId", win32more.Foundation.PWSTR),
        ("address", win32more.NetworkManagement.P2P.PEER_ADDRESS),
    ]
    return PEER_CONNECTION_INFO
def _define_PEER_EVENT_INCOMING_DATA_head():
    class PEER_EVENT_INCOMING_DATA(Structure):
        pass
    return PEER_EVENT_INCOMING_DATA
def _define_PEER_EVENT_INCOMING_DATA():
    PEER_EVENT_INCOMING_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA_head
    PEER_EVENT_INCOMING_DATA._fields_ = [
        ("dwSize", UInt32),
        ("ullConnectionId", UInt64),
        ("type", Guid),
        ("data", win32more.NetworkManagement.P2P.PEER_DATA),
    ]
    return PEER_EVENT_INCOMING_DATA
def _define_PEER_EVENT_RECORD_CHANGE_DATA_head():
    class PEER_EVENT_RECORD_CHANGE_DATA(Structure):
        pass
    return PEER_EVENT_RECORD_CHANGE_DATA
def _define_PEER_EVENT_RECORD_CHANGE_DATA():
    PEER_EVENT_RECORD_CHANGE_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA_head
    PEER_EVENT_RECORD_CHANGE_DATA._fields_ = [
        ("dwSize", UInt32),
        ("changeType", win32more.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE),
        ("recordId", Guid),
        ("recordType", Guid),
    ]
    return PEER_EVENT_RECORD_CHANGE_DATA
def _define_PEER_EVENT_CONNECTION_CHANGE_DATA_head():
    class PEER_EVENT_CONNECTION_CHANGE_DATA(Structure):
        pass
    return PEER_EVENT_CONNECTION_CHANGE_DATA
def _define_PEER_EVENT_CONNECTION_CHANGE_DATA():
    PEER_EVENT_CONNECTION_CHANGE_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA_head
    PEER_EVENT_CONNECTION_CHANGE_DATA._fields_ = [
        ("dwSize", UInt32),
        ("status", win32more.NetworkManagement.P2P.PEER_CONNECTION_STATUS),
        ("ullConnectionId", UInt64),
        ("ullNodeId", UInt64),
        ("ullNextConnectionId", UInt64),
        ("hrConnectionFailedReason", win32more.Foundation.HRESULT),
    ]
    return PEER_EVENT_CONNECTION_CHANGE_DATA
def _define_PEER_EVENT_SYNCHRONIZED_DATA_head():
    class PEER_EVENT_SYNCHRONIZED_DATA(Structure):
        pass
    return PEER_EVENT_SYNCHRONIZED_DATA
def _define_PEER_EVENT_SYNCHRONIZED_DATA():
    PEER_EVENT_SYNCHRONIZED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_SYNCHRONIZED_DATA_head
    PEER_EVENT_SYNCHRONIZED_DATA._fields_ = [
        ("dwSize", UInt32),
        ("recordType", Guid),
    ]
    return PEER_EVENT_SYNCHRONIZED_DATA
PEER_GRAPH_EVENT_TYPE = Int32
PEER_GRAPH_EVENT_STATUS_CHANGED = 1
PEER_GRAPH_EVENT_PROPERTY_CHANGED = 2
PEER_GRAPH_EVENT_RECORD_CHANGED = 3
PEER_GRAPH_EVENT_DIRECT_CONNECTION = 4
PEER_GRAPH_EVENT_NEIGHBOR_CONNECTION = 5
PEER_GRAPH_EVENT_INCOMING_DATA = 6
PEER_GRAPH_EVENT_CONNECTION_REQUIRED = 7
PEER_GRAPH_EVENT_NODE_CHANGED = 8
PEER_GRAPH_EVENT_SYNCHRONIZED = 9
PEER_NODE_CHANGE_TYPE = Int32
PEER_NODE_CHANGE_CONNECTED = 1
PEER_NODE_CHANGE_DISCONNECTED = 2
PEER_NODE_CHANGE_UPDATED = 3
PEER_GRAPH_STATUS_FLAGS = Int32
PEER_GRAPH_STATUS_LISTENING = 1
PEER_GRAPH_STATUS_HAS_CONNECTIONS = 2
PEER_GRAPH_STATUS_SYNCHRONIZED = 4
PEER_GRAPH_PROPERTY_FLAGS = Int32
PEER_GRAPH_PROPERTY_HEARTBEATS = 1
PEER_GRAPH_PROPERTY_DEFER_EXPIRATION = 2
PEER_GRAPH_SCOPE = Int32
PEER_GRAPH_SCOPE_ANY = 0
PEER_GRAPH_SCOPE_GLOBAL = 1
PEER_GRAPH_SCOPE_SITELOCAL = 2
PEER_GRAPH_SCOPE_LINKLOCAL = 3
PEER_GRAPH_SCOPE_LOOPBACK = 4
def _define_PEER_GRAPH_PROPERTIES_head():
    class PEER_GRAPH_PROPERTIES(Structure):
        pass
    return PEER_GRAPH_PROPERTIES
def _define_PEER_GRAPH_PROPERTIES():
    PEER_GRAPH_PROPERTIES = win32more.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head
    PEER_GRAPH_PROPERTIES._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwScope", UInt32),
        ("dwMaxRecordSize", UInt32),
        ("pwzGraphId", win32more.Foundation.PWSTR),
        ("pwzCreatorId", win32more.Foundation.PWSTR),
        ("pwzFriendlyName", win32more.Foundation.PWSTR),
        ("pwzComment", win32more.Foundation.PWSTR),
        ("ulPresenceLifetime", UInt32),
        ("cPresenceMax", UInt32),
    ]
    return PEER_GRAPH_PROPERTIES
def _define_PEER_NODE_INFO_head():
    class PEER_NODE_INFO(Structure):
        pass
    return PEER_NODE_INFO
def _define_PEER_NODE_INFO():
    PEER_NODE_INFO = win32more.NetworkManagement.P2P.PEER_NODE_INFO_head
    PEER_NODE_INFO._fields_ = [
        ("dwSize", UInt32),
        ("ullNodeId", UInt64),
        ("pwzPeerId", win32more.Foundation.PWSTR),
        ("cAddresses", UInt32),
        ("pAddresses", POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head)),
        ("pwzAttributes", win32more.Foundation.PWSTR),
    ]
    return PEER_NODE_INFO
def _define_PEER_EVENT_NODE_CHANGE_DATA_head():
    class PEER_EVENT_NODE_CHANGE_DATA(Structure):
        pass
    return PEER_EVENT_NODE_CHANGE_DATA
def _define_PEER_EVENT_NODE_CHANGE_DATA():
    PEER_EVENT_NODE_CHANGE_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_NODE_CHANGE_DATA_head
    PEER_EVENT_NODE_CHANGE_DATA._fields_ = [
        ("dwSize", UInt32),
        ("changeType", win32more.NetworkManagement.P2P.PEER_NODE_CHANGE_TYPE),
        ("ullNodeId", UInt64),
        ("pwzPeerId", win32more.Foundation.PWSTR),
    ]
    return PEER_EVENT_NODE_CHANGE_DATA
def _define_PEER_GRAPH_EVENT_REGISTRATION_head():
    class PEER_GRAPH_EVENT_REGISTRATION(Structure):
        pass
    return PEER_GRAPH_EVENT_REGISTRATION
def _define_PEER_GRAPH_EVENT_REGISTRATION():
    PEER_GRAPH_EVENT_REGISTRATION = win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_REGISTRATION_head
    PEER_GRAPH_EVENT_REGISTRATION._fields_ = [
        ("eventType", win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE),
        ("pType", POINTER(Guid)),
    ]
    return PEER_GRAPH_EVENT_REGISTRATION
def _define_PEER_GRAPH_EVENT_DATA_head():
    class PEER_GRAPH_EVENT_DATA(Structure):
        pass
    return PEER_GRAPH_EVENT_DATA
def _define_PEER_GRAPH_EVENT_DATA():
    PEER_GRAPH_EVENT_DATA = win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_DATA_head
    class PEER_GRAPH_EVENT_DATA__Anonymous_e__Union(Union):
        pass
    PEER_GRAPH_EVENT_DATA__Anonymous_e__Union._fields_ = [
        ("dwStatus", win32more.NetworkManagement.P2P.PEER_GRAPH_STATUS_FLAGS),
        ("incomingData", win32more.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA),
        ("recordChangeData", win32more.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA),
        ("connectionChangeData", win32more.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA),
        ("nodeChangeData", win32more.NetworkManagement.P2P.PEER_EVENT_NODE_CHANGE_DATA),
        ("synchronizedData", win32more.NetworkManagement.P2P.PEER_EVENT_SYNCHRONIZED_DATA),
    ]
    PEER_GRAPH_EVENT_DATA._anonymous_ = [
        'Anonymous',
    ]
    PEER_GRAPH_EVENT_DATA._fields_ = [
        ("eventType", win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE),
        ("Anonymous", PEER_GRAPH_EVENT_DATA__Anonymous_e__Union),
    ]
    return PEER_GRAPH_EVENT_DATA
def _define_PFNPEER_VALIDATE_RECORD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head),win32more.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE, use_last_error=False)
def _define_PFNPEER_SECURE_RECORD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head),win32more.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_DATA_head)), use_last_error=False)
def _define_PFNPEER_FREE_SECURITY_DATA():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_DATA_head), use_last_error=False)
def _define_PFNPEER_ON_PASSWORD_AUTH_FAILED():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p, use_last_error=False)
def _define_PEER_SECURITY_INTERFACE_head():
    class PEER_SECURITY_INTERFACE(Structure):
        pass
    return PEER_SECURITY_INTERFACE
def _define_PEER_SECURITY_INTERFACE():
    PEER_SECURITY_INTERFACE = win32more.NetworkManagement.P2P.PEER_SECURITY_INTERFACE_head
    PEER_SECURITY_INTERFACE._fields_ = [
        ("dwSize", UInt32),
        ("pwzSspFilename", win32more.Foundation.PWSTR),
        ("pwzPackageName", win32more.Foundation.PWSTR),
        ("cbSecurityInfo", UInt32),
        ("pbSecurityInfo", c_char_p_no),
        ("pvContext", c_void_p),
        ("pfnValidateRecord", win32more.NetworkManagement.P2P.PFNPEER_VALIDATE_RECORD),
        ("pfnSecureRecord", win32more.NetworkManagement.P2P.PFNPEER_SECURE_RECORD),
        ("pfnFreeSecurityData", win32more.NetworkManagement.P2P.PFNPEER_FREE_SECURITY_DATA),
        ("pfnAuthFailed", win32more.NetworkManagement.P2P.PFNPEER_ON_PASSWORD_AUTH_FAILED),
    ]
    return PEER_SECURITY_INTERFACE
PEER_GROUP_EVENT_TYPE = Int32
PEER_GROUP_EVENT_STATUS_CHANGED = 1
PEER_GROUP_EVENT_PROPERTY_CHANGED = 2
PEER_GROUP_EVENT_RECORD_CHANGED = 3
PEER_GROUP_EVENT_DIRECT_CONNECTION = 4
PEER_GROUP_EVENT_NEIGHBOR_CONNECTION = 5
PEER_GROUP_EVENT_INCOMING_DATA = 6
PEER_GROUP_EVENT_MEMBER_CHANGED = 8
PEER_GROUP_EVENT_CONNECTION_FAILED = 10
PEER_GROUP_EVENT_AUTHENTICATION_FAILED = 11
PEER_GROUP_STATUS = Int32
PEER_GROUP_STATUS_LISTENING = 1
PEER_GROUP_STATUS_HAS_CONNECTIONS = 2
PEER_GROUP_PROPERTY_FLAGS = Int32
PEER_MEMBER_DATA_OPTIONAL = 1
PEER_DISABLE_PRESENCE = 2
PEER_DEFER_EXPIRATION = 4
PEER_GROUP_AUTHENTICATION_SCHEME = Int32
PEER_GROUP_GMC_AUTHENTICATION = 1
PEER_GROUP_PASSWORD_AUTHENTICATION = 2
PEER_MEMBER_FLAGS = Int32
PEER_MEMBER_PRESENT = 1
PEER_MEMBER_CHANGE_TYPE = Int32
PEER_MEMBER_CONNECTED = 1
PEER_MEMBER_DISCONNECTED = 2
PEER_MEMBER_UPDATED = 3
PEER_MEMBER_JOINED = 4
PEER_MEMBER_LEFT = 5
PEER_GROUP_ISSUE_CREDENTIAL_FLAGS = Int32
PEER_GROUP_STORE_CREDENTIALS = 1
def _define_PEER_CREDENTIAL_INFO_head():
    class PEER_CREDENTIAL_INFO(Structure):
        pass
    return PEER_CREDENTIAL_INFO
def _define_PEER_CREDENTIAL_INFO():
    PEER_CREDENTIAL_INFO = win32more.NetworkManagement.P2P.PEER_CREDENTIAL_INFO_head
    PEER_CREDENTIAL_INFO._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("pwzFriendlyName", win32more.Foundation.PWSTR),
        ("pPublicKey", POINTER(win32more.Security.Cryptography.CERT_PUBLIC_KEY_INFO_head)),
        ("pwzIssuerPeerName", win32more.Foundation.PWSTR),
        ("pwzIssuerFriendlyName", win32more.Foundation.PWSTR),
        ("ftValidityStart", win32more.Foundation.FILETIME),
        ("ftValidityEnd", win32more.Foundation.FILETIME),
        ("cRoles", UInt32),
        ("pRoles", POINTER(Guid)),
    ]
    return PEER_CREDENTIAL_INFO
def _define_PEER_MEMBER_head():
    class PEER_MEMBER(Structure):
        pass
    return PEER_MEMBER
def _define_PEER_MEMBER():
    PEER_MEMBER = win32more.NetworkManagement.P2P.PEER_MEMBER_head
    PEER_MEMBER._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("pwzIdentity", win32more.Foundation.PWSTR),
        ("pwzAttributes", win32more.Foundation.PWSTR),
        ("ullNodeId", UInt64),
        ("cAddresses", UInt32),
        ("pAddresses", POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head)),
        ("pCredentialInfo", POINTER(win32more.NetworkManagement.P2P.PEER_CREDENTIAL_INFO_head)),
    ]
    return PEER_MEMBER
def _define_PEER_INVITATION_INFO_head():
    class PEER_INVITATION_INFO(Structure):
        pass
    return PEER_INVITATION_INFO
def _define_PEER_INVITATION_INFO():
    PEER_INVITATION_INFO = win32more.NetworkManagement.P2P.PEER_INVITATION_INFO_head
    PEER_INVITATION_INFO._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("pwzCloudName", win32more.Foundation.PWSTR),
        ("dwScope", UInt32),
        ("dwCloudFlags", UInt32),
        ("pwzGroupPeerName", win32more.Foundation.PWSTR),
        ("pwzIssuerPeerName", win32more.Foundation.PWSTR),
        ("pwzSubjectPeerName", win32more.Foundation.PWSTR),
        ("pwzGroupFriendlyName", win32more.Foundation.PWSTR),
        ("pwzIssuerFriendlyName", win32more.Foundation.PWSTR),
        ("pwzSubjectFriendlyName", win32more.Foundation.PWSTR),
        ("ftValidityStart", win32more.Foundation.FILETIME),
        ("ftValidityEnd", win32more.Foundation.FILETIME),
        ("cRoles", UInt32),
        ("pRoles", POINTER(Guid)),
        ("cClassifiers", UInt32),
        ("ppwzClassifiers", POINTER(win32more.Foundation.PWSTR)),
        ("pSubjectPublicKey", POINTER(win32more.Security.Cryptography.CERT_PUBLIC_KEY_INFO_head)),
        ("authScheme", win32more.NetworkManagement.P2P.PEER_GROUP_AUTHENTICATION_SCHEME),
    ]
    return PEER_INVITATION_INFO
def _define_PEER_GROUP_PROPERTIES_head():
    class PEER_GROUP_PROPERTIES(Structure):
        pass
    return PEER_GROUP_PROPERTIES
def _define_PEER_GROUP_PROPERTIES():
    PEER_GROUP_PROPERTIES = win32more.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head
    PEER_GROUP_PROPERTIES._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("pwzCloud", win32more.Foundation.PWSTR),
        ("pwzClassifier", win32more.Foundation.PWSTR),
        ("pwzGroupPeerName", win32more.Foundation.PWSTR),
        ("pwzCreatorPeerName", win32more.Foundation.PWSTR),
        ("pwzFriendlyName", win32more.Foundation.PWSTR),
        ("pwzComment", win32more.Foundation.PWSTR),
        ("ulMemberDataLifetime", UInt32),
        ("ulPresenceLifetime", UInt32),
        ("dwAuthenticationSchemes", UInt32),
        ("pwzGroupPassword", win32more.Foundation.PWSTR),
        ("groupPasswordRole", Guid),
    ]
    return PEER_GROUP_PROPERTIES
def _define_PEER_EVENT_MEMBER_CHANGE_DATA_head():
    class PEER_EVENT_MEMBER_CHANGE_DATA(Structure):
        pass
    return PEER_EVENT_MEMBER_CHANGE_DATA
def _define_PEER_EVENT_MEMBER_CHANGE_DATA():
    PEER_EVENT_MEMBER_CHANGE_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_MEMBER_CHANGE_DATA_head
    PEER_EVENT_MEMBER_CHANGE_DATA._fields_ = [
        ("dwSize", UInt32),
        ("changeType", win32more.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE),
        ("pwzIdentity", win32more.Foundation.PWSTR),
    ]
    return PEER_EVENT_MEMBER_CHANGE_DATA
def _define_PEER_GROUP_EVENT_REGISTRATION_head():
    class PEER_GROUP_EVENT_REGISTRATION(Structure):
        pass
    return PEER_GROUP_EVENT_REGISTRATION
def _define_PEER_GROUP_EVENT_REGISTRATION():
    PEER_GROUP_EVENT_REGISTRATION = win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_REGISTRATION_head
    PEER_GROUP_EVENT_REGISTRATION._fields_ = [
        ("eventType", win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE),
        ("pType", POINTER(Guid)),
    ]
    return PEER_GROUP_EVENT_REGISTRATION
def _define_PEER_GROUP_EVENT_DATA_head():
    class PEER_GROUP_EVENT_DATA(Structure):
        pass
    return PEER_GROUP_EVENT_DATA
def _define_PEER_GROUP_EVENT_DATA():
    PEER_GROUP_EVENT_DATA = win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_DATA_head
    class PEER_GROUP_EVENT_DATA__Anonymous_e__Union(Union):
        pass
    PEER_GROUP_EVENT_DATA__Anonymous_e__Union._fields_ = [
        ("dwStatus", win32more.NetworkManagement.P2P.PEER_GROUP_STATUS),
        ("incomingData", win32more.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA),
        ("recordChangeData", win32more.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA),
        ("connectionChangeData", win32more.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA),
        ("memberChangeData", win32more.NetworkManagement.P2P.PEER_EVENT_MEMBER_CHANGE_DATA),
        ("hrConnectionFailedReason", win32more.Foundation.HRESULT),
    ]
    PEER_GROUP_EVENT_DATA._anonymous_ = [
        'Anonymous',
    ]
    PEER_GROUP_EVENT_DATA._fields_ = [
        ("eventType", win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE),
        ("Anonymous", PEER_GROUP_EVENT_DATA__Anonymous_e__Union),
    ]
    return PEER_GROUP_EVENT_DATA
def _define_PEER_NAME_PAIR_head():
    class PEER_NAME_PAIR(Structure):
        pass
    return PEER_NAME_PAIR
def _define_PEER_NAME_PAIR():
    PEER_NAME_PAIR = win32more.NetworkManagement.P2P.PEER_NAME_PAIR_head
    PEER_NAME_PAIR._fields_ = [
        ("dwSize", UInt32),
        ("pwzPeerName", win32more.Foundation.PWSTR),
        ("pwzFriendlyName", win32more.Foundation.PWSTR),
    ]
    return PEER_NAME_PAIR
PEER_SIGNIN_FLAGS = Int32
PEER_SIGNIN_NONE = 0
PEER_SIGNIN_NEAR_ME = 1
PEER_SIGNIN_INTERNET = 2
PEER_SIGNIN_ALL = 3
PEER_WATCH_PERMISSION = Int32
PEER_WATCH_BLOCKED = 0
PEER_WATCH_ALLOWED = 1
PEER_PUBLICATION_SCOPE = Int32
PEER_PUBLICATION_SCOPE_NONE = 0
PEER_PUBLICATION_SCOPE_NEAR_ME = 1
PEER_PUBLICATION_SCOPE_INTERNET = 2
PEER_PUBLICATION_SCOPE_ALL = 3
def _define_PEER_APPLICATION_head():
    class PEER_APPLICATION(Structure):
        pass
    return PEER_APPLICATION
def _define_PEER_APPLICATION():
    PEER_APPLICATION = win32more.NetworkManagement.P2P.PEER_APPLICATION_head
    PEER_APPLICATION._fields_ = [
        ("id", Guid),
        ("data", win32more.NetworkManagement.P2P.PEER_DATA),
        ("pwzDescription", win32more.Foundation.PWSTR),
    ]
    return PEER_APPLICATION
def _define_PEER_OBJECT_head():
    class PEER_OBJECT(Structure):
        pass
    return PEER_OBJECT
def _define_PEER_OBJECT():
    PEER_OBJECT = win32more.NetworkManagement.P2P.PEER_OBJECT_head
    PEER_OBJECT._fields_ = [
        ("id", Guid),
        ("data", win32more.NetworkManagement.P2P.PEER_DATA),
        ("dwPublicationScope", UInt32),
    ]
    return PEER_OBJECT
def _define_PEER_CONTACT_head():
    class PEER_CONTACT(Structure):
        pass
    return PEER_CONTACT
def _define_PEER_CONTACT():
    PEER_CONTACT = win32more.NetworkManagement.P2P.PEER_CONTACT_head
    PEER_CONTACT._fields_ = [
        ("pwzPeerName", win32more.Foundation.PWSTR),
        ("pwzNickName", win32more.Foundation.PWSTR),
        ("pwzDisplayName", win32more.Foundation.PWSTR),
        ("pwzEmailAddress", win32more.Foundation.PWSTR),
        ("fWatch", win32more.Foundation.BOOL),
        ("WatcherPermissions", win32more.NetworkManagement.P2P.PEER_WATCH_PERMISSION),
        ("credentials", win32more.NetworkManagement.P2P.PEER_DATA),
    ]
    return PEER_CONTACT
def _define_PEER_ENDPOINT_head():
    class PEER_ENDPOINT(Structure):
        pass
    return PEER_ENDPOINT
def _define_PEER_ENDPOINT():
    PEER_ENDPOINT = win32more.NetworkManagement.P2P.PEER_ENDPOINT_head
    PEER_ENDPOINT._fields_ = [
        ("address", win32more.NetworkManagement.P2P.PEER_ADDRESS),
        ("pwzEndpointName", win32more.Foundation.PWSTR),
    ]
    return PEER_ENDPOINT
def _define_PEER_PEOPLE_NEAR_ME_head():
    class PEER_PEOPLE_NEAR_ME(Structure):
        pass
    return PEER_PEOPLE_NEAR_ME
def _define_PEER_PEOPLE_NEAR_ME():
    PEER_PEOPLE_NEAR_ME = win32more.NetworkManagement.P2P.PEER_PEOPLE_NEAR_ME_head
    PEER_PEOPLE_NEAR_ME._fields_ = [
        ("pwzNickName", win32more.Foundation.PWSTR),
        ("endpoint", win32more.NetworkManagement.P2P.PEER_ENDPOINT),
        ("id", Guid),
    ]
    return PEER_PEOPLE_NEAR_ME
PEER_INVITATION_RESPONSE_TYPE = Int32
PEER_INVITATION_RESPONSE_DECLINED = 0
PEER_INVITATION_RESPONSE_ACCEPTED = 1
PEER_INVITATION_RESPONSE_EXPIRED = 2
PEER_INVITATION_RESPONSE_ERROR = 3
PEER_APPLICATION_REGISTRATION_TYPE = Int32
PEER_APPLICATION_CURRENT_USER = 0
PEER_APPLICATION_ALL_USERS = 1
def _define_PEER_INVITATION_head():
    class PEER_INVITATION(Structure):
        pass
    return PEER_INVITATION
def _define_PEER_INVITATION():
    PEER_INVITATION = win32more.NetworkManagement.P2P.PEER_INVITATION_head
    PEER_INVITATION._fields_ = [
        ("applicationId", Guid),
        ("applicationData", win32more.NetworkManagement.P2P.PEER_DATA),
        ("pwzMessage", win32more.Foundation.PWSTR),
    ]
    return PEER_INVITATION
def _define_PEER_INVITATION_RESPONSE_head():
    class PEER_INVITATION_RESPONSE(Structure):
        pass
    return PEER_INVITATION_RESPONSE
def _define_PEER_INVITATION_RESPONSE():
    PEER_INVITATION_RESPONSE = win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head
    PEER_INVITATION_RESPONSE._fields_ = [
        ("action", win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE),
        ("pwzMessage", win32more.Foundation.PWSTR),
        ("hrExtendedInfo", win32more.Foundation.HRESULT),
    ]
    return PEER_INVITATION_RESPONSE
def _define_PEER_APP_LAUNCH_INFO_head():
    class PEER_APP_LAUNCH_INFO(Structure):
        pass
    return PEER_APP_LAUNCH_INFO
def _define_PEER_APP_LAUNCH_INFO():
    PEER_APP_LAUNCH_INFO = win32more.NetworkManagement.P2P.PEER_APP_LAUNCH_INFO_head
    PEER_APP_LAUNCH_INFO._fields_ = [
        ("pContact", POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)),
        ("pEndpoint", POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)),
        ("pInvitation", POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head)),
    ]
    return PEER_APP_LAUNCH_INFO
def _define_PEER_APPLICATION_REGISTRATION_INFO_head():
    class PEER_APPLICATION_REGISTRATION_INFO(Structure):
        pass
    return PEER_APPLICATION_REGISTRATION_INFO
def _define_PEER_APPLICATION_REGISTRATION_INFO():
    PEER_APPLICATION_REGISTRATION_INFO = win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO_head
    PEER_APPLICATION_REGISTRATION_INFO._fields_ = [
        ("application", win32more.NetworkManagement.P2P.PEER_APPLICATION),
        ("pwzApplicationToLaunch", win32more.Foundation.PWSTR),
        ("pwzApplicationArguments", win32more.Foundation.PWSTR),
        ("dwPublicationScope", UInt32),
    ]
    return PEER_APPLICATION_REGISTRATION_INFO
PEER_PRESENCE_STATUS = Int32
PEER_PRESENCE_OFFLINE = 0
PEER_PRESENCE_OUT_TO_LUNCH = 1
PEER_PRESENCE_AWAY = 2
PEER_PRESENCE_BE_RIGHT_BACK = 3
PEER_PRESENCE_IDLE = 4
PEER_PRESENCE_BUSY = 5
PEER_PRESENCE_ON_THE_PHONE = 6
PEER_PRESENCE_ONLINE = 7
def _define_PEER_PRESENCE_INFO_head():
    class PEER_PRESENCE_INFO(Structure):
        pass
    return PEER_PRESENCE_INFO
def _define_PEER_PRESENCE_INFO():
    PEER_PRESENCE_INFO = win32more.NetworkManagement.P2P.PEER_PRESENCE_INFO_head
    PEER_PRESENCE_INFO._fields_ = [
        ("status", win32more.NetworkManagement.P2P.PEER_PRESENCE_STATUS),
        ("pwzDescriptiveText", win32more.Foundation.PWSTR),
    ]
    return PEER_PRESENCE_INFO
PEER_CHANGE_TYPE = Int32
PEER_CHANGE_ADDED = 0
PEER_CHANGE_DELETED = 1
PEER_CHANGE_UPDATED = 2
PEER_COLLAB_EVENT_TYPE = Int32
PEER_EVENT_WATCHLIST_CHANGED = 1
PEER_EVENT_ENDPOINT_CHANGED = 2
PEER_EVENT_ENDPOINT_PRESENCE_CHANGED = 3
PEER_EVENT_ENDPOINT_APPLICATION_CHANGED = 4
PEER_EVENT_ENDPOINT_OBJECT_CHANGED = 5
PEER_EVENT_MY_ENDPOINT_CHANGED = 6
PEER_EVENT_MY_PRESENCE_CHANGED = 7
PEER_EVENT_MY_APPLICATION_CHANGED = 8
PEER_EVENT_MY_OBJECT_CHANGED = 9
PEER_EVENT_PEOPLE_NEAR_ME_CHANGED = 10
PEER_EVENT_REQUEST_STATUS_CHANGED = 11
def _define_PEER_COLLAB_EVENT_REGISTRATION_head():
    class PEER_COLLAB_EVENT_REGISTRATION(Structure):
        pass
    return PEER_COLLAB_EVENT_REGISTRATION
def _define_PEER_COLLAB_EVENT_REGISTRATION():
    PEER_COLLAB_EVENT_REGISTRATION = win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_REGISTRATION_head
    PEER_COLLAB_EVENT_REGISTRATION._fields_ = [
        ("eventType", win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE),
        ("pInstance", POINTER(Guid)),
    ]
    return PEER_COLLAB_EVENT_REGISTRATION
def _define_PEER_EVENT_WATCHLIST_CHANGED_DATA_head():
    class PEER_EVENT_WATCHLIST_CHANGED_DATA(Structure):
        pass
    return PEER_EVENT_WATCHLIST_CHANGED_DATA
def _define_PEER_EVENT_WATCHLIST_CHANGED_DATA():
    PEER_EVENT_WATCHLIST_CHANGED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_WATCHLIST_CHANGED_DATA_head
    PEER_EVENT_WATCHLIST_CHANGED_DATA._fields_ = [
        ("pContact", POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)),
        ("changeType", win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE),
    ]
    return PEER_EVENT_WATCHLIST_CHANGED_DATA
def _define_PEER_EVENT_PRESENCE_CHANGED_DATA_head():
    class PEER_EVENT_PRESENCE_CHANGED_DATA(Structure):
        pass
    return PEER_EVENT_PRESENCE_CHANGED_DATA
def _define_PEER_EVENT_PRESENCE_CHANGED_DATA():
    PEER_EVENT_PRESENCE_CHANGED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_PRESENCE_CHANGED_DATA_head
    PEER_EVENT_PRESENCE_CHANGED_DATA._fields_ = [
        ("pContact", POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)),
        ("pEndpoint", POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)),
        ("changeType", win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE),
        ("pPresenceInfo", POINTER(win32more.NetworkManagement.P2P.PEER_PRESENCE_INFO_head)),
    ]
    return PEER_EVENT_PRESENCE_CHANGED_DATA
def _define_PEER_EVENT_APPLICATION_CHANGED_DATA_head():
    class PEER_EVENT_APPLICATION_CHANGED_DATA(Structure):
        pass
    return PEER_EVENT_APPLICATION_CHANGED_DATA
def _define_PEER_EVENT_APPLICATION_CHANGED_DATA():
    PEER_EVENT_APPLICATION_CHANGED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_APPLICATION_CHANGED_DATA_head
    PEER_EVENT_APPLICATION_CHANGED_DATA._fields_ = [
        ("pContact", POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)),
        ("pEndpoint", POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)),
        ("changeType", win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE),
        ("pApplication", POINTER(win32more.NetworkManagement.P2P.PEER_APPLICATION_head)),
    ]
    return PEER_EVENT_APPLICATION_CHANGED_DATA
def _define_PEER_EVENT_OBJECT_CHANGED_DATA_head():
    class PEER_EVENT_OBJECT_CHANGED_DATA(Structure):
        pass
    return PEER_EVENT_OBJECT_CHANGED_DATA
def _define_PEER_EVENT_OBJECT_CHANGED_DATA():
    PEER_EVENT_OBJECT_CHANGED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_OBJECT_CHANGED_DATA_head
    PEER_EVENT_OBJECT_CHANGED_DATA._fields_ = [
        ("pContact", POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)),
        ("pEndpoint", POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)),
        ("changeType", win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE),
        ("pObject", POINTER(win32more.NetworkManagement.P2P.PEER_OBJECT_head)),
    ]
    return PEER_EVENT_OBJECT_CHANGED_DATA
def _define_PEER_EVENT_ENDPOINT_CHANGED_DATA_head():
    class PEER_EVENT_ENDPOINT_CHANGED_DATA(Structure):
        pass
    return PEER_EVENT_ENDPOINT_CHANGED_DATA
def _define_PEER_EVENT_ENDPOINT_CHANGED_DATA():
    PEER_EVENT_ENDPOINT_CHANGED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_ENDPOINT_CHANGED_DATA_head
    PEER_EVENT_ENDPOINT_CHANGED_DATA._fields_ = [
        ("pContact", POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)),
        ("pEndpoint", POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)),
    ]
    return PEER_EVENT_ENDPOINT_CHANGED_DATA
def _define_PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA_head():
    class PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA(Structure):
        pass
    return PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA
def _define_PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA():
    PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA_head
    PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA._fields_ = [
        ("changeType", win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE),
        ("pPeopleNearMe", POINTER(win32more.NetworkManagement.P2P.PEER_PEOPLE_NEAR_ME_head)),
    ]
    return PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA
def _define_PEER_EVENT_REQUEST_STATUS_CHANGED_DATA_head():
    class PEER_EVENT_REQUEST_STATUS_CHANGED_DATA(Structure):
        pass
    return PEER_EVENT_REQUEST_STATUS_CHANGED_DATA
def _define_PEER_EVENT_REQUEST_STATUS_CHANGED_DATA():
    PEER_EVENT_REQUEST_STATUS_CHANGED_DATA = win32more.NetworkManagement.P2P.PEER_EVENT_REQUEST_STATUS_CHANGED_DATA_head
    PEER_EVENT_REQUEST_STATUS_CHANGED_DATA._fields_ = [
        ("pEndpoint", POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)),
        ("hrChange", win32more.Foundation.HRESULT),
    ]
    return PEER_EVENT_REQUEST_STATUS_CHANGED_DATA
def _define_PEER_COLLAB_EVENT_DATA_head():
    class PEER_COLLAB_EVENT_DATA(Structure):
        pass
    return PEER_COLLAB_EVENT_DATA
def _define_PEER_COLLAB_EVENT_DATA():
    PEER_COLLAB_EVENT_DATA = win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_DATA_head
    class PEER_COLLAB_EVENT_DATA__Anonymous_e__Union(Union):
        pass
    PEER_COLLAB_EVENT_DATA__Anonymous_e__Union._fields_ = [
        ("watchListChangedData", win32more.NetworkManagement.P2P.PEER_EVENT_WATCHLIST_CHANGED_DATA),
        ("presenceChangedData", win32more.NetworkManagement.P2P.PEER_EVENT_PRESENCE_CHANGED_DATA),
        ("applicationChangedData", win32more.NetworkManagement.P2P.PEER_EVENT_APPLICATION_CHANGED_DATA),
        ("objectChangedData", win32more.NetworkManagement.P2P.PEER_EVENT_OBJECT_CHANGED_DATA),
        ("endpointChangedData", win32more.NetworkManagement.P2P.PEER_EVENT_ENDPOINT_CHANGED_DATA),
        ("peopleNearMeChangedData", win32more.NetworkManagement.P2P.PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA),
        ("requestStatusChangedData", win32more.NetworkManagement.P2P.PEER_EVENT_REQUEST_STATUS_CHANGED_DATA),
    ]
    PEER_COLLAB_EVENT_DATA._anonymous_ = [
        'Anonymous',
    ]
    PEER_COLLAB_EVENT_DATA._fields_ = [
        ("eventType", win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE),
        ("Anonymous", PEER_COLLAB_EVENT_DATA__Anonymous_e__Union),
    ]
    return PEER_COLLAB_EVENT_DATA
def _define_PEER_PNRP_ENDPOINT_INFO_head():
    class PEER_PNRP_ENDPOINT_INFO(Structure):
        pass
    return PEER_PNRP_ENDPOINT_INFO
def _define_PEER_PNRP_ENDPOINT_INFO():
    PEER_PNRP_ENDPOINT_INFO = win32more.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO_head
    PEER_PNRP_ENDPOINT_INFO._fields_ = [
        ("pwzPeerName", win32more.Foundation.PWSTR),
        ("cAddresses", UInt32),
        ("ppAddresses", POINTER(POINTER(win32more.Networking.WinSock.SOCKADDR_head))),
        ("pwzComment", win32more.Foundation.PWSTR),
        ("payload", win32more.NetworkManagement.P2P.PEER_DATA),
    ]
    return PEER_PNRP_ENDPOINT_INFO
def _define_PEER_PNRP_CLOUD_INFO_head():
    class PEER_PNRP_CLOUD_INFO(Structure):
        pass
    return PEER_PNRP_CLOUD_INFO
def _define_PEER_PNRP_CLOUD_INFO():
    PEER_PNRP_CLOUD_INFO = win32more.NetworkManagement.P2P.PEER_PNRP_CLOUD_INFO_head
    PEER_PNRP_CLOUD_INFO._fields_ = [
        ("pwzCloudName", win32more.Foundation.PWSTR),
        ("dwScope", win32more.NetworkManagement.P2P.PNRP_SCOPE),
        ("dwScopeId", UInt32),
    ]
    return PEER_PNRP_CLOUD_INFO
def _define_PEER_PNRP_REGISTRATION_INFO_head():
    class PEER_PNRP_REGISTRATION_INFO(Structure):
        pass
    return PEER_PNRP_REGISTRATION_INFO
def _define_PEER_PNRP_REGISTRATION_INFO():
    PEER_PNRP_REGISTRATION_INFO = win32more.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO_head
    PEER_PNRP_REGISTRATION_INFO._fields_ = [
        ("pwzCloudName", win32more.Foundation.PWSTR),
        ("pwzPublishingIdentity", win32more.Foundation.PWSTR),
        ("cAddresses", UInt32),
        ("ppAddresses", POINTER(POINTER(win32more.Networking.WinSock.SOCKADDR_head))),
        ("wPort", UInt16),
        ("pwzComment", win32more.Foundation.PWSTR),
        ("payload", win32more.NetworkManagement.P2P.PEER_DATA),
    ]
    return PEER_PNRP_REGISTRATION_INFO
DRT_SCOPE = Int32
DRT_GLOBAL_SCOPE = 1
DRT_SITE_LOCAL_SCOPE = 2
DRT_LINK_LOCAL_SCOPE = 3
DRT_STATUS = Int32
DRT_ACTIVE = 0
DRT_ALONE = 1
DRT_NO_NETWORK = 10
DRT_FAULTED = 20
DRT_MATCH_TYPE = Int32
DRT_MATCH_EXACT = 0
DRT_MATCH_NEAR = 1
DRT_MATCH_INTERMEDIATE = 2
DRT_LEAFSET_KEY_CHANGE_TYPE = Int32
DRT_LEAFSET_KEY_ADDED = 0
DRT_LEAFSET_KEY_DELETED = 1
DRT_EVENT_TYPE = Int32
DRT_EVENT_STATUS_CHANGED = 0
DRT_EVENT_LEAFSET_KEY_CHANGED = 1
DRT_EVENT_REGISTRATION_STATE_CHANGED = 2
DRT_SECURITY_MODE = Int32
DRT_SECURE_RESOLVE = 0
DRT_SECURE_MEMBERSHIP = 1
DRT_SECURE_CONFIDENTIALPAYLOAD = 2
DRT_REGISTRATION_STATE = Int32
DRT_REGISTRATION_STATE_UNRESOLVEABLE = 1
DRT_ADDRESS_FLAGS = Int32
DRT_ADDRESS_FLAG_ACCEPTED = 1
DRT_ADDRESS_FLAG_REJECTED = 2
DRT_ADDRESS_FLAG_UNREACHABLE = 4
DRT_ADDRESS_FLAG_LOOP = 8
DRT_ADDRESS_FLAG_TOO_BUSY = 16
DRT_ADDRESS_FLAG_BAD_VALIDATE_ID = 32
DRT_ADDRESS_FLAG_SUSPECT_UNREGISTERED_ID = 64
DRT_ADDRESS_FLAG_INQUIRE = 128
def _define_DRT_DATA_head():
    class DRT_DATA(Structure):
        pass
    return DRT_DATA
def _define_DRT_DATA():
    DRT_DATA = win32more.NetworkManagement.P2P.DRT_DATA_head
    DRT_DATA._fields_ = [
        ("cb", UInt32),
        ("pb", c_char_p_no),
    ]
    return DRT_DATA
def _define_DRT_REGISTRATION_head():
    class DRT_REGISTRATION(Structure):
        pass
    return DRT_REGISTRATION
def _define_DRT_REGISTRATION():
    DRT_REGISTRATION = win32more.NetworkManagement.P2P.DRT_REGISTRATION_head
    DRT_REGISTRATION._fields_ = [
        ("key", win32more.NetworkManagement.P2P.DRT_DATA),
        ("appData", win32more.NetworkManagement.P2P.DRT_DATA),
    ]
    return DRT_REGISTRATION
def _define_DRT_SECURITY_PROVIDER_head():
    class DRT_SECURITY_PROVIDER(Structure):
        pass
    return DRT_SECURITY_PROVIDER
def _define_DRT_SECURITY_PROVIDER():
    DRT_SECURITY_PROVIDER = win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head
    DRT_SECURITY_PROVIDER._fields_ = [
        ("pvContext", c_void_p),
        ("Attach", IntPtr),
        ("Detach", IntPtr),
        ("RegisterKey", IntPtr),
        ("UnregisterKey", IntPtr),
        ("ValidateAndUnpackPayload", IntPtr),
        ("SecureAndPackPayload", IntPtr),
        ("FreeData", IntPtr),
        ("EncryptData", IntPtr),
        ("DecryptData", IntPtr),
        ("GetSerializedCredential", IntPtr),
        ("ValidateRemoteCredential", IntPtr),
        ("SignData", IntPtr),
        ("VerifyData", IntPtr),
    ]
    return DRT_SECURITY_PROVIDER
def _define_DRT_BOOTSTRAP_RESOLVE_CALLBACK():
    return CFUNCTYPE(Void,win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS_LIST_head),win32more.Foundation.BOOL, use_last_error=False)
def _define_DRT_BOOTSTRAP_PROVIDER_head():
    class DRT_BOOTSTRAP_PROVIDER(Structure):
        pass
    return DRT_BOOTSTRAP_PROVIDER
def _define_DRT_BOOTSTRAP_PROVIDER():
    DRT_BOOTSTRAP_PROVIDER = win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head
    DRT_BOOTSTRAP_PROVIDER._fields_ = [
        ("pvContext", c_void_p),
        ("Attach", IntPtr),
        ("Detach", IntPtr),
        ("InitResolve", IntPtr),
        ("IssueResolve", IntPtr),
        ("EndResolve", IntPtr),
        ("Register", IntPtr),
        ("Unregister", IntPtr),
    ]
    return DRT_BOOTSTRAP_PROVIDER
def _define_DRT_SETTINGS_head():
    class DRT_SETTINGS(Structure):
        pass
    return DRT_SETTINGS
def _define_DRT_SETTINGS():
    DRT_SETTINGS = win32more.NetworkManagement.P2P.DRT_SETTINGS_head
    DRT_SETTINGS._fields_ = [
        ("dwSize", UInt32),
        ("cbKey", UInt32),
        ("bProtocolMajorVersion", Byte),
        ("bProtocolMinorVersion", Byte),
        ("ulMaxRoutingAddresses", UInt32),
        ("pwzDrtInstancePrefix", win32more.Foundation.PWSTR),
        ("hTransport", c_void_p),
        ("pSecurityProvider", POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)),
        ("pBootstrapProvider", POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)),
        ("eSecurityMode", win32more.NetworkManagement.P2P.DRT_SECURITY_MODE),
    ]
    return DRT_SETTINGS
def _define_DRT_SEARCH_INFO_head():
    class DRT_SEARCH_INFO(Structure):
        pass
    return DRT_SEARCH_INFO
def _define_DRT_SEARCH_INFO():
    DRT_SEARCH_INFO = win32more.NetworkManagement.P2P.DRT_SEARCH_INFO_head
    DRT_SEARCH_INFO._fields_ = [
        ("dwSize", UInt32),
        ("fIterative", win32more.Foundation.BOOL),
        ("fAllowCurrentInstanceMatch", win32more.Foundation.BOOL),
        ("fAnyMatchInRange", win32more.Foundation.BOOL),
        ("cMaxEndpoints", UInt32),
        ("pMaximumKey", POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head)),
        ("pMinimumKey", POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head)),
    ]
    return DRT_SEARCH_INFO
def _define_DRT_ADDRESS_head():
    class DRT_ADDRESS(Structure):
        pass
    return DRT_ADDRESS
def _define_DRT_ADDRESS():
    DRT_ADDRESS = win32more.NetworkManagement.P2P.DRT_ADDRESS_head
    DRT_ADDRESS._fields_ = [
        ("socketAddress", win32more.Networking.WinSock.SOCKADDR_STORAGE),
        ("flags", UInt32),
        ("nearness", Int32),
        ("latency", UInt32),
    ]
    return DRT_ADDRESS
def _define_DRT_ADDRESS_LIST_head():
    class DRT_ADDRESS_LIST(Structure):
        pass
    return DRT_ADDRESS_LIST
def _define_DRT_ADDRESS_LIST():
    DRT_ADDRESS_LIST = win32more.NetworkManagement.P2P.DRT_ADDRESS_LIST_head
    DRT_ADDRESS_LIST._fields_ = [
        ("AddressCount", UInt32),
        ("AddressList", win32more.NetworkManagement.P2P.DRT_ADDRESS * 0),
    ]
    return DRT_ADDRESS_LIST
def _define_DRT_SEARCH_RESULT_head():
    class DRT_SEARCH_RESULT(Structure):
        pass
    return DRT_SEARCH_RESULT
def _define_DRT_SEARCH_RESULT():
    DRT_SEARCH_RESULT = win32more.NetworkManagement.P2P.DRT_SEARCH_RESULT_head
    DRT_SEARCH_RESULT._fields_ = [
        ("dwSize", UInt32),
        ("type", win32more.NetworkManagement.P2P.DRT_MATCH_TYPE),
        ("pvContext", c_void_p),
        ("registration", win32more.NetworkManagement.P2P.DRT_REGISTRATION),
    ]
    return DRT_SEARCH_RESULT
def _define_DRT_EVENT_DATA_head():
    class DRT_EVENT_DATA(Structure):
        pass
    return DRT_EVENT_DATA
def _define_DRT_EVENT_DATA():
    DRT_EVENT_DATA = win32more.NetworkManagement.P2P.DRT_EVENT_DATA_head
    class DRT_EVENT_DATA__Anonymous_e__Union(Union):
        pass
    class DRT_EVENT_DATA__Anonymous_e__Union__statusChange_e__Struct(Structure):
        pass
    class DRT_EVENT_DATA__Anonymous_e__Union__statusChange_e__Struct__bootstrapAddresses_e__Struct(Structure):
        pass
    DRT_EVENT_DATA__Anonymous_e__Union__statusChange_e__Struct__bootstrapAddresses_e__Struct._fields_ = [
        ("cntAddress", UInt32),
        ("pAddresses", POINTER(win32more.Networking.WinSock.SOCKADDR_STORAGE_head)),
    ]
    DRT_EVENT_DATA__Anonymous_e__Union__statusChange_e__Struct._fields_ = [
        ("status", win32more.NetworkManagement.P2P.DRT_STATUS),
        ("bootstrapAddresses", DRT_EVENT_DATA__Anonymous_e__Union__statusChange_e__Struct__bootstrapAddresses_e__Struct),
    ]
    class DRT_EVENT_DATA__Anonymous_e__Union__leafsetKeyChange_e__Struct(Structure):
        pass
    DRT_EVENT_DATA__Anonymous_e__Union__leafsetKeyChange_e__Struct._fields_ = [
        ("change", win32more.NetworkManagement.P2P.DRT_LEAFSET_KEY_CHANGE_TYPE),
        ("localKey", win32more.NetworkManagement.P2P.DRT_DATA),
        ("remoteKey", win32more.NetworkManagement.P2P.DRT_DATA),
    ]
    class DRT_EVENT_DATA__Anonymous_e__Union__registrationStateChange_e__Struct(Structure):
        pass
    DRT_EVENT_DATA__Anonymous_e__Union__registrationStateChange_e__Struct._fields_ = [
        ("state", win32more.NetworkManagement.P2P.DRT_REGISTRATION_STATE),
        ("localKey", win32more.NetworkManagement.P2P.DRT_DATA),
    ]
    DRT_EVENT_DATA__Anonymous_e__Union._fields_ = [
        ("leafsetKeyChange", DRT_EVENT_DATA__Anonymous_e__Union__leafsetKeyChange_e__Struct),
        ("registrationStateChange", DRT_EVENT_DATA__Anonymous_e__Union__registrationStateChange_e__Struct),
        ("statusChange", DRT_EVENT_DATA__Anonymous_e__Union__statusChange_e__Struct),
    ]
    DRT_EVENT_DATA._anonymous_ = [
        'Anonymous',
    ]
    DRT_EVENT_DATA._fields_ = [
        ("type", win32more.NetworkManagement.P2P.DRT_EVENT_TYPE),
        ("hr", win32more.Foundation.HRESULT),
        ("pvContext", c_void_p),
        ("Anonymous", DRT_EVENT_DATA__Anonymous_e__Union),
    ]
    return DRT_EVENT_DATA
PEERDIST_STATUS = Int32
PEERDIST_STATUS_DISABLED = 0
PEERDIST_STATUS_UNAVAILABLE = 1
PEERDIST_STATUS_AVAILABLE = 2
def _define_PEERDIST_PUBLICATION_OPTIONS_head():
    class PEERDIST_PUBLICATION_OPTIONS(Structure):
        pass
    return PEERDIST_PUBLICATION_OPTIONS
def _define_PEERDIST_PUBLICATION_OPTIONS():
    PEERDIST_PUBLICATION_OPTIONS = win32more.NetworkManagement.P2P.PEERDIST_PUBLICATION_OPTIONS_head
    PEERDIST_PUBLICATION_OPTIONS._fields_ = [
        ("dwVersion", UInt32),
        ("dwFlags", UInt32),
    ]
    return PEERDIST_PUBLICATION_OPTIONS
def _define_PEERDIST_CONTENT_TAG_head():
    class PEERDIST_CONTENT_TAG(Structure):
        pass
    return PEERDIST_CONTENT_TAG
def _define_PEERDIST_CONTENT_TAG():
    PEERDIST_CONTENT_TAG = win32more.NetworkManagement.P2P.PEERDIST_CONTENT_TAG_head
    PEERDIST_CONTENT_TAG._fields_ = [
        ("Data", Byte * 16),
    ]
    return PEERDIST_CONTENT_TAG
def _define_PEERDIST_RETRIEVAL_OPTIONS_head():
    class PEERDIST_RETRIEVAL_OPTIONS(Structure):
        pass
    return PEERDIST_RETRIEVAL_OPTIONS
def _define_PEERDIST_RETRIEVAL_OPTIONS():
    PEERDIST_RETRIEVAL_OPTIONS = win32more.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_head
    PEERDIST_RETRIEVAL_OPTIONS._fields_ = [
        ("cbSize", UInt32),
        ("dwContentInfoMinVersion", UInt32),
        ("dwContentInfoMaxVersion", UInt32),
        ("dwReserved", UInt32),
    ]
    return PEERDIST_RETRIEVAL_OPTIONS
def _define_PEERDIST_STATUS_INFO_head():
    class PEERDIST_STATUS_INFO(Structure):
        pass
    return PEERDIST_STATUS_INFO
def _define_PEERDIST_STATUS_INFO():
    PEERDIST_STATUS_INFO = win32more.NetworkManagement.P2P.PEERDIST_STATUS_INFO_head
    PEERDIST_STATUS_INFO._fields_ = [
        ("cbSize", UInt32),
        ("status", win32more.NetworkManagement.P2P.PEERDIST_STATUS),
        ("dwMinVer", win32more.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE),
        ("dwMaxVer", win32more.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE),
    ]
    return PEERDIST_STATUS_INFO
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = Int32
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_PeerDistClientBasicInfo = 0
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_MaximumPeerDistClientInfoByHandlesClass = 1
def _define_PEERDIST_CLIENT_BASIC_INFO_head():
    class PEERDIST_CLIENT_BASIC_INFO(Structure):
        pass
    return PEERDIST_CLIENT_BASIC_INFO
def _define_PEERDIST_CLIENT_BASIC_INFO():
    PEERDIST_CLIENT_BASIC_INFO = win32more.NetworkManagement.P2P.PEERDIST_CLIENT_BASIC_INFO_head
    PEERDIST_CLIENT_BASIC_INFO._fields_ = [
        ("fFlashCrowd", win32more.Foundation.BOOL),
    ]
    return PEERDIST_CLIENT_BASIC_INFO
def _define_PeerGraphStartup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.NetworkManagement.P2P.PEER_VERSION_DATA_head), use_last_error=False)(("PeerGraphStartup", windll["P2PGRAPH"]), ((1, 'wVersionRequested'),(1, 'pVersionData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphShutdown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("PeerGraphShutdown", windll["P2PGRAPH"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphFreeData():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("PeerGraphFreeData", windll["P2PGRAPH"]), ((1, 'pvData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphGetItemCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("PeerGraphGetItemCount", windll["P2PGRAPH"]), ((1, 'hPeerEnum'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphGetNextItem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(POINTER(c_void_p)), use_last_error=False)(("PeerGraphGetNextItem", windll["P2PGRAPH"]), ((1, 'hPeerEnum'),(1, 'pCount'),(1, 'pppvItems'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphEndEnumeration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerGraphEndEnumeration", windll["P2PGRAPH"]), ((1, 'hPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head),win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.P2P.PEER_SECURITY_INTERFACE_head),POINTER(c_void_p), use_last_error=False)(("PeerGraphCreate", windll["P2PGRAPH"]), ((1, 'pGraphProperties'),(1, 'pwzDatabaseName'),(1, 'pSecurityInterface'),(1, 'phGraph'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphOpen():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.P2P.PEER_SECURITY_INTERFACE_head),UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PeerGraphOpen", windll["P2PGRAPH"]), ((1, 'pwzGraphId'),(1, 'pwzPeerId'),(1, 'pwzDatabaseName'),(1, 'pSecurityInterface'),(1, 'cRecordTypeSyncPrecedence'),(1, 'pRecordTypeSyncPrecedence'),(1, 'phGraph'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphListen():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32,UInt16, use_last_error=False)(("PeerGraphListen", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'dwScope'),(1, 'dwScopeId'),(1, 'wPort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphConnect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head),POINTER(UInt64), use_last_error=False)(("PeerGraphConnect", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pwzPeerId'),(1, 'pAddress'),(1, 'pullConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerGraphClose", windll["P2PGRAPH"]), ((1, 'hGraph'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphDelete():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("PeerGraphDelete", windll["P2PGRAPH"]), ((1, 'pwzGraphId'),(1, 'pwzPeerId'),(1, 'pwzDatabaseName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphGetStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("PeerGraphGetStatus", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pdwStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphGetProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head)), use_last_error=False)(("PeerGraphGetProperties", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'ppGraphProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphSetProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head), use_last_error=False)(("PeerGraphSetProperties", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pGraphProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphRegisterEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_REGISTRATION),POINTER(c_void_p), use_last_error=False)(("PeerGraphRegisterEvent", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'hEvent'),(1, 'cEventRegistrations'),(1, 'pEventRegistrations'),(1, 'phPeerEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphUnregisterEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerGraphUnregisterEvent", windll["P2PGRAPH"]), ((1, 'hPeerEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphGetEventData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_DATA_head)), use_last_error=False)(("PeerGraphGetEventData", windll["P2PGRAPH"]), ((1, 'hPeerEvent'),(1, 'ppEventData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphGetRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head)), use_last_error=False)(("PeerGraphGetRecord", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pRecordId'),(1, 'ppRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphAddRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head),POINTER(Guid), use_last_error=False)(("PeerGraphAddRecord", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pRecord'),(1, 'pRecordId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphUpdateRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head), use_last_error=False)(("PeerGraphUpdateRecord", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphDeleteRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),win32more.Foundation.BOOL, use_last_error=False)(("PeerGraphDeleteRecord", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pRecordId'),(1, 'fLocal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphEnumRecords():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGraphEnumRecords", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pRecordType'),(1, 'pwzPeerId'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphSearchRecords():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGraphSearchRecords", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pwzCriteria'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphExportDatabase():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR, use_last_error=False)(("PeerGraphExportDatabase", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pwzFilePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphImportDatabase():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR, use_last_error=False)(("PeerGraphImportDatabase", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pwzFilePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphValidateDeferredRecords():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(Guid), use_last_error=False)(("PeerGraphValidateDeferredRecords", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'cRecordIds'),(1, 'pRecordIds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphOpenDirectConnection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head),POINTER(UInt64), use_last_error=False)(("PeerGraphOpenDirectConnection", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pwzPeerId'),(1, 'pAddress'),(1, 'pullConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphSendData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,POINTER(Guid),UInt32,c_void_p, use_last_error=False)(("PeerGraphSendData", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'ullConnectionId'),(1, 'pType'),(1, 'cbData'),(1, 'pvData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphCloseDirectConnection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64, use_last_error=False)(("PeerGraphCloseDirectConnection", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'ullConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphEnumConnections():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(c_void_p), use_last_error=False)(("PeerGraphEnumConnections", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'dwFlags'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphEnumNodes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGraphEnumNodes", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pwzPeerId'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphSetPresence():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.BOOL, use_last_error=False)(("PeerGraphSetPresence", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'fPresent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphGetNodeInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_NODE_INFO_head)), use_last_error=False)(("PeerGraphGetNodeInfo", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'ullNodeId'),(1, 'ppNodeInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphSetNodeAttributes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR, use_last_error=False)(("PeerGraphSetNodeAttributes", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pwzAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphPeerTimeToUniversalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("PeerGraphPeerTimeToUniversalTime", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pftPeerTime'),(1, 'pftUniversalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGraphUniversalTimeToPeerTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("PeerGraphUniversalTimeToPeerTime", windll["P2PGRAPH"]), ((1, 'hGraph'),(1, 'pftUniversalTime'),(1, 'pftPeerTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerFreeData():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("PeerFreeData", windll["P2P"]), ((1, 'pvData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGetItemCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("PeerGetItemCount", windll["P2P"]), ((1, 'hPeerEnum'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGetNextItem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(POINTER(c_void_p)), use_last_error=False)(("PeerGetNextItem", windll["P2P"]), ((1, 'hPeerEnum'),(1, 'pCount'),(1, 'pppvItems'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerEndEnumeration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerEndEnumeration", windll["P2P"]), ((1, 'hPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupStartup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.NetworkManagement.P2P.PEER_VERSION_DATA_head), use_last_error=False)(("PeerGroupStartup", windll["P2P"]), ((1, 'wVersionRequested'),(1, 'pVersionData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupShutdown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("PeerGroupShutdown", windll["P2P"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head),POINTER(c_void_p), use_last_error=False)(("PeerGroupCreate", windll["P2P"]), ((1, 'pProperties'),(1, 'phGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupOpen():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGroupOpen", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'pwzGroupPeerName'),(1, 'pwzCloud'),(1, 'phGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupJoin():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGroupJoin", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'pwzInvitation'),(1, 'pwzCloud'),(1, 'phGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupPasswordJoin():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGroupPasswordJoin", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'pwzInvitation'),(1, 'pwzPassword'),(1, 'pwzCloud'),(1, 'phGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupConnect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerGroupConnect", windll["P2P"]), ((1, 'hGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupConnectByAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS), use_last_error=False)(("PeerGroupConnectByAddress", windll["P2P"]), ((1, 'hGroup'),(1, 'cAddresses'),(1, 'pAddresses'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerGroupClose", windll["P2P"]), ((1, 'hGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupDelete():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("PeerGroupDelete", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'pwzGroupPeerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupCreateInvitation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),UInt32,POINTER(Guid),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerGroupCreateInvitation", windll["P2P"]), ((1, 'hGroup'),(1, 'pwzIdentityInfo'),(1, 'pftExpiration'),(1, 'cRoles'),(1, 'pRoles'),(1, 'ppwzInvitation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupCreatePasswordInvitation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerGroupCreatePasswordInvitation", windll["P2P"]), ((1, 'hGroup'),(1, 'ppwzInvitation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupParseInvitation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_INFO_head)), use_last_error=False)(("PeerGroupParseInvitation", windll["P2P"]), ((1, 'pwzInvitation'),(1, 'ppInvitationInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupGetStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("PeerGroupGetStatus", windll["P2P"]), ((1, 'hGroup'),(1, 'pdwStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupGetProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head)), use_last_error=False)(("PeerGroupGetProperties", windll["P2P"]), ((1, 'hGroup'),(1, 'ppProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupSetProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head), use_last_error=False)(("PeerGroupSetProperties", windll["P2P"]), ((1, 'hGroup'),(1, 'pProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupEnumMembers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGroupEnumMembers", windll["P2P"]), ((1, 'hGroup'),(1, 'dwFlags'),(1, 'pwzIdentity'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupOpenDirectConnection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head),POINTER(UInt64), use_last_error=False)(("PeerGroupOpenDirectConnection", windll["P2P"]), ((1, 'hGroup'),(1, 'pwzIdentity'),(1, 'pAddress'),(1, 'pullConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupCloseDirectConnection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64, use_last_error=False)(("PeerGroupCloseDirectConnection", windll["P2P"]), ((1, 'hGroup'),(1, 'ullConnectionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupEnumConnections():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(c_void_p), use_last_error=False)(("PeerGroupEnumConnections", windll["P2P"]), ((1, 'hGroup'),(1, 'dwFlags'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupSendData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,POINTER(Guid),UInt32,c_void_p, use_last_error=False)(("PeerGroupSendData", windll["P2P"]), ((1, 'hGroup'),(1, 'ullConnectionId'),(1, 'pType'),(1, 'cbData'),(1, 'pvData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupRegisterEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_REGISTRATION),POINTER(c_void_p), use_last_error=False)(("PeerGroupRegisterEvent", windll["P2P"]), ((1, 'hGroup'),(1, 'hEvent'),(1, 'cEventRegistration'),(1, 'pEventRegistrations'),(1, 'phPeerEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupUnregisterEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerGroupUnregisterEvent", windll["P2P"]), ((1, 'hPeerEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupGetEventData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_DATA_head)), use_last_error=False)(("PeerGroupGetEventData", windll["P2P"]), ((1, 'hPeerEvent'),(1, 'ppEventData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupGetRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head)), use_last_error=False)(("PeerGroupGetRecord", windll["P2P"]), ((1, 'hGroup'),(1, 'pRecordId'),(1, 'ppRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupAddRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head),POINTER(Guid), use_last_error=False)(("PeerGroupAddRecord", windll["P2P"]), ((1, 'hGroup'),(1, 'pRecord'),(1, 'pRecordId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupUpdateRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head), use_last_error=False)(("PeerGroupUpdateRecord", windll["P2P"]), ((1, 'hGroup'),(1, 'pRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupDeleteRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid), use_last_error=False)(("PeerGroupDeleteRecord", windll["P2P"]), ((1, 'hGroup'),(1, 'pRecordId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupEnumRecords():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PeerGroupEnumRecords", windll["P2P"]), ((1, 'hGroup'),(1, 'pRecordType'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupSearchRecords():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerGroupSearchRecords", windll["P2P"]), ((1, 'hGroup'),(1, 'pwzCriteria'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupExportDatabase():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR, use_last_error=False)(("PeerGroupExportDatabase", windll["P2P"]), ((1, 'hGroup'),(1, 'pwzFilePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupImportDatabase():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR, use_last_error=False)(("PeerGroupImportDatabase", windll["P2P"]), ((1, 'hGroup'),(1, 'pwzFilePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupIssueCredentials():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.P2P.PEER_CREDENTIAL_INFO_head),UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerGroupIssueCredentials", windll["P2P"]), ((1, 'hGroup'),(1, 'pwzSubjectIdentity'),(1, 'pCredentialInfo'),(1, 'dwFlags'),(1, 'ppwzInvitation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupExportConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerGroupExportConfig", windll["P2P"]), ((1, 'hGroup'),(1, 'pwzPassword'),(1, 'ppwzXML'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupImportConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerGroupImportConfig", windll["P2P"]), ((1, 'pwzXML'),(1, 'pwzPassword'),(1, 'fOverwrite'),(1, 'ppwzIdentity'),(1, 'ppwzGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupPeerTimeToUniversalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("PeerGroupPeerTimeToUniversalTime", windll["P2P"]), ((1, 'hGroup'),(1, 'pftPeerTime'),(1, 'pftUniversalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupUniversalTimeToPeerTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("PeerGroupUniversalTimeToPeerTime", windll["P2P"]), ((1, 'hGroup'),(1, 'pftUniversalTime'),(1, 'pftPeerTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerGroupResumePasswordAuthentication():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p, use_last_error=False)(("PeerGroupResumePasswordAuthentication", windll["P2P"]), ((1, 'hGroup'),(1, 'hPeerEventHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UIntPtr,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerIdentityCreate", windll["P2P"]), ((1, 'pwzClassifier'),(1, 'pwzFriendlyName'),(1, 'hCryptProv'),(1, 'ppwzIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityGetFriendlyName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerIdentityGetFriendlyName", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'ppwzFriendlyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentitySetFriendlyName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("PeerIdentitySetFriendlyName", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'pwzFriendlyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityGetCryptKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UIntPtr), use_last_error=False)(("PeerIdentityGetCryptKey", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'phCryptProv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityDelete():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("PeerIdentityDelete", windll["P2P"]), ((1, 'pwzIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerEnumIdentities():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(("PeerEnumIdentities", windll["P2P"]), ((1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerEnumGroups():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("PeerEnumGroups", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCreatePeerName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerCreatePeerName", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'pwzClassifier'),(1, 'ppwzPeerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityGetXML():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerIdentityGetXML", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'ppwzIdentityXML'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityExport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerIdentityExport", windll["P2P"]), ((1, 'pwzIdentity'),(1, 'pwzPassword'),(1, 'ppwzExportXML'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityImport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerIdentityImport", windll["P2P"]), ((1, 'pwzImportXML'),(1, 'pwzPassword'),(1, 'ppwzIdentity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerIdentityGetDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerIdentityGetDefault", windll["P2P"]), ((1, 'ppwzPeerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabStartup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(("PeerCollabStartup", windll["P2P"]), ((1, 'wVersionRequested'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabShutdown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("PeerCollabShutdown", windll["P2P"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabSignin():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(("PeerCollabSignin", windll["P2P"]), ((1, 'hwndParent'),(1, 'dwSigninOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabSignout():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("PeerCollabSignout", windll["P2P"]), ((1, 'dwSigninOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetSigninOptions():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(("PeerCollabGetSigninOptions", windll["P2P"]), ((1, 'pdwSigninOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabAsyncInviteContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head),POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head),win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("PeerCollabAsyncInviteContact", windll["P2P"]), ((1, 'pcContact'),(1, 'pcEndpoint'),(1, 'pcInvitation'),(1, 'hEvent'),(1, 'phInvitation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetInvitationResponse():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head)), use_last_error=False)(("PeerCollabGetInvitationResponse", windll["P2P"]), ((1, 'hInvitation'),(1, 'ppInvitationResponse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabCancelInvitation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("PeerCollabCancelInvitation", windll["P2P"]), ((1, 'hInvitation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabCloseHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("PeerCollabCloseHandle", windll["P2P"]), ((1, 'hInvitation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabInviteContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head),POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head),POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head)), use_last_error=False)(("PeerCollabInviteContact", windll["P2P"]), ((1, 'pcContact'),(1, 'pcEndpoint'),(1, 'pcInvitation'),(1, 'ppResponse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabAsyncInviteEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head),win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("PeerCollabAsyncInviteEndpoint", windll["P2P"]), ((1, 'pcEndpoint'),(1, 'pcInvitation'),(1, 'hEvent'),(1, 'phInvitation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabInviteEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head),POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head)), use_last_error=False)(("PeerCollabInviteEndpoint", windll["P2P"]), ((1, 'pcEndpoint'),(1, 'pcInvitation'),(1, 'ppResponse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetAppLaunchInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_APP_LAUNCH_INFO_head)), use_last_error=False)(("PeerCollabGetAppLaunchInfo", windll["P2P"]), ((1, 'ppLaunchInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabRegisterApplication():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO_head),win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, use_last_error=False)(("PeerCollabRegisterApplication", windll["P2P"]), ((1, 'pcApplication'),(1, 'registrationType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabUnregisterApplication():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, use_last_error=False)(("PeerCollabUnregisterApplication", windll["P2P"]), ((1, 'pApplicationId'),(1, 'registrationType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetApplicationRegistrationInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO_head)), use_last_error=False)(("PeerCollabGetApplicationRegistrationInfo", windll["P2P"]), ((1, 'pApplicationId'),(1, 'registrationType'),(1, 'ppApplication'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabEnumApplicationRegistrationInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE,POINTER(c_void_p), use_last_error=False)(("PeerCollabEnumApplicationRegistrationInfo", windll["P2P"]), ((1, 'registrationType'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetPresenceInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PRESENCE_INFO_head)), use_last_error=False)(("PeerCollabGetPresenceInfo", windll["P2P"]), ((1, 'pcEndpoint'),(1, 'ppPresenceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabEnumApplications():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PeerCollabEnumApplications", windll["P2P"]), ((1, 'pcEndpoint'),(1, 'pApplicationId'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabEnumObjects():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("PeerCollabEnumObjects", windll["P2P"]), ((1, 'pcEndpoint'),(1, 'pObjectId'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabEnumEndpoints():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head),POINTER(c_void_p), use_last_error=False)(("PeerCollabEnumEndpoints", windll["P2P"]), ((1, 'pcContact'),(1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabRefreshEndpointData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), use_last_error=False)(("PeerCollabRefreshEndpointData", windll["P2P"]), ((1, 'pcEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabDeleteEndpointData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), use_last_error=False)(("PeerCollabDeleteEndpointData", windll["P2P"]), ((1, 'pcEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabQueryContactData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerCollabQueryContactData", windll["P2P"]), ((1, 'pcEndpoint'),(1, 'ppwzContactData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabSubscribeEndpointData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), use_last_error=False)(("PeerCollabSubscribeEndpointData", windll["P2P"]), ((1, 'pcEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabUnsubscribeEndpointData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), use_last_error=False)(("PeerCollabUnsubscribeEndpointData", windll["P2P"]), ((1, 'pcEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabSetPresenceInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_PRESENCE_INFO_head), use_last_error=False)(("PeerCollabSetPresenceInfo", windll["P2P"]), ((1, 'pcPresenceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetEndpointName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerCollabGetEndpointName", windll["P2P"]), ((1, 'ppwzEndpointName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabSetEndpointName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("PeerCollabSetEndpointName", windll["P2P"]), ((1, 'pwzEndpointName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabSetObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_OBJECT_head), use_last_error=False)(("PeerCollabSetObject", windll["P2P"]), ((1, 'pcObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabDeleteObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(("PeerCollabDeleteObject", windll["P2P"]), ((1, 'pObjectId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabRegisterEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_REGISTRATION),POINTER(c_void_p), use_last_error=False)(("PeerCollabRegisterEvent", windll["P2P"]), ((1, 'hEvent'),(1, 'cEventRegistration'),(1, 'pEventRegistrations'),(1, 'phPeerEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetEventData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_DATA_head)), use_last_error=False)(("PeerCollabGetEventData", windll["P2P"]), ((1, 'hPeerEvent'),(1, 'ppEventData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabUnregisterEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerCollabUnregisterEvent", windll["P2P"]), ((1, 'hPeerEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabEnumPeopleNearMe():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(("PeerCollabEnumPeopleNearMe", windll["P2P"]), ((1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabAddContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)), use_last_error=False)(("PeerCollabAddContact", windll["P2P"]), ((1, 'pwzContactData'),(1, 'ppContact'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabDeleteContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("PeerCollabDeleteContact", windll["P2P"]), ((1, 'pwzPeerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabGetContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)), use_last_error=False)(("PeerCollabGetContact", windll["P2P"]), ((1, 'pwzPeerName'),(1, 'ppContact'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabUpdateContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head), use_last_error=False)(("PeerCollabUpdateContact", windll["P2P"]), ((1, 'pContact'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabEnumContacts():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(("PeerCollabEnumContacts", windll["P2P"]), ((1, 'phPeerEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabExportContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerCollabExportContact", windll["P2P"]), ((1, 'pwzPeerName'),(1, 'ppwzContactData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerCollabParseContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)), use_last_error=False)(("PeerCollabParseContact", windll["P2P"]), ((1, 'pwzContactData'),(1, 'ppContact'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerNameToPeerHostName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerNameToPeerHostName", windll["P2P"]), ((1, 'pwzPeerName'),(1, 'ppwzHostName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerHostNameToPeerName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("PeerHostNameToPeerName", windll["P2P"]), ((1, 'pwzHostName'),(1, 'ppwzPeerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpStartup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(("PeerPnrpStartup", windll["P2P"]), ((1, 'wVersionRequested'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpShutdown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("PeerPnrpShutdown", windll["P2P"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpRegister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO_head),POINTER(c_void_p), use_last_error=False)(("PeerPnrpRegister", windll["P2P"]), ((1, 'pcwzPeerName'),(1, 'pRegistrationInfo'),(1, 'phRegistration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpUpdateRegistration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO_head), use_last_error=False)(("PeerPnrpUpdateRegistration", windll["P2P"]), ((1, 'hRegistration'),(1, 'pRegistrationInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpUnregister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerPnrpUnregister", windll["P2P"]), ((1, 'hRegistration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpResolve():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO_head)), use_last_error=False)(("PeerPnrpResolve", windll["P2P"]), ((1, 'pcwzPeerName'),(1, 'pcwzCloudName'),(1, 'pcEndpoints'),(1, 'ppEndpoints'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpStartResolve():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.HANDLE,POINTER(c_void_p), use_last_error=False)(("PeerPnrpStartResolve", windll["P2P"]), ((1, 'pcwzPeerName'),(1, 'pcwzCloudName'),(1, 'cMaxEndpoints'),(1, 'hEvent'),(1, 'phResolve'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpGetCloudInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_CLOUD_INFO_head)), use_last_error=False)(("PeerPnrpGetCloudInfo", windll["P2P"]), ((1, 'pcNumClouds'),(1, 'ppCloudInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpGetEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO_head)), use_last_error=False)(("PeerPnrpGetEndpoint", windll["P2P"]), ((1, 'hResolve'),(1, 'ppEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerPnrpEndResolve():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PeerPnrpEndResolve", windll["P2P"]), ((1, 'hResolve'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtCreatePnrpBootstrapResolver():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)), use_last_error=False)(("DrtCreatePnrpBootstrapResolver", windll["drtprov"]), ((1, 'fPublish'),(1, 'pwzPeerName'),(1, 'pwzCloudName'),(1, 'pwzPublishingIdentity'),(1, 'ppResolver'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtDeletePnrpBootstrapResolver():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head), use_last_error=False)(("DrtDeletePnrpBootstrapResolver", windll["drtprov"]), ((1, 'pResolver'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtCreateDnsBootstrapResolver():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)), use_last_error=False)(("DrtCreateDnsBootstrapResolver", windll["drtprov"]), ((1, 'port'),(1, 'pwszAddress'),(1, 'ppModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtDeleteDnsBootstrapResolver():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head), use_last_error=False)(("DrtDeleteDnsBootstrapResolver", windll["drtprov"]), ((1, 'pResolver'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtCreateIpv6UdpTransport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.P2P.DRT_SCOPE,UInt32,UInt32,POINTER(UInt16),POINTER(c_void_p), use_last_error=False)(("DrtCreateIpv6UdpTransport", windll["drttransport"]), ((1, 'scope'),(1, 'dwScopeId'),(1, 'dwLocalityThreshold'),(1, 'pwPort'),(1, 'phTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtDeleteIpv6UdpTransport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("DrtDeleteIpv6UdpTransport", windll["drttransport"]), ((1, 'hTransport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtCreateDerivedKeySecurityProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)), use_last_error=False)(("DrtCreateDerivedKeySecurityProvider", windll["drtprov"]), ((1, 'pRootCert'),(1, 'pLocalCert'),(1, 'ppSecurityProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtCreateDerivedKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head), use_last_error=False)(("DrtCreateDerivedKey", windll["drtprov"]), ((1, 'pLocalCert'),(1, 'pKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtDeleteDerivedKeySecurityProvider():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head), use_last_error=False)(("DrtDeleteDerivedKeySecurityProvider", windll["drtprov"]), ((1, 'pSecurityProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtCreateNullSecurityProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)), use_last_error=False)(("DrtCreateNullSecurityProvider", windll["drtprov"]), ((1, 'ppSecurityProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtDeleteNullSecurityProvider():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head), use_last_error=False)(("DrtDeleteNullSecurityProvider", windll["drtprov"]), ((1, 'pSecurityProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtOpen():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.P2P.DRT_SETTINGS_head),win32more.Foundation.HANDLE,c_void_p,POINTER(c_void_p), use_last_error=False)(("DrtOpen", windll["drt"]), ((1, 'pSettings'),(1, 'hEvent'),(1, 'pvContext'),(1, 'phDrt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtClose():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("DrtClose", windll["drt"]), ((1, 'hDrt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetEventDataSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("DrtGetEventDataSize", windll["drt"]), ((1, 'hDrt'),(1, 'pulEventDataLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetEventData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.NetworkManagement.P2P.DRT_EVENT_DATA_head), use_last_error=False)(("DrtGetEventData", windll["drt"]), ((1, 'hDrt'),(1, 'ulEventDataLen'),(1, 'pEventData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtRegisterKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.DRT_REGISTRATION_head),c_void_p,POINTER(c_void_p), use_last_error=False)(("DrtRegisterKey", windll["drt"]), ((1, 'hDrt'),(1, 'pRegistration'),(1, 'pvKeyContext'),(1, 'phKeyRegistration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtUpdateKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head), use_last_error=False)(("DrtUpdateKey", windll["drt"]), ((1, 'hKeyRegistration'),(1, 'pAppData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtUnregisterKey():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("DrtUnregisterKey", windll["drt"]), ((1, 'hKeyRegistration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtStartSearch():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head),POINTER(win32more.NetworkManagement.P2P.DRT_SEARCH_INFO_head),UInt32,win32more.Foundation.HANDLE,c_void_p,POINTER(c_void_p), use_last_error=False)(("DrtStartSearch", windll["drt"]), ((1, 'hDrt'),(1, 'pKey'),(1, 'pInfo'),(1, 'timeout'),(1, 'hEvent'),(1, 'pvContext'),(1, 'hSearchContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtContinueSearch():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("DrtContinueSearch", windll["drt"]), ((1, 'hSearchContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetSearchResultSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("DrtGetSearchResultSize", windll["drt"]), ((1, 'hSearchContext'),(1, 'pulSearchResultSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetSearchResult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.NetworkManagement.P2P.DRT_SEARCH_RESULT_head), use_last_error=False)(("DrtGetSearchResult", windll["drt"]), ((1, 'hSearchContext'),(1, 'ulSearchResultSize'),(1, 'pSearchResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetSearchPathSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("DrtGetSearchPathSize", windll["drt"]), ((1, 'hSearchContext'),(1, 'pulSearchPathSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetSearchPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.NetworkManagement.P2P.DRT_ADDRESS_LIST_head), use_last_error=False)(("DrtGetSearchPath", windll["drt"]), ((1, 'hSearchContext'),(1, 'ulSearchPathSize'),(1, 'pSearchPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtEndSearch():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("DrtEndSearch", windll["drt"]), ((1, 'hSearchContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetInstanceName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DrtGetInstanceName", windll["drt"]), ((1, 'hDrt'),(1, 'ulcbInstanceNameSize'),(1, 'pwzDrtInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrtGetInstanceNameSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32), use_last_error=False)(("DrtGetInstanceNameSize", windll["drt"]), ((1, 'hDrt'),(1, 'pulcbInstanceNameSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistStartup():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(IntPtr),POINTER(UInt32), use_last_error=False)(("PeerDistStartup", windll["PeerDist"]), ((1, 'dwVersionRequested'),(1, 'phPeerDist'),(1, 'pdwSupportedVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistShutdown():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("PeerDistShutdown", windll["PeerDist"]), ((1, 'hPeerDist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistGetStatus():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS), use_last_error=False)(("PeerDistGetStatus", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'pPeerDistStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistRegisterForStatusChangeNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UIntPtr,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS), use_last_error=False)(("PeerDistRegisterForStatusChangeNotification", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hCompletionPort'),(1, 'ulCompletionKey'),(1, 'lpOverlapped'),(1, 'pPeerDistStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistUnregisterForStatusChangeNotification():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=True)(("PeerDistUnregisterForStatusChangeNotification", windll["PeerDist"]), ((1, 'hPeerDist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerPublishStream():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no,UInt64,POINTER(win32more.NetworkManagement.P2P.PEERDIST_PUBLICATION_OPTIONS_head),win32more.Foundation.HANDLE,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PeerDistServerPublishStream", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'cbContentIdentifier'),(1, 'pContentIdentifier'),(1, 'cbContentLength'),(1, 'pPublishOptions'),(1, 'hCompletionPort'),(1, 'ulCompletionKey'),(1, 'phStream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerPublishAddToStream():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,c_char_p_no,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistServerPublishAddToStream", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hStream'),(1, 'cbNumberOfBytes'),(1, 'pBuffer'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerPublishCompleteStream():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistServerPublishCompleteStream", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hStream'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerCloseStreamHandle():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr, use_last_error=False)(("PeerDistServerCloseStreamHandle", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hStream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerUnpublish():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no, use_last_error=False)(("PeerDistServerUnpublish", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'cbContentIdentifier'),(1, 'pContentIdentifier'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerOpenContentInformation():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no,UInt64,UInt64,win32more.Foundation.HANDLE,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PeerDistServerOpenContentInformation", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'cbContentIdentifier'),(1, 'pContentIdentifier'),(1, 'ullContentOffset'),(1, 'cbContentLength'),(1, 'hCompletionPort'),(1, 'ulCompletionKey'),(1, 'phContentInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerRetrieveContentInformation():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,c_char_p_no,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistServerRetrieveContentInformation", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentInfo'),(1, 'cbMaxNumberOfBytes'),(1, 'pBuffer'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerCloseContentInformation():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr, use_last_error=False)(("PeerDistServerCloseContentInformation", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerCancelAsyncOperation():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("PeerDistServerCancelAsyncOperation", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'cbContentIdentifier'),(1, 'pContentIdentifier'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientOpenContent():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.P2P.PEERDIST_CONTENT_TAG_head),win32more.Foundation.HANDLE,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PeerDistClientOpenContent", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'pContentTag'),(1, 'hCompletionPort'),(1, 'ulCompletionKey'),(1, 'phContentHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientCloseContent():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr, use_last_error=False)(("PeerDistClientCloseContent", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientAddContentInformation():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,c_char_p_no,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistClientAddContentInformation", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),(1, 'cbNumberOfBytes'),(1, 'pBuffer'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientCompleteContentInformation():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistClientCompleteContentInformation", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientAddData():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,c_char_p_no,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistClientAddData", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),(1, 'cbNumberOfBytes'),(1, 'pBuffer'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientBlockRead():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,c_char_p_no,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistClientBlockRead", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),(1, 'cbMaxNumberOfBytes'),(1, 'pBuffer'),(1, 'dwTimeoutInMilliseconds'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientStreamRead():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,UInt32,c_char_p_no,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistClientStreamRead", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),(1, 'cbMaxNumberOfBytes'),(1, 'pBuffer'),(1, 'dwTimeoutInMilliseconds'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientFlushContent():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.P2P.PEERDIST_CONTENT_TAG_head),win32more.Foundation.HANDLE,UIntPtr,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("PeerDistClientFlushContent", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'pContentTag'),(1, 'hCompletionPort'),(1, 'ulCompletionKey'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientCancelAsyncOperation():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("PeerDistClientCancelAsyncOperation", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistGetStatusEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS_INFO_head), use_last_error=False)(("PeerDistGetStatusEx", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'pPeerDistStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistRegisterForStatusChangeNotificationEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HANDLE,UIntPtr,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS_INFO_head), use_last_error=False)(("PeerDistRegisterForStatusChangeNotificationEx", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hCompletionPort'),(1, 'ulCompletionKey'),(1, 'lpOverlapped'),(1, 'pPeerDistStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistGetOverlappedResult():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("PeerDistGetOverlappedResult", windll["PeerDist"]), ((1, 'lpOverlapped'),(1, 'lpNumberOfBytesTransferred'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistServerOpenContentInformationEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,c_char_p_no,UInt64,UInt64,POINTER(win32more.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_head),win32more.Foundation.HANDLE,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PeerDistServerOpenContentInformationEx", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'cbContentIdentifier'),(1, 'pContentIdentifier'),(1, 'ullContentOffset'),(1, 'cbContentLength'),(1, 'pRetrievalOptions'),(1, 'hCompletionPort'),(1, 'ulCompletionKey'),(1, 'phContentInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeerDistClientGetInformationByHandle():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,win32more.NetworkManagement.P2P.PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS,UInt32,c_void_p, use_last_error=False)(("PeerDistClientGetInformationByHandle", windll["PeerDist"]), ((1, 'hPeerDist'),(1, 'hContentHandle'),(1, 'PeerDistClientInfoClass'),(1, 'dwBufferSize'),(1, 'lpInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "NS_PNRPNAME",
    "NS_PNRPCLOUD",
    "PNRPINFO_HINT",
    "NS_PROVIDER_PNRPNAME",
    "NS_PROVIDER_PNRPCLOUD",
    "SVCID_PNRPCLOUD",
    "SVCID_PNRPNAME_V1",
    "SVCID_PNRPNAME_V2",
    "PNRP_MAX_ENDPOINT_ADDRESSES",
    "PNRP_MAX_EXTENDED_PAYLOAD_BYTES",
    "WSA_PNRP_ERROR_BASE",
    "WSA_PNRP_CLOUD_NOT_FOUND",
    "WSA_PNRP_CLOUD_DISABLED",
    "WSA_PNRP_INVALID_IDENTITY",
    "WSA_PNRP_TOO_MUCH_LOAD",
    "WSA_PNRP_CLOUD_IS_SEARCH_ONLY",
    "WSA_PNRP_CLIENT_INVALID_COMPARTMENT_ID",
    "WSA_PNRP_DUPLICATE_PEER_NAME",
    "WSA_PNRP_CLOUD_IS_DEAD",
    "PEER_E_CLOUD_NOT_FOUND",
    "PEER_E_CLOUD_DISABLED",
    "PEER_E_INVALID_IDENTITY",
    "PEER_E_TOO_MUCH_LOAD",
    "PEER_E_CLOUD_IS_SEARCH_ONLY",
    "PEER_E_CLIENT_INVALID_COMPARTMENT_ID",
    "PEER_E_DUPLICATE_PEER_NAME",
    "PEER_E_CLOUD_IS_DEAD",
    "PEER_E_NOT_FOUND",
    "PEER_E_DISK_FULL",
    "PEER_E_ALREADY_EXISTS",
    "PEER_GROUP_ROLE_ADMIN",
    "PEER_GROUP_ROLE_MEMBER",
    "PEER_GROUP_ROLE_INVITING_MEMBER",
    "PEER_COLLAB_OBJECTID_USER_PICTURE",
    "FACILITY_DRT",
    "DRT_E_TIMEOUT",
    "DRT_E_INVALID_KEY_SIZE",
    "DRT_E_INVALID_CERT_CHAIN",
    "DRT_E_INVALID_MESSAGE",
    "DRT_E_NO_MORE",
    "DRT_E_INVALID_MAX_ADDRESSES",
    "DRT_E_SEARCH_IN_PROGRESS",
    "DRT_E_INVALID_KEY",
    "DRT_S_RETRY",
    "DRT_E_INVALID_MAX_ENDPOINTS",
    "DRT_E_INVALID_SEARCH_RANGE",
    "DRT_E_INVALID_PORT",
    "DRT_E_INVALID_TRANSPORT_PROVIDER",
    "DRT_E_INVALID_SECURITY_PROVIDER",
    "DRT_E_STILL_IN_USE",
    "DRT_E_INVALID_BOOTSTRAP_PROVIDER",
    "DRT_E_INVALID_ADDRESS",
    "DRT_E_INVALID_SCOPE",
    "DRT_E_TRANSPORT_SHUTTING_DOWN",
    "DRT_E_NO_ADDRESSES_AVAILABLE",
    "DRT_E_DUPLICATE_KEY",
    "DRT_E_TRANSPORTPROVIDER_IN_USE",
    "DRT_E_TRANSPORTPROVIDER_NOT_ATTACHED",
    "DRT_E_SECURITYPROVIDER_IN_USE",
    "DRT_E_SECURITYPROVIDER_NOT_ATTACHED",
    "DRT_E_BOOTSTRAPPROVIDER_IN_USE",
    "DRT_E_BOOTSTRAPPROVIDER_NOT_ATTACHED",
    "DRT_E_TRANSPORT_ALREADY_BOUND",
    "DRT_E_TRANSPORT_NOT_BOUND",
    "DRT_E_TRANSPORT_UNEXPECTED",
    "DRT_E_TRANSPORT_INVALID_ARGUMENT",
    "DRT_E_TRANSPORT_NO_DEST_ADDRESSES",
    "DRT_E_TRANSPORT_EXECUTING_CALLBACK",
    "DRT_E_TRANSPORT_ALREADY_EXISTS_FOR_SCOPE",
    "DRT_E_INVALID_SETTINGS",
    "DRT_E_INVALID_SEARCH_INFO",
    "DRT_E_FAULTED",
    "DRT_E_TRANSPORT_STILL_BOUND",
    "DRT_E_INSUFFICIENT_BUFFER",
    "DRT_E_INVALID_INSTANCE_PREFIX",
    "DRT_E_INVALID_SECURITY_MODE",
    "DRT_E_CAPABILITY_MISMATCH",
    "DRT_PAYLOAD_REVOKED",
    "DRT_MIN_ROUTING_ADDRESSES",
    "DRT_MAX_ROUTING_ADDRESSES",
    "DRT_MAX_PAYLOAD_SIZE",
    "DRT_MAX_INSTANCE_PREFIX_LEN",
    "DRT_LINK_LOCAL_ISATAP_SCOPEID",
    "PEERDIST_PUBLICATION_OPTIONS_VERSION_1",
    "PEERDIST_PUBLICATION_OPTIONS_VERSION",
    "PEERDIST_PUBLICATION_OPTIONS_VERSION_2",
    "PEERDIST_READ_TIMEOUT_LOCAL_CACHE_ONLY",
    "PEERDIST_READ_TIMEOUT_DEFAULT",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_1",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_2",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION",
    "PNRP_SCOPE",
    "PNRP_SCOPE_ANY",
    "PNRP_GLOBAL_SCOPE",
    "PNRP_SITE_LOCAL_SCOPE",
    "PNRP_LINK_LOCAL_SCOPE",
    "PNRP_CLOUD_STATE",
    "PNRP_CLOUD_STATE_VIRTUAL",
    "PNRP_CLOUD_STATE_SYNCHRONISING",
    "PNRP_CLOUD_STATE_ACTIVE",
    "PNRP_CLOUD_STATE_DEAD",
    "PNRP_CLOUD_STATE_DISABLED",
    "PNRP_CLOUD_STATE_NO_NET",
    "PNRP_CLOUD_STATE_ALONE",
    "PNRP_CLOUD_FLAGS",
    "PNRP_CLOUD_NO_FLAGS",
    "PNRP_CLOUD_NAME_LOCAL",
    "PNRP_CLOUD_RESOLVE_ONLY",
    "PNRP_CLOUD_FULL_PARTICIPANT",
    "PNRP_REGISTERED_ID_STATE",
    "PNRP_REGISTERED_ID_STATE_OK",
    "PNRP_REGISTERED_ID_STATE_PROBLEM",
    "PNRP_RESOLVE_CRITERIA",
    "PNRP_RESOLVE_CRITERIA_DEFAULT",
    "PNRP_RESOLVE_CRITERIA_REMOTE_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_NEAREST_REMOTE_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_NON_CURRENT_PROCESS_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_NEAREST_NON_CURRENT_PROCESS_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_ANY_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_NEAREST_PEER_NAME",
    "PNRP_CLOUD_ID",
    "PNRP_EXTENDED_PAYLOAD_TYPE",
    "PNRP_EXTENDED_PAYLOAD_TYPE_NONE",
    "PNRP_EXTENDED_PAYLOAD_TYPE_BINARY",
    "PNRP_EXTENDED_PAYLOAD_TYPE_STRING",
    "PNRPINFO_V1",
    "PNRPINFO_V2",
    "PNRPCLOUDINFO",
    "PEER_RECORD_CHANGE_TYPE",
    "PEER_RECORD_ADDED",
    "PEER_RECORD_UPDATED",
    "PEER_RECORD_DELETED",
    "PEER_RECORD_EXPIRED",
    "PEER_CONNECTION_STATUS",
    "PEER_CONNECTED",
    "PEER_DISCONNECTED",
    "PEER_CONNECTION_FAILED",
    "PEER_CONNECTION_FLAGS",
    "PEER_CONNECTION_NEIGHBOR",
    "PEER_CONNECTION_DIRECT",
    "PEER_RECORD_FLAGS",
    "PEER_RECORD_FLAG_AUTOREFRESH",
    "PEER_RECORD_FLAG_DELETED",
    "PEER_VERSION_DATA",
    "PEER_DATA",
    "PEER_RECORD",
    "PEER_ADDRESS",
    "PEER_CONNECTION_INFO",
    "PEER_EVENT_INCOMING_DATA",
    "PEER_EVENT_RECORD_CHANGE_DATA",
    "PEER_EVENT_CONNECTION_CHANGE_DATA",
    "PEER_EVENT_SYNCHRONIZED_DATA",
    "PEER_GRAPH_EVENT_TYPE",
    "PEER_GRAPH_EVENT_STATUS_CHANGED",
    "PEER_GRAPH_EVENT_PROPERTY_CHANGED",
    "PEER_GRAPH_EVENT_RECORD_CHANGED",
    "PEER_GRAPH_EVENT_DIRECT_CONNECTION",
    "PEER_GRAPH_EVENT_NEIGHBOR_CONNECTION",
    "PEER_GRAPH_EVENT_INCOMING_DATA",
    "PEER_GRAPH_EVENT_CONNECTION_REQUIRED",
    "PEER_GRAPH_EVENT_NODE_CHANGED",
    "PEER_GRAPH_EVENT_SYNCHRONIZED",
    "PEER_NODE_CHANGE_TYPE",
    "PEER_NODE_CHANGE_CONNECTED",
    "PEER_NODE_CHANGE_DISCONNECTED",
    "PEER_NODE_CHANGE_UPDATED",
    "PEER_GRAPH_STATUS_FLAGS",
    "PEER_GRAPH_STATUS_LISTENING",
    "PEER_GRAPH_STATUS_HAS_CONNECTIONS",
    "PEER_GRAPH_STATUS_SYNCHRONIZED",
    "PEER_GRAPH_PROPERTY_FLAGS",
    "PEER_GRAPH_PROPERTY_HEARTBEATS",
    "PEER_GRAPH_PROPERTY_DEFER_EXPIRATION",
    "PEER_GRAPH_SCOPE",
    "PEER_GRAPH_SCOPE_ANY",
    "PEER_GRAPH_SCOPE_GLOBAL",
    "PEER_GRAPH_SCOPE_SITELOCAL",
    "PEER_GRAPH_SCOPE_LINKLOCAL",
    "PEER_GRAPH_SCOPE_LOOPBACK",
    "PEER_GRAPH_PROPERTIES",
    "PEER_NODE_INFO",
    "PEER_EVENT_NODE_CHANGE_DATA",
    "PEER_GRAPH_EVENT_REGISTRATION",
    "PEER_GRAPH_EVENT_DATA",
    "PFNPEER_VALIDATE_RECORD",
    "PFNPEER_SECURE_RECORD",
    "PFNPEER_FREE_SECURITY_DATA",
    "PFNPEER_ON_PASSWORD_AUTH_FAILED",
    "PEER_SECURITY_INTERFACE",
    "PEER_GROUP_EVENT_TYPE",
    "PEER_GROUP_EVENT_STATUS_CHANGED",
    "PEER_GROUP_EVENT_PROPERTY_CHANGED",
    "PEER_GROUP_EVENT_RECORD_CHANGED",
    "PEER_GROUP_EVENT_DIRECT_CONNECTION",
    "PEER_GROUP_EVENT_NEIGHBOR_CONNECTION",
    "PEER_GROUP_EVENT_INCOMING_DATA",
    "PEER_GROUP_EVENT_MEMBER_CHANGED",
    "PEER_GROUP_EVENT_CONNECTION_FAILED",
    "PEER_GROUP_EVENT_AUTHENTICATION_FAILED",
    "PEER_GROUP_STATUS",
    "PEER_GROUP_STATUS_LISTENING",
    "PEER_GROUP_STATUS_HAS_CONNECTIONS",
    "PEER_GROUP_PROPERTY_FLAGS",
    "PEER_MEMBER_DATA_OPTIONAL",
    "PEER_DISABLE_PRESENCE",
    "PEER_DEFER_EXPIRATION",
    "PEER_GROUP_AUTHENTICATION_SCHEME",
    "PEER_GROUP_GMC_AUTHENTICATION",
    "PEER_GROUP_PASSWORD_AUTHENTICATION",
    "PEER_MEMBER_FLAGS",
    "PEER_MEMBER_PRESENT",
    "PEER_MEMBER_CHANGE_TYPE",
    "PEER_MEMBER_CONNECTED",
    "PEER_MEMBER_DISCONNECTED",
    "PEER_MEMBER_UPDATED",
    "PEER_MEMBER_JOINED",
    "PEER_MEMBER_LEFT",
    "PEER_GROUP_ISSUE_CREDENTIAL_FLAGS",
    "PEER_GROUP_STORE_CREDENTIALS",
    "PEER_CREDENTIAL_INFO",
    "PEER_MEMBER",
    "PEER_INVITATION_INFO",
    "PEER_GROUP_PROPERTIES",
    "PEER_EVENT_MEMBER_CHANGE_DATA",
    "PEER_GROUP_EVENT_REGISTRATION",
    "PEER_GROUP_EVENT_DATA",
    "PEER_NAME_PAIR",
    "PEER_SIGNIN_FLAGS",
    "PEER_SIGNIN_NONE",
    "PEER_SIGNIN_NEAR_ME",
    "PEER_SIGNIN_INTERNET",
    "PEER_SIGNIN_ALL",
    "PEER_WATCH_PERMISSION",
    "PEER_WATCH_BLOCKED",
    "PEER_WATCH_ALLOWED",
    "PEER_PUBLICATION_SCOPE",
    "PEER_PUBLICATION_SCOPE_NONE",
    "PEER_PUBLICATION_SCOPE_NEAR_ME",
    "PEER_PUBLICATION_SCOPE_INTERNET",
    "PEER_PUBLICATION_SCOPE_ALL",
    "PEER_APPLICATION",
    "PEER_OBJECT",
    "PEER_CONTACT",
    "PEER_ENDPOINT",
    "PEER_PEOPLE_NEAR_ME",
    "PEER_INVITATION_RESPONSE_TYPE",
    "PEER_INVITATION_RESPONSE_DECLINED",
    "PEER_INVITATION_RESPONSE_ACCEPTED",
    "PEER_INVITATION_RESPONSE_EXPIRED",
    "PEER_INVITATION_RESPONSE_ERROR",
    "PEER_APPLICATION_REGISTRATION_TYPE",
    "PEER_APPLICATION_CURRENT_USER",
    "PEER_APPLICATION_ALL_USERS",
    "PEER_INVITATION",
    "PEER_INVITATION_RESPONSE",
    "PEER_APP_LAUNCH_INFO",
    "PEER_APPLICATION_REGISTRATION_INFO",
    "PEER_PRESENCE_STATUS",
    "PEER_PRESENCE_OFFLINE",
    "PEER_PRESENCE_OUT_TO_LUNCH",
    "PEER_PRESENCE_AWAY",
    "PEER_PRESENCE_BE_RIGHT_BACK",
    "PEER_PRESENCE_IDLE",
    "PEER_PRESENCE_BUSY",
    "PEER_PRESENCE_ON_THE_PHONE",
    "PEER_PRESENCE_ONLINE",
    "PEER_PRESENCE_INFO",
    "PEER_CHANGE_TYPE",
    "PEER_CHANGE_ADDED",
    "PEER_CHANGE_DELETED",
    "PEER_CHANGE_UPDATED",
    "PEER_COLLAB_EVENT_TYPE",
    "PEER_EVENT_WATCHLIST_CHANGED",
    "PEER_EVENT_ENDPOINT_CHANGED",
    "PEER_EVENT_ENDPOINT_PRESENCE_CHANGED",
    "PEER_EVENT_ENDPOINT_APPLICATION_CHANGED",
    "PEER_EVENT_ENDPOINT_OBJECT_CHANGED",
    "PEER_EVENT_MY_ENDPOINT_CHANGED",
    "PEER_EVENT_MY_PRESENCE_CHANGED",
    "PEER_EVENT_MY_APPLICATION_CHANGED",
    "PEER_EVENT_MY_OBJECT_CHANGED",
    "PEER_EVENT_PEOPLE_NEAR_ME_CHANGED",
    "PEER_EVENT_REQUEST_STATUS_CHANGED",
    "PEER_COLLAB_EVENT_REGISTRATION",
    "PEER_EVENT_WATCHLIST_CHANGED_DATA",
    "PEER_EVENT_PRESENCE_CHANGED_DATA",
    "PEER_EVENT_APPLICATION_CHANGED_DATA",
    "PEER_EVENT_OBJECT_CHANGED_DATA",
    "PEER_EVENT_ENDPOINT_CHANGED_DATA",
    "PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA",
    "PEER_EVENT_REQUEST_STATUS_CHANGED_DATA",
    "PEER_COLLAB_EVENT_DATA",
    "PEER_PNRP_ENDPOINT_INFO",
    "PEER_PNRP_CLOUD_INFO",
    "PEER_PNRP_REGISTRATION_INFO",
    "DRT_SCOPE",
    "DRT_GLOBAL_SCOPE",
    "DRT_SITE_LOCAL_SCOPE",
    "DRT_LINK_LOCAL_SCOPE",
    "DRT_STATUS",
    "DRT_ACTIVE",
    "DRT_ALONE",
    "DRT_NO_NETWORK",
    "DRT_FAULTED",
    "DRT_MATCH_TYPE",
    "DRT_MATCH_EXACT",
    "DRT_MATCH_NEAR",
    "DRT_MATCH_INTERMEDIATE",
    "DRT_LEAFSET_KEY_CHANGE_TYPE",
    "DRT_LEAFSET_KEY_ADDED",
    "DRT_LEAFSET_KEY_DELETED",
    "DRT_EVENT_TYPE",
    "DRT_EVENT_STATUS_CHANGED",
    "DRT_EVENT_LEAFSET_KEY_CHANGED",
    "DRT_EVENT_REGISTRATION_STATE_CHANGED",
    "DRT_SECURITY_MODE",
    "DRT_SECURE_RESOLVE",
    "DRT_SECURE_MEMBERSHIP",
    "DRT_SECURE_CONFIDENTIALPAYLOAD",
    "DRT_REGISTRATION_STATE",
    "DRT_REGISTRATION_STATE_UNRESOLVEABLE",
    "DRT_ADDRESS_FLAGS",
    "DRT_ADDRESS_FLAG_ACCEPTED",
    "DRT_ADDRESS_FLAG_REJECTED",
    "DRT_ADDRESS_FLAG_UNREACHABLE",
    "DRT_ADDRESS_FLAG_LOOP",
    "DRT_ADDRESS_FLAG_TOO_BUSY",
    "DRT_ADDRESS_FLAG_BAD_VALIDATE_ID",
    "DRT_ADDRESS_FLAG_SUSPECT_UNREGISTERED_ID",
    "DRT_ADDRESS_FLAG_INQUIRE",
    "DRT_DATA",
    "DRT_REGISTRATION",
    "DRT_SECURITY_PROVIDER",
    "DRT_BOOTSTRAP_RESOLVE_CALLBACK",
    "DRT_BOOTSTRAP_PROVIDER",
    "DRT_SETTINGS",
    "DRT_SEARCH_INFO",
    "DRT_ADDRESS",
    "DRT_ADDRESS_LIST",
    "DRT_SEARCH_RESULT",
    "DRT_EVENT_DATA",
    "PEERDIST_STATUS",
    "PEERDIST_STATUS_DISABLED",
    "PEERDIST_STATUS_UNAVAILABLE",
    "PEERDIST_STATUS_AVAILABLE",
    "PEERDIST_PUBLICATION_OPTIONS",
    "PEERDIST_CONTENT_TAG",
    "PEERDIST_RETRIEVAL_OPTIONS",
    "PEERDIST_STATUS_INFO",
    "PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS",
    "PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_PeerDistClientBasicInfo",
    "PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_MaximumPeerDistClientInfoByHandlesClass",
    "PEERDIST_CLIENT_BASIC_INFO",
    "PeerGraphStartup",
    "PeerGraphShutdown",
    "PeerGraphFreeData",
    "PeerGraphGetItemCount",
    "PeerGraphGetNextItem",
    "PeerGraphEndEnumeration",
    "PeerGraphCreate",
    "PeerGraphOpen",
    "PeerGraphListen",
    "PeerGraphConnect",
    "PeerGraphClose",
    "PeerGraphDelete",
    "PeerGraphGetStatus",
    "PeerGraphGetProperties",
    "PeerGraphSetProperties",
    "PeerGraphRegisterEvent",
    "PeerGraphUnregisterEvent",
    "PeerGraphGetEventData",
    "PeerGraphGetRecord",
    "PeerGraphAddRecord",
    "PeerGraphUpdateRecord",
    "PeerGraphDeleteRecord",
    "PeerGraphEnumRecords",
    "PeerGraphSearchRecords",
    "PeerGraphExportDatabase",
    "PeerGraphImportDatabase",
    "PeerGraphValidateDeferredRecords",
    "PeerGraphOpenDirectConnection",
    "PeerGraphSendData",
    "PeerGraphCloseDirectConnection",
    "PeerGraphEnumConnections",
    "PeerGraphEnumNodes",
    "PeerGraphSetPresence",
    "PeerGraphGetNodeInfo",
    "PeerGraphSetNodeAttributes",
    "PeerGraphPeerTimeToUniversalTime",
    "PeerGraphUniversalTimeToPeerTime",
    "PeerFreeData",
    "PeerGetItemCount",
    "PeerGetNextItem",
    "PeerEndEnumeration",
    "PeerGroupStartup",
    "PeerGroupShutdown",
    "PeerGroupCreate",
    "PeerGroupOpen",
    "PeerGroupJoin",
    "PeerGroupPasswordJoin",
    "PeerGroupConnect",
    "PeerGroupConnectByAddress",
    "PeerGroupClose",
    "PeerGroupDelete",
    "PeerGroupCreateInvitation",
    "PeerGroupCreatePasswordInvitation",
    "PeerGroupParseInvitation",
    "PeerGroupGetStatus",
    "PeerGroupGetProperties",
    "PeerGroupSetProperties",
    "PeerGroupEnumMembers",
    "PeerGroupOpenDirectConnection",
    "PeerGroupCloseDirectConnection",
    "PeerGroupEnumConnections",
    "PeerGroupSendData",
    "PeerGroupRegisterEvent",
    "PeerGroupUnregisterEvent",
    "PeerGroupGetEventData",
    "PeerGroupGetRecord",
    "PeerGroupAddRecord",
    "PeerGroupUpdateRecord",
    "PeerGroupDeleteRecord",
    "PeerGroupEnumRecords",
    "PeerGroupSearchRecords",
    "PeerGroupExportDatabase",
    "PeerGroupImportDatabase",
    "PeerGroupIssueCredentials",
    "PeerGroupExportConfig",
    "PeerGroupImportConfig",
    "PeerGroupPeerTimeToUniversalTime",
    "PeerGroupUniversalTimeToPeerTime",
    "PeerGroupResumePasswordAuthentication",
    "PeerIdentityCreate",
    "PeerIdentityGetFriendlyName",
    "PeerIdentitySetFriendlyName",
    "PeerIdentityGetCryptKey",
    "PeerIdentityDelete",
    "PeerEnumIdentities",
    "PeerEnumGroups",
    "PeerCreatePeerName",
    "PeerIdentityGetXML",
    "PeerIdentityExport",
    "PeerIdentityImport",
    "PeerIdentityGetDefault",
    "PeerCollabStartup",
    "PeerCollabShutdown",
    "PeerCollabSignin",
    "PeerCollabSignout",
    "PeerCollabGetSigninOptions",
    "PeerCollabAsyncInviteContact",
    "PeerCollabGetInvitationResponse",
    "PeerCollabCancelInvitation",
    "PeerCollabCloseHandle",
    "PeerCollabInviteContact",
    "PeerCollabAsyncInviteEndpoint",
    "PeerCollabInviteEndpoint",
    "PeerCollabGetAppLaunchInfo",
    "PeerCollabRegisterApplication",
    "PeerCollabUnregisterApplication",
    "PeerCollabGetApplicationRegistrationInfo",
    "PeerCollabEnumApplicationRegistrationInfo",
    "PeerCollabGetPresenceInfo",
    "PeerCollabEnumApplications",
    "PeerCollabEnumObjects",
    "PeerCollabEnumEndpoints",
    "PeerCollabRefreshEndpointData",
    "PeerCollabDeleteEndpointData",
    "PeerCollabQueryContactData",
    "PeerCollabSubscribeEndpointData",
    "PeerCollabUnsubscribeEndpointData",
    "PeerCollabSetPresenceInfo",
    "PeerCollabGetEndpointName",
    "PeerCollabSetEndpointName",
    "PeerCollabSetObject",
    "PeerCollabDeleteObject",
    "PeerCollabRegisterEvent",
    "PeerCollabGetEventData",
    "PeerCollabUnregisterEvent",
    "PeerCollabEnumPeopleNearMe",
    "PeerCollabAddContact",
    "PeerCollabDeleteContact",
    "PeerCollabGetContact",
    "PeerCollabUpdateContact",
    "PeerCollabEnumContacts",
    "PeerCollabExportContact",
    "PeerCollabParseContact",
    "PeerNameToPeerHostName",
    "PeerHostNameToPeerName",
    "PeerPnrpStartup",
    "PeerPnrpShutdown",
    "PeerPnrpRegister",
    "PeerPnrpUpdateRegistration",
    "PeerPnrpUnregister",
    "PeerPnrpResolve",
    "PeerPnrpStartResolve",
    "PeerPnrpGetCloudInfo",
    "PeerPnrpGetEndpoint",
    "PeerPnrpEndResolve",
    "DrtCreatePnrpBootstrapResolver",
    "DrtDeletePnrpBootstrapResolver",
    "DrtCreateDnsBootstrapResolver",
    "DrtDeleteDnsBootstrapResolver",
    "DrtCreateIpv6UdpTransport",
    "DrtDeleteIpv6UdpTransport",
    "DrtCreateDerivedKeySecurityProvider",
    "DrtCreateDerivedKey",
    "DrtDeleteDerivedKeySecurityProvider",
    "DrtCreateNullSecurityProvider",
    "DrtDeleteNullSecurityProvider",
    "DrtOpen",
    "DrtClose",
    "DrtGetEventDataSize",
    "DrtGetEventData",
    "DrtRegisterKey",
    "DrtUpdateKey",
    "DrtUnregisterKey",
    "DrtStartSearch",
    "DrtContinueSearch",
    "DrtGetSearchResultSize",
    "DrtGetSearchResult",
    "DrtGetSearchPathSize",
    "DrtGetSearchPath",
    "DrtEndSearch",
    "DrtGetInstanceName",
    "DrtGetInstanceNameSize",
    "PeerDistStartup",
    "PeerDistShutdown",
    "PeerDistGetStatus",
    "PeerDistRegisterForStatusChangeNotification",
    "PeerDistUnregisterForStatusChangeNotification",
    "PeerDistServerPublishStream",
    "PeerDistServerPublishAddToStream",
    "PeerDistServerPublishCompleteStream",
    "PeerDistServerCloseStreamHandle",
    "PeerDistServerUnpublish",
    "PeerDistServerOpenContentInformation",
    "PeerDistServerRetrieveContentInformation",
    "PeerDistServerCloseContentInformation",
    "PeerDistServerCancelAsyncOperation",
    "PeerDistClientOpenContent",
    "PeerDistClientCloseContent",
    "PeerDistClientAddContentInformation",
    "PeerDistClientCompleteContentInformation",
    "PeerDistClientAddData",
    "PeerDistClientBlockRead",
    "PeerDistClientStreamRead",
    "PeerDistClientFlushContent",
    "PeerDistClientCancelAsyncOperation",
    "PeerDistGetStatusEx",
    "PeerDistRegisterForStatusChangeNotificationEx",
    "PeerDistGetOverlappedResult",
    "PeerDistServerOpenContentInformationEx",
    "PeerDistClientGetInformationByHandle",
]
