from win32more.base import *
import win32more.Foundation
import win32more.Networking.Ldap
import win32more.Security.Authentication.Identity
import win32more.Security.Cryptography

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
LDAP_VENDOR_VERSION = 510
LDAP_FEATURE_INFO_VERSION = 1
LDAP_API_FEATURE_VIRTUAL_LIST_VIEW = 1001
LDAP_VLVINFO_VERSION = 1
LDAP_OPT_REFERRAL_CALLBACK = 112
LDAP_OPT_CLIENT_CERTIFICATE = 128
LDAP_OPT_SERVER_CERTIFICATE = 129
LDAP_OPT_REF_DEREF_CONN_PER_MSG = 148
SERVER_SEARCH_FLAG_DOMAIN_SCOPE = 1
SERVER_SEARCH_FLAG_PHANTOM_ROOT = 2
LDAP_DIRSYNC_OBJECT_SECURITY = 1
LDAP_DIRSYNC_ANCESTORS_FIRST_ORDER = 2048
LDAP_DIRSYNC_PUBLIC_DATA_ONLY = 8192
LDAP_DIRSYNC_INCREMENTAL_VALUES = 2147483648
LDAP_DIRSYNC_ROPAS_DATA_ONLY = 1073741824
LDAP_POLICYHINT_APPLY_FULLPWDPOLICY = 1
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
def _define_ldap_head():
    class ldap(Structure):
        pass
    return ldap
def _define_ldap():
    ldap = win32more.Networking.Ldap.ldap_head
    class ldap__ld_sb_e__Struct(Structure):
        pass
    ldap__ld_sb_e__Struct._fields_ = [
        ("sb_sd", UIntPtr),
        ("Reserved1", Byte * 41),
        ("sb_naddr", UIntPtr),
        ("Reserved2", Byte * 24),
    ]
    ldap._fields_ = [
        ("ld_sb", ldap__ld_sb_e__Struct),
        ("ld_host", win32more.Foundation.PSTR),
        ("ld_version", UInt32),
        ("ld_lberoptions", Byte),
        ("ld_deref", UInt32),
        ("ld_timelimit", UInt32),
        ("ld_sizelimit", UInt32),
        ("ld_errno", UInt32),
        ("ld_matched", win32more.Foundation.PSTR),
        ("ld_error", win32more.Foundation.PSTR),
        ("ld_msgid", UInt32),
        ("Reserved3", Byte * 25),
        ("ld_cldaptries", UInt32),
        ("ld_cldaptimeout", UInt32),
        ("ld_refhoplimit", UInt32),
        ("ld_options", UInt32),
    ]
    return ldap
def _define_LDAP_TIMEVAL_head():
    class LDAP_TIMEVAL(Structure):
        pass
    return LDAP_TIMEVAL
def _define_LDAP_TIMEVAL():
    LDAP_TIMEVAL = win32more.Networking.Ldap.LDAP_TIMEVAL_head
    LDAP_TIMEVAL._fields_ = [
        ("tv_sec", Int32),
        ("tv_usec", Int32),
    ]
    return LDAP_TIMEVAL
def _define_LDAP_BERVAL_head():
    class LDAP_BERVAL(Structure):
        pass
    return LDAP_BERVAL
def _define_LDAP_BERVAL():
    LDAP_BERVAL = win32more.Networking.Ldap.LDAP_BERVAL_head
    LDAP_BERVAL._fields_ = [
        ("bv_len", UInt32),
        ("bv_val", win32more.Foundation.PSTR),
    ]
    return LDAP_BERVAL
def _define_LDAPMessage_head():
    class LDAPMessage(Structure):
        pass
    return LDAPMessage
def _define_LDAPMessage():
    LDAPMessage = win32more.Networking.Ldap.LDAPMessage_head
    LDAPMessage._fields_ = [
        ("lm_msgid", UInt32),
        ("lm_msgtype", UInt32),
        ("lm_ber", c_void_p),
        ("lm_chain", POINTER(win32more.Networking.Ldap.LDAPMessage_head)),
        ("lm_next", POINTER(win32more.Networking.Ldap.LDAPMessage_head)),
        ("lm_time", UInt32),
        ("Connection", POINTER(win32more.Networking.Ldap.ldap_head)),
        ("Request", c_void_p),
        ("lm_returncode", UInt32),
        ("lm_referral", UInt16),
        ("lm_chased", win32more.Foundation.BOOLEAN),
        ("lm_eom", win32more.Foundation.BOOLEAN),
        ("ConnectionReferenced", win32more.Foundation.BOOLEAN),
    ]
    return LDAPMessage
def _define_ldapcontrolA_head():
    class ldapcontrolA(Structure):
        pass
    return ldapcontrolA
def _define_ldapcontrolA():
    ldapcontrolA = win32more.Networking.Ldap.ldapcontrolA_head
    ldapcontrolA._fields_ = [
        ("ldctl_oid", win32more.Foundation.PSTR),
        ("ldctl_value", win32more.Networking.Ldap.LDAP_BERVAL),
        ("ldctl_iscritical", win32more.Foundation.BOOLEAN),
    ]
    return ldapcontrolA
def _define_ldapcontrolW_head():
    class ldapcontrolW(Structure):
        pass
    return ldapcontrolW
def _define_ldapcontrolW():
    ldapcontrolW = win32more.Networking.Ldap.ldapcontrolW_head
    ldapcontrolW._fields_ = [
        ("ldctl_oid", win32more.Foundation.PWSTR),
        ("ldctl_value", win32more.Networking.Ldap.LDAP_BERVAL),
        ("ldctl_iscritical", win32more.Foundation.BOOLEAN),
    ]
    return ldapcontrolW
def _define_ldapmodW_head():
    class ldapmodW(Structure):
        pass
    return ldapmodW
def _define_ldapmodW():
    ldapmodW = win32more.Networking.Ldap.ldapmodW_head
    class ldapmodW__mod_vals_e__Union(Union):
        pass
    ldapmodW__mod_vals_e__Union._fields_ = [
        ("modv_strvals", POINTER(win32more.Foundation.PWSTR)),
        ("modv_bvals", POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))),
    ]
    ldapmodW._fields_ = [
        ("mod_op", UInt32),
        ("mod_type", win32more.Foundation.PWSTR),
        ("mod_vals", ldapmodW__mod_vals_e__Union),
    ]
    return ldapmodW
def _define_ldapmodA_head():
    class ldapmodA(Structure):
        pass
    return ldapmodA
def _define_ldapmodA():
    ldapmodA = win32more.Networking.Ldap.ldapmodA_head
    class ldapmodA__mod_vals_e__Union(Union):
        pass
    ldapmodA__mod_vals_e__Union._fields_ = [
        ("modv_strvals", POINTER(win32more.Foundation.PSTR)),
        ("modv_bvals", POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head))),
    ]
    ldapmodA._fields_ = [
        ("mod_op", UInt32),
        ("mod_type", win32more.Foundation.PSTR),
        ("mod_vals", ldapmodA__mod_vals_e__Union),
    ]
    return ldapmodA
def _define_berelement_head():
    class berelement(Structure):
        pass
    return berelement
def _define_berelement():
    berelement = win32more.Networking.Ldap.berelement_head
    berelement._fields_ = [
        ("opaque", win32more.Foundation.PSTR),
    ]
    return berelement
def _define_ldap_version_info_head():
    class ldap_version_info(Structure):
        pass
    return ldap_version_info
def _define_ldap_version_info():
    ldap_version_info = win32more.Networking.Ldap.ldap_version_info_head
    ldap_version_info._fields_ = [
        ("lv_size", UInt32),
        ("lv_major", UInt32),
        ("lv_minor", UInt32),
    ]
    return ldap_version_info
def _define_ldapapiinfoA_head():
    class ldapapiinfoA(Structure):
        pass
    return ldapapiinfoA
def _define_ldapapiinfoA():
    ldapapiinfoA = win32more.Networking.Ldap.ldapapiinfoA_head
    ldapapiinfoA._fields_ = [
        ("ldapai_info_version", Int32),
        ("ldapai_api_version", Int32),
        ("ldapai_protocol_version", Int32),
        ("ldapai_extensions", POINTER(POINTER(SByte))),
        ("ldapai_vendor_name", win32more.Foundation.PSTR),
        ("ldapai_vendor_version", Int32),
    ]
    return ldapapiinfoA
def _define_ldapapiinfoW_head():
    class ldapapiinfoW(Structure):
        pass
    return ldapapiinfoW
def _define_ldapapiinfoW():
    ldapapiinfoW = win32more.Networking.Ldap.ldapapiinfoW_head
    ldapapiinfoW._fields_ = [
        ("ldapai_info_version", Int32),
        ("ldapai_api_version", Int32),
        ("ldapai_protocol_version", Int32),
        ("ldapai_extensions", POINTER(win32more.Foundation.PWSTR)),
        ("ldapai_vendor_name", win32more.Foundation.PWSTR),
        ("ldapai_vendor_version", Int32),
    ]
    return ldapapiinfoW
def _define_LDAPAPIFeatureInfoA_head():
    class LDAPAPIFeatureInfoA(Structure):
        pass
    return LDAPAPIFeatureInfoA
def _define_LDAPAPIFeatureInfoA():
    LDAPAPIFeatureInfoA = win32more.Networking.Ldap.LDAPAPIFeatureInfoA_head
    LDAPAPIFeatureInfoA._fields_ = [
        ("ldapaif_info_version", Int32),
        ("ldapaif_name", win32more.Foundation.PSTR),
        ("ldapaif_version", Int32),
    ]
    return LDAPAPIFeatureInfoA
def _define_LDAPAPIFeatureInfoW_head():
    class LDAPAPIFeatureInfoW(Structure):
        pass
    return LDAPAPIFeatureInfoW
def _define_LDAPAPIFeatureInfoW():
    LDAPAPIFeatureInfoW = win32more.Networking.Ldap.LDAPAPIFeatureInfoW_head
    LDAPAPIFeatureInfoW._fields_ = [
        ("ldapaif_info_version", Int32),
        ("ldapaif_name", win32more.Foundation.PWSTR),
        ("ldapaif_version", Int32),
    ]
    return LDAPAPIFeatureInfoW
def _define_DBGPRINT():
    return CFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)
def _define_ldapsearch_head():
    class ldapsearch(Structure):
        pass
    return ldapsearch
def _define_ldapsearch():
    ldapsearch = win32more.Networking.Ldap.ldapsearch_head
    return ldapsearch
def _define_ldapsortkeyW_head():
    class ldapsortkeyW(Structure):
        pass
    return ldapsortkeyW
def _define_ldapsortkeyW():
    ldapsortkeyW = win32more.Networking.Ldap.ldapsortkeyW_head
    ldapsortkeyW._fields_ = [
        ("sk_attrtype", win32more.Foundation.PWSTR),
        ("sk_matchruleoid", win32more.Foundation.PWSTR),
        ("sk_reverseorder", win32more.Foundation.BOOLEAN),
    ]
    return ldapsortkeyW
def _define_ldapsortkeyA_head():
    class ldapsortkeyA(Structure):
        pass
    return ldapsortkeyA
def _define_ldapsortkeyA():
    ldapsortkeyA = win32more.Networking.Ldap.ldapsortkeyA_head
    ldapsortkeyA._fields_ = [
        ("sk_attrtype", win32more.Foundation.PSTR),
        ("sk_matchruleoid", win32more.Foundation.PSTR),
        ("sk_reverseorder", win32more.Foundation.BOOLEAN),
    ]
    return ldapsortkeyA
def _define_ldapvlvinfo_head():
    class ldapvlvinfo(Structure):
        pass
    return ldapvlvinfo
def _define_ldapvlvinfo():
    ldapvlvinfo = win32more.Networking.Ldap.ldapvlvinfo_head
    ldapvlvinfo._fields_ = [
        ("ldvlv_version", Int32),
        ("ldvlv_before_count", UInt32),
        ("ldvlv_after_count", UInt32),
        ("ldvlv_offset", UInt32),
        ("ldvlv_count", UInt32),
        ("ldvlv_attrvalue", POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),
        ("ldvlv_context", POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),
        ("ldvlv_extradata", c_void_p),
    ]
    return ldapvlvinfo
def _define_QUERYFORCONNECTION():
    return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PSTR,UInt32,c_void_p,c_void_p,POINTER(POINTER(win32more.Networking.Ldap.ldap_head)), use_last_error=False)
def _define_NOTIFYOFNEWCONNECTION():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.ldap_head),UInt32,c_void_p,c_void_p,UInt32, use_last_error=False)
def _define_DEREFERENCECONNECTION():
    return CFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldap_head), use_last_error=False)
def _define_LDAP_REFERRAL_CALLBACK_head():
    class LDAP_REFERRAL_CALLBACK(Structure):
        pass
    return LDAP_REFERRAL_CALLBACK
def _define_LDAP_REFERRAL_CALLBACK():
    LDAP_REFERRAL_CALLBACK = win32more.Networking.Ldap.LDAP_REFERRAL_CALLBACK_head
    LDAP_REFERRAL_CALLBACK._fields_ = [
        ("SizeOfCallbacks", UInt32),
        ("QueryForConnection", win32more.Networking.Ldap.QUERYFORCONNECTION),
        ("NotifyRoutine", win32more.Networking.Ldap.NOTIFYOFNEWCONNECTION),
        ("DereferenceRoutine", win32more.Networking.Ldap.DEREFERENCECONNECTION),
    ]
    return LDAP_REFERRAL_CALLBACK
def _define_QUERYCLIENTCERT():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head),POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)), use_last_error=False)
def _define_VERIFYSERVERCERT():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)), use_last_error=False)
def _define_ldap_openW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ldap_openW", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_openA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_openA", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_initW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ldap_initW", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_initA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_initA", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sslinitW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32,Int32, use_last_error=False)(("ldap_sslinitW", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),(1, 'secure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sslinitA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,Int32, use_last_error=False)(("ldap_sslinitA", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),(1, 'secure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_connect():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head), use_last_error=False)(("ldap_connect", windll["WLDAP32"]), ((1, 'ld'),(1, 'timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_open():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_open", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_init():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_init", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sslinit():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,Int32, use_last_error=False)(("ldap_sslinit", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),(1, 'secure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_cldap_openW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("cldap_openW", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_cldap_openA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32, use_last_error=True)(("cldap_openA", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_cldap_open():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32, use_last_error=True)(("cldap_open", windll["WLDAP32"]), ((1, 'HostName'),(1, 'PortNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_unbind():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head), use_last_error=False)(("ldap_unbind", windll["WLDAP32"]), ((1, 'ld'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_unbind_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head), use_last_error=False)(("ldap_unbind_s", windll["WLDAP32"]), ((1, 'ld'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_option():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),Int32,c_void_p, use_last_error=False)(("ldap_get_option", windll["WLDAP32"]), ((1, 'ld'),(1, 'option'),(1, 'outvalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_optionW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),Int32,c_void_p, use_last_error=False)(("ldap_get_optionW", windll["WLDAP32"]), ((1, 'ld'),(1, 'option'),(1, 'outvalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_option():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),Int32,c_void_p, use_last_error=False)(("ldap_set_option", windll["WLDAP32"]), ((1, 'ld'),(1, 'option'),(1, 'invalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_optionW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),Int32,c_void_p, use_last_error=False)(("ldap_set_optionW", windll["WLDAP32"]), ((1, 'ld'),(1, 'option'),(1, 'invalue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bindW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_simple_bindW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bindA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_simple_bindA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bind_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_simple_bind_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bind_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_simple_bind_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bindW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ldap_bindW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bindA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_bindA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ldap_bind_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_bind_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bindA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(Int32), use_last_error=False)(("ldap_sasl_bindA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bindW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(Int32), use_last_error=False)(("ldap_sasl_bindW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bind():
    return win32more.Networking.Ldap.ldap_sasl_bindW
def _define_ldap_sasl_bind_sA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_sasl_bind_sA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'ServerData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bind_sW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_sasl_bind_sW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistName'),(1, 'AuthMechanism'),(1, 'cred'),(1, 'ServerCtrls'),(1, 'ClientCtrls'),(1, 'ServerData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_sasl_bind_s():
    return win32more.Networking.Ldap.ldap_sasl_bind_sW
def _define_ldap_simple_bind():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_simple_bind", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_simple_bind_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_simple_bind_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'passwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_bind", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_bind_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_bind_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'cred'),(1, 'method'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_searchW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32, use_last_error=False)(("ldap_searchW", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_searchA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32, use_last_error=False)(("ldap_searchA", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_stW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_stW", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_stA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_stA", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_extW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("ldap_search_extW", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'TimeLimit'),(1, 'SizeLimit'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_extA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("ldap_search_extA", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'TimeLimit'),(1, 'SizeLimit'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_ext_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'timeout'),(1, 'SizeLimit'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_ext_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'timeout'),(1, 'SizeLimit'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32, use_last_error=False)(("ldap_search", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_st():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_st", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("ldap_search_ext", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'TimeLimit'),(1, 'SizeLimit'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_ext_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_search_ext_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'base'),(1, 'scope'),(1, 'filter'),(1, 'attrs'),(1, 'attrsonly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'timeout'),(1, 'SizeLimit'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_check_filterW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR, use_last_error=False)(("ldap_check_filterW", windll["WLDAP32"]), ((1, 'ld'),(1, 'SearchFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_check_filter():
    return win32more.Networking.Ldap.ldap_check_filterW
def _define_ldap_check_filterA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_check_filterA", windll["WLDAP32"]), ((1, 'ld'),(1, 'SearchFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modifyW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)), use_last_error=False)(("ldap_modifyW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modifyA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_modifyA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)), use_last_error=False)(("ldap_modify_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_modify_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_extW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32), use_last_error=False)(("ldap_modify_extW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_extA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_modify_extA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_modify_ext_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_modify_ext_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_modify", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_modify_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_modify_ext", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modify_ext_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_modify_ext_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'mods'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2W():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32, use_last_error=False)(("ldap_modrdn2W", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2A():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("ldap_modrdn2A", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdnW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_modrdnW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdnA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_modrdnA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32, use_last_error=False)(("ldap_modrdn2_sW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("ldap_modrdn2_sA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_modrdn_sW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_modrdn_sA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("ldap_modrdn2", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_modrdn", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn2_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("ldap_modrdn2_s", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),(1, 'DeleteOldRdn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_modrdn_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_modrdn_s", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'NewDistinguishedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_extW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32), use_last_error=False)(("ldap_rename_extW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_extA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_rename_extA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_rename_ext_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_rename_ext_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_rename_ext", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_rename_ext_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_rename_ext_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'NewRDN'),(1, 'NewParent'),(1, 'DeleteOldRdn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_addW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)), use_last_error=False)(("ldap_addW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_addA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_addA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)), use_last_error=False)(("ldap_add_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_add_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_extW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32), use_last_error=False)(("ldap_add_extW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_extA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_add_extA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_add_ext_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_add_ext_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_add", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)), use_last_error=False)(("ldap_add_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_add_ext", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_add_ext_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapmodA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_add_ext_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attrs'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compareW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_compareW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compareA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_compareA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_compare_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_compare_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_compare", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_compare_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'attr'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_extW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32), use_last_error=False)(("ldap_compare_extW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_extA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_compare_extA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_compare_ext_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_compare_ext_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_compare_ext", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_compare_ext_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_compare_ext_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'Attr'),(1, 'Value'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_deleteW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR, use_last_error=False)(("ldap_deleteW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_deleteA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_deleteA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR, use_last_error=False)(("ldap_delete_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_delete_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_extW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32), use_last_error=False)(("ldap_delete_extW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_extA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_delete_extA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_delete_ext_sW", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_delete_ext_sA", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_delete", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_delete_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_delete_ext", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_delete_ext_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_delete_ext_s", windll["WLDAP32"]), ((1, 'ld'),(1, 'dn'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_abandon():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),UInt32, use_last_error=False)(("ldap_abandon", windll["WLDAP32"]), ((1, 'ld'),(1, 'msgid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_result():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),UInt32,UInt32,POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_result", windll["WLDAP32"]), ((1, 'ld'),(1, 'msgid'),(1, 'all'),(1, 'timeout'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_msgfree():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_msgfree", windll["WLDAP32"]), ((1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_result2error():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),UInt32, use_last_error=False)(("ldap_result2error", windll["WLDAP32"]), ((1, 'ld'),(1, 'res'),(1, 'freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_resultW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(POINTER(UInt16))),POINTER(POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head))),win32more.Foundation.BOOLEAN, use_last_error=False)(("ldap_parse_resultW", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ReturnCode'),(1, 'MatchedDNs'),(1, 'ErrorMessage'),(1, 'Referrals'),(1, 'ServerControls'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_resultA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(UInt32),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(POINTER(SByte))),POINTER(POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head))),win32more.Foundation.BOOLEAN, use_last_error=False)(("ldap_parse_resultA", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ReturnCode'),(1, 'MatchedDNs'),(1, 'ErrorMessage'),(1, 'Referrals'),(1, 'ServerControls'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_extended_resultA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),win32more.Foundation.BOOLEAN, use_last_error=False)(("ldap_parse_extended_resultA", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ResultOID'),(1, 'ResultData'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_extended_resultW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),win32more.Foundation.BOOLEAN, use_last_error=False)(("ldap_parse_extended_resultW", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ResultOID'),(1, 'ResultData'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_extended_result():
    return win32more.Networking.Ldap.ldap_parse_extended_resultW
def _define_ldap_controls_freeA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_controls_freeA", windll["WLDAP32"]), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_control_freeA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldapcontrolA_head), use_last_error=False)(("ldap_control_freeA", windll["WLDAP32"]), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_controls_freeW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_controls_freeW", windll["WLDAP32"]), ((1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_control_freeW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldapcontrolW_head), use_last_error=False)(("ldap_control_freeW", windll["WLDAP32"]), ((1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_free_controlsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_free_controlsW", windll["WLDAP32"]), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_free_controlsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_free_controlsA", windll["WLDAP32"]), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_result():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(UInt32),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(win32more.Foundation.PSTR)),POINTER(POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head))),win32more.Foundation.BOOLEAN, use_last_error=False)(("ldap_parse_result", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'ReturnCode'),(1, 'MatchedDNs'),(1, 'ErrorMessage'),(1, 'Referrals'),(1, 'ServerControls'),(1, 'Freeit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_controls_free():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_controls_free", windll["WLDAP32"]), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_control_free():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldapcontrolA_head), use_last_error=False)(("ldap_control_free", windll["WLDAP32"]), ((1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_free_controls():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_free_controls", windll["WLDAP32"]), ((1, 'Controls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_err2stringW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ldap_err2stringW", windll["WLDAP32"]), ((1, 'err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_err2stringA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_err2stringA", windll["WLDAP32"]), ((1, 'err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_err2string():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_err2string", windll["WLDAP32"]), ((1, 'err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_perror():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_perror", windll["WLDAP32"]), ((1, 'ld'),(1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_entry():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_first_entry", windll["WLDAP32"]), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_entry():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_next_entry", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_entries():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_count_entries", windll["WLDAP32"]), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_attributeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Networking.Ldap.berelement_head)), use_last_error=False)(("ldap_first_attributeW", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_attributeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Networking.Ldap.berelement_head)), use_last_error=False)(("ldap_first_attributeA", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_attribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Networking.Ldap.berelement_head)), use_last_error=False)(("ldap_first_attribute", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_attributeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.berelement_head), use_last_error=False)(("ldap_next_attributeW", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_attributeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.berelement_head), use_last_error=False)(("ldap_next_attributeA", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_attribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.berelement_head), use_last_error=False)(("ldap_next_attribute", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'ptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_valuesW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PWSTR, use_last_error=False)(("ldap_get_valuesW", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_valuesA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Foundation.PSTR),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_get_valuesA", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values():
    try:
        return WINFUNCTYPE(POINTER(win32more.Foundation.PSTR),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_get_values", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values_lenW():
    try:
        return WINFUNCTYPE(POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PWSTR, use_last_error=False)(("ldap_get_values_lenW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Message'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values_lenA():
    try:
        return WINFUNCTYPE(POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_get_values_lenA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Message'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_values_len():
    try:
        return WINFUNCTYPE(POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),win32more.Foundation.PSTR, use_last_error=False)(("ldap_get_values_len", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Message'),(1, 'attr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_valuesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ldap_count_valuesW", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_valuesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_count_valuesA", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_values():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_count_values", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_values_len():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_count_values_len", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_freeW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ldap_value_freeW", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_freeA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_value_freeA", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_free():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_value_free", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_value_free_len():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_value_free_len", windll["WLDAP32"]), ((1, 'vals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_dnW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_get_dnW", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_dnA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_get_dnA", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_dn():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_get_dn", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_explode_dnW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Foundation.PWSTR),win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ldap_explode_dnW", windll["WLDAP32"]), ((1, 'dn'),(1, 'notypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_explode_dnA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Foundation.PSTR),win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_explode_dnA", windll["WLDAP32"]), ((1, 'dn'),(1, 'notypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_explode_dn():
    try:
        return WINFUNCTYPE(POINTER(win32more.Foundation.PSTR),win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_explode_dn", windll["WLDAP32"]), ((1, 'dn'),(1, 'notypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_dn2ufnW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_dn2ufnW", windll["WLDAP32"]), ((1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_dn2ufnA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_dn2ufnA", windll["WLDAP32"]), ((1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_dn2ufn():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ldap_dn2ufn", windll["WLDAP32"]), ((1, 'dn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_memfreeW():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PWSTR, use_last_error=False)(("ldap_memfreeW", windll["WLDAP32"]), ((1, 'Block'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_memfreeA():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PSTR, use_last_error=False)(("ldap_memfreeA", windll["WLDAP32"]), ((1, 'Block'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_bvfree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), use_last_error=False)(("ber_bvfree", windll["WLDAP32"]), ((1, 'bv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_memfree():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PSTR, use_last_error=False)(("ldap_memfree", windll["WLDAP32"]), ((1, 'Block'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_ufn2dnW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ldap_ufn2dnW", windll["WLDAP32"]), ((1, 'ufn'),(1, 'pDn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_ufn2dnA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_ufn2dnA", windll["WLDAP32"]), ((1, 'ufn'),(1, 'pDn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_ufn2dn():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_ufn2dn", windll["WLDAP32"]), ((1, 'ufn'),(1, 'pDn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_startup():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_version_info_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("ldap_startup", windll["WLDAP32"]), ((1, 'version'),(1, 'Instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_cleanup():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("ldap_cleanup", windll["WLDAP32"]), ((1, 'hInstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_escape_filter_elementW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ldap_escape_filter_elementW", windll["WLDAP32"]), ((1, 'sourceFilterElement'),(1, 'sourceLength'),(1, 'destFilterElement'),(1, 'destLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_escape_filter_elementA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_escape_filter_elementA", windll["WLDAP32"]), ((1, 'sourceFilterElement'),(1, 'sourceLength'),(1, 'destFilterElement'),(1, 'destLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_escape_filter_element():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ldap_escape_filter_element", windll["WLDAP32"]), ((1, 'sourceFilterElement'),(1, 'sourceLength'),(1, 'destFilterElement'),(1, 'destLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_dbg_flags():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("ldap_set_dbg_flags", windll["WLDAP32"]), ((1, 'NewFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_set_dbg_routine():
    try:
        return WINFUNCTYPE(Void,win32more.Networking.Ldap.DBGPRINT, use_last_error=False)(("ldap_set_dbg_routine", windll["WLDAP32"]), ((1, 'DebugPrintRoutine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapUTF8ToUnicode():
    try:
        return WINFUNCTYPE(Int32,POINTER(Byte),Int32,POINTER(Char),Int32, use_last_error=True)(("LdapUTF8ToUnicode", windll["WLDAP32"]), ((1, 'lpSrcStr'),(1, 'cchSrc'),(1, 'lpDestStr'),(1, 'cchDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapUnicodeToUTF8():
    try:
        return WINFUNCTYPE(Int32,POINTER(Char),Int32,POINTER(Byte),Int32, use_last_error=True)(("LdapUnicodeToUTF8", windll["WLDAP32"]), ((1, 'lpSrcStr'),(1, 'cchSrc'),(1, 'lpDestStr'),(1, 'cchDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_sort_controlA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyA_head)),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_create_sort_controlA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_sort_controlW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyW_head)),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_create_sort_controlW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_sort_controlA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32),POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_parse_sort_controlA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'Result'),(1, 'Attribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_sort_controlW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ldap_parse_sort_controlW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'Result'),(1, 'Attribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_sort_control():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyA_head)),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_create_sort_control", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_sort_control():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32),POINTER(win32more.Foundation.PSTR), use_last_error=False)(("ldap_parse_sort_control", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'Result'),(1, 'Attribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_encode_sort_controlW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyW_head)),POINTER(win32more.Networking.Ldap.ldapcontrolW_head),win32more.Foundation.BOOLEAN, use_last_error=False)(("ldap_encode_sort_controlW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'Control'),(1, 'Criticality'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_encode_sort_control():
    return win32more.Networking.Ldap.ldap_encode_sort_controlW
def _define_ldap_encode_sort_controlA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyA_head)),POINTER(win32more.Networking.Ldap.ldapcontrolA_head),win32more.Foundation.BOOLEAN, use_last_error=False)(("ldap_encode_sort_controlA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SortKeys'),(1, 'Control'),(1, 'Criticality'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_page_controlW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),UInt32,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_create_page_controlW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'PageSize'),(1, 'Cookie'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_page_controlA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),UInt32,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_create_page_controlA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'PageSize'),(1, 'Cookie'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_page_controlW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_parse_page_controlW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'ServerControls'),(1, 'TotalCount'),(1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_page_controlA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_parse_page_controlA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'ServerControls'),(1, 'TotalCount'),(1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_page_control():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),UInt32,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_create_page_control", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'PageSize'),(1, 'Cookie'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_page_control():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_parse_page_control", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'ServerControls'),(1, 'TotalCount'),(1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_init_pageW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldapsearch_head),POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),UInt32,UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyW_head)), use_last_error=True)(("ldap_search_init_pageW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'ScopeOfSearch'),(1, 'SearchFilter'),(1, 'AttributeList'),(1, 'AttributesOnly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'PageTimeLimit'),(1, 'TotalSizeLimit'),(1, 'SortKeys'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_init_pageA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldapsearch_head),POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),UInt32,UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyA_head)), use_last_error=True)(("ldap_search_init_pageA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'ScopeOfSearch'),(1, 'SearchFilter'),(1, 'AttributeList'),(1, 'AttributesOnly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'PageTimeLimit'),(1, 'TotalSizeLimit'),(1, 'SortKeys'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_init_page():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldapsearch_head),POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),UInt32,UInt32,POINTER(POINTER(win32more.Networking.Ldap.ldapsortkeyA_head)), use_last_error=True)(("ldap_search_init_page", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'DistinguishedName'),(1, 'ScopeOfSearch'),(1, 'SearchFilter'),(1, 'AttributeList'),(1, 'AttributesOnly'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'PageTimeLimit'),(1, 'TotalSizeLimit'),(1, 'SortKeys'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_next_page():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldapsearch_head),UInt32,POINTER(UInt32), use_last_error=False)(("ldap_get_next_page", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SearchHandle'),(1, 'PageSize'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_next_page_s():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldapsearch_head),POINTER(win32more.Networking.Ldap.LDAP_TIMEVAL_head),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)), use_last_error=False)(("ldap_get_next_page_s", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SearchHandle'),(1, 'timeout'),(1, 'PageSize'),(1, 'TotalCount'),(1, 'Results'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_get_paged_count():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldapsearch_head),POINTER(UInt32),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_get_paged_count", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SearchBlock'),(1, 'TotalCount'),(1, 'Results'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_search_abandon_page():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldapsearch_head), use_last_error=False)(("ldap_search_abandon_page", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'SearchBlock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_vlv_controlW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldapvlvinfo_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_create_vlv_controlW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'VlvInfo'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_create_vlv_control():
    return win32more.Networking.Ldap.ldap_create_vlv_controlW
def _define_ldap_create_vlv_controlA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldapvlvinfo_head),Byte,POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_create_vlv_controlA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'VlvInfo'),(1, 'IsCritical'),(1, 'Control'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_vlv_controlW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(Int32), use_last_error=False)(("ldap_parse_vlv_controlW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'TargetPos'),(1, 'ListCount'),(1, 'Context'),(1, 'ErrCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_vlv_control():
    return win32more.Networking.Ldap.ldap_parse_vlv_controlW
def _define_ldap_parse_vlv_controlA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)),POINTER(Int32), use_last_error=False)(("ldap_parse_vlv_controlA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Control'),(1, 'TargetPos'),(1, 'ListCount'),(1, 'Context'),(1, 'ErrCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_start_tls_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)), use_last_error=False)(("ldap_start_tls_sW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'ServerReturnValue'),(1, 'result'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_start_tls_s():
    return win32more.Networking.Ldap.ldap_start_tls_sW
def _define_ldap_start_tls_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(UInt32),POINTER(POINTER(win32more.Networking.Ldap.LDAPMessage_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)), use_last_error=False)(("ldap_start_tls_sA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'ServerReturnValue'),(1, 'result'),(1, 'ServerControls'),(1, 'ClientControls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_stop_tls_s():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Networking.Ldap.ldap_head), use_last_error=False)(("ldap_stop_tls_s", windll["WLDAP32"]), ((1, 'ExternalHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_first_reference():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_first_reference", windll["WLDAP32"]), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_next_reference():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_next_reference", windll["WLDAP32"]), ((1, 'ld'),(1, 'entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_count_references():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_count_references", windll["WLDAP32"]), ((1, 'ld'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_referenceW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Foundation.PWSTR)), use_last_error=False)(("ldap_parse_referenceW", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'Referrals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_referenceA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Foundation.PSTR)), use_last_error=False)(("ldap_parse_referenceA", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'Referrals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_parse_reference():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head),POINTER(POINTER(win32more.Foundation.PSTR)), use_last_error=False)(("ldap_parse_reference", windll["WLDAP32"]), ((1, 'Connection'),(1, 'ResultMessage'),(1, 'Referrals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operationW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(UInt32), use_last_error=False)(("ldap_extended_operationW", windll["WLDAP32"]), ((1, 'ld'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operationA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_extended_operationA", windll["WLDAP32"]), ((1, 'ld'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operation_sA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(win32more.Foundation.PSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_extended_operation_sA", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'ReturnedOid'),(1, 'ReturnedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operation_sW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PWSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolW_head)),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ldap_extended_operation_sW", windll["WLDAP32"]), ((1, 'ExternalHandle'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'ReturnedOid'),(1, 'ReturnedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_extended_operation_s():
    return win32more.Networking.Ldap.ldap_extended_operation_sW
def _define_ldap_extended_operation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),win32more.Foundation.PSTR,POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(POINTER(win32more.Networking.Ldap.ldapcontrolA_head)),POINTER(UInt32), use_last_error=False)(("ldap_extended_operation", windll["WLDAP32"]), ((1, 'ld'),(1, 'Oid'),(1, 'Data'),(1, 'ServerControls'),(1, 'ClientControls'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_close_extended_op():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.ldap_head),UInt32, use_last_error=False)(("ldap_close_extended_op", windll["WLDAP32"]), ((1, 'ld'),(1, 'MessageNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapGetLastError():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("LdapGetLastError", windll["WLDAP32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_LdapMapErrorToWin32():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("LdapMapErrorToWin32", windll["WLDAP32"]), ((1, 'LdapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ldap_conn_from_msg():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.ldap_head),POINTER(win32more.Networking.Ldap.LDAPMessage_head), use_last_error=False)(("ldap_conn_from_msg", windll["WLDAP32"]), ((1, 'PrimaryConn'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_init():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.berelement_head),POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), use_last_error=False)(("ber_init", windll["WLDAP32"]), ((1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_free():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.Ldap.berelement_head),Int32, use_last_error=False)(("ber_free", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'fbuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_bvecfree():
    try:
        return WINFUNCTYPE(Void,POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ber_bvecfree", windll["WLDAP32"]), ((1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_bvdup():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head),POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head), use_last_error=False)(("ber_bvdup", windll["WLDAP32"]), ((1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_alloc_t():
    try:
        return WINFUNCTYPE(POINTER(win32more.Networking.Ldap.berelement_head),Int32, use_last_error=False)(("ber_alloc_t", windll["WLDAP32"]), ((1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_skip_tag():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.berelement_head),POINTER(UInt32), use_last_error=False)(("ber_skip_tag", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'pLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_peek_tag():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.berelement_head),POINTER(UInt32), use_last_error=False)(("ber_peek_tag", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'pLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_first_element():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.berelement_head),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.CHAR)), use_last_error=False)(("ber_first_element", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'pLen'),(1, 'ppOpaque'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_next_element():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.berelement_head),POINTER(UInt32),win32more.Foundation.PSTR, use_last_error=False)(("ber_next_element", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'pLen'),(1, 'opaque'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_flatten():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.berelement_head),POINTER(POINTER(win32more.Networking.Ldap.LDAP_BERVAL_head)), use_last_error=False)(("ber_flatten", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'pBerVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_printf():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Networking.Ldap.berelement_head),win32more.Foundation.PSTR, use_last_error=False)(("ber_printf", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'fmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ber_scanf():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.Ldap.berelement_head),win32more.Foundation.PSTR, use_last_error=False)(("ber_scanf", windll["WLDAP32"]), ((1, 'pBerElement'),(1, 'fmt'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "LBER_ERROR",
    "LBER_DEFAULT",
    "LDAP_UNICODE",
    "LDAP_PORT",
    "LDAP_SSL_PORT",
    "LDAP_GC_PORT",
    "LDAP_SSL_GC_PORT",
    "LDAP_VERSION1",
    "LDAP_VERSION2",
    "LDAP_VERSION3",
    "LDAP_VERSION",
    "LDAP_BIND_CMD",
    "LDAP_UNBIND_CMD",
    "LDAP_SEARCH_CMD",
    "LDAP_MODIFY_CMD",
    "LDAP_ADD_CMD",
    "LDAP_DELETE_CMD",
    "LDAP_MODRDN_CMD",
    "LDAP_COMPARE_CMD",
    "LDAP_ABANDON_CMD",
    "LDAP_SESSION_CMD",
    "LDAP_EXTENDED_CMD",
    "LDAP_RES_BIND",
    "LDAP_RES_SEARCH_ENTRY",
    "LDAP_RES_SEARCH_RESULT",
    "LDAP_RES_MODIFY",
    "LDAP_RES_ADD",
    "LDAP_RES_DELETE",
    "LDAP_RES_MODRDN",
    "LDAP_RES_COMPARE",
    "LDAP_RES_SESSION",
    "LDAP_RES_REFERRAL",
    "LDAP_RES_EXTENDED",
    "LDAP_RES_ANY",
    "LDAP_INVALID_CMD",
    "LDAP_INVALID_RES",
    "LDAP_AUTH_SIMPLE",
    "LDAP_AUTH_SASL",
    "LDAP_AUTH_OTHERKIND",
    "LDAP_FILTER_AND",
    "LDAP_FILTER_OR",
    "LDAP_FILTER_NOT",
    "LDAP_FILTER_EQUALITY",
    "LDAP_FILTER_SUBSTRINGS",
    "LDAP_FILTER_GE",
    "LDAP_FILTER_LE",
    "LDAP_FILTER_PRESENT",
    "LDAP_FILTER_APPROX",
    "LDAP_FILTER_EXTENSIBLE",
    "LDAP_SUBSTRING_INITIAL",
    "LDAP_SUBSTRING_ANY",
    "LDAP_SUBSTRING_FINAL",
    "LDAP_DEREF_NEVER",
    "LDAP_DEREF_SEARCHING",
    "LDAP_DEREF_FINDING",
    "LDAP_DEREF_ALWAYS",
    "LDAP_NO_LIMIT",
    "LDAP_OPT_DNS",
    "LDAP_OPT_CHASE_REFERRALS",
    "LDAP_OPT_RETURN_REFS",
    "LDAP_MOD_ADD",
    "LDAP_MOD_DELETE",
    "LDAP_MOD_REPLACE",
    "LDAP_MOD_BVALUES",
    "LDAP_OPT_API_INFO",
    "LDAP_OPT_DESC",
    "LDAP_OPT_DEREF",
    "LDAP_OPT_SIZELIMIT",
    "LDAP_OPT_TIMELIMIT",
    "LDAP_OPT_THREAD_FN_PTRS",
    "LDAP_OPT_REBIND_FN",
    "LDAP_OPT_REBIND_ARG",
    "LDAP_OPT_REFERRALS",
    "LDAP_OPT_RESTART",
    "LDAP_OPT_SSL",
    "LDAP_OPT_IO_FN_PTRS",
    "LDAP_OPT_CACHE_FN_PTRS",
    "LDAP_OPT_CACHE_STRATEGY",
    "LDAP_OPT_CACHE_ENABLE",
    "LDAP_OPT_REFERRAL_HOP_LIMIT",
    "LDAP_OPT_PROTOCOL_VERSION",
    "LDAP_OPT_VERSION",
    "LDAP_OPT_API_FEATURE_INFO",
    "LDAP_OPT_HOST_NAME",
    "LDAP_OPT_ERROR_NUMBER",
    "LDAP_OPT_ERROR_STRING",
    "LDAP_OPT_SERVER_ERROR",
    "LDAP_OPT_SERVER_EXT_ERROR",
    "LDAP_OPT_HOST_REACHABLE",
    "LDAP_OPT_PING_KEEP_ALIVE",
    "LDAP_OPT_PING_WAIT_TIME",
    "LDAP_OPT_PING_LIMIT",
    "LDAP_OPT_DNSDOMAIN_NAME",
    "LDAP_OPT_GETDSNAME_FLAGS",
    "LDAP_OPT_PROMPT_CREDENTIALS",
    "LDAP_OPT_AUTO_RECONNECT",
    "LDAP_OPT_SSPI_FLAGS",
    "LDAP_OPT_SSL_INFO",
    "LDAP_OPT_TLS",
    "LDAP_OPT_TLS_INFO",
    "LDAP_OPT_SIGN",
    "LDAP_OPT_ENCRYPT",
    "LDAP_OPT_SASL_METHOD",
    "LDAP_OPT_AREC_EXCLUSIVE",
    "LDAP_OPT_SECURITY_CONTEXT",
    "LDAP_OPT_ROOTDSE_CACHE",
    "LDAP_OPT_TCP_KEEPALIVE",
    "LDAP_OPT_FAST_CONCURRENT_BIND",
    "LDAP_OPT_SEND_TIMEOUT",
    "LDAP_OPT_SCH_FLAGS",
    "LDAP_OPT_SOCKET_BIND_ADDRESSES",
    "LDAP_CHASE_SUBORDINATE_REFERRALS",
    "LDAP_CHASE_EXTERNAL_REFERRALS",
    "LDAP_SCOPE_BASE",
    "LDAP_SCOPE_ONELEVEL",
    "LDAP_SCOPE_SUBTREE",
    "LDAP_MSG_ONE",
    "LDAP_MSG_ALL",
    "LDAP_MSG_RECEIVED",
    "LBER_USE_DER",
    "LBER_USE_INDEFINITE_LEN",
    "LBER_TRANSLATE_STRINGS",
    "LAPI_MAJOR_VER1",
    "LAPI_MINOR_VER1",
    "LDAP_API_INFO_VERSION",
    "LDAP_API_VERSION",
    "LDAP_VERSION_MIN",
    "LDAP_VERSION_MAX",
    "LDAP_VENDOR_VERSION",
    "LDAP_FEATURE_INFO_VERSION",
    "LDAP_API_FEATURE_VIRTUAL_LIST_VIEW",
    "LDAP_VLVINFO_VERSION",
    "LDAP_OPT_REFERRAL_CALLBACK",
    "LDAP_OPT_CLIENT_CERTIFICATE",
    "LDAP_OPT_SERVER_CERTIFICATE",
    "LDAP_OPT_REF_DEREF_CONN_PER_MSG",
    "SERVER_SEARCH_FLAG_DOMAIN_SCOPE",
    "SERVER_SEARCH_FLAG_PHANTOM_ROOT",
    "LDAP_DIRSYNC_OBJECT_SECURITY",
    "LDAP_DIRSYNC_ANCESTORS_FIRST_ORDER",
    "LDAP_DIRSYNC_PUBLIC_DATA_ONLY",
    "LDAP_DIRSYNC_INCREMENTAL_VALUES",
    "LDAP_DIRSYNC_ROPAS_DATA_ONLY",
    "LDAP_POLICYHINT_APPLY_FULLPWDPOLICY",
    "LDAP_RETCODE",
    "LDAP_SUCCESS",
    "LDAP_OPERATIONS_ERROR",
    "LDAP_PROTOCOL_ERROR",
    "LDAP_TIMELIMIT_EXCEEDED",
    "LDAP_SIZELIMIT_EXCEEDED",
    "LDAP_COMPARE_FALSE",
    "LDAP_COMPARE_TRUE",
    "LDAP_AUTH_METHOD_NOT_SUPPORTED",
    "LDAP_STRONG_AUTH_REQUIRED",
    "LDAP_REFERRAL_V2",
    "LDAP_PARTIAL_RESULTS",
    "LDAP_REFERRAL",
    "LDAP_ADMIN_LIMIT_EXCEEDED",
    "LDAP_UNAVAILABLE_CRIT_EXTENSION",
    "LDAP_CONFIDENTIALITY_REQUIRED",
    "LDAP_SASL_BIND_IN_PROGRESS",
    "LDAP_NO_SUCH_ATTRIBUTE",
    "LDAP_UNDEFINED_TYPE",
    "LDAP_INAPPROPRIATE_MATCHING",
    "LDAP_CONSTRAINT_VIOLATION",
    "LDAP_ATTRIBUTE_OR_VALUE_EXISTS",
    "LDAP_INVALID_SYNTAX",
    "LDAP_NO_SUCH_OBJECT",
    "LDAP_ALIAS_PROBLEM",
    "LDAP_INVALID_DN_SYNTAX",
    "LDAP_IS_LEAF",
    "LDAP_ALIAS_DEREF_PROBLEM",
    "LDAP_INAPPROPRIATE_AUTH",
    "LDAP_INVALID_CREDENTIALS",
    "LDAP_INSUFFICIENT_RIGHTS",
    "LDAP_BUSY",
    "LDAP_UNAVAILABLE",
    "LDAP_UNWILLING_TO_PERFORM",
    "LDAP_LOOP_DETECT",
    "LDAP_SORT_CONTROL_MISSING",
    "LDAP_OFFSET_RANGE_ERROR",
    "LDAP_NAMING_VIOLATION",
    "LDAP_OBJECT_CLASS_VIOLATION",
    "LDAP_NOT_ALLOWED_ON_NONLEAF",
    "LDAP_NOT_ALLOWED_ON_RDN",
    "LDAP_ALREADY_EXISTS",
    "LDAP_NO_OBJECT_CLASS_MODS",
    "LDAP_RESULTS_TOO_LARGE",
    "LDAP_AFFECTS_MULTIPLE_DSAS",
    "LDAP_VIRTUAL_LIST_VIEW_ERROR",
    "LDAP_OTHER",
    "LDAP_SERVER_DOWN",
    "LDAP_LOCAL_ERROR",
    "LDAP_ENCODING_ERROR",
    "LDAP_DECODING_ERROR",
    "LDAP_TIMEOUT",
    "LDAP_AUTH_UNKNOWN",
    "LDAP_FILTER_ERROR",
    "LDAP_USER_CANCELLED",
    "LDAP_PARAM_ERROR",
    "LDAP_NO_MEMORY",
    "LDAP_CONNECT_ERROR",
    "LDAP_NOT_SUPPORTED",
    "LDAP_NO_RESULTS_RETURNED",
    "LDAP_CONTROL_NOT_FOUND",
    "LDAP_MORE_RESULTS_TO_RETURN",
    "LDAP_CLIENT_LOOP",
    "LDAP_REFERRAL_LIMIT_EXCEEDED",
    "ldap",
    "LDAP_TIMEVAL",
    "LDAP_BERVAL",
    "LDAPMessage",
    "ldapcontrolA",
    "ldapcontrolW",
    "ldapmodW",
    "ldapmodA",
    "berelement",
    "ldap_version_info",
    "ldapapiinfoA",
    "ldapapiinfoW",
    "LDAPAPIFeatureInfoA",
    "LDAPAPIFeatureInfoW",
    "DBGPRINT",
    "ldapsearch",
    "ldapsortkeyW",
    "ldapsortkeyA",
    "ldapvlvinfo",
    "QUERYFORCONNECTION",
    "NOTIFYOFNEWCONNECTION",
    "DEREFERENCECONNECTION",
    "LDAP_REFERRAL_CALLBACK",
    "QUERYCLIENTCERT",
    "VERIFYSERVERCERT",
    "ldap_openW",
    "ldap_openA",
    "ldap_initW",
    "ldap_initA",
    "ldap_sslinitW",
    "ldap_sslinitA",
    "ldap_connect",
    "ldap_open",
    "ldap_init",
    "ldap_sslinit",
    "cldap_openW",
    "cldap_openA",
    "cldap_open",
    "ldap_unbind",
    "ldap_unbind_s",
    "ldap_get_option",
    "ldap_get_optionW",
    "ldap_set_option",
    "ldap_set_optionW",
    "ldap_simple_bindW",
    "ldap_simple_bindA",
    "ldap_simple_bind_sW",
    "ldap_simple_bind_sA",
    "ldap_bindW",
    "ldap_bindA",
    "ldap_bind_sW",
    "ldap_bind_sA",
    "ldap_sasl_bindA",
    "ldap_sasl_bindW",
    "ldap_sasl_bind",
    "ldap_sasl_bind_sA",
    "ldap_sasl_bind_sW",
    "ldap_sasl_bind_s",
    "ldap_simple_bind",
    "ldap_simple_bind_s",
    "ldap_bind",
    "ldap_bind_s",
    "ldap_searchW",
    "ldap_searchA",
    "ldap_search_sW",
    "ldap_search_sA",
    "ldap_search_stW",
    "ldap_search_stA",
    "ldap_search_extW",
    "ldap_search_extA",
    "ldap_search_ext_sW",
    "ldap_search_ext_sA",
    "ldap_search",
    "ldap_search_s",
    "ldap_search_st",
    "ldap_search_ext",
    "ldap_search_ext_s",
    "ldap_check_filterW",
    "ldap_check_filter",
    "ldap_check_filterA",
    "ldap_modifyW",
    "ldap_modifyA",
    "ldap_modify_sW",
    "ldap_modify_sA",
    "ldap_modify_extW",
    "ldap_modify_extA",
    "ldap_modify_ext_sW",
    "ldap_modify_ext_sA",
    "ldap_modify",
    "ldap_modify_s",
    "ldap_modify_ext",
    "ldap_modify_ext_s",
    "ldap_modrdn2W",
    "ldap_modrdn2A",
    "ldap_modrdnW",
    "ldap_modrdnA",
    "ldap_modrdn2_sW",
    "ldap_modrdn2_sA",
    "ldap_modrdn_sW",
    "ldap_modrdn_sA",
    "ldap_modrdn2",
    "ldap_modrdn",
    "ldap_modrdn2_s",
    "ldap_modrdn_s",
    "ldap_rename_extW",
    "ldap_rename_extA",
    "ldap_rename_ext_sW",
    "ldap_rename_ext_sA",
    "ldap_rename_ext",
    "ldap_rename_ext_s",
    "ldap_addW",
    "ldap_addA",
    "ldap_add_sW",
    "ldap_add_sA",
    "ldap_add_extW",
    "ldap_add_extA",
    "ldap_add_ext_sW",
    "ldap_add_ext_sA",
    "ldap_add",
    "ldap_add_s",
    "ldap_add_ext",
    "ldap_add_ext_s",
    "ldap_compareW",
    "ldap_compareA",
    "ldap_compare_sW",
    "ldap_compare_sA",
    "ldap_compare",
    "ldap_compare_s",
    "ldap_compare_extW",
    "ldap_compare_extA",
    "ldap_compare_ext_sW",
    "ldap_compare_ext_sA",
    "ldap_compare_ext",
    "ldap_compare_ext_s",
    "ldap_deleteW",
    "ldap_deleteA",
    "ldap_delete_sW",
    "ldap_delete_sA",
    "ldap_delete_extW",
    "ldap_delete_extA",
    "ldap_delete_ext_sW",
    "ldap_delete_ext_sA",
    "ldap_delete",
    "ldap_delete_s",
    "ldap_delete_ext",
    "ldap_delete_ext_s",
    "ldap_abandon",
    "ldap_result",
    "ldap_msgfree",
    "ldap_result2error",
    "ldap_parse_resultW",
    "ldap_parse_resultA",
    "ldap_parse_extended_resultA",
    "ldap_parse_extended_resultW",
    "ldap_parse_extended_result",
    "ldap_controls_freeA",
    "ldap_control_freeA",
    "ldap_controls_freeW",
    "ldap_control_freeW",
    "ldap_free_controlsW",
    "ldap_free_controlsA",
    "ldap_parse_result",
    "ldap_controls_free",
    "ldap_control_free",
    "ldap_free_controls",
    "ldap_err2stringW",
    "ldap_err2stringA",
    "ldap_err2string",
    "ldap_perror",
    "ldap_first_entry",
    "ldap_next_entry",
    "ldap_count_entries",
    "ldap_first_attributeW",
    "ldap_first_attributeA",
    "ldap_first_attribute",
    "ldap_next_attributeW",
    "ldap_next_attributeA",
    "ldap_next_attribute",
    "ldap_get_valuesW",
    "ldap_get_valuesA",
    "ldap_get_values",
    "ldap_get_values_lenW",
    "ldap_get_values_lenA",
    "ldap_get_values_len",
    "ldap_count_valuesW",
    "ldap_count_valuesA",
    "ldap_count_values",
    "ldap_count_values_len",
    "ldap_value_freeW",
    "ldap_value_freeA",
    "ldap_value_free",
    "ldap_value_free_len",
    "ldap_get_dnW",
    "ldap_get_dnA",
    "ldap_get_dn",
    "ldap_explode_dnW",
    "ldap_explode_dnA",
    "ldap_explode_dn",
    "ldap_dn2ufnW",
    "ldap_dn2ufnA",
    "ldap_dn2ufn",
    "ldap_memfreeW",
    "ldap_memfreeA",
    "ber_bvfree",
    "ldap_memfree",
    "ldap_ufn2dnW",
    "ldap_ufn2dnA",
    "ldap_ufn2dn",
    "ldap_startup",
    "ldap_cleanup",
    "ldap_escape_filter_elementW",
    "ldap_escape_filter_elementA",
    "ldap_escape_filter_element",
    "ldap_set_dbg_flags",
    "ldap_set_dbg_routine",
    "LdapUTF8ToUnicode",
    "LdapUnicodeToUTF8",
    "ldap_create_sort_controlA",
    "ldap_create_sort_controlW",
    "ldap_parse_sort_controlA",
    "ldap_parse_sort_controlW",
    "ldap_create_sort_control",
    "ldap_parse_sort_control",
    "ldap_encode_sort_controlW",
    "ldap_encode_sort_control",
    "ldap_encode_sort_controlA",
    "ldap_create_page_controlW",
    "ldap_create_page_controlA",
    "ldap_parse_page_controlW",
    "ldap_parse_page_controlA",
    "ldap_create_page_control",
    "ldap_parse_page_control",
    "ldap_search_init_pageW",
    "ldap_search_init_pageA",
    "ldap_search_init_page",
    "ldap_get_next_page",
    "ldap_get_next_page_s",
    "ldap_get_paged_count",
    "ldap_search_abandon_page",
    "ldap_create_vlv_controlW",
    "ldap_create_vlv_control",
    "ldap_create_vlv_controlA",
    "ldap_parse_vlv_controlW",
    "ldap_parse_vlv_control",
    "ldap_parse_vlv_controlA",
    "ldap_start_tls_sW",
    "ldap_start_tls_s",
    "ldap_start_tls_sA",
    "ldap_stop_tls_s",
    "ldap_first_reference",
    "ldap_next_reference",
    "ldap_count_references",
    "ldap_parse_referenceW",
    "ldap_parse_referenceA",
    "ldap_parse_reference",
    "ldap_extended_operationW",
    "ldap_extended_operationA",
    "ldap_extended_operation_sA",
    "ldap_extended_operation_sW",
    "ldap_extended_operation_s",
    "ldap_extended_operation",
    "ldap_close_extended_op",
    "LdapGetLastError",
    "LdapMapErrorToWin32",
    "ldap_conn_from_msg",
    "ber_init",
    "ber_free",
    "ber_bvecfree",
    "ber_bvdup",
    "ber_alloc_t",
    "ber_skip_tag",
    "ber_peek_tag",
    "ber_first_element",
    "ber_next_element",
    "ber_flatten",
    "ber_printf",
    "ber_scanf",
]
