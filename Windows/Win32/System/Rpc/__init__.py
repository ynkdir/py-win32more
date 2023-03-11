from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security.Cryptography
import Windows.Win32.System.Com
import Windows.Win32.System.IO
import Windows.Win32.System.Rpc
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
class ARRAY_INFO(Structure):
    Dimension: Int32
    BufferConformanceMark: POINTER(UInt32)
    BufferVarianceMark: POINTER(UInt32)
    MaxCountArray: POINTER(UInt32)
    OffsetArray: POINTER(UInt32)
    ActualCountArray: POINTER(UInt32)
RPC_C_BINDING_INFINITE_TIMEOUT: UInt32 = 10
RPC_C_BINDING_MIN_TIMEOUT: UInt32 = 0
RPC_C_BINDING_DEFAULT_TIMEOUT: UInt32 = 5
RPC_C_BINDING_MAX_TIMEOUT: UInt32 = 9
RPC_C_CANCEL_INFINITE_TIMEOUT: Int32 = -1
RPC_C_LISTEN_MAX_CALLS_DEFAULT: UInt32 = 1234
RPC_C_PROTSEQ_MAX_REQS_DEFAULT: UInt32 = 10
RPC_C_BIND_TO_ALL_NICS: UInt32 = 1
RPC_C_USE_INTERNET_PORT: UInt32 = 1
RPC_C_USE_INTRANET_PORT: UInt32 = 2
RPC_C_DONT_FAIL: UInt32 = 4
RPC_C_RPCHTTP_USE_LOAD_BALANCE: UInt32 = 8
RPC_C_TRY_ENFORCE_MAX_CALLS: UInt32 = 16
RPC_C_MQ_TEMPORARY: UInt32 = 0
RPC_C_MQ_PERMANENT: UInt32 = 1
RPC_C_MQ_CLEAR_ON_OPEN: UInt32 = 2
RPC_C_MQ_USE_EXISTING_SECURITY: UInt32 = 4
RPC_C_MQ_AUTHN_LEVEL_NONE: UInt32 = 0
RPC_C_MQ_AUTHN_LEVEL_PKT_INTEGRITY: UInt32 = 8
RPC_C_MQ_AUTHN_LEVEL_PKT_PRIVACY: UInt32 = 16
RPC_C_MQ_EXPRESS: UInt32 = 0
RPC_C_MQ_RECOVERABLE: UInt32 = 1
RPC_C_MQ_JOURNAL_NONE: UInt32 = 0
RPC_C_MQ_JOURNAL_DEADLETTER: UInt32 = 1
RPC_C_MQ_JOURNAL_ALWAYS: UInt32 = 2
RPC_C_OPT_MQ_DELIVERY: UInt32 = 1
RPC_C_OPT_MQ_PRIORITY: UInt32 = 2
RPC_C_OPT_MQ_JOURNAL: UInt32 = 3
RPC_C_OPT_MQ_ACKNOWLEDGE: UInt32 = 4
RPC_C_OPT_MQ_AUTHN_SERVICE: UInt32 = 5
RPC_C_OPT_MQ_AUTHN_LEVEL: UInt32 = 6
RPC_C_OPT_MQ_TIME_TO_REACH_QUEUE: UInt32 = 7
RPC_C_OPT_MQ_TIME_TO_BE_RECEIVED: UInt32 = 8
RPC_C_OPT_BINDING_NONCAUSAL: UInt32 = 9
RPC_C_OPT_SECURITY_CALLBACK: UInt32 = 10
RPC_C_OPT_UNIQUE_BINDING: UInt32 = 11
RPC_C_OPT_MAX_OPTIONS: UInt32 = 12
RPC_C_OPT_CALL_TIMEOUT: UInt32 = 12
RPC_C_OPT_DONT_LINGER: UInt32 = 13
RPC_C_OPT_TRANS_SEND_BUFFER_SIZE: UInt32 = 5
RPC_C_OPT_TRUST_PEER: UInt32 = 14
RPC_C_OPT_ASYNC_BLOCK: UInt32 = 15
RPC_C_OPT_OPTIMIZE_TIME: UInt32 = 16
RPC_C_FULL_CERT_CHAIN: UInt32 = 1
RPC_C_STATS_CALLS_IN: UInt32 = 0
RPC_C_STATS_CALLS_OUT: UInt32 = 1
RPC_C_STATS_PKTS_IN: UInt32 = 2
RPC_C_STATS_PKTS_OUT: UInt32 = 3
RPC_C_AUTHN_NONE: UInt32 = 0
RPC_C_AUTHN_DCE_PRIVATE: UInt32 = 1
RPC_C_AUTHN_DCE_PUBLIC: UInt32 = 2
RPC_C_AUTHN_DEC_PUBLIC: UInt32 = 4
RPC_C_AUTHN_GSS_NEGOTIATE: UInt32 = 9
RPC_C_AUTHN_WINNT: UInt32 = 10
RPC_C_AUTHN_GSS_SCHANNEL: UInt32 = 14
RPC_C_AUTHN_GSS_KERBEROS: UInt32 = 16
RPC_C_AUTHN_DPA: UInt32 = 17
RPC_C_AUTHN_MSN: UInt32 = 18
RPC_C_AUTHN_DIGEST: UInt32 = 21
RPC_C_AUTHN_KERNEL: UInt32 = 20
RPC_C_AUTHN_NEGO_EXTENDER: UInt32 = 30
RPC_C_AUTHN_PKU2U: UInt32 = 31
RPC_C_AUTHN_LIVE_SSP: UInt32 = 32
RPC_C_AUTHN_LIVEXP_SSP: UInt32 = 35
RPC_C_AUTHN_CLOUD_AP: UInt32 = 36
RPC_C_AUTHN_MSONLINE: UInt32 = 82
RPC_C_AUTHN_MQ: UInt32 = 100
RPC_C_AUTHN_DEFAULT: Int32 = -1
RPC_C_SECURITY_QOS_VERSION: Int32 = 1
RPC_C_SECURITY_QOS_VERSION_1: Int32 = 1
RPC_C_SECURITY_QOS_VERSION_2: Int32 = 2
RPC_C_HTTP_AUTHN_SCHEME_BASIC: UInt32 = 1
RPC_C_HTTP_AUTHN_SCHEME_NTLM: UInt32 = 2
RPC_C_HTTP_AUTHN_SCHEME_PASSPORT: UInt32 = 4
RPC_C_HTTP_AUTHN_SCHEME_DIGEST: UInt32 = 8
RPC_C_HTTP_AUTHN_SCHEME_NEGOTIATE: UInt32 = 16
RPC_C_HTTP_AUTHN_SCHEME_CERT: UInt32 = 65536
RPC_C_SECURITY_QOS_VERSION_3: Int32 = 3
RPC_C_SECURITY_QOS_VERSION_4: Int32 = 4
RPC_C_SECURITY_QOS_VERSION_5: Int32 = 5
RPC_PROTSEQ_TCP: UInt32 = 1
RPC_PROTSEQ_NMP: UInt32 = 2
RPC_PROTSEQ_LRPC: UInt32 = 3
RPC_PROTSEQ_HTTP: UInt32 = 4
RPC_BHT_OBJECT_UUID_VALID: UInt32 = 1
RPC_BHO_EXCLUSIVE_AND_GUARANTEED: UInt32 = 4
RPC_C_AUTHZ_NONE: UInt32 = 0
RPC_C_AUTHZ_NAME: UInt32 = 1
RPC_C_AUTHZ_DCE: UInt32 = 2
RPC_C_AUTHZ_DEFAULT: UInt32 = 4294967295
DCE_C_ERROR_STRING_LEN: UInt32 = 256
RPC_C_EP_ALL_ELTS: UInt32 = 0
RPC_C_EP_MATCH_BY_IF: UInt32 = 1
RPC_C_EP_MATCH_BY_OBJ: UInt32 = 2
RPC_C_EP_MATCH_BY_BOTH: UInt32 = 3
RPC_C_VERS_ALL: UInt32 = 1
RPC_C_VERS_COMPATIBLE: UInt32 = 2
RPC_C_VERS_EXACT: UInt32 = 3
RPC_C_VERS_MAJOR_ONLY: UInt32 = 4
RPC_C_VERS_UPTO: UInt32 = 5
RPC_C_MGMT_INQ_IF_IDS: UInt32 = 0
RPC_C_MGMT_INQ_PRINC_NAME: UInt32 = 1
RPC_C_MGMT_INQ_STATS: UInt32 = 2
RPC_C_MGMT_IS_SERVER_LISTEN: UInt32 = 3
RPC_C_MGMT_STOP_SERVER_LISTEN: UInt32 = 4
RPC_C_PARM_MAX_PACKET_LENGTH: UInt32 = 1
RPC_C_PARM_BUFFER_LENGTH: UInt32 = 2
RPC_IF_AUTOLISTEN: UInt32 = 1
RPC_IF_OLE: UInt32 = 2
RPC_IF_ALLOW_UNKNOWN_AUTHORITY: UInt32 = 4
RPC_IF_ALLOW_SECURE_ONLY: UInt32 = 8
RPC_IF_ALLOW_CALLBACKS_WITH_NO_AUTH: UInt32 = 16
RPC_IF_ALLOW_LOCAL_ONLY: UInt32 = 32
RPC_IF_SEC_NO_CACHE: UInt32 = 64
RPC_IF_SEC_CACHE_PER_PROC: UInt32 = 128
RPC_IF_ASYNC_CALLBACK: UInt32 = 256
RPC_FW_IF_FLAG_DCOM: UInt32 = 1
RPC_C_NOTIFY_ON_SEND_COMPLETE: UInt32 = 1
MaxNumberOfEEInfoParams: UInt32 = 4
RPC_EEINFO_VERSION: UInt32 = 1
EEInfoPreviousRecordsMissing: UInt32 = 1
EEInfoNextRecordsMissing: UInt32 = 2
EEInfoUseFileTime: UInt32 = 4
EEInfoGCCOM: UInt32 = 11
EEInfoGCFRS: UInt32 = 12
RPC_CALL_ATTRIBUTES_VERSION: UInt32 = 2
RPC_QUERY_SERVER_PRINCIPAL_NAME: UInt32 = 2
RPC_QUERY_CLIENT_PRINCIPAL_NAME: UInt32 = 4
RPC_QUERY_CALL_LOCAL_ADDRESS: UInt32 = 8
RPC_QUERY_CLIENT_PID: UInt32 = 16
RPC_QUERY_IS_CLIENT_LOCAL: UInt32 = 32
RPC_QUERY_NO_AUTH_REQUIRED: UInt32 = 64
RPC_QUERY_CLIENT_ID: UInt32 = 128
RPC_CALL_STATUS_CANCELLED: UInt32 = 1
RPC_CALL_STATUS_DISCONNECTED: UInt32 = 2
RPC_CONTEXT_HANDLE_DEFAULT_FLAGS: UInt32 = 0
RPC_CONTEXT_HANDLE_FLAGS: UInt32 = 805306368
RPC_CONTEXT_HANDLE_SERIALIZE: UInt32 = 268435456
RPC_CONTEXT_HANDLE_DONT_SERIALIZE: UInt32 = 536870912
RPC_TYPE_STRICT_CONTEXT_HANDLE: UInt32 = 1073741824
RPC_TYPE_DISCONNECT_EVENT_CONTEXT_HANDLE: UInt32 = 2147483648
RPC_NCA_FLAGS_DEFAULT: UInt32 = 0
RPC_NCA_FLAGS_IDEMPOTENT: UInt32 = 1
RPC_NCA_FLAGS_BROADCAST: UInt32 = 2
RPC_NCA_FLAGS_MAYBE: UInt32 = 4
RPCFLG_HAS_GUARANTEE: UInt32 = 16
RPCFLG_WINRT_REMOTE_ASYNC: UInt32 = 32
RPC_BUFFER_COMPLETE: UInt32 = 4096
RPC_BUFFER_PARTIAL: UInt32 = 8192
RPC_BUFFER_EXTRA: UInt32 = 16384
RPC_BUFFER_ASYNC: UInt32 = 32768
RPC_BUFFER_NONOTIFY: UInt32 = 65536
RPCFLG_MESSAGE: UInt32 = 16777216
RPCFLG_AUTO_COMPLETE: UInt32 = 134217728
RPCFLG_LOCAL_CALL: UInt32 = 268435456
RPCFLG_INPUT_SYNCHRONOUS: UInt32 = 536870912
RPCFLG_ASYNCHRONOUS: UInt32 = 1073741824
RPCFLG_NON_NDR: UInt32 = 2147483648
RPCFLG_HAS_MULTI_SYNTAXES: UInt32 = 33554432
RPCFLG_HAS_CALLBACK: UInt32 = 67108864
RPCFLG_ACCESSIBILITY_BIT1: UInt32 = 1048576
RPCFLG_ACCESSIBILITY_BIT2: UInt32 = 2097152
RPCFLG_ACCESS_LOCAL: UInt32 = 4194304
NDR_CUSTOM_OR_DEFAULT_ALLOCATOR: UInt32 = 268435456
NDR_DEFAULT_ALLOCATOR: UInt32 = 536870912
RPCFLG_NDR64_CONTAINS_ARM_LAYOUT: UInt32 = 67108864
RPCFLG_SENDER_WAITING_FOR_REPLY: UInt32 = 8388608
RPC_FLAGS_VALID_BIT: UInt32 = 32768
NT351_INTERFACE_SIZE: UInt32 = 64
RPC_INTERFACE_HAS_PIPES: UInt32 = 1
RPC_SYSTEM_HANDLE_FREE_UNRETRIEVED: UInt32 = 1
RPC_SYSTEM_HANDLE_FREE_RETRIEVED: UInt32 = 2
RPC_SYSTEM_HANDLE_FREE_ALL: UInt32 = 3
RPC_SYSTEM_HANDLE_FREE_ERROR_ON_CLOSE: UInt32 = 4
TRANSPORT_TYPE_CN: UInt32 = 1
TRANSPORT_TYPE_DG: UInt32 = 2
TRANSPORT_TYPE_LPC: UInt32 = 4
TRANSPORT_TYPE_WMSG: UInt32 = 8
RPC_P_ADDR_FORMAT_TCP_IPV4: UInt32 = 1
RPC_P_ADDR_FORMAT_TCP_IPV6: UInt32 = 2
RPC_C_OPT_SESSION_ID: UInt32 = 6
RPC_C_OPT_COOKIE_AUTH: UInt32 = 7
RPC_C_OPT_RESOURCE_TYPE_UUID: UInt32 = 8
RPC_PROXY_CONNECTION_TYPE_IN_PROXY: UInt32 = 0
RPC_PROXY_CONNECTION_TYPE_OUT_PROXY: UInt32 = 1
RPC_C_OPT_PRIVATE_SUPPRESS_WAKE: UInt32 = 1
RPC_C_OPT_PRIVATE_DO_NOT_DISTURB: UInt32 = 2
RPC_C_OPT_PRIVATE_BREAK_ON_SUSPEND: UInt32 = 3
RPC_C_PROFILE_DEFAULT_ELT: UInt32 = 0
RPC_C_PROFILE_ALL_ELT: UInt32 = 1
RPC_C_PROFILE_ALL_ELTS: UInt32 = 1
RPC_C_PROFILE_MATCH_BY_IF: UInt32 = 2
RPC_C_PROFILE_MATCH_BY_MBR: UInt32 = 3
RPC_C_PROFILE_MATCH_BY_BOTH: UInt32 = 4
RPC_C_NS_DEFAULT_EXP_AGE: Int32 = -1
TARGET_IS_NT100_OR_LATER: UInt32 = 1
TARGET_IS_NT63_OR_LATER: UInt32 = 1
TARGET_IS_NT62_OR_LATER: UInt32 = 1
TARGET_IS_NT61_OR_LATER: UInt32 = 1
TARGET_IS_NT60_OR_LATER: UInt32 = 1
TARGET_IS_NT51_OR_LATER: UInt32 = 1
TARGET_IS_NT50_OR_LATER: UInt32 = 1
TARGET_IS_NT40_OR_LATER: UInt32 = 1
TARGET_IS_NT351_OR_WIN95_OR_LATER: UInt32 = 1
cbNDRContext: UInt32 = 20
USER_CALL_IS_ASYNC: UInt32 = 256
USER_CALL_NEW_CORRELATION_DESC: UInt32 = 512
MIDL_WINRT_TYPE_SERIALIZATION_INFO_CURRENT_VERSION: Int32 = 1
USER_MARSHAL_FC_BYTE: UInt32 = 1
USER_MARSHAL_FC_CHAR: UInt32 = 2
USER_MARSHAL_FC_SMALL: UInt32 = 3
USER_MARSHAL_FC_USMALL: UInt32 = 4
USER_MARSHAL_FC_WCHAR: UInt32 = 5
USER_MARSHAL_FC_SHORT: UInt32 = 6
USER_MARSHAL_FC_USHORT: UInt32 = 7
USER_MARSHAL_FC_LONG: UInt32 = 8
USER_MARSHAL_FC_ULONG: UInt32 = 9
USER_MARSHAL_FC_FLOAT: UInt32 = 10
USER_MARSHAL_FC_HYPER: UInt32 = 11
USER_MARSHAL_FC_DOUBLE: UInt32 = 12
INVALID_FRAGMENT_ID: UInt32 = 0
NDR64_FC_EXPLICIT_HANDLE: UInt32 = 0
NDR64_FC_BIND_GENERIC: UInt32 = 1
NDR64_FC_BIND_PRIMITIVE: UInt32 = 2
NDR64_FC_AUTO_HANDLE: UInt32 = 3
NDR64_FC_CALLBACK_HANDLE: UInt32 = 4
NDR64_FC_NO_HANDLE: UInt32 = 5
__RPCPROXY_H_VERSION__: UInt32 = 475
MidlInterceptionInfoVersionOne: Int32 = 1
MidlWinrtTypeSerializationInfoVersionOne: Int32 = 1
@winfunctype('RPCRT4.dll')
def IUnknown_QueryInterface_Proxy(This: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RPCRT4.dll')
def IUnknown_AddRef_Proxy(This: Windows.Win32.System.Com.IUnknown_head) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def IUnknown_Release_Proxy(This: Windows.Win32.System.Com.IUnknown_head) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def RpcBindingCopy(SourceBinding: c_void_p, DestinationBinding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingFree(Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetOption(hBinding: c_void_p, option: UInt32, optionValue: UIntPtr) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqOption(hBinding: c_void_p, option: UInt32, pOptionValue: POINTER(UIntPtr)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingFromStringBindingA(StringBinding: c_char_p_no, Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingFromStringBindingW(StringBinding: POINTER(UInt16), Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsGetContextBinding(ContextHandle: c_void_p, Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqMaxCalls(Binding: c_void_p, MaxCalls: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqObject(Binding: c_void_p, ObjectUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingReset(Binding: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetObject(Binding: c_void_p, ObjectUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqDefaultProtectLevel(AuthnSvc: UInt32, AuthnLevel: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingToStringBindingA(Binding: c_void_p, StringBinding: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingToStringBindingW(Binding: c_void_p, StringBinding: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingVectorFree(BindingVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringBindingComposeA(ObjUuid: c_char_p_no, ProtSeq: c_char_p_no, NetworkAddr: c_char_p_no, Endpoint: c_char_p_no, Options: c_char_p_no, StringBinding: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringBindingComposeW(ObjUuid: POINTER(UInt16), ProtSeq: POINTER(UInt16), NetworkAddr: POINTER(UInt16), Endpoint: POINTER(UInt16), Options: POINTER(UInt16), StringBinding: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringBindingParseA(StringBinding: c_char_p_no, ObjUuid: POINTER(c_char_p_no), Protseq: POINTER(c_char_p_no), NetworkAddr: POINTER(c_char_p_no), Endpoint: POINTER(c_char_p_no), NetworkOptions: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringBindingParseW(StringBinding: POINTER(UInt16), ObjUuid: POINTER(POINTER(UInt16)), Protseq: POINTER(POINTER(UInt16)), NetworkAddr: POINTER(POINTER(UInt16)), Endpoint: POINTER(POINTER(UInt16)), NetworkOptions: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringFreeA(String: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringFreeW(String: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcIfInqId(RpcIfHandle: c_void_p, RpcIfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkIsProtseqValidA(Protseq: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkIsProtseqValidW(Protseq: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqComTimeout(Binding: c_void_p, Timeout: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetComTimeout(Binding: c_void_p, Timeout: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetCancelTimeout(Timeout: Int32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkInqProtseqsA(ProtseqVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORA_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkInqProtseqsW(ProtseqVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORW_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcObjectInqType(ObjUuid: POINTER(Guid), TypeUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcObjectSetInqFn(InquiryFn: Windows.Win32.System.Rpc.RPC_OBJECT_INQ_FN) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcObjectSetType(ObjUuid: POINTER(Guid), TypeUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcProtseqVectorFreeA(ProtseqVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORA_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcProtseqVectorFreeW(ProtseqVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORW_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqBindings(BindingVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqBindingsEx(SecurityDescriptor: c_void_p, BindingVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqIf(IfSpec: c_void_p, MgrTypeUuid: POINTER(Guid), MgrEpv: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerListen(MinimumCallThreads: UInt32, MaxCalls: UInt32, DontWait: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIf(IfSpec: c_void_p, MgrTypeUuid: POINTER(Guid), MgrEpv: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIfEx(IfSpec: c_void_p, MgrTypeUuid: POINTER(Guid), MgrEpv: c_void_p, Flags: UInt32, MaxCalls: UInt32, IfCallback: Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIf2(IfSpec: c_void_p, MgrTypeUuid: POINTER(Guid), MgrEpv: c_void_p, Flags: UInt32, MaxCalls: UInt32, MaxRpcSize: UInt32, IfCallbackFn: Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIf3(IfSpec: c_void_p, MgrTypeUuid: POINTER(Guid), MgrEpv: c_void_p, Flags: UInt32, MaxCalls: UInt32, MaxRpcSize: UInt32, IfCallback: Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUnregisterIf(IfSpec: c_void_p, MgrTypeUuid: POINTER(Guid), WaitForCallsToComplete: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUnregisterIfEx(IfSpec: c_void_p, MgrTypeUuid: POINTER(Guid), RundownContextHandles: Int32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqs(MaxCalls: UInt32, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqsEx(MaxCalls: UInt32, SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqsIf(MaxCalls: UInt32, IfSpec: c_void_p, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqsIfEx(MaxCalls: UInt32, IfSpec: c_void_p, SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqA(Protseq: c_char_p_no, MaxCalls: UInt32, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqExA(Protseq: c_char_p_no, MaxCalls: UInt32, SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqW(Protseq: POINTER(UInt16), MaxCalls: UInt32, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqExW(Protseq: POINTER(UInt16), MaxCalls: UInt32, SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpA(Protseq: c_char_p_no, MaxCalls: UInt32, Endpoint: c_char_p_no, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpExA(Protseq: c_char_p_no, MaxCalls: UInt32, Endpoint: c_char_p_no, SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpW(Protseq: POINTER(UInt16), MaxCalls: UInt32, Endpoint: POINTER(UInt16), SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpExW(Protseq: POINTER(UInt16), MaxCalls: UInt32, Endpoint: POINTER(UInt16), SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfA(Protseq: c_char_p_no, MaxCalls: UInt32, IfSpec: c_void_p, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfExA(Protseq: c_char_p_no, MaxCalls: UInt32, IfSpec: c_void_p, SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfW(Protseq: POINTER(UInt16), MaxCalls: UInt32, IfSpec: c_void_p, SecurityDescriptor: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfExW(Protseq: POINTER(UInt16), MaxCalls: UInt32, IfSpec: c_void_p, SecurityDescriptor: c_void_p, Policy: POINTER(Windows.Win32.System.Rpc.RPC_POLICY_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerYield() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtStatsVectorFree(StatsVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_STATS_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqStats(Binding: c_void_p, Statistics: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_STATS_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtIsServerListening(Binding: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtStopServerListening(Binding: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtWaitServerListen() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetServerStackSize(ThreadStackSize: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsDontSerializeContext() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEnableIdleCleanup() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqIfIds(Binding: c_void_p, IfIdVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcIfIdVectorFree(IfIdVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqServerPrincNameA(Binding: c_void_p, AuthnSvc: UInt32, ServerPrincName: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqServerPrincNameW(Binding: c_void_p, AuthnSvc: UInt32, ServerPrincName: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqDefaultPrincNameA(AuthnSvc: UInt32, PrincName: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqDefaultPrincNameW(AuthnSvc: UInt32, PrincName: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcEpResolveBinding(Binding: c_void_p, IfSpec: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNsBindingInqEntryNameA(Binding: c_void_p, EntryNameSyntax: UInt32, EntryName: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNsBindingInqEntryNameW(Binding: c_void_p, EntryNameSyntax: UInt32, EntryName: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingCreateA(Template: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_A_head), Security: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_A_head), Options: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_V1_head), Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingCreateW(Template: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_W_head), Security: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_W_head), Options: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_V1_head), Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqBindingHandle(Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcImpersonateClient(BindingHandle: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcImpersonateClient2(BindingHandle: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRevertToSelfEx(BindingHandle: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRevertToSelf() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcImpersonateClientContainer(BindingHandle: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRevertContainerImpersonation() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientA(ClientBinding: c_void_p, Privs: POINTER(c_void_p), ServerPrincName: POINTER(c_char_p_no), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientW(ClientBinding: c_void_p, Privs: POINTER(c_void_p), ServerPrincName: POINTER(POINTER(UInt16)), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientExA(ClientBinding: c_void_p, Privs: POINTER(c_void_p), ServerPrincName: POINTER(c_char_p_no), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32), Flags: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientExW(ClientBinding: c_void_p, Privs: POINTER(c_void_p), ServerPrincName: POINTER(POINTER(UInt16)), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32), Flags: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoA(Binding: c_void_p, ServerPrincName: POINTER(c_char_p_no), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(c_void_p), AuthzSvc: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoW(Binding: c_void_p, ServerPrincName: POINTER(POINTER(UInt16)), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(c_void_p), AuthzSvc: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoA(Binding: c_void_p, ServerPrincName: c_char_p_no, AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: c_void_p, AuthzSvc: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoExA(Binding: c_void_p, ServerPrincName: c_char_p_no, AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: c_void_p, AuthzSvc: UInt32, SecurityQos: POINTER(Windows.Win32.System.Rpc.RPC_SECURITY_QOS_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoW(Binding: c_void_p, ServerPrincName: POINTER(UInt16), AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: c_void_p, AuthzSvc: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoExW(Binding: c_void_p, ServerPrincName: POINTER(UInt16), AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: c_void_p, AuthzSvc: UInt32, SecurityQOS: POINTER(Windows.Win32.System.Rpc.RPC_SECURITY_QOS_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoExA(Binding: c_void_p, ServerPrincName: POINTER(c_char_p_no), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(c_void_p), AuthzSvc: POINTER(UInt32), RpcQosVersion: UInt32, SecurityQOS: POINTER(Windows.Win32.System.Rpc.RPC_SECURITY_QOS_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoExW(Binding: c_void_p, ServerPrincName: POINTER(POINTER(UInt16)), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(c_void_p), AuthzSvc: POINTER(UInt32), RpcQosVersion: UInt32, SecurityQOS: POINTER(Windows.Win32.System.Rpc.RPC_SECURITY_QOS_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerCompleteSecurityCallback(BindingHandle: c_void_p, Status: Windows.Win32.System.Rpc.RPC_STATUS) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterAuthInfoA(ServerPrincName: c_char_p_no, AuthnSvc: UInt32, GetKeyFn: Windows.Win32.System.Rpc.RPC_AUTH_KEY_RETRIEVAL_FN, Arg: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterAuthInfoW(ServerPrincName: POINTER(UInt16), AuthnSvc: UInt32, GetKeyFn: Windows.Win32.System.Rpc.RPC_AUTH_KEY_RETRIEVAL_FN, Arg: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingServerFromClient(ClientBinding: c_void_p, ServerBinding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRaiseException(exception: Windows.Win32.System.Rpc.RPC_STATUS) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcTestCancel() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerTestCancel(BindingHandle: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcCancelThread(Thread: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcCancelThreadEx(Thread: c_void_p, Timeout: Int32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidCreate(Uuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidCreateSequential(Uuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidToStringA(Uuid: POINTER(Guid), StringUuid: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidFromStringA(StringUuid: c_char_p_no, Uuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidToStringW(Uuid: POINTER(Guid), StringUuid: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidFromStringW(StringUuid: POINTER(UInt16), Uuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidCompare(Uuid1: POINTER(Guid), Uuid2: POINTER(Guid), Status: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def UuidCreateNil(NilUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidEqual(Uuid1: POINTER(Guid), Uuid2: POINTER(Guid), Status: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def UuidHash(Uuid: POINTER(Guid), Status: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> UInt16: ...
@winfunctype('RPCRT4.dll')
def UuidIsNil(Uuid: POINTER(Guid), Status: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def RpcEpRegisterNoReplaceA(IfSpec: c_void_p, BindingVector: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), UuidVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head), Annotation: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcEpRegisterNoReplaceW(IfSpec: c_void_p, BindingVector: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), UuidVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head), Annotation: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcEpRegisterA(IfSpec: c_void_p, BindingVector: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), UuidVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head), Annotation: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcEpRegisterW(IfSpec: c_void_p, BindingVector: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), UuidVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head), Annotation: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcEpUnregister(IfSpec: c_void_p, BindingVector: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), UuidVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def DceErrorInqTextA(RpcStatus: Windows.Win32.System.Rpc.RPC_STATUS, ErrorText: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def DceErrorInqTextW(RpcStatus: Windows.Win32.System.Rpc.RPC_STATUS, ErrorText: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqBegin(EpBinding: c_void_p, InquiryType: UInt32, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), VersOption: UInt32, ObjectUuid: POINTER(Guid), InquiryContext: POINTER(POINTER(c_void_p))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqDone(InquiryContext: POINTER(POINTER(c_void_p))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqNextA(InquiryContext: POINTER(c_void_p), IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), Binding: POINTER(c_void_p), ObjectUuid: POINTER(Guid), Annotation: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqNextW(InquiryContext: POINTER(c_void_p), IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), Binding: POINTER(c_void_p), ObjectUuid: POINTER(Guid), Annotation: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpUnregister(EpBinding: c_void_p, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), Binding: c_void_p, ObjectUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetAuthorizationFn(AuthorizationFn: Windows.Win32.System.Rpc.RPC_MGMT_AUTHORIZATION_FN) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcExceptionFilter(ExceptionCode: UInt32) -> Int32: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupCreateW(Interfaces: POINTER(Windows.Win32.System.Rpc.RPC_INTERFACE_TEMPLATEW_head), NumIfs: UInt32, Endpoints: POINTER(Windows.Win32.System.Rpc.RPC_ENDPOINT_TEMPLATEW_head), NumEndpoints: UInt32, IdlePeriod: UInt32, IdleCallbackFn: Windows.Win32.System.Rpc.RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN, IdleCallbackContext: c_void_p, IfGroup: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupCreateA(Interfaces: POINTER(Windows.Win32.System.Rpc.RPC_INTERFACE_TEMPLATEA_head), NumIfs: UInt32, Endpoints: POINTER(Windows.Win32.System.Rpc.RPC_ENDPOINT_TEMPLATEA_head), NumEndpoints: UInt32, IdlePeriod: UInt32, IdleCallbackFn: Windows.Win32.System.Rpc.RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN, IdleCallbackContext: c_void_p, IfGroup: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupClose(IfGroup: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupActivate(IfGroup: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupDeactivate(IfGroup: c_void_p, ForceDeactivation: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupInqBindings(IfGroup: c_void_p, BindingVector: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcNegotiateTransferSyntax(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetBuffer(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetBufferWithObject(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), ObjectUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSendReceive(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcFreeBuffer(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSend(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcReceive(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), Size: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcFreePipeBuffer(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcReallocPipeBuffer(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), NewSize: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcRequestMutex(Mutex: POINTER(c_void_p)) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcClearMutex(Mutex: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcDeleteMutex(Mutex: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcAllocate(Size: UInt32) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def I_RpcFree(Object: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcPauseExecution(Milliseconds: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetExtendedError() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSystemHandleTypeSpecificWork(Handle: c_void_p, ActualType: Byte, IdlType: Byte, MarshalDirection: Windows.Win32.System.Rpc.LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetCurrentCallHandle() -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def I_RpcNsInterfaceExported(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), RpcInterfaceInformation: POINTER(Windows.Win32.System.Rpc.RPC_SERVER_INTERFACE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcNsInterfaceUnexported(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), RpcInterfaceInformation: POINTER(Windows.Win32.System.Rpc.RPC_SERVER_INTERFACE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingToStaticStringBindingW(Binding: c_void_p, StringBinding: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqSecurityContext(Binding: c_void_p, SecurityContextHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqSecurityContextKeyInfo(Binding: c_void_p, KeyInfo: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqWireIdForSnego(Binding: c_void_p, WireId: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqMarshalledTargetInfo(Binding: c_void_p, MarshalledTargetInfoSize: POINTER(UInt32), MarshalledTargetInfo: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqLocalClientPID(Binding: c_void_p, Pid: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingHandleToAsyncHandle(Binding: c_void_p, AsyncHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcNsBindingSetEntryNameW(Binding: c_void_p, EntryNameSyntax: UInt32, EntryName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcNsBindingSetEntryNameA(Binding: c_void_p, EntryNameSyntax: UInt32, EntryName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseqEp2A(NetworkAddress: c_char_p_no, Protseq: c_char_p_no, MaxCalls: UInt32, Endpoint: c_char_p_no, SecurityDescriptor: c_void_p, Policy: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseqEp2W(NetworkAddress: POINTER(UInt16), Protseq: POINTER(UInt16), MaxCalls: UInt32, Endpoint: POINTER(UInt16), SecurityDescriptor: c_void_p, Policy: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseq2W(NetworkAddress: POINTER(UInt16), Protseq: POINTER(UInt16), MaxCalls: UInt32, SecurityDescriptor: c_void_p, Policy: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseq2A(NetworkAddress: c_char_p_no, Protseq: c_char_p_no, MaxCalls: UInt32, SecurityDescriptor: c_void_p, Policy: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerStartService(Protseq: POINTER(UInt16), Endpoint: POINTER(UInt16), IfSpec: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqDynamicEndpointW(Binding: c_void_p, DynamicEndpoint: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqDynamicEndpointA(Binding: c_void_p, DynamicEndpoint: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerCheckClientRestriction(Context: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqTransportType(Binding: c_void_p, Type: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcIfInqTransferSyntaxes(RpcIfHandle: c_void_p, TransferSyntaxes: POINTER(Windows.Win32.System.Rpc.RPC_TRANSFER_SYNTAX_head), TransferSyntaxSize: UInt32, TransferSyntaxCount: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_UuidCreate(Uuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingCopy(SourceBinding: c_void_p, DestinationBinding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingIsClientLocal(BindingHandle: c_void_p, ClientLocalFlag: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingCreateNP(ServerName: POINTER(UInt16), ServiceName: POINTER(UInt16), NetworkOptions: POINTER(UInt16), Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSsDontSerializeContext() -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerRegisterForwardFunction(pForwardFunction: POINTER(Windows.Win32.System.Rpc.RPC_FORWARD_FUNCTION)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqAddressChangeFn() -> POINTER(Windows.Win32.System.Rpc.RPC_ADDRESS_CHANGE_FN): ...
@winfunctype('RPCRT4.dll')
def I_RpcServerSetAddressChangeFn(pAddressChangeFn: POINTER(Windows.Win32.System.Rpc.RPC_ADDRESS_CHANGE_FN)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqLocalConnAddress(Binding: c_void_p, Buffer: c_void_p, BufferSize: POINTER(UInt32), AddressFormat: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqRemoteConnAddress(Binding: c_void_p, Buffer: c_void_p, BufferSize: POINTER(UInt32), AddressFormat: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSessionStrictContextHandle() -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcTurnOnEEInfoPropagation() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqTransportType(Type: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcMapWin32Status(Status: Windows.Win32.System.Rpc.RPC_STATUS) -> Int32: ...
@winfunctype('RPCRT4.dll')
def I_RpcRecordCalloutFailure(RpcStatus: Windows.Win32.System.Rpc.RPC_STATUS, CallOutState: POINTER(Windows.Win32.System.Rpc.RDR_CALLOUT_STATE_head), DllName: POINTER(UInt16)) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcMgmtEnableDedicatedThreadPool() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetDefaultSD(ppSecurityDescriptor: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcOpenClientProcess(Binding: c_void_p, DesiredAccess: UInt32, ClientProcess: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingIsServerLocal(Binding: c_void_p, ServerLocalFlag: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingSetPrivateOption(hBinding: c_void_p, option: UInt32, optionValue: UIntPtr) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerSubscribeForDisconnectNotification(Binding: c_void_p, hEvent: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerGetAssociationID(Binding: c_void_p, AssociationID: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerDisableExceptionFilter() -> Int32: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerSubscribeForDisconnectNotification2(Binding: c_void_p, hEvent: c_void_p, SubscriptionId: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUnsubscribeForDisconnectNotification(Binding: c_void_p, SubscriptionId: Guid) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfSpec: c_void_p, BindingVec: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), ObjectUuidVec: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfSpec: c_void_p, ObjectUuidVec: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfSpec: c_void_p, BindingVec: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), ObjectUuidVec: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfSpec: c_void_p, ObjectUuidVec: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportPnPA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfSpec: c_void_p, ObjectVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportPnPA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfSpec: c_void_p, ObjectVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportPnPW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfSpec: c_void_p, ObjectVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportPnPW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfSpec: c_void_p, ObjectVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupBeginA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfSpec: c_void_p, ObjUuid: POINTER(Guid), BindingMaxCount: UInt32, LookupContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupBeginW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfSpec: c_void_p, ObjUuid: POINTER(Guid), BindingMaxCount: UInt32, LookupContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupNext(LookupContext: c_void_p, BindingVec: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupDone(LookupContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupDeleteA(GroupNameSyntax: Windows.Win32.System.Rpc.GROUP_NAME_SYNTAX, GroupName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrAddA(GroupNameSyntax: UInt32, GroupName: c_char_p_no, MemberNameSyntax: UInt32, MemberName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrRemoveA(GroupNameSyntax: UInt32, GroupName: c_char_p_no, MemberNameSyntax: UInt32, MemberName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqBeginA(GroupNameSyntax: UInt32, GroupName: c_char_p_no, MemberNameSyntax: UInt32, InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqNextA(InquiryContext: c_void_p, MemberName: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupDeleteW(GroupNameSyntax: Windows.Win32.System.Rpc.GROUP_NAME_SYNTAX, GroupName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrAddW(GroupNameSyntax: UInt32, GroupName: POINTER(UInt16), MemberNameSyntax: UInt32, MemberName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrRemoveW(GroupNameSyntax: UInt32, GroupName: POINTER(UInt16), MemberNameSyntax: UInt32, MemberName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqBeginW(GroupNameSyntax: UInt32, GroupName: POINTER(UInt16), MemberNameSyntax: UInt32, InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqNextW(InquiryContext: c_void_p, MemberName: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqDone(InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileDeleteA(ProfileNameSyntax: UInt32, ProfileName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltAddA(ProfileNameSyntax: UInt32, ProfileName: c_char_p_no, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), MemberNameSyntax: UInt32, MemberName: c_char_p_no, Priority: UInt32, Annotation: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltRemoveA(ProfileNameSyntax: UInt32, ProfileName: c_char_p_no, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), MemberNameSyntax: UInt32, MemberName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqBeginA(ProfileNameSyntax: UInt32, ProfileName: c_char_p_no, InquiryType: UInt32, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), VersOption: UInt32, MemberNameSyntax: UInt32, MemberName: c_char_p_no, InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqNextA(InquiryContext: c_void_p, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), MemberName: POINTER(c_char_p_no), Priority: POINTER(UInt32), Annotation: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileDeleteW(ProfileNameSyntax: UInt32, ProfileName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltAddW(ProfileNameSyntax: UInt32, ProfileName: POINTER(UInt16), IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), MemberNameSyntax: UInt32, MemberName: POINTER(UInt16), Priority: UInt32, Annotation: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltRemoveW(ProfileNameSyntax: UInt32, ProfileName: POINTER(UInt16), IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), MemberNameSyntax: UInt32, MemberName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqBeginW(ProfileNameSyntax: UInt32, ProfileName: POINTER(UInt16), InquiryType: UInt32, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), VersOption: UInt32, MemberNameSyntax: UInt32, MemberName: POINTER(UInt16), InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqNextW(InquiryContext: c_void_p, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), MemberName: POINTER(POINTER(UInt16)), Priority: POINTER(UInt32), Annotation: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqDone(InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqBeginA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqBeginW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqNext(InquiryContext: c_void_p, ObjUuid: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqDone(InquiryContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryExpandNameA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, ExpandedName: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtBindingUnexportA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), VersOption: UInt32, ObjectUuidVec: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryCreateA(EntryNameSyntax: UInt32, EntryName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryDeleteA(EntryNameSyntax: UInt32, EntryName: c_char_p_no) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryInqIfIdsA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfIdVec: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtHandleSetExpAge(NsHandle: c_void_p, ExpirationAge: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtInqExpAge(ExpirationAge: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtSetExpAge(ExpirationAge: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryExpandNameW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), ExpandedName: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtBindingUnexportW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head), VersOption: UInt32, ObjectUuidVec: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryCreateW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryDeleteW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryInqIfIdsW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfIdVec: POINTER(POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR_head))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportBeginA(EntryNameSyntax: UInt32, EntryName: c_char_p_no, IfSpec: c_void_p, ObjUuid: POINTER(Guid), ImportContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportBeginW(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), IfSpec: c_void_p, ObjUuid: POINTER(Guid), ImportContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportNext(ImportContext: c_void_p, Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportDone(ImportContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingSelect(BindingVec: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head), Binding: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncRegisterInfo(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncInitializeHandle(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head), Size: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncGetCallStatus(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncCompleteCall(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head), Reply: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncAbortCall(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head), ExceptionCode: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncCancelCall(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head), fAbort: Windows.Win32.Foundation.BOOL) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorStartEnumeration(EnumHandle: POINTER(Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorGetNextRecord(EnumHandle: POINTER(Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE_head), CopyStrings: Windows.Win32.Foundation.BOOL, ErrorInfo: POINTER(Windows.Win32.System.Rpc.RPC_EXTENDED_ERROR_INFO_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorEndEnumeration(EnumHandle: POINTER(Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorResetEnumeration(EnumHandle: POINTER(Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorGetNumberOfRecords(EnumHandle: POINTER(Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE_head), Records: POINTER(Int32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorSaveErrorInfo(EnumHandle: POINTER(Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE_head), ErrorBlob: POINTER(c_void_p), BlobSize: POINTER(UIntPtr)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorLoadErrorInfo(ErrorBlob: c_void_p, BlobSize: UIntPtr, EnumHandle: POINTER(Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorAddRecord(ErrorInfo: POINTER(Windows.Win32.System.Rpc.RPC_EXTENDED_ERROR_INFO_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorClearInformation() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcGetAuthorizationContextForClient(ClientBinding: c_void_p, ImpersonateOnReturn: Windows.Win32.Foundation.BOOL, Reserved1: c_void_p, pExpirationTime: POINTER(Int64), Reserved2: Windows.Win32.Foundation.LUID, Reserved3: UInt32, Reserved4: c_void_p, pAuthzClientContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcFreeAuthorizationContext(pAuthzClientContext: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsContextLockExclusive(ServerBindingHandle: c_void_p, UserContext: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsContextLockShared(ServerBindingHandle: c_void_p, UserContext: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqCallAttributesW(ClientBinding: c_void_p, RpcCallAttributes: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqCallAttributesA(ClientBinding: c_void_p, RpcCallAttributes: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerSubscribeForNotification(Binding: c_void_p, Notification: Windows.Win32.System.Rpc.RPC_NOTIFICATIONS, NotificationType: Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES, NotificationInfo: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_NOTIFICATION_INFO_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUnsubscribeForNotification(Binding: c_void_p, Notification: Windows.Win32.System.Rpc.RPC_NOTIFICATIONS, NotificationsQueued: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingBind(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head), Binding: c_void_p, IfSpec: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingUnbind(Binding: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcAsyncSetHandle(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcAsyncAbortCall(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head), ExceptionCode: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcExceptionFilter(ExceptionCode: UInt32) -> Int32: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqClientTokenAttributes(Binding: c_void_p, TokenId: POINTER(Windows.Win32.Foundation.LUID_head), AuthenticationId: POINTER(Windows.Win32.Foundation.LUID_head), ModifiedId: POINTER(Windows.Win32.Foundation.LUID_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def I_RpcNsGetBuffer(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def I_RpcNsSendReceive(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), Handle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def I_RpcNsRaiseException(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), Status: Windows.Win32.System.Rpc.RPC_STATUS) -> Void: ...
@winfunctype('RPCNS4.dll')
def I_RpcReBindBuffer(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NDRCContextBinding(CContext: IntPtr) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def NDRCContextMarshall(CContext: IntPtr, pBuff: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRCContextUnmarshall(pCContext: POINTER(IntPtr), hBinding: c_void_p, pBuff: c_void_p, DataRepresentation: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextMarshall(CContext: POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head), pBuff: c_void_p, userRunDownIn: Windows.Win32.System.Rpc.NDR_RUNDOWN) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextUnmarshall(pBuff: c_void_p, DataRepresentation: UInt32) -> POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head): ...
@winfunctype('RPCRT4.dll')
def NDRSContextMarshallEx(BindingHandle: c_void_p, CContext: POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head), pBuff: c_void_p, userRunDownIn: Windows.Win32.System.Rpc.NDR_RUNDOWN) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextMarshall2(BindingHandle: c_void_p, CContext: POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head), pBuff: c_void_p, userRunDownIn: Windows.Win32.System.Rpc.NDR_RUNDOWN, CtxGuard: c_void_p, Flags: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextUnmarshallEx(BindingHandle: c_void_p, pBuff: c_void_p, DataRepresentation: UInt32) -> POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head): ...
@winfunctype('RPCRT4.dll')
def NDRSContextUnmarshall2(BindingHandle: c_void_p, pBuff: c_void_p, DataRepresentation: UInt32, CtxGuard: c_void_p, Flags: UInt32) -> POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head): ...
@winfunctype('RPCRT4.dll')
def RpcSsDestroyClientContext(ContextHandle: POINTER(c_void_p)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleTypeMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, FormatChar: Byte) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPointerMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrClientContextMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ContextHandle: IntPtr, fCheck: Int32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerContextMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ContextHandle: POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head), RundownRoutine: Windows.Win32.System.Rpc.NDR_RUNDOWN) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerContextNewMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ContextHandle: POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head), RundownRoutine: Windows.Win32.System.Rpc.NDR_RUNDOWN, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleTypeUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, FormatChar: Byte) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRangeUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrCorrelationInitialize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_void_p, CacheSize: UInt32, flags: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrCorrelationPass(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrCorrelationFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPointerUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_char_p_no), pFormat: c_char_p_no, fMustAlloc: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrClientContextUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pContextHandle: POINTER(IntPtr), BindHandle: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerContextUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head): ...
@winfunctype('RPCRT4.dll')
def NdrContextHandleInitialize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head): ...
@winfunctype('RPCRT4.dll')
def NdrServerContextNewUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head): ...
@winfunctype('RPCRT4.dll')
def NdrPointerBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrContextHandleSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPointerMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerMemorySize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrPointerFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerFree(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_char_p_no, pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConvert2(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no, NumberParams: Int32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConvert(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalSimpleTypeConvert(pFlags: POINTER(UInt32), pBuffer: c_char_p_no, FormatChar: Byte) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrClientInitializeNew(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), ProcNum: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializeNew(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head)) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializePartial(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), RequestedBufferSize: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrClientInitialize(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), ProcNum: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerInitialize(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head)) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializeUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializeMarshall(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrGetBuffer(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), BufferLength: UInt32, Handle: c_void_p) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrNsGetBuffer(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), BufferLength: UInt32, Handle: c_void_p) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrSendReceive(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pBufferEnd: c_char_p_no) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrNsSendReceive(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pBufferEnd: c_char_p_no, pAutoHandle: POINTER(c_void_p)) -> c_char_p_no: ...
@winfunctype('RPCRT4.dll')
def NdrFreeBuffer(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrGetDcomProtocolVersion(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pVersion: POINTER(Windows.Win32.System.Rpc.RPC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('RPCRT4.dll')
def NdrClientCall2(pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormat: c_char_p_no) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll')
def NdrAsyncClientCall(pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormat: c_char_p_no) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll')
def NdrDcomAsyncClientCall(pStubDescriptor: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormat: c_char_p_no) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def NdrAsyncServerCall(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrDcomAsyncStubCall(pThis: Windows.Win32.System.Com.IRpcStubBuffer_head, pChannel: Windows.Win32.System.Com.IRpcChannelBuffer_head, pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrStubCall2(pThis: c_void_p, pChannel: c_void_p, pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrServerCall2(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMapCommAndFaultStatus(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pCommStatus: POINTER(UInt32), pFaultStatus: POINTER(UInt32), Status: Windows.Win32.System.Rpc.RPC_STATUS) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsAllocate(Size: UIntPtr) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def RpcSsDisableAllocate() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsEnableAllocate() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsFree(NodeToFree: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsGetThreadHandle() -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def RpcSsSetClientAllocFree(ClientAlloc: Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: Windows.Win32.System.Rpc.RPC_CLIENT_FREE) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsSetThreadHandle(Id: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsSwapClientAllocFree(ClientAlloc: Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: Windows.Win32.System.Rpc.RPC_CLIENT_FREE, OldClientAlloc: POINTER(Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC), OldClientFree: POINTER(Windows.Win32.System.Rpc.RPC_CLIENT_FREE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSmAllocate(Size: UIntPtr, pStatus: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def RpcSmClientFree(pNodeToFree: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmDestroyClientContext(ContextHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmDisableAllocate() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmEnableAllocate() -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmFree(NodeToFree: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmGetThreadHandle(pStatus: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def RpcSmSetClientAllocFree(ClientAlloc: Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: Windows.Win32.System.Rpc.RPC_CLIENT_FREE) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmSetThreadHandle(Id: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmSwapClientAllocFree(ClientAlloc: Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: Windows.Win32.System.Rpc.RPC_CLIENT_FREE, OldClientAlloc: POINTER(Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC), OldClientFree: POINTER(Windows.Win32.System.Rpc.RPC_CLIENT_FREE)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsEnableAllocate(pMessage: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsDisableAllocate(pMessage: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSmSetClientToOsf(pMessage: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSmClientAllocate(Size: UIntPtr) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSmClientFree(NodeToFree: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsDefaultAllocate(Size: UIntPtr) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsDefaultFree(NodeToFree: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrFullPointerXlatInit(NumberOfPointers: UInt32, XlatSide: Windows.Win32.System.Rpc.XLAT_SIDE) -> POINTER(Windows.Win32.System.Rpc.FULL_PTR_XLAT_TABLES_head): ...
@winfunctype('RPCRT4.dll')
def NdrFullPointerXlatFree(pXlatTables: POINTER(Windows.Win32.System.Rpc.FULL_PTR_XLAT_TABLES_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrAllocate(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), Len: UIntPtr) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def NdrClearOutParameters(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pFormat: c_char_p_no, ArgAddr: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrOleAllocate(Size: UIntPtr) -> c_void_p: ...
@winfunctype('RPCRT4.dll')
def NdrOleFree(NodeToFree: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrGetUserMarshalInfo(pFlags: POINTER(UInt32), InformationLevel: UInt32, pMarshalInfo: POINTER(Windows.Win32.System.Rpc.NDR_USER_MARSHAL_INFO_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NdrCreateServerInterfaceFromStub(pStub: Windows.Win32.System.Com.IRpcStubBuffer_head, pServerIf: POINTER(Windows.Win32.System.Rpc.RPC_SERVER_INTERFACE_head)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@cfunctype('RPCRT4.dll')
def NdrClientCall3(pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), nProcNum: UInt32, pReturnValue: c_void_p) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll')
def Ndr64AsyncClientCall(pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), nProcNum: UInt32, pReturnValue: c_void_p) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll')
def Ndr64DcomAsyncClientCall(pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), nProcNum: UInt32, pReturnValue: c_void_p) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def Ndr64AsyncServerCall64(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def Ndr64AsyncServerCallAll(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def Ndr64DcomAsyncStubCall(pThis: Windows.Win32.System.Com.IRpcStubBuffer_head, pChannel: Windows.Win32.System.Com.IRpcChannelBuffer_head, pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrStubCall3(pThis: c_void_p, pChannel: c_void_p, pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrServerCallAll(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerCallNdr64(pRpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreClientMarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreServerUnmarshall(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_void_p)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreClientBufferSize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), pMemory: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreServerInitialize(pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head), ppMemory: POINTER(c_void_p), pFormat: c_char_p_no) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcUserFree(AsyncHandle: c_void_p, pBuffer: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def MesEncodeIncrementalHandleCreate(UserState: c_void_p, AllocFn: Windows.Win32.System.Rpc.MIDL_ES_ALLOC, WriteFn: Windows.Win32.System.Rpc.MIDL_ES_WRITE, pHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesDecodeIncrementalHandleCreate(UserState: c_void_p, ReadFn: Windows.Win32.System.Rpc.MIDL_ES_READ, pHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesIncrementalHandleReset(Handle: c_void_p, UserState: c_void_p, AllocFn: Windows.Win32.System.Rpc.MIDL_ES_ALLOC, WriteFn: Windows.Win32.System.Rpc.MIDL_ES_WRITE, ReadFn: Windows.Win32.System.Rpc.MIDL_ES_READ, Operation: Windows.Win32.System.Rpc.MIDL_ES_CODE) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesEncodeFixedBufferHandleCreate(pBuffer: Windows.Win32.Foundation.PSTR, BufferSize: UInt32, pEncodedSize: POINTER(UInt32), pHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesEncodeDynBufferHandleCreate(pBuffer: POINTER(POINTER(SByte)), pEncodedSize: POINTER(UInt32), pHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesDecodeBufferHandleCreate(Buffer: Windows.Win32.Foundation.PSTR, BufferSize: UInt32, pHandle: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesBufferHandleReset(Handle: c_void_p, HandleStyle: UInt32, Operation: Windows.Win32.System.Rpc.MIDL_ES_CODE, pBuffer: POINTER(POINTER(SByte)), BufferSize: UInt32, pEncodedSize: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesHandleFree(Handle: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesInqProcEncodingId(Handle: c_void_p, pInterfaceId: POINTER(Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER_head), pProcNum: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeAlignSize(param0: c_void_p) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeDecode(Handle: c_void_p, pObject: c_void_p, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeEncode(Handle: c_void_p, pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pObject: c_void_p, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeAlignSize(Handle: c_void_p, pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no, pObject: c_void_p) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeEncode(Handle: c_void_p, pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no, pObject: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeDecode(Handle: c_void_p, pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no, pObject: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeAlignSize2(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no, pObject: c_void_p) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeEncode2(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no, pObject: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeDecode2(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no, pObject: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeFree2(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no, pObject: c_void_p) -> Void: ...
@cfunctype('RPCRT4.dll')
def NdrMesProcEncodeDecode(Handle: c_void_p, pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no) -> Void: ...
@cfunctype('RPCRT4.dll')
def NdrMesProcEncodeDecode2(Handle: c_void_p, pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head), pFormatString: c_char_p_no) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeAlignSize3(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: c_void_p) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeEncode3(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeDecode3(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: c_void_p) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeFree3(Handle: c_void_p, pPicklingInfo: POINTER(Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO_head), pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: c_void_p) -> Void: ...
@cfunctype('RPCRT4.dll')
def NdrMesProcEncodeDecode3(Handle: c_void_p, pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), nProcNum: UInt32, pReturnValue: c_void_p) -> Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeDecodeAll(Handle: c_void_p, pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), pObject: c_void_p, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeEncodeAll(Handle: c_void_p, pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head), pObject: c_void_p, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeAlignSizeAll(Handle: c_void_p, pProxyInfo: POINTER(Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO_head)) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def RpcCertGeneratePrincipalNameW(Context: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), Flags: UInt32, pBuffer: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcCertGeneratePrincipalNameA(Context: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), Flags: UInt32, pBuffer: POINTER(c_char_p_no)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
class BinaryParam(Structure):
    Buffer: c_void_p
    Size: Int16
class CLIENT_CALL_RETURN(Union):
    Pointer: c_void_p
    Simple: IntPtr
class COMM_FAULT_OFFSETS(Structure):
    CommOffset: Int16
    FaultOffset: Int16
@winfunctype_pointer
def CS_TAG_GETTING_ROUTINE(hBinding: c_void_p, fServerSide: Int32, pulSendingTag: POINTER(UInt32), pulDesiredReceivingTag: POINTER(UInt32), pulReceivingTag: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_FROM_NETCS_ROUTINE(hBinding: c_void_p, ulNetworkCodeSet: UInt32, pNetworkData: c_char_p_no, ulNetworkDataLength: UInt32, ulLocalBufferSize: UInt32, pLocalData: c_void_p, pulLocalDataLength: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_LOCAL_SIZE_ROUTINE(hBinding: c_void_p, ulNetworkCodeSet: UInt32, ulNetworkBufferSize: UInt32, conversionType: POINTER(Windows.Win32.System.Rpc.IDL_CS_CONVERT), pulLocalBufferSize: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_NET_SIZE_ROUTINE(hBinding: c_void_p, ulNetworkCodeSet: UInt32, ulLocalBufferSize: UInt32, conversionType: POINTER(Windows.Win32.System.Rpc.IDL_CS_CONVERT), pulNetworkBufferSize: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_TO_NETCS_ROUTINE(hBinding: c_void_p, ulNetworkCodeSet: UInt32, pLocalData: c_void_p, ulLocalDataLength: UInt32, pNetworkData: c_char_p_no, pulNetworkDataLength: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def EXPR_EVAL(param0: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
EXPR_TOKEN = Int32
FC_EXPR_START: EXPR_TOKEN = 0
FC_EXPR_ILLEGAL: EXPR_TOKEN = 0
FC_EXPR_CONST32: EXPR_TOKEN = 1
FC_EXPR_CONST64: EXPR_TOKEN = 2
FC_EXPR_VAR: EXPR_TOKEN = 3
FC_EXPR_OPER: EXPR_TOKEN = 4
FC_EXPR_NOOP: EXPR_TOKEN = 5
FC_EXPR_END: EXPR_TOKEN = 6
ExtendedErrorParamTypes = Int32
ExtendedErrorParamTypes_eeptAnsiString: ExtendedErrorParamTypes = 1
ExtendedErrorParamTypes_eeptUnicodeString: ExtendedErrorParamTypes = 2
ExtendedErrorParamTypes_eeptLongVal: ExtendedErrorParamTypes = 3
ExtendedErrorParamTypes_eeptShortVal: ExtendedErrorParamTypes = 4
ExtendedErrorParamTypes_eeptPointerVal: ExtendedErrorParamTypes = 5
ExtendedErrorParamTypes_eeptNone: ExtendedErrorParamTypes = 6
ExtendedErrorParamTypes_eeptBinary: ExtendedErrorParamTypes = 7
class FULL_PTR_XLAT_TABLES(Structure):
    RefIdToPointer: c_void_p
    PointerToRefId: c_void_p
    NextRefId: UInt32
    XlatSide: Windows.Win32.System.Rpc.XLAT_SIDE
class GENERIC_BINDING_INFO(Structure):
    pObj: c_void_p
    Size: UInt32
    pfnBind: Windows.Win32.System.Rpc.GENERIC_BINDING_ROUTINE
    pfnUnbind: Windows.Win32.System.Rpc.GENERIC_UNBIND_ROUTINE
@winfunctype_pointer
def GENERIC_BINDING_ROUTINE(param0: c_void_p) -> c_void_p: ...
class GENERIC_BINDING_ROUTINE_PAIR(Structure):
    pfnBind: Windows.Win32.System.Rpc.GENERIC_BINDING_ROUTINE
    pfnUnbind: Windows.Win32.System.Rpc.GENERIC_UNBIND_ROUTINE
@winfunctype_pointer
def GENERIC_UNBIND_ROUTINE(param0: c_void_p, param1: c_char_p_no) -> Void: ...
GROUP_NAME_SYNTAX = UInt32
RPC_C_NS_SYNTAX_DEFAULT: GROUP_NAME_SYNTAX = 0
RPC_C_NS_SYNTAX_DCE: GROUP_NAME_SYNTAX = 3
IDL_CS_CONVERT = Int32
IDL_CS_NO_CONVERT: IDL_CS_CONVERT = 0
IDL_CS_IN_PLACE_CONVERT: IDL_CS_CONVERT = 1
IDL_CS_NEW_BUFFER_CONVERT: IDL_CS_CONVERT = 2
@winfunctype_pointer
def I_RpcFreeCalloutStateFn(CallOutState: POINTER(Windows.Win32.System.Rpc.RDR_CALLOUT_STATE_head)) -> Void: ...
@winfunctype_pointer
def I_RpcPerformCalloutFn(Context: c_void_p, CallOutState: POINTER(Windows.Win32.System.Rpc.RDR_CALLOUT_STATE_head), Stage: Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
class I_RpcProxyCallbackInterface(Structure):
    IsValidMachineFn: Windows.Win32.System.Rpc.I_RpcProxyIsValidMachineFn
    GetClientAddressFn: Windows.Win32.System.Rpc.I_RpcProxyGetClientAddressFn
    GetConnectionTimeoutFn: Windows.Win32.System.Rpc.I_RpcProxyGetConnectionTimeoutFn
    PerformCalloutFn: Windows.Win32.System.Rpc.I_RpcPerformCalloutFn
    FreeCalloutStateFn: Windows.Win32.System.Rpc.I_RpcFreeCalloutStateFn
    GetClientSessionAndResourceUUIDFn: Windows.Win32.System.Rpc.I_RpcProxyGetClientSessionAndResourceUUID
    ProxyFilterIfFn: Windows.Win32.System.Rpc.I_RpcProxyFilterIfFn
    RpcProxyUpdatePerfCounterFn: Windows.Win32.System.Rpc.I_RpcProxyUpdatePerfCounterFn
    RpcProxyUpdatePerfCounterBackendServerFn: Windows.Win32.System.Rpc.I_RpcProxyUpdatePerfCounterBackendServerFn
@winfunctype_pointer
def I_RpcProxyFilterIfFn(Context: c_void_p, IfUuid: POINTER(Guid), IfMajorVersion: UInt16, fAllow: POINTER(Int32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyGetClientAddressFn(Context: c_void_p, Buffer: Windows.Win32.Foundation.PSTR, BufferLength: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyGetClientSessionAndResourceUUID(Context: c_void_p, SessionIdPresent: POINTER(Int32), SessionId: POINTER(Guid), ResourceIdPresent: POINTER(Int32), ResourceId: POINTER(Guid)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyGetConnectionTimeoutFn(ConnectionTimeout: POINTER(UInt32)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyIsValidMachineFn(Machine: POINTER(UInt16), DotMachine: POINTER(UInt16), PortNumber: UInt32) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyUpdatePerfCounterBackendServerFn(MachineName: POINTER(UInt16), IsConnectEvent: Int32) -> Void: ...
@winfunctype_pointer
def I_RpcProxyUpdatePerfCounterFn(Counter: Windows.Win32.System.Rpc.RpcPerfCounters, ModifyTrend: Int32, Size: UInt32) -> Void: ...
LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION = Int32
LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION_MarshalDirectionMarshal: LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION = 0
LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION_MarshalDirectionUnmarshal: LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION = 1
class MALLOC_FREE_STRUCT(Structure):
    pfnAllocate: IntPtr
    pfnFree: IntPtr
@winfunctype_pointer
def MIDL_ES_ALLOC(state: c_void_p, pbuffer: POINTER(POINTER(SByte)), psize: POINTER(UInt32)) -> Void: ...
MIDL_ES_CODE = Int32
MES_ENCODE: MIDL_ES_CODE = 0
MES_DECODE: MIDL_ES_CODE = 1
MES_ENCODE_NDR64: MIDL_ES_CODE = 2
MIDL_ES_HANDLE_STYLE = Int32
MES_INCREMENTAL_HANDLE: MIDL_ES_HANDLE_STYLE = 0
MES_FIXED_BUFFER_HANDLE: MIDL_ES_HANDLE_STYLE = 1
MES_DYNAMIC_BUFFER_HANDLE: MIDL_ES_HANDLE_STYLE = 2
@winfunctype_pointer
def MIDL_ES_READ(state: c_void_p, pbuffer: POINTER(POINTER(SByte)), psize: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def MIDL_ES_WRITE(state: c_void_p, buffer: Windows.Win32.Foundation.PSTR, size: UInt32) -> Void: ...
class MIDL_FORMAT_STRING(Structure):
    Pad: Int16
    Format: Byte * 1
class MIDL_INTERCEPTION_INFO(Structure):
    Version: UInt32
    ProcString: c_char_p_no
    ProcFormatOffsetTable: POINTER(UInt16)
    ProcCount: UInt32
    TypeString: c_char_p_no
class MIDL_INTERFACE_METHOD_PROPERTIES(Structure):
    MethodCount: UInt16
    MethodProperties: POINTER(POINTER(Windows.Win32.System.Rpc.MIDL_METHOD_PROPERTY_MAP_head))
class MIDL_METHOD_PROPERTY(Structure):
    Id: UInt32
    Value: UIntPtr
class MIDL_METHOD_PROPERTY_MAP(Structure):
    Count: UInt32
    Properties: POINTER(Windows.Win32.System.Rpc.MIDL_METHOD_PROPERTY_head)
class MIDL_SERVER_INFO(Structure):
    pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head)
    DispatchTable: POINTER(Windows.Win32.System.Rpc.SERVER_ROUTINE)
    ProcString: c_char_p_no
    FmtStringOffset: POINTER(UInt16)
    ThunkTable: POINTER(Windows.Win32.System.Rpc.STUB_THUNK)
    pTransferSyntax: POINTER(Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER_head)
    nCount: UIntPtr
    pSyntaxInfo: POINTER(Windows.Win32.System.Rpc.MIDL_SYNTAX_INFO_head)
class MIDL_STUBLESS_PROXY_INFO(Structure):
    pStubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head)
    ProcFormatString: c_char_p_no
    FormatStringOffset: POINTER(UInt16)
    pTransferSyntax: POINTER(Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER_head)
    nCount: UIntPtr
    pSyntaxInfo: POINTER(Windows.Win32.System.Rpc.MIDL_SYNTAX_INFO_head)
class MIDL_STUB_DESC(Structure):
    RpcInterfaceInformation: c_void_p
    pfnAllocate: IntPtr
    pfnFree: IntPtr
    IMPLICIT_HANDLE_INFO: _IMPLICIT_HANDLE_INFO_e__Union
    apfnNdrRundownRoutines: POINTER(Windows.Win32.System.Rpc.NDR_RUNDOWN)
    aGenericBindingRoutinePairs: POINTER(Windows.Win32.System.Rpc.GENERIC_BINDING_ROUTINE_PAIR_head)
    apfnExprEval: POINTER(Windows.Win32.System.Rpc.EXPR_EVAL)
    aXmitQuintuple: POINTER(Windows.Win32.System.Rpc.XMIT_ROUTINE_QUINTUPLE_head)
    pFormatTypes: c_char_p_no
    fCheckBounds: Int32
    Version: UInt32
    pMallocFreeStruct: POINTER(Windows.Win32.System.Rpc.MALLOC_FREE_STRUCT_head)
    MIDLVersion: Int32
    CommFaultOffsets: POINTER(Windows.Win32.System.Rpc.COMM_FAULT_OFFSETS_head)
    aUserMarshalQuadruple: POINTER(Windows.Win32.System.Rpc.USER_MARSHAL_ROUTINE_QUADRUPLE_head)
    NotifyRoutineTable: POINTER(Windows.Win32.System.Rpc.NDR_NOTIFY_ROUTINE)
    mFlags: UIntPtr
    CsRoutineTables: POINTER(Windows.Win32.System.Rpc.NDR_CS_ROUTINES_head)
    ProxyServerInfo: c_void_p
    pExprInfo: POINTER(Windows.Win32.System.Rpc.NDR_EXPR_DESC_head)
    class _IMPLICIT_HANDLE_INFO_e__Union(Union):
        pAutoHandle: POINTER(c_void_p)
        pPrimitiveHandle: POINTER(c_void_p)
        pGenericBindingInfo: POINTER(Windows.Win32.System.Rpc.GENERIC_BINDING_INFO_head)
class MIDL_STUB_MESSAGE(Structure):
    RpcMsg: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)
    Buffer: c_char_p_no
    BufferStart: c_char_p_no
    BufferEnd: c_char_p_no
    BufferMark: c_char_p_no
    BufferLength: UInt32
    MemorySize: UInt32
    Memory: c_char_p_no
    IsClient: Byte
    Pad: Byte
    uFlags2: UInt16
    ReuseBuffer: Int32
    pAllocAllNodesContext: POINTER(Windows.Win32.System.Rpc.NDR_ALLOC_ALL_NODES_CONTEXT_head)
    pPointerQueueState: POINTER(Windows.Win32.System.Rpc.NDR_POINTER_QUEUE_STATE_head)
    IgnoreEmbeddedPointers: Int32
    PointerBufferMark: c_char_p_no
    CorrDespIncrement: Byte
    uFlags: Byte
    UniquePtrCount: UInt16
    MaxCount: UIntPtr
    Offset: UInt32
    ActualCount: UInt32
    pfnAllocate: IntPtr
    pfnFree: IntPtr
    StackTop: c_char_p_no
    pPresentedType: c_char_p_no
    pTransmitType: c_char_p_no
    SavedHandle: c_void_p
    StubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head)
    FullPtrXlatTables: POINTER(Windows.Win32.System.Rpc.FULL_PTR_XLAT_TABLES_head)
    FullPtrRefId: UInt32
    PointerLength: UInt32
    _bitfield: Int32
    dwDestContext: UInt32
    pvDestContext: c_void_p
    SavedContextHandles: POINTER(POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head))
    ParamNumber: Int32
    pRpcChannelBuffer: Windows.Win32.System.Com.IRpcChannelBuffer_head
    pArrayInfo: POINTER(Windows.Win32.System.Rpc.ARRAY_INFO_head)
    SizePtrCountArray: POINTER(UInt32)
    SizePtrOffsetArray: POINTER(UInt32)
    SizePtrLengthArray: POINTER(UInt32)
    pArgQueue: c_void_p
    dwStubPhase: UInt32
    LowStackMark: c_void_p
    pAsyncMsg: POINTER(Windows.Win32.System.Rpc._NDR_ASYNC_MESSAGE_head)
    pCorrInfo: POINTER(Windows.Win32.System.Rpc._NDR_CORRELATION_INFO_head)
    pCorrMemory: c_char_p_no
    pMemoryList: c_void_p
    pCSInfo: IntPtr
    ConformanceMark: c_char_p_no
    VarianceMark: c_char_p_no
    Unused: IntPtr
    pContext: POINTER(Windows.Win32.System.Rpc._NDR_PROC_CONTEXT_head)
    ContextHandleHash: c_void_p
    pUserMarshalList: c_void_p
    Reserved51_3: IntPtr
    Reserved51_4: IntPtr
    Reserved51_5: IntPtr
class MIDL_SYNTAX_INFO(Structure):
    TransferSyntax: Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    DispatchTable: POINTER(Windows.Win32.System.Rpc.RPC_DISPATCH_TABLE_head)
    ProcString: c_char_p_no
    FmtStringOffset: POINTER(UInt16)
    TypeString: c_char_p_no
    aUserMarshalQuadruple: c_void_p
    pMethodProperties: POINTER(Windows.Win32.System.Rpc.MIDL_INTERFACE_METHOD_PROPERTIES_head)
    pReserved2: UIntPtr
class MIDL_TYPE_PICKLING_INFO(Structure):
    Version: UInt32
    Flags: UInt32
    Reserved: UIntPtr * 3
class MIDL_WINRT_TYPE_SERIALIZATION_INFO(Structure):
    Version: UInt32
    TypeFormatString: c_char_p_no
    FormatStringSize: UInt16
    TypeOffset: UInt16
    StubDesc: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_DESC_head)
class NDR64_ARRAY_ELEMENT_INFO(Structure):
    ElementMemSize: UInt32
    Element: c_void_p
class NDR64_ARRAY_FLAGS(Structure):
    _bitfield: Byte
class NDR64_BINDINGS(Union):
    Primitive: Windows.Win32.System.Rpc.NDR64_BIND_PRIMITIVE
    Generic: Windows.Win32.System.Rpc.NDR64_BIND_GENERIC
    Context: Windows.Win32.System.Rpc.NDR64_BIND_CONTEXT
class NDR64_BIND_AND_NOTIFY_EXTENSION(Structure):
    Binding: Windows.Win32.System.Rpc.NDR64_BIND_CONTEXT
    NotifyIndex: UInt16
class NDR64_BIND_CONTEXT(Structure):
    HandleType: Byte
    Flags: Byte
    StackOffset: UInt16
    RoutineIndex: Byte
    Ordinal: Byte
class NDR64_BIND_GENERIC(Structure):
    HandleType: Byte
    Flags: Byte
    StackOffset: UInt16
    RoutineIndex: Byte
    Size: Byte
class NDR64_BIND_PRIMITIVE(Structure):
    HandleType: Byte
    Flags: Byte
    StackOffset: UInt16
    Reserved: UInt16
class NDR64_BOGUS_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    NumberDims: Byte
    NumberElements: UInt32
    Element: c_void_p
class NDR64_BOGUS_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Reserve: Byte
    MemorySize: UInt32
    OriginalMemberLayout: c_void_p
    OriginalPointerLayout: c_void_p
    PointerLayout: c_void_p
class NDR64_BUFFER_ALIGN_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Reserved: UInt16
    Reserved2: UInt32
class NDR64_CONFORMANT_STRING_FORMAT(Structure):
    Header: Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
class NDR64_CONF_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    ElementSize: UInt32
    ConfDescriptor: c_void_p
class NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Dimensions: Byte
    MemorySize: UInt32
    OriginalMemberLayout: c_void_p
    OriginalPointerLayout: c_void_p
    PointerLayout: c_void_p
    ConfArrayDescription: c_void_p
class NDR64_CONF_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Reserve: Byte
    MemorySize: UInt32
    ArrayDescription: c_void_p
class NDR64_CONF_VAR_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    ElementSize: UInt32
    ConfDescriptor: c_void_p
    VarDescriptor: c_void_p
class NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT(Structure):
    FixedArrayFormat: Windows.Win32.System.Rpc.NDR64_BOGUS_ARRAY_HEADER_FORMAT
    ConfDescription: c_void_p
    VarDescription: c_void_p
    OffsetDescription: c_void_p
class NDR64_CONSTANT_IID_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved: UInt16
    Guid: Guid
class NDR64_CONTEXT_HANDLE_FLAGS(Structure):
    _bitfield: Byte
class NDR64_CONTEXT_HANDLE_FORMAT(Structure):
    FormatCode: Byte
    ContextFlags: Byte
    RundownRoutineIndex: Byte
    Ordinal: Byte
class NDR64_EMBEDDED_COMPLEX_FORMAT(Structure):
    FormatCode: Byte
    Reserve1: Byte
    Reserve2: UInt16
    Type: c_void_p
class NDR64_ENCAPSULATED_UNION(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Byte
    SwitchType: Byte
    MemoryOffset: UInt32
    MemorySize: UInt32
    Reserved: UInt32
class NDR64_EXPR_CONST32(Structure):
    ExprType: Byte
    Reserved: Byte
    Reserved1: UInt16
    ConstValue: UInt32
class NDR64_EXPR_CONST64(Structure):
    ExprType: Byte
    Reserved: Byte
    Reserved1: UInt16
    ConstValue: Int64
class NDR64_EXPR_NOOP(Structure):
    ExprType: Byte
    Size: Byte
    Reserved: UInt16
class NDR64_EXPR_OPERATOR(Structure):
    ExprType: Byte
    Operator: Byte
    CastType: Byte
    Reserved: Byte
class NDR64_EXPR_VAR(Structure):
    ExprType: Byte
    VarType: Byte
    Reserved: UInt16
    Offset: UInt32
class NDR64_FIXED_REPEAT_FORMAT(Structure):
    RepeatFormat: Windows.Win32.System.Rpc.NDR64_REPEAT_FORMAT
    Iterations: UInt32
    Reserved: UInt32
class NDR64_FIX_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    TotalSize: UInt32
class NDR64_IID_FLAGS(Structure):
    _bitfield: Byte
class NDR64_IID_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved: UInt16
    IIDDescriptor: c_void_p
class NDR64_MEMPAD_FORMAT(Structure):
    FormatCode: Byte
    Reserve1: Byte
    MemPad: UInt16
    Reserved2: UInt32
class NDR64_NON_CONFORMANT_STRING_FORMAT(Structure):
    Header: Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
    TotalSize: UInt32
class NDR64_NON_ENCAPSULATED_UNION(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Byte
    SwitchType: Byte
    MemorySize: UInt32
    Switch: c_void_p
    Reserved: UInt32
class NDR64_NO_REPEAT_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved1: UInt16
    Reserved2: UInt32
class NDR64_PARAM_FLAGS(Structure):
    _bitfield: UInt16
class NDR64_PARAM_FORMAT(Structure):
    Type: c_void_p
    Attributes: Windows.Win32.System.Rpc.NDR64_PARAM_FLAGS
    Reserved: UInt16
    StackOffset: UInt32
class NDR64_PIPE_FLAGS(Structure):
    _bitfield: Byte
class NDR64_PIPE_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Alignment: Byte
    Reserved: Byte
    Type: c_void_p
    MemorySize: UInt32
    BufferSize: UInt32
class NDR64_POINTER_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved: UInt16
    Pointee: c_void_p
class NDR64_POINTER_INSTANCE_HEADER_FORMAT(Structure):
    Offset: UInt32
    Reserved: UInt32
class NDR64_POINTER_REPEAT_FLAGS(Structure):
    _bitfield: Byte
class NDR64_PROC_FLAGS(Structure):
    _bitfield: UInt32
class NDR64_PROC_FORMAT(Structure):
    Flags: UInt32
    StackSize: UInt32
    ConstantClientBufferSize: UInt32
    ConstantServerBufferSize: UInt32
    RpcFlags: UInt16
    FloatDoubleMask: UInt16
    NumberOfParams: UInt16
    ExtensionSize: UInt16
class NDR64_RANGED_STRING_FORMAT(Structure):
    Header: Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
    Reserved: UInt32
    Min: UInt64
    Max: UInt64
class NDR64_RANGE_FORMAT(Structure):
    FormatCode: Byte
    RangeType: Byte
    Reserved: UInt16
    MinValue: Int64
    MaxValue: Int64
class NDR64_RANGE_PIPE_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Alignment: Byte
    Reserved: Byte
    Type: c_void_p
    MemorySize: UInt32
    BufferSize: UInt32
    MinValue: UInt32
    MaxValue: UInt32
class NDR64_REPEAT_FORMAT(Structure):
    FormatCode: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_POINTER_REPEAT_FLAGS
    Reserved: UInt16
    Increment: UInt32
    OffsetToArray: UInt32
    NumberOfPointers: UInt32
class NDR64_RPC_FLAGS(Structure):
    _bitfield: UInt16
class NDR64_SIMPLE_MEMBER_FORMAT(Structure):
    FormatCode: Byte
    Reserved1: Byte
    Reserved2: UInt16
    Reserved3: UInt32
class NDR64_SIMPLE_REGION_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    RegionSize: UInt16
    Reserved: UInt32
class NDR64_SIZED_CONFORMANT_STRING_FORMAT(Structure):
    Header: Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
    SizeDescription: c_void_p
class NDR64_STRING_FLAGS(Structure):
    _bitfield: Byte
class NDR64_STRING_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_STRING_FLAGS
    ElementSize: UInt16
class NDR64_STRUCTURE_FLAGS(Structure):
    _bitfield: Byte
class NDR64_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Reserve: Byte
    MemorySize: UInt32
class NDR64_SYSTEM_HANDLE_FORMAT(Structure):
    FormatCode: Byte
    HandleType: Byte
    DesiredAccess: UInt32
class NDR64_TRANSMIT_AS_FLAGS(Structure):
    _bitfield: Byte
class NDR64_TRANSMIT_AS_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    RoutineIndex: UInt16
    TransmittedTypeWireAlignment: UInt16
    MemoryAlignment: UInt16
    PresentedTypeMemorySize: UInt32
    TransmittedTypeBufferSize: UInt32
    TransmittedType: c_void_p
class NDR64_TYPE_STRICT_CONTEXT_HANDLE(Structure):
    FormatCode: Byte
    RealFormatCode: Byte
    Reserved: UInt16
    Type: c_void_p
    CtxtFlags: UInt32
    CtxtID: UInt32
class NDR64_UNION_ARM(Structure):
    CaseValue: Int64
    Type: c_void_p
    Reserved: UInt32
class NDR64_UNION_ARM_SELECTOR(Structure):
    Reserved1: Byte
    Alignment: Byte
    Reserved2: UInt16
    Arms: UInt32
class NDR64_USER_MARSHAL_FLAGS(Structure):
    _bitfield: Byte
class NDR64_USER_MARSHAL_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    RoutineIndex: UInt16
    TransmittedTypeWireAlignment: UInt16
    MemoryAlignment: UInt16
    UserTypeMemorySize: UInt32
    TransmittedTypeBufferSize: UInt32
    TransmittedType: c_void_p
class NDR64_VAR_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    TotalSize: UInt32
    ElementSize: UInt32
    VarDescriptor: c_void_p
class NDR_ALLOC_ALL_NODES_CONTEXT(Structure):
    pass
class NDR_CS_ROUTINES(Structure):
    pSizeConvertRoutines: POINTER(Windows.Win32.System.Rpc.NDR_CS_SIZE_CONVERT_ROUTINES_head)
    pTagGettingRoutines: POINTER(Windows.Win32.System.Rpc.CS_TAG_GETTING_ROUTINE)
class NDR_CS_SIZE_CONVERT_ROUTINES(Structure):
    pfnNetSize: Windows.Win32.System.Rpc.CS_TYPE_NET_SIZE_ROUTINE
    pfnToNetCs: Windows.Win32.System.Rpc.CS_TYPE_TO_NETCS_ROUTINE
    pfnLocalSize: Windows.Win32.System.Rpc.CS_TYPE_LOCAL_SIZE_ROUTINE
    pfnFromNetCs: Windows.Win32.System.Rpc.CS_TYPE_FROM_NETCS_ROUTINE
class NDR_EXPR_DESC(Structure):
    pOffset: POINTER(UInt16)
    pFormatExpr: c_char_p_no
@winfunctype_pointer
def NDR_NOTIFY2_ROUTINE(flag: Byte) -> Void: ...
@winfunctype_pointer
def NDR_NOTIFY_ROUTINE() -> Void: ...
class NDR_POINTER_QUEUE_STATE(Structure):
    pass
@winfunctype_pointer
def NDR_RUNDOWN(context: c_void_p) -> Void: ...
class NDR_SCONTEXT(Structure):
    pad: c_void_p * 2
    userContext: c_void_p
class NDR_USER_MARSHAL_INFO(Structure):
    InformationLevel: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Level1: Windows.Win32.System.Rpc.NDR_USER_MARSHAL_INFO_LEVEL1
class NDR_USER_MARSHAL_INFO_LEVEL1(Structure):
    Buffer: c_void_p
    BufferSize: UInt32
    pfnAllocate: IntPtr
    pfnFree: IntPtr
    pRpcChannelBuffer: Windows.Win32.System.Com.IRpcChannelBuffer_head
    Reserved: UIntPtr * 5
@winfunctype_pointer
def PFN_RPCNOTIFICATION_ROUTINE(pAsync: POINTER(Windows.Win32.System.Rpc.RPC_ASYNC_STATE_head), Context: c_void_p, Event: Windows.Win32.System.Rpc.RPC_ASYNC_EVENT) -> Void: ...
PROXY_PHASE = Int32
PROXY_CALCSIZE: PROXY_PHASE = 0
PROXY_GETBUFFER: PROXY_PHASE = 1
PROXY_MARSHAL: PROXY_PHASE = 2
PROXY_SENDRECEIVE: PROXY_PHASE = 3
PROXY_UNMARSHAL: PROXY_PHASE = 4
@winfunctype_pointer
def PRPC_RUNDOWN(AssociationContext: c_void_p) -> Void: ...
class RDR_CALLOUT_STATE(Structure):
    LastError: Windows.Win32.System.Rpc.RPC_STATUS
    LastEEInfo: c_void_p
    LastCalledStage: Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE
    ServerName: POINTER(UInt16)
    ServerPort: POINTER(UInt16)
    RemoteUser: POINTER(UInt16)
    AuthType: POINTER(UInt16)
    ResourceTypePresent: Byte
    SessionIdPresent: Byte
    InterfacePresent: Byte
    ResourceType: Guid
    SessionId: Guid
    Interface: Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    CertContext: c_void_p
@winfunctype_pointer
def RPCLT_PDU_FILTER_FUNC(Buffer: c_void_p, BufferLength: UInt32, fDatagram: Int32) -> Void: ...
@winfunctype_pointer
def RPC_ADDRESS_CHANGE_FN(arg: c_void_p) -> Void: ...
RPC_ADDRESS_CHANGE_TYPE = Int32
PROTOCOL_NOT_LOADED: RPC_ADDRESS_CHANGE_TYPE = 1
PROTOCOL_LOADED: RPC_ADDRESS_CHANGE_TYPE = 2
PROTOCOL_ADDRESS_CHANGE: RPC_ADDRESS_CHANGE_TYPE = 3
RPC_ASYNC_EVENT = Int32
RPC_ASYNC_EVENT_RpcCallComplete: RPC_ASYNC_EVENT = 0
RPC_ASYNC_EVENT_RpcSendComplete: RPC_ASYNC_EVENT = 1
RPC_ASYNC_EVENT_RpcReceiveComplete: RPC_ASYNC_EVENT = 2
RPC_ASYNC_EVENT_RpcClientDisconnect: RPC_ASYNC_EVENT = 3
RPC_ASYNC_EVENT_RpcClientCancel: RPC_ASYNC_EVENT = 4
class RPC_ASYNC_NOTIFICATION_INFO(Union):
    APC: _APC_e__Struct
    IOC: _IOC_e__Struct
    IntPtr: _IntPtr_e__Struct
    hEvent: Windows.Win32.Foundation.HANDLE
    NotificationRoutine: Windows.Win32.System.Rpc.PFN_RPCNOTIFICATION_ROUTINE
    class _APC_e__Struct(Structure):
        NotificationRoutine: Windows.Win32.System.Rpc.PFN_RPCNOTIFICATION_ROUTINE
        hThread: Windows.Win32.Foundation.HANDLE
    class _IOC_e__Struct(Structure):
        hIOPort: Windows.Win32.Foundation.HANDLE
        dwNumberOfBytesTransferred: UInt32
        dwCompletionKey: UIntPtr
        lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)
    class _IntPtr_e__Struct(Structure):
        hWnd: Windows.Win32.Foundation.HWND
        Msg: UInt32
class RPC_ASYNC_STATE(Structure):
    Size: UInt32
    Signature: UInt32
    Lock: Int32
    Flags: UInt32
    StubInfo: c_void_p
    UserInfo: c_void_p
    RuntimeInfo: c_void_p
    Event: Windows.Win32.System.Rpc.RPC_ASYNC_EVENT
    NotificationType: Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES
    u: Windows.Win32.System.Rpc.RPC_ASYNC_NOTIFICATION_INFO
    Reserved: IntPtr * 4
@winfunctype_pointer
def RPC_AUTH_KEY_RETRIEVAL_FN(Arg: c_void_p, ServerPrincName: POINTER(UInt16), KeyVer: UInt32, Key: POINTER(c_void_p), Status: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> Void: ...
RPC_BINDING_HANDLE_OPTIONS_FLAGS = UInt32
RPC_BHO_NONCAUSAL: RPC_BINDING_HANDLE_OPTIONS_FLAGS = 1
RPC_BHO_DONTLINGER: RPC_BINDING_HANDLE_OPTIONS_FLAGS = 2
class RPC_BINDING_HANDLE_OPTIONS_V1(Structure):
    Version: UInt32
    Flags: Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_FLAGS
    ComTimeout: UInt32
    CallTimeout: UInt32
class RPC_BINDING_HANDLE_SECURITY_V1_A(Structure):
    Version: UInt32
    ServerPrincName: c_char_p_no
    AuthnLevel: UInt32
    AuthnSvc: UInt32
    AuthIdentity: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)
    SecurityQos: POINTER(Windows.Win32.System.Rpc.RPC_SECURITY_QOS_head)
class RPC_BINDING_HANDLE_SECURITY_V1_W(Structure):
    Version: UInt32
    ServerPrincName: POINTER(UInt16)
    AuthnLevel: UInt32
    AuthnSvc: UInt32
    AuthIdentity: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)
    SecurityQos: POINTER(Windows.Win32.System.Rpc.RPC_SECURITY_QOS_head)
class RPC_BINDING_HANDLE_TEMPLATE_V1_A(Structure):
    Version: UInt32
    Flags: UInt32
    ProtocolSequence: UInt32
    NetworkAddress: c_char_p_no
    StringEndpoint: c_char_p_no
    u1: _u1_e__Union
    ObjectUuid: Guid
    class _u1_e__Union(Union):
        Reserved: c_char_p_no
class RPC_BINDING_HANDLE_TEMPLATE_V1_W(Structure):
    Version: UInt32
    Flags: UInt32
    ProtocolSequence: UInt32
    NetworkAddress: POINTER(UInt16)
    StringEndpoint: POINTER(UInt16)
    u1: _u1_e__Union
    ObjectUuid: Guid
    class _u1_e__Union(Union):
        Reserved: POINTER(UInt16)
class RPC_BINDING_VECTOR(Structure):
    Count: UInt32
    BindingH: c_void_p * 1
@winfunctype_pointer
def RPC_BLOCKING_FN(hWnd: c_void_p, Context: c_void_p, hSyncEvent: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
class RPC_CALL_ATTRIBUTES_V1_A(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: c_char_p_no
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: c_char_p_no
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: Windows.Win32.Foundation.BOOL
class RPC_CALL_ATTRIBUTES_V1_W(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(UInt16)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(UInt16)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: Windows.Win32.Foundation.BOOL
class RPC_CALL_ATTRIBUTES_V2_A(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: c_char_p_no
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: c_char_p_no
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: Windows.Win32.Foundation.BOOL
    KernelModeCaller: Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: UInt32
    ClientPID: Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)
    OpNum: UInt16
    InterfaceUuid: Guid
class RPC_CALL_ATTRIBUTES_V2_W(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(UInt16)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(UInt16)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: Windows.Win32.Foundation.BOOL
    KernelModeCaller: Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: Windows.Win32.System.Rpc.RpcCallClientLocality
    ClientPID: Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)
    OpNum: UInt16
    InterfaceUuid: Guid
class RPC_CALL_ATTRIBUTES_V3_A(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: c_char_p_no
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: c_char_p_no
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: Windows.Win32.Foundation.BOOL
    KernelModeCaller: Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: UInt32
    ClientPID: Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)
    OpNum: UInt16
    InterfaceUuid: Guid
    ClientIdentifierBufferLength: UInt32
    ClientIdentifier: c_char_p_no
class RPC_CALL_ATTRIBUTES_V3_W(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(UInt16)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(UInt16)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: Windows.Win32.Foundation.BOOL
    KernelModeCaller: Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: Windows.Win32.System.Rpc.RpcCallClientLocality
    ClientPID: Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1_head)
    OpNum: UInt16
    InterfaceUuid: Guid
    ClientIdentifierBufferLength: UInt32
    ClientIdentifier: c_char_p_no
class RPC_CALL_LOCAL_ADDRESS_V1(Structure):
    Version: UInt32
    Buffer: c_void_p
    BufferSize: UInt32
    AddressFormat: Windows.Win32.System.Rpc.RpcLocalAddressFormat
@winfunctype_pointer
def RPC_CLIENT_ALLOC(Size: UIntPtr) -> c_void_p: ...
@winfunctype_pointer
def RPC_CLIENT_FREE(Ptr: c_void_p) -> Void: ...
class RPC_CLIENT_INFORMATION1(Structure):
    UserName: c_char_p_no
    ComputerName: c_char_p_no
    Privilege: UInt16
    AuthFlags: UInt32
class RPC_CLIENT_INTERFACE(Structure):
    Length: UInt32
    InterfaceId: Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    TransferSyntax: Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    DispatchTable: POINTER(Windows.Win32.System.Rpc.RPC_DISPATCH_TABLE_head)
    RpcProtseqEndpointCount: UInt32
    RpcProtseqEndpoint: POINTER(Windows.Win32.System.Rpc.RPC_PROTSEQ_ENDPOINT_head)
    Reserved: UIntPtr
    InterpreterInfo: c_void_p
    Flags: UInt32
RPC_C_AUTHN_INFO_TYPE = UInt32
RPC_C_AUTHN_INFO_NONE: RPC_C_AUTHN_INFO_TYPE = 0
RPC_C_AUTHN_INFO_TYPE_HTTP: RPC_C_AUTHN_INFO_TYPE = 1
RPC_C_HTTP_AUTHN_TARGET = UInt32
RPC_C_HTTP_AUTHN_TARGET_SERVER: RPC_C_HTTP_AUTHN_TARGET = 1
RPC_C_HTTP_AUTHN_TARGET_PROXY: RPC_C_HTTP_AUTHN_TARGET = 2
RPC_C_HTTP_FLAGS = UInt32
RPC_C_HTTP_FLAG_USE_SSL: RPC_C_HTTP_FLAGS = 1
RPC_C_HTTP_FLAG_USE_FIRST_AUTH_SCHEME: RPC_C_HTTP_FLAGS = 2
RPC_C_HTTP_FLAG_IGNORE_CERT_CN_INVALID: RPC_C_HTTP_FLAGS = 8
RPC_C_HTTP_FLAG_ENABLE_CERT_REVOCATION_CHECK: RPC_C_HTTP_FLAGS = 16
class RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR(Structure):
    BufferSize: UInt32
    Buffer: Windows.Win32.Foundation.PSTR
RPC_C_QOS_CAPABILITIES = UInt32
RPC_C_QOS_CAPABILITIES_DEFAULT: RPC_C_QOS_CAPABILITIES = 0
RPC_C_QOS_CAPABILITIES_MUTUAL_AUTH: RPC_C_QOS_CAPABILITIES = 1
RPC_C_QOS_CAPABILITIES_MAKE_FULLSIC: RPC_C_QOS_CAPABILITIES = 2
RPC_C_QOS_CAPABILITIES_ANY_AUTHORITY: RPC_C_QOS_CAPABILITIES = 4
RPC_C_QOS_CAPABILITIES_IGNORE_DELEGATE_FAILURE: RPC_C_QOS_CAPABILITIES = 8
RPC_C_QOS_CAPABILITIES_LOCAL_MA_HINT: RPC_C_QOS_CAPABILITIES = 16
RPC_C_QOS_CAPABILITIES_SCHANNEL_FULL_AUTH_IDENTITY: RPC_C_QOS_CAPABILITIES = 32
RPC_C_QOS_IDENTITY = UInt32
RPC_C_QOS_IDENTITY_STATIC: RPC_C_QOS_IDENTITY = 0
RPC_C_QOS_IDENTITY_DYNAMIC: RPC_C_QOS_IDENTITY = 1
@winfunctype_pointer
def RPC_DISPATCH_FUNCTION(Message: POINTER(Windows.Win32.System.Rpc.RPC_MESSAGE_head)) -> Void: ...
class RPC_DISPATCH_TABLE(Structure):
    DispatchTableCount: UInt32
    DispatchTable: Windows.Win32.System.Rpc.RPC_DISPATCH_FUNCTION
    Reserved: IntPtr
class RPC_EE_INFO_PARAM(Structure):
    ParameterType: Windows.Win32.System.Rpc.ExtendedErrorParamTypes
    u: _u_e__Union
    class _u_e__Union(Union):
        AnsiString: Windows.Win32.Foundation.PSTR
        UnicodeString: Windows.Win32.Foundation.PWSTR
        LVal: Int32
        SVal: Int16
        PVal: UInt64
        BVal: Windows.Win32.System.Rpc.BinaryParam
class RPC_ENDPOINT_TEMPLATEA(Structure):
    Version: UInt32
    ProtSeq: c_char_p_no
    Endpoint: c_char_p_no
    SecurityDescriptor: c_void_p
    Backlog: UInt32
class RPC_ENDPOINT_TEMPLATEW(Structure):
    Version: UInt32
    ProtSeq: POINTER(UInt16)
    Endpoint: POINTER(UInt16)
    SecurityDescriptor: c_void_p
    Backlog: UInt32
class RPC_ERROR_ENUM_HANDLE(Structure):
    Signature: UInt32
    CurrentPos: c_void_p
    Head: c_void_p
class RPC_EXTENDED_ERROR_INFO(Structure):
    Version: UInt32
    ComputerName: Windows.Win32.Foundation.PWSTR
    ProcessID: UInt32
    u: _u_e__Union
    GeneratingComponent: UInt32
    Status: UInt32
    DetectionLocation: UInt16
    Flags: UInt16
    NumberOfParameters: Int32
    Parameters: Windows.Win32.System.Rpc.RPC_EE_INFO_PARAM * 4
    class _u_e__Union(Union):
        SystemTime: Windows.Win32.Foundation.SYSTEMTIME
        FileTime: Windows.Win32.Foundation.FILETIME
@winfunctype_pointer
def RPC_FORWARD_FUNCTION(InterfaceId: POINTER(Guid), InterfaceVersion: POINTER(Windows.Win32.System.Rpc.RPC_VERSION_head), ObjectId: POINTER(Guid), Rpcpro: c_char_p_no, ppDestEndpoint: POINTER(c_void_p)) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def RPC_HTTP_PROXY_FREE_STRING(String: POINTER(UInt16)) -> Void: ...
RPC_HTTP_REDIRECTOR_STAGE = Int32
RPCHTTP_RS_REDIRECT: RPC_HTTP_REDIRECTOR_STAGE = 1
RPCHTTP_RS_ACCESS_1: RPC_HTTP_REDIRECTOR_STAGE = 2
RPCHTTP_RS_SESSION: RPC_HTTP_REDIRECTOR_STAGE = 3
RPCHTTP_RS_ACCESS_2: RPC_HTTP_REDIRECTOR_STAGE = 4
RPCHTTP_RS_INTERFACE: RPC_HTTP_REDIRECTOR_STAGE = 5
class RPC_HTTP_TRANSPORT_CREDENTIALS_A(Structure):
    TransportCredentials: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)
    Flags: Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: c_char_p_no
class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A(Structure):
    TransportCredentials: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)
    Flags: Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: c_char_p_no
    ProxyCredentials: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A_head)
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W(Structure):
    TransportCredentials: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)
    Flags: Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(UInt16)
    ProxyCredentials: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A(Structure):
    TransportCredentials: c_void_p
    Flags: Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: c_char_p_no
    ProxyCredentials: c_void_p
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W(Structure):
    TransportCredentials: c_void_p
    Flags: Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(UInt16)
    ProxyCredentials: c_void_p
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
class RPC_HTTP_TRANSPORT_CREDENTIALS_W(Structure):
    TransportCredentials: POINTER(Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W_head)
    Flags: Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(UInt16)
@winfunctype_pointer
def RPC_IF_CALLBACK_FN(InterfaceUuid: c_void_p, Context: c_void_p) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
class RPC_IF_ID(Structure):
    Uuid: Guid
    VersMajor: UInt16
    VersMinor: UInt16
class RPC_IF_ID_VECTOR(Structure):
    Count: UInt32
    IfId: POINTER(Windows.Win32.System.Rpc.RPC_IF_ID_head) * 1
class RPC_IMPORT_CONTEXT_P(Structure):
    LookupContext: c_void_p
    ProposedHandle: c_void_p
    Bindings: POINTER(Windows.Win32.System.Rpc.RPC_BINDING_VECTOR_head)
@winfunctype_pointer
def RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN(IfGroup: c_void_p, IdleCallbackContext: c_void_p, IsGroupIdle: UInt32) -> Void: ...
class RPC_INTERFACE_TEMPLATEA(Structure):
    Version: UInt32
    IfSpec: c_void_p
    MgrTypeUuid: POINTER(Guid)
    MgrEpv: c_void_p
    Flags: UInt32
    MaxCalls: UInt32
    MaxRpcSize: UInt32
    IfCallback: Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN
    UuidVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)
    Annotation: c_char_p_no
    SecurityDescriptor: c_void_p
class RPC_INTERFACE_TEMPLATEW(Structure):
    Version: UInt32
    IfSpec: c_void_p
    MgrTypeUuid: POINTER(Guid)
    MgrEpv: c_void_p
    Flags: UInt32
    MaxCalls: UInt32
    MaxRpcSize: UInt32
    IfCallback: Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN
    UuidVector: POINTER(Windows.Win32.System.Rpc.UUID_VECTOR_head)
    Annotation: POINTER(UInt16)
    SecurityDescriptor: c_void_p
class RPC_MESSAGE(Structure):
    Handle: c_void_p
    DataRepresentation: UInt32
    Buffer: c_void_p
    BufferLength: UInt32
    ProcNum: UInt32
    TransferSyntax: POINTER(Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER_head)
    RpcInterfaceInformation: c_void_p
    ReservedForRuntime: c_void_p
    ManagerEpv: c_void_p
    ImportContext: c_void_p
    RpcFlags: UInt32
@winfunctype_pointer
def RPC_MGMT_AUTHORIZATION_FN(ClientBinding: c_void_p, RequestedMgmtOperation: UInt32, Status: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype_pointer
def RPC_NEW_HTTP_PROXY_CHANNEL(RedirectorStage: Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE, ServerName: POINTER(UInt16), ServerPort: POINTER(UInt16), RemoteUser: POINTER(UInt16), AuthType: POINTER(UInt16), ResourceUuid: c_void_p, SessionId: c_void_p, Interface: c_void_p, Reserved: c_void_p, Flags: UInt32, NewServerName: POINTER(POINTER(UInt16)), NewServerPort: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Rpc.RPC_STATUS: ...
RPC_NOTIFICATIONS = Int32
RPC_NOTIFICATIONS_RpcNotificationCallNone: RPC_NOTIFICATIONS = 0
RPC_NOTIFICATIONS_RpcNotificationClientDisconnect: RPC_NOTIFICATIONS = 1
RPC_NOTIFICATIONS_RpcNotificationCallCancel: RPC_NOTIFICATIONS = 2
RPC_NOTIFICATION_TYPES = Int32
RPC_NOTIFICATION_TYPES_RpcNotificationTypeNone: RPC_NOTIFICATION_TYPES = 0
RPC_NOTIFICATION_TYPES_RpcNotificationTypeEvent: RPC_NOTIFICATION_TYPES = 1
RPC_NOTIFICATION_TYPES_RpcNotificationTypeApc: RPC_NOTIFICATION_TYPES = 2
RPC_NOTIFICATION_TYPES_RpcNotificationTypeIoc: RPC_NOTIFICATION_TYPES = 3
RPC_NOTIFICATION_TYPES_RpcNotificationTypeHwnd: RPC_NOTIFICATION_TYPES = 4
RPC_NOTIFICATION_TYPES_RpcNotificationTypeCallback: RPC_NOTIFICATION_TYPES = 5
@winfunctype_pointer
def RPC_OBJECT_INQ_FN(ObjectUuid: POINTER(Guid), TypeUuid: POINTER(Guid), Status: POINTER(Windows.Win32.System.Rpc.RPC_STATUS)) -> Void: ...
class RPC_POLICY(Structure):
    Length: UInt32
    EndpointFlags: UInt32
    NICFlags: UInt32
class RPC_PROTSEQ_ENDPOINT(Structure):
    RpcProtocolSequence: c_char_p_no
    Endpoint: c_char_p_no
class RPC_PROTSEQ_VECTORA(Structure):
    Count: UInt32
    Protseq: c_char_p_no * 1
class RPC_PROTSEQ_VECTORW(Structure):
    Count: UInt32
    Protseq: POINTER(UInt16) * 1
@winfunctype_pointer
def RPC_SECURITY_CALLBACK_FN(Context: c_void_p) -> Void: ...
class RPC_SECURITY_QOS(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
class RPC_SECURITY_QOS_V2_A(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)
class RPC_SECURITY_QOS_V2_W(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)
class RPC_SECURITY_QOS_V3_A(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: c_void_p
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)
class RPC_SECURITY_QOS_V3_W(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: c_void_p
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)
class RPC_SECURITY_QOS_V4_A(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: c_void_p
    EffectiveOnly: UInt32
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)
class RPC_SECURITY_QOS_V4_W(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: c_void_p
    EffectiveOnly: UInt32
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)
class RPC_SECURITY_QOS_V5_A(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: c_void_p
    EffectiveOnly: UInt32
    ServerSecurityDescriptor: c_void_p
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A_head)
class RPC_SECURITY_QOS_V5_W(Structure):
    Version: UInt32
    Capabilities: Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: c_void_p
    EffectiveOnly: UInt32
    ServerSecurityDescriptor: c_void_p
    class _u_e__Union(Union):
        HttpCredentials: POINTER(Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W_head)
class RPC_SEC_CONTEXT_KEY_INFO(Structure):
    EncryptAlgorithm: UInt32
    KeySize: UInt32
    SignatureAlgorithm: UInt32
class RPC_SERVER_INTERFACE(Structure):
    Length: UInt32
    InterfaceId: Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    TransferSyntax: Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    DispatchTable: POINTER(Windows.Win32.System.Rpc.RPC_DISPATCH_TABLE_head)
    RpcProtseqEndpointCount: UInt32
    RpcProtseqEndpoint: POINTER(Windows.Win32.System.Rpc.RPC_PROTSEQ_ENDPOINT_head)
    DefaultManagerEpv: c_void_p
    InterpreterInfo: c_void_p
    Flags: UInt32
@cfunctype_pointer
def RPC_SETFILTER_FUNC(pfnFilter: Windows.Win32.System.Rpc.RPCLT_PDU_FILTER_FUNC) -> Void: ...
class RPC_STATS_VECTOR(Structure):
    Count: UInt32
    Stats: UInt32 * 1
RPC_STATUS = Int32
RPC_S_INVALID_STRING_BINDING: RPC_STATUS = 1700
RPC_S_WRONG_KIND_OF_BINDING: RPC_STATUS = 1701
RPC_S_INVALID_BINDING: RPC_STATUS = 1702
RPC_S_PROTSEQ_NOT_SUPPORTED: RPC_STATUS = 1703
RPC_S_INVALID_RPC_PROTSEQ: RPC_STATUS = 1704
RPC_S_INVALID_STRING_UUID: RPC_STATUS = 1705
RPC_S_INVALID_ENDPOINT_FORMAT: RPC_STATUS = 1706
RPC_S_INVALID_NET_ADDR: RPC_STATUS = 1707
RPC_S_NO_ENDPOINT_FOUND: RPC_STATUS = 1708
RPC_S_INVALID_TIMEOUT: RPC_STATUS = 1709
RPC_S_OBJECT_NOT_FOUND: RPC_STATUS = 1710
RPC_S_ALREADY_REGISTERED: RPC_STATUS = 1711
RPC_S_TYPE_ALREADY_REGISTERED: RPC_STATUS = 1712
RPC_S_ALREADY_LISTENING: RPC_STATUS = 1713
RPC_S_NO_PROTSEQS_REGISTERED: RPC_STATUS = 1714
RPC_S_NOT_LISTENING: RPC_STATUS = 1715
RPC_S_UNKNOWN_MGR_TYPE: RPC_STATUS = 1716
RPC_S_UNKNOWN_IF: RPC_STATUS = 1717
RPC_S_NO_BINDINGS: RPC_STATUS = 1718
RPC_S_NO_PROTSEQS: RPC_STATUS = 1719
RPC_S_CANT_CREATE_ENDPOINT: RPC_STATUS = 1720
RPC_S_OUT_OF_RESOURCES: RPC_STATUS = 1721
RPC_S_SERVER_UNAVAILABLE: RPC_STATUS = 1722
RPC_S_SERVER_TOO_BUSY: RPC_STATUS = 1723
RPC_S_INVALID_NETWORK_OPTIONS: RPC_STATUS = 1724
RPC_S_NO_CALL_ACTIVE: RPC_STATUS = 1725
RPC_S_CALL_FAILED: RPC_STATUS = 1726
RPC_S_CALL_FAILED_DNE: RPC_STATUS = 1727
RPC_S_PROTOCOL_ERROR: RPC_STATUS = 1728
RPC_S_PROXY_ACCESS_DENIED: RPC_STATUS = 1729
RPC_S_UNSUPPORTED_TRANS_SYN: RPC_STATUS = 1730
RPC_S_UNSUPPORTED_TYPE: RPC_STATUS = 1732
RPC_S_INVALID_TAG: RPC_STATUS = 1733
RPC_S_INVALID_BOUND: RPC_STATUS = 1734
RPC_S_NO_ENTRY_NAME: RPC_STATUS = 1735
RPC_S_INVALID_NAME_SYNTAX: RPC_STATUS = 1736
RPC_S_UNSUPPORTED_NAME_SYNTAX: RPC_STATUS = 1737
RPC_S_UUID_NO_ADDRESS: RPC_STATUS = 1739
RPC_S_DUPLICATE_ENDPOINT: RPC_STATUS = 1740
RPC_S_UNKNOWN_AUTHN_TYPE: RPC_STATUS = 1741
RPC_S_MAX_CALLS_TOO_SMALL: RPC_STATUS = 1742
RPC_S_STRING_TOO_LONG: RPC_STATUS = 1743
RPC_S_PROTSEQ_NOT_FOUND: RPC_STATUS = 1744
RPC_S_PROCNUM_OUT_OF_RANGE: RPC_STATUS = 1745
RPC_S_BINDING_HAS_NO_AUTH: RPC_STATUS = 1746
RPC_S_UNKNOWN_AUTHN_SERVICE: RPC_STATUS = 1747
RPC_S_UNKNOWN_AUTHN_LEVEL: RPC_STATUS = 1748
RPC_S_INVALID_AUTH_IDENTITY: RPC_STATUS = 1749
RPC_S_UNKNOWN_AUTHZ_SERVICE: RPC_STATUS = 1750
EPT_S_INVALID_ENTRY: RPC_STATUS = 1751
EPT_S_CANT_PERFORM_OP: RPC_STATUS = 1752
EPT_S_NOT_REGISTERED: RPC_STATUS = 1753
RPC_S_NOTHING_TO_EXPORT: RPC_STATUS = 1754
RPC_S_INCOMPLETE_NAME: RPC_STATUS = 1755
RPC_S_INVALID_VERS_OPTION: RPC_STATUS = 1756
RPC_S_NO_MORE_MEMBERS: RPC_STATUS = 1757
RPC_S_NOT_ALL_OBJS_UNEXPORTED: RPC_STATUS = 1758
RPC_S_INTERFACE_NOT_FOUND: RPC_STATUS = 1759
RPC_S_ENTRY_ALREADY_EXISTS: RPC_STATUS = 1760
RPC_S_ENTRY_NOT_FOUND: RPC_STATUS = 1761
RPC_S_NAME_SERVICE_UNAVAILABLE: RPC_STATUS = 1762
RPC_S_INVALID_NAF_ID: RPC_STATUS = 1763
RPC_S_CANNOT_SUPPORT: RPC_STATUS = 1764
RPC_S_NO_CONTEXT_AVAILABLE: RPC_STATUS = 1765
RPC_S_INTERNAL_ERROR: RPC_STATUS = 1766
RPC_S_ZERO_DIVIDE: RPC_STATUS = 1767
RPC_S_ADDRESS_ERROR: RPC_STATUS = 1768
RPC_S_FP_DIV_ZERO: RPC_STATUS = 1769
RPC_S_FP_UNDERFLOW: RPC_STATUS = 1770
RPC_S_FP_OVERFLOW: RPC_STATUS = 1771
RPC_S_CALL_IN_PROGRESS: RPC_STATUS = 1791
RPC_S_NO_MORE_BINDINGS: RPC_STATUS = 1806
RPC_S_NO_INTERFACES: RPC_STATUS = 1817
RPC_S_CALL_CANCELLED: RPC_STATUS = 1818
RPC_S_BINDING_INCOMPLETE: RPC_STATUS = 1819
RPC_S_COMM_FAILURE: RPC_STATUS = 1820
RPC_S_UNSUPPORTED_AUTHN_LEVEL: RPC_STATUS = 1821
RPC_S_NO_PRINC_NAME: RPC_STATUS = 1822
RPC_S_NOT_RPC_ERROR: RPC_STATUS = 1823
RPC_S_UUID_LOCAL_ONLY: RPC_STATUS = 1824
RPC_S_SEC_PKG_ERROR: RPC_STATUS = 1825
RPC_S_NOT_CANCELLED: RPC_STATUS = 1826
RPC_S_COOKIE_AUTH_FAILED: RPC_STATUS = 1833
RPC_S_DO_NOT_DISTURB: RPC_STATUS = 1834
RPC_S_SYSTEM_HANDLE_COUNT_EXCEEDED: RPC_STATUS = 1835
RPC_S_SYSTEM_HANDLE_TYPE_MISMATCH: RPC_STATUS = 1836
RPC_S_GROUP_MEMBER_NOT_FOUND: RPC_STATUS = 1898
EPT_S_CANT_CREATE: RPC_STATUS = 1899
RPC_S_INVALID_OBJECT: RPC_STATUS = 1900
RPC_S_SEND_INCOMPLETE: RPC_STATUS = 1913
RPC_S_INVALID_ASYNC_HANDLE: RPC_STATUS = 1914
RPC_S_INVALID_ASYNC_CALL: RPC_STATUS = 1915
RPC_S_ENTRY_TYPE_MISMATCH: RPC_STATUS = 1922
RPC_S_NOT_ALL_OBJS_EXPORTED: RPC_STATUS = 1923
RPC_S_INTERFACE_NOT_EXPORTED: RPC_STATUS = 1924
RPC_S_PROFILE_NOT_ADDED: RPC_STATUS = 1925
RPC_S_PRF_ELT_NOT_ADDED: RPC_STATUS = 1926
RPC_S_PRF_ELT_NOT_REMOVED: RPC_STATUS = 1927
RPC_S_GRP_ELT_NOT_ADDED: RPC_STATUS = 1928
RPC_S_GRP_ELT_NOT_REMOVED: RPC_STATUS = 1929
class RPC_SYNTAX_IDENTIFIER(Structure):
    SyntaxGUID: Guid
    SyntaxVersion: Windows.Win32.System.Rpc.RPC_VERSION
class RPC_TRANSFER_SYNTAX(Structure):
    Uuid: Guid
    VersMajor: UInt16
    VersMinor: UInt16
class RPC_VERSION(Structure):
    MajorVersion: UInt16
    MinorVersion: UInt16
RpcCallClientLocality = Int32
RpcCallClientLocality_rcclInvalid: RpcCallClientLocality = 0
RpcCallClientLocality_rcclLocal: RpcCallClientLocality = 1
RpcCallClientLocality_rcclRemote: RpcCallClientLocality = 2
RpcCallClientLocality_rcclClientUnknownLocality: RpcCallClientLocality = 3
RpcCallType = Int32
RpcCallType_rctInvalid: RpcCallType = 0
RpcCallType_rctNormal: RpcCallType = 1
RpcCallType_rctTraining: RpcCallType = 2
RpcCallType_rctGuaranteed: RpcCallType = 3
RpcLocalAddressFormat = Int32
RpcLocalAddressFormat_rlafInvalid: RpcLocalAddressFormat = 0
RpcLocalAddressFormat_rlafIPv4: RpcLocalAddressFormat = 1
RpcLocalAddressFormat_rlafIPv6: RpcLocalAddressFormat = 2
RpcPerfCounters = Int32
RpcPerfCounters_RpcCurrentUniqueUser: RpcPerfCounters = 1
RpcPerfCounters_RpcBackEndConnectionAttempts: RpcPerfCounters = 2
RpcPerfCounters_RpcBackEndConnectionFailed: RpcPerfCounters = 3
RpcPerfCounters_RpcRequestsPerSecond: RpcPerfCounters = 4
RpcPerfCounters_RpcIncomingConnections: RpcPerfCounters = 5
RpcPerfCounters_RpcIncomingBandwidth: RpcPerfCounters = 6
RpcPerfCounters_RpcOutgoingBandwidth: RpcPerfCounters = 7
RpcPerfCounters_RpcAttemptedLbsDecisions: RpcPerfCounters = 8
RpcPerfCounters_RpcFailedLbsDecisions: RpcPerfCounters = 9
RpcPerfCounters_RpcAttemptedLbsMessages: RpcPerfCounters = 10
RpcPerfCounters_RpcFailedLbsMessages: RpcPerfCounters = 11
RpcPerfCounters_RpcLastCounter: RpcPerfCounters = 12
class SCONTEXT_QUEUE(Structure):
    NumberOfObjects: UInt32
    ArrayOfObjects: POINTER(POINTER(Windows.Win32.System.Rpc.NDR_SCONTEXT_head))
SEC_WINNT_AUTH_IDENTITY = UInt32
SEC_WINNT_AUTH_IDENTITY_ANSI: SEC_WINNT_AUTH_IDENTITY = 1
SEC_WINNT_AUTH_IDENTITY_UNICODE: SEC_WINNT_AUTH_IDENTITY = 2
class SEC_WINNT_AUTH_IDENTITY_A(Structure):
    User: c_char_p_no
    UserLength: UInt32
    Domain: c_char_p_no
    DomainLength: UInt32
    Password: c_char_p_no
    PasswordLength: UInt32
    Flags: Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY
class SEC_WINNT_AUTH_IDENTITY_W(Structure):
    User: POINTER(UInt16)
    UserLength: UInt32
    Domain: POINTER(UInt16)
    DomainLength: UInt32
    Password: POINTER(UInt16)
    PasswordLength: UInt32
    Flags: Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY
@winfunctype_pointer
def SERVER_ROUTINE() -> Int32: ...
STUB_PHASE = Int32
STUB_UNMARSHAL: STUB_PHASE = 0
STUB_CALL_SERVER: STUB_PHASE = 1
STUB_MARSHAL: STUB_PHASE = 2
STUB_CALL_SERVER_NO_HRESULT: STUB_PHASE = 3
@winfunctype_pointer
def STUB_THUNK(param0: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
class USER_MARSHAL_CB(Structure):
    Flags: UInt32
    pStubMsg: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)
    pReserve: c_char_p_no
    Signature: UInt32
    CBType: Windows.Win32.System.Rpc.USER_MARSHAL_CB_TYPE
    pFormat: c_char_p_no
    pTypeFormat: c_char_p_no
USER_MARSHAL_CB_TYPE = Int32
USER_MARSHAL_CB_BUFFER_SIZE: USER_MARSHAL_CB_TYPE = 0
USER_MARSHAL_CB_MARSHALL: USER_MARSHAL_CB_TYPE = 1
USER_MARSHAL_CB_UNMARSHALL: USER_MARSHAL_CB_TYPE = 2
USER_MARSHAL_CB_FREE: USER_MARSHAL_CB_TYPE = 3
@winfunctype_pointer
def USER_MARSHAL_FREEING_ROUTINE(param0: POINTER(UInt32), param1: c_void_p) -> Void: ...
@winfunctype_pointer
def USER_MARSHAL_MARSHALLING_ROUTINE(param0: POINTER(UInt32), param1: c_char_p_no, param2: c_void_p) -> c_char_p_no: ...
class USER_MARSHAL_ROUTINE_QUADRUPLE(Structure):
    pfnBufferSize: Windows.Win32.System.Rpc.USER_MARSHAL_SIZING_ROUTINE
    pfnMarshall: Windows.Win32.System.Rpc.USER_MARSHAL_MARSHALLING_ROUTINE
    pfnUnmarshall: Windows.Win32.System.Rpc.USER_MARSHAL_UNMARSHALLING_ROUTINE
    pfnFree: Windows.Win32.System.Rpc.USER_MARSHAL_FREEING_ROUTINE
@winfunctype_pointer
def USER_MARSHAL_SIZING_ROUTINE(param0: POINTER(UInt32), param1: UInt32, param2: c_void_p) -> UInt32: ...
@winfunctype_pointer
def USER_MARSHAL_UNMARSHALLING_ROUTINE(param0: POINTER(UInt32), param1: c_char_p_no, param2: c_void_p) -> c_char_p_no: ...
class UUID_VECTOR(Structure):
    Count: UInt32
    Uuid: POINTER(Guid) * 1
XLAT_SIDE = Int32
XLAT_SERVER: XLAT_SIDE = 1
XLAT_CLIENT: XLAT_SIDE = 2
@winfunctype_pointer
def XMIT_HELPER_ROUTINE(param0: POINTER(Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE_head)) -> Void: ...
class XMIT_ROUTINE_QUINTUPLE(Structure):
    pfnTranslateToXmit: Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
    pfnTranslateFromXmit: Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
    pfnFreeXmit: Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
    pfnFreeInst: Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
class _NDR_ASYNC_MESSAGE(Structure):
    pass
class _NDR_CORRELATION_INFO(Structure):
    pass
class _NDR_PROC_CONTEXT(Structure):
    pass
system_handle_t = Int32
SYSTEM_HANDLE_FILE: system_handle_t = 0
SYSTEM_HANDLE_SEMAPHORE: system_handle_t = 1
SYSTEM_HANDLE_EVENT: system_handle_t = 2
SYSTEM_HANDLE_MUTEX: system_handle_t = 3
SYSTEM_HANDLE_PROCESS: system_handle_t = 4
SYSTEM_HANDLE_TOKEN: system_handle_t = 5
SYSTEM_HANDLE_SECTION: system_handle_t = 6
SYSTEM_HANDLE_REG_KEY: system_handle_t = 7
SYSTEM_HANDLE_THREAD: system_handle_t = 8
SYSTEM_HANDLE_COMPOSITION_OBJECT: system_handle_t = 9
SYSTEM_HANDLE_SOCKET: system_handle_t = 10
SYSTEM_HANDLE_JOB: system_handle_t = 11
SYSTEM_HANDLE_PIPE: system_handle_t = 12
SYSTEM_HANDLE_MAX: system_handle_t = 12
SYSTEM_HANDLE_INVALID: system_handle_t = 255
make_head(_module, 'ARRAY_INFO')
make_head(_module, 'BinaryParam')
make_head(_module, 'CLIENT_CALL_RETURN')
make_head(_module, 'COMM_FAULT_OFFSETS')
make_head(_module, 'CS_TAG_GETTING_ROUTINE')
make_head(_module, 'CS_TYPE_FROM_NETCS_ROUTINE')
make_head(_module, 'CS_TYPE_LOCAL_SIZE_ROUTINE')
make_head(_module, 'CS_TYPE_NET_SIZE_ROUTINE')
make_head(_module, 'CS_TYPE_TO_NETCS_ROUTINE')
make_head(_module, 'EXPR_EVAL')
make_head(_module, 'FULL_PTR_XLAT_TABLES')
make_head(_module, 'GENERIC_BINDING_INFO')
make_head(_module, 'GENERIC_BINDING_ROUTINE')
make_head(_module, 'GENERIC_BINDING_ROUTINE_PAIR')
make_head(_module, 'GENERIC_UNBIND_ROUTINE')
make_head(_module, 'I_RpcFreeCalloutStateFn')
make_head(_module, 'I_RpcPerformCalloutFn')
make_head(_module, 'I_RpcProxyCallbackInterface')
make_head(_module, 'I_RpcProxyFilterIfFn')
make_head(_module, 'I_RpcProxyGetClientAddressFn')
make_head(_module, 'I_RpcProxyGetClientSessionAndResourceUUID')
make_head(_module, 'I_RpcProxyGetConnectionTimeoutFn')
make_head(_module, 'I_RpcProxyIsValidMachineFn')
make_head(_module, 'I_RpcProxyUpdatePerfCounterBackendServerFn')
make_head(_module, 'I_RpcProxyUpdatePerfCounterFn')
make_head(_module, 'MALLOC_FREE_STRUCT')
make_head(_module, 'MIDL_ES_ALLOC')
make_head(_module, 'MIDL_ES_READ')
make_head(_module, 'MIDL_ES_WRITE')
make_head(_module, 'MIDL_FORMAT_STRING')
make_head(_module, 'MIDL_INTERCEPTION_INFO')
make_head(_module, 'MIDL_INTERFACE_METHOD_PROPERTIES')
make_head(_module, 'MIDL_METHOD_PROPERTY')
make_head(_module, 'MIDL_METHOD_PROPERTY_MAP')
make_head(_module, 'MIDL_SERVER_INFO')
make_head(_module, 'MIDL_STUBLESS_PROXY_INFO')
make_head(_module, 'MIDL_STUB_DESC')
make_head(_module, 'MIDL_STUB_MESSAGE')
make_head(_module, 'MIDL_SYNTAX_INFO')
make_head(_module, 'MIDL_TYPE_PICKLING_INFO')
make_head(_module, 'MIDL_WINRT_TYPE_SERIALIZATION_INFO')
make_head(_module, 'NDR64_ARRAY_ELEMENT_INFO')
make_head(_module, 'NDR64_ARRAY_FLAGS')
make_head(_module, 'NDR64_BINDINGS')
make_head(_module, 'NDR64_BIND_AND_NOTIFY_EXTENSION')
make_head(_module, 'NDR64_BIND_CONTEXT')
make_head(_module, 'NDR64_BIND_GENERIC')
make_head(_module, 'NDR64_BIND_PRIMITIVE')
make_head(_module, 'NDR64_BOGUS_ARRAY_HEADER_FORMAT')
make_head(_module, 'NDR64_BOGUS_STRUCTURE_HEADER_FORMAT')
make_head(_module, 'NDR64_BUFFER_ALIGN_FORMAT')
make_head(_module, 'NDR64_CONFORMANT_STRING_FORMAT')
make_head(_module, 'NDR64_CONF_ARRAY_HEADER_FORMAT')
make_head(_module, 'NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT')
make_head(_module, 'NDR64_CONF_STRUCTURE_HEADER_FORMAT')
make_head(_module, 'NDR64_CONF_VAR_ARRAY_HEADER_FORMAT')
make_head(_module, 'NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT')
make_head(_module, 'NDR64_CONSTANT_IID_FORMAT')
make_head(_module, 'NDR64_CONTEXT_HANDLE_FLAGS')
make_head(_module, 'NDR64_CONTEXT_HANDLE_FORMAT')
make_head(_module, 'NDR64_EMBEDDED_COMPLEX_FORMAT')
make_head(_module, 'NDR64_ENCAPSULATED_UNION')
make_head(_module, 'NDR64_EXPR_CONST32')
make_head(_module, 'NDR64_EXPR_CONST64')
make_head(_module, 'NDR64_EXPR_NOOP')
make_head(_module, 'NDR64_EXPR_OPERATOR')
make_head(_module, 'NDR64_EXPR_VAR')
make_head(_module, 'NDR64_FIXED_REPEAT_FORMAT')
make_head(_module, 'NDR64_FIX_ARRAY_HEADER_FORMAT')
make_head(_module, 'NDR64_IID_FLAGS')
make_head(_module, 'NDR64_IID_FORMAT')
make_head(_module, 'NDR64_MEMPAD_FORMAT')
make_head(_module, 'NDR64_NON_CONFORMANT_STRING_FORMAT')
make_head(_module, 'NDR64_NON_ENCAPSULATED_UNION')
make_head(_module, 'NDR64_NO_REPEAT_FORMAT')
make_head(_module, 'NDR64_PARAM_FLAGS')
make_head(_module, 'NDR64_PARAM_FORMAT')
make_head(_module, 'NDR64_PIPE_FLAGS')
make_head(_module, 'NDR64_PIPE_FORMAT')
make_head(_module, 'NDR64_POINTER_FORMAT')
make_head(_module, 'NDR64_POINTER_INSTANCE_HEADER_FORMAT')
make_head(_module, 'NDR64_POINTER_REPEAT_FLAGS')
make_head(_module, 'NDR64_PROC_FLAGS')
make_head(_module, 'NDR64_PROC_FORMAT')
make_head(_module, 'NDR64_RANGED_STRING_FORMAT')
make_head(_module, 'NDR64_RANGE_FORMAT')
make_head(_module, 'NDR64_RANGE_PIPE_FORMAT')
make_head(_module, 'NDR64_REPEAT_FORMAT')
make_head(_module, 'NDR64_RPC_FLAGS')
make_head(_module, 'NDR64_SIMPLE_MEMBER_FORMAT')
make_head(_module, 'NDR64_SIMPLE_REGION_FORMAT')
make_head(_module, 'NDR64_SIZED_CONFORMANT_STRING_FORMAT')
make_head(_module, 'NDR64_STRING_FLAGS')
make_head(_module, 'NDR64_STRING_HEADER_FORMAT')
make_head(_module, 'NDR64_STRUCTURE_FLAGS')
make_head(_module, 'NDR64_STRUCTURE_HEADER_FORMAT')
make_head(_module, 'NDR64_SYSTEM_HANDLE_FORMAT')
make_head(_module, 'NDR64_TRANSMIT_AS_FLAGS')
make_head(_module, 'NDR64_TRANSMIT_AS_FORMAT')
make_head(_module, 'NDR64_TYPE_STRICT_CONTEXT_HANDLE')
make_head(_module, 'NDR64_UNION_ARM')
make_head(_module, 'NDR64_UNION_ARM_SELECTOR')
make_head(_module, 'NDR64_USER_MARSHAL_FLAGS')
make_head(_module, 'NDR64_USER_MARSHAL_FORMAT')
make_head(_module, 'NDR64_VAR_ARRAY_HEADER_FORMAT')
make_head(_module, 'NDR_ALLOC_ALL_NODES_CONTEXT')
make_head(_module, 'NDR_CS_ROUTINES')
make_head(_module, 'NDR_CS_SIZE_CONVERT_ROUTINES')
make_head(_module, 'NDR_EXPR_DESC')
make_head(_module, 'NDR_NOTIFY2_ROUTINE')
make_head(_module, 'NDR_NOTIFY_ROUTINE')
make_head(_module, 'NDR_POINTER_QUEUE_STATE')
make_head(_module, 'NDR_RUNDOWN')
make_head(_module, 'NDR_SCONTEXT')
make_head(_module, 'NDR_USER_MARSHAL_INFO')
make_head(_module, 'NDR_USER_MARSHAL_INFO_LEVEL1')
make_head(_module, 'PFN_RPCNOTIFICATION_ROUTINE')
make_head(_module, 'PRPC_RUNDOWN')
make_head(_module, 'RDR_CALLOUT_STATE')
make_head(_module, 'RPCLT_PDU_FILTER_FUNC')
make_head(_module, 'RPC_ADDRESS_CHANGE_FN')
make_head(_module, 'RPC_ASYNC_NOTIFICATION_INFO')
make_head(_module, 'RPC_ASYNC_STATE')
make_head(_module, 'RPC_AUTH_KEY_RETRIEVAL_FN')
make_head(_module, 'RPC_BINDING_HANDLE_OPTIONS_V1')
make_head(_module, 'RPC_BINDING_HANDLE_SECURITY_V1_A')
make_head(_module, 'RPC_BINDING_HANDLE_SECURITY_V1_W')
make_head(_module, 'RPC_BINDING_HANDLE_TEMPLATE_V1_A')
make_head(_module, 'RPC_BINDING_HANDLE_TEMPLATE_V1_W')
make_head(_module, 'RPC_BINDING_VECTOR')
make_head(_module, 'RPC_BLOCKING_FN')
make_head(_module, 'RPC_CALL_ATTRIBUTES_V1_A')
make_head(_module, 'RPC_CALL_ATTRIBUTES_V1_W')
make_head(_module, 'RPC_CALL_ATTRIBUTES_V2_A')
make_head(_module, 'RPC_CALL_ATTRIBUTES_V2_W')
make_head(_module, 'RPC_CALL_ATTRIBUTES_V3_A')
make_head(_module, 'RPC_CALL_ATTRIBUTES_V3_W')
make_head(_module, 'RPC_CALL_LOCAL_ADDRESS_V1')
make_head(_module, 'RPC_CLIENT_ALLOC')
make_head(_module, 'RPC_CLIENT_FREE')
make_head(_module, 'RPC_CLIENT_INFORMATION1')
make_head(_module, 'RPC_CLIENT_INTERFACE')
make_head(_module, 'RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR')
make_head(_module, 'RPC_DISPATCH_FUNCTION')
make_head(_module, 'RPC_DISPATCH_TABLE')
make_head(_module, 'RPC_EE_INFO_PARAM')
make_head(_module, 'RPC_ENDPOINT_TEMPLATEA')
make_head(_module, 'RPC_ENDPOINT_TEMPLATEW')
make_head(_module, 'RPC_ERROR_ENUM_HANDLE')
make_head(_module, 'RPC_EXTENDED_ERROR_INFO')
make_head(_module, 'RPC_FORWARD_FUNCTION')
make_head(_module, 'RPC_HTTP_PROXY_FREE_STRING')
make_head(_module, 'RPC_HTTP_TRANSPORT_CREDENTIALS_A')
make_head(_module, 'RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A')
make_head(_module, 'RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W')
make_head(_module, 'RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A')
make_head(_module, 'RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W')
make_head(_module, 'RPC_HTTP_TRANSPORT_CREDENTIALS_W')
make_head(_module, 'RPC_IF_CALLBACK_FN')
make_head(_module, 'RPC_IF_ID')
make_head(_module, 'RPC_IF_ID_VECTOR')
make_head(_module, 'RPC_IMPORT_CONTEXT_P')
make_head(_module, 'RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN')
make_head(_module, 'RPC_INTERFACE_TEMPLATEA')
make_head(_module, 'RPC_INTERFACE_TEMPLATEW')
make_head(_module, 'RPC_MESSAGE')
make_head(_module, 'RPC_MGMT_AUTHORIZATION_FN')
make_head(_module, 'RPC_NEW_HTTP_PROXY_CHANNEL')
make_head(_module, 'RPC_OBJECT_INQ_FN')
make_head(_module, 'RPC_POLICY')
make_head(_module, 'RPC_PROTSEQ_ENDPOINT')
make_head(_module, 'RPC_PROTSEQ_VECTORA')
make_head(_module, 'RPC_PROTSEQ_VECTORW')
make_head(_module, 'RPC_SECURITY_CALLBACK_FN')
make_head(_module, 'RPC_SECURITY_QOS')
make_head(_module, 'RPC_SECURITY_QOS_V2_A')
make_head(_module, 'RPC_SECURITY_QOS_V2_W')
make_head(_module, 'RPC_SECURITY_QOS_V3_A')
make_head(_module, 'RPC_SECURITY_QOS_V3_W')
make_head(_module, 'RPC_SECURITY_QOS_V4_A')
make_head(_module, 'RPC_SECURITY_QOS_V4_W')
make_head(_module, 'RPC_SECURITY_QOS_V5_A')
make_head(_module, 'RPC_SECURITY_QOS_V5_W')
make_head(_module, 'RPC_SEC_CONTEXT_KEY_INFO')
make_head(_module, 'RPC_SERVER_INTERFACE')
make_head(_module, 'RPC_SETFILTER_FUNC')
make_head(_module, 'RPC_STATS_VECTOR')
make_head(_module, 'RPC_SYNTAX_IDENTIFIER')
make_head(_module, 'RPC_TRANSFER_SYNTAX')
make_head(_module, 'RPC_VERSION')
make_head(_module, 'SCONTEXT_QUEUE')
make_head(_module, 'SEC_WINNT_AUTH_IDENTITY_A')
make_head(_module, 'SEC_WINNT_AUTH_IDENTITY_W')
make_head(_module, 'SERVER_ROUTINE')
make_head(_module, 'STUB_THUNK')
make_head(_module, 'USER_MARSHAL_CB')
make_head(_module, 'USER_MARSHAL_FREEING_ROUTINE')
make_head(_module, 'USER_MARSHAL_MARSHALLING_ROUTINE')
make_head(_module, 'USER_MARSHAL_ROUTINE_QUADRUPLE')
make_head(_module, 'USER_MARSHAL_SIZING_ROUTINE')
make_head(_module, 'USER_MARSHAL_UNMARSHALLING_ROUTINE')
make_head(_module, 'UUID_VECTOR')
make_head(_module, 'XMIT_HELPER_ROUTINE')
make_head(_module, 'XMIT_ROUTINE_QUINTUPLE')
make_head(_module, '_NDR_ASYNC_MESSAGE')
make_head(_module, '_NDR_CORRELATION_INFO')
make_head(_module, '_NDR_PROC_CONTEXT')
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
    "NDR_SCONTEXT",
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
    "__RPCPROXY_H_VERSION__",
    "cbNDRContext",
    "system_handle_t",
]
_arch_optional = [
]
