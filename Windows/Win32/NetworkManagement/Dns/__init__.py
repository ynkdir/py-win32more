from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.Dns
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
SIZEOF_IP4_ADDRESS: UInt32 = 4
IP4_ADDRESS_STRING_LENGTH: UInt32 = 16
IP4_ADDRESS_STRING_BUFFER_LENGTH: UInt32 = 16
DNS_ADDR_MAX_SOCKADDR_LENGTH: UInt32 = 32
IP6_ADDRESS_STRING_LENGTH: UInt32 = 65
IP6_ADDRESS_STRING_BUFFER_LENGTH: UInt32 = 65
DNS_ADDRESS_STRING_LENGTH: UInt32 = 65
DNS_PORT_HOST_ORDER: UInt32 = 53
DNS_PORT_NET_ORDER: UInt32 = 13568
DNS_RFC_MAX_UDP_PACKET_LENGTH: UInt32 = 512
DNS_MAX_NAME_LENGTH: UInt32 = 255
DNS_MAX_LABEL_LENGTH: UInt32 = 63
DNS_MAX_NAME_BUFFER_LENGTH: UInt32 = 256
DNS_MAX_LABEL_BUFFER_LENGTH: UInt32 = 64
DNS_MAX_IP4_REVERSE_NAME_LENGTH: UInt32 = 31
DNS_MAX_IP6_REVERSE_NAME_LENGTH: UInt32 = 75
DNS_MAX_REVERSE_NAME_LENGTH: UInt32 = 75
DNS_MAX_IP4_REVERSE_NAME_BUFFER_LENGTH: UInt32 = 31
DNS_MAX_IP6_REVERSE_NAME_BUFFER_LENGTH: UInt32 = 75
DNS_MAX_REVERSE_NAME_BUFFER_LENGTH: UInt32 = 75
DNS_MAX_TEXT_STRING_LENGTH: UInt32 = 255
DNS_COMPRESSED_QUESTION_NAME: UInt32 = 49164
DNS_OPCODE_QUERY: UInt32 = 0
DNS_OPCODE_IQUERY: UInt32 = 1
DNS_OPCODE_SERVER_STATUS: UInt32 = 2
DNS_OPCODE_UNKNOWN: UInt32 = 3
DNS_OPCODE_NOTIFY: UInt32 = 4
DNS_OPCODE_UPDATE: UInt32 = 5
DNS_RCODE_NOERROR: UInt32 = 0
DNS_RCODE_FORMERR: UInt32 = 1
DNS_RCODE_SERVFAIL: UInt32 = 2
DNS_RCODE_NXDOMAIN: UInt32 = 3
DNS_RCODE_NOTIMPL: UInt32 = 4
DNS_RCODE_REFUSED: UInt32 = 5
DNS_RCODE_YXDOMAIN: UInt32 = 6
DNS_RCODE_YXRRSET: UInt32 = 7
DNS_RCODE_NXRRSET: UInt32 = 8
DNS_RCODE_NOTAUTH: UInt32 = 9
DNS_RCODE_NOTZONE: UInt32 = 10
DNS_RCODE_MAX: UInt32 = 15
DNS_RCODE_BADVERS: UInt32 = 16
DNS_RCODE_BADSIG: UInt32 = 16
DNS_RCODE_BADKEY: UInt32 = 17
DNS_RCODE_BADTIME: UInt32 = 18
DNS_RCODE_NO_ERROR: UInt32 = 0
DNS_RCODE_FORMAT_ERROR: UInt32 = 1
DNS_RCODE_SERVER_FAILURE: UInt32 = 2
DNS_RCODE_NAME_ERROR: UInt32 = 3
DNS_RCODE_NOT_IMPLEMENTED: UInt32 = 4
DNS_CLASS_INTERNET: UInt32 = 1
DNS_CLASS_CSNET: UInt32 = 2
DNS_CLASS_CHAOS: UInt32 = 3
DNS_CLASS_HESIOD: UInt32 = 4
DNS_CLASS_NONE: UInt32 = 254
DNS_CLASS_ALL: UInt32 = 255
DNS_CLASS_ANY: UInt32 = 255
DNS_CLASS_UNICAST_RESPONSE: UInt32 = 32768
DNS_RCLASS_INTERNET: UInt32 = 256
DNS_RCLASS_CSNET: UInt32 = 512
DNS_RCLASS_CHAOS: UInt32 = 768
DNS_RCLASS_HESIOD: UInt32 = 1024
DNS_RCLASS_NONE: UInt32 = 65024
DNS_RCLASS_ALL: UInt32 = 65280
DNS_RCLASS_ANY: UInt32 = 65280
DNS_RCLASS_UNICAST_RESPONSE: UInt32 = 128
DNS_RCLASS_MDNS_CACHE_FLUSH: UInt32 = 128
DNS_RTYPE_A: UInt32 = 256
DNS_RTYPE_NS: UInt32 = 512
DNS_RTYPE_MD: UInt32 = 768
DNS_RTYPE_MF: UInt32 = 1024
DNS_RTYPE_CNAME: UInt32 = 1280
DNS_RTYPE_SOA: UInt32 = 1536
DNS_RTYPE_MB: UInt32 = 1792
DNS_RTYPE_MG: UInt32 = 2048
DNS_RTYPE_MR: UInt32 = 2304
DNS_RTYPE_NULL: UInt32 = 2560
DNS_RTYPE_WKS: UInt32 = 2816
DNS_RTYPE_PTR: UInt32 = 3072
DNS_RTYPE_HINFO: UInt32 = 3328
DNS_RTYPE_MINFO: UInt32 = 3584
DNS_RTYPE_MX: UInt32 = 3840
DNS_RTYPE_TEXT: UInt32 = 4096
DNS_RTYPE_RP: UInt32 = 4352
DNS_RTYPE_AFSDB: UInt32 = 4608
DNS_RTYPE_X25: UInt32 = 4864
DNS_RTYPE_ISDN: UInt32 = 5120
DNS_RTYPE_RT: UInt32 = 5376
DNS_RTYPE_NSAP: UInt32 = 5632
DNS_RTYPE_NSAPPTR: UInt32 = 5888
DNS_RTYPE_SIG: UInt32 = 6144
DNS_RTYPE_KEY: UInt32 = 6400
DNS_RTYPE_PX: UInt32 = 6656
DNS_RTYPE_GPOS: UInt32 = 6912
DNS_RTYPE_AAAA: UInt32 = 7168
DNS_RTYPE_LOC: UInt32 = 7424
DNS_RTYPE_NXT: UInt32 = 7680
DNS_RTYPE_EID: UInt32 = 7936
DNS_RTYPE_NIMLOC: UInt32 = 8192
DNS_RTYPE_SRV: UInt32 = 8448
DNS_RTYPE_ATMA: UInt32 = 8704
DNS_RTYPE_NAPTR: UInt32 = 8960
DNS_RTYPE_KX: UInt32 = 9216
DNS_RTYPE_CERT: UInt32 = 9472
DNS_RTYPE_A6: UInt32 = 9728
DNS_RTYPE_DNAME: UInt32 = 9984
DNS_RTYPE_SINK: UInt32 = 10240
DNS_RTYPE_OPT: UInt32 = 10496
DNS_RTYPE_DS: UInt32 = 11008
DNS_RTYPE_RRSIG: UInt32 = 11776
DNS_RTYPE_NSEC: UInt32 = 12032
DNS_RTYPE_DNSKEY: UInt32 = 12288
DNS_RTYPE_DHCID: UInt32 = 12544
DNS_RTYPE_NSEC3: UInt32 = 12800
DNS_RTYPE_NSEC3PARAM: UInt32 = 13056
DNS_RTYPE_TLSA: UInt32 = 13312
DNS_RTYPE_UINFO: UInt32 = 25600
DNS_RTYPE_UID: UInt32 = 25856
DNS_RTYPE_GID: UInt32 = 26112
DNS_RTYPE_UNSPEC: UInt32 = 26368
DNS_RTYPE_TKEY: UInt32 = 63744
DNS_RTYPE_TSIG: UInt32 = 64000
DNS_RTYPE_IXFR: UInt32 = 64256
DNS_RTYPE_AXFR: UInt32 = 64512
DNS_RTYPE_MAILB: UInt32 = 64768
DNS_RTYPE_MAILA: UInt32 = 65024
DNS_RTYPE_ALL: UInt32 = 65280
DNS_RTYPE_ANY: UInt32 = 65280
DNS_RTYPE_WINS: UInt32 = 511
DNS_RTYPE_WINSR: UInt32 = 767
DNS_ATMA_FORMAT_E164: UInt32 = 1
DNS_ATMA_FORMAT_AESA: UInt32 = 2
DNS_ATMA_MAX_ADDR_LENGTH: UInt32 = 20
DNS_ATMA_AESA_ADDR_LENGTH: UInt32 = 20
DNS_ATMA_MAX_RECORD_LENGTH: UInt32 = 21
DNSSEC_ALGORITHM_RSAMD5: UInt32 = 1
DNSSEC_ALGORITHM_RSASHA1: UInt32 = 5
DNSSEC_ALGORITHM_RSASHA1_NSEC3: UInt32 = 7
DNSSEC_ALGORITHM_RSASHA256: UInt32 = 8
DNSSEC_ALGORITHM_RSASHA512: UInt32 = 10
DNSSEC_ALGORITHM_ECDSAP256_SHA256: UInt32 = 13
DNSSEC_ALGORITHM_ECDSAP384_SHA384: UInt32 = 14
DNSSEC_ALGORITHM_NULL: UInt32 = 253
DNSSEC_ALGORITHM_PRIVATE: UInt32 = 254
DNSSEC_DIGEST_ALGORITHM_SHA1: UInt32 = 1
DNSSEC_DIGEST_ALGORITHM_SHA256: UInt32 = 2
DNSSEC_DIGEST_ALGORITHM_SHA384: UInt32 = 4
DNSSEC_PROTOCOL_NONE: UInt32 = 0
DNSSEC_PROTOCOL_TLS: UInt32 = 1
DNSSEC_PROTOCOL_EMAIL: UInt32 = 2
DNSSEC_PROTOCOL_DNSSEC: UInt32 = 3
DNSSEC_PROTOCOL_IPSEC: UInt32 = 4
DNSSEC_KEY_FLAG_NOAUTH: UInt32 = 1
DNSSEC_KEY_FLAG_NOCONF: UInt32 = 2
DNSSEC_KEY_FLAG_FLAG2: UInt32 = 4
DNSSEC_KEY_FLAG_EXTEND: UInt32 = 8
DNSSEC_KEY_FLAG_FLAG4: UInt32 = 16
DNSSEC_KEY_FLAG_FLAG5: UInt32 = 32
DNSSEC_KEY_FLAG_USER: UInt32 = 0
DNSSEC_KEY_FLAG_ZONE: UInt32 = 64
DNSSEC_KEY_FLAG_HOST: UInt32 = 128
DNSSEC_KEY_FLAG_NTPE3: UInt32 = 192
DNSSEC_KEY_FLAG_FLAG8: UInt32 = 256
DNSSEC_KEY_FLAG_FLAG9: UInt32 = 512
DNSSEC_KEY_FLAG_FLAG10: UInt32 = 1024
DNSSEC_KEY_FLAG_FLAG11: UInt32 = 2048
DNSSEC_KEY_FLAG_SIG0: UInt32 = 0
DNSSEC_KEY_FLAG_SIG1: UInt32 = 4096
DNSSEC_KEY_FLAG_SIG2: UInt32 = 8192
DNSSEC_KEY_FLAG_SIG3: UInt32 = 12288
DNSSEC_KEY_FLAG_SIG4: UInt32 = 16384
DNSSEC_KEY_FLAG_SIG5: UInt32 = 20480
DNSSEC_KEY_FLAG_SIG6: UInt32 = 24576
DNSSEC_KEY_FLAG_SIG7: UInt32 = 28672
DNSSEC_KEY_FLAG_SIG8: UInt32 = 32768
DNSSEC_KEY_FLAG_SIG9: UInt32 = 36864
DNSSEC_KEY_FLAG_SIG10: UInt32 = 40960
DNSSEC_KEY_FLAG_SIG11: UInt32 = 45056
DNSSEC_KEY_FLAG_SIG12: UInt32 = 49152
DNSSEC_KEY_FLAG_SIG13: UInt32 = 53248
DNSSEC_KEY_FLAG_SIG14: UInt32 = 57344
DNSSEC_KEY_FLAG_SIG15: UInt32 = 61440
DNS_TKEY_MODE_SERVER_ASSIGN: UInt32 = 1
DNS_TKEY_MODE_DIFFIE_HELLMAN: UInt32 = 2
DNS_TKEY_MODE_GSS: UInt32 = 3
DNS_TKEY_MODE_RESOLVER_ASSIGN: UInt32 = 4
DNS_WINS_FLAG_SCOPE: UInt32 = 2147483648
DNS_WINS_FLAG_LOCAL: UInt32 = 65536
DNS_CONFIG_FLAG_ALLOC: UInt32 = 1
DDR_MAX_IP_HINTS: UInt32 = 4
DNSREC_SECTION: UInt32 = 3
DNSREC_QUESTION: UInt32 = 0
DNSREC_ANSWER: UInt32 = 1
DNSREC_AUTHORITY: UInt32 = 2
DNSREC_ADDITIONAL: UInt32 = 3
DNSREC_ZONE: UInt32 = 0
DNSREC_PREREQ: UInt32 = 1
DNSREC_UPDATE: UInt32 = 2
DNSREC_DELETE: UInt32 = 4
DNSREC_NOEXIST: UInt32 = 4
DNS_CUSTOM_SERVER_TYPE_UDP: UInt32 = 1
DNS_CUSTOM_SERVER_TYPE_DOH: UInt32 = 2
DNS_CUSTOM_SERVER_UDP_FALLBACK: UInt32 = 1
DNS_APP_SETTINGS_VERSION1: UInt32 = 1
DNS_APP_SETTINGS_EXCLUSIVE_SERVERS: UInt32 = 1
DNS_UPDATE_SECURITY_USE_DEFAULT: UInt32 = 0
DNS_UPDATE_SECURITY_OFF: UInt32 = 16
DNS_UPDATE_SECURITY_ON: UInt32 = 32
DNS_UPDATE_SECURITY_ONLY: UInt32 = 256
DNS_UPDATE_CACHE_SECURITY_CONTEXT: UInt32 = 512
DNS_UPDATE_TEST_USE_LOCAL_SYS_ACCT: UInt32 = 1024
DNS_UPDATE_FORCE_SECURITY_NEGO: UInt32 = 2048
DNS_UPDATE_TRY_ALL_MASTER_SERVERS: UInt32 = 4096
DNS_UPDATE_SKIP_NO_UPDATE_ADAPTERS: UInt32 = 8192
DNS_UPDATE_REMOTE_SERVER: UInt32 = 16384
DNS_UPDATE_RESERVED: UInt32 = 4294901760
DNS_VALSVR_ERROR_INVALID_ADDR: UInt32 = 1
DNS_VALSVR_ERROR_INVALID_NAME: UInt32 = 2
DNS_VALSVR_ERROR_UNREACHABLE: UInt32 = 3
DNS_VALSVR_ERROR_NO_RESPONSE: UInt32 = 4
DNS_VALSVR_ERROR_NO_AUTH: UInt32 = 5
DNS_VALSVR_ERROR_REFUSED: UInt32 = 6
DNS_VALSVR_ERROR_NO_TCP: UInt32 = 16
DNS_VALSVR_ERROR_UNKNOWN: UInt32 = 255
DNS_CONNECTION_NAME_MAX_LENGTH: UInt32 = 64
DNS_CONNECTION_PROXY_INFO_CURRENT_VERSION: UInt32 = 1
DNS_CONNECTION_PROXY_INFO_SERVER_MAX_LENGTH: UInt32 = 256
DNS_CONNECTION_PROXY_INFO_FRIENDLY_NAME_MAX_LENGTH: UInt32 = 64
DNS_CONNECTION_PROXY_INFO_USERNAME_MAX_LENGTH: UInt32 = 128
DNS_CONNECTION_PROXY_INFO_PASSWORD_MAX_LENGTH: UInt32 = 128
DNS_CONNECTION_PROXY_INFO_EXCEPTION_MAX_LENGTH: UInt32 = 1024
DNS_CONNECTION_PROXY_INFO_EXTRA_INFO_MAX_LENGTH: UInt32 = 1024
DNS_CONNECTION_PROXY_INFO_FLAG_DISABLED: UInt32 = 1
DNS_CONNECTION_PROXY_INFO_FLAG_BYPASSLOCAL: UInt32 = 2
DNS_CONNECTION_POLICY_ENTRY_ONDEMAND: UInt32 = 1
@winfunctype('DNSAPI.dll')
def DnsQueryConfig(Config: Windows.Win32.NetworkManagement.Dns.DNS_CONFIG_TYPE, Flag: UInt32, pwsAdapterName: Windows.Win32.Foundation.PWSTR, pReserved: VoidPtr, pBuffer: VoidPtr, pBufLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsRecordCopyEx(pRecord: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), CharSetIn: Windows.Win32.NetworkManagement.Dns.DNS_CHARSET, CharSetOut: Windows.Win32.NetworkManagement.Dns.DNS_CHARSET) -> POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head): ...
@winfunctype('DNSAPI.dll')
def DnsRecordSetCopyEx(pRecordSet: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), CharSetIn: Windows.Win32.NetworkManagement.Dns.DNS_CHARSET, CharSetOut: Windows.Win32.NetworkManagement.Dns.DNS_CHARSET) -> POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head): ...
@winfunctype('DNSAPI.dll')
def DnsRecordCompare(pRecord1: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), pRecord2: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DNSAPI.dll')
def DnsRecordSetCompare(pRR1: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), pRR2: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), ppDiff1: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)), ppDiff2: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DNSAPI.dll')
def DnsRecordSetDetach(pRecordList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)) -> POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head): ...
@winfunctype('DNSAPI.dll')
def DnsFree(pData: VoidPtr, FreeType: Windows.Win32.NetworkManagement.Dns.DNS_FREE_TYPE) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsQuery_A(pszName: Windows.Win32.Foundation.PSTR, wType: Windows.Win32.NetworkManagement.Dns.DNS_TYPE, Options: Windows.Win32.NetworkManagement.Dns.DNS_QUERY_OPTIONS, pExtra: VoidPtr, ppQueryResults: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)), pReserved: POINTER(VoidPtr)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('DNSAPI.dll')
def DnsQuery_UTF8(pszName: Windows.Win32.Foundation.PSTR, wType: Windows.Win32.NetworkManagement.Dns.DNS_TYPE, Options: Windows.Win32.NetworkManagement.Dns.DNS_QUERY_OPTIONS, pExtra: VoidPtr, ppQueryResults: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)), pReserved: POINTER(VoidPtr)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('DNSAPI.dll')
def DnsQuery_W(pszName: Windows.Win32.Foundation.PWSTR, wType: Windows.Win32.NetworkManagement.Dns.DNS_TYPE, Options: Windows.Win32.NetworkManagement.Dns.DNS_QUERY_OPTIONS, pExtra: VoidPtr, ppQueryResults: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)), pReserved: POINTER(VoidPtr)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('DNSAPI.dll')
def DnsQueryEx(pQueryRequest: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_QUERY_REQUEST_head), pQueryResults: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_QUERY_RESULT_head), pCancelHandle: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_QUERY_CANCEL_head)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsCancelQuery(pCancelHandle: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_QUERY_CANCEL_head)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsFreeCustomServers(pcServers: POINTER(UInt32), ppServers: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head))) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsGetApplicationSettings(pcServers: POINTER(UInt32), ppDefaultServers: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head)), pSettings: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_APPLICATION_SETTINGS_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsSetApplicationSettings(cServers: UInt32, pServers: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head), pSettings: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_APPLICATION_SETTINGS_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsAcquireContextHandle_W(CredentialFlags: UInt32, Credentials: VoidPtr, pContext: POINTER(Windows.Win32.Foundation.HANDLE)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsAcquireContextHandle_A(CredentialFlags: UInt32, Credentials: VoidPtr, pContext: POINTER(Windows.Win32.Foundation.HANDLE)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsReleaseContextHandle(hContext: Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsModifyRecordsInSet_W(pAddRecords: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), pDeleteRecords: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), Options: UInt32, hCredentials: Windows.Win32.Foundation.HANDLE, pExtraList: VoidPtr, pReserved: VoidPtr) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsModifyRecordsInSet_A(pAddRecords: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), pDeleteRecords: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), Options: UInt32, hCredentials: Windows.Win32.Foundation.HANDLE, pExtraList: VoidPtr, pReserved: VoidPtr) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsModifyRecordsInSet_UTF8(pAddRecords: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), pDeleteRecords: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), Options: UInt32, hCredentials: Windows.Win32.Foundation.HANDLE, pExtraList: VoidPtr, pReserved: VoidPtr) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsReplaceRecordSetW(pReplaceSet: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), Options: UInt32, hContext: Windows.Win32.Foundation.HANDLE, pExtraInfo: VoidPtr, pReserved: VoidPtr) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsReplaceRecordSetA(pReplaceSet: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), Options: UInt32, hContext: Windows.Win32.Foundation.HANDLE, pExtraInfo: VoidPtr, pReserved: VoidPtr) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsReplaceRecordSetUTF8(pReplaceSet: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head), Options: UInt32, hContext: Windows.Win32.Foundation.HANDLE, pExtraInfo: VoidPtr, pReserved: VoidPtr) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsValidateName_W(pszName: Windows.Win32.Foundation.PWSTR, Format: Windows.Win32.NetworkManagement.Dns.DNS_NAME_FORMAT) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsValidateName_A(pszName: Windows.Win32.Foundation.PSTR, Format: Windows.Win32.NetworkManagement.Dns.DNS_NAME_FORMAT) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsValidateName_UTF8(pszName: Windows.Win32.Foundation.PSTR, Format: Windows.Win32.NetworkManagement.Dns.DNS_NAME_FORMAT) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsNameCompare_A(pName1: Windows.Win32.Foundation.PSTR, pName2: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DNSAPI.dll')
def DnsNameCompare_W(pName1: Windows.Win32.Foundation.PWSTR, pName2: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DNSAPI.dll')
def DnsWriteQuestionToBuffer_W(pDnsBuffer: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head), pdwBufferSize: POINTER(UInt32), pszName: Windows.Win32.Foundation.PWSTR, wType: UInt16, Xid: UInt16, fRecursionDesired: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DNSAPI.dll')
def DnsWriteQuestionToBuffer_UTF8(pDnsBuffer: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head), pdwBufferSize: POINTER(UInt32), pszName: Windows.Win32.Foundation.PSTR, wType: UInt16, Xid: UInt16, fRecursionDesired: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('DNSAPI.dll')
def DnsExtractRecordsFromMessage_W(pDnsBuffer: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head), wMessageLength: UInt16, ppRecord: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head))) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsExtractRecordsFromMessage_UTF8(pDnsBuffer: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head), wMessageLength: UInt16, ppRecord: POINTER(POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head))) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsGetProxyInformation(hostName: Windows.Win32.Foundation.PWSTR, proxyInformation: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_PROXY_INFORMATION_head), defaultProxyInformation: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_PROXY_INFORMATION_head), completionRoutine: Windows.Win32.NetworkManagement.Dns.DNS_PROXY_COMPLETION_ROUTINE, completionContext: VoidPtr) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsFreeProxyName(proxyName: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionGetProxyInfoForHostUrl(pwszHostUrl: Windows.Win32.Foundation.PWSTR, pSelectionContext: POINTER(Byte), dwSelectionContextLength: UInt32, dwExplicitInterfaceIndex: UInt32, pProxyInfoEx: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_EX_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionGetProxyInfoForHostUrlEx(pwszHostUrl: Windows.Win32.Foundation.PWSTR, pSelectionContext: POINTER(Byte), dwSelectionContextLength: UInt32, dwExplicitInterfaceIndex: UInt32, pwszConnectionName: Windows.Win32.Foundation.PWSTR, pProxyInfoEx: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_EX_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionFreeProxyInfoEx(pProxyInfoEx: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_EX_head)) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionGetProxyInfo(pwszConnectionName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE, pProxyInfo: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionFreeProxyInfo(pProxyInfo: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_head)) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionSetProxyInfo(pwszConnectionName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE, pProxyInfo: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionDeleteProxyInfo(pwszConnectionName: Windows.Win32.Foundation.PWSTR, Type: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionGetProxyList(pwszConnectionName: Windows.Win32.Foundation.PWSTR, pProxyList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_LIST_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionFreeProxyList(pProxyList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_LIST_head)) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionGetNameList(pNameList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_NAME_LIST_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionFreeNameList(pNameList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_NAME_LIST_head)) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionUpdateIfIndexTable(pConnectionIfIndexEntries: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_IFINDEX_LIST_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionSetPolicyEntries(PolicyEntryTag: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_POLICY_TAG, pPolicyEntryList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_POLICY_ENTRY_LIST_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsConnectionDeletePolicyEntries(PolicyEntryTag: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_POLICY_TAG) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsServiceConstructInstance(pServiceName: Windows.Win32.Foundation.PWSTR, pHostName: Windows.Win32.Foundation.PWSTR, pIp4: POINTER(UInt32), pIp6: POINTER(Windows.Win32.NetworkManagement.Dns.IP6_ADDRESS_head), wPort: UInt16, wPriority: UInt16, wWeight: UInt16, dwPropertiesCount: UInt32, keys: POINTER(Windows.Win32.Foundation.PWSTR), values: POINTER(Windows.Win32.Foundation.PWSTR)) -> POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head): ...
@winfunctype('DNSAPI.dll')
def DnsServiceCopyInstance(pOrig: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head)) -> POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head): ...
@winfunctype('DNSAPI.dll')
def DnsServiceFreeInstance(pInstance: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head)) -> Void: ...
@winfunctype('DNSAPI.dll')
def DnsServiceBrowse(pRequest: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_BROWSE_REQUEST_head), pCancel: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsServiceBrowseCancel(pCancelHandle: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsServiceResolve(pRequest: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_RESOLVE_REQUEST_head), pCancel: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsServiceResolveCancel(pCancelHandle: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsServiceRegister(pRequest: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_REGISTER_REQUEST_head), pCancel: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsServiceDeRegister(pRequest: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_REGISTER_REQUEST_head), pCancel: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsServiceRegisterCancel(pCancelHandle: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head)) -> UInt32: ...
@winfunctype('DNSAPI.dll')
def DnsStartMulticastQuery(pQueryRequest: POINTER(Windows.Win32.NetworkManagement.Dns.MDNS_QUERY_REQUEST_head), pHandle: POINTER(Windows.Win32.NetworkManagement.Dns.MDNS_QUERY_HANDLE_head)) -> Int32: ...
@winfunctype('DNSAPI.dll')
def DnsStopMulticastQuery(pHandle: POINTER(Windows.Win32.NetworkManagement.Dns.MDNS_QUERY_HANDLE_head)) -> Int32: ...
class DNS_AAAA_DATA(EasyCastStructure):
    Ip6Address: Windows.Win32.NetworkManagement.Dns.IP6_ADDRESS
class DNS_ADDR(EasyCastStructure):
    MaxSa: Windows.Win32.Foundation.CHAR * 32
    Data: _Data_e__Union
    class _Data_e__Union(EasyCastUnion):
        DnsAddrUserDword: UInt32 * 8
        _pack_ = 1
class DNS_ADDR_ARRAY(EasyCastStructure):
    MaxCount: UInt32
    AddrCount: UInt32
    Tag: UInt32
    Family: UInt16
    WordReserved: UInt16
    Flags: UInt32
    MatchFlag: UInt32
    Reserved1: UInt32
    Reserved2: UInt32
    AddrArray: Windows.Win32.NetworkManagement.Dns.DNS_ADDR * 1
    _pack_ = 1
class DNS_APPLICATION_SETTINGS(EasyCastStructure):
    Version: UInt32
    Flags: UInt64
class DNS_ATMA_DATA(EasyCastStructure):
    AddressType: Byte
    Address: Byte * 20
class DNS_A_DATA(EasyCastStructure):
    IpAddress: UInt32
DNS_CHARSET = Int32
DNS_CHARSET_DnsCharSetUnknown: DNS_CHARSET = 0
DNS_CHARSET_DnsCharSetUnicode: DNS_CHARSET = 1
DNS_CHARSET_DnsCharSetUtf8: DNS_CHARSET = 2
DNS_CHARSET_DnsCharSetAnsi: DNS_CHARSET = 3
DNS_CONFIG_TYPE = Int32
DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_W: DNS_CONFIG_TYPE = 0
DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_A: DNS_CONFIG_TYPE = 1
DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_UTF8: DNS_CONFIG_TYPE = 2
DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_W: DNS_CONFIG_TYPE = 3
DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_A: DNS_CONFIG_TYPE = 4
DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_UTF8: DNS_CONFIG_TYPE = 5
DNS_CONFIG_TYPE_DnsConfigDnsServerList: DNS_CONFIG_TYPE = 6
DNS_CONFIG_TYPE_DnsConfigSearchList: DNS_CONFIG_TYPE = 7
DNS_CONFIG_TYPE_DnsConfigAdapterInfo: DNS_CONFIG_TYPE = 8
DNS_CONFIG_TYPE_DnsConfigPrimaryHostNameRegistrationEnabled: DNS_CONFIG_TYPE = 9
DNS_CONFIG_TYPE_DnsConfigAdapterHostNameRegistrationEnabled: DNS_CONFIG_TYPE = 10
DNS_CONFIG_TYPE_DnsConfigAddressRegistrationMaxCount: DNS_CONFIG_TYPE = 11
DNS_CONFIG_TYPE_DnsConfigHostName_W: DNS_CONFIG_TYPE = 12
DNS_CONFIG_TYPE_DnsConfigHostName_A: DNS_CONFIG_TYPE = 13
DNS_CONFIG_TYPE_DnsConfigHostName_UTF8: DNS_CONFIG_TYPE = 14
DNS_CONFIG_TYPE_DnsConfigFullHostName_W: DNS_CONFIG_TYPE = 15
DNS_CONFIG_TYPE_DnsConfigFullHostName_A: DNS_CONFIG_TYPE = 16
DNS_CONFIG_TYPE_DnsConfigFullHostName_UTF8: DNS_CONFIG_TYPE = 17
DNS_CONFIG_TYPE_DnsConfigNameServer: DNS_CONFIG_TYPE = 18
class DNS_CONNECTION_IFINDEX_ENTRY(EasyCastStructure):
    pwszConnectionName: Windows.Win32.Foundation.PWSTR
    dwIfIndex: UInt32
class DNS_CONNECTION_IFINDEX_LIST(EasyCastStructure):
    pConnectionIfIndexEntries: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_IFINDEX_ENTRY_head)
    nEntries: UInt32
class DNS_CONNECTION_NAME(EasyCastStructure):
    wszName: Char * 65
class DNS_CONNECTION_NAME_LIST(EasyCastStructure):
    cNames: UInt32
    pNames: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_NAME_head)
class DNS_CONNECTION_POLICY_ENTRY(EasyCastStructure):
    pwszHost: Windows.Win32.Foundation.PWSTR
    pwszAppId: Windows.Win32.Foundation.PWSTR
    cbAppSid: UInt32
    pbAppSid: POINTER(Byte)
    nConnections: UInt32
    ppwszConnections: POINTER(Windows.Win32.Foundation.PWSTR)
    dwPolicyEntryFlags: UInt32
class DNS_CONNECTION_POLICY_ENTRY_LIST(EasyCastStructure):
    pPolicyEntries: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_POLICY_ENTRY_head)
    nEntries: UInt32
DNS_CONNECTION_POLICY_TAG = Int32
TAG_DNS_CONNECTION_POLICY_TAG_DEFAULT: DNS_CONNECTION_POLICY_TAG = 0
TAG_DNS_CONNECTION_POLICY_TAG_CONNECTION_MANAGER: DNS_CONNECTION_POLICY_TAG = 1
TAG_DNS_CONNECTION_POLICY_TAG_WWWPT: DNS_CONNECTION_POLICY_TAG = 2
class DNS_CONNECTION_PROXY_ELEMENT(EasyCastStructure):
    Type: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE
    Info: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO
class DNS_CONNECTION_PROXY_INFO(EasyCastStructure):
    Version: UInt32
    pwszFriendlyName: Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    Switch: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_SWITCH
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Config: _DNS_CONNECTION_PROXY_INFO_CONFIG
        Script: _DNS_CONNECTION_PROXY_INFO_SCRIPT
        class _DNS_CONNECTION_PROXY_INFO_CONFIG(EasyCastStructure):
            pwszServer: Windows.Win32.Foundation.PWSTR
            pwszUsername: Windows.Win32.Foundation.PWSTR
            pwszPassword: Windows.Win32.Foundation.PWSTR
            pwszException: Windows.Win32.Foundation.PWSTR
            pwszExtraInfo: Windows.Win32.Foundation.PWSTR
            Port: UInt16
        class _DNS_CONNECTION_PROXY_INFO_SCRIPT(EasyCastStructure):
            pwszScript: Windows.Win32.Foundation.PWSTR
            pwszUsername: Windows.Win32.Foundation.PWSTR
            pwszPassword: Windows.Win32.Foundation.PWSTR
class DNS_CONNECTION_PROXY_INFO_EX(EasyCastStructure):
    ProxyInfo: Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO
    dwInterfaceIndex: UInt32
    pwszConnectionName: Windows.Win32.Foundation.PWSTR
    fDirectConfiguration: Windows.Win32.Foundation.BOOL
    hConnection: Windows.Win32.Foundation.HANDLE
DNS_CONNECTION_PROXY_INFO_SWITCH = Int32
DNS_CONNECTION_PROXY_INFO_SWITCH_CONFIG: DNS_CONNECTION_PROXY_INFO_SWITCH = 0
DNS_CONNECTION_PROXY_INFO_SWITCH_SCRIPT: DNS_CONNECTION_PROXY_INFO_SWITCH = 1
DNS_CONNECTION_PROXY_INFO_SWITCH_WPAD: DNS_CONNECTION_PROXY_INFO_SWITCH = 2
class DNS_CONNECTION_PROXY_LIST(EasyCastStructure):
    cProxies: UInt32
    pProxies: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CONNECTION_PROXY_ELEMENT_head)
DNS_CONNECTION_PROXY_TYPE = Int32
DNS_CONNECTION_PROXY_TYPE_NULL: DNS_CONNECTION_PROXY_TYPE = 0
DNS_CONNECTION_PROXY_TYPE_HTTP: DNS_CONNECTION_PROXY_TYPE = 1
DNS_CONNECTION_PROXY_TYPE_WAP: DNS_CONNECTION_PROXY_TYPE = 2
DNS_CONNECTION_PROXY_TYPE_SOCKS4: DNS_CONNECTION_PROXY_TYPE = 4
DNS_CONNECTION_PROXY_TYPE_SOCKS5: DNS_CONNECTION_PROXY_TYPE = 5
class DNS_CUSTOM_SERVER(EasyCastStructure):
    dwServerType: UInt32
    ullFlags: UInt64
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(EasyCastUnion):
        pwszTemplate: Windows.Win32.Foundation.PWSTR
    class _Anonymous2_e__Union(EasyCastUnion):
        MaxSa: Windows.Win32.Foundation.CHAR * 32
class DNS_DHCID_DATA(EasyCastStructure):
    dwByteCount: UInt32
    DHCID: Byte * 1
class DNS_DS_DATA(EasyCastStructure):
    wKeyTag: UInt16
    chAlgorithm: Byte
    chDigestType: Byte
    wDigestLength: UInt16
    wPad: UInt16
    Digest: Byte * 1
DNS_FREE_TYPE = Int32
DNS_FREE_TYPE_DnsFreeFlat: DNS_FREE_TYPE = 0
DNS_FREE_TYPE_DnsFreeRecordList: DNS_FREE_TYPE = 1
DNS_FREE_TYPE_DnsFreeParsedMessageFields: DNS_FREE_TYPE = 2
class DNS_HEADER(EasyCastStructure):
    Xid: UInt16
    _bitfield1: Byte
    _bitfield2: Byte
    QuestionCount: UInt16
    AnswerCount: UInt16
    NameServerCount: UInt16
    AdditionalCount: UInt16
    _pack_ = 1
class DNS_HEADER_EXT(EasyCastStructure):
    _bitfield: UInt16
    chRcode: Byte
    chVersion: Byte
    _pack_ = 1
class DNS_KEY_DATA(EasyCastStructure):
    wFlags: UInt16
    chProtocol: Byte
    chAlgorithm: Byte
    wKeyLength: UInt16
    wPad: UInt16
    Key: Byte * 1
class DNS_LOC_DATA(EasyCastStructure):
    wVersion: UInt16
    wSize: UInt16
    wHorPrec: UInt16
    wVerPrec: UInt16
    dwLatitude: UInt32
    dwLongitude: UInt32
    dwAltitude: UInt32
class DNS_MESSAGE_BUFFER(EasyCastStructure):
    MessageHead: Windows.Win32.NetworkManagement.Dns.DNS_HEADER
    MessageBody: Windows.Win32.Foundation.CHAR * 1
class DNS_MINFO_DATAA(EasyCastStructure):
    pNameMailbox: Windows.Win32.Foundation.PSTR
    pNameErrorsMailbox: Windows.Win32.Foundation.PSTR
class DNS_MINFO_DATAW(EasyCastStructure):
    pNameMailbox: Windows.Win32.Foundation.PWSTR
    pNameErrorsMailbox: Windows.Win32.Foundation.PWSTR
class DNS_MX_DATAA(EasyCastStructure):
    pNameExchange: Windows.Win32.Foundation.PSTR
    wPreference: UInt16
    Pad: UInt16
class DNS_MX_DATAW(EasyCastStructure):
    pNameExchange: Windows.Win32.Foundation.PWSTR
    wPreference: UInt16
    Pad: UInt16
DNS_NAME_FORMAT = Int32
DNS_NAME_FORMAT_DnsNameDomain: DNS_NAME_FORMAT = 0
DNS_NAME_FORMAT_DnsNameDomainLabel: DNS_NAME_FORMAT = 1
DNS_NAME_FORMAT_DnsNameHostnameFull: DNS_NAME_FORMAT = 2
DNS_NAME_FORMAT_DnsNameHostnameLabel: DNS_NAME_FORMAT = 3
DNS_NAME_FORMAT_DnsNameWildcard: DNS_NAME_FORMAT = 4
DNS_NAME_FORMAT_DnsNameSrvRecord: DNS_NAME_FORMAT = 5
DNS_NAME_FORMAT_DnsNameValidateTld: DNS_NAME_FORMAT = 6
class DNS_NAPTR_DATAA(EasyCastStructure):
    wOrder: UInt16
    wPreference: UInt16
    pFlags: Windows.Win32.Foundation.PSTR
    pService: Windows.Win32.Foundation.PSTR
    pRegularExpression: Windows.Win32.Foundation.PSTR
    pReplacement: Windows.Win32.Foundation.PSTR
class DNS_NAPTR_DATAW(EasyCastStructure):
    wOrder: UInt16
    wPreference: UInt16
    pFlags: Windows.Win32.Foundation.PWSTR
    pService: Windows.Win32.Foundation.PWSTR
    pRegularExpression: Windows.Win32.Foundation.PWSTR
    pReplacement: Windows.Win32.Foundation.PWSTR
class DNS_NSEC3PARAM_DATA(EasyCastStructure):
    chAlgorithm: Byte
    bFlags: Byte
    wIterations: UInt16
    bSaltLength: Byte
    bPad: Byte * 3
    pbSalt: Byte * 1
class DNS_NSEC3_DATA(EasyCastStructure):
    chAlgorithm: Byte
    bFlags: Byte
    wIterations: UInt16
    bSaltLength: Byte
    bHashLength: Byte
    wTypeBitMapsLength: UInt16
    chData: Byte * 1
class DNS_NSEC_DATAA(EasyCastStructure):
    pNextDomainName: Windows.Win32.Foundation.PSTR
    wTypeBitMapsLength: UInt16
    wPad: UInt16
    TypeBitMaps: Byte * 1
class DNS_NSEC_DATAW(EasyCastStructure):
    pNextDomainName: Windows.Win32.Foundation.PWSTR
    wTypeBitMapsLength: UInt16
    wPad: UInt16
    TypeBitMaps: Byte * 1
class DNS_NULL_DATA(EasyCastStructure):
    dwByteCount: UInt32
    Data: Byte * 1
class DNS_NXT_DATAA(EasyCastStructure):
    pNameNext: Windows.Win32.Foundation.PSTR
    wNumTypes: UInt16
    wTypes: UInt16 * 1
class DNS_NXT_DATAW(EasyCastStructure):
    pNameNext: Windows.Win32.Foundation.PWSTR
    wNumTypes: UInt16
    wTypes: UInt16 * 1
class DNS_OPT_DATA(EasyCastStructure):
    wDataLength: UInt16
    wPad: UInt16
    Data: Byte * 1
@winfunctype_pointer
def DNS_PROXY_COMPLETION_ROUTINE(completionContext: VoidPtr, status: Int32) -> Void: ...
class DNS_PROXY_INFORMATION(EasyCastStructure):
    version: UInt32
    proxyInformationType: Windows.Win32.NetworkManagement.Dns.DNS_PROXY_INFORMATION_TYPE
    proxyName: Windows.Win32.Foundation.PWSTR
DNS_PROXY_INFORMATION_TYPE = Int32
DNS_PROXY_INFORMATION_DIRECT: DNS_PROXY_INFORMATION_TYPE = 0
DNS_PROXY_INFORMATION_DEFAULT_SETTINGS: DNS_PROXY_INFORMATION_TYPE = 1
DNS_PROXY_INFORMATION_PROXY_NAME: DNS_PROXY_INFORMATION_TYPE = 2
DNS_PROXY_INFORMATION_DOES_NOT_EXIST: DNS_PROXY_INFORMATION_TYPE = 3
class DNS_PTR_DATAA(EasyCastStructure):
    pNameHost: Windows.Win32.Foundation.PSTR
class DNS_PTR_DATAW(EasyCastStructure):
    pNameHost: Windows.Win32.Foundation.PWSTR
class DNS_QUERY_CANCEL(EasyCastStructure):
    Reserved: Windows.Win32.Foundation.CHAR * 32
DNS_QUERY_OPTIONS = UInt32
DNS_QUERY_STANDARD: DNS_QUERY_OPTIONS = 0
DNS_QUERY_ACCEPT_TRUNCATED_RESPONSE: DNS_QUERY_OPTIONS = 1
DNS_QUERY_USE_TCP_ONLY: DNS_QUERY_OPTIONS = 2
DNS_QUERY_NO_RECURSION: DNS_QUERY_OPTIONS = 4
DNS_QUERY_BYPASS_CACHE: DNS_QUERY_OPTIONS = 8
DNS_QUERY_NO_WIRE_QUERY: DNS_QUERY_OPTIONS = 16
DNS_QUERY_NO_LOCAL_NAME: DNS_QUERY_OPTIONS = 32
DNS_QUERY_NO_HOSTS_FILE: DNS_QUERY_OPTIONS = 64
DNS_QUERY_NO_NETBT: DNS_QUERY_OPTIONS = 128
DNS_QUERY_WIRE_ONLY: DNS_QUERY_OPTIONS = 256
DNS_QUERY_RETURN_MESSAGE: DNS_QUERY_OPTIONS = 512
DNS_QUERY_MULTICAST_ONLY: DNS_QUERY_OPTIONS = 1024
DNS_QUERY_NO_MULTICAST: DNS_QUERY_OPTIONS = 2048
DNS_QUERY_TREAT_AS_FQDN: DNS_QUERY_OPTIONS = 4096
DNS_QUERY_ADDRCONFIG: DNS_QUERY_OPTIONS = 8192
DNS_QUERY_DUAL_ADDR: DNS_QUERY_OPTIONS = 16384
DNS_QUERY_DONT_RESET_TTL_VALUES: DNS_QUERY_OPTIONS = 1048576
DNS_QUERY_DISABLE_IDN_ENCODING: DNS_QUERY_OPTIONS = 2097152
DNS_QUERY_APPEND_MULTILABEL: DNS_QUERY_OPTIONS = 8388608
DNS_QUERY_DNSSEC_OK: DNS_QUERY_OPTIONS = 16777216
DNS_QUERY_DNSSEC_CHECKING_DISABLED: DNS_QUERY_OPTIONS = 33554432
DNS_QUERY_RESERVED: DNS_QUERY_OPTIONS = 4026531840
DNS_QUERY_CACHE_ONLY: DNS_QUERY_OPTIONS = 16
DNS_QUERY_REQUEST_VERSION1: DNS_QUERY_OPTIONS = 1
DNS_QUERY_REQUEST_VERSION2: DNS_QUERY_OPTIONS = 2
DNS_QUERY_RESULTS_VERSION1: DNS_QUERY_OPTIONS = 1
DNS_QUERY_REQUEST_VERSION3: DNS_QUERY_OPTIONS = 3
class DNS_QUERY_REQUEST(EasyCastStructure):
    Version: UInt32
    QueryName: Windows.Win32.Foundation.PWSTR
    QueryType: UInt16
    QueryOptions: UInt64
    pDnsServerList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_ADDR_ARRAY_head)
    InterfaceIndex: UInt32
    pQueryCompletionCallback: Windows.Win32.NetworkManagement.Dns.PDNS_QUERY_COMPLETION_ROUTINE
    pQueryContext: VoidPtr
class DNS_QUERY_REQUEST3(EasyCastStructure):
    Version: UInt32
    QueryName: Windows.Win32.Foundation.PWSTR
    QueryType: UInt16
    QueryOptions: UInt64
    pDnsServerList: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_ADDR_ARRAY_head)
    InterfaceIndex: UInt32
    pQueryCompletionCallback: Windows.Win32.NetworkManagement.Dns.PDNS_QUERY_COMPLETION_ROUTINE
    pQueryContext: VoidPtr
    IsNetworkQueryRequired: Windows.Win32.Foundation.BOOL
    RequiredNetworkIndex: UInt32
    cCustomServers: UInt32
    pCustomServers: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head)
class DNS_QUERY_RESULT(EasyCastStructure):
    Version: UInt32
    QueryStatus: Int32
    QueryOptions: UInt64
    pQueryRecords: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)
    Reserved: VoidPtr
class DNS_RECORDA(EasyCastStructure):
    pNext: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)
    pName: Windows.Win32.Foundation.PSTR
    wType: UInt16
    wDataLength: UInt16
    Flags: _Flags_e__Union
    dwTtl: UInt32
    dwReserved: UInt32
    Data: _Data_e__Union
    class _Flags_e__Union(EasyCastUnion):
        DW: UInt32
        S: Windows.Win32.NetworkManagement.Dns.DNS_RECORD_FLAGS
    class _Data_e__Union(EasyCastUnion):
        A: Windows.Win32.NetworkManagement.Dns.DNS_A_DATA
        SOA: Windows.Win32.NetworkManagement.Dns.DNS_SOA_DATAA
        Soa: Windows.Win32.NetworkManagement.Dns.DNS_SOA_DATAA
        PTR: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Ptr: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        NS: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Ns: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        CNAME: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Cname: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        DNAME: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Dname: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        MB: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Mb: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        MD: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Md: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        MF: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Mf: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        MG: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Mg: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        MR: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        Mr: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAA
        MINFO: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAA
        Minfo: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAA
        RP: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAA
        Rp: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAA
        MX: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAA
        Mx: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAA
        AFSDB: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAA
        Afsdb: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAA
        RT: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAA
        Rt: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAA
        HINFO: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAA
        Hinfo: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAA
        ISDN: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAA
        Isdn: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAA
        TXT: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAA
        Txt: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAA
        X25: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAA
        Null: Windows.Win32.NetworkManagement.Dns.DNS_NULL_DATA
        WKS: Windows.Win32.NetworkManagement.Dns.DNS_WKS_DATA
        Wks: Windows.Win32.NetworkManagement.Dns.DNS_WKS_DATA
        AAAA: Windows.Win32.NetworkManagement.Dns.DNS_AAAA_DATA
        KEY: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        Key: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        SIG: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAA
        Sig: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAA
        ATMA: Windows.Win32.NetworkManagement.Dns.DNS_ATMA_DATA
        Atma: Windows.Win32.NetworkManagement.Dns.DNS_ATMA_DATA
        NXT: Windows.Win32.NetworkManagement.Dns.DNS_NXT_DATAA
        Nxt: Windows.Win32.NetworkManagement.Dns.DNS_NXT_DATAA
        SRV: Windows.Win32.NetworkManagement.Dns.DNS_SRV_DATAA
        Srv: Windows.Win32.NetworkManagement.Dns.DNS_SRV_DATAA
        NAPTR: Windows.Win32.NetworkManagement.Dns.DNS_NAPTR_DATAA
        Naptr: Windows.Win32.NetworkManagement.Dns.DNS_NAPTR_DATAA
        OPT: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
        Opt: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
        DS: Windows.Win32.NetworkManagement.Dns.DNS_DS_DATA
        Ds: Windows.Win32.NetworkManagement.Dns.DNS_DS_DATA
        RRSIG: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAA
        Rrsig: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAA
        NSEC: Windows.Win32.NetworkManagement.Dns.DNS_NSEC_DATAA
        Nsec: Windows.Win32.NetworkManagement.Dns.DNS_NSEC_DATAA
        DNSKEY: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        Dnskey: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        TKEY: Windows.Win32.NetworkManagement.Dns.DNS_TKEY_DATAA
        Tkey: Windows.Win32.NetworkManagement.Dns.DNS_TKEY_DATAA
        TSIG: Windows.Win32.NetworkManagement.Dns.DNS_TSIG_DATAA
        Tsig: Windows.Win32.NetworkManagement.Dns.DNS_TSIG_DATAA
        WINS: Windows.Win32.NetworkManagement.Dns.DNS_WINS_DATA
        Wins: Windows.Win32.NetworkManagement.Dns.DNS_WINS_DATA
        WINSR: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAA
        WinsR: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAA
        NBSTAT: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAA
        Nbstat: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAA
        DHCID: Windows.Win32.NetworkManagement.Dns.DNS_DHCID_DATA
        NSEC3: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3_DATA
        Nsec3: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3_DATA
        NSEC3PARAM: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA
        Nsec3Param: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA
        TLSA: Windows.Win32.NetworkManagement.Dns.DNS_TLSA_DATA
        Tlsa: Windows.Win32.NetworkManagement.Dns.DNS_TLSA_DATA
        SVCB: Windows.Win32.NetworkManagement.Dns.DNS_SVCB_DATA
        Svcb: Windows.Win32.NetworkManagement.Dns.DNS_SVCB_DATA
        UNKNOWN: Windows.Win32.NetworkManagement.Dns.DNS_UNKNOWN_DATA
        Unknown: Windows.Win32.NetworkManagement.Dns.DNS_UNKNOWN_DATA
        pDataPtr: POINTER(Byte)
class DNS_RECORDW(EasyCastStructure):
    pNext: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDW_head)
    pName: Windows.Win32.Foundation.PWSTR
    wType: UInt16
    wDataLength: UInt16
    Flags: _Flags_e__Union
    dwTtl: UInt32
    dwReserved: UInt32
    Data: _Data_e__Union
    class _Flags_e__Union(EasyCastUnion):
        DW: UInt32
        S: Windows.Win32.NetworkManagement.Dns.DNS_RECORD_FLAGS
    class _Data_e__Union(EasyCastUnion):
        A: Windows.Win32.NetworkManagement.Dns.DNS_A_DATA
        SOA: Windows.Win32.NetworkManagement.Dns.DNS_SOA_DATAW
        Soa: Windows.Win32.NetworkManagement.Dns.DNS_SOA_DATAW
        PTR: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Ptr: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        NS: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Ns: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        CNAME: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Cname: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        DNAME: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Dname: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        MB: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Mb: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        MD: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Md: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        MF: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Mf: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        MG: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Mg: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        MR: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        Mr: Windows.Win32.NetworkManagement.Dns.DNS_PTR_DATAW
        MINFO: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAW
        Minfo: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAW
        RP: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAW
        Rp: Windows.Win32.NetworkManagement.Dns.DNS_MINFO_DATAW
        MX: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAW
        Mx: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAW
        AFSDB: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAW
        Afsdb: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAW
        RT: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAW
        Rt: Windows.Win32.NetworkManagement.Dns.DNS_MX_DATAW
        HINFO: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAW
        Hinfo: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAW
        ISDN: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAW
        Isdn: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAW
        TXT: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAW
        Txt: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAW
        X25: Windows.Win32.NetworkManagement.Dns.DNS_TXT_DATAW
        Null: Windows.Win32.NetworkManagement.Dns.DNS_NULL_DATA
        WKS: Windows.Win32.NetworkManagement.Dns.DNS_WKS_DATA
        Wks: Windows.Win32.NetworkManagement.Dns.DNS_WKS_DATA
        AAAA: Windows.Win32.NetworkManagement.Dns.DNS_AAAA_DATA
        KEY: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        Key: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        SIG: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAW
        Sig: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAW
        ATMA: Windows.Win32.NetworkManagement.Dns.DNS_ATMA_DATA
        Atma: Windows.Win32.NetworkManagement.Dns.DNS_ATMA_DATA
        NXT: Windows.Win32.NetworkManagement.Dns.DNS_NXT_DATAW
        Nxt: Windows.Win32.NetworkManagement.Dns.DNS_NXT_DATAW
        SRV: Windows.Win32.NetworkManagement.Dns.DNS_SRV_DATAW
        Srv: Windows.Win32.NetworkManagement.Dns.DNS_SRV_DATAW
        NAPTR: Windows.Win32.NetworkManagement.Dns.DNS_NAPTR_DATAW
        Naptr: Windows.Win32.NetworkManagement.Dns.DNS_NAPTR_DATAW
        OPT: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
        Opt: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
        DS: Windows.Win32.NetworkManagement.Dns.DNS_DS_DATA
        Ds: Windows.Win32.NetworkManagement.Dns.DNS_DS_DATA
        RRSIG: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAW
        Rrsig: Windows.Win32.NetworkManagement.Dns.DNS_SIG_DATAW
        NSEC: Windows.Win32.NetworkManagement.Dns.DNS_NSEC_DATAW
        Nsec: Windows.Win32.NetworkManagement.Dns.DNS_NSEC_DATAW
        DNSKEY: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        Dnskey: Windows.Win32.NetworkManagement.Dns.DNS_KEY_DATA
        TKEY: Windows.Win32.NetworkManagement.Dns.DNS_TKEY_DATAW
        Tkey: Windows.Win32.NetworkManagement.Dns.DNS_TKEY_DATAW
        TSIG: Windows.Win32.NetworkManagement.Dns.DNS_TSIG_DATAW
        Tsig: Windows.Win32.NetworkManagement.Dns.DNS_TSIG_DATAW
        WINS: Windows.Win32.NetworkManagement.Dns.DNS_WINS_DATA
        Wins: Windows.Win32.NetworkManagement.Dns.DNS_WINS_DATA
        WINSR: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAW
        WinsR: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAW
        NBSTAT: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAW
        Nbstat: Windows.Win32.NetworkManagement.Dns.DNS_WINSR_DATAW
        DHCID: Windows.Win32.NetworkManagement.Dns.DNS_DHCID_DATA
        NSEC3: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3_DATA
        Nsec3: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3_DATA
        NSEC3PARAM: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA
        Nsec3Param: Windows.Win32.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA
        TLSA: Windows.Win32.NetworkManagement.Dns.DNS_TLSA_DATA
        Tlsa: Windows.Win32.NetworkManagement.Dns.DNS_TLSA_DATA
        SVCB: Windows.Win32.NetworkManagement.Dns.DNS_SVCB_DATA
        Svcb: Windows.Win32.NetworkManagement.Dns.DNS_SVCB_DATA
        UNKNOWN: Windows.Win32.NetworkManagement.Dns.DNS_UNKNOWN_DATA
        Unknown: Windows.Win32.NetworkManagement.Dns.DNS_UNKNOWN_DATA
        pDataPtr: POINTER(Byte)
class DNS_RECORD_FLAGS(EasyCastStructure):
    _bitfield: UInt32
class DNS_RECORD_OPTW(EasyCastStructure):
    pNext: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDW_head)
    pName: Windows.Win32.Foundation.PWSTR
    wType: UInt16
    wDataLength: UInt16
    Flags: _Flags_e__Union
    ExtHeader: Windows.Win32.NetworkManagement.Dns.DNS_HEADER_EXT
    wPayloadSize: UInt16
    wReserved: UInt16
    Data: _Data_e__Union
    class _Flags_e__Union(EasyCastUnion):
        DW: UInt32
        S: Windows.Win32.NetworkManagement.Dns.DNS_RECORD_FLAGS
    class _Data_e__Union(EasyCastUnion):
        OPT: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
        Opt: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
class DNS_RRSET(EasyCastStructure):
    pFirstRR: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)
    pLastRR: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)
DNS_SECTION = Int32
DNS_SECTION_DnsSectionQuestion: DNS_SECTION = 0
DNS_SECTION_DnsSectionAnswer: DNS_SECTION = 1
DNS_SECTION_DnsSectionAuthority: DNS_SECTION = 2
DNS_SECTION_DnsSectionAddtional: DNS_SECTION = 3
class DNS_SERVICE_BROWSE_REQUEST(EasyCastStructure):
    Version: UInt32
    InterfaceIndex: UInt32
    QueryName: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    pQueryContext: VoidPtr
    class _Anonymous_e__Union(EasyCastUnion):
        pBrowseCallback: Windows.Win32.NetworkManagement.Dns.PDNS_SERVICE_BROWSE_CALLBACK
        pBrowseCallbackV2: Windows.Win32.NetworkManagement.Dns.PDNS_QUERY_COMPLETION_ROUTINE
class DNS_SERVICE_CANCEL(EasyCastStructure):
    reserved: VoidPtr
class DNS_SERVICE_INSTANCE(EasyCastStructure):
    pszInstanceName: Windows.Win32.Foundation.PWSTR
    pszHostName: Windows.Win32.Foundation.PWSTR
    ip4Address: POINTER(UInt32)
    ip6Address: POINTER(Windows.Win32.NetworkManagement.Dns.IP6_ADDRESS_head)
    wPort: UInt16
    wPriority: UInt16
    wWeight: UInt16
    dwPropertyCount: UInt32
    keys: POINTER(Windows.Win32.Foundation.PWSTR)
    values: POINTER(Windows.Win32.Foundation.PWSTR)
    dwInterfaceIndex: UInt32
class DNS_SERVICE_REGISTER_REQUEST(EasyCastStructure):
    Version: UInt32
    InterfaceIndex: UInt32
    pServiceInstance: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head)
    pRegisterCompletionCallback: Windows.Win32.NetworkManagement.Dns.PDNS_SERVICE_REGISTER_COMPLETE
    pQueryContext: VoidPtr
    hCredentials: Windows.Win32.Foundation.HANDLE
    unicastEnabled: Windows.Win32.Foundation.BOOL
class DNS_SERVICE_RESOLVE_REQUEST(EasyCastStructure):
    Version: UInt32
    InterfaceIndex: UInt32
    QueryName: Windows.Win32.Foundation.PWSTR
    pResolveCompletionCallback: Windows.Win32.NetworkManagement.Dns.PDNS_SERVICE_RESOLVE_COMPLETE
    pQueryContext: VoidPtr
class DNS_SIG_DATAA(EasyCastStructure):
    wTypeCovered: UInt16
    chAlgorithm: Byte
    chLabelCount: Byte
    dwOriginalTtl: UInt32
    dwExpiration: UInt32
    dwTimeSigned: UInt32
    wKeyTag: UInt16
    wSignatureLength: UInt16
    pNameSigner: Windows.Win32.Foundation.PSTR
    Signature: Byte * 1
class DNS_SIG_DATAW(EasyCastStructure):
    wTypeCovered: UInt16
    chAlgorithm: Byte
    chLabelCount: Byte
    dwOriginalTtl: UInt32
    dwExpiration: UInt32
    dwTimeSigned: UInt32
    wKeyTag: UInt16
    wSignatureLength: UInt16
    pNameSigner: Windows.Win32.Foundation.PWSTR
    Signature: Byte * 1
class DNS_SOA_DATAA(EasyCastStructure):
    pNamePrimaryServer: Windows.Win32.Foundation.PSTR
    pNameAdministrator: Windows.Win32.Foundation.PSTR
    dwSerialNo: UInt32
    dwRefresh: UInt32
    dwRetry: UInt32
    dwExpire: UInt32
    dwDefaultTtl: UInt32
class DNS_SOA_DATAW(EasyCastStructure):
    pNamePrimaryServer: Windows.Win32.Foundation.PWSTR
    pNameAdministrator: Windows.Win32.Foundation.PWSTR
    dwSerialNo: UInt32
    dwRefresh: UInt32
    dwRetry: UInt32
    dwExpire: UInt32
    dwDefaultTtl: UInt32
class DNS_SRV_DATAA(EasyCastStructure):
    pNameTarget: Windows.Win32.Foundation.PSTR
    wPriority: UInt16
    wWeight: UInt16
    wPort: UInt16
    Pad: UInt16
class DNS_SRV_DATAW(EasyCastStructure):
    pNameTarget: Windows.Win32.Foundation.PWSTR
    wPriority: UInt16
    wWeight: UInt16
    wPort: UInt16
    Pad: UInt16
class DNS_SVCB_DATA(EasyCastStructure):
    wSvcPriority: UInt16
    pszTargetName: Windows.Win32.Foundation.PSTR
    cSvcParams: UInt16
    pSvcParams: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SVCB_PARAM_head)
class DNS_SVCB_PARAM(EasyCastStructure):
    wSvcParamKey: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pIpv4Hints: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SVCB_PARAM_IPV4_head)
        pIpv6Hints: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SVCB_PARAM_IPV6_head)
        pMandatory: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SVCB_PARAM_MANDATORY_head)
        pAlpn: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SVCB_PARAM_ALPN_head)
        wPort: UInt16
        pUnknown: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SVCB_PARAM_UNKNOWN_head)
        pszDohPath: Windows.Win32.Foundation.PSTR
        pReserved: VoidPtr
class DNS_SVCB_PARAM_ALPN(EasyCastStructure):
    cIds: UInt16
    rgIds: Windows.Win32.NetworkManagement.Dns.DNS_SVCB_PARAM_ALPN_ID * 1
class DNS_SVCB_PARAM_ALPN_ID(EasyCastStructure):
    cBytes: Byte
    pbId: POINTER(Byte)
class DNS_SVCB_PARAM_IPV4(EasyCastStructure):
    cIps: UInt16
    rgIps: UInt32 * 1
class DNS_SVCB_PARAM_IPV6(EasyCastStructure):
    cIps: UInt16
    rgIps: Windows.Win32.NetworkManagement.Dns.IP6_ADDRESS * 1
class DNS_SVCB_PARAM_MANDATORY(EasyCastStructure):
    cMandatoryKeys: UInt16
    rgwMandatoryKeys: UInt16 * 1
DNS_SVCB_PARAM_TYPE = Int32
DNS_SVCB_PARAM_TYPE_DnsSvcbParamMandatory: DNS_SVCB_PARAM_TYPE = 0
DNS_SVCB_PARAM_TYPE_DnsSvcbParamAlpn: DNS_SVCB_PARAM_TYPE = 1
DNS_SVCB_PARAM_TYPE_DnsSvcbParamNoDefaultAlpn: DNS_SVCB_PARAM_TYPE = 2
DNS_SVCB_PARAM_TYPE_DnsSvcbParamPort: DNS_SVCB_PARAM_TYPE = 3
DNS_SVCB_PARAM_TYPE_DnsSvcbParamIpv4Hint: DNS_SVCB_PARAM_TYPE = 4
DNS_SVCB_PARAM_TYPE_DnsSvcbParamEch: DNS_SVCB_PARAM_TYPE = 5
DNS_SVCB_PARAM_TYPE_DnsSvcbParamIpv6Hint: DNS_SVCB_PARAM_TYPE = 6
DNS_SVCB_PARAM_TYPE_DnsSvcbParamDohPath: DNS_SVCB_PARAM_TYPE = 7
DNS_SVCB_PARAM_TYPE_DnsSvcbParamDohPathQuad9: DNS_SVCB_PARAM_TYPE = 65380
DNS_SVCB_PARAM_TYPE_DnsSvcbParamDohPathOpenDns: DNS_SVCB_PARAM_TYPE = 65432
class DNS_SVCB_PARAM_UNKNOWN(EasyCastStructure):
    cBytes: UInt16
    pbSvcParamValue: Byte * 1
class DNS_TKEY_DATAA(EasyCastStructure):
    pNameAlgorithm: Windows.Win32.Foundation.PSTR
    pAlgorithmPacket: POINTER(Byte)
    pKey: POINTER(Byte)
    pOtherData: POINTER(Byte)
    dwCreateTime: UInt32
    dwExpireTime: UInt32
    wMode: UInt16
    wError: UInt16
    wKeyLength: UInt16
    wOtherLength: UInt16
    cAlgNameLength: Byte
    bPacketPointers: Windows.Win32.Foundation.BOOL
class DNS_TKEY_DATAW(EasyCastStructure):
    pNameAlgorithm: Windows.Win32.Foundation.PWSTR
    pAlgorithmPacket: POINTER(Byte)
    pKey: POINTER(Byte)
    pOtherData: POINTER(Byte)
    dwCreateTime: UInt32
    dwExpireTime: UInt32
    wMode: UInt16
    wError: UInt16
    wKeyLength: UInt16
    wOtherLength: UInt16
    cAlgNameLength: Byte
    bPacketPointers: Windows.Win32.Foundation.BOOL
class DNS_TLSA_DATA(EasyCastStructure):
    bCertUsage: Byte
    bSelector: Byte
    bMatchingType: Byte
    bCertificateAssociationDataLength: UInt16
    bPad: Byte * 3
    bCertificateAssociationData: Byte * 1
class DNS_TSIG_DATAA(EasyCastStructure):
    pNameAlgorithm: Windows.Win32.Foundation.PSTR
    pAlgorithmPacket: POINTER(Byte)
    pSignature: POINTER(Byte)
    pOtherData: POINTER(Byte)
    i64CreateTime: Int64
    wFudgeTime: UInt16
    wOriginalXid: UInt16
    wError: UInt16
    wSigLength: UInt16
    wOtherLength: UInt16
    cAlgNameLength: Byte
    bPacketPointers: Windows.Win32.Foundation.BOOL
class DNS_TSIG_DATAW(EasyCastStructure):
    pNameAlgorithm: Windows.Win32.Foundation.PWSTR
    pAlgorithmPacket: POINTER(Byte)
    pSignature: POINTER(Byte)
    pOtherData: POINTER(Byte)
    i64CreateTime: Int64
    wFudgeTime: UInt16
    wOriginalXid: UInt16
    wError: UInt16
    wSigLength: UInt16
    wOtherLength: UInt16
    cAlgNameLength: Byte
    bPacketPointers: Windows.Win32.Foundation.BOOL
class DNS_TXT_DATAA(EasyCastStructure):
    dwStringCount: UInt32
    pStringArray: Windows.Win32.Foundation.PSTR * 1
class DNS_TXT_DATAW(EasyCastStructure):
    dwStringCount: UInt32
    pStringArray: Windows.Win32.Foundation.PWSTR * 1
DNS_TYPE = UInt16
DNS_TYPE_ZERO: DNS_TYPE = 0
DNS_TYPE_A: DNS_TYPE = 1
DNS_TYPE_NS: DNS_TYPE = 2
DNS_TYPE_MD: DNS_TYPE = 3
DNS_TYPE_MF: DNS_TYPE = 4
DNS_TYPE_CNAME: DNS_TYPE = 5
DNS_TYPE_SOA: DNS_TYPE = 6
DNS_TYPE_MB: DNS_TYPE = 7
DNS_TYPE_MG: DNS_TYPE = 8
DNS_TYPE_MR: DNS_TYPE = 9
DNS_TYPE_NULL: DNS_TYPE = 10
DNS_TYPE_WKS: DNS_TYPE = 11
DNS_TYPE_PTR: DNS_TYPE = 12
DNS_TYPE_HINFO: DNS_TYPE = 13
DNS_TYPE_MINFO: DNS_TYPE = 14
DNS_TYPE_MX: DNS_TYPE = 15
DNS_TYPE_TEXT: DNS_TYPE = 16
DNS_TYPE_RP: DNS_TYPE = 17
DNS_TYPE_AFSDB: DNS_TYPE = 18
DNS_TYPE_X25: DNS_TYPE = 19
DNS_TYPE_ISDN: DNS_TYPE = 20
DNS_TYPE_RT: DNS_TYPE = 21
DNS_TYPE_NSAP: DNS_TYPE = 22
DNS_TYPE_NSAPPTR: DNS_TYPE = 23
DNS_TYPE_SIG: DNS_TYPE = 24
DNS_TYPE_KEY: DNS_TYPE = 25
DNS_TYPE_PX: DNS_TYPE = 26
DNS_TYPE_GPOS: DNS_TYPE = 27
DNS_TYPE_AAAA: DNS_TYPE = 28
DNS_TYPE_LOC: DNS_TYPE = 29
DNS_TYPE_NXT: DNS_TYPE = 30
DNS_TYPE_EID: DNS_TYPE = 31
DNS_TYPE_NIMLOC: DNS_TYPE = 32
DNS_TYPE_SRV: DNS_TYPE = 33
DNS_TYPE_ATMA: DNS_TYPE = 34
DNS_TYPE_NAPTR: DNS_TYPE = 35
DNS_TYPE_KX: DNS_TYPE = 36
DNS_TYPE_CERT: DNS_TYPE = 37
DNS_TYPE_A6: DNS_TYPE = 38
DNS_TYPE_DNAME: DNS_TYPE = 39
DNS_TYPE_SINK: DNS_TYPE = 40
DNS_TYPE_OPT: DNS_TYPE = 41
DNS_TYPE_DS: DNS_TYPE = 43
DNS_TYPE_RRSIG: DNS_TYPE = 46
DNS_TYPE_NSEC: DNS_TYPE = 47
DNS_TYPE_DNSKEY: DNS_TYPE = 48
DNS_TYPE_DHCID: DNS_TYPE = 49
DNS_TYPE_NSEC3: DNS_TYPE = 50
DNS_TYPE_NSEC3PARAM: DNS_TYPE = 51
DNS_TYPE_TLSA: DNS_TYPE = 52
DNS_TYPE_SVCB: DNS_TYPE = 64
DNS_TYPE_HTTPS: DNS_TYPE = 65
DNS_TYPE_UINFO: DNS_TYPE = 100
DNS_TYPE_UID: DNS_TYPE = 101
DNS_TYPE_GID: DNS_TYPE = 102
DNS_TYPE_UNSPEC: DNS_TYPE = 103
DNS_TYPE_ADDRS: DNS_TYPE = 248
DNS_TYPE_TKEY: DNS_TYPE = 249
DNS_TYPE_TSIG: DNS_TYPE = 250
DNS_TYPE_IXFR: DNS_TYPE = 251
DNS_TYPE_AXFR: DNS_TYPE = 252
DNS_TYPE_MAILB: DNS_TYPE = 253
DNS_TYPE_MAILA: DNS_TYPE = 254
DNS_TYPE_ALL: DNS_TYPE = 255
DNS_TYPE_ANY: DNS_TYPE = 255
DNS_TYPE_WINS: DNS_TYPE = 65281
DNS_TYPE_WINSR: DNS_TYPE = 65282
DNS_TYPE_NBSTAT: DNS_TYPE = 65282
class DNS_UNKNOWN_DATA(EasyCastStructure):
    dwByteCount: UInt32
    bData: Byte * 1
class DNS_WINSR_DATAA(EasyCastStructure):
    dwMappingFlag: UInt32
    dwLookupTimeout: UInt32
    dwCacheTimeout: UInt32
    pNameResultDomain: Windows.Win32.Foundation.PSTR
class DNS_WINSR_DATAW(EasyCastStructure):
    dwMappingFlag: UInt32
    dwLookupTimeout: UInt32
    dwCacheTimeout: UInt32
    pNameResultDomain: Windows.Win32.Foundation.PWSTR
class DNS_WINS_DATA(EasyCastStructure):
    dwMappingFlag: UInt32
    dwLookupTimeout: UInt32
    dwCacheTimeout: UInt32
    cWinsServerCount: UInt32
    WinsServers: UInt32 * 1
class DNS_WIRE_QUESTION(EasyCastStructure):
    QuestionType: UInt16
    QuestionClass: UInt16
    _pack_ = 1
class DNS_WIRE_RECORD(EasyCastStructure):
    RecordType: UInt16
    RecordClass: UInt16
    TimeToLive: UInt32
    DataLength: UInt16
    _pack_ = 1
class DNS_WKS_DATA(EasyCastStructure):
    IpAddress: UInt32
    chProtocol: Byte
    BitMask: Byte * 1
class IP4_ARRAY(EasyCastStructure):
    AddrCount: UInt32
    AddrArray: UInt32 * 1
if ARCH in 'X64,ARM64':
    class IP6_ADDRESS(EasyCastUnion):
        IP6Qword: UInt64 * 2
        IP6Dword: UInt32 * 4
        IP6Word: UInt16 * 8
        IP6Byte: Byte * 16
if ARCH in 'X86':
    class IP6_ADDRESS(EasyCastUnion):
        IP6Dword: UInt32 * 4
        IP6Word: UInt16 * 8
        IP6Byte: Byte * 16
class MDNS_QUERY_HANDLE(EasyCastStructure):
    nameBuf: Char * 256
    wType: UInt16
    pSubscription: VoidPtr
    pWnfCallbackParams: VoidPtr
    stateNameData: UInt32 * 2
class MDNS_QUERY_REQUEST(EasyCastStructure):
    Version: UInt32
    ulRefCount: UInt32
    Query: Windows.Win32.Foundation.PWSTR
    QueryType: UInt16
    QueryOptions: UInt64
    InterfaceIndex: UInt32
    pQueryCallback: Windows.Win32.NetworkManagement.Dns.PMDNS_QUERY_CALLBACK
    pQueryContext: VoidPtr
    fAnswerReceived: Windows.Win32.Foundation.BOOL
    ulResendCount: UInt32
@winfunctype_pointer
def PDNS_QUERY_COMPLETION_ROUTINE(pQueryContext: VoidPtr, pQueryResults: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_QUERY_RESULT_head)) -> Void: ...
@winfunctype_pointer
def PDNS_SERVICE_BROWSE_CALLBACK(Status: UInt32, pQueryContext: VoidPtr, pDnsRecord: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDW_head)) -> Void: ...
@winfunctype_pointer
def PDNS_SERVICE_REGISTER_COMPLETE(Status: UInt32, pQueryContext: VoidPtr, pInstance: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head)) -> Void: ...
@winfunctype_pointer
def PDNS_SERVICE_RESOLVE_COMPLETE(Status: UInt32, pQueryContext: VoidPtr, pInstance: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head)) -> Void: ...
@winfunctype_pointer
def PMDNS_QUERY_CALLBACK(pQueryContext: VoidPtr, pQueryHandle: POINTER(Windows.Win32.NetworkManagement.Dns.MDNS_QUERY_HANDLE_head), pQueryResults: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_QUERY_RESULT_head)) -> Void: ...
class _DnsRecordOptA(EasyCastStructure):
    pNext: POINTER(Windows.Win32.NetworkManagement.Dns.DNS_RECORDA_head)
    pName: Windows.Win32.Foundation.PSTR
    wType: UInt16
    wDataLength: UInt16
    Flags: _Flags_e__Union
    ExtHeader: Windows.Win32.NetworkManagement.Dns.DNS_HEADER_EXT
    wPayloadSize: UInt16
    wReserved: UInt16
    Data: _Data_e__Union
    class _Flags_e__Union(EasyCastUnion):
        DW: UInt32
        S: Windows.Win32.NetworkManagement.Dns.DNS_RECORD_FLAGS
    class _Data_e__Union(EasyCastUnion):
        OPT: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
        Opt: Windows.Win32.NetworkManagement.Dns.DNS_OPT_DATA
make_head(_module, 'DNS_AAAA_DATA')
make_head(_module, 'DNS_ADDR')
make_head(_module, 'DNS_ADDR_ARRAY')
make_head(_module, 'DNS_APPLICATION_SETTINGS')
make_head(_module, 'DNS_ATMA_DATA')
make_head(_module, 'DNS_A_DATA')
make_head(_module, 'DNS_CONNECTION_IFINDEX_ENTRY')
make_head(_module, 'DNS_CONNECTION_IFINDEX_LIST')
make_head(_module, 'DNS_CONNECTION_NAME')
make_head(_module, 'DNS_CONNECTION_NAME_LIST')
make_head(_module, 'DNS_CONNECTION_POLICY_ENTRY')
make_head(_module, 'DNS_CONNECTION_POLICY_ENTRY_LIST')
make_head(_module, 'DNS_CONNECTION_PROXY_ELEMENT')
make_head(_module, 'DNS_CONNECTION_PROXY_INFO')
make_head(_module, 'DNS_CONNECTION_PROXY_INFO_EX')
make_head(_module, 'DNS_CONNECTION_PROXY_LIST')
make_head(_module, 'DNS_CUSTOM_SERVER')
make_head(_module, 'DNS_DHCID_DATA')
make_head(_module, 'DNS_DS_DATA')
make_head(_module, 'DNS_HEADER')
make_head(_module, 'DNS_HEADER_EXT')
make_head(_module, 'DNS_KEY_DATA')
make_head(_module, 'DNS_LOC_DATA')
make_head(_module, 'DNS_MESSAGE_BUFFER')
make_head(_module, 'DNS_MINFO_DATAA')
make_head(_module, 'DNS_MINFO_DATAW')
make_head(_module, 'DNS_MX_DATAA')
make_head(_module, 'DNS_MX_DATAW')
make_head(_module, 'DNS_NAPTR_DATAA')
make_head(_module, 'DNS_NAPTR_DATAW')
make_head(_module, 'DNS_NSEC3PARAM_DATA')
make_head(_module, 'DNS_NSEC3_DATA')
make_head(_module, 'DNS_NSEC_DATAA')
make_head(_module, 'DNS_NSEC_DATAW')
make_head(_module, 'DNS_NULL_DATA')
make_head(_module, 'DNS_NXT_DATAA')
make_head(_module, 'DNS_NXT_DATAW')
make_head(_module, 'DNS_OPT_DATA')
make_head(_module, 'DNS_PROXY_COMPLETION_ROUTINE')
make_head(_module, 'DNS_PROXY_INFORMATION')
make_head(_module, 'DNS_PTR_DATAA')
make_head(_module, 'DNS_PTR_DATAW')
make_head(_module, 'DNS_QUERY_CANCEL')
make_head(_module, 'DNS_QUERY_REQUEST')
make_head(_module, 'DNS_QUERY_REQUEST3')
make_head(_module, 'DNS_QUERY_RESULT')
make_head(_module, 'DNS_RECORDA')
make_head(_module, 'DNS_RECORDW')
make_head(_module, 'DNS_RECORD_FLAGS')
make_head(_module, 'DNS_RECORD_OPTW')
make_head(_module, 'DNS_RRSET')
make_head(_module, 'DNS_SERVICE_BROWSE_REQUEST')
make_head(_module, 'DNS_SERVICE_CANCEL')
make_head(_module, 'DNS_SERVICE_INSTANCE')
make_head(_module, 'DNS_SERVICE_REGISTER_REQUEST')
make_head(_module, 'DNS_SERVICE_RESOLVE_REQUEST')
make_head(_module, 'DNS_SIG_DATAA')
make_head(_module, 'DNS_SIG_DATAW')
make_head(_module, 'DNS_SOA_DATAA')
make_head(_module, 'DNS_SOA_DATAW')
make_head(_module, 'DNS_SRV_DATAA')
make_head(_module, 'DNS_SRV_DATAW')
make_head(_module, 'DNS_SVCB_DATA')
make_head(_module, 'DNS_SVCB_PARAM')
make_head(_module, 'DNS_SVCB_PARAM_ALPN')
make_head(_module, 'DNS_SVCB_PARAM_ALPN_ID')
make_head(_module, 'DNS_SVCB_PARAM_IPV4')
make_head(_module, 'DNS_SVCB_PARAM_IPV6')
make_head(_module, 'DNS_SVCB_PARAM_MANDATORY')
make_head(_module, 'DNS_SVCB_PARAM_UNKNOWN')
make_head(_module, 'DNS_TKEY_DATAA')
make_head(_module, 'DNS_TKEY_DATAW')
make_head(_module, 'DNS_TLSA_DATA')
make_head(_module, 'DNS_TSIG_DATAA')
make_head(_module, 'DNS_TSIG_DATAW')
make_head(_module, 'DNS_TXT_DATAA')
make_head(_module, 'DNS_TXT_DATAW')
make_head(_module, 'DNS_UNKNOWN_DATA')
make_head(_module, 'DNS_WINSR_DATAA')
make_head(_module, 'DNS_WINSR_DATAW')
make_head(_module, 'DNS_WINS_DATA')
make_head(_module, 'DNS_WIRE_QUESTION')
make_head(_module, 'DNS_WIRE_RECORD')
make_head(_module, 'DNS_WKS_DATA')
make_head(_module, 'IP4_ARRAY')
if ARCH in 'X64,ARM64':
    make_head(_module, 'IP6_ADDRESS')
if ARCH in 'X86':
    make_head(_module, 'IP6_ADDRESS')
make_head(_module, 'MDNS_QUERY_HANDLE')
make_head(_module, 'MDNS_QUERY_REQUEST')
make_head(_module, 'PDNS_QUERY_COMPLETION_ROUTINE')
make_head(_module, 'PDNS_SERVICE_BROWSE_CALLBACK')
make_head(_module, 'PDNS_SERVICE_REGISTER_COMPLETE')
make_head(_module, 'PDNS_SERVICE_RESOLVE_COMPLETE')
make_head(_module, 'PMDNS_QUERY_CALLBACK')
make_head(_module, '_DnsRecordOptA')
