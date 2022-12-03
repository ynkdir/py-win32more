from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Networking.Ldap
import win32more.Security.Authentication.Identity
import win32more.Security.Cryptography
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
LBER_ERROR = -1
LBER_DEFAULT = -1
LDAP_UNICODE = 1
LDAP_PORT = 389
LDAP_SSL_PORT = 636
LDAP_GC_PORT = 3268
LDAP_SSL_GC_PORT = 3269
LDAP_VERSION1 = 1
LDAP_VERSION2 = 2
LDAP_VERSION3 = 3
LDAP_VERSION = 2
LDAP_BIND_CMD = 96
LDAP_UNBIND_CMD = 66
LDAP_SEARCH_CMD = 99
LDAP_MODIFY_CMD = 102
LDAP_ADD_CMD = 104
LDAP_DELETE_CMD = 74
LDAP_MODRDN_CMD = 108
LDAP_COMPARE_CMD = 110
LDAP_ABANDON_CMD = 80
LDAP_SESSION_CMD = 113
LDAP_EXTENDED_CMD = 119
LDAP_RES_BIND = 97
LDAP_RES_SEARCH_ENTRY = 100
LDAP_RES_SEARCH_RESULT = 101
LDAP_RES_MODIFY = 103
LDAP_RES_ADD = 105
LDAP_RES_DELETE = 107
LDAP_RES_MODRDN = 109
LDAP_RES_COMPARE = 111
LDAP_RES_SESSION = 114
LDAP_RES_REFERRAL = 115
LDAP_RES_EXTENDED = 120
LDAP_RES_ANY = -1
LDAP_INVALID_CMD = 255
LDAP_INVALID_RES = 255
LDAP_AUTH_SIMPLE = 128
LDAP_AUTH_SASL = 131
LDAP_AUTH_OTHERKIND = 134
LDAP_FILTER_AND = 160
LDAP_FILTER_OR = 161
LDAP_FILTER_NOT = 162
LDAP_FILTER_EQUALITY = 163
LDAP_FILTER_SUBSTRINGS = 164
LDAP_FILTER_GE = 165
LDAP_FILTER_LE = 166
LDAP_FILTER_PRESENT = 135
LDAP_FILTER_APPROX = 168
LDAP_FILTER_EXTENSIBLE = 169
LDAP_SUBSTRING_INITIAL = 128
LDAP_SUBSTRING_ANY = 129
LDAP_SUBSTRING_FINAL = 130
LDAP_DEREF_NEVER = 0
LDAP_DEREF_SEARCHING = 1
LDAP_DEREF_FINDING = 2
LDAP_DEREF_ALWAYS = 3
LDAP_NO_LIMIT = 0
LDAP_OPT_DNS = 1
LDAP_OPT_CHASE_REFERRALS = 2
LDAP_OPT_RETURN_REFS = 4
LDAP_CONTROL_REFERRALS_W = '1.2.840.113556.1.4.616'
LDAP_CONTROL_REFERRALS = '1.2.840.113556.1.4.616'
LDAP_MOD_ADD = 0
LDAP_MOD_DELETE = 1
LDAP_MOD_REPLACE = 2
LDAP_MOD_BVALUES = 128
LDAP_OPT_API_INFO = 0
LDAP_OPT_DESC = 1
LDAP_OPT_DEREF = 2
LDAP_OPT_SIZELIMIT = 3
LDAP_OPT_TIMELIMIT = 4
LDAP_OPT_THREAD_FN_PTRS = 5
LDAP_OPT_REBIND_FN = 6
LDAP_OPT_REBIND_ARG = 7
LDAP_OPT_REFERRALS = 8
LDAP_OPT_RESTART = 9
LDAP_OPT_SSL = 10
LDAP_OPT_IO_FN_PTRS = 11
LDAP_OPT_CACHE_FN_PTRS = 13
LDAP_OPT_CACHE_STRATEGY = 14
LDAP_OPT_CACHE_ENABLE = 15
LDAP_OPT_REFERRAL_HOP_LIMIT = 16
LDAP_OPT_PROTOCOL_VERSION = 17
LDAP_OPT_VERSION = 17
LDAP_OPT_API_FEATURE_INFO = 21
LDAP_OPT_HOST_NAME = 48
LDAP_OPT_ERROR_NUMBER = 49
LDAP_OPT_ERROR_STRING = 50
LDAP_OPT_SERVER_ERROR = 51
LDAP_OPT_SERVER_EXT_ERROR = 52
LDAP_OPT_HOST_REACHABLE = 62
LDAP_OPT_PING_KEEP_ALIVE = 54
LDAP_OPT_PING_WAIT_TIME = 55
LDAP_OPT_PING_LIMIT = 56
LDAP_OPT_DNSDOMAIN_NAME = 59
LDAP_OPT_GETDSNAME_FLAGS = 61
LDAP_OPT_PROMPT_CREDENTIALS = 63
LDAP_OPT_AUTO_RECONNECT = 145
LDAP_OPT_SSPI_FLAGS = 146
LDAP_OPT_SSL_INFO = 147
LDAP_OPT_TLS = 10
LDAP_OPT_TLS_INFO = 147
LDAP_OPT_SIGN = 149
LDAP_OPT_ENCRYPT = 150
LDAP_OPT_SASL_METHOD = 151
LDAP_OPT_AREC_EXCLUSIVE = 152
LDAP_OPT_SECURITY_CONTEXT = 153
LDAP_OPT_ROOTDSE_CACHE = 154
LDAP_OPT_TCP_KEEPALIVE = 64
LDAP_OPT_FAST_CONCURRENT_BIND = 65
LDAP_OPT_SEND_TIMEOUT = 66
LDAP_OPT_SCH_FLAGS = 67
LDAP_OPT_SOCKET_BIND_ADDRESSES = 68
LDAP_CHASE_SUBORDINATE_REFERRALS = 32
LDAP_CHASE_EXTERNAL_REFERRALS = 64
LDAP_SCOPE_BASE = 0
LDAP_SCOPE_ONELEVEL = 1
LDAP_SCOPE_SUBTREE = 2
LDAP_MSG_ONE = 0
LDAP_MSG_ALL = 1
LDAP_MSG_RECEIVED = 2
LBER_USE_DER = 1
LBER_USE_INDEFINITE_LEN = 2
LBER_TRANSLATE_STRINGS = 4
LAPI_MAJOR_VER1 = 1
LAPI_MINOR_VER1 = 1
LDAP_API_INFO_VERSION = 1
LDAP_API_VERSION = 2004
LDAP_VERSION_MIN = 2
LDAP_VERSION_MAX = 3
LDAP_VENDOR_NAME = 'Microsoft Corporation.'
LDAP_VENDOR_NAME_W = 'Microsoft Corporation.'
LDAP_VENDOR_VERSION = 510
LDAP_FEATURE_INFO_VERSION = 1
LDAP_SERVER_SORT_OID = '1.2.840.113556.1.4.473'
LDAP_SERVER_SORT_OID_W = '1.2.840.113556.1.4.473'
LDAP_SERVER_RESP_SORT_OID = '1.2.840.113556.1.4.474'
LDAP_SERVER_RESP_SORT_OID_W = '1.2.840.113556.1.4.474'
LDAP_PAGED_RESULT_OID_STRING = '1.2.840.113556.1.4.319'
LDAP_PAGED_RESULT_OID_STRING_W = '1.2.840.113556.1.4.319'
LDAP_CONTROL_VLVREQUEST = '2.16.840.1.113730.3.4.9'
LDAP_CONTROL_VLVREQUEST_W = '2.16.840.1.113730.3.4.9'
LDAP_CONTROL_VLVRESPONSE = '2.16.840.1.113730.3.4.10'
LDAP_CONTROL_VLVRESPONSE_W = '2.16.840.1.113730.3.4.10'
LDAP_API_FEATURE_VIRTUAL_LIST_VIEW = 1001
LDAP_VLVINFO_VERSION = 1
LDAP_START_TLS_OID = '1.3.6.1.4.1.1466.20037'
LDAP_START_TLS_OID_W = '1.3.6.1.4.1.1466.20037'
LDAP_TTL_EXTENDED_OP_OID = '1.3.6.1.4.1.1466.101.119.1'
LDAP_TTL_EXTENDED_OP_OID_W = '1.3.6.1.4.1.1466.101.119.1'
LDAP_OPT_REFERRAL_CALLBACK = 112
LDAP_OPT_CLIENT_CERTIFICATE = 128
LDAP_OPT_SERVER_CERTIFICATE = 129
LDAP_OPT_REF_DEREF_CONN_PER_MSG = 148
LDAP_SERVER_FORCE_UPDATE_OID = '1.2.840.113556.1.4.1974'
LDAP_SERVER_FORCE_UPDATE_OID_W = '1.2.840.113556.1.4.1974'
LDAP_SERVER_PERMISSIVE_MODIFY_OID = '1.2.840.113556.1.4.1413'
LDAP_SERVER_PERMISSIVE_MODIFY_OID_W = '1.2.840.113556.1.4.1413'
LDAP_SERVER_SHOW_DELETED_OID = '1.2.840.113556.1.4.417'
LDAP_SERVER_SHOW_DELETED_OID_W = '1.2.840.113556.1.4.417'
LDAP_SERVER_SHOW_RECYCLED_OID = '1.2.840.113556.1.4.2064'
LDAP_SERVER_SHOW_RECYCLED_OID_W = '1.2.840.113556.1.4.2064'
LDAP_SERVER_EXPECTED_ENTRY_COUNT_OID = '1.2.840.113556.1.4.2211'
LDAP_SERVER_EXPECTED_ENTRY_COUNT_OID_W = '1.2.840.113556.1.4.2211'
LDAP_SERVER_SEARCH_HINTS_OID = '1.2.840.113556.1.4.2206'
LDAP_SERVER_SEARCH_HINTS_OID_W = '1.2.840.113556.1.4.2206'
LDAP_SEARCH_HINT_INDEX_ONLY_OID = '1.2.840.113556.1.4.2207'
LDAP_SEARCH_HINT_INDEX_ONLY_OID_W = '1.2.840.113556.1.4.2207'
LDAP_SEARCH_HINT_SOFT_SIZE_LIMIT_OID = '1.2.840.113556.1.4.2210'
LDAP_SEARCH_HINT_SOFT_SIZE_LIMIT_OID_W = '1.2.840.113556.1.4.2210'
LDAP_SEARCH_HINT_REQUIRED_INDEX_OID = '1.2.840.113556.1.4.2306'
LDAP_SEARCH_HINT_REQUIRED_INDEX_OID_W = '1.2.840.113556.1.4.2306'
LDAP_SERVER_UPDATE_STATS_OID = '1.2.840.113556.1.4.2205'
LDAP_SERVER_UPDATE_STATS_OID_W = '1.2.840.113556.1.4.2205'
LDAP_UPDATE_STATS_USN_OID = '1.2.840.113556.1.4.2208'
LDAP_UPDATE_STATS_USN_OID_W = '1.2.840.113556.1.4.2208'
LDAP_UPDATE_STATS_INVOCATIONID_OID = '1.2.840.113556.1.4.2209'
LDAP_UPDATE_STATS_INVOCATIONID_OID_W = '1.2.840.113556.1.4.2209'
LDAP_SERVER_GET_STATS_OID = '1.2.840.113556.1.4.970'
LDAP_SERVER_GET_STATS_OID_W = '1.2.840.113556.1.4.970'
LDAP_SERVER_SHOW_DEACTIVATED_LINK_OID = '1.2.840.113556.1.4.2065'
LDAP_SERVER_SHOW_DEACTIVATED_LINK_OID_W = '1.2.840.113556.1.4.2065'
LDAP_SERVER_POLICY_HINTS_DEPRECATED_OID = '1.2.840.113556.1.4.2066'
LDAP_SERVER_POLICY_HINTS_DEPRECATED_OID_W = '1.2.840.113556.1.4.2066'
LDAP_SERVER_POLICY_HINTS_OID = '1.2.840.113556.1.4.2239'
LDAP_SERVER_POLICY_HINTS_OID_W = '1.2.840.113556.1.4.2239'
LDAP_SERVER_RANGE_OPTION_OID = '1.2.840.113556.1.4.802'
LDAP_SERVER_RANGE_OPTION_OID_W = '1.2.840.113556.1.4.802'
LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID = '1.2.840.113556.1.4.521'
LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID_W = '1.2.840.113556.1.4.521'
LDAP_SERVER_NOTIFICATION_OID = '1.2.840.113556.1.4.528'
LDAP_SERVER_NOTIFICATION_OID_W = '1.2.840.113556.1.4.528'
LDAP_SERVER_SHUTDOWN_NOTIFY_OID = '1.2.840.113556.1.4.1907'
LDAP_SERVER_SHUTDOWN_NOTIFY_OID_W = '1.2.840.113556.1.4.1907'
LDAP_SERVER_LAZY_COMMIT_OID = '1.2.840.113556.1.4.619'
LDAP_SERVER_LAZY_COMMIT_OID_W = '1.2.840.113556.1.4.619'
LDAP_SERVER_SD_FLAGS_OID = '1.2.840.113556.1.4.801'
LDAP_SERVER_SD_FLAGS_OID_W = '1.2.840.113556.1.4.801'
LDAP_SERVER_TREE_DELETE_EX_OID = '1.2.840.113556.1.4.2204'
LDAP_SERVER_TREE_DELETE_EX_OID_W = '1.2.840.113556.1.4.2204'
LDAP_SERVER_TREE_DELETE_OID = '1.2.840.113556.1.4.805'
LDAP_SERVER_TREE_DELETE_OID_W = '1.2.840.113556.1.4.805'
LDAP_SERVER_ASQ_OID = '1.2.840.113556.1.4.1504'
LDAP_SERVER_ASQ_OID_W = '1.2.840.113556.1.4.1504'
LDAP_SERVER_DIRSYNC_OID = '1.2.840.113556.1.4.841'
LDAP_SERVER_DIRSYNC_OID_W = '1.2.840.113556.1.4.841'
LDAP_SERVER_DIRSYNC_EX_OID = '1.2.840.113556.1.4.2090'
LDAP_SERVER_DIRSYNC_EX_OID_W = '1.2.840.113556.1.4.2090'
LDAP_SERVER_EXTENDED_DN_OID = '1.2.840.113556.1.4.529'
LDAP_SERVER_EXTENDED_DN_OID_W = '1.2.840.113556.1.4.529'
LDAP_SERVER_VERIFY_NAME_OID = '1.2.840.113556.1.4.1338'
LDAP_SERVER_VERIFY_NAME_OID_W = '1.2.840.113556.1.4.1338'
LDAP_SERVER_DOMAIN_SCOPE_OID = '1.2.840.113556.1.4.1339'
LDAP_SERVER_DOMAIN_SCOPE_OID_W = '1.2.840.113556.1.4.1339'
LDAP_SERVER_SEARCH_OPTIONS_OID = '1.2.840.113556.1.4.1340'
LDAP_SERVER_SEARCH_OPTIONS_OID_W = '1.2.840.113556.1.4.1340'
SERVER_SEARCH_FLAG_DOMAIN_SCOPE = 1
SERVER_SEARCH_FLAG_PHANTOM_ROOT = 2
LDAP_SERVER_QUOTA_CONTROL_OID = '1.2.840.113556.1.4.1852'
LDAP_SERVER_QUOTA_CONTROL_OID_W = '1.2.840.113556.1.4.1852'
LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID = '1.2.840.113556.1.4.1948'
LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID_W = '1.2.840.113556.1.4.1948'
LDAP_SERVER_DN_INPUT_OID = '1.2.840.113556.1.4.2026'
LDAP_SERVER_DN_INPUT_OID_W = '1.2.840.113556.1.4.2026'
LDAP_SERVER_SET_OWNER_OID = '1.2.840.113556.1.4.2255'
LDAP_SERVER_SET_OWNER_OID_W = '1.2.840.113556.1.4.2255'
LDAP_SERVER_BYPASS_QUOTA_OID = '1.2.840.113556.1.4.2256'
LDAP_SERVER_BYPASS_QUOTA_OID_W = '1.2.840.113556.1.4.2256'
LDAP_SERVER_LINK_TTL_OID = '1.2.840.113556.1.4.2309'
LDAP_SERVER_LINK_TTL_OID_W = '1.2.840.113556.1.4.2309'
LDAP_OPATT_BECOME_DOM_MASTER = 'becomeDomainMaster'
LDAP_OPATT_BECOME_DOM_MASTER_W = 'becomeDomainMaster'
LDAP_OPATT_BECOME_RID_MASTER = 'becomeRidMaster'
LDAP_OPATT_BECOME_RID_MASTER_W = 'becomeRidMaster'
LDAP_OPATT_BECOME_SCHEMA_MASTER = 'becomeSchemaMaster'
LDAP_OPATT_BECOME_SCHEMA_MASTER_W = 'becomeSchemaMaster'
LDAP_OPATT_RECALC_HIERARCHY = 'recalcHierarchy'
LDAP_OPATT_RECALC_HIERARCHY_W = 'recalcHierarchy'
LDAP_OPATT_SCHEMA_UPDATE_NOW = 'schemaUpdateNow'
LDAP_OPATT_SCHEMA_UPDATE_NOW_W = 'schemaUpdateNow'
LDAP_OPATT_BECOME_PDC = 'becomePdc'
LDAP_OPATT_BECOME_PDC_W = 'becomePdc'
LDAP_OPATT_FIXUP_INHERITANCE = 'fixupInheritance'
LDAP_OPATT_FIXUP_INHERITANCE_W = 'fixupInheritance'
LDAP_OPATT_INVALIDATE_RID_POOL = 'invalidateRidPool'
LDAP_OPATT_INVALIDATE_RID_POOL_W = 'invalidateRidPool'
LDAP_OPATT_ABANDON_REPL = 'abandonReplication'
LDAP_OPATT_ABANDON_REPL_W = 'abandonReplication'
LDAP_OPATT_DO_GARBAGE_COLLECTION = 'doGarbageCollection'
LDAP_OPATT_DO_GARBAGE_COLLECTION_W = 'doGarbageCollection'
LDAP_OPATT_SUBSCHEMA_SUBENTRY = 'subschemaSubentry'
LDAP_OPATT_SUBSCHEMA_SUBENTRY_W = 'subschemaSubentry'
LDAP_OPATT_CURRENT_TIME = 'currentTime'
LDAP_OPATT_CURRENT_TIME_W = 'currentTime'
LDAP_OPATT_SERVER_NAME = 'serverName'
LDAP_OPATT_SERVER_NAME_W = 'serverName'
LDAP_OPATT_NAMING_CONTEXTS = 'namingContexts'
LDAP_OPATT_NAMING_CONTEXTS_W = 'namingContexts'
LDAP_OPATT_DEFAULT_NAMING_CONTEXT = 'defaultNamingContext'
LDAP_OPATT_DEFAULT_NAMING_CONTEXT_W = 'defaultNamingContext'
LDAP_OPATT_SUPPORTED_CONTROL = 'supportedControl'
LDAP_OPATT_SUPPORTED_CONTROL_W = 'supportedControl'
LDAP_OPATT_HIGHEST_COMMITTED_USN = 'highestCommitedUSN'
LDAP_OPATT_HIGHEST_COMMITTED_USN_W = 'highestCommitedUSN'
LDAP_OPATT_SUPPORTED_LDAP_VERSION = 'supportedLDAPVersion'
LDAP_OPATT_SUPPORTED_LDAP_VERSION_W = 'supportedLDAPVersion'
LDAP_OPATT_SUPPORTED_LDAP_POLICIES = 'supportedLDAPPolicies'
LDAP_OPATT_SUPPORTED_LDAP_POLICIES_W = 'supportedLDAPPolicies'
LDAP_OPATT_SCHEMA_NAMING_CONTEXT = 'schemaNamingContext'
LDAP_OPATT_SCHEMA_NAMING_CONTEXT_W = 'schemaNamingContext'
LDAP_OPATT_CONFIG_NAMING_CONTEXT = 'configurationNamingContext'
LDAP_OPATT_CONFIG_NAMING_CONTEXT_W = 'configurationNamingContext'
LDAP_OPATT_ROOT_DOMAIN_NAMING_CONTEXT = 'rootDomainNamingContext'
LDAP_OPATT_ROOT_DOMAIN_NAMING_CONTEXT_W = 'rootDomainNamingContext'
LDAP_OPATT_SUPPORTED_SASL_MECHANISM = 'supportedSASLMechanisms'
LDAP_OPATT_SUPPORTED_SASL_MECHANISM_W = 'supportedSASLMechanisms'
LDAP_OPATT_DNS_HOST_NAME = 'dnsHostName'
LDAP_OPATT_DNS_HOST_NAME_W = 'dnsHostName'
LDAP_OPATT_LDAP_SERVICE_NAME = 'ldapServiceName'
LDAP_OPATT_LDAP_SERVICE_NAME_W = 'ldapServiceName'
LDAP_OPATT_DS_SERVICE_NAME = 'dsServiceName'
LDAP_OPATT_DS_SERVICE_NAME_W = 'dsServiceName'
LDAP_OPATT_SUPPORTED_CAPABILITIES = 'supportedCapabilities'
LDAP_OPATT_SUPPORTED_CAPABILITIES_W = 'supportedCapabilities'
LDAP_CAP_ACTIVE_DIRECTORY_OID = '1.2.840.113556.1.4.800'
LDAP_CAP_ACTIVE_DIRECTORY_OID_W = '1.2.840.113556.1.4.800'
LDAP_CAP_ACTIVE_DIRECTORY_V51_OID = '1.2.840.113556.1.4.1670'
LDAP_CAP_ACTIVE_DIRECTORY_V51_OID_W = '1.2.840.113556.1.4.1670'
LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID = '1.2.840.113556.1.4.1791'
LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID_W = '1.2.840.113556.1.4.1791'
LDAP_CAP_ACTIVE_DIRECTORY_ADAM_OID = '1.2.840.113556.1.4.1851'
LDAP_CAP_ACTIVE_DIRECTORY_ADAM_OID_W = '1.2.840.113556.1.4.1851'
LDAP_CAP_ACTIVE_DIRECTORY_PARTIAL_SECRETS_OID = '1.2.840.113556.1.4.1920'
LDAP_CAP_ACTIVE_DIRECTORY_PARTIAL_SECRETS_OID_W = '1.2.840.113556.1.4.1920'
LDAP_CAP_ACTIVE_DIRECTORY_V60_OID = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V60_OID_W = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V61_OID = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V61_OID_W = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V61_R2_OID = '1.2.840.113556.1.4.2080'
LDAP_CAP_ACTIVE_DIRECTORY_V61_R2_OID_W = '1.2.840.113556.1.4.2080'
LDAP_CAP_ACTIVE_DIRECTORY_W8_OID = '1.2.840.113556.1.4.2237'
LDAP_CAP_ACTIVE_DIRECTORY_W8_OID_W = '1.2.840.113556.1.4.2237'
LDAP_MATCHING_RULE_BIT_AND = '1.2.840.113556.1.4.803'
LDAP_MATCHING_RULE_BIT_AND_W = '1.2.840.113556.1.4.803'
LDAP_MATCHING_RULE_BIT_OR = '1.2.840.113556.1.4.804'
LDAP_MATCHING_RULE_BIT_OR_W = '1.2.840.113556.1.4.804'
LDAP_MATCHING_RULE_TRANSITIVE_EVALUATION = '1.2.840.113556.1.4.1941'
LDAP_MATCHING_RULE_TRANSITIVE_EVALUATION_W = '1.2.840.113556.1.4.1941'
LDAP_MATCHING_RULE_DN_BINARY_COMPLEX = '1.2.840.113556.1.4.2253'
LDAP_MATCHING_RULE_DN_BINARY_COMPLEX_W = '1.2.840.113556.1.4.2253'
LDAP_SERVER_FAST_BIND_OID = '1.2.840.113556.1.4.1781'
LDAP_SERVER_FAST_BIND_OID_W = '1.2.840.113556.1.4.1781'
LDAP_SERVER_WHO_AM_I_OID = '1.3.6.1.4.1.4203.1.11.3'
LDAP_SERVER_WHO_AM_I_OID_W = '1.3.6.1.4.1.4203.1.11.3'
LDAP_SERVER_BATCH_REQUEST_OID = '1.2.840.113556.1.4.2212'
LDAP_SERVER_BATCH_REQUEST_OID_W = '1.2.840.113556.1.4.2212'
LDAP_DIRSYNC_OBJECT_SECURITY = 1
LDAP_DIRSYNC_ANCESTORS_FIRST_ORDER = 2048
LDAP_DIRSYNC_PUBLIC_DATA_ONLY = 8192
LDAP_DIRSYNC_INCREMENTAL_VALUES = 2147483648
LDAP_DIRSYNC_ROPAS_DATA_ONLY = 1073741824
LDAP_POLICYHINT_APPLY_FULLPWDPOLICY = 1
def _define_ldap_openW():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32)(('ldap_openW', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_openA():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32)(('ldap_openA', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_initW():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32)(('ldap_initW', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_initA():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32)(('ldap_initA', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sslinitW():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32,Int32)(('ldap_sslinitW', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),(1, 'secure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sslinitA():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,Int32)(('ldap_sslinitA', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),(1, 'secure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_connect():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head))(('ldap_connect', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_open():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32)(('ldap_open', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_init():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32)(('ldap_init', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sslinit():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,Int32)(('ldap_sslinit', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),(1, 'secure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_cldap_openW():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32)(('cldap_openW', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_cldap_openA():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32)(('cldap_openA', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_cldap_open():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32)(('cldap_open', cdll['WLDAP32.dll']), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_unbind():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head))(('ldap_unbind', cdll['WLDAP32.dll']), ((1, 'ld'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_unbind_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head))(('ldap_unbind_s', cdll['WLDAP32.dll']), ((1, 'ld'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_option():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),Int32,c_void_p)(('ldap_get_option', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'option'),(1, 'outvalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_optionW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),Int32,c_void_p)(('ldap_get_optionW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'option'),(1, 'outvalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_option():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),Int32,c_void_p)(('ldap_set_option', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'option'),(1, 'invalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_optionW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),Int32,c_void_p)(('ldap_set_optionW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'option'),(1, 'invalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bindW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ldap_simple_bindW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bindA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_simple_bindA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bind_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ldap_simple_bind_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bind_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_simple_bind_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bindW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('ldap_bindW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bindA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('ldap_bindA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('ldap_bind_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('ldap_bind_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bindA():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(Int32))(('ldap_sasl_bindA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bindW():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(Int32))(('ldap_sasl_bindW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bind_sA():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_sasl_bind_sA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'ServerData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bind_sW():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_sasl_bind_sW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'ServerData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bind():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_simple_bind', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bind_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_simple_bind_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('ldap_bind', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('ldap_bind_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_searchW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32)(('ldap_searchW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_searchA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32)(('ldap_searchA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_stW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_stW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_stA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_stA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_extW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),UInt32,UInt32,POINTER(UInt32))(('ldap_search_extW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'TimeLimit'),(1, 'SizeLimit'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_extA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),UInt32,UInt32,POINTER(UInt32))(('ldap_search_extA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'TimeLimit'),(1, 'SizeLimit'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_ext_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'timeout'),(1, 'SizeLimit'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_ext_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'timeout'),(1, 'SizeLimit'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32)(('ldap_search', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_st():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_st', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),UInt32,UInt32,POINTER(UInt32))(('ldap_search_ext', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'TimeLimit'),(1, 'SizeLimit'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_search_ext_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'timeout'),(1, 'SizeLimit'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_check_filterW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR)(('ldap_check_filterW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'SearchFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_check_filterA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR)(('ldap_check_filterA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'SearchFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modifyW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)))(('ldap_modifyW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modifyA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_modifyA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)))(('ldap_modify_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_modify_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_extW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32))(('ldap_modify_extW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_extA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_modify_extA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_modify_ext_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_modify_ext_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_modify', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_modify_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_modify_ext', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_modify_ext_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2W():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32)(('ldap_modrdn2W', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2A():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32)(('ldap_modrdn2A', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdnW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ldap_modrdnW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdnA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_modrdnA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32)(('ldap_modrdn2_sW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32)(('ldap_modrdn2_sA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ldap_modrdn_sW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_modrdn_sA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32)(('ldap_modrdn2', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_modrdn', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32)(('ldap_modrdn2_s', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_modrdn_s', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_extW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32))(('ldap_rename_extW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_extA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_rename_extA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_rename_ext_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_rename_ext_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_rename_ext', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_rename_ext_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_addW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)))(('ldap_addW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_addA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_addA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)))(('ldap_add_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_add_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_extW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32))(('ldap_add_extW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_extA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_add_extA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_add_ext_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_add_ext_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_add', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)))(('ldap_add_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_add_ext', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_add_ext_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compareW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ldap_compareW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compareA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_compareA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ldap_compare_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_compare_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_compare', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_compare_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_extW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32))(('ldap_compare_extW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_extA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_compare_extA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_compare_ext_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_compare_ext_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_compare_ext', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_compare_ext_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_deleteW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR)(('ldap_deleteW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_deleteA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR)(('ldap_deleteA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR)(('ldap_delete_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR)(('ldap_delete_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_extW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32))(('ldap_delete_extW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_extA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_delete_extA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_delete_ext_sW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_delete_ext_sA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR)(('ldap_delete', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR)(('ldap_delete_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_delete_ext', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_delete_ext_s', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_abandon():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),UInt32)(('ldap_abandon', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'msgid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_result():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),UInt32,UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_result', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'msgid'),(1, 'all'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_msgfree():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_msgfree', cdll['WLDAP32.dll']), ((1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_result2error():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),UInt32)(('ldap_result2error', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'res'),(1, 'freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_resultW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(POINTER(UInt16))),POINTER(POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))),win32more.Foundation.BOOLEAN)(('ldap_parse_resultW', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ReturnCode'),(1, 'MatchedDNs'),(1, 'ErrorMessage'),(1, 'Referrals'),(1, 'ServerControls'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_resultA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(UInt32),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(POINTER(SByte))),POINTER(POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))),win32more.Foundation.BOOLEAN)(('ldap_parse_resultA', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ReturnCode'),(1, 'MatchedDNs'),(1, 'ErrorMessage'),(1, 'Referrals'),(1, 'ServerControls'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_extended_resultA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),win32more.Foundation.BOOLEAN)(('ldap_parse_extended_resultA', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ResultOID'),(1, 'ResultData'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_extended_resultW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),win32more.Foundation.BOOLEAN)(('ldap_parse_extended_resultW', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ResultOID'),(1, 'ResultData'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_controls_freeA():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_controls_freeA', cdll['WLDAP32.dll']), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_control_freeA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAPControlA_head))(('ldap_control_freeA', cdll['WLDAP32.dll']), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_controls_freeW():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_controls_freeW', cdll['WLDAP32.dll']), ((1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_control_freeW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAPControlW_head))(('ldap_control_freeW', cdll['WLDAP32.dll']), ((1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_free_controlsW():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_free_controlsW', cdll['WLDAP32.dll']), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_free_controlsA():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_free_controlsA', cdll['WLDAP32.dll']), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_result():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(UInt32),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(win32more.Foundation.PSTR)),POINTER(POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))),win32more.Foundation.BOOLEAN)(('ldap_parse_result', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ReturnCode'),(1, 'MatchedDNs'),(1, 'ErrorMessage'),(1, 'Referrals'),(1, 'ServerControls'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_controls_free():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_controls_free', cdll['WLDAP32.dll']), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_control_free():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAPControlA_head))(('ldap_control_free', cdll['WLDAP32.dll']), ((1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_free_controls():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_free_controls', cdll['WLDAP32.dll']), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_err2stringW():
    try:
        return CFUNCTYPE(win32more.Foundation.PWSTR,UInt32)(('ldap_err2stringW', cdll['WLDAP32.dll']), ((1, 'err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_err2stringA():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,UInt32)(('ldap_err2stringA', cdll['WLDAP32.dll']), ((1, 'err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_err2string():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,UInt32)(('ldap_err2string', cdll['WLDAP32.dll']), ((1, 'err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_perror():
    try:
        return CFUNCTYPE(Void,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR)(('ldap_perror', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_entry():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_first_entry', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_entry():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_next_entry', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_entries():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_count_entries', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_attributeW():
    try:
        return CFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Networking.Ldap.BerElement_head)))(('ldap_first_attributeW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_attributeA():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Networking.Ldap.BerElement_head)))(('ldap_first_attributeA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_attribute():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Networking.Ldap.BerElement_head)))(('ldap_first_attribute', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_attributeW():
    try:
        return CFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.BerElement_head))(('ldap_next_attributeW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_attributeA():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.BerElement_head))(('ldap_next_attributeA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_attribute():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.BerElement_head))(('ldap_next_attribute', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_valuesW():
    try:
        return CFUNCTYPE(POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PWSTR)(('ldap_get_valuesW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_valuesA():
    try:
        return CFUNCTYPE(POINTER(win32more.Foundation.PSTR),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR)(('ldap_get_valuesA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values():
    try:
        return CFUNCTYPE(POINTER(win32more.Foundation.PSTR),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR)(('ldap_get_values', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values_lenW():
    try:
        return CFUNCTYPE(POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PWSTR)(('ldap_get_values_lenW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Message'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values_lenA():
    try:
        return CFUNCTYPE(POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR)(('ldap_get_values_lenA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Message'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values_len():
    try:
        return CFUNCTYPE(POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR)(('ldap_get_values_len', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Message'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_valuesW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Foundation.PWSTR))(('ldap_count_valuesW', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_valuesA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR))(('ldap_count_valuesA', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_values():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR))(('ldap_count_values', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_values_len():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_count_values_len', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_freeW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Foundation.PWSTR))(('ldap_value_freeW', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_freeA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR))(('ldap_value_freeA', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_free():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR))(('ldap_value_free', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_free_len():
    try:
        return CFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_value_free_len', cdll['WLDAP32.dll']), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_dnW():
    try:
        return CFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_get_dnW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_dnA():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_get_dnA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_dn():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_get_dn', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_explode_dnW():
    try:
        return CFUNCTYPE(POINTER(win32more.Foundation.PWSTR),win32more.Foundation.PWSTR,UInt32)(('ldap_explode_dnW', cdll['WLDAP32.dll']), ((1, 'dn'),(1, 'notypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_explode_dnA():
    try:
        return CFUNCTYPE(POINTER(win32more.Foundation.PSTR),win32more.Foundation.PSTR,UInt32)(('ldap_explode_dnA', cdll['WLDAP32.dll']), ((1, 'dn'),(1, 'notypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_explode_dn():
    try:
        return CFUNCTYPE(POINTER(win32more.Foundation.PSTR),win32more.Foundation.PSTR,UInt32)(('ldap_explode_dn', cdll['WLDAP32.dll']), ((1, 'dn'),(1, 'notypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_dn2ufnW():
    try:
        return CFUNCTYPE(win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('ldap_dn2ufnW', cdll['WLDAP32.dll']), ((1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_dn2ufnA():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_dn2ufnA', cdll['WLDAP32.dll']), ((1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_dn2ufn():
    try:
        return CFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('ldap_dn2ufn', cdll['WLDAP32.dll']), ((1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_memfreeW():
    try:
        return CFUNCTYPE(Void,win32more.Foundation.PWSTR)(('ldap_memfreeW', cdll['WLDAP32.dll']), ((1, 'Block'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_memfreeA():
    try:
        return CFUNCTYPE(Void,win32more.Foundation.PSTR)(('ldap_memfreeA', cdll['WLDAP32.dll']), ((1, 'Block'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_bvfree():
    try:
        return CFUNCTYPE(Void,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))(('ber_bvfree', cdll['WLDAP32.dll']), ((1, 'bv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_memfree():
    try:
        return CFUNCTYPE(Void,win32more.Foundation.PSTR)(('ldap_memfree', cdll['WLDAP32.dll']), ((1, 'Block'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_ufn2dnW():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('ldap_ufn2dnW', cdll['WLDAP32.dll']), ((1, 'ufn'),(1, 'pDn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_ufn2dnA():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR))(('ldap_ufn2dnA', cdll['WLDAP32.dll']), ((1, 'ufn'),(1, 'pDn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_ufn2dn():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR))(('ldap_ufn2dn', cdll['WLDAP32.dll']), ((1, 'ufn'),(1, 'pDn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_startup():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_VERSION_INFO_head),POINTER(win32more.Foundation.HANDLE))(('ldap_startup', cdll['WLDAP32.dll']), ((1, 'version'),(1, 'Instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_cleanup():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('ldap_cleanup', cdll['WLDAP32.dll']), ((1, 'hInstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_escape_filter_elementW():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PWSTR,UInt32)(('ldap_escape_filter_elementW', cdll['WLDAP32.dll']), ((1, 'sourceFilterElement'),(1, 'sourceLength'),(1, 'destFilterElement'),(1, 'destLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_escape_filter_elementA():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32)(('ldap_escape_filter_elementA', cdll['WLDAP32.dll']), ((1, 'sourceFilterElement'),(1, 'sourceLength'),(1, 'destFilterElement'),(1, 'destLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_escape_filter_element():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32)(('ldap_escape_filter_element', cdll['WLDAP32.dll']), ((1, 'sourceFilterElement'),(1, 'sourceLength'),(1, 'destFilterElement'),(1, 'destLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_dbg_flags():
    try:
        return CFUNCTYPE(UInt32,UInt32)(('ldap_set_dbg_flags', cdll['WLDAP32.dll']), ((1, 'NewFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_dbg_routine():
    try:
        return CFUNCTYPE(Void,win32more.Networking.Ldap.DBGPRINT)(('ldap_set_dbg_routine', cdll['WLDAP32.dll']), ((1, 'DebugPrintRoutine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapUTF8ToUnicode():
    try:
        return CFUNCTYPE(Int32,win32more.Foundation.PSTR,Int32,win32more.Foundation.PWSTR,Int32)(('LdapUTF8ToUnicode', cdll['WLDAP32.dll']), ((1, 'lpSrcStr'),(1, 'cchSrc'),(1, 'lpDestStr'),(1, 'cchDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapUnicodeToUTF8():
    try:
        return CFUNCTYPE(Int32,win32more.Foundation.PWSTR,Int32,win32more.Foundation.PSTR,Int32)(('LdapUnicodeToUTF8', cdll['WLDAP32.dll']), ((1, 'lpSrcStr'),(1, 'cchSrc'),(1, 'lpDestStr'),(1, 'cchDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_sort_controlA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_create_sort_controlA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_sort_controlW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyW_head)),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_create_sort_controlW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_sort_controlA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32),POINTER(win32more.Foundation.PSTR))(('ldap_parse_sort_controlA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'Result'),(1, 'Attribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_sort_controlW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(('ldap_parse_sort_controlW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'Result'),(1, 'Attribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_sort_control():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_create_sort_control', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_sort_control():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32),POINTER(win32more.Foundation.PSTR))(('ldap_parse_sort_control', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'Result'),(1, 'Attribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_encode_sort_controlW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyW_head)),POINTER(win32more.Networking.Ldap.LDAPControlW_head),win32more.Foundation.BOOLEAN)(('ldap_encode_sort_controlW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'Control'),(1, 'Criticality'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_encode_sort_controlA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)),POINTER(win32more.Networking.Ldap.LDAPControlA_head),win32more.Foundation.BOOLEAN)(('ldap_encode_sort_controlA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'Control'),(1, 'Criticality'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_page_controlW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),UInt32,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_create_page_controlW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'PageSize'),(1, 'Cookie'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_page_controlA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),UInt32,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_create_page_controlA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'PageSize'),(1, 'Cookie'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_page_controlW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_parse_page_controlW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'ServerControls'),(1, 'TotalCount'),(1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_page_controlA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_parse_page_controlA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'ServerControls'),(1, 'TotalCount'),(1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_page_control():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),UInt32,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_create_page_control', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'PageSize'),(1, 'Cookie'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_page_control():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_parse_page_control', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'ServerControls'),(1, 'TotalCount'),(1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_init_pageW():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPSearch_head),POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),UInt32,UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyW_head)))(('ldap_search_init_pageW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'ScopeOfSearch'),(1, 'SearchFilter'),(1, 'AttributeList'),(1, 'AttributesOnly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'PageTimeLimit'),(1, 'TotalSizeLimit'),(1, 'SortKeys'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_init_pageA():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPSearch_head),POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),UInt32,UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)))(('ldap_search_init_pageA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'ScopeOfSearch'),(1, 'SearchFilter'),(1, 'AttributeList'),(1, 'AttributesOnly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'PageTimeLimit'),(1, 'TotalSizeLimit'),(1, 'SortKeys'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_init_page():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPSearch_head),POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),UInt32,UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)))(('ldap_search_init_page', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'ScopeOfSearch'),(1, 'SearchFilter'),(1, 'AttributeList'),(1, 'AttributesOnly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'PageTimeLimit'),(1, 'TotalSizeLimit'),(1, 'SortKeys'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_next_page():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPSearch_head),UInt32,POINTER(UInt32))(('ldap_get_next_page', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SearchHandle'),(1, 'PageSize'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_next_page_s():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPSearch_head),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)))(('ldap_get_next_page_s', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SearchHandle'),(1, 'timeout'),(1, 'PageSize'),(1, 'TotalCount'),(1, 'Results'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_paged_count():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPSearch_head),POINTER(UInt32),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_get_paged_count', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SearchBlock'),(1, 'TotalCount'),(1, 'Results'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_abandon_page():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPSearch_head))(('ldap_search_abandon_page', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'SearchBlock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_vlv_controlW():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPVLVInfo_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_create_vlv_controlW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'VlvInfo'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_vlv_controlA():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPVLVInfo_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_create_vlv_controlA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'VlvInfo'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_vlv_controlW():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(Int32))(('ldap_parse_vlv_controlW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'TargetPos'),(1, 'ListCount'),(1, 'Context'),(1, 'ErrCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_vlv_controlA():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(Int32))(('ldap_parse_vlv_controlA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'TargetPos'),(1, 'ListCount'),(1, 'Context'),(1, 'ErrCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_start_tls_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)))(('ldap_start_tls_sW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'ServerReturnValue'),(1, 'result'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_start_tls_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)))(('ldap_start_tls_sA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'ServerReturnValue'),(1, 'result'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_stop_tls_s():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.LDAP_head))(('ldap_stop_tls_s', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_reference():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_first_reference', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_reference():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_next_reference', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_references():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_count_references', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_referenceW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Foundation.PWSTR)))(('ldap_parse_referenceW', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'Referrals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_referenceA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Foundation.PSTR)))(('ldap_parse_referenceA', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'Referrals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_reference():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Foundation.PSTR)))(('ldap_parse_reference', cdll['WLDAP32.dll']), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'Referrals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operationW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(UInt32))(('ldap_extended_operationW', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operationA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_extended_operationA', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operation_sA():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_extended_operation_sA', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'ReturnedOid'),(1, 'ReturnedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operation_sW():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ldap_extended_operation_sW', cdll['WLDAP32.dll']), ((1, 'ExternalHandle'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'ReturnedOid'),(1, 'ReturnedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operation():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)),POINTER(UInt32))(('ldap_extended_operation', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_close_extended_op():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),UInt32)(('ldap_close_extended_op', cdll['WLDAP32.dll']), ((1, 'ld'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapGetLastError():
    try:
        return CFUNCTYPE(UInt32,)(('LdapGetLastError', cdll['WLDAP32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapMapErrorToWin32():
    try:
        return CFUNCTYPE(win32more.Foundation.WIN32_ERROR,win32more.Networking.Ldap.LDAP_RETCODE)(('LdapMapErrorToWin32', cdll['WLDAP32.dll']), ((1, 'LdapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_conn_from_msg():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head))(('ldap_conn_from_msg', cdll['WLDAP32.dll']), ((1, 'PrimaryConn'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_init():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.BerElement_head),POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))(('ber_init', cdll['WLDAP32.dll']), ((1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_free():
    try:
        return CFUNCTYPE(Void,POINTER(win32more.Networking.Ldap.BerElement_head),Int32)(('ber_free', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'fbuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_bvecfree():
    try:
        return CFUNCTYPE(Void,POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ber_bvecfree', cdll['WLDAP32.dll']), ((1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_bvdup():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))(('ber_bvdup', cdll['WLDAP32.dll']), ((1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_alloc_t():
    try:
        return CFUNCTYPE(POINTER(win32more.Networking.Ldap.BerElement_head),Int32)(('ber_alloc_t', cdll['WLDAP32.dll']), ((1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_skip_tag():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.BerElement_head),POINTER(UInt32))(('ber_skip_tag', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'pLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_peek_tag():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.BerElement_head),POINTER(UInt32))(('ber_peek_tag', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'pLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_first_element():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.BerElement_head),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.CHAR)))(('ber_first_element', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'pLen'),(1, 'ppOpaque'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_next_element():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.BerElement_head),POINTER(UInt32),win32more.Foundation.PSTR)(('ber_next_element', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'pLen'),(1, 'opaque'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_flatten():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.BerElement_head),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)))(('ber_flatten', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_printf():
    try:
        return CFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.BerElement_head),win32more.Foundation.PSTR)(('ber_printf', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'fmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_scanf():
    try:
        return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.BerElement_head),win32more.Foundation.PSTR)(('ber_scanf', cdll['WLDAP32.dll']), ((1, 'pBerElement'),(1, 'fmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BerElement_head():
    class BerElement(Structure):
        pass
    return BerElement
def _define_BerElement():
    BerElement = win32more.Networking.Ldap.BerElement_head
    BerElement._fields_ = [
        ('opaque', win32more.Foundation.PSTR),
    ]
    return BerElement
def _define_DBGPRINT():
    return CFUNCTYPE(UInt32,win32more.Foundation.PSTR)
def _define_DEREFERENCECONNECTION():
    return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAP_head))
def _define_LDAP_head():
    class LDAP(Structure):
        pass
    return LDAP
def _define_LDAP():
    LDAP = win32more.Networking.Ldap.LDAP_head
    class LDAP__ld_sb_e__Struct(Structure):
        pass
    LDAP__ld_sb_e__Struct._fields_ = [
        ('sb_sd', UIntPtr),
        ('Reserved1', Byte * 41),
        ('sb_naddr', UIntPtr),
        ('Reserved2', Byte * 24),
    ]
    LDAP._fields_ = [
        ('ld_sb', LDAP__ld_sb_e__Struct),
        ('ld_host', win32more.Foundation.PSTR),
        ('ld_version', UInt32),
        ('ld_lberoptions', Byte),
        ('ld_deref', UInt32),
        ('ld_timelimit', UInt32),
        ('ld_sizelimit', UInt32),
        ('ld_errno', UInt32),
        ('ld_matched', win32more.Foundation.PSTR),
        ('ld_error', win32more.Foundation.PSTR),
        ('ld_msgid', UInt32),
        ('Reserved3', Byte * 25),
        ('ld_cldaptries', UInt32),
        ('ld_cldaptimeout', UInt32),
        ('ld_refhoplimit', UInt32),
        ('ld_options', UInt32),
    ]
    return LDAP
def _define_LDAP_BERVAL_head():
    class LDAP_BERVAL(Structure):
        pass
    return LDAP_BERVAL
def _define_LDAP_BERVAL():
    LDAP_BERVAL = win32more.Networking.Ldap.LDAP_BERVAL_head
    LDAP_BERVAL._fields_ = [
        ('bv_len', UInt32),
        ('bv_val', win32more.Foundation.PSTR),
    ]
    return LDAP_BERVAL
def _define_LDAP_REFERRAL_CALLBACK_head():
    class LDAP_REFERRAL_CALLBACK(Structure):
        pass
    return LDAP_REFERRAL_CALLBACK
def _define_LDAP_REFERRAL_CALLBACK():
    LDAP_REFERRAL_CALLBACK = win32more.Networking.Ldap.LDAP_REFERRAL_CALLBACK_head
    LDAP_REFERRAL_CALLBACK._fields_ = [
        ('SizeOfCallbacks', UInt32),
        ('QueryForConnection', win32more.Networking.Ldap.QUERYFORCONNECTION),
        ('NotifyRoutine', win32more.Networking.Ldap.NOTIFYOFNEWCONNECTION),
        ('DereferenceRoutine', win32more.Networking.Ldap.DEREFERENCECONNECTION),
    ]
    return LDAP_REFERRAL_CALLBACK
LDAP_RETCODE = Int32
LDAP_SUCCESS = 0
LDAP_OPERATIONS_ERROR = 1
LDAP_PROTOCOL_ERROR = 2
LDAP_TIMELIMIT_EXCEEDED = 3
LDAP_SIZELIMIT_EXCEEDED = 4
LDAP_COMPARE_FALSE = 5
LDAP_COMPARE_TRUE = 6
LDAP_AUTH_METHOD_NOT_SUPPORTED = 7
LDAP_STRONG_AUTH_REQUIRED = 8
LDAP_REFERRAL_V2 = 9
LDAP_PARTIAL_RESULTS = 9
LDAP_REFERRAL = 10
LDAP_ADMIN_LIMIT_EXCEEDED = 11
LDAP_UNAVAILABLE_CRIT_EXTENSION = 12
LDAP_CONFIDENTIALITY_REQUIRED = 13
LDAP_SASL_BIND_IN_PROGRESS = 14
LDAP_NO_SUCH_ATTRIBUTE = 16
LDAP_UNDEFINED_TYPE = 17
LDAP_INAPPROPRIATE_MATCHING = 18
LDAP_CONSTRAINT_VIOLATION = 19
LDAP_ATTRIBUTE_OR_VALUE_EXISTS = 20
LDAP_INVALID_SYNTAX = 21
LDAP_NO_SUCH_OBJECT = 32
LDAP_ALIAS_PROBLEM = 33
LDAP_INVALID_DN_SYNTAX = 34
LDAP_IS_LEAF = 35
LDAP_ALIAS_DEREF_PROBLEM = 36
LDAP_INAPPROPRIATE_AUTH = 48
LDAP_INVALID_CREDENTIALS = 49
LDAP_INSUFFICIENT_RIGHTS = 50
LDAP_BUSY = 51
LDAP_UNAVAILABLE = 52
LDAP_UNWILLING_TO_PERFORM = 53
LDAP_LOOP_DETECT = 54
LDAP_SORT_CONTROL_MISSING = 60
LDAP_OFFSET_RANGE_ERROR = 61
LDAP_NAMING_VIOLATION = 64
LDAP_OBJECT_CLASS_VIOLATION = 65
LDAP_NOT_ALLOWED_ON_NONLEAF = 66
LDAP_NOT_ALLOWED_ON_RDN = 67
LDAP_ALREADY_EXISTS = 68
LDAP_NO_OBJECT_CLASS_MODS = 69
LDAP_RESULTS_TOO_LARGE = 70
LDAP_AFFECTS_MULTIPLE_DSAS = 71
LDAP_VIRTUAL_LIST_VIEW_ERROR = 76
LDAP_OTHER = 80
LDAP_SERVER_DOWN = 81
LDAP_LOCAL_ERROR = 82
LDAP_ENCODING_ERROR = 83
LDAP_DECODING_ERROR = 84
LDAP_TIMEOUT = 85
LDAP_AUTH_UNKNOWN = 86
LDAP_FILTER_ERROR = 87
LDAP_USER_CANCELLED = 88
LDAP_PARAM_ERROR = 89
LDAP_NO_MEMORY = 90
LDAP_CONNECT_ERROR = 91
LDAP_NOT_SUPPORTED = 92
LDAP_NO_RESULTS_RETURNED = 94
LDAP_CONTROL_NOT_FOUND = 93
LDAP_MORE_RESULTS_TO_RETURN = 95
LDAP_CLIENT_LOOP = 96
LDAP_REFERRAL_LIMIT_EXCEEDED = 97
def _define_LDAP_TIMEVAL_head():
    class LDAP_TIMEVAL(Structure):
        pass
    return LDAP_TIMEVAL
def _define_LDAP_TIMEVAL():
    LDAP_TIMEVAL = win32more.Networking.Ldap.LDAP_TIMEVAL_head
    LDAP_TIMEVAL._fields_ = [
        ('tv_sec', Int32),
        ('tv_usec', Int32),
    ]
    return LDAP_TIMEVAL
def _define_LDAP_VERSION_INFO_head():
    class LDAP_VERSION_INFO(Structure):
        pass
    return LDAP_VERSION_INFO
def _define_LDAP_VERSION_INFO():
    LDAP_VERSION_INFO = win32more.Networking.Ldap.LDAP_VERSION_INFO_head
    LDAP_VERSION_INFO._fields_ = [
        ('lv_size', UInt32),
        ('lv_major', UInt32),
        ('lv_minor', UInt32),
    ]
    return LDAP_VERSION_INFO
def _define_LDAPAPIFeatureInfoA_head():
    class LDAPAPIFeatureInfoA(Structure):
        pass
    return LDAPAPIFeatureInfoA
def _define_LDAPAPIFeatureInfoA():
    LDAPAPIFeatureInfoA = win32more.Networking.Ldap.LDAPAPIFeatureInfoA_head
    LDAPAPIFeatureInfoA._fields_ = [
        ('ldapaif_info_version', Int32),
        ('ldapaif_name', win32more.Foundation.PSTR),
        ('ldapaif_version', Int32),
    ]
    return LDAPAPIFeatureInfoA
def _define_LDAPAPIFeatureInfoW_head():
    class LDAPAPIFeatureInfoW(Structure):
        pass
    return LDAPAPIFeatureInfoW
def _define_LDAPAPIFeatureInfoW():
    LDAPAPIFeatureInfoW = win32more.Networking.Ldap.LDAPAPIFeatureInfoW_head
    LDAPAPIFeatureInfoW._fields_ = [
        ('ldapaif_info_version', Int32),
        ('ldapaif_name', win32more.Foundation.PWSTR),
        ('ldapaif_version', Int32),
    ]
    return LDAPAPIFeatureInfoW
def _define_LDAPAPIInfoA_head():
    class LDAPAPIInfoA(Structure):
        pass
    return LDAPAPIInfoA
def _define_LDAPAPIInfoA():
    LDAPAPIInfoA = win32more.Networking.Ldap.LDAPAPIInfoA_head
    LDAPAPIInfoA._fields_ = [
        ('ldapai_info_version', Int32),
        ('ldapai_api_version', Int32),
        ('ldapai_protocol_version', Int32),
        ('ldapai_extensions', POINTER(POINTER(SByte))),
        ('ldapai_vendor_name', win32more.Foundation.PSTR),
        ('ldapai_vendor_version', Int32),
    ]
    return LDAPAPIInfoA
def _define_LDAPAPIInfoW_head():
    class LDAPAPIInfoW(Structure):
        pass
    return LDAPAPIInfoW
def _define_LDAPAPIInfoW():
    LDAPAPIInfoW = win32more.Networking.Ldap.LDAPAPIInfoW_head
    LDAPAPIInfoW._fields_ = [
        ('ldapai_info_version', Int32),
        ('ldapai_api_version', Int32),
        ('ldapai_protocol_version', Int32),
        ('ldapai_extensions', POINTER(win32more.Foundation.PWSTR)),
        ('ldapai_vendor_name', win32more.Foundation.PWSTR),
        ('ldapai_vendor_version', Int32),
    ]
    return LDAPAPIInfoW
def _define_LDAPControlA_head():
    class LDAPControlA(Structure):
        pass
    return LDAPControlA
def _define_LDAPControlA():
    LDAPControlA = win32more.Networking.Ldap.LDAPControlA_head
    LDAPControlA._fields_ = [
        ('ldctl_oid', win32more.Foundation.PSTR),
        ('ldctl_value', win32more.Networking.Ldap.LDAP_BERVAL),
        ('ldctl_iscritical', win32more.Foundation.BOOLEAN),
    ]
    return LDAPControlA
def _define_LDAPControlW_head():
    class LDAPControlW(Structure):
        pass
    return LDAPControlW
def _define_LDAPControlW():
    LDAPControlW = win32more.Networking.Ldap.LDAPControlW_head
    LDAPControlW._fields_ = [
        ('ldctl_oid', win32more.Foundation.PWSTR),
        ('ldctl_value', win32more.Networking.Ldap.LDAP_BERVAL),
        ('ldctl_iscritical', win32more.Foundation.BOOLEAN),
    ]
    return LDAPControlW
def _define_LDAPMessage_head():
    class LDAPMessage(Structure):
        pass
    return LDAPMessage
def _define_LDAPMessage():
    LDAPMessage = win32more.Networking.Ldap.LDAPMessage_head
    LDAPMessage._fields_ = [
        ('lm_msgid', UInt32),
        ('lm_msgtype', UInt32),
        ('lm_ber', c_void_p),
        ('lm_chain', POINTER(win32more.Networking.Ldap.LDAPMessage_head)),
        ('lm_next', POINTER(win32more.Networking.Ldap.LDAPMessage_head)),
        ('lm_time', UInt32),
        ('Connection', POINTER(win32more.Networking.Ldap.LDAP_head)),
        ('Request', c_void_p),
        ('lm_returncode', UInt32),
        ('lm_referral', UInt16),
        ('lm_chased', win32more.Foundation.BOOLEAN),
        ('lm_eom', win32more.Foundation.BOOLEAN),
        ('ConnectionReferenced', win32more.Foundation.BOOLEAN),
    ]
    return LDAPMessage
def _define_LDAPModA_head():
    class LDAPModA(Structure):
        pass
    return LDAPModA
def _define_LDAPModA():
    LDAPModA = win32more.Networking.Ldap.LDAPModA_head
    class LDAPModA__mod_vals_e__Union(Union):
        pass
    LDAPModA__mod_vals_e__Union._fields_ = [
        ('modv_strvals', POINTER(win32more.Foundation.PSTR)),
        ('modv_bvals', POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))),
    ]
    LDAPModA._fields_ = [
        ('mod_op', UInt32),
        ('mod_type', win32more.Foundation.PSTR),
        ('mod_vals', LDAPModA__mod_vals_e__Union),
    ]
    return LDAPModA
def _define_LDAPModW_head():
    class LDAPModW(Structure):
        pass
    return LDAPModW
def _define_LDAPModW():
    LDAPModW = win32more.Networking.Ldap.LDAPModW_head
    class LDAPModW__mod_vals_e__Union(Union):
        pass
    LDAPModW__mod_vals_e__Union._fields_ = [
        ('modv_strvals', POINTER(win32more.Foundation.PWSTR)),
        ('modv_bvals', POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))),
    ]
    LDAPModW._fields_ = [
        ('mod_op', UInt32),
        ('mod_type', win32more.Foundation.PWSTR),
        ('mod_vals', LDAPModW__mod_vals_e__Union),
    ]
    return LDAPModW
def _define_LDAPSearch_head():
    class LDAPSearch(Structure):
        pass
    return LDAPSearch
def _define_LDAPSearch():
    LDAPSearch = win32more.Networking.Ldap.LDAPSearch_head
    return LDAPSearch
def _define_LDAPSortKeyA_head():
    class LDAPSortKeyA(Structure):
        pass
    return LDAPSortKeyA
def _define_LDAPSortKeyA():
    LDAPSortKeyA = win32more.Networking.Ldap.LDAPSortKeyA_head
    LDAPSortKeyA._fields_ = [
        ('sk_attrtype', win32more.Foundation.PSTR),
        ('sk_matchruleoid', win32more.Foundation.PSTR),
        ('sk_reverseorder', win32more.Foundation.BOOLEAN),
    ]
    return LDAPSortKeyA
def _define_LDAPSortKeyW_head():
    class LDAPSortKeyW(Structure):
        pass
    return LDAPSortKeyW
def _define_LDAPSortKeyW():
    LDAPSortKeyW = win32more.Networking.Ldap.LDAPSortKeyW_head
    LDAPSortKeyW._fields_ = [
        ('sk_attrtype', win32more.Foundation.PWSTR),
        ('sk_matchruleoid', win32more.Foundation.PWSTR),
        ('sk_reverseorder', win32more.Foundation.BOOLEAN),
    ]
    return LDAPSortKeyW
def _define_LDAPVLVInfo_head():
    class LDAPVLVInfo(Structure):
        pass
    return LDAPVLVInfo
def _define_LDAPVLVInfo():
    LDAPVLVInfo = win32more.Networking.Ldap.LDAPVLVInfo_head
    LDAPVLVInfo._fields_ = [
        ('ldvlv_version', Int32),
        ('ldvlv_before_count', UInt32),
        ('ldvlv_after_count', UInt32),
        ('ldvlv_offset', UInt32),
        ('ldvlv_count', UInt32),
        ('ldvlv_attrvalue', POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),
        ('ldvlv_context', POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),
        ('ldvlv_extradata', c_void_p),
    ]
    return LDAPVLVInfo
def _define_NOTIFYOFNEWCONNECTION():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_head),UInt32,c_void_p,c_void_p,UInt32)
def _define_QUERYCLIENTCERT():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head),POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)))
def _define_QUERYFORCONNECTION():
    return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(win32more.Networking.Ldap.LDAP_head),win32more.Foundation.PWSTR,win32more.Foundation.PSTR,UInt32,c_void_p,c_void_p,POINTER(POINTER(win32more.Networking.Ldap.LDAP_head)))
def _define_VERIFYSERVERCERT():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.LDAP_head),POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)))
__all__ = [
    "BerElement",
    "DBGPRINT",
    "DEREFERENCECONNECTION",
    "LAPI_MAJOR_VER1",
    "LAPI_MINOR_VER1",
    "LBER_DEFAULT",
    "LBER_ERROR",
    "LBER_TRANSLATE_STRINGS",
    "LBER_USE_DER",
    "LBER_USE_INDEFINITE_LEN",
    "LDAP",
    "LDAPAPIFeatureInfoA",
    "LDAPAPIFeatureInfoW",
    "LDAPAPIInfoA",
    "LDAPAPIInfoW",
    "LDAPControlA",
    "LDAPControlW",
    "LDAPMessage",
    "LDAPModA",
    "LDAPModW",
    "LDAPSearch",
    "LDAPSortKeyA",
    "LDAPSortKeyW",
    "LDAPVLVInfo",
    "LDAP_ABANDON_CMD",
    "LDAP_ADD_CMD",
    "LDAP_ADMIN_LIMIT_EXCEEDED",
    "LDAP_AFFECTS_MULTIPLE_DSAS",
    "LDAP_ALIAS_DEREF_PROBLEM",
    "LDAP_ALIAS_PROBLEM",
    "LDAP_ALREADY_EXISTS",
    "LDAP_API_FEATURE_VIRTUAL_LIST_VIEW",
    "LDAP_API_INFO_VERSION",
    "LDAP_API_VERSION",
    "LDAP_ATTRIBUTE_OR_VALUE_EXISTS",
    "LDAP_AUTH_METHOD_NOT_SUPPORTED",
    "LDAP_AUTH_OTHERKIND",
    "LDAP_AUTH_SASL",
    "LDAP_AUTH_SIMPLE",
    "LDAP_AUTH_UNKNOWN",
    "LDAP_BERVAL",
    "LDAP_BIND_CMD",
    "LDAP_BUSY",
    "LDAP_CAP_ACTIVE_DIRECTORY_ADAM_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_ADAM_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_PARTIAL_SECRETS_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_PARTIAL_SECRETS_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_V51_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_V51_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_V60_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_V60_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_V61_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_V61_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_V61_R2_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_V61_R2_OID_W",
    "LDAP_CAP_ACTIVE_DIRECTORY_W8_OID",
    "LDAP_CAP_ACTIVE_DIRECTORY_W8_OID_W",
    "LDAP_CHASE_EXTERNAL_REFERRALS",
    "LDAP_CHASE_SUBORDINATE_REFERRALS",
    "LDAP_CLIENT_LOOP",
    "LDAP_COMPARE_CMD",
    "LDAP_COMPARE_FALSE",
    "LDAP_COMPARE_TRUE",
    "LDAP_CONFIDENTIALITY_REQUIRED",
    "LDAP_CONNECT_ERROR",
    "LDAP_CONSTRAINT_VIOLATION",
    "LDAP_CONTROL_NOT_FOUND",
    "LDAP_CONTROL_REFERRALS",
    "LDAP_CONTROL_REFERRALS_W",
    "LDAP_CONTROL_VLVREQUEST",
    "LDAP_CONTROL_VLVREQUEST_W",
    "LDAP_CONTROL_VLVRESPONSE",
    "LDAP_CONTROL_VLVRESPONSE_W",
    "LDAP_DECODING_ERROR",
    "LDAP_DELETE_CMD",
    "LDAP_DEREF_ALWAYS",
    "LDAP_DEREF_FINDING",
    "LDAP_DEREF_NEVER",
    "LDAP_DEREF_SEARCHING",
    "LDAP_DIRSYNC_ANCESTORS_FIRST_ORDER",
    "LDAP_DIRSYNC_INCREMENTAL_VALUES",
    "LDAP_DIRSYNC_OBJECT_SECURITY",
    "LDAP_DIRSYNC_PUBLIC_DATA_ONLY",
    "LDAP_DIRSYNC_ROPAS_DATA_ONLY",
    "LDAP_ENCODING_ERROR",
    "LDAP_EXTENDED_CMD",
    "LDAP_FEATURE_INFO_VERSION",
    "LDAP_FILTER_AND",
    "LDAP_FILTER_APPROX",
    "LDAP_FILTER_EQUALITY",
    "LDAP_FILTER_ERROR",
    "LDAP_FILTER_EXTENSIBLE",
    "LDAP_FILTER_GE",
    "LDAP_FILTER_LE",
    "LDAP_FILTER_NOT",
    "LDAP_FILTER_OR",
    "LDAP_FILTER_PRESENT",
    "LDAP_FILTER_SUBSTRINGS",
    "LDAP_GC_PORT",
    "LDAP_INAPPROPRIATE_AUTH",
    "LDAP_INAPPROPRIATE_MATCHING",
    "LDAP_INSUFFICIENT_RIGHTS",
    "LDAP_INVALID_CMD",
    "LDAP_INVALID_CREDENTIALS",
    "LDAP_INVALID_DN_SYNTAX",
    "LDAP_INVALID_RES",
    "LDAP_INVALID_SYNTAX",
    "LDAP_IS_LEAF",
    "LDAP_LOCAL_ERROR",
    "LDAP_LOOP_DETECT",
    "LDAP_MATCHING_RULE_BIT_AND",
    "LDAP_MATCHING_RULE_BIT_AND_W",
    "LDAP_MATCHING_RULE_BIT_OR",
    "LDAP_MATCHING_RULE_BIT_OR_W",
    "LDAP_MATCHING_RULE_DN_BINARY_COMPLEX",
    "LDAP_MATCHING_RULE_DN_BINARY_COMPLEX_W",
    "LDAP_MATCHING_RULE_TRANSITIVE_EVALUATION",
    "LDAP_MATCHING_RULE_TRANSITIVE_EVALUATION_W",
    "LDAP_MODIFY_CMD",
    "LDAP_MODRDN_CMD",
    "LDAP_MOD_ADD",
    "LDAP_MOD_BVALUES",
    "LDAP_MOD_DELETE",
    "LDAP_MOD_REPLACE",
    "LDAP_MORE_RESULTS_TO_RETURN",
    "LDAP_MSG_ALL",
    "LDAP_MSG_ONE",
    "LDAP_MSG_RECEIVED",
    "LDAP_NAMING_VIOLATION",
    "LDAP_NOT_ALLOWED_ON_NONLEAF",
    "LDAP_NOT_ALLOWED_ON_RDN",
    "LDAP_NOT_SUPPORTED",
    "LDAP_NO_LIMIT",
    "LDAP_NO_MEMORY",
    "LDAP_NO_OBJECT_CLASS_MODS",
    "LDAP_NO_RESULTS_RETURNED",
    "LDAP_NO_SUCH_ATTRIBUTE",
    "LDAP_NO_SUCH_OBJECT",
    "LDAP_OBJECT_CLASS_VIOLATION",
    "LDAP_OFFSET_RANGE_ERROR",
    "LDAP_OPATT_ABANDON_REPL",
    "LDAP_OPATT_ABANDON_REPL_W",
    "LDAP_OPATT_BECOME_DOM_MASTER",
    "LDAP_OPATT_BECOME_DOM_MASTER_W",
    "LDAP_OPATT_BECOME_PDC",
    "LDAP_OPATT_BECOME_PDC_W",
    "LDAP_OPATT_BECOME_RID_MASTER",
    "LDAP_OPATT_BECOME_RID_MASTER_W",
    "LDAP_OPATT_BECOME_SCHEMA_MASTER",
    "LDAP_OPATT_BECOME_SCHEMA_MASTER_W",
    "LDAP_OPATT_CONFIG_NAMING_CONTEXT",
    "LDAP_OPATT_CONFIG_NAMING_CONTEXT_W",
    "LDAP_OPATT_CURRENT_TIME",
    "LDAP_OPATT_CURRENT_TIME_W",
    "LDAP_OPATT_DEFAULT_NAMING_CONTEXT",
    "LDAP_OPATT_DEFAULT_NAMING_CONTEXT_W",
    "LDAP_OPATT_DNS_HOST_NAME",
    "LDAP_OPATT_DNS_HOST_NAME_W",
    "LDAP_OPATT_DO_GARBAGE_COLLECTION",
    "LDAP_OPATT_DO_GARBAGE_COLLECTION_W",
    "LDAP_OPATT_DS_SERVICE_NAME",
    "LDAP_OPATT_DS_SERVICE_NAME_W",
    "LDAP_OPATT_FIXUP_INHERITANCE",
    "LDAP_OPATT_FIXUP_INHERITANCE_W",
    "LDAP_OPATT_HIGHEST_COMMITTED_USN",
    "LDAP_OPATT_HIGHEST_COMMITTED_USN_W",
    "LDAP_OPATT_INVALIDATE_RID_POOL",
    "LDAP_OPATT_INVALIDATE_RID_POOL_W",
    "LDAP_OPATT_LDAP_SERVICE_NAME",
    "LDAP_OPATT_LDAP_SERVICE_NAME_W",
    "LDAP_OPATT_NAMING_CONTEXTS",
    "LDAP_OPATT_NAMING_CONTEXTS_W",
    "LDAP_OPATT_RECALC_HIERARCHY",
    "LDAP_OPATT_RECALC_HIERARCHY_W",
    "LDAP_OPATT_ROOT_DOMAIN_NAMING_CONTEXT",
    "LDAP_OPATT_ROOT_DOMAIN_NAMING_CONTEXT_W",
    "LDAP_OPATT_SCHEMA_NAMING_CONTEXT",
    "LDAP_OPATT_SCHEMA_NAMING_CONTEXT_W",
    "LDAP_OPATT_SCHEMA_UPDATE_NOW",
    "LDAP_OPATT_SCHEMA_UPDATE_NOW_W",
    "LDAP_OPATT_SERVER_NAME",
    "LDAP_OPATT_SERVER_NAME_W",
    "LDAP_OPATT_SUBSCHEMA_SUBENTRY",
    "LDAP_OPATT_SUBSCHEMA_SUBENTRY_W",
    "LDAP_OPATT_SUPPORTED_CAPABILITIES",
    "LDAP_OPATT_SUPPORTED_CAPABILITIES_W",
    "LDAP_OPATT_SUPPORTED_CONTROL",
    "LDAP_OPATT_SUPPORTED_CONTROL_W",
    "LDAP_OPATT_SUPPORTED_LDAP_POLICIES",
    "LDAP_OPATT_SUPPORTED_LDAP_POLICIES_W",
    "LDAP_OPATT_SUPPORTED_LDAP_VERSION",
    "LDAP_OPATT_SUPPORTED_LDAP_VERSION_W",
    "LDAP_OPATT_SUPPORTED_SASL_MECHANISM",
    "LDAP_OPATT_SUPPORTED_SASL_MECHANISM_W",
    "LDAP_OPERATIONS_ERROR",
    "LDAP_OPT_API_FEATURE_INFO",
    "LDAP_OPT_API_INFO",
    "LDAP_OPT_AREC_EXCLUSIVE",
    "LDAP_OPT_AUTO_RECONNECT",
    "LDAP_OPT_CACHE_ENABLE",
    "LDAP_OPT_CACHE_FN_PTRS",
    "LDAP_OPT_CACHE_STRATEGY",
    "LDAP_OPT_CHASE_REFERRALS",
    "LDAP_OPT_CLIENT_CERTIFICATE",
    "LDAP_OPT_DEREF",
    "LDAP_OPT_DESC",
    "LDAP_OPT_DNS",
    "LDAP_OPT_DNSDOMAIN_NAME",
    "LDAP_OPT_ENCRYPT",
    "LDAP_OPT_ERROR_NUMBER",
    "LDAP_OPT_ERROR_STRING",
    "LDAP_OPT_FAST_CONCURRENT_BIND",
    "LDAP_OPT_GETDSNAME_FLAGS",
    "LDAP_OPT_HOST_NAME",
    "LDAP_OPT_HOST_REACHABLE",
    "LDAP_OPT_IO_FN_PTRS",
    "LDAP_OPT_PING_KEEP_ALIVE",
    "LDAP_OPT_PING_LIMIT",
    "LDAP_OPT_PING_WAIT_TIME",
    "LDAP_OPT_PROMPT_CREDENTIALS",
    "LDAP_OPT_PROTOCOL_VERSION",
    "LDAP_OPT_REBIND_ARG",
    "LDAP_OPT_REBIND_FN",
    "LDAP_OPT_REFERRALS",
    "LDAP_OPT_REFERRAL_CALLBACK",
    "LDAP_OPT_REFERRAL_HOP_LIMIT",
    "LDAP_OPT_REF_DEREF_CONN_PER_MSG",
    "LDAP_OPT_RESTART",
    "LDAP_OPT_RETURN_REFS",
    "LDAP_OPT_ROOTDSE_CACHE",
    "LDAP_OPT_SASL_METHOD",
    "LDAP_OPT_SCH_FLAGS",
    "LDAP_OPT_SECURITY_CONTEXT",
    "LDAP_OPT_SEND_TIMEOUT",
    "LDAP_OPT_SERVER_CERTIFICATE",
    "LDAP_OPT_SERVER_ERROR",
    "LDAP_OPT_SERVER_EXT_ERROR",
    "LDAP_OPT_SIGN",
    "LDAP_OPT_SIZELIMIT",
    "LDAP_OPT_SOCKET_BIND_ADDRESSES",
    "LDAP_OPT_SSL",
    "LDAP_OPT_SSL_INFO",
    "LDAP_OPT_SSPI_FLAGS",
    "LDAP_OPT_TCP_KEEPALIVE",
    "LDAP_OPT_THREAD_FN_PTRS",
    "LDAP_OPT_TIMELIMIT",
    "LDAP_OPT_TLS",
    "LDAP_OPT_TLS_INFO",
    "LDAP_OPT_VERSION",
    "LDAP_OTHER",
    "LDAP_PAGED_RESULT_OID_STRING",
    "LDAP_PAGED_RESULT_OID_STRING_W",
    "LDAP_PARAM_ERROR",
    "LDAP_PARTIAL_RESULTS",
    "LDAP_POLICYHINT_APPLY_FULLPWDPOLICY",
    "LDAP_PORT",
    "LDAP_PROTOCOL_ERROR",
    "LDAP_REFERRAL",
    "LDAP_REFERRAL_CALLBACK",
    "LDAP_REFERRAL_LIMIT_EXCEEDED",
    "LDAP_REFERRAL_V2",
    "LDAP_RESULTS_TOO_LARGE",
    "LDAP_RES_ADD",
    "LDAP_RES_ANY",
    "LDAP_RES_BIND",
    "LDAP_RES_COMPARE",
    "LDAP_RES_DELETE",
    "LDAP_RES_EXTENDED",
    "LDAP_RES_MODIFY",
    "LDAP_RES_MODRDN",
    "LDAP_RES_REFERRAL",
    "LDAP_RES_SEARCH_ENTRY",
    "LDAP_RES_SEARCH_RESULT",
    "LDAP_RES_SESSION",
    "LDAP_RETCODE",
    "LDAP_SASL_BIND_IN_PROGRESS",
    "LDAP_SCOPE_BASE",
    "LDAP_SCOPE_ONELEVEL",
    "LDAP_SCOPE_SUBTREE",
    "LDAP_SEARCH_CMD",
    "LDAP_SEARCH_HINT_INDEX_ONLY_OID",
    "LDAP_SEARCH_HINT_INDEX_ONLY_OID_W",
    "LDAP_SEARCH_HINT_REQUIRED_INDEX_OID",
    "LDAP_SEARCH_HINT_REQUIRED_INDEX_OID_W",
    "LDAP_SEARCH_HINT_SOFT_SIZE_LIMIT_OID",
    "LDAP_SEARCH_HINT_SOFT_SIZE_LIMIT_OID_W",
    "LDAP_SERVER_ASQ_OID",
    "LDAP_SERVER_ASQ_OID_W",
    "LDAP_SERVER_BATCH_REQUEST_OID",
    "LDAP_SERVER_BATCH_REQUEST_OID_W",
    "LDAP_SERVER_BYPASS_QUOTA_OID",
    "LDAP_SERVER_BYPASS_QUOTA_OID_W",
    "LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID",
    "LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID_W",
    "LDAP_SERVER_DIRSYNC_EX_OID",
    "LDAP_SERVER_DIRSYNC_EX_OID_W",
    "LDAP_SERVER_DIRSYNC_OID",
    "LDAP_SERVER_DIRSYNC_OID_W",
    "LDAP_SERVER_DN_INPUT_OID",
    "LDAP_SERVER_DN_INPUT_OID_W",
    "LDAP_SERVER_DOMAIN_SCOPE_OID",
    "LDAP_SERVER_DOMAIN_SCOPE_OID_W",
    "LDAP_SERVER_DOWN",
    "LDAP_SERVER_EXPECTED_ENTRY_COUNT_OID",
    "LDAP_SERVER_EXPECTED_ENTRY_COUNT_OID_W",
    "LDAP_SERVER_EXTENDED_DN_OID",
    "LDAP_SERVER_EXTENDED_DN_OID_W",
    "LDAP_SERVER_FAST_BIND_OID",
    "LDAP_SERVER_FAST_BIND_OID_W",
    "LDAP_SERVER_FORCE_UPDATE_OID",
    "LDAP_SERVER_FORCE_UPDATE_OID_W",
    "LDAP_SERVER_GET_STATS_OID",
    "LDAP_SERVER_GET_STATS_OID_W",
    "LDAP_SERVER_LAZY_COMMIT_OID",
    "LDAP_SERVER_LAZY_COMMIT_OID_W",
    "LDAP_SERVER_LINK_TTL_OID",
    "LDAP_SERVER_LINK_TTL_OID_W",
    "LDAP_SERVER_NOTIFICATION_OID",
    "LDAP_SERVER_NOTIFICATION_OID_W",
    "LDAP_SERVER_PERMISSIVE_MODIFY_OID",
    "LDAP_SERVER_PERMISSIVE_MODIFY_OID_W",
    "LDAP_SERVER_POLICY_HINTS_DEPRECATED_OID",
    "LDAP_SERVER_POLICY_HINTS_DEPRECATED_OID_W",
    "LDAP_SERVER_POLICY_HINTS_OID",
    "LDAP_SERVER_POLICY_HINTS_OID_W",
    "LDAP_SERVER_QUOTA_CONTROL_OID",
    "LDAP_SERVER_QUOTA_CONTROL_OID_W",
    "LDAP_SERVER_RANGE_OPTION_OID",
    "LDAP_SERVER_RANGE_OPTION_OID_W",
    "LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID",
    "LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID_W",
    "LDAP_SERVER_RESP_SORT_OID",
    "LDAP_SERVER_RESP_SORT_OID_W",
    "LDAP_SERVER_SD_FLAGS_OID",
    "LDAP_SERVER_SD_FLAGS_OID_W",
    "LDAP_SERVER_SEARCH_HINTS_OID",
    "LDAP_SERVER_SEARCH_HINTS_OID_W",
    "LDAP_SERVER_SEARCH_OPTIONS_OID",
    "LDAP_SERVER_SEARCH_OPTIONS_OID_W",
    "LDAP_SERVER_SET_OWNER_OID",
    "LDAP_SERVER_SET_OWNER_OID_W",
    "LDAP_SERVER_SHOW_DEACTIVATED_LINK_OID",
    "LDAP_SERVER_SHOW_DEACTIVATED_LINK_OID_W",
    "LDAP_SERVER_SHOW_DELETED_OID",
    "LDAP_SERVER_SHOW_DELETED_OID_W",
    "LDAP_SERVER_SHOW_RECYCLED_OID",
    "LDAP_SERVER_SHOW_RECYCLED_OID_W",
    "LDAP_SERVER_SHUTDOWN_NOTIFY_OID",
    "LDAP_SERVER_SHUTDOWN_NOTIFY_OID_W",
    "LDAP_SERVER_SORT_OID",
    "LDAP_SERVER_SORT_OID_W",
    "LDAP_SERVER_TREE_DELETE_EX_OID",
    "LDAP_SERVER_TREE_DELETE_EX_OID_W",
    "LDAP_SERVER_TREE_DELETE_OID",
    "LDAP_SERVER_TREE_DELETE_OID_W",
    "LDAP_SERVER_UPDATE_STATS_OID",
    "LDAP_SERVER_UPDATE_STATS_OID_W",
    "LDAP_SERVER_VERIFY_NAME_OID",
    "LDAP_SERVER_VERIFY_NAME_OID_W",
    "LDAP_SERVER_WHO_AM_I_OID",
    "LDAP_SERVER_WHO_AM_I_OID_W",
    "LDAP_SESSION_CMD",
    "LDAP_SIZELIMIT_EXCEEDED",
    "LDAP_SORT_CONTROL_MISSING",
    "LDAP_SSL_GC_PORT",
    "LDAP_SSL_PORT",
    "LDAP_START_TLS_OID",
    "LDAP_START_TLS_OID_W",
    "LDAP_STRONG_AUTH_REQUIRED",
    "LDAP_SUBSTRING_ANY",
    "LDAP_SUBSTRING_FINAL",
    "LDAP_SUBSTRING_INITIAL",
    "LDAP_SUCCESS",
    "LDAP_TIMELIMIT_EXCEEDED",
    "LDAP_TIMEOUT",
    "LDAP_TIMEVAL",
    "LDAP_TTL_EXTENDED_OP_OID",
    "LDAP_TTL_EXTENDED_OP_OID_W",
    "LDAP_UNAVAILABLE",
    "LDAP_UNAVAILABLE_CRIT_EXTENSION",
    "LDAP_UNBIND_CMD",
    "LDAP_UNDEFINED_TYPE",
    "LDAP_UNICODE",
    "LDAP_UNWILLING_TO_PERFORM",
    "LDAP_UPDATE_STATS_INVOCATIONID_OID",
    "LDAP_UPDATE_STATS_INVOCATIONID_OID_W",
    "LDAP_UPDATE_STATS_USN_OID",
    "LDAP_UPDATE_STATS_USN_OID_W",
    "LDAP_USER_CANCELLED",
    "LDAP_VENDOR_NAME",
    "LDAP_VENDOR_NAME_W",
    "LDAP_VENDOR_VERSION",
    "LDAP_VERSION",
    "LDAP_VERSION1",
    "LDAP_VERSION2",
    "LDAP_VERSION3",
    "LDAP_VERSION_INFO",
    "LDAP_VERSION_MAX",
    "LDAP_VERSION_MIN",
    "LDAP_VIRTUAL_LIST_VIEW_ERROR",
    "LDAP_VLVINFO_VERSION",
    "LdapGetLastError",
    "LdapMapErrorToWin32",
    "LdapUTF8ToUnicode",
    "LdapUnicodeToUTF8",
    "NOTIFYOFNEWCONNECTION",
    "QUERYCLIENTCERT",
    "QUERYFORCONNECTION",
    "SERVER_SEARCH_FLAG_DOMAIN_SCOPE",
    "SERVER_SEARCH_FLAG_PHANTOM_ROOT",
    "VERIFYSERVERCERT",
    "ber_alloc_t",
    "ber_bvdup",
    "ber_bvecfree",
    "ber_bvfree",
    "ber_first_element",
    "ber_flatten",
    "ber_free",
    "ber_init",
    "ber_next_element",
    "ber_peek_tag",
    "ber_printf",
    "ber_scanf",
    "ber_skip_tag",
    "cldap_open",
    "cldap_openA",
    "cldap_openW",
    "ldap_abandon",
    "ldap_add",
    "ldap_addA",
    "ldap_addW",
    "ldap_add_ext",
    "ldap_add_extA",
    "ldap_add_extW",
    "ldap_add_ext_s",
    "ldap_add_ext_sA",
    "ldap_add_ext_sW",
    "ldap_add_s",
    "ldap_add_sA",
    "ldap_add_sW",
    "ldap_bind",
    "ldap_bindA",
    "ldap_bindW",
    "ldap_bind_s",
    "ldap_bind_sA",
    "ldap_bind_sW",
    "ldap_check_filterA",
    "ldap_check_filterW",
    "ldap_cleanup",
    "ldap_close_extended_op",
    "ldap_compare",
    "ldap_compareA",
    "ldap_compareW",
    "ldap_compare_ext",
    "ldap_compare_extA",
    "ldap_compare_extW",
    "ldap_compare_ext_s",
    "ldap_compare_ext_sA",
    "ldap_compare_ext_sW",
    "ldap_compare_s",
    "ldap_compare_sA",
    "ldap_compare_sW",
    "ldap_conn_from_msg",
    "ldap_connect",
    "ldap_control_free",
    "ldap_control_freeA",
    "ldap_control_freeW",
    "ldap_controls_free",
    "ldap_controls_freeA",
    "ldap_controls_freeW",
    "ldap_count_entries",
    "ldap_count_references",
    "ldap_count_values",
    "ldap_count_valuesA",
    "ldap_count_valuesW",
    "ldap_count_values_len",
    "ldap_create_page_control",
    "ldap_create_page_controlA",
    "ldap_create_page_controlW",
    "ldap_create_sort_control",
    "ldap_create_sort_controlA",
    "ldap_create_sort_controlW",
    "ldap_create_vlv_controlA",
    "ldap_create_vlv_controlW",
    "ldap_delete",
    "ldap_deleteA",
    "ldap_deleteW",
    "ldap_delete_ext",
    "ldap_delete_extA",
    "ldap_delete_extW",
    "ldap_delete_ext_s",
    "ldap_delete_ext_sA",
    "ldap_delete_ext_sW",
    "ldap_delete_s",
    "ldap_delete_sA",
    "ldap_delete_sW",
    "ldap_dn2ufn",
    "ldap_dn2ufnA",
    "ldap_dn2ufnW",
    "ldap_encode_sort_controlA",
    "ldap_encode_sort_controlW",
    "ldap_err2string",
    "ldap_err2stringA",
    "ldap_err2stringW",
    "ldap_escape_filter_element",
    "ldap_escape_filter_elementA",
    "ldap_escape_filter_elementW",
    "ldap_explode_dn",
    "ldap_explode_dnA",
    "ldap_explode_dnW",
    "ldap_extended_operation",
    "ldap_extended_operationA",
    "ldap_extended_operationW",
    "ldap_extended_operation_sA",
    "ldap_extended_operation_sW",
    "ldap_first_attribute",
    "ldap_first_attributeA",
    "ldap_first_attributeW",
    "ldap_first_entry",
    "ldap_first_reference",
    "ldap_free_controls",
    "ldap_free_controlsA",
    "ldap_free_controlsW",
    "ldap_get_dn",
    "ldap_get_dnA",
    "ldap_get_dnW",
    "ldap_get_next_page",
    "ldap_get_next_page_s",
    "ldap_get_option",
    "ldap_get_optionW",
    "ldap_get_paged_count",
    "ldap_get_values",
    "ldap_get_valuesA",
    "ldap_get_valuesW",
    "ldap_get_values_len",
    "ldap_get_values_lenA",
    "ldap_get_values_lenW",
    "ldap_init",
    "ldap_initA",
    "ldap_initW",
    "ldap_memfree",
    "ldap_memfreeA",
    "ldap_memfreeW",
    "ldap_modify",
    "ldap_modifyA",
    "ldap_modifyW",
    "ldap_modify_ext",
    "ldap_modify_extA",
    "ldap_modify_extW",
    "ldap_modify_ext_s",
    "ldap_modify_ext_sA",
    "ldap_modify_ext_sW",
    "ldap_modify_s",
    "ldap_modify_sA",
    "ldap_modify_sW",
    "ldap_modrdn",
    "ldap_modrdn2",
    "ldap_modrdn2A",
    "ldap_modrdn2W",
    "ldap_modrdn2_s",
    "ldap_modrdn2_sA",
    "ldap_modrdn2_sW",
    "ldap_modrdnA",
    "ldap_modrdnW",
    "ldap_modrdn_s",
    "ldap_modrdn_sA",
    "ldap_modrdn_sW",
    "ldap_msgfree",
    "ldap_next_attribute",
    "ldap_next_attributeA",
    "ldap_next_attributeW",
    "ldap_next_entry",
    "ldap_next_reference",
    "ldap_open",
    "ldap_openA",
    "ldap_openW",
    "ldap_parse_extended_resultA",
    "ldap_parse_extended_resultW",
    "ldap_parse_page_control",
    "ldap_parse_page_controlA",
    "ldap_parse_page_controlW",
    "ldap_parse_reference",
    "ldap_parse_referenceA",
    "ldap_parse_referenceW",
    "ldap_parse_result",
    "ldap_parse_resultA",
    "ldap_parse_resultW",
    "ldap_parse_sort_control",
    "ldap_parse_sort_controlA",
    "ldap_parse_sort_controlW",
    "ldap_parse_vlv_controlA",
    "ldap_parse_vlv_controlW",
    "ldap_perror",
    "ldap_rename_ext",
    "ldap_rename_extA",
    "ldap_rename_extW",
    "ldap_rename_ext_s",
    "ldap_rename_ext_sA",
    "ldap_rename_ext_sW",
    "ldap_result",
    "ldap_result2error",
    "ldap_sasl_bindA",
    "ldap_sasl_bindW",
    "ldap_sasl_bind_sA",
    "ldap_sasl_bind_sW",
    "ldap_search",
    "ldap_searchA",
    "ldap_searchW",
    "ldap_search_abandon_page",
    "ldap_search_ext",
    "ldap_search_extA",
    "ldap_search_extW",
    "ldap_search_ext_s",
    "ldap_search_ext_sA",
    "ldap_search_ext_sW",
    "ldap_search_init_page",
    "ldap_search_init_pageA",
    "ldap_search_init_pageW",
    "ldap_search_s",
    "ldap_search_sA",
    "ldap_search_sW",
    "ldap_search_st",
    "ldap_search_stA",
    "ldap_search_stW",
    "ldap_set_dbg_flags",
    "ldap_set_dbg_routine",
    "ldap_set_option",
    "ldap_set_optionW",
    "ldap_simple_bind",
    "ldap_simple_bindA",
    "ldap_simple_bindW",
    "ldap_simple_bind_s",
    "ldap_simple_bind_sA",
    "ldap_simple_bind_sW",
    "ldap_sslinit",
    "ldap_sslinitA",
    "ldap_sslinitW",
    "ldap_start_tls_sA",
    "ldap_start_tls_sW",
    "ldap_startup",
    "ldap_stop_tls_s",
    "ldap_ufn2dn",
    "ldap_ufn2dnA",
    "ldap_ufn2dnW",
    "ldap_unbind",
    "ldap_unbind_s",
    "ldap_value_free",
    "ldap_value_freeA",
    "ldap_value_freeW",
    "ldap_value_free_len",
]
