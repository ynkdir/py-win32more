from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.Dhcp
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
OPTION_PAD: UInt32 = 0
OPTION_SUBNET_MASK: UInt32 = 1
OPTION_TIME_OFFSET: UInt32 = 2
OPTION_ROUTER_ADDRESS: UInt32 = 3
OPTION_TIME_SERVERS: UInt32 = 4
OPTION_IEN116_NAME_SERVERS: UInt32 = 5
OPTION_DOMAIN_NAME_SERVERS: UInt32 = 6
OPTION_LOG_SERVERS: UInt32 = 7
OPTION_COOKIE_SERVERS: UInt32 = 8
OPTION_LPR_SERVERS: UInt32 = 9
OPTION_IMPRESS_SERVERS: UInt32 = 10
OPTION_RLP_SERVERS: UInt32 = 11
OPTION_HOST_NAME: UInt32 = 12
OPTION_BOOT_FILE_SIZE: UInt32 = 13
OPTION_MERIT_DUMP_FILE: UInt32 = 14
OPTION_DOMAIN_NAME: UInt32 = 15
OPTION_SWAP_SERVER: UInt32 = 16
OPTION_ROOT_DISK: UInt32 = 17
OPTION_EXTENSIONS_PATH: UInt32 = 18
OPTION_BE_A_ROUTER: UInt32 = 19
OPTION_NON_LOCAL_SOURCE_ROUTING: UInt32 = 20
OPTION_POLICY_FILTER_FOR_NLSR: UInt32 = 21
OPTION_MAX_REASSEMBLY_SIZE: UInt32 = 22
OPTION_DEFAULT_TTL: UInt32 = 23
OPTION_PMTU_AGING_TIMEOUT: UInt32 = 24
OPTION_PMTU_PLATEAU_TABLE: UInt32 = 25
OPTION_MTU: UInt32 = 26
OPTION_ALL_SUBNETS_MTU: UInt32 = 27
OPTION_BROADCAST_ADDRESS: UInt32 = 28
OPTION_PERFORM_MASK_DISCOVERY: UInt32 = 29
OPTION_BE_A_MASK_SUPPLIER: UInt32 = 30
OPTION_PERFORM_ROUTER_DISCOVERY: UInt32 = 31
OPTION_ROUTER_SOLICITATION_ADDR: UInt32 = 32
OPTION_STATIC_ROUTES: UInt32 = 33
OPTION_TRAILERS: UInt32 = 34
OPTION_ARP_CACHE_TIMEOUT: UInt32 = 35
OPTION_ETHERNET_ENCAPSULATION: UInt32 = 36
OPTION_TTL: UInt32 = 37
OPTION_KEEP_ALIVE_INTERVAL: UInt32 = 38
OPTION_KEEP_ALIVE_DATA_SIZE: UInt32 = 39
OPTION_NETWORK_INFO_SERVICE_DOM: UInt32 = 40
OPTION_NETWORK_INFO_SERVERS: UInt32 = 41
OPTION_NETWORK_TIME_SERVERS: UInt32 = 42
OPTION_VENDOR_SPEC_INFO: UInt32 = 43
OPTION_NETBIOS_NAME_SERVER: UInt32 = 44
OPTION_NETBIOS_DATAGRAM_SERVER: UInt32 = 45
OPTION_NETBIOS_NODE_TYPE: UInt32 = 46
OPTION_NETBIOS_SCOPE_OPTION: UInt32 = 47
OPTION_XWINDOW_FONT_SERVER: UInt32 = 48
OPTION_XWINDOW_DISPLAY_MANAGER: UInt32 = 49
OPTION_REQUESTED_ADDRESS: UInt32 = 50
OPTION_LEASE_TIME: UInt32 = 51
OPTION_OK_TO_OVERLAY: UInt32 = 52
OPTION_MESSAGE_TYPE: UInt32 = 53
OPTION_SERVER_IDENTIFIER: UInt32 = 54
OPTION_PARAMETER_REQUEST_LIST: UInt32 = 55
OPTION_MESSAGE: UInt32 = 56
OPTION_MESSAGE_LENGTH: UInt32 = 57
OPTION_RENEWAL_TIME: UInt32 = 58
OPTION_REBIND_TIME: UInt32 = 59
OPTION_CLIENT_CLASS_INFO: UInt32 = 60
OPTION_CLIENT_ID: UInt32 = 61
OPTION_TFTP_SERVER_NAME: UInt32 = 66
OPTION_BOOTFILE_NAME: UInt32 = 67
OPTION_MSFT_IE_PROXY: UInt32 = 252
OPTION_END: UInt32 = 255
DHCPCAPI_REQUEST_PERSISTENT: UInt32 = 1
DHCPCAPI_REQUEST_SYNCHRONOUS: UInt32 = 2
DHCPCAPI_REQUEST_ASYNCHRONOUS: UInt32 = 4
DHCPCAPI_REQUEST_CANCEL: UInt32 = 8
DHCPCAPI_REQUEST_MASK: UInt32 = 15
DHCPCAPI_REGISTER_HANDLE_EVENT: UInt32 = 1
DHCPCAPI_DEREGISTER_HANDLE_EVENT: UInt32 = 1
ERROR_DHCP_REGISTRY_INIT_FAILED: UInt32 = 20000
ERROR_DHCP_DATABASE_INIT_FAILED: UInt32 = 20001
ERROR_DHCP_RPC_INIT_FAILED: UInt32 = 20002
ERROR_DHCP_NETWORK_INIT_FAILED: UInt32 = 20003
ERROR_DHCP_SUBNET_EXITS: UInt32 = 20004
ERROR_DHCP_SUBNET_NOT_PRESENT: UInt32 = 20005
ERROR_DHCP_PRIMARY_NOT_FOUND: UInt32 = 20006
ERROR_DHCP_ELEMENT_CANT_REMOVE: UInt32 = 20007
ERROR_DHCP_OPTION_EXITS: UInt32 = 20009
ERROR_DHCP_OPTION_NOT_PRESENT: UInt32 = 20010
ERROR_DHCP_ADDRESS_NOT_AVAILABLE: UInt32 = 20011
ERROR_DHCP_RANGE_FULL: UInt32 = 20012
ERROR_DHCP_JET_ERROR: UInt32 = 20013
ERROR_DHCP_CLIENT_EXISTS: UInt32 = 20014
ERROR_DHCP_INVALID_DHCP_MESSAGE: UInt32 = 20015
ERROR_DHCP_INVALID_DHCP_CLIENT: UInt32 = 20016
ERROR_DHCP_SERVICE_PAUSED: UInt32 = 20017
ERROR_DHCP_NOT_RESERVED_CLIENT: UInt32 = 20018
ERROR_DHCP_RESERVED_CLIENT: UInt32 = 20019
ERROR_DHCP_RANGE_TOO_SMALL: UInt32 = 20020
ERROR_DHCP_IPRANGE_EXITS: UInt32 = 20021
ERROR_DHCP_RESERVEDIP_EXITS: UInt32 = 20022
ERROR_DHCP_INVALID_RANGE: UInt32 = 20023
ERROR_DHCP_RANGE_EXTENDED: UInt32 = 20024
ERROR_EXTEND_TOO_SMALL: UInt32 = 20025
WARNING_EXTENDED_LESS: Int32 = 20026
ERROR_DHCP_JET_CONV_REQUIRED: UInt32 = 20027
ERROR_SERVER_INVALID_BOOT_FILE_TABLE: UInt32 = 20028
ERROR_SERVER_UNKNOWN_BOOT_FILE_NAME: UInt32 = 20029
ERROR_DHCP_SUPER_SCOPE_NAME_TOO_LONG: UInt32 = 20030
ERROR_DHCP_IP_ADDRESS_IN_USE: UInt32 = 20032
ERROR_DHCP_LOG_FILE_PATH_TOO_LONG: UInt32 = 20033
ERROR_DHCP_UNSUPPORTED_CLIENT: UInt32 = 20034
ERROR_DHCP_JET97_CONV_REQUIRED: UInt32 = 20036
ERROR_DHCP_ROGUE_INIT_FAILED: UInt32 = 20037
ERROR_DHCP_ROGUE_SAMSHUTDOWN: UInt32 = 20038
ERROR_DHCP_ROGUE_NOT_AUTHORIZED: UInt32 = 20039
ERROR_DHCP_ROGUE_DS_UNREACHABLE: UInt32 = 20040
ERROR_DHCP_ROGUE_DS_CONFLICT: UInt32 = 20041
ERROR_DHCP_ROGUE_NOT_OUR_ENTERPRISE: UInt32 = 20042
ERROR_DHCP_ROGUE_STANDALONE_IN_DS: UInt32 = 20043
ERROR_DHCP_CLASS_NOT_FOUND: UInt32 = 20044
ERROR_DHCP_CLASS_ALREADY_EXISTS: UInt32 = 20045
ERROR_DHCP_SCOPE_NAME_TOO_LONG: UInt32 = 20046
ERROR_DHCP_DEFAULT_SCOPE_EXITS: UInt32 = 20047
ERROR_DHCP_CANT_CHANGE_ATTRIBUTE: UInt32 = 20048
ERROR_DHCP_IPRANGE_CONV_ILLEGAL: UInt32 = 20049
ERROR_DHCP_NETWORK_CHANGED: UInt32 = 20050
ERROR_DHCP_CANNOT_MODIFY_BINDINGS: UInt32 = 20051
ERROR_DHCP_SUBNET_EXISTS: UInt32 = 20052
ERROR_DHCP_MSCOPE_EXISTS: UInt32 = 20053
ERROR_MSCOPE_RANGE_TOO_SMALL: UInt32 = 20054
ERROR_DHCP_EXEMPTION_EXISTS: UInt32 = 20055
ERROR_DHCP_EXEMPTION_NOT_PRESENT: UInt32 = 20056
ERROR_DHCP_INVALID_PARAMETER_OPTION32: UInt32 = 20057
ERROR_DDS_NO_DS_AVAILABLE: UInt32 = 20070
ERROR_DDS_NO_DHCP_ROOT: UInt32 = 20071
ERROR_DDS_UNEXPECTED_ERROR: UInt32 = 20072
ERROR_DDS_TOO_MANY_ERRORS: UInt32 = 20073
ERROR_DDS_DHCP_SERVER_NOT_FOUND: UInt32 = 20074
ERROR_DDS_OPTION_ALREADY_EXISTS: UInt32 = 20075
ERROR_DDS_OPTION_DOES_NOT_EXIST: UInt32 = 20076
ERROR_DDS_CLASS_EXISTS: UInt32 = 20077
ERROR_DDS_CLASS_DOES_NOT_EXIST: UInt32 = 20078
ERROR_DDS_SERVER_ALREADY_EXISTS: UInt32 = 20079
ERROR_DDS_SERVER_DOES_NOT_EXIST: UInt32 = 20080
ERROR_DDS_SERVER_ADDRESS_MISMATCH: UInt32 = 20081
ERROR_DDS_SUBNET_EXISTS: UInt32 = 20082
ERROR_DDS_SUBNET_HAS_DIFF_SSCOPE: UInt32 = 20083
ERROR_DDS_SUBNET_NOT_PRESENT: UInt32 = 20084
ERROR_DDS_RESERVATION_NOT_PRESENT: UInt32 = 20085
ERROR_DDS_RESERVATION_CONFLICT: UInt32 = 20086
ERROR_DDS_POSSIBLE_RANGE_CONFLICT: UInt32 = 20087
ERROR_DDS_RANGE_DOES_NOT_EXIST: UInt32 = 20088
ERROR_DHCP_DELETE_BUILTIN_CLASS: UInt32 = 20089
ERROR_DHCP_INVALID_SUBNET_PREFIX: UInt32 = 20091
ERROR_DHCP_INVALID_DELAY: UInt32 = 20092
ERROR_DHCP_LINKLAYER_ADDRESS_EXISTS: UInt32 = 20093
ERROR_DHCP_LINKLAYER_ADDRESS_RESERVATION_EXISTS: UInt32 = 20094
ERROR_DHCP_LINKLAYER_ADDRESS_DOES_NOT_EXIST: UInt32 = 20095
ERROR_DHCP_HARDWARE_ADDRESS_TYPE_ALREADY_EXEMPT: UInt32 = 20101
ERROR_DHCP_UNDEFINED_HARDWARE_ADDRESS_TYPE: UInt32 = 20102
ERROR_DHCP_OPTION_TYPE_MISMATCH: UInt32 = 20103
ERROR_DHCP_POLICY_BAD_PARENT_EXPR: UInt32 = 20104
ERROR_DHCP_POLICY_EXISTS: UInt32 = 20105
ERROR_DHCP_POLICY_RANGE_EXISTS: UInt32 = 20106
ERROR_DHCP_POLICY_RANGE_BAD: UInt32 = 20107
ERROR_DHCP_RANGE_INVALID_IN_SERVER_POLICY: UInt32 = 20108
ERROR_DHCP_INVALID_POLICY_EXPRESSION: UInt32 = 20109
ERROR_DHCP_INVALID_PROCESSING_ORDER: UInt32 = 20110
ERROR_DHCP_POLICY_NOT_FOUND: UInt32 = 20111
ERROR_SCOPE_RANGE_POLICY_RANGE_CONFLICT: UInt32 = 20112
ERROR_DHCP_FO_SCOPE_ALREADY_IN_RELATIONSHIP: UInt32 = 20113
ERROR_DHCP_FO_RELATIONSHIP_EXISTS: UInt32 = 20114
ERROR_DHCP_FO_RELATIONSHIP_DOES_NOT_EXIST: UInt32 = 20115
ERROR_DHCP_FO_SCOPE_NOT_IN_RELATIONSHIP: UInt32 = 20116
ERROR_DHCP_FO_RELATION_IS_SECONDARY: UInt32 = 20117
ERROR_DHCP_FO_NOT_SUPPORTED: UInt32 = 20118
ERROR_DHCP_FO_TIME_OUT_OF_SYNC: UInt32 = 20119
ERROR_DHCP_FO_STATE_NOT_NORMAL: UInt32 = 20120
ERROR_DHCP_NO_ADMIN_PERMISSION: UInt32 = 20121
ERROR_DHCP_SERVER_NOT_REACHABLE: UInt32 = 20122
ERROR_DHCP_SERVER_NOT_RUNNING: UInt32 = 20123
ERROR_DHCP_SERVER_NAME_NOT_RESOLVED: UInt32 = 20124
ERROR_DHCP_FO_RELATIONSHIP_NAME_TOO_LONG: UInt32 = 20125
ERROR_DHCP_REACHED_END_OF_SELECTION: UInt32 = 20126
ERROR_DHCP_FO_ADDSCOPE_LEASES_NOT_SYNCED: UInt32 = 20127
ERROR_DHCP_FO_MAX_RELATIONSHIPS: UInt32 = 20128
ERROR_DHCP_FO_IPRANGE_TYPE_CONV_ILLEGAL: UInt32 = 20129
ERROR_DHCP_FO_MAX_ADD_SCOPES: UInt32 = 20130
ERROR_DHCP_FO_BOOT_NOT_SUPPORTED: UInt32 = 20131
ERROR_DHCP_FO_RANGE_PART_OF_REL: UInt32 = 20132
ERROR_DHCP_FO_SCOPE_SYNC_IN_PROGRESS: UInt32 = 20133
ERROR_DHCP_FO_FEATURE_NOT_SUPPORTED: UInt32 = 20134
ERROR_DHCP_POLICY_FQDN_RANGE_UNSUPPORTED: UInt32 = 20135
ERROR_DHCP_POLICY_FQDN_OPTION_UNSUPPORTED: UInt32 = 20136
ERROR_DHCP_POLICY_EDIT_FQDN_UNSUPPORTED: UInt32 = 20137
ERROR_DHCP_NAP_NOT_SUPPORTED: UInt32 = 20138
ERROR_LAST_DHCP_SERVER_ERROR: UInt32 = 20139
DHCP_SUBNET_INFO_VQ_FLAG_QUARANTINE: UInt32 = 1
MAX_PATTERN_LENGTH: UInt32 = 255
MAC_ADDRESS_LENGTH: UInt32 = 6
HWTYPE_ETHERNET_10MB: UInt32 = 1
FILTER_STATUS_NONE: UInt32 = 1
FILTER_STATUS_FULL_MATCH_IN_ALLOW_LIST: UInt32 = 2
FILTER_STATUS_FULL_MATCH_IN_DENY_LIST: UInt32 = 4
FILTER_STATUS_WILDCARD_MATCH_IN_ALLOW_LIST: UInt32 = 8
FILTER_STATUS_WILDCARD_MATCH_IN_DENY_LIST: UInt32 = 16
Set_APIProtocolSupport: UInt32 = 1
Set_DatabaseName: UInt32 = 2
Set_DatabasePath: UInt32 = 4
Set_BackupPath: UInt32 = 8
Set_BackupInterval: UInt32 = 16
Set_DatabaseLoggingFlag: UInt32 = 32
Set_RestoreFlag: UInt32 = 64
Set_DatabaseCleanupInterval: UInt32 = 128
Set_DebugFlag: UInt32 = 256
Set_PingRetries: UInt32 = 512
Set_BootFileTable: UInt32 = 1024
Set_AuditLogState: UInt32 = 2048
Set_QuarantineON: UInt32 = 4096
Set_QuarantineDefFail: UInt32 = 8192
CLIENT_TYPE_UNSPECIFIED: UInt32 = 0
CLIENT_TYPE_DHCP: UInt32 = 1
CLIENT_TYPE_BOOTP: UInt32 = 2
CLIENT_TYPE_RESERVATION_FLAG: UInt32 = 4
CLIENT_TYPE_NONE: UInt32 = 100
Set_UnicastFlag: UInt32 = 1
Set_RapidCommitFlag: UInt32 = 2
Set_PreferredLifetime: UInt32 = 4
Set_ValidLifetime: UInt32 = 8
Set_T1: UInt32 = 16
Set_T2: UInt32 = 32
Set_PreferredLifetimeIATA: UInt32 = 64
Set_ValidLifetimeIATA: UInt32 = 128
V5_ADDRESS_STATE_OFFERED: UInt32 = 0
V5_ADDRESS_STATE_ACTIVE: UInt32 = 1
V5_ADDRESS_STATE_DECLINED: UInt32 = 2
V5_ADDRESS_STATE_DOOM: UInt32 = 3
V5_ADDRESS_BIT_DELETED: UInt32 = 128
V5_ADDRESS_BIT_UNREGISTERED: UInt32 = 64
V5_ADDRESS_BIT_BOTH_REC: UInt32 = 32
V5_ADDRESS_EX_BIT_DISABLE_PTR_RR: UInt32 = 1
DNS_FLAG_ENABLED: UInt32 = 1
DNS_FLAG_UPDATE_DOWNLEVEL: UInt32 = 2
DNS_FLAG_CLEANUP_EXPIRED: UInt32 = 4
DNS_FLAG_UPDATE_BOTH_ALWAYS: UInt32 = 16
DNS_FLAG_UPDATE_DHCID: UInt32 = 32
DNS_FLAG_DISABLE_PTR_UPDATE: UInt32 = 64
DNS_FLAG_HAS_DNS_SUFFIX: UInt32 = 128
DHCP_OPT_ENUM_IGNORE_VENDOR: UInt32 = 1
DHCP_OPT_ENUM_USE_CLASSNAME: UInt32 = 2
DHCP_FLAGS_DONT_ACCESS_DS: UInt32 = 1
DHCP_FLAGS_DONT_DO_RPC: UInt32 = 2
DHCP_FLAGS_OPTION_IS_VENDOR: UInt32 = 3
DHCP_ATTRIB_BOOL_IS_ROGUE: UInt32 = 1
DHCP_ATTRIB_BOOL_IS_DYNBOOTP: UInt32 = 2
DHCP_ATTRIB_BOOL_IS_PART_OF_DSDC: UInt32 = 3
DHCP_ATTRIB_BOOL_IS_BINDING_AWARE: UInt32 = 4
DHCP_ATTRIB_BOOL_IS_ADMIN: UInt32 = 5
DHCP_ATTRIB_ULONG_RESTORE_STATUS: UInt32 = 6
DHCP_ATTRIB_TYPE_BOOL: UInt32 = 1
DHCP_ATTRIB_TYPE_ULONG: UInt32 = 2
DHCP_ENDPOINT_FLAG_CANT_MODIFY: UInt32 = 1
QUARANTIN_OPTION_BASE: UInt32 = 43220
QUARANTINE_SCOPE_QUARPROFILE_OPTION: UInt32 = 43221
QUARANTINE_CONFIG_OPTION: UInt32 = 43222
ADDRESS_TYPE_IANA: UInt32 = 0
ADDRESS_TYPE_IATA: UInt32 = 1
DHCP_MIN_DELAY: UInt32 = 0
DHCP_MAX_DELAY: UInt32 = 1000
DHCP_FAILOVER_DELETE_SCOPES: UInt32 = 1
DHCP_FAILOVER_MAX_NUM_ADD_SCOPES: UInt32 = 400
DHCP_FAILOVER_MAX_NUM_REL: UInt32 = 31
MCLT: UInt32 = 1
SAFEPERIOD: UInt32 = 2
CHANGESTATE: UInt32 = 4
PERCENTAGE: UInt32 = 8
MODE: UInt32 = 16
PREVSTATE: UInt32 = 32
SHAREDSECRET: UInt32 = 64
DHCP_CALLOUT_LIST_KEY: String = 'System\\CurrentControlSet\\Services\\DHCPServer\\Parameters'
DHCP_CALLOUT_LIST_VALUE: String = 'CalloutDlls'
DHCP_CALLOUT_ENTRY_POINT: String = 'DhcpServerCalloutEntry'
DHCP_CONTROL_START: UInt32 = 1
DHCP_CONTROL_STOP: UInt32 = 2
DHCP_CONTROL_PAUSE: UInt32 = 3
DHCP_CONTROL_CONTINUE: UInt32 = 4
DHCP_DROP_DUPLICATE: UInt32 = 1
DHCP_DROP_NOMEM: UInt32 = 2
DHCP_DROP_INTERNAL_ERROR: UInt32 = 3
DHCP_DROP_TIMEOUT: UInt32 = 4
DHCP_DROP_UNAUTH: UInt32 = 5
DHCP_DROP_PAUSED: UInt32 = 6
DHCP_DROP_NO_SUBNETS: UInt32 = 7
DHCP_DROP_INVALID: UInt32 = 8
DHCP_DROP_WRONG_SERVER: UInt32 = 9
DHCP_DROP_NOADDRESS: UInt32 = 10
DHCP_DROP_PROCESSED: UInt32 = 11
DHCP_DROP_GEN_FAILURE: UInt32 = 256
DHCP_SEND_PACKET: UInt32 = 268435456
DHCP_PROB_CONFLICT: UInt32 = 536870913
DHCP_PROB_DECLINE: UInt32 = 536870914
DHCP_PROB_RELEASE: UInt32 = 536870915
DHCP_PROB_NACKED: UInt32 = 536870916
DHCP_GIVE_ADDRESS_NEW: UInt32 = 805306369
DHCP_GIVE_ADDRESS_OLD: UInt32 = 805306370
DHCP_CLIENT_BOOTP: UInt32 = 805306371
DHCP_CLIENT_DHCP: UInt32 = 805306372
DHCPV6_OPTION_CLIENTID: UInt32 = 1
DHCPV6_OPTION_SERVERID: UInt32 = 2
DHCPV6_OPTION_IA_NA: UInt32 = 3
DHCPV6_OPTION_IA_TA: UInt32 = 4
DHCPV6_OPTION_ORO: UInt32 = 6
DHCPV6_OPTION_PREFERENCE: UInt32 = 7
DHCPV6_OPTION_UNICAST: UInt32 = 12
DHCPV6_OPTION_RAPID_COMMIT: UInt32 = 14
DHCPV6_OPTION_USER_CLASS: UInt32 = 15
DHCPV6_OPTION_VENDOR_CLASS: UInt32 = 16
DHCPV6_OPTION_VENDOR_OPTS: UInt32 = 17
DHCPV6_OPTION_RECONF_MSG: UInt32 = 19
DHCPV6_OPTION_SIP_SERVERS_NAMES: UInt32 = 21
DHCPV6_OPTION_SIP_SERVERS_ADDRS: UInt32 = 22
DHCPV6_OPTION_DNS_SERVERS: UInt32 = 23
DHCPV6_OPTION_DOMAIN_LIST: UInt32 = 24
DHCPV6_OPTION_IA_PD: UInt32 = 25
DHCPV6_OPTION_NIS_SERVERS: UInt32 = 27
DHCPV6_OPTION_NISP_SERVERS: UInt32 = 28
DHCPV6_OPTION_NIS_DOMAIN_NAME: UInt32 = 29
DHCPV6_OPTION_NISP_DOMAIN_NAME: UInt32 = 30
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6CApiInitialize(Version: POINTER(UInt32)) -> Void: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6CApiCleanup() -> Void: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6RequestParams(forceNewInform: win32more.Foundation.BOOL, reserved: c_void_p, adapterName: win32more.Foundation.PWSTR, classId: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), recdParams: win32more.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_ARRAY, buffer: c_char_p_no, pSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6RequestPrefix(adapterName: win32more.Foundation.PWSTR, pclassId: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), prefixleaseInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head), pdwTimeToWait: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6RenewPrefix(adapterName: win32more.Foundation.PWSTR, pclassId: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), prefixleaseInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head), pdwTimeToWait: POINTER(UInt32), bValidatePrefix: UInt32) -> UInt32: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6ReleasePrefix(adapterName: win32more.Foundation.PWSTR, classId: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), leaseInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpCApiInitialize(Version: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpCApiCleanup() -> Void: ...
@winfunctype('dhcpcsvc.dll')
def DhcpRequestParams(Flags: UInt32, Reserved: c_void_p, AdapterName: win32more.Foundation.PWSTR, ClassId: POINTER(win32more.NetworkManagement.Dhcp.DHCPCAPI_CLASSID_head), SendParams: win32more.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY, RecdParams: win32more.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY, Buffer: c_char_p_no, pSize: POINTER(UInt32), RequestIdStr: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpUndoRequestParams(Flags: UInt32, Reserved: c_void_p, AdapterName: win32more.Foundation.PWSTR, RequestIdStr: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpRegisterParamChange(Flags: UInt32, Reserved: c_void_p, AdapterName: win32more.Foundation.PWSTR, ClassId: POINTER(win32more.NetworkManagement.Dhcp.DHCPCAPI_CLASSID_head), Params: win32more.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY, Handle: c_void_p) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpDeRegisterParamChange(Flags: UInt32, Reserved: c_void_p, Event: c_void_p) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpRemoveDNSRegistrations() -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpGetOriginalSubnetMask(sAdapterName: win32more.Foundation.PWSTR, dwSubnetMask: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddFilterV4(ServerIpAddress: win32more.Foundation.PWSTR, AddFilterInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_ADD_INFO_head), ForceFlag: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteFilterV4(ServerIpAddress: win32more.Foundation.PWSTR, DeleteFilterInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetFilterV4(ServerIpAddress: win32more.Foundation.PWSTR, GlobalFilterInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_GLOBAL_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetFilterV4(ServerIpAddress: win32more.Foundation.PWSTR, GlobalFilterInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_GLOBAL_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumFilterV4(ServerIpAddress: win32more.Foundation.PWSTR, ResumeHandle: POINTER(win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN_head), PreferredMaximum: UInt32, ListType: win32more.NetworkManagement.Dhcp.DHCP_FILTER_LIST_TYPE, EnumFilterInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_ENUM_INFO_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateSubnet(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetInfo(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetInfo(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnets(ServerIpAddress: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElement(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, AddElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElements(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, EnumElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElement(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, RemoveElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head), ForceFlag: win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteSubnet(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ForceFlag: win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateOption(ServerIpAddress: win32more.Foundation.PWSTR, OptionID: UInt32, OptionInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionInfo(ServerIpAddress: win32more.Foundation.PWSTR, OptionID: UInt32, OptionInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionInfo(ServerIpAddress: win32more.Foundation.PWSTR, OptionID: UInt32, OptionInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptions(ServerIpAddress: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, Options: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOption(ServerIpAddress: win32more.Foundation.PWSTR, OptionID: UInt32) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValue(ServerIpAddress: win32more.Foundation.PWSTR, OptionID: UInt32, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValues(ServerIpAddress: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValues: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionValue(ServerIpAddress: win32more.Foundation.PWSTR, OptionID: UInt32, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionValues(ServerIpAddress: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, OptionValues: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionValue(ServerIpAddress: win32more.Foundation.PWSTR, OptionID: UInt32, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClientInfoVQ(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfoVQ(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfoVQ(ServerIpAddress: win32more.Foundation.PWSTR, SearchInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsVQ(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_VQ_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsFilterStatusInfo(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, SearchInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClients(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientOptions(ServerIpAddress: win32more.Foundation.PWSTR, ClientIpAddress: UInt32, ClientSubnetMask: UInt32, ClientOptions: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_LIST_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetMibInfo(ServerIpAddress: win32more.Foundation.PWSTR, MibInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfig(ServerIpAddress: win32more.Foundation.PWSTR, FieldsToSet: UInt32, ConfigInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfig(ServerIpAddress: win32more.Foundation.PWSTR, ConfigInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpScanDatabase(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, FixFlag: UInt32, ScanList: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SCAN_LIST_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRpcFreeMemory(BufferPointer: c_void_p) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetVersion(ServerIpAddress: win32more.Foundation.PWSTR, MajorVersion: POINTER(UInt32), MinorVersion: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElementV4(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, AddElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElementsV4(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, EnumElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElementV4(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, RemoveElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head), ForceFlag: win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClientInfoV4(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfoV4(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfoV4(ServerIpAddress: win32more.Foundation.PWSTR, SearchInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsV4(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V4_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfigV4(ServerIpAddress: win32more.Foundation.PWSTR, FieldsToSet: UInt32, ConfigInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfigV4(ServerIpAddress: win32more.Foundation.PWSTR, ConfigInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V4_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSuperScopeV4(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, SuperScopeName: win32more.Foundation.PWSTR, ChangeExisting: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteSuperScopeV4(ServerIpAddress: win32more.Foundation.PWSTR, SuperScopeName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSuperScopeInfoV4(ServerIpAddress: win32more.Foundation.PWSTR, SuperScopeTable: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsV5(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V5_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateOptionV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, OptionInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionInfoV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, OptionInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionInfoV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, OptionInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionsV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, Options: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValueV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValuesV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValues: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionValueV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionValueV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), OptionValue: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionValuesV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, OptionValues: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionValueV5(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClass(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpModifyClass(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClass(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClassInfo(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, PartialClassInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head), FilledClassInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumClasses(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClassInfoArray: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_head)), nRead: POINTER(UInt32), nTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptions(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionStruct: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTIONS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptionsV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionStruct: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTIONS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptionValues(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), Values: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptionValuesV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), Values: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumServers(Flags: UInt32, IdInfo: c_void_p, Servers: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVERS_head)), CallbackFn: c_void_p, CallbackData: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddServer(Flags: UInt32, IdInfo: c_void_p, NewServer: POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVER_head), CallbackFn: c_void_p, CallbackData: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteServer(Flags: UInt32, IdInfo: c_void_p, NewServer: POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVER_head), CallbackFn: c_void_p, CallbackData: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetServerBindingInfo(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, BindElementsInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetServerBindingInfo(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, BindElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElementV5(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, AddElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElementsV5(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, EnumElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElementV5(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, RemoveElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head), ForceFlag: win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumSubnetReservations(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_RESERVATION_INFO_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateOptionV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, OptionInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionsV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, Options: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionValueV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, OptionInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, OptionInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValueV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), OptionValue: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetInfoVQ(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateSubnetVQ(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetInfoVQ(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionValuesV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ClassName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, OptionValues: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDsInit() -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDsCleanup() -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetThreadOptions(Flags: UInt32, Reserved: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetThreadOptions(pFlags: POINTER(UInt32), Reserved: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerQueryAttribute(ServerIpAddr: win32more.Foundation.PWSTR, dwReserved: UInt32, DhcpAttribId: UInt32, pDhcpAttrib: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerQueryAttributes(ServerIpAddr: win32more.Foundation.PWSTR, dwReserved: UInt32, dwAttribCount: UInt32, pDhcpAttribs: POINTER(UInt32), pDhcpAttribArr: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerRedoAuthorization(ServerIpAddr: win32more.Foundation.PWSTR, dwReserved: UInt32) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAuditLogSetParams(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, AuditLogDir: win32more.Foundation.PWSTR, DiskCheckInterval: UInt32, MaxLogFilesSize: UInt32, MinSpaceOnDisk: UInt32) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAuditLogGetParams(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, AuditLogDir: POINTER(win32more.Foundation.PWSTR), DiskCheckInterval: POINTER(UInt32), MaxLogFilesSize: POINTER(UInt32), MinSpaceOnDisk: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerQueryDnsRegCredentials(ServerIpAddress: win32more.Foundation.PWSTR, UnameSize: UInt32, Uname: win32more.Foundation.PWSTR, DomainSize: UInt32, Domain: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetDnsRegCredentials(ServerIpAddress: win32more.Foundation.PWSTR, Uname: win32more.Foundation.PWSTR, Domain: win32more.Foundation.PWSTR, Passwd: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetDnsRegCredentialsV5(ServerIpAddress: win32more.Foundation.PWSTR, Uname: win32more.Foundation.PWSTR, Domain: win32more.Foundation.PWSTR, Passwd: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerBackupDatabase(ServerIpAddress: win32more.Foundation.PWSTR, Path: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerRestoreDatabase(ServerIpAddress: win32more.Foundation.PWSTR, Path: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfigVQ(ServerIpAddress: win32more.Foundation.PWSTR, FieldsToSet: UInt32, ConfigInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfigVQ(ServerIpAddress: win32more.Foundation.PWSTR, ConfigInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetServerSpecificStrings(ServerIpAddress: win32more.Foundation.PWSTR, ServerSpecificStrings: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_SPECIFIC_STRINGS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerAuditlogParamsFree(ConfigInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateSubnetV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, SubnetInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteSubnetV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, ForceFlag: win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetsV6(ServerIpAddress: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_IP_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElementV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, AddElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElementV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, RemoveElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head), ForceFlag: win32more.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElementsV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, EnumElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE_V6, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, SubnetInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, ResumeHandle: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS_head), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V6_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfigV6(ServerIpAddress: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), ConfigInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfigV6(ServerIpAddress: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), FieldsToSet: UInt32, ConfigInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, SubnetInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetMibInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, MibInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetServerBindingInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, BindElementsInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetServerBindingInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, BindElementInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, SearchInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_V6_head), ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClientInfoV6(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClassV6(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpModifyClassV6(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClassV6(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumClassesV6(ServerIpAddress: win32more.Foundation.PWSTR, ReservedMustBeZero: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClassInfoArray: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_V6_head)), nRead: POINTER(UInt32), nTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetDelayOffer(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, TimeDelayInMilliseconds: UInt16) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetDelayOffer(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, TimeDelayInMilliseconds: POINTER(UInt16)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetMibInfoV5(ServerIpAddress: win32more.Foundation.PWSTR, MibInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_MIB_INFO_V5_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSecurityGroup(pServer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetOptionValue(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, PolicyName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetOptionValue(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, PolicyName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetOptionValues(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, PolicyName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValues: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4RemoveOptionValue(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, PolicyName: win32more.Foundation.PWSTR, VendorName: win32more.Foundation.PWSTR, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetAllOptionValues(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), Values: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_PB_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverCreateRelationship(ServerIpAddress: win32more.Foundation.PWSTR, pRelationship: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverSetRelationship(ServerIpAddress: win32more.Foundation.PWSTR, Flags: UInt32, pRelationship: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverDeleteRelationship(ServerIpAddress: win32more.Foundation.PWSTR, pRelationshipName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetRelationship(ServerIpAddress: win32more.Foundation.PWSTR, pRelationshipName: win32more.Foundation.PWSTR, pRelationship: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverEnumRelationship(ServerIpAddress: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, pRelationship: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_ARRAY_head)), RelationshipRead: POINTER(UInt32), RelationshipTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverAddScopeToRelationship(ServerIpAddress: win32more.Foundation.PWSTR, pRelationship: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverDeleteScopeFromRelationship(ServerIpAddress: win32more.Foundation.PWSTR, pRelationship: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetScopeRelationship(ServerIpAddress: win32more.Foundation.PWSTR, ScopeId: UInt32, pRelationship: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetScopeStatistics(ServerIpAddress: win32more.Foundation.PWSTR, ScopeId: UInt32, pStats: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_STATISTICS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, SearchInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetSystemTime(ServerIpAddress: win32more.Foundation.PWSTR, pTime: POINTER(UInt32), pMaxAllowedDeltaTime: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetAddressStatus(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, pStatus: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverTriggerAddrAllocation(ServerIpAddress: win32more.Foundation.PWSTR, pFailRelName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprCreateV4Policy(PolicyName: win32more.Foundation.PWSTR, fGlobalPolicy: win32more.Foundation.BOOL, Subnet: UInt32, ProcessingOrder: UInt32, RootOperator: win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER, Description: win32more.Foundation.PWSTR, Enabled: win32more.Foundation.BOOL, Policy: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprCreateV4PolicyEx(PolicyName: win32more.Foundation.PWSTR, fGlobalPolicy: win32more.Foundation.BOOL, Subnet: UInt32, ProcessingOrder: UInt32, RootOperator: win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER, Description: win32more.Foundation.PWSTR, Enabled: win32more.Foundation.BOOL, Policy: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprAddV4PolicyExpr(Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), ParentExpr: UInt32, Operator: win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER, ExprIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprAddV4PolicyCondition(Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), ParentExpr: UInt32, Type: win32more.NetworkManagement.Dhcp.DHCP_POL_ATTR_TYPE, OptionID: UInt32, SubOptionID: UInt32, VendorName: win32more.Foundation.PWSTR, Operator: win32more.NetworkManagement.Dhcp.DHCP_POL_COMPARATOR, Value: c_char_p_no, ValueLength: UInt32, ConditionIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprAddV4PolicyRange(Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), Range: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprResetV4PolicyExpr(Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprModifyV4PolicyExpr(Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head), Operator: win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4Policy(Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4PolicyArray(PolicyArray: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_ARRAY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4PolicyEx(PolicyEx: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4PolicyExArray(PolicyExArray: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_ARRAY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4DhcpProperty(Property: POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4DhcpPropertyArray(PropertyArray: POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFindV4DhcpProperty(PropertyArray: POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head), ID: win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ID, Type: win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_TYPE) -> POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_head): ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprIsV4PolicySingleUC(Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4QueryPolicyEnforcement(ServerIpAddress: win32more.Foundation.PWSTR, fGlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, Enabled: POINTER(win32more.Foundation.BOOL)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetPolicyEnforcement(ServerIpAddress: win32more.Foundation.PWSTR, fGlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, Enable: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprIsV4PolicyWellFormed(pPolicy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprIsV4PolicyValid(pPolicy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreatePolicy(ServerIpAddress: win32more.Foundation.PWSTR, pPolicy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetPolicy(ServerIpAddress: win32more.Foundation.PWSTR, fGlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: win32more.Foundation.PWSTR, Policy: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetPolicy(ServerIpAddress: win32more.Foundation.PWSTR, FieldsModified: UInt32, fGlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: win32more.Foundation.PWSTR, Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4DeletePolicy(ServerIpAddress: win32more.Foundation.PWSTR, fGlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumPolicies(ServerIpAddress: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, fGlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, EnumInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4AddPolicyRange(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, PolicyName: win32more.Foundation.PWSTR, Range: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4RemovePolicyRange(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, PolicyName: win32more.Foundation.PWSTR, Range: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6SetStatelessStoreParams(ServerIpAddress: win32more.Foundation.PWSTR, fServerLevel: win32more.Foundation.BOOL, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, FieldModified: UInt32, Params: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_PARAMS_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6GetStatelessStoreParams(ServerIpAddress: win32more.Foundation.PWSTR, fServerLevel: win32more.Foundation.BOOL, SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, Params: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_PARAMS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6GetStatelessStatistics(ServerIpAddress: win32more.Foundation.PWSTR, StatelessStats: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_STATS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreateClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumSubnetClients(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, SearchInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6CreateClientInfo(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetFreeIPAddress(ServerIpAddress: win32more.Foundation.PWSTR, ScopeId: UInt32, StartIP: UInt32, EndIP: UInt32, NumFreeAddrReq: UInt32, IPAddrList: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6GetFreeIPAddress(ServerIpAddress: win32more.Foundation.PWSTR, ScopeId: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, StartIP: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, EndIP: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, NumFreeAddrReq: UInt32, IPAddrList: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_IP_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreateClientInfoEx(ServerIpAddress: win32more.Foundation.PWSTR, ClientInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumSubnetClientsEx(ServerIpAddress: win32more.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetClientInfoEx(ServerIpAddress: win32more.Foundation.PWSTR, SearchInfo: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreatePolicyEx(ServerIpAddress: win32more.Foundation.PWSTR, PolicyEx: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetPolicyEx(ServerIpAddress: win32more.Foundation.PWSTR, GlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: win32more.Foundation.PWSTR, Policy: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetPolicyEx(ServerIpAddress: win32more.Foundation.PWSTR, FieldsModified: UInt32, GlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: win32more.Foundation.PWSTR, Policy: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumPoliciesEx(ServerIpAddress: win32more.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, GlobalPolicy: win32more.Foundation.BOOL, SubnetAddress: UInt32, EnumInfo: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
class DATE_TIME(Structure):
    dwLowDateTime: UInt32
    dwHighDateTime: UInt32
class DHCP_ADDR_PATTERN(Structure):
    MatchHWType: win32more.Foundation.BOOL
    HWType: Byte
    IsWildcard: win32more.Foundation.BOOL
    Length: Byte
    Pattern: Byte * 255
class DHCP_ALL_OPTION_VALUES(Structure):
    Flags: UInt32
    NumElements: UInt32
    Options: POINTER(_Anonymous_e__Struct)
    class _Anonymous_e__Struct(Structure):
        ClassName: win32more.Foundation.PWSTR
        VendorName: win32more.Foundation.PWSTR
        IsVendor: win32more.Foundation.BOOL
        OptionsArray: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)
class DHCP_ALL_OPTION_VALUES_PB(Structure):
    Flags: UInt32
    NumElements: UInt32
    Options: POINTER(_Anonymous_e__Struct)
    class _Anonymous_e__Struct(Structure):
        PolicyName: win32more.Foundation.PWSTR
        VendorName: win32more.Foundation.PWSTR
        IsVendor: win32more.Foundation.BOOL
        OptionsArray: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)
class DHCP_ALL_OPTIONS(Structure):
    Flags: UInt32
    NonVendorOptions: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)
    NumVendorOptions: UInt32
    VendorOptions: POINTER(_Anonymous_e__Struct)
    class _Anonymous_e__Struct(Structure):
        Option: win32more.NetworkManagement.Dhcp.DHCP_OPTION
        VendorName: win32more.Foundation.PWSTR
        ClassName: win32more.Foundation.PWSTR
class DHCP_ATTRIB(Structure):
    DhcpAttribId: UInt32
    DhcpAttribType: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        DhcpAttribBool: win32more.Foundation.BOOL
        DhcpAttribUlong: UInt32
class DHCP_ATTRIB_ARRAY(Structure):
    NumElements: UInt32
    DhcpAttribs: POINTER(win32more.NetworkManagement.Dhcp.DHCP_ATTRIB_head)
class DHCP_BINARY_DATA(Structure):
    DataLength: UInt32
    Data: c_char_p_no
class DHCP_BIND_ELEMENT(Structure):
    Flags: UInt32
    fBoundToDHCPServer: win32more.Foundation.BOOL
    AdapterPrimaryAddress: UInt32
    AdapterSubnetAddress: UInt32
    IfDescription: win32more.Foundation.PWSTR
    IfIdSize: UInt32
    IfId: c_char_p_no
class DHCP_BIND_ELEMENT_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_head)
class DHCP_BOOTP_IP_RANGE(Structure):
    StartAddress: UInt32
    EndAddress: UInt32
    BootpAllocated: UInt32
    MaxBootpAllowed: UInt32
class DHCP_CALLOUT_TABLE(Structure):
    DhcpControlHook: win32more.NetworkManagement.Dhcp.LPDHCP_CONTROL
    DhcpNewPktHook: win32more.NetworkManagement.Dhcp.LPDHCP_NEWPKT
    DhcpPktDropHook: win32more.NetworkManagement.Dhcp.LPDHCP_DROP_SEND
    DhcpPktSendHook: win32more.NetworkManagement.Dhcp.LPDHCP_DROP_SEND
    DhcpAddressDelHook: win32more.NetworkManagement.Dhcp.LPDHCP_PROB
    DhcpAddressOfferHook: win32more.NetworkManagement.Dhcp.LPDHCP_GIVE_ADDRESS
    DhcpHandleOptionsHook: win32more.NetworkManagement.Dhcp.LPDHCP_HANDLE_OPTIONS
    DhcpDeleteClientHook: win32more.NetworkManagement.Dhcp.LPDHCP_DELETE_CLIENT
    DhcpExtensionHook: c_void_p
    DhcpReservedHook: c_void_p
class DHCP_CLASS_INFO(Structure):
    ClassName: win32more.Foundation.PWSTR
    ClassComment: win32more.Foundation.PWSTR
    ClassDataLength: UInt32
    IsVendor: win32more.Foundation.BOOL
    Flags: UInt32
    ClassData: c_char_p_no
class DHCP_CLASS_INFO_ARRAY(Structure):
    NumElements: UInt32
    Classes: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)
class DHCP_CLASS_INFO_ARRAY_V6(Structure):
    NumElements: UInt32
    Classes: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head)
class DHCP_CLASS_INFO_V6(Structure):
    ClassName: win32more.Foundation.PWSTR
    ClassComment: win32more.Foundation.PWSTR
    ClassDataLength: UInt32
    IsVendor: win32more.Foundation.BOOL
    EnterpriseNumber: UInt32
    Flags: UInt32
    ClassData: c_char_p_no
class DHCP_CLIENT_FILTER_STATUS_INFO(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: win32more.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: win32more.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: win32more.Foundation.BOOL
    FilterStatus: UInt32
class DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_head))
class DHCP_CLIENT_INFO(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
class DHCP_CLIENT_INFO_ARRAY(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head))
class DHCP_CLIENT_INFO_ARRAY_V4(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head))
class DHCP_CLIENT_INFO_ARRAY_V5(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V5_head))
class DHCP_CLIENT_INFO_ARRAY_V6(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head))
class DHCP_CLIENT_INFO_ARRAY_VQ(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head))
class DHCP_CLIENT_INFO_EX(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: win32more.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: win32more.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: win32more.Foundation.BOOL
    FilterStatus: UInt32
    PolicyName: win32more.Foundation.PWSTR
    Properties: POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)
class DHCP_CLIENT_INFO_EX_ARRAY(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head))
class DHCP_CLIENT_INFO_PB(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: win32more.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: win32more.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: win32more.Foundation.BOOL
    FilterStatus: UInt32
    PolicyName: win32more.Foundation.PWSTR
class DHCP_CLIENT_INFO_PB_ARRAY(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head))
class DHCP_CLIENT_INFO_V4(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
class DHCP_CLIENT_INFO_V5(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
class DHCP_CLIENT_INFO_V6(Structure):
    ClientIpAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    ClientDUID: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    AddressType: UInt32
    IAID: UInt32
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientValidLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    ClientPrefLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_V6
class DHCP_CLIENT_INFO_VQ(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: win32more.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: win32more.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: win32more.Foundation.BOOL
class DHCP_CLIENT_SEARCH_UNION(Union):
    pass
DHCP_FAILOVER_MODE = Int32
DHCP_FAILOVER_MODE_LoadBalance: DHCP_FAILOVER_MODE = 0
DHCP_FAILOVER_MODE_HotStandby: DHCP_FAILOVER_MODE = 1
class DHCP_FAILOVER_RELATIONSHIP(Structure):
    PrimaryServer: UInt32
    SecondaryServer: UInt32
    Mode: win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_MODE
    ServerType: win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_SERVER
    State: win32more.NetworkManagement.Dhcp.FSM_STATE
    PrevState: win32more.NetworkManagement.Dhcp.FSM_STATE
    Mclt: UInt32
    SafePeriod: UInt32
    RelationshipName: win32more.Foundation.PWSTR
    PrimaryServerName: win32more.Foundation.PWSTR
    SecondaryServerName: win32more.Foundation.PWSTR
    pScopes: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head)
    Percentage: Byte
    SharedSecret: win32more.Foundation.PWSTR
class DHCP_FAILOVER_RELATIONSHIP_ARRAY(Structure):
    NumElements: UInt32
    pRelationships: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)
DHCP_FAILOVER_SERVER = Int32
DHCP_FAILOVER_SERVER_PrimaryServer: DHCP_FAILOVER_SERVER = 0
DHCP_FAILOVER_SERVER_SecondaryServer: DHCP_FAILOVER_SERVER = 1
class DHCP_FAILOVER_STATISTICS(Structure):
    NumAddr: UInt32
    AddrFree: UInt32
    AddrInUse: UInt32
    PartnerAddrFree: UInt32
    ThisAddrFree: UInt32
    PartnerAddrInUse: UInt32
    ThisAddrInUse: UInt32
class DHCP_FILTER_ADD_INFO(Structure):
    AddrPatt: win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN
    Comment: win32more.Foundation.PWSTR
    ListType: win32more.NetworkManagement.Dhcp.DHCP_FILTER_LIST_TYPE
class DHCP_FILTER_ENUM_INFO(Structure):
    NumElements: UInt32
    pEnumRecords: POINTER(win32more.NetworkManagement.Dhcp.DHCP_FILTER_RECORD_head)
class DHCP_FILTER_GLOBAL_INFO(Structure):
    EnforceAllowList: win32more.Foundation.BOOL
    EnforceDenyList: win32more.Foundation.BOOL
DHCP_FILTER_LIST_TYPE = Int32
DHCP_FILTER_LIST_TYPE_Deny: DHCP_FILTER_LIST_TYPE = 0
DHCP_FILTER_LIST_TYPE_Allow: DHCP_FILTER_LIST_TYPE = 1
class DHCP_FILTER_RECORD(Structure):
    AddrPatt: win32more.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN
    Comment: win32more.Foundation.PWSTR
DHCP_FORCE_FLAG = Int32
DHCP_FORCE_FLAG_DhcpFullForce: DHCP_FORCE_FLAG = 0
DHCP_FORCE_FLAG_DhcpNoForce: DHCP_FORCE_FLAG = 1
DHCP_FORCE_FLAG_DhcpFailoverForce: DHCP_FORCE_FLAG = 2
class DHCP_HOST_INFO(Structure):
    IpAddress: UInt32
    NetBiosName: win32more.Foundation.PWSTR
    HostName: win32more.Foundation.PWSTR
class DHCP_HOST_INFO_V6(Structure):
    IpAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    NetBiosName: win32more.Foundation.PWSTR
    HostName: win32more.Foundation.PWSTR
class DHCP_IP_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(UInt32)
class DHCP_IP_CLUSTER(Structure):
    ClusterAddress: UInt32
    ClusterMask: UInt32
class DHCP_IP_RANGE(Structure):
    StartAddress: UInt32
    EndAddress: UInt32
class DHCP_IP_RANGE_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
class DHCP_IP_RANGE_V6(Structure):
    StartAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    EndAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
class DHCP_IP_RESERVATION(Structure):
    ReservedIpAddress: UInt32
    ReservedForClient: POINTER(win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)
class DHCP_IP_RESERVATION_INFO(Structure):
    ReservedIpAddress: UInt32
    ReservedForClient: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ReservedClientName: win32more.Foundation.PWSTR
    ReservedClientDesc: win32more.Foundation.PWSTR
    bAllowedClientTypes: Byte
    fOptionsPresent: Byte
class DHCP_IP_RESERVATION_V4(Structure):
    ReservedIpAddress: UInt32
    ReservedForClient: POINTER(win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)
    bAllowedClientTypes: Byte
class DHCP_IP_RESERVATION_V6(Structure):
    ReservedIpAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    ReservedForClient: POINTER(win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)
    InterfaceId: UInt32
class DHCP_IPV6_ADDRESS(Structure):
    HighOrderBits: UInt64
    LowOrderBits: UInt64
class DHCP_MIB_INFO(Structure):
    Discovers: UInt32
    Offers: UInt32
    Requests: UInt32
    Acks: UInt32
    Naks: UInt32
    Declines: UInt32
    Releases: UInt32
    ServerStartTime: win32more.NetworkManagement.Dhcp.DATE_TIME
    Scopes: UInt32
    ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_head)
class DHCP_MIB_INFO_V5(Structure):
    Discovers: UInt32
    Offers: UInt32
    Requests: UInt32
    Acks: UInt32
    Naks: UInt32
    Declines: UInt32
    Releases: UInt32
    ServerStartTime: win32more.NetworkManagement.Dhcp.DATE_TIME
    QtnNumLeases: UInt32
    QtnPctQtnLeases: UInt32
    QtnProbationLeases: UInt32
    QtnNonQtnLeases: UInt32
    QtnExemptLeases: UInt32
    QtnCapableClients: UInt32
    QtnIASErrors: UInt32
    DelayedOffers: UInt32
    ScopesWithDelayedOffers: UInt32
    Scopes: UInt32
    ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V5_head)
class DHCP_MIB_INFO_V6(Structure):
    Solicits: UInt32
    Advertises: UInt32
    Requests: UInt32
    Renews: UInt32
    Rebinds: UInt32
    Replies: UInt32
    Confirms: UInt32
    Declines: UInt32
    Releases: UInt32
    Informs: UInt32
    ServerStartTime: win32more.NetworkManagement.Dhcp.DATE_TIME
    Scopes: UInt32
    ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V6_head)
class DHCP_MIB_INFO_VQ(Structure):
    Discovers: UInt32
    Offers: UInt32
    Requests: UInt32
    Acks: UInt32
    Naks: UInt32
    Declines: UInt32
    Releases: UInt32
    ServerStartTime: win32more.NetworkManagement.Dhcp.DATE_TIME
    QtnNumLeases: UInt32
    QtnPctQtnLeases: UInt32
    QtnProbationLeases: UInt32
    QtnNonQtnLeases: UInt32
    QtnExemptLeases: UInt32
    QtnCapableClients: UInt32
    QtnIASErrors: UInt32
    Scopes: UInt32
    ScopeInfo: POINTER(win32more.NetworkManagement.Dhcp.SCOPE_MIB_INFO_VQ_head)
class DHCP_OPTION(Structure):
    OptionID: UInt32
    OptionName: win32more.Foundation.PWSTR
    OptionComment: win32more.Foundation.PWSTR
    DefaultValue: win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA
    OptionType: win32more.NetworkManagement.Dhcp.DHCP_OPTION_TYPE
class DHCP_OPTION_ARRAY(Structure):
    NumElements: UInt32
    Options: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_head)
class DHCP_OPTION_DATA(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_ELEMENT_head)
class DHCP_OPTION_DATA_ELEMENT(Structure):
    OptionType: win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA_TYPE
    Element: DHCP_OPTION_ELEMENT_UNION
    class DHCP_OPTION_ELEMENT_UNION(Union):
        ByteOption: Byte
        WordOption: UInt16
        DWordOption: UInt32
        DWordDWordOption: win32more.NetworkManagement.Dhcp.DWORD_DWORD
        IpAddressOption: UInt32
        StringDataOption: win32more.Foundation.PWSTR
        BinaryDataOption: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        EncapsulatedDataOption: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        Ipv6AddressDataOption: win32more.Foundation.PWSTR
DHCP_OPTION_DATA_TYPE = Int32
DHCP_OPTION_DATA_TYPE_DhcpByteOption: DHCP_OPTION_DATA_TYPE = 0
DHCP_OPTION_DATA_TYPE_DhcpWordOption: DHCP_OPTION_DATA_TYPE = 1
DHCP_OPTION_DATA_TYPE_DhcpDWordOption: DHCP_OPTION_DATA_TYPE = 2
DHCP_OPTION_DATA_TYPE_DhcpDWordDWordOption: DHCP_OPTION_DATA_TYPE = 3
DHCP_OPTION_DATA_TYPE_DhcpIpAddressOption: DHCP_OPTION_DATA_TYPE = 4
DHCP_OPTION_DATA_TYPE_DhcpStringDataOption: DHCP_OPTION_DATA_TYPE = 5
DHCP_OPTION_DATA_TYPE_DhcpBinaryDataOption: DHCP_OPTION_DATA_TYPE = 6
DHCP_OPTION_DATA_TYPE_DhcpEncapsulatedDataOption: DHCP_OPTION_DATA_TYPE = 7
DHCP_OPTION_DATA_TYPE_DhcpIpv6AddressOption: DHCP_OPTION_DATA_TYPE = 8
class DHCP_OPTION_ELEMENT_UNION(Union):
    pass
class DHCP_OPTION_LIST(Structure):
    NumOptions: UInt32
    Options: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)
class DHCP_OPTION_SCOPE_INFO(Structure):
    ScopeType: win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_TYPE
    ScopeInfo: _DHCP_OPTION_SCOPE_UNION
    class _DHCP_OPTION_SCOPE_UNION(Union):
        DefaultScopeInfo: c_void_p
        GlobalScopeInfo: c_void_p
        SubnetScopeInfo: UInt32
        ReservedScopeInfo: win32more.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE
        MScopeInfo: win32more.Foundation.PWSTR
class DHCP_OPTION_SCOPE_INFO6(Structure):
    ScopeType: win32more.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_TYPE6
    ScopeInfo: DHCP_OPTION_SCOPE_UNION6
    class DHCP_OPTION_SCOPE_UNION6(Union):
        DefaultScopeInfo: c_void_p
        SubnetScopeInfo: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
        ReservedScopeInfo: win32more.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE6
DHCP_OPTION_SCOPE_TYPE = Int32
DHCP_OPTION_SCOPE_TYPE_DhcpDefaultOptions: DHCP_OPTION_SCOPE_TYPE = 0
DHCP_OPTION_SCOPE_TYPE_DhcpGlobalOptions: DHCP_OPTION_SCOPE_TYPE = 1
DHCP_OPTION_SCOPE_TYPE_DhcpSubnetOptions: DHCP_OPTION_SCOPE_TYPE = 2
DHCP_OPTION_SCOPE_TYPE_DhcpReservedOptions: DHCP_OPTION_SCOPE_TYPE = 3
DHCP_OPTION_SCOPE_TYPE_DhcpMScopeOptions: DHCP_OPTION_SCOPE_TYPE = 4
DHCP_OPTION_SCOPE_TYPE6 = Int32
DHCP_OPTION_SCOPE_TYPE6_DhcpDefaultOptions6: DHCP_OPTION_SCOPE_TYPE6 = 0
DHCP_OPTION_SCOPE_TYPE6_DhcpScopeOptions6: DHCP_OPTION_SCOPE_TYPE6 = 1
DHCP_OPTION_SCOPE_TYPE6_DhcpReservedOptions6: DHCP_OPTION_SCOPE_TYPE6 = 2
DHCP_OPTION_SCOPE_TYPE6_DhcpGlobalOptions6: DHCP_OPTION_SCOPE_TYPE6 = 3
class DHCP_OPTION_SCOPE_UNION6(Union):
    pass
DHCP_OPTION_TYPE = Int32
DHCP_OPTION_TYPE_DhcpUnaryElementTypeOption: DHCP_OPTION_TYPE = 0
DHCP_OPTION_TYPE_DhcpArrayTypeOption: DHCP_OPTION_TYPE = 1
class DHCP_OPTION_VALUE(Structure):
    OptionID: UInt32
    Value: win32more.NetworkManagement.Dhcp.DHCP_OPTION_DATA
class DHCP_OPTION_VALUE_ARRAY(Structure):
    NumElements: UInt32
    Values: POINTER(win32more.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)
class DHCP_PERF_STATS(Structure):
    dwNumPacketsReceived: UInt32
    dwNumPacketsDuplicate: UInt32
    dwNumPacketsExpired: UInt32
    dwNumMilliSecondsProcessed: UInt32
    dwNumPacketsInActiveQueue: UInt32
    dwNumPacketsInPingQueue: UInt32
    dwNumDiscoversReceived: UInt32
    dwNumOffersSent: UInt32
    dwNumRequestsReceived: UInt32
    dwNumInformsReceived: UInt32
    dwNumAcksSent: UInt32
    dwNumNacksSent: UInt32
    dwNumDeclinesReceived: UInt32
    dwNumReleasesReceived: UInt32
    dwNumDelayedOfferInQueue: UInt32
    dwNumPacketsProcessed: UInt32
    dwNumPacketsInQuarWaitingQueue: UInt32
    dwNumPacketsInQuarReadyQueue: UInt32
    dwNumPacketsInQuarDecisionQueue: UInt32
DHCP_POL_ATTR_TYPE = Int32
DHCP_POL_ATTR_TYPE_DhcpAttrHWAddr: DHCP_POL_ATTR_TYPE = 0
DHCP_POL_ATTR_TYPE_DhcpAttrOption: DHCP_POL_ATTR_TYPE = 1
DHCP_POL_ATTR_TYPE_DhcpAttrSubOption: DHCP_POL_ATTR_TYPE = 2
DHCP_POL_ATTR_TYPE_DhcpAttrFqdn: DHCP_POL_ATTR_TYPE = 3
DHCP_POL_ATTR_TYPE_DhcpAttrFqdnSingleLabel: DHCP_POL_ATTR_TYPE = 4
DHCP_POL_COMPARATOR = Int32
DHCP_POL_COMPARATOR_DhcpCompEqual: DHCP_POL_COMPARATOR = 0
DHCP_POL_COMPARATOR_DhcpCompNotEqual: DHCP_POL_COMPARATOR = 1
DHCP_POL_COMPARATOR_DhcpCompBeginsWith: DHCP_POL_COMPARATOR = 2
DHCP_POL_COMPARATOR_DhcpCompNotBeginWith: DHCP_POL_COMPARATOR = 3
DHCP_POL_COMPARATOR_DhcpCompEndsWith: DHCP_POL_COMPARATOR = 4
DHCP_POL_COMPARATOR_DhcpCompNotEndWith: DHCP_POL_COMPARATOR = 5
class DHCP_POL_COND(Structure):
    ParentExpr: UInt32
    Type: win32more.NetworkManagement.Dhcp.DHCP_POL_ATTR_TYPE
    OptionID: UInt32
    SubOptionID: UInt32
    VendorName: win32more.Foundation.PWSTR
    Operator: win32more.NetworkManagement.Dhcp.DHCP_POL_COMPARATOR
    Value: c_char_p_no
    ValueLength: UInt32
class DHCP_POL_COND_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_COND_head)
class DHCP_POL_EXPR(Structure):
    ParentExpr: UInt32
    Operator: win32more.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER
class DHCP_POL_EXPR_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_head)
DHCP_POL_LOGIC_OPER = Int32
DHCP_POL_LOGIC_OPER_DhcpLogicalOr: DHCP_POL_LOGIC_OPER = 0
DHCP_POL_LOGIC_OPER_DhcpLogicalAnd: DHCP_POL_LOGIC_OPER = 1
class DHCP_POLICY(Structure):
    PolicyName: win32more.Foundation.PWSTR
    IsGlobalPolicy: win32more.Foundation.BOOL
    Subnet: UInt32
    ProcessingOrder: UInt32
    Conditions: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_COND_ARRAY_head)
    Expressions: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_ARRAY_head)
    Ranges: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_ARRAY_head)
    Description: win32more.Foundation.PWSTR
    Enabled: win32more.Foundation.BOOL
class DHCP_POLICY_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_head)
class DHCP_POLICY_EX(Structure):
    PolicyName: win32more.Foundation.PWSTR
    IsGlobalPolicy: win32more.Foundation.BOOL
    Subnet: UInt32
    ProcessingOrder: UInt32
    Conditions: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_COND_ARRAY_head)
    Expressions: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POL_EXPR_ARRAY_head)
    Ranges: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_ARRAY_head)
    Description: win32more.Foundation.PWSTR
    Enabled: win32more.Foundation.BOOL
    Properties: POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)
class DHCP_POLICY_EX_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)
DHCP_POLICY_FIELDS_TO_UPDATE = Int32
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyName: DHCP_POLICY_FIELDS_TO_UPDATE = 1
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyOrder: DHCP_POLICY_FIELDS_TO_UPDATE = 2
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyExpr: DHCP_POLICY_FIELDS_TO_UPDATE = 4
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyRanges: DHCP_POLICY_FIELDS_TO_UPDATE = 8
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDescr: DHCP_POLICY_FIELDS_TO_UPDATE = 16
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyStatus: DHCP_POLICY_FIELDS_TO_UPDATE = 32
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDnsSuffix: DHCP_POLICY_FIELDS_TO_UPDATE = 64
class DHCP_PROPERTY(Structure):
    ID: win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_ID
    Type: win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_TYPE
    Value: _DHCP_PROPERTY_VALUE_UNION
    class _DHCP_PROPERTY_VALUE_UNION(Union):
        ByteValue: Byte
        WordValue: UInt16
        DWordValue: UInt32
        StringValue: win32more.Foundation.PWSTR
        BinaryValue: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
class DHCP_PROPERTY_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_PROPERTY_head)
DHCP_PROPERTY_ID = Int32
DHCP_PROPERTY_ID_DhcpPropIdPolicyDnsSuffix: DHCP_PROPERTY_ID = 0
DHCP_PROPERTY_ID_DhcpPropIdClientAddressStateEx: DHCP_PROPERTY_ID = 1
DHCP_PROPERTY_TYPE = Int32
DHCP_PROPERTY_TYPE_DhcpPropTypeByte: DHCP_PROPERTY_TYPE = 0
DHCP_PROPERTY_TYPE_DhcpPropTypeWord: DHCP_PROPERTY_TYPE = 1
DHCP_PROPERTY_TYPE_DhcpPropTypeDword: DHCP_PROPERTY_TYPE = 2
DHCP_PROPERTY_TYPE_DhcpPropTypeString: DHCP_PROPERTY_TYPE = 3
DHCP_PROPERTY_TYPE_DhcpPropTypeBinary: DHCP_PROPERTY_TYPE = 4
class DHCP_RESERVATION_INFO_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_INFO_head))
class DHCP_RESERVED_SCOPE(Structure):
    ReservedIpAddress: UInt32
    ReservedIpSubnetAddress: UInt32
class DHCP_RESERVED_SCOPE6(Structure):
    ReservedIpAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    ReservedIpSubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
DHCP_SCAN_FLAG = Int32
DHCP_SCAN_FLAG_DhcpRegistryFix: DHCP_SCAN_FLAG = 0
DHCP_SCAN_FLAG_DhcpDatabaseFix: DHCP_SCAN_FLAG = 1
class DHCP_SCAN_ITEM(Structure):
    IpAddress: UInt32
    ScanFlag: win32more.NetworkManagement.Dhcp.DHCP_SCAN_FLAG
class DHCP_SCAN_LIST(Structure):
    NumScanItems: UInt32
    ScanItems: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SCAN_ITEM_head)
class DHCP_SEARCH_INFO(Structure):
    SearchType: win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_TYPE
    SearchInfo: DHCP_CLIENT_SEARCH_UNION
    class DHCP_CLIENT_SEARCH_UNION(Union):
        ClientIpAddress: UInt32
        ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        ClientName: win32more.Foundation.PWSTR
DHCP_SEARCH_INFO_TYPE = Int32
DHCP_SEARCH_INFO_TYPE_DhcpClientIpAddress: DHCP_SEARCH_INFO_TYPE = 0
DHCP_SEARCH_INFO_TYPE_DhcpClientHardwareAddress: DHCP_SEARCH_INFO_TYPE = 1
DHCP_SEARCH_INFO_TYPE_DhcpClientName: DHCP_SEARCH_INFO_TYPE = 2
DHCP_SEARCH_INFO_TYPE_V6 = Int32
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientIpAddress: DHCP_SEARCH_INFO_TYPE_V6 = 0
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientDUID: DHCP_SEARCH_INFO_TYPE_V6 = 1
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientName: DHCP_SEARCH_INFO_TYPE_V6 = 2
class DHCP_SEARCH_INFO_V6(Structure):
    SearchType: win32more.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_TYPE_V6
    SearchInfo: _DHCP_CLIENT_SEARCH_UNION_V6
    class _DHCP_CLIENT_SEARCH_UNION_V6(Union):
        ClientIpAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
        ClientDUID: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        ClientName: win32more.Foundation.PWSTR
class DHCP_SERVER_CONFIG_INFO(Structure):
    APIProtocolSupport: UInt32
    DatabaseName: win32more.Foundation.PWSTR
    DatabasePath: win32more.Foundation.PWSTR
    BackupPath: win32more.Foundation.PWSTR
    BackupInterval: UInt32
    DatabaseLoggingFlag: UInt32
    RestoreFlag: UInt32
    DatabaseCleanupInterval: UInt32
    DebugFlag: UInt32
class DHCP_SERVER_CONFIG_INFO_V4(Structure):
    APIProtocolSupport: UInt32
    DatabaseName: win32more.Foundation.PWSTR
    DatabasePath: win32more.Foundation.PWSTR
    BackupPath: win32more.Foundation.PWSTR
    BackupInterval: UInt32
    DatabaseLoggingFlag: UInt32
    RestoreFlag: UInt32
    DatabaseCleanupInterval: UInt32
    DebugFlag: UInt32
    dwPingRetries: UInt32
    cbBootTableString: UInt32
    wszBootTableString: win32more.Foundation.PWSTR
    fAuditLog: win32more.Foundation.BOOL
class DHCP_SERVER_CONFIG_INFO_V6(Structure):
    UnicastFlag: win32more.Foundation.BOOL
    RapidCommitFlag: win32more.Foundation.BOOL
    PreferredLifetime: UInt32
    ValidLifetime: UInt32
    T1: UInt32
    T2: UInt32
    PreferredLifetimeIATA: UInt32
    ValidLifetimeIATA: UInt32
    fAuditLog: win32more.Foundation.BOOL
class DHCP_SERVER_CONFIG_INFO_VQ(Structure):
    APIProtocolSupport: UInt32
    DatabaseName: win32more.Foundation.PWSTR
    DatabasePath: win32more.Foundation.PWSTR
    BackupPath: win32more.Foundation.PWSTR
    BackupInterval: UInt32
    DatabaseLoggingFlag: UInt32
    RestoreFlag: UInt32
    DatabaseCleanupInterval: UInt32
    DebugFlag: UInt32
    dwPingRetries: UInt32
    cbBootTableString: UInt32
    wszBootTableString: win32more.Foundation.PWSTR
    fAuditLog: win32more.Foundation.BOOL
    QuarantineOn: win32more.Foundation.BOOL
    QuarDefFail: UInt32
    QuarRuntimeStatus: win32more.Foundation.BOOL
class DHCP_SERVER_OPTIONS(Structure):
    MessageType: c_char_p_no
    SubnetMask: POINTER(UInt32)
    RequestedAddress: POINTER(UInt32)
    RequestLeaseTime: POINTER(UInt32)
    OverlayFields: c_char_p_no
    RouterAddress: POINTER(UInt32)
    Server: POINTER(UInt32)
    ParameterRequestList: c_char_p_no
    ParameterRequestListLength: UInt32
    MachineName: win32more.Foundation.PSTR
    MachineNameLength: UInt32
    ClientHardwareAddressType: Byte
    ClientHardwareAddressLength: Byte
    ClientHardwareAddress: c_char_p_no
    ClassIdentifier: win32more.Foundation.PSTR
    ClassIdentifierLength: UInt32
    VendorClass: c_char_p_no
    VendorClassLength: UInt32
    DNSFlags: UInt32
    DNSNameLength: UInt32
    DNSName: c_char_p_no
    DSDomainNameRequested: win32more.Foundation.BOOLEAN
    DSDomainName: win32more.Foundation.PSTR
    DSDomainNameLen: UInt32
    ScopeId: POINTER(UInt32)
class DHCP_SERVER_SPECIFIC_STRINGS(Structure):
    DefaultVendorClassName: win32more.Foundation.PWSTR
    DefaultUserClassName: win32more.Foundation.PWSTR
class DHCP_SUBNET_ELEMENT_DATA(Structure):
    ElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE
    Element: DHCP_SUBNET_ELEMENT_UNION
    class DHCP_SUBNET_ELEMENT_UNION(Union):
        IpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        SecondaryHost: POINTER(win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)
        ReservedIp: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_head)
        ExcludeIpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        IpUsedCluster: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)
class DHCP_SUBNET_ELEMENT_DATA_V4(Structure):
    ElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE
    Element: DHCP_SUBNET_ELEMENT_UNION_V4
    class DHCP_SUBNET_ELEMENT_UNION_V4(Union):
        IpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        SecondaryHost: POINTER(win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)
        ReservedIp: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V4_head)
        ExcludeIpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        IpUsedCluster: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)
class DHCP_SUBNET_ELEMENT_DATA_V5(Structure):
    ElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE
    Element: _DHCP_SUBNET_ELEMENT_UNION_V5
    class _DHCP_SUBNET_ELEMENT_UNION_V5(Union):
        IpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_BOOTP_IP_RANGE_head)
        SecondaryHost: POINTER(win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)
        ReservedIp: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V4_head)
        ExcludeIpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        IpUsedCluster: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)
class DHCP_SUBNET_ELEMENT_DATA_V6(Structure):
    ElementType: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE_V6
    Element: DHCP_SUBNET_ELEMENT_UNION_V6
    class DHCP_SUBNET_ELEMENT_UNION_V6(Union):
        IpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_V6_head)
        ReservedIp: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V6_head)
        ExcludeIpRange: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IP_RANGE_V6_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head)
DHCP_SUBNET_ELEMENT_TYPE = Int32
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRanges: DHCP_SUBNET_ELEMENT_TYPE = 0
DHCP_SUBNET_ELEMENT_TYPE_DhcpSecondaryHosts: DHCP_SUBNET_ELEMENT_TYPE = 1
DHCP_SUBNET_ELEMENT_TYPE_DhcpReservedIps: DHCP_SUBNET_ELEMENT_TYPE = 2
DHCP_SUBNET_ELEMENT_TYPE_DhcpExcludedIpRanges: DHCP_SUBNET_ELEMENT_TYPE = 3
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpUsedClusters: DHCP_SUBNET_ELEMENT_TYPE = 4
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpOnly: DHCP_SUBNET_ELEMENT_TYPE = 5
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpBootp: DHCP_SUBNET_ELEMENT_TYPE = 6
DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesBootpOnly: DHCP_SUBNET_ELEMENT_TYPE = 7
DHCP_SUBNET_ELEMENT_TYPE_V6 = Int32
DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6IpRanges: DHCP_SUBNET_ELEMENT_TYPE_V6 = 0
DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ReservedIps: DHCP_SUBNET_ELEMENT_TYPE_V6 = 1
DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ExcludedIpRanges: DHCP_SUBNET_ELEMENT_TYPE_V6 = 2
class DHCP_SUBNET_ELEMENT_UNION(Union):
    pass
class DHCP_SUBNET_ELEMENT_UNION_V4(Union):
    pass
class DHCP_SUBNET_ELEMENT_UNION_V6(Union):
    pass
class DHCP_SUBNET_INFO(Structure):
    SubnetAddress: UInt32
    SubnetMask: UInt32
    SubnetName: win32more.Foundation.PWSTR
    SubnetComment: win32more.Foundation.PWSTR
    PrimaryHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    SubnetState: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_STATE
class DHCP_SUBNET_INFO_V6(Structure):
    SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    Prefix: UInt32
    Preference: UInt16
    SubnetName: win32more.Foundation.PWSTR
    SubnetComment: win32more.Foundation.PWSTR
    State: UInt32
    ScopeId: UInt32
class DHCP_SUBNET_INFO_VQ(Structure):
    SubnetAddress: UInt32
    SubnetMask: UInt32
    SubnetName: win32more.Foundation.PWSTR
    SubnetComment: win32more.Foundation.PWSTR
    PrimaryHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    SubnetState: win32more.NetworkManagement.Dhcp.DHCP_SUBNET_STATE
    QuarantineOn: UInt32
    Reserved1: UInt32
    Reserved2: UInt32
    Reserved3: Int64
    Reserved4: Int64
DHCP_SUBNET_STATE = Int32
DHCP_SUBNET_STATE_DhcpSubnetEnabled: DHCP_SUBNET_STATE = 0
DHCP_SUBNET_STATE_DhcpSubnetDisabled: DHCP_SUBNET_STATE = 1
DHCP_SUBNET_STATE_DhcpSubnetEnabledSwitched: DHCP_SUBNET_STATE = 2
DHCP_SUBNET_STATE_DhcpSubnetDisabledSwitched: DHCP_SUBNET_STATE = 3
DHCP_SUBNET_STATE_DhcpSubnetInvalidState: DHCP_SUBNET_STATE = 4
class DHCP_SUPER_SCOPE_TABLE(Structure):
    cEntries: UInt32
    pEntries: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_ENTRY_head)
class DHCP_SUPER_SCOPE_TABLE_ENTRY(Structure):
    SubnetAddress: UInt32
    SuperScopeNumber: UInt32
    NextInSuperScope: UInt32
    SuperScopeName: win32more.Foundation.PWSTR
class DHCPAPI_PARAMS(Structure):
    Flags: UInt32
    OptionId: UInt32
    IsVendor: win32more.Foundation.BOOL
    Data: c_char_p_no
    nBytesData: UInt32
class DHCPCAPI_CLASSID(Structure):
    Flags: UInt32
    Data: c_char_p_no
    nBytesData: UInt32
class DHCPCAPI_PARAMS_ARRAY(Structure):
    nParams: UInt32
    Params: POINTER(win32more.NetworkManagement.Dhcp.DHCPAPI_PARAMS_head)
class DHCPDS_SERVER(Structure):
    Version: UInt32
    ServerName: win32more.Foundation.PWSTR
    ServerAddress: UInt32
    Flags: UInt32
    State: UInt32
    DsLocation: win32more.Foundation.PWSTR
    DsLocType: UInt32
class DHCPDS_SERVERS(Structure):
    Flags: UInt32
    NumElements: UInt32
    Servers: POINTER(win32more.NetworkManagement.Dhcp.DHCPDS_SERVER_head)
class DHCPV4_FAILOVER_CLIENT_INFO(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: win32more.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: win32more.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: win32more.Foundation.BOOL
    SentPotExpTime: UInt32
    AckPotExpTime: UInt32
    RecvPotExpTime: UInt32
    StartTime: UInt32
    CltLastTransTime: UInt32
    LastBndUpdTime: UInt32
    BndMsgStatus: UInt32
    PolicyName: win32more.Foundation.PWSTR
    Flags: Byte
class DHCPV4_FAILOVER_CLIENT_INFO_ARRAY(Structure):
    NumElements: UInt32
    Clients: POINTER(POINTER(win32more.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_head))
class DHCPV4_FAILOVER_CLIENT_INFO_EX(Structure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: win32more.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: win32more.Foundation.PWSTR
    ClientComment: win32more.Foundation.PWSTR
    ClientLeaseExpires: win32more.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: win32more.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: win32more.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: win32more.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: win32more.Foundation.BOOL
    SentPotExpTime: UInt32
    AckPotExpTime: UInt32
    RecvPotExpTime: UInt32
    StartTime: UInt32
    CltLastTransTime: UInt32
    LastBndUpdTime: UInt32
    BndMsgStatus: UInt32
    PolicyName: win32more.Foundation.PWSTR
    Flags: Byte
    AddressStateEx: UInt32
class DHCPV6_BIND_ELEMENT(Structure):
    Flags: UInt32
    fBoundToDHCPServer: win32more.Foundation.BOOL
    AdapterPrimaryAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    AdapterSubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    IfDescription: win32more.Foundation.PWSTR
    IpV6IfIndex: UInt32
    IfIdSize: UInt32
    IfId: c_char_p_no
class DHCPV6_BIND_ELEMENT_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_head)
class DHCPV6_IP_ARRAY(Structure):
    NumElements: UInt32
    Elements: POINTER(win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS_head)
DHCPV6_STATELESS_PARAM_TYPE = Int32
DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessPurgeInterval: DHCPV6_STATELESS_PARAM_TYPE = 1
DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessStatus: DHCPV6_STATELESS_PARAM_TYPE = 2
class DHCPV6_STATELESS_PARAMS(Structure):
    Status: win32more.Foundation.BOOL
    PurgeInterval: UInt32
class DHCPV6_STATELESS_SCOPE_STATS(Structure):
    SubnetAddress: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    NumStatelessClientsAdded: UInt64
    NumStatelessClientsRemoved: UInt64
class DHCPV6_STATELESS_STATS(Structure):
    NumScopes: UInt32
    ScopeStats: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6_STATELESS_SCOPE_STATS_head)
class DHCPV6CAPI_CLASSID(Structure):
    Flags: UInt32
    Data: c_char_p_no
    nBytesData: UInt32
class DHCPV6CAPI_PARAMS(Structure):
    Flags: UInt32
    OptionId: UInt32
    IsVendor: win32more.Foundation.BOOL
    Data: c_char_p_no
    nBytesData: UInt32
class DHCPV6CAPI_PARAMS_ARRAY(Structure):
    nParams: UInt32
    Params: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_head)
class DHCPV6Prefix(Structure):
    prefix: Byte * 16
    prefixLength: UInt32
    preferredLifeTime: UInt32
    validLifeTime: UInt32
    status: win32more.NetworkManagement.Dhcp.StatusCode
class DHCPV6PrefixLeaseInformation(Structure):
    nPrefixes: UInt32
    prefixArray: POINTER(win32more.NetworkManagement.Dhcp.DHCPV6Prefix_head)
    iaid: UInt32
    T1: Int64
    T2: Int64
    MaxLeaseExpirationTime: Int64
    LastRenewalTime: Int64
    status: win32more.NetworkManagement.Dhcp.StatusCode
    ServerId: c_char_p_no
    ServerIdLen: UInt32
class DWORD_DWORD(Structure):
    DWord1: UInt32
    DWord2: UInt32
FSM_STATE = Int32
NO_STATE: FSM_STATE = 0
INIT: FSM_STATE = 1
STARTUP: FSM_STATE = 2
NORMAL: FSM_STATE = 3
COMMUNICATION_INT: FSM_STATE = 4
PARTNER_DOWN: FSM_STATE = 5
POTENTIAL_CONFLICT: FSM_STATE = 6
CONFLICT_DONE: FSM_STATE = 7
RESOLUTION_INT: FSM_STATE = 8
RECOVER: FSM_STATE = 9
RECOVER_WAIT: FSM_STATE = 10
RECOVER_DONE: FSM_STATE = 11
PAUSED: FSM_STATE = 12
SHUTDOWN: FSM_STATE = 13
@winfunctype_pointer
def LPDHCP_CONTROL(dwControlCode: UInt32, lpReserved: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_DELETE_CLIENT(IpAddress: UInt32, HwAddress: c_char_p_no, HwAddressLength: UInt32, Reserved: UInt32, ClientType: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_DROP_SEND(Packet: POINTER(c_char_p_no), PacketSize: POINTER(UInt32), ControlCode: UInt32, IpAddress: UInt32, Reserved: c_void_p, PktContext: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_ENTRY_POINT_FUNC(ChainDlls: win32more.Foundation.PWSTR, CalloutVersion: UInt32, CalloutTbl: POINTER(win32more.NetworkManagement.Dhcp.DHCP_CALLOUT_TABLE_head)) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_GIVE_ADDRESS(Packet: c_char_p_no, PacketSize: UInt32, ControlCode: UInt32, IpAddress: UInt32, AltAddress: UInt32, AddrType: UInt32, LeaseTime: UInt32, Reserved: c_void_p, PktContext: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_HANDLE_OPTIONS(Packet: c_char_p_no, PacketSize: UInt32, Reserved: c_void_p, PktContext: c_void_p, ServerOptions: POINTER(win32more.NetworkManagement.Dhcp.DHCP_SERVER_OPTIONS_head)) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_NEWPKT(Packet: POINTER(c_char_p_no), PacketSize: POINTER(UInt32), IpAddress: UInt32, Reserved: c_void_p, PktContext: POINTER(c_void_p), ProcessIt: POINTER(Int32)) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_PROB(Packet: c_char_p_no, PacketSize: UInt32, ControlCode: UInt32, IpAddress: UInt32, AltAddress: UInt32, Reserved: c_void_p, PktContext: c_void_p) -> UInt32: ...
QuarantineStatus = Int32
NOQUARANTINE: QuarantineStatus = 0
RESTRICTEDACCESS: QuarantineStatus = 1
DROPPACKET: QuarantineStatus = 2
PROBATION: QuarantineStatus = 3
EXEMPT: QuarantineStatus = 4
DEFAULTQUARSETTING: QuarantineStatus = 5
NOQUARINFO: QuarantineStatus = 6
class SCOPE_MIB_INFO(Structure):
    Subnet: UInt32
    NumAddressesInuse: UInt32
    NumAddressesFree: UInt32
    NumPendingOffers: UInt32
class SCOPE_MIB_INFO_V5(Structure):
    Subnet: UInt32
    NumAddressesInuse: UInt32
    NumAddressesFree: UInt32
    NumPendingOffers: UInt32
class SCOPE_MIB_INFO_V6(Structure):
    Subnet: win32more.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    NumAddressesInuse: UInt64
    NumAddressesFree: UInt64
    NumPendingAdvertises: UInt64
class SCOPE_MIB_INFO_VQ(Structure):
    Subnet: UInt32
    NumAddressesInuse: UInt32
    NumAddressesFree: UInt32
    NumPendingOffers: UInt32
    QtnNumLeases: UInt32
    QtnPctQtnLeases: UInt32
    QtnProbationLeases: UInt32
    QtnNonQtnLeases: UInt32
    QtnExemptLeases: UInt32
    QtnCapableClients: UInt32
StatusCode = Int32
STATUS_NO_ERROR: StatusCode = 0
STATUS_UNSPECIFIED_FAILURE: StatusCode = 1
STATUS_NO_BINDING: StatusCode = 3
STATUS_NOPREFIX_AVAIL: StatusCode = 6
make_head(_module, 'DATE_TIME')
make_head(_module, 'DHCP_ADDR_PATTERN')
make_head(_module, 'DHCP_ALL_OPTION_VALUES')
make_head(_module, 'DHCP_ALL_OPTION_VALUES_PB')
make_head(_module, 'DHCP_ALL_OPTIONS')
make_head(_module, 'DHCP_ATTRIB')
make_head(_module, 'DHCP_ATTRIB_ARRAY')
make_head(_module, 'DHCP_BINARY_DATA')
make_head(_module, 'DHCP_BIND_ELEMENT')
make_head(_module, 'DHCP_BIND_ELEMENT_ARRAY')
make_head(_module, 'DHCP_BOOTP_IP_RANGE')
make_head(_module, 'DHCP_CALLOUT_TABLE')
make_head(_module, 'DHCP_CLASS_INFO')
make_head(_module, 'DHCP_CLASS_INFO_ARRAY')
make_head(_module, 'DHCP_CLASS_INFO_ARRAY_V6')
make_head(_module, 'DHCP_CLASS_INFO_V6')
make_head(_module, 'DHCP_CLIENT_FILTER_STATUS_INFO')
make_head(_module, 'DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY')
make_head(_module, 'DHCP_CLIENT_INFO')
make_head(_module, 'DHCP_CLIENT_INFO_ARRAY')
make_head(_module, 'DHCP_CLIENT_INFO_ARRAY_V4')
make_head(_module, 'DHCP_CLIENT_INFO_ARRAY_V5')
make_head(_module, 'DHCP_CLIENT_INFO_ARRAY_V6')
make_head(_module, 'DHCP_CLIENT_INFO_ARRAY_VQ')
make_head(_module, 'DHCP_CLIENT_INFO_EX')
make_head(_module, 'DHCP_CLIENT_INFO_EX_ARRAY')
make_head(_module, 'DHCP_CLIENT_INFO_PB')
make_head(_module, 'DHCP_CLIENT_INFO_PB_ARRAY')
make_head(_module, 'DHCP_CLIENT_INFO_V4')
make_head(_module, 'DHCP_CLIENT_INFO_V5')
make_head(_module, 'DHCP_CLIENT_INFO_V6')
make_head(_module, 'DHCP_CLIENT_INFO_VQ')
make_head(_module, 'DHCP_CLIENT_SEARCH_UNION')
make_head(_module, 'DHCP_FAILOVER_RELATIONSHIP')
make_head(_module, 'DHCP_FAILOVER_RELATIONSHIP_ARRAY')
make_head(_module, 'DHCP_FAILOVER_STATISTICS')
make_head(_module, 'DHCP_FILTER_ADD_INFO')
make_head(_module, 'DHCP_FILTER_ENUM_INFO')
make_head(_module, 'DHCP_FILTER_GLOBAL_INFO')
make_head(_module, 'DHCP_FILTER_RECORD')
make_head(_module, 'DHCP_HOST_INFO')
make_head(_module, 'DHCP_HOST_INFO_V6')
make_head(_module, 'DHCP_IP_ARRAY')
make_head(_module, 'DHCP_IP_CLUSTER')
make_head(_module, 'DHCP_IP_RANGE')
make_head(_module, 'DHCP_IP_RANGE_ARRAY')
make_head(_module, 'DHCP_IP_RANGE_V6')
make_head(_module, 'DHCP_IP_RESERVATION')
make_head(_module, 'DHCP_IP_RESERVATION_INFO')
make_head(_module, 'DHCP_IP_RESERVATION_V4')
make_head(_module, 'DHCP_IP_RESERVATION_V6')
make_head(_module, 'DHCP_IPV6_ADDRESS')
make_head(_module, 'DHCP_MIB_INFO')
make_head(_module, 'DHCP_MIB_INFO_V5')
make_head(_module, 'DHCP_MIB_INFO_V6')
make_head(_module, 'DHCP_MIB_INFO_VQ')
make_head(_module, 'DHCP_OPTION')
make_head(_module, 'DHCP_OPTION_ARRAY')
make_head(_module, 'DHCP_OPTION_DATA')
make_head(_module, 'DHCP_OPTION_DATA_ELEMENT')
make_head(_module, 'DHCP_OPTION_ELEMENT_UNION')
make_head(_module, 'DHCP_OPTION_LIST')
make_head(_module, 'DHCP_OPTION_SCOPE_INFO')
make_head(_module, 'DHCP_OPTION_SCOPE_INFO6')
make_head(_module, 'DHCP_OPTION_SCOPE_UNION6')
make_head(_module, 'DHCP_OPTION_VALUE')
make_head(_module, 'DHCP_OPTION_VALUE_ARRAY')
make_head(_module, 'DHCP_PERF_STATS')
make_head(_module, 'DHCP_POL_COND')
make_head(_module, 'DHCP_POL_COND_ARRAY')
make_head(_module, 'DHCP_POL_EXPR')
make_head(_module, 'DHCP_POL_EXPR_ARRAY')
make_head(_module, 'DHCP_POLICY')
make_head(_module, 'DHCP_POLICY_ARRAY')
make_head(_module, 'DHCP_POLICY_EX')
make_head(_module, 'DHCP_POLICY_EX_ARRAY')
make_head(_module, 'DHCP_PROPERTY')
make_head(_module, 'DHCP_PROPERTY_ARRAY')
make_head(_module, 'DHCP_RESERVATION_INFO_ARRAY')
make_head(_module, 'DHCP_RESERVED_SCOPE')
make_head(_module, 'DHCP_RESERVED_SCOPE6')
make_head(_module, 'DHCP_SCAN_ITEM')
make_head(_module, 'DHCP_SCAN_LIST')
make_head(_module, 'DHCP_SEARCH_INFO')
make_head(_module, 'DHCP_SEARCH_INFO_V6')
make_head(_module, 'DHCP_SERVER_CONFIG_INFO')
make_head(_module, 'DHCP_SERVER_CONFIG_INFO_V4')
make_head(_module, 'DHCP_SERVER_CONFIG_INFO_V6')
make_head(_module, 'DHCP_SERVER_CONFIG_INFO_VQ')
make_head(_module, 'DHCP_SERVER_OPTIONS')
make_head(_module, 'DHCP_SERVER_SPECIFIC_STRINGS')
make_head(_module, 'DHCP_SUBNET_ELEMENT_DATA')
make_head(_module, 'DHCP_SUBNET_ELEMENT_DATA_V4')
make_head(_module, 'DHCP_SUBNET_ELEMENT_DATA_V5')
make_head(_module, 'DHCP_SUBNET_ELEMENT_DATA_V6')
make_head(_module, 'DHCP_SUBNET_ELEMENT_INFO_ARRAY')
make_head(_module, 'DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4')
make_head(_module, 'DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5')
make_head(_module, 'DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6')
make_head(_module, 'DHCP_SUBNET_ELEMENT_UNION')
make_head(_module, 'DHCP_SUBNET_ELEMENT_UNION_V4')
make_head(_module, 'DHCP_SUBNET_ELEMENT_UNION_V6')
make_head(_module, 'DHCP_SUBNET_INFO')
make_head(_module, 'DHCP_SUBNET_INFO_V6')
make_head(_module, 'DHCP_SUBNET_INFO_VQ')
make_head(_module, 'DHCP_SUPER_SCOPE_TABLE')
make_head(_module, 'DHCP_SUPER_SCOPE_TABLE_ENTRY')
make_head(_module, 'DHCPAPI_PARAMS')
make_head(_module, 'DHCPCAPI_CLASSID')
make_head(_module, 'DHCPCAPI_PARAMS_ARRAY')
make_head(_module, 'DHCPDS_SERVER')
make_head(_module, 'DHCPDS_SERVERS')
make_head(_module, 'DHCPV4_FAILOVER_CLIENT_INFO')
make_head(_module, 'DHCPV4_FAILOVER_CLIENT_INFO_ARRAY')
make_head(_module, 'DHCPV4_FAILOVER_CLIENT_INFO_EX')
make_head(_module, 'DHCPV6_BIND_ELEMENT')
make_head(_module, 'DHCPV6_BIND_ELEMENT_ARRAY')
make_head(_module, 'DHCPV6_IP_ARRAY')
make_head(_module, 'DHCPV6_STATELESS_PARAMS')
make_head(_module, 'DHCPV6_STATELESS_SCOPE_STATS')
make_head(_module, 'DHCPV6_STATELESS_STATS')
make_head(_module, 'DHCPV6CAPI_CLASSID')
make_head(_module, 'DHCPV6CAPI_PARAMS')
make_head(_module, 'DHCPV6CAPI_PARAMS_ARRAY')
make_head(_module, 'DHCPV6Prefix')
make_head(_module, 'DHCPV6PrefixLeaseInformation')
make_head(_module, 'DWORD_DWORD')
make_head(_module, 'LPDHCP_CONTROL')
make_head(_module, 'LPDHCP_DELETE_CLIENT')
make_head(_module, 'LPDHCP_DROP_SEND')
make_head(_module, 'LPDHCP_ENTRY_POINT_FUNC')
make_head(_module, 'LPDHCP_GIVE_ADDRESS')
make_head(_module, 'LPDHCP_HANDLE_OPTIONS')
make_head(_module, 'LPDHCP_NEWPKT')
make_head(_module, 'LPDHCP_PROB')
make_head(_module, 'SCOPE_MIB_INFO')
make_head(_module, 'SCOPE_MIB_INFO_V5')
make_head(_module, 'SCOPE_MIB_INFO_V6')
make_head(_module, 'SCOPE_MIB_INFO_VQ')
__all__ = [
    "ADDRESS_TYPE_IANA",
    "ADDRESS_TYPE_IATA",
    "CHANGESTATE",
    "CLIENT_TYPE_BOOTP",
    "CLIENT_TYPE_DHCP",
    "CLIENT_TYPE_NONE",
    "CLIENT_TYPE_RESERVATION_FLAG",
    "CLIENT_TYPE_UNSPECIFIED",
    "COMMUNICATION_INT",
    "CONFLICT_DONE",
    "DATE_TIME",
    "DEFAULTQUARSETTING",
    "DHCPAPI_PARAMS",
    "DHCPCAPI_CLASSID",
    "DHCPCAPI_DEREGISTER_HANDLE_EVENT",
    "DHCPCAPI_PARAMS_ARRAY",
    "DHCPCAPI_REGISTER_HANDLE_EVENT",
    "DHCPCAPI_REQUEST_ASYNCHRONOUS",
    "DHCPCAPI_REQUEST_CANCEL",
    "DHCPCAPI_REQUEST_MASK",
    "DHCPCAPI_REQUEST_PERSISTENT",
    "DHCPCAPI_REQUEST_SYNCHRONOUS",
    "DHCPDS_SERVER",
    "DHCPDS_SERVERS",
    "DHCPV4_FAILOVER_CLIENT_INFO",
    "DHCPV4_FAILOVER_CLIENT_INFO_ARRAY",
    "DHCPV4_FAILOVER_CLIENT_INFO_EX",
    "DHCPV6CAPI_CLASSID",
    "DHCPV6CAPI_PARAMS",
    "DHCPV6CAPI_PARAMS_ARRAY",
    "DHCPV6Prefix",
    "DHCPV6PrefixLeaseInformation",
    "DHCPV6_BIND_ELEMENT",
    "DHCPV6_BIND_ELEMENT_ARRAY",
    "DHCPV6_IP_ARRAY",
    "DHCPV6_OPTION_CLIENTID",
    "DHCPV6_OPTION_DNS_SERVERS",
    "DHCPV6_OPTION_DOMAIN_LIST",
    "DHCPV6_OPTION_IA_NA",
    "DHCPV6_OPTION_IA_PD",
    "DHCPV6_OPTION_IA_TA",
    "DHCPV6_OPTION_NISP_DOMAIN_NAME",
    "DHCPV6_OPTION_NISP_SERVERS",
    "DHCPV6_OPTION_NIS_DOMAIN_NAME",
    "DHCPV6_OPTION_NIS_SERVERS",
    "DHCPV6_OPTION_ORO",
    "DHCPV6_OPTION_PREFERENCE",
    "DHCPV6_OPTION_RAPID_COMMIT",
    "DHCPV6_OPTION_RECONF_MSG",
    "DHCPV6_OPTION_SERVERID",
    "DHCPV6_OPTION_SIP_SERVERS_ADDRS",
    "DHCPV6_OPTION_SIP_SERVERS_NAMES",
    "DHCPV6_OPTION_UNICAST",
    "DHCPV6_OPTION_USER_CLASS",
    "DHCPV6_OPTION_VENDOR_CLASS",
    "DHCPV6_OPTION_VENDOR_OPTS",
    "DHCPV6_STATELESS_PARAMS",
    "DHCPV6_STATELESS_PARAM_TYPE",
    "DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessPurgeInterval",
    "DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessStatus",
    "DHCPV6_STATELESS_SCOPE_STATS",
    "DHCPV6_STATELESS_STATS",
    "DHCP_ADDR_PATTERN",
    "DHCP_ALL_OPTIONS",
    "DHCP_ALL_OPTION_VALUES",
    "DHCP_ALL_OPTION_VALUES_PB",
    "DHCP_ATTRIB",
    "DHCP_ATTRIB_ARRAY",
    "DHCP_ATTRIB_BOOL_IS_ADMIN",
    "DHCP_ATTRIB_BOOL_IS_BINDING_AWARE",
    "DHCP_ATTRIB_BOOL_IS_DYNBOOTP",
    "DHCP_ATTRIB_BOOL_IS_PART_OF_DSDC",
    "DHCP_ATTRIB_BOOL_IS_ROGUE",
    "DHCP_ATTRIB_TYPE_BOOL",
    "DHCP_ATTRIB_TYPE_ULONG",
    "DHCP_ATTRIB_ULONG_RESTORE_STATUS",
    "DHCP_BINARY_DATA",
    "DHCP_BIND_ELEMENT",
    "DHCP_BIND_ELEMENT_ARRAY",
    "DHCP_BOOTP_IP_RANGE",
    "DHCP_CALLOUT_ENTRY_POINT",
    "DHCP_CALLOUT_LIST_KEY",
    "DHCP_CALLOUT_LIST_VALUE",
    "DHCP_CALLOUT_TABLE",
    "DHCP_CLASS_INFO",
    "DHCP_CLASS_INFO_ARRAY",
    "DHCP_CLASS_INFO_ARRAY_V6",
    "DHCP_CLASS_INFO_V6",
    "DHCP_CLIENT_BOOTP",
    "DHCP_CLIENT_DHCP",
    "DHCP_CLIENT_FILTER_STATUS_INFO",
    "DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY",
    "DHCP_CLIENT_INFO",
    "DHCP_CLIENT_INFO_ARRAY",
    "DHCP_CLIENT_INFO_ARRAY_V4",
    "DHCP_CLIENT_INFO_ARRAY_V5",
    "DHCP_CLIENT_INFO_ARRAY_V6",
    "DHCP_CLIENT_INFO_ARRAY_VQ",
    "DHCP_CLIENT_INFO_EX",
    "DHCP_CLIENT_INFO_EX_ARRAY",
    "DHCP_CLIENT_INFO_PB",
    "DHCP_CLIENT_INFO_PB_ARRAY",
    "DHCP_CLIENT_INFO_V4",
    "DHCP_CLIENT_INFO_V5",
    "DHCP_CLIENT_INFO_V6",
    "DHCP_CLIENT_INFO_VQ",
    "DHCP_CLIENT_SEARCH_UNION",
    "DHCP_CONTROL_CONTINUE",
    "DHCP_CONTROL_PAUSE",
    "DHCP_CONTROL_START",
    "DHCP_CONTROL_STOP",
    "DHCP_DROP_DUPLICATE",
    "DHCP_DROP_GEN_FAILURE",
    "DHCP_DROP_INTERNAL_ERROR",
    "DHCP_DROP_INVALID",
    "DHCP_DROP_NOADDRESS",
    "DHCP_DROP_NOMEM",
    "DHCP_DROP_NO_SUBNETS",
    "DHCP_DROP_PAUSED",
    "DHCP_DROP_PROCESSED",
    "DHCP_DROP_TIMEOUT",
    "DHCP_DROP_UNAUTH",
    "DHCP_DROP_WRONG_SERVER",
    "DHCP_ENDPOINT_FLAG_CANT_MODIFY",
    "DHCP_FAILOVER_DELETE_SCOPES",
    "DHCP_FAILOVER_MAX_NUM_ADD_SCOPES",
    "DHCP_FAILOVER_MAX_NUM_REL",
    "DHCP_FAILOVER_MODE",
    "DHCP_FAILOVER_MODE_HotStandby",
    "DHCP_FAILOVER_MODE_LoadBalance",
    "DHCP_FAILOVER_RELATIONSHIP",
    "DHCP_FAILOVER_RELATIONSHIP_ARRAY",
    "DHCP_FAILOVER_SERVER",
    "DHCP_FAILOVER_SERVER_PrimaryServer",
    "DHCP_FAILOVER_SERVER_SecondaryServer",
    "DHCP_FAILOVER_STATISTICS",
    "DHCP_FILTER_ADD_INFO",
    "DHCP_FILTER_ENUM_INFO",
    "DHCP_FILTER_GLOBAL_INFO",
    "DHCP_FILTER_LIST_TYPE",
    "DHCP_FILTER_LIST_TYPE_Allow",
    "DHCP_FILTER_LIST_TYPE_Deny",
    "DHCP_FILTER_RECORD",
    "DHCP_FLAGS_DONT_ACCESS_DS",
    "DHCP_FLAGS_DONT_DO_RPC",
    "DHCP_FLAGS_OPTION_IS_VENDOR",
    "DHCP_FORCE_FLAG",
    "DHCP_FORCE_FLAG_DhcpFailoverForce",
    "DHCP_FORCE_FLAG_DhcpFullForce",
    "DHCP_FORCE_FLAG_DhcpNoForce",
    "DHCP_GIVE_ADDRESS_NEW",
    "DHCP_GIVE_ADDRESS_OLD",
    "DHCP_HOST_INFO",
    "DHCP_HOST_INFO_V6",
    "DHCP_IPV6_ADDRESS",
    "DHCP_IP_ARRAY",
    "DHCP_IP_CLUSTER",
    "DHCP_IP_RANGE",
    "DHCP_IP_RANGE_ARRAY",
    "DHCP_IP_RANGE_V6",
    "DHCP_IP_RESERVATION",
    "DHCP_IP_RESERVATION_INFO",
    "DHCP_IP_RESERVATION_V4",
    "DHCP_IP_RESERVATION_V6",
    "DHCP_MAX_DELAY",
    "DHCP_MIB_INFO",
    "DHCP_MIB_INFO_V5",
    "DHCP_MIB_INFO_V6",
    "DHCP_MIB_INFO_VQ",
    "DHCP_MIN_DELAY",
    "DHCP_OPTION",
    "DHCP_OPTION_ARRAY",
    "DHCP_OPTION_DATA",
    "DHCP_OPTION_DATA_ELEMENT",
    "DHCP_OPTION_DATA_TYPE",
    "DHCP_OPTION_DATA_TYPE_DhcpBinaryDataOption",
    "DHCP_OPTION_DATA_TYPE_DhcpByteOption",
    "DHCP_OPTION_DATA_TYPE_DhcpDWordDWordOption",
    "DHCP_OPTION_DATA_TYPE_DhcpDWordOption",
    "DHCP_OPTION_DATA_TYPE_DhcpEncapsulatedDataOption",
    "DHCP_OPTION_DATA_TYPE_DhcpIpAddressOption",
    "DHCP_OPTION_DATA_TYPE_DhcpIpv6AddressOption",
    "DHCP_OPTION_DATA_TYPE_DhcpStringDataOption",
    "DHCP_OPTION_DATA_TYPE_DhcpWordOption",
    "DHCP_OPTION_ELEMENT_UNION",
    "DHCP_OPTION_LIST",
    "DHCP_OPTION_SCOPE_INFO",
    "DHCP_OPTION_SCOPE_INFO6",
    "DHCP_OPTION_SCOPE_TYPE",
    "DHCP_OPTION_SCOPE_TYPE6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpDefaultOptions6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpGlobalOptions6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpReservedOptions6",
    "DHCP_OPTION_SCOPE_TYPE6_DhcpScopeOptions6",
    "DHCP_OPTION_SCOPE_TYPE_DhcpDefaultOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpGlobalOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpMScopeOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpReservedOptions",
    "DHCP_OPTION_SCOPE_TYPE_DhcpSubnetOptions",
    "DHCP_OPTION_SCOPE_UNION6",
    "DHCP_OPTION_TYPE",
    "DHCP_OPTION_TYPE_DhcpArrayTypeOption",
    "DHCP_OPTION_TYPE_DhcpUnaryElementTypeOption",
    "DHCP_OPTION_VALUE",
    "DHCP_OPTION_VALUE_ARRAY",
    "DHCP_OPT_ENUM_IGNORE_VENDOR",
    "DHCP_OPT_ENUM_USE_CLASSNAME",
    "DHCP_PERF_STATS",
    "DHCP_POLICY",
    "DHCP_POLICY_ARRAY",
    "DHCP_POLICY_EX",
    "DHCP_POLICY_EX_ARRAY",
    "DHCP_POLICY_FIELDS_TO_UPDATE",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDescr",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDnsSuffix",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyExpr",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyName",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyOrder",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyRanges",
    "DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyStatus",
    "DHCP_POL_ATTR_TYPE",
    "DHCP_POL_ATTR_TYPE_DhcpAttrFqdn",
    "DHCP_POL_ATTR_TYPE_DhcpAttrFqdnSingleLabel",
    "DHCP_POL_ATTR_TYPE_DhcpAttrHWAddr",
    "DHCP_POL_ATTR_TYPE_DhcpAttrOption",
    "DHCP_POL_ATTR_TYPE_DhcpAttrSubOption",
    "DHCP_POL_COMPARATOR",
    "DHCP_POL_COMPARATOR_DhcpCompBeginsWith",
    "DHCP_POL_COMPARATOR_DhcpCompEndsWith",
    "DHCP_POL_COMPARATOR_DhcpCompEqual",
    "DHCP_POL_COMPARATOR_DhcpCompNotBeginWith",
    "DHCP_POL_COMPARATOR_DhcpCompNotEndWith",
    "DHCP_POL_COMPARATOR_DhcpCompNotEqual",
    "DHCP_POL_COND",
    "DHCP_POL_COND_ARRAY",
    "DHCP_POL_EXPR",
    "DHCP_POL_EXPR_ARRAY",
    "DHCP_POL_LOGIC_OPER",
    "DHCP_POL_LOGIC_OPER_DhcpLogicalAnd",
    "DHCP_POL_LOGIC_OPER_DhcpLogicalOr",
    "DHCP_PROB_CONFLICT",
    "DHCP_PROB_DECLINE",
    "DHCP_PROB_NACKED",
    "DHCP_PROB_RELEASE",
    "DHCP_PROPERTY",
    "DHCP_PROPERTY_ARRAY",
    "DHCP_PROPERTY_ID",
    "DHCP_PROPERTY_ID_DhcpPropIdClientAddressStateEx",
    "DHCP_PROPERTY_ID_DhcpPropIdPolicyDnsSuffix",
    "DHCP_PROPERTY_TYPE",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeBinary",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeByte",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeDword",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeString",
    "DHCP_PROPERTY_TYPE_DhcpPropTypeWord",
    "DHCP_RESERVATION_INFO_ARRAY",
    "DHCP_RESERVED_SCOPE",
    "DHCP_RESERVED_SCOPE6",
    "DHCP_SCAN_FLAG",
    "DHCP_SCAN_FLAG_DhcpDatabaseFix",
    "DHCP_SCAN_FLAG_DhcpRegistryFix",
    "DHCP_SCAN_ITEM",
    "DHCP_SCAN_LIST",
    "DHCP_SEARCH_INFO",
    "DHCP_SEARCH_INFO_TYPE",
    "DHCP_SEARCH_INFO_TYPE_DhcpClientHardwareAddress",
    "DHCP_SEARCH_INFO_TYPE_DhcpClientIpAddress",
    "DHCP_SEARCH_INFO_TYPE_DhcpClientName",
    "DHCP_SEARCH_INFO_TYPE_V6",
    "DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientDUID",
    "DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientIpAddress",
    "DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientName",
    "DHCP_SEARCH_INFO_V6",
    "DHCP_SEND_PACKET",
    "DHCP_SERVER_CONFIG_INFO",
    "DHCP_SERVER_CONFIG_INFO_V4",
    "DHCP_SERVER_CONFIG_INFO_V6",
    "DHCP_SERVER_CONFIG_INFO_VQ",
    "DHCP_SERVER_OPTIONS",
    "DHCP_SERVER_SPECIFIC_STRINGS",
    "DHCP_SUBNET_ELEMENT_DATA",
    "DHCP_SUBNET_ELEMENT_DATA_V4",
    "DHCP_SUBNET_ELEMENT_DATA_V5",
    "DHCP_SUBNET_ELEMENT_DATA_V6",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5",
    "DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6",
    "DHCP_SUBNET_ELEMENT_TYPE",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpExcludedIpRanges",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRanges",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesBootpOnly",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpBootp",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpRangesDhcpOnly",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpIpUsedClusters",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpReservedIps",
    "DHCP_SUBNET_ELEMENT_TYPE_DhcpSecondaryHosts",
    "DHCP_SUBNET_ELEMENT_TYPE_V6",
    "DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ExcludedIpRanges",
    "DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6IpRanges",
    "DHCP_SUBNET_ELEMENT_TYPE_V6_Dhcpv6ReservedIps",
    "DHCP_SUBNET_ELEMENT_UNION",
    "DHCP_SUBNET_ELEMENT_UNION_V4",
    "DHCP_SUBNET_ELEMENT_UNION_V6",
    "DHCP_SUBNET_INFO",
    "DHCP_SUBNET_INFO_V6",
    "DHCP_SUBNET_INFO_VQ",
    "DHCP_SUBNET_INFO_VQ_FLAG_QUARANTINE",
    "DHCP_SUBNET_STATE",
    "DHCP_SUBNET_STATE_DhcpSubnetDisabled",
    "DHCP_SUBNET_STATE_DhcpSubnetDisabledSwitched",
    "DHCP_SUBNET_STATE_DhcpSubnetEnabled",
    "DHCP_SUBNET_STATE_DhcpSubnetEnabledSwitched",
    "DHCP_SUBNET_STATE_DhcpSubnetInvalidState",
    "DHCP_SUPER_SCOPE_TABLE",
    "DHCP_SUPER_SCOPE_TABLE_ENTRY",
    "DNS_FLAG_CLEANUP_EXPIRED",
    "DNS_FLAG_DISABLE_PTR_UPDATE",
    "DNS_FLAG_ENABLED",
    "DNS_FLAG_HAS_DNS_SUFFIX",
    "DNS_FLAG_UPDATE_BOTH_ALWAYS",
    "DNS_FLAG_UPDATE_DHCID",
    "DNS_FLAG_UPDATE_DOWNLEVEL",
    "DROPPACKET",
    "DWORD_DWORD",
    "DhcpAddFilterV4",
    "DhcpAddSecurityGroup",
    "DhcpAddServer",
    "DhcpAddSubnetElement",
    "DhcpAddSubnetElementV4",
    "DhcpAddSubnetElementV5",
    "DhcpAddSubnetElementV6",
    "DhcpAuditLogGetParams",
    "DhcpAuditLogSetParams",
    "DhcpCApiCleanup",
    "DhcpCApiInitialize",
    "DhcpCreateClass",
    "DhcpCreateClassV6",
    "DhcpCreateClientInfo",
    "DhcpCreateClientInfoV4",
    "DhcpCreateClientInfoVQ",
    "DhcpCreateOption",
    "DhcpCreateOptionV5",
    "DhcpCreateOptionV6",
    "DhcpCreateSubnet",
    "DhcpCreateSubnetV6",
    "DhcpCreateSubnetVQ",
    "DhcpDeRegisterParamChange",
    "DhcpDeleteClass",
    "DhcpDeleteClassV6",
    "DhcpDeleteClientInfo",
    "DhcpDeleteClientInfoV6",
    "DhcpDeleteFilterV4",
    "DhcpDeleteServer",
    "DhcpDeleteSubnet",
    "DhcpDeleteSubnetV6",
    "DhcpDeleteSuperScopeV4",
    "DhcpDsCleanup",
    "DhcpDsInit",
    "DhcpEnumClasses",
    "DhcpEnumClassesV6",
    "DhcpEnumFilterV4",
    "DhcpEnumOptionValues",
    "DhcpEnumOptionValuesV5",
    "DhcpEnumOptionValuesV6",
    "DhcpEnumOptions",
    "DhcpEnumOptionsV5",
    "DhcpEnumOptionsV6",
    "DhcpEnumServers",
    "DhcpEnumSubnetClients",
    "DhcpEnumSubnetClientsFilterStatusInfo",
    "DhcpEnumSubnetClientsV4",
    "DhcpEnumSubnetClientsV5",
    "DhcpEnumSubnetClientsV6",
    "DhcpEnumSubnetClientsVQ",
    "DhcpEnumSubnetElements",
    "DhcpEnumSubnetElementsV4",
    "DhcpEnumSubnetElementsV5",
    "DhcpEnumSubnetElementsV6",
    "DhcpEnumSubnets",
    "DhcpEnumSubnetsV6",
    "DhcpGetAllOptionValues",
    "DhcpGetAllOptionValuesV6",
    "DhcpGetAllOptions",
    "DhcpGetAllOptionsV6",
    "DhcpGetClassInfo",
    "DhcpGetClientInfo",
    "DhcpGetClientInfoV4",
    "DhcpGetClientInfoV6",
    "DhcpGetClientInfoVQ",
    "DhcpGetClientOptions",
    "DhcpGetFilterV4",
    "DhcpGetMibInfo",
    "DhcpGetMibInfoV5",
    "DhcpGetMibInfoV6",
    "DhcpGetOptionInfo",
    "DhcpGetOptionInfoV5",
    "DhcpGetOptionInfoV6",
    "DhcpGetOptionValue",
    "DhcpGetOptionValueV5",
    "DhcpGetOptionValueV6",
    "DhcpGetOriginalSubnetMask",
    "DhcpGetServerBindingInfo",
    "DhcpGetServerBindingInfoV6",
    "DhcpGetServerSpecificStrings",
    "DhcpGetSubnetDelayOffer",
    "DhcpGetSubnetInfo",
    "DhcpGetSubnetInfoV6",
    "DhcpGetSubnetInfoVQ",
    "DhcpGetSuperScopeInfoV4",
    "DhcpGetThreadOptions",
    "DhcpGetVersion",
    "DhcpHlprAddV4PolicyCondition",
    "DhcpHlprAddV4PolicyExpr",
    "DhcpHlprAddV4PolicyRange",
    "DhcpHlprCreateV4Policy",
    "DhcpHlprCreateV4PolicyEx",
    "DhcpHlprFindV4DhcpProperty",
    "DhcpHlprFreeV4DhcpProperty",
    "DhcpHlprFreeV4DhcpPropertyArray",
    "DhcpHlprFreeV4Policy",
    "DhcpHlprFreeV4PolicyArray",
    "DhcpHlprFreeV4PolicyEx",
    "DhcpHlprFreeV4PolicyExArray",
    "DhcpHlprIsV4PolicySingleUC",
    "DhcpHlprIsV4PolicyValid",
    "DhcpHlprIsV4PolicyWellFormed",
    "DhcpHlprModifyV4PolicyExpr",
    "DhcpHlprResetV4PolicyExpr",
    "DhcpModifyClass",
    "DhcpModifyClassV6",
    "DhcpRegisterParamChange",
    "DhcpRemoveDNSRegistrations",
    "DhcpRemoveOption",
    "DhcpRemoveOptionV5",
    "DhcpRemoveOptionV6",
    "DhcpRemoveOptionValue",
    "DhcpRemoveOptionValueV5",
    "DhcpRemoveOptionValueV6",
    "DhcpRemoveSubnetElement",
    "DhcpRemoveSubnetElementV4",
    "DhcpRemoveSubnetElementV5",
    "DhcpRemoveSubnetElementV6",
    "DhcpRequestParams",
    "DhcpRpcFreeMemory",
    "DhcpScanDatabase",
    "DhcpServerAuditlogParamsFree",
    "DhcpServerBackupDatabase",
    "DhcpServerGetConfig",
    "DhcpServerGetConfigV4",
    "DhcpServerGetConfigV6",
    "DhcpServerGetConfigVQ",
    "DhcpServerQueryAttribute",
    "DhcpServerQueryAttributes",
    "DhcpServerQueryDnsRegCredentials",
    "DhcpServerRedoAuthorization",
    "DhcpServerRestoreDatabase",
    "DhcpServerSetConfig",
    "DhcpServerSetConfigV4",
    "DhcpServerSetConfigV6",
    "DhcpServerSetConfigVQ",
    "DhcpServerSetDnsRegCredentials",
    "DhcpServerSetDnsRegCredentialsV5",
    "DhcpSetClientInfo",
    "DhcpSetClientInfoV4",
    "DhcpSetClientInfoV6",
    "DhcpSetClientInfoVQ",
    "DhcpSetFilterV4",
    "DhcpSetOptionInfo",
    "DhcpSetOptionInfoV5",
    "DhcpSetOptionInfoV6",
    "DhcpSetOptionValue",
    "DhcpSetOptionValueV5",
    "DhcpSetOptionValueV6",
    "DhcpSetOptionValues",
    "DhcpSetOptionValuesV5",
    "DhcpSetServerBindingInfo",
    "DhcpSetServerBindingInfoV6",
    "DhcpSetSubnetDelayOffer",
    "DhcpSetSubnetInfo",
    "DhcpSetSubnetInfoV6",
    "DhcpSetSubnetInfoVQ",
    "DhcpSetSuperScopeV4",
    "DhcpSetThreadOptions",
    "DhcpUndoRequestParams",
    "DhcpV4AddPolicyRange",
    "DhcpV4CreateClientInfo",
    "DhcpV4CreateClientInfoEx",
    "DhcpV4CreatePolicy",
    "DhcpV4CreatePolicyEx",
    "DhcpV4DeletePolicy",
    "DhcpV4EnumPolicies",
    "DhcpV4EnumPoliciesEx",
    "DhcpV4EnumSubnetClients",
    "DhcpV4EnumSubnetClientsEx",
    "DhcpV4EnumSubnetReservations",
    "DhcpV4FailoverAddScopeToRelationship",
    "DhcpV4FailoverCreateRelationship",
    "DhcpV4FailoverDeleteRelationship",
    "DhcpV4FailoverDeleteScopeFromRelationship",
    "DhcpV4FailoverEnumRelationship",
    "DhcpV4FailoverGetAddressStatus",
    "DhcpV4FailoverGetClientInfo",
    "DhcpV4FailoverGetRelationship",
    "DhcpV4FailoverGetScopeRelationship",
    "DhcpV4FailoverGetScopeStatistics",
    "DhcpV4FailoverGetSystemTime",
    "DhcpV4FailoverSetRelationship",
    "DhcpV4FailoverTriggerAddrAllocation",
    "DhcpV4GetAllOptionValues",
    "DhcpV4GetClientInfo",
    "DhcpV4GetClientInfoEx",
    "DhcpV4GetFreeIPAddress",
    "DhcpV4GetOptionValue",
    "DhcpV4GetPolicy",
    "DhcpV4GetPolicyEx",
    "DhcpV4QueryPolicyEnforcement",
    "DhcpV4RemoveOptionValue",
    "DhcpV4RemovePolicyRange",
    "DhcpV4SetOptionValue",
    "DhcpV4SetOptionValues",
    "DhcpV4SetPolicy",
    "DhcpV4SetPolicyEnforcement",
    "DhcpV4SetPolicyEx",
    "DhcpV6CreateClientInfo",
    "DhcpV6GetFreeIPAddress",
    "DhcpV6GetStatelessStatistics",
    "DhcpV6GetStatelessStoreParams",
    "DhcpV6SetStatelessStoreParams",
    "Dhcpv6CApiCleanup",
    "Dhcpv6CApiInitialize",
    "Dhcpv6ReleasePrefix",
    "Dhcpv6RenewPrefix",
    "Dhcpv6RequestParams",
    "Dhcpv6RequestPrefix",
    "ERROR_DDS_CLASS_DOES_NOT_EXIST",
    "ERROR_DDS_CLASS_EXISTS",
    "ERROR_DDS_DHCP_SERVER_NOT_FOUND",
    "ERROR_DDS_NO_DHCP_ROOT",
    "ERROR_DDS_NO_DS_AVAILABLE",
    "ERROR_DDS_OPTION_ALREADY_EXISTS",
    "ERROR_DDS_OPTION_DOES_NOT_EXIST",
    "ERROR_DDS_POSSIBLE_RANGE_CONFLICT",
    "ERROR_DDS_RANGE_DOES_NOT_EXIST",
    "ERROR_DDS_RESERVATION_CONFLICT",
    "ERROR_DDS_RESERVATION_NOT_PRESENT",
    "ERROR_DDS_SERVER_ADDRESS_MISMATCH",
    "ERROR_DDS_SERVER_ALREADY_EXISTS",
    "ERROR_DDS_SERVER_DOES_NOT_EXIST",
    "ERROR_DDS_SUBNET_EXISTS",
    "ERROR_DDS_SUBNET_HAS_DIFF_SSCOPE",
    "ERROR_DDS_SUBNET_NOT_PRESENT",
    "ERROR_DDS_TOO_MANY_ERRORS",
    "ERROR_DDS_UNEXPECTED_ERROR",
    "ERROR_DHCP_ADDRESS_NOT_AVAILABLE",
    "ERROR_DHCP_CANNOT_MODIFY_BINDINGS",
    "ERROR_DHCP_CANT_CHANGE_ATTRIBUTE",
    "ERROR_DHCP_CLASS_ALREADY_EXISTS",
    "ERROR_DHCP_CLASS_NOT_FOUND",
    "ERROR_DHCP_CLIENT_EXISTS",
    "ERROR_DHCP_DATABASE_INIT_FAILED",
    "ERROR_DHCP_DEFAULT_SCOPE_EXITS",
    "ERROR_DHCP_DELETE_BUILTIN_CLASS",
    "ERROR_DHCP_ELEMENT_CANT_REMOVE",
    "ERROR_DHCP_EXEMPTION_EXISTS",
    "ERROR_DHCP_EXEMPTION_NOT_PRESENT",
    "ERROR_DHCP_FO_ADDSCOPE_LEASES_NOT_SYNCED",
    "ERROR_DHCP_FO_BOOT_NOT_SUPPORTED",
    "ERROR_DHCP_FO_FEATURE_NOT_SUPPORTED",
    "ERROR_DHCP_FO_IPRANGE_TYPE_CONV_ILLEGAL",
    "ERROR_DHCP_FO_MAX_ADD_SCOPES",
    "ERROR_DHCP_FO_MAX_RELATIONSHIPS",
    "ERROR_DHCP_FO_NOT_SUPPORTED",
    "ERROR_DHCP_FO_RANGE_PART_OF_REL",
    "ERROR_DHCP_FO_RELATIONSHIP_DOES_NOT_EXIST",
    "ERROR_DHCP_FO_RELATIONSHIP_EXISTS",
    "ERROR_DHCP_FO_RELATIONSHIP_NAME_TOO_LONG",
    "ERROR_DHCP_FO_RELATION_IS_SECONDARY",
    "ERROR_DHCP_FO_SCOPE_ALREADY_IN_RELATIONSHIP",
    "ERROR_DHCP_FO_SCOPE_NOT_IN_RELATIONSHIP",
    "ERROR_DHCP_FO_SCOPE_SYNC_IN_PROGRESS",
    "ERROR_DHCP_FO_STATE_NOT_NORMAL",
    "ERROR_DHCP_FO_TIME_OUT_OF_SYNC",
    "ERROR_DHCP_HARDWARE_ADDRESS_TYPE_ALREADY_EXEMPT",
    "ERROR_DHCP_INVALID_DELAY",
    "ERROR_DHCP_INVALID_DHCP_CLIENT",
    "ERROR_DHCP_INVALID_DHCP_MESSAGE",
    "ERROR_DHCP_INVALID_PARAMETER_OPTION32",
    "ERROR_DHCP_INVALID_POLICY_EXPRESSION",
    "ERROR_DHCP_INVALID_PROCESSING_ORDER",
    "ERROR_DHCP_INVALID_RANGE",
    "ERROR_DHCP_INVALID_SUBNET_PREFIX",
    "ERROR_DHCP_IPRANGE_CONV_ILLEGAL",
    "ERROR_DHCP_IPRANGE_EXITS",
    "ERROR_DHCP_IP_ADDRESS_IN_USE",
    "ERROR_DHCP_JET97_CONV_REQUIRED",
    "ERROR_DHCP_JET_CONV_REQUIRED",
    "ERROR_DHCP_JET_ERROR",
    "ERROR_DHCP_LINKLAYER_ADDRESS_DOES_NOT_EXIST",
    "ERROR_DHCP_LINKLAYER_ADDRESS_EXISTS",
    "ERROR_DHCP_LINKLAYER_ADDRESS_RESERVATION_EXISTS",
    "ERROR_DHCP_LOG_FILE_PATH_TOO_LONG",
    "ERROR_DHCP_MSCOPE_EXISTS",
    "ERROR_DHCP_NAP_NOT_SUPPORTED",
    "ERROR_DHCP_NETWORK_CHANGED",
    "ERROR_DHCP_NETWORK_INIT_FAILED",
    "ERROR_DHCP_NOT_RESERVED_CLIENT",
    "ERROR_DHCP_NO_ADMIN_PERMISSION",
    "ERROR_DHCP_OPTION_EXITS",
    "ERROR_DHCP_OPTION_NOT_PRESENT",
    "ERROR_DHCP_OPTION_TYPE_MISMATCH",
    "ERROR_DHCP_POLICY_BAD_PARENT_EXPR",
    "ERROR_DHCP_POLICY_EDIT_FQDN_UNSUPPORTED",
    "ERROR_DHCP_POLICY_EXISTS",
    "ERROR_DHCP_POLICY_FQDN_OPTION_UNSUPPORTED",
    "ERROR_DHCP_POLICY_FQDN_RANGE_UNSUPPORTED",
    "ERROR_DHCP_POLICY_NOT_FOUND",
    "ERROR_DHCP_POLICY_RANGE_BAD",
    "ERROR_DHCP_POLICY_RANGE_EXISTS",
    "ERROR_DHCP_PRIMARY_NOT_FOUND",
    "ERROR_DHCP_RANGE_EXTENDED",
    "ERROR_DHCP_RANGE_FULL",
    "ERROR_DHCP_RANGE_INVALID_IN_SERVER_POLICY",
    "ERROR_DHCP_RANGE_TOO_SMALL",
    "ERROR_DHCP_REACHED_END_OF_SELECTION",
    "ERROR_DHCP_REGISTRY_INIT_FAILED",
    "ERROR_DHCP_RESERVEDIP_EXITS",
    "ERROR_DHCP_RESERVED_CLIENT",
    "ERROR_DHCP_ROGUE_DS_CONFLICT",
    "ERROR_DHCP_ROGUE_DS_UNREACHABLE",
    "ERROR_DHCP_ROGUE_INIT_FAILED",
    "ERROR_DHCP_ROGUE_NOT_AUTHORIZED",
    "ERROR_DHCP_ROGUE_NOT_OUR_ENTERPRISE",
    "ERROR_DHCP_ROGUE_SAMSHUTDOWN",
    "ERROR_DHCP_ROGUE_STANDALONE_IN_DS",
    "ERROR_DHCP_RPC_INIT_FAILED",
    "ERROR_DHCP_SCOPE_NAME_TOO_LONG",
    "ERROR_DHCP_SERVER_NAME_NOT_RESOLVED",
    "ERROR_DHCP_SERVER_NOT_REACHABLE",
    "ERROR_DHCP_SERVER_NOT_RUNNING",
    "ERROR_DHCP_SERVICE_PAUSED",
    "ERROR_DHCP_SUBNET_EXISTS",
    "ERROR_DHCP_SUBNET_EXITS",
    "ERROR_DHCP_SUBNET_NOT_PRESENT",
    "ERROR_DHCP_SUPER_SCOPE_NAME_TOO_LONG",
    "ERROR_DHCP_UNDEFINED_HARDWARE_ADDRESS_TYPE",
    "ERROR_DHCP_UNSUPPORTED_CLIENT",
    "ERROR_EXTEND_TOO_SMALL",
    "ERROR_LAST_DHCP_SERVER_ERROR",
    "ERROR_MSCOPE_RANGE_TOO_SMALL",
    "ERROR_SCOPE_RANGE_POLICY_RANGE_CONFLICT",
    "ERROR_SERVER_INVALID_BOOT_FILE_TABLE",
    "ERROR_SERVER_UNKNOWN_BOOT_FILE_NAME",
    "EXEMPT",
    "FILTER_STATUS_FULL_MATCH_IN_ALLOW_LIST",
    "FILTER_STATUS_FULL_MATCH_IN_DENY_LIST",
    "FILTER_STATUS_NONE",
    "FILTER_STATUS_WILDCARD_MATCH_IN_ALLOW_LIST",
    "FILTER_STATUS_WILDCARD_MATCH_IN_DENY_LIST",
    "FSM_STATE",
    "HWTYPE_ETHERNET_10MB",
    "INIT",
    "LPDHCP_CONTROL",
    "LPDHCP_DELETE_CLIENT",
    "LPDHCP_DROP_SEND",
    "LPDHCP_ENTRY_POINT_FUNC",
    "LPDHCP_GIVE_ADDRESS",
    "LPDHCP_HANDLE_OPTIONS",
    "LPDHCP_NEWPKT",
    "LPDHCP_PROB",
    "MAC_ADDRESS_LENGTH",
    "MAX_PATTERN_LENGTH",
    "MCLT",
    "MODE",
    "NOQUARANTINE",
    "NOQUARINFO",
    "NORMAL",
    "NO_STATE",
    "OPTION_ALL_SUBNETS_MTU",
    "OPTION_ARP_CACHE_TIMEOUT",
    "OPTION_BE_A_MASK_SUPPLIER",
    "OPTION_BE_A_ROUTER",
    "OPTION_BOOTFILE_NAME",
    "OPTION_BOOT_FILE_SIZE",
    "OPTION_BROADCAST_ADDRESS",
    "OPTION_CLIENT_CLASS_INFO",
    "OPTION_CLIENT_ID",
    "OPTION_COOKIE_SERVERS",
    "OPTION_DEFAULT_TTL",
    "OPTION_DOMAIN_NAME",
    "OPTION_DOMAIN_NAME_SERVERS",
    "OPTION_END",
    "OPTION_ETHERNET_ENCAPSULATION",
    "OPTION_EXTENSIONS_PATH",
    "OPTION_HOST_NAME",
    "OPTION_IEN116_NAME_SERVERS",
    "OPTION_IMPRESS_SERVERS",
    "OPTION_KEEP_ALIVE_DATA_SIZE",
    "OPTION_KEEP_ALIVE_INTERVAL",
    "OPTION_LEASE_TIME",
    "OPTION_LOG_SERVERS",
    "OPTION_LPR_SERVERS",
    "OPTION_MAX_REASSEMBLY_SIZE",
    "OPTION_MERIT_DUMP_FILE",
    "OPTION_MESSAGE",
    "OPTION_MESSAGE_LENGTH",
    "OPTION_MESSAGE_TYPE",
    "OPTION_MSFT_IE_PROXY",
    "OPTION_MTU",
    "OPTION_NETBIOS_DATAGRAM_SERVER",
    "OPTION_NETBIOS_NAME_SERVER",
    "OPTION_NETBIOS_NODE_TYPE",
    "OPTION_NETBIOS_SCOPE_OPTION",
    "OPTION_NETWORK_INFO_SERVERS",
    "OPTION_NETWORK_INFO_SERVICE_DOM",
    "OPTION_NETWORK_TIME_SERVERS",
    "OPTION_NON_LOCAL_SOURCE_ROUTING",
    "OPTION_OK_TO_OVERLAY",
    "OPTION_PAD",
    "OPTION_PARAMETER_REQUEST_LIST",
    "OPTION_PERFORM_MASK_DISCOVERY",
    "OPTION_PERFORM_ROUTER_DISCOVERY",
    "OPTION_PMTU_AGING_TIMEOUT",
    "OPTION_PMTU_PLATEAU_TABLE",
    "OPTION_POLICY_FILTER_FOR_NLSR",
    "OPTION_REBIND_TIME",
    "OPTION_RENEWAL_TIME",
    "OPTION_REQUESTED_ADDRESS",
    "OPTION_RLP_SERVERS",
    "OPTION_ROOT_DISK",
    "OPTION_ROUTER_ADDRESS",
    "OPTION_ROUTER_SOLICITATION_ADDR",
    "OPTION_SERVER_IDENTIFIER",
    "OPTION_STATIC_ROUTES",
    "OPTION_SUBNET_MASK",
    "OPTION_SWAP_SERVER",
    "OPTION_TFTP_SERVER_NAME",
    "OPTION_TIME_OFFSET",
    "OPTION_TIME_SERVERS",
    "OPTION_TRAILERS",
    "OPTION_TTL",
    "OPTION_VENDOR_SPEC_INFO",
    "OPTION_XWINDOW_DISPLAY_MANAGER",
    "OPTION_XWINDOW_FONT_SERVER",
    "PARTNER_DOWN",
    "PAUSED",
    "PERCENTAGE",
    "POTENTIAL_CONFLICT",
    "PREVSTATE",
    "PROBATION",
    "QUARANTINE_CONFIG_OPTION",
    "QUARANTINE_SCOPE_QUARPROFILE_OPTION",
    "QUARANTIN_OPTION_BASE",
    "QuarantineStatus",
    "RECOVER",
    "RECOVER_DONE",
    "RECOVER_WAIT",
    "RESOLUTION_INT",
    "RESTRICTEDACCESS",
    "SAFEPERIOD",
    "SCOPE_MIB_INFO",
    "SCOPE_MIB_INFO_V5",
    "SCOPE_MIB_INFO_V6",
    "SCOPE_MIB_INFO_VQ",
    "SHAREDSECRET",
    "SHUTDOWN",
    "STARTUP",
    "STATUS_NOPREFIX_AVAIL",
    "STATUS_NO_BINDING",
    "STATUS_NO_ERROR",
    "STATUS_UNSPECIFIED_FAILURE",
    "Set_APIProtocolSupport",
    "Set_AuditLogState",
    "Set_BackupInterval",
    "Set_BackupPath",
    "Set_BootFileTable",
    "Set_DatabaseCleanupInterval",
    "Set_DatabaseLoggingFlag",
    "Set_DatabaseName",
    "Set_DatabasePath",
    "Set_DebugFlag",
    "Set_PingRetries",
    "Set_PreferredLifetime",
    "Set_PreferredLifetimeIATA",
    "Set_QuarantineDefFail",
    "Set_QuarantineON",
    "Set_RapidCommitFlag",
    "Set_RestoreFlag",
    "Set_T1",
    "Set_T2",
    "Set_UnicastFlag",
    "Set_ValidLifetime",
    "Set_ValidLifetimeIATA",
    "StatusCode",
    "V5_ADDRESS_BIT_BOTH_REC",
    "V5_ADDRESS_BIT_DELETED",
    "V5_ADDRESS_BIT_UNREGISTERED",
    "V5_ADDRESS_EX_BIT_DISABLE_PTR_RR",
    "V5_ADDRESS_STATE_ACTIVE",
    "V5_ADDRESS_STATE_DECLINED",
    "V5_ADDRESS_STATE_DOOM",
    "V5_ADDRESS_STATE_OFFERED",
    "WARNING_EXTENDED_LESS",
]
