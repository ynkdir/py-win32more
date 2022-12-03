from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.System.Com
import win32more.System.IO
import win32more.System.Rpc
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
def _define__NDR_ASYNC_MESSAGE_head():
    class _NDR_ASYNC_MESSAGE(Structure):
        pass
    return _NDR_ASYNC_MESSAGE
def _define__NDR_ASYNC_MESSAGE():
    _NDR_ASYNC_MESSAGE = win32more.System.Rpc._NDR_ASYNC_MESSAGE_head
    return _NDR_ASYNC_MESSAGE
def _define__NDR_CORRELATION_INFO_head():
    class _NDR_CORRELATION_INFO(Structure):
        pass
    return _NDR_CORRELATION_INFO
def _define__NDR_CORRELATION_INFO():
    _NDR_CORRELATION_INFO = win32more.System.Rpc._NDR_CORRELATION_INFO_head
    return _NDR_CORRELATION_INFO
def _define__NDR_PROC_CONTEXT_head():
    class _NDR_PROC_CONTEXT(Structure):
        pass
    return _NDR_PROC_CONTEXT
def _define__NDR_PROC_CONTEXT():
    _NDR_PROC_CONTEXT = win32more.System.Rpc._NDR_PROC_CONTEXT_head
    return _NDR_PROC_CONTEXT
def _define__NDR_SCONTEXT_head():
    class _NDR_SCONTEXT(Structure):
        pass
    return _NDR_SCONTEXT
def _define__NDR_SCONTEXT():
    _NDR_SCONTEXT = win32more.System.Rpc._NDR_SCONTEXT_head
    _NDR_SCONTEXT._fields_ = [
        ('pad', c_void_p * 2),
        ('userContext', c_void_p),
    ]
    return _NDR_SCONTEXT
RPC_C_BINDING_INFINITE_TIMEOUT = 10
RPC_C_BINDING_MIN_TIMEOUT = 0
RPC_C_BINDING_DEFAULT_TIMEOUT = 5
RPC_C_BINDING_MAX_TIMEOUT = 9
RPC_C_CANCEL_INFINITE_TIMEOUT = -1
RPC_C_LISTEN_MAX_CALLS_DEFAULT = 1234
RPC_C_PROTSEQ_MAX_REQS_DEFAULT = 10
RPC_C_BIND_TO_ALL_NICS = 1
RPC_C_USE_INTERNET_PORT = 1
RPC_C_USE_INTRANET_PORT = 2
RPC_C_DONT_FAIL = 4
RPC_C_RPCHTTP_USE_LOAD_BALANCE = 8
RPC_C_TRY_ENFORCE_MAX_CALLS = 16
RPC_C_MQ_TEMPORARY = 0
RPC_C_MQ_PERMANENT = 1
RPC_C_MQ_CLEAR_ON_OPEN = 2
RPC_C_MQ_USE_EXISTING_SECURITY = 4
RPC_C_MQ_AUTHN_LEVEL_NONE = 0
RPC_C_MQ_AUTHN_LEVEL_PKT_INTEGRITY = 8
RPC_C_MQ_AUTHN_LEVEL_PKT_PRIVACY = 16
RPC_C_MQ_EXPRESS = 0
RPC_C_MQ_RECOVERABLE = 1
RPC_C_MQ_JOURNAL_NONE = 0
RPC_C_MQ_JOURNAL_DEADLETTER = 1
RPC_C_MQ_JOURNAL_ALWAYS = 2
RPC_C_OPT_MQ_DELIVERY = 1
RPC_C_OPT_MQ_PRIORITY = 2
RPC_C_OPT_MQ_JOURNAL = 3
RPC_C_OPT_MQ_ACKNOWLEDGE = 4
RPC_C_OPT_MQ_AUTHN_SERVICE = 5
RPC_C_OPT_MQ_AUTHN_LEVEL = 6
RPC_C_OPT_MQ_TIME_TO_REACH_QUEUE = 7
RPC_C_OPT_MQ_TIME_TO_BE_RECEIVED = 8
RPC_C_OPT_BINDING_NONCAUSAL = 9
RPC_C_OPT_SECURITY_CALLBACK = 10
RPC_C_OPT_UNIQUE_BINDING = 11
RPC_C_OPT_MAX_OPTIONS = 12
RPC_C_OPT_CALL_TIMEOUT = 12
RPC_C_OPT_DONT_LINGER = 13
RPC_C_OPT_TRANS_SEND_BUFFER_SIZE = 5
RPC_C_OPT_TRUST_PEER = 14
RPC_C_OPT_ASYNC_BLOCK = 15
RPC_C_OPT_OPTIMIZE_TIME = 16
RPC_C_FULL_CERT_CHAIN = 1
RPC_C_STATS_CALLS_IN = 0
RPC_C_STATS_CALLS_OUT = 1
RPC_C_STATS_PKTS_IN = 2
RPC_C_STATS_PKTS_OUT = 3
RPC_C_AUTHN_NONE = 0
RPC_C_AUTHN_DCE_PRIVATE = 1
RPC_C_AUTHN_DCE_PUBLIC = 2
RPC_C_AUTHN_DEC_PUBLIC = 4
RPC_C_AUTHN_GSS_NEGOTIATE = 9
RPC_C_AUTHN_WINNT = 10
RPC_C_AUTHN_GSS_SCHANNEL = 14
RPC_C_AUTHN_GSS_KERBEROS = 16
RPC_C_AUTHN_DPA = 17
RPC_C_AUTHN_MSN = 18
RPC_C_AUTHN_DIGEST = 21
RPC_C_AUTHN_KERNEL = 20
RPC_C_AUTHN_NEGO_EXTENDER = 30
RPC_C_AUTHN_PKU2U = 31
RPC_C_AUTHN_LIVE_SSP = 32
RPC_C_AUTHN_LIVEXP_SSP = 35
RPC_C_AUTHN_CLOUD_AP = 36
RPC_C_AUTHN_MSONLINE = 82
RPC_C_AUTHN_MQ = 100
RPC_C_AUTHN_DEFAULT = -1
RPC_C_SECURITY_QOS_VERSION = 1
RPC_C_SECURITY_QOS_VERSION_1 = 1
RPC_C_SECURITY_QOS_VERSION_2 = 2
RPC_C_HTTP_AUTHN_SCHEME_BASIC = 1
RPC_C_HTTP_AUTHN_SCHEME_NTLM = 2
RPC_C_HTTP_AUTHN_SCHEME_PASSPORT = 4
RPC_C_HTTP_AUTHN_SCHEME_DIGEST = 8
RPC_C_HTTP_AUTHN_SCHEME_NEGOTIATE = 16
RPC_C_HTTP_AUTHN_SCHEME_CERT = 65536
RPC_C_SECURITY_QOS_VERSION_3 = 3
RPC_C_SECURITY_QOS_VERSION_4 = 4
RPC_C_SECURITY_QOS_VERSION_5 = 5
RPC_PROTSEQ_TCP = 1
RPC_PROTSEQ_NMP = 2
RPC_PROTSEQ_LRPC = 3
RPC_PROTSEQ_HTTP = 4
RPC_BHT_OBJECT_UUID_VALID = 1
RPC_BHO_EXCLUSIVE_AND_GUARANTEED = 4
RPC_C_AUTHZ_NONE = 0
RPC_C_AUTHZ_NAME = 1
RPC_C_AUTHZ_DCE = 2
RPC_C_AUTHZ_DEFAULT = 4294967295
DCE_C_ERROR_STRING_LEN = 256
RPC_C_EP_ALL_ELTS = 0
RPC_C_EP_MATCH_BY_IF = 1
RPC_C_EP_MATCH_BY_OBJ = 2
RPC_C_EP_MATCH_BY_BOTH = 3
RPC_C_VERS_ALL = 1
RPC_C_VERS_COMPATIBLE = 2
RPC_C_VERS_EXACT = 3
RPC_C_VERS_MAJOR_ONLY = 4
RPC_C_VERS_UPTO = 5
RPC_C_MGMT_INQ_IF_IDS = 0
RPC_C_MGMT_INQ_PRINC_NAME = 1
RPC_C_MGMT_INQ_STATS = 2
RPC_C_MGMT_IS_SERVER_LISTEN = 3
RPC_C_MGMT_STOP_SERVER_LISTEN = 4
RPC_C_PARM_MAX_PACKET_LENGTH = 1
RPC_C_PARM_BUFFER_LENGTH = 2
RPC_IF_AUTOLISTEN = 1
RPC_IF_OLE = 2
RPC_IF_ALLOW_UNKNOWN_AUTHORITY = 4
RPC_IF_ALLOW_SECURE_ONLY = 8
RPC_IF_ALLOW_CALLBACKS_WITH_NO_AUTH = 16
RPC_IF_ALLOW_LOCAL_ONLY = 32
RPC_IF_SEC_NO_CACHE = 64
RPC_IF_SEC_CACHE_PER_PROC = 128
RPC_IF_ASYNC_CALLBACK = 256
RPC_FW_IF_FLAG_DCOM = 1
RPC_C_NOTIFY_ON_SEND_COMPLETE = 1
MaxNumberOfEEInfoParams = 4
RPC_EEINFO_VERSION = 1
EEInfoPreviousRecordsMissing = 1
EEInfoNextRecordsMissing = 2
EEInfoUseFileTime = 4
EEInfoGCCOM = 11
EEInfoGCFRS = 12
RPC_CALL_ATTRIBUTES_VERSION = 2
RPC_QUERY_SERVER_PRINCIPAL_NAME = 2
RPC_QUERY_CLIENT_PRINCIPAL_NAME = 4
RPC_QUERY_CALL_LOCAL_ADDRESS = 8
RPC_QUERY_CLIENT_PID = 16
RPC_QUERY_IS_CLIENT_LOCAL = 32
RPC_QUERY_NO_AUTH_REQUIRED = 64
RPC_QUERY_CLIENT_ID = 128
RPC_CALL_STATUS_CANCELLED = 1
RPC_CALL_STATUS_DISCONNECTED = 2
RPC_CONTEXT_HANDLE_DEFAULT_FLAGS = 0
RPC_CONTEXT_HANDLE_FLAGS = 805306368
RPC_CONTEXT_HANDLE_SERIALIZE = 268435456
RPC_CONTEXT_HANDLE_DONT_SERIALIZE = 536870912
RPC_TYPE_STRICT_CONTEXT_HANDLE = 1073741824
RPC_TYPE_DISCONNECT_EVENT_CONTEXT_HANDLE = 2147483648
RPC_NCA_FLAGS_DEFAULT = 0
RPC_NCA_FLAGS_IDEMPOTENT = 1
RPC_NCA_FLAGS_BROADCAST = 2
RPC_NCA_FLAGS_MAYBE = 4
RPCFLG_HAS_GUARANTEE = 16
RPCFLG_WINRT_REMOTE_ASYNC = 32
RPC_BUFFER_COMPLETE = 4096
RPC_BUFFER_PARTIAL = 8192
RPC_BUFFER_EXTRA = 16384
RPC_BUFFER_ASYNC = 32768
RPC_BUFFER_NONOTIFY = 65536
RPCFLG_MESSAGE = 16777216
RPCFLG_AUTO_COMPLETE = 134217728
RPCFLG_LOCAL_CALL = 268435456
RPCFLG_INPUT_SYNCHRONOUS = 536870912
RPCFLG_ASYNCHRONOUS = 1073741824
RPCFLG_NON_NDR = 2147483648
RPCFLG_HAS_MULTI_SYNTAXES = 33554432
RPCFLG_HAS_CALLBACK = 67108864
RPCFLG_ACCESSIBILITY_BIT1 = 1048576
RPCFLG_ACCESSIBILITY_BIT2 = 2097152
RPCFLG_ACCESS_LOCAL = 4194304
NDR_CUSTOM_OR_DEFAULT_ALLOCATOR = 268435456
NDR_DEFAULT_ALLOCATOR = 536870912
RPCFLG_NDR64_CONTAINS_ARM_LAYOUT = 67108864
RPCFLG_SENDER_WAITING_FOR_REPLY = 8388608
RPC_FLAGS_VALID_BIT = 32768
NT351_INTERFACE_SIZE = 64
RPC_INTERFACE_HAS_PIPES = 1
RPC_SYSTEM_HANDLE_FREE_UNRETRIEVED = 1
RPC_SYSTEM_HANDLE_FREE_RETRIEVED = 2
RPC_SYSTEM_HANDLE_FREE_ALL = 3
RPC_SYSTEM_HANDLE_FREE_ERROR_ON_CLOSE = 4
TRANSPORT_TYPE_CN = 1
TRANSPORT_TYPE_DG = 2
TRANSPORT_TYPE_LPC = 4
TRANSPORT_TYPE_WMSG = 8
RPC_P_ADDR_FORMAT_TCP_IPV4 = 1
RPC_P_ADDR_FORMAT_TCP_IPV6 = 2
RPC_C_OPT_SESSION_ID = 6
RPC_C_OPT_COOKIE_AUTH = 7
RPC_C_OPT_RESOURCE_TYPE_UUID = 8
RPC_PROXY_CONNECTION_TYPE_IN_PROXY = 0
RPC_PROXY_CONNECTION_TYPE_OUT_PROXY = 1
RPC_C_OPT_PRIVATE_SUPPRESS_WAKE = 1
RPC_C_OPT_PRIVATE_DO_NOT_DISTURB = 2
RPC_C_OPT_PRIVATE_BREAK_ON_SUSPEND = 3
RPC_C_PROFILE_DEFAULT_ELT = 0
RPC_C_PROFILE_ALL_ELT = 1
RPC_C_PROFILE_ALL_ELTS = 1
RPC_C_PROFILE_MATCH_BY_IF = 2
RPC_C_PROFILE_MATCH_BY_MBR = 3
RPC_C_PROFILE_MATCH_BY_BOTH = 4
RPC_C_NS_DEFAULT_EXP_AGE = -1
TARGET_IS_NT100_OR_LATER = 1
TARGET_IS_NT63_OR_LATER = 1
TARGET_IS_NT62_OR_LATER = 1
TARGET_IS_NT61_OR_LATER = 1
TARGET_IS_NT60_OR_LATER = 1
TARGET_IS_NT51_OR_LATER = 1
TARGET_IS_NT50_OR_LATER = 1
TARGET_IS_NT40_OR_LATER = 1
TARGET_IS_NT351_OR_WIN95_OR_LATER = 1
cbNDRContext = 20
USER_CALL_IS_ASYNC = 256
USER_CALL_NEW_CORRELATION_DESC = 512
MIDL_WINRT_TYPE_SERIALIZATION_INFO_CURRENT_VERSION = 1
USER_MARSHAL_FC_BYTE = 1
USER_MARSHAL_FC_CHAR = 2
USER_MARSHAL_FC_SMALL = 3
USER_MARSHAL_FC_USMALL = 4
USER_MARSHAL_FC_WCHAR = 5
USER_MARSHAL_FC_SHORT = 6
USER_MARSHAL_FC_USHORT = 7
USER_MARSHAL_FC_LONG = 8
USER_MARSHAL_FC_ULONG = 9
USER_MARSHAL_FC_FLOAT = 10
USER_MARSHAL_FC_HYPER = 11
USER_MARSHAL_FC_DOUBLE = 12
INVALID_FRAGMENT_ID = 0
NDR64_FC_EXPLICIT_HANDLE = 0
NDR64_FC_BIND_GENERIC = 1
NDR64_FC_BIND_PRIMITIVE = 2
NDR64_FC_AUTO_HANDLE = 3
NDR64_FC_CALLBACK_HANDLE = 4
NDR64_FC_NO_HANDLE = 5
__RPCPROXY_H_VERSION__ = 475
MidlInterceptionInfoVersionOne = 1
MidlWinrtTypeSerializationInfoVersionOne = 1
def _define_IUnknown_QueryInterface_Proxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(('IUnknown_QueryInterface_Proxy', windll['RPCRT4.dll']), ((1, 'This'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IUnknown_AddRef_Proxy():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Com.IUnknown_head)(('IUnknown_AddRef_Proxy', windll['RPCRT4.dll']), ((1, 'This'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IUnknown_Release_Proxy():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Com.IUnknown_head)(('IUnknown_Release_Proxy', windll['RPCRT4.dll']), ((1, 'This'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingCopy():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p))(('RpcBindingCopy', windll['RPCRT4.dll']), ((1, 'SourceBinding'),(1, 'DestinationBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcBindingFree', windll['RPCRT4.dll']), ((1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingSetOption():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,UIntPtr)(('RpcBindingSetOption', windll['RPCRT4.dll']), ((1, 'hBinding'),(1, 'option'),(1, 'optionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqOption():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(UIntPtr))(('RpcBindingInqOption', windll['RPCRT4.dll']), ((1, 'hBinding'),(1, 'option'),(1, 'pOptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingFromStringBindingA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,POINTER(c_void_p))(('RpcBindingFromStringBindingA', windll['RPCRT4.dll']), ((1, 'StringBinding'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingFromStringBindingW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(c_void_p))(('RpcBindingFromStringBindingW', windll['RPCRT4.dll']), ((1, 'StringBinding'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsGetContextBinding():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p))(('RpcSsGetContextBinding', windll['RPCRT4.dll']), ((1, 'ContextHandle'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqMaxCalls():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32))(('RpcBindingInqMaxCalls', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'MaxCalls'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqObject():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid))(('RpcBindingInqObject', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ObjectUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingReset():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcBindingReset', windll['RPCRT4.dll']), ((1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingSetObject():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid))(('RpcBindingSetObject', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ObjectUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtInqDefaultProtectLevel():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt32))(('RpcMgmtInqDefaultProtectLevel', windll['RPCRT4.dll']), ((1, 'AuthnSvc'),(1, 'AuthnLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingToStringBindingA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_char_p_no))(('RpcBindingToStringBindingA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'StringBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingToStringBindingW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(UInt16)))(('RpcBindingToStringBindingW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'StringBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingVectorFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head)))(('RpcBindingVectorFree', windll['RPCRT4.dll']), ((1, 'BindingVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcStringBindingComposeA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,c_char_p_no,c_char_p_no,c_char_p_no,c_char_p_no,POINTER(c_char_p_no))(('RpcStringBindingComposeA', windll['RPCRT4.dll']), ((1, 'ObjUuid'),(1, 'ProtSeq'),(1, 'NetworkAddr'),(1, 'Endpoint'),(1, 'Options'),(1, 'StringBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcStringBindingComposeW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(POINTER(UInt16)))(('RpcStringBindingComposeW', windll['RPCRT4.dll']), ((1, 'ObjUuid'),(1, 'ProtSeq'),(1, 'NetworkAddr'),(1, 'Endpoint'),(1, 'Options'),(1, 'StringBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcStringBindingParseA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,POINTER(c_char_p_no),POINTER(c_char_p_no),POINTER(c_char_p_no),POINTER(c_char_p_no),POINTER(c_char_p_no))(('RpcStringBindingParseA', windll['RPCRT4.dll']), ((1, 'StringBinding'),(1, 'ObjUuid'),(1, 'Protseq'),(1, 'NetworkAddr'),(1, 'Endpoint'),(1, 'NetworkOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcStringBindingParseW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)))(('RpcStringBindingParseW', windll['RPCRT4.dll']), ((1, 'StringBinding'),(1, 'ObjUuid'),(1, 'Protseq'),(1, 'NetworkAddr'),(1, 'Endpoint'),(1, 'NetworkOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcStringFreeA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_char_p_no))(('RpcStringFreeA', windll['RPCRT4.dll']), ((1, 'String'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcStringFreeW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(UInt16)))(('RpcStringFreeW', windll['RPCRT4.dll']), ((1, 'String'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcIfInqId():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_IF_ID_head))(('RpcIfInqId', windll['RPCRT4.dll']), ((1, 'RpcIfHandle'),(1, 'RpcIfId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNetworkIsProtseqValidA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no)(('RpcNetworkIsProtseqValidA', windll['RPCRT4.dll']), ((1, 'Protseq'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNetworkIsProtseqValidW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16))(('RpcNetworkIsProtseqValidW', windll['RPCRT4.dll']), ((1, 'Protseq'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtInqComTimeout():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32))(('RpcMgmtInqComTimeout', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtSetComTimeout():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32)(('RpcMgmtSetComTimeout', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtSetCancelTimeout():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,Int32)(('RpcMgmtSetCancelTimeout', windll['RPCRT4.dll']), ((1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNetworkInqProtseqsA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_PROTSEQ_VECTORA_head)))(('RpcNetworkInqProtseqsA', windll['RPCRT4.dll']), ((1, 'ProtseqVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNetworkInqProtseqsW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_PROTSEQ_VECTORW_head)))(('RpcNetworkInqProtseqsW', windll['RPCRT4.dll']), ((1, 'ProtseqVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcObjectInqType():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid),POINTER(Guid))(('RpcObjectInqType', windll['RPCRT4.dll']), ((1, 'ObjUuid'),(1, 'TypeUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcObjectSetInqFn():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.RPC_OBJECT_INQ_FN)(('RpcObjectSetInqFn', windll['RPCRT4.dll']), ((1, 'InquiryFn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcObjectSetType():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid),POINTER(Guid))(('RpcObjectSetType', windll['RPCRT4.dll']), ((1, 'ObjUuid'),(1, 'TypeUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcProtseqVectorFreeA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_PROTSEQ_VECTORA_head)))(('RpcProtseqVectorFreeA', windll['RPCRT4.dll']), ((1, 'ProtseqVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcProtseqVectorFreeW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_PROTSEQ_VECTORW_head)))(('RpcProtseqVectorFreeW', windll['RPCRT4.dll']), ((1, 'ProtseqVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqBindings():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head)))(('RpcServerInqBindings', windll['RPCRT4.dll']), ((1, 'BindingVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqBindingsEx():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head)))(('RpcServerInqBindingsEx', windll['RPCRT4.dll']), ((1, 'SecurityDescriptor'),(1, 'BindingVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqIf():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),POINTER(c_void_p))(('RpcServerInqIf', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'MgrTypeUuid'),(1, 'MgrEpv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerListen():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,UInt32,UInt32)(('RpcServerListen', windll['RPCRT4.dll']), ((1, 'MinimumCallThreads'),(1, 'MaxCalls'),(1, 'DontWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerRegisterIf():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),c_void_p)(('RpcServerRegisterIf', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'MgrTypeUuid'),(1, 'MgrEpv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerRegisterIfEx():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),c_void_p,UInt32,UInt32,win32more.System.Rpc.RPC_IF_CALLBACK_FN)(('RpcServerRegisterIfEx', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'MgrTypeUuid'),(1, 'MgrEpv'),(1, 'Flags'),(1, 'MaxCalls'),(1, 'IfCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerRegisterIf2():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),c_void_p,UInt32,UInt32,UInt32,win32more.System.Rpc.RPC_IF_CALLBACK_FN)(('RpcServerRegisterIf2', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'MgrTypeUuid'),(1, 'MgrEpv'),(1, 'Flags'),(1, 'MaxCalls'),(1, 'MaxRpcSize'),(1, 'IfCallbackFn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerRegisterIf3():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),c_void_p,UInt32,UInt32,UInt32,win32more.System.Rpc.RPC_IF_CALLBACK_FN,c_void_p)(('RpcServerRegisterIf3', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'MgrTypeUuid'),(1, 'MgrEpv'),(1, 'Flags'),(1, 'MaxCalls'),(1, 'MaxRpcSize'),(1, 'IfCallback'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUnregisterIf():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),UInt32)(('RpcServerUnregisterIf', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'MgrTypeUuid'),(1, 'WaitForCallsToComplete'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUnregisterIfEx():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),Int32)(('RpcServerUnregisterIfEx', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'MgrTypeUuid'),(1, 'RundownContextHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseAllProtseqs():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_void_p)(('RpcServerUseAllProtseqs', windll['RPCRT4.dll']), ((1, 'MaxCalls'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseAllProtseqsEx():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseAllProtseqsEx', windll['RPCRT4.dll']), ((1, 'MaxCalls'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseAllProtseqsIf():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_void_p,c_void_p)(('RpcServerUseAllProtseqsIf', windll['RPCRT4.dll']), ((1, 'MaxCalls'),(1, 'IfSpec'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseAllProtseqsIfEx():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_void_p,c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseAllProtseqsIfEx', windll['RPCRT4.dll']), ((1, 'MaxCalls'),(1, 'IfSpec'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,UInt32,c_void_p)(('RpcServerUseProtseqA', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqExA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,UInt32,c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseProtseqExA', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),UInt32,c_void_p)(('RpcServerUseProtseqW', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqExW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),UInt32,c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseProtseqExW', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqEpA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,UInt32,c_char_p_no,c_void_p)(('RpcServerUseProtseqEpA', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'Endpoint'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqEpExA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,UInt32,c_char_p_no,c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseProtseqEpExA', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'Endpoint'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqEpW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),UInt32,POINTER(UInt16),c_void_p)(('RpcServerUseProtseqEpW', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'Endpoint'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqEpExW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),UInt32,POINTER(UInt16),c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseProtseqEpExW', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'Endpoint'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqIfA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,UInt32,c_void_p,c_void_p)(('RpcServerUseProtseqIfA', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'IfSpec'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqIfExA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,UInt32,c_void_p,c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseProtseqIfExA', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'IfSpec'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqIfW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),UInt32,c_void_p,c_void_p)(('RpcServerUseProtseqIfW', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'IfSpec'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUseProtseqIfExW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),UInt32,c_void_p,c_void_p,POINTER(win32more.System.Rpc.RPC_POLICY_head))(('RpcServerUseProtseqIfExW', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'MaxCalls'),(1, 'IfSpec'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerYield():
    try:
        return WINFUNCTYPE(Void,)(('RpcServerYield', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtStatsVectorFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_STATS_VECTOR_head)))(('RpcMgmtStatsVectorFree', windll['RPCRT4.dll']), ((1, 'StatsVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtInqStats():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(win32more.System.Rpc.RPC_STATS_VECTOR_head)))(('RpcMgmtInqStats', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Statistics'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtIsServerListening():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcMgmtIsServerListening', windll['RPCRT4.dll']), ((1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtStopServerListening():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcMgmtStopServerListening', windll['RPCRT4.dll']), ((1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtWaitServerListen():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('RpcMgmtWaitServerListen', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtSetServerStackSize():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32)(('RpcMgmtSetServerStackSize', windll['RPCRT4.dll']), ((1, 'ThreadStackSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsDontSerializeContext():
    try:
        return WINFUNCTYPE(Void,)(('RpcSsDontSerializeContext', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtEnableIdleCleanup():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('RpcMgmtEnableIdleCleanup', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtInqIfIds():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(win32more.System.Rpc.RPC_IF_ID_VECTOR_head)))(('RpcMgmtInqIfIds', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'IfIdVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcIfIdVectorFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(win32more.System.Rpc.RPC_IF_ID_VECTOR_head)))(('RpcIfIdVectorFree', windll['RPCNS4.dll']), ((1, 'IfIdVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtInqServerPrincNameA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(c_char_p_no))(('RpcMgmtInqServerPrincNameA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'AuthnSvc'),(1, 'ServerPrincName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtInqServerPrincNameW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(POINTER(UInt16)))(('RpcMgmtInqServerPrincNameW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'AuthnSvc'),(1, 'ServerPrincName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqDefaultPrincNameA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(c_char_p_no))(('RpcServerInqDefaultPrincNameA', windll['RPCRT4.dll']), ((1, 'AuthnSvc'),(1, 'PrincName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqDefaultPrincNameW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(POINTER(UInt16)))(('RpcServerInqDefaultPrincNameW', windll['RPCRT4.dll']), ((1, 'AuthnSvc'),(1, 'PrincName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcEpResolveBinding():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)(('RpcEpResolveBinding', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'IfSpec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingInqEntryNameA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(c_char_p_no))(('RpcNsBindingInqEntryNameA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingInqEntryNameW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(POINTER(UInt16)))(('RpcNsBindingInqEntryNameW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingCreateA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_A_head),POINTER(win32more.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_A_head),POINTER(win32more.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_V1_head),POINTER(c_void_p))(('RpcBindingCreateA', windll['RPCRT4.dll']), ((1, 'Template'),(1, 'Security'),(1, 'Options'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingCreateW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_W_head),POINTER(win32more.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_W_head),POINTER(win32more.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_V1_head),POINTER(c_void_p))(('RpcBindingCreateW', windll['RPCRT4.dll']), ((1, 'Template'),(1, 'Security'),(1, 'Options'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqBindingHandle():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcServerInqBindingHandle', windll['RPCRT4.dll']), ((1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcImpersonateClient():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcImpersonateClient', windll['RPCRT4.dll']), ((1, 'BindingHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcImpersonateClient2():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcImpersonateClient2', windll['RPCRT4.dll']), ((1, 'BindingHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcRevertToSelfEx():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcRevertToSelfEx', windll['RPCRT4.dll']), ((1, 'BindingHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcRevertToSelf():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('RpcRevertToSelf', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcImpersonateClientContainer():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcImpersonateClientContainer', windll['RPCRT4.dll']), ((1, 'BindingHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcRevertContainerImpersonation():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('RpcRevertContainerImpersonation', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthClientA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p),POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('RpcBindingInqAuthClientA', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'Privs'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthzSvc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthClientW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p),POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('RpcBindingInqAuthClientW', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'Privs'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthzSvc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthClientExA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p),POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),UInt32)(('RpcBindingInqAuthClientExA', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'Privs'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthzSvc'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthClientExW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p),POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),UInt32)(('RpcBindingInqAuthClientExW', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'Privs'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthzSvc'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthInfoA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32))(('RpcBindingInqAuthInfoA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthInfoW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32))(('RpcBindingInqAuthInfoW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingSetAuthInfoA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_char_p_no,UInt32,UInt32,c_void_p,UInt32)(('RpcBindingSetAuthInfoA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingSetAuthInfoExA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_char_p_no,UInt32,UInt32,c_void_p,UInt32,POINTER(win32more.System.Rpc.RPC_SECURITY_QOS_head))(('RpcBindingSetAuthInfoExA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),(1, 'SecurityQos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingSetAuthInfoW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt16),UInt32,UInt32,c_void_p,UInt32)(('RpcBindingSetAuthInfoW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingSetAuthInfoExW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt16),UInt32,UInt32,c_void_p,UInt32,POINTER(win32more.System.Rpc.RPC_SECURITY_QOS_head))(('RpcBindingSetAuthInfoExW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),(1, 'SecurityQOS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthInfoExA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32),UInt32,POINTER(win32more.System.Rpc.RPC_SECURITY_QOS_head))(('RpcBindingInqAuthInfoExA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),(1, 'RpcQosVersion'),(1, 'SecurityQOS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingInqAuthInfoExW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32),UInt32,POINTER(win32more.System.Rpc.RPC_SECURITY_QOS_head))(('RpcBindingInqAuthInfoExW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerPrincName'),(1, 'AuthnLevel'),(1, 'AuthnSvc'),(1, 'AuthIdentity'),(1, 'AuthzSvc'),(1, 'RpcQosVersion'),(1, 'SecurityQOS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerCompleteSecurityCallback():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,win32more.System.Rpc.RPC_STATUS)(('RpcServerCompleteSecurityCallback', windll['RPCRT4.dll']), ((1, 'BindingHandle'),(1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerRegisterAuthInfoA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,UInt32,win32more.System.Rpc.RPC_AUTH_KEY_RETRIEVAL_FN,c_void_p)(('RpcServerRegisterAuthInfoA', windll['RPCRT4.dll']), ((1, 'ServerPrincName'),(1, 'AuthnSvc'),(1, 'GetKeyFn'),(1, 'Arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerRegisterAuthInfoW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),UInt32,win32more.System.Rpc.RPC_AUTH_KEY_RETRIEVAL_FN,c_void_p)(('RpcServerRegisterAuthInfoW', windll['RPCRT4.dll']), ((1, 'ServerPrincName'),(1, 'AuthnSvc'),(1, 'GetKeyFn'),(1, 'Arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingServerFromClient():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p))(('RpcBindingServerFromClient', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'ServerBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcRaiseException():
    try:
        return WINFUNCTYPE(Void,win32more.System.Rpc.RPC_STATUS)(('RpcRaiseException', windll['RPCRT4.dll']), ((1, 'exception'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcTestCancel():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('RpcTestCancel', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerTestCancel():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcServerTestCancel', windll['RPCRT4.dll']), ((1, 'BindingHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcCancelThread():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcCancelThread', windll['RPCRT4.dll']), ((1, 'Thread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcCancelThreadEx():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,Int32)(('RpcCancelThreadEx', windll['RPCRT4.dll']), ((1, 'Thread'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidCreate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid))(('UuidCreate', windll['RPCRT4.dll']), ((1, 'Uuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidCreateSequential():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid))(('UuidCreateSequential', windll['RPCRT4.dll']), ((1, 'Uuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidToStringA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid),POINTER(c_char_p_no))(('UuidToStringA', windll['RPCRT4.dll']), ((1, 'Uuid'),(1, 'StringUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidFromStringA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,POINTER(Guid))(('UuidFromStringA', windll['RPCRT4.dll']), ((1, 'StringUuid'),(1, 'Uuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidToStringW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid),POINTER(POINTER(UInt16)))(('UuidToStringW', windll['RPCRT4.dll']), ((1, 'Uuid'),(1, 'StringUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidFromStringW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(Guid))(('UuidFromStringW', windll['RPCRT4.dll']), ((1, 'StringUuid'),(1, 'Uuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidCompare():
    try:
        return WINFUNCTYPE(Int32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Rpc.RPC_STATUS))(('UuidCompare', windll['RPCRT4.dll']), ((1, 'Uuid1'),(1, 'Uuid2'),(1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidCreateNil():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid))(('UuidCreateNil', windll['RPCRT4.dll']), ((1, 'NilUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidEqual():
    try:
        return WINFUNCTYPE(Int32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Rpc.RPC_STATUS))(('UuidEqual', windll['RPCRT4.dll']), ((1, 'Uuid1'),(1, 'Uuid2'),(1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidHash():
    try:
        return WINFUNCTYPE(UInt16,POINTER(Guid),POINTER(win32more.System.Rpc.RPC_STATUS))(('UuidHash', windll['RPCRT4.dll']), ((1, 'Uuid'),(1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UuidIsNil():
    try:
        return WINFUNCTYPE(Int32,POINTER(Guid),POINTER(win32more.System.Rpc.RPC_STATUS))(('UuidIsNil', windll['RPCRT4.dll']), ((1, 'Uuid'),(1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcEpRegisterNoReplaceA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(win32more.System.Rpc.UUID_VECTOR_head),c_char_p_no)(('RpcEpRegisterNoReplaceA', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'BindingVector'),(1, 'UuidVector'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcEpRegisterNoReplaceW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(win32more.System.Rpc.UUID_VECTOR_head),POINTER(UInt16))(('RpcEpRegisterNoReplaceW', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'BindingVector'),(1, 'UuidVector'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcEpRegisterA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(win32more.System.Rpc.UUID_VECTOR_head),c_char_p_no)(('RpcEpRegisterA', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'BindingVector'),(1, 'UuidVector'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcEpRegisterW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(win32more.System.Rpc.UUID_VECTOR_head),POINTER(UInt16))(('RpcEpRegisterW', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'BindingVector'),(1, 'UuidVector'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcEpUnregister():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcEpUnregister', windll['RPCRT4.dll']), ((1, 'IfSpec'),(1, 'BindingVector'),(1, 'UuidVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DceErrorInqTextA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.RPC_STATUS,c_char_p_no)(('DceErrorInqTextA', windll['RPCRT4.dll']), ((1, 'RpcStatus'),(1, 'ErrorText'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DceErrorInqTextW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.RPC_STATUS,POINTER(UInt16))(('DceErrorInqTextW', windll['RPCRT4.dll']), ((1, 'RpcStatus'),(1, 'ErrorText'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtEpEltInqBegin():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,POINTER(Guid),POINTER(POINTER(c_void_p)))(('RpcMgmtEpEltInqBegin', windll['RPCRT4.dll']), ((1, 'EpBinding'),(1, 'InquiryType'),(1, 'IfId'),(1, 'VersOption'),(1, 'ObjectUuid'),(1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtEpEltInqDone():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(c_void_p)))(('RpcMgmtEpEltInqDone', windll['RPCRT4.dll']), ((1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtEpEltInqNextA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p),POINTER(win32more.System.Rpc.RPC_IF_ID_head),POINTER(c_void_p),POINTER(Guid),POINTER(c_char_p_no))(('RpcMgmtEpEltInqNextA', windll['RPCRT4.dll']), ((1, 'InquiryContext'),(1, 'IfId'),(1, 'Binding'),(1, 'ObjectUuid'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtEpEltInqNextW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p),POINTER(win32more.System.Rpc.RPC_IF_ID_head),POINTER(c_void_p),POINTER(Guid),POINTER(POINTER(UInt16)))(('RpcMgmtEpEltInqNextW', windll['RPCRT4.dll']), ((1, 'InquiryContext'),(1, 'IfId'),(1, 'Binding'),(1, 'ObjectUuid'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtEpUnregister():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_IF_ID_head),c_void_p,POINTER(Guid))(('RpcMgmtEpUnregister', windll['RPCRT4.dll']), ((1, 'EpBinding'),(1, 'IfId'),(1, 'Binding'),(1, 'ObjectUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcMgmtSetAuthorizationFn():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.RPC_MGMT_AUTHORIZATION_FN)(('RpcMgmtSetAuthorizationFn', windll['RPCRT4.dll']), ((1, 'AuthorizationFn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcExceptionFilter():
    try:
        return WINFUNCTYPE(Int32,UInt32)(('RpcExceptionFilter', windll['RPCRT4.dll']), ((1, 'ExceptionCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInterfaceGroupCreateW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_INTERFACE_TEMPLATEW_head),UInt32,POINTER(win32more.System.Rpc.RPC_ENDPOINT_TEMPLATEW_head),UInt32,UInt32,win32more.System.Rpc.RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN,c_void_p,POINTER(c_void_p))(('RpcServerInterfaceGroupCreateW', windll['RPCRT4.dll']), ((1, 'Interfaces'),(1, 'NumIfs'),(1, 'Endpoints'),(1, 'NumEndpoints'),(1, 'IdlePeriod'),(1, 'IdleCallbackFn'),(1, 'IdleCallbackContext'),(1, 'IfGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInterfaceGroupCreateA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_INTERFACE_TEMPLATEA_head),UInt32,POINTER(win32more.System.Rpc.RPC_ENDPOINT_TEMPLATEA_head),UInt32,UInt32,win32more.System.Rpc.RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN,c_void_p,POINTER(c_void_p))(('RpcServerInterfaceGroupCreateA', windll['RPCRT4.dll']), ((1, 'Interfaces'),(1, 'NumIfs'),(1, 'Endpoints'),(1, 'NumEndpoints'),(1, 'IdlePeriod'),(1, 'IdleCallbackFn'),(1, 'IdleCallbackContext'),(1, 'IfGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInterfaceGroupClose():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcServerInterfaceGroupClose', windll['RPCRT4.dll']), ((1, 'IfGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInterfaceGroupActivate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcServerInterfaceGroupActivate', windll['RPCRT4.dll']), ((1, 'IfGroup'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInterfaceGroupDeactivate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32)(('RpcServerInterfaceGroupDeactivate', windll['RPCRT4.dll']), ((1, 'IfGroup'),(1, 'ForceDeactivation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInterfaceGroupInqBindings():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head)))(('RpcServerInterfaceGroupInqBindings', windll['RPCRT4.dll']), ((1, 'IfGroup'),(1, 'BindingVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNegotiateTransferSyntax():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcNegotiateTransferSyntax', windll['RPCRT4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcGetBuffer():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcGetBuffer', windll['RPCRT4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcGetBufferWithObject():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(Guid))(('I_RpcGetBufferWithObject', windll['RPCRT4.dll']), ((1, 'Message'),(1, 'ObjectUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcSendReceive():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcSendReceive', windll['RPCRT4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcFreeBuffer():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcFreeBuffer', windll['RPCRT4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcSend():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcSend', windll['RPCRT4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcReceive():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),UInt32)(('I_RpcReceive', windll['RPCRT4.dll']), ((1, 'Message'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcFreePipeBuffer():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcFreePipeBuffer', windll['RPCRT4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcReallocPipeBuffer():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),UInt32)(('I_RpcReallocPipeBuffer', windll['RPCRT4.dll']), ((1, 'Message'),(1, 'NewSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcRequestMutex():
    try:
        return WINFUNCTYPE(Void,POINTER(c_void_p))(('I_RpcRequestMutex', windll['RPCRT4.dll']), ((1, 'Mutex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcClearMutex():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('I_RpcClearMutex', windll['RPCRT4.dll']), ((1, 'Mutex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcDeleteMutex():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('I_RpcDeleteMutex', windll['RPCRT4.dll']), ((1, 'Mutex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcAllocate():
    try:
        return WINFUNCTYPE(c_void_p,UInt32)(('I_RpcAllocate', windll['RPCRT4.dll']), ((1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcFree():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('I_RpcFree', windll['RPCRT4.dll']), ((1, 'Object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcPauseExecution():
    try:
        return WINFUNCTYPE(Void,UInt32)(('I_RpcPauseExecution', windll['RPCRT4.dll']), ((1, 'Milliseconds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcGetExtendedError():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('I_RpcGetExtendedError', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcSystemHandleTypeSpecificWork():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,Byte,Byte,win32more.System.Rpc.LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION)(('I_RpcSystemHandleTypeSpecificWork', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'ActualType'),(1, 'IdlType'),(1, 'MarshalDirection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcGetCurrentCallHandle():
    try:
        return WINFUNCTYPE(c_void_p,)(('I_RpcGetCurrentCallHandle', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNsInterfaceExported():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(win32more.System.Rpc.RPC_SERVER_INTERFACE_head))(('I_RpcNsInterfaceExported', windll['RPCRT4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'RpcInterfaceInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNsInterfaceUnexported():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(win32more.System.Rpc.RPC_SERVER_INTERFACE_head))(('I_RpcNsInterfaceUnexported', windll['RPCRT4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'RpcInterfaceInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingToStaticStringBindingW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(UInt16)))(('I_RpcBindingToStaticStringBindingW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'StringBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqSecurityContext():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p))(('I_RpcBindingInqSecurityContext', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'SecurityContextHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqSecurityContextKeyInfo():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)(('I_RpcBindingInqSecurityContextKeyInfo', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'KeyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqWireIdForSnego():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_char_p_no)(('I_RpcBindingInqWireIdForSnego', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'WireId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqMarshalledTargetInfo():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32),POINTER(c_char_p_no))(('I_RpcBindingInqMarshalledTargetInfo', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'MarshalledTargetInfoSize'),(1, 'MarshalledTargetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqLocalClientPID():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32))(('I_RpcBindingInqLocalClientPID', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Pid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingHandleToAsyncHandle():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p))(('I_RpcBindingHandleToAsyncHandle', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'AsyncHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNsBindingSetEntryNameW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(UInt16))(('I_RpcNsBindingSetEntryNameW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNsBindingSetEntryNameA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,c_char_p_no)(('I_RpcNsBindingSetEntryNameA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerUseProtseqEp2A():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,c_char_p_no,UInt32,c_char_p_no,c_void_p,c_void_p)(('I_RpcServerUseProtseqEp2A', windll['RPCRT4.dll']), ((1, 'NetworkAddress'),(1, 'Protseq'),(1, 'MaxCalls'),(1, 'Endpoint'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerUseProtseqEp2W():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(UInt16),UInt32,POINTER(UInt16),c_void_p,c_void_p)(('I_RpcServerUseProtseqEp2W', windll['RPCRT4.dll']), ((1, 'NetworkAddress'),(1, 'Protseq'),(1, 'MaxCalls'),(1, 'Endpoint'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerUseProtseq2W():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(UInt16),UInt32,c_void_p,c_void_p)(('I_RpcServerUseProtseq2W', windll['RPCRT4.dll']), ((1, 'NetworkAddress'),(1, 'Protseq'),(1, 'MaxCalls'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerUseProtseq2A():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_char_p_no,c_char_p_no,UInt32,c_void_p,c_void_p)(('I_RpcServerUseProtseq2A', windll['RPCRT4.dll']), ((1, 'NetworkAddress'),(1, 'Protseq'),(1, 'MaxCalls'),(1, 'SecurityDescriptor'),(1, 'Policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerStartService():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(UInt16),c_void_p)(('I_RpcServerStartService', windll['RPCRT4.dll']), ((1, 'Protseq'),(1, 'Endpoint'),(1, 'IfSpec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqDynamicEndpointW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(UInt16)))(('I_RpcBindingInqDynamicEndpointW', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'DynamicEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqDynamicEndpointA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_char_p_no))(('I_RpcBindingInqDynamicEndpointA', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'DynamicEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerCheckClientRestriction():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('I_RpcServerCheckClientRestriction', windll['RPCRT4.dll']), ((1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqTransportType():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32))(('I_RpcBindingInqTransportType', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcIfInqTransferSyntaxes():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_TRANSFER_SYNTAX_head),UInt32,POINTER(UInt32))(('I_RpcIfInqTransferSyntaxes', windll['RPCRT4.dll']), ((1, 'RpcIfHandle'),(1, 'TransferSyntaxes'),(1, 'TransferSyntaxSize'),(1, 'TransferSyntaxCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_UuidCreate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid))(('I_UuidCreate', windll['RPCRT4.dll']), ((1, 'Uuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingCopy():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p))(('I_RpcBindingCopy', windll['RPCRT4.dll']), ((1, 'SourceBinding'),(1, 'DestinationBinding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingIsClientLocal():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32))(('I_RpcBindingIsClientLocal', windll['RPCRT4.dll']), ((1, 'BindingHandle'),(1, 'ClientLocalFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingCreateNP():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(c_void_p))(('I_RpcBindingCreateNP', windll['RPCRT4.dll']), ((1, 'ServerName'),(1, 'ServiceName'),(1, 'NetworkOptions'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcSsDontSerializeContext():
    try:
        return WINFUNCTYPE(Void,)(('I_RpcSsDontSerializeContext', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerRegisterForwardFunction():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_FORWARD_FUNCTION))(('I_RpcServerRegisterForwardFunction', windll['RPCRT4.dll']), ((1, 'pForwardFunction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerInqAddressChangeFn():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.RPC_ADDRESS_CHANGE_FN),)(('I_RpcServerInqAddressChangeFn', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerSetAddressChangeFn():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ADDRESS_CHANGE_FN))(('I_RpcServerSetAddressChangeFn', windll['RPCRT4.dll']), ((1, 'pAddressChangeFn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerInqLocalConnAddress():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p,POINTER(UInt32),POINTER(UInt32))(('I_RpcServerInqLocalConnAddress', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'AddressFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerInqRemoteConnAddress():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p,POINTER(UInt32),POINTER(UInt32))(('I_RpcServerInqRemoteConnAddress', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'AddressFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcSessionStrictContextHandle():
    try:
        return WINFUNCTYPE(Void,)(('I_RpcSessionStrictContextHandle', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcTurnOnEEInfoPropagation():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('I_RpcTurnOnEEInfoPropagation', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerInqTransportType():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt32))(('I_RpcServerInqTransportType', windll['RPCRT4.dll']), ((1, 'Type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcMapWin32Status():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Rpc.RPC_STATUS)(('I_RpcMapWin32Status', windll['RPCRT4.dll']), ((1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcRecordCalloutFailure():
    try:
        return WINFUNCTYPE(Void,win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RDR_CALLOUT_STATE_head),POINTER(UInt16))(('I_RpcRecordCalloutFailure', windll['RPCRT4.dll']), ((1, 'RpcStatus'),(1, 'CallOutState'),(1, 'DllName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcMgmtEnableDedicatedThreadPool():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('I_RpcMgmtEnableDedicatedThreadPool', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcGetDefaultSD():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('I_RpcGetDefaultSD', windll['RPCRT4.dll']), ((1, 'ppSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcOpenClientProcess():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,POINTER(c_void_p))(('I_RpcOpenClientProcess', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'DesiredAccess'),(1, 'ClientProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingIsServerLocal():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32))(('I_RpcBindingIsServerLocal', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'ServerLocalFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingSetPrivateOption():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,UIntPtr)(('I_RpcBindingSetPrivateOption', windll['RPCRT4.dll']), ((1, 'hBinding'),(1, 'option'),(1, 'optionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerSubscribeForDisconnectNotification():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)(('I_RpcServerSubscribeForDisconnectNotification', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerGetAssociationID():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(UInt32))(('I_RpcServerGetAssociationID', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'AssociationID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerDisableExceptionFilter():
    try:
        return WINFUNCTYPE(Int32,)(('I_RpcServerDisableExceptionFilter', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerSubscribeForDisconnectNotification2():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p,POINTER(Guid))(('I_RpcServerSubscribeForDisconnectNotification2', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'hEvent'),(1, 'SubscriptionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcServerUnsubscribeForDisconnectNotification():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,Guid)(('I_RpcServerUnsubscribeForDisconnectNotification', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'SubscriptionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingExportA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,c_void_p,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingExportA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'BindingVec'),(1, 'ObjectUuidVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingUnexportA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,c_void_p,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingUnexportA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjectUuidVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingExportW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),c_void_p,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingExportW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'BindingVec'),(1, 'ObjectUuidVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingUnexportW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),c_void_p,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingUnexportW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjectUuidVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingExportPnPA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,c_void_p,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingExportPnPA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjectVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingUnexportPnPA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,c_void_p,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingUnexportPnPA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjectVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingExportPnPW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),c_void_p,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingExportPnPW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjectVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingUnexportPnPW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),c_void_p,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsBindingUnexportPnPW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjectVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingLookupBeginA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,c_void_p,POINTER(Guid),UInt32,POINTER(c_void_p))(('RpcNsBindingLookupBeginA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjUuid'),(1, 'BindingMaxCount'),(1, 'LookupContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingLookupBeginW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),c_void_p,POINTER(Guid),UInt32,POINTER(c_void_p))(('RpcNsBindingLookupBeginW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjUuid'),(1, 'BindingMaxCount'),(1, 'LookupContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingLookupNext():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head)))(('RpcNsBindingLookupNext', windll['RPCNS4.dll']), ((1, 'LookupContext'),(1, 'BindingVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingLookupDone():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcNsBindingLookupDone', windll['RPCNS4.dll']), ((1, 'LookupContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupDeleteA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.GROUP_NAME_SYNTAX,c_char_p_no)(('RpcNsGroupDeleteA', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrAddA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,UInt32,c_char_p_no)(('RpcNsGroupMbrAddA', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),(1, 'MemberNameSyntax'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrRemoveA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,UInt32,c_char_p_no)(('RpcNsGroupMbrRemoveA', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),(1, 'MemberNameSyntax'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrInqBeginA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,UInt32,POINTER(c_void_p))(('RpcNsGroupMbrInqBeginA', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),(1, 'MemberNameSyntax'),(1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrInqNextA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_char_p_no))(('RpcNsGroupMbrInqNextA', windll['RPCNS4.dll']), ((1, 'InquiryContext'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupDeleteW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.GROUP_NAME_SYNTAX,POINTER(UInt16))(('RpcNsGroupDeleteW', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrAddW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),UInt32,POINTER(UInt16))(('RpcNsGroupMbrAddW', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),(1, 'MemberNameSyntax'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrRemoveW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),UInt32,POINTER(UInt16))(('RpcNsGroupMbrRemoveW', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),(1, 'MemberNameSyntax'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrInqBeginW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),UInt32,POINTER(c_void_p))(('RpcNsGroupMbrInqBeginW', windll['RPCNS4.dll']), ((1, 'GroupNameSyntax'),(1, 'GroupName'),(1, 'MemberNameSyntax'),(1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrInqNextW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(POINTER(UInt16)))(('RpcNsGroupMbrInqNextW', windll['RPCNS4.dll']), ((1, 'InquiryContext'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsGroupMbrInqDone():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcNsGroupMbrInqDone', windll['RPCNS4.dll']), ((1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileDeleteA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no)(('RpcNsProfileDeleteA', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltAddA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,c_char_p_no,UInt32,c_char_p_no)(('RpcNsProfileEltAddA', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),(1, 'IfId'),(1, 'MemberNameSyntax'),(1, 'MemberName'),(1, 'Priority'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltRemoveA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,c_char_p_no)(('RpcNsProfileEltRemoveA', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),(1, 'IfId'),(1, 'MemberNameSyntax'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltInqBeginA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,UInt32,POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,UInt32,c_char_p_no,POINTER(c_void_p))(('RpcNsProfileEltInqBeginA', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),(1, 'InquiryType'),(1, 'IfId'),(1, 'VersOption'),(1, 'MemberNameSyntax'),(1, 'MemberName'),(1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltInqNextA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_IF_ID_head),POINTER(c_char_p_no),POINTER(UInt32),POINTER(c_char_p_no))(('RpcNsProfileEltInqNextA', windll['RPCNS4.dll']), ((1, 'InquiryContext'),(1, 'IfId'),(1, 'MemberName'),(1, 'Priority'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileDeleteW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16))(('RpcNsProfileDeleteW', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltAddW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,POINTER(UInt16),UInt32,POINTER(UInt16))(('RpcNsProfileEltAddW', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),(1, 'IfId'),(1, 'MemberNameSyntax'),(1, 'MemberName'),(1, 'Priority'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltRemoveW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,POINTER(UInt16))(('RpcNsProfileEltRemoveW', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),(1, 'IfId'),(1, 'MemberNameSyntax'),(1, 'MemberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltInqBeginW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),UInt32,POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,UInt32,POINTER(UInt16),POINTER(c_void_p))(('RpcNsProfileEltInqBeginW', windll['RPCNS4.dll']), ((1, 'ProfileNameSyntax'),(1, 'ProfileName'),(1, 'InquiryType'),(1, 'IfId'),(1, 'VersOption'),(1, 'MemberNameSyntax'),(1, 'MemberName'),(1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltInqNextW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_IF_ID_head),POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(POINTER(UInt16)))(('RpcNsProfileEltInqNextW', windll['RPCNS4.dll']), ((1, 'InquiryContext'),(1, 'IfId'),(1, 'MemberName'),(1, 'Priority'),(1, 'Annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsProfileEltInqDone():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcNsProfileEltInqDone', windll['RPCNS4.dll']), ((1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsEntryObjectInqBeginA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,POINTER(c_void_p))(('RpcNsEntryObjectInqBeginA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsEntryObjectInqBeginW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(c_void_p))(('RpcNsEntryObjectInqBeginW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsEntryObjectInqNext():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid))(('RpcNsEntryObjectInqNext', windll['RPCNS4.dll']), ((1, 'InquiryContext'),(1, 'ObjUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsEntryObjectInqDone():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcNsEntryObjectInqDone', windll['RPCNS4.dll']), ((1, 'InquiryContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsEntryExpandNameA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,POINTER(c_char_p_no))(('RpcNsEntryExpandNameA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'ExpandedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtBindingUnexportA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsMgmtBindingUnexportA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfId'),(1, 'VersOption'),(1, 'ObjectUuidVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtEntryCreateA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no)(('RpcNsMgmtEntryCreateA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtEntryDeleteA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no)(('RpcNsMgmtEntryDeleteA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtEntryInqIfIdsA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,POINTER(POINTER(win32more.System.Rpc.RPC_IF_ID_VECTOR_head)))(('RpcNsMgmtEntryInqIfIdsA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfIdVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtHandleSetExpAge():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32)(('RpcNsMgmtHandleSetExpAge', windll['RPCNS4.dll']), ((1, 'NsHandle'),(1, 'ExpirationAge'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtInqExpAge():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt32))(('RpcNsMgmtInqExpAge', windll['RPCNS4.dll']), ((1, 'ExpirationAge'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtSetExpAge():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32)(('RpcNsMgmtSetExpAge', windll['RPCNS4.dll']), ((1, 'ExpirationAge'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsEntryExpandNameW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(POINTER(UInt16)))(('RpcNsEntryExpandNameW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'ExpandedName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtBindingUnexportW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(win32more.System.Rpc.RPC_IF_ID_head),UInt32,POINTER(win32more.System.Rpc.UUID_VECTOR_head))(('RpcNsMgmtBindingUnexportW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfId'),(1, 'VersOption'),(1, 'ObjectUuidVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtEntryCreateW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16))(('RpcNsMgmtEntryCreateW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtEntryDeleteW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16))(('RpcNsMgmtEntryDeleteW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsMgmtEntryInqIfIdsW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),POINTER(POINTER(win32more.System.Rpc.RPC_IF_ID_VECTOR_head)))(('RpcNsMgmtEntryInqIfIdsW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfIdVec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingImportBeginA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,c_char_p_no,c_void_p,POINTER(Guid),POINTER(c_void_p))(('RpcNsBindingImportBeginA', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjUuid'),(1, 'ImportContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingImportBeginW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,UInt32,POINTER(UInt16),c_void_p,POINTER(Guid),POINTER(c_void_p))(('RpcNsBindingImportBeginW', windll['RPCNS4.dll']), ((1, 'EntryNameSyntax'),(1, 'EntryName'),(1, 'IfSpec'),(1, 'ObjUuid'),(1, 'ImportContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingImportNext():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(c_void_p))(('RpcNsBindingImportNext', windll['RPCNS4.dll']), ((1, 'ImportContext'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingImportDone():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcNsBindingImportDone', windll['RPCNS4.dll']), ((1, 'ImportContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcNsBindingSelect():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head),POINTER(c_void_p))(('RpcNsBindingSelect', windll['RPCNS4.dll']), ((1, 'BindingVec'),(1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcAsyncRegisterInfo():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head))(('RpcAsyncRegisterInfo', windll['RPCRT4.dll']), ((1, 'pAsync'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcAsyncInitializeHandle():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head),UInt32)(('RpcAsyncInitializeHandle', windll['RPCRT4.dll']), ((1, 'pAsync'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcAsyncGetCallStatus():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head))(('RpcAsyncGetCallStatus', windll['RPCRT4.dll']), ((1, 'pAsync'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcAsyncCompleteCall():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head),c_void_p)(('RpcAsyncCompleteCall', windll['RPCRT4.dll']), ((1, 'pAsync'),(1, 'Reply'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcAsyncAbortCall():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head),UInt32)(('RpcAsyncAbortCall', windll['RPCRT4.dll']), ((1, 'pAsync'),(1, 'ExceptionCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcAsyncCancelCall():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head),win32more.Foundation.BOOL)(('RpcAsyncCancelCall', windll['RPCRT4.dll']), ((1, 'pAsync'),(1, 'fAbort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorStartEnumeration():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head))(('RpcErrorStartEnumeration', windll['RPCRT4.dll']), ((1, 'EnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorGetNextRecord():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head),win32more.Foundation.BOOL,POINTER(win32more.System.Rpc.RPC_EXTENDED_ERROR_INFO_head))(('RpcErrorGetNextRecord', windll['RPCRT4.dll']), ((1, 'EnumHandle'),(1, 'CopyStrings'),(1, 'ErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorEndEnumeration():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head))(('RpcErrorEndEnumeration', windll['RPCRT4.dll']), ((1, 'EnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorResetEnumeration():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head))(('RpcErrorResetEnumeration', windll['RPCRT4.dll']), ((1, 'EnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorGetNumberOfRecords():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head),POINTER(Int32))(('RpcErrorGetNumberOfRecords', windll['RPCRT4.dll']), ((1, 'EnumHandle'),(1, 'Records'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorSaveErrorInfo():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head),POINTER(c_void_p),POINTER(UIntPtr))(('RpcErrorSaveErrorInfo', windll['RPCRT4.dll']), ((1, 'EnumHandle'),(1, 'ErrorBlob'),(1, 'BlobSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorLoadErrorInfo():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UIntPtr,POINTER(win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head))(('RpcErrorLoadErrorInfo', windll['RPCRT4.dll']), ((1, 'ErrorBlob'),(1, 'BlobSize'),(1, 'EnumHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorAddRecord():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_EXTENDED_ERROR_INFO_head))(('RpcErrorAddRecord', windll['RPCRT4.dll']), ((1, 'ErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcErrorClearInformation():
    try:
        return WINFUNCTYPE(Void,)(('RpcErrorClearInformation', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcGetAuthorizationContextForClient():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Foundation.LARGE_INTEGER_head),win32more.Foundation.LUID,UInt32,c_void_p,POINTER(c_void_p))(('RpcGetAuthorizationContextForClient', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'ImpersonateOnReturn'),(1, 'Reserved1'),(1, 'pExpirationTime'),(1, 'Reserved2'),(1, 'Reserved3'),(1, 'Reserved4'),(1, 'pAuthzClientContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcFreeAuthorizationContext():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcFreeAuthorizationContext', windll['RPCRT4.dll']), ((1, 'pAuthzClientContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsContextLockExclusive():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)(('RpcSsContextLockExclusive', windll['RPCRT4.dll']), ((1, 'ServerBindingHandle'),(1, 'UserContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsContextLockShared():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)(('RpcSsContextLockShared', windll['RPCRT4.dll']), ((1, 'ServerBindingHandle'),(1, 'UserContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqCallAttributesW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)(('RpcServerInqCallAttributesW', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'RpcCallAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerInqCallAttributesA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)(('RpcServerInqCallAttributesA', windll['RPCRT4.dll']), ((1, 'ClientBinding'),(1, 'RpcCallAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerSubscribeForNotification():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,win32more.System.Rpc.RPC_NOTIFICATIONS,win32more.System.Rpc.RPC_NOTIFICATION_TYPES,POINTER(win32more.System.Rpc.RPC_ASYNC_NOTIFICATION_INFO_head))(('RpcServerSubscribeForNotification', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Notification'),(1, 'NotificationType'),(1, 'NotificationInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcServerUnsubscribeForNotification():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,win32more.System.Rpc.RPC_NOTIFICATIONS,POINTER(UInt32))(('RpcServerUnsubscribeForNotification', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'Notification'),(1, 'NotificationsQueued'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingBind():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head),c_void_p,c_void_p)(('RpcBindingBind', windll['RPCRT4.dll']), ((1, 'pAsync'),(1, 'Binding'),(1, 'IfSpec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcBindingUnbind():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcBindingUnbind', windll['RPCRT4.dll']), ((1, 'Binding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcAsyncSetHandle():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head))(('I_RpcAsyncSetHandle', windll['RPCRT4.dll']), ((1, 'Message'),(1, 'pAsync'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcAsyncAbortCall():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head),UInt32)(('I_RpcAsyncAbortCall', windll['RPCRT4.dll']), ((1, 'pAsync'),(1, 'ExceptionCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcExceptionFilter():
    try:
        return WINFUNCTYPE(Int32,UInt32)(('I_RpcExceptionFilter', windll['RPCRT4.dll']), ((1, 'ExceptionCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcBindingInqClientTokenAttributes():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.Foundation.LUID_head),POINTER(win32more.Foundation.LUID_head),POINTER(win32more.Foundation.LUID_head))(('I_RpcBindingInqClientTokenAttributes', windll['RPCRT4.dll']), ((1, 'Binding'),(1, 'TokenId'),(1, 'AuthenticationId'),(1, 'ModifiedId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNsGetBuffer():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcNsGetBuffer', windll['RPCNS4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNsSendReceive():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(c_void_p))(('I_RpcNsSendReceive', windll['RPCNS4.dll']), ((1, 'Message'),(1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcNsRaiseException():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),win32more.System.Rpc.RPC_STATUS)(('I_RpcNsRaiseException', windll['RPCNS4.dll']), ((1, 'Message'),(1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_I_RpcReBindBuffer():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('I_RpcReBindBuffer', windll['RPCNS4.dll']), ((1, 'Message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRCContextBinding():
    try:
        return WINFUNCTYPE(c_void_p,IntPtr)(('NDRCContextBinding', windll['RPCRT4.dll']), ((1, 'CContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRCContextMarshall():
    try:
        return WINFUNCTYPE(Void,IntPtr,c_void_p)(('NDRCContextMarshall', windll['RPCRT4.dll']), ((1, 'CContext'),(1, 'pBuff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRCContextUnmarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(IntPtr),c_void_p,c_void_p,UInt32)(('NDRCContextUnmarshall', windll['RPCRT4.dll']), ((1, 'pCContext'),(1, 'hBinding'),(1, 'pBuff'),(1, 'DataRepresentation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRSContextMarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),c_void_p,win32more.System.Rpc.NDR_RUNDOWN)(('NDRSContextMarshall', windll['RPCRT4.dll']), ((1, 'CContext'),(1, 'pBuff'),(1, 'userRunDownIn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRSContextUnmarshall():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),c_void_p,UInt32)(('NDRSContextUnmarshall', windll['RPCRT4.dll']), ((1, 'pBuff'),(1, 'DataRepresentation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRSContextMarshallEx():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),c_void_p,win32more.System.Rpc.NDR_RUNDOWN)(('NDRSContextMarshallEx', windll['RPCRT4.dll']), ((1, 'BindingHandle'),(1, 'CContext'),(1, 'pBuff'),(1, 'userRunDownIn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRSContextMarshall2():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),c_void_p,win32more.System.Rpc.NDR_RUNDOWN,c_void_p,UInt32)(('NDRSContextMarshall2', windll['RPCRT4.dll']), ((1, 'BindingHandle'),(1, 'CContext'),(1, 'pBuff'),(1, 'userRunDownIn'),(1, 'CtxGuard'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRSContextUnmarshallEx():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),c_void_p,c_void_p,UInt32)(('NDRSContextUnmarshallEx', windll['RPCRT4.dll']), ((1, 'BindingHandle'),(1, 'pBuff'),(1, 'DataRepresentation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NDRSContextUnmarshall2():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),c_void_p,c_void_p,UInt32,c_void_p,UInt32)(('NDRSContextUnmarshall2', windll['RPCRT4.dll']), ((1, 'BindingHandle'),(1, 'pBuff'),(1, 'DataRepresentation'),(1, 'CtxGuard'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsDestroyClientContext():
    try:
        return WINFUNCTYPE(Void,POINTER(c_void_p))(('RpcSsDestroyClientContext', windll['RPCRT4.dll']), ((1, 'ContextHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSimpleTypeMarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,Byte)(('NdrSimpleTypeMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'FormatChar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPointerMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrPointerMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSimpleStructMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrSimpleStructMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStructMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantStructMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingStructMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantVaryingStructMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexStructMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrComplexStructMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFixedArrayMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrFixedArrayMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantArrayMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantArrayMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingArrayMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantVaryingArrayMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrVaryingArrayMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrVaryingArrayMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexArrayMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrComplexArrayMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonConformantStringMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrNonConformantStringMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStringMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantStringMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrEncapsulatedUnionMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrEncapsulatedUnionMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonEncapsulatedUnionMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrNonEncapsulatedUnionMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrByteCountPointerMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrByteCountPointerMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrXmitOrRepAsMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrXmitOrRepAsMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrUserMarshalMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrUserMarshalMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrInterfacePointerMarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrInterfacePointerMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrClientContextMarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),IntPtr,Int32)(('NdrClientContextMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ContextHandle'),(1, 'fCheck'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerContextMarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),win32more.System.Rpc.NDR_RUNDOWN)(('NdrServerContextMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ContextHandle'),(1, 'RundownRoutine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerContextNewMarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),win32more.System.Rpc.NDR_RUNDOWN,c_char_p_no)(('NdrServerContextNewMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ContextHandle'),(1, 'RundownRoutine'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSimpleTypeUnmarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,Byte)(('NdrSimpleTypeUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'FormatChar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRangeUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrRangeUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrCorrelationInitialize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_void_p,UInt32,UInt32)(('NdrCorrelationInitialize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'CacheSize'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrCorrelationPass():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrCorrelationPass', windll['RPCRT4.dll']), ((1, 'pStubMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrCorrelationFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrCorrelationFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPointerUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrPointerUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSimpleStructUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrSimpleStructUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStructUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrConformantStructUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingStructUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrConformantVaryingStructUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexStructUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrComplexStructUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFixedArrayUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrFixedArrayUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantArrayUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrConformantArrayUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingArrayUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrConformantVaryingArrayUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrVaryingArrayUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrVaryingArrayUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexArrayUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrComplexArrayUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonConformantStringUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrNonConformantStringUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStringUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrConformantStringUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrEncapsulatedUnionUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrEncapsulatedUnionUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonEncapsulatedUnionUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrNonEncapsulatedUnionUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrByteCountPointerUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrByteCountPointerUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrXmitOrRepAsUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrXmitOrRepAsUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrUserMarshalUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrUserMarshalUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrInterfacePointerUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_char_p_no),c_char_p_no,Byte)(('NdrInterfacePointerUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),(1, 'fMustAlloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrClientContextUnmarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(IntPtr),c_void_p)(('NdrClientContextUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pContextHandle'),(1, 'BindHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerContextUnmarshall():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrServerContextUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrContextHandleInitialize():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrContextHandleInitialize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerContextNewUnmarshall():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrServerContextNewUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPointerBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrPointerBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSimpleStructBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrSimpleStructBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStructBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantStructBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingStructBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantVaryingStructBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexStructBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrComplexStructBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFixedArrayBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrFixedArrayBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantArrayBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantArrayBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingArrayBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantVaryingArrayBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrVaryingArrayBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrVaryingArrayBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexArrayBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrComplexArrayBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStringBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantStringBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonConformantStringBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrNonConformantStringBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrEncapsulatedUnionBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrEncapsulatedUnionBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonEncapsulatedUnionBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrNonEncapsulatedUnionBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrByteCountPointerBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrByteCountPointerBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrXmitOrRepAsBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrXmitOrRepAsBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrUserMarshalBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrUserMarshalBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrInterfacePointerBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrInterfacePointerBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrContextHandleSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrContextHandleSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPointerMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrPointerMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSimpleStructMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrSimpleStructMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStructMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrConformantStructMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingStructMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrConformantVaryingStructMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexStructMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrComplexStructMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFixedArrayMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrFixedArrayMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantArrayMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrConformantArrayMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingArrayMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrConformantVaryingArrayMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrVaryingArrayMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrVaryingArrayMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexArrayMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrComplexArrayMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStringMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrConformantStringMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonConformantStringMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrNonConformantStringMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrEncapsulatedUnionMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrEncapsulatedUnionMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonEncapsulatedUnionMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrNonEncapsulatedUnionMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrXmitOrRepAsMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrXmitOrRepAsMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrUserMarshalMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrUserMarshalMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrInterfacePointerMemorySize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrInterfacePointerMemorySize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPointerFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrPointerFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSimpleStructFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrSimpleStructFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantStructFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantStructFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingStructFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantVaryingStructFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexStructFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrComplexStructFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFixedArrayFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrFixedArrayFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantArrayFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantArrayFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConformantVaryingArrayFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrConformantVaryingArrayFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrVaryingArrayFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrVaryingArrayFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrComplexArrayFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrComplexArrayFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrEncapsulatedUnionFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrEncapsulatedUnionFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNonEncapsulatedUnionFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrNonEncapsulatedUnionFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrByteCountPointerFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrByteCountPointerFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrXmitOrRepAsFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrXmitOrRepAsFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrUserMarshalFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrUserMarshalFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrInterfacePointerFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_char_p_no)(('NdrInterfacePointerFree', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConvert2():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,Int32)(('NdrConvert2', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),(1, 'NumberParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrConvert():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrConvert', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrUserMarshalSimpleTypeConvert():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,Byte)(('NdrUserMarshalSimpleTypeConvert', windll['RPCRT4.dll']), ((1, 'pFlags'),(1, 'pBuffer'),(1, 'FormatChar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrClientInitializeNew():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),UInt32)(('NdrClientInitializeNew', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),(1, 'pStubMsg'),(1, 'pStubDescriptor'),(1, 'ProcNum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerInitializeNew():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head))(('NdrServerInitializeNew', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),(1, 'pStubMsg'),(1, 'pStubDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerInitializePartial():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),UInt32)(('NdrServerInitializePartial', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),(1, 'pStubMsg'),(1, 'pStubDescriptor'),(1, 'RequestedBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrClientInitialize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),UInt32)(('NdrClientInitialize', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),(1, 'pStubMsg'),(1, 'pStubDescriptor'),(1, 'ProcNum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerInitialize():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head))(('NdrServerInitialize', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),(1, 'pStubMsg'),(1, 'pStubDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerInitializeUnmarshall():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('NdrServerInitializeUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pStubDescriptor'),(1, 'pRpcMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerInitializeMarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrServerInitializeMarshall', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),(1, 'pStubMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrGetBuffer():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),UInt32,c_void_p)(('NdrGetBuffer', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'BufferLength'),(1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNsGetBuffer():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),UInt32,c_void_p)(('NdrNsGetBuffer', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'BufferLength'),(1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrSendReceive():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no)(('NdrSendReceive', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pBufferEnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrNsSendReceive():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,POINTER(c_void_p))(('NdrNsSendReceive', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pBufferEnd'),(1, 'pAutoHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFreeBuffer():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrFreeBuffer', windll['RPCRT4.dll']), ((1, 'pStubMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrGetDcomProtocolVersion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(win32more.System.Rpc.RPC_VERSION_head))(('NdrGetDcomProtocolVersion', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrClientCall2():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no)(('NdrClientCall2', cdll['RPCRT4.dll']), ((1, 'pStubDescriptor'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrAsyncClientCall():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no)(('NdrAsyncClientCall', cdll['RPCRT4.dll']), ((1, 'pStubDescriptor'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrDcomAsyncClientCall():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no)(('NdrDcomAsyncClientCall', cdll['RPCRT4.dll']), ((1, 'pStubDescriptor'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrAsyncServerCall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('NdrAsyncServerCall', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrDcomAsyncStubCall():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Com.IRpcStubBuffer_head,win32more.System.Com.IRpcChannelBuffer_head,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(UInt32))(('NdrDcomAsyncStubCall', windll['RPCRT4.dll']), ((1, 'pThis'),(1, 'pChannel'),(1, 'pRpcMsg'),(1, 'pdwStubPhase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrStubCall2():
    try:
        return WINFUNCTYPE(Int32,c_void_p,c_void_p,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(UInt32))(('NdrStubCall2', windll['RPCRT4.dll']), ((1, 'pThis'),(1, 'pChannel'),(1, 'pRpcMsg'),(1, 'pdwStubPhase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerCall2():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('NdrServerCall2', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMapCommAndFaultStatus():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(UInt32),POINTER(UInt32),win32more.System.Rpc.RPC_STATUS)(('NdrMapCommAndFaultStatus', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pCommStatus'),(1, 'pFaultStatus'),(1, 'Status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsAllocate():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr)(('RpcSsAllocate', windll['RPCRT4.dll']), ((1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsDisableAllocate():
    try:
        return WINFUNCTYPE(Void,)(('RpcSsDisableAllocate', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsEnableAllocate():
    try:
        return WINFUNCTYPE(Void,)(('RpcSsEnableAllocate', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsFree():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('RpcSsFree', windll['RPCRT4.dll']), ((1, 'NodeToFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsGetThreadHandle():
    try:
        return WINFUNCTYPE(c_void_p,)(('RpcSsGetThreadHandle', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsSetClientAllocFree():
    try:
        return WINFUNCTYPE(Void,win32more.System.Rpc.RPC_CLIENT_ALLOC,win32more.System.Rpc.RPC_CLIENT_FREE)(('RpcSsSetClientAllocFree', windll['RPCRT4.dll']), ((1, 'ClientAlloc'),(1, 'ClientFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsSetThreadHandle():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('RpcSsSetThreadHandle', windll['RPCRT4.dll']), ((1, 'Id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSsSwapClientAllocFree():
    try:
        return WINFUNCTYPE(Void,win32more.System.Rpc.RPC_CLIENT_ALLOC,win32more.System.Rpc.RPC_CLIENT_FREE,POINTER(win32more.System.Rpc.RPC_CLIENT_ALLOC),POINTER(win32more.System.Rpc.RPC_CLIENT_FREE))(('RpcSsSwapClientAllocFree', windll['RPCRT4.dll']), ((1, 'ClientAlloc'),(1, 'ClientFree'),(1, 'OldClientAlloc'),(1, 'OldClientFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmAllocate():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr,POINTER(win32more.System.Rpc.RPC_STATUS))(('RpcSmAllocate', windll['RPCRT4.dll']), ((1, 'Size'),(1, 'pStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmClientFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcSmClientFree', windll['RPCRT4.dll']), ((1, 'pNodeToFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmDestroyClientContext():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(c_void_p))(('RpcSmDestroyClientContext', windll['RPCRT4.dll']), ((1, 'ContextHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmDisableAllocate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('RpcSmDisableAllocate', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmEnableAllocate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,)(('RpcSmEnableAllocate', windll['RPCRT4.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcSmFree', windll['RPCRT4.dll']), ((1, 'NodeToFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmGetThreadHandle():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.Rpc.RPC_STATUS))(('RpcSmGetThreadHandle', windll['RPCRT4.dll']), ((1, 'pStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmSetClientAllocFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.RPC_CLIENT_ALLOC,win32more.System.Rpc.RPC_CLIENT_FREE)(('RpcSmSetClientAllocFree', windll['RPCRT4.dll']), ((1, 'ClientAlloc'),(1, 'ClientFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmSetThreadHandle():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('RpcSmSetThreadHandle', windll['RPCRT4.dll']), ((1, 'Id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcSmSwapClientAllocFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.RPC_CLIENT_ALLOC,win32more.System.Rpc.RPC_CLIENT_FREE,POINTER(win32more.System.Rpc.RPC_CLIENT_ALLOC),POINTER(win32more.System.Rpc.RPC_CLIENT_FREE))(('RpcSmSwapClientAllocFree', windll['RPCRT4.dll']), ((1, 'ClientAlloc'),(1, 'ClientFree'),(1, 'OldClientAlloc'),(1, 'OldClientFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRpcSsEnableAllocate():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrRpcSsEnableAllocate', windll['RPCRT4.dll']), ((1, 'pMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRpcSsDisableAllocate():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrRpcSsDisableAllocate', windll['RPCRT4.dll']), ((1, 'pMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRpcSmSetClientToOsf():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))(('NdrRpcSmSetClientToOsf', windll['RPCRT4.dll']), ((1, 'pMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRpcSmClientAllocate():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr)(('NdrRpcSmClientAllocate', windll['RPCRT4.dll']), ((1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRpcSmClientFree():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('NdrRpcSmClientFree', windll['RPCRT4.dll']), ((1, 'NodeToFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRpcSsDefaultAllocate():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr)(('NdrRpcSsDefaultAllocate', windll['RPCRT4.dll']), ((1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrRpcSsDefaultFree():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('NdrRpcSsDefaultFree', windll['RPCRT4.dll']), ((1, 'NodeToFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFullPointerXlatInit():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Rpc.FULL_PTR_XLAT_TABLES_head),UInt32,win32more.System.Rpc.XLAT_SIDE)(('NdrFullPointerXlatInit', windll['RPCRT4.dll']), ((1, 'NumberOfPointers'),(1, 'XlatSide'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrFullPointerXlatFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.FULL_PTR_XLAT_TABLES_head))(('NdrFullPointerXlatFree', windll['RPCRT4.dll']), ((1, 'pXlatTables'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrAllocate():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),UIntPtr)(('NdrAllocate', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'Len'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrClearOutParameters():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_char_p_no,c_void_p)(('NdrClearOutParameters', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pFormat'),(1, 'ArgAddr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrOleAllocate():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr)(('NdrOleAllocate', windll['RPCRT4.dll']), ((1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrOleFree():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('NdrOleFree', windll['RPCRT4.dll']), ((1, 'NodeToFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrGetUserMarshalInfo():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt32),UInt32,POINTER(win32more.System.Rpc.NDR_USER_MARSHAL_INFO_head))(('NdrGetUserMarshalInfo', windll['RPCRT4.dll']), ((1, 'pFlags'),(1, 'InformationLevel'),(1, 'pMarshalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrCreateServerInterfaceFromStub():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Com.IRpcStubBuffer_head,POINTER(win32more.System.Rpc.RPC_SERVER_INTERFACE_head))(('NdrCreateServerInterfaceFromStub', windll['RPCRT4.dll']), ((1, 'pStub'),(1, 'pServerIf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrClientCall3():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),UInt32,c_void_p)(('NdrClientCall3', cdll['RPCRT4.dll']), ((1, 'pProxyInfo'),(1, 'nProcNum'),(1, 'pReturnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Ndr64AsyncClientCall():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),UInt32,c_void_p)(('Ndr64AsyncClientCall', cdll['RPCRT4.dll']), ((1, 'pProxyInfo'),(1, 'nProcNum'),(1, 'pReturnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Ndr64DcomAsyncClientCall():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),UInt32,c_void_p)(('Ndr64DcomAsyncClientCall', cdll['RPCRT4.dll']), ((1, 'pProxyInfo'),(1, 'nProcNum'),(1, 'pReturnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Ndr64AsyncServerCall64():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('Ndr64AsyncServerCall64', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Ndr64AsyncServerCallAll():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('Ndr64AsyncServerCallAll', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Ndr64DcomAsyncStubCall():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Com.IRpcStubBuffer_head,win32more.System.Com.IRpcChannelBuffer_head,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(UInt32))(('Ndr64DcomAsyncStubCall', windll['RPCRT4.dll']), ((1, 'pThis'),(1, 'pChannel'),(1, 'pRpcMsg'),(1, 'pdwStubPhase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrStubCall3():
    try:
        return WINFUNCTYPE(Int32,c_void_p,c_void_p,POINTER(win32more.System.Rpc.RPC_MESSAGE_head),POINTER(UInt32))(('NdrStubCall3', windll['RPCRT4.dll']), ((1, 'pThis'),(1, 'pChannel'),(1, 'pRpcMsg'),(1, 'pdwStubPhase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerCallAll():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('NdrServerCallAll', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrServerCallNdr64():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))(('NdrServerCallNdr64', windll['RPCRT4.dll']), ((1, 'pRpcMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPartialIgnoreClientMarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_void_p)(('NdrPartialIgnoreClientMarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPartialIgnoreServerUnmarshall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_void_p))(('NdrPartialIgnoreServerUnmarshall', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPartialIgnoreClientBufferSize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),c_void_p)(('NdrPartialIgnoreClientBufferSize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'pMemory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrPartialIgnoreServerInitialize():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head),POINTER(c_void_p),c_char_p_no)(('NdrPartialIgnoreServerInitialize', windll['RPCRT4.dll']), ((1, 'pStubMsg'),(1, 'ppMemory'),(1, 'pFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcUserFree():
    try:
        return WINFUNCTYPE(Void,c_void_p,c_void_p)(('RpcUserFree', windll['RPCRT4.dll']), ((1, 'AsyncHandle'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesEncodeIncrementalHandleCreate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,win32more.System.Rpc.MIDL_ES_ALLOC,win32more.System.Rpc.MIDL_ES_WRITE,POINTER(c_void_p))(('MesEncodeIncrementalHandleCreate', windll['RPCRT4.dll']), ((1, 'UserState'),(1, 'AllocFn'),(1, 'WriteFn'),(1, 'pHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesDecodeIncrementalHandleCreate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,win32more.System.Rpc.MIDL_ES_READ,POINTER(c_void_p))(('MesDecodeIncrementalHandleCreate', windll['RPCRT4.dll']), ((1, 'UserState'),(1, 'ReadFn'),(1, 'pHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesIncrementalHandleReset():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p,win32more.System.Rpc.MIDL_ES_ALLOC,win32more.System.Rpc.MIDL_ES_WRITE,win32more.System.Rpc.MIDL_ES_READ,win32more.System.Rpc.MIDL_ES_CODE)(('MesIncrementalHandleReset', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'UserState'),(1, 'AllocFn'),(1, 'WriteFn'),(1, 'ReadFn'),(1, 'Operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesEncodeFixedBufferHandleCreate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),POINTER(c_void_p))(('MesEncodeFixedBufferHandleCreate', windll['RPCRT4.dll']), ((1, 'pBuffer'),(1, 'BufferSize'),(1, 'pEncodedSize'),(1, 'pHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesEncodeDynBufferHandleCreate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(POINTER(SByte)),POINTER(UInt32),POINTER(c_void_p))(('MesEncodeDynBufferHandleCreate', windll['RPCRT4.dll']), ((1, 'pBuffer'),(1, 'pEncodedSize'),(1, 'pHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesDecodeBufferHandleCreate():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.Foundation.PSTR,UInt32,POINTER(c_void_p))(('MesDecodeBufferHandleCreate', windll['RPCRT4.dll']), ((1, 'Buffer'),(1, 'BufferSize'),(1, 'pHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesBufferHandleReset():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,UInt32,win32more.System.Rpc.MIDL_ES_CODE,POINTER(POINTER(SByte)),UInt32,POINTER(UInt32))(('MesBufferHandleReset', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'HandleStyle'),(1, 'Operation'),(1, 'pBuffer'),(1, 'BufferSize'),(1, 'pEncodedSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesHandleFree():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p)(('MesHandleFree', windll['RPCRT4.dll']), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MesInqProcEncodingId():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER_head),POINTER(UInt32))(('MesInqProcEncodingId', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pInterfaceId'),(1, 'pProcNum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesSimpleTypeAlignSize():
    try:
        return WINFUNCTYPE(UIntPtr,c_void_p)(('NdrMesSimpleTypeAlignSize', windll['RPCRT4.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesSimpleTypeDecode():
    try:
        return WINFUNCTYPE(Void,c_void_p,c_void_p,Int16)(('NdrMesSimpleTypeDecode', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pObject'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesSimpleTypeEncode():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_void_p,Int16)(('NdrMesSimpleTypeEncode', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pStubDesc'),(1, 'pObject'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeAlignSize():
    try:
        return WINFUNCTYPE(UIntPtr,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no,c_void_p)(('NdrMesTypeAlignSize', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pStubDesc'),(1, 'pFormatString'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeEncode():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no,c_void_p)(('NdrMesTypeEncode', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pStubDesc'),(1, 'pFormatString'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeDecode():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no,c_void_p)(('NdrMesTypeDecode', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pStubDesc'),(1, 'pFormatString'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeAlignSize2():
    try:
        return WINFUNCTYPE(UIntPtr,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no,c_void_p)(('NdrMesTypeAlignSize2', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pStubDesc'),(1, 'pFormatString'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeEncode2():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no,c_void_p)(('NdrMesTypeEncode2', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pStubDesc'),(1, 'pFormatString'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeDecode2():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no,c_void_p)(('NdrMesTypeDecode2', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pStubDesc'),(1, 'pFormatString'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeFree2():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no,c_void_p)(('NdrMesTypeFree2', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pStubDesc'),(1, 'pFormatString'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesProcEncodeDecode():
    try:
        return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no)(('NdrMesProcEncodeDecode', cdll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pStubDesc'),(1, 'pFormatString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesProcEncodeDecode2():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head),c_char_p_no)(('NdrMesProcEncodeDecode2', cdll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pStubDesc'),(1, 'pFormatString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeAlignSize3():
    try:
        return WINFUNCTYPE(UIntPtr,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),POINTER(POINTER(UInt32)),UInt32,c_void_p)(('NdrMesTypeAlignSize3', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pProxyInfo'),(1, 'ArrTypeOffset'),(1, 'nTypeIndex'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeEncode3():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),POINTER(POINTER(UInt32)),UInt32,c_void_p)(('NdrMesTypeEncode3', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pProxyInfo'),(1, 'ArrTypeOffset'),(1, 'nTypeIndex'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeDecode3():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),POINTER(POINTER(UInt32)),UInt32,c_void_p)(('NdrMesTypeDecode3', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pProxyInfo'),(1, 'ArrTypeOffset'),(1, 'nTypeIndex'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesTypeFree3():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head),POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),POINTER(POINTER(UInt32)),UInt32,c_void_p)(('NdrMesTypeFree3', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pPicklingInfo'),(1, 'pProxyInfo'),(1, 'ArrTypeOffset'),(1, 'nTypeIndex'),(1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesProcEncodeDecode3():
    try:
        return CFUNCTYPE(win32more.System.Rpc.CLIENT_CALL_RETURN,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),UInt32,c_void_p)(('NdrMesProcEncodeDecode3', cdll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pProxyInfo'),(1, 'nProcNum'),(1, 'pReturnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesSimpleTypeDecodeAll():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),c_void_p,Int16)(('NdrMesSimpleTypeDecodeAll', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pProxyInfo'),(1, 'pObject'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesSimpleTypeEncodeAll():
    try:
        return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head),c_void_p,Int16)(('NdrMesSimpleTypeEncodeAll', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pProxyInfo'),(1, 'pObject'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdrMesSimpleTypeAlignSizeAll():
    try:
        return WINFUNCTYPE(UIntPtr,c_void_p,POINTER(win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head))(('NdrMesSimpleTypeAlignSizeAll', windll['RPCRT4.dll']), ((1, 'Handle'),(1, 'pProxyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcCertGeneratePrincipalNameW():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),UInt32,POINTER(POINTER(UInt16)))(('RpcCertGeneratePrincipalNameW', windll['RPCRT4.dll']), ((1, 'Context'),(1, 'Flags'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RpcCertGeneratePrincipalNameA():
    try:
        return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),UInt32,POINTER(c_char_p_no))(('RpcCertGeneratePrincipalNameA', windll['RPCRT4.dll']), ((1, 'Context'),(1, 'Flags'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ARRAY_INFO_head():
    class ARRAY_INFO(Structure):
        pass
    return ARRAY_INFO
def _define_ARRAY_INFO():
    ARRAY_INFO = win32more.System.Rpc.ARRAY_INFO_head
    ARRAY_INFO._fields_ = [
        ('Dimension', Int32),
        ('BufferConformanceMark', POINTER(UInt32)),
        ('BufferVarianceMark', POINTER(UInt32)),
        ('MaxCountArray', POINTER(UInt32)),
        ('OffsetArray', POINTER(UInt32)),
        ('ActualCountArray', POINTER(UInt32)),
    ]
    return ARRAY_INFO
def _define_BinaryParam_head():
    class BinaryParam(Structure):
        pass
    return BinaryParam
def _define_BinaryParam():
    BinaryParam = win32more.System.Rpc.BinaryParam_head
    BinaryParam._fields_ = [
        ('Buffer', c_void_p),
        ('Size', Int16),
    ]
    return BinaryParam
def _define_CLIENT_CALL_RETURN_head():
    class CLIENT_CALL_RETURN(Union):
        pass
    return CLIENT_CALL_RETURN
def _define_CLIENT_CALL_RETURN():
    CLIENT_CALL_RETURN = win32more.System.Rpc.CLIENT_CALL_RETURN_head
    CLIENT_CALL_RETURN._fields_ = [
        ('Pointer', c_void_p),
        ('Simple', IntPtr),
    ]
    return CLIENT_CALL_RETURN
def _define_COMM_FAULT_OFFSETS_head():
    class COMM_FAULT_OFFSETS(Structure):
        pass
    return COMM_FAULT_OFFSETS
def _define_COMM_FAULT_OFFSETS():
    COMM_FAULT_OFFSETS = win32more.System.Rpc.COMM_FAULT_OFFSETS_head
    COMM_FAULT_OFFSETS._fields_ = [
        ('CommOffset', Int16),
        ('FaultOffset', Int16),
    ]
    return COMM_FAULT_OFFSETS
def _define_CS_TAG_GETTING_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,Int32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))
def _define_CS_TYPE_FROM_NETCS_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,UInt32,c_char_p_no,UInt32,UInt32,c_void_p,POINTER(UInt32),POINTER(UInt32))
def _define_CS_TYPE_LOCAL_SIZE_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,UInt32,UInt32,POINTER(win32more.System.Rpc.IDL_CS_CONVERT),POINTER(UInt32),POINTER(UInt32))
def _define_CS_TYPE_NET_SIZE_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,UInt32,UInt32,POINTER(win32more.System.Rpc.IDL_CS_CONVERT),POINTER(UInt32),POINTER(UInt32))
def _define_CS_TYPE_TO_NETCS_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,UInt32,c_void_p,UInt32,c_char_p_no,POINTER(UInt32),POINTER(UInt32))
def _define_EXPR_EVAL():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))
EXPR_TOKEN = Int32
FC_EXPR_START = 0
FC_EXPR_ILLEGAL = 0
FC_EXPR_CONST32 = 1
FC_EXPR_CONST64 = 2
FC_EXPR_VAR = 3
FC_EXPR_OPER = 4
FC_EXPR_NOOP = 5
FC_EXPR_END = 6
ExtendedErrorParamTypes = Int32
ExtendedErrorParamTypes_eeptAnsiString = 1
ExtendedErrorParamTypes_eeptUnicodeString = 2
ExtendedErrorParamTypes_eeptLongVal = 3
ExtendedErrorParamTypes_eeptShortVal = 4
ExtendedErrorParamTypes_eeptPointerVal = 5
ExtendedErrorParamTypes_eeptNone = 6
ExtendedErrorParamTypes_eeptBinary = 7
def _define_FULL_PTR_XLAT_TABLES_head():
    class FULL_PTR_XLAT_TABLES(Structure):
        pass
    return FULL_PTR_XLAT_TABLES
def _define_FULL_PTR_XLAT_TABLES():
    FULL_PTR_XLAT_TABLES = win32more.System.Rpc.FULL_PTR_XLAT_TABLES_head
    FULL_PTR_XLAT_TABLES._fields_ = [
        ('RefIdToPointer', c_void_p),
        ('PointerToRefId', c_void_p),
        ('NextRefId', UInt32),
        ('XlatSide', win32more.System.Rpc.XLAT_SIDE),
    ]
    return FULL_PTR_XLAT_TABLES
def _define_GENERIC_BINDING_INFO_head():
    class GENERIC_BINDING_INFO(Structure):
        pass
    return GENERIC_BINDING_INFO
def _define_GENERIC_BINDING_INFO():
    GENERIC_BINDING_INFO = win32more.System.Rpc.GENERIC_BINDING_INFO_head
    GENERIC_BINDING_INFO._fields_ = [
        ('pObj', c_void_p),
        ('Size', UInt32),
        ('pfnBind', win32more.System.Rpc.GENERIC_BINDING_ROUTINE),
        ('pfnUnbind', win32more.System.Rpc.GENERIC_UNBIND_ROUTINE),
    ]
    return GENERIC_BINDING_INFO
def _define_GENERIC_BINDING_ROUTINE():
    return WINFUNCTYPE(c_void_p,c_void_p)
def _define_GENERIC_BINDING_ROUTINE_PAIR_head():
    class GENERIC_BINDING_ROUTINE_PAIR(Structure):
        pass
    return GENERIC_BINDING_ROUTINE_PAIR
def _define_GENERIC_BINDING_ROUTINE_PAIR():
    GENERIC_BINDING_ROUTINE_PAIR = win32more.System.Rpc.GENERIC_BINDING_ROUTINE_PAIR_head
    GENERIC_BINDING_ROUTINE_PAIR._fields_ = [
        ('pfnBind', win32more.System.Rpc.GENERIC_BINDING_ROUTINE),
        ('pfnUnbind', win32more.System.Rpc.GENERIC_UNBIND_ROUTINE),
    ]
    return GENERIC_BINDING_ROUTINE_PAIR
def _define_GENERIC_UNBIND_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,c_char_p_no)
GROUP_NAME_SYNTAX = UInt32
RPC_C_NS_SYNTAX_DEFAULT = 0
RPC_C_NS_SYNTAX_DCE = 3
def _define_I_RpcFreeCalloutStateFn():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RDR_CALLOUT_STATE_head))
def _define_I_RpcPerformCalloutFn():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(win32more.System.Rpc.RDR_CALLOUT_STATE_head),win32more.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE)
def _define_I_RpcProxyCallbackInterface_head():
    class I_RpcProxyCallbackInterface(Structure):
        pass
    return I_RpcProxyCallbackInterface
def _define_I_RpcProxyCallbackInterface():
    I_RpcProxyCallbackInterface = win32more.System.Rpc.I_RpcProxyCallbackInterface_head
    I_RpcProxyCallbackInterface._fields_ = [
        ('IsValidMachineFn', win32more.System.Rpc.I_RpcProxyIsValidMachineFn),
        ('GetClientAddressFn', win32more.System.Rpc.I_RpcProxyGetClientAddressFn),
        ('GetConnectionTimeoutFn', win32more.System.Rpc.I_RpcProxyGetConnectionTimeoutFn),
        ('PerformCalloutFn', win32more.System.Rpc.I_RpcPerformCalloutFn),
        ('FreeCalloutStateFn', win32more.System.Rpc.I_RpcFreeCalloutStateFn),
        ('GetClientSessionAndResourceUUIDFn', win32more.System.Rpc.I_RpcProxyGetClientSessionAndResourceUUID),
        ('ProxyFilterIfFn', win32more.System.Rpc.I_RpcProxyFilterIfFn),
        ('RpcProxyUpdatePerfCounterFn', win32more.System.Rpc.I_RpcProxyUpdatePerfCounterFn),
        ('RpcProxyUpdatePerfCounterBackendServerFn', win32more.System.Rpc.I_RpcProxyUpdatePerfCounterBackendServerFn),
    ]
    return I_RpcProxyCallbackInterface
def _define_I_RpcProxyFilterIfFn():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Guid),UInt16,POINTER(Int32))
def _define_I_RpcProxyGetClientAddressFn():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,win32more.Foundation.PSTR,POINTER(UInt32))
def _define_I_RpcProxyGetClientSessionAndResourceUUID():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,POINTER(Int32),POINTER(Guid),POINTER(Int32),POINTER(Guid))
def _define_I_RpcProxyGetConnectionTimeoutFn():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt32))
def _define_I_RpcProxyIsValidMachineFn():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(UInt16),POINTER(UInt16),UInt32)
def _define_I_RpcProxyUpdatePerfCounterBackendServerFn():
    return WINFUNCTYPE(Void,POINTER(UInt16),Int32)
def _define_I_RpcProxyUpdatePerfCounterFn():
    return WINFUNCTYPE(Void,win32more.System.Rpc.RpcPerfCounters,Int32,UInt32)
IDL_CS_CONVERT = Int32
IDL_CS_NO_CONVERT = 0
IDL_CS_IN_PLACE_CONVERT = 1
IDL_CS_NEW_BUFFER_CONVERT = 2
LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION = Int32
LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION_MarshalDirectionMarshal = 0
LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION_MarshalDirectionUnmarshal = 1
def _define_MALLOC_FREE_STRUCT_head():
    class MALLOC_FREE_STRUCT(Structure):
        pass
    return MALLOC_FREE_STRUCT
def _define_MALLOC_FREE_STRUCT():
    MALLOC_FREE_STRUCT = win32more.System.Rpc.MALLOC_FREE_STRUCT_head
    MALLOC_FREE_STRUCT._fields_ = [
        ('pfnAllocate', IntPtr),
        ('pfnFree', IntPtr),
    ]
    return MALLOC_FREE_STRUCT
def _define_MIDL_ES_ALLOC():
    return WINFUNCTYPE(Void,c_void_p,POINTER(POINTER(SByte)),POINTER(UInt32))
MIDL_ES_CODE = Int32
MES_ENCODE = 0
MES_DECODE = 1
MES_ENCODE_NDR64 = 2
MIDL_ES_HANDLE_STYLE = Int32
MES_INCREMENTAL_HANDLE = 0
MES_FIXED_BUFFER_HANDLE = 1
MES_DYNAMIC_BUFFER_HANDLE = 2
def _define_MIDL_ES_READ():
    return WINFUNCTYPE(Void,c_void_p,POINTER(POINTER(SByte)),POINTER(UInt32))
def _define_MIDL_ES_WRITE():
    return WINFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,UInt32)
def _define_MIDL_FORMAT_STRING_head():
    class MIDL_FORMAT_STRING(Structure):
        pass
    return MIDL_FORMAT_STRING
def _define_MIDL_FORMAT_STRING():
    MIDL_FORMAT_STRING = win32more.System.Rpc.MIDL_FORMAT_STRING_head
    MIDL_FORMAT_STRING._fields_ = [
        ('Pad', Int16),
        ('Format', Byte * 1),
    ]
    return MIDL_FORMAT_STRING
def _define_MIDL_INTERCEPTION_INFO_head():
    class MIDL_INTERCEPTION_INFO(Structure):
        pass
    return MIDL_INTERCEPTION_INFO
def _define_MIDL_INTERCEPTION_INFO():
    MIDL_INTERCEPTION_INFO = win32more.System.Rpc.MIDL_INTERCEPTION_INFO_head
    MIDL_INTERCEPTION_INFO._fields_ = [
        ('Version', UInt32),
        ('ProcString', c_char_p_no),
        ('ProcFormatOffsetTable', POINTER(UInt16)),
        ('ProcCount', UInt32),
        ('TypeString', c_char_p_no),
    ]
    return MIDL_INTERCEPTION_INFO
def _define_MIDL_INTERFACE_METHOD_PROPERTIES_head():
    class MIDL_INTERFACE_METHOD_PROPERTIES(Structure):
        pass
    return MIDL_INTERFACE_METHOD_PROPERTIES
def _define_MIDL_INTERFACE_METHOD_PROPERTIES():
    MIDL_INTERFACE_METHOD_PROPERTIES = win32more.System.Rpc.MIDL_INTERFACE_METHOD_PROPERTIES_head
    MIDL_INTERFACE_METHOD_PROPERTIES._fields_ = [
        ('MethodCount', UInt16),
        ('MethodProperties', POINTER(POINTER(win32more.System.Rpc.MIDL_METHOD_PROPERTY_MAP_head))),
    ]
    return MIDL_INTERFACE_METHOD_PROPERTIES
def _define_MIDL_METHOD_PROPERTY_head():
    class MIDL_METHOD_PROPERTY(Structure):
        pass
    return MIDL_METHOD_PROPERTY
def _define_MIDL_METHOD_PROPERTY():
    MIDL_METHOD_PROPERTY = win32more.System.Rpc.MIDL_METHOD_PROPERTY_head
    MIDL_METHOD_PROPERTY._fields_ = [
        ('Id', UInt32),
        ('Value', UIntPtr),
    ]
    return MIDL_METHOD_PROPERTY
def _define_MIDL_METHOD_PROPERTY_MAP_head():
    class MIDL_METHOD_PROPERTY_MAP(Structure):
        pass
    return MIDL_METHOD_PROPERTY_MAP
def _define_MIDL_METHOD_PROPERTY_MAP():
    MIDL_METHOD_PROPERTY_MAP = win32more.System.Rpc.MIDL_METHOD_PROPERTY_MAP_head
    MIDL_METHOD_PROPERTY_MAP._fields_ = [
        ('Count', UInt32),
        ('Properties', POINTER(win32more.System.Rpc.MIDL_METHOD_PROPERTY_head)),
    ]
    return MIDL_METHOD_PROPERTY_MAP
def _define_MIDL_SERVER_INFO_head():
    class MIDL_SERVER_INFO(Structure):
        pass
    return MIDL_SERVER_INFO
def _define_MIDL_SERVER_INFO():
    MIDL_SERVER_INFO = win32more.System.Rpc.MIDL_SERVER_INFO_head
    MIDL_SERVER_INFO._fields_ = [
        ('pStubDesc', POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head)),
        ('DispatchTable', POINTER(win32more.System.Rpc.SERVER_ROUTINE)),
        ('ProcString', c_char_p_no),
        ('FmtStringOffset', POINTER(UInt16)),
        ('ThunkTable', POINTER(win32more.System.Rpc.STUB_THUNK)),
        ('pTransferSyntax', POINTER(win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER_head)),
        ('nCount', UIntPtr),
        ('pSyntaxInfo', POINTER(win32more.System.Rpc.MIDL_SYNTAX_INFO_head)),
    ]
    return MIDL_SERVER_INFO
def _define_MIDL_STUB_DESC_head():
    class MIDL_STUB_DESC(Structure):
        pass
    return MIDL_STUB_DESC
def _define_MIDL_STUB_DESC():
    MIDL_STUB_DESC = win32more.System.Rpc.MIDL_STUB_DESC_head
    class MIDL_STUB_DESC__IMPLICIT_HANDLE_INFO_e__Union(Union):
        pass
    MIDL_STUB_DESC__IMPLICIT_HANDLE_INFO_e__Union._fields_ = [
        ('pAutoHandle', POINTER(c_void_p)),
        ('pPrimitiveHandle', POINTER(c_void_p)),
        ('pGenericBindingInfo', POINTER(win32more.System.Rpc.GENERIC_BINDING_INFO_head)),
    ]
    MIDL_STUB_DESC._fields_ = [
        ('RpcInterfaceInformation', c_void_p),
        ('pfnAllocate', IntPtr),
        ('pfnFree', IntPtr),
        ('IMPLICIT_HANDLE_INFO', MIDL_STUB_DESC__IMPLICIT_HANDLE_INFO_e__Union),
        ('apfnNdrRundownRoutines', POINTER(win32more.System.Rpc.NDR_RUNDOWN)),
        ('aGenericBindingRoutinePairs', POINTER(win32more.System.Rpc.GENERIC_BINDING_ROUTINE_PAIR_head)),
        ('apfnExprEval', POINTER(win32more.System.Rpc.EXPR_EVAL)),
        ('aXmitQuintuple', POINTER(win32more.System.Rpc.XMIT_ROUTINE_QUINTUPLE_head)),
        ('pFormatTypes', c_char_p_no),
        ('fCheckBounds', Int32),
        ('Version', UInt32),
        ('pMallocFreeStruct', POINTER(win32more.System.Rpc.MALLOC_FREE_STRUCT_head)),
        ('MIDLVersion', Int32),
        ('CommFaultOffsets', POINTER(win32more.System.Rpc.COMM_FAULT_OFFSETS_head)),
        ('aUserMarshalQuadruple', POINTER(win32more.System.Rpc.USER_MARSHAL_ROUTINE_QUADRUPLE_head)),
        ('NotifyRoutineTable', POINTER(win32more.System.Rpc.NDR_NOTIFY_ROUTINE)),
        ('mFlags', UIntPtr),
        ('CsRoutineTables', POINTER(win32more.System.Rpc.NDR_CS_ROUTINES_head)),
        ('ProxyServerInfo', c_void_p),
        ('pExprInfo', POINTER(win32more.System.Rpc.NDR_EXPR_DESC_head)),
    ]
    return MIDL_STUB_DESC
def _define_MIDL_STUB_MESSAGE_head():
    class MIDL_STUB_MESSAGE(Structure):
        pass
    return MIDL_STUB_MESSAGE
def _define_MIDL_STUB_MESSAGE():
    MIDL_STUB_MESSAGE = win32more.System.Rpc.MIDL_STUB_MESSAGE_head
    MIDL_STUB_MESSAGE._fields_ = [
        ('RpcMsg', POINTER(win32more.System.Rpc.RPC_MESSAGE_head)),
        ('Buffer', c_char_p_no),
        ('BufferStart', c_char_p_no),
        ('BufferEnd', c_char_p_no),
        ('BufferMark', c_char_p_no),
        ('BufferLength', UInt32),
        ('MemorySize', UInt32),
        ('Memory', c_char_p_no),
        ('IsClient', Byte),
        ('Pad', Byte),
        ('uFlags2', UInt16),
        ('ReuseBuffer', Int32),
        ('pAllocAllNodesContext', POINTER(win32more.System.Rpc.NDR_ALLOC_ALL_NODES_CONTEXT_head)),
        ('pPointerQueueState', POINTER(win32more.System.Rpc.NDR_POINTER_QUEUE_STATE_head)),
        ('IgnoreEmbeddedPointers', Int32),
        ('PointerBufferMark', c_char_p_no),
        ('CorrDespIncrement', Byte),
        ('uFlags', Byte),
        ('UniquePtrCount', UInt16),
        ('MaxCount', UIntPtr),
        ('Offset', UInt32),
        ('ActualCount', UInt32),
        ('pfnAllocate', IntPtr),
        ('pfnFree', IntPtr),
        ('StackTop', c_char_p_no),
        ('pPresentedType', c_char_p_no),
        ('pTransmitType', c_char_p_no),
        ('SavedHandle', c_void_p),
        ('StubDesc', POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head)),
        ('FullPtrXlatTables', POINTER(win32more.System.Rpc.FULL_PTR_XLAT_TABLES_head)),
        ('FullPtrRefId', UInt32),
        ('PointerLength', UInt32),
        ('_bitfield', Int32),
        ('dwDestContext', UInt32),
        ('pvDestContext', c_void_p),
        ('SavedContextHandles', POINTER(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head))),
        ('ParamNumber', Int32),
        ('pRpcChannelBuffer', win32more.System.Com.IRpcChannelBuffer_head),
        ('pArrayInfo', POINTER(win32more.System.Rpc.ARRAY_INFO_head)),
        ('SizePtrCountArray', POINTER(UInt32)),
        ('SizePtrOffsetArray', POINTER(UInt32)),
        ('SizePtrLengthArray', POINTER(UInt32)),
        ('pArgQueue', c_void_p),
        ('dwStubPhase', UInt32),
        ('LowStackMark', c_void_p),
        ('pAsyncMsg', POINTER(win32more.System.Rpc._NDR_ASYNC_MESSAGE_head)),
        ('pCorrInfo', POINTER(win32more.System.Rpc._NDR_CORRELATION_INFO_head)),
        ('pCorrMemory', c_char_p_no),
        ('pMemoryList', c_void_p),
        ('pCSInfo', IntPtr),
        ('ConformanceMark', c_char_p_no),
        ('VarianceMark', c_char_p_no),
        ('Unused', IntPtr),
        ('pContext', POINTER(win32more.System.Rpc._NDR_PROC_CONTEXT_head)),
        ('ContextHandleHash', c_void_p),
        ('pUserMarshalList', c_void_p),
        ('Reserved51_3', IntPtr),
        ('Reserved51_4', IntPtr),
        ('Reserved51_5', IntPtr),
    ]
    return MIDL_STUB_MESSAGE
def _define_MIDL_STUBLESS_PROXY_INFO_head():
    class MIDL_STUBLESS_PROXY_INFO(Structure):
        pass
    return MIDL_STUBLESS_PROXY_INFO
def _define_MIDL_STUBLESS_PROXY_INFO():
    MIDL_STUBLESS_PROXY_INFO = win32more.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head
    MIDL_STUBLESS_PROXY_INFO._fields_ = [
        ('pStubDesc', POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head)),
        ('ProcFormatString', c_char_p_no),
        ('FormatStringOffset', POINTER(UInt16)),
        ('pTransferSyntax', POINTER(win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER_head)),
        ('nCount', UIntPtr),
        ('pSyntaxInfo', POINTER(win32more.System.Rpc.MIDL_SYNTAX_INFO_head)),
    ]
    return MIDL_STUBLESS_PROXY_INFO
def _define_MIDL_SYNTAX_INFO_head():
    class MIDL_SYNTAX_INFO(Structure):
        pass
    return MIDL_SYNTAX_INFO
def _define_MIDL_SYNTAX_INFO():
    MIDL_SYNTAX_INFO = win32more.System.Rpc.MIDL_SYNTAX_INFO_head
    MIDL_SYNTAX_INFO._fields_ = [
        ('TransferSyntax', win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER),
        ('DispatchTable', POINTER(win32more.System.Rpc.RPC_DISPATCH_TABLE_head)),
        ('ProcString', c_char_p_no),
        ('FmtStringOffset', POINTER(UInt16)),
        ('TypeString', c_char_p_no),
        ('aUserMarshalQuadruple', c_void_p),
        ('pMethodProperties', POINTER(win32more.System.Rpc.MIDL_INTERFACE_METHOD_PROPERTIES_head)),
        ('pReserved2', UIntPtr),
    ]
    return MIDL_SYNTAX_INFO
def _define_MIDL_TYPE_PICKLING_INFO_head():
    class MIDL_TYPE_PICKLING_INFO(Structure):
        pass
    return MIDL_TYPE_PICKLING_INFO
def _define_MIDL_TYPE_PICKLING_INFO():
    MIDL_TYPE_PICKLING_INFO = win32more.System.Rpc.MIDL_TYPE_PICKLING_INFO_head
    MIDL_TYPE_PICKLING_INFO._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('Reserved', UIntPtr * 3),
    ]
    return MIDL_TYPE_PICKLING_INFO
def _define_MIDL_WINRT_TYPE_SERIALIZATION_INFO_head():
    class MIDL_WINRT_TYPE_SERIALIZATION_INFO(Structure):
        pass
    return MIDL_WINRT_TYPE_SERIALIZATION_INFO
def _define_MIDL_WINRT_TYPE_SERIALIZATION_INFO():
    MIDL_WINRT_TYPE_SERIALIZATION_INFO = win32more.System.Rpc.MIDL_WINRT_TYPE_SERIALIZATION_INFO_head
    MIDL_WINRT_TYPE_SERIALIZATION_INFO._fields_ = [
        ('Version', UInt32),
        ('TypeFormatString', c_char_p_no),
        ('FormatStringSize', UInt16),
        ('TypeOffset', UInt16),
        ('StubDesc', POINTER(win32more.System.Rpc.MIDL_STUB_DESC_head)),
    ]
    return MIDL_WINRT_TYPE_SERIALIZATION_INFO
def _define_NDR_ALLOC_ALL_NODES_CONTEXT_head():
    class NDR_ALLOC_ALL_NODES_CONTEXT(Structure):
        pass
    return NDR_ALLOC_ALL_NODES_CONTEXT
def _define_NDR_ALLOC_ALL_NODES_CONTEXT():
    NDR_ALLOC_ALL_NODES_CONTEXT = win32more.System.Rpc.NDR_ALLOC_ALL_NODES_CONTEXT_head
    return NDR_ALLOC_ALL_NODES_CONTEXT
def _define_NDR_CS_ROUTINES_head():
    class NDR_CS_ROUTINES(Structure):
        pass
    return NDR_CS_ROUTINES
def _define_NDR_CS_ROUTINES():
    NDR_CS_ROUTINES = win32more.System.Rpc.NDR_CS_ROUTINES_head
    NDR_CS_ROUTINES._fields_ = [
        ('pSizeConvertRoutines', POINTER(win32more.System.Rpc.NDR_CS_SIZE_CONVERT_ROUTINES_head)),
        ('pTagGettingRoutines', POINTER(win32more.System.Rpc.CS_TAG_GETTING_ROUTINE)),
    ]
    return NDR_CS_ROUTINES
def _define_NDR_CS_SIZE_CONVERT_ROUTINES_head():
    class NDR_CS_SIZE_CONVERT_ROUTINES(Structure):
        pass
    return NDR_CS_SIZE_CONVERT_ROUTINES
def _define_NDR_CS_SIZE_CONVERT_ROUTINES():
    NDR_CS_SIZE_CONVERT_ROUTINES = win32more.System.Rpc.NDR_CS_SIZE_CONVERT_ROUTINES_head
    NDR_CS_SIZE_CONVERT_ROUTINES._fields_ = [
        ('pfnNetSize', win32more.System.Rpc.CS_TYPE_NET_SIZE_ROUTINE),
        ('pfnToNetCs', win32more.System.Rpc.CS_TYPE_TO_NETCS_ROUTINE),
        ('pfnLocalSize', win32more.System.Rpc.CS_TYPE_LOCAL_SIZE_ROUTINE),
        ('pfnFromNetCs', win32more.System.Rpc.CS_TYPE_FROM_NETCS_ROUTINE),
    ]
    return NDR_CS_SIZE_CONVERT_ROUTINES
def _define_NDR_EXPR_DESC_head():
    class NDR_EXPR_DESC(Structure):
        pass
    return NDR_EXPR_DESC
def _define_NDR_EXPR_DESC():
    NDR_EXPR_DESC = win32more.System.Rpc.NDR_EXPR_DESC_head
    NDR_EXPR_DESC._fields_ = [
        ('pOffset', POINTER(UInt16)),
        ('pFormatExpr', c_char_p_no),
    ]
    return NDR_EXPR_DESC
def _define_NDR_NOTIFY_ROUTINE():
    return WINFUNCTYPE(Void,)
def _define_NDR_NOTIFY2_ROUTINE():
    return WINFUNCTYPE(Void,Byte)
def _define_NDR_POINTER_QUEUE_STATE_head():
    class NDR_POINTER_QUEUE_STATE(Structure):
        pass
    return NDR_POINTER_QUEUE_STATE
def _define_NDR_POINTER_QUEUE_STATE():
    NDR_POINTER_QUEUE_STATE = win32more.System.Rpc.NDR_POINTER_QUEUE_STATE_head
    return NDR_POINTER_QUEUE_STATE
def _define_NDR_RUNDOWN():
    return WINFUNCTYPE(Void,c_void_p)
def _define_NDR_SCONTEXT_1_head():
    class NDR_SCONTEXT_1(Structure):
        pass
    return NDR_SCONTEXT_1
def _define_NDR_SCONTEXT_1():
    NDR_SCONTEXT_1 = win32more.System.Rpc.NDR_SCONTEXT_1_head
    NDR_SCONTEXT_1._fields_ = [
        ('pad', c_void_p * 2),
        ('userContext', c_void_p),
    ]
    return NDR_SCONTEXT_1
def _define_NDR_USER_MARSHAL_INFO_head():
    class NDR_USER_MARSHAL_INFO(Structure):
        pass
    return NDR_USER_MARSHAL_INFO
def _define_NDR_USER_MARSHAL_INFO():
    NDR_USER_MARSHAL_INFO = win32more.System.Rpc.NDR_USER_MARSHAL_INFO_head
    class NDR_USER_MARSHAL_INFO__Anonymous_e__Union(Union):
        pass
    NDR_USER_MARSHAL_INFO__Anonymous_e__Union._fields_ = [
        ('Level1', win32more.System.Rpc.NDR_USER_MARSHAL_INFO_LEVEL1),
    ]
    NDR_USER_MARSHAL_INFO._anonymous_ = [
        'Anonymous',
    ]
    NDR_USER_MARSHAL_INFO._fields_ = [
        ('InformationLevel', UInt32),
        ('Anonymous', NDR_USER_MARSHAL_INFO__Anonymous_e__Union),
    ]
    return NDR_USER_MARSHAL_INFO
def _define_NDR_USER_MARSHAL_INFO_LEVEL1_head():
    class NDR_USER_MARSHAL_INFO_LEVEL1(Structure):
        pass
    return NDR_USER_MARSHAL_INFO_LEVEL1
def _define_NDR_USER_MARSHAL_INFO_LEVEL1():
    NDR_USER_MARSHAL_INFO_LEVEL1 = win32more.System.Rpc.NDR_USER_MARSHAL_INFO_LEVEL1_head
    NDR_USER_MARSHAL_INFO_LEVEL1._fields_ = [
        ('Buffer', c_void_p),
        ('BufferSize', UInt32),
        ('pfnAllocate', IntPtr),
        ('pfnFree', IntPtr),
        ('pRpcChannelBuffer', win32more.System.Com.IRpcChannelBuffer_head),
        ('Reserved', UIntPtr * 5),
    ]
    return NDR_USER_MARSHAL_INFO_LEVEL1
def _define_NDR64_ARRAY_ELEMENT_INFO_head():
    class NDR64_ARRAY_ELEMENT_INFO(Structure):
        pass
    return NDR64_ARRAY_ELEMENT_INFO
def _define_NDR64_ARRAY_ELEMENT_INFO():
    NDR64_ARRAY_ELEMENT_INFO = win32more.System.Rpc.NDR64_ARRAY_ELEMENT_INFO_head
    NDR64_ARRAY_ELEMENT_INFO._fields_ = [
        ('ElementMemSize', UInt32),
        ('Element', c_void_p),
    ]
    return NDR64_ARRAY_ELEMENT_INFO
def _define_NDR64_ARRAY_FLAGS_head():
    class NDR64_ARRAY_FLAGS(Structure):
        pass
    return NDR64_ARRAY_FLAGS
def _define_NDR64_ARRAY_FLAGS():
    NDR64_ARRAY_FLAGS = win32more.System.Rpc.NDR64_ARRAY_FLAGS_head
    NDR64_ARRAY_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_ARRAY_FLAGS
def _define_NDR64_BIND_AND_NOTIFY_EXTENSION_head():
    class NDR64_BIND_AND_NOTIFY_EXTENSION(Structure):
        pass
    return NDR64_BIND_AND_NOTIFY_EXTENSION
def _define_NDR64_BIND_AND_NOTIFY_EXTENSION():
    NDR64_BIND_AND_NOTIFY_EXTENSION = win32more.System.Rpc.NDR64_BIND_AND_NOTIFY_EXTENSION_head
    NDR64_BIND_AND_NOTIFY_EXTENSION._fields_ = [
        ('Binding', win32more.System.Rpc.NDR64_BIND_CONTEXT),
        ('NotifyIndex', UInt16),
    ]
    return NDR64_BIND_AND_NOTIFY_EXTENSION
def _define_NDR64_BIND_CONTEXT_head():
    class NDR64_BIND_CONTEXT(Structure):
        pass
    return NDR64_BIND_CONTEXT
def _define_NDR64_BIND_CONTEXT():
    NDR64_BIND_CONTEXT = win32more.System.Rpc.NDR64_BIND_CONTEXT_head
    NDR64_BIND_CONTEXT._fields_ = [
        ('HandleType', Byte),
        ('Flags', Byte),
        ('StackOffset', UInt16),
        ('RoutineIndex', Byte),
        ('Ordinal', Byte),
    ]
    return NDR64_BIND_CONTEXT
def _define_NDR64_BIND_GENERIC_head():
    class NDR64_BIND_GENERIC(Structure):
        pass
    return NDR64_BIND_GENERIC
def _define_NDR64_BIND_GENERIC():
    NDR64_BIND_GENERIC = win32more.System.Rpc.NDR64_BIND_GENERIC_head
    NDR64_BIND_GENERIC._fields_ = [
        ('HandleType', Byte),
        ('Flags', Byte),
        ('StackOffset', UInt16),
        ('RoutineIndex', Byte),
        ('Size', Byte),
    ]
    return NDR64_BIND_GENERIC
def _define_NDR64_BIND_PRIMITIVE_head():
    class NDR64_BIND_PRIMITIVE(Structure):
        pass
    return NDR64_BIND_PRIMITIVE
def _define_NDR64_BIND_PRIMITIVE():
    NDR64_BIND_PRIMITIVE = win32more.System.Rpc.NDR64_BIND_PRIMITIVE_head
    NDR64_BIND_PRIMITIVE._fields_ = [
        ('HandleType', Byte),
        ('Flags', Byte),
        ('StackOffset', UInt16),
        ('Reserved', UInt16),
    ]
    return NDR64_BIND_PRIMITIVE
def _define_NDR64_BINDINGS_head():
    class NDR64_BINDINGS(Union):
        pass
    return NDR64_BINDINGS
def _define_NDR64_BINDINGS():
    NDR64_BINDINGS = win32more.System.Rpc.NDR64_BINDINGS_head
    NDR64_BINDINGS._fields_ = [
        ('Primitive', win32more.System.Rpc.NDR64_BIND_PRIMITIVE),
        ('Generic', win32more.System.Rpc.NDR64_BIND_GENERIC),
        ('Context', win32more.System.Rpc.NDR64_BIND_CONTEXT),
    ]
    return NDR64_BINDINGS
def _define_NDR64_BOGUS_ARRAY_HEADER_FORMAT_head():
    class NDR64_BOGUS_ARRAY_HEADER_FORMAT(Structure):
        pass
    return NDR64_BOGUS_ARRAY_HEADER_FORMAT
def _define_NDR64_BOGUS_ARRAY_HEADER_FORMAT():
    NDR64_BOGUS_ARRAY_HEADER_FORMAT = win32more.System.Rpc.NDR64_BOGUS_ARRAY_HEADER_FORMAT_head
    NDR64_BOGUS_ARRAY_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_ARRAY_FLAGS),
        ('NumberDims', Byte),
        ('NumberElements', UInt32),
        ('Element', c_void_p),
    ]
    return NDR64_BOGUS_ARRAY_HEADER_FORMAT
def _define_NDR64_BOGUS_STRUCTURE_HEADER_FORMAT_head():
    class NDR64_BOGUS_STRUCTURE_HEADER_FORMAT(Structure):
        pass
    return NDR64_BOGUS_STRUCTURE_HEADER_FORMAT
def _define_NDR64_BOGUS_STRUCTURE_HEADER_FORMAT():
    NDR64_BOGUS_STRUCTURE_HEADER_FORMAT = win32more.System.Rpc.NDR64_BOGUS_STRUCTURE_HEADER_FORMAT_head
    NDR64_BOGUS_STRUCTURE_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_STRUCTURE_FLAGS),
        ('Reserve', Byte),
        ('MemorySize', UInt32),
        ('OriginalMemberLayout', c_void_p),
        ('OriginalPointerLayout', c_void_p),
        ('PointerLayout', c_void_p),
    ]
    return NDR64_BOGUS_STRUCTURE_HEADER_FORMAT
def _define_NDR64_BUFFER_ALIGN_FORMAT_head():
    class NDR64_BUFFER_ALIGN_FORMAT(Structure):
        pass
    return NDR64_BUFFER_ALIGN_FORMAT
def _define_NDR64_BUFFER_ALIGN_FORMAT():
    NDR64_BUFFER_ALIGN_FORMAT = win32more.System.Rpc.NDR64_BUFFER_ALIGN_FORMAT_head
    NDR64_BUFFER_ALIGN_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Reserved', UInt16),
        ('Reserved2', UInt32),
    ]
    return NDR64_BUFFER_ALIGN_FORMAT
def _define_NDR64_CONF_ARRAY_HEADER_FORMAT_head():
    class NDR64_CONF_ARRAY_HEADER_FORMAT(Structure):
        pass
    return NDR64_CONF_ARRAY_HEADER_FORMAT
def _define_NDR64_CONF_ARRAY_HEADER_FORMAT():
    NDR64_CONF_ARRAY_HEADER_FORMAT = win32more.System.Rpc.NDR64_CONF_ARRAY_HEADER_FORMAT_head
    NDR64_CONF_ARRAY_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_ARRAY_FLAGS),
        ('Reserved', Byte),
        ('ElementSize', UInt32),
        ('ConfDescriptor', c_void_p),
    ]
    return NDR64_CONF_ARRAY_HEADER_FORMAT
def _define_NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT_head():
    class NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT(Structure):
        pass
    return NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT
def _define_NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT():
    NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT = win32more.System.Rpc.NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT_head
    NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_STRUCTURE_FLAGS),
        ('Dimensions', Byte),
        ('MemorySize', UInt32),
        ('OriginalMemberLayout', c_void_p),
        ('OriginalPointerLayout', c_void_p),
        ('PointerLayout', c_void_p),
        ('ConfArrayDescription', c_void_p),
    ]
    return NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT
def _define_NDR64_CONF_STRUCTURE_HEADER_FORMAT_head():
    class NDR64_CONF_STRUCTURE_HEADER_FORMAT(Structure):
        pass
    return NDR64_CONF_STRUCTURE_HEADER_FORMAT
def _define_NDR64_CONF_STRUCTURE_HEADER_FORMAT():
    NDR64_CONF_STRUCTURE_HEADER_FORMAT = win32more.System.Rpc.NDR64_CONF_STRUCTURE_HEADER_FORMAT_head
    NDR64_CONF_STRUCTURE_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_STRUCTURE_FLAGS),
        ('Reserve', Byte),
        ('MemorySize', UInt32),
        ('ArrayDescription', c_void_p),
    ]
    return NDR64_CONF_STRUCTURE_HEADER_FORMAT
def _define_NDR64_CONF_VAR_ARRAY_HEADER_FORMAT_head():
    class NDR64_CONF_VAR_ARRAY_HEADER_FORMAT(Structure):
        pass
    return NDR64_CONF_VAR_ARRAY_HEADER_FORMAT
def _define_NDR64_CONF_VAR_ARRAY_HEADER_FORMAT():
    NDR64_CONF_VAR_ARRAY_HEADER_FORMAT = win32more.System.Rpc.NDR64_CONF_VAR_ARRAY_HEADER_FORMAT_head
    NDR64_CONF_VAR_ARRAY_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_ARRAY_FLAGS),
        ('Reserved', Byte),
        ('ElementSize', UInt32),
        ('ConfDescriptor', c_void_p),
        ('VarDescriptor', c_void_p),
    ]
    return NDR64_CONF_VAR_ARRAY_HEADER_FORMAT
def _define_NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT_head():
    class NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT(Structure):
        pass
    return NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT
def _define_NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT():
    NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT = win32more.System.Rpc.NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT_head
    NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT._fields_ = [
        ('FixedArrayFormat', win32more.System.Rpc.NDR64_BOGUS_ARRAY_HEADER_FORMAT),
        ('ConfDescription', c_void_p),
        ('VarDescription', c_void_p),
        ('OffsetDescription', c_void_p),
    ]
    return NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT
def _define_NDR64_CONFORMANT_STRING_FORMAT_head():
    class NDR64_CONFORMANT_STRING_FORMAT(Structure):
        pass
    return NDR64_CONFORMANT_STRING_FORMAT
def _define_NDR64_CONFORMANT_STRING_FORMAT():
    NDR64_CONFORMANT_STRING_FORMAT = win32more.System.Rpc.NDR64_CONFORMANT_STRING_FORMAT_head
    NDR64_CONFORMANT_STRING_FORMAT._fields_ = [
        ('Header', win32more.System.Rpc.NDR64_STRING_HEADER_FORMAT),
    ]
    return NDR64_CONFORMANT_STRING_FORMAT
def _define_NDR64_CONSTANT_IID_FORMAT_head():
    class NDR64_CONSTANT_IID_FORMAT(Structure):
        pass
    return NDR64_CONSTANT_IID_FORMAT
def _define_NDR64_CONSTANT_IID_FORMAT():
    NDR64_CONSTANT_IID_FORMAT = win32more.System.Rpc.NDR64_CONSTANT_IID_FORMAT_head
    NDR64_CONSTANT_IID_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('Reserved', UInt16),
        ('Guid', Guid),
    ]
    return NDR64_CONSTANT_IID_FORMAT
def _define_NDR64_CONTEXT_HANDLE_FLAGS_head():
    class NDR64_CONTEXT_HANDLE_FLAGS(Structure):
        pass
    return NDR64_CONTEXT_HANDLE_FLAGS
def _define_NDR64_CONTEXT_HANDLE_FLAGS():
    NDR64_CONTEXT_HANDLE_FLAGS = win32more.System.Rpc.NDR64_CONTEXT_HANDLE_FLAGS_head
    NDR64_CONTEXT_HANDLE_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_CONTEXT_HANDLE_FLAGS
def _define_NDR64_CONTEXT_HANDLE_FORMAT_head():
    class NDR64_CONTEXT_HANDLE_FORMAT(Structure):
        pass
    return NDR64_CONTEXT_HANDLE_FORMAT
def _define_NDR64_CONTEXT_HANDLE_FORMAT():
    NDR64_CONTEXT_HANDLE_FORMAT = win32more.System.Rpc.NDR64_CONTEXT_HANDLE_FORMAT_head
    NDR64_CONTEXT_HANDLE_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('ContextFlags', Byte),
        ('RundownRoutineIndex', Byte),
        ('Ordinal', Byte),
    ]
    return NDR64_CONTEXT_HANDLE_FORMAT
def _define_NDR64_EMBEDDED_COMPLEX_FORMAT_head():
    class NDR64_EMBEDDED_COMPLEX_FORMAT(Structure):
        pass
    return NDR64_EMBEDDED_COMPLEX_FORMAT
def _define_NDR64_EMBEDDED_COMPLEX_FORMAT():
    NDR64_EMBEDDED_COMPLEX_FORMAT = win32more.System.Rpc.NDR64_EMBEDDED_COMPLEX_FORMAT_head
    NDR64_EMBEDDED_COMPLEX_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Reserve1', Byte),
        ('Reserve2', UInt16),
        ('Type', c_void_p),
    ]
    return NDR64_EMBEDDED_COMPLEX_FORMAT
def _define_NDR64_ENCAPSULATED_UNION_head():
    class NDR64_ENCAPSULATED_UNION(Structure):
        pass
    return NDR64_ENCAPSULATED_UNION
def _define_NDR64_ENCAPSULATED_UNION():
    NDR64_ENCAPSULATED_UNION = win32more.System.Rpc.NDR64_ENCAPSULATED_UNION_head
    NDR64_ENCAPSULATED_UNION._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', Byte),
        ('SwitchType', Byte),
        ('MemoryOffset', UInt32),
        ('MemorySize', UInt32),
        ('Reserved', UInt32),
    ]
    return NDR64_ENCAPSULATED_UNION
def _define_NDR64_EXPR_CONST32_head():
    class NDR64_EXPR_CONST32(Structure):
        pass
    return NDR64_EXPR_CONST32
def _define_NDR64_EXPR_CONST32():
    NDR64_EXPR_CONST32 = win32more.System.Rpc.NDR64_EXPR_CONST32_head
    NDR64_EXPR_CONST32._fields_ = [
        ('ExprType', Byte),
        ('Reserved', Byte),
        ('Reserved1', UInt16),
        ('ConstValue', UInt32),
    ]
    return NDR64_EXPR_CONST32
def _define_NDR64_EXPR_CONST64_head():
    class NDR64_EXPR_CONST64(Structure):
        pass
    return NDR64_EXPR_CONST64
def _define_NDR64_EXPR_CONST64():
    NDR64_EXPR_CONST64 = win32more.System.Rpc.NDR64_EXPR_CONST64_head
    NDR64_EXPR_CONST64._fields_ = [
        ('ExprType', Byte),
        ('Reserved', Byte),
        ('Reserved1', UInt16),
        ('ConstValue', Int64),
    ]
    return NDR64_EXPR_CONST64
def _define_NDR64_EXPR_NOOP_head():
    class NDR64_EXPR_NOOP(Structure):
        pass
    return NDR64_EXPR_NOOP
def _define_NDR64_EXPR_NOOP():
    NDR64_EXPR_NOOP = win32more.System.Rpc.NDR64_EXPR_NOOP_head
    NDR64_EXPR_NOOP._fields_ = [
        ('ExprType', Byte),
        ('Size', Byte),
        ('Reserved', UInt16),
    ]
    return NDR64_EXPR_NOOP
def _define_NDR64_EXPR_OPERATOR_head():
    class NDR64_EXPR_OPERATOR(Structure):
        pass
    return NDR64_EXPR_OPERATOR
def _define_NDR64_EXPR_OPERATOR():
    NDR64_EXPR_OPERATOR = win32more.System.Rpc.NDR64_EXPR_OPERATOR_head
    NDR64_EXPR_OPERATOR._fields_ = [
        ('ExprType', Byte),
        ('Operator', Byte),
        ('CastType', Byte),
        ('Reserved', Byte),
    ]
    return NDR64_EXPR_OPERATOR
def _define_NDR64_EXPR_VAR_head():
    class NDR64_EXPR_VAR(Structure):
        pass
    return NDR64_EXPR_VAR
def _define_NDR64_EXPR_VAR():
    NDR64_EXPR_VAR = win32more.System.Rpc.NDR64_EXPR_VAR_head
    NDR64_EXPR_VAR._fields_ = [
        ('ExprType', Byte),
        ('VarType', Byte),
        ('Reserved', UInt16),
        ('Offset', UInt32),
    ]
    return NDR64_EXPR_VAR
def _define_NDR64_FIX_ARRAY_HEADER_FORMAT_head():
    class NDR64_FIX_ARRAY_HEADER_FORMAT(Structure):
        pass
    return NDR64_FIX_ARRAY_HEADER_FORMAT
def _define_NDR64_FIX_ARRAY_HEADER_FORMAT():
    NDR64_FIX_ARRAY_HEADER_FORMAT = win32more.System.Rpc.NDR64_FIX_ARRAY_HEADER_FORMAT_head
    NDR64_FIX_ARRAY_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_ARRAY_FLAGS),
        ('Reserved', Byte),
        ('TotalSize', UInt32),
    ]
    return NDR64_FIX_ARRAY_HEADER_FORMAT
def _define_NDR64_FIXED_REPEAT_FORMAT_head():
    class NDR64_FIXED_REPEAT_FORMAT(Structure):
        pass
    return NDR64_FIXED_REPEAT_FORMAT
def _define_NDR64_FIXED_REPEAT_FORMAT():
    NDR64_FIXED_REPEAT_FORMAT = win32more.System.Rpc.NDR64_FIXED_REPEAT_FORMAT_head
    NDR64_FIXED_REPEAT_FORMAT._fields_ = [
        ('RepeatFormat', win32more.System.Rpc.NDR64_REPEAT_FORMAT),
        ('Iterations', UInt32),
        ('Reserved', UInt32),
    ]
    return NDR64_FIXED_REPEAT_FORMAT
def _define_NDR64_IID_FLAGS_head():
    class NDR64_IID_FLAGS(Structure):
        pass
    return NDR64_IID_FLAGS
def _define_NDR64_IID_FLAGS():
    NDR64_IID_FLAGS = win32more.System.Rpc.NDR64_IID_FLAGS_head
    NDR64_IID_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_IID_FLAGS
def _define_NDR64_IID_FORMAT_head():
    class NDR64_IID_FORMAT(Structure):
        pass
    return NDR64_IID_FORMAT
def _define_NDR64_IID_FORMAT():
    NDR64_IID_FORMAT = win32more.System.Rpc.NDR64_IID_FORMAT_head
    NDR64_IID_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('Reserved', UInt16),
        ('IIDDescriptor', c_void_p),
    ]
    return NDR64_IID_FORMAT
def _define_NDR64_MEMPAD_FORMAT_head():
    class NDR64_MEMPAD_FORMAT(Structure):
        pass
    return NDR64_MEMPAD_FORMAT
def _define_NDR64_MEMPAD_FORMAT():
    NDR64_MEMPAD_FORMAT = win32more.System.Rpc.NDR64_MEMPAD_FORMAT_head
    NDR64_MEMPAD_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Reserve1', Byte),
        ('MemPad', UInt16),
        ('Reserved2', UInt32),
    ]
    return NDR64_MEMPAD_FORMAT
def _define_NDR64_NO_REPEAT_FORMAT_head():
    class NDR64_NO_REPEAT_FORMAT(Structure):
        pass
    return NDR64_NO_REPEAT_FORMAT
def _define_NDR64_NO_REPEAT_FORMAT():
    NDR64_NO_REPEAT_FORMAT = win32more.System.Rpc.NDR64_NO_REPEAT_FORMAT_head
    NDR64_NO_REPEAT_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('Reserved1', UInt16),
        ('Reserved2', UInt32),
    ]
    return NDR64_NO_REPEAT_FORMAT
def _define_NDR64_NON_CONFORMANT_STRING_FORMAT_head():
    class NDR64_NON_CONFORMANT_STRING_FORMAT(Structure):
        pass
    return NDR64_NON_CONFORMANT_STRING_FORMAT
def _define_NDR64_NON_CONFORMANT_STRING_FORMAT():
    NDR64_NON_CONFORMANT_STRING_FORMAT = win32more.System.Rpc.NDR64_NON_CONFORMANT_STRING_FORMAT_head
    NDR64_NON_CONFORMANT_STRING_FORMAT._fields_ = [
        ('Header', win32more.System.Rpc.NDR64_STRING_HEADER_FORMAT),
        ('TotalSize', UInt32),
    ]
    return NDR64_NON_CONFORMANT_STRING_FORMAT
def _define_NDR64_NON_ENCAPSULATED_UNION_head():
    class NDR64_NON_ENCAPSULATED_UNION(Structure):
        pass
    return NDR64_NON_ENCAPSULATED_UNION
def _define_NDR64_NON_ENCAPSULATED_UNION():
    NDR64_NON_ENCAPSULATED_UNION = win32more.System.Rpc.NDR64_NON_ENCAPSULATED_UNION_head
    NDR64_NON_ENCAPSULATED_UNION._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', Byte),
        ('SwitchType', Byte),
        ('MemorySize', UInt32),
        ('Switch', c_void_p),
        ('Reserved', UInt32),
    ]
    return NDR64_NON_ENCAPSULATED_UNION
def _define_NDR64_PARAM_FLAGS_head():
    class NDR64_PARAM_FLAGS(Structure):
        pass
    return NDR64_PARAM_FLAGS
def _define_NDR64_PARAM_FLAGS():
    NDR64_PARAM_FLAGS = win32more.System.Rpc.NDR64_PARAM_FLAGS_head
    NDR64_PARAM_FLAGS._fields_ = [
        ('_bitfield', UInt16),
    ]
    return NDR64_PARAM_FLAGS
def _define_NDR64_PARAM_FORMAT_head():
    class NDR64_PARAM_FORMAT(Structure):
        pass
    return NDR64_PARAM_FORMAT
def _define_NDR64_PARAM_FORMAT():
    NDR64_PARAM_FORMAT = win32more.System.Rpc.NDR64_PARAM_FORMAT_head
    NDR64_PARAM_FORMAT._fields_ = [
        ('Type', c_void_p),
        ('Attributes', win32more.System.Rpc.NDR64_PARAM_FLAGS),
        ('Reserved', UInt16),
        ('StackOffset', UInt32),
    ]
    return NDR64_PARAM_FORMAT
def _define_NDR64_PIPE_FLAGS_head():
    class NDR64_PIPE_FLAGS(Structure):
        pass
    return NDR64_PIPE_FLAGS
def _define_NDR64_PIPE_FLAGS():
    NDR64_PIPE_FLAGS = win32more.System.Rpc.NDR64_PIPE_FLAGS_head
    NDR64_PIPE_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_PIPE_FLAGS
def _define_NDR64_PIPE_FORMAT_head():
    class NDR64_PIPE_FORMAT(Structure):
        pass
    return NDR64_PIPE_FORMAT
def _define_NDR64_PIPE_FORMAT():
    NDR64_PIPE_FORMAT = win32more.System.Rpc.NDR64_PIPE_FORMAT_head
    NDR64_PIPE_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('Alignment', Byte),
        ('Reserved', Byte),
        ('Type', c_void_p),
        ('MemorySize', UInt32),
        ('BufferSize', UInt32),
    ]
    return NDR64_PIPE_FORMAT
def _define_NDR64_POINTER_FORMAT_head():
    class NDR64_POINTER_FORMAT(Structure):
        pass
    return NDR64_POINTER_FORMAT
def _define_NDR64_POINTER_FORMAT():
    NDR64_POINTER_FORMAT = win32more.System.Rpc.NDR64_POINTER_FORMAT_head
    NDR64_POINTER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('Reserved', UInt16),
        ('Pointee', c_void_p),
    ]
    return NDR64_POINTER_FORMAT
def _define_NDR64_POINTER_INSTANCE_HEADER_FORMAT_head():
    class NDR64_POINTER_INSTANCE_HEADER_FORMAT(Structure):
        pass
    return NDR64_POINTER_INSTANCE_HEADER_FORMAT
def _define_NDR64_POINTER_INSTANCE_HEADER_FORMAT():
    NDR64_POINTER_INSTANCE_HEADER_FORMAT = win32more.System.Rpc.NDR64_POINTER_INSTANCE_HEADER_FORMAT_head
    NDR64_POINTER_INSTANCE_HEADER_FORMAT._fields_ = [
        ('Offset', UInt32),
        ('Reserved', UInt32),
    ]
    return NDR64_POINTER_INSTANCE_HEADER_FORMAT
def _define_NDR64_POINTER_REPEAT_FLAGS_head():
    class NDR64_POINTER_REPEAT_FLAGS(Structure):
        pass
    return NDR64_POINTER_REPEAT_FLAGS
def _define_NDR64_POINTER_REPEAT_FLAGS():
    NDR64_POINTER_REPEAT_FLAGS = win32more.System.Rpc.NDR64_POINTER_REPEAT_FLAGS_head
    NDR64_POINTER_REPEAT_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_POINTER_REPEAT_FLAGS
def _define_NDR64_PROC_FLAGS_head():
    class NDR64_PROC_FLAGS(Structure):
        pass
    return NDR64_PROC_FLAGS
def _define_NDR64_PROC_FLAGS():
    NDR64_PROC_FLAGS = win32more.System.Rpc.NDR64_PROC_FLAGS_head
    NDR64_PROC_FLAGS._fields_ = [
        ('_bitfield', UInt32),
    ]
    return NDR64_PROC_FLAGS
def _define_NDR64_PROC_FORMAT_head():
    class NDR64_PROC_FORMAT(Structure):
        pass
    return NDR64_PROC_FORMAT
def _define_NDR64_PROC_FORMAT():
    NDR64_PROC_FORMAT = win32more.System.Rpc.NDR64_PROC_FORMAT_head
    NDR64_PROC_FORMAT._fields_ = [
        ('Flags', UInt32),
        ('StackSize', UInt32),
        ('ConstantClientBufferSize', UInt32),
        ('ConstantServerBufferSize', UInt32),
        ('RpcFlags', UInt16),
        ('FloatDoubleMask', UInt16),
        ('NumberOfParams', UInt16),
        ('ExtensionSize', UInt16),
    ]
    return NDR64_PROC_FORMAT
def _define_NDR64_RANGE_FORMAT_head():
    class NDR64_RANGE_FORMAT(Structure):
        pass
    return NDR64_RANGE_FORMAT
def _define_NDR64_RANGE_FORMAT():
    NDR64_RANGE_FORMAT = win32more.System.Rpc.NDR64_RANGE_FORMAT_head
    NDR64_RANGE_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('RangeType', Byte),
        ('Reserved', UInt16),
        ('MinValue', Int64),
        ('MaxValue', Int64),
    ]
    return NDR64_RANGE_FORMAT
def _define_NDR64_RANGE_PIPE_FORMAT_head():
    class NDR64_RANGE_PIPE_FORMAT(Structure):
        pass
    return NDR64_RANGE_PIPE_FORMAT
def _define_NDR64_RANGE_PIPE_FORMAT():
    NDR64_RANGE_PIPE_FORMAT = win32more.System.Rpc.NDR64_RANGE_PIPE_FORMAT_head
    NDR64_RANGE_PIPE_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('Alignment', Byte),
        ('Reserved', Byte),
        ('Type', c_void_p),
        ('MemorySize', UInt32),
        ('BufferSize', UInt32),
        ('MinValue', UInt32),
        ('MaxValue', UInt32),
    ]
    return NDR64_RANGE_PIPE_FORMAT
def _define_NDR64_RANGED_STRING_FORMAT_head():
    class NDR64_RANGED_STRING_FORMAT(Structure):
        pass
    return NDR64_RANGED_STRING_FORMAT
def _define_NDR64_RANGED_STRING_FORMAT():
    NDR64_RANGED_STRING_FORMAT = win32more.System.Rpc.NDR64_RANGED_STRING_FORMAT_head
    NDR64_RANGED_STRING_FORMAT._fields_ = [
        ('Header', win32more.System.Rpc.NDR64_STRING_HEADER_FORMAT),
        ('Reserved', UInt32),
        ('Min', UInt64),
        ('Max', UInt64),
    ]
    return NDR64_RANGED_STRING_FORMAT
def _define_NDR64_REPEAT_FORMAT_head():
    class NDR64_REPEAT_FORMAT(Structure):
        pass
    return NDR64_REPEAT_FORMAT
def _define_NDR64_REPEAT_FORMAT():
    NDR64_REPEAT_FORMAT = win32more.System.Rpc.NDR64_REPEAT_FORMAT_head
    NDR64_REPEAT_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', win32more.System.Rpc.NDR64_POINTER_REPEAT_FLAGS),
        ('Reserved', UInt16),
        ('Increment', UInt32),
        ('OffsetToArray', UInt32),
        ('NumberOfPointers', UInt32),
    ]
    return NDR64_REPEAT_FORMAT
def _define_NDR64_RPC_FLAGS_head():
    class NDR64_RPC_FLAGS(Structure):
        pass
    return NDR64_RPC_FLAGS
def _define_NDR64_RPC_FLAGS():
    NDR64_RPC_FLAGS = win32more.System.Rpc.NDR64_RPC_FLAGS_head
    NDR64_RPC_FLAGS._fields_ = [
        ('_bitfield', UInt16),
    ]
    return NDR64_RPC_FLAGS
def _define_NDR64_SIMPLE_MEMBER_FORMAT_head():
    class NDR64_SIMPLE_MEMBER_FORMAT(Structure):
        pass
    return NDR64_SIMPLE_MEMBER_FORMAT
def _define_NDR64_SIMPLE_MEMBER_FORMAT():
    NDR64_SIMPLE_MEMBER_FORMAT = win32more.System.Rpc.NDR64_SIMPLE_MEMBER_FORMAT_head
    NDR64_SIMPLE_MEMBER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Reserved1', Byte),
        ('Reserved2', UInt16),
        ('Reserved3', UInt32),
    ]
    return NDR64_SIMPLE_MEMBER_FORMAT
def _define_NDR64_SIMPLE_REGION_FORMAT_head():
    class NDR64_SIMPLE_REGION_FORMAT(Structure):
        pass
    return NDR64_SIMPLE_REGION_FORMAT
def _define_NDR64_SIMPLE_REGION_FORMAT():
    NDR64_SIMPLE_REGION_FORMAT = win32more.System.Rpc.NDR64_SIMPLE_REGION_FORMAT_head
    NDR64_SIMPLE_REGION_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('RegionSize', UInt16),
        ('Reserved', UInt32),
    ]
    return NDR64_SIMPLE_REGION_FORMAT
def _define_NDR64_SIZED_CONFORMANT_STRING_FORMAT_head():
    class NDR64_SIZED_CONFORMANT_STRING_FORMAT(Structure):
        pass
    return NDR64_SIZED_CONFORMANT_STRING_FORMAT
def _define_NDR64_SIZED_CONFORMANT_STRING_FORMAT():
    NDR64_SIZED_CONFORMANT_STRING_FORMAT = win32more.System.Rpc.NDR64_SIZED_CONFORMANT_STRING_FORMAT_head
    NDR64_SIZED_CONFORMANT_STRING_FORMAT._fields_ = [
        ('Header', win32more.System.Rpc.NDR64_STRING_HEADER_FORMAT),
        ('SizeDescription', c_void_p),
    ]
    return NDR64_SIZED_CONFORMANT_STRING_FORMAT
def _define_NDR64_STRING_FLAGS_head():
    class NDR64_STRING_FLAGS(Structure):
        pass
    return NDR64_STRING_FLAGS
def _define_NDR64_STRING_FLAGS():
    NDR64_STRING_FLAGS = win32more.System.Rpc.NDR64_STRING_FLAGS_head
    NDR64_STRING_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_STRING_FLAGS
def _define_NDR64_STRING_HEADER_FORMAT_head():
    class NDR64_STRING_HEADER_FORMAT(Structure):
        pass
    return NDR64_STRING_HEADER_FORMAT
def _define_NDR64_STRING_HEADER_FORMAT():
    NDR64_STRING_HEADER_FORMAT = win32more.System.Rpc.NDR64_STRING_HEADER_FORMAT_head
    NDR64_STRING_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', win32more.System.Rpc.NDR64_STRING_FLAGS),
        ('ElementSize', UInt16),
    ]
    return NDR64_STRING_HEADER_FORMAT
def _define_NDR64_STRUCTURE_FLAGS_head():
    class NDR64_STRUCTURE_FLAGS(Structure):
        pass
    return NDR64_STRUCTURE_FLAGS
def _define_NDR64_STRUCTURE_FLAGS():
    NDR64_STRUCTURE_FLAGS = win32more.System.Rpc.NDR64_STRUCTURE_FLAGS_head
    NDR64_STRUCTURE_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_STRUCTURE_FLAGS
def _define_NDR64_STRUCTURE_HEADER_FORMAT_head():
    class NDR64_STRUCTURE_HEADER_FORMAT(Structure):
        pass
    return NDR64_STRUCTURE_HEADER_FORMAT
def _define_NDR64_STRUCTURE_HEADER_FORMAT():
    NDR64_STRUCTURE_HEADER_FORMAT = win32more.System.Rpc.NDR64_STRUCTURE_HEADER_FORMAT_head
    NDR64_STRUCTURE_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_STRUCTURE_FLAGS),
        ('Reserve', Byte),
        ('MemorySize', UInt32),
    ]
    return NDR64_STRUCTURE_HEADER_FORMAT
def _define_NDR64_SYSTEM_HANDLE_FORMAT_head():
    class NDR64_SYSTEM_HANDLE_FORMAT(Structure):
        pass
    return NDR64_SYSTEM_HANDLE_FORMAT
def _define_NDR64_SYSTEM_HANDLE_FORMAT():
    NDR64_SYSTEM_HANDLE_FORMAT = win32more.System.Rpc.NDR64_SYSTEM_HANDLE_FORMAT_head
    NDR64_SYSTEM_HANDLE_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('HandleType', Byte),
        ('DesiredAccess', UInt32),
    ]
    return NDR64_SYSTEM_HANDLE_FORMAT
def _define_NDR64_TRANSMIT_AS_FLAGS_head():
    class NDR64_TRANSMIT_AS_FLAGS(Structure):
        pass
    return NDR64_TRANSMIT_AS_FLAGS
def _define_NDR64_TRANSMIT_AS_FLAGS():
    NDR64_TRANSMIT_AS_FLAGS = win32more.System.Rpc.NDR64_TRANSMIT_AS_FLAGS_head
    NDR64_TRANSMIT_AS_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_TRANSMIT_AS_FLAGS
def _define_NDR64_TRANSMIT_AS_FORMAT_head():
    class NDR64_TRANSMIT_AS_FORMAT(Structure):
        pass
    return NDR64_TRANSMIT_AS_FORMAT
def _define_NDR64_TRANSMIT_AS_FORMAT():
    NDR64_TRANSMIT_AS_FORMAT = win32more.System.Rpc.NDR64_TRANSMIT_AS_FORMAT_head
    NDR64_TRANSMIT_AS_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('RoutineIndex', UInt16),
        ('TransmittedTypeWireAlignment', UInt16),
        ('MemoryAlignment', UInt16),
        ('PresentedTypeMemorySize', UInt32),
        ('TransmittedTypeBufferSize', UInt32),
        ('TransmittedType', c_void_p),
    ]
    return NDR64_TRANSMIT_AS_FORMAT
def _define_NDR64_TYPE_STRICT_CONTEXT_HANDLE_head():
    class NDR64_TYPE_STRICT_CONTEXT_HANDLE(Structure):
        pass
    return NDR64_TYPE_STRICT_CONTEXT_HANDLE
def _define_NDR64_TYPE_STRICT_CONTEXT_HANDLE():
    NDR64_TYPE_STRICT_CONTEXT_HANDLE = win32more.System.Rpc.NDR64_TYPE_STRICT_CONTEXT_HANDLE_head
    NDR64_TYPE_STRICT_CONTEXT_HANDLE._fields_ = [
        ('FormatCode', Byte),
        ('RealFormatCode', Byte),
        ('Reserved', UInt16),
        ('Type', c_void_p),
        ('CtxtFlags', UInt32),
        ('CtxtID', UInt32),
    ]
    return NDR64_TYPE_STRICT_CONTEXT_HANDLE
def _define_NDR64_UNION_ARM_head():
    class NDR64_UNION_ARM(Structure):
        pass
    return NDR64_UNION_ARM
def _define_NDR64_UNION_ARM():
    NDR64_UNION_ARM = win32more.System.Rpc.NDR64_UNION_ARM_head
    NDR64_UNION_ARM._fields_ = [
        ('CaseValue', Int64),
        ('Type', c_void_p),
        ('Reserved', UInt32),
    ]
    return NDR64_UNION_ARM
def _define_NDR64_UNION_ARM_SELECTOR_head():
    class NDR64_UNION_ARM_SELECTOR(Structure):
        pass
    return NDR64_UNION_ARM_SELECTOR
def _define_NDR64_UNION_ARM_SELECTOR():
    NDR64_UNION_ARM_SELECTOR = win32more.System.Rpc.NDR64_UNION_ARM_SELECTOR_head
    NDR64_UNION_ARM_SELECTOR._fields_ = [
        ('Reserved1', Byte),
        ('Alignment', Byte),
        ('Reserved2', UInt16),
        ('Arms', UInt32),
    ]
    return NDR64_UNION_ARM_SELECTOR
def _define_NDR64_USER_MARSHAL_FLAGS_head():
    class NDR64_USER_MARSHAL_FLAGS(Structure):
        pass
    return NDR64_USER_MARSHAL_FLAGS
def _define_NDR64_USER_MARSHAL_FLAGS():
    NDR64_USER_MARSHAL_FLAGS = win32more.System.Rpc.NDR64_USER_MARSHAL_FLAGS_head
    NDR64_USER_MARSHAL_FLAGS._fields_ = [
        ('_bitfield', Byte),
    ]
    return NDR64_USER_MARSHAL_FLAGS
def _define_NDR64_USER_MARSHAL_FORMAT_head():
    class NDR64_USER_MARSHAL_FORMAT(Structure):
        pass
    return NDR64_USER_MARSHAL_FORMAT
def _define_NDR64_USER_MARSHAL_FORMAT():
    NDR64_USER_MARSHAL_FORMAT = win32more.System.Rpc.NDR64_USER_MARSHAL_FORMAT_head
    NDR64_USER_MARSHAL_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Flags', Byte),
        ('RoutineIndex', UInt16),
        ('TransmittedTypeWireAlignment', UInt16),
        ('MemoryAlignment', UInt16),
        ('UserTypeMemorySize', UInt32),
        ('TransmittedTypeBufferSize', UInt32),
        ('TransmittedType', c_void_p),
    ]
    return NDR64_USER_MARSHAL_FORMAT
def _define_NDR64_VAR_ARRAY_HEADER_FORMAT_head():
    class NDR64_VAR_ARRAY_HEADER_FORMAT(Structure):
        pass
    return NDR64_VAR_ARRAY_HEADER_FORMAT
def _define_NDR64_VAR_ARRAY_HEADER_FORMAT():
    NDR64_VAR_ARRAY_HEADER_FORMAT = win32more.System.Rpc.NDR64_VAR_ARRAY_HEADER_FORMAT_head
    NDR64_VAR_ARRAY_HEADER_FORMAT._fields_ = [
        ('FormatCode', Byte),
        ('Alignment', Byte),
        ('Flags', win32more.System.Rpc.NDR64_ARRAY_FLAGS),
        ('Reserved', Byte),
        ('TotalSize', UInt32),
        ('ElementSize', UInt32),
        ('VarDescriptor', c_void_p),
    ]
    return NDR64_VAR_ARRAY_HEADER_FORMAT
def _define_PFN_RPCNOTIFICATION_ROUTINE():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_ASYNC_STATE_head),c_void_p,win32more.System.Rpc.RPC_ASYNC_EVENT)
PROXY_PHASE = Int32
PROXY_CALCSIZE = 0
PROXY_GETBUFFER = 1
PROXY_MARSHAL = 2
PROXY_SENDRECEIVE = 3
PROXY_UNMARSHAL = 4
def _define_PRPC_RUNDOWN():
    return WINFUNCTYPE(Void,c_void_p)
def _define_RDR_CALLOUT_STATE_head():
    class RDR_CALLOUT_STATE(Structure):
        pass
    return RDR_CALLOUT_STATE
def _define_RDR_CALLOUT_STATE():
    RDR_CALLOUT_STATE = win32more.System.Rpc.RDR_CALLOUT_STATE_head
    RDR_CALLOUT_STATE._fields_ = [
        ('LastError', win32more.System.Rpc.RPC_STATUS),
        ('LastEEInfo', c_void_p),
        ('LastCalledStage', win32more.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE),
        ('ServerName', POINTER(UInt16)),
        ('ServerPort', POINTER(UInt16)),
        ('RemoteUser', POINTER(UInt16)),
        ('AuthType', POINTER(UInt16)),
        ('ResourceTypePresent', Byte),
        ('SessionIdPresent', Byte),
        ('InterfacePresent', Byte),
        ('ResourceType', Guid),
        ('SessionId', Guid),
        ('Interface', win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER),
        ('CertContext', c_void_p),
    ]
    return RDR_CALLOUT_STATE
def _define_RPC_ADDRESS_CHANGE_FN():
    return WINFUNCTYPE(Void,c_void_p)
RPC_ADDRESS_CHANGE_TYPE = Int32
PROTOCOL_NOT_LOADED = 1
PROTOCOL_LOADED = 2
PROTOCOL_ADDRESS_CHANGE = 3
RPC_ASYNC_EVENT = Int32
RPC_ASYNC_EVENT_RpcCallComplete = 0
RPC_ASYNC_EVENT_RpcSendComplete = 1
RPC_ASYNC_EVENT_RpcReceiveComplete = 2
RPC_ASYNC_EVENT_RpcClientDisconnect = 3
RPC_ASYNC_EVENT_RpcClientCancel = 4
def _define_RPC_ASYNC_NOTIFICATION_INFO_head():
    class RPC_ASYNC_NOTIFICATION_INFO(Union):
        pass
    return RPC_ASYNC_NOTIFICATION_INFO
def _define_RPC_ASYNC_NOTIFICATION_INFO():
    RPC_ASYNC_NOTIFICATION_INFO = win32more.System.Rpc.RPC_ASYNC_NOTIFICATION_INFO_head
    class RPC_ASYNC_NOTIFICATION_INFO__APC_e__Struct(Structure):
        pass
    RPC_ASYNC_NOTIFICATION_INFO__APC_e__Struct._fields_ = [
        ('NotificationRoutine', win32more.System.Rpc.PFN_RPCNOTIFICATION_ROUTINE),
        ('hThread', win32more.Foundation.HANDLE),
    ]
    class RPC_ASYNC_NOTIFICATION_INFO__IOC_e__Struct(Structure):
        pass
    RPC_ASYNC_NOTIFICATION_INFO__IOC_e__Struct._fields_ = [
        ('hIOPort', win32more.Foundation.HANDLE),
        ('dwNumberOfBytesTransferred', UInt32),
        ('dwCompletionKey', UIntPtr),
        ('lpOverlapped', POINTER(win32more.System.IO.OVERLAPPED_head)),
    ]
    class RPC_ASYNC_NOTIFICATION_INFO__IntPtr_e__Struct(Structure):
        pass
    RPC_ASYNC_NOTIFICATION_INFO__IntPtr_e__Struct._fields_ = [
        ('hWnd', win32more.Foundation.HWND),
        ('Msg', UInt32),
    ]
    RPC_ASYNC_NOTIFICATION_INFO._fields_ = [
        ('APC', RPC_ASYNC_NOTIFICATION_INFO__APC_e__Struct),
        ('IOC', RPC_ASYNC_NOTIFICATION_INFO__IOC_e__Struct),
        ('IntPtr', RPC_ASYNC_NOTIFICATION_INFO__IntPtr_e__Struct),
        ('hEvent', win32more.Foundation.HANDLE),
        ('NotificationRoutine', win32more.System.Rpc.PFN_RPCNOTIFICATION_ROUTINE),
    ]
    return RPC_ASYNC_NOTIFICATION_INFO
def _define_RPC_ASYNC_STATE_head():
    class RPC_ASYNC_STATE(Structure):
        pass
    return RPC_ASYNC_STATE
def _define_RPC_ASYNC_STATE():
    RPC_ASYNC_STATE = win32more.System.Rpc.RPC_ASYNC_STATE_head
    RPC_ASYNC_STATE._fields_ = [
        ('Size', UInt32),
        ('Signature', UInt32),
        ('Lock', Int32),
        ('Flags', UInt32),
        ('StubInfo', c_void_p),
        ('UserInfo', c_void_p),
        ('RuntimeInfo', c_void_p),
        ('Event', win32more.System.Rpc.RPC_ASYNC_EVENT),
        ('NotificationType', win32more.System.Rpc.RPC_NOTIFICATION_TYPES),
        ('u', win32more.System.Rpc.RPC_ASYNC_NOTIFICATION_INFO),
        ('Reserved', IntPtr * 4),
    ]
    return RPC_ASYNC_STATE
def _define_RPC_AUTH_KEY_RETRIEVAL_FN():
    return WINFUNCTYPE(Void,c_void_p,POINTER(UInt16),UInt32,POINTER(c_void_p),POINTER(win32more.System.Rpc.RPC_STATUS))
RPC_BINDING_HANDLE_OPTIONS_FLAGS = UInt32
RPC_BHO_NONCAUSAL = 1
RPC_BHO_DONTLINGER = 2
def _define_RPC_BINDING_HANDLE_OPTIONS_V1_head():
    class RPC_BINDING_HANDLE_OPTIONS_V1(Structure):
        pass
    return RPC_BINDING_HANDLE_OPTIONS_V1
def _define_RPC_BINDING_HANDLE_OPTIONS_V1():
    RPC_BINDING_HANDLE_OPTIONS_V1 = win32more.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_V1_head
    RPC_BINDING_HANDLE_OPTIONS_V1._fields_ = [
        ('Version', UInt32),
        ('Flags', win32more.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_FLAGS),
        ('ComTimeout', UInt32),
        ('CallTimeout', UInt32),
    ]
    return RPC_BINDING_HANDLE_OPTIONS_V1
def _define_RPC_BINDING_HANDLE_SECURITY_V1_A_head():
    class RPC_BINDING_HANDLE_SECURITY_V1_A(Structure):
        pass
    return RPC_BINDING_HANDLE_SECURITY_V1_A
def _define_RPC_BINDING_HANDLE_SECURITY_V1_A():
    RPC_BINDING_HANDLE_SECURITY_V1_A = win32more.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_A_head
    RPC_BINDING_HANDLE_SECURITY_V1_A._fields_ = [
        ('Version', UInt32),
        ('ServerPrincName', c_char_p_no),
        ('AuthnLevel', UInt32),
        ('AuthnSvc', UInt32),
        ('AuthIdentity', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)),
        ('SecurityQos', POINTER(win32more.System.Rpc.RPC_SECURITY_QOS_head)),
    ]
    return RPC_BINDING_HANDLE_SECURITY_V1_A
def _define_RPC_BINDING_HANDLE_SECURITY_V1_W_head():
    class RPC_BINDING_HANDLE_SECURITY_V1_W(Structure):
        pass
    return RPC_BINDING_HANDLE_SECURITY_V1_W
def _define_RPC_BINDING_HANDLE_SECURITY_V1_W():
    RPC_BINDING_HANDLE_SECURITY_V1_W = win32more.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_W_head
    RPC_BINDING_HANDLE_SECURITY_V1_W._fields_ = [
        ('Version', UInt32),
        ('ServerPrincName', POINTER(UInt16)),
        ('AuthnLevel', UInt32),
        ('AuthnSvc', UInt32),
        ('AuthIdentity', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)),
        ('SecurityQos', POINTER(win32more.System.Rpc.RPC_SECURITY_QOS_head)),
    ]
    return RPC_BINDING_HANDLE_SECURITY_V1_W
def _define_RPC_BINDING_HANDLE_TEMPLATE_V1_A_head():
    class RPC_BINDING_HANDLE_TEMPLATE_V1_A(Structure):
        pass
    return RPC_BINDING_HANDLE_TEMPLATE_V1_A
def _define_RPC_BINDING_HANDLE_TEMPLATE_V1_A():
    RPC_BINDING_HANDLE_TEMPLATE_V1_A = win32more.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_A_head
    class RPC_BINDING_HANDLE_TEMPLATE_V1_A__u1_e__Union(Union):
        pass
    RPC_BINDING_HANDLE_TEMPLATE_V1_A__u1_e__Union._fields_ = [
        ('Reserved', c_char_p_no),
    ]
    RPC_BINDING_HANDLE_TEMPLATE_V1_A._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ProtocolSequence', UInt32),
        ('NetworkAddress', c_char_p_no),
        ('StringEndpoint', c_char_p_no),
        ('u1', RPC_BINDING_HANDLE_TEMPLATE_V1_A__u1_e__Union),
        ('ObjectUuid', Guid),
    ]
    return RPC_BINDING_HANDLE_TEMPLATE_V1_A
def _define_RPC_BINDING_HANDLE_TEMPLATE_V1_W_head():
    class RPC_BINDING_HANDLE_TEMPLATE_V1_W(Structure):
        pass
    return RPC_BINDING_HANDLE_TEMPLATE_V1_W
def _define_RPC_BINDING_HANDLE_TEMPLATE_V1_W():
    RPC_BINDING_HANDLE_TEMPLATE_V1_W = win32more.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_W_head
    class RPC_BINDING_HANDLE_TEMPLATE_V1_W__u1_e__Union(Union):
        pass
    RPC_BINDING_HANDLE_TEMPLATE_V1_W__u1_e__Union._fields_ = [
        ('Reserved', POINTER(UInt16)),
    ]
    RPC_BINDING_HANDLE_TEMPLATE_V1_W._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ProtocolSequence', UInt32),
        ('NetworkAddress', POINTER(UInt16)),
        ('StringEndpoint', POINTER(UInt16)),
        ('u1', RPC_BINDING_HANDLE_TEMPLATE_V1_W__u1_e__Union),
        ('ObjectUuid', Guid),
    ]
    return RPC_BINDING_HANDLE_TEMPLATE_V1_W
def _define_RPC_BINDING_VECTOR_head():
    class RPC_BINDING_VECTOR(Structure):
        pass
    return RPC_BINDING_VECTOR
def _define_RPC_BINDING_VECTOR():
    RPC_BINDING_VECTOR = win32more.System.Rpc.RPC_BINDING_VECTOR_head
    RPC_BINDING_VECTOR._fields_ = [
        ('Count', UInt32),
        ('BindingH', c_void_p * 1),
    ]
    return RPC_BINDING_VECTOR
def _define_RPC_BLOCKING_FN():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p,c_void_p)
RPC_C_AUTHN_INFO_TYPE = UInt32
RPC_C_AUTHN_INFO_NONE = 0
RPC_C_AUTHN_INFO_TYPE_HTTP = 1
RPC_C_HTTP_AUTHN_TARGET = UInt32
RPC_C_HTTP_AUTHN_TARGET_SERVER = 1
RPC_C_HTTP_AUTHN_TARGET_PROXY = 2
RPC_C_HTTP_FLAGS = UInt32
RPC_C_HTTP_FLAG_USE_SSL = 1
RPC_C_HTTP_FLAG_USE_FIRST_AUTH_SCHEME = 2
RPC_C_HTTP_FLAG_IGNORE_CERT_CN_INVALID = 8
RPC_C_HTTP_FLAG_ENABLE_CERT_REVOCATION_CHECK = 16
def _define_RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR_head():
    class RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR(Structure):
        pass
    return RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR
def _define_RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR():
    RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR = win32more.System.Rpc.RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR_head
    RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR._fields_ = [
        ('BufferSize', UInt32),
        ('Buffer', win32more.Foundation.PSTR),
    ]
    return RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR
RPC_C_QOS_CAPABILITIES = UInt32
RPC_C_QOS_CAPABILITIES_DEFAULT = 0
RPC_C_QOS_CAPABILITIES_MUTUAL_AUTH = 1
RPC_C_QOS_CAPABILITIES_MAKE_FULLSIC = 2
RPC_C_QOS_CAPABILITIES_ANY_AUTHORITY = 4
RPC_C_QOS_CAPABILITIES_IGNORE_DELEGATE_FAILURE = 8
RPC_C_QOS_CAPABILITIES_LOCAL_MA_HINT = 16
RPC_C_QOS_CAPABILITIES_SCHANNEL_FULL_AUTH_IDENTITY = 32
RPC_C_QOS_IDENTITY = UInt32
RPC_C_QOS_IDENTITY_STATIC = 0
RPC_C_QOS_IDENTITY_DYNAMIC = 1
def _define_RPC_CALL_ATTRIBUTES_V1_A_head():
    class RPC_CALL_ATTRIBUTES_V1_A(Structure):
        pass
    return RPC_CALL_ATTRIBUTES_V1_A
def _define_RPC_CALL_ATTRIBUTES_V1_A():
    RPC_CALL_ATTRIBUTES_V1_A = win32more.System.Rpc.RPC_CALL_ATTRIBUTES_V1_A_head
    RPC_CALL_ATTRIBUTES_V1_A._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ServerPrincipalNameBufferLength', UInt32),
        ('ServerPrincipalName', c_char_p_no),
        ('ClientPrincipalNameBufferLength', UInt32),
        ('ClientPrincipalName', c_char_p_no),
        ('AuthenticationLevel', UInt32),
        ('AuthenticationService', UInt32),
        ('NullSession', win32more.Foundation.BOOL),
    ]
    return RPC_CALL_ATTRIBUTES_V1_A
def _define_RPC_CALL_ATTRIBUTES_V1_W_head():
    class RPC_CALL_ATTRIBUTES_V1_W(Structure):
        pass
    return RPC_CALL_ATTRIBUTES_V1_W
def _define_RPC_CALL_ATTRIBUTES_V1_W():
    RPC_CALL_ATTRIBUTES_V1_W = win32more.System.Rpc.RPC_CALL_ATTRIBUTES_V1_W_head
    RPC_CALL_ATTRIBUTES_V1_W._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ServerPrincipalNameBufferLength', UInt32),
        ('ServerPrincipalName', POINTER(UInt16)),
        ('ClientPrincipalNameBufferLength', UInt32),
        ('ClientPrincipalName', POINTER(UInt16)),
        ('AuthenticationLevel', UInt32),
        ('AuthenticationService', UInt32),
        ('NullSession', win32more.Foundation.BOOL),
    ]
    return RPC_CALL_ATTRIBUTES_V1_W
def _define_RPC_CALL_ATTRIBUTES_V2_A_head():
    class RPC_CALL_ATTRIBUTES_V2_A(Structure):
        pass
    return RPC_CALL_ATTRIBUTES_V2_A
def _define_RPC_CALL_ATTRIBUTES_V2_A():
    RPC_CALL_ATTRIBUTES_V2_A = win32more.System.Rpc.RPC_CALL_ATTRIBUTES_V2_A_head
    RPC_CALL_ATTRIBUTES_V2_A._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ServerPrincipalNameBufferLength', UInt32),
        ('ServerPrincipalName', c_char_p_no),
        ('ClientPrincipalNameBufferLength', UInt32),
        ('ClientPrincipalName', c_char_p_no),
        ('AuthenticationLevel', UInt32),
        ('AuthenticationService', UInt32),
        ('NullSession', win32more.Foundation.BOOL),
        ('KernelModeCaller', win32more.Foundation.BOOL),
        ('ProtocolSequence', UInt32),
        ('IsClientLocal', UInt32),
        ('ClientPID', win32more.Foundation.HANDLE),
        ('CallStatus', UInt32),
        ('CallType', win32more.System.Rpc.RpcCallType),
        ('CallLocalAddress', POINTER(win32more.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)),
        ('OpNum', UInt16),
        ('InterfaceUuid', Guid),
    ]
    return RPC_CALL_ATTRIBUTES_V2_A
def _define_RPC_CALL_ATTRIBUTES_V2_W_head():
    class RPC_CALL_ATTRIBUTES_V2_W(Structure):
        pass
    return RPC_CALL_ATTRIBUTES_V2_W
def _define_RPC_CALL_ATTRIBUTES_V2_W():
    RPC_CALL_ATTRIBUTES_V2_W = win32more.System.Rpc.RPC_CALL_ATTRIBUTES_V2_W_head
    RPC_CALL_ATTRIBUTES_V2_W._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ServerPrincipalNameBufferLength', UInt32),
        ('ServerPrincipalName', POINTER(UInt16)),
        ('ClientPrincipalNameBufferLength', UInt32),
        ('ClientPrincipalName', POINTER(UInt16)),
        ('AuthenticationLevel', UInt32),
        ('AuthenticationService', UInt32),
        ('NullSession', win32more.Foundation.BOOL),
        ('KernelModeCaller', win32more.Foundation.BOOL),
        ('ProtocolSequence', UInt32),
        ('IsClientLocal', win32more.System.Rpc.RpcCallClientLocality),
        ('ClientPID', win32more.Foundation.HANDLE),
        ('CallStatus', UInt32),
        ('CallType', win32more.System.Rpc.RpcCallType),
        ('CallLocalAddress', POINTER(win32more.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)),
        ('OpNum', UInt16),
        ('InterfaceUuid', Guid),
    ]
    return RPC_CALL_ATTRIBUTES_V2_W
def _define_RPC_CALL_ATTRIBUTES_V3_A_head():
    class RPC_CALL_ATTRIBUTES_V3_A(Structure):
        pass
    return RPC_CALL_ATTRIBUTES_V3_A
def _define_RPC_CALL_ATTRIBUTES_V3_A():
    RPC_CALL_ATTRIBUTES_V3_A = win32more.System.Rpc.RPC_CALL_ATTRIBUTES_V3_A_head
    RPC_CALL_ATTRIBUTES_V3_A._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ServerPrincipalNameBufferLength', UInt32),
        ('ServerPrincipalName', c_char_p_no),
        ('ClientPrincipalNameBufferLength', UInt32),
        ('ClientPrincipalName', c_char_p_no),
        ('AuthenticationLevel', UInt32),
        ('AuthenticationService', UInt32),
        ('NullSession', win32more.Foundation.BOOL),
        ('KernelModeCaller', win32more.Foundation.BOOL),
        ('ProtocolSequence', UInt32),
        ('IsClientLocal', UInt32),
        ('ClientPID', win32more.Foundation.HANDLE),
        ('CallStatus', UInt32),
        ('CallType', win32more.System.Rpc.RpcCallType),
        ('CallLocalAddress', POINTER(win32more.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)),
        ('OpNum', UInt16),
        ('InterfaceUuid', Guid),
        ('ClientIdentifierBufferLength', UInt32),
        ('ClientIdentifier', c_char_p_no),
    ]
    return RPC_CALL_ATTRIBUTES_V3_A
def _define_RPC_CALL_ATTRIBUTES_V3_W_head():
    class RPC_CALL_ATTRIBUTES_V3_W(Structure):
        pass
    return RPC_CALL_ATTRIBUTES_V3_W
def _define_RPC_CALL_ATTRIBUTES_V3_W():
    RPC_CALL_ATTRIBUTES_V3_W = win32more.System.Rpc.RPC_CALL_ATTRIBUTES_V3_W_head
    RPC_CALL_ATTRIBUTES_V3_W._fields_ = [
        ('Version', UInt32),
        ('Flags', UInt32),
        ('ServerPrincipalNameBufferLength', UInt32),
        ('ServerPrincipalName', POINTER(UInt16)),
        ('ClientPrincipalNameBufferLength', UInt32),
        ('ClientPrincipalName', POINTER(UInt16)),
        ('AuthenticationLevel', UInt32),
        ('AuthenticationService', UInt32),
        ('NullSession', win32more.Foundation.BOOL),
        ('KernelModeCaller', win32more.Foundation.BOOL),
        ('ProtocolSequence', UInt32),
        ('IsClientLocal', win32more.System.Rpc.RpcCallClientLocality),
        ('ClientPID', win32more.Foundation.HANDLE),
        ('CallStatus', UInt32),
        ('CallType', win32more.System.Rpc.RpcCallType),
        ('CallLocalAddress', POINTER(win32more.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)),
        ('OpNum', UInt16),
        ('InterfaceUuid', Guid),
        ('ClientIdentifierBufferLength', UInt32),
        ('ClientIdentifier', c_char_p_no),
    ]
    return RPC_CALL_ATTRIBUTES_V3_W
def _define_RPC_CALL_LOCAL_ADDRESS_V1_head():
    class RPC_CALL_LOCAL_ADDRESS_V1(Structure):
        pass
    return RPC_CALL_LOCAL_ADDRESS_V1
def _define_RPC_CALL_LOCAL_ADDRESS_V1():
    RPC_CALL_LOCAL_ADDRESS_V1 = win32more.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head
    RPC_CALL_LOCAL_ADDRESS_V1._fields_ = [
        ('Version', UInt32),
        ('Buffer', c_void_p),
        ('BufferSize', UInt32),
        ('AddressFormat', win32more.System.Rpc.RpcLocalAddressFormat),
    ]
    return RPC_CALL_LOCAL_ADDRESS_V1
def _define_RPC_CLIENT_ALLOC():
    return WINFUNCTYPE(c_void_p,UIntPtr)
def _define_RPC_CLIENT_FREE():
    return WINFUNCTYPE(Void,c_void_p)
def _define_RPC_CLIENT_INFORMATION1_head():
    class RPC_CLIENT_INFORMATION1(Structure):
        pass
    return RPC_CLIENT_INFORMATION1
def _define_RPC_CLIENT_INFORMATION1():
    RPC_CLIENT_INFORMATION1 = win32more.System.Rpc.RPC_CLIENT_INFORMATION1_head
    RPC_CLIENT_INFORMATION1._fields_ = [
        ('UserName', c_char_p_no),
        ('ComputerName', c_char_p_no),
        ('Privilege', UInt16),
        ('AuthFlags', UInt32),
    ]
    return RPC_CLIENT_INFORMATION1
def _define_RPC_CLIENT_INTERFACE_head():
    class RPC_CLIENT_INTERFACE(Structure):
        pass
    return RPC_CLIENT_INTERFACE
def _define_RPC_CLIENT_INTERFACE():
    RPC_CLIENT_INTERFACE = win32more.System.Rpc.RPC_CLIENT_INTERFACE_head
    RPC_CLIENT_INTERFACE._fields_ = [
        ('Length', UInt32),
        ('InterfaceId', win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER),
        ('TransferSyntax', win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER),
        ('DispatchTable', POINTER(win32more.System.Rpc.RPC_DISPATCH_TABLE_head)),
        ('RpcProtseqEndpointCount', UInt32),
        ('RpcProtseqEndpoint', POINTER(win32more.System.Rpc.RPC_PROTSEQ_ENDPOINT_head)),
        ('Reserved', UIntPtr),
        ('InterpreterInfo', c_void_p),
        ('Flags', UInt32),
    ]
    return RPC_CLIENT_INTERFACE
def _define_RPC_DISPATCH_FUNCTION():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.RPC_MESSAGE_head))
def _define_RPC_DISPATCH_TABLE_head():
    class RPC_DISPATCH_TABLE(Structure):
        pass
    return RPC_DISPATCH_TABLE
def _define_RPC_DISPATCH_TABLE():
    RPC_DISPATCH_TABLE = win32more.System.Rpc.RPC_DISPATCH_TABLE_head
    RPC_DISPATCH_TABLE._fields_ = [
        ('DispatchTableCount', UInt32),
        ('DispatchTable', win32more.System.Rpc.RPC_DISPATCH_FUNCTION),
        ('Reserved', IntPtr),
    ]
    return RPC_DISPATCH_TABLE
def _define_RPC_EE_INFO_PARAM_head():
    class RPC_EE_INFO_PARAM(Structure):
        pass
    return RPC_EE_INFO_PARAM
def _define_RPC_EE_INFO_PARAM():
    RPC_EE_INFO_PARAM = win32more.System.Rpc.RPC_EE_INFO_PARAM_head
    class RPC_EE_INFO_PARAM__u_e__Union(Union):
        pass
    RPC_EE_INFO_PARAM__u_e__Union._fields_ = [
        ('AnsiString', win32more.Foundation.PSTR),
        ('UnicodeString', win32more.Foundation.PWSTR),
        ('LVal', Int32),
        ('SVal', Int16),
        ('PVal', UInt64),
        ('BVal', win32more.System.Rpc.BinaryParam),
    ]
    RPC_EE_INFO_PARAM._fields_ = [
        ('ParameterType', win32more.System.Rpc.ExtendedErrorParamTypes),
        ('u', RPC_EE_INFO_PARAM__u_e__Union),
    ]
    return RPC_EE_INFO_PARAM
def _define_RPC_ENDPOINT_TEMPLATEA_head():
    class RPC_ENDPOINT_TEMPLATEA(Structure):
        pass
    return RPC_ENDPOINT_TEMPLATEA
def _define_RPC_ENDPOINT_TEMPLATEA():
    RPC_ENDPOINT_TEMPLATEA = win32more.System.Rpc.RPC_ENDPOINT_TEMPLATEA_head
    RPC_ENDPOINT_TEMPLATEA._fields_ = [
        ('Version', UInt32),
        ('ProtSeq', c_char_p_no),
        ('Endpoint', c_char_p_no),
        ('SecurityDescriptor', c_void_p),
        ('Backlog', UInt32),
    ]
    return RPC_ENDPOINT_TEMPLATEA
def _define_RPC_ENDPOINT_TEMPLATEW_head():
    class RPC_ENDPOINT_TEMPLATEW(Structure):
        pass
    return RPC_ENDPOINT_TEMPLATEW
def _define_RPC_ENDPOINT_TEMPLATEW():
    RPC_ENDPOINT_TEMPLATEW = win32more.System.Rpc.RPC_ENDPOINT_TEMPLATEW_head
    RPC_ENDPOINT_TEMPLATEW._fields_ = [
        ('Version', UInt32),
        ('ProtSeq', POINTER(UInt16)),
        ('Endpoint', POINTER(UInt16)),
        ('SecurityDescriptor', c_void_p),
        ('Backlog', UInt32),
    ]
    return RPC_ENDPOINT_TEMPLATEW
def _define_RPC_ERROR_ENUM_HANDLE_head():
    class RPC_ERROR_ENUM_HANDLE(Structure):
        pass
    return RPC_ERROR_ENUM_HANDLE
def _define_RPC_ERROR_ENUM_HANDLE():
    RPC_ERROR_ENUM_HANDLE = win32more.System.Rpc.RPC_ERROR_ENUM_HANDLE_head
    RPC_ERROR_ENUM_HANDLE._fields_ = [
        ('Signature', UInt32),
        ('CurrentPos', c_void_p),
        ('Head', c_void_p),
    ]
    return RPC_ERROR_ENUM_HANDLE
def _define_RPC_EXTENDED_ERROR_INFO_head():
    class RPC_EXTENDED_ERROR_INFO(Structure):
        pass
    return RPC_EXTENDED_ERROR_INFO
def _define_RPC_EXTENDED_ERROR_INFO():
    RPC_EXTENDED_ERROR_INFO = win32more.System.Rpc.RPC_EXTENDED_ERROR_INFO_head
    class RPC_EXTENDED_ERROR_INFO__u_e__Union(Union):
        pass
    RPC_EXTENDED_ERROR_INFO__u_e__Union._fields_ = [
        ('SystemTime', win32more.Foundation.SYSTEMTIME),
        ('FileTime', win32more.Foundation.FILETIME),
    ]
    RPC_EXTENDED_ERROR_INFO._fields_ = [
        ('Version', UInt32),
        ('ComputerName', win32more.Foundation.PWSTR),
        ('ProcessID', UInt32),
        ('u', RPC_EXTENDED_ERROR_INFO__u_e__Union),
        ('GeneratingComponent', UInt32),
        ('Status', UInt32),
        ('DetectionLocation', UInt16),
        ('Flags', UInt16),
        ('NumberOfParameters', Int32),
        ('Parameters', win32more.System.Rpc.RPC_EE_INFO_PARAM * 4),
    ]
    return RPC_EXTENDED_ERROR_INFO
def _define_RPC_FORWARD_FUNCTION():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,POINTER(Guid),POINTER(win32more.System.Rpc.RPC_VERSION_head),POINTER(Guid),c_char_p_no,POINTER(c_void_p))
def _define_RPC_HTTP_PROXY_FREE_STRING():
    return WINFUNCTYPE(Void,POINTER(UInt16))
RPC_HTTP_REDIRECTOR_STAGE = Int32
RPCHTTP_RS_REDIRECT = 1
RPCHTTP_RS_ACCESS_1 = 2
RPCHTTP_RS_SESSION = 3
RPCHTTP_RS_ACCESS_2 = 4
RPCHTTP_RS_INTERFACE = 5
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_A_head():
    class RPC_HTTP_TRANSPORT_CREDENTIALS_A(Structure):
        pass
    return RPC_HTTP_TRANSPORT_CREDENTIALS_A
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_A():
    RPC_HTTP_TRANSPORT_CREDENTIALS_A = win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head
    RPC_HTTP_TRANSPORT_CREDENTIALS_A._fields_ = [
        ('TransportCredentials', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)),
        ('Flags', win32more.System.Rpc.RPC_C_HTTP_FLAGS),
        ('AuthenticationTarget', win32more.System.Rpc.RPC_C_HTTP_AUTHN_TARGET),
        ('NumberOfAuthnSchemes', UInt32),
        ('AuthnSchemes', POINTER(UInt32)),
        ('ServerCertificateSubject', c_char_p_no),
    ]
    return RPC_HTTP_TRANSPORT_CREDENTIALS_A
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A_head():
    class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A(Structure):
        pass
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A():
    RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A = win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A_head
    RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A._fields_ = [
        ('TransportCredentials', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)),
        ('Flags', win32more.System.Rpc.RPC_C_HTTP_FLAGS),
        ('AuthenticationTarget', win32more.System.Rpc.RPC_C_HTTP_AUTHN_TARGET),
        ('NumberOfAuthnSchemes', UInt32),
        ('AuthnSchemes', POINTER(UInt32)),
        ('ServerCertificateSubject', c_char_p_no),
        ('ProxyCredentials', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)),
        ('NumberOfProxyAuthnSchemes', UInt32),
        ('ProxyAuthnSchemes', POINTER(UInt32)),
    ]
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W_head():
    class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W(Structure):
        pass
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W():
    RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W = win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W_head
    RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W._fields_ = [
        ('TransportCredentials', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)),
        ('Flags', win32more.System.Rpc.RPC_C_HTTP_FLAGS),
        ('AuthenticationTarget', win32more.System.Rpc.RPC_C_HTTP_AUTHN_TARGET),
        ('NumberOfAuthnSchemes', UInt32),
        ('AuthnSchemes', POINTER(UInt32)),
        ('ServerCertificateSubject', POINTER(UInt16)),
        ('ProxyCredentials', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)),
        ('NumberOfProxyAuthnSchemes', UInt32),
        ('ProxyAuthnSchemes', POINTER(UInt32)),
    ]
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A_head():
    class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A(Structure):
        pass
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A():
    RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A = win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A_head
    RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A._fields_ = [
        ('TransportCredentials', c_void_p),
        ('Flags', win32more.System.Rpc.RPC_C_HTTP_FLAGS),
        ('AuthenticationTarget', win32more.System.Rpc.RPC_C_HTTP_AUTHN_TARGET),
        ('NumberOfAuthnSchemes', UInt32),
        ('AuthnSchemes', POINTER(UInt32)),
        ('ServerCertificateSubject', c_char_p_no),
        ('ProxyCredentials', c_void_p),
        ('NumberOfProxyAuthnSchemes', UInt32),
        ('ProxyAuthnSchemes', POINTER(UInt32)),
    ]
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W_head():
    class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W(Structure):
        pass
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W():
    RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W = win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W_head
    RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W._fields_ = [
        ('TransportCredentials', c_void_p),
        ('Flags', win32more.System.Rpc.RPC_C_HTTP_FLAGS),
        ('AuthenticationTarget', win32more.System.Rpc.RPC_C_HTTP_AUTHN_TARGET),
        ('NumberOfAuthnSchemes', UInt32),
        ('AuthnSchemes', POINTER(UInt32)),
        ('ServerCertificateSubject', POINTER(UInt16)),
        ('ProxyCredentials', c_void_p),
        ('NumberOfProxyAuthnSchemes', UInt32),
        ('ProxyAuthnSchemes', POINTER(UInt32)),
    ]
    return RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_W_head():
    class RPC_HTTP_TRANSPORT_CREDENTIALS_W(Structure):
        pass
    return RPC_HTTP_TRANSPORT_CREDENTIALS_W
def _define_RPC_HTTP_TRANSPORT_CREDENTIALS_W():
    RPC_HTTP_TRANSPORT_CREDENTIALS_W = win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head
    RPC_HTTP_TRANSPORT_CREDENTIALS_W._fields_ = [
        ('TransportCredentials', POINTER(win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)),
        ('Flags', win32more.System.Rpc.RPC_C_HTTP_FLAGS),
        ('AuthenticationTarget', win32more.System.Rpc.RPC_C_HTTP_AUTHN_TARGET),
        ('NumberOfAuthnSchemes', UInt32),
        ('AuthnSchemes', POINTER(UInt32)),
        ('ServerCertificateSubject', POINTER(UInt16)),
    ]
    return RPC_HTTP_TRANSPORT_CREDENTIALS_W
def _define_RPC_IF_CALLBACK_FN():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,c_void_p,c_void_p)
def _define_RPC_IF_ID_head():
    class RPC_IF_ID(Structure):
        pass
    return RPC_IF_ID
def _define_RPC_IF_ID():
    RPC_IF_ID = win32more.System.Rpc.RPC_IF_ID_head
    RPC_IF_ID._fields_ = [
        ('Uuid', Guid),
        ('VersMajor', UInt16),
        ('VersMinor', UInt16),
    ]
    return RPC_IF_ID
def _define_RPC_IF_ID_VECTOR_head():
    class RPC_IF_ID_VECTOR(Structure):
        pass
    return RPC_IF_ID_VECTOR
def _define_RPC_IF_ID_VECTOR():
    RPC_IF_ID_VECTOR = win32more.System.Rpc.RPC_IF_ID_VECTOR_head
    RPC_IF_ID_VECTOR._fields_ = [
        ('Count', UInt32),
        ('IfId', POINTER(win32more.System.Rpc.RPC_IF_ID_head) * 1),
    ]
    return RPC_IF_ID_VECTOR
def _define_RPC_IMPORT_CONTEXT_P_head():
    class RPC_IMPORT_CONTEXT_P(Structure):
        pass
    return RPC_IMPORT_CONTEXT_P
def _define_RPC_IMPORT_CONTEXT_P():
    RPC_IMPORT_CONTEXT_P = win32more.System.Rpc.RPC_IMPORT_CONTEXT_P_head
    RPC_IMPORT_CONTEXT_P._fields_ = [
        ('LookupContext', c_void_p),
        ('ProposedHandle', c_void_p),
        ('Bindings', POINTER(win32more.System.Rpc.RPC_BINDING_VECTOR_head)),
    ]
    return RPC_IMPORT_CONTEXT_P
def _define_RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN():
    return WINFUNCTYPE(Void,c_void_p,c_void_p,UInt32)
def _define_RPC_INTERFACE_TEMPLATEA_head():
    class RPC_INTERFACE_TEMPLATEA(Structure):
        pass
    return RPC_INTERFACE_TEMPLATEA
def _define_RPC_INTERFACE_TEMPLATEA():
    RPC_INTERFACE_TEMPLATEA = win32more.System.Rpc.RPC_INTERFACE_TEMPLATEA_head
    RPC_INTERFACE_TEMPLATEA._fields_ = [
        ('Version', UInt32),
        ('IfSpec', c_void_p),
        ('MgrTypeUuid', POINTER(Guid)),
        ('MgrEpv', c_void_p),
        ('Flags', UInt32),
        ('MaxCalls', UInt32),
        ('MaxRpcSize', UInt32),
        ('IfCallback', win32more.System.Rpc.RPC_IF_CALLBACK_FN),
        ('UuidVector', POINTER(win32more.System.Rpc.UUID_VECTOR_head)),
        ('Annotation', c_char_p_no),
        ('SecurityDescriptor', c_void_p),
    ]
    return RPC_INTERFACE_TEMPLATEA
def _define_RPC_INTERFACE_TEMPLATEW_head():
    class RPC_INTERFACE_TEMPLATEW(Structure):
        pass
    return RPC_INTERFACE_TEMPLATEW
def _define_RPC_INTERFACE_TEMPLATEW():
    RPC_INTERFACE_TEMPLATEW = win32more.System.Rpc.RPC_INTERFACE_TEMPLATEW_head
    RPC_INTERFACE_TEMPLATEW._fields_ = [
        ('Version', UInt32),
        ('IfSpec', c_void_p),
        ('MgrTypeUuid', POINTER(Guid)),
        ('MgrEpv', c_void_p),
        ('Flags', UInt32),
        ('MaxCalls', UInt32),
        ('MaxRpcSize', UInt32),
        ('IfCallback', win32more.System.Rpc.RPC_IF_CALLBACK_FN),
        ('UuidVector', POINTER(win32more.System.Rpc.UUID_VECTOR_head)),
        ('Annotation', POINTER(UInt16)),
        ('SecurityDescriptor', c_void_p),
    ]
    return RPC_INTERFACE_TEMPLATEW
def _define_RPC_MESSAGE_head():
    class RPC_MESSAGE(Structure):
        pass
    return RPC_MESSAGE
def _define_RPC_MESSAGE():
    RPC_MESSAGE = win32more.System.Rpc.RPC_MESSAGE_head
    RPC_MESSAGE._fields_ = [
        ('Handle', c_void_p),
        ('DataRepresentation', UInt32),
        ('Buffer', c_void_p),
        ('BufferLength', UInt32),
        ('ProcNum', UInt32),
        ('TransferSyntax', POINTER(win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER_head)),
        ('RpcInterfaceInformation', c_void_p),
        ('ReservedForRuntime', c_void_p),
        ('ManagerEpv', c_void_p),
        ('ImportContext', c_void_p),
        ('RpcFlags', UInt32),
    ]
    return RPC_MESSAGE
def _define_RPC_MGMT_AUTHORIZATION_FN():
    return WINFUNCTYPE(Int32,c_void_p,UInt32,POINTER(win32more.System.Rpc.RPC_STATUS))
def _define_RPC_NEW_HTTP_PROXY_CHANNEL():
    return WINFUNCTYPE(win32more.System.Rpc.RPC_STATUS,win32more.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),c_void_p,c_void_p,c_void_p,c_void_p,UInt32,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)))
RPC_NOTIFICATION_TYPES = Int32
RPC_NOTIFICATION_TYPES_RpcNotificationTypeNone = 0
RPC_NOTIFICATION_TYPES_RpcNotificationTypeEvent = 1
RPC_NOTIFICATION_TYPES_RpcNotificationTypeApc = 2
RPC_NOTIFICATION_TYPES_RpcNotificationTypeIoc = 3
RPC_NOTIFICATION_TYPES_RpcNotificationTypeHwnd = 4
RPC_NOTIFICATION_TYPES_RpcNotificationTypeCallback = 5
RPC_NOTIFICATIONS = Int32
RPC_NOTIFICATIONS_RpcNotificationCallNone = 0
RPC_NOTIFICATIONS_RpcNotificationClientDisconnect = 1
RPC_NOTIFICATIONS_RpcNotificationCallCancel = 2
def _define_RPC_OBJECT_INQ_FN():
    return WINFUNCTYPE(Void,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Rpc.RPC_STATUS))
def _define_RPC_POLICY_head():
    class RPC_POLICY(Structure):
        pass
    return RPC_POLICY
def _define_RPC_POLICY():
    RPC_POLICY = win32more.System.Rpc.RPC_POLICY_head
    RPC_POLICY._fields_ = [
        ('Length', UInt32),
        ('EndpointFlags', UInt32),
        ('NICFlags', UInt32),
    ]
    return RPC_POLICY
def _define_RPC_PROTSEQ_ENDPOINT_head():
    class RPC_PROTSEQ_ENDPOINT(Structure):
        pass
    return RPC_PROTSEQ_ENDPOINT
def _define_RPC_PROTSEQ_ENDPOINT():
    RPC_PROTSEQ_ENDPOINT = win32more.System.Rpc.RPC_PROTSEQ_ENDPOINT_head
    RPC_PROTSEQ_ENDPOINT._fields_ = [
        ('RpcProtocolSequence', c_char_p_no),
        ('Endpoint', c_char_p_no),
    ]
    return RPC_PROTSEQ_ENDPOINT
def _define_RPC_PROTSEQ_VECTORA_head():
    class RPC_PROTSEQ_VECTORA(Structure):
        pass
    return RPC_PROTSEQ_VECTORA
def _define_RPC_PROTSEQ_VECTORA():
    RPC_PROTSEQ_VECTORA = win32more.System.Rpc.RPC_PROTSEQ_VECTORA_head
    RPC_PROTSEQ_VECTORA._fields_ = [
        ('Count', UInt32),
        ('Protseq', c_char_p_no * 1),
    ]
    return RPC_PROTSEQ_VECTORA
def _define_RPC_PROTSEQ_VECTORW_head():
    class RPC_PROTSEQ_VECTORW(Structure):
        pass
    return RPC_PROTSEQ_VECTORW
def _define_RPC_PROTSEQ_VECTORW():
    RPC_PROTSEQ_VECTORW = win32more.System.Rpc.RPC_PROTSEQ_VECTORW_head
    RPC_PROTSEQ_VECTORW._fields_ = [
        ('Count', UInt32),
        ('Protseq', POINTER(UInt16) * 1),
    ]
    return RPC_PROTSEQ_VECTORW
def _define_RPC_SEC_CONTEXT_KEY_INFO_head():
    class RPC_SEC_CONTEXT_KEY_INFO(Structure):
        pass
    return RPC_SEC_CONTEXT_KEY_INFO
def _define_RPC_SEC_CONTEXT_KEY_INFO():
    RPC_SEC_CONTEXT_KEY_INFO = win32more.System.Rpc.RPC_SEC_CONTEXT_KEY_INFO_head
    RPC_SEC_CONTEXT_KEY_INFO._fields_ = [
        ('EncryptAlgorithm', UInt32),
        ('KeySize', UInt32),
        ('SignatureAlgorithm', UInt32),
    ]
    return RPC_SEC_CONTEXT_KEY_INFO
def _define_RPC_SECURITY_CALLBACK_FN():
    return WINFUNCTYPE(Void,c_void_p)
def _define_RPC_SECURITY_QOS_head():
    class RPC_SECURITY_QOS(Structure):
        pass
    return RPC_SECURITY_QOS
def _define_RPC_SECURITY_QOS():
    RPC_SECURITY_QOS = win32more.System.Rpc.RPC_SECURITY_QOS_head
    RPC_SECURITY_QOS._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
    ]
    return RPC_SECURITY_QOS
def _define_RPC_SECURITY_QOS_V2_A_head():
    class RPC_SECURITY_QOS_V2_A(Structure):
        pass
    return RPC_SECURITY_QOS_V2_A
def _define_RPC_SECURITY_QOS_V2_A():
    RPC_SECURITY_QOS_V2_A = win32more.System.Rpc.RPC_SECURITY_QOS_V2_A_head
    class RPC_SECURITY_QOS_V2_A__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V2_A__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)),
    ]
    RPC_SECURITY_QOS_V2_A._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V2_A__u_e__Union),
    ]
    return RPC_SECURITY_QOS_V2_A
def _define_RPC_SECURITY_QOS_V2_W_head():
    class RPC_SECURITY_QOS_V2_W(Structure):
        pass
    return RPC_SECURITY_QOS_V2_W
def _define_RPC_SECURITY_QOS_V2_W():
    RPC_SECURITY_QOS_V2_W = win32more.System.Rpc.RPC_SECURITY_QOS_V2_W_head
    class RPC_SECURITY_QOS_V2_W__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V2_W__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)),
    ]
    RPC_SECURITY_QOS_V2_W._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V2_W__u_e__Union),
    ]
    return RPC_SECURITY_QOS_V2_W
def _define_RPC_SECURITY_QOS_V3_A_head():
    class RPC_SECURITY_QOS_V3_A(Structure):
        pass
    return RPC_SECURITY_QOS_V3_A
def _define_RPC_SECURITY_QOS_V3_A():
    RPC_SECURITY_QOS_V3_A = win32more.System.Rpc.RPC_SECURITY_QOS_V3_A_head
    class RPC_SECURITY_QOS_V3_A__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V3_A__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)),
    ]
    RPC_SECURITY_QOS_V3_A._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V3_A__u_e__Union),
        ('Sid', c_void_p),
    ]
    return RPC_SECURITY_QOS_V3_A
def _define_RPC_SECURITY_QOS_V3_W_head():
    class RPC_SECURITY_QOS_V3_W(Structure):
        pass
    return RPC_SECURITY_QOS_V3_W
def _define_RPC_SECURITY_QOS_V3_W():
    RPC_SECURITY_QOS_V3_W = win32more.System.Rpc.RPC_SECURITY_QOS_V3_W_head
    class RPC_SECURITY_QOS_V3_W__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V3_W__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)),
    ]
    RPC_SECURITY_QOS_V3_W._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V3_W__u_e__Union),
        ('Sid', c_void_p),
    ]
    return RPC_SECURITY_QOS_V3_W
def _define_RPC_SECURITY_QOS_V4_A_head():
    class RPC_SECURITY_QOS_V4_A(Structure):
        pass
    return RPC_SECURITY_QOS_V4_A
def _define_RPC_SECURITY_QOS_V4_A():
    RPC_SECURITY_QOS_V4_A = win32more.System.Rpc.RPC_SECURITY_QOS_V4_A_head
    class RPC_SECURITY_QOS_V4_A__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V4_A__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)),
    ]
    RPC_SECURITY_QOS_V4_A._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V4_A__u_e__Union),
        ('Sid', c_void_p),
        ('EffectiveOnly', UInt32),
    ]
    return RPC_SECURITY_QOS_V4_A
def _define_RPC_SECURITY_QOS_V4_W_head():
    class RPC_SECURITY_QOS_V4_W(Structure):
        pass
    return RPC_SECURITY_QOS_V4_W
def _define_RPC_SECURITY_QOS_V4_W():
    RPC_SECURITY_QOS_V4_W = win32more.System.Rpc.RPC_SECURITY_QOS_V4_W_head
    class RPC_SECURITY_QOS_V4_W__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V4_W__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)),
    ]
    RPC_SECURITY_QOS_V4_W._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V4_W__u_e__Union),
        ('Sid', c_void_p),
        ('EffectiveOnly', UInt32),
    ]
    return RPC_SECURITY_QOS_V4_W
def _define_RPC_SECURITY_QOS_V5_A_head():
    class RPC_SECURITY_QOS_V5_A(Structure):
        pass
    return RPC_SECURITY_QOS_V5_A
def _define_RPC_SECURITY_QOS_V5_A():
    RPC_SECURITY_QOS_V5_A = win32more.System.Rpc.RPC_SECURITY_QOS_V5_A_head
    class RPC_SECURITY_QOS_V5_A__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V5_A__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)),
    ]
    RPC_SECURITY_QOS_V5_A._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V5_A__u_e__Union),
        ('Sid', c_void_p),
        ('EffectiveOnly', UInt32),
        ('ServerSecurityDescriptor', c_void_p),
    ]
    return RPC_SECURITY_QOS_V5_A
def _define_RPC_SECURITY_QOS_V5_W_head():
    class RPC_SECURITY_QOS_V5_W(Structure):
        pass
    return RPC_SECURITY_QOS_V5_W
def _define_RPC_SECURITY_QOS_V5_W():
    RPC_SECURITY_QOS_V5_W = win32more.System.Rpc.RPC_SECURITY_QOS_V5_W_head
    class RPC_SECURITY_QOS_V5_W__u_e__Union(Union):
        pass
    RPC_SECURITY_QOS_V5_W__u_e__Union._fields_ = [
        ('HttpCredentials', POINTER(win32more.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)),
    ]
    RPC_SECURITY_QOS_V5_W._fields_ = [
        ('Version', UInt32),
        ('Capabilities', win32more.System.Rpc.RPC_C_QOS_CAPABILITIES),
        ('IdentityTracking', win32more.System.Rpc.RPC_C_QOS_IDENTITY),
        ('ImpersonationType', win32more.System.Com.RPC_C_IMP_LEVEL),
        ('AdditionalSecurityInfoType', win32more.System.Rpc.RPC_C_AUTHN_INFO_TYPE),
        ('u', RPC_SECURITY_QOS_V5_W__u_e__Union),
        ('Sid', c_void_p),
        ('EffectiveOnly', UInt32),
        ('ServerSecurityDescriptor', c_void_p),
    ]
    return RPC_SECURITY_QOS_V5_W
def _define_RPC_SERVER_INTERFACE_head():
    class RPC_SERVER_INTERFACE(Structure):
        pass
    return RPC_SERVER_INTERFACE
def _define_RPC_SERVER_INTERFACE():
    RPC_SERVER_INTERFACE = win32more.System.Rpc.RPC_SERVER_INTERFACE_head
    RPC_SERVER_INTERFACE._fields_ = [
        ('Length', UInt32),
        ('InterfaceId', win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER),
        ('TransferSyntax', win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER),
        ('DispatchTable', POINTER(win32more.System.Rpc.RPC_DISPATCH_TABLE_head)),
        ('RpcProtseqEndpointCount', UInt32),
        ('RpcProtseqEndpoint', POINTER(win32more.System.Rpc.RPC_PROTSEQ_ENDPOINT_head)),
        ('DefaultManagerEpv', c_void_p),
        ('InterpreterInfo', c_void_p),
        ('Flags', UInt32),
    ]
    return RPC_SERVER_INTERFACE
def _define_RPC_SETFILTER_FUNC():
    return CFUNCTYPE(Void,win32more.System.Rpc.RPCLT_PDU_FILTER_FUNC)
def _define_RPC_STATS_VECTOR_head():
    class RPC_STATS_VECTOR(Structure):
        pass
    return RPC_STATS_VECTOR
def _define_RPC_STATS_VECTOR():
    RPC_STATS_VECTOR = win32more.System.Rpc.RPC_STATS_VECTOR_head
    RPC_STATS_VECTOR._fields_ = [
        ('Count', UInt32),
        ('Stats', UInt32 * 1),
    ]
    return RPC_STATS_VECTOR
RPC_STATUS = Int32
RPC_S_INVALID_STRING_BINDING = 1700
RPC_S_WRONG_KIND_OF_BINDING = 1701
RPC_S_INVALID_BINDING = 1702
RPC_S_PROTSEQ_NOT_SUPPORTED = 1703
RPC_S_INVALID_RPC_PROTSEQ = 1704
RPC_S_INVALID_STRING_UUID = 1705
RPC_S_INVALID_ENDPOINT_FORMAT = 1706
RPC_S_INVALID_NET_ADDR = 1707
RPC_S_NO_ENDPOINT_FOUND = 1708
RPC_S_INVALID_TIMEOUT = 1709
RPC_S_OBJECT_NOT_FOUND = 1710
RPC_S_ALREADY_REGISTERED = 1711
RPC_S_TYPE_ALREADY_REGISTERED = 1712
RPC_S_ALREADY_LISTENING = 1713
RPC_S_NO_PROTSEQS_REGISTERED = 1714
RPC_S_NOT_LISTENING = 1715
RPC_S_UNKNOWN_MGR_TYPE = 1716
RPC_S_UNKNOWN_IF = 1717
RPC_S_NO_BINDINGS = 1718
RPC_S_NO_PROTSEQS = 1719
RPC_S_CANT_CREATE_ENDPOINT = 1720
RPC_S_OUT_OF_RESOURCES = 1721
RPC_S_SERVER_UNAVAILABLE = 1722
RPC_S_SERVER_TOO_BUSY = 1723
RPC_S_INVALID_NETWORK_OPTIONS = 1724
RPC_S_NO_CALL_ACTIVE = 1725
RPC_S_CALL_FAILED = 1726
RPC_S_CALL_FAILED_DNE = 1727
RPC_S_PROTOCOL_ERROR = 1728
RPC_S_PROXY_ACCESS_DENIED = 1729
RPC_S_UNSUPPORTED_TRANS_SYN = 1730
RPC_S_UNSUPPORTED_TYPE = 1732
RPC_S_INVALID_TAG = 1733
RPC_S_INVALID_BOUND = 1734
RPC_S_NO_ENTRY_NAME = 1735
RPC_S_INVALID_NAME_SYNTAX = 1736
RPC_S_UNSUPPORTED_NAME_SYNTAX = 1737
RPC_S_UUID_NO_ADDRESS = 1739
RPC_S_DUPLICATE_ENDPOINT = 1740
RPC_S_UNKNOWN_AUTHN_TYPE = 1741
RPC_S_MAX_CALLS_TOO_SMALL = 1742
RPC_S_STRING_TOO_LONG = 1743
RPC_S_PROTSEQ_NOT_FOUND = 1744
RPC_S_PROCNUM_OUT_OF_RANGE = 1745
RPC_S_BINDING_HAS_NO_AUTH = 1746
RPC_S_UNKNOWN_AUTHN_SERVICE = 1747
RPC_S_UNKNOWN_AUTHN_LEVEL = 1748
RPC_S_INVALID_AUTH_IDENTITY = 1749
RPC_S_UNKNOWN_AUTHZ_SERVICE = 1750
EPT_S_INVALID_ENTRY = 1751
EPT_S_CANT_PERFORM_OP = 1752
EPT_S_NOT_REGISTERED = 1753
RPC_S_NOTHING_TO_EXPORT = 1754
RPC_S_INCOMPLETE_NAME = 1755
RPC_S_INVALID_VERS_OPTION = 1756
RPC_S_NO_MORE_MEMBERS = 1757
RPC_S_NOT_ALL_OBJS_UNEXPORTED = 1758
RPC_S_INTERFACE_NOT_FOUND = 1759
RPC_S_ENTRY_ALREADY_EXISTS = 1760
RPC_S_ENTRY_NOT_FOUND = 1761
RPC_S_NAME_SERVICE_UNAVAILABLE = 1762
RPC_S_INVALID_NAF_ID = 1763
RPC_S_CANNOT_SUPPORT = 1764
RPC_S_NO_CONTEXT_AVAILABLE = 1765
RPC_S_INTERNAL_ERROR = 1766
RPC_S_ZERO_DIVIDE = 1767
RPC_S_ADDRESS_ERROR = 1768
RPC_S_FP_DIV_ZERO = 1769
RPC_S_FP_UNDERFLOW = 1770
RPC_S_FP_OVERFLOW = 1771
RPC_S_CALL_IN_PROGRESS = 1791
RPC_S_NO_MORE_BINDINGS = 1806
RPC_S_NO_INTERFACES = 1817
RPC_S_CALL_CANCELLED = 1818
RPC_S_BINDING_INCOMPLETE = 1819
RPC_S_COMM_FAILURE = 1820
RPC_S_UNSUPPORTED_AUTHN_LEVEL = 1821
RPC_S_NO_PRINC_NAME = 1822
RPC_S_NOT_RPC_ERROR = 1823
RPC_S_UUID_LOCAL_ONLY = 1824
RPC_S_SEC_PKG_ERROR = 1825
RPC_S_NOT_CANCELLED = 1826
RPC_S_COOKIE_AUTH_FAILED = 1833
RPC_S_DO_NOT_DISTURB = 1834
RPC_S_SYSTEM_HANDLE_COUNT_EXCEEDED = 1835
RPC_S_SYSTEM_HANDLE_TYPE_MISMATCH = 1836
RPC_S_GROUP_MEMBER_NOT_FOUND = 1898
EPT_S_CANT_CREATE = 1899
RPC_S_INVALID_OBJECT = 1900
RPC_S_SEND_INCOMPLETE = 1913
RPC_S_INVALID_ASYNC_HANDLE = 1914
RPC_S_INVALID_ASYNC_CALL = 1915
RPC_S_ENTRY_TYPE_MISMATCH = 1922
RPC_S_NOT_ALL_OBJS_EXPORTED = 1923
RPC_S_INTERFACE_NOT_EXPORTED = 1924
RPC_S_PROFILE_NOT_ADDED = 1925
RPC_S_PRF_ELT_NOT_ADDED = 1926
RPC_S_PRF_ELT_NOT_REMOVED = 1927
RPC_S_GRP_ELT_NOT_ADDED = 1928
RPC_S_GRP_ELT_NOT_REMOVED = 1929
def _define_RPC_SYNTAX_IDENTIFIER_head():
    class RPC_SYNTAX_IDENTIFIER(Structure):
        pass
    return RPC_SYNTAX_IDENTIFIER
def _define_RPC_SYNTAX_IDENTIFIER():
    RPC_SYNTAX_IDENTIFIER = win32more.System.Rpc.RPC_SYNTAX_IDENTIFIER_head
    RPC_SYNTAX_IDENTIFIER._fields_ = [
        ('SyntaxGUID', Guid),
        ('SyntaxVersion', win32more.System.Rpc.RPC_VERSION),
    ]
    return RPC_SYNTAX_IDENTIFIER
def _define_RPC_TRANSFER_SYNTAX_head():
    class RPC_TRANSFER_SYNTAX(Structure):
        pass
    return RPC_TRANSFER_SYNTAX
def _define_RPC_TRANSFER_SYNTAX():
    RPC_TRANSFER_SYNTAX = win32more.System.Rpc.RPC_TRANSFER_SYNTAX_head
    RPC_TRANSFER_SYNTAX._fields_ = [
        ('Uuid', Guid),
        ('VersMajor', UInt16),
        ('VersMinor', UInt16),
    ]
    return RPC_TRANSFER_SYNTAX
def _define_RPC_VERSION_head():
    class RPC_VERSION(Structure):
        pass
    return RPC_VERSION
def _define_RPC_VERSION():
    RPC_VERSION = win32more.System.Rpc.RPC_VERSION_head
    RPC_VERSION._fields_ = [
        ('MajorVersion', UInt16),
        ('MinorVersion', UInt16),
    ]
    return RPC_VERSION
RpcCallClientLocality = Int32
RpcCallClientLocality_rcclInvalid = 0
RpcCallClientLocality_rcclLocal = 1
RpcCallClientLocality_rcclRemote = 2
RpcCallClientLocality_rcclClientUnknownLocality = 3
RpcCallType = Int32
RpcCallType_rctInvalid = 0
RpcCallType_rctNormal = 1
RpcCallType_rctTraining = 2
RpcCallType_rctGuaranteed = 3
RpcLocalAddressFormat = Int32
RpcLocalAddressFormat_rlafInvalid = 0
RpcLocalAddressFormat_rlafIPv4 = 1
RpcLocalAddressFormat_rlafIPv6 = 2
def _define_RPCLT_PDU_FILTER_FUNC():
    return WINFUNCTYPE(Void,c_void_p,UInt32,Int32)
RpcPerfCounters = Int32
RpcPerfCounters_RpcCurrentUniqueUser = 1
RpcPerfCounters_RpcBackEndConnectionAttempts = 2
RpcPerfCounters_RpcBackEndConnectionFailed = 3
RpcPerfCounters_RpcRequestsPerSecond = 4
RpcPerfCounters_RpcIncomingConnections = 5
RpcPerfCounters_RpcIncomingBandwidth = 6
RpcPerfCounters_RpcOutgoingBandwidth = 7
RpcPerfCounters_RpcAttemptedLbsDecisions = 8
RpcPerfCounters_RpcFailedLbsDecisions = 9
RpcPerfCounters_RpcAttemptedLbsMessages = 10
RpcPerfCounters_RpcFailedLbsMessages = 11
RpcPerfCounters_RpcLastCounter = 12
def _define_SCONTEXT_QUEUE_head():
    class SCONTEXT_QUEUE(Structure):
        pass
    return SCONTEXT_QUEUE
def _define_SCONTEXT_QUEUE():
    SCONTEXT_QUEUE = win32more.System.Rpc.SCONTEXT_QUEUE_head
    SCONTEXT_QUEUE._fields_ = [
        ('NumberOfObjects', UInt32),
        ('ArrayOfObjects', POINTER(POINTER(win32more.System.Rpc.NDR_SCONTEXT_1_head))),
    ]
    return SCONTEXT_QUEUE
SEC_WINNT_AUTH_IDENTITY = UInt32
SEC_WINNT_AUTH_IDENTITY_ANSI = 1
SEC_WINNT_AUTH_IDENTITY_UNICODE = 2
def _define_SEC_WINNT_AUTH_IDENTITY_A_head():
    class SEC_WINNT_AUTH_IDENTITY_A(Structure):
        pass
    return SEC_WINNT_AUTH_IDENTITY_A
def _define_SEC_WINNT_AUTH_IDENTITY_A():
    SEC_WINNT_AUTH_IDENTITY_A = win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head
    SEC_WINNT_AUTH_IDENTITY_A._fields_ = [
        ('User', c_char_p_no),
        ('UserLength', UInt32),
        ('Domain', c_char_p_no),
        ('DomainLength', UInt32),
        ('Password', c_char_p_no),
        ('PasswordLength', UInt32),
        ('Flags', win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY),
    ]
    return SEC_WINNT_AUTH_IDENTITY_A
def _define_SEC_WINNT_AUTH_IDENTITY_W_head():
    class SEC_WINNT_AUTH_IDENTITY_W(Structure):
        pass
    return SEC_WINNT_AUTH_IDENTITY_W
def _define_SEC_WINNT_AUTH_IDENTITY_W():
    SEC_WINNT_AUTH_IDENTITY_W = win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head
    SEC_WINNT_AUTH_IDENTITY_W._fields_ = [
        ('User', POINTER(UInt16)),
        ('UserLength', UInt32),
        ('Domain', POINTER(UInt16)),
        ('DomainLength', UInt32),
        ('Password', POINTER(UInt16)),
        ('PasswordLength', UInt32),
        ('Flags', win32more.System.Rpc.SEC_WINNT_AUTH_IDENTITY),
    ]
    return SEC_WINNT_AUTH_IDENTITY_W
def _define_SERVER_ROUTINE():
    return WINFUNCTYPE(Int32,)
STUB_PHASE = Int32
STUB_UNMARSHAL = 0
STUB_CALL_SERVER = 1
STUB_MARSHAL = 2
STUB_CALL_SERVER_NO_HRESULT = 3
def _define_STUB_THUNK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))
system_handle_t = Int32
SYSTEM_HANDLE_FILE = 0
SYSTEM_HANDLE_SEMAPHORE = 1
SYSTEM_HANDLE_EVENT = 2
SYSTEM_HANDLE_MUTEX = 3
SYSTEM_HANDLE_PROCESS = 4
SYSTEM_HANDLE_TOKEN = 5
SYSTEM_HANDLE_SECTION = 6
SYSTEM_HANDLE_REG_KEY = 7
SYSTEM_HANDLE_THREAD = 8
SYSTEM_HANDLE_COMPOSITION_OBJECT = 9
SYSTEM_HANDLE_SOCKET = 10
SYSTEM_HANDLE_JOB = 11
SYSTEM_HANDLE_PIPE = 12
SYSTEM_HANDLE_MAX = 12
SYSTEM_HANDLE_INVALID = 255
def _define_USER_MARSHAL_CB_head():
    class USER_MARSHAL_CB(Structure):
        pass
    return USER_MARSHAL_CB
def _define_USER_MARSHAL_CB():
    USER_MARSHAL_CB = win32more.System.Rpc.USER_MARSHAL_CB_head
    USER_MARSHAL_CB._fields_ = [
        ('Flags', UInt32),
        ('pStubMsg', POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head)),
        ('pReserve', c_char_p_no),
        ('Signature', UInt32),
        ('CBType', win32more.System.Rpc.USER_MARSHAL_CB_TYPE),
        ('pFormat', c_char_p_no),
        ('pTypeFormat', c_char_p_no),
    ]
    return USER_MARSHAL_CB
USER_MARSHAL_CB_TYPE = Int32
USER_MARSHAL_CB_BUFFER_SIZE = 0
USER_MARSHAL_CB_MARSHALL = 1
USER_MARSHAL_CB_UNMARSHALL = 2
USER_MARSHAL_CB_FREE = 3
def _define_USER_MARSHAL_FREEING_ROUTINE():
    return WINFUNCTYPE(Void,POINTER(UInt32),c_void_p)
def _define_USER_MARSHAL_MARSHALLING_ROUTINE():
    return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,c_void_p)
def _define_USER_MARSHAL_ROUTINE_QUADRUPLE_head():
    class USER_MARSHAL_ROUTINE_QUADRUPLE(Structure):
        pass
    return USER_MARSHAL_ROUTINE_QUADRUPLE
def _define_USER_MARSHAL_ROUTINE_QUADRUPLE():
    USER_MARSHAL_ROUTINE_QUADRUPLE = win32more.System.Rpc.USER_MARSHAL_ROUTINE_QUADRUPLE_head
    USER_MARSHAL_ROUTINE_QUADRUPLE._fields_ = [
        ('pfnBufferSize', win32more.System.Rpc.USER_MARSHAL_SIZING_ROUTINE),
        ('pfnMarshall', win32more.System.Rpc.USER_MARSHAL_MARSHALLING_ROUTINE),
        ('pfnUnmarshall', win32more.System.Rpc.USER_MARSHAL_UNMARSHALLING_ROUTINE),
        ('pfnFree', win32more.System.Rpc.USER_MARSHAL_FREEING_ROUTINE),
    ]
    return USER_MARSHAL_ROUTINE_QUADRUPLE
def _define_USER_MARSHAL_SIZING_ROUTINE():
    return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,c_void_p)
def _define_USER_MARSHAL_UNMARSHALLING_ROUTINE():
    return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,c_void_p)
def _define_UUID_VECTOR_head():
    class UUID_VECTOR(Structure):
        pass
    return UUID_VECTOR
def _define_UUID_VECTOR():
    UUID_VECTOR = win32more.System.Rpc.UUID_VECTOR_head
    UUID_VECTOR._fields_ = [
        ('Count', UInt32),
        ('Uuid', POINTER(Guid) * 1),
    ]
    return UUID_VECTOR
XLAT_SIDE = Int32
XLAT_SERVER = 1
XLAT_CLIENT = 2
def _define_XMIT_HELPER_ROUTINE():
    return WINFUNCTYPE(Void,POINTER(win32more.System.Rpc.MIDL_STUB_MESSAGE_head))
def _define_XMIT_ROUTINE_QUINTUPLE_head():
    class XMIT_ROUTINE_QUINTUPLE(Structure):
        pass
    return XMIT_ROUTINE_QUINTUPLE
def _define_XMIT_ROUTINE_QUINTUPLE():
    XMIT_ROUTINE_QUINTUPLE = win32more.System.Rpc.XMIT_ROUTINE_QUINTUPLE_head
    XMIT_ROUTINE_QUINTUPLE._fields_ = [
        ('pfnTranslateToXmit', win32more.System.Rpc.XMIT_HELPER_ROUTINE),
        ('pfnTranslateFromXmit', win32more.System.Rpc.XMIT_HELPER_ROUTINE),
        ('pfnFreeXmit', win32more.System.Rpc.XMIT_HELPER_ROUTINE),
        ('pfnFreeInst', win32more.System.Rpc.XMIT_HELPER_ROUTINE),
    ]
    return XMIT_ROUTINE_QUINTUPLE
__all__ = [
    "ARRAY_INFO",
    "BinaryParam",
    "CLIENT_CALL_RETURN",
    "COMM_FAULT_OFFSETS",
    "CS_TAG_GETTING_ROUTINE",
    "CS_TYPE_FROM_NETCS_ROUTINE",
    "CS_TYPE_LOCAL_SIZE_ROUTINE",
    "CS_TYPE_NET_SIZE_ROUTINE",
    "CS_TYPE_TO_NETCS_ROUTINE",
    "DCE_C_ERROR_STRING_LEN",
    "DceErrorInqTextA",
    "DceErrorInqTextW",
    "EEInfoGCCOM",
    "EEInfoGCFRS",
    "EEInfoNextRecordsMissing",
    "EEInfoPreviousRecordsMissing",
    "EEInfoUseFileTime",
    "EPT_S_CANT_CREATE",
    "EPT_S_CANT_PERFORM_OP",
    "EPT_S_INVALID_ENTRY",
    "EPT_S_NOT_REGISTERED",
    "EXPR_EVAL",
    "EXPR_TOKEN",
    "ExtendedErrorParamTypes",
    "ExtendedErrorParamTypes_eeptAnsiString",
    "ExtendedErrorParamTypes_eeptBinary",
    "ExtendedErrorParamTypes_eeptLongVal",
    "ExtendedErrorParamTypes_eeptNone",
    "ExtendedErrorParamTypes_eeptPointerVal",
    "ExtendedErrorParamTypes_eeptShortVal",
    "ExtendedErrorParamTypes_eeptUnicodeString",
    "FC_EXPR_CONST32",
    "FC_EXPR_CONST64",
    "FC_EXPR_END",
    "FC_EXPR_ILLEGAL",
    "FC_EXPR_NOOP",
    "FC_EXPR_OPER",
    "FC_EXPR_START",
    "FC_EXPR_VAR",
    "FULL_PTR_XLAT_TABLES",
    "GENERIC_BINDING_INFO",
    "GENERIC_BINDING_ROUTINE",
    "GENERIC_BINDING_ROUTINE_PAIR",
    "GENERIC_UNBIND_ROUTINE",
    "GROUP_NAME_SYNTAX",
    "IDL_CS_CONVERT",
    "IDL_CS_IN_PLACE_CONVERT",
    "IDL_CS_NEW_BUFFER_CONVERT",
    "IDL_CS_NO_CONVERT",
    "INVALID_FRAGMENT_ID",
    "IUnknown_AddRef_Proxy",
    "IUnknown_QueryInterface_Proxy",
    "IUnknown_Release_Proxy",
    "I_RpcAllocate",
    "I_RpcAsyncAbortCall",
    "I_RpcAsyncSetHandle",
    "I_RpcBindingCopy",
    "I_RpcBindingCreateNP",
    "I_RpcBindingHandleToAsyncHandle",
    "I_RpcBindingInqClientTokenAttributes",
    "I_RpcBindingInqDynamicEndpointA",
    "I_RpcBindingInqDynamicEndpointW",
    "I_RpcBindingInqLocalClientPID",
    "I_RpcBindingInqMarshalledTargetInfo",
    "I_RpcBindingInqSecurityContext",
    "I_RpcBindingInqSecurityContextKeyInfo",
    "I_RpcBindingInqTransportType",
    "I_RpcBindingInqWireIdForSnego",
    "I_RpcBindingIsClientLocal",
    "I_RpcBindingIsServerLocal",
    "I_RpcBindingSetPrivateOption",
    "I_RpcBindingToStaticStringBindingW",
    "I_RpcClearMutex",
    "I_RpcDeleteMutex",
    "I_RpcExceptionFilter",
    "I_RpcFree",
    "I_RpcFreeBuffer",
    "I_RpcFreeCalloutStateFn",
    "I_RpcFreePipeBuffer",
    "I_RpcGetBuffer",
    "I_RpcGetBufferWithObject",
    "I_RpcGetCurrentCallHandle",
    "I_RpcGetDefaultSD",
    "I_RpcGetExtendedError",
    "I_RpcIfInqTransferSyntaxes",
    "I_RpcMapWin32Status",
    "I_RpcMgmtEnableDedicatedThreadPool",
    "I_RpcNegotiateTransferSyntax",
    "I_RpcNsBindingSetEntryNameA",
    "I_RpcNsBindingSetEntryNameW",
    "I_RpcNsGetBuffer",
    "I_RpcNsInterfaceExported",
    "I_RpcNsInterfaceUnexported",
    "I_RpcNsRaiseException",
    "I_RpcNsSendReceive",
    "I_RpcOpenClientProcess",
    "I_RpcPauseExecution",
    "I_RpcPerformCalloutFn",
    "I_RpcProxyCallbackInterface",
    "I_RpcProxyFilterIfFn",
    "I_RpcProxyGetClientAddressFn",
    "I_RpcProxyGetClientSessionAndResourceUUID",
    "I_RpcProxyGetConnectionTimeoutFn",
    "I_RpcProxyIsValidMachineFn",
    "I_RpcProxyUpdatePerfCounterBackendServerFn",
    "I_RpcProxyUpdatePerfCounterFn",
    "I_RpcReBindBuffer",
    "I_RpcReallocPipeBuffer",
    "I_RpcReceive",
    "I_RpcRecordCalloutFailure",
    "I_RpcRequestMutex",
    "I_RpcSend",
    "I_RpcSendReceive",
    "I_RpcServerCheckClientRestriction",
    "I_RpcServerDisableExceptionFilter",
    "I_RpcServerGetAssociationID",
    "I_RpcServerInqAddressChangeFn",
    "I_RpcServerInqLocalConnAddress",
    "I_RpcServerInqRemoteConnAddress",
    "I_RpcServerInqTransportType",
    "I_RpcServerRegisterForwardFunction",
    "I_RpcServerSetAddressChangeFn",
    "I_RpcServerStartService",
    "I_RpcServerSubscribeForDisconnectNotification",
    "I_RpcServerSubscribeForDisconnectNotification2",
    "I_RpcServerUnsubscribeForDisconnectNotification",
    "I_RpcServerUseProtseq2A",
    "I_RpcServerUseProtseq2W",
    "I_RpcServerUseProtseqEp2A",
    "I_RpcServerUseProtseqEp2W",
    "I_RpcSessionStrictContextHandle",
    "I_RpcSsDontSerializeContext",
    "I_RpcSystemHandleTypeSpecificWork",
    "I_RpcTurnOnEEInfoPropagation",
    "I_UuidCreate",
    "LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION",
    "LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION_MarshalDirectionMarshal",
    "LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION_MarshalDirectionUnmarshal",
    "MALLOC_FREE_STRUCT",
    "MES_DECODE",
    "MES_DYNAMIC_BUFFER_HANDLE",
    "MES_ENCODE",
    "MES_ENCODE_NDR64",
    "MES_FIXED_BUFFER_HANDLE",
    "MES_INCREMENTAL_HANDLE",
    "MIDL_ES_ALLOC",
    "MIDL_ES_CODE",
    "MIDL_ES_HANDLE_STYLE",
    "MIDL_ES_READ",
    "MIDL_ES_WRITE",
    "MIDL_FORMAT_STRING",
    "MIDL_INTERCEPTION_INFO",
    "MIDL_INTERFACE_METHOD_PROPERTIES",
    "MIDL_METHOD_PROPERTY",
    "MIDL_METHOD_PROPERTY_MAP",
    "MIDL_SERVER_INFO",
    "MIDL_STUBLESS_PROXY_INFO",
    "MIDL_STUB_DESC",
    "MIDL_STUB_MESSAGE",
    "MIDL_SYNTAX_INFO",
    "MIDL_TYPE_PICKLING_INFO",
    "MIDL_WINRT_TYPE_SERIALIZATION_INFO",
    "MIDL_WINRT_TYPE_SERIALIZATION_INFO_CURRENT_VERSION",
    "MaxNumberOfEEInfoParams",
    "MesBufferHandleReset",
    "MesDecodeBufferHandleCreate",
    "MesDecodeIncrementalHandleCreate",
    "MesEncodeDynBufferHandleCreate",
    "MesEncodeFixedBufferHandleCreate",
    "MesEncodeIncrementalHandleCreate",
    "MesHandleFree",
    "MesIncrementalHandleReset",
    "MesInqProcEncodingId",
    "MidlInterceptionInfoVersionOne",
    "MidlWinrtTypeSerializationInfoVersionOne",
    "NDR64_ARRAY_ELEMENT_INFO",
    "NDR64_ARRAY_FLAGS",
    "NDR64_BINDINGS",
    "NDR64_BIND_AND_NOTIFY_EXTENSION",
    "NDR64_BIND_CONTEXT",
    "NDR64_BIND_GENERIC",
    "NDR64_BIND_PRIMITIVE",
    "NDR64_BOGUS_ARRAY_HEADER_FORMAT",
    "NDR64_BOGUS_STRUCTURE_HEADER_FORMAT",
    "NDR64_BUFFER_ALIGN_FORMAT",
    "NDR64_CONFORMANT_STRING_FORMAT",
    "NDR64_CONF_ARRAY_HEADER_FORMAT",
    "NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT",
    "NDR64_CONF_STRUCTURE_HEADER_FORMAT",
    "NDR64_CONF_VAR_ARRAY_HEADER_FORMAT",
    "NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT",
    "NDR64_CONSTANT_IID_FORMAT",
    "NDR64_CONTEXT_HANDLE_FLAGS",
    "NDR64_CONTEXT_HANDLE_FORMAT",
    "NDR64_EMBEDDED_COMPLEX_FORMAT",
    "NDR64_ENCAPSULATED_UNION",
    "NDR64_EXPR_CONST32",
    "NDR64_EXPR_CONST64",
    "NDR64_EXPR_NOOP",
    "NDR64_EXPR_OPERATOR",
    "NDR64_EXPR_VAR",
    "NDR64_FC_AUTO_HANDLE",
    "NDR64_FC_BIND_GENERIC",
    "NDR64_FC_BIND_PRIMITIVE",
    "NDR64_FC_CALLBACK_HANDLE",
    "NDR64_FC_EXPLICIT_HANDLE",
    "NDR64_FC_NO_HANDLE",
    "NDR64_FIXED_REPEAT_FORMAT",
    "NDR64_FIX_ARRAY_HEADER_FORMAT",
    "NDR64_IID_FLAGS",
    "NDR64_IID_FORMAT",
    "NDR64_MEMPAD_FORMAT",
    "NDR64_NON_CONFORMANT_STRING_FORMAT",
    "NDR64_NON_ENCAPSULATED_UNION",
    "NDR64_NO_REPEAT_FORMAT",
    "NDR64_PARAM_FLAGS",
    "NDR64_PARAM_FORMAT",
    "NDR64_PIPE_FLAGS",
    "NDR64_PIPE_FORMAT",
    "NDR64_POINTER_FORMAT",
    "NDR64_POINTER_INSTANCE_HEADER_FORMAT",
    "NDR64_POINTER_REPEAT_FLAGS",
    "NDR64_PROC_FLAGS",
    "NDR64_PROC_FORMAT",
    "NDR64_RANGED_STRING_FORMAT",
    "NDR64_RANGE_FORMAT",
    "NDR64_RANGE_PIPE_FORMAT",
    "NDR64_REPEAT_FORMAT",
    "NDR64_RPC_FLAGS",
    "NDR64_SIMPLE_MEMBER_FORMAT",
    "NDR64_SIMPLE_REGION_FORMAT",
    "NDR64_SIZED_CONFORMANT_STRING_FORMAT",
    "NDR64_STRING_FLAGS",
    "NDR64_STRING_HEADER_FORMAT",
    "NDR64_STRUCTURE_FLAGS",
    "NDR64_STRUCTURE_HEADER_FORMAT",
    "NDR64_SYSTEM_HANDLE_FORMAT",
    "NDR64_TRANSMIT_AS_FLAGS",
    "NDR64_TRANSMIT_AS_FORMAT",
    "NDR64_TYPE_STRICT_CONTEXT_HANDLE",
    "NDR64_UNION_ARM",
    "NDR64_UNION_ARM_SELECTOR",
    "NDR64_USER_MARSHAL_FLAGS",
    "NDR64_USER_MARSHAL_FORMAT",
    "NDR64_VAR_ARRAY_HEADER_FORMAT",
    "NDRCContextBinding",
    "NDRCContextMarshall",
    "NDRCContextUnmarshall",
    "NDRSContextMarshall",
    "NDRSContextMarshall2",
    "NDRSContextMarshallEx",
    "NDRSContextUnmarshall",
    "NDRSContextUnmarshall2",
    "NDRSContextUnmarshallEx",
    "NDR_ALLOC_ALL_NODES_CONTEXT",
    "NDR_CS_ROUTINES",
    "NDR_CS_SIZE_CONVERT_ROUTINES",
    "NDR_CUSTOM_OR_DEFAULT_ALLOCATOR",
    "NDR_DEFAULT_ALLOCATOR",
    "NDR_EXPR_DESC",
    "NDR_NOTIFY2_ROUTINE",
    "NDR_NOTIFY_ROUTINE",
    "NDR_POINTER_QUEUE_STATE",
    "NDR_RUNDOWN",
    "NDR_SCONTEXT_1",
    "NDR_USER_MARSHAL_INFO",
    "NDR_USER_MARSHAL_INFO_LEVEL1",
    "NT351_INTERFACE_SIZE",
    "Ndr64AsyncClientCall",
    "Ndr64AsyncServerCall64",
    "Ndr64AsyncServerCallAll",
    "Ndr64DcomAsyncClientCall",
    "Ndr64DcomAsyncStubCall",
    "NdrAllocate",
    "NdrAsyncClientCall",
    "NdrAsyncServerCall",
    "NdrByteCountPointerBufferSize",
    "NdrByteCountPointerFree",
    "NdrByteCountPointerMarshall",
    "NdrByteCountPointerUnmarshall",
    "NdrClearOutParameters",
    "NdrClientCall2",
    "NdrClientCall3",
    "NdrClientContextMarshall",
    "NdrClientContextUnmarshall",
    "NdrClientInitialize",
    "NdrClientInitializeNew",
    "NdrComplexArrayBufferSize",
    "NdrComplexArrayFree",
    "NdrComplexArrayMarshall",
    "NdrComplexArrayMemorySize",
    "NdrComplexArrayUnmarshall",
    "NdrComplexStructBufferSize",
    "NdrComplexStructFree",
    "NdrComplexStructMarshall",
    "NdrComplexStructMemorySize",
    "NdrComplexStructUnmarshall",
    "NdrConformantArrayBufferSize",
    "NdrConformantArrayFree",
    "NdrConformantArrayMarshall",
    "NdrConformantArrayMemorySize",
    "NdrConformantArrayUnmarshall",
    "NdrConformantStringBufferSize",
    "NdrConformantStringMarshall",
    "NdrConformantStringMemorySize",
    "NdrConformantStringUnmarshall",
    "NdrConformantStructBufferSize",
    "NdrConformantStructFree",
    "NdrConformantStructMarshall",
    "NdrConformantStructMemorySize",
    "NdrConformantStructUnmarshall",
    "NdrConformantVaryingArrayBufferSize",
    "NdrConformantVaryingArrayFree",
    "NdrConformantVaryingArrayMarshall",
    "NdrConformantVaryingArrayMemorySize",
    "NdrConformantVaryingArrayUnmarshall",
    "NdrConformantVaryingStructBufferSize",
    "NdrConformantVaryingStructFree",
    "NdrConformantVaryingStructMarshall",
    "NdrConformantVaryingStructMemorySize",
    "NdrConformantVaryingStructUnmarshall",
    "NdrContextHandleInitialize",
    "NdrContextHandleSize",
    "NdrConvert",
    "NdrConvert2",
    "NdrCorrelationFree",
    "NdrCorrelationInitialize",
    "NdrCorrelationPass",
    "NdrCreateServerInterfaceFromStub",
    "NdrDcomAsyncClientCall",
    "NdrDcomAsyncStubCall",
    "NdrEncapsulatedUnionBufferSize",
    "NdrEncapsulatedUnionFree",
    "NdrEncapsulatedUnionMarshall",
    "NdrEncapsulatedUnionMemorySize",
    "NdrEncapsulatedUnionUnmarshall",
    "NdrFixedArrayBufferSize",
    "NdrFixedArrayFree",
    "NdrFixedArrayMarshall",
    "NdrFixedArrayMemorySize",
    "NdrFixedArrayUnmarshall",
    "NdrFreeBuffer",
    "NdrFullPointerXlatFree",
    "NdrFullPointerXlatInit",
    "NdrGetBuffer",
    "NdrGetDcomProtocolVersion",
    "NdrGetUserMarshalInfo",
    "NdrInterfacePointerBufferSize",
    "NdrInterfacePointerFree",
    "NdrInterfacePointerMarshall",
    "NdrInterfacePointerMemorySize",
    "NdrInterfacePointerUnmarshall",
    "NdrMapCommAndFaultStatus",
    "NdrMesProcEncodeDecode",
    "NdrMesProcEncodeDecode2",
    "NdrMesProcEncodeDecode3",
    "NdrMesSimpleTypeAlignSize",
    "NdrMesSimpleTypeAlignSizeAll",
    "NdrMesSimpleTypeDecode",
    "NdrMesSimpleTypeDecodeAll",
    "NdrMesSimpleTypeEncode",
    "NdrMesSimpleTypeEncodeAll",
    "NdrMesTypeAlignSize",
    "NdrMesTypeAlignSize2",
    "NdrMesTypeAlignSize3",
    "NdrMesTypeDecode",
    "NdrMesTypeDecode2",
    "NdrMesTypeDecode3",
    "NdrMesTypeEncode",
    "NdrMesTypeEncode2",
    "NdrMesTypeEncode3",
    "NdrMesTypeFree2",
    "NdrMesTypeFree3",
    "NdrNonConformantStringBufferSize",
    "NdrNonConformantStringMarshall",
    "NdrNonConformantStringMemorySize",
    "NdrNonConformantStringUnmarshall",
    "NdrNonEncapsulatedUnionBufferSize",
    "NdrNonEncapsulatedUnionFree",
    "NdrNonEncapsulatedUnionMarshall",
    "NdrNonEncapsulatedUnionMemorySize",
    "NdrNonEncapsulatedUnionUnmarshall",
    "NdrNsGetBuffer",
    "NdrNsSendReceive",
    "NdrOleAllocate",
    "NdrOleFree",
    "NdrPartialIgnoreClientBufferSize",
    "NdrPartialIgnoreClientMarshall",
    "NdrPartialIgnoreServerInitialize",
    "NdrPartialIgnoreServerUnmarshall",
    "NdrPointerBufferSize",
    "NdrPointerFree",
    "NdrPointerMarshall",
    "NdrPointerMemorySize",
    "NdrPointerUnmarshall",
    "NdrRangeUnmarshall",
    "NdrRpcSmClientAllocate",
    "NdrRpcSmClientFree",
    "NdrRpcSmSetClientToOsf",
    "NdrRpcSsDefaultAllocate",
    "NdrRpcSsDefaultFree",
    "NdrRpcSsDisableAllocate",
    "NdrRpcSsEnableAllocate",
    "NdrSendReceive",
    "NdrServerCall2",
    "NdrServerCallAll",
    "NdrServerCallNdr64",
    "NdrServerContextMarshall",
    "NdrServerContextNewMarshall",
    "NdrServerContextNewUnmarshall",
    "NdrServerContextUnmarshall",
    "NdrServerInitialize",
    "NdrServerInitializeMarshall",
    "NdrServerInitializeNew",
    "NdrServerInitializePartial",
    "NdrServerInitializeUnmarshall",
    "NdrSimpleStructBufferSize",
    "NdrSimpleStructFree",
    "NdrSimpleStructMarshall",
    "NdrSimpleStructMemorySize",
    "NdrSimpleStructUnmarshall",
    "NdrSimpleTypeMarshall",
    "NdrSimpleTypeUnmarshall",
    "NdrStubCall2",
    "NdrStubCall3",
    "NdrUserMarshalBufferSize",
    "NdrUserMarshalFree",
    "NdrUserMarshalMarshall",
    "NdrUserMarshalMemorySize",
    "NdrUserMarshalSimpleTypeConvert",
    "NdrUserMarshalUnmarshall",
    "NdrVaryingArrayBufferSize",
    "NdrVaryingArrayFree",
    "NdrVaryingArrayMarshall",
    "NdrVaryingArrayMemorySize",
    "NdrVaryingArrayUnmarshall",
    "NdrXmitOrRepAsBufferSize",
    "NdrXmitOrRepAsFree",
    "NdrXmitOrRepAsMarshall",
    "NdrXmitOrRepAsMemorySize",
    "NdrXmitOrRepAsUnmarshall",
    "PFN_RPCNOTIFICATION_ROUTINE",
    "PROTOCOL_ADDRESS_CHANGE",
    "PROTOCOL_LOADED",
    "PROTOCOL_NOT_LOADED",
    "PROXY_CALCSIZE",
    "PROXY_GETBUFFER",
    "PROXY_MARSHAL",
    "PROXY_PHASE",
    "PROXY_SENDRECEIVE",
    "PROXY_UNMARSHAL",
    "PRPC_RUNDOWN",
    "RDR_CALLOUT_STATE",
    "RPCFLG_ACCESSIBILITY_BIT1",
    "RPCFLG_ACCESSIBILITY_BIT2",
    "RPCFLG_ACCESS_LOCAL",
    "RPCFLG_ASYNCHRONOUS",
    "RPCFLG_AUTO_COMPLETE",
    "RPCFLG_HAS_CALLBACK",
    "RPCFLG_HAS_GUARANTEE",
    "RPCFLG_HAS_MULTI_SYNTAXES",
    "RPCFLG_INPUT_SYNCHRONOUS",
    "RPCFLG_LOCAL_CALL",
    "RPCFLG_MESSAGE",
    "RPCFLG_NDR64_CONTAINS_ARM_LAYOUT",
    "RPCFLG_NON_NDR",
    "RPCFLG_SENDER_WAITING_FOR_REPLY",
    "RPCFLG_WINRT_REMOTE_ASYNC",
    "RPCHTTP_RS_ACCESS_1",
    "RPCHTTP_RS_ACCESS_2",
    "RPCHTTP_RS_INTERFACE",
    "RPCHTTP_RS_REDIRECT",
    "RPCHTTP_RS_SESSION",
    "RPCLT_PDU_FILTER_FUNC",
    "RPC_ADDRESS_CHANGE_FN",
    "RPC_ADDRESS_CHANGE_TYPE",
    "RPC_ASYNC_EVENT",
    "RPC_ASYNC_EVENT_RpcCallComplete",
    "RPC_ASYNC_EVENT_RpcClientCancel",
    "RPC_ASYNC_EVENT_RpcClientDisconnect",
    "RPC_ASYNC_EVENT_RpcReceiveComplete",
    "RPC_ASYNC_EVENT_RpcSendComplete",
    "RPC_ASYNC_NOTIFICATION_INFO",
    "RPC_ASYNC_STATE",
    "RPC_AUTH_KEY_RETRIEVAL_FN",
    "RPC_BHO_DONTLINGER",
    "RPC_BHO_EXCLUSIVE_AND_GUARANTEED",
    "RPC_BHO_NONCAUSAL",
    "RPC_BHT_OBJECT_UUID_VALID",
    "RPC_BINDING_HANDLE_OPTIONS_FLAGS",
    "RPC_BINDING_HANDLE_OPTIONS_V1",
    "RPC_BINDING_HANDLE_SECURITY_V1_A",
    "RPC_BINDING_HANDLE_SECURITY_V1_W",
    "RPC_BINDING_HANDLE_TEMPLATE_V1_A",
    "RPC_BINDING_HANDLE_TEMPLATE_V1_W",
    "RPC_BINDING_VECTOR",
    "RPC_BLOCKING_FN",
    "RPC_BUFFER_ASYNC",
    "RPC_BUFFER_COMPLETE",
    "RPC_BUFFER_EXTRA",
    "RPC_BUFFER_NONOTIFY",
    "RPC_BUFFER_PARTIAL",
    "RPC_CALL_ATTRIBUTES_V1_A",
    "RPC_CALL_ATTRIBUTES_V1_W",
    "RPC_CALL_ATTRIBUTES_V2_A",
    "RPC_CALL_ATTRIBUTES_V2_W",
    "RPC_CALL_ATTRIBUTES_V3_A",
    "RPC_CALL_ATTRIBUTES_V3_W",
    "RPC_CALL_ATTRIBUTES_VERSION",
    "RPC_CALL_LOCAL_ADDRESS_V1",
    "RPC_CALL_STATUS_CANCELLED",
    "RPC_CALL_STATUS_DISCONNECTED",
    "RPC_CLIENT_ALLOC",
    "RPC_CLIENT_FREE",
    "RPC_CLIENT_INFORMATION1",
    "RPC_CLIENT_INTERFACE",
    "RPC_CONTEXT_HANDLE_DEFAULT_FLAGS",
    "RPC_CONTEXT_HANDLE_DONT_SERIALIZE",
    "RPC_CONTEXT_HANDLE_FLAGS",
    "RPC_CONTEXT_HANDLE_SERIALIZE",
    "RPC_C_AUTHN_CLOUD_AP",
    "RPC_C_AUTHN_DCE_PRIVATE",
    "RPC_C_AUTHN_DCE_PUBLIC",
    "RPC_C_AUTHN_DEC_PUBLIC",
    "RPC_C_AUTHN_DEFAULT",
    "RPC_C_AUTHN_DIGEST",
    "RPC_C_AUTHN_DPA",
    "RPC_C_AUTHN_GSS_KERBEROS",
    "RPC_C_AUTHN_GSS_NEGOTIATE",
    "RPC_C_AUTHN_GSS_SCHANNEL",
    "RPC_C_AUTHN_INFO_NONE",
    "RPC_C_AUTHN_INFO_TYPE",
    "RPC_C_AUTHN_INFO_TYPE_HTTP",
    "RPC_C_AUTHN_KERNEL",
    "RPC_C_AUTHN_LIVEXP_SSP",
    "RPC_C_AUTHN_LIVE_SSP",
    "RPC_C_AUTHN_MQ",
    "RPC_C_AUTHN_MSN",
    "RPC_C_AUTHN_MSONLINE",
    "RPC_C_AUTHN_NEGO_EXTENDER",
    "RPC_C_AUTHN_NONE",
    "RPC_C_AUTHN_PKU2U",
    "RPC_C_AUTHN_WINNT",
    "RPC_C_AUTHZ_DCE",
    "RPC_C_AUTHZ_DEFAULT",
    "RPC_C_AUTHZ_NAME",
    "RPC_C_AUTHZ_NONE",
    "RPC_C_BINDING_DEFAULT_TIMEOUT",
    "RPC_C_BINDING_INFINITE_TIMEOUT",
    "RPC_C_BINDING_MAX_TIMEOUT",
    "RPC_C_BINDING_MIN_TIMEOUT",
    "RPC_C_BIND_TO_ALL_NICS",
    "RPC_C_CANCEL_INFINITE_TIMEOUT",
    "RPC_C_DONT_FAIL",
    "RPC_C_EP_ALL_ELTS",
    "RPC_C_EP_MATCH_BY_BOTH",
    "RPC_C_EP_MATCH_BY_IF",
    "RPC_C_EP_MATCH_BY_OBJ",
    "RPC_C_FULL_CERT_CHAIN",
    "RPC_C_HTTP_AUTHN_SCHEME_BASIC",
    "RPC_C_HTTP_AUTHN_SCHEME_CERT",
    "RPC_C_HTTP_AUTHN_SCHEME_DIGEST",
    "RPC_C_HTTP_AUTHN_SCHEME_NEGOTIATE",
    "RPC_C_HTTP_AUTHN_SCHEME_NTLM",
    "RPC_C_HTTP_AUTHN_SCHEME_PASSPORT",
    "RPC_C_HTTP_AUTHN_TARGET",
    "RPC_C_HTTP_AUTHN_TARGET_PROXY",
    "RPC_C_HTTP_AUTHN_TARGET_SERVER",
    "RPC_C_HTTP_FLAGS",
    "RPC_C_HTTP_FLAG_ENABLE_CERT_REVOCATION_CHECK",
    "RPC_C_HTTP_FLAG_IGNORE_CERT_CN_INVALID",
    "RPC_C_HTTP_FLAG_USE_FIRST_AUTH_SCHEME",
    "RPC_C_HTTP_FLAG_USE_SSL",
    "RPC_C_LISTEN_MAX_CALLS_DEFAULT",
    "RPC_C_MGMT_INQ_IF_IDS",
    "RPC_C_MGMT_INQ_PRINC_NAME",
    "RPC_C_MGMT_INQ_STATS",
    "RPC_C_MGMT_IS_SERVER_LISTEN",
    "RPC_C_MGMT_STOP_SERVER_LISTEN",
    "RPC_C_MQ_AUTHN_LEVEL_NONE",
    "RPC_C_MQ_AUTHN_LEVEL_PKT_INTEGRITY",
    "RPC_C_MQ_AUTHN_LEVEL_PKT_PRIVACY",
    "RPC_C_MQ_CLEAR_ON_OPEN",
    "RPC_C_MQ_EXPRESS",
    "RPC_C_MQ_JOURNAL_ALWAYS",
    "RPC_C_MQ_JOURNAL_DEADLETTER",
    "RPC_C_MQ_JOURNAL_NONE",
    "RPC_C_MQ_PERMANENT",
    "RPC_C_MQ_RECOVERABLE",
    "RPC_C_MQ_TEMPORARY",
    "RPC_C_MQ_USE_EXISTING_SECURITY",
    "RPC_C_NOTIFY_ON_SEND_COMPLETE",
    "RPC_C_NS_DEFAULT_EXP_AGE",
    "RPC_C_NS_SYNTAX_DCE",
    "RPC_C_NS_SYNTAX_DEFAULT",
    "RPC_C_OPT_ASYNC_BLOCK",
    "RPC_C_OPT_BINDING_NONCAUSAL",
    "RPC_C_OPT_CALL_TIMEOUT",
    "RPC_C_OPT_COOKIE_AUTH",
    "RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR",
    "RPC_C_OPT_DONT_LINGER",
    "RPC_C_OPT_MAX_OPTIONS",
    "RPC_C_OPT_MQ_ACKNOWLEDGE",
    "RPC_C_OPT_MQ_AUTHN_LEVEL",
    "RPC_C_OPT_MQ_AUTHN_SERVICE",
    "RPC_C_OPT_MQ_DELIVERY",
    "RPC_C_OPT_MQ_JOURNAL",
    "RPC_C_OPT_MQ_PRIORITY",
    "RPC_C_OPT_MQ_TIME_TO_BE_RECEIVED",
    "RPC_C_OPT_MQ_TIME_TO_REACH_QUEUE",
    "RPC_C_OPT_OPTIMIZE_TIME",
    "RPC_C_OPT_PRIVATE_BREAK_ON_SUSPEND",
    "RPC_C_OPT_PRIVATE_DO_NOT_DISTURB",
    "RPC_C_OPT_PRIVATE_SUPPRESS_WAKE",
    "RPC_C_OPT_RESOURCE_TYPE_UUID",
    "RPC_C_OPT_SECURITY_CALLBACK",
    "RPC_C_OPT_SESSION_ID",
    "RPC_C_OPT_TRANS_SEND_BUFFER_SIZE",
    "RPC_C_OPT_TRUST_PEER",
    "RPC_C_OPT_UNIQUE_BINDING",
    "RPC_C_PARM_BUFFER_LENGTH",
    "RPC_C_PARM_MAX_PACKET_LENGTH",
    "RPC_C_PROFILE_ALL_ELT",
    "RPC_C_PROFILE_ALL_ELTS",
    "RPC_C_PROFILE_DEFAULT_ELT",
    "RPC_C_PROFILE_MATCH_BY_BOTH",
    "RPC_C_PROFILE_MATCH_BY_IF",
    "RPC_C_PROFILE_MATCH_BY_MBR",
    "RPC_C_PROTSEQ_MAX_REQS_DEFAULT",
    "RPC_C_QOS_CAPABILITIES",
    "RPC_C_QOS_CAPABILITIES_ANY_AUTHORITY",
    "RPC_C_QOS_CAPABILITIES_DEFAULT",
    "RPC_C_QOS_CAPABILITIES_IGNORE_DELEGATE_FAILURE",
    "RPC_C_QOS_CAPABILITIES_LOCAL_MA_HINT",
    "RPC_C_QOS_CAPABILITIES_MAKE_FULLSIC",
    "RPC_C_QOS_CAPABILITIES_MUTUAL_AUTH",
    "RPC_C_QOS_CAPABILITIES_SCHANNEL_FULL_AUTH_IDENTITY",
    "RPC_C_QOS_IDENTITY",
    "RPC_C_QOS_IDENTITY_DYNAMIC",
    "RPC_C_QOS_IDENTITY_STATIC",
    "RPC_C_RPCHTTP_USE_LOAD_BALANCE",
    "RPC_C_SECURITY_QOS_VERSION",
    "RPC_C_SECURITY_QOS_VERSION_1",
    "RPC_C_SECURITY_QOS_VERSION_2",
    "RPC_C_SECURITY_QOS_VERSION_3",
    "RPC_C_SECURITY_QOS_VERSION_4",
    "RPC_C_SECURITY_QOS_VERSION_5",
    "RPC_C_STATS_CALLS_IN",
    "RPC_C_STATS_CALLS_OUT",
    "RPC_C_STATS_PKTS_IN",
    "RPC_C_STATS_PKTS_OUT",
    "RPC_C_TRY_ENFORCE_MAX_CALLS",
    "RPC_C_USE_INTERNET_PORT",
    "RPC_C_USE_INTRANET_PORT",
    "RPC_C_VERS_ALL",
    "RPC_C_VERS_COMPATIBLE",
    "RPC_C_VERS_EXACT",
    "RPC_C_VERS_MAJOR_ONLY",
    "RPC_C_VERS_UPTO",
    "RPC_DISPATCH_FUNCTION",
    "RPC_DISPATCH_TABLE",
    "RPC_EEINFO_VERSION",
    "RPC_EE_INFO_PARAM",
    "RPC_ENDPOINT_TEMPLATEA",
    "RPC_ENDPOINT_TEMPLATEW",
    "RPC_ERROR_ENUM_HANDLE",
    "RPC_EXTENDED_ERROR_INFO",
    "RPC_FLAGS_VALID_BIT",
    "RPC_FORWARD_FUNCTION",
    "RPC_FW_IF_FLAG_DCOM",
    "RPC_HTTP_PROXY_FREE_STRING",
    "RPC_HTTP_REDIRECTOR_STAGE",
    "RPC_HTTP_TRANSPORT_CREDENTIALS_A",
    "RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A",
    "RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W",
    "RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A",
    "RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W",
    "RPC_HTTP_TRANSPORT_CREDENTIALS_W",
    "RPC_IF_ALLOW_CALLBACKS_WITH_NO_AUTH",
    "RPC_IF_ALLOW_LOCAL_ONLY",
    "RPC_IF_ALLOW_SECURE_ONLY",
    "RPC_IF_ALLOW_UNKNOWN_AUTHORITY",
    "RPC_IF_ASYNC_CALLBACK",
    "RPC_IF_AUTOLISTEN",
    "RPC_IF_CALLBACK_FN",
    "RPC_IF_ID",
    "RPC_IF_ID_VECTOR",
    "RPC_IF_OLE",
    "RPC_IF_SEC_CACHE_PER_PROC",
    "RPC_IF_SEC_NO_CACHE",
    "RPC_IMPORT_CONTEXT_P",
    "RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN",
    "RPC_INTERFACE_HAS_PIPES",
    "RPC_INTERFACE_TEMPLATEA",
    "RPC_INTERFACE_TEMPLATEW",
    "RPC_MESSAGE",
    "RPC_MGMT_AUTHORIZATION_FN",
    "RPC_NCA_FLAGS_BROADCAST",
    "RPC_NCA_FLAGS_DEFAULT",
    "RPC_NCA_FLAGS_IDEMPOTENT",
    "RPC_NCA_FLAGS_MAYBE",
    "RPC_NEW_HTTP_PROXY_CHANNEL",
    "RPC_NOTIFICATIONS",
    "RPC_NOTIFICATIONS_RpcNotificationCallCancel",
    "RPC_NOTIFICATIONS_RpcNotificationCallNone",
    "RPC_NOTIFICATIONS_RpcNotificationClientDisconnect",
    "RPC_NOTIFICATION_TYPES",
    "RPC_NOTIFICATION_TYPES_RpcNotificationTypeApc",
    "RPC_NOTIFICATION_TYPES_RpcNotificationTypeCallback",
    "RPC_NOTIFICATION_TYPES_RpcNotificationTypeEvent",
    "RPC_NOTIFICATION_TYPES_RpcNotificationTypeHwnd",
    "RPC_NOTIFICATION_TYPES_RpcNotificationTypeIoc",
    "RPC_NOTIFICATION_TYPES_RpcNotificationTypeNone",
    "RPC_OBJECT_INQ_FN",
    "RPC_POLICY",
    "RPC_PROTSEQ_ENDPOINT",
    "RPC_PROTSEQ_HTTP",
    "RPC_PROTSEQ_LRPC",
    "RPC_PROTSEQ_NMP",
    "RPC_PROTSEQ_TCP",
    "RPC_PROTSEQ_VECTORA",
    "RPC_PROTSEQ_VECTORW",
    "RPC_PROXY_CONNECTION_TYPE_IN_PROXY",
    "RPC_PROXY_CONNECTION_TYPE_OUT_PROXY",
    "RPC_P_ADDR_FORMAT_TCP_IPV4",
    "RPC_P_ADDR_FORMAT_TCP_IPV6",
    "RPC_QUERY_CALL_LOCAL_ADDRESS",
    "RPC_QUERY_CLIENT_ID",
    "RPC_QUERY_CLIENT_PID",
    "RPC_QUERY_CLIENT_PRINCIPAL_NAME",
    "RPC_QUERY_IS_CLIENT_LOCAL",
    "RPC_QUERY_NO_AUTH_REQUIRED",
    "RPC_QUERY_SERVER_PRINCIPAL_NAME",
    "RPC_SECURITY_CALLBACK_FN",
    "RPC_SECURITY_QOS",
    "RPC_SECURITY_QOS_V2_A",
    "RPC_SECURITY_QOS_V2_W",
    "RPC_SECURITY_QOS_V3_A",
    "RPC_SECURITY_QOS_V3_W",
    "RPC_SECURITY_QOS_V4_A",
    "RPC_SECURITY_QOS_V4_W",
    "RPC_SECURITY_QOS_V5_A",
    "RPC_SECURITY_QOS_V5_W",
    "RPC_SEC_CONTEXT_KEY_INFO",
    "RPC_SERVER_INTERFACE",
    "RPC_SETFILTER_FUNC",
    "RPC_STATS_VECTOR",
    "RPC_STATUS",
    "RPC_SYNTAX_IDENTIFIER",
    "RPC_SYSTEM_HANDLE_FREE_ALL",
    "RPC_SYSTEM_HANDLE_FREE_ERROR_ON_CLOSE",
    "RPC_SYSTEM_HANDLE_FREE_RETRIEVED",
    "RPC_SYSTEM_HANDLE_FREE_UNRETRIEVED",
    "RPC_S_ADDRESS_ERROR",
    "RPC_S_ALREADY_LISTENING",
    "RPC_S_ALREADY_REGISTERED",
    "RPC_S_BINDING_HAS_NO_AUTH",
    "RPC_S_BINDING_INCOMPLETE",
    "RPC_S_CALL_CANCELLED",
    "RPC_S_CALL_FAILED",
    "RPC_S_CALL_FAILED_DNE",
    "RPC_S_CALL_IN_PROGRESS",
    "RPC_S_CANNOT_SUPPORT",
    "RPC_S_CANT_CREATE_ENDPOINT",
    "RPC_S_COMM_FAILURE",
    "RPC_S_COOKIE_AUTH_FAILED",
    "RPC_S_DO_NOT_DISTURB",
    "RPC_S_DUPLICATE_ENDPOINT",
    "RPC_S_ENTRY_ALREADY_EXISTS",
    "RPC_S_ENTRY_NOT_FOUND",
    "RPC_S_ENTRY_TYPE_MISMATCH",
    "RPC_S_FP_DIV_ZERO",
    "RPC_S_FP_OVERFLOW",
    "RPC_S_FP_UNDERFLOW",
    "RPC_S_GROUP_MEMBER_NOT_FOUND",
    "RPC_S_GRP_ELT_NOT_ADDED",
    "RPC_S_GRP_ELT_NOT_REMOVED",
    "RPC_S_INCOMPLETE_NAME",
    "RPC_S_INTERFACE_NOT_EXPORTED",
    "RPC_S_INTERFACE_NOT_FOUND",
    "RPC_S_INTERNAL_ERROR",
    "RPC_S_INVALID_ASYNC_CALL",
    "RPC_S_INVALID_ASYNC_HANDLE",
    "RPC_S_INVALID_AUTH_IDENTITY",
    "RPC_S_INVALID_BINDING",
    "RPC_S_INVALID_BOUND",
    "RPC_S_INVALID_ENDPOINT_FORMAT",
    "RPC_S_INVALID_NAF_ID",
    "RPC_S_INVALID_NAME_SYNTAX",
    "RPC_S_INVALID_NETWORK_OPTIONS",
    "RPC_S_INVALID_NET_ADDR",
    "RPC_S_INVALID_OBJECT",
    "RPC_S_INVALID_RPC_PROTSEQ",
    "RPC_S_INVALID_STRING_BINDING",
    "RPC_S_INVALID_STRING_UUID",
    "RPC_S_INVALID_TAG",
    "RPC_S_INVALID_TIMEOUT",
    "RPC_S_INVALID_VERS_OPTION",
    "RPC_S_MAX_CALLS_TOO_SMALL",
    "RPC_S_NAME_SERVICE_UNAVAILABLE",
    "RPC_S_NOTHING_TO_EXPORT",
    "RPC_S_NOT_ALL_OBJS_EXPORTED",
    "RPC_S_NOT_ALL_OBJS_UNEXPORTED",
    "RPC_S_NOT_CANCELLED",
    "RPC_S_NOT_LISTENING",
    "RPC_S_NOT_RPC_ERROR",
    "RPC_S_NO_BINDINGS",
    "RPC_S_NO_CALL_ACTIVE",
    "RPC_S_NO_CONTEXT_AVAILABLE",
    "RPC_S_NO_ENDPOINT_FOUND",
    "RPC_S_NO_ENTRY_NAME",
    "RPC_S_NO_INTERFACES",
    "RPC_S_NO_MORE_BINDINGS",
    "RPC_S_NO_MORE_MEMBERS",
    "RPC_S_NO_PRINC_NAME",
    "RPC_S_NO_PROTSEQS",
    "RPC_S_NO_PROTSEQS_REGISTERED",
    "RPC_S_OBJECT_NOT_FOUND",
    "RPC_S_OUT_OF_RESOURCES",
    "RPC_S_PRF_ELT_NOT_ADDED",
    "RPC_S_PRF_ELT_NOT_REMOVED",
    "RPC_S_PROCNUM_OUT_OF_RANGE",
    "RPC_S_PROFILE_NOT_ADDED",
    "RPC_S_PROTOCOL_ERROR",
    "RPC_S_PROTSEQ_NOT_FOUND",
    "RPC_S_PROTSEQ_NOT_SUPPORTED",
    "RPC_S_PROXY_ACCESS_DENIED",
    "RPC_S_SEC_PKG_ERROR",
    "RPC_S_SEND_INCOMPLETE",
    "RPC_S_SERVER_TOO_BUSY",
    "RPC_S_SERVER_UNAVAILABLE",
    "RPC_S_STRING_TOO_LONG",
    "RPC_S_SYSTEM_HANDLE_COUNT_EXCEEDED",
    "RPC_S_SYSTEM_HANDLE_TYPE_MISMATCH",
    "RPC_S_TYPE_ALREADY_REGISTERED",
    "RPC_S_UNKNOWN_AUTHN_LEVEL",
    "RPC_S_UNKNOWN_AUTHN_SERVICE",
    "RPC_S_UNKNOWN_AUTHN_TYPE",
    "RPC_S_UNKNOWN_AUTHZ_SERVICE",
    "RPC_S_UNKNOWN_IF",
    "RPC_S_UNKNOWN_MGR_TYPE",
    "RPC_S_UNSUPPORTED_AUTHN_LEVEL",
    "RPC_S_UNSUPPORTED_NAME_SYNTAX",
    "RPC_S_UNSUPPORTED_TRANS_SYN",
    "RPC_S_UNSUPPORTED_TYPE",
    "RPC_S_UUID_LOCAL_ONLY",
    "RPC_S_UUID_NO_ADDRESS",
    "RPC_S_WRONG_KIND_OF_BINDING",
    "RPC_S_ZERO_DIVIDE",
    "RPC_TRANSFER_SYNTAX",
    "RPC_TYPE_DISCONNECT_EVENT_CONTEXT_HANDLE",
    "RPC_TYPE_STRICT_CONTEXT_HANDLE",
    "RPC_VERSION",
    "RpcAsyncAbortCall",
    "RpcAsyncCancelCall",
    "RpcAsyncCompleteCall",
    "RpcAsyncGetCallStatus",
    "RpcAsyncInitializeHandle",
    "RpcAsyncRegisterInfo",
    "RpcBindingBind",
    "RpcBindingCopy",
    "RpcBindingCreateA",
    "RpcBindingCreateW",
    "RpcBindingFree",
    "RpcBindingFromStringBindingA",
    "RpcBindingFromStringBindingW",
    "RpcBindingInqAuthClientA",
    "RpcBindingInqAuthClientExA",
    "RpcBindingInqAuthClientExW",
    "RpcBindingInqAuthClientW",
    "RpcBindingInqAuthInfoA",
    "RpcBindingInqAuthInfoExA",
    "RpcBindingInqAuthInfoExW",
    "RpcBindingInqAuthInfoW",
    "RpcBindingInqMaxCalls",
    "RpcBindingInqObject",
    "RpcBindingInqOption",
    "RpcBindingReset",
    "RpcBindingServerFromClient",
    "RpcBindingSetAuthInfoA",
    "RpcBindingSetAuthInfoExA",
    "RpcBindingSetAuthInfoExW",
    "RpcBindingSetAuthInfoW",
    "RpcBindingSetObject",
    "RpcBindingSetOption",
    "RpcBindingToStringBindingA",
    "RpcBindingToStringBindingW",
    "RpcBindingUnbind",
    "RpcBindingVectorFree",
    "RpcCallClientLocality",
    "RpcCallClientLocality_rcclClientUnknownLocality",
    "RpcCallClientLocality_rcclInvalid",
    "RpcCallClientLocality_rcclLocal",
    "RpcCallClientLocality_rcclRemote",
    "RpcCallType",
    "RpcCallType_rctGuaranteed",
    "RpcCallType_rctInvalid",
    "RpcCallType_rctNormal",
    "RpcCallType_rctTraining",
    "RpcCancelThread",
    "RpcCancelThreadEx",
    "RpcCertGeneratePrincipalNameA",
    "RpcCertGeneratePrincipalNameW",
    "RpcEpRegisterA",
    "RpcEpRegisterNoReplaceA",
    "RpcEpRegisterNoReplaceW",
    "RpcEpRegisterW",
    "RpcEpResolveBinding",
    "RpcEpUnregister",
    "RpcErrorAddRecord",
    "RpcErrorClearInformation",
    "RpcErrorEndEnumeration",
    "RpcErrorGetNextRecord",
    "RpcErrorGetNumberOfRecords",
    "RpcErrorLoadErrorInfo",
    "RpcErrorResetEnumeration",
    "RpcErrorSaveErrorInfo",
    "RpcErrorStartEnumeration",
    "RpcExceptionFilter",
    "RpcFreeAuthorizationContext",
    "RpcGetAuthorizationContextForClient",
    "RpcIfIdVectorFree",
    "RpcIfInqId",
    "RpcImpersonateClient",
    "RpcImpersonateClient2",
    "RpcImpersonateClientContainer",
    "RpcLocalAddressFormat",
    "RpcLocalAddressFormat_rlafIPv4",
    "RpcLocalAddressFormat_rlafIPv6",
    "RpcLocalAddressFormat_rlafInvalid",
    "RpcMgmtEnableIdleCleanup",
    "RpcMgmtEpEltInqBegin",
    "RpcMgmtEpEltInqDone",
    "RpcMgmtEpEltInqNextA",
    "RpcMgmtEpEltInqNextW",
    "RpcMgmtEpUnregister",
    "RpcMgmtInqComTimeout",
    "RpcMgmtInqDefaultProtectLevel",
    "RpcMgmtInqIfIds",
    "RpcMgmtInqServerPrincNameA",
    "RpcMgmtInqServerPrincNameW",
    "RpcMgmtInqStats",
    "RpcMgmtIsServerListening",
    "RpcMgmtSetAuthorizationFn",
    "RpcMgmtSetCancelTimeout",
    "RpcMgmtSetComTimeout",
    "RpcMgmtSetServerStackSize",
    "RpcMgmtStatsVectorFree",
    "RpcMgmtStopServerListening",
    "RpcMgmtWaitServerListen",
    "RpcNetworkInqProtseqsA",
    "RpcNetworkInqProtseqsW",
    "RpcNetworkIsProtseqValidA",
    "RpcNetworkIsProtseqValidW",
    "RpcNsBindingExportA",
    "RpcNsBindingExportPnPA",
    "RpcNsBindingExportPnPW",
    "RpcNsBindingExportW",
    "RpcNsBindingImportBeginA",
    "RpcNsBindingImportBeginW",
    "RpcNsBindingImportDone",
    "RpcNsBindingImportNext",
    "RpcNsBindingInqEntryNameA",
    "RpcNsBindingInqEntryNameW",
    "RpcNsBindingLookupBeginA",
    "RpcNsBindingLookupBeginW",
    "RpcNsBindingLookupDone",
    "RpcNsBindingLookupNext",
    "RpcNsBindingSelect",
    "RpcNsBindingUnexportA",
    "RpcNsBindingUnexportPnPA",
    "RpcNsBindingUnexportPnPW",
    "RpcNsBindingUnexportW",
    "RpcNsEntryExpandNameA",
    "RpcNsEntryExpandNameW",
    "RpcNsEntryObjectInqBeginA",
    "RpcNsEntryObjectInqBeginW",
    "RpcNsEntryObjectInqDone",
    "RpcNsEntryObjectInqNext",
    "RpcNsGroupDeleteA",
    "RpcNsGroupDeleteW",
    "RpcNsGroupMbrAddA",
    "RpcNsGroupMbrAddW",
    "RpcNsGroupMbrInqBeginA",
    "RpcNsGroupMbrInqBeginW",
    "RpcNsGroupMbrInqDone",
    "RpcNsGroupMbrInqNextA",
    "RpcNsGroupMbrInqNextW",
    "RpcNsGroupMbrRemoveA",
    "RpcNsGroupMbrRemoveW",
    "RpcNsMgmtBindingUnexportA",
    "RpcNsMgmtBindingUnexportW",
    "RpcNsMgmtEntryCreateA",
    "RpcNsMgmtEntryCreateW",
    "RpcNsMgmtEntryDeleteA",
    "RpcNsMgmtEntryDeleteW",
    "RpcNsMgmtEntryInqIfIdsA",
    "RpcNsMgmtEntryInqIfIdsW",
    "RpcNsMgmtHandleSetExpAge",
    "RpcNsMgmtInqExpAge",
    "RpcNsMgmtSetExpAge",
    "RpcNsProfileDeleteA",
    "RpcNsProfileDeleteW",
    "RpcNsProfileEltAddA",
    "RpcNsProfileEltAddW",
    "RpcNsProfileEltInqBeginA",
    "RpcNsProfileEltInqBeginW",
    "RpcNsProfileEltInqDone",
    "RpcNsProfileEltInqNextA",
    "RpcNsProfileEltInqNextW",
    "RpcNsProfileEltRemoveA",
    "RpcNsProfileEltRemoveW",
    "RpcObjectInqType",
    "RpcObjectSetInqFn",
    "RpcObjectSetType",
    "RpcPerfCounters",
    "RpcPerfCounters_RpcAttemptedLbsDecisions",
    "RpcPerfCounters_RpcAttemptedLbsMessages",
    "RpcPerfCounters_RpcBackEndConnectionAttempts",
    "RpcPerfCounters_RpcBackEndConnectionFailed",
    "RpcPerfCounters_RpcCurrentUniqueUser",
    "RpcPerfCounters_RpcFailedLbsDecisions",
    "RpcPerfCounters_RpcFailedLbsMessages",
    "RpcPerfCounters_RpcIncomingBandwidth",
    "RpcPerfCounters_RpcIncomingConnections",
    "RpcPerfCounters_RpcLastCounter",
    "RpcPerfCounters_RpcOutgoingBandwidth",
    "RpcPerfCounters_RpcRequestsPerSecond",
    "RpcProtseqVectorFreeA",
    "RpcProtseqVectorFreeW",
    "RpcRaiseException",
    "RpcRevertContainerImpersonation",
    "RpcRevertToSelf",
    "RpcRevertToSelfEx",
    "RpcServerCompleteSecurityCallback",
    "RpcServerInqBindingHandle",
    "RpcServerInqBindings",
    "RpcServerInqBindingsEx",
    "RpcServerInqCallAttributesA",
    "RpcServerInqCallAttributesW",
    "RpcServerInqDefaultPrincNameA",
    "RpcServerInqDefaultPrincNameW",
    "RpcServerInqIf",
    "RpcServerInterfaceGroupActivate",
    "RpcServerInterfaceGroupClose",
    "RpcServerInterfaceGroupCreateA",
    "RpcServerInterfaceGroupCreateW",
    "RpcServerInterfaceGroupDeactivate",
    "RpcServerInterfaceGroupInqBindings",
    "RpcServerListen",
    "RpcServerRegisterAuthInfoA",
    "RpcServerRegisterAuthInfoW",
    "RpcServerRegisterIf",
    "RpcServerRegisterIf2",
    "RpcServerRegisterIf3",
    "RpcServerRegisterIfEx",
    "RpcServerSubscribeForNotification",
    "RpcServerTestCancel",
    "RpcServerUnregisterIf",
    "RpcServerUnregisterIfEx",
    "RpcServerUnsubscribeForNotification",
    "RpcServerUseAllProtseqs",
    "RpcServerUseAllProtseqsEx",
    "RpcServerUseAllProtseqsIf",
    "RpcServerUseAllProtseqsIfEx",
    "RpcServerUseProtseqA",
    "RpcServerUseProtseqEpA",
    "RpcServerUseProtseqEpExA",
    "RpcServerUseProtseqEpExW",
    "RpcServerUseProtseqEpW",
    "RpcServerUseProtseqExA",
    "RpcServerUseProtseqExW",
    "RpcServerUseProtseqIfA",
    "RpcServerUseProtseqIfExA",
    "RpcServerUseProtseqIfExW",
    "RpcServerUseProtseqIfW",
    "RpcServerUseProtseqW",
    "RpcServerYield",
    "RpcSmAllocate",
    "RpcSmClientFree",
    "RpcSmDestroyClientContext",
    "RpcSmDisableAllocate",
    "RpcSmEnableAllocate",
    "RpcSmFree",
    "RpcSmGetThreadHandle",
    "RpcSmSetClientAllocFree",
    "RpcSmSetThreadHandle",
    "RpcSmSwapClientAllocFree",
    "RpcSsAllocate",
    "RpcSsContextLockExclusive",
    "RpcSsContextLockShared",
    "RpcSsDestroyClientContext",
    "RpcSsDisableAllocate",
    "RpcSsDontSerializeContext",
    "RpcSsEnableAllocate",
    "RpcSsFree",
    "RpcSsGetContextBinding",
    "RpcSsGetThreadHandle",
    "RpcSsSetClientAllocFree",
    "RpcSsSetThreadHandle",
    "RpcSsSwapClientAllocFree",
    "RpcStringBindingComposeA",
    "RpcStringBindingComposeW",
    "RpcStringBindingParseA",
    "RpcStringBindingParseW",
    "RpcStringFreeA",
    "RpcStringFreeW",
    "RpcTestCancel",
    "RpcUserFree",
    "SCONTEXT_QUEUE",
    "SEC_WINNT_AUTH_IDENTITY",
    "SEC_WINNT_AUTH_IDENTITY_A",
    "SEC_WINNT_AUTH_IDENTITY_ANSI",
    "SEC_WINNT_AUTH_IDENTITY_UNICODE",
    "SEC_WINNT_AUTH_IDENTITY_W",
    "SERVER_ROUTINE",
    "STUB_CALL_SERVER",
    "STUB_CALL_SERVER_NO_HRESULT",
    "STUB_MARSHAL",
    "STUB_PHASE",
    "STUB_THUNK",
    "STUB_UNMARSHAL",
    "SYSTEM_HANDLE_COMPOSITION_OBJECT",
    "SYSTEM_HANDLE_EVENT",
    "SYSTEM_HANDLE_FILE",
    "SYSTEM_HANDLE_INVALID",
    "SYSTEM_HANDLE_JOB",
    "SYSTEM_HANDLE_MAX",
    "SYSTEM_HANDLE_MUTEX",
    "SYSTEM_HANDLE_PIPE",
    "SYSTEM_HANDLE_PROCESS",
    "SYSTEM_HANDLE_REG_KEY",
    "SYSTEM_HANDLE_SECTION",
    "SYSTEM_HANDLE_SEMAPHORE",
    "SYSTEM_HANDLE_SOCKET",
    "SYSTEM_HANDLE_THREAD",
    "SYSTEM_HANDLE_TOKEN",
    "TARGET_IS_NT100_OR_LATER",
    "TARGET_IS_NT351_OR_WIN95_OR_LATER",
    "TARGET_IS_NT40_OR_LATER",
    "TARGET_IS_NT50_OR_LATER",
    "TARGET_IS_NT51_OR_LATER",
    "TARGET_IS_NT60_OR_LATER",
    "TARGET_IS_NT61_OR_LATER",
    "TARGET_IS_NT62_OR_LATER",
    "TARGET_IS_NT63_OR_LATER",
    "TRANSPORT_TYPE_CN",
    "TRANSPORT_TYPE_DG",
    "TRANSPORT_TYPE_LPC",
    "TRANSPORT_TYPE_WMSG",
    "USER_CALL_IS_ASYNC",
    "USER_CALL_NEW_CORRELATION_DESC",
    "USER_MARSHAL_CB",
    "USER_MARSHAL_CB_BUFFER_SIZE",
    "USER_MARSHAL_CB_FREE",
    "USER_MARSHAL_CB_MARSHALL",
    "USER_MARSHAL_CB_TYPE",
    "USER_MARSHAL_CB_UNMARSHALL",
    "USER_MARSHAL_FC_BYTE",
    "USER_MARSHAL_FC_CHAR",
    "USER_MARSHAL_FC_DOUBLE",
    "USER_MARSHAL_FC_FLOAT",
    "USER_MARSHAL_FC_HYPER",
    "USER_MARSHAL_FC_LONG",
    "USER_MARSHAL_FC_SHORT",
    "USER_MARSHAL_FC_SMALL",
    "USER_MARSHAL_FC_ULONG",
    "USER_MARSHAL_FC_USHORT",
    "USER_MARSHAL_FC_USMALL",
    "USER_MARSHAL_FC_WCHAR",
    "USER_MARSHAL_FREEING_ROUTINE",
    "USER_MARSHAL_MARSHALLING_ROUTINE",
    "USER_MARSHAL_ROUTINE_QUADRUPLE",
    "USER_MARSHAL_SIZING_ROUTINE",
    "USER_MARSHAL_UNMARSHALLING_ROUTINE",
    "UUID_VECTOR",
    "UuidCompare",
    "UuidCreate",
    "UuidCreateNil",
    "UuidCreateSequential",
    "UuidEqual",
    "UuidFromStringA",
    "UuidFromStringW",
    "UuidHash",
    "UuidIsNil",
    "UuidToStringA",
    "UuidToStringW",
    "XLAT_CLIENT",
    "XLAT_SERVER",
    "XLAT_SIDE",
    "XMIT_HELPER_ROUTINE",
    "XMIT_ROUTINE_QUINTUPLE",
    "_NDR_ASYNC_MESSAGE",
    "_NDR_CORRELATION_INFO",
    "_NDR_PROC_CONTEXT",
    "_NDR_SCONTEXT",
    "__RPCPROXY_H_VERSION__",
    "cbNDRContext",
    "system_handle_t",
]
