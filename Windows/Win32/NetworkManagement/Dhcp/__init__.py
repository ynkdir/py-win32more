from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.Dhcp
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def Dhcpv6RequestParams(forceNewInform: Windows.Win32.Foundation.BOOL, reserved: c_void_p, adapterName: Windows.Win32.Foundation.PWSTR, classId: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), recdParams: Windows.Win32.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_ARRAY, buffer: POINTER(Byte), pSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6RequestPrefix(adapterName: Windows.Win32.Foundation.PWSTR, pclassId: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), prefixleaseInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head), pdwTimeToWait: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6RenewPrefix(adapterName: Windows.Win32.Foundation.PWSTR, pclassId: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), prefixleaseInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head), pdwTimeToWait: POINTER(UInt32), bValidatePrefix: UInt32) -> UInt32: ...
@winfunctype('dhcpcsvc6.dll')
def Dhcpv6ReleasePrefix(adapterName: Windows.Win32.Foundation.PWSTR, classId: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6CAPI_CLASSID_head), leaseInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6PrefixLeaseInformation_head)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpCApiInitialize(Version: POINTER(UInt32)) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpCApiCleanup() -> Void: ...
@winfunctype('dhcpcsvc.dll')
def DhcpRequestParams(Flags: UInt32, Reserved: c_void_p, AdapterName: Windows.Win32.Foundation.PWSTR, ClassId: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPCAPI_CLASSID_head), SendParams: Windows.Win32.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY, RecdParams: Windows.Win32.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY, Buffer: POINTER(Byte), pSize: POINTER(UInt32), RequestIdStr: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpUndoRequestParams(Flags: UInt32, Reserved: c_void_p, AdapterName: Windows.Win32.Foundation.PWSTR, RequestIdStr: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpRegisterParamChange(Flags: UInt32, Reserved: c_void_p, AdapterName: Windows.Win32.Foundation.PWSTR, ClassId: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPCAPI_CLASSID_head), Params: Windows.Win32.NetworkManagement.Dhcp.DHCPCAPI_PARAMS_ARRAY, Handle: c_void_p) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpDeRegisterParamChange(Flags: UInt32, Reserved: c_void_p, Event: c_void_p) -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpRemoveDNSRegistrations() -> UInt32: ...
@winfunctype('dhcpcsvc.dll')
def DhcpGetOriginalSubnetMask(sAdapterName: Windows.Win32.Foundation.PWSTR, dwSubnetMask: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddFilterV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, AddFilterInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FILTER_ADD_INFO_head), ForceFlag: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteFilterV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, DeleteFilterInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetFilterV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, GlobalFilterInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FILTER_GLOBAL_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetFilterV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, GlobalFilterInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FILTER_GLOBAL_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumFilterV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN_head), PreferredMaximum: UInt32, ListType: Windows.Win32.NetworkManagement.Dhcp.DHCP_FILTER_LIST_TYPE, EnumFilterInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FILTER_ENUM_INFO_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateSubnet(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnets(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElement(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, AddElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElements(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, EnumElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElement(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, RemoveElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head), ForceFlag: Windows.Win32.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteSubnet(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ForceFlag: Windows.Win32.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateOption(ServerIpAddress: Windows.Win32.Foundation.PWSTR, OptionID: UInt32, OptionInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, OptionID: UInt32, OptionInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, OptionID: UInt32, OptionInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptions(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, Options: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOption(ServerIpAddress: Windows.Win32.Foundation.PWSTR, OptionID: UInt32) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValue(ServerIpAddress: Windows.Win32.Foundation.PWSTR, OptionID: UInt32, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValues(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValues: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionValue(ServerIpAddress: Windows.Win32.Foundation.PWSTR, OptionID: UInt32, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionValues(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, OptionValues: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionValue(ServerIpAddress: Windows.Win32.Foundation.PWSTR, OptionID: UInt32, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClientInfoVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfoVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfoVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SearchInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_VQ_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsFilterStatusInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SearchInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClients(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientOptions(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientIpAddress: UInt32, ClientSubnetMask: UInt32, ClientOptions: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_LIST_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetMibInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, MibInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_MIB_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfig(ServerIpAddress: Windows.Win32.Foundation.PWSTR, FieldsToSet: UInt32, ConfigInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfig(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ConfigInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpScanDatabase(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, FixFlag: UInt32, ScanList: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SCAN_LIST_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRpcFreeMemory(BufferPointer: c_void_p) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetVersion(ServerIpAddress: Windows.Win32.Foundation.PWSTR, MajorVersion: POINTER(UInt32), MinorVersion: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElementV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, AddElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElementsV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, EnumElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElementV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, RemoveElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head), ForceFlag: Windows.Win32.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClientInfoV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfoV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfoV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SearchInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V4_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfigV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, FieldsToSet: UInt32, ConfigInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V4_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfigV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ConfigInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V4_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSuperScopeV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, SuperScopeName: Windows.Win32.Foundation.PWSTR, ChangeExisting: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteSuperScopeV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SuperScopeName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSuperScopeInfoV4(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SuperScopeTable: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V5_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateOptionV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, OptionInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionInfoV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, OptionInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionInfoV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, OptionInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionsV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, Options: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValueV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValuesV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValues: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionValueV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionValueV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), OptionValue: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionValuesV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, OptionValues: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionValueV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClass(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpModifyClass(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClass(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClassInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, PartialClassInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head), FilledClassInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumClasses(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClassInfoArray: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_head)), nRead: POINTER(UInt32), nTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptions(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionStruct: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ALL_OPTIONS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptionsV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionStruct: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ALL_OPTIONS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptionValues(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), Values: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetAllOptionValuesV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), Values: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumServers(Flags: UInt32, IdInfo: c_void_p, Servers: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPDS_SERVERS_head)), CallbackFn: c_void_p, CallbackData: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddServer(Flags: UInt32, IdInfo: c_void_p, NewServer: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPDS_SERVER_head), CallbackFn: c_void_p, CallbackData: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteServer(Flags: UInt32, IdInfo: c_void_p, NewServer: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPDS_SERVER_head), CallbackFn: c_void_p, CallbackData: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetServerBindingInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, BindElementsInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetServerBindingInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, BindElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElementV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, AddElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElementsV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, EnumElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElementV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, RemoveElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head), ForceFlag: Windows.Win32.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumSubnetReservations(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_RESERVATION_INFO_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateOptionV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, OptionInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionsV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, Options: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveOptionValueV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetOptionInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, OptionInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, OptionInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetOptionValueV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), OptionValue: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetInfoVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateSubnetVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetInfoVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, SubnetInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumOptionValuesV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ClassName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, OptionValues: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)), OptionsRead: POINTER(UInt32), OptionsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDsInit() -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDsCleanup() -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetThreadOptions(Flags: UInt32, Reserved: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetThreadOptions(pFlags: POINTER(UInt32), Reserved: c_void_p) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerQueryAttribute(ServerIpAddr: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32, DhcpAttribId: UInt32, pDhcpAttrib: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ATTRIB_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerQueryAttributes(ServerIpAddr: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32, dwAttribCount: UInt32, pDhcpAttribs: POINTER(UInt32), pDhcpAttribArr: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ATTRIB_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerRedoAuthorization(ServerIpAddr: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAuditLogSetParams(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, AuditLogDir: Windows.Win32.Foundation.PWSTR, DiskCheckInterval: UInt32, MaxLogFilesSize: UInt32, MinSpaceOnDisk: UInt32) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAuditLogGetParams(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, AuditLogDir: POINTER(Windows.Win32.Foundation.PWSTR), DiskCheckInterval: POINTER(UInt32), MaxLogFilesSize: POINTER(UInt32), MinSpaceOnDisk: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerQueryDnsRegCredentials(ServerIpAddress: Windows.Win32.Foundation.PWSTR, UnameSize: UInt32, Uname: Windows.Win32.Foundation.PWSTR, DomainSize: UInt32, Domain: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetDnsRegCredentials(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Uname: Windows.Win32.Foundation.PWSTR, Domain: Windows.Win32.Foundation.PWSTR, Passwd: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetDnsRegCredentialsV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Uname: Windows.Win32.Foundation.PWSTR, Domain: Windows.Win32.Foundation.PWSTR, Passwd: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerBackupDatabase(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Path: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerRestoreDatabase(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Path: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfigVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, FieldsToSet: UInt32, ConfigInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfigVQ(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ConfigInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetServerSpecificStrings(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ServerSpecificStrings: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_SPECIFIC_STRINGS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerAuditlogParamsFree(ConfigInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_VQ_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateSubnetV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, SubnetInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteSubnetV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, ForceFlag: Windows.Win32.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetsV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_IP_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSubnetElementV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, AddElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpRemoveSubnetElementV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, RemoveElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head), ForceFlag: Windows.Win32.NetworkManagement.Dhcp.DHCP_FORCE_FLAG) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetElementsV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, EnumElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE_V6, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, EnumElementInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, SubnetInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumSubnetClientsV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, ResumeHandle: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS_head), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_ARRAY_V6_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerGetConfigV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), ConfigInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpServerSetConfigV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO6_head), FieldsToSet: UInt32, ConfigInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_CONFIG_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, SubnetInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetMibInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, MibInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_MIB_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetServerBindingInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, BindElementsInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetServerBindingInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, BindElementInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetClientInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetClientInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SearchInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_V6_head), ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClientInfoV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpCreateClassV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpModifyClassV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpDeleteClassV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ClassName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpEnumClassesV6(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ReservedMustBeZero: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClassInfoArray: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_ARRAY_V6_head)), nRead: POINTER(UInt32), nTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpSetSubnetDelayOffer(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, TimeDelayInMilliseconds: UInt16) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetSubnetDelayOffer(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, TimeDelayInMilliseconds: POINTER(UInt16)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpGetMibInfoV5(ServerIpAddress: Windows.Win32.Foundation.PWSTR, MibInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_MIB_INFO_V5_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpAddSecurityGroup(pServer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetOptionValue(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetOptionValue(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionId: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValue: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetOptionValues(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), OptionValues: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4RemoveOptionValue(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, OptionID: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, VendorName: Windows.Win32.Foundation.PWSTR, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetAllOptionValues(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_INFO_head), Values: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ALL_OPTION_VALUES_PB_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverCreateRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pRelationship: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverSetRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, Flags: UInt32, pRelationship: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverDeleteRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pRelationshipName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pRelationshipName: Windows.Win32.Foundation.PWSTR, pRelationship: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverEnumRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, pRelationship: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_ARRAY_head)), RelationshipRead: POINTER(UInt32), RelationshipTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverAddScopeToRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pRelationship: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverDeleteScopeFromRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pRelationship: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetScopeRelationship(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeId: UInt32, pRelationship: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetScopeStatistics(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeId: UInt32, pStats: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_STATISTICS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SearchInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetSystemTime(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pTime: POINTER(UInt32), pMaxAllowedDeltaTime: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverGetAddressStatus(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, pStatus: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4FailoverTriggerAddrAllocation(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pFailRelName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprCreateV4Policy(PolicyName: Windows.Win32.Foundation.PWSTR, fGlobalPolicy: Windows.Win32.Foundation.BOOL, Subnet: UInt32, ProcessingOrder: UInt32, RootOperator: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER, Description: Windows.Win32.Foundation.PWSTR, Enabled: Windows.Win32.Foundation.BOOL, Policy: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprCreateV4PolicyEx(PolicyName: Windows.Win32.Foundation.PWSTR, fGlobalPolicy: Windows.Win32.Foundation.BOOL, Subnet: UInt32, ProcessingOrder: UInt32, RootOperator: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER, Description: Windows.Win32.Foundation.PWSTR, Enabled: Windows.Win32.Foundation.BOOL, Policy: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprAddV4PolicyExpr(Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head), ParentExpr: UInt32, Operator: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER, ExprIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprAddV4PolicyCondition(Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head), ParentExpr: UInt32, Type: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_ATTR_TYPE, OptionID: UInt32, SubOptionID: UInt32, VendorName: Windows.Win32.Foundation.PWSTR, Operator: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_COMPARATOR, Value: POINTER(Byte), ValueLength: UInt32, ConditionIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprAddV4PolicyRange(Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head), Range: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprResetV4PolicyExpr(Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprModifyV4PolicyExpr(Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head), Operator: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4Policy(Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4PolicyArray(PolicyArray: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_ARRAY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4PolicyEx(PolicyEx: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4PolicyExArray(PolicyExArray: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_ARRAY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4DhcpProperty(Property: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFreeV4DhcpPropertyArray(PropertyArray: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)) -> Void: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprFindV4DhcpProperty(PropertyArray: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head), ID: Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_ID, Type: Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_TYPE) -> POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_head): ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprIsV4PolicySingleUC(Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4QueryPolicyEnforcement(ServerIpAddress: Windows.Win32.Foundation.PWSTR, fGlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, Enabled: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetPolicyEnforcement(ServerIpAddress: Windows.Win32.Foundation.PWSTR, fGlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, Enable: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprIsV4PolicyWellFormed(pPolicy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DHCPSAPI.dll')
def DhcpHlprIsV4PolicyValid(pPolicy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreatePolicy(ServerIpAddress: Windows.Win32.Foundation.PWSTR, pPolicy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetPolicy(ServerIpAddress: Windows.Win32.Foundation.PWSTR, fGlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, Policy: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetPolicy(ServerIpAddress: Windows.Win32.Foundation.PWSTR, FieldsModified: UInt32, fGlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4DeletePolicy(ServerIpAddress: Windows.Win32.Foundation.PWSTR, fGlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumPolicies(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, fGlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, EnumInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4AddPolicyRange(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, Range: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4RemovePolicyRange(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, Range: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6SetStatelessStoreParams(ServerIpAddress: Windows.Win32.Foundation.PWSTR, fServerLevel: Windows.Win32.Foundation.BOOL, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, FieldModified: UInt32, Params: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_STATELESS_PARAMS_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6GetStatelessStoreParams(ServerIpAddress: Windows.Win32.Foundation.PWSTR, fServerLevel: Windows.Win32.Foundation.BOOL, SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, Params: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_STATELESS_PARAMS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6GetStatelessStatistics(ServerIpAddress: Windows.Win32.Foundation.PWSTR, StatelessStats: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_STATELESS_STATS_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreateClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumSubnetClients(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SearchInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6CreateClientInfo(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetFreeIPAddress(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeId: UInt32, StartIP: UInt32, EndIP: UInt32, NumFreeAddrReq: UInt32, IPAddrList: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV6GetFreeIPAddress(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ScopeId: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, StartIP: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, EndIP: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS, NumFreeAddrReq: UInt32, IPAddrList: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_IP_ARRAY_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreateClientInfoEx(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ClientInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumSubnetClientsEx(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SubnetAddress: UInt32, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_ARRAY_head)), ClientsRead: POINTER(UInt32), ClientsTotal: POINTER(UInt32)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetClientInfoEx(ServerIpAddress: Windows.Win32.Foundation.PWSTR, SearchInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_head), ClientInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4CreatePolicyEx(ServerIpAddress: Windows.Win32.Foundation.PWSTR, PolicyEx: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4GetPolicyEx(ServerIpAddress: Windows.Win32.Foundation.PWSTR, GlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, Policy: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_head))) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4SetPolicyEx(ServerIpAddress: Windows.Win32.Foundation.PWSTR, FieldsModified: UInt32, GlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, PolicyName: Windows.Win32.Foundation.PWSTR, Policy: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)) -> UInt32: ...
@winfunctype('DHCPSAPI.dll')
def DhcpV4EnumPoliciesEx(ServerIpAddress: Windows.Win32.Foundation.PWSTR, ResumeHandle: POINTER(UInt32), PreferredMaximum: UInt32, GlobalPolicy: Windows.Win32.Foundation.BOOL, SubnetAddress: UInt32, EnumInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_ARRAY_head)), ElementsRead: POINTER(UInt32), ElementsTotal: POINTER(UInt32)) -> UInt32: ...
class DATE_TIME(EasyCastStructure):
    dwLowDateTime: UInt32
    dwHighDateTime: UInt32
class DHCPAPI_PARAMS(EasyCastStructure):
    Flags: UInt32
    OptionId: UInt32
    IsVendor: Windows.Win32.Foundation.BOOL
    Data: POINTER(Byte)
    nBytesData: UInt32
class DHCPCAPI_CLASSID(EasyCastStructure):
    Flags: UInt32
    Data: POINTER(Byte)
    nBytesData: UInt32
class DHCPCAPI_PARAMS_ARRAY(EasyCastStructure):
    nParams: UInt32
    Params: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPAPI_PARAMS_head)
class DHCPDS_SERVER(EasyCastStructure):
    Version: UInt32
    ServerName: Windows.Win32.Foundation.PWSTR
    ServerAddress: UInt32
    Flags: UInt32
    State: UInt32
    DsLocation: Windows.Win32.Foundation.PWSTR
    DsLocType: UInt32
class DHCPDS_SERVERS(EasyCastStructure):
    Flags: UInt32
    NumElements: UInt32
    Servers: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPDS_SERVER_head)
class DHCPV4_FAILOVER_CLIENT_INFO(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: Windows.Win32.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: Windows.Win32.Foundation.BOOL
    SentPotExpTime: UInt32
    AckPotExpTime: UInt32
    RecvPotExpTime: UInt32
    StartTime: UInt32
    CltLastTransTime: UInt32
    LastBndUpdTime: UInt32
    BndMsgStatus: UInt32
    PolicyName: Windows.Win32.Foundation.PWSTR
    Flags: Byte
class DHCPV4_FAILOVER_CLIENT_INFO_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV4_FAILOVER_CLIENT_INFO_head))
class DHCPV4_FAILOVER_CLIENT_INFO_EX(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: Windows.Win32.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: Windows.Win32.Foundation.BOOL
    SentPotExpTime: UInt32
    AckPotExpTime: UInt32
    RecvPotExpTime: UInt32
    StartTime: UInt32
    CltLastTransTime: UInt32
    LastBndUpdTime: UInt32
    BndMsgStatus: UInt32
    PolicyName: Windows.Win32.Foundation.PWSTR
    Flags: Byte
    AddressStateEx: UInt32
class DHCPV6CAPI_CLASSID(EasyCastStructure):
    Flags: UInt32
    Data: POINTER(Byte)
    nBytesData: UInt32
class DHCPV6CAPI_PARAMS(EasyCastStructure):
    Flags: UInt32
    OptionId: UInt32
    IsVendor: Windows.Win32.Foundation.BOOL
    Data: POINTER(Byte)
    nBytesData: UInt32
class DHCPV6CAPI_PARAMS_ARRAY(EasyCastStructure):
    nParams: UInt32
    Params: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6CAPI_PARAMS_head)
class DHCPV6Prefix(EasyCastStructure):
    prefix: Byte * 16
    prefixLength: UInt32
    preferredLifeTime: UInt32
    validLifeTime: UInt32
    status: Windows.Win32.NetworkManagement.Dhcp.StatusCode
class DHCPV6PrefixLeaseInformation(EasyCastStructure):
    nPrefixes: UInt32
    prefixArray: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6Prefix_head)
    iaid: UInt32
    T1: Int64
    T2: Int64
    MaxLeaseExpirationTime: Int64
    LastRenewalTime: Int64
    status: Windows.Win32.NetworkManagement.Dhcp.StatusCode
    ServerId: POINTER(Byte)
    ServerIdLen: UInt32
class DHCPV6_BIND_ELEMENT(EasyCastStructure):
    Flags: UInt32
    fBoundToDHCPServer: Windows.Win32.Foundation.BOOL
    AdapterPrimaryAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    AdapterSubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    IfDescription: Windows.Win32.Foundation.PWSTR
    IpV6IfIndex: UInt32
    IfIdSize: UInt32
    IfId: POINTER(Byte)
class DHCPV6_BIND_ELEMENT_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_BIND_ELEMENT_head)
class DHCPV6_IP_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS_head)
class DHCPV6_STATELESS_PARAMS(EasyCastStructure):
    Status: Windows.Win32.Foundation.BOOL
    PurgeInterval: UInt32
DHCPV6_STATELESS_PARAM_TYPE = Int32
DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessPurgeInterval: DHCPV6_STATELESS_PARAM_TYPE = 1
DHCPV6_STATELESS_PARAM_TYPE_DhcpStatelessStatus: DHCPV6_STATELESS_PARAM_TYPE = 2
class DHCPV6_STATELESS_SCOPE_STATS(EasyCastStructure):
    SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    NumStatelessClientsAdded: UInt64
    NumStatelessClientsRemoved: UInt64
class DHCPV6_STATELESS_STATS(EasyCastStructure):
    NumScopes: UInt32
    ScopeStats: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCPV6_STATELESS_SCOPE_STATS_head)
class DHCP_ADDR_PATTERN(EasyCastStructure):
    MatchHWType: Windows.Win32.Foundation.BOOL
    HWType: Byte
    IsWildcard: Windows.Win32.Foundation.BOOL
    Length: Byte
    Pattern: Byte * 255
class DHCP_ALL_OPTIONS(EasyCastStructure):
    Flags: UInt32
    NonVendorOptions: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_ARRAY_head)
    NumVendorOptions: UInt32
    VendorOptions: POINTER(_Anonymous_e__Struct)
    class _Anonymous_e__Struct(EasyCastStructure):
        Option: Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION
        VendorName: Windows.Win32.Foundation.PWSTR
        ClassName: Windows.Win32.Foundation.PWSTR
class DHCP_ALL_OPTION_VALUES(EasyCastStructure):
    Flags: UInt32
    NumElements: UInt32
    Options: POINTER(_Anonymous_e__Struct)
    class _Anonymous_e__Struct(EasyCastStructure):
        ClassName: Windows.Win32.Foundation.PWSTR
        VendorName: Windows.Win32.Foundation.PWSTR
        IsVendor: Windows.Win32.Foundation.BOOL
        OptionsArray: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)
class DHCP_ALL_OPTION_VALUES_PB(EasyCastStructure):
    Flags: UInt32
    NumElements: UInt32
    Options: POINTER(_Anonymous_e__Struct)
    class _Anonymous_e__Struct(EasyCastStructure):
        PolicyName: Windows.Win32.Foundation.PWSTR
        VendorName: Windows.Win32.Foundation.PWSTR
        IsVendor: Windows.Win32.Foundation.BOOL
        OptionsArray: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_ARRAY_head)
class DHCP_ATTRIB(EasyCastStructure):
    DhcpAttribId: UInt32
    DhcpAttribType: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        DhcpAttribBool: Windows.Win32.Foundation.BOOL
        DhcpAttribUlong: UInt32
class DHCP_ATTRIB_ARRAY(EasyCastStructure):
    NumElements: UInt32
    DhcpAttribs: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_ATTRIB_head)
class DHCP_BINARY_DATA(EasyCastStructure):
    DataLength: UInt32
    Data: POINTER(Byte)
class DHCP_BIND_ELEMENT(EasyCastStructure):
    Flags: UInt32
    fBoundToDHCPServer: Windows.Win32.Foundation.BOOL
    AdapterPrimaryAddress: UInt32
    AdapterSubnetAddress: UInt32
    IfDescription: Windows.Win32.Foundation.PWSTR
    IfIdSize: UInt32
    IfId: POINTER(Byte)
class DHCP_BIND_ELEMENT_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_BIND_ELEMENT_head)
class DHCP_BOOTP_IP_RANGE(EasyCastStructure):
    StartAddress: UInt32
    EndAddress: UInt32
    BootpAllocated: UInt32
    MaxBootpAllowed: UInt32
class DHCP_CALLOUT_TABLE(EasyCastStructure):
    DhcpControlHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_CONTROL
    DhcpNewPktHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_NEWPKT
    DhcpPktDropHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_DROP_SEND
    DhcpPktSendHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_DROP_SEND
    DhcpAddressDelHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_PROB
    DhcpAddressOfferHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_GIVE_ADDRESS
    DhcpHandleOptionsHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_HANDLE_OPTIONS
    DhcpDeleteClientHook: Windows.Win32.NetworkManagement.Dhcp.LPDHCP_DELETE_CLIENT
    DhcpExtensionHook: c_void_p
    DhcpReservedHook: c_void_p
class DHCP_CLASS_INFO(EasyCastStructure):
    ClassName: Windows.Win32.Foundation.PWSTR
    ClassComment: Windows.Win32.Foundation.PWSTR
    ClassDataLength: UInt32
    IsVendor: Windows.Win32.Foundation.BOOL
    Flags: UInt32
    ClassData: POINTER(Byte)
class DHCP_CLASS_INFO_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Classes: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_head)
class DHCP_CLASS_INFO_ARRAY_V6(EasyCastStructure):
    NumElements: UInt32
    Classes: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLASS_INFO_V6_head)
class DHCP_CLASS_INFO_V6(EasyCastStructure):
    ClassName: Windows.Win32.Foundation.PWSTR
    ClassComment: Windows.Win32.Foundation.PWSTR
    ClassDataLength: UInt32
    IsVendor: Windows.Win32.Foundation.BOOL
    EnterpriseNumber: UInt32
    Flags: UInt32
    ClassData: POINTER(Byte)
class DHCP_CLIENT_FILTER_STATUS_INFO(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: Windows.Win32.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: Windows.Win32.Foundation.BOOL
    FilterStatus: UInt32
class DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_FILTER_STATUS_INFO_head))
class DHCP_CLIENT_INFO(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
class DHCP_CLIENT_INFO_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_head))
class DHCP_CLIENT_INFO_ARRAY_V4(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V4_head))
class DHCP_CLIENT_INFO_ARRAY_V5(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V5_head))
class DHCP_CLIENT_INFO_ARRAY_V6(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_V6_head))
class DHCP_CLIENT_INFO_ARRAY_VQ(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_VQ_head))
class DHCP_CLIENT_INFO_EX(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: Windows.Win32.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: Windows.Win32.Foundation.BOOL
    FilterStatus: UInt32
    PolicyName: Windows.Win32.Foundation.PWSTR
    Properties: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)
class DHCP_CLIENT_INFO_EX_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_EX_head))
class DHCP_CLIENT_INFO_PB(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: Windows.Win32.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: Windows.Win32.Foundation.BOOL
    FilterStatus: UInt32
    PolicyName: Windows.Win32.Foundation.PWSTR
class DHCP_CLIENT_INFO_PB_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Clients: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CLIENT_INFO_PB_head))
class DHCP_CLIENT_INFO_V4(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
class DHCP_CLIENT_INFO_V5(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
class DHCP_CLIENT_INFO_V6(EasyCastStructure):
    ClientIpAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    ClientDUID: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    AddressType: UInt32
    IAID: UInt32
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientValidLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    ClientPrefLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO_V6
class DHCP_CLIENT_INFO_VQ(EasyCastStructure):
    ClientIpAddress: UInt32
    SubnetMask: UInt32
    ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ClientName: Windows.Win32.Foundation.PWSTR
    ClientComment: Windows.Win32.Foundation.PWSTR
    ClientLeaseExpires: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    OwnerHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    bClientType: Byte
    AddressState: Byte
    Status: Windows.Win32.NetworkManagement.Dhcp.QuarantineStatus
    ProbationEnds: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    QuarantineCapable: Windows.Win32.Foundation.BOOL
class DHCP_CLIENT_SEARCH_UNION(EasyCastUnion):
    pass
DHCP_FAILOVER_MODE = Int32
DHCP_FAILOVER_MODE_LoadBalance: DHCP_FAILOVER_MODE = 0
DHCP_FAILOVER_MODE_HotStandby: DHCP_FAILOVER_MODE = 1
class DHCP_FAILOVER_RELATIONSHIP(EasyCastStructure):
    PrimaryServer: UInt32
    SecondaryServer: UInt32
    Mode: Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_MODE
    ServerType: Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_SERVER
    State: Windows.Win32.NetworkManagement.Dhcp.FSM_STATE
    PrevState: Windows.Win32.NetworkManagement.Dhcp.FSM_STATE
    Mclt: UInt32
    SafePeriod: UInt32
    RelationshipName: Windows.Win32.Foundation.PWSTR
    PrimaryServerName: Windows.Win32.Foundation.PWSTR
    SecondaryServerName: Windows.Win32.Foundation.PWSTR
    pScopes: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_ARRAY_head)
    Percentage: Byte
    SharedSecret: Windows.Win32.Foundation.PWSTR
class DHCP_FAILOVER_RELATIONSHIP_ARRAY(EasyCastStructure):
    NumElements: UInt32
    pRelationships: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FAILOVER_RELATIONSHIP_head)
DHCP_FAILOVER_SERVER = Int32
DHCP_FAILOVER_SERVER_PrimaryServer: DHCP_FAILOVER_SERVER = 0
DHCP_FAILOVER_SERVER_SecondaryServer: DHCP_FAILOVER_SERVER = 1
class DHCP_FAILOVER_STATISTICS(EasyCastStructure):
    NumAddr: UInt32
    AddrFree: UInt32
    AddrInUse: UInt32
    PartnerAddrFree: UInt32
    ThisAddrFree: UInt32
    PartnerAddrInUse: UInt32
    ThisAddrInUse: UInt32
class DHCP_FILTER_ADD_INFO(EasyCastStructure):
    AddrPatt: Windows.Win32.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN
    Comment: Windows.Win32.Foundation.PWSTR
    ListType: Windows.Win32.NetworkManagement.Dhcp.DHCP_FILTER_LIST_TYPE
class DHCP_FILTER_ENUM_INFO(EasyCastStructure):
    NumElements: UInt32
    pEnumRecords: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_FILTER_RECORD_head)
class DHCP_FILTER_GLOBAL_INFO(EasyCastStructure):
    EnforceAllowList: Windows.Win32.Foundation.BOOL
    EnforceDenyList: Windows.Win32.Foundation.BOOL
DHCP_FILTER_LIST_TYPE = Int32
DHCP_FILTER_LIST_TYPE_Deny: DHCP_FILTER_LIST_TYPE = 0
DHCP_FILTER_LIST_TYPE_Allow: DHCP_FILTER_LIST_TYPE = 1
class DHCP_FILTER_RECORD(EasyCastStructure):
    AddrPatt: Windows.Win32.NetworkManagement.Dhcp.DHCP_ADDR_PATTERN
    Comment: Windows.Win32.Foundation.PWSTR
DHCP_FORCE_FLAG = Int32
DHCP_FORCE_FLAG_DhcpFullForce: DHCP_FORCE_FLAG = 0
DHCP_FORCE_FLAG_DhcpNoForce: DHCP_FORCE_FLAG = 1
DHCP_FORCE_FLAG_DhcpFailoverForce: DHCP_FORCE_FLAG = 2
class DHCP_HOST_INFO(EasyCastStructure):
    IpAddress: UInt32
    NetBiosName: Windows.Win32.Foundation.PWSTR
    HostName: Windows.Win32.Foundation.PWSTR
class DHCP_HOST_INFO_V6(EasyCastStructure):
    IpAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    NetBiosName: Windows.Win32.Foundation.PWSTR
    HostName: Windows.Win32.Foundation.PWSTR
class DHCP_IPV6_ADDRESS(EasyCastStructure):
    HighOrderBits: UInt64
    LowOrderBits: UInt64
class DHCP_IP_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(UInt32)
class DHCP_IP_CLUSTER(EasyCastStructure):
    ClusterAddress: UInt32
    ClusterMask: UInt32
class DHCP_IP_RANGE(EasyCastStructure):
    StartAddress: UInt32
    EndAddress: UInt32
class DHCP_IP_RANGE_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
class DHCP_IP_RANGE_V6(EasyCastStructure):
    StartAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    EndAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
class DHCP_IP_RESERVATION(EasyCastStructure):
    ReservedIpAddress: UInt32
    ReservedForClient: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)
class DHCP_IP_RESERVATION_INFO(EasyCastStructure):
    ReservedIpAddress: UInt32
    ReservedForClient: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
    ReservedClientName: Windows.Win32.Foundation.PWSTR
    ReservedClientDesc: Windows.Win32.Foundation.PWSTR
    bAllowedClientTypes: Byte
    fOptionsPresent: Byte
class DHCP_IP_RESERVATION_V4(EasyCastStructure):
    ReservedIpAddress: UInt32
    ReservedForClient: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)
    bAllowedClientTypes: Byte
class DHCP_IP_RESERVATION_V6(EasyCastStructure):
    ReservedIpAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    ReservedForClient: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA_head)
    InterfaceId: UInt32
class DHCP_MIB_INFO(EasyCastStructure):
    Discovers: UInt32
    Offers: UInt32
    Requests: UInt32
    Acks: UInt32
    Naks: UInt32
    Declines: UInt32
    Releases: UInt32
    ServerStartTime: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    Scopes: UInt32
    ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.SCOPE_MIB_INFO_head)
class DHCP_MIB_INFO_V5(EasyCastStructure):
    Discovers: UInt32
    Offers: UInt32
    Requests: UInt32
    Acks: UInt32
    Naks: UInt32
    Declines: UInt32
    Releases: UInt32
    ServerStartTime: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
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
    ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V5_head)
class DHCP_MIB_INFO_V6(EasyCastStructure):
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
    ServerStartTime: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    Scopes: UInt32
    ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.SCOPE_MIB_INFO_V6_head)
class DHCP_MIB_INFO_VQ(EasyCastStructure):
    Discovers: UInt32
    Offers: UInt32
    Requests: UInt32
    Acks: UInt32
    Naks: UInt32
    Declines: UInt32
    Releases: UInt32
    ServerStartTime: Windows.Win32.NetworkManagement.Dhcp.DATE_TIME
    QtnNumLeases: UInt32
    QtnPctQtnLeases: UInt32
    QtnProbationLeases: UInt32
    QtnNonQtnLeases: UInt32
    QtnExemptLeases: UInt32
    QtnCapableClients: UInt32
    QtnIASErrors: UInt32
    Scopes: UInt32
    ScopeInfo: POINTER(Windows.Win32.NetworkManagement.Dhcp.SCOPE_MIB_INFO_VQ_head)
class DHCP_OPTION(EasyCastStructure):
    OptionID: UInt32
    OptionName: Windows.Win32.Foundation.PWSTR
    OptionComment: Windows.Win32.Foundation.PWSTR
    DefaultValue: Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA
    OptionType: Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_TYPE
class DHCP_OPTION_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Options: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_head)
class DHCP_OPTION_DATA(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA_ELEMENT_head)
class DHCP_OPTION_DATA_ELEMENT(EasyCastStructure):
    OptionType: Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA_TYPE
    Element: DHCP_OPTION_ELEMENT_UNION
    class DHCP_OPTION_ELEMENT_UNION(EasyCastUnion):
        ByteOption: Byte
        WordOption: UInt16
        DWordOption: UInt32
        DWordDWordOption: Windows.Win32.NetworkManagement.Dhcp.DWORD_DWORD
        IpAddressOption: UInt32
        StringDataOption: Windows.Win32.Foundation.PWSTR
        BinaryDataOption: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        EncapsulatedDataOption: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        Ipv6AddressDataOption: Windows.Win32.Foundation.PWSTR
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
class DHCP_OPTION_ELEMENT_UNION(EasyCastUnion):
    pass
class DHCP_OPTION_LIST(EasyCastStructure):
    NumOptions: UInt32
    Options: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)
class DHCP_OPTION_SCOPE_INFO(EasyCastStructure):
    ScopeType: Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_TYPE
    ScopeInfo: _DHCP_OPTION_SCOPE_UNION
    class _DHCP_OPTION_SCOPE_UNION(EasyCastUnion):
        DefaultScopeInfo: c_void_p
        GlobalScopeInfo: c_void_p
        SubnetScopeInfo: UInt32
        ReservedScopeInfo: Windows.Win32.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE
        MScopeInfo: Windows.Win32.Foundation.PWSTR
class DHCP_OPTION_SCOPE_INFO6(EasyCastStructure):
    ScopeType: Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_SCOPE_TYPE6
    ScopeInfo: DHCP_OPTION_SCOPE_UNION6
    class DHCP_OPTION_SCOPE_UNION6(EasyCastUnion):
        DefaultScopeInfo: c_void_p
        SubnetScopeInfo: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
        ReservedScopeInfo: Windows.Win32.NetworkManagement.Dhcp.DHCP_RESERVED_SCOPE6
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
class DHCP_OPTION_SCOPE_UNION6(EasyCastUnion):
    pass
DHCP_OPTION_TYPE = Int32
DHCP_OPTION_TYPE_DhcpUnaryElementTypeOption: DHCP_OPTION_TYPE = 0
DHCP_OPTION_TYPE_DhcpArrayTypeOption: DHCP_OPTION_TYPE = 1
class DHCP_OPTION_VALUE(EasyCastStructure):
    OptionID: UInt32
    Value: Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_DATA
class DHCP_OPTION_VALUE_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Values: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_OPTION_VALUE_head)
class DHCP_PERF_STATS(EasyCastStructure):
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
class DHCP_POLICY(EasyCastStructure):
    PolicyName: Windows.Win32.Foundation.PWSTR
    IsGlobalPolicy: Windows.Win32.Foundation.BOOL
    Subnet: UInt32
    ProcessingOrder: UInt32
    Conditions: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_COND_ARRAY_head)
    Expressions: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_EXPR_ARRAY_head)
    Ranges: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_ARRAY_head)
    Description: Windows.Win32.Foundation.PWSTR
    Enabled: Windows.Win32.Foundation.BOOL
class DHCP_POLICY_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_head)
class DHCP_POLICY_EX(EasyCastStructure):
    PolicyName: Windows.Win32.Foundation.PWSTR
    IsGlobalPolicy: Windows.Win32.Foundation.BOOL
    Subnet: UInt32
    ProcessingOrder: UInt32
    Conditions: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_COND_ARRAY_head)
    Expressions: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_EXPR_ARRAY_head)
    Ranges: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_ARRAY_head)
    Description: Windows.Win32.Foundation.PWSTR
    Enabled: Windows.Win32.Foundation.BOOL
    Properties: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_ARRAY_head)
class DHCP_POLICY_EX_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POLICY_EX_head)
DHCP_POLICY_FIELDS_TO_UPDATE = Int32
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyName: DHCP_POLICY_FIELDS_TO_UPDATE = 1
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyOrder: DHCP_POLICY_FIELDS_TO_UPDATE = 2
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyExpr: DHCP_POLICY_FIELDS_TO_UPDATE = 4
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyRanges: DHCP_POLICY_FIELDS_TO_UPDATE = 8
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDescr: DHCP_POLICY_FIELDS_TO_UPDATE = 16
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyStatus: DHCP_POLICY_FIELDS_TO_UPDATE = 32
DHCP_POLICY_FIELDS_TO_UPDATE_DhcpUpdatePolicyDnsSuffix: DHCP_POLICY_FIELDS_TO_UPDATE = 64
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
class DHCP_POL_COND(EasyCastStructure):
    ParentExpr: UInt32
    Type: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_ATTR_TYPE
    OptionID: UInt32
    SubOptionID: UInt32
    VendorName: Windows.Win32.Foundation.PWSTR
    Operator: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_COMPARATOR
    Value: POINTER(Byte)
    ValueLength: UInt32
class DHCP_POL_COND_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_COND_head)
class DHCP_POL_EXPR(EasyCastStructure):
    ParentExpr: UInt32
    Operator: Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_LOGIC_OPER
class DHCP_POL_EXPR_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_POL_EXPR_head)
DHCP_POL_LOGIC_OPER = Int32
DHCP_POL_LOGIC_OPER_DhcpLogicalOr: DHCP_POL_LOGIC_OPER = 0
DHCP_POL_LOGIC_OPER_DhcpLogicalAnd: DHCP_POL_LOGIC_OPER = 1
class DHCP_PROPERTY(EasyCastStructure):
    ID: Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_ID
    Type: Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_TYPE
    Value: _DHCP_PROPERTY_VALUE_UNION
    class _DHCP_PROPERTY_VALUE_UNION(EasyCastUnion):
        ByteValue: Byte
        WordValue: UInt16
        DWordValue: UInt32
        StringValue: Windows.Win32.Foundation.PWSTR
        BinaryValue: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
class DHCP_PROPERTY_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_PROPERTY_head)
DHCP_PROPERTY_ID = Int32
DHCP_PROPERTY_ID_DhcpPropIdPolicyDnsSuffix: DHCP_PROPERTY_ID = 0
DHCP_PROPERTY_ID_DhcpPropIdClientAddressStateEx: DHCP_PROPERTY_ID = 1
DHCP_PROPERTY_TYPE = Int32
DHCP_PROPERTY_TYPE_DhcpPropTypeByte: DHCP_PROPERTY_TYPE = 0
DHCP_PROPERTY_TYPE_DhcpPropTypeWord: DHCP_PROPERTY_TYPE = 1
DHCP_PROPERTY_TYPE_DhcpPropTypeDword: DHCP_PROPERTY_TYPE = 2
DHCP_PROPERTY_TYPE_DhcpPropTypeString: DHCP_PROPERTY_TYPE = 3
DHCP_PROPERTY_TYPE_DhcpPropTypeBinary: DHCP_PROPERTY_TYPE = 4
class DHCP_RESERVATION_INFO_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_INFO_head))
class DHCP_RESERVED_SCOPE(EasyCastStructure):
    ReservedIpAddress: UInt32
    ReservedIpSubnetAddress: UInt32
class DHCP_RESERVED_SCOPE6(EasyCastStructure):
    ReservedIpAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    ReservedIpSubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
DHCP_SCAN_FLAG = Int32
DHCP_SCAN_FLAG_DhcpRegistryFix: DHCP_SCAN_FLAG = 0
DHCP_SCAN_FLAG_DhcpDatabaseFix: DHCP_SCAN_FLAG = 1
class DHCP_SCAN_ITEM(EasyCastStructure):
    IpAddress: UInt32
    ScanFlag: Windows.Win32.NetworkManagement.Dhcp.DHCP_SCAN_FLAG
class DHCP_SCAN_LIST(EasyCastStructure):
    NumScanItems: UInt32
    ScanItems: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SCAN_ITEM_head)
class DHCP_SEARCH_INFO(EasyCastStructure):
    SearchType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_TYPE
    SearchInfo: DHCP_CLIENT_SEARCH_UNION
    class DHCP_CLIENT_SEARCH_UNION(EasyCastUnion):
        ClientIpAddress: UInt32
        ClientHardwareAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        ClientName: Windows.Win32.Foundation.PWSTR
DHCP_SEARCH_INFO_TYPE = Int32
DHCP_SEARCH_INFO_TYPE_DhcpClientIpAddress: DHCP_SEARCH_INFO_TYPE = 0
DHCP_SEARCH_INFO_TYPE_DhcpClientHardwareAddress: DHCP_SEARCH_INFO_TYPE = 1
DHCP_SEARCH_INFO_TYPE_DhcpClientName: DHCP_SEARCH_INFO_TYPE = 2
DHCP_SEARCH_INFO_TYPE_V6 = Int32
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientIpAddress: DHCP_SEARCH_INFO_TYPE_V6 = 0
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientDUID: DHCP_SEARCH_INFO_TYPE_V6 = 1
DHCP_SEARCH_INFO_TYPE_V6_Dhcpv6ClientName: DHCP_SEARCH_INFO_TYPE_V6 = 2
class DHCP_SEARCH_INFO_V6(EasyCastStructure):
    SearchType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SEARCH_INFO_TYPE_V6
    SearchInfo: _DHCP_CLIENT_SEARCH_UNION_V6
    class _DHCP_CLIENT_SEARCH_UNION_V6(EasyCastUnion):
        ClientIpAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
        ClientDUID: Windows.Win32.NetworkManagement.Dhcp.DHCP_BINARY_DATA
        ClientName: Windows.Win32.Foundation.PWSTR
class DHCP_SERVER_CONFIG_INFO(EasyCastStructure):
    APIProtocolSupport: UInt32
    DatabaseName: Windows.Win32.Foundation.PWSTR
    DatabasePath: Windows.Win32.Foundation.PWSTR
    BackupPath: Windows.Win32.Foundation.PWSTR
    BackupInterval: UInt32
    DatabaseLoggingFlag: UInt32
    RestoreFlag: UInt32
    DatabaseCleanupInterval: UInt32
    DebugFlag: UInt32
class DHCP_SERVER_CONFIG_INFO_V4(EasyCastStructure):
    APIProtocolSupport: UInt32
    DatabaseName: Windows.Win32.Foundation.PWSTR
    DatabasePath: Windows.Win32.Foundation.PWSTR
    BackupPath: Windows.Win32.Foundation.PWSTR
    BackupInterval: UInt32
    DatabaseLoggingFlag: UInt32
    RestoreFlag: UInt32
    DatabaseCleanupInterval: UInt32
    DebugFlag: UInt32
    dwPingRetries: UInt32
    cbBootTableString: UInt32
    wszBootTableString: Windows.Win32.Foundation.PWSTR
    fAuditLog: Windows.Win32.Foundation.BOOL
class DHCP_SERVER_CONFIG_INFO_V6(EasyCastStructure):
    UnicastFlag: Windows.Win32.Foundation.BOOL
    RapidCommitFlag: Windows.Win32.Foundation.BOOL
    PreferredLifetime: UInt32
    ValidLifetime: UInt32
    T1: UInt32
    T2: UInt32
    PreferredLifetimeIATA: UInt32
    ValidLifetimeIATA: UInt32
    fAuditLog: Windows.Win32.Foundation.BOOL
class DHCP_SERVER_CONFIG_INFO_VQ(EasyCastStructure):
    APIProtocolSupport: UInt32
    DatabaseName: Windows.Win32.Foundation.PWSTR
    DatabasePath: Windows.Win32.Foundation.PWSTR
    BackupPath: Windows.Win32.Foundation.PWSTR
    BackupInterval: UInt32
    DatabaseLoggingFlag: UInt32
    RestoreFlag: UInt32
    DatabaseCleanupInterval: UInt32
    DebugFlag: UInt32
    dwPingRetries: UInt32
    cbBootTableString: UInt32
    wszBootTableString: Windows.Win32.Foundation.PWSTR
    fAuditLog: Windows.Win32.Foundation.BOOL
    QuarantineOn: Windows.Win32.Foundation.BOOL
    QuarDefFail: UInt32
    QuarRuntimeStatus: Windows.Win32.Foundation.BOOL
class DHCP_SERVER_OPTIONS(EasyCastStructure):
    MessageType: POINTER(Byte)
    SubnetMask: POINTER(UInt32)
    RequestedAddress: POINTER(UInt32)
    RequestLeaseTime: POINTER(UInt32)
    OverlayFields: POINTER(Byte)
    RouterAddress: POINTER(UInt32)
    Server: POINTER(UInt32)
    ParameterRequestList: POINTER(Byte)
    ParameterRequestListLength: UInt32
    MachineName: Windows.Win32.Foundation.PSTR
    MachineNameLength: UInt32
    ClientHardwareAddressType: Byte
    ClientHardwareAddressLength: Byte
    ClientHardwareAddress: POINTER(Byte)
    ClassIdentifier: Windows.Win32.Foundation.PSTR
    ClassIdentifierLength: UInt32
    VendorClass: POINTER(Byte)
    VendorClassLength: UInt32
    DNSFlags: UInt32
    DNSNameLength: UInt32
    DNSName: POINTER(Byte)
    DSDomainNameRequested: Windows.Win32.Foundation.BOOLEAN
    DSDomainName: Windows.Win32.Foundation.PSTR
    DSDomainNameLen: UInt32
    ScopeId: POINTER(UInt32)
class DHCP_SERVER_SPECIFIC_STRINGS(EasyCastStructure):
    DefaultVendorClassName: Windows.Win32.Foundation.PWSTR
    DefaultUserClassName: Windows.Win32.Foundation.PWSTR
class DHCP_SUBNET_ELEMENT_DATA(EasyCastStructure):
    ElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE
    Element: DHCP_SUBNET_ELEMENT_UNION
    class DHCP_SUBNET_ELEMENT_UNION(EasyCastUnion):
        IpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        SecondaryHost: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)
        ReservedIp: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_head)
        ExcludeIpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        IpUsedCluster: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)
class DHCP_SUBNET_ELEMENT_DATA_V4(EasyCastStructure):
    ElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE
    Element: DHCP_SUBNET_ELEMENT_UNION_V4
    class DHCP_SUBNET_ELEMENT_UNION_V4(EasyCastUnion):
        IpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        SecondaryHost: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)
        ReservedIp: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V4_head)
        ExcludeIpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        IpUsedCluster: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)
class DHCP_SUBNET_ELEMENT_DATA_V5(EasyCastStructure):
    ElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE
    Element: _DHCP_SUBNET_ELEMENT_UNION_V5
    class _DHCP_SUBNET_ELEMENT_UNION_V5(EasyCastUnion):
        IpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_BOOTP_IP_RANGE_head)
        SecondaryHost: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO_head)
        ReservedIp: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V4_head)
        ExcludeIpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_head)
        IpUsedCluster: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_CLUSTER_head)
class DHCP_SUBNET_ELEMENT_DATA_V6(EasyCastStructure):
    ElementType: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_TYPE_V6
    Element: DHCP_SUBNET_ELEMENT_UNION_V6
    class DHCP_SUBNET_ELEMENT_UNION_V6(EasyCastUnion):
        IpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_V6_head)
        ReservedIp: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RESERVATION_V6_head)
        ExcludeIpRange: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_IP_RANGE_V6_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V4_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V5_head)
class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(EasyCastStructure):
    NumElements: UInt32
    Elements: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_ELEMENT_DATA_V6_head)
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
class DHCP_SUBNET_ELEMENT_UNION(EasyCastUnion):
    pass
class DHCP_SUBNET_ELEMENT_UNION_V4(EasyCastUnion):
    pass
class DHCP_SUBNET_ELEMENT_UNION_V6(EasyCastUnion):
    pass
class DHCP_SUBNET_INFO(EasyCastStructure):
    SubnetAddress: UInt32
    SubnetMask: UInt32
    SubnetName: Windows.Win32.Foundation.PWSTR
    SubnetComment: Windows.Win32.Foundation.PWSTR
    PrimaryHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    SubnetState: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_STATE
class DHCP_SUBNET_INFO_V6(EasyCastStructure):
    SubnetAddress: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    Prefix: UInt32
    Preference: UInt16
    SubnetName: Windows.Win32.Foundation.PWSTR
    SubnetComment: Windows.Win32.Foundation.PWSTR
    State: UInt32
    ScopeId: UInt32
class DHCP_SUBNET_INFO_VQ(EasyCastStructure):
    SubnetAddress: UInt32
    SubnetMask: UInt32
    SubnetName: Windows.Win32.Foundation.PWSTR
    SubnetComment: Windows.Win32.Foundation.PWSTR
    PrimaryHost: Windows.Win32.NetworkManagement.Dhcp.DHCP_HOST_INFO
    SubnetState: Windows.Win32.NetworkManagement.Dhcp.DHCP_SUBNET_STATE
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
class DHCP_SUPER_SCOPE_TABLE(EasyCastStructure):
    cEntries: UInt32
    pEntries: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SUPER_SCOPE_TABLE_ENTRY_head)
class DHCP_SUPER_SCOPE_TABLE_ENTRY(EasyCastStructure):
    SubnetAddress: UInt32
    SuperScopeNumber: UInt32
    NextInSuperScope: UInt32
    SuperScopeName: Windows.Win32.Foundation.PWSTR
class DWORD_DWORD(EasyCastStructure):
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
def LPDHCP_DELETE_CLIENT(IpAddress: UInt32, HwAddress: POINTER(Byte), HwAddressLength: UInt32, Reserved: UInt32, ClientType: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_DROP_SEND(Packet: POINTER(POINTER(Byte)), PacketSize: POINTER(UInt32), ControlCode: UInt32, IpAddress: UInt32, Reserved: c_void_p, PktContext: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_ENTRY_POINT_FUNC(ChainDlls: Windows.Win32.Foundation.PWSTR, CalloutVersion: UInt32, CalloutTbl: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_CALLOUT_TABLE_head)) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_GIVE_ADDRESS(Packet: POINTER(Byte), PacketSize: UInt32, ControlCode: UInt32, IpAddress: UInt32, AltAddress: UInt32, AddrType: UInt32, LeaseTime: UInt32, Reserved: c_void_p, PktContext: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_HANDLE_OPTIONS(Packet: POINTER(Byte), PacketSize: UInt32, Reserved: c_void_p, PktContext: c_void_p, ServerOptions: POINTER(Windows.Win32.NetworkManagement.Dhcp.DHCP_SERVER_OPTIONS_head)) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_NEWPKT(Packet: POINTER(POINTER(Byte)), PacketSize: POINTER(UInt32), IpAddress: UInt32, Reserved: c_void_p, PktContext: POINTER(c_void_p), ProcessIt: POINTER(Int32)) -> UInt32: ...
@winfunctype_pointer
def LPDHCP_PROB(Packet: POINTER(Byte), PacketSize: UInt32, ControlCode: UInt32, IpAddress: UInt32, AltAddress: UInt32, Reserved: c_void_p, PktContext: c_void_p) -> UInt32: ...
QuarantineStatus = Int32
NOQUARANTINE: QuarantineStatus = 0
RESTRICTEDACCESS: QuarantineStatus = 1
DROPPACKET: QuarantineStatus = 2
PROBATION: QuarantineStatus = 3
EXEMPT: QuarantineStatus = 4
DEFAULTQUARSETTING: QuarantineStatus = 5
NOQUARINFO: QuarantineStatus = 6
class SCOPE_MIB_INFO(EasyCastStructure):
    Subnet: UInt32
    NumAddressesInuse: UInt32
    NumAddressesFree: UInt32
    NumPendingOffers: UInt32
class SCOPE_MIB_INFO_V5(EasyCastStructure):
    Subnet: UInt32
    NumAddressesInuse: UInt32
    NumAddressesFree: UInt32
    NumPendingOffers: UInt32
class SCOPE_MIB_INFO_V6(EasyCastStructure):
    Subnet: Windows.Win32.NetworkManagement.Dhcp.DHCP_IPV6_ADDRESS
    NumAddressesInuse: UInt64
    NumAddressesFree: UInt64
    NumPendingAdvertises: UInt64
class SCOPE_MIB_INFO_VQ(EasyCastStructure):
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
make_head(_module, 'DHCPAPI_PARAMS')
make_head(_module, 'DHCPCAPI_CLASSID')
make_head(_module, 'DHCPCAPI_PARAMS_ARRAY')
make_head(_module, 'DHCPDS_SERVER')
make_head(_module, 'DHCPDS_SERVERS')
make_head(_module, 'DHCPV4_FAILOVER_CLIENT_INFO')
make_head(_module, 'DHCPV4_FAILOVER_CLIENT_INFO_ARRAY')
make_head(_module, 'DHCPV4_FAILOVER_CLIENT_INFO_EX')
make_head(_module, 'DHCPV6CAPI_CLASSID')
make_head(_module, 'DHCPV6CAPI_PARAMS')
make_head(_module, 'DHCPV6CAPI_PARAMS_ARRAY')
make_head(_module, 'DHCPV6Prefix')
make_head(_module, 'DHCPV6PrefixLeaseInformation')
make_head(_module, 'DHCPV6_BIND_ELEMENT')
make_head(_module, 'DHCPV6_BIND_ELEMENT_ARRAY')
make_head(_module, 'DHCPV6_IP_ARRAY')
make_head(_module, 'DHCPV6_STATELESS_PARAMS')
make_head(_module, 'DHCPV6_STATELESS_SCOPE_STATS')
make_head(_module, 'DHCPV6_STATELESS_STATS')
make_head(_module, 'DHCP_ADDR_PATTERN')
make_head(_module, 'DHCP_ALL_OPTIONS')
make_head(_module, 'DHCP_ALL_OPTION_VALUES')
make_head(_module, 'DHCP_ALL_OPTION_VALUES_PB')
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
make_head(_module, 'DHCP_IPV6_ADDRESS')
make_head(_module, 'DHCP_IP_ARRAY')
make_head(_module, 'DHCP_IP_CLUSTER')
make_head(_module, 'DHCP_IP_RANGE')
make_head(_module, 'DHCP_IP_RANGE_ARRAY')
make_head(_module, 'DHCP_IP_RANGE_V6')
make_head(_module, 'DHCP_IP_RESERVATION')
make_head(_module, 'DHCP_IP_RESERVATION_INFO')
make_head(_module, 'DHCP_IP_RESERVATION_V4')
make_head(_module, 'DHCP_IP_RESERVATION_V6')
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
make_head(_module, 'DHCP_POLICY')
make_head(_module, 'DHCP_POLICY_ARRAY')
make_head(_module, 'DHCP_POLICY_EX')
make_head(_module, 'DHCP_POLICY_EX_ARRAY')
make_head(_module, 'DHCP_POL_COND')
make_head(_module, 'DHCP_POL_COND_ARRAY')
make_head(_module, 'DHCP_POL_EXPR')
make_head(_module, 'DHCP_POL_EXPR_ARRAY')
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
