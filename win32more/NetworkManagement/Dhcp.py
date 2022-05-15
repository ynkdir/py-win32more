from win32more import *
import win32more.NetworkManagement.Dhcp
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.NetworkManagement.Dhcp, name, globals()[f"_define_{name}"]())
    return getattr(win32more.NetworkManagement.Dhcp, name)
def __dir__():
    return __all__
OPTION_PAD = 0
OPTION_SUBNET_MASK = 1
OPTION_TIME_OFFSET = 2
OPTION_ROUTER_ADDRESS = 3
OPTION_TIME_SERVERS = 4
OPTION_IEN116_NAME_SERVERS = 5
OPTION_DOMAIN_NAME_SERVERS = 6
OPTION_LOG_SERVERS = 7
OPTION_COOKIE_SERVERS = 8
OPTION_LPR_SERVERS = 9
OPTION_IMPRESS_SERVERS = 10
OPTION_RLP_SERVERS = 11
OPTION_HOST_NAME = 12
OPTION_BOOT_FILE_SIZE = 13
OPTION_MERIT_DUMP_FILE = 14
OPTION_DOMAIN_NAME = 15
OPTION_SWAP_SERVER = 16
OPTION_ROOT_DISK = 17
OPTION_EXTENSIONS_PATH = 18
OPTION_BE_A_ROUTER = 19
OPTION_NON_LOCAL_SOURCE_ROUTING = 20
OPTION_POLICY_FILTER_FOR_NLSR = 21
OPTION_MAX_REASSEMBLY_SIZE = 22
OPTION_DEFAULT_TTL = 23
OPTION_PMTU_AGING_TIMEOUT = 24
OPTION_PMTU_PLATEAU_TABLE = 25
OPTION_MTU = 26
OPTION_ALL_SUBNETS_MTU = 27
OPTION_BROADCAST_ADDRESS = 28
OPTION_PERFORM_MASK_DISCOVERY = 29
OPTION_BE_A_MASK_SUPPLIER = 30
OPTION_PERFORM_ROUTER_DISCOVERY = 31
OPTION_ROUTER_SOLICITATION_ADDR = 32
OPTION_STATIC_ROUTES = 33
OPTION_TRAILERS = 34
OPTION_ARP_CACHE_TIMEOUT = 35
OPTION_ETHERNET_ENCAPSULATION = 36
OPTION_TTL = 37
OPTION_KEEP_ALIVE_INTERVAL = 38
OPTION_KEEP_ALIVE_DATA_SIZE = 39
OPTION_NETWORK_INFO_SERVICE_DOM = 40
OPTION_NETWORK_INFO_SERVERS = 41
OPTION_NETWORK_TIME_SERVERS = 42
OPTION_VENDOR_SPEC_INFO = 43
OPTION_NETBIOS_NAME_SERVER = 44
OPTION_NETBIOS_DATAGRAM_SERVER = 45
OPTION_NETBIOS_NODE_TYPE = 46
OPTION_NETBIOS_SCOPE_OPTION = 47
OPTION_XWINDOW_FONT_SERVER = 48
OPTION_XWINDOW_DISPLAY_MANAGER = 49
OPTION_REQUESTED_ADDRESS = 50
OPTION_LEASE_TIME = 51
OPTION_OK_TO_OVERLAY = 52
OPTION_MESSAGE_TYPE = 53
OPTION_SERVER_IDENTIFIER = 54
OPTION_PARAMETER_REQUEST_LIST = 55
OPTION_MESSAGE = 56
OPTION_MESSAGE_LENGTH = 57
OPTION_RENEWAL_TIME = 58
OPTION_REBIND_TIME = 59
OPTION_CLIENT_CLASS_INFO = 60
OPTION_CLIENT_ID = 61
OPTION_TFTP_SERVER_NAME = 66
OPTION_BOOTFILE_NAME = 67
OPTION_MSFT_IE_PROXY = 252
OPTION_END = 255
DHCPCAPI_REQUEST_PERSISTENT = 1
DHCPCAPI_REQUEST_SYNCHRONOUS = 2
DHCPCAPI_REQUEST_ASYNCHRONOUS = 4
DHCPCAPI_REQUEST_CANCEL = 8
DHCPCAPI_REQUEST_MASK = 15
DHCPCAPI_REGISTER_HANDLE_EVENT = 1
DHCPCAPI_DEREGISTER_HANDLE_EVENT = 1
ERROR_DHCP_REGISTRY_INIT_FAILED = 20000
ERROR_DHCP_DATABASE_INIT_FAILED = 20001
ERROR_DHCP_RPC_INIT_FAILED = 20002
ERROR_DHCP_NETWORK_INIT_FAILED = 20003
ERROR_DHCP_SUBNET_EXITS = 20004
ERROR_DHCP_SUBNET_NOT_PRESENT = 20005
ERROR_DHCP_PRIMARY_NOT_FOUND = 20006
ERROR_DHCP_ELEMENT_CANT_REMOVE = 20007
ERROR_DHCP_OPTION_EXITS = 20009
ERROR_DHCP_OPTION_NOT_PRESENT = 20010
ERROR_DHCP_ADDRESS_NOT_AVAILABLE = 20011
ERROR_DHCP_RANGE_FULL = 20012
ERROR_DHCP_JET_ERROR = 20013
ERROR_DHCP_CLIENT_EXISTS = 20014
ERROR_DHCP_INVALID_DHCP_MESSAGE = 20015
ERROR_DHCP_INVALID_DHCP_CLIENT = 20016
ERROR_DHCP_SERVICE_PAUSED = 20017
ERROR_DHCP_NOT_RESERVED_CLIENT = 20018
ERROR_DHCP_RESERVED_CLIENT = 20019
ERROR_DHCP_RANGE_TOO_SMALL = 20020
ERROR_DHCP_IPRANGE_EXITS = 20021
ERROR_DHCP_RESERVEDIP_EXITS = 20022
ERROR_DHCP_INVALID_RANGE = 20023
ERROR_DHCP_RANGE_EXTENDED = 20024
ERROR_EXTEND_TOO_SMALL = 20025
WARNING_EXTENDED_LESS = 20026
ERROR_DHCP_JET_CONV_REQUIRED = 20027
ERROR_SERVER_INVALID_BOOT_FILE_TABLE = 20028
ERROR_SERVER_UNKNOWN_BOOT_FILE_NAME = 20029
ERROR_DHCP_SUPER_SCOPE_NAME_TOO_LONG = 20030
ERROR_DHCP_IP_ADDRESS_IN_USE = 20032
ERROR_DHCP_LOG_FILE_PATH_TOO_LONG = 20033
ERROR_DHCP_UNSUPPORTED_CLIENT = 20034
ERROR_DHCP_JET97_CONV_REQUIRED = 20036
ERROR_DHCP_ROGUE_INIT_FAILED = 20037
ERROR_DHCP_ROGUE_SAMSHUTDOWN = 20038
ERROR_DHCP_ROGUE_NOT_AUTHORIZED = 20039
ERROR_DHCP_ROGUE_DS_UNREACHABLE = 20040
ERROR_DHCP_ROGUE_DS_CONFLICT = 20041
ERROR_DHCP_ROGUE_NOT_OUR_ENTERPRISE = 20042
ERROR_DHCP_ROGUE_STANDALONE_IN_DS = 20043
ERROR_DHCP_CLASS_NOT_FOUND = 20044
ERROR_DHCP_CLASS_ALREADY_EXISTS = 20045
ERROR_DHCP_SCOPE_NAME_TOO_LONG = 20046
ERROR_DHCP_DEFAULT_SCOPE_EXITS = 20047
ERROR_DHCP_CANT_CHANGE_ATTRIBUTE = 20048
ERROR_DHCP_IPRANGE_CONV_ILLEGAL = 20049
ERROR_DHCP_NETWORK_CHANGED = 20050
ERROR_DHCP_CANNOT_MODIFY_BINDINGS = 20051
ERROR_DHCP_SUBNET_EXISTS = 20052
ERROR_DHCP_MSCOPE_EXISTS = 20053
ERROR_MSCOPE_RANGE_TOO_SMALL = 20054
ERROR_DHCP_EXEMPTION_EXISTS = 20055
ERROR_DHCP_EXEMPTION_NOT_PRESENT = 20056
ERROR_DHCP_INVALID_PARAMETER_OPTION32 = 20057
ERROR_DDS_NO_DS_AVAILABLE = 20070
ERROR_DDS_NO_DHCP_ROOT = 20071
ERROR_DDS_UNEXPECTED_ERROR = 20072
ERROR_DDS_TOO_MANY_ERRORS = 20073
ERROR_DDS_DHCP_SERVER_NOT_FOUND = 20074
ERROR_DDS_OPTION_ALREADY_EXISTS = 20075
ERROR_DDS_OPTION_DOES_NOT_EXIST = 20076
ERROR_DDS_CLASS_EXISTS = 20077
ERROR_DDS_CLASS_DOES_NOT_EXIST = 20078
ERROR_DDS_SERVER_ALREADY_EXISTS = 20079
ERROR_DDS_SERVER_DOES_NOT_EXIST = 20080
ERROR_DDS_SERVER_ADDRESS_MISMATCH = 20081
ERROR_DDS_SUBNET_EXISTS = 20082
ERROR_DDS_SUBNET_HAS_DIFF_SSCOPE = 20083
ERROR_DDS_SUBNET_NOT_PRESENT = 20084
ERROR_DDS_RESERVATION_NOT_PRESENT = 20085
ERROR_DDS_RESERVATION_CONFLICT = 20086
ERROR_DDS_POSSIBLE_RANGE_CONFLICT = 20087
ERROR_DDS_RANGE_DOES_NOT_EXIST = 20088
ERROR_DHCP_DELETE_BUILTIN_CLASS = 20089
ERROR_DHCP_INVALID_SUBNET_PREFIX = 20091
ERROR_DHCP_INVALID_DELAY = 20092
ERROR_DHCP_LINKLAYER_ADDRESS_EXISTS = 20093
ERROR_DHCP_LINKLAYER_ADDRESS_RESERVATION_EXISTS = 20094
ERROR_DHCP_LINKLAYER_ADDRESS_DOES_NOT_EXIST = 20095
ERROR_DHCP_HARDWARE_ADDRESS_TYPE_ALREADY_EXEMPT = 20101
ERROR_DHCP_UNDEFINED_HARDWARE_ADDRESS_TYPE = 20102
ERROR_DHCP_OPTION_TYPE_MISMATCH = 20103
ERROR_DHCP_POLICY_BAD_PARENT_EXPR = 20104
ERROR_DHCP_POLICY_EXISTS = 20105
ERROR_DHCP_POLICY_RANGE_EXISTS = 20106
ERROR_DHCP_POLICY_RANGE_BAD = 20107
ERROR_DHCP_RANGE_INVALID_IN_SERVER_POLICY = 20108
ERROR_DHCP_INVALID_POLICY_EXPRESSION = 20109
ERROR_DHCP_INVALID_PROCESSING_ORDER = 20110
ERROR_DHCP_POLICY_NOT_FOUND = 20111
ERROR_SCOPE_RANGE_POLICY_RANGE_CONFLICT = 20112
ERROR_DHCP_FO_SCOPE_ALREADY_IN_RELATIONSHIP = 20113
ERROR_DHCP_FO_RELATIONSHIP_EXISTS = 20114
ERROR_DHCP_FO_RELATIONSHIP_DOES_NOT_EXIST = 20115
ERROR_DHCP_FO_SCOPE_NOT_IN_RELATIONSHIP = 20116
ERROR_DHCP_FO_RELATION_IS_SECONDARY = 20117
ERROR_DHCP_FO_NOT_SUPPORTED = 20118
ERROR_DHCP_FO_TIME_OUT_OF_SYNC = 20119
ERROR_DHCP_FO_STATE_NOT_NORMAL = 20120
ERROR_DHCP_NO_ADMIN_PERMISSION = 20121
ERROR_DHCP_SERVER_NOT_REACHABLE = 20122
ERROR_DHCP_SERVER_NOT_RUNNING = 20123
ERROR_DHCP_SERVER_NAME_NOT_RESOLVED = 20124
ERROR_DHCP_FO_RELATIONSHIP_NAME_TOO_LONG = 20125
ERROR_DHCP_REACHED_END_OF_SELECTION = 20126
ERROR_DHCP_FO_ADDSCOPE_LEASES_NOT_SYNCED = 20127
ERROR_DHCP_FO_MAX_RELATIONSHIPS = 20128
ERROR_DHCP_FO_IPRANGE_TYPE_CONV_ILLEGAL = 20129
ERROR_DHCP_FO_MAX_ADD_SCOPES = 20130
ERROR_DHCP_FO_BOOT_NOT_SUPPORTED = 20131
ERROR_DHCP_FO_RANGE_PART_OF_REL = 20132
ERROR_DHCP_FO_SCOPE_SYNC_IN_PROGRESS = 20133
ERROR_DHCP_FO_FEATURE_NOT_SUPPORTED = 20134
ERROR_DHCP_POLICY_FQDN_RANGE_UNSUPPORTED = 20135
ERROR_DHCP_POLICY_FQDN_OPTION_UNSUPPORTED = 20136
ERROR_DHCP_POLICY_EDIT_FQDN_UNSUPPORTED = 20137
ERROR_DHCP_NAP_NOT_SUPPORTED = 20138
ERROR_LAST_DHCP_SERVER_ERROR = 20139
DHCP_SUBNET_INFO_VQ_FLAG_QUARANTINE = 1
MAX_PATTERN_LENGTH = 255
MAC_ADDRESS_LENGTH = 6
HWTYPE_ETHERNET_10MB = 1
FILTER_STATUS_NONE = 1
FILTER_STATUS_FULL_MATCH_IN_ALLOW_LIST = 2
FILTER_STATUS_FULL_MATCH_IN_DENY_LIST = 4
FILTER_STATUS_WILDCARD_MATCH_IN_ALLOW_LIST = 8
FILTER_STATUS_WILDCARD_MATCH_IN_DENY_LIST = 16
Set_APIProtocolSupport = 1
Set_DatabaseName = 2
Set_DatabasePath = 4
Set_BackupPath = 8
Set_BackupInterval = 16
Set_DatabaseLoggingFlag = 32
Set_RestoreFlag = 64
Set_DatabaseCleanupInterval = 128
Set_DebugFlag = 256
Set_PingRetries = 512
Set_BootFileTable = 1024
Set_AuditLogState = 2048
Set_QuarantineON = 4096
Set_QuarantineDefFail = 8192
CLIENT_TYPE_UNSPECIFIED = 0
CLIENT_TYPE_DHCP = 1
CLIENT_TYPE_BOOTP = 2
CLIENT_TYPE_RESERVATION_FLAG = 4
CLIENT_TYPE_NONE = 100
Set_UnicastFlag = 1
Set_RapidCommitFlag = 2
Set_PreferredLifetime = 4
Set_ValidLifetime = 8
Set_T1 = 16
Set_T2 = 32
Set_PreferredLifetimeIATA = 64
Set_ValidLifetimeIATA = 128
V5_ADDRESS_STATE_OFFERED = 0
V5_ADDRESS_STATE_ACTIVE = 1
V5_ADDRESS_STATE_DECLINED = 2
V5_ADDRESS_STATE_DOOM = 3
V5_ADDRESS_BIT_DELETED = 128
V5_ADDRESS_BIT_UNREGISTERED = 64
V5_ADDRESS_BIT_BOTH_REC = 32
V5_ADDRESS_EX_BIT_DISABLE_PTR_RR = 1
DNS_FLAG_ENABLED = 1
DNS_FLAG_UPDATE_DOWNLEVEL = 2
DNS_FLAG_CLEANUP_EXPIRED = 4
DNS_FLAG_UPDATE_BOTH_ALWAYS = 16
DNS_FLAG_UPDATE_DHCID = 32
DNS_FLAG_DISABLE_PTR_UPDATE = 64
DNS_FLAG_HAS_DNS_SUFFIX = 128
DHCP_OPT_ENUM_IGNORE_VENDOR = 1
DHCP_OPT_ENUM_USE_CLASSNAME = 2
DHCP_FLAGS_DONT_ACCESS_DS = 1
DHCP_FLAGS_DONT_DO_RPC = 2
DHCP_FLAGS_OPTION_IS_VENDOR = 3
DHCP_ATTRIB_BOOL_IS_ROGUE = 1
DHCP_ATTRIB_BOOL_IS_DYNBOOTP = 2
DHCP_ATTRIB_BOOL_IS_PART_OF_DSDC = 3
DHCP_ATTRIB_BOOL_IS_BINDING_AWARE = 4
DHCP_ATTRIB_BOOL_IS_ADMIN = 5
DHCP_ATTRIB_ULONG_RESTORE_STATUS = 6
DHCP_ATTRIB_TYPE_BOOL = 1
DHCP_ATTRIB_TYPE_ULONG = 2
DHCP_ENDPOINT_FLAG_CANT_MODIFY = 1
QUARANTIN_OPTION_BASE = 43220
QUARANTINE_SCOPE_QUARPROFILE_OPTION = 43221
QUARANTINE_CONFIG_OPTION = 43222
ADDRESS_TYPE_IANA = 0
ADDRESS_TYPE_IATA = 1
DHCP_MIN_DELAY = 0
DHCP_MAX_DELAY = 1000
DHCP_FAILOVER_DELETE_SCOPES = 1
DHCP_FAILOVER_MAX_NUM_ADD_SCOPES = 400
DHCP_FAILOVER_MAX_NUM_REL = 31
MCLT = 1
SAFEPERIOD = 2
CHANGESTATE = 4
PERCENTAGE = 8
MODE = 16
PREVSTATE = 32
SHAREDSECRET = 64
DHCP_CONTROL_START = 1
DHCP_CONTROL_STOP = 2
DHCP_CONTROL_PAUSE = 3
DHCP_CONTROL_CONTINUE = 4
DHCP_DROP_DUPLICATE = 1
DHCP_DROP_NOMEM = 2
DHCP_DROP_INTERNAL_ERROR = 3
DHCP_DROP_TIMEOUT = 4
DHCP_DROP_UNAUTH = 5
DHCP_DROP_PAUSED = 6
DHCP_DROP_NO_SUBNETS = 7
DHCP_DROP_INVALID = 8
DHCP_DROP_WRONG_SERVER = 9
DHCP_DROP_NOADDRESS = 10
DHCP_DROP_PROCESSED = 11
DHCP_DROP_GEN_FAILURE = 256
DHCP_SEND_PACKET = 268435456
DHCP_PROB_CONFLICT = 536870913
DHCP_PROB_DECLINE = 536870914
DHCP_PROB_RELEASE = 536870915
DHCP_PROB_NACKED = 536870916
DHCP_GIVE_ADDRESS_NEW = 805306369
DHCP_GIVE_ADDRESS_OLD = 805306370
DHCP_CLIENT_BOOTP = 805306371
DHCP_CLIENT_DHCP = 805306372
DHCPV6_OPTION_CLIENTID = 1
DHCPV6_OPTION_SERVERID = 2
DHCPV6_OPTION_IA_NA = 3
DHCPV6_OPTION_IA_TA = 4
DHCPV6_OPTION_ORO = 6
DHCPV6_OPTION_PREFERENCE = 7
DHCPV6_OPTION_UNICAST = 12
DHCPV6_OPTION_RAPID_COMMIT = 14
DHCPV6_OPTION_USER_CLASS = 15
DHCPV6_OPTION_VENDOR_CLASS = 16
DHCPV6_OPTION_VENDOR_OPTS = 17
DHCPV6_OPTION_RECONF_MSG = 19
DHCPV6_OPTION_SIP_SERVERS_NAMES = 21
DHCPV6_OPTION_SIP_SERVERS_ADDRS = 22
DHCPV6_OPTION_DNS_SERVERS = 23
DHCPV6_OPTION_DOMAIN_LIST = 24
DHCPV6_OPTION_IA_PD = 25
DHCPV6_OPTION_NIS_SERVERS = 27
DHCPV6_OPTION_NISP_SERVERS = 28
DHCPV6_OPTION_NIS_DOMAIN_NAME = 29
DHCPV6_OPTION_NISP_DOMAIN_NAME = 30
def _define_DHCPV6CAPI_PARAMS_head():
    class DHCPV6CAPI_PARAMS(Structure):
        pass
    return DHCPV6CAPI_PARAMS
def _define_DHCPV6CAPI_PARAMS():
    DHCPV6CAPI_PARAMS = win32more.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_head
    DHCPV6CAPI_PARAMS._fields_ = [
        ("Flags", UInt32),
        ("OptionId", UInt32),
        ("IsVendor", win32more.Foundation.BOOL),
        ("Data", c_char_p_no),
        ("nBytesData", UInt32),
    ]
    return DHCPV6CAPI_PARAMS
def _define_DHCPV6CAPI_PARAMS_ARRAY_head():
    class DHCPV6CAPI_PARAMS_ARRAY(Structure):
        pass
    return DHCPV6CAPI_PARAMS_ARRAY
def _define_DHCPV6CAPI_PARAMS_ARRAY():
    DHCPV6CAPI_PARAMS_ARRAY = win32more.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_ARRAY_head
    DHCPV6CAPI_PARAMS_ARRAY._fields_ = [
        ("nParams", UInt32),
        ("Params", POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_head)),
    ]
    return DHCPV6CAPI_PARAMS_ARRAY
def _define_DHCPV6CAPI_CLASSID_head():
    class DHCPV6CAPI_CLASSID(Structure):
        pass
    return DHCPV6CAPI_CLASSID
def _define_DHCPV6CAPI_CLASSID():
    DHCPV6CAPI_CLASSID = win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head
    DHCPV6CAPI_CLASSID._fields_ = [
        ("Flags", UInt32),
        ("Data", c_char_p_no),
        ("nBytesData", UInt32),
    ]
    return DHCPV6CAPI_CLASSID
StatusCode = Int32
STATUS_NO_ERROR = 0
STATUS_UNSPECIFIED_FAILURE = 1
STATUS_NO_BINDING = 3
STATUS_NOPREFIX_AVAIL = 6
def _define_DHCPV6Prefix_head():
    class DHCPV6Prefix(Structure):
        pass
    return DHCPV6Prefix
def _define_DHCPV6Prefix():
    DHCPV6Prefix = win32more.NetworkManagement.Dhcp.DHCPV6Prefix_head
    DHCPV6Prefix._fields_ = [
        ("prefix", Byte * 16),
        ("prefixLength", UInt32),
        ("preferredLifeTime", UInt32),
        ("validLifeTime", UInt32),
        ("status", win32more.NetworkManagement.Dhcp.StatusCode),
    ]
    return DHCPV6Prefix
def _define_DHCPV6PrefixLeaseInformation_head():
    class DHCPV6PrefixLeaseInformation(Structure):
        pass
    return DHCPV6PrefixLeaseInformation
def _define_DHCPV6PrefixLeaseInformation():
    DHCPV6PrefixLeaseInformation = win32more.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head
    DHCPV6PrefixLeaseInformation._fields_ = [
        ("nPrefixes", UInt32),
        ("prefixArray", POINTER(win32more.NetworkManagement.Dhcp.DHCPV6Prefix_head)),
        ("iaid", UInt32),
        ("T1", Int64),
        ("T2", Int64),
        ("MaxLeaseExpirationTime", Int64),
        ("LastRenewalTime", Int64),
        ("status", win32more.NetworkManagement.Dhcp.StatusCode),
        ("ServerId", c_char_p_no),
        ("ServerIdLen", UInt32),
    ]
    return DHCPV6PrefixLeaseInformation
def _define_DHCPAPI_PARAMS_head():
    class DHCPAPI_PARAMS(Structure):
        pass
    return DHCPAPI_PARAMS
def _define_DHCPAPI_PARAMS():
    DHCPAPI_PARAMS = win32more.NetworkManagement.Dhcp.DHCPAPI_PARAMS_head
    DHCPAPI_PARAMS._fields_ = [
        ("Flags", UInt32),
        ("OptionId", UInt32),
        ("IsVendor", win32more.Foundation.BOOL),
        ("Data", c_char_p_no),
        ("nBytesData", UInt32),
    ]
    return DHCPAPI_PARAMS
def _define_DHCPCAPI_PARAMS_ARRAY_head():
    class DHCPCAPI_PARAMS_ARRAY(Structure):
        pass
    return DHCPCAPI_PARAMS_ARRAY
def _define_DHCPCAPI_PARAMS_ARRAY():
    DHCPCAPI_PARAMS_ARRAY = win32more.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY_head
    DHCPCAPI_PARAMS_ARRAY._fields_ = [
        ("nParams", UInt32),
        ("Params", POINTER(win32more.NetworkManagement.Dhcp.DHCPAPI_PARAMS_head)),
    ]
    return DHCPCAPI_PARAMS_ARRAY
def _define_DHCPCAPI_CLASSID_head():
    class DHCPCAPI_CLASSID(Structure):
        pass
    return DHCPCAPI_CLASSID
def _define_DHCPCAPI_CLASSID():
    DHCPCAPI_CLASSID = win32more.NetworkManagement.Dhcp.DHCPCAPI_CLASSID_head
    DHCPCAPI_CLASSID._fields_ = [
        ("Flags", UInt32),
        ("Data", c_char_p_no),
        ("nBytesData", UInt32),
    ]
    return DHCPCAPI_CLASSID
def _define_DHCP_SERVER_OPTIONS_head():
    class DHCP_SERVER_OPTIONS(Structure):
        pass
    return DHCP_SERVER_OPTIONS
def _define_DHCP_SERVER_OPTIONS():
    DHCP_SERVER_OPTIONS = win32more.NetworkManagement.Dhcp.DHCP_SERVER_OPTIONS_head
    DHCP_SERVER_OPTIONS._fields_ = [
        ("MessageType", c_char_p_no),
        ("SubnetMask", POINTER(UInt32)),
        ("RequestedAddress", POINTER(UInt32)),
        ("RequestLeaseTime", POINTER(UInt32)),
        ("OverlayFields", c_char_p_no),
        ("RouterAddress", POINTER(UInt32)),
        ("Server", POINTER(UInt32)),
        ("ParameterRequestList", c_char_p_no),
        ("ParameterRequestListLength", UInt32),
        ("MachineName", win32more.Foundation.PSTR),
        ("MachineNameLength", UInt32),
        ("ClientHardwareAddressType", Byte),
        ("ClientHardwareAddressLength", Byte),
        ("ClientHardwareAddress", c_char_p_no),
        ("ClassIdentifier", win32more.Foundation.PSTR),
        ("ClassIdentifierLength", UInt32),
        ("VendorClass", c_char_p_no),
        ("VendorClassLength", UInt32),
        ("DNSFlags", UInt32),
        ("DNSNameLength", UInt32),
        ("DNSName", c_char_p_no),
        ("DSDomainNameRequested", win32more.Foundation.BOOLEAN),
        ("DSDomainName", win32more.Foundation.PSTR),
        ("DSDomainNameLen", UInt32),
        ("ScopeId", POINTER(UInt32)),
    ]
    return DHCP_SERVER_OPTIONS
def _define_LPDHCP_CONTROL():
    return CFUNCTYPE(UInt32,UInt32,c_void_p, use_last_error=False)
def _define_LPDHCP_NEWPKT():
    return CFUNCTYPE(UInt32,POINTER(c_char_p_no),POINTER(UInt32),UInt32,c_void_p,POINTER(c_void_p),POINTER(Int32), use_last_error=False)
def _define_LPDHCP_DROP_SEND():
    return CFUNCTYPE(UInt32,POINTER(c_char_p_no),POINTER(UInt32),UInt32,UInt32,c_void_p,c_void_p, use_last_error=False)
def _define_LPDHCP_PROB():
    return CFUNCTYPE(UInt32,c_char_p_no,UInt32,UInt32,UInt32,UInt32,c_void_p,c_void_p, use_last_error=False)
def _define_LPDHCP_GIVE_ADDRESS():
    return CFUNCTYPE(UInt32,c_char_p_no,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,c_void_p,c_void_p, use_last_error=False)
def _define_LPDHCP_HANDLE_OPTIONS():
    return CFUNCTYPE(UInt32,c_char_p_no,UInt32,c_void_p,c_void_p,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_OPTIONS_head), use_last_error=False)
def _define_LPDHCP_DELETE_CLIENT():
    return CFUNCTYPE(UInt32,UInt32,c_char_p_no,UInt32,UInt32,UInt32, use_last_error=False)
def _define_DHCP_CALLOUT_TABLE_head():
    class DHCP_CALLOUT_TABLE(Structure):
        pass
    return DHCP_CALLOUT_TABLE
def _define_DHCP_CALLOUT_TABLE():
    DHCP_CALLOUT_TABLE = win32more.NetworkManagement.Dhcp.DHCP_CALLOUT_TABLE_head
    DHCP_CALLOUT_TABLE._fields_ = [
        ("DhcpControlHook", win32more.NetworkManagement.Dhcp.LPDHCP_CONTROL),
        ("DhcpNewPktHook", win32more.NetworkManagement.Dhcp.LPDHCP_NEWPKT),
        ("DhcpPktDropHook", win32more.NetworkManagement.Dhcp.LPDHCP_DROP_SEND),
        ("DhcpPktSendHook", win32more.NetworkManagement.Dhcp.LPDHCP_DROP_SEND),
        ("DhcpAddressDelHook", win32more.NetworkManagement.Dhcp.LPDHCP_PROB),
        ("DhcpAddressOfferHook", win32more.NetworkManagement.Dhcp.LPDHCP_GIVE_ADDRESS),
        ("DhcpHandleOptionsHook", win32more.NetworkManagement.Dhcp.LPDHCP_HANDLE_OPTIONS),
        ("DhcpDeleteClientHook", win32more.NetworkManagement.Dhcp.LPDHCP_DELETE_CLIENT),
        ("DhcpExtensionHook", c_void_p),
        ("DhcpReservedHook", c_void_p),
    ]
    return DHCP_CALLOUT_TABLE
def _define_LPDHCP_ENTRY_POINT_FUNC():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CALLOUT_TABLE_head), use_last_error=False)
def _define_DATE_TIME_head():
    class DATE_TIME(Structure):
        pass
    return DATE_TIME
def _define_DATE_TIME():
    DATE_TIME = win32more.NetworkManagement.Dhcp.DATE_TIME_head
    DATE_TIME._fields_ = [
        ("dwLowDateTime", UInt32),
        ("dwHighDateTime", UInt32),
    ]
    return DATE_TIME
def _define_DHCP_IP_RANGE_head():
    class DHCP_IP_RANGE(Structure):
        pass
    return DHCP_IP_RANGE
def _define_DHCP_IP_RANGE():
    DHCP_IP_RANGE = win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head
    DHCP_IP_RANGE._fields_ = [
        ("StartAddress", UInt32),
        ("EndAddress", UInt32),
    ]
    return DHCP_IP_RANGE
def _define_DHCP_BINARY_DATA_head():
    class DHCP_BINARY_DATA(Structure):
        pass
    return DHCP_BINARY_DATA
def _define_DHCP_BINARY_DATA():
    DHCP_BINARY_DATA = win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head
    DHCP_BINARY_DATA._fields_ = [
        ("DataLength", UInt32),
        ("Data", c_char_p_no),
    ]
    return DHCP_BINARY_DATA
def _define_DHCP_HOST_INFO_head():
    class DHCP_HOST_INFO(Structure):
        pass
    return DHCP_HOST_INFO
def _define_DHCP_HOST_INFO():
    DHCP_HOST_INFO = win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_head
    DHCP_HOST_INFO._fields_ = [
        ("IpAddress", UInt32),
        ("NetBiosName", win32more.Foundation.PWSTR),
        ("HostName", win32more.Foundation.PWSTR),
    ]
    return DHCP_HOST_INFO
DHCP_FORCE_FLAG = Int32
DHCP_FORCE_FLAG_DhcpFullForce = 0
DHCP_FORCE_FLAG_DhcpNoForce = 1
DHCP_FORCE_FLAG_DhcpFailoverForce = 2
def _define_DWORD_DWORD_head():
    class DWORD_DWORD(Structure):
        pass
    return DWORD_DWORD
def _define_DWORD_DWORD():
    DWORD_DWORD = win32more.NetworkManagement.Dhcp.DWORD_DWORD_head
    DWORD_DWORD._fields_ = [
        ("DWord1", UInt32),
        ("DWord2", UInt32),
    ]
    return DWORD_DWORD
DHCP_SUBNET_STATE = Int32
DHCP_SUBNET_STATE_DhcpSubnetEnabled = 0
DHCP_SUBNET_STATE_DhcpSubnetDisabled = 1
DHCP_SUBNET_STATE_DhcpSubnetEnabledSwitched = 2
DHCP_SUBNET_STATE_DhcpSubnetDisabledSwitched = 3
DHCP_SUBNET_STATE_DhcpSubnetInvalidState = 4
def _define_DHCP_SUBNET_INFO_head():
    class DHCP_SUBNET_INFO(Structure):
        pass
    return DHCP_SUBNET_INFO
def _define_DHCP_SUBNET_INFO():
    DHCP_SUBNET_INFO = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head
    DHCP_SUBNET_INFO._fields_ = [
        ("SubnetAddress", UInt32),
        ("SubnetMask", UInt32),
        ("SubnetName", win32more.Foundation.PWSTR),
        ("SubnetComment", win32more.Foundation.PWSTR),
        ("PrimaryHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("SubnetState", win32more.NetworkManagement.Dhcp.DHCP_SUBNET_STATE),
    ]
    return DHCP_SUBNET_INFO
def _define_DHCP_SUBNET_INFO_VQ_head():
    class DHCP_SUBNET_INFO_VQ(Structure):
        pass
    return DHCP_SUBNET_INFO_VQ
def _define_DHCP_SUBNET_INFO_VQ():
    DHCP_SUBNET_INFO_VQ = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head
    DHCP_SUBNET_INFO_VQ._fields_ = [
        ("SubnetAddress", UInt32),
        ("SubnetMask", UInt32),
        ("SubnetName", win32more.Foundation.PWSTR),
        ("SubnetComment", win32more.Foundation.PWSTR),
        ("PrimaryHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("SubnetState", win32more.NetworkManagement.Dhcp.DHCP_SUBNET_STATE),
        ("QuarantineOn", UInt32),
        ("Reserved1", UInt32),
        ("Reserved2", UInt32),
        ("Reserved3", Int64),
        ("Reserved4", Int64),
    ]
    return DHCP_SUBNET_INFO_VQ
def _define_DHCP_IP_ARRAY_head():
    class DHCP_IP_ARRAY(Structure):
        pass
    return DHCP_IP_ARRAY
def _define_DHCP_IP_ARRAY():
    DHCP_IP_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head
    DHCP_IP_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(UInt32)),
    ]
    return DHCP_IP_ARRAY
def _define_DHCP_IP_CLUSTER_head():
    class DHCP_IP_CLUSTER(Structure):
        pass
    return DHCP_IP_CLUSTER
def _define_DHCP_IP_CLUSTER():
    DHCP_IP_CLUSTER = win32more.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head
    DHCP_IP_CLUSTER._fields_ = [
        ("ClusterAddress", UInt32),
        ("ClusterMask", UInt32),
    ]
    return DHCP_IP_CLUSTER
def _define_DHCP_IP_RESERVATION_head():
    class DHCP_IP_RESERVATION(Structure):
        pass
    return DHCP_IP_RESERVATION
def _define_DHCP_IP_RESERVATION():
    DHCP_IP_RESERVATION = win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_head
    DHCP_IP_RESERVATION._fields_ = [
        ("ReservedIpAddress", UInt32),
        ("ReservedForClient", POINTER(win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)),
    ]
    return DHCP_IP_RESERVATION
DHCP_SUBNET_ELEMENT_TYPE = Int32
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRanges = 0
DHCP_SUBNET_ELEMENT_TYPE_DhcpSecondaryHosts = 1
DHCP_SUBNET_ELEMENT_TYPE_DhcpReservedIps = 2
DHCP_SUBNET_ELEMENT_TYPE_DhcpExcludedIpRanges = 3
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpUsedClusters = 4
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpOnly = 5
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpBootp = 6
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesBootpOnly = 7
def _define_DHCP_SUBNET_ELEMENT_DATA_head():
    class DHCP_SUBNET_ELEMENT_DATA(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_DATA
def _define_DHCP_SUBNET_ELEMENT_DATA():
    DHCP_SUBNET_ELEMENT_DATA = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head
    class DHCP_SUBNET_ELEMENT_DATA_DHCP_SUBNET_ELEMENT_UNION(Union):
        pass
    DHCP_SUBNET_ELEMENT_DATA_DHCP_SUBNET_ELEMENT_UNION._fields_ = [
        ("IpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)),
        ("SecondaryHost", POINTER(win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)),
        ("ReservedIp", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_head)),
        ("ExcludeIpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)),
        ("IpUsedCluster", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)),
    ]
    DHCP_SUBNET_ELEMENT_DATA._fields_ = [
        ("ElementType", win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE),
        ("Element", DHCP_SUBNET_ELEMENT_DATA_DHCP_SUBNET_ELEMENT_UNION),
    ]
    return DHCP_SUBNET_ELEMENT_DATA
def _define_DHCP_SUBNET_ELEMENT_UNION_head():
    class DHCP_SUBNET_ELEMENT_UNION(Union):
        pass
    return DHCP_SUBNET_ELEMENT_UNION
def _define_DHCP_SUBNET_ELEMENT_UNION():
    DHCP_SUBNET_ELEMENT_UNION = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_UNION_head
    return DHCP_SUBNET_ELEMENT_UNION
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY_head():
    class DHCP_SUBNET_ELEMENT_INFO_ARRAY(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY():
    DHCP_SUBNET_ELEMENT_INFO_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_head
    DHCP_SUBNET_ELEMENT_INFO_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head)),
    ]
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY
def _define_DHCP_IPV6_ADDRESS_head():
    class DHCP_IPV6_ADDRESS(Structure):
        pass
    return DHCP_IPV6_ADDRESS
def _define_DHCP_IPV6_ADDRESS():
    DHCP_IPV6_ADDRESS = win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS_head
    DHCP_IPV6_ADDRESS._fields_ = [
        ("HighOrderBits", UInt64),
        ("LowOrderBits", UInt64),
    ]
    return DHCP_IPV6_ADDRESS
DHCP_FILTER_LIST_TYPE = Int32
DHCP_FILTER_LIST_TYPE_Deny = 0
DHCP_FILTER_LIST_TYPE_Allow = 1
def _define_DHCP_ADDR_PATTERN_head():
    class DHCP_ADDR_PATTERN(Structure):
        pass
    return DHCP_ADDR_PATTERN
def _define_DHCP_ADDR_PATTERN():
    DHCP_ADDR_PATTERN = win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN_head
    DHCP_ADDR_PATTERN._fields_ = [
        ("MatchHWType", win32more.Foundation.BOOL),
        ("HWType", Byte),
        ("IsWildcard", win32more.Foundation.BOOL),
        ("Length", Byte),
        ("Pattern", Byte * 255),
    ]
    return DHCP_ADDR_PATTERN
def _define_DHCP_FILTER_ADD_INFO_head():
    class DHCP_FILTER_ADD_INFO(Structure):
        pass
    return DHCP_FILTER_ADD_INFO
def _define_DHCP_FILTER_ADD_INFO():
    DHCP_FILTER_ADD_INFO = win32more.NetworkManagement.Dhcp.DHCP_FILTER_ADD_INFO_head
    DHCP_FILTER_ADD_INFO._fields_ = [
        ("AddrPatt", win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN),
        ("Comment", win32more.Foundation.PWSTR),
        ("ListType", win32more.NetworkManagement.Dhcp.DHCP_FILTER_LIST_TYPE),
    ]
    return DHCP_FILTER_ADD_INFO
def _define_DHCP_FILTER_GLOBAL_INFO_head():
    class DHCP_FILTER_GLOBAL_INFO(Structure):
        pass
    return DHCP_FILTER_GLOBAL_INFO
def _define_DHCP_FILTER_GLOBAL_INFO():
    DHCP_FILTER_GLOBAL_INFO = win32more.NetworkManagement.Dhcp.DHCP_FILTER_GLOBAL_INFO_head
    DHCP_FILTER_GLOBAL_INFO._fields_ = [
        ("EnforceAllowList", win32more.Foundation.BOOL),
        ("EnforceDenyList", win32more.Foundation.BOOL),
    ]
    return DHCP_FILTER_GLOBAL_INFO
def _define_DHCP_FILTER_RECORD_head():
    class DHCP_FILTER_RECORD(Structure):
        pass
    return DHCP_FILTER_RECORD
def _define_DHCP_FILTER_RECORD():
    DHCP_FILTER_RECORD = win32more.NetworkManagement.Dhcp.DHCP_FILTER_RECORD_head
    DHCP_FILTER_RECORD._fields_ = [
        ("AddrPatt", win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN),
        ("Comment", win32more.Foundation.PWSTR),
    ]
    return DHCP_FILTER_RECORD
def _define_DHCP_FILTER_ENUM_INFO_head():
    class DHCP_FILTER_ENUM_INFO(Structure):
        pass
    return DHCP_FILTER_ENUM_INFO
def _define_DHCP_FILTER_ENUM_INFO():
    DHCP_FILTER_ENUM_INFO = win32more.NetworkManagement.Dhcp.DHCP_FILTER_ENUM_INFO_head
    DHCP_FILTER_ENUM_INFO._fields_ = [
        ("NumElements", UInt32),
        ("pEnumRecords", POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_RECORD_head)),
    ]
    return DHCP_FILTER_ENUM_INFO
DHCP_OPTION_DATA_TYPE = Int32
DHCP_OPTION_DATA_TYPE_DhcpByteOption = 0
DHCP_OPTION_DATA_TYPE_DhcpWordOption = 1
DHCP_OPTION_DATA_TYPE_DhcpDWordOption = 2
DHCP_OPTION_DATA_TYPE_DhcpDWordDWordOption = 3
DHCP_OPTION_DATA_TYPE_DhcpIpAddressOption = 4
DHCP_OPTION_DATA_TYPE_DhcpStringDataOption = 5
DHCP_OPTION_DATA_TYPE_DhcpBinaryDataOption = 6
DHCP_OPTION_DATA_TYPE_DhcpEncapsulatedDataOption = 7
DHCP_OPTION_DATA_TYPE_DhcpIpv6AddressOption = 8
def _define_DHCP_OPTION_DATA_ELEMENT_head():
    class DHCP_OPTION_DATA_ELEMENT(Structure):
        pass
    return DHCP_OPTION_DATA_ELEMENT
def _define_DHCP_OPTION_DATA_ELEMENT():
    DHCP_OPTION_DATA_ELEMENT = win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_ELEMENT_head
    class DHCP_OPTION_DATA_ELEMENT_DHCP_OPTION_ELEMENT_UNION(Union):
        pass
    DHCP_OPTION_DATA_ELEMENT_DHCP_OPTION_ELEMENT_UNION._fields_ = [
        ("ByteOption", Byte),
        ("WordOption", UInt16),
        ("DWordOption", UInt32),
        ("DWordDWordOption", win32more.NetworkManagement.Dhcp.DWORD_DWORD),
        ("IpAddressOption", UInt32),
        ("StringDataOption", win32more.Foundation.PWSTR),
        ("BinaryDataOption", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("EncapsulatedDataOption", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("Ipv6AddressDataOption", win32more.Foundation.PWSTR),
    ]
    DHCP_OPTION_DATA_ELEMENT._fields_ = [
        ("OptionType", win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_TYPE),
        ("Element", DHCP_OPTION_DATA_ELEMENT_DHCP_OPTION_ELEMENT_UNION),
    ]
    return DHCP_OPTION_DATA_ELEMENT
def _define_DHCP_OPTION_ELEMENT_UNION_head():
    class DHCP_OPTION_ELEMENT_UNION(Union):
        pass
    return DHCP_OPTION_ELEMENT_UNION
def _define_DHCP_OPTION_ELEMENT_UNION():
    DHCP_OPTION_ELEMENT_UNION = win32more.NetworkManagement.Dhcp.DHCP_OPTION_ELEMENT_UNION_head
    return DHCP_OPTION_ELEMENT_UNION
def _define_DHCP_OPTION_DATA_head():
    class DHCP_OPTION_DATA(Structure):
        pass
    return DHCP_OPTION_DATA
def _define_DHCP_OPTION_DATA():
    DHCP_OPTION_DATA = win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head
    DHCP_OPTION_DATA._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_ELEMENT_head)),
    ]
    return DHCP_OPTION_DATA
DHCP_OPTION_TYPE = Int32
DHCP_OPTION_TYPE_DhcpUnaryElementTypeOption = 0
DHCP_OPTION_TYPE_DhcpArrayTypeOption = 1
def _define_DHCP_OPTION_head():
    class DHCP_OPTION(Structure):
        pass
    return DHCP_OPTION
def _define_DHCP_OPTION():
    DHCP_OPTION = win32more.NetworkManagement.Dhcp.DHCP_OPTION_head
    DHCP_OPTION._fields_ = [
        ("OptionID", UInt32),
        ("OptionName", win32more.Foundation.PWSTR),
        ("OptionComment", win32more.Foundation.PWSTR),
        ("DefaultValue", win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA),
        ("OptionType", win32more.NetworkManagement.Dhcp.DHCP_OPTION_TYPE),
    ]
    return DHCP_OPTION
def _define_DHCP_OPTION_ARRAY_head():
    class DHCP_OPTION_ARRAY(Structure):
        pass
    return DHCP_OPTION_ARRAY
def _define_DHCP_OPTION_ARRAY():
    DHCP_OPTION_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head
    DHCP_OPTION_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Options", POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)),
    ]
    return DHCP_OPTION_ARRAY
def _define_DHCP_OPTION_VALUE_head():
    class DHCP_OPTION_VALUE(Structure):
        pass
    return DHCP_OPTION_VALUE
def _define_DHCP_OPTION_VALUE():
    DHCP_OPTION_VALUE = win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head
    DHCP_OPTION_VALUE._fields_ = [
        ("OptionID", UInt32),
        ("Value", win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA),
    ]
    return DHCP_OPTION_VALUE
def _define_DHCP_OPTION_VALUE_ARRAY_head():
    class DHCP_OPTION_VALUE_ARRAY(Structure):
        pass
    return DHCP_OPTION_VALUE_ARRAY
def _define_DHCP_OPTION_VALUE_ARRAY():
    DHCP_OPTION_VALUE_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head
    DHCP_OPTION_VALUE_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Values", POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)),
    ]
    return DHCP_OPTION_VALUE_ARRAY
DHCP_OPTION_SCOPE_TYPE = Int32
DHCP_OPTION_SCOPE_TYPE_DhcpDefaultOptions = 0
DHCP_OPTION_SCOPE_TYPE_DhcpGlobalOptions = 1
DHCP_OPTION_SCOPE_TYPE_DhcpSubnetOptions = 2
DHCP_OPTION_SCOPE_TYPE_DhcpReservedOptions = 3
DHCP_OPTION_SCOPE_TYPE_DhcpMScopeOptions = 4
def _define_DHCP_RESERVED_SCOPE_head():
    class DHCP_RESERVED_SCOPE(Structure):
        pass
    return DHCP_RESERVED_SCOPE
def _define_DHCP_RESERVED_SCOPE():
    DHCP_RESERVED_SCOPE = win32more.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE_head
    DHCP_RESERVED_SCOPE._fields_ = [
        ("ReservedIpAddress", UInt32),
        ("ReservedIpSubnetAddress", UInt32),
    ]
    return DHCP_RESERVED_SCOPE
def _define_DHCP_OPTION_SCOPE_INFO_head():
    class DHCP_OPTION_SCOPE_INFO(Structure):
        pass
    return DHCP_OPTION_SCOPE_INFO
def _define_DHCP_OPTION_SCOPE_INFO():
    DHCP_OPTION_SCOPE_INFO = win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head
    class DHCP_OPTION_SCOPE_INFO__DHCP_OPTION_SCOPE_UNION(Union):
        pass
    DHCP_OPTION_SCOPE_INFO__DHCP_OPTION_SCOPE_UNION._fields_ = [
        ("DefaultScopeInfo", c_void_p),
        ("GlobalScopeInfo", c_void_p),
        ("SubnetScopeInfo", UInt32),
        ("ReservedScopeInfo", win32more.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE),
        ("MScopeInfo", win32more.Foundation.PWSTR),
    ]
    DHCP_OPTION_SCOPE_INFO._fields_ = [
        ("ScopeType", win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_TYPE),
        ("ScopeInfo", DHCP_OPTION_SCOPE_INFO__DHCP_OPTION_SCOPE_UNION),
    ]
    return DHCP_OPTION_SCOPE_INFO
DHCP_OPTION_SCOPE_TYPE6 = Int32
DHCP_OPTION_SCOPE_TYPE6_DhcpDefaultOptions6 = 0
DHCP_OPTION_SCOPE_TYPE6_DhcpScopeOptions6 = 1
DHCP_OPTION_SCOPE_TYPE6_DhcpReservedOptions6 = 2
DHCP_OPTION_SCOPE_TYPE6_DhcpGlobalOptions6 = 3
def _define_DHCP_RESERVED_SCOPE6_head():
    class DHCP_RESERVED_SCOPE6(Structure):
        pass
    return DHCP_RESERVED_SCOPE6
def _define_DHCP_RESERVED_SCOPE6():
    DHCP_RESERVED_SCOPE6 = win32more.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE6_head
    DHCP_RESERVED_SCOPE6._fields_ = [
        ("ReservedIpAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("ReservedIpSubnetAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
    ]
    return DHCP_RESERVED_SCOPE6
def _define_DHCP_OPTION_SCOPE_INFO6_head():
    class DHCP_OPTION_SCOPE_INFO6(Structure):
        pass
    return DHCP_OPTION_SCOPE_INFO6
def _define_DHCP_OPTION_SCOPE_INFO6():
    DHCP_OPTION_SCOPE_INFO6 = win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head
    class DHCP_OPTION_SCOPE_INFO6_DHCP_OPTION_SCOPE_UNION6(Union):
        pass
    DHCP_OPTION_SCOPE_INFO6_DHCP_OPTION_SCOPE_UNION6._fields_ = [
        ("DefaultScopeInfo", c_void_p),
        ("SubnetScopeInfo", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("ReservedScopeInfo", win32more.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE6),
    ]
    DHCP_OPTION_SCOPE_INFO6._fields_ = [
        ("ScopeType", win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_TYPE6),
        ("ScopeInfo", DHCP_OPTION_SCOPE_INFO6_DHCP_OPTION_SCOPE_UNION6),
    ]
    return DHCP_OPTION_SCOPE_INFO6
def _define_DHCP_OPTION_SCOPE_UNION6_head():
    class DHCP_OPTION_SCOPE_UNION6(Union):
        pass
    return DHCP_OPTION_SCOPE_UNION6
def _define_DHCP_OPTION_SCOPE_UNION6():
    DHCP_OPTION_SCOPE_UNION6 = win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_UNION6_head
    return DHCP_OPTION_SCOPE_UNION6
def _define_DHCP_OPTION_LIST_head():
    class DHCP_OPTION_LIST(Structure):
        pass
    return DHCP_OPTION_LIST
def _define_DHCP_OPTION_LIST():
    DHCP_OPTION_LIST = win32more.NetworkManagement.Dhcp.DHCP_OPTION_LIST_head
    DHCP_OPTION_LIST._fields_ = [
        ("NumOptions", UInt32),
        ("Options", POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)),
    ]
    return DHCP_OPTION_LIST
def _define_DHCP_CLIENT_INFO_head():
    class DHCP_CLIENT_INFO(Structure):
        pass
    return DHCP_CLIENT_INFO
def _define_DHCP_CLIENT_INFO():
    DHCP_CLIENT_INFO = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head
    DHCP_CLIENT_INFO._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
    ]
    return DHCP_CLIENT_INFO
def _define_DHCP_CLIENT_INFO_ARRAY_head():
    class DHCP_CLIENT_INFO_ARRAY(Structure):
        pass
    return DHCP_CLIENT_INFO_ARRAY
def _define_DHCP_CLIENT_INFO_ARRAY():
    DHCP_CLIENT_INFO_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_head
    DHCP_CLIENT_INFO_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head))),
    ]
    return DHCP_CLIENT_INFO_ARRAY
QuarantineStatus = Int32
NOQUARANTINE = 0
RESTRICTEDACCESS = 1
DROPPACKET = 2
PROBATION = 3
EXEMPT = 4
DEFAULTQUARSETTING = 5
NOQUARINFO = 6
def _define_DHCP_CLIENT_INFO_VQ_head():
    class DHCP_CLIENT_INFO_VQ(Structure):
        pass
    return DHCP_CLIENT_INFO_VQ
def _define_DHCP_CLIENT_INFO_VQ():
    DHCP_CLIENT_INFO_VQ = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head
    DHCP_CLIENT_INFO_VQ._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
        ("AddressState", Byte),
        ("Status", win32more.NetworkManagement.Dhcp.QuarantineStatus),
        ("ProbationEnds", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QuarantineCapable", win32more.Foundation.BOOL),
    ]
    return DHCP_CLIENT_INFO_VQ
def _define_DHCP_CLIENT_INFO_ARRAY_VQ_head():
    class DHCP_CLIENT_INFO_ARRAY_VQ(Structure):
        pass
    return DHCP_CLIENT_INFO_ARRAY_VQ
def _define_DHCP_CLIENT_INFO_ARRAY_VQ():
    DHCP_CLIENT_INFO_ARRAY_VQ = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_VQ_head
    DHCP_CLIENT_INFO_ARRAY_VQ._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head))),
    ]
    return DHCP_CLIENT_INFO_ARRAY_VQ
def _define_DHCP_CLIENT_FILTER_STATUS_INFO_head():
    class DHCP_CLIENT_FILTER_STATUS_INFO(Structure):
        pass
    return DHCP_CLIENT_FILTER_STATUS_INFO
def _define_DHCP_CLIENT_FILTER_STATUS_INFO():
    DHCP_CLIENT_FILTER_STATUS_INFO = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_head
    DHCP_CLIENT_FILTER_STATUS_INFO._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
        ("AddressState", Byte),
        ("Status", win32more.NetworkManagement.Dhcp.QuarantineStatus),
        ("ProbationEnds", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QuarantineCapable", win32more.Foundation.BOOL),
        ("FilterStatus", UInt32),
    ]
    return DHCP_CLIENT_FILTER_STATUS_INFO
def _define_DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY_head():
    class DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(Structure):
        pass
    return DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY
def _define_DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY():
    DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY_head
    DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_head))),
    ]
    return DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY
def _define_DHCP_CLIENT_INFO_PB_head():
    class DHCP_CLIENT_INFO_PB(Structure):
        pass
    return DHCP_CLIENT_INFO_PB
def _define_DHCP_CLIENT_INFO_PB():
    DHCP_CLIENT_INFO_PB = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head
    DHCP_CLIENT_INFO_PB._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
        ("AddressState", Byte),
        ("Status", win32more.NetworkManagement.Dhcp.QuarantineStatus),
        ("ProbationEnds", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QuarantineCapable", win32more.Foundation.BOOL),
        ("FilterStatus", UInt32),
        ("PolicyName", win32more.Foundation.PWSTR),
    ]
    return DHCP_CLIENT_INFO_PB
def _define_DHCP_CLIENT_INFO_PB_ARRAY_head():
    class DHCP_CLIENT_INFO_PB_ARRAY(Structure):
        pass
    return DHCP_CLIENT_INFO_PB_ARRAY
def _define_DHCP_CLIENT_INFO_PB_ARRAY():
    DHCP_CLIENT_INFO_PB_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_ARRAY_head
    DHCP_CLIENT_INFO_PB_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head))),
    ]
    return DHCP_CLIENT_INFO_PB_ARRAY
DHCP_SEARCH_INFO_TYPE = Int32
DHCP_SEARCH_INFO_TYPE_DhcpClientIpAddress = 0
DHCP_SEARCH_INFO_TYPE_DhcpClientHardwareAddress = 1
DHCP_SEARCH_INFO_TYPE_DhcpClientName = 2
def _define_DHCP_SEARCH_INFO_head():
    class DHCP_SEARCH_INFO(Structure):
        pass
    return DHCP_SEARCH_INFO
def _define_DHCP_SEARCH_INFO():
    DHCP_SEARCH_INFO = win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head
    class DHCP_SEARCH_INFO_DHCP_CLIENT_SEARCH_UNION(Union):
        pass
    DHCP_SEARCH_INFO_DHCP_CLIENT_SEARCH_UNION._fields_ = [
        ("ClientIpAddress", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
    ]
    DHCP_SEARCH_INFO._fields_ = [
        ("SearchType", win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_TYPE),
        ("SearchInfo", DHCP_SEARCH_INFO_DHCP_CLIENT_SEARCH_UNION),
    ]
    return DHCP_SEARCH_INFO
def _define_DHCP_CLIENT_SEARCH_UNION_head():
    class DHCP_CLIENT_SEARCH_UNION(Union):
        pass
    return DHCP_CLIENT_SEARCH_UNION
def _define_DHCP_CLIENT_SEARCH_UNION():
    DHCP_CLIENT_SEARCH_UNION = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_SEARCH_UNION_head
    return DHCP_CLIENT_SEARCH_UNION
DHCP_PROPERTY_TYPE = Int32
DHCP_PROPERTY_TYPE_DhcpPropTypeByte = 0
DHCP_PROPERTY_TYPE_DhcpPropTypeWord = 1
DHCP_PROPERTY_TYPE_DhcpPropTypeDword = 2
DHCP_PROPERTY_TYPE_DhcpPropTypeString = 3
DHCP_PROPERTY_TYPE_DhcpPropTypeBinary = 4
DHCP_PROPERTY_ID = Int32
DHCP_PROPERTY_ID_DhcpPropIdPolicyDnsSuffix = 0
DHCP_PROPERTY_ID_DhcpPropIdClientAddressStateEx = 1
def _define_DHCP_PROPERTY_head():
    class DHCP_PROPERTY(Structure):
        pass
    return DHCP_PROPERTY
def _define_DHCP_PROPERTY():
    DHCP_PROPERTY = win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_head
    class DHCP_PROPERTY__DHCP_PROPERTY_VALUE_UNION(Union):
        pass
    DHCP_PROPERTY__DHCP_PROPERTY_VALUE_UNION._fields_ = [
        ("ByteValue", Byte),
        ("WordValue", UInt16),
        ("DWordValue", UInt32),
        ("StringValue", win32more.Foundation.PWSTR),
        ("BinaryValue", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
    ]
    DHCP_PROPERTY._fields_ = [
        ("ID", win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ID),
        ("Type", win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_TYPE),
        ("Value", DHCP_PROPERTY__DHCP_PROPERTY_VALUE_UNION),
    ]
    return DHCP_PROPERTY
def _define_DHCP_PROPERTY_ARRAY_head():
    class DHCP_PROPERTY_ARRAY(Structure):
        pass
    return DHCP_PROPERTY_ARRAY
def _define_DHCP_PROPERTY_ARRAY():
    DHCP_PROPERTY_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head
    DHCP_PROPERTY_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_head)),
    ]
    return DHCP_PROPERTY_ARRAY
def _define_DHCP_CLIENT_INFO_EX_head():
    class DHCP_CLIENT_INFO_EX(Structure):
        pass
    return DHCP_CLIENT_INFO_EX
def _define_DHCP_CLIENT_INFO_EX():
    DHCP_CLIENT_INFO_EX = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head
    DHCP_CLIENT_INFO_EX._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
        ("AddressState", Byte),
        ("Status", win32more.NetworkManagement.Dhcp.QuarantineStatus),
        ("ProbationEnds", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QuarantineCapable", win32more.Foundation.BOOL),
        ("FilterStatus", UInt32),
        ("PolicyName", win32more.Foundation.PWSTR),
        ("Properties", POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)),
    ]
    return DHCP_CLIENT_INFO_EX
def _define_DHCP_CLIENT_INFO_EX_ARRAY_head():
    class DHCP_CLIENT_INFO_EX_ARRAY(Structure):
        pass
    return DHCP_CLIENT_INFO_EX_ARRAY
def _define_DHCP_CLIENT_INFO_EX_ARRAY():
    DHCP_CLIENT_INFO_EX_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_ARRAY_head
    DHCP_CLIENT_INFO_EX_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head))),
    ]
    return DHCP_CLIENT_INFO_EX_ARRAY
def _define_SCOPE_MIB_INFO_head():
    class SCOPE_MIB_INFO(Structure):
        pass
    return SCOPE_MIB_INFO
def _define_SCOPE_MIB_INFO():
    SCOPE_MIB_INFO = win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_head
    SCOPE_MIB_INFO._fields_ = [
        ("Subnet", UInt32),
        ("NumAddressesInuse", UInt32),
        ("NumAddressesFree", UInt32),
        ("NumPendingOffers", UInt32),
    ]
    return SCOPE_MIB_INFO
def _define_DHCP_MIB_INFO_head():
    class DHCP_MIB_INFO(Structure):
        pass
    return DHCP_MIB_INFO
def _define_DHCP_MIB_INFO():
    DHCP_MIB_INFO = win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_head
    DHCP_MIB_INFO._fields_ = [
        ("Discovers", UInt32),
        ("Offers", UInt32),
        ("Requests", UInt32),
        ("Acks", UInt32),
        ("Naks", UInt32),
        ("Declines", UInt32),
        ("Releases", UInt32),
        ("ServerStartTime", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("Scopes", UInt32),
        ("ScopeInfo", POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_head)),
    ]
    return DHCP_MIB_INFO
def _define_SCOPE_MIB_INFO_VQ_head():
    class SCOPE_MIB_INFO_VQ(Structure):
        pass
    return SCOPE_MIB_INFO_VQ
def _define_SCOPE_MIB_INFO_VQ():
    SCOPE_MIB_INFO_VQ = win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_VQ_head
    SCOPE_MIB_INFO_VQ._fields_ = [
        ("Subnet", UInt32),
        ("NumAddressesInuse", UInt32),
        ("NumAddressesFree", UInt32),
        ("NumPendingOffers", UInt32),
        ("QtnNumLeases", UInt32),
        ("QtnPctQtnLeases", UInt32),
        ("QtnProbationLeases", UInt32),
        ("QtnNonQtnLeases", UInt32),
        ("QtnExemptLeases", UInt32),
        ("QtnCapableClients", UInt32),
    ]
    return SCOPE_MIB_INFO_VQ
def _define_DHCP_MIB_INFO_VQ_head():
    class DHCP_MIB_INFO_VQ(Structure):
        pass
    return DHCP_MIB_INFO_VQ
def _define_DHCP_MIB_INFO_VQ():
    DHCP_MIB_INFO_VQ = win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_VQ_head
    DHCP_MIB_INFO_VQ._fields_ = [
        ("Discovers", UInt32),
        ("Offers", UInt32),
        ("Requests", UInt32),
        ("Acks", UInt32),
        ("Naks", UInt32),
        ("Declines", UInt32),
        ("Releases", UInt32),
        ("ServerStartTime", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QtnNumLeases", UInt32),
        ("QtnPctQtnLeases", UInt32),
        ("QtnProbationLeases", UInt32),
        ("QtnNonQtnLeases", UInt32),
        ("QtnExemptLeases", UInt32),
        ("QtnCapableClients", UInt32),
        ("QtnIASErrors", UInt32),
        ("Scopes", UInt32),
        ("ScopeInfo", POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_VQ_head)),
    ]
    return DHCP_MIB_INFO_VQ
def _define_SCOPE_MIB_INFO_V5_head():
    class SCOPE_MIB_INFO_V5(Structure):
        pass
    return SCOPE_MIB_INFO_V5
def _define_SCOPE_MIB_INFO_V5():
    SCOPE_MIB_INFO_V5 = win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V5_head
    SCOPE_MIB_INFO_V5._fields_ = [
        ("Subnet", UInt32),
        ("NumAddressesInuse", UInt32),
        ("NumAddressesFree", UInt32),
        ("NumPendingOffers", UInt32),
    ]
    return SCOPE_MIB_INFO_V5
def _define_DHCP_MIB_INFO_V5_head():
    class DHCP_MIB_INFO_V5(Structure):
        pass
    return DHCP_MIB_INFO_V5
def _define_DHCP_MIB_INFO_V5():
    DHCP_MIB_INFO_V5 = win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_V5_head
    DHCP_MIB_INFO_V5._fields_ = [
        ("Discovers", UInt32),
        ("Offers", UInt32),
        ("Requests", UInt32),
        ("Acks", UInt32),
        ("Naks", UInt32),
        ("Declines", UInt32),
        ("Releases", UInt32),
        ("ServerStartTime", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QtnNumLeases", UInt32),
        ("QtnPctQtnLeases", UInt32),
        ("QtnProbationLeases", UInt32),
        ("QtnNonQtnLeases", UInt32),
        ("QtnExemptLeases", UInt32),
        ("QtnCapableClients", UInt32),
        ("QtnIASErrors", UInt32),
        ("DelayedOffers", UInt32),
        ("ScopesWithDelayedOffers", UInt32),
        ("Scopes", UInt32),
        ("ScopeInfo", POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V5_head)),
    ]
    return DHCP_MIB_INFO_V5
def _define_DHCP_SERVER_CONFIG_INFO_head():
    class DHCP_SERVER_CONFIG_INFO(Structure):
        pass
    return DHCP_SERVER_CONFIG_INFO
def _define_DHCP_SERVER_CONFIG_INFO():
    DHCP_SERVER_CONFIG_INFO = win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_head
    DHCP_SERVER_CONFIG_INFO._fields_ = [
        ("APIProtocolSupport", UInt32),
        ("DatabaseName", win32more.Foundation.PWSTR),
        ("DatabasePath", win32more.Foundation.PWSTR),
        ("BackupPath", win32more.Foundation.PWSTR),
        ("BackupInterval", UInt32),
        ("DatabaseLoggingFlag", UInt32),
        ("RestoreFlag", UInt32),
        ("DatabaseCleanupInterval", UInt32),
        ("DebugFlag", UInt32),
    ]
    return DHCP_SERVER_CONFIG_INFO
DHCP_SCAN_FLAG = Int32
DHCP_SCAN_FLAG_DhcpRegistryFix = 0
DHCP_SCAN_FLAG_DhcpDatabaseFix = 1
def _define_DHCP_SCAN_ITEM_head():
    class DHCP_SCAN_ITEM(Structure):
        pass
    return DHCP_SCAN_ITEM
def _define_DHCP_SCAN_ITEM():
    DHCP_SCAN_ITEM = win32more.NetworkManagement.Dhcp.DHCP_SCAN_ITEM_head
    DHCP_SCAN_ITEM._fields_ = [
        ("IpAddress", UInt32),
        ("ScanFlag", win32more.NetworkManagement.Dhcp.DHCP_SCAN_FLAG),
    ]
    return DHCP_SCAN_ITEM
def _define_DHCP_SCAN_LIST_head():
    class DHCP_SCAN_LIST(Structure):
        pass
    return DHCP_SCAN_LIST
def _define_DHCP_SCAN_LIST():
    DHCP_SCAN_LIST = win32more.NetworkManagement.Dhcp.DHCP_SCAN_LIST_head
    DHCP_SCAN_LIST._fields_ = [
        ("NumScanItems", UInt32),
        ("ScanItems", POINTER(win32more.NetworkManagement.Dhcp.DHCP_SCAN_ITEM_head)),
    ]
    return DHCP_SCAN_LIST
def _define_DHCP_CLASS_INFO_head():
    class DHCP_CLASS_INFO(Structure):
        pass
    return DHCP_CLASS_INFO
def _define_DHCP_CLASS_INFO():
    DHCP_CLASS_INFO = win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head
    DHCP_CLASS_INFO._fields_ = [
        ("ClassName", win32more.Foundation.PWSTR),
        ("ClassComment", win32more.Foundation.PWSTR),
        ("ClassDataLength", UInt32),
        ("IsVendor", win32more.Foundation.BOOL),
        ("Flags", UInt32),
        ("ClassData", c_char_p_no),
    ]
    return DHCP_CLASS_INFO
def _define_DHCP_CLASS_INFO_ARRAY_head():
    class DHCP_CLASS_INFO_ARRAY(Structure):
        pass
    return DHCP_CLASS_INFO_ARRAY
def _define_DHCP_CLASS_INFO_ARRAY():
    DHCP_CLASS_INFO_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_head
    DHCP_CLASS_INFO_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Classes", POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)),
    ]
    return DHCP_CLASS_INFO_ARRAY
def _define_DHCP_CLASS_INFO_V6_head():
    class DHCP_CLASS_INFO_V6(Structure):
        pass
    return DHCP_CLASS_INFO_V6
def _define_DHCP_CLASS_INFO_V6():
    DHCP_CLASS_INFO_V6 = win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head
    DHCP_CLASS_INFO_V6._fields_ = [
        ("ClassName", win32more.Foundation.PWSTR),
        ("ClassComment", win32more.Foundation.PWSTR),
        ("ClassDataLength", UInt32),
        ("IsVendor", win32more.Foundation.BOOL),
        ("EnterpriseNumber", UInt32),
        ("Flags", UInt32),
        ("ClassData", c_char_p_no),
    ]
    return DHCP_CLASS_INFO_V6
def _define_DHCP_CLASS_INFO_ARRAY_V6_head():
    class DHCP_CLASS_INFO_ARRAY_V6(Structure):
        pass
    return DHCP_CLASS_INFO_ARRAY_V6
def _define_DHCP_CLASS_INFO_ARRAY_V6():
    DHCP_CLASS_INFO_ARRAY_V6 = win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_V6_head
    DHCP_CLASS_INFO_ARRAY_V6._fields_ = [
        ("NumElements", UInt32),
        ("Classes", POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head)),
    ]
    return DHCP_CLASS_INFO_ARRAY_V6
def _define_DHCP_SERVER_SPECIFIC_STRINGS_head():
    class DHCP_SERVER_SPECIFIC_STRINGS(Structure):
        pass
    return DHCP_SERVER_SPECIFIC_STRINGS
def _define_DHCP_SERVER_SPECIFIC_STRINGS():
    DHCP_SERVER_SPECIFIC_STRINGS = win32more.NetworkManagement.Dhcp.DHCP_SERVER_SPECIFIC_STRINGS_head
    DHCP_SERVER_SPECIFIC_STRINGS._fields_ = [
        ("DefaultVendorClassName", win32more.Foundation.PWSTR),
        ("DefaultUserClassName", win32more.Foundation.PWSTR),
    ]
    return DHCP_SERVER_SPECIFIC_STRINGS
def _define_DHCP_IP_RESERVATION_V4_head():
    class DHCP_IP_RESERVATION_V4(Structure):
        pass
    return DHCP_IP_RESERVATION_V4
def _define_DHCP_IP_RESERVATION_V4():
    DHCP_IP_RESERVATION_V4 = win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V4_head
    DHCP_IP_RESERVATION_V4._fields_ = [
        ("ReservedIpAddress", UInt32),
        ("ReservedForClient", POINTER(win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)),
        ("bAllowedClientTypes", Byte),
    ]
    return DHCP_IP_RESERVATION_V4
def _define_DHCP_IP_RESERVATION_INFO_head():
    class DHCP_IP_RESERVATION_INFO(Structure):
        pass
    return DHCP_IP_RESERVATION_INFO
def _define_DHCP_IP_RESERVATION_INFO():
    DHCP_IP_RESERVATION_INFO = win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_INFO_head
    DHCP_IP_RESERVATION_INFO._fields_ = [
        ("ReservedIpAddress", UInt32),
        ("ReservedForClient", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ReservedClientName", win32more.Foundation.PWSTR),
        ("ReservedClientDesc", win32more.Foundation.PWSTR),
        ("bAllowedClientTypes", Byte),
        ("fOptionsPresent", Byte),
    ]
    return DHCP_IP_RESERVATION_INFO
def _define_DHCP_RESERVATION_INFO_ARRAY_head():
    class DHCP_RESERVATION_INFO_ARRAY(Structure):
        pass
    return DHCP_RESERVATION_INFO_ARRAY
def _define_DHCP_RESERVATION_INFO_ARRAY():
    DHCP_RESERVATION_INFO_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_RESERVATION_INFO_ARRAY_head
    DHCP_RESERVATION_INFO_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_INFO_head))),
    ]
    return DHCP_RESERVATION_INFO_ARRAY
def _define_DHCP_SUBNET_ELEMENT_DATA_V4_head():
    class DHCP_SUBNET_ELEMENT_DATA_V4(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_DATA_V4
def _define_DHCP_SUBNET_ELEMENT_DATA_V4():
    DHCP_SUBNET_ELEMENT_DATA_V4 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head
    class DHCP_SUBNET_ELEMENT_DATA_V4_DHCP_SUBNET_ELEMENT_UNION_V4(Union):
        pass
    DHCP_SUBNET_ELEMENT_DATA_V4_DHCP_SUBNET_ELEMENT_UNION_V4._fields_ = [
        ("IpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)),
        ("SecondaryHost", POINTER(win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)),
        ("ReservedIp", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V4_head)),
        ("ExcludeIpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)),
        ("IpUsedCluster", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)),
    ]
    DHCP_SUBNET_ELEMENT_DATA_V4._fields_ = [
        ("ElementType", win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE),
        ("Element", DHCP_SUBNET_ELEMENT_DATA_V4_DHCP_SUBNET_ELEMENT_UNION_V4),
    ]
    return DHCP_SUBNET_ELEMENT_DATA_V4
def _define_DHCP_SUBNET_ELEMENT_UNION_V4_head():
    class DHCP_SUBNET_ELEMENT_UNION_V4(Union):
        pass
    return DHCP_SUBNET_ELEMENT_UNION_V4
def _define_DHCP_SUBNET_ELEMENT_UNION_V4():
    DHCP_SUBNET_ELEMENT_UNION_V4 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_UNION_V4_head
    return DHCP_SUBNET_ELEMENT_UNION_V4
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4_head():
    class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4():
    DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4_head
    DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head)),
    ]
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4
def _define_DHCP_CLIENT_INFO_V4_head():
    class DHCP_CLIENT_INFO_V4(Structure):
        pass
    return DHCP_CLIENT_INFO_V4
def _define_DHCP_CLIENT_INFO_V4():
    DHCP_CLIENT_INFO_V4 = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head
    DHCP_CLIENT_INFO_V4._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
    ]
    return DHCP_CLIENT_INFO_V4
def _define_DHCP_CLIENT_INFO_ARRAY_V4_head():
    class DHCP_CLIENT_INFO_ARRAY_V4(Structure):
        pass
    return DHCP_CLIENT_INFO_ARRAY_V4
def _define_DHCP_CLIENT_INFO_ARRAY_V4():
    DHCP_CLIENT_INFO_ARRAY_V4 = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V4_head
    DHCP_CLIENT_INFO_ARRAY_V4._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head))),
    ]
    return DHCP_CLIENT_INFO_ARRAY_V4
def _define_DHCP_SERVER_CONFIG_INFO_V4_head():
    class DHCP_SERVER_CONFIG_INFO_V4(Structure):
        pass
    return DHCP_SERVER_CONFIG_INFO_V4
def _define_DHCP_SERVER_CONFIG_INFO_V4():
    DHCP_SERVER_CONFIG_INFO_V4 = win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V4_head
    DHCP_SERVER_CONFIG_INFO_V4._fields_ = [
        ("APIProtocolSupport", UInt32),
        ("DatabaseName", win32more.Foundation.PWSTR),
        ("DatabasePath", win32more.Foundation.PWSTR),
        ("BackupPath", win32more.Foundation.PWSTR),
        ("BackupInterval", UInt32),
        ("DatabaseLoggingFlag", UInt32),
        ("RestoreFlag", UInt32),
        ("DatabaseCleanupInterval", UInt32),
        ("DebugFlag", UInt32),
        ("dwPingRetries", UInt32),
        ("cbBootTableString", UInt32),
        ("wszBootTableString", win32more.Foundation.PWSTR),
        ("fAuditLog", win32more.Foundation.BOOL),
    ]
    return DHCP_SERVER_CONFIG_INFO_V4
def _define_DHCP_SERVER_CONFIG_INFO_VQ_head():
    class DHCP_SERVER_CONFIG_INFO_VQ(Structure):
        pass
    return DHCP_SERVER_CONFIG_INFO_VQ
def _define_DHCP_SERVER_CONFIG_INFO_VQ():
    DHCP_SERVER_CONFIG_INFO_VQ = win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head
    DHCP_SERVER_CONFIG_INFO_VQ._fields_ = [
        ("APIProtocolSupport", UInt32),
        ("DatabaseName", win32more.Foundation.PWSTR),
        ("DatabasePath", win32more.Foundation.PWSTR),
        ("BackupPath", win32more.Foundation.PWSTR),
        ("BackupInterval", UInt32),
        ("DatabaseLoggingFlag", UInt32),
        ("RestoreFlag", UInt32),
        ("DatabaseCleanupInterval", UInt32),
        ("DebugFlag", UInt32),
        ("dwPingRetries", UInt32),
        ("cbBootTableString", UInt32),
        ("wszBootTableString", win32more.Foundation.PWSTR),
        ("fAuditLog", win32more.Foundation.BOOL),
        ("QuarantineOn", win32more.Foundation.BOOL),
        ("QuarDefFail", UInt32),
        ("QuarRuntimeStatus", win32more.Foundation.BOOL),
    ]
    return DHCP_SERVER_CONFIG_INFO_VQ
def _define_DHCP_SERVER_CONFIG_INFO_V6_head():
    class DHCP_SERVER_CONFIG_INFO_V6(Structure):
        pass
    return DHCP_SERVER_CONFIG_INFO_V6
def _define_DHCP_SERVER_CONFIG_INFO_V6():
    DHCP_SERVER_CONFIG_INFO_V6 = win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V6_head
    DHCP_SERVER_CONFIG_INFO_V6._fields_ = [
        ("UnicastFlag", win32more.Foundation.BOOL),
        ("RapidCommitFlag", win32more.Foundation.BOOL),
        ("PreferredLifetime", UInt32),
        ("ValidLifetime", UInt32),
        ("T1", UInt32),
        ("T2", UInt32),
        ("PreferredLifetimeIATA", UInt32),
        ("ValidLifetimeIATA", UInt32),
        ("fAuditLog", win32more.Foundation.BOOL),
    ]
    return DHCP_SERVER_CONFIG_INFO_V6
def _define_DHCP_SUPER_SCOPE_TABLE_ENTRY_head():
    class DHCP_SUPER_SCOPE_TABLE_ENTRY(Structure):
        pass
    return DHCP_SUPER_SCOPE_TABLE_ENTRY
def _define_DHCP_SUPER_SCOPE_TABLE_ENTRY():
    DHCP_SUPER_SCOPE_TABLE_ENTRY = win32more.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_ENTRY_head
    DHCP_SUPER_SCOPE_TABLE_ENTRY._fields_ = [
        ("SubnetAddress", UInt32),
        ("SuperScopeNumber", UInt32),
        ("NextInSuperScope", UInt32),
        ("SuperScopeName", win32more.Foundation.PWSTR),
    ]
    return DHCP_SUPER_SCOPE_TABLE_ENTRY
def _define_DHCP_SUPER_SCOPE_TABLE_head():
    class DHCP_SUPER_SCOPE_TABLE(Structure):
        pass
    return DHCP_SUPER_SCOPE_TABLE
def _define_DHCP_SUPER_SCOPE_TABLE():
    DHCP_SUPER_SCOPE_TABLE = win32more.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_head
    DHCP_SUPER_SCOPE_TABLE._fields_ = [
        ("cEntries", UInt32),
        ("pEntries", POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_ENTRY_head)),
    ]
    return DHCP_SUPER_SCOPE_TABLE
def _define_DHCP_CLIENT_INFO_V5_head():
    class DHCP_CLIENT_INFO_V5(Structure):
        pass
    return DHCP_CLIENT_INFO_V5
def _define_DHCP_CLIENT_INFO_V5():
    DHCP_CLIENT_INFO_V5 = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V5_head
    DHCP_CLIENT_INFO_V5._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
        ("AddressState", Byte),
    ]
    return DHCP_CLIENT_INFO_V5
def _define_DHCP_CLIENT_INFO_ARRAY_V5_head():
    class DHCP_CLIENT_INFO_ARRAY_V5(Structure):
        pass
    return DHCP_CLIENT_INFO_ARRAY_V5
def _define_DHCP_CLIENT_INFO_ARRAY_V5():
    DHCP_CLIENT_INFO_ARRAY_V5 = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V5_head
    DHCP_CLIENT_INFO_ARRAY_V5._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V5_head))),
    ]
    return DHCP_CLIENT_INFO_ARRAY_V5
def _define_DHCP_ALL_OPTIONS_head():
    class DHCP_ALL_OPTIONS(Structure):
        pass
    return DHCP_ALL_OPTIONS
def _define_DHCP_ALL_OPTIONS():
    DHCP_ALL_OPTIONS = win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTIONS_head
    class DHCP_ALL_OPTIONS__Anonymous_e__Struct(Structure):
        pass
    DHCP_ALL_OPTIONS__Anonymous_e__Struct._fields_ = [
        ("Option", win32more.NetworkManagement.Dhcp.DHCP_OPTION),
        ("VendorName", win32more.Foundation.PWSTR),
        ("ClassName", win32more.Foundation.PWSTR),
    ]
    DHCP_ALL_OPTIONS._fields_ = [
        ("Flags", UInt32),
        ("NonVendorOptions", POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)),
        ("NumVendorOptions", UInt32),
        ("VendorOptions", POINTER(DHCP_ALL_OPTIONS__Anonymous_e__Struct)),
    ]
    return DHCP_ALL_OPTIONS
def _define_DHCP_ALL_OPTION_VALUES_head():
    class DHCP_ALL_OPTION_VALUES(Structure):
        pass
    return DHCP_ALL_OPTION_VALUES
def _define_DHCP_ALL_OPTION_VALUES():
    DHCP_ALL_OPTION_VALUES = win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_head
    class DHCP_ALL_OPTION_VALUES__Anonymous_e__Struct(Structure):
        pass
    DHCP_ALL_OPTION_VALUES__Anonymous_e__Struct._fields_ = [
        ("ClassName", win32more.Foundation.PWSTR),
        ("VendorName", win32more.Foundation.PWSTR),
        ("IsVendor", win32more.Foundation.BOOL),
        ("OptionsArray", POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)),
    ]
    DHCP_ALL_OPTION_VALUES._fields_ = [
        ("Flags", UInt32),
        ("NumElements", UInt32),
        ("Options", POINTER(DHCP_ALL_OPTION_VALUES__Anonymous_e__Struct)),
    ]
    return DHCP_ALL_OPTION_VALUES
def _define_DHCP_ALL_OPTION_VALUES_PB_head():
    class DHCP_ALL_OPTION_VALUES_PB(Structure):
        pass
    return DHCP_ALL_OPTION_VALUES_PB
def _define_DHCP_ALL_OPTION_VALUES_PB():
    DHCP_ALL_OPTION_VALUES_PB = win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_PB_head
    class DHCP_ALL_OPTION_VALUES_PB__Anonymous_e__Struct(Structure):
        pass
    DHCP_ALL_OPTION_VALUES_PB__Anonymous_e__Struct._fields_ = [
        ("PolicyName", win32more.Foundation.PWSTR),
        ("VendorName", win32more.Foundation.PWSTR),
        ("IsVendor", win32more.Foundation.BOOL),
        ("OptionsArray", POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)),
    ]
    DHCP_ALL_OPTION_VALUES_PB._fields_ = [
        ("Flags", UInt32),
        ("NumElements", UInt32),
        ("Options", POINTER(DHCP_ALL_OPTION_VALUES_PB__Anonymous_e__Struct)),
    ]
    return DHCP_ALL_OPTION_VALUES_PB
def _define_DHCPDS_SERVER_head():
    class DHCPDS_SERVER(Structure):
        pass
    return DHCPDS_SERVER
def _define_DHCPDS_SERVER():
    DHCPDS_SERVER = win32more.NetworkManagement.Dhcp.DHCPDS_SERVER_head
    DHCPDS_SERVER._fields_ = [
        ("Version", UInt32),
        ("ServerName", win32more.Foundation.PWSTR),
        ("ServerAddress", UInt32),
        ("Flags", UInt32),
        ("State", UInt32),
        ("DsLocation", win32more.Foundation.PWSTR),
        ("DsLocType", UInt32),
    ]
    return DHCPDS_SERVER
def _define_DHCPDS_SERVERS_head():
    class DHCPDS_SERVERS(Structure):
        pass
    return DHCPDS_SERVERS
def _define_DHCPDS_SERVERS():
    DHCPDS_SERVERS = win32more.NetworkManagement.Dhcp.DHCPDS_SERVERS_head
    DHCPDS_SERVERS._fields_ = [
        ("Flags", UInt32),
        ("NumElements", UInt32),
        ("Servers", POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVER_head)),
    ]
    return DHCPDS_SERVERS
def _define_DHCP_ATTRIB_head():
    class DHCP_ATTRIB(Structure):
        pass
    return DHCP_ATTRIB
def _define_DHCP_ATTRIB():
    DHCP_ATTRIB = win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_head
    class DHCP_ATTRIB__Anonymous_e__Union(Union):
        pass
    DHCP_ATTRIB__Anonymous_e__Union._fields_ = [
        ("DhcpAttribBool", win32more.Foundation.BOOL),
        ("DhcpAttribUlong", UInt32),
    ]
    DHCP_ATTRIB._anonymous_ = [
        'Anonymous',
    ]
    DHCP_ATTRIB._fields_ = [
        ("DhcpAttribId", UInt32),
        ("DhcpAttribType", UInt32),
        ("Anonymous", DHCP_ATTRIB__Anonymous_e__Union),
    ]
    return DHCP_ATTRIB
def _define_DHCP_ATTRIB_ARRAY_head():
    class DHCP_ATTRIB_ARRAY(Structure):
        pass
    return DHCP_ATTRIB_ARRAY
def _define_DHCP_ATTRIB_ARRAY():
    DHCP_ATTRIB_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_ARRAY_head
    DHCP_ATTRIB_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("DhcpAttribs", POINTER(win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_head)),
    ]
    return DHCP_ATTRIB_ARRAY
def _define_DHCP_BOOTP_IP_RANGE_head():
    class DHCP_BOOTP_IP_RANGE(Structure):
        pass
    return DHCP_BOOTP_IP_RANGE
def _define_DHCP_BOOTP_IP_RANGE():
    DHCP_BOOTP_IP_RANGE = win32more.NetworkManagement.Dhcp.DHCP_BOOTP_IP_RANGE_head
    DHCP_BOOTP_IP_RANGE._fields_ = [
        ("StartAddress", UInt32),
        ("EndAddress", UInt32),
        ("BootpAllocated", UInt32),
        ("MaxBootpAllowed", UInt32),
    ]
    return DHCP_BOOTP_IP_RANGE
def _define_DHCP_SUBNET_ELEMENT_DATA_V5_head():
    class DHCP_SUBNET_ELEMENT_DATA_V5(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_DATA_V5
def _define_DHCP_SUBNET_ELEMENT_DATA_V5():
    DHCP_SUBNET_ELEMENT_DATA_V5 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head
    class DHCP_SUBNET_ELEMENT_DATA_V5__DHCP_SUBNET_ELEMENT_UNION_V5(Union):
        pass
    DHCP_SUBNET_ELEMENT_DATA_V5__DHCP_SUBNET_ELEMENT_UNION_V5._fields_ = [
        ("IpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_BOOTP_IP_RANGE_head)),
        ("SecondaryHost", POINTER(win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)),
        ("ReservedIp", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V4_head)),
        ("ExcludeIpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)),
        ("IpUsedCluster", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)),
    ]
    DHCP_SUBNET_ELEMENT_DATA_V5._fields_ = [
        ("ElementType", win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE),
        ("Element", DHCP_SUBNET_ELEMENT_DATA_V5__DHCP_SUBNET_ELEMENT_UNION_V5),
    ]
    return DHCP_SUBNET_ELEMENT_DATA_V5
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5_head():
    class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5():
    DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5_head
    DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head)),
    ]
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5
def _define_DHCP_PERF_STATS_head():
    class DHCP_PERF_STATS(Structure):
        pass
    return DHCP_PERF_STATS
def _define_DHCP_PERF_STATS():
    DHCP_PERF_STATS = win32more.NetworkManagement.Dhcp.DHCP_PERF_STATS_head
    DHCP_PERF_STATS._fields_ = [
        ("dwNumPacketsReceived", UInt32),
        ("dwNumPacketsDuplicate", UInt32),
        ("dwNumPacketsExpired", UInt32),
        ("dwNumMilliSecondsProcessed", UInt32),
        ("dwNumPacketsInActiveQueue", UInt32),
        ("dwNumPacketsInPingQueue", UInt32),
        ("dwNumDiscoversReceived", UInt32),
        ("dwNumOffersSent", UInt32),
        ("dwNumRequestsReceived", UInt32),
        ("dwNumInformsReceived", UInt32),
        ("dwNumAcksSent", UInt32),
        ("dwNumNacksSent", UInt32),
        ("dwNumDeclinesReceived", UInt32),
        ("dwNumReleasesReceived", UInt32),
        ("dwNumDelayedOfferInQueue", UInt32),
        ("dwNumPacketsProcessed", UInt32),
        ("dwNumPacketsInQuarWaitingQueue", UInt32),
        ("dwNumPacketsInQuarReadyQueue", UInt32),
        ("dwNumPacketsInQuarDecisionQueue", UInt32),
    ]
    return DHCP_PERF_STATS
def _define_DHCP_BIND_ELEMENT_head():
    class DHCP_BIND_ELEMENT(Structure):
        pass
    return DHCP_BIND_ELEMENT
def _define_DHCP_BIND_ELEMENT():
    DHCP_BIND_ELEMENT = win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_head
    DHCP_BIND_ELEMENT._fields_ = [
        ("Flags", UInt32),
        ("fBoundToDHCPServer", win32more.Foundation.BOOL),
        ("AdapterPrimaryAddress", UInt32),
        ("AdapterSubnetAddress", UInt32),
        ("IfDescription", win32more.Foundation.PWSTR),
        ("IfIdSize", UInt32),
        ("IfId", c_char_p_no),
    ]
    return DHCP_BIND_ELEMENT
def _define_DHCP_BIND_ELEMENT_ARRAY_head():
    class DHCP_BIND_ELEMENT_ARRAY(Structure):
        pass
    return DHCP_BIND_ELEMENT_ARRAY
def _define_DHCP_BIND_ELEMENT_ARRAY():
    DHCP_BIND_ELEMENT_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_ARRAY_head
    DHCP_BIND_ELEMENT_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_head)),
    ]
    return DHCP_BIND_ELEMENT_ARRAY
def _define_DHCPV6_BIND_ELEMENT_head():
    class DHCPV6_BIND_ELEMENT(Structure):
        pass
    return DHCPV6_BIND_ELEMENT
def _define_DHCPV6_BIND_ELEMENT():
    DHCPV6_BIND_ELEMENT = win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_head
    DHCPV6_BIND_ELEMENT._fields_ = [
        ("Flags", UInt32),
        ("fBoundToDHCPServer", win32more.Foundation.BOOL),
        ("AdapterPrimaryAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("AdapterSubnetAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("IfDescription", win32more.Foundation.PWSTR),
        ("IpV6IfIndex", UInt32),
        ("IfIdSize", UInt32),
        ("IfId", c_char_p_no),
    ]
    return DHCPV6_BIND_ELEMENT
def _define_DHCPV6_BIND_ELEMENT_ARRAY_head():
    class DHCPV6_BIND_ELEMENT_ARRAY(Structure):
        pass
    return DHCPV6_BIND_ELEMENT_ARRAY
def _define_DHCPV6_BIND_ELEMENT_ARRAY():
    DHCPV6_BIND_ELEMENT_ARRAY = win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_ARRAY_head
    DHCPV6_BIND_ELEMENT_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_head)),
    ]
    return DHCPV6_BIND_ELEMENT_ARRAY
def _define_DHCP_IP_RANGE_V6_head():
    class DHCP_IP_RANGE_V6(Structure):
        pass
    return DHCP_IP_RANGE_V6
def _define_DHCP_IP_RANGE_V6():
    DHCP_IP_RANGE_V6 = win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_V6_head
    DHCP_IP_RANGE_V6._fields_ = [
        ("StartAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("EndAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
    ]
    return DHCP_IP_RANGE_V6
def _define_DHCP_HOST_INFO_V6_head():
    class DHCP_HOST_INFO_V6(Structure):
        pass
    return DHCP_HOST_INFO_V6
def _define_DHCP_HOST_INFO_V6():
    DHCP_HOST_INFO_V6 = win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_V6_head
    DHCP_HOST_INFO_V6._fields_ = [
        ("IpAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("NetBiosName", win32more.Foundation.PWSTR),
        ("HostName", win32more.Foundation.PWSTR),
    ]
    return DHCP_HOST_INFO_V6
def _define_DHCP_SUBNET_INFO_V6_head():
    class DHCP_SUBNET_INFO_V6(Structure):
        pass
    return DHCP_SUBNET_INFO_V6
def _define_DHCP_SUBNET_INFO_V6():
    DHCP_SUBNET_INFO_V6 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head
    DHCP_SUBNET_INFO_V6._fields_ = [
        ("SubnetAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("Prefix", UInt32),
        ("Preference", UInt16),
        ("SubnetName", win32more.Foundation.PWSTR),
        ("SubnetComment", win32more.Foundation.PWSTR),
        ("State", UInt32),
        ("ScopeId", UInt32),
    ]
    return DHCP_SUBNET_INFO_V6
def _define_SCOPE_MIB_INFO_V6_head():
    class SCOPE_MIB_INFO_V6(Structure):
        pass
    return SCOPE_MIB_INFO_V6
def _define_SCOPE_MIB_INFO_V6():
    SCOPE_MIB_INFO_V6 = win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V6_head
    SCOPE_MIB_INFO_V6._fields_ = [
        ("Subnet", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("NumAddressesInuse", UInt64),
        ("NumAddressesFree", UInt64),
        ("NumPendingAdvertises", UInt64),
    ]
    return SCOPE_MIB_INFO_V6
def _define_DHCP_MIB_INFO_V6_head():
    class DHCP_MIB_INFO_V6(Structure):
        pass
    return DHCP_MIB_INFO_V6
def _define_DHCP_MIB_INFO_V6():
    DHCP_MIB_INFO_V6 = win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_V6_head
    DHCP_MIB_INFO_V6._fields_ = [
        ("Solicits", UInt32),
        ("Advertises", UInt32),
        ("Requests", UInt32),
        ("Renews", UInt32),
        ("Rebinds", UInt32),
        ("Replies", UInt32),
        ("Confirms", UInt32),
        ("Declines", UInt32),
        ("Releases", UInt32),
        ("Informs", UInt32),
        ("ServerStartTime", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("Scopes", UInt32),
        ("ScopeInfo", POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V6_head)),
    ]
    return DHCP_MIB_INFO_V6
def _define_DHCP_IP_RESERVATION_V6_head():
    class DHCP_IP_RESERVATION_V6(Structure):
        pass
    return DHCP_IP_RESERVATION_V6
def _define_DHCP_IP_RESERVATION_V6():
    DHCP_IP_RESERVATION_V6 = win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V6_head
    DHCP_IP_RESERVATION_V6._fields_ = [
        ("ReservedIpAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("ReservedForClient", POINTER(win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)),
        ("InterfaceId", UInt32),
    ]
    return DHCP_IP_RESERVATION_V6
DHCP_SUBNET_ELEMENT_TYPE_V6 = Int32
DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6IpRanges = 0
DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ReservedIps = 1
DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ExcludedIpRanges = 2
def _define_DHCP_SUBNET_ELEMENT_DATA_V6_head():
    class DHCP_SUBNET_ELEMENT_DATA_V6(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_DATA_V6
def _define_DHCP_SUBNET_ELEMENT_DATA_V6():
    DHCP_SUBNET_ELEMENT_DATA_V6 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head
    class DHCP_SUBNET_ELEMENT_DATA_V6_DHCP_SUBNET_ELEMENT_UNION_V6(Union):
        pass
    DHCP_SUBNET_ELEMENT_DATA_V6_DHCP_SUBNET_ELEMENT_UNION_V6._fields_ = [
        ("IpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_V6_head)),
        ("ReservedIp", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V6_head)),
        ("ExcludeIpRange", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_V6_head)),
    ]
    DHCP_SUBNET_ELEMENT_DATA_V6._fields_ = [
        ("ElementType", win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE_V6),
        ("Element", DHCP_SUBNET_ELEMENT_DATA_V6_DHCP_SUBNET_ELEMENT_UNION_V6),
    ]
    return DHCP_SUBNET_ELEMENT_DATA_V6
def _define_DHCP_SUBNET_ELEMENT_UNION_V6_head():
    class DHCP_SUBNET_ELEMENT_UNION_V6(Union):
        pass
    return DHCP_SUBNET_ELEMENT_UNION_V6
def _define_DHCP_SUBNET_ELEMENT_UNION_V6():
    DHCP_SUBNET_ELEMENT_UNION_V6 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_UNION_V6_head
    return DHCP_SUBNET_ELEMENT_UNION_V6
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6_head():
    class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(Structure):
        pass
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6
def _define_DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6():
    DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6 = win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6_head
    DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head)),
    ]
    return DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6
def _define_DHCP_CLIENT_INFO_V6_head():
    class DHCP_CLIENT_INFO_V6(Structure):
        pass
    return DHCP_CLIENT_INFO_V6
def _define_DHCP_CLIENT_INFO_V6():
    DHCP_CLIENT_INFO_V6 = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head
    DHCP_CLIENT_INFO_V6._fields_ = [
        ("ClientIpAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("ClientDUID", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("AddressType", UInt32),
        ("IAID", UInt32),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientValidLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("ClientPrefLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_V6),
    ]
    return DHCP_CLIENT_INFO_V6
def _define_DHCPV6_IP_ARRAY_head():
    class DHCPV6_IP_ARRAY(Structure):
        pass
    return DHCPV6_IP_ARRAY
def _define_DHCPV6_IP_ARRAY():
    DHCPV6_IP_ARRAY = win32more.NetworkManagement.Dhcp.DHCPV6_IP_ARRAY_head
    DHCPV6_IP_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS_head)),
    ]
    return DHCPV6_IP_ARRAY
def _define_DHCP_CLIENT_INFO_ARRAY_V6_head():
    class DHCP_CLIENT_INFO_ARRAY_V6(Structure):
        pass
    return DHCP_CLIENT_INFO_ARRAY_V6
def _define_DHCP_CLIENT_INFO_ARRAY_V6():
    DHCP_CLIENT_INFO_ARRAY_V6 = win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V6_head
    DHCP_CLIENT_INFO_ARRAY_V6._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head))),
    ]
    return DHCP_CLIENT_INFO_ARRAY_V6
DHCP_SEARCH_INFO_TYPE_V6 = Int32
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientIpAddress = 0
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientDUID = 1
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientName = 2
def _define_DHCP_SEARCH_INFO_V6_head():
    class DHCP_SEARCH_INFO_V6(Structure):
        pass
    return DHCP_SEARCH_INFO_V6
def _define_DHCP_SEARCH_INFO_V6():
    DHCP_SEARCH_INFO_V6 = win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_V6_head
    class DHCP_SEARCH_INFO_V6__DHCP_CLIENT_SEARCH_UNION_V6(Union):
        pass
    DHCP_SEARCH_INFO_V6__DHCP_CLIENT_SEARCH_UNION_V6._fields_ = [
        ("ClientIpAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("ClientDUID", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
    ]
    DHCP_SEARCH_INFO_V6._fields_ = [
        ("SearchType", win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_TYPE_V6),
        ("SearchInfo", DHCP_SEARCH_INFO_V6__DHCP_CLIENT_SEARCH_UNION_V6),
    ]
    return DHCP_SEARCH_INFO_V6
DHCP_POL_ATTR_TYPE = Int32
DHCP_POL_ATTR_TYPE_DhcpAttrHWAddr = 0
DHCP_POL_ATTR_TYPE_DhcpAttrOption = 1
DHCP_POL_ATTR_TYPE_DhcpAttrSubOption = 2
DHCP_POL_ATTR_TYPE_DhcpAttrFqdn = 3
DHCP_POL_ATTR_TYPE_DhcpAttrFqdnSingleLabel = 4
DHCP_POL_COMPARATOR = Int32
DHCP_POL_COMPARATOR_DhcpCompEqual = 0
DHCP_POL_COMPARATOR_DhcpCompNotEqual = 1
DHCP_POL_COMPARATOR_DhcpCompBeginsWith = 2
DHCP_POL_COMPARATOR_DhcpCompNotBeginWith = 3
DHCP_POL_COMPARATOR_DhcpCompEndsWith = 4
DHCP_POL_COMPARATOR_DhcpCompNotEndWith = 5
DHCP_POL_LOGIC_OPER = Int32
DHCP_POL_LOGIC_OPER_DhcpLogicalOr = 0
DHCP_POL_LOGIC_OPER_DhcpLogicalAnd = 1
DHCP_POLICY_FIELDS_TO_UPDATE = Int32
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyName = 1
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyOrder = 2
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyExpr = 4
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyRanges = 8
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDescr = 16
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyStatus = 32
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDnsSuffix = 64
def _define_DHCP_POL_COND_head():
    class DHCP_POL_COND(Structure):
        pass
    return DHCP_POL_COND
def _define_DHCP_POL_COND():
    DHCP_POL_COND = win32more.NetworkManagement.Dhcp.DHCP_POL_COND_head
    DHCP_POL_COND._fields_ = [
        ("ParentExpr", UInt32),
        ("Type", win32more.NetworkManagement.Dhcp.DHCP_POL_ATTR_TYPE),
        ("OptionID", UInt32),
        ("SubOptionID", UInt32),
        ("VendorName", win32more.Foundation.PWSTR),
        ("Operator", win32more.NetworkManagement.Dhcp.DHCP_POL_COMPARATOR),
        ("Value", c_char_p_no),
        ("ValueLength", UInt32),
    ]
    return DHCP_POL_COND
def _define_DHCP_POL_COND_ARRAY_head():
    class DHCP_POL_COND_ARRAY(Structure):
        pass
    return DHCP_POL_COND_ARRAY
def _define_DHCP_POL_COND_ARRAY():
    DHCP_POL_COND_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_POL_COND_ARRAY_head
    DHCP_POL_COND_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_COND_head)),
    ]
    return DHCP_POL_COND_ARRAY
def _define_DHCP_POL_EXPR_head():
    class DHCP_POL_EXPR(Structure):
        pass
    return DHCP_POL_EXPR
def _define_DHCP_POL_EXPR():
    DHCP_POL_EXPR = win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_head
    DHCP_POL_EXPR._fields_ = [
        ("ParentExpr", UInt32),
        ("Operator", win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER),
    ]
    return DHCP_POL_EXPR
def _define_DHCP_POL_EXPR_ARRAY_head():
    class DHCP_POL_EXPR_ARRAY(Structure):
        pass
    return DHCP_POL_EXPR_ARRAY
def _define_DHCP_POL_EXPR_ARRAY():
    DHCP_POL_EXPR_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_ARRAY_head
    DHCP_POL_EXPR_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_head)),
    ]
    return DHCP_POL_EXPR_ARRAY
def _define_DHCP_IP_RANGE_ARRAY_head():
    class DHCP_IP_RANGE_ARRAY(Structure):
        pass
    return DHCP_IP_RANGE_ARRAY
def _define_DHCP_IP_RANGE_ARRAY():
    DHCP_IP_RANGE_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_ARRAY_head
    DHCP_IP_RANGE_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)),
    ]
    return DHCP_IP_RANGE_ARRAY
def _define_DHCP_POLICY_head():
    class DHCP_POLICY(Structure):
        pass
    return DHCP_POLICY
def _define_DHCP_POLICY():
    DHCP_POLICY = win32more.NetworkManagement.Dhcp.DHCP_POLICY_head
    DHCP_POLICY._fields_ = [
        ("PolicyName", win32more.Foundation.PWSTR),
        ("IsGlobalPolicy", win32more.Foundation.BOOL),
        ("Subnet", UInt32),
        ("ProcessingOrder", UInt32),
        ("Conditions", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_COND_ARRAY_head)),
        ("Expressions", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_ARRAY_head)),
        ("Ranges", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_ARRAY_head)),
        ("Description", win32more.Foundation.PWSTR),
        ("Enabled", win32more.Foundation.BOOL),
    ]
    return DHCP_POLICY
def _define_DHCP_POLICY_ARRAY_head():
    class DHCP_POLICY_ARRAY(Structure):
        pass
    return DHCP_POLICY_ARRAY
def _define_DHCP_POLICY_ARRAY():
    DHCP_POLICY_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_POLICY_ARRAY_head
    DHCP_POLICY_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)),
    ]
    return DHCP_POLICY_ARRAY
def _define_DHCP_POLICY_EX_head():
    class DHCP_POLICY_EX(Structure):
        pass
    return DHCP_POLICY_EX
def _define_DHCP_POLICY_EX():
    DHCP_POLICY_EX = win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head
    DHCP_POLICY_EX._fields_ = [
        ("PolicyName", win32more.Foundation.PWSTR),
        ("IsGlobalPolicy", win32more.Foundation.BOOL),
        ("Subnet", UInt32),
        ("ProcessingOrder", UInt32),
        ("Conditions", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_COND_ARRAY_head)),
        ("Expressions", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_ARRAY_head)),
        ("Ranges", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_ARRAY_head)),
        ("Description", win32more.Foundation.PWSTR),
        ("Enabled", win32more.Foundation.BOOL),
        ("Properties", POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)),
    ]
    return DHCP_POLICY_EX
def _define_DHCP_POLICY_EX_ARRAY_head():
    class DHCP_POLICY_EX_ARRAY(Structure):
        pass
    return DHCP_POLICY_EX_ARRAY
def _define_DHCP_POLICY_EX_ARRAY():
    DHCP_POLICY_EX_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_ARRAY_head
    DHCP_POLICY_EX_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Elements", POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)),
    ]
    return DHCP_POLICY_EX_ARRAY
DHCPV6_STATELESS_PARAM_TYPE = Int32
DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessPurgeInterval = 1
DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessStatus = 2
def _define_DHCPV6_STATELESS_PARAMS_head():
    class DHCPV6_STATELESS_PARAMS(Structure):
        pass
    return DHCPV6_STATELESS_PARAMS
def _define_DHCPV6_STATELESS_PARAMS():
    DHCPV6_STATELESS_PARAMS = win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_PARAMS_head
    DHCPV6_STATELESS_PARAMS._fields_ = [
        ("Status", win32more.Foundation.BOOL),
        ("PurgeInterval", UInt32),
    ]
    return DHCPV6_STATELESS_PARAMS
def _define_DHCPV6_STATELESS_SCOPE_STATS_head():
    class DHCPV6_STATELESS_SCOPE_STATS(Structure):
        pass
    return DHCPV6_STATELESS_SCOPE_STATS
def _define_DHCPV6_STATELESS_SCOPE_STATS():
    DHCPV6_STATELESS_SCOPE_STATS = win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_SCOPE_STATS_head
    DHCPV6_STATELESS_SCOPE_STATS._fields_ = [
        ("SubnetAddress", win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS),
        ("NumStatelessClientsAdded", UInt64),
        ("NumStatelessClientsRemoved", UInt64),
    ]
    return DHCPV6_STATELESS_SCOPE_STATS
def _define_DHCPV6_STATELESS_STATS_head():
    class DHCPV6_STATELESS_STATS(Structure):
        pass
    return DHCPV6_STATELESS_STATS
def _define_DHCPV6_STATELESS_STATS():
    DHCPV6_STATELESS_STATS = win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_STATS_head
    DHCPV6_STATELESS_STATS._fields_ = [
        ("NumScopes", UInt32),
        ("ScopeStats", POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_SCOPE_STATS_head)),
    ]
    return DHCPV6_STATELESS_STATS
DHCP_FAILOVER_MODE = Int32
DHCP_FAILOVER_MODE_LoadBalance = 0
DHCP_FAILOVER_MODE_HotStandby = 1
DHCP_FAILOVER_SERVER = Int32
DHCP_FAILOVER_SERVER_PrimaryServer = 0
DHCP_FAILOVER_SERVER_SecondaryServer = 1
FSM_STATE = Int32
NO_STATE = 0
INIT = 1
STARTUP = 2
NORMAL = 3
COMMUNICATION_INT = 4
PARTNER_DOWN = 5
POTENTIAL_CONFLICT = 6
CONFLICT_DONE = 7
RESOLUTION_INT = 8
RECOVER = 9
RECOVER_WAIT = 10
RECOVER_DONE = 11
PAUSED = 12
SHUTDOWN = 13
def _define_DHCP_FAILOVER_RELATIONSHIP_head():
    class DHCP_FAILOVER_RELATIONSHIP(Structure):
        pass
    return DHCP_FAILOVER_RELATIONSHIP
def _define_DHCP_FAILOVER_RELATIONSHIP():
    DHCP_FAILOVER_RELATIONSHIP = win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head
    DHCP_FAILOVER_RELATIONSHIP._fields_ = [
        ("PrimaryServer", UInt32),
        ("SecondaryServer", UInt32),
        ("Mode", win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_MODE),
        ("ServerType", win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_SERVER),
        ("State", win32more.NetworkManagement.Dhcp.FSM_STATE),
        ("PrevState", win32more.NetworkManagement.Dhcp.FSM_STATE),
        ("Mclt", UInt32),
        ("SafePeriod", UInt32),
        ("RelationshipName", win32more.Foundation.PWSTR),
        ("PrimaryServerName", win32more.Foundation.PWSTR),
        ("SecondaryServerName", win32more.Foundation.PWSTR),
        ("pScopes", POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head)),
        ("Percentage", Byte),
        ("SharedSecret", win32more.Foundation.PWSTR),
    ]
    return DHCP_FAILOVER_RELATIONSHIP
def _define_DHCP_FAILOVER_RELATIONSHIP_ARRAY_head():
    class DHCP_FAILOVER_RELATIONSHIP_ARRAY(Structure):
        pass
    return DHCP_FAILOVER_RELATIONSHIP_ARRAY
def _define_DHCP_FAILOVER_RELATIONSHIP_ARRAY():
    DHCP_FAILOVER_RELATIONSHIP_ARRAY = win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_ARRAY_head
    DHCP_FAILOVER_RELATIONSHIP_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("pRelationships", POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)),
    ]
    return DHCP_FAILOVER_RELATIONSHIP_ARRAY
def _define_DHCPV4_FAILOVER_CLIENT_INFO_head():
    class DHCPV4_FAILOVER_CLIENT_INFO(Structure):
        pass
    return DHCPV4_FAILOVER_CLIENT_INFO
def _define_DHCPV4_FAILOVER_CLIENT_INFO():
    DHCPV4_FAILOVER_CLIENT_INFO = win32more.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_head
    DHCPV4_FAILOVER_CLIENT_INFO._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
        ("AddressState", Byte),
        ("Status", win32more.NetworkManagement.Dhcp.QuarantineStatus),
        ("ProbationEnds", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QuarantineCapable", win32more.Foundation.BOOL),
        ("SentPotExpTime", UInt32),
        ("AckPotExpTime", UInt32),
        ("RecvPotExpTime", UInt32),
        ("StartTime", UInt32),
        ("CltLastTransTime", UInt32),
        ("LastBndUpdTime", UInt32),
        ("BndMsgStatus", UInt32),
        ("PolicyName", win32more.Foundation.PWSTR),
        ("Flags", Byte),
    ]
    return DHCPV4_FAILOVER_CLIENT_INFO
def _define_DHCPV4_FAILOVER_CLIENT_INFO_ARRAY_head():
    class DHCPV4_FAILOVER_CLIENT_INFO_ARRAY(Structure):
        pass
    return DHCPV4_FAILOVER_CLIENT_INFO_ARRAY
def _define_DHCPV4_FAILOVER_CLIENT_INFO_ARRAY():
    DHCPV4_FAILOVER_CLIENT_INFO_ARRAY = win32more.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_ARRAY_head
    DHCPV4_FAILOVER_CLIENT_INFO_ARRAY._fields_ = [
        ("NumElements", UInt32),
        ("Clients", POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_head))),
    ]
    return DHCPV4_FAILOVER_CLIENT_INFO_ARRAY
def _define_DHCPV4_FAILOVER_CLIENT_INFO_EX_head():
    class DHCPV4_FAILOVER_CLIENT_INFO_EX(Structure):
        pass
    return DHCPV4_FAILOVER_CLIENT_INFO_EX
def _define_DHCPV4_FAILOVER_CLIENT_INFO_EX():
    DHCPV4_FAILOVER_CLIENT_INFO_EX = win32more.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_EX_head
    DHCPV4_FAILOVER_CLIENT_INFO_EX._fields_ = [
        ("ClientIpAddress", UInt32),
        ("SubnetMask", UInt32),
        ("ClientHardwareAddress", win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA),
        ("ClientName", win32more.Foundation.PWSTR),
        ("ClientComment", win32more.Foundation.PWSTR),
        ("ClientLeaseExpires", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("OwnerHost", win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO),
        ("bClientType", Byte),
        ("AddressState", Byte),
        ("Status", win32more.NetworkManagement.Dhcp.QuarantineStatus),
        ("ProbationEnds", win32more.NetworkManagement.Dhcp.DATE_TIME),
        ("QuarantineCapable", win32more.Foundation.BOOL),
        ("SentPotExpTime", UInt32),
        ("AckPotExpTime", UInt32),
        ("RecvPotExpTime", UInt32),
        ("StartTime", UInt32),
        ("CltLastTransTime", UInt32),
        ("LastBndUpdTime", UInt32),
        ("BndMsgStatus", UInt32),
        ("PolicyName", win32more.Foundation.PWSTR),
        ("Flags", Byte),
        ("AddressStateEx", UInt32),
    ]
    return DHCPV4_FAILOVER_CLIENT_INFO_EX
def _define_DHCP_FAILOVER_STATISTICS_head():
    class DHCP_FAILOVER_STATISTICS(Structure):
        pass
    return DHCP_FAILOVER_STATISTICS
def _define_DHCP_FAILOVER_STATISTICS():
    DHCP_FAILOVER_STATISTICS = win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_STATISTICS_head
    DHCP_FAILOVER_STATISTICS._fields_ = [
        ("NumAddr", UInt32),
        ("AddrFree", UInt32),
        ("AddrInUse", UInt32),
        ("PartnerAddrFree", UInt32),
        ("ThisAddrFree", UInt32),
        ("PartnerAddrInUse", UInt32),
        ("ThisAddrInUse", UInt32),
    ]
    return DHCP_FAILOVER_STATISTICS
def _define_Dhcpv6CApiInitialize():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32), use_last_error=False)(("Dhcpv6CApiInitialize", windll["dhcpcsvc6"]), ((1, 'Version'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Dhcpv6CApiCleanup():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("Dhcpv6CApiCleanup", windll["dhcpcsvc6"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_Dhcpv6RequestParams():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head),win32more.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_ARRAY,c_char_p_no,POINTER(UInt32), use_last_error=False)(("Dhcpv6RequestParams", windll["dhcpcsvc6"]), ((1, 'forceNewInform'),(1, 'reserved'),(1, 'adapterName'),(1, 'classId'),(1, 'recdParams'),(1, 'buffer'),(1, 'pSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Dhcpv6RequestPrefix():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head),POINTER(win32more.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head),POINTER(UInt32), use_last_error=False)(("Dhcpv6RequestPrefix", windll["dhcpcsvc6"]), ((1, 'adapterName'),(1, 'pclassId'),(1, 'prefixleaseInfo'),(1, 'pdwTimeToWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Dhcpv6RenewPrefix():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head),POINTER(win32more.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head),POINTER(UInt32),UInt32, use_last_error=False)(("Dhcpv6RenewPrefix", windll["dhcpcsvc6"]), ((1, 'adapterName'),(1, 'pclassId'),(1, 'prefixleaseInfo'),(1, 'pdwTimeToWait'),(1, 'bValidatePrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Dhcpv6ReleasePrefix():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head),POINTER(win32more.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head), use_last_error=False)(("Dhcpv6ReleasePrefix", windll["dhcpcsvc6"]), ((1, 'adapterName'),(1, 'classId'),(1, 'leaseInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCApiInitialize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32), use_last_error=False)(("DhcpCApiInitialize", windll["dhcpcsvc"]), ((1, 'Version'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCApiCleanup():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("DhcpCApiCleanup", windll["dhcpcsvc"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRequestParams():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCPCAPI_CLASSID_head),win32more.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY,win32more.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY,c_char_p_no,POINTER(UInt32),win32more.Foundation.PWSTR, use_last_error=False)(("DhcpRequestParams", windll["dhcpcsvc"]), ((1, 'Flags'),(1, 'Reserved'),(1, 'AdapterName'),(1, 'ClassId'),(1, 'SendParams'),(1, 'RecdParams'),(1, 'Buffer'),(1, 'pSize'),(1, 'RequestIdStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpUndoRequestParams():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpUndoRequestParams", windll["dhcpcsvc"]), ((1, 'Flags'),(1, 'Reserved'),(1, 'AdapterName'),(1, 'RequestIdStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRegisterParamChange():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCPCAPI_CLASSID_head),win32more.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY,c_void_p, use_last_error=False)(("DhcpRegisterParamChange", windll["dhcpcsvc"]), ((1, 'Flags'),(1, 'Reserved'),(1, 'AdapterName'),(1, 'ClassId'),(1, 'Params'),(1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeRegisterParamChange():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,c_void_p, use_last_error=False)(("DhcpDeRegisterParamChange", windll["dhcpcsvc"]), ((1, 'Flags'),(1, 'Reserved'),(1, 'Event'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveDNSRegistrations():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("DhcpRemoveDNSRegistrations", windll["dhcpcsvc"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetOriginalSubnetMask():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DhcpGetOriginalSubnetMask", windll["dhcpcsvc"]), ((1, 'sAdapterName'),(1, 'dwSubnetMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAddFilterV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_ADD_INFO_head),win32more.Foundation.BOOL, use_last_error=False)(("DhcpAddFilterV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'AddFilterInfo'),(1, 'ForceFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteFilterV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN_head), use_last_error=False)(("DhcpDeleteFilterV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'DeleteFilterInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetFilterV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_GLOBAL_INFO_head), use_last_error=False)(("DhcpSetFilterV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'GlobalFilterInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetFilterV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_GLOBAL_INFO_head), use_last_error=False)(("DhcpGetFilterV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'GlobalFilterInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumFilterV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN_head),UInt32,win32more.NetworkManagement.Dhcp.DHCP_FILTER_LIST_TYPE,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_ENUM_INFO_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumFilterV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ListType'),(1, 'EnumFilterInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateSubnet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head), use_last_error=False)(("DhcpCreateSubnet", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetSubnetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head), use_last_error=False)(("DhcpSetSubnetInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetSubnetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head)), use_last_error=False)(("DhcpGetSubnetInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnets():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnets", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'EnumInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAddSubnetElement():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head), use_last_error=False)(("DhcpAddSubnetElement", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'AddElementInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetElements():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetElements", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'EnumElementType'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'EnumElementInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveSubnetElement():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head),win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG, use_last_error=False)(("DhcpRemoveSubnetElement", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'RemoveElementInfo'),(1, 'ForceFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteSubnet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG, use_last_error=False)(("DhcpDeleteSubnet", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ForceFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateOption():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head), use_last_error=False)(("DhcpCreateOption", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'OptionID'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head), use_last_error=False)(("DhcpSetOptionInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'OptionID'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetOptionInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)), use_last_error=False)(("DhcpGetOptionInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'OptionID'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumOptions():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumOptions", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'Options'),(1, 'OptionsRead'),(1, 'OptionsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveOption():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("DhcpRemoveOption", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'OptionID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head), use_last_error=False)(("DhcpSetOptionValue", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'OptionID'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionValues():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head), use_last_error=False)(("DhcpSetOptionValues", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeInfo'),(1, 'OptionValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetOptionValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)), use_last_error=False)(("DhcpGetOptionValue", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'OptionID'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumOptionValues():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumOptionValues", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeInfo'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'OptionValues'),(1, 'OptionsRead'),(1, 'OptionsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveOptionValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), use_last_error=False)(("DhcpRemoveOptionValue", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'OptionID'),(1, 'ScopeInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateClientInfoVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head), use_last_error=False)(("DhcpCreateClientInfoVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetClientInfoVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head), use_last_error=False)(("DhcpSetClientInfoVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetClientInfoVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head)), use_last_error=False)(("DhcpGetClientInfoVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SearchInfo'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetClientsVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_VQ_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetClientsVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetClientsFilterStatusInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetClientsFilterStatusInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head), use_last_error=False)(("DhcpCreateClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head), use_last_error=False)(("DhcpSetClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head)), use_last_error=False)(("DhcpGetClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SearchInfo'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), use_last_error=False)(("DhcpDeleteClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetClients():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetClients", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetClientOptions():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_LIST_head)), use_last_error=False)(("DhcpGetClientOptions", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientIpAddress'),(1, 'ClientSubnetMask'),(1, 'ClientOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetMibInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_head)), use_last_error=False)(("DhcpGetMibInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'MibInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerSetConfig():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_head), use_last_error=False)(("DhcpServerSetConfig", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'FieldsToSet'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerGetConfig():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_head)), use_last_error=False)(("DhcpServerGetConfig", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpScanDatabase():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SCAN_LIST_head)), use_last_error=False)(("DhcpScanDatabase", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'FixFlag'),(1, 'ScanList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRpcFreeMemory():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("DhcpRpcFreeMemory", windll["DHCPSAPI"]), ((1, 'BufferPointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetVersion():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpGetVersion", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'MajorVersion'),(1, 'MinorVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAddSubnetElementV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head), use_last_error=False)(("DhcpAddSubnetElementV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'AddElementInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetElementsV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetElementsV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'EnumElementType'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'EnumElementInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveSubnetElementV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head),win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG, use_last_error=False)(("DhcpRemoveSubnetElementV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'RemoveElementInfo'),(1, 'ForceFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateClientInfoV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head), use_last_error=False)(("DhcpCreateClientInfoV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetClientInfoV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head), use_last_error=False)(("DhcpSetClientInfoV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetClientInfoV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head)), use_last_error=False)(("DhcpGetClientInfoV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SearchInfo'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetClientsV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V4_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetClientsV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerSetConfigV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V4_head), use_last_error=False)(("DhcpServerSetConfigV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'FieldsToSet'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerGetConfigV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V4_head)), use_last_error=False)(("DhcpServerGetConfigV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetSuperScopeV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("DhcpSetSuperScopeV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SuperScopeName'),(1, 'ChangeExisting'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteSuperScopeV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpDeleteSuperScopeV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SuperScopeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetSuperScopeInfoV4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_head)), use_last_error=False)(("DhcpGetSuperScopeInfoV4", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SuperScopeTable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetClientsV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V5_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetClientsV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateOptionV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head), use_last_error=False)(("DhcpCreateOptionV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionId'),(1, 'ClassName'),(1, 'VendorName'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionInfoV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head), use_last_error=False)(("DhcpSetOptionInfoV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetOptionInfoV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)), use_last_error=False)(("DhcpGetOptionInfoV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumOptionsV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumOptionsV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'Options'),(1, 'OptionsRead'),(1, 'OptionsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveOptionV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpRemoveOptionV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionValueV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head), use_last_error=False)(("DhcpSetOptionValueV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionId'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionValuesV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head), use_last_error=False)(("DhcpSetOptionValuesV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetOptionValueV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)), use_last_error=False)(("DhcpGetOptionValueV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetOptionValueV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)), use_last_error=False)(("DhcpGetOptionValueV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumOptionValuesV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumOptionValuesV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'OptionValues'),(1, 'OptionsRead'),(1, 'OptionsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveOptionValueV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), use_last_error=False)(("DhcpRemoveOptionValueV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateClass():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head), use_last_error=False)(("DhcpCreateClass", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ClassInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpModifyClass():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head), use_last_error=False)(("DhcpModifyClass", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ClassInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteClass():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpDeleteClass", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ClassName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetClassInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)), use_last_error=False)(("DhcpGetClassInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'PartialClassInfo'),(1, 'FilledClassInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumClasses():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumClasses", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClassInfoArray'),(1, 'nRead'),(1, 'nTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetAllOptions():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTIONS_head)), use_last_error=False)(("DhcpGetAllOptions", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetAllOptionsV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTIONS_head)), use_last_error=False)(("DhcpGetAllOptionsV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetAllOptionValues():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_head)), use_last_error=False)(("DhcpGetAllOptionValues", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ScopeInfo'),(1, 'Values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetAllOptionValuesV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_head)), use_last_error=False)(("DhcpGetAllOptionValuesV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ScopeInfo'),(1, 'Values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumServers():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVERS_head)),c_void_p,c_void_p, use_last_error=False)(("DhcpEnumServers", windll["DHCPSAPI"]), ((1, 'Flags'),(1, 'IdInfo'),(1, 'Servers'),(1, 'CallbackFn'),(1, 'CallbackData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAddServer():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVER_head),c_void_p,c_void_p, use_last_error=False)(("DhcpAddServer", windll["DHCPSAPI"]), ((1, 'Flags'),(1, 'IdInfo'),(1, 'NewServer'),(1, 'CallbackFn'),(1, 'CallbackData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteServer():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVER_head),c_void_p,c_void_p, use_last_error=False)(("DhcpDeleteServer", windll["DHCPSAPI"]), ((1, 'Flags'),(1, 'IdInfo'),(1, 'NewServer'),(1, 'CallbackFn'),(1, 'CallbackData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetServerBindingInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_ARRAY_head)), use_last_error=False)(("DhcpGetServerBindingInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'BindElementsInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetServerBindingInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_ARRAY_head), use_last_error=False)(("DhcpSetServerBindingInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'BindElementInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAddSubnetElementV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head), use_last_error=False)(("DhcpAddSubnetElementV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'AddElementInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetElementsV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetElementsV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'EnumElementType'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'EnumElementInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveSubnetElementV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head),win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG, use_last_error=False)(("DhcpRemoveSubnetElementV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'RemoveElementInfo'),(1, 'ForceFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4EnumSubnetReservations():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_RESERVATION_INFO_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpV4EnumSubnetReservations", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'EnumElementInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateOptionV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head), use_last_error=False)(("DhcpCreateOptionV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionId'),(1, 'ClassName'),(1, 'VendorName'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveOptionV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpRemoveOptionV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumOptionsV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumOptionsV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'Options'),(1, 'OptionsRead'),(1, 'OptionsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveOptionValueV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), use_last_error=False)(("DhcpRemoveOptionValueV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetOptionInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)), use_last_error=False)(("DhcpGetOptionInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head), use_last_error=False)(("DhcpSetOptionInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'ClassName'),(1, 'VendorName'),(1, 'OptionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetOptionValueV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head), use_last_error=False)(("DhcpSetOptionValueV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionId'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetSubnetInfoVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head)), use_last_error=False)(("DhcpGetSubnetInfoVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateSubnetVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head), use_last_error=False)(("DhcpCreateSubnetVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetSubnetInfoVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head), use_last_error=False)(("DhcpSetSubnetInfoVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumOptionValuesV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head),POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumOptionValuesV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ClassName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'OptionValues'),(1, 'OptionsRead'),(1, 'OptionsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDsInit():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("DhcpDsInit", windll["DHCPSAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDsCleanup():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("DhcpDsCleanup", windll["DHCPSAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetThreadOptions():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p, use_last_error=False)(("DhcpSetThreadOptions", windll["DHCPSAPI"]), ((1, 'Flags'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetThreadOptions():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),c_void_p, use_last_error=False)(("DhcpGetThreadOptions", windll["DHCPSAPI"]), ((1, 'pFlags'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerQueryAttribute():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_head)), use_last_error=False)(("DhcpServerQueryAttribute", windll["DHCPSAPI"]), ((1, 'ServerIpAddr'),(1, 'dwReserved'),(1, 'DhcpAttribId'),(1, 'pDhcpAttrib'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerQueryAttributes():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_ARRAY_head)), use_last_error=False)(("DhcpServerQueryAttributes", windll["DHCPSAPI"]), ((1, 'ServerIpAddr'),(1, 'dwReserved'),(1, 'dwAttribCount'),(1, 'pDhcpAttribs'),(1, 'pDhcpAttribArr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerRedoAuthorization():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("DhcpServerRedoAuthorization", windll["DHCPSAPI"]), ((1, 'ServerIpAddr'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAuditLogSetParams():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32, use_last_error=False)(("DhcpAuditLogSetParams", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'AuditLogDir'),(1, 'DiskCheckInterval'),(1, 'MaxLogFilesSize'),(1, 'MinSpaceOnDisk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAuditLogGetParams():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpAuditLogGetParams", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'AuditLogDir'),(1, 'DiskCheckInterval'),(1, 'MaxLogFilesSize'),(1, 'MinSpaceOnDisk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerQueryDnsRegCredentials():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(Char),UInt32,POINTER(Char), use_last_error=False)(("DhcpServerQueryDnsRegCredentials", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'UnameSize'),(1, 'Uname'),(1, 'DomainSize'),(1, 'Domain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerSetDnsRegCredentials():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpServerSetDnsRegCredentials", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Uname'),(1, 'Domain'),(1, 'Passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerSetDnsRegCredentialsV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpServerSetDnsRegCredentialsV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Uname'),(1, 'Domain'),(1, 'Passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerBackupDatabase():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpServerBackupDatabase", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerRestoreDatabase():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpServerRestoreDatabase", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerSetConfigVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head), use_last_error=False)(("DhcpServerSetConfigVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'FieldsToSet'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerGetConfigVQ():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head)), use_last_error=False)(("DhcpServerGetConfigVQ", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetServerSpecificStrings():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_SPECIFIC_STRINGS_head)), use_last_error=False)(("DhcpGetServerSpecificStrings", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ServerSpecificStrings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerAuditlogParamsFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head), use_last_error=False)(("DhcpServerAuditlogParamsFree", windll["DHCPSAPI"]), ((1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateSubnetV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head), use_last_error=False)(("DhcpCreateSubnetV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteSubnetV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG, use_last_error=False)(("DhcpDeleteSubnetV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ForceFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetsV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_IP_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetsV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'EnumInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAddSubnetElementV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head), use_last_error=False)(("DhcpAddSubnetElementV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'AddElementInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpRemoveSubnetElementV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head),win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG, use_last_error=False)(("DhcpRemoveSubnetElementV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'RemoveElementInfo'),(1, 'ForceFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetElementsV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE_V6,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetElementsV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'EnumElementType'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'EnumElementInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetSubnetInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head)), use_last_error=False)(("DhcpGetSubnetInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumSubnetClientsV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,POINTER(win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS_head),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V6_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumSubnetClientsV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerGetConfigV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V6_head)), use_last_error=False)(("DhcpServerGetConfigV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeInfo'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpServerSetConfigV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head),UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V6_head), use_last_error=False)(("DhcpServerSetConfigV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeInfo'),(1, 'FieldsToSet'),(1, 'ConfigInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetSubnetInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head), use_last_error=False)(("DhcpSetSubnetInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'SubnetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetMibInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_V6_head)), use_last_error=False)(("DhcpGetMibInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'MibInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetServerBindingInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_ARRAY_head)), use_last_error=False)(("DhcpGetServerBindingInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'BindElementsInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetServerBindingInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_ARRAY_head), use_last_error=False)(("DhcpSetServerBindingInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'BindElementInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetClientInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head), use_last_error=False)(("DhcpSetClientInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetClientInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_V6_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head)), use_last_error=False)(("DhcpGetClientInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SearchInfo'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteClientInfoV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_V6_head), use_last_error=False)(("DhcpDeleteClientInfoV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpCreateClassV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head), use_last_error=False)(("DhcpCreateClassV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ClassInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpModifyClassV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head), use_last_error=False)(("DhcpModifyClassV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ClassInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpDeleteClassV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpDeleteClassV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ClassName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpEnumClassesV6():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_V6_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpEnumClassesV6", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ReservedMustBeZero'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClassInfoArray'),(1, 'nRead'),(1, 'nTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpSetSubnetDelayOffer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt16, use_last_error=False)(("DhcpSetSubnetDelayOffer", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'TimeDelayInMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetSubnetDelayOffer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt16), use_last_error=False)(("DhcpGetSubnetDelayOffer", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'TimeDelayInMilliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpGetMibInfoV5():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_V5_head)), use_last_error=False)(("DhcpGetMibInfoV5", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'MibInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpAddSecurityGroup():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpAddSecurityGroup", windll["DHCPSAPI"]), ((1, 'pServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4GetOptionValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)), use_last_error=False)(("DhcpV4GetOptionValue", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'PolicyName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4SetOptionValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head), use_last_error=False)(("DhcpV4SetOptionValue", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionId'),(1, 'PolicyName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4SetOptionValues():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head), use_last_error=False)(("DhcpV4SetOptionValues", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'PolicyName'),(1, 'VendorName'),(1, 'ScopeInfo'),(1, 'OptionValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4RemoveOptionValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), use_last_error=False)(("DhcpV4RemoveOptionValue", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'OptionID'),(1, 'PolicyName'),(1, 'VendorName'),(1, 'ScopeInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4GetAllOptionValues():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_PB_head)), use_last_error=False)(("DhcpV4GetAllOptionValues", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'ScopeInfo'),(1, 'Values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverCreateRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head), use_last_error=False)(("DhcpV4FailoverCreateRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pRelationship'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverSetRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head), use_last_error=False)(("DhcpV4FailoverSetRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'Flags'),(1, 'pRelationship'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverDeleteRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpV4FailoverDeleteRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pRelationshipName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverGetRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)), use_last_error=False)(("DhcpV4FailoverGetRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pRelationshipName'),(1, 'pRelationship'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverEnumRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpV4FailoverEnumRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'pRelationship'),(1, 'RelationshipRead'),(1, 'RelationshipTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverAddScopeToRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head), use_last_error=False)(("DhcpV4FailoverAddScopeToRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pRelationship'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverDeleteScopeFromRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head), use_last_error=False)(("DhcpV4FailoverDeleteScopeFromRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pRelationship'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverGetScopeRelationship():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)), use_last_error=False)(("DhcpV4FailoverGetScopeRelationship", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeId'),(1, 'pRelationship'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverGetScopeStatistics():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_STATISTICS_head)), use_last_error=False)(("DhcpV4FailoverGetScopeStatistics", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeId'),(1, 'pStats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverGetClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_head)), use_last_error=False)(("DhcpV4FailoverGetClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SearchInfo'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverGetSystemTime():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpV4FailoverGetSystemTime", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pTime'),(1, 'pMaxAllowedDeltaTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverGetAddressStatus():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32), use_last_error=False)(("DhcpV4FailoverGetAddressStatus", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'pStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4FailoverTriggerAddrAllocation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpV4FailoverTriggerAddrAllocation", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pFailRelName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprCreateV4Policy():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32,UInt32,win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)), use_last_error=False)(("DhcpHlprCreateV4Policy", windll["DHCPSAPI"]), ((1, 'PolicyName'),(1, 'fGlobalPolicy'),(1, 'Subnet'),(1, 'ProcessingOrder'),(1, 'RootOperator'),(1, 'Description'),(1, 'Enabled'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprCreateV4PolicyEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32,UInt32,win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)), use_last_error=False)(("DhcpHlprCreateV4PolicyEx", windll["DHCPSAPI"]), ((1, 'PolicyName'),(1, 'fGlobalPolicy'),(1, 'Subnet'),(1, 'ProcessingOrder'),(1, 'RootOperator'),(1, 'Description'),(1, 'Enabled'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprAddV4PolicyExpr():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head),UInt32,win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER,POINTER(UInt32), use_last_error=False)(("DhcpHlprAddV4PolicyExpr", windll["DHCPSAPI"]), ((1, 'Policy'),(1, 'ParentExpr'),(1, 'Operator'),(1, 'ExprIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprAddV4PolicyCondition():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head),UInt32,win32more.NetworkManagement.Dhcp.DHCP_POL_ATTR_TYPE,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_POL_COMPARATOR,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(("DhcpHlprAddV4PolicyCondition", windll["DHCPSAPI"]), ((1, 'Policy'),(1, 'ParentExpr'),(1, 'Type'),(1, 'OptionID'),(1, 'SubOptionID'),(1, 'VendorName'),(1, 'Operator'),(1, 'Value'),(1, 'ValueLength'),(1, 'ConditionIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprAddV4PolicyRange():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head), use_last_error=False)(("DhcpHlprAddV4PolicyRange", windll["DHCPSAPI"]), ((1, 'Policy'),(1, 'Range'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprResetV4PolicyExpr():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), use_last_error=False)(("DhcpHlprResetV4PolicyExpr", windll["DHCPSAPI"]), ((1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprModifyV4PolicyExpr():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head),win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER, use_last_error=False)(("DhcpHlprModifyV4PolicyExpr", windll["DHCPSAPI"]), ((1, 'Policy'),(1, 'Operator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprFreeV4Policy():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), use_last_error=False)(("DhcpHlprFreeV4Policy", windll["DHCPSAPI"]), ((1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprFreeV4PolicyArray():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_ARRAY_head), use_last_error=False)(("DhcpHlprFreeV4PolicyArray", windll["DHCPSAPI"]), ((1, 'PolicyArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprFreeV4PolicyEx():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head), use_last_error=False)(("DhcpHlprFreeV4PolicyEx", windll["DHCPSAPI"]), ((1, 'PolicyEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprFreeV4PolicyExArray():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_ARRAY_head), use_last_error=False)(("DhcpHlprFreeV4PolicyExArray", windll["DHCPSAPI"]), ((1, 'PolicyExArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprFreeV4DhcpProperty():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_head), use_last_error=False)(("DhcpHlprFreeV4DhcpProperty", windll["DHCPSAPI"]), ((1, 'Property'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprFreeV4DhcpPropertyArray():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head), use_last_error=False)(("DhcpHlprFreeV4DhcpPropertyArray", windll["DHCPSAPI"]), ((1, 'PropertyArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprFindV4DhcpProperty():
    try:
        return WINFUNCTYPE(POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_head),POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head),win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ID,win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_TYPE, use_last_error=False)(("DhcpHlprFindV4DhcpProperty", windll["DHCPSAPI"]), ((1, 'PropertyArray'),(1, 'ID'),(1, 'Type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprIsV4PolicySingleUC():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), use_last_error=False)(("DhcpHlprIsV4PolicySingleUC", windll["DHCPSAPI"]), ((1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4QueryPolicyEnforcement():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("DhcpV4QueryPolicyEnforcement", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'fGlobalPolicy'),(1, 'SubnetAddress'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4SetPolicyEnforcement():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("DhcpV4SetPolicyEnforcement", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'fGlobalPolicy'),(1, 'SubnetAddress'),(1, 'Enable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprIsV4PolicyWellFormed():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), use_last_error=False)(("DhcpHlprIsV4PolicyWellFormed", windll["DHCPSAPI"]), ((1, 'pPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpHlprIsV4PolicyValid():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), use_last_error=False)(("DhcpHlprIsV4PolicyValid", windll["DHCPSAPI"]), ((1, 'pPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4CreatePolicy():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), use_last_error=False)(("DhcpV4CreatePolicy", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'pPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4GetPolicy():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)), use_last_error=False)(("DhcpV4GetPolicy", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'fGlobalPolicy'),(1, 'SubnetAddress'),(1, 'PolicyName'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4SetPolicy():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), use_last_error=False)(("DhcpV4SetPolicy", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'FieldsModified'),(1, 'fGlobalPolicy'),(1, 'SubnetAddress'),(1, 'PolicyName'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4DeletePolicy():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DhcpV4DeletePolicy", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'fGlobalPolicy'),(1, 'SubnetAddress'),(1, 'PolicyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4EnumPolicies():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,win32more.Foundation.BOOL,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpV4EnumPolicies", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'fGlobalPolicy'),(1, 'SubnetAddress'),(1, 'EnumInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4AddPolicyRange():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head), use_last_error=False)(("DhcpV4AddPolicyRange", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'PolicyName'),(1, 'Range'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4RemovePolicyRange():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head), use_last_error=False)(("DhcpV4RemovePolicyRange", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'PolicyName'),(1, 'Range'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV6SetStatelessStoreParams():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,UInt32,POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_PARAMS_head), use_last_error=False)(("DhcpV6SetStatelessStoreParams", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'fServerLevel'),(1, 'SubnetAddress'),(1, 'FieldModified'),(1, 'Params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV6GetStatelessStoreParams():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_PARAMS_head)), use_last_error=False)(("DhcpV6GetStatelessStoreParams", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'fServerLevel'),(1, 'SubnetAddress'),(1, 'Params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV6GetStatelessStatistics():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_STATS_head)), use_last_error=False)(("DhcpV6GetStatelessStatistics", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'StatelessStats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4CreateClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head), use_last_error=False)(("DhcpV4CreateClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4EnumSubnetClients():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpV4EnumSubnetClients", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4GetClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head)), use_last_error=False)(("DhcpV4GetClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SearchInfo'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV6CreateClientInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head), use_last_error=False)(("DhcpV6CreateClientInfo", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4GetFreeIPAddress():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head)), use_last_error=False)(("DhcpV4GetFreeIPAddress", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeId'),(1, 'StartIP'),(1, 'EndIP'),(1, 'NumFreeAddrReq'),(1, 'IPAddrList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV6GetFreeIPAddress():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_IP_ARRAY_head)), use_last_error=False)(("DhcpV6GetFreeIPAddress", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ScopeId'),(1, 'StartIP'),(1, 'EndIP'),(1, 'NumFreeAddrReq'),(1, 'IPAddrList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4CreateClientInfoEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head), use_last_error=False)(("DhcpV4CreateClientInfoEx", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4EnumSubnetClientsEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpV4EnumSubnetClientsEx", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SubnetAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'ClientInfo'),(1, 'ClientsRead'),(1, 'ClientsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4GetClientInfoEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head),POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head)), use_last_error=False)(("DhcpV4GetClientInfoEx", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'SearchInfo'),(1, 'ClientInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4CreatePolicyEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head), use_last_error=False)(("DhcpV4CreatePolicyEx", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'PolicyEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4GetPolicyEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)), use_last_error=False)(("DhcpV4GetPolicyEx", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'GlobalPolicy'),(1, 'SubnetAddress'),(1, 'PolicyName'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4SetPolicyEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head), use_last_error=False)(("DhcpV4SetPolicyEx", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'FieldsModified'),(1, 'GlobalPolicy'),(1, 'SubnetAddress'),(1, 'PolicyName'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DhcpV4EnumPoliciesEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32,win32more.Foundation.BOOL,UInt32,POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_ARRAY_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("DhcpV4EnumPoliciesEx", windll["DHCPSAPI"]), ((1, 'ServerIpAddress'),(1, 'ResumeHandle'),(1, 'PreferredMaximum'),(1, 'GlobalPolicy'),(1, 'SubnetAddress'),(1, 'EnumInfo'),(1, 'ElementsRead'),(1, 'ElementsTotal'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "OPTION_PAD",
    "OPTION_SUBNET_MASK",
    "OPTION_TIME_OFFSET",
    "OPTION_ROUTER_ADDRESS",
    "OPTION_TIME_SERVERS",
    "OPTION_IEN116_NAME_SERVERS",
    "OPTION_DOMAIN_NAME_SERVERS",
    "OPTION_LOG_SERVERS",
    "OPTION_COOKIE_SERVERS",
    "OPTION_LPR_SERVERS",
    "OPTION_IMPRESS_SERVERS",
    "OPTION_RLP_SERVERS",
    "OPTION_HOST_NAME",
    "OPTION_BOOT_FILE_SIZE",
    "OPTION_MERIT_DUMP_FILE",
    "OPTION_DOMAIN_NAME",
    "OPTION_SWAP_SERVER",
    "OPTION_ROOT_DISK",
    "OPTION_EXTENSIONS_PATH",
    "OPTION_BE_A_ROUTER",
    "OPTION_NON_LOCAL_SOURCE_ROUTING",
    "OPTION_POLICY_FILTER_FOR_NLSR",
    "OPTION_MAX_REASSEMBLY_SIZE",
    "OPTION_DEFAULT_TTL",
    "OPTION_PMTU_AGING_TIMEOUT",
    "OPTION_PMTU_PLATEAU_TABLE",
    "OPTION_MTU",
    "OPTION_ALL_SUBNETS_MTU",
    "OPTION_BROADCAST_ADDRESS",
    "OPTION_PERFORM_MASK_DISCOVERY",
    "OPTION_BE_A_MASK_SUPPLIER",
    "OPTION_PERFORM_ROUTER_DISCOVERY",
    "OPTION_ROUTER_SOLICITATION_ADDR",
    "OPTION_STATIC_ROUTES",
    "OPTION_TRAILERS",
    "OPTION_ARP_CACHE_TIMEOUT",
    "OPTION_ETHERNET_ENCAPSULATION",
    "OPTION_TTL",
    "OPTION_KEEP_ALIVE_INTERVAL",
    "OPTION_KEEP_ALIVE_DATA_SIZE",
    "OPTION_NETWORK_INFO_SERVICE_DOM",
    "OPTION_NETWORK_INFO_SERVERS",
    "OPTION_NETWORK_TIME_SERVERS",
    "OPTION_VENDOR_SPEC_INFO",
    "OPTION_NETBIOS_NAME_SERVER",
    "OPTION_NETBIOS_DATAGRAM_SERVER",
    "OPTION_NETBIOS_NODE_TYPE",
    "OPTION_NETBIOS_SCOPE_OPTION",
    "OPTION_XWINDOW_FONT_SERVER",
    "OPTION_XWINDOW_DISPLAY_MANAGER",
    "OPTION_REQUESTED_ADDRESS",
    "OPTION_LEASE_TIME",
    "OPTION_OK_TO_OVERLAY",
    "OPTION_MESSAGE_TYPE",
    "OPTION_SERVER_IDENTIFIER",
    "OPTION_PARAMETER_REQUEST_LIST",
    "OPTION_MESSAGE",
    "OPTION_MESSAGE_LENGTH",
    "OPTION_RENEWAL_TIME",
    "OPTION_REBIND_TIME",
    "OPTION_CLIENT_CLASS_INFO",
    "OPTION_CLIENT_ID",
    "OPTION_TFTP_SERVER_NAME",
    "OPTION_BOOTFILE_NAME",
    "OPTION_MSFT_IE_PROXY",
    "OPTION_END",
    "DHCPCAPI_REQUEST_PERSISTENT",
    "DHCPCAPI_REQUEST_SYNCHRONOUS",
    "DHCPCAPI_REQUEST_ASYNCHRONOUS",
    "DHCPCAPI_REQUEST_CANCEL",
    "DHCPCAPI_REQUEST_MASK",
    "DHCPCAPI_REGISTER_HANDLE_EVENT",
    "DHCPCAPI_DEREGISTER_HANDLE_EVENT",
    "ERROR_DHCP_REGISTRY_INIT_FAILED",
    "ERROR_DHCP_DATABASE_INIT_FAILED",
    "ERROR_DHCP_RPC_INIT_FAILED",
    "ERROR_DHCP_NETWORK_INIT_FAILED",
    "ERROR_DHCP_SUBNET_EXITS",
    "ERROR_DHCP_SUBNET_NOT_PRESENT",
    "ERROR_DHCP_PRIMARY_NOT_FOUND",
    "ERROR_DHCP_ELEMENT_CANT_REMOVE",
    "ERROR_DHCP_OPTION_EXITS",
    "ERROR_DHCP_OPTION_NOT_PRESENT",
    "ERROR_DHCP_ADDRESS_NOT_AVAILABLE",
    "ERROR_DHCP_RANGE_FULL",
    "ERROR_DHCP_JET_ERROR",
    "ERROR_DHCP_CLIENT_EXISTS",
    "ERROR_DHCP_INVALID_DHCP_MESSAGE",
    "ERROR_DHCP_INVALID_DHCP_CLIENT",
    "ERROR_DHCP_SERVICE_PAUSED",
    "ERROR_DHCP_NOT_RESERVED_CLIENT",
    "ERROR_DHCP_RESERVED_CLIENT",
    "ERROR_DHCP_RANGE_TOO_SMALL",
    "ERROR_DHCP_IPRANGE_EXITS",
    "ERROR_DHCP_RESERVEDIP_EXITS",
    "ERROR_DHCP_INVALID_RANGE",
    "ERROR_DHCP_RANGE_EXTENDED",
    "ERROR_EXTEND_TOO_SMALL",
    "WARNING_EXTENDED_LESS",
    "ERROR_DHCP_JET_CONV_REQUIRED",
    "ERROR_SERVER_INVALID_BOOT_FILE_TABLE",
    "ERROR_SERVER_UNKNOWN_BOOT_FILE_NAME",
    "ERROR_DHCP_SUPER_SCOPE_NAME_TOO_LONG",
    "ERROR_DHCP_IP_ADDRESS_IN_USE",
    "ERROR_DHCP_LOG_FILE_PATH_TOO_LONG",
    "ERROR_DHCP_UNSUPPORTED_CLIENT",
    "ERROR_DHCP_JET97_CONV_REQUIRED",
    "ERROR_DHCP_ROGUE_INIT_FAILED",
    "ERROR_DHCP_ROGUE_SAMSHUTDOWN",
    "ERROR_DHCP_ROGUE_NOT_AUTHORIZED",
    "ERROR_DHCP_ROGUE_DS_UNREACHABLE",
    "ERROR_DHCP_ROGUE_DS_CONFLICT",
    "ERROR_DHCP_ROGUE_NOT_OUR_ENTERPRISE",
    "ERROR_DHCP_ROGUE_STANDALONE_IN_DS",
    "ERROR_DHCP_CLASS_NOT_FOUND",
    "ERROR_DHCP_CLASS_ALREADY_EXISTS",
    "ERROR_DHCP_SCOPE_NAME_TOO_LONG",
    "ERROR_DHCP_DEFAULT_SCOPE_EXITS",
    "ERROR_DHCP_CANT_CHANGE_ATTRIBUTE",
    "ERROR_DHCP_IPRANGE_CONV_ILLEGAL",
    "ERROR_DHCP_NETWORK_CHANGED",
    "ERROR_DHCP_CANNOT_MODIFY_BINDINGS",
    "ERROR_DHCP_SUBNET_EXISTS",
    "ERROR_DHCP_MSCOPE_EXISTS",
    "ERROR_MSCOPE_RANGE_TOO_SMALL",
    "ERROR_DHCP_EXEMPTION_EXISTS",
    "ERROR_DHCP_EXEMPTION_NOT_PRESENT",
    "ERROR_DHCP_INVALID_PARAMETER_OPTION32",
    "ERROR_DDS_NO_DS_AVAILABLE",
    "ERROR_DDS_NO_DHCP_ROOT",
    "ERROR_DDS_UNEXPECTED_ERROR",
    "ERROR_DDS_TOO_MANY_ERRORS",
    "ERROR_DDS_DHCP_SERVER_NOT_FOUND",
    "ERROR_DDS_OPTION_ALREADY_EXISTS",
    "ERROR_DDS_OPTION_DOES_NOT_EXIST",
    "ERROR_DDS_CLASS_EXISTS",
    "ERROR_DDS_CLASS_DOES_NOT_EXIST",
    "ERROR_DDS_SERVER_ALREADY_EXISTS",
    "ERROR_DDS_SERVER_DOES_NOT_EXIST",
    "ERROR_DDS_SERVER_ADDRESS_MISMATCH",
    "ERROR_DDS_SUBNET_EXISTS",
    "ERROR_DDS_SUBNET_HAS_DIFF_SSCOPE",
    "ERROR_DDS_SUBNET_NOT_PRESENT",
    "ERROR_DDS_RESERVATION_NOT_PRESENT",
    "ERROR_DDS_RESERVATION_CONFLICT",
    "ERROR_DDS_POSSIBLE_RANGE_CONFLICT",
    "ERROR_DDS_RANGE_DOES_NOT_EXIST",
    "ERROR_DHCP_DELETE_BUILTIN_CLASS",
    "ERROR_DHCP_INVALID_SUBNET_PREFIX",
    "ERROR_DHCP_INVALID_DELAY",
    "ERROR_DHCP_LINKLAYER_ADDRESS_EXISTS",
    "ERROR_DHCP_LINKLAYER_ADDRESS_RESERVATION_EXISTS",
    "ERROR_DHCP_LINKLAYER_ADDRESS_DOES_NOT_EXIST",
    "ERROR_DHCP_HARDWARE_ADDRESS_TYPE_ALREADY_EXEMPT",
    "ERROR_DHCP_UNDEFINED_HARDWARE_ADDRESS_TYPE",
    "ERROR_DHCP_OPTION_TYPE_MISMATCH",
    "ERROR_DHCP_POLICY_BAD_PARENT_EXPR",
    "ERROR_DHCP_POLICY_EXISTS",
    "ERROR_DHCP_POLICY_RANGE_EXISTS",
    "ERROR_DHCP_POLICY_RANGE_BAD",
    "ERROR_DHCP_RANGE_INVALID_IN_SERVER_POLICY",
    "ERROR_DHCP_INVALID_POLICY_EXPRESSION",
    "ERROR_DHCP_INVALID_PROCESSING_ORDER",
    "ERROR_DHCP_POLICY_NOT_FOUND",
    "ERROR_SCOPE_RANGE_POLICY_RANGE_CONFLICT",
    "ERROR_DHCP_FO_SCOPE_ALREADY_IN_RELATIONSHIP",
    "ERROR_DHCP_FO_RELATIONSHIP_EXISTS",
    "ERROR_DHCP_FO_RELATIONSHIP_DOES_NOT_EXIST",
    "ERROR_DHCP_FO_SCOPE_NOT_IN_RELATIONSHIP",
    "ERROR_DHCP_FO_RELATION_IS_SECONDARY",
    "ERROR_DHCP_FO_NOT_SUPPORTED",
    "ERROR_DHCP_FO_TIME_OUT_OF_SYNC",
    "ERROR_DHCP_FO_STATE_NOT_NORMAL",
    "ERROR_DHCP_NO_ADMIN_PERMISSION",
    "ERROR_DHCP_SERVER_NOT_REACHABLE",
    "ERROR_DHCP_SERVER_NOT_RUNNING",
    "ERROR_DHCP_SERVER_NAME_NOT_RESOLVED",
    "ERROR_DHCP_FO_RELATIONSHIP_NAME_TOO_LONG",
    "ERROR_DHCP_REACHED_END_OF_SELECTION",
    "ERROR_DHCP_FO_ADDSCOPE_LEASES_NOT_SYNCED",
    "ERROR_DHCP_FO_MAX_RELATIONSHIPS",
    "ERROR_DHCP_FO_IPRANGE_TYPE_CONV_ILLEGAL",
    "ERROR_DHCP_FO_MAX_ADD_SCOPES",
    "ERROR_DHCP_FO_BOOT_NOT_SUPPORTED",
    "ERROR_DHCP_FO_RANGE_PART_OF_REL",
    "ERROR_DHCP_FO_SCOPE_SYNC_IN_PROGRESS",
    "ERROR_DHCP_FO_FEATURE_NOT_SUPPORTED",
    "ERROR_DHCP_POLICY_FQDN_RANGE_UNSUPPORTED",
    "ERROR_DHCP_POLICY_FQDN_OPTION_UNSUPPORTED",
    "ERROR_DHCP_POLICY_EDIT_FQDN_UNSUPPORTED",
    "ERROR_DHCP_NAP_NOT_SUPPORTED",
    "ERROR_LAST_DHCP_SERVER_ERROR",
    "DHCP_SUBNET_INFO_VQ_FLAG_QUARANTINE",
    "MAX_PATTERN_LENGTH",
    "MAC_ADDRESS_LENGTH",
    "HWTYPE_ETHERNET_10MB",
    "FILTER_STATUS_NONE",
    "FILTER_STATUS_FULL_MATCH_IN_ALLOW_LIST",
    "FILTER_STATUS_FULL_MATCH_IN_DENY_LIST",
    "FILTER_STATUS_WILDCARD_MATCH_IN_ALLOW_LIST",
    "FILTER_STATUS_WILDCARD_MATCH_IN_DENY_LIST",
    "Set_APIProtocolSupport",
    "Set_DatabaseName",
    "Set_DatabasePath",
    "Set_BackupPath",
    "Set_BackupInterval",
    "Set_DatabaseLoggingFlag",
    "Set_RestoreFlag",
    "Set_DatabaseCleanupInterval",
    "Set_DebugFlag",
    "Set_PingRetries",
    "Set_BootFileTable",
    "Set_AuditLogState",
    "Set_QuarantineON",
    "Set_QuarantineDefFail",
    "CLIENT_TYPE_UNSPECIFIED",
    "CLIENT_TYPE_DHCP",
    "CLIENT_TYPE_BOOTP",
    "CLIENT_TYPE_RESERVATION_FLAG",
    "CLIENT_TYPE_NONE",
    "Set_UnicastFlag",
    "Set_RapidCommitFlag",
    "Set_PreferredLifetime",
    "Set_ValidLifetime",
    "Set_T1",
    "Set_T2",
    "Set_PreferredLifetimeIATA",
    "Set_ValidLifetimeIATA",
    "V5_ADDRESS_STATE_OFFERED",
    "V5_ADDRESS_STATE_ACTIVE",
    "V5_ADDRESS_STATE_DECLINED",
    "V5_ADDRESS_STATE_DOOM",
    "V5_ADDRESS_BIT_DELETED",
    "V5_ADDRESS_BIT_UNREGISTERED",
    "V5_ADDRESS_BIT_BOTH_REC",
    "V5_ADDRESS_EX_BIT_DISABLE_PTR_RR",
    "DNS_FLAG_ENABLED",
    "DNS_FLAG_UPDATE_DOWNLEVEL",
    "DNS_FLAG_CLEANUP_EXPIRED",
    "DNS_FLAG_UPDATE_BOTH_ALWAYS",
    "DNS_FLAG_UPDATE_DHCID",
    "DNS_FLAG_DISABLE_PTR_UPDATE",
    "DNS_FLAG_HAS_DNS_SUFFIX",
    "DHCP_OPT_ENUM_IGNORE_VENDOR",
    "DHCP_OPT_ENUM_USE_CLASSNAME",
    "DHCP_FLAGS_DONT_ACCESS_DS",
    "DHCP_FLAGS_DONT_DO_RPC",
    "DHCP_FLAGS_OPTION_IS_VENDOR",
    "DHCP_ATTRIB_BOOL_IS_ROGUE",
    "DHCP_ATTRIB_BOOL_IS_DYNBOOTP",
    "DHCP_ATTRIB_BOOL_IS_PART_OF_DSDC",
    "DHCP_ATTRIB_BOOL_IS_BINDING_AWARE",
    "DHCP_ATTRIB_BOOL_IS_ADMIN",
    "DHCP_ATTRIB_ULONG_RESTORE_STATUS",
    "DHCP_ATTRIB_TYPE_BOOL",
    "DHCP_ATTRIB_TYPE_ULONG",
    "DHCP_ENDPOINT_FLAG_CANT_MODIFY",
    "QUARANTIN_OPTION_BASE",
    "QUARANTINE_SCOPE_QUARPROFILE_OPTION",
    "QUARANTINE_CONFIG_OPTION",
    "ADDRESS_TYPE_IANA",
    "ADDRESS_TYPE_IATA",
    "DHCP_MIN_DELAY",
    "DHCP_MAX_DELAY",
    "DHCP_FAILOVER_DELETE_SCOPES",
    "DHCP_FAILOVER_MAX_NUM_ADD_SCOPES",
    "DHCP_FAILOVER_MAX_NUM_REL",
    "MCLT",
    "SAFEPERIOD",
    "CHANGESTATE",
    "PERCENTAGE",
    "MODE",
    "PREVSTATE",
    "SHAREDSECRET",
    "DHCP_CONTROL_START",
    "DHCP_CONTROL_STOP",
    "DHCP_CONTROL_PAUSE",
    "DHCP_CONTROL_CONTINUE",
    "DHCP_DROP_DUPLICATE",
    "DHCP_DROP_NOMEM",
    "DHCP_DROP_INTERNAL_ERROR",
    "DHCP_DROP_TIMEOUT",
    "DHCP_DROP_UNAUTH",
    "DHCP_DROP_PAUSED",
    "DHCP_DROP_NO_SUBNETS",
    "DHCP_DROP_INVALID",
    "DHCP_DROP_WRONG_SERVER",
    "DHCP_DROP_NOADDRESS",
    "DHCP_DROP_PROCESSED",
    "DHCP_DROP_GEN_FAILURE",
    "DHCP_SEND_PACKET",
    "DHCP_PROB_CONFLICT",
    "DHCP_PROB_DECLINE",
    "DHCP_PROB_RELEASE",
    "DHCP_PROB_NACKED",
    "DHCP_GIVE_ADDRESS_NEW",
    "DHCP_GIVE_ADDRESS_OLD",
    "DHCP_CLIENT_BOOTP",
    "DHCP_CLIENT_DHCP",
    "DHCPV6_OPTION_CLIENTID",
    "DHCPV6_OPTION_SERVERID",
    "DHCPV6_OPTION_IA_NA",
    "DHCPV6_OPTION_IA_TA",
    "DHCPV6_OPTION_ORO",
    "DHCPV6_OPTION_PREFERENCE",
    "DHCPV6_OPTION_UNICAST",
    "DHCPV6_OPTION_RAPID_COMMIT",
    "DHCPV6_OPTION_USER_CLASS",
    "DHCPV6_OPTION_VENDOR_CLASS",
    "DHCPV6_OPTION_VENDOR_OPTS",
    "DHCPV6_OPTION_RECONF_MSG",
    "DHCPV6_OPTION_SIP_SERVERS_NAMES",
    "DHCPV6_OPTION_SIP_SERVERS_ADDRS",
    "DHCPV6_OPTION_DNS_SERVERS",
    "DHCPV6_OPTION_DOMAIN_LIST",
    "DHCPV6_OPTION_IA_PD",
    "DHCPV6_OPTION_NIS_SERVERS",
    "DHCPV6_OPTION_NISP_SERVERS",
    "DHCPV6_OPTION_NIS_DOMAIN_NAME",
    "DHCPV6_OPTION_NISP_DOMAIN_NAME",
    "DHCPV6CAPI_PARAMS",
    "DHCPV6CAPI_PARAMS_ARRAY",
    "DHCPV6CAPI_CLASSID",
    "StatusCode",
    "STATUS_NO_ERROR",
    "STATUS_UNSPECIFIED_FAILURE",
    "STATUS_NO_BINDING",
    "STATUS_NOPREFIX_AVAIL",
    "DHCPV6Prefix",
    "DHCPV6PrefixLeaseInformation",
    "DHCPAPI_PARAMS",
    "DHCPCAPI_PARAMS_ARRAY",
    "DHCPCAPI_CLASSID",
    "DHCP_SERVER_OPTIONS",
    "LPDHCP_CONTROL",
    "LPDHCP_NEWPKT",
    "LPDHCP_DROP_SEND",
    "LPDHCP_PROB",
    "LPDHCP_GIVE_ADDRESS",
    "LPDHCP_HANDLE_OPTIONS",
    "LPDHCP_DELETE_CLIENT",
    "DHCP_CALLOUT_TABLE",
    "LPDHCP_ENTRY_POINT_FUNC",
    "DATE_TIME",
    "DHCP_IP_RANGE",
    "DHCP_BINARY_DATA",
    "DHCP_HOST_INFO",
    "DHCP_FORCE_FLAG",
    "DHCP_FORCE_FLAG_DhcpFullForce",
    "DHCP_FORCE_FLAG_DhcpNoForce",
    "DHCP_FORCE_FLAG_DhcpFailoverForce",
    "DWORD_DWORD",
    "DHCP_SUBNET_STATE",
    "DHCP_SUBNET_STATE_DhcpSubnetEnabled",
    "DHCP_SUBNET_STATE_DhcpSubnetDisabled",
    "DHCP_SUBNET_STATE_DhcpSubnetEnabledSwitched",
    "DHCP_SUBNET_STATE_DhcpSubnetDisabledSwitched",
    "DHCP_SUBNET_STATE_DhcpSubnetInvalidState",
    "DHCP_SUBNET_INFO",
    "DHCP_SUBNET_INFO_VQ",
    "DHCP_IP_ARRAY",
    "DHCP_IP_CLUSTER",
    "DHCP_IP_RESERVATION",
    "DHCP_SUBNET_ELEMENT_TYPE",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRanges",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpSecondaryHosts",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpReservedIps",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpExcludedIpRanges",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpUsedClusters",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpOnly",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpBootp",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesBootpOnly",
    "DHCP_SUBNET_ELEMENT_DATA",
    "DHCP_SUBNET_ELEMENT_UNION",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY",
    "DHCP_IPV6_ADDRESS",
    "DHCP_FILTER_LIST_TYPE",
    "DHCP_FILTER_LIST_TYPE_Deny",
    "DHCP_FILTER_LIST_TYPE_Allow",
    "DHCP_ADDR_PATTERN",
    "DHCP_FILTER_ADD_INFO",
    "DHCP_FILTER_GLOBAL_INFO",
    "DHCP_FILTER_RECORD",
    "DHCP_FILTER_ENUM_INFO",
    "DHCP_OPTION_DATA_TYPE",
    "DHCP_OPTION_DATA_TYPE_DhcpByteOption",
    "DHCP_OPTION_DATA_TYPE_DhcpWordOption",
    "DHCP_OPTION_DATA_TYPE_DhcpDWordOption",
    "DHCP_OPTION_DATA_TYPE_DhcpDWordDWordOption",
    "DHCP_OPTION_DATA_TYPE_DhcpIpAddressOption",
    "DHCP_OPTION_DATA_TYPE_DhcpStringDataOption",
    "DHCP_OPTION_DATA_TYPE_DhcpBinaryDataOption",
    "DHCP_OPTION_DATA_TYPE_DhcpEncapsulatedDataOption",
    "DHCP_OPTION_DATA_TYPE_DhcpIpv6AddressOption",
    "DHCP_OPTION_DATA_ELEMENT",
    "DHCP_OPTION_ELEMENT_UNION",
    "DHCP_OPTION_DATA",
    "DHCP_OPTION_TYPE",
    "DHCP_OPTION_TYPE_DhcpUnaryElementTypeOption",
    "DHCP_OPTION_TYPE_DhcpArrayTypeOption",
    "DHCP_OPTION",
    "DHCP_OPTION_ARRAY",
    "DHCP_OPTION_VALUE",
    "DHCP_OPTION_VALUE_ARRAY",
    "DHCP_OPTION_SCOPE_TYPE",
    "DHCP_OPTION_SCOPE_TYPE_DhcpDefaultOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpGlobalOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpSubnetOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpReservedOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpMScopeOptions",
    "DHCP_RESERVED_SCOPE",
    "DHCP_OPTION_SCOPE_INFO",
    "DHCP_OPTION_SCOPE_TYPE6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpDefaultOptions6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpScopeOptions6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpReservedOptions6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpGlobalOptions6",
    "DHCP_RESERVED_SCOPE6",
    "DHCP_OPTION_SCOPE_INFO6",
    "DHCP_OPTION_SCOPE_UNION6",
    "DHCP_OPTION_LIST",
    "DHCP_CLIENT_INFO",
    "DHCP_CLIENT_INFO_ARRAY",
    "QuarantineStatus",
    "NOQUARANTINE",
    "RESTRICTEDACCESS",
    "DROPPACKET",
    "PROBATION",
    "EXEMPT",
    "DEFAULTQUARSETTING",
    "NOQUARINFO",
    "DHCP_CLIENT_INFO_VQ",
    "DHCP_CLIENT_INFO_ARRAY_VQ",
    "DHCP_CLIENT_FILTER_STATUS_INFO",
    "DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY",
    "DHCP_CLIENT_INFO_PB",
    "DHCP_CLIENT_INFO_PB_ARRAY",
    "DHCP_SEARCH_INFO_TYPE",
    "DHCP_SEARCH_INFO_TYPE_DhcpClientIpAddress",
    "DHCP_SEARCH_INFO_TYPE_DhcpClientHardwareAddress",
    "DHCP_SEARCH_INFO_TYPE_DhcpClientName",
    "DHCP_SEARCH_INFO",
    "DHCP_CLIENT_SEARCH_UNION",
    "DHCP_PROPERTY_TYPE",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeByte",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeWord",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeDword",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeString",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeBinary",
    "DHCP_PROPERTY_ID",
    "DHCP_PROPERTY_ID_DhcpPropIdPolicyDnsSuffix",
    "DHCP_PROPERTY_ID_DhcpPropIdClientAddressStateEx",
    "DHCP_PROPERTY",
    "DHCP_PROPERTY_ARRAY",
    "DHCP_CLIENT_INFO_EX",
    "DHCP_CLIENT_INFO_EX_ARRAY",
    "SCOPE_MIB_INFO",
    "DHCP_MIB_INFO",
    "SCOPE_MIB_INFO_VQ",
    "DHCP_MIB_INFO_VQ",
    "SCOPE_MIB_INFO_V5",
    "DHCP_MIB_INFO_V5",
    "DHCP_SERVER_CONFIG_INFO",
    "DHCP_SCAN_FLAG",
    "DHCP_SCAN_FLAG_DhcpRegistryFix",
    "DHCP_SCAN_FLAG_DhcpDatabaseFix",
    "DHCP_SCAN_ITEM",
    "DHCP_SCAN_LIST",
    "DHCP_CLASS_INFO",
    "DHCP_CLASS_INFO_ARRAY",
    "DHCP_CLASS_INFO_V6",
    "DHCP_CLASS_INFO_ARRAY_V6",
    "DHCP_SERVER_SPECIFIC_STRINGS",
    "DHCP_IP_RESERVATION_V4",
    "DHCP_IP_RESERVATION_INFO",
    "DHCP_RESERVATION_INFO_ARRAY",
    "DHCP_SUBNET_ELEMENT_DATA_V4",
    "DHCP_SUBNET_ELEMENT_UNION_V4",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4",
    "DHCP_CLIENT_INFO_V4",
    "DHCP_CLIENT_INFO_ARRAY_V4",
    "DHCP_SERVER_CONFIG_INFO_V4",
    "DHCP_SERVER_CONFIG_INFO_VQ",
    "DHCP_SERVER_CONFIG_INFO_V6",
    "DHCP_SUPER_SCOPE_TABLE_ENTRY",
    "DHCP_SUPER_SCOPE_TABLE",
    "DHCP_CLIENT_INFO_V5",
    "DHCP_CLIENT_INFO_ARRAY_V5",
    "DHCP_ALL_OPTIONS",
    "DHCP_ALL_OPTION_VALUES",
    "DHCP_ALL_OPTION_VALUES_PB",
    "DHCPDS_SERVER",
    "DHCPDS_SERVERS",
    "DHCP_ATTRIB",
    "DHCP_ATTRIB_ARRAY",
    "DHCP_BOOTP_IP_RANGE",
    "DHCP_SUBNET_ELEMENT_DATA_V5",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5",
    "DHCP_PERF_STATS",
    "DHCP_BIND_ELEMENT",
    "DHCP_BIND_ELEMENT_ARRAY",
    "DHCPV6_BIND_ELEMENT",
    "DHCPV6_BIND_ELEMENT_ARRAY",
    "DHCP_IP_RANGE_V6",
    "DHCP_HOST_INFO_V6",
    "DHCP_SUBNET_INFO_V6",
    "SCOPE_MIB_INFO_V6",
    "DHCP_MIB_INFO_V6",
    "DHCP_IP_RESERVATION_V6",
    "DHCP_SUBNET_ELEMENT_TYPE_V6",
    "DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6IpRanges",
    "DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ReservedIps",
    "DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ExcludedIpRanges",
    "DHCP_SUBNET_ELEMENT_DATA_V6",
    "DHCP_SUBNET_ELEMENT_UNION_V6",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6",
    "DHCP_CLIENT_INFO_V6",
    "DHCPV6_IP_ARRAY",
    "DHCP_CLIENT_INFO_ARRAY_V6",
    "DHCP_SEARCH_INFO_TYPE_V6",
    "DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientIpAddress",
    "DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientDUID",
    "DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientName",
    "DHCP_SEARCH_INFO_V6",
    "DHCP_POL_ATTR_TYPE",
    "DHCP_POL_ATTR_TYPE_DhcpAttrHWAddr",
    "DHCP_POL_ATTR_TYPE_DhcpAttrOption",
    "DHCP_POL_ATTR_TYPE_DhcpAttrSubOption",
    "DHCP_POL_ATTR_TYPE_DhcpAttrFqdn",
    "DHCP_POL_ATTR_TYPE_DhcpAttrFqdnSingleLabel",
    "DHCP_POL_COMPARATOR",
    "DHCP_POL_COMPARATOR_DhcpCompEqual",
    "DHCP_POL_COMPARATOR_DhcpCompNotEqual",
    "DHCP_POL_COMPARATOR_DhcpCompBeginsWith",
    "DHCP_POL_COMPARATOR_DhcpCompNotBeginWith",
    "DHCP_POL_COMPARATOR_DhcpCompEndsWith",
    "DHCP_POL_COMPARATOR_DhcpCompNotEndWith",
    "DHCP_POL_LOGIC_OPER",
    "DHCP_POL_LOGIC_OPER_DhcpLogicalOr",
    "DHCP_POL_LOGIC_OPER_DhcpLogicalAnd",
    "DHCP_POLICY_FIELDS_TO_UPDATE",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyName",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyOrder",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyExpr",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyRanges",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDescr",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyStatus",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDnsSuffix",
    "DHCP_POL_COND",
    "DHCP_POL_COND_ARRAY",
    "DHCP_POL_EXPR",
    "DHCP_POL_EXPR_ARRAY",
    "DHCP_IP_RANGE_ARRAY",
    "DHCP_POLICY",
    "DHCP_POLICY_ARRAY",
    "DHCP_POLICY_EX",
    "DHCP_POLICY_EX_ARRAY",
    "DHCPV6_STATELESS_PARAM_TYPE",
    "DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessPurgeInterval",
    "DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessStatus",
    "DHCPV6_STATELESS_PARAMS",
    "DHCPV6_STATELESS_SCOPE_STATS",
    "DHCPV6_STATELESS_STATS",
    "DHCP_FAILOVER_MODE",
    "DHCP_FAILOVER_MODE_LoadBalance",
    "DHCP_FAILOVER_MODE_HotStandby",
    "DHCP_FAILOVER_SERVER",
    "DHCP_FAILOVER_SERVER_PrimaryServer",
    "DHCP_FAILOVER_SERVER_SecondaryServer",
    "FSM_STATE",
    "NO_STATE",
    "INIT",
    "STARTUP",
    "NORMAL",
    "COMMUNICATION_INT",
    "PARTNER_DOWN",
    "POTENTIAL_CONFLICT",
    "CONFLICT_DONE",
    "RESOLUTION_INT",
    "RECOVER",
    "RECOVER_WAIT",
    "RECOVER_DONE",
    "PAUSED",
    "SHUTDOWN",
    "DHCP_FAILOVER_RELATIONSHIP",
    "DHCP_FAILOVER_RELATIONSHIP_ARRAY",
    "DHCPV4_FAILOVER_CLIENT_INFO",
    "DHCPV4_FAILOVER_CLIENT_INFO_ARRAY",
    "DHCPV4_FAILOVER_CLIENT_INFO_EX",
    "DHCP_FAILOVER_STATISTICS",
    "Dhcpv6CApiInitialize",
    "Dhcpv6CApiCleanup",
    "Dhcpv6RequestParams",
    "Dhcpv6RequestPrefix",
    "Dhcpv6RenewPrefix",
    "Dhcpv6ReleasePrefix",
    "DhcpCApiInitialize",
    "DhcpCApiCleanup",
    "DhcpRequestParams",
    "DhcpUndoRequestParams",
    "DhcpRegisterParamChange",
    "DhcpDeRegisterParamChange",
    "DhcpRemoveDNSRegistrations",
    "DhcpGetOriginalSubnetMask",
    "DhcpAddFilterV4",
    "DhcpDeleteFilterV4",
    "DhcpSetFilterV4",
    "DhcpGetFilterV4",
    "DhcpEnumFilterV4",
    "DhcpCreateSubnet",
    "DhcpSetSubnetInfo",
    "DhcpGetSubnetInfo",
    "DhcpEnumSubnets",
    "DhcpAddSubnetElement",
    "DhcpEnumSubnetElements",
    "DhcpRemoveSubnetElement",
    "DhcpDeleteSubnet",
    "DhcpCreateOption",
    "DhcpSetOptionInfo",
    "DhcpGetOptionInfo",
    "DhcpEnumOptions",
    "DhcpRemoveOption",
    "DhcpSetOptionValue",
    "DhcpSetOptionValues",
    "DhcpGetOptionValue",
    "DhcpEnumOptionValues",
    "DhcpRemoveOptionValue",
    "DhcpCreateClientInfoVQ",
    "DhcpSetClientInfoVQ",
    "DhcpGetClientInfoVQ",
    "DhcpEnumSubnetClientsVQ",
    "DhcpEnumSubnetClientsFilterStatusInfo",
    "DhcpCreateClientInfo",
    "DhcpSetClientInfo",
    "DhcpGetClientInfo",
    "DhcpDeleteClientInfo",
    "DhcpEnumSubnetClients",
    "DhcpGetClientOptions",
    "DhcpGetMibInfo",
    "DhcpServerSetConfig",
    "DhcpServerGetConfig",
    "DhcpScanDatabase",
    "DhcpRpcFreeMemory",
    "DhcpGetVersion",
    "DhcpAddSubnetElementV4",
    "DhcpEnumSubnetElementsV4",
    "DhcpRemoveSubnetElementV4",
    "DhcpCreateClientInfoV4",
    "DhcpSetClientInfoV4",
    "DhcpGetClientInfoV4",
    "DhcpEnumSubnetClientsV4",
    "DhcpServerSetConfigV4",
    "DhcpServerGetConfigV4",
    "DhcpSetSuperScopeV4",
    "DhcpDeleteSuperScopeV4",
    "DhcpGetSuperScopeInfoV4",
    "DhcpEnumSubnetClientsV5",
    "DhcpCreateOptionV5",
    "DhcpSetOptionInfoV5",
    "DhcpGetOptionInfoV5",
    "DhcpEnumOptionsV5",
    "DhcpRemoveOptionV5",
    "DhcpSetOptionValueV5",
    "DhcpSetOptionValuesV5",
    "DhcpGetOptionValueV5",
    "DhcpGetOptionValueV6",
    "DhcpEnumOptionValuesV5",
    "DhcpRemoveOptionValueV5",
    "DhcpCreateClass",
    "DhcpModifyClass",
    "DhcpDeleteClass",
    "DhcpGetClassInfo",
    "DhcpEnumClasses",
    "DhcpGetAllOptions",
    "DhcpGetAllOptionsV6",
    "DhcpGetAllOptionValues",
    "DhcpGetAllOptionValuesV6",
    "DhcpEnumServers",
    "DhcpAddServer",
    "DhcpDeleteServer",
    "DhcpGetServerBindingInfo",
    "DhcpSetServerBindingInfo",
    "DhcpAddSubnetElementV5",
    "DhcpEnumSubnetElementsV5",
    "DhcpRemoveSubnetElementV5",
    "DhcpV4EnumSubnetReservations",
    "DhcpCreateOptionV6",
    "DhcpRemoveOptionV6",
    "DhcpEnumOptionsV6",
    "DhcpRemoveOptionValueV6",
    "DhcpGetOptionInfoV6",
    "DhcpSetOptionInfoV6",
    "DhcpSetOptionValueV6",
    "DhcpGetSubnetInfoVQ",
    "DhcpCreateSubnetVQ",
    "DhcpSetSubnetInfoVQ",
    "DhcpEnumOptionValuesV6",
    "DhcpDsInit",
    "DhcpDsCleanup",
    "DhcpSetThreadOptions",
    "DhcpGetThreadOptions",
    "DhcpServerQueryAttribute",
    "DhcpServerQueryAttributes",
    "DhcpServerRedoAuthorization",
    "DhcpAuditLogSetParams",
    "DhcpAuditLogGetParams",
    "DhcpServerQueryDnsRegCredentials",
    "DhcpServerSetDnsRegCredentials",
    "DhcpServerSetDnsRegCredentialsV5",
    "DhcpServerBackupDatabase",
    "DhcpServerRestoreDatabase",
    "DhcpServerSetConfigVQ",
    "DhcpServerGetConfigVQ",
    "DhcpGetServerSpecificStrings",
    "DhcpServerAuditlogParamsFree",
    "DhcpCreateSubnetV6",
    "DhcpDeleteSubnetV6",
    "DhcpEnumSubnetsV6",
    "DhcpAddSubnetElementV6",
    "DhcpRemoveSubnetElementV6",
    "DhcpEnumSubnetElementsV6",
    "DhcpGetSubnetInfoV6",
    "DhcpEnumSubnetClientsV6",
    "DhcpServerGetConfigV6",
    "DhcpServerSetConfigV6",
    "DhcpSetSubnetInfoV6",
    "DhcpGetMibInfoV6",
    "DhcpGetServerBindingInfoV6",
    "DhcpSetServerBindingInfoV6",
    "DhcpSetClientInfoV6",
    "DhcpGetClientInfoV6",
    "DhcpDeleteClientInfoV6",
    "DhcpCreateClassV6",
    "DhcpModifyClassV6",
    "DhcpDeleteClassV6",
    "DhcpEnumClassesV6",
    "DhcpSetSubnetDelayOffer",
    "DhcpGetSubnetDelayOffer",
    "DhcpGetMibInfoV5",
    "DhcpAddSecurityGroup",
    "DhcpV4GetOptionValue",
    "DhcpV4SetOptionValue",
    "DhcpV4SetOptionValues",
    "DhcpV4RemoveOptionValue",
    "DhcpV4GetAllOptionValues",
    "DhcpV4FailoverCreateRelationship",
    "DhcpV4FailoverSetRelationship",
    "DhcpV4FailoverDeleteRelationship",
    "DhcpV4FailoverGetRelationship",
    "DhcpV4FailoverEnumRelationship",
    "DhcpV4FailoverAddScopeToRelationship",
    "DhcpV4FailoverDeleteScopeFromRelationship",
    "DhcpV4FailoverGetScopeRelationship",
    "DhcpV4FailoverGetScopeStatistics",
    "DhcpV4FailoverGetClientInfo",
    "DhcpV4FailoverGetSystemTime",
    "DhcpV4FailoverGetAddressStatus",
    "DhcpV4FailoverTriggerAddrAllocation",
    "DhcpHlprCreateV4Policy",
    "DhcpHlprCreateV4PolicyEx",
    "DhcpHlprAddV4PolicyExpr",
    "DhcpHlprAddV4PolicyCondition",
    "DhcpHlprAddV4PolicyRange",
    "DhcpHlprResetV4PolicyExpr",
    "DhcpHlprModifyV4PolicyExpr",
    "DhcpHlprFreeV4Policy",
    "DhcpHlprFreeV4PolicyArray",
    "DhcpHlprFreeV4PolicyEx",
    "DhcpHlprFreeV4PolicyExArray",
    "DhcpHlprFreeV4DhcpProperty",
    "DhcpHlprFreeV4DhcpPropertyArray",
    "DhcpHlprFindV4DhcpProperty",
    "DhcpHlprIsV4PolicySingleUC",
    "DhcpV4QueryPolicyEnforcement",
    "DhcpV4SetPolicyEnforcement",
    "DhcpHlprIsV4PolicyWellFormed",
    "DhcpHlprIsV4PolicyValid",
    "DhcpV4CreatePolicy",
    "DhcpV4GetPolicy",
    "DhcpV4SetPolicy",
    "DhcpV4DeletePolicy",
    "DhcpV4EnumPolicies",
    "DhcpV4AddPolicyRange",
    "DhcpV4RemovePolicyRange",
    "DhcpV6SetStatelessStoreParams",
    "DhcpV6GetStatelessStoreParams",
    "DhcpV6GetStatelessStatistics",
    "DhcpV4CreateClientInfo",
    "DhcpV4EnumSubnetClients",
    "DhcpV4GetClientInfo",
    "DhcpV6CreateClientInfo",
    "DhcpV4GetFreeIPAddress",
    "DhcpV6GetFreeIPAddress",
    "DhcpV4CreateClientInfoEx",
    "DhcpV4EnumSubnetClientsEx",
    "DhcpV4GetClientInfoEx",
    "DhcpV4CreatePolicyEx",
    "DhcpV4GetPolicyEx",
    "DhcpV4SetPolicyEx",
    "DhcpV4EnumPoliciesEx",
]
