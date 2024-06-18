from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.Ldap
import win32more.Windows.Win32.Security.Authentication.Identity
import win32more.Windows.Win32.Security.Cryptography
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
LDAP_OPT_CLDAP_TIMEOUT: UInt32 = 69
LDAP_OPT_CLDAP_TRIES: UInt32 = 70
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
def ldap_openW(HostName: win32more.Windows.Win32.Foundation.PWSTR, PortNumber: UInt32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
ldap_open = UnicodeAlias('ldap_openW')
@cfunctype('WLDAP32.dll')
def ldap_openA(HostName: win32more.Windows.Win32.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
@cfunctype('WLDAP32.dll')
def ldap_initW(HostName: win32more.Windows.Win32.Foundation.PWSTR, PortNumber: UInt32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
ldap_init = UnicodeAlias('ldap_initW')
@cfunctype('WLDAP32.dll')
def ldap_initA(HostName: win32more.Windows.Win32.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
@cfunctype('WLDAP32.dll')
def ldap_sslinitW(HostName: win32more.Windows.Win32.Foundation.PWSTR, PortNumber: UInt32, secure: Int32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
ldap_sslinit = UnicodeAlias('ldap_sslinitW')
@cfunctype('WLDAP32.dll')
def ldap_sslinitA(HostName: win32more.Windows.Win32.Foundation.PSTR, PortNumber: UInt32, secure: Int32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
@cfunctype('WLDAP32.dll')
def ldap_connect(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), timeout: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_TIMEVAL)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def cldap_openW(HostName: win32more.Windows.Win32.Foundation.PWSTR, PortNumber: UInt32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
cldap_open = UnicodeAlias('cldap_openW')
@cfunctype('WLDAP32.dll')
def cldap_openA(HostName: win32more.Windows.Win32.Foundation.PSTR, PortNumber: UInt32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
@cfunctype('WLDAP32.dll')
def ldap_unbind(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_unbind_s(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_optionW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), option: Int32, outvalue: VoidPtr) -> UInt32: ...
ldap_get_option = UnicodeAlias('ldap_get_optionW')
@cfunctype('WLDAP32.dll')
def ldap_set_optionW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), option: Int32, invalue: VoidPtr) -> UInt32: ...
ldap_set_option = UnicodeAlias('ldap_set_optionW')
@cfunctype('WLDAP32.dll')
def ldap_simple_bindW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, passwd: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_simple_bind = UnicodeAlias('ldap_simple_bindW')
@cfunctype('WLDAP32.dll')
def ldap_simple_bindA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, passwd: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_simple_bind_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, passwd: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_simple_bind_s = UnicodeAlias('ldap_simple_bind_sW')
@cfunctype('WLDAP32.dll')
def ldap_simple_bind_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, passwd: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bindW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, cred: win32more.Windows.Win32.Foundation.PWSTR, method: UInt32) -> UInt32: ...
ldap_bind = UnicodeAlias('ldap_bindW')
@cfunctype('WLDAP32.dll')
def ldap_bindA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, cred: win32more.Windows.Win32.Foundation.PSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_bind_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, cred: win32more.Windows.Win32.Foundation.PWSTR, method: UInt32) -> UInt32: ...
ldap_bind_s = UnicodeAlias('ldap_bind_sW')
@cfunctype('WLDAP32.dll')
def ldap_bind_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, cred: win32more.Windows.Win32.Foundation.PSTR, method: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_sasl_bindA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistName: win32more.Windows.Win32.Foundation.PSTR, AuthMechanism: win32more.Windows.Win32.Foundation.PSTR, cred: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), MessageNumber: POINTER(Int32)) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_sasl_bindW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistName: win32more.Windows.Win32.Foundation.PWSTR, AuthMechanism: win32more.Windows.Win32.Foundation.PWSTR, cred: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), MessageNumber: POINTER(Int32)) -> Int32: ...
ldap_sasl_bind = UnicodeAlias('ldap_sasl_bindW')
@cfunctype('WLDAP32.dll')
def ldap_sasl_bind_sA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistName: win32more.Windows.Win32.Foundation.PSTR, AuthMechanism: win32more.Windows.Win32.Foundation.PSTR, cred: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ServerData: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_sasl_bind_sW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistName: win32more.Windows.Win32.Foundation.PWSTR, AuthMechanism: win32more.Windows.Win32.Foundation.PWSTR, cred: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientCtrls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ServerData: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> Int32: ...
ldap_sasl_bind_s = UnicodeAlias('ldap_sasl_bind_sW')
@cfunctype('WLDAP32.dll')
def ldap_searchW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PWSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32) -> UInt32: ...
ldap_search = UnicodeAlias('ldap_searchW')
@cfunctype('WLDAP32.dll')
def ldap_searchA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PWSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, res: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
ldap_search_s = UnicodeAlias('ldap_search_sW')
@cfunctype('WLDAP32.dll')
def ldap_search_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, res: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_stW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PWSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, timeout: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_TIMEVAL), res: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
ldap_search_st = UnicodeAlias('ldap_search_stW')
@cfunctype('WLDAP32.dll')
def ldap_search_stA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, timeout: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_TIMEVAL), res: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_extW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PWSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), TimeLimit: UInt32, SizeLimit: UInt32, MessageNumber: POINTER(UInt32)) -> UInt32: ...
ldap_search_ext = UnicodeAlias('ldap_search_extW')
@cfunctype('WLDAP32.dll')
def ldap_search_extA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), TimeLimit: UInt32, SizeLimit: UInt32, MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_ext_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PWSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(UInt16)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), timeout: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_TIMEVAL), SizeLimit: UInt32, res: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
ldap_search_ext_s = UnicodeAlias('ldap_search_ext_sW')
@cfunctype('WLDAP32.dll')
def ldap_search_ext_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), base: win32more.Windows.Win32.Foundation.PSTR, scope: UInt32, filter: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(SByte)), attrsonly: UInt32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), timeout: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_TIMEVAL), SizeLimit: UInt32, res: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_check_filterW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SearchFilter: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_check_filter = UnicodeAlias('ldap_check_filterW')
@cfunctype('WLDAP32.dll')
def ldap_check_filterA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SearchFilter: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modifyW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW))) -> UInt32: ...
ldap_modify = UnicodeAlias('ldap_modifyW')
@cfunctype('WLDAP32.dll')
def ldap_modifyA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW))) -> UInt32: ...
ldap_modify_s = UnicodeAlias('ldap_modify_sW')
@cfunctype('WLDAP32.dll')
def ldap_modify_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_extW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
ldap_modify_ext = UnicodeAlias('ldap_modify_extW')
@cfunctype('WLDAP32.dll')
def ldap_modify_extA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modify_ext_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_modify_ext_s = UnicodeAlias('ldap_modify_ext_sW')
@cfunctype('WLDAP32.dll')
def ldap_modify_ext_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, mods: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2W(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PWSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PWSTR, DeleteOldRdn: Int32) -> UInt32: ...
ldap_modrdn2 = UnicodeAlias('ldap_modrdn2W')
@cfunctype('WLDAP32.dll')
def ldap_modrdn2A(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdnW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PWSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_modrdn = UnicodeAlias('ldap_modrdnW')
@cfunctype('WLDAP32.dll')
def ldap_modrdnA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn2_sW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PWSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PWSTR, DeleteOldRdn: Int32) -> UInt32: ...
ldap_modrdn2_s = UnicodeAlias('ldap_modrdn2_sW')
@cfunctype('WLDAP32.dll')
def ldap_modrdn2_sA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PSTR, DeleteOldRdn: Int32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_modrdn_sW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PWSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_modrdn_s = UnicodeAlias('ldap_modrdn_sW')
@cfunctype('WLDAP32.dll')
def ldap_modrdn_sA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PSTR, NewDistinguishedName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_extW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, NewRDN: win32more.Windows.Win32.Foundation.PWSTR, NewParent: win32more.Windows.Win32.Foundation.PWSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
ldap_rename_ext = UnicodeAlias('ldap_rename_extW')
@cfunctype('WLDAP32.dll')
def ldap_rename_extA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, NewRDN: win32more.Windows.Win32.Foundation.PSTR, NewParent: win32more.Windows.Win32.Foundation.PSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_rename_ext_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, NewRDN: win32more.Windows.Win32.Foundation.PWSTR, NewParent: win32more.Windows.Win32.Foundation.PWSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_rename_ext_s = UnicodeAlias('ldap_rename_ext_sW')
@cfunctype('WLDAP32.dll')
def ldap_rename_ext_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, NewRDN: win32more.Windows.Win32.Foundation.PSTR, NewParent: win32more.Windows.Win32.Foundation.PSTR, DeleteOldRdn: Int32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_addW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW))) -> UInt32: ...
ldap_add = UnicodeAlias('ldap_addW')
@cfunctype('WLDAP32.dll')
def ldap_addA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW))) -> UInt32: ...
ldap_add_s = UnicodeAlias('ldap_add_sW')
@cfunctype('WLDAP32.dll')
def ldap_add_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_extW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
ldap_add_ext = UnicodeAlias('ldap_add_extW')
@cfunctype('WLDAP32.dll')
def ldap_add_extA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_add_ext_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModW)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_add_ext_s = UnicodeAlias('ldap_add_ext_sW')
@cfunctype('WLDAP32.dll')
def ldap_add_ext_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, attrs: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPModA)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compareW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, attr: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_compare = UnicodeAlias('ldap_compareW')
@cfunctype('WLDAP32.dll')
def ldap_compareA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, attr: win32more.Windows.Win32.Foundation.PSTR, value: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, attr: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_compare_s = UnicodeAlias('ldap_compare_sW')
@cfunctype('WLDAP32.dll')
def ldap_compare_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, attr: win32more.Windows.Win32.Foundation.PSTR, value: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_extW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, Attr: win32more.Windows.Win32.Foundation.PWSTR, Value: win32more.Windows.Win32.Foundation.PWSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
ldap_compare_ext = UnicodeAlias('ldap_compare_extW')
@cfunctype('WLDAP32.dll')
def ldap_compare_extA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, Attr: win32more.Windows.Win32.Foundation.PSTR, Value: win32more.Windows.Win32.Foundation.PSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_compare_ext_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, Attr: win32more.Windows.Win32.Foundation.PWSTR, Value: win32more.Windows.Win32.Foundation.PWSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_compare_ext_s = UnicodeAlias('ldap_compare_ext_sW')
@cfunctype('WLDAP32.dll')
def ldap_compare_ext_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, Attr: win32more.Windows.Win32.Foundation.PSTR, Value: win32more.Windows.Win32.Foundation.PSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_deleteW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_delete = UnicodeAlias('ldap_deleteW')
@cfunctype('WLDAP32.dll')
def ldap_deleteA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
ldap_delete_s = UnicodeAlias('ldap_delete_sW')
@cfunctype('WLDAP32.dll')
def ldap_delete_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_extW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
ldap_delete_ext = UnicodeAlias('ldap_delete_extW')
@cfunctype('WLDAP32.dll')
def ldap_delete_extA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_delete_ext_sW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PWSTR, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_delete_ext_s = UnicodeAlias('ldap_delete_ext_sW')
@cfunctype('WLDAP32.dll')
def ldap_delete_ext_sA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), dn: win32more.Windows.Win32.Foundation.PSTR, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_abandon(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), msgid: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_result(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), msgid: UInt32, all: UInt32, timeout: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_TIMEVAL), res: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_msgfree(res: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_result2error(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), res: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), freeit: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_resultW(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ResultMessage: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ReturnCode: POINTER(UInt32), MatchedDNs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorMessage: POINTER(win32more.Windows.Win32.Foundation.PWSTR), Referrals: POINTER(POINTER(POINTER(UInt16))), ServerControls: POINTER(POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))), Freeit: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
ldap_parse_result = UnicodeAlias('ldap_parse_resultW')
@cfunctype('WLDAP32.dll')
def ldap_parse_resultA(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ResultMessage: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ReturnCode: POINTER(UInt32), MatchedDNs: POINTER(win32more.Windows.Win32.Foundation.PSTR), ErrorMessage: POINTER(win32more.Windows.Win32.Foundation.PSTR), Referrals: POINTER(POINTER(POINTER(SByte))), ServerControls: POINTER(POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))), Freeit: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_extended_resultA(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ResultMessage: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ResultOID: POINTER(win32more.Windows.Win32.Foundation.PSTR), ResultData: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)), Freeit: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_extended_resultW(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ResultMessage: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ResultOID: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ResultData: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)), Freeit: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
ldap_parse_extended_result = UnicodeAlias('ldap_parse_extended_resultW')
@cfunctype('WLDAP32.dll')
def ldap_controls_freeA(Controls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_control_freeA(Controls: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_controls_freeW(Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_controls_free = UnicodeAlias('ldap_controls_freeW')
@cfunctype('WLDAP32.dll')
def ldap_control_freeW(Control: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)) -> UInt32: ...
ldap_control_free = UnicodeAlias('ldap_control_freeW')
@cfunctype('WLDAP32.dll')
def ldap_free_controlsW(Controls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_free_controls = UnicodeAlias('ldap_free_controlsW')
@cfunctype('WLDAP32.dll')
def ldap_free_controlsA(Controls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_err2stringW(err: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
ldap_err2string = UnicodeAlias('ldap_err2stringW')
@cfunctype('WLDAP32.dll')
def ldap_err2stringA(err: UInt32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_perror(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), msg: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@cfunctype('WLDAP32.dll')
def ldap_first_entry(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), res: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage): ...
@cfunctype('WLDAP32.dll')
def ldap_next_entry(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage): ...
@cfunctype('WLDAP32.dll')
def ldap_count_entries(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), res: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_first_attributeW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ptr: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement))) -> win32more.Windows.Win32.Foundation.PWSTR: ...
ldap_first_attribute = UnicodeAlias('ldap_first_attributeW')
@cfunctype('WLDAP32.dll')
def ldap_first_attributeA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ptr: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement))) -> win32more.Windows.Win32.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_next_attributeW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ptr: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement)) -> win32more.Windows.Win32.Foundation.PWSTR: ...
ldap_next_attribute = UnicodeAlias('ldap_next_attributeW')
@cfunctype('WLDAP32.dll')
def ldap_next_attributeA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), ptr: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement)) -> win32more.Windows.Win32.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_get_valuesW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), attr: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(win32more.Windows.Win32.Foundation.PWSTR): ...
ldap_get_values = UnicodeAlias('ldap_get_valuesW')
@cfunctype('WLDAP32.dll')
def ldap_get_valuesA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), attr: win32more.Windows.Win32.Foundation.PSTR) -> POINTER(win32more.Windows.Win32.Foundation.PSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_get_values_lenW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Message: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), attr: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)): ...
ldap_get_values_len = UnicodeAlias('ldap_get_values_lenW')
@cfunctype('WLDAP32.dll')
def ldap_get_values_lenA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Message: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), attr: win32more.Windows.Win32.Foundation.PSTR) -> POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)): ...
@cfunctype('WLDAP32.dll')
def ldap_count_valuesW(vals: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
ldap_count_values = UnicodeAlias('ldap_count_valuesW')
@cfunctype('WLDAP32.dll')
def ldap_count_valuesA(vals: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_count_values_len(vals: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_value_freeW(vals: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
ldap_value_free = UnicodeAlias('ldap_value_freeW')
@cfunctype('WLDAP32.dll')
def ldap_value_freeA(vals: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_value_free_len(vals: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_dnW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> win32more.Windows.Win32.Foundation.PWSTR: ...
ldap_get_dn = UnicodeAlias('ldap_get_dnW')
@cfunctype('WLDAP32.dll')
def ldap_get_dnA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> win32more.Windows.Win32.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_explode_dnW(dn: win32more.Windows.Win32.Foundation.PWSTR, notypes: UInt32) -> POINTER(win32more.Windows.Win32.Foundation.PWSTR): ...
ldap_explode_dn = UnicodeAlias('ldap_explode_dnW')
@cfunctype('WLDAP32.dll')
def ldap_explode_dnA(dn: win32more.Windows.Win32.Foundation.PSTR, notypes: UInt32) -> POINTER(win32more.Windows.Win32.Foundation.PSTR): ...
@cfunctype('WLDAP32.dll')
def ldap_dn2ufnW(dn: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
ldap_dn2ufn = UnicodeAlias('ldap_dn2ufnW')
@cfunctype('WLDAP32.dll')
def ldap_dn2ufnA(dn: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@cfunctype('WLDAP32.dll')
def ldap_memfreeW(Block: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
ldap_memfree = UnicodeAlias('ldap_memfreeW')
@cfunctype('WLDAP32.dll')
def ldap_memfreeA(Block: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@cfunctype('WLDAP32.dll')
def ber_bvfree(bv: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)) -> Void: ...
@cfunctype('WLDAP32.dll')
def ldap_ufn2dnW(ufn: win32more.Windows.Win32.Foundation.PWSTR, pDn: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
ldap_ufn2dn = UnicodeAlias('ldap_ufn2dnW')
@cfunctype('WLDAP32.dll')
def ldap_ufn2dnA(ufn: win32more.Windows.Win32.Foundation.PSTR, pDn: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_startup(version: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_VERSION_INFO), Instance: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_cleanup(hInstance: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_escape_filter_elementW(sourceFilterElement: win32more.Windows.Win32.Foundation.PSTR, sourceLength: UInt32, destFilterElement: win32more.Windows.Win32.Foundation.PWSTR, destLength: UInt32) -> UInt32: ...
ldap_escape_filter_element = UnicodeAlias('ldap_escape_filter_elementW')
@cfunctype('WLDAP32.dll')
def ldap_escape_filter_elementA(sourceFilterElement: win32more.Windows.Win32.Foundation.PSTR, sourceLength: UInt32, destFilterElement: win32more.Windows.Win32.Foundation.PSTR, destLength: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_set_dbg_flags(NewFlags: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_set_dbg_routine(DebugPrintRoutine: win32more.Windows.Win32.Networking.Ldap.DBGPRINT) -> Void: ...
@cfunctype('WLDAP32.dll')
def LdapUTF8ToUnicode(lpSrcStr: win32more.Windows.Win32.Foundation.PSTR, cchSrc: Int32, lpDestStr: win32more.Windows.Win32.Foundation.PWSTR, cchDest: Int32) -> Int32: ...
@cfunctype('WLDAP32.dll')
def LdapUnicodeToUTF8(lpSrcStr: win32more.Windows.Win32.Foundation.PWSTR, cchSrc: Int32, lpDestStr: win32more.Windows.Win32.Foundation.PSTR, cchDest: Int32) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_sort_controlA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SortKeys: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPSortKeyA)), IsCritical: Byte, Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_sort_controlW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SortKeys: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPSortKeyW)), IsCritical: Byte, Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_create_sort_control = UnicodeAlias('ldap_create_sort_controlW')
@cfunctype('WLDAP32.dll')
def ldap_parse_sort_controlA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), Result: POINTER(UInt32), Attribute: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_sort_controlW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), Result: POINTER(UInt32), Attribute: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
ldap_parse_sort_control = UnicodeAlias('ldap_parse_sort_controlW')
@cfunctype('WLDAP32.dll')
def ldap_encode_sort_controlW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SortKeys: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPSortKeyW)), Control: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW), Criticality: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
ldap_encode_sort_control = UnicodeAlias('ldap_encode_sort_controlW')
@cfunctype('WLDAP32.dll')
def ldap_encode_sort_controlA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SortKeys: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPSortKeyA)), Control: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA), Criticality: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_page_controlW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), PageSize: UInt32, Cookie: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), IsCritical: Byte, Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_create_page_control = UnicodeAlias('ldap_create_page_controlW')
@cfunctype('WLDAP32.dll')
def ldap_create_page_controlA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), PageSize: UInt32, Cookie: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), IsCritical: Byte, Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_page_controlW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), TotalCount: POINTER(UInt32), Cookie: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> UInt32: ...
ldap_parse_page_control = UnicodeAlias('ldap_parse_page_controlW')
@cfunctype('WLDAP32.dll')
def ldap_parse_page_controlA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), TotalCount: POINTER(UInt32), Cookie: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_init_pageW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PWSTR, ScopeOfSearch: UInt32, SearchFilter: win32more.Windows.Win32.Foundation.PWSTR, AttributeList: POINTER(POINTER(UInt16)), AttributesOnly: UInt32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), PageTimeLimit: UInt32, TotalSizeLimit: UInt32, SortKeys: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPSortKeyW))) -> win32more.Windows.Win32.Networking.Ldap.PLDAPSearch: ...
ldap_search_init_page = UnicodeAlias('ldap_search_init_pageW')
@cfunctype('WLDAP32.dll')
def ldap_search_init_pageA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), DistinguishedName: win32more.Windows.Win32.Foundation.PSTR, ScopeOfSearch: UInt32, SearchFilter: win32more.Windows.Win32.Foundation.PSTR, AttributeList: POINTER(POINTER(SByte)), AttributesOnly: UInt32, ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), PageTimeLimit: UInt32, TotalSizeLimit: UInt32, SortKeys: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPSortKeyA))) -> win32more.Windows.Win32.Networking.Ldap.PLDAPSearch: ...
@cfunctype('WLDAP32.dll')
def ldap_get_next_page(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SearchHandle: win32more.Windows.Win32.Networking.Ldap.PLDAPSearch, PageSize: UInt32, MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_next_page_s(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SearchHandle: win32more.Windows.Win32.Networking.Ldap.PLDAPSearch, timeout: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_TIMEVAL), PageSize: UInt32, TotalCount: POINTER(UInt32), Results: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_get_paged_count(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SearchBlock: win32more.Windows.Win32.Networking.Ldap.PLDAPSearch, TotalCount: POINTER(UInt32), Results: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_search_abandon_page(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), SearchBlock: win32more.Windows.Win32.Networking.Ldap.PLDAPSearch) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_create_vlv_controlW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), VlvInfo: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPVLVInfo), IsCritical: Byte, Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> Int32: ...
ldap_create_vlv_control = UnicodeAlias('ldap_create_vlv_controlW')
@cfunctype('WLDAP32.dll')
def ldap_create_vlv_controlA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), VlvInfo: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPVLVInfo), IsCritical: Byte, Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_vlv_controlW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), TargetPos: POINTER(UInt32), ListCount: POINTER(UInt32), Context: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)), ErrCode: POINTER(Int32)) -> Int32: ...
ldap_parse_vlv_control = UnicodeAlias('ldap_parse_vlv_controlW')
@cfunctype('WLDAP32.dll')
def ldap_parse_vlv_controlA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Control: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), TargetPos: POINTER(UInt32), ListCount: POINTER(UInt32), Context: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)), ErrCode: POINTER(Int32)) -> Int32: ...
@cfunctype('WLDAP32.dll')
def ldap_start_tls_sW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ServerReturnValue: POINTER(UInt32), result: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW))) -> UInt32: ...
ldap_start_tls_s = UnicodeAlias('ldap_start_tls_sW')
@cfunctype('WLDAP32.dll')
def ldap_start_tls_sA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ServerReturnValue: POINTER(UInt32), result: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_stop_tls_s(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@cfunctype('WLDAP32.dll')
def ldap_first_reference(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), res: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage): ...
@cfunctype('WLDAP32.dll')
def ldap_next_reference(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), entry: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage): ...
@cfunctype('WLDAP32.dll')
def ldap_count_references(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), res: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_parse_referenceW(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ResultMessage: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), Referrals: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> UInt32: ...
ldap_parse_reference = UnicodeAlias('ldap_parse_referenceW')
@cfunctype('WLDAP32.dll')
def ldap_parse_referenceA(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ResultMessage: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage), Referrals: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSTR))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operationW(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Oid: win32more.Windows.Win32.Foundation.PWSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
ldap_extended_operation = UnicodeAlias('ldap_extended_operationW')
@cfunctype('WLDAP32.dll')
def ldap_extended_operationA(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Oid: win32more.Windows.Win32.Foundation.PSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), MessageNumber: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operation_sA(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Oid: win32more.Windows.Win32.Foundation.PSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlA)), ReturnedOid: POINTER(win32more.Windows.Win32.Foundation.PSTR), ReturnedData: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ldap_extended_operation_sW(ExternalHandle: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), Oid: win32more.Windows.Win32.Foundation.PWSTR, Data: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL), ServerControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ClientControls: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPControlW)), ReturnedOid: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ReturnedData: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> UInt32: ...
ldap_extended_operation_s = UnicodeAlias('ldap_extended_operation_sW')
@cfunctype('WLDAP32.dll')
def ldap_close_extended_op(ld: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), MessageNumber: UInt32) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def LdapGetLastError() -> UInt32: ...
@cfunctype('WLDAP32.dll')
def LdapMapErrorToWin32(LdapError: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@cfunctype('WLDAP32.dll')
def ldap_conn_from_msg(PrimaryConn: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), res: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP): ...
@cfunctype('WLDAP32.dll')
def ber_init(pBerVal: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)) -> POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement): ...
@cfunctype('WLDAP32.dll')
def ber_free(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), fbuf: Int32) -> Void: ...
@cfunctype('WLDAP32.dll')
def ber_bvecfree(pBerVal: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> Void: ...
@cfunctype('WLDAP32.dll')
def ber_bvdup(pBerVal: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)) -> POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL): ...
@cfunctype('WLDAP32.dll')
def ber_alloc_t(options: Int32) -> POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement): ...
@cfunctype('WLDAP32.dll')
def ber_skip_tag(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), pLen: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_peek_tag(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), pLen: POINTER(UInt32)) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_first_element(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), pLen: POINTER(UInt32), ppOpaque: POINTER(POINTER(win32more.Windows.Win32.Foundation.CHAR))) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_next_element(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), pLen: POINTER(UInt32), opaque: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype('WLDAP32.dll')
def ber_flatten(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), pBerVal: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))) -> Int32: ...
@cfunctype('WLDAP32.dll', variadic=True)
def ber_printf(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), fmt: win32more.Windows.Win32.Foundation.PSTR, *__arglist) -> Int32: ...
@cfunctype('WLDAP32.dll', variadic=True)
def ber_scanf(pBerElement: POINTER(win32more.Windows.Win32.Networking.Ldap.BerElement), fmt: win32more.Windows.Win32.Foundation.PSTR, *__arglist) -> UInt32: ...
class BerElement(Structure):
    opaque: win32more.Windows.Win32.Foundation.PSTR
@cfunctype_pointer
def DBGPRINT(Format: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@cfunctype_pointer
def DEREFERENCECONNECTION(PrimaryConnection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ConnectionToDereference: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP)) -> UInt32: ...
class LDAP(Structure):
    ld_sb: _ld_sb_e__Struct
    ld_host: win32more.Windows.Win32.Foundation.PSTR
    ld_version: UInt32
    ld_lberoptions: Byte
    ld_deref: UInt32
    ld_timelimit: UInt32
    ld_sizelimit: UInt32
    ld_errno: UInt32
    ld_matched: win32more.Windows.Win32.Foundation.PSTR
    ld_error: win32more.Windows.Win32.Foundation.PSTR
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
    ldapaif_name: win32more.Windows.Win32.Foundation.PSTR
    ldapaif_version: Int32
class LDAPAPIFeatureInfoW(Structure):
    ldapaif_info_version: Int32
    ldapaif_name: win32more.Windows.Win32.Foundation.PWSTR
    ldapaif_version: Int32
LDAPAPIFeatureInfo = UnicodeAlias('LDAPAPIFeatureInfoW')
class LDAPAPIInfoA(Structure):
    ldapai_info_version: Int32
    ldapai_api_version: Int32
    ldapai_protocol_version: Int32
    ldapai_extensions: POINTER(POINTER(SByte))
    ldapai_vendor_name: win32more.Windows.Win32.Foundation.PSTR
    ldapai_vendor_version: Int32
class LDAPAPIInfoW(Structure):
    ldapai_info_version: Int32
    ldapai_api_version: Int32
    ldapai_protocol_version: Int32
    ldapai_extensions: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    ldapai_vendor_name: win32more.Windows.Win32.Foundation.PWSTR
    ldapai_vendor_version: Int32
LDAPAPIInfo = UnicodeAlias('LDAPAPIInfoW')
class LDAPControlA(Structure):
    ldctl_oid: win32more.Windows.Win32.Foundation.PSTR
    ldctl_value: win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL
    ldctl_iscritical: win32more.Windows.Win32.Foundation.BOOLEAN
class LDAPControlW(Structure):
    ldctl_oid: win32more.Windows.Win32.Foundation.PWSTR
    ldctl_value: win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL
    ldctl_iscritical: win32more.Windows.Win32.Foundation.BOOLEAN
LDAPControl = UnicodeAlias('LDAPControlW')
class LDAPMessage(Structure):
    lm_msgid: UInt32
    lm_msgtype: UInt32
    lm_ber: VoidPtr
    lm_chain: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)
    lm_next: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAPMessage)
    lm_time: UInt32
    Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP)
    Request: VoidPtr
    lm_returncode: UInt32
    lm_referral: UInt16
    lm_chased: win32more.Windows.Win32.Foundation.BOOLEAN
    lm_eom: win32more.Windows.Win32.Foundation.BOOLEAN
    ConnectionReferenced: win32more.Windows.Win32.Foundation.BOOLEAN
class LDAPModA(Structure):
    mod_op: UInt32
    mod_type: win32more.Windows.Win32.Foundation.PSTR
    mod_vals: _mod_vals_e__Union
    class _mod_vals_e__Union(Union):
        modv_strvals: POINTER(win32more.Windows.Win32.Foundation.PSTR)
        modv_bvals: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))
class LDAPModW(Structure):
    mod_op: UInt32
    mod_type: win32more.Windows.Win32.Foundation.PWSTR
    mod_vals: _mod_vals_e__Union
    class _mod_vals_e__Union(Union):
        modv_strvals: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        modv_bvals: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL))
LDAPMod = UnicodeAlias('LDAPModW')
class LDAPSortKeyA(Structure):
    sk_attrtype: win32more.Windows.Win32.Foundation.PSTR
    sk_matchruleoid: win32more.Windows.Win32.Foundation.PSTR
    sk_reverseorder: win32more.Windows.Win32.Foundation.BOOLEAN
class LDAPSortKeyW(Structure):
    sk_attrtype: win32more.Windows.Win32.Foundation.PWSTR
    sk_matchruleoid: win32more.Windows.Win32.Foundation.PWSTR
    sk_reverseorder: win32more.Windows.Win32.Foundation.BOOLEAN
LDAPSortKey = UnicodeAlias('LDAPSortKeyW')
class LDAPVLVInfo(Structure):
    ldvlv_version: Int32
    ldvlv_before_count: UInt32
    ldvlv_after_count: UInt32
    ldvlv_offset: UInt32
    ldvlv_count: UInt32
    ldvlv_attrvalue: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)
    ldvlv_context: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP_BERVAL)
    ldvlv_extradata: VoidPtr
class LDAP_BERVAL(Structure):
    bv_len: UInt32
    bv_val: win32more.Windows.Win32.Foundation.PSTR
class LDAP_REFERRAL_CALLBACK(Structure):
    SizeOfCallbacks: UInt32
    QueryForConnection: win32more.Windows.Win32.Networking.Ldap.QUERYFORCONNECTION
    NotifyRoutine: win32more.Windows.Win32.Networking.Ldap.NOTIFYOFNEWCONNECTION
    DereferenceRoutine: win32more.Windows.Win32.Networking.Ldap.DEREFERENCECONNECTION
LDAP_RETCODE = Int32
LDAP_SUCCESS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 0
LDAP_OPERATIONS_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 1
LDAP_PROTOCOL_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 2
LDAP_TIMELIMIT_EXCEEDED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 3
LDAP_SIZELIMIT_EXCEEDED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 4
LDAP_COMPARE_FALSE: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 5
LDAP_COMPARE_TRUE: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 6
LDAP_AUTH_METHOD_NOT_SUPPORTED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 7
LDAP_STRONG_AUTH_REQUIRED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 8
LDAP_REFERRAL_V2: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 9
LDAP_PARTIAL_RESULTS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 9
LDAP_REFERRAL: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 10
LDAP_ADMIN_LIMIT_EXCEEDED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 11
LDAP_UNAVAILABLE_CRIT_EXTENSION: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 12
LDAP_CONFIDENTIALITY_REQUIRED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 13
LDAP_SASL_BIND_IN_PROGRESS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 14
LDAP_NO_SUCH_ATTRIBUTE: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 16
LDAP_UNDEFINED_TYPE: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 17
LDAP_INAPPROPRIATE_MATCHING: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 18
LDAP_CONSTRAINT_VIOLATION: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 19
LDAP_ATTRIBUTE_OR_VALUE_EXISTS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 20
LDAP_INVALID_SYNTAX: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 21
LDAP_NO_SUCH_OBJECT: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 32
LDAP_ALIAS_PROBLEM: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 33
LDAP_INVALID_DN_SYNTAX: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 34
LDAP_IS_LEAF: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 35
LDAP_ALIAS_DEREF_PROBLEM: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 36
LDAP_INAPPROPRIATE_AUTH: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 48
LDAP_INVALID_CREDENTIALS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 49
LDAP_INSUFFICIENT_RIGHTS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 50
LDAP_BUSY: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 51
LDAP_UNAVAILABLE: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 52
LDAP_UNWILLING_TO_PERFORM: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 53
LDAP_LOOP_DETECT: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 54
LDAP_SORT_CONTROL_MISSING: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 60
LDAP_OFFSET_RANGE_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 61
LDAP_NAMING_VIOLATION: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 64
LDAP_OBJECT_CLASS_VIOLATION: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 65
LDAP_NOT_ALLOWED_ON_NONLEAF: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 66
LDAP_NOT_ALLOWED_ON_RDN: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 67
LDAP_ALREADY_EXISTS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 68
LDAP_NO_OBJECT_CLASS_MODS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 69
LDAP_RESULTS_TOO_LARGE: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 70
LDAP_AFFECTS_MULTIPLE_DSAS: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 71
LDAP_VIRTUAL_LIST_VIEW_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 76
LDAP_OTHER: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 80
LDAP_SERVER_DOWN: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 81
LDAP_LOCAL_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 82
LDAP_ENCODING_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 83
LDAP_DECODING_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 84
LDAP_TIMEOUT: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 85
LDAP_AUTH_UNKNOWN: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 86
LDAP_FILTER_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 87
LDAP_USER_CANCELLED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 88
LDAP_PARAM_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 89
LDAP_NO_MEMORY: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 90
LDAP_CONNECT_ERROR: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 91
LDAP_NOT_SUPPORTED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 92
LDAP_NO_RESULTS_RETURNED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 94
LDAP_CONTROL_NOT_FOUND: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 93
LDAP_MORE_RESULTS_TO_RETURN: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 95
LDAP_CLIENT_LOOP: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 96
LDAP_REFERRAL_LIMIT_EXCEEDED: win32more.Windows.Win32.Networking.Ldap.LDAP_RETCODE = 97
class LDAP_TIMEVAL(Structure):
    tv_sec: Int32
    tv_usec: Int32
class LDAP_VERSION_INFO(Structure):
    lv_size: UInt32
    lv_major: UInt32
    lv_minor: UInt32
@cfunctype_pointer
def NOTIFYOFNEWCONNECTION(PrimaryConnection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ReferralFromConnection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), NewDN: win32more.Windows.Win32.Foundation.PWSTR, HostName: win32more.Windows.Win32.Foundation.PSTR, NewConnection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), PortNumber: UInt32, SecAuthIdentity: VoidPtr, CurrentUser: VoidPtr, ErrorCodeFromBind: UInt32) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
PLDAPSearch = IntPtr
@cfunctype_pointer
def QUERYCLIENTCERT(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), trusted_CAs: POINTER(win32more.Windows.Win32.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx), ppCertificate: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@cfunctype_pointer
def QUERYFORCONNECTION(PrimaryConnection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), ReferralFromConnection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), NewDN: win32more.Windows.Win32.Foundation.PWSTR, HostName: win32more.Windows.Win32.Foundation.PSTR, PortNumber: UInt32, SecAuthIdentity: VoidPtr, CurrentUserToken: VoidPtr, ConnectionToUse: POINTER(POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP))) -> UInt32: ...
@cfunctype_pointer
def VERIFYSERVERCERT(Connection: POINTER(win32more.Windows.Win32.Networking.Ldap.LDAP), pServerCert: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...


make_ready(__name__)
