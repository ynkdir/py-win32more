from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Networking.Ldap
import win32more.Security.Authentication.Identity
import win32more.Security.Cryptography
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
LBER_ERROR: Int32 = -1
LBER_DEFAULT: Int32 = -1
LDAP_UNICODE: UInt32 = 1
LDAP_PORT: UInt32 = 389
LDAP_SSL_PORT: UInt32 = 636
LDAP_GC_PORT: UInt32 = 3268
LDAP_SSL_GC_PORT: UInt32 = 3269
LDAP_VERSION1: UInt32 = 1
LDAP_VERSION2: UInt32 = 2
LDAP_VERSION3: UInt32 = 3
LDAP_VERSION: UInt32 = 2
LDAP_BIND_CMD: Int32 = 96
LDAP_UNBIND_CMD: Int32 = 66
LDAP_SEARCH_CMD: Int32 = 99
LDAP_MODIFY_CMD: Int32 = 102
LDAP_ADD_CMD: Int32 = 104
LDAP_DELETE_CMD: Int32 = 74
LDAP_MODRDN_CMD: Int32 = 108
LDAP_COMPARE_CMD: Int32 = 110
LDAP_ABANDON_CMD: Int32 = 80
LDAP_SESSION_CMD: Int32 = 113
LDAP_EXTENDED_CMD: Int32 = 119
LDAP_RES_BIND: Int32 = 97
LDAP_RES_SEARCH_ENTRY: Int32 = 100
LDAP_RES_SEARCH_RESULT: Int32 = 101
LDAP_RES_MODIFY: Int32 = 103
LDAP_RES_ADD: Int32 = 105
LDAP_RES_DELETE: Int32 = 107
LDAP_RES_MODRDN: Int32 = 109
LDAP_RES_COMPARE: Int32 = 111
LDAP_RES_SESSION: Int32 = 114
LDAP_RES_REFERRAL: Int32 = 115
LDAP_RES_EXTENDED: Int32 = 120
LDAP_RES_ANY: Int32 = -1
LDAP_INVALID_CMD: UInt32 = 255
LDAP_INVALID_RES: UInt32 = 255
LDAP_AUTH_SIMPLE: Int32 = 128
LDAP_AUTH_SASL: Int32 = 131
LDAP_AUTH_OTHERKIND: Int32 = 134
LDAP_FILTER_AND: UInt32 = 160
LDAP_FILTER_OR: UInt32 = 161
LDAP_FILTER_NOT: UInt32 = 162
LDAP_FILTER_EQUALITY: UInt32 = 163
LDAP_FILTER_SUBSTRINGS: UInt32 = 164
LDAP_FILTER_GE: UInt32 = 165
LDAP_FILTER_LE: UInt32 = 166
LDAP_FILTER_PRESENT: UInt32 = 135
LDAP_FILTER_APPROX: UInt32 = 168
LDAP_FILTER_EXTENSIBLE: UInt32 = 169
LDAP_SUBSTRING_INITIAL: Int32 = 128
LDAP_SUBSTRING_ANY: Int32 = 129
LDAP_SUBSTRING_FINAL: Int32 = 130
LDAP_DEREF_NEVER: UInt32 = 0
LDAP_DEREF_SEARCHING: UInt32 = 1
LDAP_DEREF_FINDING: UInt32 = 2
LDAP_DEREF_ALWAYS: UInt32 = 3
LDAP_NO_LIMIT: UInt32 = 0
LDAP_OPT_DNS: UInt32 = 1
LDAP_OPT_CHASE_REFERRALS: UInt32 = 2
LDAP_OPT_RETURN_REFS: UInt32 = 4
LDAP_CONTROL_REFERRALS_W: String = '1.2.840.113556.1.4.616'
LDAP_CONTROL_REFERRALS: String = '1.2.840.113556.1.4.616'
LDAP_MOD_ADD: UInt32 = 0
LDAP_MOD_DELETE: UInt32 = 1
LDAP_MOD_REPLACE: UInt32 = 2
LDAP_MOD_BVALUES: UInt32 = 128
LDAP_OPT_API_INFO: UInt32 = 0
LDAP_OPT_DESC: UInt32 = 1
LDAP_OPT_DEREF: UInt32 = 2
LDAP_OPT_SIZELIMIT: UInt32 = 3
LDAP_OPT_TIMELIMIT: UInt32 = 4
LDAP_OPT_THREAD_FN_PTRS: UInt32 = 5
LDAP_OPT_REBIND_FN: UInt32 = 6
LDAP_OPT_REBIND_ARG: UInt32 = 7
LDAP_OPT_REFERRALS: UInt32 = 8
LDAP_OPT_RESTART: UInt32 = 9
LDAP_OPT_SSL: UInt32 = 10
LDAP_OPT_IO_FN_PTRS: UInt32 = 11
LDAP_OPT_CACHE_FN_PTRS: UInt32 = 13
LDAP_OPT_CACHE_STRATEGY: UInt32 = 14
LDAP_OPT_CACHE_ENABLE: UInt32 = 15
LDAP_OPT_REFERRAL_HOP_LIMIT: UInt32 = 16
LDAP_OPT_PROTOCOL_VERSION: UInt32 = 17
LDAP_OPT_VERSION: UInt32 = 17
LDAP_OPT_API_FEATURE_INFO: UInt32 = 21
LDAP_OPT_HOST_NAME: UInt32 = 48
LDAP_OPT_ERROR_NUMBER: UInt32 = 49
LDAP_OPT_ERROR_STRING: UInt32 = 50
LDAP_OPT_SERVER_ERROR: UInt32 = 51
LDAP_OPT_SERVER_EXT_ERROR: UInt32 = 52
LDAP_OPT_HOST_REACHABLE: UInt32 = 62
LDAP_OPT_PING_KEEP_ALIVE: UInt32 = 54
LDAP_OPT_PING_WAIT_TIME: UInt32 = 55
LDAP_OPT_PING_LIMIT: UInt32 = 56
LDAP_OPT_DNSDOMAIN_NAME: UInt32 = 59
LDAP_OPT_GETDSNAME_FLAGS: UInt32 = 61
LDAP_OPT_PROMPT_CREDENTIALS: UInt32 = 63
LDAP_OPT_AUTO_RECONNECT: UInt32 = 145
LDAP_OPT_SSPI_FLAGS: UInt32 = 146
LDAP_OPT_SSL_INFO: UInt32 = 147
LDAP_OPT_TLS: UInt32 = 10
LDAP_OPT_TLS_INFO: UInt32 = 147
LDAP_OPT_SIGN: UInt32 = 149
LDAP_OPT_ENCRYPT: UInt32 = 150
LDAP_OPT_SASL_METHOD: UInt32 = 151
LDAP_OPT_AREC_EXCLUSIVE: UInt32 = 152
LDAP_OPT_SECURITY_CONTEXT: UInt32 = 153
LDAP_OPT_ROOTDSE_CACHE: UInt32 = 154
LDAP_OPT_TCP_KEEPALIVE: UInt32 = 64
LDAP_OPT_FAST_CONCURRENT_BIND: UInt32 = 65
LDAP_OPT_SEND_TIMEOUT: UInt32 = 66
LDAP_OPT_SCH_FLAGS: UInt32 = 67
LDAP_OPT_SOCKET_BIND_ADDRESSES: UInt32 = 68
LDAP_CHASE_SUBORDINATE_REFERRALS: UInt32 = 32
LDAP_CHASE_EXTERNAL_REFERRALS: UInt32 = 64
LDAP_SCOPE_BASE: UInt32 = 0
LDAP_SCOPE_ONELEVEL: UInt32 = 1
LDAP_SCOPE_SUBTREE: UInt32 = 2
LDAP_MSG_ONE: UInt32 = 0
LDAP_MSG_ALL: UInt32 = 1
LDAP_MSG_RECEIVED: UInt32 = 2
LBER_USE_DER: UInt32 = 1
LBER_USE_INDEFINITE_LEN: UInt32 = 2
LBER_TRANSLATE_STRINGS: UInt32 = 4
LAPI_MAJOR_VER1: UInt32 = 1
LAPI_MINOR_VER1: UInt32 = 1
LDAP_API_INFO_VERSION: UInt32 = 1
LDAP_API_VERSION: UInt32 = 2004
LDAP_VERSION_MIN: UInt32 = 2
LDAP_VERSION_MAX: UInt32 = 3
LDAP_VENDOR_NAME: String = 'Microsoft Corporation.'
LDAP_VENDOR_NAME_W: String = 'Microsoft Corporation.'
LDAP_VENDOR_VERSION: UInt32 = 510
LDAP_FEATURE_INFO_VERSION: UInt32 = 1
LDAP_SERVER_SORT_OID: String = '1.2.840.113556.1.4.473'
LDAP_SERVER_SORT_OID_W: String = '1.2.840.113556.1.4.473'
LDAP_SERVER_RESP_SORT_OID: String = '1.2.840.113556.1.4.474'
LDAP_SERVER_RESP_SORT_OID_W: String = '1.2.840.113556.1.4.474'
LDAP_PAGED_RESULT_OID_STRING: String = '1.2.840.113556.1.4.319'
LDAP_PAGED_RESULT_OID_STRING_W: String = '1.2.840.113556.1.4.319'
LDAP_CONTROL_VLVREQUEST: String = '2.16.840.1.113730.3.4.9'
LDAP_CONTROL_VLVREQUEST_W: String = '2.16.840.1.113730.3.4.9'
LDAP_CONTROL_VLVRESPONSE: String = '2.16.840.1.113730.3.4.10'
LDAP_CONTROL_VLVRESPONSE_W: String = '2.16.840.1.113730.3.4.10'
LDAP_API_FEATURE_VIRTUAL_LIST_VIEW: UInt32 = 1001
LDAP_VLVINFO_VERSION: UInt32 = 1
LDAP_START_TLS_OID: String = '1.3.6.1.4.1.1466.20037'
LDAP_START_TLS_OID_W: String = '1.3.6.1.4.1.1466.20037'
LDAP_TTL_EXTENDED_OP_OID: String = '1.3.6.1.4.1.1466.101.119.1'
LDAP_TTL_EXTENDED_OP_OID_W: String = '1.3.6.1.4.1.1466.101.119.1'
LDAP_OPT_REFERRAL_CALLBACK: UInt32 = 112
LDAP_OPT_CLIENT_CERTIFICATE: UInt32 = 128
LDAP_OPT_SERVER_CERTIFICATE: UInt32 = 129
LDAP_OPT_REF_DEREF_CONN_PER_MSG: UInt32 = 148
LDAP_SERVER_FORCE_UPDATE_OID: String = '1.2.840.113556.1.4.1974'
LDAP_SERVER_FORCE_UPDATE_OID_W: String = '1.2.840.113556.1.4.1974'
LDAP_SERVER_PERMISSIVE_MODIFY_OID: String = '1.2.840.113556.1.4.1413'
LDAP_SERVER_PERMISSIVE_MODIFY_OID_W: String = '1.2.840.113556.1.4.1413'
LDAP_SERVER_SHOW_DELETED_OID: String = '1.2.840.113556.1.4.417'
LDAP_SERVER_SHOW_DELETED_OID_W: String = '1.2.840.113556.1.4.417'
LDAP_SERVER_SHOW_RECYCLED_OID: String = '1.2.840.113556.1.4.2064'
LDAP_SERVER_SHOW_RECYCLED_OID_W: String = '1.2.840.113556.1.4.2064'
LDAP_SERVER_EXPECTED_ENTRY_COUNT_OID: String = '1.2.840.113556.1.4.2211'
LDAP_SERVER_EXPECTED_ENTRY_COUNT_OID_W: String = '1.2.840.113556.1.4.2211'
LDAP_SERVER_SEARCH_HINTS_OID: String = '1.2.840.113556.1.4.2206'
LDAP_SERVER_SEARCH_HINTS_OID_W: String = '1.2.840.113556.1.4.2206'
LDAP_SEARCH_HINT_INDEX_ONLY_OID: String = '1.2.840.113556.1.4.2207'
LDAP_SEARCH_HINT_INDEX_ONLY_OID_W: String = '1.2.840.113556.1.4.2207'
LDAP_SEARCH_HINT_SOFT_SIZE_LIMIT_OID: String = '1.2.840.113556.1.4.2210'
LDAP_SEARCH_HINT_SOFT_SIZE_LIMIT_OID_W: String = '1.2.840.113556.1.4.2210'
LDAP_SEARCH_HINT_REQUIRED_INDEX_OID: String = '1.2.840.113556.1.4.2306'
LDAP_SEARCH_HINT_REQUIRED_INDEX_OID_W: String = '1.2.840.113556.1.4.2306'
LDAP_SERVER_UPDATE_STATS_OID: String = '1.2.840.113556.1.4.2205'
LDAP_SERVER_UPDATE_STATS_OID_W: String = '1.2.840.113556.1.4.2205'
LDAP_UPDATE_STATS_USN_OID: String = '1.2.840.113556.1.4.2208'
LDAP_UPDATE_STATS_USN_OID_W: String = '1.2.840.113556.1.4.2208'
LDAP_UPDATE_STATS_INVOCATIONID_OID: String = '1.2.840.113556.1.4.2209'
LDAP_UPDATE_STATS_INVOCATIONID_OID_W: String = '1.2.840.113556.1.4.2209'
LDAP_SERVER_GET_STATS_OID: String = '1.2.840.113556.1.4.970'
LDAP_SERVER_GET_STATS_OID_W: String = '1.2.840.113556.1.4.970'
LDAP_SERVER_SHOW_DEACTIVATED_LINK_OID: String = '1.2.840.113556.1.4.2065'
LDAP_SERVER_SHOW_DEACTIVATED_LINK_OID_W: String = '1.2.840.113556.1.4.2065'
LDAP_SERVER_POLICY_HINTS_DEPRECATED_OID: String = '1.2.840.113556.1.4.2066'
LDAP_SERVER_POLICY_HINTS_DEPRECATED_OID_W: String = '1.2.840.113556.1.4.2066'
LDAP_SERVER_POLICY_HINTS_OID: String = '1.2.840.113556.1.4.2239'
LDAP_SERVER_POLICY_HINTS_OID_W: String = '1.2.840.113556.1.4.2239'
LDAP_SERVER_RANGE_OPTION_OID: String = '1.2.840.113556.1.4.802'
LDAP_SERVER_RANGE_OPTION_OID_W: String = '1.2.840.113556.1.4.802'
LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID: String = '1.2.840.113556.1.4.521'
LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID_W: String = '1.2.840.113556.1.4.521'
LDAP_SERVER_NOTIFICATION_OID: String = '1.2.840.113556.1.4.528'
LDAP_SERVER_NOTIFICATION_OID_W: String = '1.2.840.113556.1.4.528'
LDAP_SERVER_SHUTDOWN_NOTIFY_OID: String = '1.2.840.113556.1.4.1907'
LDAP_SERVER_SHUTDOWN_NOTIFY_OID_W: String = '1.2.840.113556.1.4.1907'
LDAP_SERVER_LAZY_COMMIT_OID: String = '1.2.840.113556.1.4.619'
LDAP_SERVER_LAZY_COMMIT_OID_W: String = '1.2.840.113556.1.4.619'
LDAP_SERVER_SD_FLAGS_OID: String = '1.2.840.113556.1.4.801'
LDAP_SERVER_SD_FLAGS_OID_W: String = '1.2.840.113556.1.4.801'
LDAP_SERVER_TREE_DELETE_EX_OID: String = '1.2.840.113556.1.4.2204'
LDAP_SERVER_TREE_DELETE_EX_OID_W: String = '1.2.840.113556.1.4.2204'
LDAP_SERVER_TREE_DELETE_OID: String = '1.2.840.113556.1.4.805'
LDAP_SERVER_TREE_DELETE_OID_W: String = '1.2.840.113556.1.4.805'
LDAP_SERVER_ASQ_OID: String = '1.2.840.113556.1.4.1504'
LDAP_SERVER_ASQ_OID_W: String = '1.2.840.113556.1.4.1504'
LDAP_SERVER_DIRSYNC_OID: String = '1.2.840.113556.1.4.841'
LDAP_SERVER_DIRSYNC_OID_W: String = '1.2.840.113556.1.4.841'
LDAP_SERVER_DIRSYNC_EX_OID: String = '1.2.840.113556.1.4.2090'
LDAP_SERVER_DIRSYNC_EX_OID_W: String = '1.2.840.113556.1.4.2090'
LDAP_SERVER_EXTENDED_DN_OID: String = '1.2.840.113556.1.4.529'
LDAP_SERVER_EXTENDED_DN_OID_W: String = '1.2.840.113556.1.4.529'
LDAP_SERVER_VERIFY_NAME_OID: String = '1.2.840.113556.1.4.1338'
LDAP_SERVER_VERIFY_NAME_OID_W: String = '1.2.840.113556.1.4.1338'
LDAP_SERVER_DOMAIN_SCOPE_OID: String = '1.2.840.113556.1.4.1339'
LDAP_SERVER_DOMAIN_SCOPE_OID_W: String = '1.2.840.113556.1.4.1339'
LDAP_SERVER_SEARCH_OPTIONS_OID: String = '1.2.840.113556.1.4.1340'
LDAP_SERVER_SEARCH_OPTIONS_OID_W: String = '1.2.840.113556.1.4.1340'
SERVER_SEARCH_FLAG_DOMAIN_SCOPE: UInt32 = 1
SERVER_SEARCH_FLAG_PHANTOM_ROOT: UInt32 = 2
LDAP_SERVER_QUOTA_CONTROL_OID: String = '1.2.840.113556.1.4.1852'
LDAP_SERVER_QUOTA_CONTROL_OID_W: String = '1.2.840.113556.1.4.1852'
LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID: String = '1.2.840.113556.1.4.1948'
LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID_W: String = '1.2.840.113556.1.4.1948'
LDAP_SERVER_DN_INPUT_OID: String = '1.2.840.113556.1.4.2026'
LDAP_SERVER_DN_INPUT_OID_W: String = '1.2.840.113556.1.4.2026'
LDAP_SERVER_SET_OWNER_OID: String = '1.2.840.113556.1.4.2255'
LDAP_SERVER_SET_OWNER_OID_W: String = '1.2.840.113556.1.4.2255'
LDAP_SERVER_BYPASS_QUOTA_OID: String = '1.2.840.113556.1.4.2256'
LDAP_SERVER_BYPASS_QUOTA_OID_W: String = '1.2.840.113556.1.4.2256'
LDAP_SERVER_LINK_TTL_OID: String = '1.2.840.113556.1.4.2309'
LDAP_SERVER_LINK_TTL_OID_W: String = '1.2.840.113556.1.4.2309'
LDAP_OPATT_BECOME_DOM_MASTER: String = 'becomeDomainMaster'
LDAP_OPATT_BECOME_DOM_MASTER_W: String = 'becomeDomainMaster'
LDAP_OPATT_BECOME_RID_MASTER: String = 'becomeRidMaster'
LDAP_OPATT_BECOME_RID_MASTER_W: String = 'becomeRidMaster'
LDAP_OPATT_BECOME_SCHEMA_MASTER: String = 'becomeSchemaMaster'
LDAP_OPATT_BECOME_SCHEMA_MASTER_W: String = 'becomeSchemaMaster'
LDAP_OPATT_RECALC_HIERARCHY: String = 'recalcHierarchy'
LDAP_OPATT_RECALC_HIERARCHY_W: String = 'recalcHierarchy'
LDAP_OPATT_SCHEMA_UPDATE_NOW: String = 'schemaUpdateNow'
LDAP_OPATT_SCHEMA_UPDATE_NOW_W: String = 'schemaUpdateNow'
LDAP_OPATT_BECOME_PDC: String = 'becomePdc'
LDAP_OPATT_BECOME_PDC_W: String = 'becomePdc'
LDAP_OPATT_FIXUP_INHERITANCE: String = 'fixupInheritance'
LDAP_OPATT_FIXUP_INHERITANCE_W: String = 'fixupInheritance'
LDAP_OPATT_INVALIDATE_RID_POOL: String = 'invalidateRidPool'
LDAP_OPATT_INVALIDATE_RID_POOL_W: String = 'invalidateRidPool'
LDAP_OPATT_ABANDON_REPL: String = 'abandonReplication'
LDAP_OPATT_ABANDON_REPL_W: String = 'abandonReplication'
LDAP_OPATT_DO_GARBAGE_COLLECTION: String = 'doGarbageCollection'
LDAP_OPATT_DO_GARBAGE_COLLECTION_W: String = 'doGarbageCollection'
LDAP_OPATT_SUBSCHEMA_SUBENTRY: String = 'subschemaSubentry'
LDAP_OPATT_SUBSCHEMA_SUBENTRY_W: String = 'subschemaSubentry'
LDAP_OPATT_CURRENT_TIME: String = 'currentTime'
LDAP_OPATT_CURRENT_TIME_W: String = 'currentTime'
LDAP_OPATT_SERVER_NAME: String = 'serverName'
LDAP_OPATT_SERVER_NAME_W: String = 'serverName'
LDAP_OPATT_NAMING_CONTEXTS: String = 'namingContexts'
LDAP_OPATT_NAMING_CONTEXTS_W: String = 'namingContexts'
LDAP_OPATT_DEFAULT_NAMING_CONTEXT: String = 'defaultNamingContext'
LDAP_OPATT_DEFAULT_NAMING_CONTEXT_W: String = 'defaultNamingContext'
LDAP_OPATT_SUPPORTED_CONTROL: String = 'supportedControl'
LDAP_OPATT_SUPPORTED_CONTROL_W: String = 'supportedControl'
LDAP_OPATT_HIGHEST_COMMITTED_USN: String = 'highestCommitedUSN'
LDAP_OPATT_HIGHEST_COMMITTED_USN_W: String = 'highestCommitedUSN'
LDAP_OPATT_SUPPORTED_LDAP_VERSION: String = 'supportedLDAPVersion'
LDAP_OPATT_SUPPORTED_LDAP_VERSION_W: String = 'supportedLDAPVersion'
LDAP_OPATT_SUPPORTED_LDAP_POLICIES: String = 'supportedLDAPPolicies'
LDAP_OPATT_SUPPORTED_LDAP_POLICIES_W: String = 'supportedLDAPPolicies'
LDAP_OPATT_SCHEMA_NAMING_CONTEXT: String = 'schemaNamingContext'
LDAP_OPATT_SCHEMA_NAMING_CONTEXT_W: String = 'schemaNamingContext'
LDAP_OPATT_CONFIG_NAMING_CONTEXT: String = 'configurationNamingContext'
LDAP_OPATT_CONFIG_NAMING_CONTEXT_W: String = 'configurationNamingContext'
LDAP_OPATT_ROOT_DOMAIN_NAMING_CONTEXT: String = 'rootDomainNamingContext'
LDAP_OPATT_ROOT_DOMAIN_NAMING_CONTEXT_W: String = 'rootDomainNamingContext'
LDAP_OPATT_SUPPORTED_SASL_MECHANISM: String = 'supportedSASLMechanisms'
LDAP_OPATT_SUPPORTED_SASL_MECHANISM_W: String = 'supportedSASLMechanisms'
LDAP_OPATT_DNS_HOST_NAME: String = 'dnsHostName'
LDAP_OPATT_DNS_HOST_NAME_W: String = 'dnsHostName'
LDAP_OPATT_LDAP_SERVICE_NAME: String = 'ldapServiceName'
LDAP_OPATT_LDAP_SERVICE_NAME_W: String = 'ldapServiceName'
LDAP_OPATT_DS_SERVICE_NAME: String = 'dsServiceName'
LDAP_OPATT_DS_SERVICE_NAME_W: String = 'dsServiceName'
LDAP_OPATT_SUPPORTED_CAPABILITIES: String = 'supportedCapabilities'
LDAP_OPATT_SUPPORTED_CAPABILITIES_W: String = 'supportedCapabilities'
LDAP_CAP_ACTIVE_DIRECTORY_OID: String = '1.2.840.113556.1.4.800'
LDAP_CAP_ACTIVE_DIRECTORY_OID_W: String = '1.2.840.113556.1.4.800'
LDAP_CAP_ACTIVE_DIRECTORY_V51_OID: String = '1.2.840.113556.1.4.1670'
LDAP_CAP_ACTIVE_DIRECTORY_V51_OID_W: String = '1.2.840.113556.1.4.1670'
LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID: String = '1.2.840.113556.1.4.1791'
LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID_W: String = '1.2.840.113556.1.4.1791'
LDAP_CAP_ACTIVE_DIRECTORY_ADAM_OID: String = '1.2.840.113556.1.4.1851'
LDAP_CAP_ACTIVE_DIRECTORY_ADAM_OID_W: String = '1.2.840.113556.1.4.1851'
LDAP_CAP_ACTIVE_DIRECTORY_PARTIAL_SECRETS_OID: String = '1.2.840.113556.1.4.1920'
LDAP_CAP_ACTIVE_DIRECTORY_PARTIAL_SECRETS_OID_W: String = '1.2.840.113556.1.4.1920'
LDAP_CAP_ACTIVE_DIRECTORY_V60_OID: String = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V60_OID_W: String = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V61_OID: String = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V61_OID_W: String = '1.2.840.113556.1.4.1935'
LDAP_CAP_ACTIVE_DIRECTORY_V61_R2_OID: String = '1.2.840.113556.1.4.2080'
LDAP_CAP_ACTIVE_DIRECTORY_V61_R2_OID_W: String = '1.2.840.113556.1.4.2080'
LDAP_CAP_ACTIVE_DIRECTORY_W8_OID: String = '1.2.840.113556.1.4.2237'
LDAP_CAP_ACTIVE_DIRECTORY_W8_OID_W: String = '1.2.840.113556.1.4.2237'
LDAP_MATCHING_RULE_BIT_AND: String = '1.2.840.113556.1.4.803'
LDAP_MATCHING_RULE_BIT_AND_W: String = '1.2.840.113556.1.4.803'
LDAP_MATCHING_RULE_BIT_OR: String = '1.2.840.113556.1.4.804'
LDAP_MATCHING_RULE_BIT_OR_W: String = '1.2.840.113556.1.4.804'
LDAP_MATCHING_RULE_TRANSITIVE_EVALUATION: String = '1.2.840.113556.1.4.1941'
LDAP_MATCHING_RULE_TRANSITIVE_EVALUATION_W: String = '1.2.840.113556.1.4.1941'
LDAP_MATCHING_RULE_DN_BINARY_COMPLEX: String = '1.2.840.113556.1.4.2253'
LDAP_MATCHING_RULE_DN_BINARY_COMPLEX_W: String = '1.2.840.113556.1.4.2253'
LDAP_SERVER_FAST_BIND_OID: String = '1.2.840.113556.1.4.1781'
LDAP_SERVER_FAST_BIND_OID_W: String = '1.2.840.113556.1.4.1781'
LDAP_SERVER_WHO_AM_I_OID: String = '1.3.6.1.4.1.4203.1.11.3'
LDAP_SERVER_WHO_AM_I_OID_W: String = '1.3.6.1.4.1.4203.1.11.3'
LDAP_SERVER_BATCH_REQUEST_OID: String = '1.2.840.113556.1.4.2212'
LDAP_SERVER_BATCH_REQUEST_OID_W: String = '1.2.840.113556.1.4.2212'
LDAP_DIRSYNC_OBJECT_SECURITY: UInt32 = 1
LDAP_DIRSYNC_ANCESTORS_FIRST_ORDER: UInt32 = 2048
LDAP_DIRSYNC_PUBLIC_DATA_ONLY: UInt32 = 8192
LDAP_DIRSYNC_INCREMENTAL_VALUES: UInt32 = 2147483648
LDAP_DIRSYNC_ROPAS_DATA_ONLY: UInt32 = 1073741824
LDAP_POLICYHINT_APPLY_FULLPWDPOLICY: UInt32 = 1
@cfunctype('WLDAP32.dll')
def ldap_openW(HostName: win32more.Foundation.PWSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_openA(HostName: win32more.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_initW(HostName: win32more.Foundation.PWSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_initA(HostName: win32more.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_sslinitW(HostName: win32more.Foundation.PWSTR, PortNumber: UInt32, secure: Int32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_sslinitA(HostName: win32more.Foundation.PSTR, PortNumber: UInt32, secure: Int32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_connect(ld: POINTER(win32more.Networking.Ldap.LDAP_head), timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_open(HostName: win32more.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_init(HostName: win32more.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_sslinit(HostName: win32more.Foundation.PSTR, PortNumber: UInt32, secure: Int32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def cldap_openW(HostName: win32more.Foundation.PWSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def cldap_openA(HostName: win32more.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def cldap_open(HostName: win32more.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ldap_unbind(ld: POINTER(win32more.Networking.Ldap.LDAP_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_unbind_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_option(ld: POINTER(win32more.Networking.Ldap.LDAP_head), option: Int32, outvalue: c_void_p) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_optionW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), option: Int32, outvalue: c_void_p) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_set_option(ld: POINTER(win32more.Networking.Ldap.LDAP_head), option: Int32, invalue: c_void_p) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_set_optionW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), option: Int32, invalue: c_void_p) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_simple_bindW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, passwd: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_simple_bindA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, passwd: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_simple_bind_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, passwd: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_simple_bind_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, passwd: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bindW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, cred: win32more.Foundation.PWSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bindA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, cred: win32more.Foundation.PSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bind_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, cred: win32more.Foundation.PWSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bind_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, cred: win32more.Foundation.PSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_sasl_bindA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistName: win32more.Foundation.PSTR, AuthMechanism: win32more.Foundation.PSTR, cred: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(Int32)) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_sasl_bindW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistName: win32more.Foundation.PWSTR, AuthMechanism: win32more.Foundation.PWSTR, cred: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), MessageNumber: POINTER(Int32)) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_sasl_bind_sA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistName: win32more.Foundation.PSTR, AuthMechanism: win32more.Foundation.PSTR, cred: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ServerData: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_sasl_bind_sW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistName: win32more.Foundation.PWSTR, AuthMechanism: win32more.Foundation.PWSTR, cred: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientCtrls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ServerData: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_simple_bind(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, passwd: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_simple_bind_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, passwd: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bind(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, cred: win32more.Foundation.PSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bind_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, cred: win32more.Foundation.PSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_searchW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PWSTR, scope: UInt32, filter: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_searchA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PWSTR, scope: UInt32, filter: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_stW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PWSTR, scope: UInt32, filter: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_stA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_extW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PWSTR, scope: UInt32, filter: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), TimeLimit: UInt32, SizeLimit: UInt32, MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_extA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), TimeLimit: UInt32, SizeLimit: UInt32, MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_ext_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PWSTR, scope: UInt32, filter: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), SizeLimit: UInt32, res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_ext_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), SizeLimit: UInt32, res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_st(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_ext(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), TimeLimit: UInt32, SizeLimit: UInt32, MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_ext_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), base: win32more.Foundation.PSTR, scope: UInt32, filter: win32more.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), SizeLimit: UInt32, res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_check_filterW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), SearchFilter: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_check_filterA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), SearchFilter: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modifyW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modifyA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_extW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_extA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_ext_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_ext_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_ext(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_ext_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, mods: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2W(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PWSTR, NewDistinguishedName: win32more.Foundation.PWSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2A(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdnW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PWSTR, NewDistinguishedName: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdnA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2_sW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PWSTR, NewDistinguishedName: win32more.Foundation.PWSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2_sA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn_sW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PWSTR, NewDistinguishedName: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn_sA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2_s(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn_s(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, NewDistinguishedName: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_extW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, NewRDN: win32more.Foundation.PWSTR, NewParent: win32more.Foundation.PWSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_extA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, NewRDN: win32more.Foundation.PSTR, NewParent: win32more.Foundation.PSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_ext_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, NewRDN: win32more.Foundation.PWSTR, NewParent: win32more.Foundation.PWSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_ext_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, NewRDN: win32more.Foundation.PSTR, NewParent: win32more.Foundation.PSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_ext(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, NewRDN: win32more.Foundation.PSTR, NewParent: win32more.Foundation.PSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_ext_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, NewRDN: win32more.Foundation.PSTR, NewParent: win32more.Foundation.PSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_addW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_addA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_extW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_extA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_ext_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModW_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_ext_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_ext(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_ext_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Networking.Ldap.LDAPModA_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compareW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, attr: win32more.Foundation.PWSTR, value: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compareA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attr: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, attr: win32more.Foundation.PWSTR, value: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attr: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attr: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, attr: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_extW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, Attr: win32more.Foundation.PWSTR, Value: win32more.Foundation.PWSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_extA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, Attr: win32more.Foundation.PSTR, Value: win32more.Foundation.PSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_ext_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, Attr: win32more.Foundation.PWSTR, Value: win32more.Foundation.PWSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_ext_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, Attr: win32more.Foundation.PSTR, Value: win32more.Foundation.PSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_ext(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, Attr: win32more.Foundation.PSTR, Value: win32more.Foundation.PSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_ext_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, Attr: win32more.Foundation.PSTR, Value: win32more.Foundation.PSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_deleteW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_deleteA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_extW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_extA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_ext_sW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PWSTR, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_ext_sA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_ext(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_ext_s(ld: POINTER(win32more.Networking.Ldap.LDAP_head), dn: win32more.Foundation.PSTR, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_abandon(ld: POINTER(win32more.Networking.Ldap.LDAP_head), msgid: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_result(ld: POINTER(win32more.Networking.Ldap.LDAP_head), msgid: UInt32, all: UInt32, timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), res: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_msgfree(res: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_result2error(ld: POINTER(win32more.Networking.Ldap.LDAP_head), res: POINTER(win32more.Networking.Ldap.LDAPMessage_head), freeit: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_resultW(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ReturnCode: POINTER(UInt32), MatchedDNs: POINTER(win32more.Foundation.PWSTR), ErrorMessage: POINTER(win32more.Foundation.PWSTR), Referrals: POINTER(POINTER(POINTER(UInt16))), ServerControls: POINTER(POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))), Freeit: win32more.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_resultA(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ReturnCode: POINTER(UInt32), MatchedDNs: POINTER(win32more.Foundation.PSTR), ErrorMessage: POINTER(win32more.Foundation.PSTR), Referrals: POINTER(POINTER(POINTER(SByte))), ServerControls: POINTER(POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))), Freeit: win32more.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_extended_resultA(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ResultOID: POINTER(win32more.Foundation.PSTR), ResultData: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), Freeit: win32more.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_extended_resultW(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ResultOID: POINTER(win32more.Foundation.PWSTR), ResultData: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), Freeit: win32more.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_controls_freeA(Controls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_control_freeA(Controls: POINTER(win32more.Networking.Ldap.LDAPControlA_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_controls_freeW(Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_control_freeW(Control: POINTER(win32more.Networking.Ldap.LDAPControlW_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_free_controlsW(Controls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_free_controlsA(Controls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_result(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ReturnCode: POINTER(UInt32), MatchedDNs: POINTER(win32more.Foundation.PSTR), ErrorMessage: POINTER(win32more.Foundation.PSTR), Referrals: POINTER(POINTER(win32more.Foundation.PSTR)), ServerControls: POINTER(POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))), Freeit: win32more.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_controls_free(Controls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_control_free(Control: POINTER(win32more.Networking.Ldap.LDAPControlA_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_free_controls(Controls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_err2stringW(err: UInt32) -> win32more.Foundation.PWSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_err2stringA(err: UInt32) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_err2string(err: UInt32) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_perror(ld: POINTER(win32more.Networking.Ldap.LDAP_head), msg: win32more.Foundation.PSTR) -> Void: ...
@cfunctype('WLDAP32.dll')
def ldap_first_entry(ld: POINTER(win32more.Networking.Ldap.LDAP_head), res: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> POINTER(win32more.Networking.Ldap.LDAPMessage_head): ...
@cfunctype('WLDAP32.dll')
def ldap_next_entry(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> POINTER(win32more.Networking.Ldap.LDAPMessage_head): ...
@cfunctype('WLDAP32.dll')
def ldap_count_entries(ld: POINTER(win32more.Networking.Ldap.LDAP_head), res: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_first_attributeW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ptr: POINTER(POINTER(win32more.Networking.Ldap.BerElement_head))) -> win32more.Foundation.PWSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_first_attributeA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ptr: POINTER(POINTER(win32more.Networking.Ldap.BerElement_head))) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_first_attribute(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ptr: POINTER(POINTER(win32more.Networking.Ldap.BerElement_head))) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_next_attributeW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ptr: POINTER(win32more.Networking.Ldap.BerElement_head)) -> win32more.Foundation.PWSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_next_attributeA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ptr: POINTER(win32more.Networking.Ldap.BerElement_head)) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_next_attribute(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), ptr: POINTER(win32more.Networking.Ldap.BerElement_head)) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_get_valuesW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), attr: win32more.Foundation.PWSTR) -> POINTER(win32more.Foundation.PWSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_get_valuesA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), attr: win32more.Foundation.PSTR) -> POINTER(win32more.Foundation.PSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_get_values(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head), attr: win32more.Foundation.PSTR) -> POINTER(win32more.Foundation.PSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_get_values_lenW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Message: POINTER(win32more.Networking.Ldap.LDAPMessage_head), attr: win32more.Foundation.PWSTR) -> POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)): ...
@cfunctype('WLDAP32.dll')
def ldap_get_values_lenA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Message: POINTER(win32more.Networking.Ldap.LDAPMessage_head), attr: win32more.Foundation.PSTR) -> POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)): ...
@cfunctype('WLDAP32.dll')
def ldap_get_values_len(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Message: POINTER(win32more.Networking.Ldap.LDAPMessage_head), attr: win32more.Foundation.PSTR) -> POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)): ...
@cfunctype('WLDAP32.dll')
def ldap_count_valuesW(vals: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_count_valuesA(vals: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_count_values(vals: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_count_values_len(vals: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_value_freeW(vals: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_value_freeA(vals: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_value_free(vals: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_value_free_len(vals: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_dnW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> win32more.Foundation.PWSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_get_dnA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_get_dn(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_explode_dnW(dn: win32more.Foundation.PWSTR, notypes: UInt32) -> POINTER(win32more.Foundation.PWSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_explode_dnA(dn: win32more.Foundation.PSTR, notypes: UInt32) -> POINTER(win32more.Foundation.PSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_explode_dn(dn: win32more.Foundation.PSTR, notypes: UInt32) -> POINTER(win32more.Foundation.PSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_dn2ufnW(dn: win32more.Foundation.PWSTR) -> win32more.Foundation.PWSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_dn2ufnA(dn: win32more.Foundation.PSTR) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_dn2ufn(dn: win32more.Foundation.PSTR) -> win32more.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_memfreeW(Block: win32more.Foundation.PWSTR) -> Void: ...
@cfunctype('WLDAP32.dll')
def ldap_memfreeA(Block: win32more.Foundation.PSTR) -> Void: ...
@cfunctype('WLDAP32.dll')
def ber_bvfree(bv: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)) -> Void: ...
@cfunctype('WLDAP32.dll')
def ldap_memfree(Block: win32more.Foundation.PSTR) -> Void: ...
@cfunctype('WLDAP32.dll')
def ldap_ufn2dnW(ufn: win32more.Foundation.PWSTR, pDn: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_ufn2dnA(ufn: win32more.Foundation.PSTR, pDn: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_ufn2dn(ufn: win32more.Foundation.PSTR, pDn: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_startup(version: POINTER(win32more.Networking.Ldap.LDAP_VERSION_INFO_head), Instance: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_cleanup(hInstance: win32more.Foundation.HANDLE) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_escape_filter_elementW(sourceFilterElement: win32more.Foundation.PSTR, sourceLength: UInt32, destFilterElement: win32more.Foundation.PWSTR, destLength: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_escape_filter_elementA(sourceFilterElement: win32more.Foundation.PSTR, sourceLength: UInt32, destFilterElement: win32more.Foundation.PSTR, destLength: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_escape_filter_element(sourceFilterElement: win32more.Foundation.PSTR, sourceLength: UInt32, destFilterElement: win32more.Foundation.PSTR, destLength: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_set_dbg_flags(NewFlags: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_set_dbg_routine(DebugPrintRoutine: win32more.Networking.Ldap.DBGPRINT) -> Void: ...
@cfunctype('WLDAP32.dll')
def LdapUTF8ToUnicode(lpSrcStr: win32more.Foundation.PSTR, cchSrc: Int32, lpDestStr: win32more.Foundation.PWSTR, cchDest: Int32) -> Int32: ...
@cfunctype('WLDAP32.dll')
def LdapUnicodeToUTF8(lpSrcStr: win32more.Foundation.PWSTR, cchSrc: Int32, lpDestStr: win32more.Foundation.PSTR, cchDest: Int32) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_sort_controlA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_sort_controlW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyW_head)), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_sort_controlA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), Result: POINTER(UInt32), Attribute: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_sort_controlW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), Result: POINTER(UInt32), Attribute: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_sort_control(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_sort_control(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), Result: POINTER(UInt32), Attribute: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_encode_sort_controlW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyW_head)), Control: POINTER(win32more.Networking.Ldap.LDAPControlW_head), Criticality: win32more.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_encode_sort_controlA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head)), Control: POINTER(win32more.Networking.Ldap.LDAPControlA_head), Criticality: win32more.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_page_controlW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), PageSize: UInt32, Cookie: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_page_controlA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), PageSize: UInt32, Cookie: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_page_controlW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), TotalCount: POINTER(UInt32), Cookie: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_page_controlA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), TotalCount: POINTER(UInt32), Cookie: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_page_control(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), PageSize: UInt32, Cookie: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_page_control(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), TotalCount: POINTER(UInt32), Cookie: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_init_pageW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PWSTR, ScopeOfSearch: UInt32, SearchFilter: win32more.Foundation.PWSTR, AttributeList: POINTER(POINTER(UInt16)), AttributesOnly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), PageTimeLimit: UInt32, TotalSizeLimit: UInt32, SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyW_head))) -> POINTER(win32more.Networking.Ldap.LDAPSearch_head): ...
@cfunctype('WLDAP32.dll')
def ldap_search_init_pageA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, ScopeOfSearch: UInt32, SearchFilter: win32more.Foundation.PSTR, AttributeList: POINTER(POINTER(SByte)), AttributesOnly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), PageTimeLimit: UInt32, TotalSizeLimit: UInt32, SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head))) -> POINTER(win32more.Networking.Ldap.LDAPSearch_head): ...
@cfunctype('WLDAP32.dll')
def ldap_search_init_page(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), DistinguishedName: win32more.Foundation.PSTR, ScopeOfSearch: UInt32, SearchFilter: win32more.Foundation.PSTR, AttributeList: POINTER(POINTER(SByte)), AttributesOnly: UInt32, ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), PageTimeLimit: UInt32, TotalSizeLimit: UInt32, SortKeys: POINTER(POINTER(win32more.Networking.Ldap.LDAPSortKeyA_head))) -> POINTER(win32more.Networking.Ldap.LDAPSearch_head): ...
@cfunctype('WLDAP32.dll')
def ldap_get_next_page(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SearchHandle: POINTER(win32more.Networking.Ldap.LDAPSearch_head), PageSize: UInt32, MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_next_page_s(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SearchHandle: POINTER(win32more.Networking.Ldap.LDAPSearch_head), timeout: POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), PageSize: UInt32, TotalCount: POINTER(UInt32), Results: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_paged_count(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SearchBlock: POINTER(win32more.Networking.Ldap.LDAPSearch_head), TotalCount: POINTER(UInt32), Results: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_abandon_page(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), SearchBlock: POINTER(win32more.Networking.Ldap.LDAPSearch_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_vlv_controlW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), VlvInfo: POINTER(win32more.Networking.Ldap.LDAPVLVInfo_head), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_vlv_controlA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), VlvInfo: POINTER(win32more.Networking.Ldap.LDAPVLVInfo_head), IsCritical: Byte, Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_vlv_controlW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), TargetPos: POINTER(UInt32), ListCount: POINTER(UInt32), Context: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), ErrCode: POINTER(Int32)) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_vlv_controlA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Control: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), TargetPos: POINTER(UInt32), ListCount: POINTER(UInt32), Context: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), ErrCode: POINTER(Int32)) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_start_tls_sW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), ServerReturnValue: POINTER(UInt32), result: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_start_tls_sA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), ServerReturnValue: POINTER(UInt32), result: POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_stop_tls_s(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head)) -> win32more.Foundation.BOOLEAN: ...
@cfunctype('WLDAP32.dll')
def ldap_first_reference(ld: POINTER(win32more.Networking.Ldap.LDAP_head), res: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> POINTER(win32more.Networking.Ldap.LDAPMessage_head): ...
@cfunctype('WLDAP32.dll')
def ldap_next_reference(ld: POINTER(win32more.Networking.Ldap.LDAP_head), entry: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> POINTER(win32more.Networking.Ldap.LDAPMessage_head): ...
@cfunctype('WLDAP32.dll')
def ldap_count_references(ld: POINTER(win32more.Networking.Ldap.LDAP_head), res: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_referenceW(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), Referrals: POINTER(POINTER(win32more.Foundation.PWSTR))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_referenceA(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), Referrals: POINTER(POINTER(win32more.Foundation.PSTR))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_reference(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), ResultMessage: POINTER(win32more.Networking.Ldap.LDAPMessage_head), Referrals: POINTER(POINTER(win32more.Foundation.PSTR))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operationW(ld: POINTER(win32more.Networking.Ldap.LDAP_head), Oid: win32more.Foundation.PWSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operationA(ld: POINTER(win32more.Networking.Ldap.LDAP_head), Oid: win32more.Foundation.PSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operation_sA(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Oid: win32more.Foundation.PSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ReturnedOid: POINTER(win32more.Foundation.PSTR), ReturnedData: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operation_sW(ExternalHandle: POINTER(win32more.Networking.Ldap.LDAP_head), Oid: win32more.Foundation.PWSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlW_head)), ReturnedOid: POINTER(win32more.Foundation.PWSTR), ReturnedData: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operation(ld: POINTER(win32more.Networking.Ldap.LDAP_head), Oid: win32more.Foundation.PSTR, Data: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), ServerControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), ClientControls: POINTER(POINTER(win32more.Networking.Ldap.LDAPControlA_head)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_close_extended_op(ld: POINTER(win32more.Networking.Ldap.LDAP_head), MessageNumber: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def LdapGetLastError() -> UInt32: ...
@cfunctype('WLDAP32.dll')
def LdapMapErrorToWin32(LdapError: win32more.Networking.Ldap.LDAP_RETCODE) -> win32more.Foundation.WIN32_ERROR: ...
@cfunctype('WLDAP32.dll')
def ldap_conn_from_msg(PrimaryConn: POINTER(win32more.Networking.Ldap.LDAP_head), res: POINTER(win32more.Networking.Ldap.LDAPMessage_head)) -> POINTER(win32more.Networking.Ldap.LDAP_head): ...
@cfunctype('WLDAP32.dll')
def ber_init(pBerVal: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)) -> POINTER(win32more.Networking.Ldap.BerElement_head): ...
@cfunctype('WLDAP32.dll')
def ber_free(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), fbuf: Int32) -> Void: ...
@cfunctype('WLDAP32.dll')
def ber_bvecfree(pBerVal: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> Void: ...
@cfunctype('WLDAP32.dll')
def ber_bvdup(pBerVal: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)) -> POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head): ...
@cfunctype('WLDAP32.dll')
def ber_alloc_t(options: Int32) -> POINTER(win32more.Networking.Ldap.BerElement_head): ...
@cfunctype('WLDAP32.dll')
def ber_skip_tag(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), pLen: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_peek_tag(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), pLen: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_first_element(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), pLen: POINTER(UInt32), ppOpaque: POINTER(POINTER(win32more.Foundation.CHAR))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_next_element(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), pLen: POINTER(UInt32), opaque: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_flatten(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), pBerVal: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ber_printf(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), fmt: win32more.Foundation.PSTR) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ber_scanf(pBerElement: POINTER(win32more.Networking.Ldap.BerElement_head), fmt: win32more.Foundation.PSTR) -> UInt32: ...
class BerElement(Structure):
    opaque: win32more.Foundation.PSTR
@cfunctype_pointer
def DBGPRINT(Format: win32more.Foundation.PSTR) -> UInt32: ...
@cfunctype_pointer
def DEREFERENCECONNECTION(PrimaryConnection: POINTER(win32more.Networking.Ldap.LDAP_head), ConnectionToDereference: POINTER(win32more.Networking.Ldap.LDAP_head)) -> UInt32: ...
class LDAP(Structure):
    ld_sb: _ld_sb_e__Struct
    ld_host: win32more.Foundation.PSTR
    ld_version: UInt32
    ld_lberoptions: Byte
    ld_deref: UInt32
    ld_timelimit: UInt32
    ld_sizelimit: UInt32
    ld_errno: UInt32
    ld_matched: win32more.Foundation.PSTR
    ld_error: win32more.Foundation.PSTR
    ld_msgid: UInt32
    Reserved3: Byte * 25
    ld_cldaptries: UInt32
    ld_cldaptimeout: UInt32
    ld_refhoplimit: UInt32
    ld_options: UInt32
    class _ld_sb_e__Struct(Structure):
        sb_sd: UIntPtr
        Reserved1: Byte * 41
        sb_naddr: UIntPtr
        Reserved2: Byte * 24
class LDAPAPIFeatureInfoA(Structure):
    ldapaif_info_version: Int32
    ldapaif_name: win32more.Foundation.PSTR
    ldapaif_version: Int32
class LDAPAPIFeatureInfoW(Structure):
    ldapaif_info_version: Int32
    ldapaif_name: win32more.Foundation.PWSTR
    ldapaif_version: Int32
class LDAPAPIInfoA(Structure):
    ldapai_info_version: Int32
    ldapai_api_version: Int32
    ldapai_protocol_version: Int32
    ldapai_extensions: POINTER(POINTER(SByte))
    ldapai_vendor_name: win32more.Foundation.PSTR
    ldapai_vendor_version: Int32
class LDAPAPIInfoW(Structure):
    ldapai_info_version: Int32
    ldapai_api_version: Int32
    ldapai_protocol_version: Int32
    ldapai_extensions: POINTER(win32more.Foundation.PWSTR)
    ldapai_vendor_name: win32more.Foundation.PWSTR
    ldapai_vendor_version: Int32
class LDAPControlA(Structure):
    ldctl_oid: win32more.Foundation.PSTR
    ldctl_value: win32more.Networking.Ldap.LDAP_BERVAL
    ldctl_iscritical: win32more.Foundation.BOOLEAN
class LDAPControlW(Structure):
    ldctl_oid: win32more.Foundation.PWSTR
    ldctl_value: win32more.Networking.Ldap.LDAP_BERVAL
    ldctl_iscritical: win32more.Foundation.BOOLEAN
class LDAPMessage(Structure):
    lm_msgid: UInt32
    lm_msgtype: UInt32
    lm_ber: c_void_p
    lm_chain: POINTER(win32more.Networking.Ldap.LDAPMessage_head)
    lm_next: POINTER(win32more.Networking.Ldap.LDAPMessage_head)
    lm_time: UInt32
    Connection: POINTER(win32more.Networking.Ldap.LDAP_head)
    Request: c_void_p
    lm_returncode: UInt32
    lm_referral: UInt16
    lm_chased: win32more.Foundation.BOOLEAN
    lm_eom: win32more.Foundation.BOOLEAN
    ConnectionReferenced: win32more.Foundation.BOOLEAN
class LDAPModA(Structure):
    mod_op: UInt32
    mod_type: win32more.Foundation.PSTR
    mod_vals: _mod_vals_e__Union
    class _mod_vals_e__Union(Union):
        modv_strvals: POINTER(win32more.Foundation.PSTR)
        modv_bvals: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))
class LDAPModW(Structure):
    mod_op: UInt32
    mod_type: win32more.Foundation.PWSTR
    mod_vals: _mod_vals_e__Union
    class _mod_vals_e__Union(Union):
        modv_strvals: POINTER(win32more.Foundation.PWSTR)
        modv_bvals: POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))
class LDAPSearch(Structure):
    pass
class LDAPSortKeyA(Structure):
    sk_attrtype: win32more.Foundation.PSTR
    sk_matchruleoid: win32more.Foundation.PSTR
    sk_reverseorder: win32more.Foundation.BOOLEAN
class LDAPSortKeyW(Structure):
    sk_attrtype: win32more.Foundation.PWSTR
    sk_matchruleoid: win32more.Foundation.PWSTR
    sk_reverseorder: win32more.Foundation.BOOLEAN
class LDAPVLVInfo(Structure):
    ldvlv_version: Int32
    ldvlv_before_count: UInt32
    ldvlv_after_count: UInt32
    ldvlv_offset: UInt32
    ldvlv_count: UInt32
    ldvlv_attrvalue: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)
    ldvlv_context: POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)
    ldvlv_extradata: c_void_p
class LDAP_BERVAL(Structure):
    bv_len: UInt32
    bv_val: win32more.Foundation.PSTR
class LDAP_REFERRAL_CALLBACK(Structure):
    SizeOfCallbacks: UInt32
    QueryForConnection: win32more.Networking.Ldap.QUERYFORCONNECTION
    NotifyRoutine: win32more.Networking.Ldap.NOTIFYOFNEWCONNECTION
    DereferenceRoutine: win32more.Networking.Ldap.DEREFERENCECONNECTION
LDAP_RETCODE = Int32
LDAP_SUCCESS: LDAP_RETCODE = 0
LDAP_OPERATIONS_ERROR: LDAP_RETCODE = 1
LDAP_PROTOCOL_ERROR: LDAP_RETCODE = 2
LDAP_TIMELIMIT_EXCEEDED: LDAP_RETCODE = 3
LDAP_SIZELIMIT_EXCEEDED: LDAP_RETCODE = 4
LDAP_COMPARE_FALSE: LDAP_RETCODE = 5
LDAP_COMPARE_TRUE: LDAP_RETCODE = 6
LDAP_AUTH_METHOD_NOT_SUPPORTED: LDAP_RETCODE = 7
LDAP_STRONG_AUTH_REQUIRED: LDAP_RETCODE = 8
LDAP_REFERRAL_V2: LDAP_RETCODE = 9
LDAP_PARTIAL_RESULTS: LDAP_RETCODE = 9
LDAP_REFERRAL: LDAP_RETCODE = 10
LDAP_ADMIN_LIMIT_EXCEEDED: LDAP_RETCODE = 11
LDAP_UNAVAILABLE_CRIT_EXTENSION: LDAP_RETCODE = 12
LDAP_CONFIDENTIALITY_REQUIRED: LDAP_RETCODE = 13
LDAP_SASL_BIND_IN_PROGRESS: LDAP_RETCODE = 14
LDAP_NO_SUCH_ATTRIBUTE: LDAP_RETCODE = 16
LDAP_UNDEFINED_TYPE: LDAP_RETCODE = 17
LDAP_INAPPROPRIATE_MATCHING: LDAP_RETCODE = 18
LDAP_CONSTRAINT_VIOLATION: LDAP_RETCODE = 19
LDAP_ATTRIBUTE_OR_VALUE_EXISTS: LDAP_RETCODE = 20
LDAP_INVALID_SYNTAX: LDAP_RETCODE = 21
LDAP_NO_SUCH_OBJECT: LDAP_RETCODE = 32
LDAP_ALIAS_PROBLEM: LDAP_RETCODE = 33
LDAP_INVALID_DN_SYNTAX: LDAP_RETCODE = 34
LDAP_IS_LEAF: LDAP_RETCODE = 35
LDAP_ALIAS_DEREF_PROBLEM: LDAP_RETCODE = 36
LDAP_INAPPROPRIATE_AUTH: LDAP_RETCODE = 48
LDAP_INVALID_CREDENTIALS: LDAP_RETCODE = 49
LDAP_INSUFFICIENT_RIGHTS: LDAP_RETCODE = 50
LDAP_BUSY: LDAP_RETCODE = 51
LDAP_UNAVAILABLE: LDAP_RETCODE = 52
LDAP_UNWILLING_TO_PERFORM: LDAP_RETCODE = 53
LDAP_LOOP_DETECT: LDAP_RETCODE = 54
LDAP_SORT_CONTROL_MISSING: LDAP_RETCODE = 60
LDAP_OFFSET_RANGE_ERROR: LDAP_RETCODE = 61
LDAP_NAMING_VIOLATION: LDAP_RETCODE = 64
LDAP_OBJECT_CLASS_VIOLATION: LDAP_RETCODE = 65
LDAP_NOT_ALLOWED_ON_NONLEAF: LDAP_RETCODE = 66
LDAP_NOT_ALLOWED_ON_RDN: LDAP_RETCODE = 67
LDAP_ALREADY_EXISTS: LDAP_RETCODE = 68
LDAP_NO_OBJECT_CLASS_MODS: LDAP_RETCODE = 69
LDAP_RESULTS_TOO_LARGE: LDAP_RETCODE = 70
LDAP_AFFECTS_MULTIPLE_DSAS: LDAP_RETCODE = 71
LDAP_VIRTUAL_LIST_VIEW_ERROR: LDAP_RETCODE = 76
LDAP_OTHER: LDAP_RETCODE = 80
LDAP_SERVER_DOWN: LDAP_RETCODE = 81
LDAP_LOCAL_ERROR: LDAP_RETCODE = 82
LDAP_ENCODING_ERROR: LDAP_RETCODE = 83
LDAP_DECODING_ERROR: LDAP_RETCODE = 84
LDAP_TIMEOUT: LDAP_RETCODE = 85
LDAP_AUTH_UNKNOWN: LDAP_RETCODE = 86
LDAP_FILTER_ERROR: LDAP_RETCODE = 87
LDAP_USER_CANCELLED: LDAP_RETCODE = 88
LDAP_PARAM_ERROR: LDAP_RETCODE = 89
LDAP_NO_MEMORY: LDAP_RETCODE = 90
LDAP_CONNECT_ERROR: LDAP_RETCODE = 91
LDAP_NOT_SUPPORTED: LDAP_RETCODE = 92
LDAP_NO_RESULTS_RETURNED: LDAP_RETCODE = 94
LDAP_CONTROL_NOT_FOUND: LDAP_RETCODE = 93
LDAP_MORE_RESULTS_TO_RETURN: LDAP_RETCODE = 95
LDAP_CLIENT_LOOP: LDAP_RETCODE = 96
LDAP_REFERRAL_LIMIT_EXCEEDED: LDAP_RETCODE = 97
class LDAP_TIMEVAL(Structure):
    tv_sec: Int32
    tv_usec: Int32
class LDAP_VERSION_INFO(Structure):
    lv_size: UInt32
    lv_major: UInt32
    lv_minor: UInt32
@cfunctype_pointer
def NOTIFYOFNEWCONNECTION(PrimaryConnection: POINTER(win32more.Networking.Ldap.LDAP_head), ReferralFromConnection: POINTER(win32more.Networking.Ldap.LDAP_head), NewDN: win32more.Foundation.PWSTR, HostName: win32more.Foundation.PSTR, NewConnection: POINTER(win32more.Networking.Ldap.LDAP_head), PortNumber: UInt32, SecAuthIdentity: c_void_p, CurrentUser: c_void_p, ErrorCodeFromBind: UInt32) -> win32more.Foundation.BOOLEAN: ...
@cfunctype_pointer
def QUERYCLIENTCERT(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), trusted_CAs: POINTER(win32more.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head), ppCertificate: POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))) -> win32more.Foundation.BOOLEAN: ...
@cfunctype_pointer
def QUERYFORCONNECTION(PrimaryConnection: POINTER(win32more.Networking.Ldap.LDAP_head), ReferralFromConnection: POINTER(win32more.Networking.Ldap.LDAP_head), NewDN: win32more.Foundation.PWSTR, HostName: win32more.Foundation.PSTR, PortNumber: UInt32, SecAuthIdentity: c_void_p, CurrentUserToken: c_void_p, ConnectionToUse: POINTER(POINTER(win32more.Networking.Ldap.LDAP_head))) -> UInt32: ...
@cfunctype_pointer
def VERIFYSERVERCERT(Connection: POINTER(win32more.Networking.Ldap.LDAP_head), pServerCert: POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))) -> win32more.Foundation.BOOLEAN: ...
make_head(_module, 'BerElement')
make_head(_module, 'DBGPRINT')
make_head(_module, 'DEREFERENCECONNECTION')
make_head(_module, 'LDAP')
make_head(_module, 'LDAPAPIFeatureInfoA')
make_head(_module, 'LDAPAPIFeatureInfoW')
make_head(_module, 'LDAPAPIInfoA')
make_head(_module, 'LDAPAPIInfoW')
make_head(_module, 'LDAPControlA')
make_head(_module, 'LDAPControlW')
make_head(_module, 'LDAPMessage')
make_head(_module, 'LDAPModA')
make_head(_module, 'LDAPModW')
make_head(_module, 'LDAPSearch')
make_head(_module, 'LDAPSortKeyA')
make_head(_module, 'LDAPSortKeyW')
make_head(_module, 'LDAPVLVInfo')
make_head(_module, 'LDAP_BERVAL')
make_head(_module, 'LDAP_REFERRAL_CALLBACK')
make_head(_module, 'LDAP_TIMEVAL')
make_head(_module, 'LDAP_VERSION_INFO')
make_head(_module, 'NOTIFYOFNEWCONNECTION')
make_head(_module, 'QUERYCLIENTCERT')
make_head(_module, 'QUERYFORCONNECTION')
make_head(_module, 'VERIFYSERVERCERT')
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
_arch_optional = [
]
