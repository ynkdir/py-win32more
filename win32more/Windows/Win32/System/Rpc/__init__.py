from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.IO
import win32more.Windows.Win32.System.Rpc
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
TARGET_IS_NT1012_OR_LATER: UInt32 = 1
TARGET_IS_NT102_OR_LATER: UInt32 = 1
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
__RPCPROXY_H_VERSION__: UInt32 = 477
MidlInterceptionInfoVersionOne: Int32 = 1
MidlWinrtTypeSerializationInfoVersionOne: Int32 = 1
@winfunctype('RPCRT4.dll')
def IUnknown_QueryInterface_Proxy(This: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('RPCRT4.dll')
def IUnknown_AddRef_Proxy(This: win32more.Windows.Win32.System.Com.IUnknown) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def IUnknown_Release_Proxy(This: win32more.Windows.Win32.System.Com.IUnknown) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def RpcBindingCopy(SourceBinding: VoidPtr, DestinationBinding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingFree(Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetOption(hBinding: VoidPtr, option: UInt32, optionValue: UIntPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqOption(hBinding: VoidPtr, option: UInt32, pOptionValue: POINTER(UIntPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingFromStringBindingA(StringBinding: win32more.Windows.Win32.Foundation.PSTR, Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingFromStringBindingW(StringBinding: win32more.Windows.Win32.Foundation.PWSTR, Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingFromStringBinding = UnicodeAlias('RpcBindingFromStringBindingW')
@winfunctype('RPCRT4.dll')
def RpcSsGetContextBinding(ContextHandle: VoidPtr, Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqMaxCalls(Binding: VoidPtr, MaxCalls: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqObject(Binding: VoidPtr, ObjectUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingReset(Binding: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetObject(Binding: VoidPtr, ObjectUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqDefaultProtectLevel(AuthnSvc: UInt32, AuthnLevel: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingToStringBindingA(Binding: VoidPtr, StringBinding: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingToStringBindingW(Binding: VoidPtr, StringBinding: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingToStringBinding = UnicodeAlias('RpcBindingToStringBindingW')
@winfunctype('RPCRT4.dll')
def RpcBindingVectorFree(BindingVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringBindingComposeA(ObjUuid: win32more.Windows.Win32.Foundation.PSTR, ProtSeq: win32more.Windows.Win32.Foundation.PSTR, NetworkAddr: win32more.Windows.Win32.Foundation.PSTR, Endpoint: win32more.Windows.Win32.Foundation.PSTR, Options: win32more.Windows.Win32.Foundation.PSTR, StringBinding: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringBindingComposeW(ObjUuid: win32more.Windows.Win32.Foundation.PWSTR, ProtSeq: win32more.Windows.Win32.Foundation.PWSTR, NetworkAddr: win32more.Windows.Win32.Foundation.PWSTR, Endpoint: win32more.Windows.Win32.Foundation.PWSTR, Options: win32more.Windows.Win32.Foundation.PWSTR, StringBinding: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcStringBindingCompose = UnicodeAlias('RpcStringBindingComposeW')
@winfunctype('RPCRT4.dll')
def RpcStringBindingParseA(StringBinding: win32more.Windows.Win32.Foundation.PSTR, ObjUuid: POINTER(win32more.Windows.Win32.Foundation.PSTR), Protseq: POINTER(win32more.Windows.Win32.Foundation.PSTR), NetworkAddr: POINTER(win32more.Windows.Win32.Foundation.PSTR), Endpoint: POINTER(win32more.Windows.Win32.Foundation.PSTR), NetworkOptions: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringBindingParseW(StringBinding: win32more.Windows.Win32.Foundation.PWSTR, ObjUuid: POINTER(win32more.Windows.Win32.Foundation.PWSTR), Protseq: POINTER(win32more.Windows.Win32.Foundation.PWSTR), NetworkAddr: POINTER(win32more.Windows.Win32.Foundation.PWSTR), Endpoint: POINTER(win32more.Windows.Win32.Foundation.PWSTR), NetworkOptions: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcStringBindingParse = UnicodeAlias('RpcStringBindingParseW')
@winfunctype('RPCRT4.dll')
def RpcStringFreeA(String: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcStringFreeW(String: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcStringFree = UnicodeAlias('RpcStringFreeW')
@winfunctype('RPCRT4.dll')
def RpcIfInqId(RpcIfHandle: VoidPtr, RpcIfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkIsProtseqValidA(Protseq: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkIsProtseqValidW(Protseq: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNetworkIsProtseqValid = UnicodeAlias('RpcNetworkIsProtseqValidW')
@winfunctype('RPCRT4.dll')
def RpcMgmtInqComTimeout(Binding: VoidPtr, Timeout: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetComTimeout(Binding: VoidPtr, Timeout: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetCancelTimeout(Timeout: Int32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkInqProtseqsA(ProtseqVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORA))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNetworkInqProtseqsW(ProtseqVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORW))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNetworkInqProtseqs = UnicodeAlias('RpcNetworkInqProtseqsW')
@winfunctype('RPCRT4.dll')
def RpcObjectInqType(ObjUuid: POINTER(Guid), TypeUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcObjectSetInqFn(InquiryFn: win32more.Windows.Win32.System.Rpc.RPC_OBJECT_INQ_FN) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcObjectSetType(ObjUuid: POINTER(Guid), TypeUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcProtseqVectorFreeA(ProtseqVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORA))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcProtseqVectorFreeW(ProtseqVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_PROTSEQ_VECTORW))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcProtseqVectorFree = UnicodeAlias('RpcProtseqVectorFreeW')
@winfunctype('RPCRT4.dll')
def RpcServerInqBindings(BindingVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqBindingsEx(SecurityDescriptor: VoidPtr, BindingVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqIf(IfSpec: VoidPtr, MgrTypeUuid: POINTER(Guid), MgrEpv: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerListen(MinimumCallThreads: UInt32, MaxCalls: UInt32, DontWait: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIf(IfSpec: VoidPtr, MgrTypeUuid: POINTER(Guid), MgrEpv: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIfEx(IfSpec: VoidPtr, MgrTypeUuid: POINTER(Guid), MgrEpv: VoidPtr, Flags: UInt32, MaxCalls: UInt32, IfCallback: win32more.Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIf2(IfSpec: VoidPtr, MgrTypeUuid: POINTER(Guid), MgrEpv: VoidPtr, Flags: UInt32, MaxCalls: UInt32, MaxRpcSize: UInt32, IfCallbackFn: win32more.Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterIf3(IfSpec: VoidPtr, MgrTypeUuid: POINTER(Guid), MgrEpv: VoidPtr, Flags: UInt32, MaxCalls: UInt32, MaxRpcSize: UInt32, IfCallback: win32more.Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUnregisterIf(IfSpec: VoidPtr, MgrTypeUuid: POINTER(Guid), WaitForCallsToComplete: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUnregisterIfEx(IfSpec: VoidPtr, MgrTypeUuid: POINTER(Guid), RundownContextHandles: Int32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqs(MaxCalls: UInt32, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqsEx(MaxCalls: UInt32, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqsIf(MaxCalls: UInt32, IfSpec: VoidPtr, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseAllProtseqsIfEx(MaxCalls: UInt32, IfSpec: VoidPtr, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqA(Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqExA(Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqW(Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerUseProtseq = UnicodeAlias('RpcServerUseProtseqW')
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqExW(Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerUseProtseqEx = UnicodeAlias('RpcServerUseProtseqExW')
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpA(Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, Endpoint: win32more.Windows.Win32.Foundation.PSTR, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpExA(Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, Endpoint: win32more.Windows.Win32.Foundation.PSTR, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpW(Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, Endpoint: win32more.Windows.Win32.Foundation.PWSTR, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerUseProtseqEp = UnicodeAlias('RpcServerUseProtseqEpW')
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqEpExW(Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, Endpoint: win32more.Windows.Win32.Foundation.PWSTR, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerUseProtseqEpEx = UnicodeAlias('RpcServerUseProtseqEpExW')
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfA(Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, IfSpec: VoidPtr, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfExA(Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, IfSpec: VoidPtr, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfW(Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, IfSpec: VoidPtr, SecurityDescriptor: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerUseProtseqIf = UnicodeAlias('RpcServerUseProtseqIfW')
@winfunctype('RPCRT4.dll')
def RpcServerUseProtseqIfExW(Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, IfSpec: VoidPtr, SecurityDescriptor: VoidPtr, Policy: POINTER(win32more.Windows.Win32.System.Rpc.RPC_POLICY)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerUseProtseqIfEx = UnicodeAlias('RpcServerUseProtseqIfExW')
@winfunctype('RPCRT4.dll')
def RpcServerYield() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtStatsVectorFree(StatsVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATS_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqStats(Binding: VoidPtr, Statistics: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATS_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtIsServerListening(Binding: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtStopServerListening(Binding: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtWaitServerListen() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetServerStackSize(ThreadStackSize: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsDontSerializeContext() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEnableIdleCleanup() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqIfIds(Binding: VoidPtr, IfIdVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcIfIdVectorFree(IfIdVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqServerPrincNameA(Binding: VoidPtr, AuthnSvc: UInt32, ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtInqServerPrincNameW(Binding: VoidPtr, AuthnSvc: UInt32, ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcMgmtInqServerPrincName = UnicodeAlias('RpcMgmtInqServerPrincNameW')
@winfunctype('RPCRT4.dll')
def RpcServerInqDefaultPrincNameA(AuthnSvc: UInt32, PrincName: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqDefaultPrincNameW(AuthnSvc: UInt32, PrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerInqDefaultPrincName = UnicodeAlias('RpcServerInqDefaultPrincNameW')
@winfunctype('RPCRT4.dll')
def RpcEpResolveBinding(Binding: VoidPtr, IfSpec: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNsBindingInqEntryNameA(Binding: VoidPtr, EntryNameSyntax: UInt32, EntryName: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcNsBindingInqEntryNameW(Binding: VoidPtr, EntryNameSyntax: UInt32, EntryName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsBindingInqEntryName = UnicodeAlias('RpcNsBindingInqEntryNameW')
@winfunctype('RPCRT4.dll')
def RpcBindingCreateA(Template: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_A), Security: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_A), Options: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_V1), Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingCreateW(Template: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_TEMPLATE_V1_W), Security: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_SECURITY_V1_W), Options: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_V1), Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingCreate = UnicodeAlias('RpcBindingCreateW')
@winfunctype('RPCRT4.dll')
def RpcServerInqBindingHandle(Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcImpersonateClient(BindingHandle: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcImpersonateClient2(BindingHandle: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRevertToSelfEx(BindingHandle: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRevertToSelf() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcImpersonateClientContainer(BindingHandle: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRevertContainerImpersonation() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientA(ClientBinding: VoidPtr, Privs: POINTER(VoidPtr), ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientW(ClientBinding: VoidPtr, Privs: POINTER(VoidPtr), ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingInqAuthClient = UnicodeAlias('RpcBindingInqAuthClientW')
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientExA(ClientBinding: VoidPtr, Privs: POINTER(VoidPtr), ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32), Flags: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthClientExW(ClientBinding: VoidPtr, Privs: POINTER(VoidPtr), ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthzSvc: POINTER(UInt32), Flags: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingInqAuthClientEx = UnicodeAlias('RpcBindingInqAuthClientExW')
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoA(Binding: VoidPtr, ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(VoidPtr), AuthzSvc: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoW(Binding: VoidPtr, ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(VoidPtr), AuthzSvc: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingInqAuthInfo = UnicodeAlias('RpcBindingInqAuthInfoW')
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoA(Binding: VoidPtr, ServerPrincName: win32more.Windows.Win32.Foundation.PSTR, AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: VoidPtr, AuthzSvc: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoExA(Binding: VoidPtr, ServerPrincName: win32more.Windows.Win32.Foundation.PSTR, AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: VoidPtr, AuthzSvc: UInt32, SecurityQos: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SECURITY_QOS)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoW(Binding: VoidPtr, ServerPrincName: win32more.Windows.Win32.Foundation.PWSTR, AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: VoidPtr, AuthzSvc: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingSetAuthInfo = UnicodeAlias('RpcBindingSetAuthInfoW')
@winfunctype('RPCRT4.dll')
def RpcBindingSetAuthInfoExW(Binding: VoidPtr, ServerPrincName: win32more.Windows.Win32.Foundation.PWSTR, AuthnLevel: UInt32, AuthnSvc: UInt32, AuthIdentity: VoidPtr, AuthzSvc: UInt32, SecurityQOS: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SECURITY_QOS)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingSetAuthInfoEx = UnicodeAlias('RpcBindingSetAuthInfoExW')
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoExA(Binding: VoidPtr, ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(VoidPtr), AuthzSvc: POINTER(UInt32), RpcQosVersion: UInt32, SecurityQOS: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SECURITY_QOS)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingInqAuthInfoExW(Binding: VoidPtr, ServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), AuthnLevel: POINTER(UInt32), AuthnSvc: POINTER(UInt32), AuthIdentity: POINTER(VoidPtr), AuthzSvc: POINTER(UInt32), RpcQosVersion: UInt32, SecurityQOS: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SECURITY_QOS)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcBindingInqAuthInfoEx = UnicodeAlias('RpcBindingInqAuthInfoExW')
@winfunctype('RPCRT4.dll')
def RpcServerCompleteSecurityCallback(BindingHandle: VoidPtr, Status: win32more.Windows.Win32.System.Rpc.RPC_STATUS) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterAuthInfoA(ServerPrincName: win32more.Windows.Win32.Foundation.PSTR, AuthnSvc: UInt32, GetKeyFn: win32more.Windows.Win32.System.Rpc.RPC_AUTH_KEY_RETRIEVAL_FN, Arg: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerRegisterAuthInfoW(ServerPrincName: win32more.Windows.Win32.Foundation.PWSTR, AuthnSvc: UInt32, GetKeyFn: win32more.Windows.Win32.System.Rpc.RPC_AUTH_KEY_RETRIEVAL_FN, Arg: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerRegisterAuthInfo = UnicodeAlias('RpcServerRegisterAuthInfoW')
@winfunctype('RPCRT4.dll')
def RpcBindingServerFromClient(ClientBinding: VoidPtr, ServerBinding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcRaiseException(exception: win32more.Windows.Win32.System.Rpc.RPC_STATUS) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcTestCancel() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerTestCancel(BindingHandle: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcCancelThread(Thread: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcCancelThreadEx(Thread: VoidPtr, Timeout: Int32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidCreate(Uuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidCreateSequential(Uuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidToStringA(Uuid: POINTER(Guid), StringUuid: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidFromStringA(StringUuid: win32more.Windows.Win32.Foundation.PSTR, Uuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidToStringW(Uuid: POINTER(Guid), StringUuid: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
UuidToString = UnicodeAlias('UuidToStringW')
@winfunctype('RPCRT4.dll')
def UuidFromStringW(StringUuid: win32more.Windows.Win32.Foundation.PWSTR, Uuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
UuidFromString = UnicodeAlias('UuidFromStringW')
@winfunctype('RPCRT4.dll')
def UuidCompare(Uuid1: POINTER(Guid), Uuid2: POINTER(Guid), Status: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def UuidCreateNil(NilUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def UuidEqual(Uuid1: POINTER(Guid), Uuid2: POINTER(Guid), Status: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def UuidHash(Uuid: POINTER(Guid), Status: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> UInt16: ...
@winfunctype('RPCRT4.dll')
def UuidIsNil(Uuid: POINTER(Guid), Status: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def RpcEpRegisterNoReplaceA(IfSpec: VoidPtr, BindingVector: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), UuidVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR), Annotation: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcEpRegisterNoReplaceW(IfSpec: VoidPtr, BindingVector: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), UuidVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR), Annotation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcEpRegisterNoReplace = UnicodeAlias('RpcEpRegisterNoReplaceW')
@winfunctype('RPCRT4.dll')
def RpcEpRegisterA(IfSpec: VoidPtr, BindingVector: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), UuidVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR), Annotation: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcEpRegisterW(IfSpec: VoidPtr, BindingVector: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), UuidVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR), Annotation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcEpRegister = UnicodeAlias('RpcEpRegisterW')
@winfunctype('RPCRT4.dll')
def RpcEpUnregister(IfSpec: VoidPtr, BindingVector: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), UuidVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def DceErrorInqTextA(RpcStatus: win32more.Windows.Win32.System.Rpc.RPC_STATUS, ErrorText: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def DceErrorInqTextW(RpcStatus: win32more.Windows.Win32.System.Rpc.RPC_STATUS, ErrorText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
DceErrorInqText = UnicodeAlias('DceErrorInqTextW')
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqBegin(EpBinding: VoidPtr, InquiryType: UInt32, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), VersOption: UInt32, ObjectUuid: POINTER(Guid), InquiryContext: POINTER(POINTER(VoidPtr))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqDone(InquiryContext: POINTER(POINTER(VoidPtr))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqNextA(InquiryContext: POINTER(VoidPtr), IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), Binding: POINTER(VoidPtr), ObjectUuid: POINTER(Guid), Annotation: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtEpEltInqNextW(InquiryContext: POINTER(VoidPtr), IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), Binding: POINTER(VoidPtr), ObjectUuid: POINTER(Guid), Annotation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcMgmtEpEltInqNext = UnicodeAlias('RpcMgmtEpEltInqNextW')
@winfunctype('RPCRT4.dll')
def RpcMgmtEpUnregister(EpBinding: VoidPtr, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), Binding: VoidPtr, ObjectUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcMgmtSetAuthorizationFn(AuthorizationFn: win32more.Windows.Win32.System.Rpc.RPC_MGMT_AUTHORIZATION_FN) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcExceptionFilter(ExceptionCode: UInt32) -> Int32: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupCreateW(Interfaces: POINTER(win32more.Windows.Win32.System.Rpc.RPC_INTERFACE_TEMPLATEW), NumIfs: UInt32, Endpoints: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ENDPOINT_TEMPLATEW), NumEndpoints: UInt32, IdlePeriod: UInt32, IdleCallbackFn: win32more.Windows.Win32.System.Rpc.RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN, IdleCallbackContext: VoidPtr, IfGroup: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerInterfaceGroupCreate = UnicodeAlias('RpcServerInterfaceGroupCreateW')
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupCreateA(Interfaces: POINTER(win32more.Windows.Win32.System.Rpc.RPC_INTERFACE_TEMPLATEA), NumIfs: UInt32, Endpoints: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ENDPOINT_TEMPLATEA), NumEndpoints: UInt32, IdlePeriod: UInt32, IdleCallbackFn: win32more.Windows.Win32.System.Rpc.RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN, IdleCallbackContext: VoidPtr, IfGroup: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupClose(IfGroup: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupActivate(IfGroup: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupDeactivate(IfGroup: VoidPtr, ForceDeactivation: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInterfaceGroupInqBindings(IfGroup: VoidPtr, BindingVector: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcNegotiateTransferSyntax(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetBuffer(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetBufferWithObject(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), ObjectUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSendReceive(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcFreeBuffer(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSend(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcReceive(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), Size: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcFreePipeBuffer(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcReallocPipeBuffer(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), NewSize: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcRequestMutex(Mutex: POINTER(VoidPtr)) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcClearMutex(Mutex: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcDeleteMutex(Mutex: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcAllocate(Size: UInt32) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def I_RpcFree(Object: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcPauseExecution(Milliseconds: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetExtendedError() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSystemHandleTypeSpecificWork(Handle: VoidPtr, ActualType: Byte, IdlType: Byte, MarshalDirection: win32more.Windows.Win32.System.Rpc.LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetCurrentCallHandle() -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def I_RpcNsInterfaceExported(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), RpcInterfaceInformation: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SERVER_INTERFACE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcNsInterfaceUnexported(EntryNameSyntax: UInt32, EntryName: POINTER(UInt16), RpcInterfaceInformation: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SERVER_INTERFACE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingToStaticStringBindingW(Binding: VoidPtr, StringBinding: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqSecurityContext(Binding: VoidPtr, SecurityContextHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqSecurityContextKeyInfo(Binding: VoidPtr, KeyInfo: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqWireIdForSnego(Binding: VoidPtr, WireId: POINTER(Byte)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqMarshalledTargetInfo(Binding: VoidPtr, MarshalledTargetInfoSize: POINTER(UInt32), MarshalledTargetInfo: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqLocalClientPID(Binding: VoidPtr, Pid: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingHandleToAsyncHandle(Binding: VoidPtr, AsyncHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcNsBindingSetEntryNameW(Binding: VoidPtr, EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
I_RpcNsBindingSetEntryName = UnicodeAlias('I_RpcNsBindingSetEntryNameW')
@winfunctype('RPCRT4.dll')
def I_RpcNsBindingSetEntryNameA(Binding: VoidPtr, EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseqEp2A(NetworkAddress: win32more.Windows.Win32.Foundation.PSTR, Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, Endpoint: win32more.Windows.Win32.Foundation.PSTR, SecurityDescriptor: VoidPtr, Policy: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseqEp2W(NetworkAddress: win32more.Windows.Win32.Foundation.PWSTR, Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, Endpoint: win32more.Windows.Win32.Foundation.PWSTR, SecurityDescriptor: VoidPtr, Policy: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
I_RpcServerUseProtseqEp2 = UnicodeAlias('I_RpcServerUseProtseqEp2W')
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseq2W(NetworkAddress: win32more.Windows.Win32.Foundation.PWSTR, Protseq: win32more.Windows.Win32.Foundation.PWSTR, MaxCalls: UInt32, SecurityDescriptor: VoidPtr, Policy: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
I_RpcServerUseProtseq2 = UnicodeAlias('I_RpcServerUseProtseq2W')
@winfunctype('RPCRT4.dll')
def I_RpcServerUseProtseq2A(NetworkAddress: win32more.Windows.Win32.Foundation.PSTR, Protseq: win32more.Windows.Win32.Foundation.PSTR, MaxCalls: UInt32, SecurityDescriptor: VoidPtr, Policy: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerStartService(Protseq: win32more.Windows.Win32.Foundation.PWSTR, Endpoint: win32more.Windows.Win32.Foundation.PWSTR, IfSpec: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqDynamicEndpointW(Binding: VoidPtr, DynamicEndpoint: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
I_RpcBindingInqDynamicEndpoint = UnicodeAlias('I_RpcBindingInqDynamicEndpointW')
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqDynamicEndpointA(Binding: VoidPtr, DynamicEndpoint: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerCheckClientRestriction(Context: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqTransportType(Binding: VoidPtr, Type: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcIfInqTransferSyntaxes(RpcIfHandle: VoidPtr, TransferSyntaxes: POINTER(win32more.Windows.Win32.System.Rpc.RPC_TRANSFER_SYNTAX), TransferSyntaxSize: UInt32, TransferSyntaxCount: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_UuidCreate(Uuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingCopy(SourceBinding: VoidPtr, DestinationBinding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingIsClientLocal(BindingHandle: VoidPtr, ClientLocalFlag: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingCreateNP(ServerName: win32more.Windows.Win32.Foundation.PWSTR, ServiceName: win32more.Windows.Win32.Foundation.PWSTR, NetworkOptions: win32more.Windows.Win32.Foundation.PWSTR, Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSsDontSerializeContext() -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerRegisterForwardFunction(pForwardFunction: POINTER(win32more.Windows.Win32.System.Rpc.RPC_FORWARD_FUNCTION)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqAddressChangeFn() -> POINTER(win32more.Windows.Win32.System.Rpc.RPC_ADDRESS_CHANGE_FN): ...
@winfunctype('RPCRT4.dll')
def I_RpcServerSetAddressChangeFn(pAddressChangeFn: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ADDRESS_CHANGE_FN)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqLocalConnAddress(Binding: VoidPtr, Buffer: VoidPtr, BufferSize: POINTER(UInt32), AddressFormat: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqRemoteConnAddress(Binding: VoidPtr, Buffer: VoidPtr, BufferSize: POINTER(UInt32), AddressFormat: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcSessionStrictContextHandle() -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcTurnOnEEInfoPropagation() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerInqTransportType(Type: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcMapWin32Status(Status: win32more.Windows.Win32.System.Rpc.RPC_STATUS) -> Int32: ...
@winfunctype('RPCRT4.dll')
def I_RpcRecordCalloutFailure(RpcStatus: win32more.Windows.Win32.System.Rpc.RPC_STATUS, CallOutState: POINTER(win32more.Windows.Win32.System.Rpc.RDR_CALLOUT_STATE), DllName: POINTER(UInt16)) -> Void: ...
@winfunctype('RPCRT4.dll')
def I_RpcMgmtEnableDedicatedThreadPool() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcGetDefaultSD(ppSecurityDescriptor: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcOpenClientProcess(Binding: VoidPtr, DesiredAccess: UInt32, ClientProcess: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingIsServerLocal(Binding: VoidPtr, ServerLocalFlag: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingSetPrivateOption(hBinding: VoidPtr, option: UInt32, optionValue: UIntPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerSubscribeForDisconnectNotification(Binding: VoidPtr, hEvent: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerGetAssociationID(Binding: VoidPtr, AssociationID: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerDisableExceptionFilter() -> Int32: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerSubscribeForDisconnectNotification2(Binding: VoidPtr, hEvent: VoidPtr, SubscriptionId: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcServerUnsubscribeForDisconnectNotification(Binding: VoidPtr, SubscriptionId: Guid) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfSpec: VoidPtr, BindingVec: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), ObjectUuidVec: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfSpec: VoidPtr, ObjectUuidVec: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfSpec: VoidPtr, BindingVec: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), ObjectUuidVec: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsBindingExport = UnicodeAlias('RpcNsBindingExportW')
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfSpec: VoidPtr, ObjectUuidVec: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsBindingUnexport = UnicodeAlias('RpcNsBindingUnexportW')
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportPnPA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfSpec: VoidPtr, ObjectVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportPnPA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfSpec: VoidPtr, ObjectVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingExportPnPW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfSpec: VoidPtr, ObjectVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsBindingExportPnP = UnicodeAlias('RpcNsBindingExportPnPW')
@winfunctype('RPCNS4.dll')
def RpcNsBindingUnexportPnPW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfSpec: VoidPtr, ObjectVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsBindingUnexportPnP = UnicodeAlias('RpcNsBindingUnexportPnPW')
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupBeginA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfSpec: VoidPtr, ObjUuid: POINTER(Guid), BindingMaxCount: UInt32, LookupContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupBeginW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfSpec: VoidPtr, ObjUuid: POINTER(Guid), BindingMaxCount: UInt32, LookupContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsBindingLookupBegin = UnicodeAlias('RpcNsBindingLookupBeginW')
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupNext(LookupContext: VoidPtr, BindingVec: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingLookupDone(LookupContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupDeleteA(GroupNameSyntax: win32more.Windows.Win32.System.Rpc.GROUP_NAME_SYNTAX, GroupName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrAddA(GroupNameSyntax: UInt32, GroupName: win32more.Windows.Win32.Foundation.PSTR, MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrRemoveA(GroupNameSyntax: UInt32, GroupName: win32more.Windows.Win32.Foundation.PSTR, MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqBeginA(GroupNameSyntax: UInt32, GroupName: win32more.Windows.Win32.Foundation.PSTR, MemberNameSyntax: UInt32, InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqNextA(InquiryContext: VoidPtr, MemberName: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsGroupDeleteW(GroupNameSyntax: win32more.Windows.Win32.System.Rpc.GROUP_NAME_SYNTAX, GroupName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsGroupDelete = UnicodeAlias('RpcNsGroupDeleteW')
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrAddW(GroupNameSyntax: UInt32, GroupName: win32more.Windows.Win32.Foundation.PWSTR, MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsGroupMbrAdd = UnicodeAlias('RpcNsGroupMbrAddW')
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrRemoveW(GroupNameSyntax: UInt32, GroupName: win32more.Windows.Win32.Foundation.PWSTR, MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsGroupMbrRemove = UnicodeAlias('RpcNsGroupMbrRemoveW')
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqBeginW(GroupNameSyntax: UInt32, GroupName: win32more.Windows.Win32.Foundation.PWSTR, MemberNameSyntax: UInt32, InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsGroupMbrInqBegin = UnicodeAlias('RpcNsGroupMbrInqBeginW')
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqNextW(InquiryContext: VoidPtr, MemberName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsGroupMbrInqNext = UnicodeAlias('RpcNsGroupMbrInqNextW')
@winfunctype('RPCNS4.dll')
def RpcNsGroupMbrInqDone(InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileDeleteA(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltAddA(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PSTR, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PSTR, Priority: UInt32, Annotation: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltRemoveA(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PSTR, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqBeginA(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PSTR, InquiryType: UInt32, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), VersOption: UInt32, MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PSTR, InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqNextA(InquiryContext: VoidPtr, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), MemberName: POINTER(win32more.Windows.Win32.Foundation.PSTR), Priority: POINTER(UInt32), Annotation: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsProfileDeleteW(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsProfileDelete = UnicodeAlias('RpcNsProfileDeleteW')
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltAddW(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PWSTR, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PWSTR, Priority: UInt32, Annotation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsProfileEltAdd = UnicodeAlias('RpcNsProfileEltAddW')
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltRemoveW(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PWSTR, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsProfileEltRemove = UnicodeAlias('RpcNsProfileEltRemoveW')
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqBeginW(ProfileNameSyntax: UInt32, ProfileName: win32more.Windows.Win32.Foundation.PWSTR, InquiryType: UInt32, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), VersOption: UInt32, MemberNameSyntax: UInt32, MemberName: win32more.Windows.Win32.Foundation.PWSTR, InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsProfileEltInqBegin = UnicodeAlias('RpcNsProfileEltInqBeginW')
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqNextW(InquiryContext: VoidPtr, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), MemberName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), Priority: POINTER(UInt32), Annotation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsProfileEltInqNext = UnicodeAlias('RpcNsProfileEltInqNextW')
@winfunctype('RPCNS4.dll')
def RpcNsProfileEltInqDone(InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqBeginA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqBeginW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsEntryObjectInqBegin = UnicodeAlias('RpcNsEntryObjectInqBeginW')
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqNext(InquiryContext: VoidPtr, ObjUuid: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryObjectInqDone(InquiryContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryExpandNameA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, ExpandedName: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtBindingUnexportA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), VersOption: UInt32, ObjectUuidVec: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryCreateA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryDeleteA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryInqIfIdsA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfIdVec: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtHandleSetExpAge(NsHandle: VoidPtr, ExpirationAge: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtInqExpAge(ExpirationAge: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsMgmtSetExpAge(ExpirationAge: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsEntryExpandNameW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, ExpandedName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsEntryExpandName = UnicodeAlias('RpcNsEntryExpandNameW')
@winfunctype('RPCNS4.dll')
def RpcNsMgmtBindingUnexportW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID), VersOption: UInt32, ObjectUuidVec: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsMgmtBindingUnexport = UnicodeAlias('RpcNsMgmtBindingUnexportW')
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryCreateW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsMgmtEntryCreate = UnicodeAlias('RpcNsMgmtEntryCreateW')
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryDeleteW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsMgmtEntryDelete = UnicodeAlias('RpcNsMgmtEntryDeleteW')
@winfunctype('RPCNS4.dll')
def RpcNsMgmtEntryInqIfIdsW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfIdVec: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID_VECTOR))) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsMgmtEntryInqIfIds = UnicodeAlias('RpcNsMgmtEntryInqIfIdsW')
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportBeginA(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PSTR, IfSpec: VoidPtr, ObjUuid: POINTER(Guid), ImportContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportBeginW(EntryNameSyntax: UInt32, EntryName: win32more.Windows.Win32.Foundation.PWSTR, IfSpec: VoidPtr, ObjUuid: POINTER(Guid), ImportContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcNsBindingImportBegin = UnicodeAlias('RpcNsBindingImportBeginW')
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportNext(ImportContext: VoidPtr, Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingImportDone(ImportContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def RpcNsBindingSelect(BindingVec: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR), Binding: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncRegisterInfo(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncInitializeHandle(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE), Size: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncGetCallStatus(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncCompleteCall(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE), Reply: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncAbortCall(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE), ExceptionCode: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcAsyncCancelCall(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE), fAbort: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorStartEnumeration(EnumHandle: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorGetNextRecord(EnumHandle: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE), CopyStrings: win32more.Windows.Win32.Foundation.BOOL, ErrorInfo: POINTER(win32more.Windows.Win32.System.Rpc.RPC_EXTENDED_ERROR_INFO)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorEndEnumeration(EnumHandle: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorResetEnumeration(EnumHandle: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorGetNumberOfRecords(EnumHandle: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE), Records: POINTER(Int32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorSaveErrorInfo(EnumHandle: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE), ErrorBlob: POINTER(VoidPtr), BlobSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorLoadErrorInfo(ErrorBlob: VoidPtr, BlobSize: UIntPtr, EnumHandle: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ERROR_ENUM_HANDLE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorAddRecord(ErrorInfo: POINTER(win32more.Windows.Win32.System.Rpc.RPC_EXTENDED_ERROR_INFO)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcErrorClearInformation() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcGetAuthorizationContextForClient(ClientBinding: VoidPtr, ImpersonateOnReturn: win32more.Windows.Win32.Foundation.BOOL, Reserved1: VoidPtr, pExpirationTime: POINTER(Int64), Reserved2: win32more.Windows.Win32.Foundation.LUID, Reserved3: UInt32, Reserved4: VoidPtr, pAuthzClientContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcFreeAuthorizationContext(pAuthzClientContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsContextLockExclusive(ServerBindingHandle: VoidPtr, UserContext: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsContextLockShared(ServerBindingHandle: VoidPtr, UserContext: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerInqCallAttributesW(ClientBinding: VoidPtr, RpcCallAttributes: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcServerInqCallAttributes = UnicodeAlias('RpcServerInqCallAttributesW')
@winfunctype('RPCRT4.dll')
def RpcServerInqCallAttributesA(ClientBinding: VoidPtr, RpcCallAttributes: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerSubscribeForNotification(Binding: VoidPtr, Notification: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATIONS, NotificationType: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES, NotificationInfo: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_NOTIFICATION_INFO)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcServerUnsubscribeForNotification(Binding: VoidPtr, Notification: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATIONS, NotificationsQueued: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingBind(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE), Binding: VoidPtr, IfSpec: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcBindingUnbind(Binding: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcAsyncSetHandle(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcAsyncAbortCall(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE), ExceptionCode: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def I_RpcExceptionFilter(ExceptionCode: UInt32) -> Int32: ...
@winfunctype('RPCRT4.dll')
def I_RpcBindingInqClientTokenAttributes(Binding: VoidPtr, TokenId: POINTER(win32more.Windows.Win32.Foundation.LUID), AuthenticationId: POINTER(win32more.Windows.Win32.Foundation.LUID), ModifiedId: POINTER(win32more.Windows.Win32.Foundation.LUID)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def I_RpcNsGetBuffer(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def I_RpcNsSendReceive(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), Handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCNS4.dll')
def I_RpcNsRaiseException(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), Status: win32more.Windows.Win32.System.Rpc.RPC_STATUS) -> Void: ...
@winfunctype('RPCNS4.dll')
def I_RpcReBindBuffer(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NDRCContextBinding(CContext: IntPtr) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def NDRCContextMarshall(CContext: IntPtr, pBuff: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRCContextUnmarshall(pCContext: POINTER(IntPtr), hBinding: VoidPtr, pBuff: VoidPtr, DataRepresentation: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextMarshall(CContext: POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT), pBuff: VoidPtr, userRunDownIn: win32more.Windows.Win32.System.Rpc.NDR_RUNDOWN) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextUnmarshall(pBuff: VoidPtr, DataRepresentation: UInt32) -> POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT): ...
@winfunctype('RPCRT4.dll')
def NDRSContextMarshallEx(BindingHandle: VoidPtr, CContext: POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT), pBuff: VoidPtr, userRunDownIn: win32more.Windows.Win32.System.Rpc.NDR_RUNDOWN) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextMarshall2(BindingHandle: VoidPtr, CContext: POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT), pBuff: VoidPtr, userRunDownIn: win32more.Windows.Win32.System.Rpc.NDR_RUNDOWN, CtxGuard: VoidPtr, Flags: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NDRSContextUnmarshallEx(BindingHandle: VoidPtr, pBuff: VoidPtr, DataRepresentation: UInt32) -> POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT): ...
@winfunctype('RPCRT4.dll')
def NDRSContextUnmarshall2(BindingHandle: VoidPtr, pBuff: VoidPtr, DataRepresentation: UInt32, CtxGuard: VoidPtr, Flags: UInt32) -> POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT): ...
@winfunctype('RPCRT4.dll')
def RpcSsDestroyClientContext(ContextHandle: POINTER(VoidPtr)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleTypeMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), FormatChar: Byte) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPointerMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrClientContextMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ContextHandle: IntPtr, fCheck: Int32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerContextMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ContextHandle: POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT), RundownRoutine: win32more.Windows.Win32.System.Rpc.NDR_RUNDOWN) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerContextNewMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ContextHandle: POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT), RundownRoutine: win32more.Windows.Win32.System.Rpc.NDR_RUNDOWN, pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleTypeUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), FormatChar: Byte) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRangeUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrCorrelationInitialize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: VoidPtr, CacheSize: UInt32, flags: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrCorrelationPass(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrCorrelationFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPointerUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(POINTER(Byte)), pFormat: POINTER(Byte), fMustAlloc: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrClientContextUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pContextHandle: POINTER(IntPtr), BindHandle: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerContextUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT): ...
@winfunctype('RPCRT4.dll')
def NdrContextHandleInitialize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT): ...
@winfunctype('RPCRT4.dll')
def NdrServerContextNewUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT): ...
@winfunctype('RPCRT4.dll')
def NdrPointerBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrContextHandleSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPointerMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStringMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrNonConformantStringMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerMemorySize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> UInt32: ...
@winfunctype('RPCRT4.dll')
def NdrPointerFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrSimpleStructFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantStructFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingStructFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexStructFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrFixedArrayFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantArrayFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConformantVaryingArrayFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrVaryingArrayFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrComplexArrayFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrEncapsulatedUnionFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrNonEncapsulatedUnionFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrByteCountPointerFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrXmitOrRepAsFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrInterfacePointerFree(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: POINTER(Byte), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConvert2(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte), NumberParams: Int32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrConvert(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrUserMarshalSimpleTypeConvert(pFlags: POINTER(UInt32), pBuffer: POINTER(Byte), FormatChar: Byte) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrClientInitializeNew(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), ProcNum: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializeNew(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializePartial(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), RequestedBufferSize: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrClientInitialize(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), ProcNum: UInt32) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerInitialize(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializeUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrServerInitializeMarshall(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrGetBuffer(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), BufferLength: UInt32, Handle: VoidPtr) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrNsGetBuffer(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), BufferLength: UInt32, Handle: VoidPtr) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrSendReceive(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pBufferEnd: POINTER(Byte)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrNsSendReceive(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pBufferEnd: POINTER(Byte), pAutoHandle: POINTER(VoidPtr)) -> POINTER(Byte): ...
@winfunctype('RPCRT4.dll')
def NdrFreeBuffer(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrGetDcomProtocolVersion(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pVersion: POINTER(win32more.Windows.Win32.System.Rpc.RPC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('RPCRT4.dll', variadic=True)
def NdrClientCall2(pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormat: POINTER(Byte), *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll', variadic=True)
def NdrAsyncClientCall(pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormat: POINTER(Byte), *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll', variadic=True)
def NdrDcomAsyncClientCall(pStubDescriptor: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormat: POINTER(Byte), *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def NdrAsyncServerCall(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrDcomAsyncStubCall(pThis: win32more.Windows.Win32.System.Com.IRpcStubBuffer, pChannel: win32more.Windows.Win32.System.Com.IRpcChannelBuffer, pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrStubCall2(pThis: VoidPtr, pChannel: VoidPtr, pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrServerCall2(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMapCommAndFaultStatus(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pCommStatus: POINTER(UInt32), pFaultStatus: POINTER(UInt32), Status: win32more.Windows.Win32.System.Rpc.RPC_STATUS) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSsAllocate(Size: UIntPtr) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def RpcSsDisableAllocate() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsEnableAllocate() -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsFree(NodeToFree: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsGetThreadHandle() -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def RpcSsSetClientAllocFree(ClientAlloc: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_FREE) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsSetThreadHandle(Id: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSsSwapClientAllocFree(ClientAlloc: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_FREE, OldClientAlloc: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC), OldClientFree: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CLIENT_FREE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcSmAllocate(Size: UIntPtr, pStatus: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def RpcSmClientFree(pNodeToFree: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmDestroyClientContext(ContextHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmDisableAllocate() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmEnableAllocate() -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmFree(NodeToFree: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmGetThreadHandle(pStatus: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def RpcSmSetClientAllocFree(ClientAlloc: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_FREE) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmSetThreadHandle(Id: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def RpcSmSwapClientAllocFree(ClientAlloc: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC, ClientFree: win32more.Windows.Win32.System.Rpc.RPC_CLIENT_FREE, OldClientAlloc: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CLIENT_ALLOC), OldClientFree: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CLIENT_FREE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsEnableAllocate(pMessage: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsDisableAllocate(pMessage: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSmSetClientToOsf(pMessage: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSmClientAllocate(Size: UIntPtr) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSmClientFree(NodeToFree: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsDefaultAllocate(Size: UIntPtr) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def NdrRpcSsDefaultFree(NodeToFree: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrFullPointerXlatInit(NumberOfPointers: UInt32, XlatSide: win32more.Windows.Win32.System.Rpc.XLAT_SIDE) -> POINTER(win32more.Windows.Win32.System.Rpc.FULL_PTR_XLAT_TABLES): ...
@winfunctype('RPCRT4.dll')
def NdrFullPointerXlatFree(pXlatTables: POINTER(win32more.Windows.Win32.System.Rpc.FULL_PTR_XLAT_TABLES)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrAllocate(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), Len: UIntPtr) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def NdrClearOutParameters(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pFormat: POINTER(Byte), ArgAddr: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrOleAllocate(Size: UIntPtr) -> VoidPtr: ...
@winfunctype('RPCRT4.dll')
def NdrOleFree(NodeToFree: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrGetUserMarshalInfo(pFlags: POINTER(UInt32), InformationLevel: UInt32, pMarshalInfo: POINTER(win32more.Windows.Win32.System.Rpc.NDR_USER_MARSHAL_INFO)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NdrCreateServerInterfaceFromStub(pStub: win32more.Windows.Win32.System.Com.IRpcStubBuffer, pServerIf: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SERVER_INTERFACE)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@cfunctype('RPCRT4.dll', variadic=True)
def NdrClientCall3(pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), nProcNum: UInt32, pReturnValue: VoidPtr, *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll', variadic=True)
def Ndr64AsyncClientCall(pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), nProcNum: UInt32, pReturnValue: VoidPtr, *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@cfunctype('RPCRT4.dll', variadic=True)
def Ndr64DcomAsyncClientCall(pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), nProcNum: UInt32, pReturnValue: VoidPtr, *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def Ndr64AsyncServerCall64(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def Ndr64AsyncServerCallAll(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def Ndr64DcomAsyncStubCall(pThis: win32more.Windows.Win32.System.Com.IRpcStubBuffer, pChannel: win32more.Windows.Win32.System.Com.IRpcChannelBuffer, pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrStubCall3(pThis: VoidPtr, pChannel: VoidPtr, pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE), pdwStubPhase: POINTER(UInt32)) -> Int32: ...
@winfunctype('RPCRT4.dll')
def NdrServerCallAll(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrServerCallNdr64(pRpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreClientMarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreServerUnmarshall(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(VoidPtr)) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreClientBufferSize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), pMemory: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrPartialIgnoreServerInitialize(pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE), ppMemory: POINTER(VoidPtr), pFormat: POINTER(Byte)) -> Void: ...
@winfunctype('RPCRT4.dll')
def RpcUserFree(AsyncHandle: VoidPtr, pBuffer: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def MesEncodeIncrementalHandleCreate(UserState: VoidPtr, AllocFn: win32more.Windows.Win32.System.Rpc.MIDL_ES_ALLOC, WriteFn: win32more.Windows.Win32.System.Rpc.MIDL_ES_WRITE, pHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesDecodeIncrementalHandleCreate(UserState: VoidPtr, ReadFn: win32more.Windows.Win32.System.Rpc.MIDL_ES_READ, pHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesIncrementalHandleReset(Handle: VoidPtr, UserState: VoidPtr, AllocFn: win32more.Windows.Win32.System.Rpc.MIDL_ES_ALLOC, WriteFn: win32more.Windows.Win32.System.Rpc.MIDL_ES_WRITE, ReadFn: win32more.Windows.Win32.System.Rpc.MIDL_ES_READ, Operation: win32more.Windows.Win32.System.Rpc.MIDL_ES_CODE) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesEncodeFixedBufferHandleCreate(pBuffer: win32more.Windows.Win32.Foundation.PSTR, BufferSize: UInt32, pEncodedSize: POINTER(UInt32), pHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesEncodeDynBufferHandleCreate(pBuffer: POINTER(POINTER(SByte)), pEncodedSize: POINTER(UInt32), pHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesDecodeBufferHandleCreate(Buffer: win32more.Windows.Win32.Foundation.PSTR, BufferSize: UInt32, pHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesBufferHandleReset(Handle: VoidPtr, HandleStyle: UInt32, Operation: win32more.Windows.Win32.System.Rpc.MIDL_ES_CODE, pBuffer: POINTER(POINTER(SByte)), BufferSize: UInt32, pEncodedSize: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesHandleFree(Handle: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def MesInqProcEncodingId(Handle: VoidPtr, pInterfaceId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER), pProcNum: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeAlignSize(param0: VoidPtr) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeDecode(Handle: VoidPtr, pObject: VoidPtr, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeEncode(Handle: VoidPtr, pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pObject: VoidPtr, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeAlignSize(Handle: VoidPtr, pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), pObject: VoidPtr) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeEncode(Handle: VoidPtr, pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), pObject: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeDecode(Handle: VoidPtr, pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), pObject: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeAlignSize2(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), pObject: VoidPtr) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeEncode2(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), pObject: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeDecode2(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), pObject: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeFree2(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), pObject: VoidPtr) -> Void: ...
@cfunctype('RPCRT4.dll', variadic=True)
def NdrMesProcEncodeDecode(Handle: VoidPtr, pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), *__arglist) -> Void: ...
@cfunctype('RPCRT4.dll', variadic=True)
def NdrMesProcEncodeDecode2(Handle: VoidPtr, pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC), pFormatString: POINTER(Byte), *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeAlignSize3(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: VoidPtr) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeEncode3(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeDecode3(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: VoidPtr) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesTypeFree3(Handle: VoidPtr, pPicklingInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_TYPE_PICKLING_INFO), pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), ArrTypeOffset: POINTER(POINTER(UInt32)), nTypeIndex: UInt32, pObject: VoidPtr) -> Void: ...
@cfunctype('RPCRT4.dll', variadic=True)
def NdrMesProcEncodeDecode3(Handle: VoidPtr, pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), nProcNum: UInt32, pReturnValue: VoidPtr, *__arglist) -> win32more.Windows.Win32.System.Rpc.CLIENT_CALL_RETURN: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeDecodeAll(Handle: VoidPtr, pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), pObject: VoidPtr, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeEncodeAll(Handle: VoidPtr, pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO), pObject: VoidPtr, Size: Int16) -> Void: ...
@winfunctype('RPCRT4.dll')
def NdrMesSimpleTypeAlignSizeAll(Handle: VoidPtr, pProxyInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUBLESS_PROXY_INFO)) -> UIntPtr: ...
@winfunctype('RPCRT4.dll')
def RpcCertGeneratePrincipalNameW(Context: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), Flags: UInt32, pBuffer: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RpcCertGeneratePrincipalName = UnicodeAlias('RpcCertGeneratePrincipalNameW')
@winfunctype('RPCRT4.dll')
def RpcCertGeneratePrincipalNameA(Context: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), Flags: UInt32, pBuffer: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
class BinaryParam(Structure):
    Buffer: VoidPtr
    Size: Int16
class CLIENT_CALL_RETURN(Union):
    Pointer: VoidPtr
    Simple: IntPtr
class COMM_FAULT_OFFSETS(Structure):
    CommOffset: Int16
    FaultOffset: Int16
@winfunctype_pointer
def CS_TAG_GETTING_ROUTINE(hBinding: VoidPtr, fServerSide: Int32, pulSendingTag: POINTER(UInt32), pulDesiredReceivingTag: POINTER(UInt32), pulReceivingTag: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_FROM_NETCS_ROUTINE(hBinding: VoidPtr, ulNetworkCodeSet: UInt32, pNetworkData: POINTER(Byte), ulNetworkDataLength: UInt32, ulLocalBufferSize: UInt32, pLocalData: VoidPtr, pulLocalDataLength: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_LOCAL_SIZE_ROUTINE(hBinding: VoidPtr, ulNetworkCodeSet: UInt32, ulNetworkBufferSize: UInt32, conversionType: POINTER(win32more.Windows.Win32.System.Rpc.IDL_CS_CONVERT), pulLocalBufferSize: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_NET_SIZE_ROUTINE(hBinding: VoidPtr, ulNetworkCodeSet: UInt32, ulLocalBufferSize: UInt32, conversionType: POINTER(win32more.Windows.Win32.System.Rpc.IDL_CS_CONVERT), pulNetworkBufferSize: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def CS_TYPE_TO_NETCS_ROUTINE(hBinding: VoidPtr, ulNetworkCodeSet: UInt32, pLocalData: VoidPtr, ulLocalDataLength: UInt32, pNetworkData: POINTER(Byte), pulNetworkDataLength: POINTER(UInt32), pStatus: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def EXPR_EVAL(param0: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
EXPR_TOKEN = Int32
FC_EXPR_START: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 0
FC_EXPR_ILLEGAL: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 0
FC_EXPR_CONST32: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 1
FC_EXPR_CONST64: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 2
FC_EXPR_VAR: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 3
FC_EXPR_OPER: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 4
FC_EXPR_NOOP: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 5
FC_EXPR_END: win32more.Windows.Win32.System.Rpc.EXPR_TOKEN = 6
ExtendedErrorParamTypes = Int32
eeptAnsiString: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes = 1
eeptUnicodeString: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes = 2
eeptLongVal: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes = 3
eeptShortVal: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes = 4
eeptPointerVal: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes = 5
eeptNone: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes = 6
eeptBinary: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes = 7
class FULL_PTR_XLAT_TABLES(Structure):
    RefIdToPointer: VoidPtr
    PointerToRefId: VoidPtr
    NextRefId: UInt32
    XlatSide: win32more.Windows.Win32.System.Rpc.XLAT_SIDE
class GENERIC_BINDING_INFO(Structure):
    pObj: VoidPtr
    Size: UInt32
    pfnBind: win32more.Windows.Win32.System.Rpc.GENERIC_BINDING_ROUTINE
    pfnUnbind: win32more.Windows.Win32.System.Rpc.GENERIC_UNBIND_ROUTINE
@winfunctype_pointer
def GENERIC_BINDING_ROUTINE(param0: VoidPtr) -> VoidPtr: ...
class GENERIC_BINDING_ROUTINE_PAIR(Structure):
    pfnBind: win32more.Windows.Win32.System.Rpc.GENERIC_BINDING_ROUTINE
    pfnUnbind: win32more.Windows.Win32.System.Rpc.GENERIC_UNBIND_ROUTINE
@winfunctype_pointer
def GENERIC_UNBIND_ROUTINE(param0: VoidPtr, param1: POINTER(Byte)) -> Void: ...
GROUP_NAME_SYNTAX = UInt32
RPC_C_NS_SYNTAX_DEFAULT: win32more.Windows.Win32.System.Rpc.GROUP_NAME_SYNTAX = 0
RPC_C_NS_SYNTAX_DCE: win32more.Windows.Win32.System.Rpc.GROUP_NAME_SYNTAX = 3
IDL_CS_CONVERT = Int32
IDL_CS_NO_CONVERT: win32more.Windows.Win32.System.Rpc.IDL_CS_CONVERT = 0
IDL_CS_IN_PLACE_CONVERT: win32more.Windows.Win32.System.Rpc.IDL_CS_CONVERT = 1
IDL_CS_NEW_BUFFER_CONVERT: win32more.Windows.Win32.System.Rpc.IDL_CS_CONVERT = 2
@winfunctype_pointer
def I_RpcFreeCalloutStateFn(CallOutState: POINTER(win32more.Windows.Win32.System.Rpc.RDR_CALLOUT_STATE)) -> Void: ...
@winfunctype_pointer
def I_RpcPerformCalloutFn(Context: VoidPtr, CallOutState: POINTER(win32more.Windows.Win32.System.Rpc.RDR_CALLOUT_STATE), Stage: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
class I_RpcProxyCallbackInterface(Structure):
    IsValidMachineFn: win32more.Windows.Win32.System.Rpc.I_RpcProxyIsValidMachineFn
    GetClientAddressFn: win32more.Windows.Win32.System.Rpc.I_RpcProxyGetClientAddressFn
    GetConnectionTimeoutFn: win32more.Windows.Win32.System.Rpc.I_RpcProxyGetConnectionTimeoutFn
    PerformCalloutFn: win32more.Windows.Win32.System.Rpc.I_RpcPerformCalloutFn
    FreeCalloutStateFn: win32more.Windows.Win32.System.Rpc.I_RpcFreeCalloutStateFn
    GetClientSessionAndResourceUUIDFn: win32more.Windows.Win32.System.Rpc.I_RpcProxyGetClientSessionAndResourceUUID
    ProxyFilterIfFn: win32more.Windows.Win32.System.Rpc.I_RpcProxyFilterIfFn
    RpcProxyUpdatePerfCounterFn: win32more.Windows.Win32.System.Rpc.I_RpcProxyUpdatePerfCounterFn
    RpcProxyUpdatePerfCounterBackendServerFn: win32more.Windows.Win32.System.Rpc.I_RpcProxyUpdatePerfCounterBackendServerFn
@winfunctype_pointer
def I_RpcProxyFilterIfFn(Context: VoidPtr, IfUuid: POINTER(Guid), IfMajorVersion: UInt16, fAllow: POINTER(Int32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyGetClientAddressFn(Context: VoidPtr, Buffer: win32more.Windows.Win32.Foundation.PSTR, BufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyGetClientSessionAndResourceUUID(Context: VoidPtr, SessionIdPresent: POINTER(Int32), SessionId: POINTER(Guid), ResourceIdPresent: POINTER(Int32), ResourceId: POINTER(Guid)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyGetConnectionTimeoutFn(ConnectionTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyIsValidMachineFn(Machine: win32more.Windows.Win32.Foundation.PWSTR, DotMachine: win32more.Windows.Win32.Foundation.PWSTR, PortNumber: UInt32) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def I_RpcProxyUpdatePerfCounterBackendServerFn(MachineName: POINTER(UInt16), IsConnectEvent: Int32) -> Void: ...
@winfunctype_pointer
def I_RpcProxyUpdatePerfCounterFn(Counter: win32more.Windows.Win32.System.Rpc.RpcPerfCounters, ModifyTrend: Int32, Size: UInt32) -> Void: ...
LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION = Int32
MarshalDirectionMarshal: win32more.Windows.Win32.System.Rpc.LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION = 0
MarshalDirectionUnmarshal: win32more.Windows.Win32.System.Rpc.LRPC_SYSTEM_HANDLE_MARSHAL_DIRECTION = 1
class MALLOC_FREE_STRUCT(Structure):
    pfnAllocate: IntPtr
    pfnFree: IntPtr
@winfunctype_pointer
def MIDL_ES_ALLOC(state: VoidPtr, pbuffer: POINTER(POINTER(SByte)), psize: POINTER(UInt32)) -> Void: ...
MIDL_ES_CODE = Int32
MES_ENCODE: win32more.Windows.Win32.System.Rpc.MIDL_ES_CODE = 0
MES_DECODE: win32more.Windows.Win32.System.Rpc.MIDL_ES_CODE = 1
MES_ENCODE_NDR64: win32more.Windows.Win32.System.Rpc.MIDL_ES_CODE = 2
MIDL_ES_HANDLE_STYLE = Int32
MES_INCREMENTAL_HANDLE: win32more.Windows.Win32.System.Rpc.MIDL_ES_HANDLE_STYLE = 0
MES_FIXED_BUFFER_HANDLE: win32more.Windows.Win32.System.Rpc.MIDL_ES_HANDLE_STYLE = 1
MES_DYNAMIC_BUFFER_HANDLE: win32more.Windows.Win32.System.Rpc.MIDL_ES_HANDLE_STYLE = 2
@winfunctype_pointer
def MIDL_ES_READ(state: VoidPtr, pbuffer: POINTER(POINTER(SByte)), psize: POINTER(UInt32)) -> Void: ...
@winfunctype_pointer
def MIDL_ES_WRITE(state: VoidPtr, buffer: win32more.Windows.Win32.Foundation.PSTR, size: UInt32) -> Void: ...
class MIDL_FORMAT_STRING(Structure):
    Pad: Int16
    Format: Byte * 1
class MIDL_INTERCEPTION_INFO(Structure):
    Version: UInt32
    ProcString: POINTER(Byte)
    ProcFormatOffsetTable: POINTER(UInt16)
    ProcCount: UInt32
    TypeString: POINTER(Byte)
class MIDL_INTERFACE_METHOD_PROPERTIES(Structure):
    MethodCount: UInt16
    MethodProperties: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.MIDL_METHOD_PROPERTY_MAP))
class MIDL_METHOD_PROPERTY(Structure):
    Id: UInt32
    Value: UIntPtr
class MIDL_METHOD_PROPERTY_MAP(Structure):
    Count: UInt32
    Properties: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_METHOD_PROPERTY)
class MIDL_SERVER_INFO(Structure):
    pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC)
    DispatchTable: POINTER(win32more.Windows.Win32.System.Rpc.SERVER_ROUTINE)
    ProcString: POINTER(Byte)
    FmtStringOffset: POINTER(UInt16)
    ThunkTable: POINTER(win32more.Windows.Win32.System.Rpc.STUB_THUNK)
    pTransferSyntax: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER)
    nCount: UIntPtr
    pSyntaxInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_SYNTAX_INFO)
class MIDL_STUBLESS_PROXY_INFO(Structure):
    pStubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC)
    ProcFormatString: POINTER(Byte)
    FormatStringOffset: POINTER(UInt16)
    pTransferSyntax: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER)
    nCount: UIntPtr
    pSyntaxInfo: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_SYNTAX_INFO)
class MIDL_STUB_DESC(Structure):
    RpcInterfaceInformation: VoidPtr
    pfnAllocate: win32more.Windows.Win32.System.Rpc.PFN_RPC_ALLOCATE
    pfnFree: win32more.Windows.Win32.System.Rpc.PFN_RPC_FREE
    IMPLICIT_HANDLE_INFO: _IMPLICIT_HANDLE_INFO_e__Union
    apfnNdrRundownRoutines: POINTER(win32more.Windows.Win32.System.Rpc.NDR_RUNDOWN)
    aGenericBindingRoutinePairs: POINTER(win32more.Windows.Win32.System.Rpc.GENERIC_BINDING_ROUTINE_PAIR)
    apfnExprEval: POINTER(win32more.Windows.Win32.System.Rpc.EXPR_EVAL)
    aXmitQuintuple: POINTER(win32more.Windows.Win32.System.Rpc.XMIT_ROUTINE_QUINTUPLE)
    pFormatTypes: POINTER(Byte)
    fCheckBounds: Int32
    Version: UInt32
    pMallocFreeStruct: POINTER(win32more.Windows.Win32.System.Rpc.MALLOC_FREE_STRUCT)
    MIDLVersion: Int32
    CommFaultOffsets: POINTER(win32more.Windows.Win32.System.Rpc.COMM_FAULT_OFFSETS)
    aUserMarshalQuadruple: POINTER(win32more.Windows.Win32.System.Rpc.USER_MARSHAL_ROUTINE_QUADRUPLE)
    NotifyRoutineTable: POINTER(win32more.Windows.Win32.System.Rpc.NDR_NOTIFY_ROUTINE)
    mFlags: UIntPtr
    CsRoutineTables: POINTER(win32more.Windows.Win32.System.Rpc.NDR_CS_ROUTINES)
    ProxyServerInfo: VoidPtr
    pExprInfo: POINTER(win32more.Windows.Win32.System.Rpc.NDR_EXPR_DESC)
    class _IMPLICIT_HANDLE_INFO_e__Union(Union):
        pAutoHandle: POINTER(VoidPtr)
        pPrimitiveHandle: POINTER(VoidPtr)
        pGenericBindingInfo: POINTER(win32more.Windows.Win32.System.Rpc.GENERIC_BINDING_INFO)
class MIDL_STUB_MESSAGE(Structure):
    RpcMsg: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)
    Buffer: POINTER(Byte)
    BufferStart: POINTER(Byte)
    BufferEnd: POINTER(Byte)
    BufferMark: POINTER(Byte)
    BufferLength: UInt32
    MemorySize: UInt32
    Memory: POINTER(Byte)
    IsClient: Byte
    Pad: Byte
    uFlags2: UInt16
    ReuseBuffer: Int32
    pAllocAllNodesContext: POINTER(win32more.Windows.Win32.System.Rpc.NDR_ALLOC_ALL_NODES_CONTEXT)
    pPointerQueueState: POINTER(win32more.Windows.Win32.System.Rpc.NDR_POINTER_QUEUE_STATE)
    IgnoreEmbeddedPointers: Int32
    PointerBufferMark: POINTER(Byte)
    CorrDespIncrement: Byte
    uFlags: Byte
    UniquePtrCount: UInt16
    MaxCount: UIntPtr
    Offset: UInt32
    ActualCount: UInt32
    pfnAllocate: win32more.Windows.Win32.System.Rpc.PFN_RPC_ALLOCATE
    pfnFree: win32more.Windows.Win32.System.Rpc.PFN_RPC_FREE
    StackTop: POINTER(Byte)
    pPresentedType: POINTER(Byte)
    pTransmitType: POINTER(Byte)
    SavedHandle: VoidPtr
    StubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC)
    FullPtrXlatTables: POINTER(win32more.Windows.Win32.System.Rpc.FULL_PTR_XLAT_TABLES)
    FullPtrRefId: UInt32
    PointerLength: UInt32
    fInDontFree: Annotated[Int32, 1]
    fDontCallFreeInst: Annotated[Int32, 1]
    fUnused1: Annotated[Int32, 1]
    fHasReturn: Annotated[Int32, 1]
    fHasExtensions: Annotated[Int32, 1]
    fHasNewCorrDesc: Annotated[Int32, 1]
    fIsIn: Annotated[Int32, 1]
    fIsOut: Annotated[Int32, 1]
    fIsOicf: Annotated[Int32, 1]
    fBufferValid: Annotated[Int32, 1]
    fHasMemoryValidateCallback: Annotated[Int32, 1]
    fInFree: Annotated[Int32, 1]
    fNeedMCCP: Annotated[Int32, 1]
    fUnused2: Annotated[Int32, 3]
    fUnused3: Annotated[Int32, 16]
    dwDestContext: UInt32
    pvDestContext: VoidPtr
    SavedContextHandles: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT))
    ParamNumber: Int32
    pRpcChannelBuffer: win32more.Windows.Win32.System.Com.IRpcChannelBuffer
    pArrayInfo: POINTER(win32more.Windows.Win32.System.Rpc.ARRAY_INFO)
    SizePtrCountArray: POINTER(UInt32)
    SizePtrOffsetArray: POINTER(UInt32)
    SizePtrLengthArray: POINTER(UInt32)
    pArgQueue: VoidPtr
    dwStubPhase: UInt32
    LowStackMark: VoidPtr
    pAsyncMsg: win32more.Windows.Win32.System.Rpc.PNDR_ASYNC_MESSAGE
    pCorrInfo: win32more.Windows.Win32.System.Rpc.PNDR_CORRELATION_INFO
    pCorrMemory: POINTER(Byte)
    pMemoryList: VoidPtr
    pCSInfo: IntPtr
    ConformanceMark: POINTER(Byte)
    VarianceMark: POINTER(Byte)
    Unused: IntPtr
    pContext: POINTER(win32more.Windows.Win32.System.Rpc._NDR_PROC_CONTEXT)
    ContextHandleHash: VoidPtr
    pUserMarshalList: VoidPtr
    Reserved51_3: IntPtr
    Reserved51_4: IntPtr
    Reserved51_5: IntPtr
class MIDL_SYNTAX_INFO(Structure):
    TransferSyntax: win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    DispatchTable: POINTER(win32more.Windows.Win32.System.Rpc.RPC_DISPATCH_TABLE)
    ProcString: POINTER(Byte)
    FmtStringOffset: POINTER(UInt16)
    TypeString: POINTER(Byte)
    aUserMarshalQuadruple: VoidPtr
    pMethodProperties: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_INTERFACE_METHOD_PROPERTIES)
    pReserved2: UIntPtr
class MIDL_TYPE_PICKLING_INFO(Structure):
    Version: UInt32
    Flags: UInt32
    Reserved: UIntPtr * 3
class MIDL_WINRT_TYPE_SERIALIZATION_INFO(Structure):
    Version: UInt32
    TypeFormatString: POINTER(Byte)
    FormatStringSize: UInt16
    TypeOffset: UInt16
    StubDesc: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_DESC)
class NDR64_ARRAY_ELEMENT_INFO(Structure):
    ElementMemSize: UInt32
    Element: VoidPtr
class NDR64_ARRAY_FLAGS(Structure):
    HasPointerInfo: Annotated[Byte, 1]
    HasElementInfo: Annotated[Byte, 1]
    IsMultiDimensional: Annotated[Byte, 1]
    IsArrayofStrings: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 1]
    Reserved2: Annotated[Byte, 1]
    Reserved3: Annotated[Byte, 1]
    Reserved4: Annotated[Byte, 1]
class NDR64_BINDINGS(Union):
    Primitive: win32more.Windows.Win32.System.Rpc.NDR64_BIND_PRIMITIVE
    Generic: win32more.Windows.Win32.System.Rpc.NDR64_BIND_GENERIC
    Context: win32more.Windows.Win32.System.Rpc.NDR64_BIND_CONTEXT
class NDR64_BIND_AND_NOTIFY_EXTENSION(Structure):
    Binding: win32more.Windows.Win32.System.Rpc.NDR64_BIND_CONTEXT
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
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    NumberDims: Byte
    NumberElements: UInt32
    Element: VoidPtr
class NDR64_BOGUS_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Reserve: Byte
    MemorySize: UInt32
    OriginalMemberLayout: VoidPtr
    OriginalPointerLayout: VoidPtr
    PointerLayout: VoidPtr
class NDR64_BUFFER_ALIGN_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Reserved: UInt16
    Reserved2: UInt32
class NDR64_CONFORMANT_STRING_FORMAT(Structure):
    Header: win32more.Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
class NDR64_CONF_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    ElementSize: UInt32
    ConfDescriptor: VoidPtr
class NDR64_CONF_BOGUS_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Dimensions: Byte
    MemorySize: UInt32
    OriginalMemberLayout: VoidPtr
    OriginalPointerLayout: VoidPtr
    PointerLayout: VoidPtr
    ConfArrayDescription: VoidPtr
class NDR64_CONF_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Reserve: Byte
    MemorySize: UInt32
    ArrayDescription: VoidPtr
class NDR64_CONF_VAR_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    ElementSize: UInt32
    ConfDescriptor: VoidPtr
    VarDescriptor: VoidPtr
class NDR64_CONF_VAR_BOGUS_ARRAY_HEADER_FORMAT(Structure):
    FixedArrayFormat: win32more.Windows.Win32.System.Rpc.NDR64_BOGUS_ARRAY_HEADER_FORMAT
    ConfDescription: VoidPtr
    VarDescription: VoidPtr
    OffsetDescription: VoidPtr
class NDR64_CONSTANT_IID_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved: UInt16
    Guid: Guid
class NDR64_CONTEXT_HANDLE_FLAGS(Structure):
    CannotBeNull: Annotated[Byte, 1]
    Serialize: Annotated[Byte, 1]
    NoSerialize: Annotated[Byte, 1]
    Strict: Annotated[Byte, 1]
    IsReturn: Annotated[Byte, 1]
    IsOut: Annotated[Byte, 1]
    IsIn: Annotated[Byte, 1]
    IsViaPointer: Annotated[Byte, 1]
class NDR64_CONTEXT_HANDLE_FORMAT(Structure):
    FormatCode: Byte
    ContextFlags: Byte
    RundownRoutineIndex: Byte
    Ordinal: Byte
class NDR64_EMBEDDED_COMPLEX_FORMAT(Structure):
    FormatCode: Byte
    Reserve1: Byte
    Reserve2: UInt16
    Type: VoidPtr
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
    RepeatFormat: win32more.Windows.Win32.System.Rpc.NDR64_REPEAT_FORMAT
    Iterations: UInt32
    Reserved: UInt32
class NDR64_FIX_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    TotalSize: UInt32
class NDR64_IID_FLAGS(Structure):
    ConstantIID: Annotated[Byte, 1]
    Reserved: Annotated[Byte, 7]
class NDR64_IID_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved: UInt16
    IIDDescriptor: VoidPtr
class NDR64_MEMPAD_FORMAT(Structure):
    FormatCode: Byte
    Reserve1: Byte
    MemPad: UInt16
    Reserved2: UInt32
class NDR64_NON_CONFORMANT_STRING_FORMAT(Structure):
    Header: win32more.Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
    TotalSize: UInt32
class NDR64_NON_ENCAPSULATED_UNION(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: Byte
    SwitchType: Byte
    MemorySize: UInt32
    Switch: VoidPtr
    Reserved: UInt32
class NDR64_NO_REPEAT_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved1: UInt16
    Reserved2: UInt32
class NDR64_PARAM_FLAGS(Structure):
    MustSize: Annotated[UInt16, 1]
    MustFree: Annotated[UInt16, 1]
    IsPipe: Annotated[UInt16, 1]
    IsIn: Annotated[UInt16, 1]
    IsOut: Annotated[UInt16, 1]
    IsReturn: Annotated[UInt16, 1]
    IsBasetype: Annotated[UInt16, 1]
    IsByValue: Annotated[UInt16, 1]
    IsSimpleRef: Annotated[UInt16, 1]
    IsDontCallFreeInst: Annotated[UInt16, 1]
    SaveForAsyncFinish: Annotated[UInt16, 1]
    IsPartialIgnore: Annotated[UInt16, 1]
    IsForceAllocate: Annotated[UInt16, 1]
    Reserved: Annotated[UInt16, 2]
    UseCache: Annotated[UInt16, 1]
class NDR64_PARAM_FORMAT(Structure):
    Type: VoidPtr
    Attributes: win32more.Windows.Win32.System.Rpc.NDR64_PARAM_FLAGS
    Reserved: UInt16
    StackOffset: UInt32
class NDR64_PIPE_FLAGS(Structure):
    Reserved1: Annotated[Byte, 5]
    HasRange: Annotated[Byte, 1]
    BlockCopy: Annotated[Byte, 1]
    Reserved2: Annotated[Byte, 1]
class NDR64_PIPE_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Alignment: Byte
    Reserved: Byte
    Type: VoidPtr
    MemorySize: UInt32
    BufferSize: UInt32
class NDR64_POINTER_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    Reserved: UInt16
    Pointee: VoidPtr
class NDR64_POINTER_INSTANCE_HEADER_FORMAT(Structure):
    Offset: UInt32
    Reserved: UInt32
class NDR64_POINTER_REPEAT_FLAGS(Structure):
    SetCorrMark: Annotated[Byte, 1]
    Reserved: Annotated[Byte, 7]
class NDR64_PROC_FLAGS(Structure):
    HandleType: Annotated[UInt32, 3]
    ProcType: Annotated[UInt32, 3]
    IsInterpreted: Annotated[UInt32, 2]
    IsObject: Annotated[UInt32, 1]
    IsAsync: Annotated[UInt32, 1]
    IsEncode: Annotated[UInt32, 1]
    IsDecode: Annotated[UInt32, 1]
    UsesFullPtrPackage: Annotated[UInt32, 1]
    UsesRpcSmPackage: Annotated[UInt32, 1]
    UsesPipes: Annotated[UInt32, 1]
    HandlesExceptions: Annotated[UInt32, 2]
    ServerMustSize: Annotated[UInt32, 1]
    ClientMustSize: Annotated[UInt32, 1]
    HasReturn: Annotated[UInt32, 1]
    HasComplexReturn: Annotated[UInt32, 1]
    ServerHasCorrelation: Annotated[UInt32, 1]
    ClientHasCorrelation: Annotated[UInt32, 1]
    HasNotify: Annotated[UInt32, 1]
    HasOtherExtensions: Annotated[UInt32, 1]
    HasBigByValueParam: Annotated[UInt32, 1]
    HasArmParamLayout: Annotated[UInt32, 1]
    Reserved: Annotated[UInt32, 5]
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
    Header: win32more.Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
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
    Type: VoidPtr
    MemorySize: UInt32
    BufferSize: UInt32
    MinValue: UInt32
    MaxValue: UInt32
class NDR64_REPEAT_FORMAT(Structure):
    FormatCode: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_POINTER_REPEAT_FLAGS
    Reserved: UInt16
    Increment: UInt32
    OffsetToArray: UInt32
    NumberOfPointers: UInt32
class NDR64_RPC_FLAGS(Structure):
    Idempotent: Annotated[UInt16, 1]
    Broadcast: Annotated[UInt16, 1]
    Maybe: Annotated[UInt16, 1]
    Reserved0: Annotated[UInt16, 1]
    HasGuarantee: Annotated[UInt16, 1]
    Reserved1: Annotated[UInt16, 3]
    Message: Annotated[UInt16, 1]
    Reserved2: Annotated[UInt16, 4]
    InputSynchronous: Annotated[UInt16, 1]
    Asynchronous: Annotated[UInt16, 1]
    WinrtRemoteAsync: Annotated[UInt16, 1]
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
    Header: win32more.Windows.Win32.System.Rpc.NDR64_STRING_HEADER_FORMAT
    SizeDescription: VoidPtr
class NDR64_STRING_FLAGS(Structure):
    IsSized: Annotated[Byte, 1]
    IsRanged: Annotated[Byte, 1]
    Reserved3: Annotated[Byte, 1]
    Reserved4: Annotated[Byte, 1]
    Reserved5: Annotated[Byte, 1]
    Reserved6: Annotated[Byte, 1]
    Reserved7: Annotated[Byte, 1]
    Reserved8: Annotated[Byte, 1]
class NDR64_STRING_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_STRING_FLAGS
    ElementSize: UInt16
class NDR64_STRUCTURE_FLAGS(Structure):
    HasPointerInfo: Annotated[Byte, 1]
    HasMemberInfo: Annotated[Byte, 1]
    HasConfArray: Annotated[Byte, 1]
    HasOrigPointerInfo: Annotated[Byte, 1]
    HasOrigMemberInfo: Annotated[Byte, 1]
    Reserved1: Annotated[Byte, 1]
    Reserved2: Annotated[Byte, 1]
    Reserved3: Annotated[Byte, 1]
class NDR64_STRUCTURE_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_STRUCTURE_FLAGS
    Reserve: Byte
    MemorySize: UInt32
class NDR64_SYSTEM_HANDLE_FORMAT(Structure):
    FormatCode: Byte
    HandleType: Byte
    DesiredAccess: UInt32
class NDR64_TRANSMIT_AS_FLAGS(Structure):
    PresentedTypeIsArray: Annotated[Byte, 1]
    PresentedTypeAlign4: Annotated[Byte, 1]
    PresentedTypeAlign8: Annotated[Byte, 1]
    Reserved: Annotated[Byte, 5]
class NDR64_TRANSMIT_AS_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    RoutineIndex: UInt16
    TransmittedTypeWireAlignment: UInt16
    MemoryAlignment: UInt16
    PresentedTypeMemorySize: UInt32
    TransmittedTypeBufferSize: UInt32
    TransmittedType: VoidPtr
class NDR64_TYPE_STRICT_CONTEXT_HANDLE(Structure):
    FormatCode: Byte
    RealFormatCode: Byte
    Reserved: UInt16
    Type: VoidPtr
    CtxtFlags: UInt32
    CtxtID: UInt32
class NDR64_UNION_ARM(Structure):
    CaseValue: Int64
    Type: VoidPtr
    Reserved: UInt32
class NDR64_UNION_ARM_SELECTOR(Structure):
    Reserved1: Byte
    Alignment: Byte
    Reserved2: UInt16
    Arms: UInt32
class NDR64_USER_MARSHAL_FLAGS(Structure):
    Reserved: Annotated[Byte, 5]
    IID: Annotated[Byte, 1]
    RefPointer: Annotated[Byte, 1]
    UniquePointer: Annotated[Byte, 1]
class NDR64_USER_MARSHAL_FORMAT(Structure):
    FormatCode: Byte
    Flags: Byte
    RoutineIndex: UInt16
    TransmittedTypeWireAlignment: UInt16
    MemoryAlignment: UInt16
    UserTypeMemorySize: UInt32
    TransmittedTypeBufferSize: UInt32
    TransmittedType: VoidPtr
class NDR64_VAR_ARRAY_HEADER_FORMAT(Structure):
    FormatCode: Byte
    Alignment: Byte
    Flags: win32more.Windows.Win32.System.Rpc.NDR64_ARRAY_FLAGS
    Reserved: Byte
    TotalSize: UInt32
    ElementSize: UInt32
    VarDescriptor: VoidPtr
NDR_ALLOC_ALL_NODES_CONTEXT = IntPtr
class NDR_CS_ROUTINES(Structure):
    pSizeConvertRoutines: POINTER(win32more.Windows.Win32.System.Rpc.NDR_CS_SIZE_CONVERT_ROUTINES)
    pTagGettingRoutines: POINTER(win32more.Windows.Win32.System.Rpc.CS_TAG_GETTING_ROUTINE)
class NDR_CS_SIZE_CONVERT_ROUTINES(Structure):
    pfnNetSize: win32more.Windows.Win32.System.Rpc.CS_TYPE_NET_SIZE_ROUTINE
    pfnToNetCs: win32more.Windows.Win32.System.Rpc.CS_TYPE_TO_NETCS_ROUTINE
    pfnLocalSize: win32more.Windows.Win32.System.Rpc.CS_TYPE_LOCAL_SIZE_ROUTINE
    pfnFromNetCs: win32more.Windows.Win32.System.Rpc.CS_TYPE_FROM_NETCS_ROUTINE
class NDR_EXPR_DESC(Structure):
    pOffset: POINTER(UInt16)
    pFormatExpr: POINTER(Byte)
@winfunctype_pointer
def NDR_NOTIFY2_ROUTINE(flag: Byte) -> Void: ...
@winfunctype_pointer
def NDR_NOTIFY_ROUTINE() -> Void: ...
NDR_POINTER_QUEUE_STATE = IntPtr
@winfunctype_pointer
def NDR_RUNDOWN(context: VoidPtr) -> Void: ...
class NDR_SCONTEXT(Structure):
    pad: VoidPtr * 2
    userContext: VoidPtr
class NDR_USER_MARSHAL_INFO(Structure):
    InformationLevel: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Level1: win32more.Windows.Win32.System.Rpc.NDR_USER_MARSHAL_INFO_LEVEL1
class NDR_USER_MARSHAL_INFO_LEVEL1(Structure):
    Buffer: VoidPtr
    BufferSize: UInt32
    pfnAllocate: IntPtr
    pfnFree: IntPtr
    pRpcChannelBuffer: win32more.Windows.Win32.System.Com.IRpcChannelBuffer
    Reserved: UIntPtr * 5
@winfunctype_pointer
def PFN_RPCNOTIFICATION_ROUTINE(pAsync: POINTER(win32more.Windows.Win32.System.Rpc.RPC_ASYNC_STATE), Context: VoidPtr, Event: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_EVENT) -> Void: ...
@winfunctype_pointer
def PFN_RPC_ALLOCATE(param0: UIntPtr) -> VoidPtr: ...
@winfunctype_pointer
def PFN_RPC_FREE(param0: VoidPtr) -> Void: ...
PNDR_ASYNC_MESSAGE = IntPtr
PNDR_CORRELATION_INFO = IntPtr
PROXY_PHASE = Int32
PROXY_CALCSIZE: win32more.Windows.Win32.System.Rpc.PROXY_PHASE = 0
PROXY_GETBUFFER: win32more.Windows.Win32.System.Rpc.PROXY_PHASE = 1
PROXY_MARSHAL: win32more.Windows.Win32.System.Rpc.PROXY_PHASE = 2
PROXY_SENDRECEIVE: win32more.Windows.Win32.System.Rpc.PROXY_PHASE = 3
PROXY_UNMARSHAL: win32more.Windows.Win32.System.Rpc.PROXY_PHASE = 4
@winfunctype_pointer
def PRPC_RUNDOWN(AssociationContext: VoidPtr) -> Void: ...
class RDR_CALLOUT_STATE(Structure):
    LastError: win32more.Windows.Win32.System.Rpc.RPC_STATUS
    LastEEInfo: VoidPtr
    LastCalledStage: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE
    ServerName: POINTER(UInt16)
    ServerPort: POINTER(UInt16)
    RemoteUser: POINTER(UInt16)
    AuthType: POINTER(UInt16)
    ResourceTypePresent: Byte
    SessionIdPresent: Byte
    InterfacePresent: Byte
    ResourceType: Guid
    SessionId: Guid
    Interface: win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    CertContext: VoidPtr
@winfunctype_pointer
def RPCLT_PDU_FILTER_FUNC(Buffer: VoidPtr, BufferLength: UInt32, fDatagram: Int32) -> Void: ...
@winfunctype_pointer
def RPC_ADDRESS_CHANGE_FN(arg: VoidPtr) -> Void: ...
RPC_ADDRESS_CHANGE_TYPE = Int32
PROTOCOL_NOT_LOADED: win32more.Windows.Win32.System.Rpc.RPC_ADDRESS_CHANGE_TYPE = 1
PROTOCOL_LOADED: win32more.Windows.Win32.System.Rpc.RPC_ADDRESS_CHANGE_TYPE = 2
PROTOCOL_ADDRESS_CHANGE: win32more.Windows.Win32.System.Rpc.RPC_ADDRESS_CHANGE_TYPE = 3
RPC_ASYNC_EVENT = Int32
RpcCallComplete: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_EVENT = 0
RpcSendComplete: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_EVENT = 1
RpcReceiveComplete: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_EVENT = 2
RpcClientDisconnect: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_EVENT = 3
RpcClientCancel: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_EVENT = 4
class RPC_ASYNC_NOTIFICATION_INFO(Union):
    APC: _APC_e__Struct
    IOC: _IOC_e__Struct
    IntPtr: _IntPtr_e__Struct
    hEvent: win32more.Windows.Win32.Foundation.HANDLE
    NotificationRoutine: win32more.Windows.Win32.System.Rpc.PFN_RPCNOTIFICATION_ROUTINE
    class _APC_e__Struct(Structure):
        NotificationRoutine: win32more.Windows.Win32.System.Rpc.PFN_RPCNOTIFICATION_ROUTINE
        hThread: win32more.Windows.Win32.Foundation.HANDLE
    class _IOC_e__Struct(Structure):
        hIOPort: win32more.Windows.Win32.Foundation.HANDLE
        dwNumberOfBytesTransferred: UInt32
        dwCompletionKey: UIntPtr
        lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)
    class _IntPtr_e__Struct(Structure):
        hWnd: win32more.Windows.Win32.Foundation.HWND
        Msg: UInt32
class RPC_ASYNC_STATE(Structure):
    Size: UInt32
    Signature: UInt32
    Lock: Int32
    Flags: UInt32
    StubInfo: VoidPtr
    UserInfo: VoidPtr
    RuntimeInfo: VoidPtr
    Event: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_EVENT
    NotificationType: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES
    u: win32more.Windows.Win32.System.Rpc.RPC_ASYNC_NOTIFICATION_INFO
    Reserved: IntPtr * 4
@winfunctype_pointer
def RPC_AUTH_KEY_RETRIEVAL_FN(Arg: VoidPtr, ServerPrincName: win32more.Windows.Win32.Foundation.PWSTR, KeyVer: UInt32, Key: POINTER(VoidPtr), Status: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> Void: ...
RPC_BINDING_HANDLE_OPTIONS_FLAGS = UInt32
RPC_BHO_NONCAUSAL: win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_FLAGS = 1
RPC_BHO_DONTLINGER: win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_FLAGS = 2
class RPC_BINDING_HANDLE_OPTIONS_V1(Structure):
    Version: UInt32
    Flags: win32more.Windows.Win32.System.Rpc.RPC_BINDING_HANDLE_OPTIONS_FLAGS
    ComTimeout: UInt32
    CallTimeout: UInt32
class RPC_BINDING_HANDLE_SECURITY_V1_A(Structure):
    Version: UInt32
    ServerPrincName: POINTER(Byte)
    AuthnLevel: UInt32
    AuthnSvc: UInt32
    AuthIdentity: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A)
    SecurityQos: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SECURITY_QOS)
class RPC_BINDING_HANDLE_SECURITY_V1_W(Structure):
    Version: UInt32
    ServerPrincName: POINTER(UInt16)
    AuthnLevel: UInt32
    AuthnSvc: UInt32
    AuthIdentity: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W)
    SecurityQos: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SECURITY_QOS)
RPC_BINDING_HANDLE_SECURITY_V1 = UnicodeAlias('RPC_BINDING_HANDLE_SECURITY_V1_W')
class RPC_BINDING_HANDLE_TEMPLATE_V1_A(Structure):
    Version: UInt32
    Flags: UInt32
    ProtocolSequence: UInt32
    NetworkAddress: POINTER(Byte)
    StringEndpoint: POINTER(Byte)
    u1: _u1_e__Union
    ObjectUuid: Guid
    class _u1_e__Union(Union):
        Reserved: POINTER(Byte)
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
RPC_BINDING_HANDLE_TEMPLATE_V1 = UnicodeAlias('RPC_BINDING_HANDLE_TEMPLATE_V1_W')
class RPC_BINDING_VECTOR(Structure):
    Count: UInt32
    BindingH: VoidPtr * 1
@winfunctype_pointer
def RPC_BLOCKING_FN(hWnd: VoidPtr, Context: VoidPtr, hSyncEvent: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
class RPC_CALL_ATTRIBUTES_V1_A(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(Byte)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(Byte)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: win32more.Windows.Win32.Foundation.BOOL
class RPC_CALL_ATTRIBUTES_V1_W(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(UInt16)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(UInt16)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: win32more.Windows.Win32.Foundation.BOOL
RPC_CALL_ATTRIBUTES_V1 = UnicodeAlias('RPC_CALL_ATTRIBUTES_V1_W')
class RPC_CALL_ATTRIBUTES_V2_A(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(Byte)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(Byte)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: win32more.Windows.Win32.Foundation.BOOL
    KernelModeCaller: win32more.Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: UInt32
    ClientPID: win32more.Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: win32more.Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1)
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
    NullSession: win32more.Windows.Win32.Foundation.BOOL
    KernelModeCaller: win32more.Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: win32more.Windows.Win32.System.Rpc.RpcCallClientLocality
    ClientPID: win32more.Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: win32more.Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1)
    OpNum: UInt16
    InterfaceUuid: Guid
RPC_CALL_ATTRIBUTES_V2 = UnicodeAlias('RPC_CALL_ATTRIBUTES_V2_W')
class RPC_CALL_ATTRIBUTES_V3_A(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(Byte)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(Byte)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: win32more.Windows.Win32.Foundation.BOOL
    KernelModeCaller: win32more.Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: UInt32
    ClientPID: win32more.Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: win32more.Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1)
    OpNum: UInt16
    InterfaceUuid: Guid
    ClientIdentifierBufferLength: UInt32
    ClientIdentifier: POINTER(Byte)
class RPC_CALL_ATTRIBUTES_V3_W(Structure):
    Version: UInt32
    Flags: UInt32
    ServerPrincipalNameBufferLength: UInt32
    ServerPrincipalName: POINTER(UInt16)
    ClientPrincipalNameBufferLength: UInt32
    ClientPrincipalName: POINTER(UInt16)
    AuthenticationLevel: UInt32
    AuthenticationService: UInt32
    NullSession: win32more.Windows.Win32.Foundation.BOOL
    KernelModeCaller: win32more.Windows.Win32.Foundation.BOOL
    ProtocolSequence: UInt32
    IsClientLocal: win32more.Windows.Win32.System.Rpc.RpcCallClientLocality
    ClientPID: win32more.Windows.Win32.Foundation.HANDLE
    CallStatus: UInt32
    CallType: win32more.Windows.Win32.System.Rpc.RpcCallType
    CallLocalAddress: POINTER(win32more.Windows.Win32.System.Rpc.RPC_CALL_LOCAL_ADDRESS_V1)
    OpNum: UInt16
    InterfaceUuid: Guid
    ClientIdentifierBufferLength: UInt32
    ClientIdentifier: POINTER(Byte)
RPC_CALL_ATTRIBUTES_V3 = UnicodeAlias('RPC_CALL_ATTRIBUTES_V3_W')
class RPC_CALL_LOCAL_ADDRESS_V1(Structure):
    Version: UInt32
    Buffer: VoidPtr
    BufferSize: UInt32
    AddressFormat: win32more.Windows.Win32.System.Rpc.RpcLocalAddressFormat
@winfunctype_pointer
def RPC_CLIENT_ALLOC(Size: UIntPtr) -> VoidPtr: ...
@winfunctype_pointer
def RPC_CLIENT_FREE(Ptr: VoidPtr) -> Void: ...
class RPC_CLIENT_INFORMATION1(Structure):
    UserName: POINTER(Byte)
    ComputerName: POINTER(Byte)
    Privilege: UInt16
    AuthFlags: UInt32
class RPC_CLIENT_INTERFACE(Structure):
    Length: UInt32
    InterfaceId: win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    TransferSyntax: win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    DispatchTable: POINTER(win32more.Windows.Win32.System.Rpc.RPC_DISPATCH_TABLE)
    RpcProtseqEndpointCount: UInt32
    RpcProtseqEndpoint: POINTER(win32more.Windows.Win32.System.Rpc.RPC_PROTSEQ_ENDPOINT)
    Reserved: UIntPtr
    InterpreterInfo: VoidPtr
    Flags: UInt32
RPC_C_AUTHN_INFO_TYPE = UInt32
RPC_C_AUTHN_INFO_NONE: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE = 0
RPC_C_AUTHN_INFO_TYPE_HTTP: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE = 1
RPC_C_HTTP_AUTHN_TARGET = UInt32
RPC_C_HTTP_AUTHN_TARGET_SERVER: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET = 1
RPC_C_HTTP_AUTHN_TARGET_PROXY: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET = 2
RPC_C_HTTP_FLAGS = UInt32
RPC_C_HTTP_FLAG_USE_SSL: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS = 1
RPC_C_HTTP_FLAG_USE_FIRST_AUTH_SCHEME: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS = 2
RPC_C_HTTP_FLAG_IGNORE_CERT_CN_INVALID: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS = 8
RPC_C_HTTP_FLAG_ENABLE_CERT_REVOCATION_CHECK: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS = 16
class RPC_C_OPT_COOKIE_AUTH_DESCRIPTOR(Structure):
    BufferSize: UInt32
    Buffer: win32more.Windows.Win32.Foundation.PSTR
RPC_C_QOS_CAPABILITIES = UInt32
RPC_C_QOS_CAPABILITIES_DEFAULT: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES = 0
RPC_C_QOS_CAPABILITIES_MUTUAL_AUTH: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES = 1
RPC_C_QOS_CAPABILITIES_MAKE_FULLSIC: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES = 2
RPC_C_QOS_CAPABILITIES_ANY_AUTHORITY: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES = 4
RPC_C_QOS_CAPABILITIES_IGNORE_DELEGATE_FAILURE: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES = 8
RPC_C_QOS_CAPABILITIES_LOCAL_MA_HINT: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES = 16
RPC_C_QOS_CAPABILITIES_SCHANNEL_FULL_AUTH_IDENTITY: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES = 32
RPC_C_QOS_IDENTITY = UInt32
RPC_C_QOS_IDENTITY_STATIC: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY = 0
RPC_C_QOS_IDENTITY_DYNAMIC: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY = 1
@winfunctype_pointer
def RPC_DISPATCH_FUNCTION(Message: POINTER(win32more.Windows.Win32.System.Rpc.RPC_MESSAGE)) -> Void: ...
class RPC_DISPATCH_TABLE(Structure):
    DispatchTableCount: UInt32
    DispatchTable: win32more.Windows.Win32.System.Rpc.RPC_DISPATCH_FUNCTION
    Reserved: IntPtr
class RPC_EE_INFO_PARAM(Structure):
    ParameterType: win32more.Windows.Win32.System.Rpc.ExtendedErrorParamTypes
    u: _u_e__Union
    class _u_e__Union(Union):
        AnsiString: win32more.Windows.Win32.Foundation.PSTR
        UnicodeString: win32more.Windows.Win32.Foundation.PWSTR
        LVal: Int32
        SVal: Int16
        PVal: UInt64
        BVal: win32more.Windows.Win32.System.Rpc.BinaryParam
class RPC_ENDPOINT_TEMPLATEA(Structure):
    Version: UInt32
    ProtSeq: win32more.Windows.Win32.Foundation.PSTR
    Endpoint: win32more.Windows.Win32.Foundation.PSTR
    SecurityDescriptor: VoidPtr
    Backlog: UInt32
class RPC_ENDPOINT_TEMPLATEW(Structure):
    Version: UInt32
    ProtSeq: win32more.Windows.Win32.Foundation.PWSTR
    Endpoint: win32more.Windows.Win32.Foundation.PWSTR
    SecurityDescriptor: VoidPtr
    Backlog: UInt32
RPC_ENDPOINT_TEMPLATE = UnicodeAlias('RPC_ENDPOINT_TEMPLATEW')
class RPC_ERROR_ENUM_HANDLE(Structure):
    Signature: UInt32
    CurrentPos: VoidPtr
    Head: VoidPtr
class RPC_EXTENDED_ERROR_INFO(Structure):
    Version: UInt32
    ComputerName: win32more.Windows.Win32.Foundation.PWSTR
    ProcessID: UInt32
    u: _u_e__Union
    GeneratingComponent: UInt32
    Status: UInt32
    DetectionLocation: UInt16
    Flags: UInt16
    NumberOfParameters: Int32
    Parameters: win32more.Windows.Win32.System.Rpc.RPC_EE_INFO_PARAM * 4
    class _u_e__Union(Union):
        SystemTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
        FileTime: win32more.Windows.Win32.Foundation.FILETIME
@winfunctype_pointer
def RPC_FORWARD_FUNCTION(InterfaceId: POINTER(Guid), InterfaceVersion: POINTER(win32more.Windows.Win32.System.Rpc.RPC_VERSION), ObjectId: POINTER(Guid), Rpcpro: POINTER(Byte), ppDestEndpoint: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
@winfunctype_pointer
def RPC_HTTP_PROXY_FREE_STRING(String: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
RPC_HTTP_REDIRECTOR_STAGE = Int32
RPCHTTP_RS_REDIRECT: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE = 1
RPCHTTP_RS_ACCESS_1: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE = 2
RPCHTTP_RS_SESSION: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE = 3
RPCHTTP_RS_ACCESS_2: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE = 4
RPCHTTP_RS_INTERFACE: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE = 5
class RPC_HTTP_TRANSPORT_CREDENTIALS_A(Structure):
    TransportCredentials: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A)
    Flags: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(Byte)
class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A(Structure):
    TransportCredentials: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A)
    Flags: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(Byte)
    ProxyCredentials: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_A)
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W(Structure):
    TransportCredentials: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W)
    Flags: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(UInt16)
    ProxyCredentials: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W)
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
RPC_HTTP_TRANSPORT_CREDENTIALS_V2 = UnicodeAlias('RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W')
class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A(Structure):
    TransportCredentials: VoidPtr
    Flags: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(Byte)
    ProxyCredentials: VoidPtr
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W(Structure):
    TransportCredentials: VoidPtr
    Flags: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(UInt16)
    ProxyCredentials: VoidPtr
    NumberOfProxyAuthnSchemes: UInt32
    ProxyAuthnSchemes: POINTER(UInt32)
RPC_HTTP_TRANSPORT_CREDENTIALS_V3 = UnicodeAlias('RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W')
class RPC_HTTP_TRANSPORT_CREDENTIALS_W(Structure):
    TransportCredentials: POINTER(win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY_W)
    Flags: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_FLAGS
    AuthenticationTarget: win32more.Windows.Win32.System.Rpc.RPC_C_HTTP_AUTHN_TARGET
    NumberOfAuthnSchemes: UInt32
    AuthnSchemes: POINTER(UInt32)
    ServerCertificateSubject: POINTER(UInt16)
RPC_HTTP_TRANSPORT_CREDENTIALS = UnicodeAlias('RPC_HTTP_TRANSPORT_CREDENTIALS_W')
@winfunctype_pointer
def RPC_IF_CALLBACK_FN(InterfaceUuid: VoidPtr, Context: VoidPtr) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
class RPC_IF_ID(Structure):
    Uuid: Guid
    VersMajor: UInt16
    VersMinor: UInt16
class RPC_IF_ID_VECTOR(Structure):
    Count: UInt32
    IfId: POINTER(win32more.Windows.Win32.System.Rpc.RPC_IF_ID) * 1
class RPC_IMPORT_CONTEXT_P(Structure):
    LookupContext: VoidPtr
    ProposedHandle: VoidPtr
    Bindings: POINTER(win32more.Windows.Win32.System.Rpc.RPC_BINDING_VECTOR)
@winfunctype_pointer
def RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN(IfGroup: VoidPtr, IdleCallbackContext: VoidPtr, IsGroupIdle: UInt32) -> Void: ...
class RPC_INTERFACE_TEMPLATEA(Structure):
    Version: UInt32
    IfSpec: VoidPtr
    MgrTypeUuid: POINTER(Guid)
    MgrEpv: VoidPtr
    Flags: UInt32
    MaxCalls: UInt32
    MaxRpcSize: UInt32
    IfCallback: win32more.Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN
    UuidVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)
    Annotation: win32more.Windows.Win32.Foundation.PSTR
    SecurityDescriptor: VoidPtr
class RPC_INTERFACE_TEMPLATEW(Structure):
    Version: UInt32
    IfSpec: VoidPtr
    MgrTypeUuid: POINTER(Guid)
    MgrEpv: VoidPtr
    Flags: UInt32
    MaxCalls: UInt32
    MaxRpcSize: UInt32
    IfCallback: win32more.Windows.Win32.System.Rpc.RPC_IF_CALLBACK_FN
    UuidVector: POINTER(win32more.Windows.Win32.System.Rpc.UUID_VECTOR)
    Annotation: win32more.Windows.Win32.Foundation.PWSTR
    SecurityDescriptor: VoidPtr
RPC_INTERFACE_TEMPLATE = UnicodeAlias('RPC_INTERFACE_TEMPLATEW')
class RPC_MESSAGE(Structure):
    Handle: VoidPtr
    DataRepresentation: UInt32
    Buffer: VoidPtr
    BufferLength: UInt32
    ProcNum: UInt32
    TransferSyntax: POINTER(win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER)
    RpcInterfaceInformation: VoidPtr
    ReservedForRuntime: VoidPtr
    ManagerEpv: VoidPtr
    ImportContext: VoidPtr
    RpcFlags: UInt32
@winfunctype_pointer
def RPC_MGMT_AUTHORIZATION_FN(ClientBinding: VoidPtr, RequestedMgmtOperation: UInt32, Status: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> Int32: ...
@winfunctype_pointer
def RPC_NEW_HTTP_PROXY_CHANNEL(RedirectorStage: win32more.Windows.Win32.System.Rpc.RPC_HTTP_REDIRECTOR_STAGE, ServerName: win32more.Windows.Win32.Foundation.PWSTR, ServerPort: win32more.Windows.Win32.Foundation.PWSTR, RemoteUser: win32more.Windows.Win32.Foundation.PWSTR, AuthType: win32more.Windows.Win32.Foundation.PWSTR, ResourceUuid: VoidPtr, SessionId: VoidPtr, Interface: VoidPtr, Reserved: VoidPtr, Flags: UInt32, NewServerName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), NewServerPort: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.System.Rpc.RPC_STATUS: ...
RPC_NOTIFICATIONS = Int32
RpcNotificationCallNone: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATIONS = 0
RpcNotificationClientDisconnect: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATIONS = 1
RpcNotificationCallCancel: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATIONS = 2
RPC_NOTIFICATION_TYPES = Int32
RpcNotificationTypeNone: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES = 0
RpcNotificationTypeEvent: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES = 1
RpcNotificationTypeApc: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES = 2
RpcNotificationTypeIoc: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES = 3
RpcNotificationTypeHwnd: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES = 4
RpcNotificationTypeCallback: win32more.Windows.Win32.System.Rpc.RPC_NOTIFICATION_TYPES = 5
@winfunctype_pointer
def RPC_OBJECT_INQ_FN(ObjectUuid: POINTER(Guid), TypeUuid: POINTER(Guid), Status: POINTER(win32more.Windows.Win32.System.Rpc.RPC_STATUS)) -> Void: ...
class RPC_POLICY(Structure):
    Length: UInt32
    EndpointFlags: UInt32
    NICFlags: UInt32
class RPC_PROTSEQ_ENDPOINT(Structure):
    RpcProtocolSequence: POINTER(Byte)
    Endpoint: POINTER(Byte)
class RPC_PROTSEQ_VECTORA(Structure):
    Count: UInt32
    Protseq: POINTER(Byte) * 1
class RPC_PROTSEQ_VECTORW(Structure):
    Count: UInt32
    Protseq: POINTER(UInt16) * 1
RPC_PROTSEQ_VECTOR = UnicodeAlias('RPC_PROTSEQ_VECTORW')
@winfunctype_pointer
def RPC_SECURITY_CALLBACK_FN(Context: VoidPtr) -> Void: ...
class RPC_SECURITY_QOS(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
class RPC_SECURITY_QOS_V2_A(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A)
class RPC_SECURITY_QOS_V2_W(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W)
RPC_SECURITY_QOS_V2 = UnicodeAlias('RPC_SECURITY_QOS_V2_W')
class RPC_SECURITY_QOS_V3_A(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: VoidPtr
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A)
class RPC_SECURITY_QOS_V3_W(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: VoidPtr
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W)
RPC_SECURITY_QOS_V3 = UnicodeAlias('RPC_SECURITY_QOS_V3_W')
class RPC_SECURITY_QOS_V4_A(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: VoidPtr
    EffectiveOnly: UInt32
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A)
class RPC_SECURITY_QOS_V4_W(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: VoidPtr
    EffectiveOnly: UInt32
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W)
RPC_SECURITY_QOS_V4 = UnicodeAlias('RPC_SECURITY_QOS_V4_W')
class RPC_SECURITY_QOS_V5_A(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: VoidPtr
    EffectiveOnly: UInt32
    ServerSecurityDescriptor: VoidPtr
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_A)
class RPC_SECURITY_QOS_V5_W(Structure):
    Version: UInt32
    Capabilities: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_CAPABILITIES
    IdentityTracking: win32more.Windows.Win32.System.Rpc.RPC_C_QOS_IDENTITY
    ImpersonationType: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL
    AdditionalSecurityInfoType: win32more.Windows.Win32.System.Rpc.RPC_C_AUTHN_INFO_TYPE
    u: _u_e__Union
    Sid: VoidPtr
    EffectiveOnly: UInt32
    ServerSecurityDescriptor: VoidPtr
    class _u_e__Union(Union):
        HttpCredentials: POINTER(win32more.Windows.Win32.System.Rpc.RPC_HTTP_TRANSPORT_CREDENTIALS_W)
RPC_SECURITY_QOS_V5 = UnicodeAlias('RPC_SECURITY_QOS_V5_W')
class RPC_SEC_CONTEXT_KEY_INFO(Structure):
    EncryptAlgorithm: UInt32
    KeySize: UInt32
    SignatureAlgorithm: UInt32
class RPC_SERVER_INTERFACE(Structure):
    Length: UInt32
    InterfaceId: win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    TransferSyntax: win32more.Windows.Win32.System.Rpc.RPC_SYNTAX_IDENTIFIER
    DispatchTable: POINTER(win32more.Windows.Win32.System.Rpc.RPC_DISPATCH_TABLE)
    RpcProtseqEndpointCount: UInt32
    RpcProtseqEndpoint: POINTER(win32more.Windows.Win32.System.Rpc.RPC_PROTSEQ_ENDPOINT)
    DefaultManagerEpv: VoidPtr
    InterpreterInfo: VoidPtr
    Flags: UInt32
@cfunctype_pointer
def RPC_SETFILTER_FUNC(pfnFilter: win32more.Windows.Win32.System.Rpc.RPCLT_PDU_FILTER_FUNC) -> Void: ...
class RPC_STATS_VECTOR(Structure):
    Count: UInt32
    Stats: UInt32 * 1
RPC_STATUS = Int32
RPC_S_OK: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 0
RPC_S_ACCESS_DENIED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 5
RPC_S_INVALID_ARG: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 87
RPC_S_OUT_OF_MEMORY: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 14
RPC_S_OUT_OF_THREADS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 164
RPC_S_INVALID_LEVEL: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 87
RPC_S_BUFFER_TOO_SMALL: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 122
RPC_S_INVALID_SECURITY_DESC: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1338
RPC_S_SERVER_OUT_OF_MEMORY: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1130
RPC_S_ASYNC_CALL_PENDING: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 997
RPC_S_UNKNOWN_PRINCIPAL: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1332
RPC_S_TIMEOUT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1460
RPC_S_RUNTIME_UNINITIALIZED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1
RPC_S_NOT_ENOUGH_QUOTA: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1816
RPC_S_INVALID_STRING_BINDING: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1700
RPC_S_WRONG_KIND_OF_BINDING: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1701
RPC_S_INVALID_BINDING: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1702
RPC_S_PROTSEQ_NOT_SUPPORTED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1703
RPC_S_INVALID_RPC_PROTSEQ: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1704
RPC_S_INVALID_STRING_UUID: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1705
RPC_S_INVALID_ENDPOINT_FORMAT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1706
RPC_S_INVALID_NET_ADDR: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1707
RPC_S_NO_ENDPOINT_FOUND: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1708
RPC_S_INVALID_TIMEOUT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1709
RPC_S_OBJECT_NOT_FOUND: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1710
RPC_S_ALREADY_REGISTERED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1711
RPC_S_TYPE_ALREADY_REGISTERED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1712
RPC_S_ALREADY_LISTENING: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1713
RPC_S_NO_PROTSEQS_REGISTERED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1714
RPC_S_NOT_LISTENING: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1715
RPC_S_UNKNOWN_MGR_TYPE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1716
RPC_S_UNKNOWN_IF: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1717
RPC_S_NO_BINDINGS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1718
RPC_S_NO_PROTSEQS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1719
RPC_S_CANT_CREATE_ENDPOINT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1720
RPC_S_OUT_OF_RESOURCES: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1721
RPC_S_SERVER_UNAVAILABLE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1722
RPC_S_SERVER_TOO_BUSY: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1723
RPC_S_INVALID_NETWORK_OPTIONS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1724
RPC_S_NO_CALL_ACTIVE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1725
RPC_S_CALL_FAILED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1726
RPC_S_CALL_FAILED_DNE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1727
RPC_S_PROTOCOL_ERROR: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1728
RPC_S_PROXY_ACCESS_DENIED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1729
RPC_S_UNSUPPORTED_TRANS_SYN: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1730
RPC_S_UNSUPPORTED_TYPE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1732
RPC_S_INVALID_TAG: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1733
RPC_S_INVALID_BOUND: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1734
RPC_S_NO_ENTRY_NAME: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1735
RPC_S_INVALID_NAME_SYNTAX: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1736
RPC_S_UNSUPPORTED_NAME_SYNTAX: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1737
RPC_S_UUID_NO_ADDRESS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1739
RPC_S_DUPLICATE_ENDPOINT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1740
RPC_S_UNKNOWN_AUTHN_TYPE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1741
RPC_S_MAX_CALLS_TOO_SMALL: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1742
RPC_S_STRING_TOO_LONG: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1743
RPC_S_PROTSEQ_NOT_FOUND: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1744
RPC_S_PROCNUM_OUT_OF_RANGE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1745
RPC_S_BINDING_HAS_NO_AUTH: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1746
RPC_S_UNKNOWN_AUTHN_SERVICE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1747
RPC_S_UNKNOWN_AUTHN_LEVEL: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1748
RPC_S_INVALID_AUTH_IDENTITY: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1749
RPC_S_UNKNOWN_AUTHZ_SERVICE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1750
EPT_S_INVALID_ENTRY: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1751
EPT_S_CANT_PERFORM_OP: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1752
EPT_S_NOT_REGISTERED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1753
RPC_S_NOTHING_TO_EXPORT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1754
RPC_S_INCOMPLETE_NAME: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1755
RPC_S_INVALID_VERS_OPTION: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1756
RPC_S_NO_MORE_MEMBERS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1757
RPC_S_NOT_ALL_OBJS_UNEXPORTED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1758
RPC_S_INTERFACE_NOT_FOUND: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1759
RPC_S_ENTRY_ALREADY_EXISTS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1760
RPC_S_ENTRY_NOT_FOUND: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1761
RPC_S_NAME_SERVICE_UNAVAILABLE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1762
RPC_S_INVALID_NAF_ID: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1763
RPC_S_CANNOT_SUPPORT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1764
RPC_S_NO_CONTEXT_AVAILABLE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1765
RPC_S_INTERNAL_ERROR: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1766
RPC_S_ZERO_DIVIDE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1767
RPC_S_ADDRESS_ERROR: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1768
RPC_S_FP_DIV_ZERO: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1769
RPC_S_FP_UNDERFLOW: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1770
RPC_S_FP_OVERFLOW: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1771
RPC_S_CALL_IN_PROGRESS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1791
RPC_S_NO_MORE_BINDINGS: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1806
RPC_S_NO_INTERFACES: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1817
RPC_S_CALL_CANCELLED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1818
RPC_S_BINDING_INCOMPLETE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1819
RPC_S_COMM_FAILURE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1820
RPC_S_UNSUPPORTED_AUTHN_LEVEL: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1821
RPC_S_NO_PRINC_NAME: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1822
RPC_S_NOT_RPC_ERROR: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1823
RPC_S_UUID_LOCAL_ONLY: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1824
RPC_S_SEC_PKG_ERROR: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1825
RPC_S_NOT_CANCELLED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1826
RPC_S_COOKIE_AUTH_FAILED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1833
RPC_S_DO_NOT_DISTURB: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1834
RPC_S_SYSTEM_HANDLE_COUNT_EXCEEDED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1835
RPC_S_SYSTEM_HANDLE_TYPE_MISMATCH: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1836
RPC_S_GROUP_MEMBER_NOT_FOUND: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1898
EPT_S_CANT_CREATE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1899
RPC_S_INVALID_OBJECT: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1900
RPC_S_SEND_INCOMPLETE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1913
RPC_S_INVALID_ASYNC_HANDLE: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1914
RPC_S_INVALID_ASYNC_CALL: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1915
RPC_S_ENTRY_TYPE_MISMATCH: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1922
RPC_S_NOT_ALL_OBJS_EXPORTED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1923
RPC_S_INTERFACE_NOT_EXPORTED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1924
RPC_S_PROFILE_NOT_ADDED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1925
RPC_S_PRF_ELT_NOT_ADDED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1926
RPC_S_PRF_ELT_NOT_REMOVED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1927
RPC_S_GRP_ELT_NOT_ADDED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1928
RPC_S_GRP_ELT_NOT_REMOVED: win32more.Windows.Win32.System.Rpc.RPC_STATUS = 1929
class RPC_SYNTAX_IDENTIFIER(Structure):
    SyntaxGUID: Guid
    SyntaxVersion: win32more.Windows.Win32.System.Rpc.RPC_VERSION
class RPC_TRANSFER_SYNTAX(Structure):
    Uuid: Guid
    VersMajor: UInt16
    VersMinor: UInt16
class RPC_VERSION(Structure):
    MajorVersion: UInt16
    MinorVersion: UInt16
RpcCallClientLocality = Int32
rcclInvalid: win32more.Windows.Win32.System.Rpc.RpcCallClientLocality = 0
rcclLocal: win32more.Windows.Win32.System.Rpc.RpcCallClientLocality = 1
rcclRemote: win32more.Windows.Win32.System.Rpc.RpcCallClientLocality = 2
rcclClientUnknownLocality: win32more.Windows.Win32.System.Rpc.RpcCallClientLocality = 3
RpcCallType = Int32
rctInvalid: win32more.Windows.Win32.System.Rpc.RpcCallType = 0
rctNormal: win32more.Windows.Win32.System.Rpc.RpcCallType = 1
rctTraining: win32more.Windows.Win32.System.Rpc.RpcCallType = 2
rctGuaranteed: win32more.Windows.Win32.System.Rpc.RpcCallType = 3
RpcLocalAddressFormat = Int32
rlafInvalid: win32more.Windows.Win32.System.Rpc.RpcLocalAddressFormat = 0
rlafIPv4: win32more.Windows.Win32.System.Rpc.RpcLocalAddressFormat = 1
rlafIPv6: win32more.Windows.Win32.System.Rpc.RpcLocalAddressFormat = 2
RpcPerfCounters = Int32
RpcCurrentUniqueUser: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 1
RpcBackEndConnectionAttempts: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 2
RpcBackEndConnectionFailed: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 3
RpcRequestsPerSecond: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 4
RpcIncomingConnections: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 5
RpcIncomingBandwidth: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 6
RpcOutgoingBandwidth: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 7
RpcAttemptedLbsDecisions: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 8
RpcFailedLbsDecisions: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 9
RpcAttemptedLbsMessages: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 10
RpcFailedLbsMessages: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 11
RpcLastCounter: win32more.Windows.Win32.System.Rpc.RpcPerfCounters = 12
class SCONTEXT_QUEUE(Structure):
    NumberOfObjects: UInt32
    ArrayOfObjects: POINTER(POINTER(win32more.Windows.Win32.System.Rpc.NDR_SCONTEXT))
SEC_WINNT_AUTH_IDENTITY = UInt32
SEC_WINNT_AUTH_IDENTITY_ANSI: win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY = 1
SEC_WINNT_AUTH_IDENTITY_UNICODE: win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY = 2
class SEC_WINNT_AUTH_IDENTITY_A(Structure):
    User: POINTER(Byte)
    UserLength: UInt32
    Domain: POINTER(Byte)
    DomainLength: UInt32
    Password: POINTER(Byte)
    PasswordLength: UInt32
    Flags: win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY
class SEC_WINNT_AUTH_IDENTITY_W(Structure):
    User: POINTER(UInt16)
    UserLength: UInt32
    Domain: POINTER(UInt16)
    DomainLength: UInt32
    Password: POINTER(UInt16)
    PasswordLength: UInt32
    Flags: win32more.Windows.Win32.System.Rpc.SEC_WINNT_AUTH_IDENTITY
@winfunctype_pointer
def SERVER_ROUTINE() -> Int32: ...
STUB_PHASE = Int32
STUB_UNMARSHAL: win32more.Windows.Win32.System.Rpc.STUB_PHASE = 0
STUB_CALL_SERVER: win32more.Windows.Win32.System.Rpc.STUB_PHASE = 1
STUB_MARSHAL: win32more.Windows.Win32.System.Rpc.STUB_PHASE = 2
STUB_CALL_SERVER_NO_HRESULT: win32more.Windows.Win32.System.Rpc.STUB_PHASE = 3
@winfunctype_pointer
def STUB_THUNK(param0: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
class USER_MARSHAL_CB(Structure):
    Flags: UInt32
    pStubMsg: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)
    pReserve: POINTER(Byte)
    Signature: UInt32
    CBType: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_CB_TYPE
    pFormat: POINTER(Byte)
    pTypeFormat: POINTER(Byte)
USER_MARSHAL_CB_TYPE = Int32
USER_MARSHAL_CB_BUFFER_SIZE: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_CB_TYPE = 0
USER_MARSHAL_CB_MARSHALL: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_CB_TYPE = 1
USER_MARSHAL_CB_UNMARSHALL: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_CB_TYPE = 2
USER_MARSHAL_CB_FREE: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_CB_TYPE = 3
@winfunctype_pointer
def USER_MARSHAL_FREEING_ROUTINE(param0: POINTER(UInt32), param1: VoidPtr) -> Void: ...
@winfunctype_pointer
def USER_MARSHAL_MARSHALLING_ROUTINE(param0: POINTER(UInt32), param1: POINTER(Byte), param2: VoidPtr) -> POINTER(Byte): ...
class USER_MARSHAL_ROUTINE_QUADRUPLE(Structure):
    pfnBufferSize: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_SIZING_ROUTINE
    pfnMarshall: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_MARSHALLING_ROUTINE
    pfnUnmarshall: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_UNMARSHALLING_ROUTINE
    pfnFree: win32more.Windows.Win32.System.Rpc.USER_MARSHAL_FREEING_ROUTINE
@winfunctype_pointer
def USER_MARSHAL_SIZING_ROUTINE(param0: POINTER(UInt32), param1: UInt32, param2: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def USER_MARSHAL_UNMARSHALLING_ROUTINE(param0: POINTER(UInt32), param1: POINTER(Byte), param2: VoidPtr) -> POINTER(Byte): ...
class UUID_VECTOR(Structure):
    Count: UInt32
    Uuid: POINTER(Guid) * 1
XLAT_SIDE = Int32
XLAT_SERVER: win32more.Windows.Win32.System.Rpc.XLAT_SIDE = 1
XLAT_CLIENT: win32more.Windows.Win32.System.Rpc.XLAT_SIDE = 2
@winfunctype_pointer
def XMIT_HELPER_ROUTINE(param0: POINTER(win32more.Windows.Win32.System.Rpc.MIDL_STUB_MESSAGE)) -> Void: ...
class XMIT_ROUTINE_QUINTUPLE(Structure):
    pfnTranslateToXmit: win32more.Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
    pfnTranslateFromXmit: win32more.Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
    pfnFreeXmit: win32more.Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
    pfnFreeInst: win32more.Windows.Win32.System.Rpc.XMIT_HELPER_ROUTINE
_NDR_PROC_CONTEXT = IntPtr
system_handle_t = Int32
SYSTEM_HANDLE_FILE: win32more.Windows.Win32.System.Rpc.system_handle_t = 0
SYSTEM_HANDLE_SEMAPHORE: win32more.Windows.Win32.System.Rpc.system_handle_t = 1
SYSTEM_HANDLE_EVENT: win32more.Windows.Win32.System.Rpc.system_handle_t = 2
SYSTEM_HANDLE_MUTEX: win32more.Windows.Win32.System.Rpc.system_handle_t = 3
SYSTEM_HANDLE_PROCESS: win32more.Windows.Win32.System.Rpc.system_handle_t = 4
SYSTEM_HANDLE_TOKEN: win32more.Windows.Win32.System.Rpc.system_handle_t = 5
SYSTEM_HANDLE_SECTION: win32more.Windows.Win32.System.Rpc.system_handle_t = 6
SYSTEM_HANDLE_REG_KEY: win32more.Windows.Win32.System.Rpc.system_handle_t = 7
SYSTEM_HANDLE_THREAD: win32more.Windows.Win32.System.Rpc.system_handle_t = 8
SYSTEM_HANDLE_COMPOSITION_OBJECT: win32more.Windows.Win32.System.Rpc.system_handle_t = 9
SYSTEM_HANDLE_SOCKET: win32more.Windows.Win32.System.Rpc.system_handle_t = 10
SYSTEM_HANDLE_JOB: win32more.Windows.Win32.System.Rpc.system_handle_t = 11
SYSTEM_HANDLE_PIPE: win32more.Windows.Win32.System.Rpc.system_handle_t = 12
SYSTEM_HANDLE_MAX: win32more.Windows.Win32.System.Rpc.system_handle_t = 12
SYSTEM_HANDLE_INVALID: win32more.Windows.Win32.System.Rpc.system_handle_t = 255


make_ready(__name__)
