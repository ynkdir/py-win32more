from win32more import *
import win32more.NetworkManagement.Dns
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.NetworkManagement.Dns, name, eval(f"_define_{name}()"))
    return getattr(win32more.NetworkManagement.Dns, name)
SIZEOF_IP4_ADDRESS = 4
IP4_ADDRESS_STRING_LENGTH = 16
IP4_ADDRESS_STRING_BUFFER_LENGTH = 16
DNS_ADDR_MAX_SOCKADDR_LENGTH = 32
IP6_ADDRESS_STRING_LENGTH = 65
IP6_ADDRESS_STRING_BUFFER_LENGTH = 65
DNS_ADDRESS_STRING_LENGTH = 65
DNS_PORT_HOST_ORDER = 53
DNS_PORT_NET_ORDER = 13568
DNS_RFC_MAX_UDP_PACKET_LENGTH = 512
DNS_MAX_NAME_LENGTH = 255
DNS_MAX_LABEL_LENGTH = 63
DNS_MAX_NAME_BUFFER_LENGTH = 256
DNS_MAX_LABEL_BUFFER_LENGTH = 64
DNS_MAX_IP4_REVERSE_NAME_LENGTH = 31
DNS_MAX_IP6_REVERSE_NAME_LENGTH = 75
DNS_MAX_REVERSE_NAME_LENGTH = 75
DNS_MAX_IP4_REVERSE_NAME_BUFFER_LENGTH = 31
DNS_MAX_IP6_REVERSE_NAME_BUFFER_LENGTH = 75
DNS_MAX_REVERSE_NAME_BUFFER_LENGTH = 75
DNS_MAX_TEXT_STRING_LENGTH = 255
DNS_COMPRESSED_QUESTION_NAME = 49164
DNS_OPCODE_QUERY = 0
DNS_OPCODE_IQUERY = 1
DNS_OPCODE_SERVER_STATUS = 2
DNS_OPCODE_UNKNOWN = 3
DNS_OPCODE_NOTIFY = 4
DNS_OPCODE_UPDATE = 5
DNS_RCODE_NOERROR = 0
DNS_RCODE_FORMERR = 1
DNS_RCODE_SERVFAIL = 2
DNS_RCODE_NXDOMAIN = 3
DNS_RCODE_NOTIMPL = 4
DNS_RCODE_REFUSED = 5
DNS_RCODE_YXDOMAIN = 6
DNS_RCODE_YXRRSET = 7
DNS_RCODE_NXRRSET = 8
DNS_RCODE_NOTAUTH = 9
DNS_RCODE_NOTZONE = 10
DNS_RCODE_MAX = 15
DNS_RCODE_BADVERS = 16
DNS_RCODE_BADSIG = 16
DNS_RCODE_BADKEY = 17
DNS_RCODE_BADTIME = 18
DNS_RCODE_NO_ERROR = 0
DNS_RCODE_FORMAT_ERROR = 1
DNS_RCODE_SERVER_FAILURE = 2
DNS_RCODE_NAME_ERROR = 3
DNS_RCODE_NOT_IMPLEMENTED = 4
DNS_CLASS_INTERNET = 1
DNS_CLASS_CSNET = 2
DNS_CLASS_CHAOS = 3
DNS_CLASS_HESIOD = 4
DNS_CLASS_NONE = 254
DNS_CLASS_ALL = 255
DNS_CLASS_ANY = 255
DNS_CLASS_UNICAST_RESPONSE = 32768
DNS_RCLASS_INTERNET = 256
DNS_RCLASS_CSNET = 512
DNS_RCLASS_CHAOS = 768
DNS_RCLASS_HESIOD = 1024
DNS_RCLASS_NONE = 65024
DNS_RCLASS_ALL = 65280
DNS_RCLASS_ANY = 65280
DNS_RCLASS_UNICAST_RESPONSE = 128
DNS_TYPE_ZERO = 0
DNS_TYPE_A = 1
DNS_TYPE_NS = 2
DNS_TYPE_MD = 3
DNS_TYPE_MF = 4
DNS_TYPE_CNAME = 5
DNS_TYPE_SOA = 6
DNS_TYPE_MB = 7
DNS_TYPE_MG = 8
DNS_TYPE_MR = 9
DNS_TYPE_NULL = 10
DNS_TYPE_WKS = 11
DNS_TYPE_PTR = 12
DNS_TYPE_HINFO = 13
DNS_TYPE_MINFO = 14
DNS_TYPE_MX = 15
DNS_TYPE_TEXT = 16
DNS_TYPE_RP = 17
DNS_TYPE_AFSDB = 18
DNS_TYPE_X25 = 19
DNS_TYPE_ISDN = 20
DNS_TYPE_RT = 21
DNS_TYPE_NSAP = 22
DNS_TYPE_NSAPPTR = 23
DNS_TYPE_SIG = 24
DNS_TYPE_KEY = 25
DNS_TYPE_PX = 26
DNS_TYPE_GPOS = 27
DNS_TYPE_AAAA = 28
DNS_TYPE_LOC = 29
DNS_TYPE_NXT = 30
DNS_TYPE_EID = 31
DNS_TYPE_NIMLOC = 32
DNS_TYPE_SRV = 33
DNS_TYPE_ATMA = 34
DNS_TYPE_NAPTR = 35
DNS_TYPE_KX = 36
DNS_TYPE_CERT = 37
DNS_TYPE_A6 = 38
DNS_TYPE_DNAME = 39
DNS_TYPE_SINK = 40
DNS_TYPE_OPT = 41
DNS_TYPE_DS = 43
DNS_TYPE_RRSIG = 46
DNS_TYPE_NSEC = 47
DNS_TYPE_DNSKEY = 48
DNS_TYPE_DHCID = 49
DNS_TYPE_NSEC3 = 50
DNS_TYPE_NSEC3PARAM = 51
DNS_TYPE_TLSA = 52
DNS_TYPE_UINFO = 100
DNS_TYPE_UID = 101
DNS_TYPE_GID = 102
DNS_TYPE_UNSPEC = 103
DNS_TYPE_ADDRS = 248
DNS_TYPE_TKEY = 249
DNS_TYPE_TSIG = 250
DNS_TYPE_IXFR = 251
DNS_TYPE_AXFR = 252
DNS_TYPE_MAILB = 253
DNS_TYPE_MAILA = 254
DNS_TYPE_ALL = 255
DNS_TYPE_ANY = 255
DNS_TYPE_WINS = 65281
DNS_TYPE_WINSR = 65282
DNS_TYPE_NBSTAT = 65282
DNS_RTYPE_A = 256
DNS_RTYPE_NS = 512
DNS_RTYPE_MD = 768
DNS_RTYPE_MF = 1024
DNS_RTYPE_CNAME = 1280
DNS_RTYPE_SOA = 1536
DNS_RTYPE_MB = 1792
DNS_RTYPE_MG = 2048
DNS_RTYPE_MR = 2304
DNS_RTYPE_NULL = 2560
DNS_RTYPE_WKS = 2816
DNS_RTYPE_PTR = 3072
DNS_RTYPE_HINFO = 3328
DNS_RTYPE_MINFO = 3584
DNS_RTYPE_MX = 3840
DNS_RTYPE_TEXT = 4096
DNS_RTYPE_RP = 4352
DNS_RTYPE_AFSDB = 4608
DNS_RTYPE_X25 = 4864
DNS_RTYPE_ISDN = 5120
DNS_RTYPE_RT = 5376
DNS_RTYPE_NSAP = 5632
DNS_RTYPE_NSAPPTR = 5888
DNS_RTYPE_SIG = 6144
DNS_RTYPE_KEY = 6400
DNS_RTYPE_PX = 6656
DNS_RTYPE_GPOS = 6912
DNS_RTYPE_AAAA = 7168
DNS_RTYPE_LOC = 7424
DNS_RTYPE_NXT = 7680
DNS_RTYPE_EID = 7936
DNS_RTYPE_NIMLOC = 8192
DNS_RTYPE_SRV = 8448
DNS_RTYPE_ATMA = 8704
DNS_RTYPE_NAPTR = 8960
DNS_RTYPE_KX = 9216
DNS_RTYPE_CERT = 9472
DNS_RTYPE_A6 = 9728
DNS_RTYPE_DNAME = 9984
DNS_RTYPE_SINK = 10240
DNS_RTYPE_OPT = 10496
DNS_RTYPE_DS = 11008
DNS_RTYPE_RRSIG = 11776
DNS_RTYPE_NSEC = 12032
DNS_RTYPE_DNSKEY = 12288
DNS_RTYPE_DHCID = 12544
DNS_RTYPE_NSEC3 = 12800
DNS_RTYPE_NSEC3PARAM = 13056
DNS_RTYPE_TLSA = 13312
DNS_RTYPE_UINFO = 25600
DNS_RTYPE_UID = 25856
DNS_RTYPE_GID = 26112
DNS_RTYPE_UNSPEC = 26368
DNS_RTYPE_TKEY = 63744
DNS_RTYPE_TSIG = 64000
DNS_RTYPE_IXFR = 64256
DNS_RTYPE_AXFR = 64512
DNS_RTYPE_MAILB = 64768
DNS_RTYPE_MAILA = 65024
DNS_RTYPE_ALL = 65280
DNS_RTYPE_ANY = 65280
DNS_RTYPE_WINS = 511
DNS_RTYPE_WINSR = 767
DNS_ATMA_FORMAT_E164 = 1
DNS_ATMA_FORMAT_AESA = 2
DNS_ATMA_MAX_ADDR_LENGTH = 20
DNS_ATMA_AESA_ADDR_LENGTH = 20
DNS_ATMA_MAX_RECORD_LENGTH = 21
DNSSEC_ALGORITHM_RSAMD5 = 1
DNSSEC_ALGORITHM_RSASHA1 = 5
DNSSEC_ALGORITHM_RSASHA1_NSEC3 = 7
DNSSEC_ALGORITHM_RSASHA256 = 8
DNSSEC_ALGORITHM_RSASHA512 = 10
DNSSEC_ALGORITHM_ECDSAP256_SHA256 = 13
DNSSEC_ALGORITHM_ECDSAP384_SHA384 = 14
DNSSEC_ALGORITHM_NULL = 253
DNSSEC_ALGORITHM_PRIVATE = 254
DNSSEC_DIGEST_ALGORITHM_SHA1 = 1
DNSSEC_DIGEST_ALGORITHM_SHA256 = 2
DNSSEC_DIGEST_ALGORITHM_SHA384 = 4
DNSSEC_PROTOCOL_NONE = 0
DNSSEC_PROTOCOL_TLS = 1
DNSSEC_PROTOCOL_EMAIL = 2
DNSSEC_PROTOCOL_DNSSEC = 3
DNSSEC_PROTOCOL_IPSEC = 4
DNSSEC_KEY_FLAG_NOAUTH = 1
DNSSEC_KEY_FLAG_NOCONF = 2
DNSSEC_KEY_FLAG_FLAG2 = 4
DNSSEC_KEY_FLAG_EXTEND = 8
DNSSEC_KEY_FLAG_FLAG4 = 16
DNSSEC_KEY_FLAG_FLAG5 = 32
DNSSEC_KEY_FLAG_USER = 0
DNSSEC_KEY_FLAG_ZONE = 64
DNSSEC_KEY_FLAG_HOST = 128
DNSSEC_KEY_FLAG_NTPE3 = 192
DNSSEC_KEY_FLAG_FLAG8 = 256
DNSSEC_KEY_FLAG_FLAG9 = 512
DNSSEC_KEY_FLAG_FLAG10 = 1024
DNSSEC_KEY_FLAG_FLAG11 = 2048
DNSSEC_KEY_FLAG_SIG0 = 0
DNSSEC_KEY_FLAG_SIG1 = 4096
DNSSEC_KEY_FLAG_SIG2 = 8192
DNSSEC_KEY_FLAG_SIG3 = 12288
DNSSEC_KEY_FLAG_SIG4 = 16384
DNSSEC_KEY_FLAG_SIG5 = 20480
DNSSEC_KEY_FLAG_SIG6 = 24576
DNSSEC_KEY_FLAG_SIG7 = 28672
DNSSEC_KEY_FLAG_SIG8 = 32768
DNSSEC_KEY_FLAG_SIG9 = 36864
DNSSEC_KEY_FLAG_SIG10 = 40960
DNSSEC_KEY_FLAG_SIG11 = 45056
DNSSEC_KEY_FLAG_SIG12 = 49152
DNSSEC_KEY_FLAG_SIG13 = 53248
DNSSEC_KEY_FLAG_SIG14 = 57344
DNSSEC_KEY_FLAG_SIG15 = 61440
DNS_TKEY_MODE_SERVER_ASSIGN = 1
DNS_TKEY_MODE_DIFFIE_HELLMAN = 2
DNS_TKEY_MODE_GSS = 3
DNS_TKEY_MODE_RESOLVER_ASSIGN = 4
DNS_WINS_FLAG_SCOPE = 2147483648
DNS_WINS_FLAG_LOCAL = 65536
DNS_CONFIG_FLAG_ALLOC = 1
DNSREC_SECTION = 3
DNSREC_QUESTION = 0
DNSREC_ANSWER = 1
DNSREC_AUTHORITY = 2
DNSREC_ADDITIONAL = 3
DNSREC_ZONE = 0
DNSREC_PREREQ = 1
DNSREC_UPDATE = 2
DNSREC_DELETE = 4
DNSREC_NOEXIST = 4
DNS_QUERY_STANDARD = 0
DNS_QUERY_ACCEPT_TRUNCATED_RESPONSE = 1
DNS_QUERY_USE_TCP_ONLY = 2
DNS_QUERY_NO_RECURSION = 4
DNS_QUERY_BYPASS_CACHE = 8
DNS_QUERY_NO_WIRE_QUERY = 16
DNS_QUERY_NO_LOCAL_NAME = 32
DNS_QUERY_NO_HOSTS_FILE = 64
DNS_QUERY_NO_NETBT = 128
DNS_QUERY_WIRE_ONLY = 256
DNS_QUERY_RETURN_MESSAGE = 512
DNS_QUERY_MULTICAST_ONLY = 1024
DNS_QUERY_NO_MULTICAST = 2048
DNS_QUERY_TREAT_AS_FQDN = 4096
DNS_QUERY_ADDRCONFIG = 8192
DNS_QUERY_DUAL_ADDR = 16384
DNS_QUERY_DONT_RESET_TTL_VALUES = 1048576
DNS_QUERY_DISABLE_IDN_ENCODING = 2097152
DNS_QUERY_APPEND_MULTILABEL = 8388608
DNS_QUERY_DNSSEC_OK = 16777216
DNS_QUERY_DNSSEC_CHECKING_DISABLED = 33554432
DNS_QUERY_RESERVED = 4026531840
DNS_QUERY_CACHE_ONLY = 16
DNS_QUERY_REQUEST_VERSION1 = 1
DNS_QUERY_REQUEST_VERSION2 = 2
DNS_QUERY_RESULTS_VERSION1 = 1
DNS_QUERY_REQUEST_VERSION3 = 3
DNS_CUSTOM_SERVER_TYPE_UDP = 1
DNS_CUSTOM_SERVER_TYPE_DOH = 2
DNS_CUSTOM_SERVER_UDP_FALLBACK = 1
DNS_APP_SETTINGS_VERSION1 = 1
DNS_APP_SETTINGS_EXCLUSIVE_SERVERS = 1
DNS_UPDATE_SECURITY_USE_DEFAULT = 0
DNS_UPDATE_SECURITY_OFF = 16
DNS_UPDATE_SECURITY_ON = 32
DNS_UPDATE_SECURITY_ONLY = 256
DNS_UPDATE_CACHE_SECURITY_CONTEXT = 512
DNS_UPDATE_TEST_USE_LOCAL_SYS_ACCT = 1024
DNS_UPDATE_FORCE_SECURITY_NEGO = 2048
DNS_UPDATE_TRY_ALL_MASTER_SERVERS = 4096
DNS_UPDATE_SKIP_NO_UPDATE_ADAPTERS = 8192
DNS_UPDATE_REMOTE_SERVER = 16384
DNS_UPDATE_RESERVED = 4294901760
DNS_VALSVR_ERROR_INVALID_ADDR = 1
DNS_VALSVR_ERROR_INVALID_NAME = 2
DNS_VALSVR_ERROR_UNREACHABLE = 3
DNS_VALSVR_ERROR_NO_RESPONSE = 4
DNS_VALSVR_ERROR_NO_AUTH = 5
DNS_VALSVR_ERROR_REFUSED = 6
DNS_VALSVR_ERROR_NO_TCP = 16
DNS_VALSVR_ERROR_UNKNOWN = 255
DNS_CONNECTION_NAME_MAX_LENGTH = 64
DNS_CONNECTION_PROXY_INFO_CURRENT_VERSION = 1
DNS_CONNECTION_PROXY_INFO_SERVER_MAX_LENGTH = 256
DNS_CONNECTION_PROXY_INFO_FRIENDLY_NAME_MAX_LENGTH = 64
DNS_CONNECTION_PROXY_INFO_USERNAME_MAX_LENGTH = 128
DNS_CONNECTION_PROXY_INFO_PASSWORD_MAX_LENGTH = 128
DNS_CONNECTION_PROXY_INFO_EXCEPTION_MAX_LENGTH = 1024
DNS_CONNECTION_PROXY_INFO_EXTRA_INFO_MAX_LENGTH = 1024
DNS_CONNECTION_PROXY_INFO_FLAG_DISABLED = 1
DNS_CONNECTION_PROXY_INFO_FLAG_BYPASSLOCAL = 2
DNS_CONNECTION_POLICY_ENTRY_ONDEMAND = 1
DnsContextHandle = IntPtr
def _define_IP4_ARRAY_head():
    class IP4_ARRAY(Structure):
        pass
    return IP4_ARRAY
def _define_IP4_ARRAY():
    IP4_ARRAY = win32more.NetworkManagement.Dns.IP4_ARRAY_head
    IP4_ARRAY._fields_ = [
        ("AddrCount", UInt32),
        ("AddrArray", UInt32 * 0),
    ]
    return IP4_ARRAY
def _define_IP6_ADDRESS_head():
    class IP6_ADDRESS(Union):
        pass
    return IP6_ADDRESS
def _define_IP6_ADDRESS():
    IP6_ADDRESS = win32more.NetworkManagement.Dns.IP6_ADDRESS_head
    IP6_ADDRESS._fields_ = [
        ("IP6Qword", UInt64 * 2),
        ("IP6Dword", UInt32 * 4),
        ("IP6Word", UInt16 * 8),
        ("IP6Byte", Byte * 16),
    ]
    return IP6_ADDRESS
def _define_DNS_ADDR_head():
    class DNS_ADDR(Structure):
        pass
    return DNS_ADDR
def _define_DNS_ADDR():
    DNS_ADDR = win32more.NetworkManagement.Dns.DNS_ADDR_head
    class DNS_ADDR__Data_e__Union(Union):
        pass
    DNS_ADDR__Data_e__Union._pack_ = 1
    DNS_ADDR__Data_e__Union._fields_ = [
        ("DnsAddrUserDword", UInt32 * 8),
    ]
    DNS_ADDR._fields_ = [
        ("MaxSa", win32more.Foundation.CHAR * 32),
        ("Data", DNS_ADDR__Data_e__Union),
    ]
    return DNS_ADDR
def _define_DNS_ADDR_ARRAY_head():
    class DNS_ADDR_ARRAY(Structure):
        pass
    return DNS_ADDR_ARRAY
def _define_DNS_ADDR_ARRAY():
    DNS_ADDR_ARRAY = win32more.NetworkManagement.Dns.DNS_ADDR_ARRAY_head
    DNS_ADDR_ARRAY._pack_ = 1
    DNS_ADDR_ARRAY._fields_ = [
        ("MaxCount", UInt32),
        ("AddrCount", UInt32),
        ("Tag", UInt32),
        ("Family", UInt16),
        ("WordReserved", UInt16),
        ("Flags", UInt32),
        ("MatchFlag", UInt32),
        ("Reserved1", UInt32),
        ("Reserved2", UInt32),
        ("AddrArray", win32more.NetworkManagement.Dns.DNS_ADDR * 0),
    ]
    return DNS_ADDR_ARRAY
def _define_DNS_HEADER_head():
    class DNS_HEADER(Structure):
        pass
    return DNS_HEADER
def _define_DNS_HEADER():
    DNS_HEADER = win32more.NetworkManagement.Dns.DNS_HEADER_head
    DNS_HEADER._pack_ = 1
    DNS_HEADER._fields_ = [
        ("Xid", UInt16),
        ("_bitfield1", Byte),
        ("_bitfield2", Byte),
        ("QuestionCount", UInt16),
        ("AnswerCount", UInt16),
        ("NameServerCount", UInt16),
        ("AdditionalCount", UInt16),
    ]
    return DNS_HEADER
def _define_DNS_HEADER_EXT_head():
    class DNS_HEADER_EXT(Structure):
        pass
    return DNS_HEADER_EXT
def _define_DNS_HEADER_EXT():
    DNS_HEADER_EXT = win32more.NetworkManagement.Dns.DNS_HEADER_EXT_head
    DNS_HEADER_EXT._pack_ = 1
    DNS_HEADER_EXT._fields_ = [
        ("_bitfield", UInt16),
        ("chRcode", Byte),
        ("chVersion", Byte),
    ]
    return DNS_HEADER_EXT
def _define_DNS_WIRE_QUESTION_head():
    class DNS_WIRE_QUESTION(Structure):
        pass
    return DNS_WIRE_QUESTION
def _define_DNS_WIRE_QUESTION():
    DNS_WIRE_QUESTION = win32more.NetworkManagement.Dns.DNS_WIRE_QUESTION_head
    DNS_WIRE_QUESTION._pack_ = 1
    DNS_WIRE_QUESTION._fields_ = [
        ("QuestionType", UInt16),
        ("QuestionClass", UInt16),
    ]
    return DNS_WIRE_QUESTION
def _define_DNS_WIRE_RECORD_head():
    class DNS_WIRE_RECORD(Structure):
        pass
    return DNS_WIRE_RECORD
def _define_DNS_WIRE_RECORD():
    DNS_WIRE_RECORD = win32more.NetworkManagement.Dns.DNS_WIRE_RECORD_head
    DNS_WIRE_RECORD._pack_ = 1
    DNS_WIRE_RECORD._fields_ = [
        ("RecordType", UInt16),
        ("RecordClass", UInt16),
        ("TimeToLive", UInt32),
        ("DataLength", UInt16),
    ]
    return DNS_WIRE_RECORD
DNS_CONFIG_TYPE = Int32
DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_W = 0
DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_A = 1
DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_UTF8 = 2
DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_W = 3
DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_A = 4
DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_UTF8 = 5
DNS_CONFIG_TYPE_DnsConfigDnsServerList = 6
DNS_CONFIG_TYPE_DnsConfigSearchList = 7
DNS_CONFIG_TYPE_DnsConfigAdapterInfo = 8
DNS_CONFIG_TYPE_DnsConfigPrimaryHostNameRegistrationEnabled = 9
DNS_CONFIG_TYPE_DnsConfigAdapterHostNameRegistrationEnabled = 10
DNS_CONFIG_TYPE_DnsConfigAddressRegistrationMaxCount = 11
DNS_CONFIG_TYPE_DnsConfigHostName_W = 12
DNS_CONFIG_TYPE_DnsConfigHostName_A = 13
DNS_CONFIG_TYPE_DnsConfigHostName_UTF8 = 14
DNS_CONFIG_TYPE_DnsConfigFullHostName_W = 15
DNS_CONFIG_TYPE_DnsConfigFullHostName_A = 16
DNS_CONFIG_TYPE_DnsConfigFullHostName_UTF8 = 17
DNS_CONFIG_TYPE_DnsConfigNameServer = 18
def _define_DNS_A_DATA_head():
    class DNS_A_DATA(Structure):
        pass
    return DNS_A_DATA
def _define_DNS_A_DATA():
    DNS_A_DATA = win32more.NetworkManagement.Dns.DNS_A_DATA_head
    DNS_A_DATA._fields_ = [
        ("IpAddress", UInt32),
    ]
    return DNS_A_DATA
def _define_DNS_PTR_DATAW_head():
    class DNS_PTR_DATAW(Structure):
        pass
    return DNS_PTR_DATAW
def _define_DNS_PTR_DATAW():
    DNS_PTR_DATAW = win32more.NetworkManagement.Dns.DNS_PTR_DATAW_head
    DNS_PTR_DATAW._fields_ = [
        ("pNameHost", win32more.Foundation.PWSTR),
    ]
    return DNS_PTR_DATAW
def _define_DNS_PTR_DATAA_head():
    class DNS_PTR_DATAA(Structure):
        pass
    return DNS_PTR_DATAA
def _define_DNS_PTR_DATAA():
    DNS_PTR_DATAA = win32more.NetworkManagement.Dns.DNS_PTR_DATAA_head
    DNS_PTR_DATAA._fields_ = [
        ("pNameHost", win32more.Foundation.PSTR),
    ]
    return DNS_PTR_DATAA
def _define_DNS_SOA_DATAW_head():
    class DNS_SOA_DATAW(Structure):
        pass
    return DNS_SOA_DATAW
def _define_DNS_SOA_DATAW():
    DNS_SOA_DATAW = win32more.NetworkManagement.Dns.DNS_SOA_DATAW_head
    DNS_SOA_DATAW._fields_ = [
        ("pNamePrimaryServer", win32more.Foundation.PWSTR),
        ("pNameAdministrator", win32more.Foundation.PWSTR),
        ("dwSerialNo", UInt32),
        ("dwRefresh", UInt32),
        ("dwRetry", UInt32),
        ("dwExpire", UInt32),
        ("dwDefaultTtl", UInt32),
    ]
    return DNS_SOA_DATAW
def _define_DNS_SOA_DATAA_head():
    class DNS_SOA_DATAA(Structure):
        pass
    return DNS_SOA_DATAA
def _define_DNS_SOA_DATAA():
    DNS_SOA_DATAA = win32more.NetworkManagement.Dns.DNS_SOA_DATAA_head
    DNS_SOA_DATAA._fields_ = [
        ("pNamePrimaryServer", win32more.Foundation.PSTR),
        ("pNameAdministrator", win32more.Foundation.PSTR),
        ("dwSerialNo", UInt32),
        ("dwRefresh", UInt32),
        ("dwRetry", UInt32),
        ("dwExpire", UInt32),
        ("dwDefaultTtl", UInt32),
    ]
    return DNS_SOA_DATAA
def _define_DNS_MINFO_DATAW_head():
    class DNS_MINFO_DATAW(Structure):
        pass
    return DNS_MINFO_DATAW
def _define_DNS_MINFO_DATAW():
    DNS_MINFO_DATAW = win32more.NetworkManagement.Dns.DNS_MINFO_DATAW_head
    DNS_MINFO_DATAW._fields_ = [
        ("pNameMailbox", win32more.Foundation.PWSTR),
        ("pNameErrorsMailbox", win32more.Foundation.PWSTR),
    ]
    return DNS_MINFO_DATAW
def _define_DNS_MINFO_DATAA_head():
    class DNS_MINFO_DATAA(Structure):
        pass
    return DNS_MINFO_DATAA
def _define_DNS_MINFO_DATAA():
    DNS_MINFO_DATAA = win32more.NetworkManagement.Dns.DNS_MINFO_DATAA_head
    DNS_MINFO_DATAA._fields_ = [
        ("pNameMailbox", win32more.Foundation.PSTR),
        ("pNameErrorsMailbox", win32more.Foundation.PSTR),
    ]
    return DNS_MINFO_DATAA
def _define_DNS_MX_DATAW_head():
    class DNS_MX_DATAW(Structure):
        pass
    return DNS_MX_DATAW
def _define_DNS_MX_DATAW():
    DNS_MX_DATAW = win32more.NetworkManagement.Dns.DNS_MX_DATAW_head
    DNS_MX_DATAW._fields_ = [
        ("pNameExchange", win32more.Foundation.PWSTR),
        ("wPreference", UInt16),
        ("Pad", UInt16),
    ]
    return DNS_MX_DATAW
def _define_DNS_MX_DATAA_head():
    class DNS_MX_DATAA(Structure):
        pass
    return DNS_MX_DATAA
def _define_DNS_MX_DATAA():
    DNS_MX_DATAA = win32more.NetworkManagement.Dns.DNS_MX_DATAA_head
    DNS_MX_DATAA._fields_ = [
        ("pNameExchange", win32more.Foundation.PSTR),
        ("wPreference", UInt16),
        ("Pad", UInt16),
    ]
    return DNS_MX_DATAA
def _define_DNS_TXT_DATAW_head():
    class DNS_TXT_DATAW(Structure):
        pass
    return DNS_TXT_DATAW
def _define_DNS_TXT_DATAW():
    DNS_TXT_DATAW = win32more.NetworkManagement.Dns.DNS_TXT_DATAW_head
    DNS_TXT_DATAW._fields_ = [
        ("dwStringCount", UInt32),
        ("pStringArray", win32more.Foundation.PWSTR * 0),
    ]
    return DNS_TXT_DATAW
def _define_DNS_TXT_DATAA_head():
    class DNS_TXT_DATAA(Structure):
        pass
    return DNS_TXT_DATAA
def _define_DNS_TXT_DATAA():
    DNS_TXT_DATAA = win32more.NetworkManagement.Dns.DNS_TXT_DATAA_head
    DNS_TXT_DATAA._fields_ = [
        ("dwStringCount", UInt32),
        ("pStringArray", win32more.Foundation.PSTR * 0),
    ]
    return DNS_TXT_DATAA
def _define_DNS_NULL_DATA_head():
    class DNS_NULL_DATA(Structure):
        pass
    return DNS_NULL_DATA
def _define_DNS_NULL_DATA():
    DNS_NULL_DATA = win32more.NetworkManagement.Dns.DNS_NULL_DATA_head
    DNS_NULL_DATA._fields_ = [
        ("dwByteCount", UInt32),
        ("Data", Byte * 0),
    ]
    return DNS_NULL_DATA
def _define_DNS_WKS_DATA_head():
    class DNS_WKS_DATA(Structure):
        pass
    return DNS_WKS_DATA
def _define_DNS_WKS_DATA():
    DNS_WKS_DATA = win32more.NetworkManagement.Dns.DNS_WKS_DATA_head
    DNS_WKS_DATA._fields_ = [
        ("IpAddress", UInt32),
        ("chProtocol", Byte),
        ("BitMask", Byte * 0),
    ]
    return DNS_WKS_DATA
def _define_DNS_AAAA_DATA_head():
    class DNS_AAAA_DATA(Structure):
        pass
    return DNS_AAAA_DATA
def _define_DNS_AAAA_DATA():
    DNS_AAAA_DATA = win32more.NetworkManagement.Dns.DNS_AAAA_DATA_head
    DNS_AAAA_DATA._fields_ = [
        ("Ip6Address", win32more.NetworkManagement.Dns.IP6_ADDRESS),
    ]
    return DNS_AAAA_DATA
def _define_DNS_SIG_DATAW_head():
    class DNS_SIG_DATAW(Structure):
        pass
    return DNS_SIG_DATAW
def _define_DNS_SIG_DATAW():
    DNS_SIG_DATAW = win32more.NetworkManagement.Dns.DNS_SIG_DATAW_head
    DNS_SIG_DATAW._fields_ = [
        ("wTypeCovered", UInt16),
        ("chAlgorithm", Byte),
        ("chLabelCount", Byte),
        ("dwOriginalTtl", UInt32),
        ("dwExpiration", UInt32),
        ("dwTimeSigned", UInt32),
        ("wKeyTag", UInt16),
        ("wSignatureLength", UInt16),
        ("pNameSigner", win32more.Foundation.PWSTR),
        ("Signature", Byte * 0),
    ]
    return DNS_SIG_DATAW
def _define_DNS_SIG_DATAA_head():
    class DNS_SIG_DATAA(Structure):
        pass
    return DNS_SIG_DATAA
def _define_DNS_SIG_DATAA():
    DNS_SIG_DATAA = win32more.NetworkManagement.Dns.DNS_SIG_DATAA_head
    DNS_SIG_DATAA._fields_ = [
        ("wTypeCovered", UInt16),
        ("chAlgorithm", Byte),
        ("chLabelCount", Byte),
        ("dwOriginalTtl", UInt32),
        ("dwExpiration", UInt32),
        ("dwTimeSigned", UInt32),
        ("wKeyTag", UInt16),
        ("wSignatureLength", UInt16),
        ("pNameSigner", win32more.Foundation.PSTR),
        ("Signature", Byte * 0),
    ]
    return DNS_SIG_DATAA
def _define_DNS_KEY_DATA_head():
    class DNS_KEY_DATA(Structure):
        pass
    return DNS_KEY_DATA
def _define_DNS_KEY_DATA():
    DNS_KEY_DATA = win32more.NetworkManagement.Dns.DNS_KEY_DATA_head
    DNS_KEY_DATA._fields_ = [
        ("wFlags", UInt16),
        ("chProtocol", Byte),
        ("chAlgorithm", Byte),
        ("wKeyLength", UInt16),
        ("wPad", UInt16),
        ("Key", Byte * 0),
    ]
    return DNS_KEY_DATA
def _define_DNS_DHCID_DATA_head():
    class DNS_DHCID_DATA(Structure):
        pass
    return DNS_DHCID_DATA
def _define_DNS_DHCID_DATA():
    DNS_DHCID_DATA = win32more.NetworkManagement.Dns.DNS_DHCID_DATA_head
    DNS_DHCID_DATA._fields_ = [
        ("dwByteCount", UInt32),
        ("DHCID", Byte * 0),
    ]
    return DNS_DHCID_DATA
def _define_DNS_NSEC_DATAW_head():
    class DNS_NSEC_DATAW(Structure):
        pass
    return DNS_NSEC_DATAW
def _define_DNS_NSEC_DATAW():
    DNS_NSEC_DATAW = win32more.NetworkManagement.Dns.DNS_NSEC_DATAW_head
    DNS_NSEC_DATAW._fields_ = [
        ("pNextDomainName", win32more.Foundation.PWSTR),
        ("wTypeBitMapsLength", UInt16),
        ("wPad", UInt16),
        ("TypeBitMaps", Byte * 0),
    ]
    return DNS_NSEC_DATAW
def _define_DNS_NSEC_DATAA_head():
    class DNS_NSEC_DATAA(Structure):
        pass
    return DNS_NSEC_DATAA
def _define_DNS_NSEC_DATAA():
    DNS_NSEC_DATAA = win32more.NetworkManagement.Dns.DNS_NSEC_DATAA_head
    DNS_NSEC_DATAA._fields_ = [
        ("pNextDomainName", win32more.Foundation.PSTR),
        ("wTypeBitMapsLength", UInt16),
        ("wPad", UInt16),
        ("TypeBitMaps", Byte * 0),
    ]
    return DNS_NSEC_DATAA
def _define_DNS_NSEC3_DATA_head():
    class DNS_NSEC3_DATA(Structure):
        pass
    return DNS_NSEC3_DATA
def _define_DNS_NSEC3_DATA():
    DNS_NSEC3_DATA = win32more.NetworkManagement.Dns.DNS_NSEC3_DATA_head
    DNS_NSEC3_DATA._fields_ = [
        ("chAlgorithm", Byte),
        ("bFlags", Byte),
        ("wIterations", UInt16),
        ("bSaltLength", Byte),
        ("bHashLength", Byte),
        ("wTypeBitMapsLength", UInt16),
        ("chData", Byte * 0),
    ]
    return DNS_NSEC3_DATA
def _define_DNS_NSEC3PARAM_DATA_head():
    class DNS_NSEC3PARAM_DATA(Structure):
        pass
    return DNS_NSEC3PARAM_DATA
def _define_DNS_NSEC3PARAM_DATA():
    DNS_NSEC3PARAM_DATA = win32more.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA_head
    DNS_NSEC3PARAM_DATA._fields_ = [
        ("chAlgorithm", Byte),
        ("bFlags", Byte),
        ("wIterations", UInt16),
        ("bSaltLength", Byte),
        ("bPad", Byte * 3),
        ("pbSalt", Byte * 0),
    ]
    return DNS_NSEC3PARAM_DATA
def _define_DNS_TLSA_DATA_head():
    class DNS_TLSA_DATA(Structure):
        pass
    return DNS_TLSA_DATA
def _define_DNS_TLSA_DATA():
    DNS_TLSA_DATA = win32more.NetworkManagement.Dns.DNS_TLSA_DATA_head
    DNS_TLSA_DATA._fields_ = [
        ("bCertUsage", Byte),
        ("bSelector", Byte),
        ("bMatchingType", Byte),
        ("bCertificateAssociationDataLength", UInt16),
        ("bPad", Byte * 3),
        ("bCertificateAssociationData", Byte * 0),
    ]
    return DNS_TLSA_DATA
def _define_DNS_DS_DATA_head():
    class DNS_DS_DATA(Structure):
        pass
    return DNS_DS_DATA
def _define_DNS_DS_DATA():
    DNS_DS_DATA = win32more.NetworkManagement.Dns.DNS_DS_DATA_head
    DNS_DS_DATA._fields_ = [
        ("wKeyTag", UInt16),
        ("chAlgorithm", Byte),
        ("chDigestType", Byte),
        ("wDigestLength", UInt16),
        ("wPad", UInt16),
        ("Digest", Byte * 0),
    ]
    return DNS_DS_DATA
def _define_DNS_OPT_DATA_head():
    class DNS_OPT_DATA(Structure):
        pass
    return DNS_OPT_DATA
def _define_DNS_OPT_DATA():
    DNS_OPT_DATA = win32more.NetworkManagement.Dns.DNS_OPT_DATA_head
    DNS_OPT_DATA._fields_ = [
        ("wDataLength", UInt16),
        ("wPad", UInt16),
        ("Data", Byte * 0),
    ]
    return DNS_OPT_DATA
def _define_DNS_LOC_DATA_head():
    class DNS_LOC_DATA(Structure):
        pass
    return DNS_LOC_DATA
def _define_DNS_LOC_DATA():
    DNS_LOC_DATA = win32more.NetworkManagement.Dns.DNS_LOC_DATA_head
    DNS_LOC_DATA._fields_ = [
        ("wVersion", UInt16),
        ("wSize", UInt16),
        ("wHorPrec", UInt16),
        ("wVerPrec", UInt16),
        ("dwLatitude", UInt32),
        ("dwLongitude", UInt32),
        ("dwAltitude", UInt32),
    ]
    return DNS_LOC_DATA
def _define_DNS_NXT_DATAW_head():
    class DNS_NXT_DATAW(Structure):
        pass
    return DNS_NXT_DATAW
def _define_DNS_NXT_DATAW():
    DNS_NXT_DATAW = win32more.NetworkManagement.Dns.DNS_NXT_DATAW_head
    DNS_NXT_DATAW._fields_ = [
        ("pNameNext", win32more.Foundation.PWSTR),
        ("wNumTypes", UInt16),
        ("wTypes", UInt16 * 0),
    ]
    return DNS_NXT_DATAW
def _define_DNS_NXT_DATAA_head():
    class DNS_NXT_DATAA(Structure):
        pass
    return DNS_NXT_DATAA
def _define_DNS_NXT_DATAA():
    DNS_NXT_DATAA = win32more.NetworkManagement.Dns.DNS_NXT_DATAA_head
    DNS_NXT_DATAA._fields_ = [
        ("pNameNext", win32more.Foundation.PSTR),
        ("wNumTypes", UInt16),
        ("wTypes", UInt16 * 0),
    ]
    return DNS_NXT_DATAA
def _define_DNS_SRV_DATAW_head():
    class DNS_SRV_DATAW(Structure):
        pass
    return DNS_SRV_DATAW
def _define_DNS_SRV_DATAW():
    DNS_SRV_DATAW = win32more.NetworkManagement.Dns.DNS_SRV_DATAW_head
    DNS_SRV_DATAW._fields_ = [
        ("pNameTarget", win32more.Foundation.PWSTR),
        ("wPriority", UInt16),
        ("wWeight", UInt16),
        ("wPort", UInt16),
        ("Pad", UInt16),
    ]
    return DNS_SRV_DATAW
def _define_DNS_SRV_DATAA_head():
    class DNS_SRV_DATAA(Structure):
        pass
    return DNS_SRV_DATAA
def _define_DNS_SRV_DATAA():
    DNS_SRV_DATAA = win32more.NetworkManagement.Dns.DNS_SRV_DATAA_head
    DNS_SRV_DATAA._fields_ = [
        ("pNameTarget", win32more.Foundation.PSTR),
        ("wPriority", UInt16),
        ("wWeight", UInt16),
        ("wPort", UInt16),
        ("Pad", UInt16),
    ]
    return DNS_SRV_DATAA
def _define_DNS_NAPTR_DATAW_head():
    class DNS_NAPTR_DATAW(Structure):
        pass
    return DNS_NAPTR_DATAW
def _define_DNS_NAPTR_DATAW():
    DNS_NAPTR_DATAW = win32more.NetworkManagement.Dns.DNS_NAPTR_DATAW_head
    DNS_NAPTR_DATAW._fields_ = [
        ("wOrder", UInt16),
        ("wPreference", UInt16),
        ("pFlags", win32more.Foundation.PWSTR),
        ("pService", win32more.Foundation.PWSTR),
        ("pRegularExpression", win32more.Foundation.PWSTR),
        ("pReplacement", win32more.Foundation.PWSTR),
    ]
    return DNS_NAPTR_DATAW
def _define_DNS_NAPTR_DATAA_head():
    class DNS_NAPTR_DATAA(Structure):
        pass
    return DNS_NAPTR_DATAA
def _define_DNS_NAPTR_DATAA():
    DNS_NAPTR_DATAA = win32more.NetworkManagement.Dns.DNS_NAPTR_DATAA_head
    DNS_NAPTR_DATAA._fields_ = [
        ("wOrder", UInt16),
        ("wPreference", UInt16),
        ("pFlags", win32more.Foundation.PSTR),
        ("pService", win32more.Foundation.PSTR),
        ("pRegularExpression", win32more.Foundation.PSTR),
        ("pReplacement", win32more.Foundation.PSTR),
    ]
    return DNS_NAPTR_DATAA
def _define_DNS_ATMA_DATA_head():
    class DNS_ATMA_DATA(Structure):
        pass
    return DNS_ATMA_DATA
def _define_DNS_ATMA_DATA():
    DNS_ATMA_DATA = win32more.NetworkManagement.Dns.DNS_ATMA_DATA_head
    DNS_ATMA_DATA._fields_ = [
        ("AddressType", Byte),
        ("Address", Byte * 20),
    ]
    return DNS_ATMA_DATA
def _define_DNS_TKEY_DATAW_head():
    class DNS_TKEY_DATAW(Structure):
        pass
    return DNS_TKEY_DATAW
def _define_DNS_TKEY_DATAW():
    DNS_TKEY_DATAW = win32more.NetworkManagement.Dns.DNS_TKEY_DATAW_head
    DNS_TKEY_DATAW._fields_ = [
        ("pNameAlgorithm", win32more.Foundation.PWSTR),
        ("pAlgorithmPacket", c_char_p_no),
        ("pKey", c_char_p_no),
        ("pOtherData", c_char_p_no),
        ("dwCreateTime", UInt32),
        ("dwExpireTime", UInt32),
        ("wMode", UInt16),
        ("wError", UInt16),
        ("wKeyLength", UInt16),
        ("wOtherLength", UInt16),
        ("cAlgNameLength", Byte),
        ("bPacketPointers", win32more.Foundation.BOOL),
    ]
    return DNS_TKEY_DATAW
def _define_DNS_TKEY_DATAA_head():
    class DNS_TKEY_DATAA(Structure):
        pass
    return DNS_TKEY_DATAA
def _define_DNS_TKEY_DATAA():
    DNS_TKEY_DATAA = win32more.NetworkManagement.Dns.DNS_TKEY_DATAA_head
    DNS_TKEY_DATAA._fields_ = [
        ("pNameAlgorithm", win32more.Foundation.PSTR),
        ("pAlgorithmPacket", c_char_p_no),
        ("pKey", c_char_p_no),
        ("pOtherData", c_char_p_no),
        ("dwCreateTime", UInt32),
        ("dwExpireTime", UInt32),
        ("wMode", UInt16),
        ("wError", UInt16),
        ("wKeyLength", UInt16),
        ("wOtherLength", UInt16),
        ("cAlgNameLength", Byte),
        ("bPacketPointers", win32more.Foundation.BOOL),
    ]
    return DNS_TKEY_DATAA
def _define_DNS_TSIG_DATAW_head():
    class DNS_TSIG_DATAW(Structure):
        pass
    return DNS_TSIG_DATAW
def _define_DNS_TSIG_DATAW():
    DNS_TSIG_DATAW = win32more.NetworkManagement.Dns.DNS_TSIG_DATAW_head
    DNS_TSIG_DATAW._fields_ = [
        ("pNameAlgorithm", win32more.Foundation.PWSTR),
        ("pAlgorithmPacket", c_char_p_no),
        ("pSignature", c_char_p_no),
        ("pOtherData", c_char_p_no),
        ("i64CreateTime", Int64),
        ("wFudgeTime", UInt16),
        ("wOriginalXid", UInt16),
        ("wError", UInt16),
        ("wSigLength", UInt16),
        ("wOtherLength", UInt16),
        ("cAlgNameLength", Byte),
        ("bPacketPointers", win32more.Foundation.BOOL),
    ]
    return DNS_TSIG_DATAW
def _define_DNS_TSIG_DATAA_head():
    class DNS_TSIG_DATAA(Structure):
        pass
    return DNS_TSIG_DATAA
def _define_DNS_TSIG_DATAA():
    DNS_TSIG_DATAA = win32more.NetworkManagement.Dns.DNS_TSIG_DATAA_head
    DNS_TSIG_DATAA._fields_ = [
        ("pNameAlgorithm", win32more.Foundation.PSTR),
        ("pAlgorithmPacket", c_char_p_no),
        ("pSignature", c_char_p_no),
        ("pOtherData", c_char_p_no),
        ("i64CreateTime", Int64),
        ("wFudgeTime", UInt16),
        ("wOriginalXid", UInt16),
        ("wError", UInt16),
        ("wSigLength", UInt16),
        ("wOtherLength", UInt16),
        ("cAlgNameLength", Byte),
        ("bPacketPointers", win32more.Foundation.BOOL),
    ]
    return DNS_TSIG_DATAA
def _define_DNS_UNKNOWN_DATA_head():
    class DNS_UNKNOWN_DATA(Structure):
        pass
    return DNS_UNKNOWN_DATA
def _define_DNS_UNKNOWN_DATA():
    DNS_UNKNOWN_DATA = win32more.NetworkManagement.Dns.DNS_UNKNOWN_DATA_head
    DNS_UNKNOWN_DATA._fields_ = [
        ("dwByteCount", UInt32),
        ("bData", Byte * 0),
    ]
    return DNS_UNKNOWN_DATA
def _define_DNS_WINS_DATA_head():
    class DNS_WINS_DATA(Structure):
        pass
    return DNS_WINS_DATA
def _define_DNS_WINS_DATA():
    DNS_WINS_DATA = win32more.NetworkManagement.Dns.DNS_WINS_DATA_head
    DNS_WINS_DATA._fields_ = [
        ("dwMappingFlag", UInt32),
        ("dwLookupTimeout", UInt32),
        ("dwCacheTimeout", UInt32),
        ("cWinsServerCount", UInt32),
        ("WinsServers", UInt32 * 0),
    ]
    return DNS_WINS_DATA
def _define_DNS_WINSR_DATAW_head():
    class DNS_WINSR_DATAW(Structure):
        pass
    return DNS_WINSR_DATAW
def _define_DNS_WINSR_DATAW():
    DNS_WINSR_DATAW = win32more.NetworkManagement.Dns.DNS_WINSR_DATAW_head
    DNS_WINSR_DATAW._fields_ = [
        ("dwMappingFlag", UInt32),
        ("dwLookupTimeout", UInt32),
        ("dwCacheTimeout", UInt32),
        ("pNameResultDomain", win32more.Foundation.PWSTR),
    ]
    return DNS_WINSR_DATAW
def _define_DNS_WINSR_DATAA_head():
    class DNS_WINSR_DATAA(Structure):
        pass
    return DNS_WINSR_DATAA
def _define_DNS_WINSR_DATAA():
    DNS_WINSR_DATAA = win32more.NetworkManagement.Dns.DNS_WINSR_DATAA_head
    DNS_WINSR_DATAA._fields_ = [
        ("dwMappingFlag", UInt32),
        ("dwLookupTimeout", UInt32),
        ("dwCacheTimeout", UInt32),
        ("pNameResultDomain", win32more.Foundation.PSTR),
    ]
    return DNS_WINSR_DATAA
def _define_DNS_RECORD_FLAGS_head():
    class DNS_RECORD_FLAGS(Structure):
        pass
    return DNS_RECORD_FLAGS
def _define_DNS_RECORD_FLAGS():
    DNS_RECORD_FLAGS = win32more.NetworkManagement.Dns.DNS_RECORD_FLAGS_head
    DNS_RECORD_FLAGS._fields_ = [
        ("_bitfield", UInt32),
    ]
    return DNS_RECORD_FLAGS
DNS_SECTION = Int32
DNS_SECTION_DnsSectionQuestion = 0
DNS_SECTION_DnsSectionAnswer = 1
DNS_SECTION_DnsSectionAuthority = 2
DNS_SECTION_DnsSectionAddtional = 3
def _define_DNS_RECORDW_head():
    class DNS_RECORDW(Structure):
        pass
    return DNS_RECORDW
def _define_DNS_RECORDW():
    DNS_RECORDW = win32more.NetworkManagement.Dns.DNS_RECORDW_head
    class DNS_RECORDW__Flags_e__Union(Union):
        pass
    DNS_RECORDW__Flags_e__Union._fields_ = [
        ("DW", UInt32),
        ("S", win32more.NetworkManagement.Dns.DNS_RECORD_FLAGS),
    ]
    class DNS_RECORDW__Data_e__Union(Union):
        pass
    DNS_RECORDW__Data_e__Union._fields_ = [
        ("A", win32more.NetworkManagement.Dns.DNS_A_DATA),
        ("SOA", win32more.NetworkManagement.Dns.DNS_SOA_DATAW),
        ("Soa", win32more.NetworkManagement.Dns.DNS_SOA_DATAW),
        ("PTR", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Ptr", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("NS", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Ns", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("CNAME", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Cname", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("DNAME", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Dname", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("MB", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Mb", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("MD", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Md", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("MF", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Mf", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("MG", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Mg", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("MR", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("Mr", win32more.NetworkManagement.Dns.DNS_PTR_DATAW),
        ("MINFO", win32more.NetworkManagement.Dns.DNS_MINFO_DATAW),
        ("Minfo", win32more.NetworkManagement.Dns.DNS_MINFO_DATAW),
        ("RP", win32more.NetworkManagement.Dns.DNS_MINFO_DATAW),
        ("Rp", win32more.NetworkManagement.Dns.DNS_MINFO_DATAW),
        ("MX", win32more.NetworkManagement.Dns.DNS_MX_DATAW),
        ("Mx", win32more.NetworkManagement.Dns.DNS_MX_DATAW),
        ("AFSDB", win32more.NetworkManagement.Dns.DNS_MX_DATAW),
        ("Afsdb", win32more.NetworkManagement.Dns.DNS_MX_DATAW),
        ("RT", win32more.NetworkManagement.Dns.DNS_MX_DATAW),
        ("Rt", win32more.NetworkManagement.Dns.DNS_MX_DATAW),
        ("HINFO", win32more.NetworkManagement.Dns.DNS_TXT_DATAW),
        ("Hinfo", win32more.NetworkManagement.Dns.DNS_TXT_DATAW),
        ("ISDN", win32more.NetworkManagement.Dns.DNS_TXT_DATAW),
        ("Isdn", win32more.NetworkManagement.Dns.DNS_TXT_DATAW),
        ("TXT", win32more.NetworkManagement.Dns.DNS_TXT_DATAW),
        ("Txt", win32more.NetworkManagement.Dns.DNS_TXT_DATAW),
        ("X25", win32more.NetworkManagement.Dns.DNS_TXT_DATAW),
        ("Null", win32more.NetworkManagement.Dns.DNS_NULL_DATA),
        ("WKS", win32more.NetworkManagement.Dns.DNS_WKS_DATA),
        ("Wks", win32more.NetworkManagement.Dns.DNS_WKS_DATA),
        ("AAAA", win32more.NetworkManagement.Dns.DNS_AAAA_DATA),
        ("KEY", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("Key", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("SIG", win32more.NetworkManagement.Dns.DNS_SIG_DATAW),
        ("Sig", win32more.NetworkManagement.Dns.DNS_SIG_DATAW),
        ("ATMA", win32more.NetworkManagement.Dns.DNS_ATMA_DATA),
        ("Atma", win32more.NetworkManagement.Dns.DNS_ATMA_DATA),
        ("NXT", win32more.NetworkManagement.Dns.DNS_NXT_DATAW),
        ("Nxt", win32more.NetworkManagement.Dns.DNS_NXT_DATAW),
        ("SRV", win32more.NetworkManagement.Dns.DNS_SRV_DATAW),
        ("Srv", win32more.NetworkManagement.Dns.DNS_SRV_DATAW),
        ("NAPTR", win32more.NetworkManagement.Dns.DNS_NAPTR_DATAW),
        ("Naptr", win32more.NetworkManagement.Dns.DNS_NAPTR_DATAW),
        ("OPT", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
        ("Opt", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
        ("DS", win32more.NetworkManagement.Dns.DNS_DS_DATA),
        ("Ds", win32more.NetworkManagement.Dns.DNS_DS_DATA),
        ("RRSIG", win32more.NetworkManagement.Dns.DNS_SIG_DATAW),
        ("Rrsig", win32more.NetworkManagement.Dns.DNS_SIG_DATAW),
        ("NSEC", win32more.NetworkManagement.Dns.DNS_NSEC_DATAW),
        ("Nsec", win32more.NetworkManagement.Dns.DNS_NSEC_DATAW),
        ("DNSKEY", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("Dnskey", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("TKEY", win32more.NetworkManagement.Dns.DNS_TKEY_DATAW),
        ("Tkey", win32more.NetworkManagement.Dns.DNS_TKEY_DATAW),
        ("TSIG", win32more.NetworkManagement.Dns.DNS_TSIG_DATAW),
        ("Tsig", win32more.NetworkManagement.Dns.DNS_TSIG_DATAW),
        ("WINS", win32more.NetworkManagement.Dns.DNS_WINS_DATA),
        ("Wins", win32more.NetworkManagement.Dns.DNS_WINS_DATA),
        ("WINSR", win32more.NetworkManagement.Dns.DNS_WINSR_DATAW),
        ("WinsR", win32more.NetworkManagement.Dns.DNS_WINSR_DATAW),
        ("NBSTAT", win32more.NetworkManagement.Dns.DNS_WINSR_DATAW),
        ("Nbstat", win32more.NetworkManagement.Dns.DNS_WINSR_DATAW),
        ("DHCID", win32more.NetworkManagement.Dns.DNS_DHCID_DATA),
        ("NSEC3", win32more.NetworkManagement.Dns.DNS_NSEC3_DATA),
        ("Nsec3", win32more.NetworkManagement.Dns.DNS_NSEC3_DATA),
        ("NSEC3PARAM", win32more.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA),
        ("Nsec3Param", win32more.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA),
        ("TLSA", win32more.NetworkManagement.Dns.DNS_TLSA_DATA),
        ("Tlsa", win32more.NetworkManagement.Dns.DNS_TLSA_DATA),
        ("UNKNOWN", win32more.NetworkManagement.Dns.DNS_UNKNOWN_DATA),
        ("Unknown", win32more.NetworkManagement.Dns.DNS_UNKNOWN_DATA),
        ("pDataPtr", c_char_p_no),
    ]
    DNS_RECORDW._fields_ = [
        ("pNext", POINTER(win32more.NetworkManagement.Dns.DNS_RECORDW_head)),
        ("pName", win32more.Foundation.PWSTR),
        ("wType", UInt16),
        ("wDataLength", UInt16),
        ("Flags", DNS_RECORDW__Flags_e__Union),
        ("dwTtl", UInt32),
        ("dwReserved", UInt32),
        ("Data", DNS_RECORDW__Data_e__Union),
    ]
    return DNS_RECORDW
def _define__DnsRecordOptW_head():
    class _DnsRecordOptW(Structure):
        pass
    return _DnsRecordOptW
def _define__DnsRecordOptW():
    _DnsRecordOptW = win32more.NetworkManagement.Dns._DnsRecordOptW_head
    class _DnsRecordOptW__Flags_e__Union(Union):
        pass
    _DnsRecordOptW__Flags_e__Union._fields_ = [
        ("DW", UInt32),
        ("S", win32more.NetworkManagement.Dns.DNS_RECORD_FLAGS),
    ]
    class _DnsRecordOptW__Data_e__Union(Union):
        pass
    _DnsRecordOptW__Data_e__Union._fields_ = [
        ("OPT", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
        ("Opt", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
    ]
    _DnsRecordOptW._fields_ = [
        ("pNext", POINTER(win32more.NetworkManagement.Dns.DNS_RECORDW_head)),
        ("pName", win32more.Foundation.PWSTR),
        ("wType", UInt16),
        ("wDataLength", UInt16),
        ("Flags", _DnsRecordOptW__Flags_e__Union),
        ("ExtHeader", win32more.NetworkManagement.Dns.DNS_HEADER_EXT),
        ("wPayloadSize", UInt16),
        ("wReserved", UInt16),
        ("Data", _DnsRecordOptW__Data_e__Union),
    ]
    return _DnsRecordOptW
def _define_DNS_RECORDA_head():
    class DNS_RECORDA(Structure):
        pass
    return DNS_RECORDA
def _define_DNS_RECORDA():
    DNS_RECORDA = win32more.NetworkManagement.Dns.DNS_RECORDA_head
    class DNS_RECORDA__Flags_e__Union(Union):
        pass
    DNS_RECORDA__Flags_e__Union._fields_ = [
        ("DW", UInt32),
        ("S", win32more.NetworkManagement.Dns.DNS_RECORD_FLAGS),
    ]
    class DNS_RECORDA__Data_e__Union(Union):
        pass
    DNS_RECORDA__Data_e__Union._fields_ = [
        ("A", win32more.NetworkManagement.Dns.DNS_A_DATA),
        ("SOA", win32more.NetworkManagement.Dns.DNS_SOA_DATAA),
        ("Soa", win32more.NetworkManagement.Dns.DNS_SOA_DATAA),
        ("PTR", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Ptr", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("NS", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Ns", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("CNAME", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Cname", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("DNAME", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Dname", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("MB", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Mb", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("MD", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Md", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("MF", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Mf", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("MG", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Mg", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("MR", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("Mr", win32more.NetworkManagement.Dns.DNS_PTR_DATAA),
        ("MINFO", win32more.NetworkManagement.Dns.DNS_MINFO_DATAA),
        ("Minfo", win32more.NetworkManagement.Dns.DNS_MINFO_DATAA),
        ("RP", win32more.NetworkManagement.Dns.DNS_MINFO_DATAA),
        ("Rp", win32more.NetworkManagement.Dns.DNS_MINFO_DATAA),
        ("MX", win32more.NetworkManagement.Dns.DNS_MX_DATAA),
        ("Mx", win32more.NetworkManagement.Dns.DNS_MX_DATAA),
        ("AFSDB", win32more.NetworkManagement.Dns.DNS_MX_DATAA),
        ("Afsdb", win32more.NetworkManagement.Dns.DNS_MX_DATAA),
        ("RT", win32more.NetworkManagement.Dns.DNS_MX_DATAA),
        ("Rt", win32more.NetworkManagement.Dns.DNS_MX_DATAA),
        ("HINFO", win32more.NetworkManagement.Dns.DNS_TXT_DATAA),
        ("Hinfo", win32more.NetworkManagement.Dns.DNS_TXT_DATAA),
        ("ISDN", win32more.NetworkManagement.Dns.DNS_TXT_DATAA),
        ("Isdn", win32more.NetworkManagement.Dns.DNS_TXT_DATAA),
        ("TXT", win32more.NetworkManagement.Dns.DNS_TXT_DATAA),
        ("Txt", win32more.NetworkManagement.Dns.DNS_TXT_DATAA),
        ("X25", win32more.NetworkManagement.Dns.DNS_TXT_DATAA),
        ("Null", win32more.NetworkManagement.Dns.DNS_NULL_DATA),
        ("WKS", win32more.NetworkManagement.Dns.DNS_WKS_DATA),
        ("Wks", win32more.NetworkManagement.Dns.DNS_WKS_DATA),
        ("AAAA", win32more.NetworkManagement.Dns.DNS_AAAA_DATA),
        ("KEY", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("Key", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("SIG", win32more.NetworkManagement.Dns.DNS_SIG_DATAA),
        ("Sig", win32more.NetworkManagement.Dns.DNS_SIG_DATAA),
        ("ATMA", win32more.NetworkManagement.Dns.DNS_ATMA_DATA),
        ("Atma", win32more.NetworkManagement.Dns.DNS_ATMA_DATA),
        ("NXT", win32more.NetworkManagement.Dns.DNS_NXT_DATAA),
        ("Nxt", win32more.NetworkManagement.Dns.DNS_NXT_DATAA),
        ("SRV", win32more.NetworkManagement.Dns.DNS_SRV_DATAA),
        ("Srv", win32more.NetworkManagement.Dns.DNS_SRV_DATAA),
        ("NAPTR", win32more.NetworkManagement.Dns.DNS_NAPTR_DATAA),
        ("Naptr", win32more.NetworkManagement.Dns.DNS_NAPTR_DATAA),
        ("OPT", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
        ("Opt", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
        ("DS", win32more.NetworkManagement.Dns.DNS_DS_DATA),
        ("Ds", win32more.NetworkManagement.Dns.DNS_DS_DATA),
        ("RRSIG", win32more.NetworkManagement.Dns.DNS_SIG_DATAA),
        ("Rrsig", win32more.NetworkManagement.Dns.DNS_SIG_DATAA),
        ("NSEC", win32more.NetworkManagement.Dns.DNS_NSEC_DATAA),
        ("Nsec", win32more.NetworkManagement.Dns.DNS_NSEC_DATAA),
        ("DNSKEY", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("Dnskey", win32more.NetworkManagement.Dns.DNS_KEY_DATA),
        ("TKEY", win32more.NetworkManagement.Dns.DNS_TKEY_DATAA),
        ("Tkey", win32more.NetworkManagement.Dns.DNS_TKEY_DATAA),
        ("TSIG", win32more.NetworkManagement.Dns.DNS_TSIG_DATAA),
        ("Tsig", win32more.NetworkManagement.Dns.DNS_TSIG_DATAA),
        ("WINS", win32more.NetworkManagement.Dns.DNS_WINS_DATA),
        ("Wins", win32more.NetworkManagement.Dns.DNS_WINS_DATA),
        ("WINSR", win32more.NetworkManagement.Dns.DNS_WINSR_DATAA),
        ("WinsR", win32more.NetworkManagement.Dns.DNS_WINSR_DATAA),
        ("NBSTAT", win32more.NetworkManagement.Dns.DNS_WINSR_DATAA),
        ("Nbstat", win32more.NetworkManagement.Dns.DNS_WINSR_DATAA),
        ("DHCID", win32more.NetworkManagement.Dns.DNS_DHCID_DATA),
        ("NSEC3", win32more.NetworkManagement.Dns.DNS_NSEC3_DATA),
        ("Nsec3", win32more.NetworkManagement.Dns.DNS_NSEC3_DATA),
        ("NSEC3PARAM", win32more.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA),
        ("Nsec3Param", win32more.NetworkManagement.Dns.DNS_NSEC3PARAM_DATA),
        ("TLSA", win32more.NetworkManagement.Dns.DNS_TLSA_DATA),
        ("Tlsa", win32more.NetworkManagement.Dns.DNS_TLSA_DATA),
        ("UNKNOWN", win32more.NetworkManagement.Dns.DNS_UNKNOWN_DATA),
        ("Unknown", win32more.NetworkManagement.Dns.DNS_UNKNOWN_DATA),
        ("pDataPtr", c_char_p_no),
    ]
    DNS_RECORDA._fields_ = [
        ("pNext", POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),
        ("pName", win32more.Foundation.PSTR),
        ("wType", UInt16),
        ("wDataLength", UInt16),
        ("Flags", DNS_RECORDA__Flags_e__Union),
        ("dwTtl", UInt32),
        ("dwReserved", UInt32),
        ("Data", DNS_RECORDA__Data_e__Union),
    ]
    return DNS_RECORDA
def _define__DnsRecordOptA_head():
    class _DnsRecordOptA(Structure):
        pass
    return _DnsRecordOptA
def _define__DnsRecordOptA():
    _DnsRecordOptA = win32more.NetworkManagement.Dns._DnsRecordOptA_head
    class _DnsRecordOptA__Flags_e__Union(Union):
        pass
    _DnsRecordOptA__Flags_e__Union._fields_ = [
        ("DW", UInt32),
        ("S", win32more.NetworkManagement.Dns.DNS_RECORD_FLAGS),
    ]
    class _DnsRecordOptA__Data_e__Union(Union):
        pass
    _DnsRecordOptA__Data_e__Union._fields_ = [
        ("OPT", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
        ("Opt", win32more.NetworkManagement.Dns.DNS_OPT_DATA),
    ]
    _DnsRecordOptA._fields_ = [
        ("pNext", POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),
        ("pName", win32more.Foundation.PSTR),
        ("wType", UInt16),
        ("wDataLength", UInt16),
        ("Flags", _DnsRecordOptA__Flags_e__Union),
        ("ExtHeader", win32more.NetworkManagement.Dns.DNS_HEADER_EXT),
        ("wPayloadSize", UInt16),
        ("wReserved", UInt16),
        ("Data", _DnsRecordOptA__Data_e__Union),
    ]
    return _DnsRecordOptA
def _define_DNS_RRSET_head():
    class DNS_RRSET(Structure):
        pass
    return DNS_RRSET
def _define_DNS_RRSET():
    DNS_RRSET = win32more.NetworkManagement.Dns.DNS_RRSET_head
    DNS_RRSET._fields_ = [
        ("pFirstRR", POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),
        ("pLastRR", POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),
    ]
    return DNS_RRSET
def _define_DNS_PROXY_COMPLETION_ROUTINE():
    return CFUNCTYPE(Void,c_void_p,Int32, use_last_error=False)
DNS_PROXY_INFORMATION_TYPE = Int32
DNS_PROXY_INFORMATION_DIRECT = 0
DNS_PROXY_INFORMATION_DEFAULT_SETTINGS = 1
DNS_PROXY_INFORMATION_PROXY_NAME = 2
DNS_PROXY_INFORMATION_DOES_NOT_EXIST = 3
def _define_DNS_PROXY_INFORMATION_head():
    class DNS_PROXY_INFORMATION(Structure):
        pass
    return DNS_PROXY_INFORMATION
def _define_DNS_PROXY_INFORMATION():
    DNS_PROXY_INFORMATION = win32more.NetworkManagement.Dns.DNS_PROXY_INFORMATION_head
    DNS_PROXY_INFORMATION._fields_ = [
        ("version", UInt32),
        ("proxyInformationType", win32more.NetworkManagement.Dns.DNS_PROXY_INFORMATION_TYPE),
        ("proxyName", win32more.Foundation.PWSTR),
    ]
    return DNS_PROXY_INFORMATION
DNS_CHARSET = Int32
DNS_CHARSET_DnsCharSetUnknown = 0
DNS_CHARSET_DnsCharSetUnicode = 1
DNS_CHARSET_DnsCharSetUtf8 = 2
DNS_CHARSET_DnsCharSetAnsi = 3
DNS_FREE_TYPE = Int32
DNS_FREE_TYPE_DnsFreeFlat = 0
DNS_FREE_TYPE_DnsFreeRecordList = 1
DNS_FREE_TYPE_DnsFreeParsedMessageFields = 2
def _define_DNS_QUERY_RESULT_head():
    class DNS_QUERY_RESULT(Structure):
        pass
    return DNS_QUERY_RESULT
def _define_DNS_QUERY_RESULT():
    DNS_QUERY_RESULT = win32more.NetworkManagement.Dns.DNS_QUERY_RESULT_head
    DNS_QUERY_RESULT._fields_ = [
        ("Version", UInt32),
        ("QueryStatus", Int32),
        ("QueryOptions", UInt64),
        ("pQueryRecords", POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),
        ("Reserved", c_void_p),
    ]
    return DNS_QUERY_RESULT
def _define_PDNS_QUERY_COMPLETION_ROUTINE():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.Dns.DNS_QUERY_RESULT_head), use_last_error=False)
def _define_DNS_QUERY_REQUEST_head():
    class DNS_QUERY_REQUEST(Structure):
        pass
    return DNS_QUERY_REQUEST
def _define_DNS_QUERY_REQUEST():
    DNS_QUERY_REQUEST = win32more.NetworkManagement.Dns.DNS_QUERY_REQUEST_head
    DNS_QUERY_REQUEST._fields_ = [
        ("Version", UInt32),
        ("QueryName", win32more.Foundation.PWSTR),
        ("QueryType", UInt16),
        ("QueryOptions", UInt64),
        ("pDnsServerList", POINTER(win32more.NetworkManagement.Dns.DNS_ADDR_ARRAY_head)),
        ("InterfaceIndex", UInt32),
        ("pQueryCompletionCallback", win32more.NetworkManagement.Dns.PDNS_QUERY_COMPLETION_ROUTINE),
        ("pQueryContext", c_void_p),
    ]
    return DNS_QUERY_REQUEST
def _define_DNS_QUERY_CANCEL_head():
    class DNS_QUERY_CANCEL(Structure):
        pass
    return DNS_QUERY_CANCEL
def _define_DNS_QUERY_CANCEL():
    DNS_QUERY_CANCEL = win32more.NetworkManagement.Dns.DNS_QUERY_CANCEL_head
    DNS_QUERY_CANCEL._fields_ = [
        ("Reserved", win32more.Foundation.CHAR * 32),
    ]
    return DNS_QUERY_CANCEL
def _define_DNS_CUSTOM_SERVER_head():
    class DNS_CUSTOM_SERVER(Structure):
        pass
    return DNS_CUSTOM_SERVER
def _define_DNS_CUSTOM_SERVER():
    DNS_CUSTOM_SERVER = win32more.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head
    class DNS_CUSTOM_SERVER__Anonymous1_e__Union(Union):
        pass
    DNS_CUSTOM_SERVER__Anonymous1_e__Union._fields_ = [
        ("pwszTemplate", win32more.Foundation.PWSTR),
    ]
    class DNS_CUSTOM_SERVER__Anonymous2_e__Union(Union):
        pass
    DNS_CUSTOM_SERVER__Anonymous2_e__Union._fields_ = [
        ("MaxSa", win32more.Foundation.CHAR * 32),
    ]
    DNS_CUSTOM_SERVER._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    DNS_CUSTOM_SERVER._fields_ = [
        ("dwServerType", UInt32),
        ("ullFlags", UInt64),
        ("Anonymous1", DNS_CUSTOM_SERVER__Anonymous1_e__Union),
        ("Anonymous2", DNS_CUSTOM_SERVER__Anonymous2_e__Union),
    ]
    return DNS_CUSTOM_SERVER
def _define_DNS_QUERY_REQUEST3_head():
    class DNS_QUERY_REQUEST3(Structure):
        pass
    return DNS_QUERY_REQUEST3
def _define_DNS_QUERY_REQUEST3():
    DNS_QUERY_REQUEST3 = win32more.NetworkManagement.Dns.DNS_QUERY_REQUEST3_head
    DNS_QUERY_REQUEST3._fields_ = [
        ("Version", UInt32),
        ("QueryName", win32more.Foundation.PWSTR),
        ("QueryType", UInt16),
        ("QueryOptions", UInt64),
        ("pDnsServerList", POINTER(win32more.NetworkManagement.Dns.DNS_ADDR_ARRAY_head)),
        ("InterfaceIndex", UInt32),
        ("pQueryCompletionCallback", win32more.NetworkManagement.Dns.PDNS_QUERY_COMPLETION_ROUTINE),
        ("pQueryContext", c_void_p),
        ("IsNetworkQueryRequired", win32more.Foundation.BOOL),
        ("RequiredNetworkIndex", UInt32),
        ("cCustomServers", UInt32),
        ("pCustomServers", POINTER(win32more.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head)),
    ]
    return DNS_QUERY_REQUEST3
def _define_DNS_APPLICATION_SETTINGS_head():
    class DNS_APPLICATION_SETTINGS(Structure):
        pass
    return DNS_APPLICATION_SETTINGS
def _define_DNS_APPLICATION_SETTINGS():
    DNS_APPLICATION_SETTINGS = win32more.NetworkManagement.Dns.DNS_APPLICATION_SETTINGS_head
    DNS_APPLICATION_SETTINGS._fields_ = [
        ("Version", UInt32),
        ("Flags", UInt64),
    ]
    return DNS_APPLICATION_SETTINGS
DNS_NAME_FORMAT = Int32
DNS_NAME_FORMAT_DnsNameDomain = 0
DNS_NAME_FORMAT_DnsNameDomainLabel = 1
DNS_NAME_FORMAT_DnsNameHostnameFull = 2
DNS_NAME_FORMAT_DnsNameHostnameLabel = 3
DNS_NAME_FORMAT_DnsNameWildcard = 4
DNS_NAME_FORMAT_DnsNameSrvRecord = 5
DNS_NAME_FORMAT_DnsNameValidateTld = 6
def _define_DNS_MESSAGE_BUFFER_head():
    class DNS_MESSAGE_BUFFER(Structure):
        pass
    return DNS_MESSAGE_BUFFER
def _define_DNS_MESSAGE_BUFFER():
    DNS_MESSAGE_BUFFER = win32more.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head
    DNS_MESSAGE_BUFFER._fields_ = [
        ("MessageHead", win32more.NetworkManagement.Dns.DNS_HEADER),
        ("MessageBody", win32more.Foundation.CHAR * 0),
    ]
    return DNS_MESSAGE_BUFFER
DNS_CONNECTION_PROXY_TYPE = Int32
DNS_CONNECTION_PROXY_TYPE_NULL = 0
DNS_CONNECTION_PROXY_TYPE_HTTP = 1
DNS_CONNECTION_PROXY_TYPE_WAP = 2
DNS_CONNECTION_PROXY_TYPE_SOCKS4 = 4
DNS_CONNECTION_PROXY_TYPE_SOCKS5 = 5
DNS_CONNECTION_PROXY_INFO_SWITCH = Int32
DNS_CONNECTION_PROXY_INFO_SWITCH_CONFIG = 0
DNS_CONNECTION_PROXY_INFO_SWITCH_SCRIPT = 1
DNS_CONNECTION_PROXY_INFO_SWITCH_WPAD = 2
def _define_DNS_CONNECTION_PROXY_INFO_head():
    class DNS_CONNECTION_PROXY_INFO(Structure):
        pass
    return DNS_CONNECTION_PROXY_INFO
def _define_DNS_CONNECTION_PROXY_INFO():
    DNS_CONNECTION_PROXY_INFO = win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_head
    class DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union(Union):
        pass
    class DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union__DNS_CONNECTION_PROXY_INFO_SCRIPT(Structure):
        pass
    DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union__DNS_CONNECTION_PROXY_INFO_SCRIPT._fields_ = [
        ("pwszScript", win32more.Foundation.PWSTR),
        ("pwszUsername", win32more.Foundation.PWSTR),
        ("pwszPassword", win32more.Foundation.PWSTR),
    ]
    class DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union__DNS_CONNECTION_PROXY_INFO_CONFIG(Structure):
        pass
    DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union__DNS_CONNECTION_PROXY_INFO_CONFIG._fields_ = [
        ("pwszServer", win32more.Foundation.PWSTR),
        ("pwszUsername", win32more.Foundation.PWSTR),
        ("pwszPassword", win32more.Foundation.PWSTR),
        ("pwszException", win32more.Foundation.PWSTR),
        ("pwszExtraInfo", win32more.Foundation.PWSTR),
        ("Port", UInt16),
    ]
    DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union._fields_ = [
        ("Config", DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union__DNS_CONNECTION_PROXY_INFO_CONFIG),
        ("Script", DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union__DNS_CONNECTION_PROXY_INFO_SCRIPT),
    ]
    DNS_CONNECTION_PROXY_INFO._anonymous_ = [
        'Anonymous',
    ]
    DNS_CONNECTION_PROXY_INFO._fields_ = [
        ("Version", UInt32),
        ("pwszFriendlyName", win32more.Foundation.PWSTR),
        ("Flags", UInt32),
        ("Switch", win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_SWITCH),
        ("Anonymous", DNS_CONNECTION_PROXY_INFO__Anonymous_e__Union),
    ]
    return DNS_CONNECTION_PROXY_INFO
def _define_DNS_CONNECTION_PROXY_INFO_EX_head():
    class DNS_CONNECTION_PROXY_INFO_EX(Structure):
        pass
    return DNS_CONNECTION_PROXY_INFO_EX
def _define_DNS_CONNECTION_PROXY_INFO_EX():
    DNS_CONNECTION_PROXY_INFO_EX = win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_EX_head
    DNS_CONNECTION_PROXY_INFO_EX._fields_ = [
        ("ProxyInfo", win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO),
        ("dwInterfaceIndex", UInt32),
        ("pwszConnectionName", win32more.Foundation.PWSTR),
        ("fDirectConfiguration", win32more.Foundation.BOOL),
        ("hConnection", win32more.Foundation.HANDLE),
    ]
    return DNS_CONNECTION_PROXY_INFO_EX
def _define_DNS_CONNECTION_PROXY_ELEMENT_head():
    class DNS_CONNECTION_PROXY_ELEMENT(Structure):
        pass
    return DNS_CONNECTION_PROXY_ELEMENT
def _define_DNS_CONNECTION_PROXY_ELEMENT():
    DNS_CONNECTION_PROXY_ELEMENT = win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_ELEMENT_head
    DNS_CONNECTION_PROXY_ELEMENT._fields_ = [
        ("Type", win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE),
        ("Info", win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO),
    ]
    return DNS_CONNECTION_PROXY_ELEMENT
def _define_DNS_CONNECTION_PROXY_LIST_head():
    class DNS_CONNECTION_PROXY_LIST(Structure):
        pass
    return DNS_CONNECTION_PROXY_LIST
def _define_DNS_CONNECTION_PROXY_LIST():
    DNS_CONNECTION_PROXY_LIST = win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_LIST_head
    DNS_CONNECTION_PROXY_LIST._fields_ = [
        ("cProxies", UInt32),
        ("pProxies", POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_ELEMENT_head)),
    ]
    return DNS_CONNECTION_PROXY_LIST
def _define_DNS_CONNECTION_NAME_head():
    class DNS_CONNECTION_NAME(Structure):
        pass
    return DNS_CONNECTION_NAME
def _define_DNS_CONNECTION_NAME():
    DNS_CONNECTION_NAME = win32more.NetworkManagement.Dns.DNS_CONNECTION_NAME_head
    DNS_CONNECTION_NAME._fields_ = [
        ("wszName", Char * 65),
    ]
    return DNS_CONNECTION_NAME
def _define_DNS_CONNECTION_NAME_LIST_head():
    class DNS_CONNECTION_NAME_LIST(Structure):
        pass
    return DNS_CONNECTION_NAME_LIST
def _define_DNS_CONNECTION_NAME_LIST():
    DNS_CONNECTION_NAME_LIST = win32more.NetworkManagement.Dns.DNS_CONNECTION_NAME_LIST_head
    DNS_CONNECTION_NAME_LIST._fields_ = [
        ("cNames", UInt32),
        ("pNames", POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_NAME_head)),
    ]
    return DNS_CONNECTION_NAME_LIST
def _define_DNS_CONNECTION_IFINDEX_ENTRY_head():
    class DNS_CONNECTION_IFINDEX_ENTRY(Structure):
        pass
    return DNS_CONNECTION_IFINDEX_ENTRY
def _define_DNS_CONNECTION_IFINDEX_ENTRY():
    DNS_CONNECTION_IFINDEX_ENTRY = win32more.NetworkManagement.Dns.DNS_CONNECTION_IFINDEX_ENTRY_head
    DNS_CONNECTION_IFINDEX_ENTRY._fields_ = [
        ("pwszConnectionName", win32more.Foundation.PWSTR),
        ("dwIfIndex", UInt32),
    ]
    return DNS_CONNECTION_IFINDEX_ENTRY
def _define_DNS_CONNECTION_IFINDEX_LIST_head():
    class DNS_CONNECTION_IFINDEX_LIST(Structure):
        pass
    return DNS_CONNECTION_IFINDEX_LIST
def _define_DNS_CONNECTION_IFINDEX_LIST():
    DNS_CONNECTION_IFINDEX_LIST = win32more.NetworkManagement.Dns.DNS_CONNECTION_IFINDEX_LIST_head
    DNS_CONNECTION_IFINDEX_LIST._fields_ = [
        ("pConnectionIfIndexEntries", POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_IFINDEX_ENTRY_head)),
        ("nEntries", UInt32),
    ]
    return DNS_CONNECTION_IFINDEX_LIST
def _define_DNS_CONNECTION_POLICY_ENTRY_head():
    class DNS_CONNECTION_POLICY_ENTRY(Structure):
        pass
    return DNS_CONNECTION_POLICY_ENTRY
def _define_DNS_CONNECTION_POLICY_ENTRY():
    DNS_CONNECTION_POLICY_ENTRY = win32more.NetworkManagement.Dns.DNS_CONNECTION_POLICY_ENTRY_head
    DNS_CONNECTION_POLICY_ENTRY._fields_ = [
        ("pwszHost", win32more.Foundation.PWSTR),
        ("pwszAppId", win32more.Foundation.PWSTR),
        ("cbAppSid", UInt32),
        ("pbAppSid", c_char_p_no),
        ("nConnections", UInt32),
        ("ppwszConnections", POINTER(win32more.Foundation.PWSTR)),
        ("dwPolicyEntryFlags", UInt32),
    ]
    return DNS_CONNECTION_POLICY_ENTRY
def _define_DNS_CONNECTION_POLICY_ENTRY_LIST_head():
    class DNS_CONNECTION_POLICY_ENTRY_LIST(Structure):
        pass
    return DNS_CONNECTION_POLICY_ENTRY_LIST
def _define_DNS_CONNECTION_POLICY_ENTRY_LIST():
    DNS_CONNECTION_POLICY_ENTRY_LIST = win32more.NetworkManagement.Dns.DNS_CONNECTION_POLICY_ENTRY_LIST_head
    DNS_CONNECTION_POLICY_ENTRY_LIST._fields_ = [
        ("pPolicyEntries", POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_POLICY_ENTRY_head)),
        ("nEntries", UInt32),
    ]
    return DNS_CONNECTION_POLICY_ENTRY_LIST
DNS_CONNECTION_POLICY_TAG = Int32
TAG_DNS_CONNECTION_POLICY_TAG_DEFAULT = 0
TAG_DNS_CONNECTION_POLICY_TAG_CONNECTION_MANAGER = 1
TAG_DNS_CONNECTION_POLICY_TAG_WWWPT = 2
def _define_DNS_SERVICE_INSTANCE_head():
    class DNS_SERVICE_INSTANCE(Structure):
        pass
    return DNS_SERVICE_INSTANCE
def _define_DNS_SERVICE_INSTANCE():
    DNS_SERVICE_INSTANCE = win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head
    DNS_SERVICE_INSTANCE._fields_ = [
        ("pszInstanceName", win32more.Foundation.PWSTR),
        ("pszHostName", win32more.Foundation.PWSTR),
        ("ip4Address", POINTER(UInt32)),
        ("ip6Address", POINTER(win32more.NetworkManagement.Dns.IP6_ADDRESS_head)),
        ("wPort", UInt16),
        ("wPriority", UInt16),
        ("wWeight", UInt16),
        ("dwPropertyCount", UInt32),
        ("keys", POINTER(win32more.Foundation.PWSTR)),
        ("values", POINTER(win32more.Foundation.PWSTR)),
        ("dwInterfaceIndex", UInt32),
    ]
    return DNS_SERVICE_INSTANCE
def _define_DNS_SERVICE_CANCEL_head():
    class DNS_SERVICE_CANCEL(Structure):
        pass
    return DNS_SERVICE_CANCEL
def _define_DNS_SERVICE_CANCEL():
    DNS_SERVICE_CANCEL = win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head
    DNS_SERVICE_CANCEL._fields_ = [
        ("reserved", c_void_p),
    ]
    return DNS_SERVICE_CANCEL
def _define_PDNS_SERVICE_BROWSE_CALLBACK():
    return CFUNCTYPE(Void,UInt32,c_void_p,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head), use_last_error=False)
def _define_DNS_SERVICE_BROWSE_REQUEST_head():
    class DNS_SERVICE_BROWSE_REQUEST(Structure):
        pass
    return DNS_SERVICE_BROWSE_REQUEST
def _define_DNS_SERVICE_BROWSE_REQUEST():
    DNS_SERVICE_BROWSE_REQUEST = win32more.NetworkManagement.Dns.DNS_SERVICE_BROWSE_REQUEST_head
    class DNS_SERVICE_BROWSE_REQUEST__Anonymous_e__Union(Union):
        pass
    DNS_SERVICE_BROWSE_REQUEST__Anonymous_e__Union._fields_ = [
        ("pBrowseCallback", win32more.NetworkManagement.Dns.PDNS_SERVICE_BROWSE_CALLBACK),
        ("pBrowseCallbackV2", win32more.NetworkManagement.Dns.PDNS_QUERY_COMPLETION_ROUTINE),
    ]
    DNS_SERVICE_BROWSE_REQUEST._anonymous_ = [
        'Anonymous',
    ]
    DNS_SERVICE_BROWSE_REQUEST._fields_ = [
        ("Version", UInt32),
        ("InterfaceIndex", UInt32),
        ("QueryName", win32more.Foundation.PWSTR),
        ("Anonymous", DNS_SERVICE_BROWSE_REQUEST__Anonymous_e__Union),
        ("pQueryContext", c_void_p),
    ]
    return DNS_SERVICE_BROWSE_REQUEST
def _define_PDNS_SERVICE_RESOLVE_COMPLETE():
    return CFUNCTYPE(Void,UInt32,c_void_p,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head), use_last_error=False)
def _define_DNS_SERVICE_RESOLVE_REQUEST_head():
    class DNS_SERVICE_RESOLVE_REQUEST(Structure):
        pass
    return DNS_SERVICE_RESOLVE_REQUEST
def _define_DNS_SERVICE_RESOLVE_REQUEST():
    DNS_SERVICE_RESOLVE_REQUEST = win32more.NetworkManagement.Dns.DNS_SERVICE_RESOLVE_REQUEST_head
    DNS_SERVICE_RESOLVE_REQUEST._fields_ = [
        ("Version", UInt32),
        ("InterfaceIndex", UInt32),
        ("QueryName", win32more.Foundation.PWSTR),
        ("pResolveCompletionCallback", win32more.NetworkManagement.Dns.PDNS_SERVICE_RESOLVE_COMPLETE),
        ("pQueryContext", c_void_p),
    ]
    return DNS_SERVICE_RESOLVE_REQUEST
def _define_PDNS_SERVICE_REGISTER_COMPLETE():
    return CFUNCTYPE(Void,UInt32,c_void_p,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head), use_last_error=False)
def _define_DNS_SERVICE_REGISTER_REQUEST_head():
    class DNS_SERVICE_REGISTER_REQUEST(Structure):
        pass
    return DNS_SERVICE_REGISTER_REQUEST
def _define_DNS_SERVICE_REGISTER_REQUEST():
    DNS_SERVICE_REGISTER_REQUEST = win32more.NetworkManagement.Dns.DNS_SERVICE_REGISTER_REQUEST_head
    DNS_SERVICE_REGISTER_REQUEST._fields_ = [
        ("Version", UInt32),
        ("InterfaceIndex", UInt32),
        ("pServiceInstance", POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head)),
        ("pRegisterCompletionCallback", win32more.NetworkManagement.Dns.PDNS_SERVICE_REGISTER_COMPLETE),
        ("pQueryContext", c_void_p),
        ("hCredentials", win32more.Foundation.HANDLE),
        ("unicastEnabled", win32more.Foundation.BOOL),
    ]
    return DNS_SERVICE_REGISTER_REQUEST
def _define_MDNS_QUERY_HANDLE_head():
    class MDNS_QUERY_HANDLE(Structure):
        pass
    return MDNS_QUERY_HANDLE
def _define_MDNS_QUERY_HANDLE():
    MDNS_QUERY_HANDLE = win32more.NetworkManagement.Dns.MDNS_QUERY_HANDLE_head
    MDNS_QUERY_HANDLE._fields_ = [
        ("nameBuf", Char * 256),
        ("wType", UInt16),
        ("pSubscription", c_void_p),
        ("pWnfCallbackParams", c_void_p),
        ("stateNameData", UInt32 * 2),
    ]
    return MDNS_QUERY_HANDLE
def _define_PMDNS_QUERY_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.Dns.MDNS_QUERY_HANDLE_head),POINTER(win32more.NetworkManagement.Dns.DNS_QUERY_RESULT_head), use_last_error=False)
def _define_MDNS_QUERY_REQUEST_head():
    class MDNS_QUERY_REQUEST(Structure):
        pass
    return MDNS_QUERY_REQUEST
def _define_MDNS_QUERY_REQUEST():
    MDNS_QUERY_REQUEST = win32more.NetworkManagement.Dns.MDNS_QUERY_REQUEST_head
    MDNS_QUERY_REQUEST._fields_ = [
        ("Version", UInt32),
        ("ulRefCount", UInt32),
        ("Query", win32more.Foundation.PWSTR),
        ("QueryType", UInt16),
        ("QueryOptions", UInt64),
        ("InterfaceIndex", UInt32),
        ("pQueryCallback", win32more.NetworkManagement.Dns.PMDNS_QUERY_CALLBACK),
        ("pQueryContext", c_void_p),
        ("fAnswerReceived", win32more.Foundation.BOOL),
        ("ulResendCount", UInt32),
    ]
    return MDNS_QUERY_REQUEST
def _define_DnsQueryConfig():
    try:
        return WINFUNCTYPE(Int32,win32more.NetworkManagement.Dns.DNS_CONFIG_TYPE,UInt32,win32more.Foundation.PWSTR,c_void_p,c_void_p,POINTER(UInt32), use_last_error=False)(("DnsQueryConfig", windll["DNSAPI"]), ((1, 'Config'),(1, 'Flag'),(1, 'pwsAdapterName'),(1, 'pReserved'),(1, 'pBuffer'),(1, 'pBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsRecordCopyEx():
    try:
        return WINFUNCTYPE(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),win32more.NetworkManagement.Dns.DNS_CHARSET,win32more.NetworkManagement.Dns.DNS_CHARSET, use_last_error=False)(("DnsRecordCopyEx", windll["DNSAPI"]), ((1, 'pRecord'),(1, 'CharSetIn'),(1, 'CharSetOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsRecordSetCopyEx():
    try:
        return WINFUNCTYPE(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),win32more.NetworkManagement.Dns.DNS_CHARSET,win32more.NetworkManagement.Dns.DNS_CHARSET, use_last_error=False)(("DnsRecordSetCopyEx", windll["DNSAPI"]), ((1, 'pRecordSet'),(1, 'CharSetIn'),(1, 'CharSetOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsRecordCompare():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head), use_last_error=False)(("DnsRecordCompare", windll["DNSAPI"]), ((1, 'pRecord1'),(1, 'pRecord2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsRecordSetCompare():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)), use_last_error=False)(("DnsRecordSetCompare", windll["DNSAPI"]), ((1, 'pRR1'),(1, 'pRR2'),(1, 'ppDiff1'),(1, 'ppDiff2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsRecordSetDetach():
    try:
        return WINFUNCTYPE(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head), use_last_error=False)(("DnsRecordSetDetach", windll["DNSAPI"]), ((1, 'pRecordList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsFree():
    try:
        return WINFUNCTYPE(Void,c_void_p,win32more.NetworkManagement.Dns.DNS_FREE_TYPE, use_last_error=False)(("DnsFree", windll["DNSAPI"]), ((1, 'pData'),(1, 'FreeType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsQuery_A():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,UInt16,UInt32,c_void_p,POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),POINTER(c_void_p), use_last_error=False)(("DnsQuery_A", windll["DNSAPI"]), ((1, 'pszName'),(1, 'wType'),(1, 'Options'),(1, 'pExtra'),(1, 'ppQueryResults'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsQuery_UTF8():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,UInt16,UInt32,c_void_p,POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),POINTER(c_void_p), use_last_error=False)(("DnsQuery_UTF8", windll["DNSAPI"]), ((1, 'pszName'),(1, 'wType'),(1, 'Options'),(1, 'pExtra'),(1, 'ppQueryResults'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsQuery_W():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,UInt16,UInt32,c_void_p,POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)),POINTER(c_void_p), use_last_error=False)(("DnsQuery_W", windll["DNSAPI"]), ((1, 'pszName'),(1, 'wType'),(1, 'Options'),(1, 'pExtra'),(1, 'ppQueryResults'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsQuery_():
    return win32more.NetworkManagement.Dns.DnsQuery_W
def _define_DnsQueryEx():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_QUERY_REQUEST_head),POINTER(win32more.NetworkManagement.Dns.DNS_QUERY_RESULT_head),POINTER(win32more.NetworkManagement.Dns.DNS_QUERY_CANCEL_head), use_last_error=False)(("DnsQueryEx", windll["DNSAPI"]), ((1, 'pQueryRequest'),(1, 'pQueryResults'),(1, 'pCancelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsCancelQuery():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_QUERY_CANCEL_head), use_last_error=False)(("DnsCancelQuery", windll["DNSAPI"]), ((1, 'pCancelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsFreeCustomServers():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head)), use_last_error=False)(("DnsFreeCustomServers", windll["DNSAPI"]), ((1, 'pcServers'),(1, 'ppServers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsGetApplicationSettings():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_CUSTOM_SERVER_head)),POINTER(win32more.NetworkManagement.Dns.DNS_APPLICATION_SETTINGS_head), use_last_error=False)(("DnsGetApplicationSettings", windll["DNSAPI"]), ((1, 'pcServers'),(1, 'ppDefaultServers'),(1, 'pSettings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsSetApplicationSettings():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.NetworkManagement.Dns.DNS_CUSTOM_SERVER),POINTER(win32more.NetworkManagement.Dns.DNS_APPLICATION_SETTINGS_head), use_last_error=False)(("DnsSetApplicationSettings", windll["DNSAPI"]), ((1, 'cServers'),(1, 'pServers'),(1, 'pSettings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsAcquireContextHandle_W():
    try:
        return WINFUNCTYPE(Int32,UInt32,c_void_p,POINTER(win32more.NetworkManagement.Dns.DnsContextHandle), use_last_error=False)(("DnsAcquireContextHandle_W", windll["DNSAPI"]), ((1, 'CredentialFlags'),(1, 'Credentials'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsAcquireContextHandle_():
    return win32more.NetworkManagement.Dns.DnsAcquireContextHandle_W
def _define_DnsAcquireContextHandle_A():
    try:
        return WINFUNCTYPE(Int32,UInt32,c_void_p,POINTER(win32more.NetworkManagement.Dns.DnsContextHandle), use_last_error=False)(("DnsAcquireContextHandle_A", windll["DNSAPI"]), ((1, 'CredentialFlags'),(1, 'Credentials'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsReleaseContextHandle():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE, use_last_error=False)(("DnsReleaseContextHandle", windll["DNSAPI"]), ((1, 'hContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsModifyRecordsInSet_W():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),UInt32,win32more.Foundation.HANDLE,c_void_p,c_void_p, use_last_error=False)(("DnsModifyRecordsInSet_W", windll["DNSAPI"]), ((1, 'pAddRecords'),(1, 'pDeleteRecords'),(1, 'Options'),(1, 'hCredentials'),(1, 'pExtraList'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsModifyRecordsInSet_():
    return win32more.NetworkManagement.Dns.DnsModifyRecordsInSet_W
def _define_DnsModifyRecordsInSet_A():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),UInt32,win32more.Foundation.HANDLE,c_void_p,c_void_p, use_last_error=False)(("DnsModifyRecordsInSet_A", windll["DNSAPI"]), ((1, 'pAddRecords'),(1, 'pDeleteRecords'),(1, 'Options'),(1, 'hCredentials'),(1, 'pExtraList'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsModifyRecordsInSet_UTF8():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),UInt32,win32more.Foundation.HANDLE,c_void_p,c_void_p, use_last_error=False)(("DnsModifyRecordsInSet_UTF8", windll["DNSAPI"]), ((1, 'pAddRecords'),(1, 'pDeleteRecords'),(1, 'Options'),(1, 'hCredentials'),(1, 'pExtraList'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsReplaceRecordSetW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),UInt32,win32more.Foundation.HANDLE,c_void_p,c_void_p, use_last_error=False)(("DnsReplaceRecordSetW", windll["DNSAPI"]), ((1, 'pReplaceSet'),(1, 'Options'),(1, 'hContext'),(1, 'pExtraInfo'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsReplaceRecordSet():
    return win32more.NetworkManagement.Dns.DnsReplaceRecordSetW
def _define_DnsReplaceRecordSetA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),UInt32,win32more.Foundation.HANDLE,c_void_p,c_void_p, use_last_error=False)(("DnsReplaceRecordSetA", windll["DNSAPI"]), ((1, 'pReplaceSet'),(1, 'Options'),(1, 'hContext'),(1, 'pExtraInfo'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsReplaceRecordSetUTF8():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head),UInt32,win32more.Foundation.HANDLE,c_void_p,c_void_p, use_last_error=False)(("DnsReplaceRecordSetUTF8", windll["DNSAPI"]), ((1, 'pReplaceSet'),(1, 'Options'),(1, 'hContext'),(1, 'pExtraInfo'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsValidateName_W():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dns.DNS_NAME_FORMAT, use_last_error=False)(("DnsValidateName_W", windll["DNSAPI"]), ((1, 'pszName'),(1, 'Format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsValidateName_():
    return win32more.NetworkManagement.Dns.DnsValidateName_W
def _define_DnsValidateName_A():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.NetworkManagement.Dns.DNS_NAME_FORMAT, use_last_error=False)(("DnsValidateName_A", windll["DNSAPI"]), ((1, 'pszName'),(1, 'Format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsValidateName_UTF8():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.NetworkManagement.Dns.DNS_NAME_FORMAT, use_last_error=False)(("DnsValidateName_UTF8", windll["DNSAPI"]), ((1, 'pszName'),(1, 'Format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsNameCompare_A():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("DnsNameCompare_A", windll["DNSAPI"]), ((1, 'pName1'),(1, 'pName2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsNameCompare_W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DnsNameCompare_W", windll["DNSAPI"]), ((1, 'pName1'),(1, 'pName2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsNameCompare_():
    return win32more.NetworkManagement.Dns.DnsNameCompare_W
def _define_DnsWriteQuestionToBuffer_W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head),POINTER(UInt32),win32more.Foundation.PWSTR,UInt16,UInt16,win32more.Foundation.BOOL, use_last_error=False)(("DnsWriteQuestionToBuffer_W", windll["DNSAPI"]), ((1, 'pDnsBuffer'),(1, 'pdwBufferSize'),(1, 'pszName'),(1, 'wType'),(1, 'Xid'),(1, 'fRecursionDesired'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsWriteQuestionToBuffer_UTF8():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head),POINTER(UInt32),win32more.Foundation.PSTR,UInt16,UInt16,win32more.Foundation.BOOL, use_last_error=False)(("DnsWriteQuestionToBuffer_UTF8", windll["DNSAPI"]), ((1, 'pDnsBuffer'),(1, 'pdwBufferSize'),(1, 'pszName'),(1, 'wType'),(1, 'Xid'),(1, 'fRecursionDesired'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsExtractRecordsFromMessage_W():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head),UInt16,POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)), use_last_error=False)(("DnsExtractRecordsFromMessage_W", windll["DNSAPI"]), ((1, 'pDnsBuffer'),(1, 'wMessageLength'),(1, 'ppRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsExtractRecordsFromMessage_UTF8():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_MESSAGE_BUFFER_head),UInt16,POINTER(POINTER(win32more.NetworkManagement.Dns.DNS_RECORDA_head)), use_last_error=False)(("DnsExtractRecordsFromMessage_UTF8", windll["DNSAPI"]), ((1, 'pDnsBuffer'),(1, 'wMessageLength'),(1, 'ppRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsGetProxyInformation():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dns.DNS_PROXY_INFORMATION_head),POINTER(win32more.NetworkManagement.Dns.DNS_PROXY_INFORMATION_head),win32more.NetworkManagement.Dns.DNS_PROXY_COMPLETION_ROUTINE,c_void_p, use_last_error=False)(("DnsGetProxyInformation", windll["DNSAPI"]), ((1, 'hostName'),(1, 'proxyInformation'),(1, 'defaultProxyInformation'),(1, 'completionRoutine'),(1, 'completionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsFreeProxyName():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PWSTR, use_last_error=False)(("DnsFreeProxyName", windll["DNSAPI"]), ((1, 'proxyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionGetProxyInfoForHostUrl():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Byte),UInt32,UInt32,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_EX_head), use_last_error=False)(("DnsConnectionGetProxyInfoForHostUrl", windll["DNSAPI"]), ((1, 'pwszHostUrl'),(1, 'pSelectionContext'),(1, 'dwSelectionContextLength'),(1, 'dwExplicitInterfaceIndex'),(1, 'pProxyInfoEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionFreeProxyInfoEx():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_EX_head), use_last_error=False)(("DnsConnectionFreeProxyInfoEx", windll["DNSAPI"]), ((1, 'pProxyInfoEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionGetProxyInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_head), use_last_error=False)(("DnsConnectionGetProxyInfo", windll["DNSAPI"]), ((1, 'pwszConnectionName'),(1, 'Type'),(1, 'pProxyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionFreeProxyInfo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_head), use_last_error=False)(("DnsConnectionFreeProxyInfo", windll["DNSAPI"]), ((1, 'pProxyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionSetProxyInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_INFO_head), use_last_error=False)(("DnsConnectionSetProxyInfo", windll["DNSAPI"]), ((1, 'pwszConnectionName'),(1, 'Type'),(1, 'pProxyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionDeleteProxyInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_TYPE, use_last_error=False)(("DnsConnectionDeleteProxyInfo", windll["DNSAPI"]), ((1, 'pwszConnectionName'),(1, 'Type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionGetProxyList():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_LIST_head), use_last_error=False)(("DnsConnectionGetProxyList", windll["DNSAPI"]), ((1, 'pwszConnectionName'),(1, 'pProxyList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionFreeProxyList():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_PROXY_LIST_head), use_last_error=False)(("DnsConnectionFreeProxyList", windll["DNSAPI"]), ((1, 'pProxyList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionGetNameList():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_NAME_LIST_head), use_last_error=False)(("DnsConnectionGetNameList", windll["DNSAPI"]), ((1, 'pNameList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionFreeNameList():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_NAME_LIST_head), use_last_error=False)(("DnsConnectionFreeNameList", windll["DNSAPI"]), ((1, 'pNameList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionUpdateIfIndexTable():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_IFINDEX_LIST_head), use_last_error=False)(("DnsConnectionUpdateIfIndexTable", windll["DNSAPI"]), ((1, 'pConnectionIfIndexEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionSetPolicyEntries():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Dns.DNS_CONNECTION_POLICY_TAG,POINTER(win32more.NetworkManagement.Dns.DNS_CONNECTION_POLICY_ENTRY_LIST_head), use_last_error=False)(("DnsConnectionSetPolicyEntries", windll["DNSAPI"]), ((1, 'PolicyEntryTag'),(1, 'pPolicyEntryList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsConnectionDeletePolicyEntries():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Dns.DNS_CONNECTION_POLICY_TAG, use_last_error=False)(("DnsConnectionDeletePolicyEntries", windll["DNSAPI"]), ((1, 'PolicyEntryTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceConstructInstance():
    try:
        return WINFUNCTYPE(POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.NetworkManagement.Dns.IP6_ADDRESS_head),UInt16,UInt16,UInt16,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("DnsServiceConstructInstance", windll["DNSAPI"]), ((1, 'pServiceName'),(1, 'pHostName'),(1, 'pIp4'),(1, 'pIp6'),(1, 'wPort'),(1, 'wPriority'),(1, 'wWeight'),(1, 'dwPropertiesCount'),(1, 'keys'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceCopyInstance():
    try:
        return WINFUNCTYPE(POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head),POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head), use_last_error=False)(("DnsServiceCopyInstance", windll["DNSAPI"]), ((1, 'pOrig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceFreeInstance():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_INSTANCE_head), use_last_error=False)(("DnsServiceFreeInstance", windll["DNSAPI"]), ((1, 'pInstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceBrowse():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_BROWSE_REQUEST_head),POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head), use_last_error=True)(("DnsServiceBrowse", windll["DNSAPI"]), ((1, 'pRequest'),(1, 'pCancel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceBrowseCancel():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head), use_last_error=True)(("DnsServiceBrowseCancel", windll["DNSAPI"]), ((1, 'pCancelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceResolve():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_RESOLVE_REQUEST_head),POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head), use_last_error=True)(("DnsServiceResolve", windll["DNSAPI"]), ((1, 'pRequest'),(1, 'pCancel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceResolveCancel():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head), use_last_error=True)(("DnsServiceResolveCancel", windll["DNSAPI"]), ((1, 'pCancelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceRegister():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_REGISTER_REQUEST_head),POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head), use_last_error=True)(("DnsServiceRegister", windll["DNSAPI"]), ((1, 'pRequest'),(1, 'pCancel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceDeRegister():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_REGISTER_REQUEST_head),POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head), use_last_error=True)(("DnsServiceDeRegister", windll["DNSAPI"]), ((1, 'pRequest'),(1, 'pCancel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsServiceRegisterCancel():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Dns.DNS_SERVICE_CANCEL_head), use_last_error=False)(("DnsServiceRegisterCancel", windll["DNSAPI"]), ((1, 'pCancelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsStartMulticastQuery():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.MDNS_QUERY_REQUEST_head),POINTER(win32more.NetworkManagement.Dns.MDNS_QUERY_HANDLE_head), use_last_error=True)(("DnsStartMulticastQuery", windll["DNSAPI"]), ((1, 'pQueryRequest'),(1, 'pHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DnsStopMulticastQuery():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Dns.MDNS_QUERY_HANDLE_head), use_last_error=True)(("DnsStopMulticastQuery", windll["DNSAPI"]), ((1, 'pHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "SIZEOF_IP4_ADDRESS",
    "IP4_ADDRESS_STRING_LENGTH",
    "IP4_ADDRESS_STRING_BUFFER_LENGTH",
    "DNS_ADDR_MAX_SOCKADDR_LENGTH",
    "IP6_ADDRESS_STRING_LENGTH",
    "IP6_ADDRESS_STRING_BUFFER_LENGTH",
    "DNS_ADDRESS_STRING_LENGTH",
    "DNS_PORT_HOST_ORDER",
    "DNS_PORT_NET_ORDER",
    "DNS_RFC_MAX_UDP_PACKET_LENGTH",
    "DNS_MAX_NAME_LENGTH",
    "DNS_MAX_LABEL_LENGTH",
    "DNS_MAX_NAME_BUFFER_LENGTH",
    "DNS_MAX_LABEL_BUFFER_LENGTH",
    "DNS_MAX_IP4_REVERSE_NAME_LENGTH",
    "DNS_MAX_IP6_REVERSE_NAME_LENGTH",
    "DNS_MAX_REVERSE_NAME_LENGTH",
    "DNS_MAX_IP4_REVERSE_NAME_BUFFER_LENGTH",
    "DNS_MAX_IP6_REVERSE_NAME_BUFFER_LENGTH",
    "DNS_MAX_REVERSE_NAME_BUFFER_LENGTH",
    "DNS_MAX_TEXT_STRING_LENGTH",
    "DNS_COMPRESSED_QUESTION_NAME",
    "DNS_OPCODE_QUERY",
    "DNS_OPCODE_IQUERY",
    "DNS_OPCODE_SERVER_STATUS",
    "DNS_OPCODE_UNKNOWN",
    "DNS_OPCODE_NOTIFY",
    "DNS_OPCODE_UPDATE",
    "DNS_RCODE_NOERROR",
    "DNS_RCODE_FORMERR",
    "DNS_RCODE_SERVFAIL",
    "DNS_RCODE_NXDOMAIN",
    "DNS_RCODE_NOTIMPL",
    "DNS_RCODE_REFUSED",
    "DNS_RCODE_YXDOMAIN",
    "DNS_RCODE_YXRRSET",
    "DNS_RCODE_NXRRSET",
    "DNS_RCODE_NOTAUTH",
    "DNS_RCODE_NOTZONE",
    "DNS_RCODE_MAX",
    "DNS_RCODE_BADVERS",
    "DNS_RCODE_BADSIG",
    "DNS_RCODE_BADKEY",
    "DNS_RCODE_BADTIME",
    "DNS_RCODE_NO_ERROR",
    "DNS_RCODE_FORMAT_ERROR",
    "DNS_RCODE_SERVER_FAILURE",
    "DNS_RCODE_NAME_ERROR",
    "DNS_RCODE_NOT_IMPLEMENTED",
    "DNS_CLASS_INTERNET",
    "DNS_CLASS_CSNET",
    "DNS_CLASS_CHAOS",
    "DNS_CLASS_HESIOD",
    "DNS_CLASS_NONE",
    "DNS_CLASS_ALL",
    "DNS_CLASS_ANY",
    "DNS_CLASS_UNICAST_RESPONSE",
    "DNS_RCLASS_INTERNET",
    "DNS_RCLASS_CSNET",
    "DNS_RCLASS_CHAOS",
    "DNS_RCLASS_HESIOD",
    "DNS_RCLASS_NONE",
    "DNS_RCLASS_ALL",
    "DNS_RCLASS_ANY",
    "DNS_RCLASS_UNICAST_RESPONSE",
    "DNS_TYPE_ZERO",
    "DNS_TYPE_A",
    "DNS_TYPE_NS",
    "DNS_TYPE_MD",
    "DNS_TYPE_MF",
    "DNS_TYPE_CNAME",
    "DNS_TYPE_SOA",
    "DNS_TYPE_MB",
    "DNS_TYPE_MG",
    "DNS_TYPE_MR",
    "DNS_TYPE_NULL",
    "DNS_TYPE_WKS",
    "DNS_TYPE_PTR",
    "DNS_TYPE_HINFO",
    "DNS_TYPE_MINFO",
    "DNS_TYPE_MX",
    "DNS_TYPE_TEXT",
    "DNS_TYPE_RP",
    "DNS_TYPE_AFSDB",
    "DNS_TYPE_X25",
    "DNS_TYPE_ISDN",
    "DNS_TYPE_RT",
    "DNS_TYPE_NSAP",
    "DNS_TYPE_NSAPPTR",
    "DNS_TYPE_SIG",
    "DNS_TYPE_KEY",
    "DNS_TYPE_PX",
    "DNS_TYPE_GPOS",
    "DNS_TYPE_AAAA",
    "DNS_TYPE_LOC",
    "DNS_TYPE_NXT",
    "DNS_TYPE_EID",
    "DNS_TYPE_NIMLOC",
    "DNS_TYPE_SRV",
    "DNS_TYPE_ATMA",
    "DNS_TYPE_NAPTR",
    "DNS_TYPE_KX",
    "DNS_TYPE_CERT",
    "DNS_TYPE_A6",
    "DNS_TYPE_DNAME",
    "DNS_TYPE_SINK",
    "DNS_TYPE_OPT",
    "DNS_TYPE_DS",
    "DNS_TYPE_RRSIG",
    "DNS_TYPE_NSEC",
    "DNS_TYPE_DNSKEY",
    "DNS_TYPE_DHCID",
    "DNS_TYPE_NSEC3",
    "DNS_TYPE_NSEC3PARAM",
    "DNS_TYPE_TLSA",
    "DNS_TYPE_UINFO",
    "DNS_TYPE_UID",
    "DNS_TYPE_GID",
    "DNS_TYPE_UNSPEC",
    "DNS_TYPE_ADDRS",
    "DNS_TYPE_TKEY",
    "DNS_TYPE_TSIG",
    "DNS_TYPE_IXFR",
    "DNS_TYPE_AXFR",
    "DNS_TYPE_MAILB",
    "DNS_TYPE_MAILA",
    "DNS_TYPE_ALL",
    "DNS_TYPE_ANY",
    "DNS_TYPE_WINS",
    "DNS_TYPE_WINSR",
    "DNS_TYPE_NBSTAT",
    "DNS_RTYPE_A",
    "DNS_RTYPE_NS",
    "DNS_RTYPE_MD",
    "DNS_RTYPE_MF",
    "DNS_RTYPE_CNAME",
    "DNS_RTYPE_SOA",
    "DNS_RTYPE_MB",
    "DNS_RTYPE_MG",
    "DNS_RTYPE_MR",
    "DNS_RTYPE_NULL",
    "DNS_RTYPE_WKS",
    "DNS_RTYPE_PTR",
    "DNS_RTYPE_HINFO",
    "DNS_RTYPE_MINFO",
    "DNS_RTYPE_MX",
    "DNS_RTYPE_TEXT",
    "DNS_RTYPE_RP",
    "DNS_RTYPE_AFSDB",
    "DNS_RTYPE_X25",
    "DNS_RTYPE_ISDN",
    "DNS_RTYPE_RT",
    "DNS_RTYPE_NSAP",
    "DNS_RTYPE_NSAPPTR",
    "DNS_RTYPE_SIG",
    "DNS_RTYPE_KEY",
    "DNS_RTYPE_PX",
    "DNS_RTYPE_GPOS",
    "DNS_RTYPE_AAAA",
    "DNS_RTYPE_LOC",
    "DNS_RTYPE_NXT",
    "DNS_RTYPE_EID",
    "DNS_RTYPE_NIMLOC",
    "DNS_RTYPE_SRV",
    "DNS_RTYPE_ATMA",
    "DNS_RTYPE_NAPTR",
    "DNS_RTYPE_KX",
    "DNS_RTYPE_CERT",
    "DNS_RTYPE_A6",
    "DNS_RTYPE_DNAME",
    "DNS_RTYPE_SINK",
    "DNS_RTYPE_OPT",
    "DNS_RTYPE_DS",
    "DNS_RTYPE_RRSIG",
    "DNS_RTYPE_NSEC",
    "DNS_RTYPE_DNSKEY",
    "DNS_RTYPE_DHCID",
    "DNS_RTYPE_NSEC3",
    "DNS_RTYPE_NSEC3PARAM",
    "DNS_RTYPE_TLSA",
    "DNS_RTYPE_UINFO",
    "DNS_RTYPE_UID",
    "DNS_RTYPE_GID",
    "DNS_RTYPE_UNSPEC",
    "DNS_RTYPE_TKEY",
    "DNS_RTYPE_TSIG",
    "DNS_RTYPE_IXFR",
    "DNS_RTYPE_AXFR",
    "DNS_RTYPE_MAILB",
    "DNS_RTYPE_MAILA",
    "DNS_RTYPE_ALL",
    "DNS_RTYPE_ANY",
    "DNS_RTYPE_WINS",
    "DNS_RTYPE_WINSR",
    "DNS_ATMA_FORMAT_E164",
    "DNS_ATMA_FORMAT_AESA",
    "DNS_ATMA_MAX_ADDR_LENGTH",
    "DNS_ATMA_AESA_ADDR_LENGTH",
    "DNS_ATMA_MAX_RECORD_LENGTH",
    "DNSSEC_ALGORITHM_RSAMD5",
    "DNSSEC_ALGORITHM_RSASHA1",
    "DNSSEC_ALGORITHM_RSASHA1_NSEC3",
    "DNSSEC_ALGORITHM_RSASHA256",
    "DNSSEC_ALGORITHM_RSASHA512",
    "DNSSEC_ALGORITHM_ECDSAP256_SHA256",
    "DNSSEC_ALGORITHM_ECDSAP384_SHA384",
    "DNSSEC_ALGORITHM_NULL",
    "DNSSEC_ALGORITHM_PRIVATE",
    "DNSSEC_DIGEST_ALGORITHM_SHA1",
    "DNSSEC_DIGEST_ALGORITHM_SHA256",
    "DNSSEC_DIGEST_ALGORITHM_SHA384",
    "DNSSEC_PROTOCOL_NONE",
    "DNSSEC_PROTOCOL_TLS",
    "DNSSEC_PROTOCOL_EMAIL",
    "DNSSEC_PROTOCOL_DNSSEC",
    "DNSSEC_PROTOCOL_IPSEC",
    "DNSSEC_KEY_FLAG_NOAUTH",
    "DNSSEC_KEY_FLAG_NOCONF",
    "DNSSEC_KEY_FLAG_FLAG2",
    "DNSSEC_KEY_FLAG_EXTEND",
    "DNSSEC_KEY_FLAG_FLAG4",
    "DNSSEC_KEY_FLAG_FLAG5",
    "DNSSEC_KEY_FLAG_USER",
    "DNSSEC_KEY_FLAG_ZONE",
    "DNSSEC_KEY_FLAG_HOST",
    "DNSSEC_KEY_FLAG_NTPE3",
    "DNSSEC_KEY_FLAG_FLAG8",
    "DNSSEC_KEY_FLAG_FLAG9",
    "DNSSEC_KEY_FLAG_FLAG10",
    "DNSSEC_KEY_FLAG_FLAG11",
    "DNSSEC_KEY_FLAG_SIG0",
    "DNSSEC_KEY_FLAG_SIG1",
    "DNSSEC_KEY_FLAG_SIG2",
    "DNSSEC_KEY_FLAG_SIG3",
    "DNSSEC_KEY_FLAG_SIG4",
    "DNSSEC_KEY_FLAG_SIG5",
    "DNSSEC_KEY_FLAG_SIG6",
    "DNSSEC_KEY_FLAG_SIG7",
    "DNSSEC_KEY_FLAG_SIG8",
    "DNSSEC_KEY_FLAG_SIG9",
    "DNSSEC_KEY_FLAG_SIG10",
    "DNSSEC_KEY_FLAG_SIG11",
    "DNSSEC_KEY_FLAG_SIG12",
    "DNSSEC_KEY_FLAG_SIG13",
    "DNSSEC_KEY_FLAG_SIG14",
    "DNSSEC_KEY_FLAG_SIG15",
    "DNS_TKEY_MODE_SERVER_ASSIGN",
    "DNS_TKEY_MODE_DIFFIE_HELLMAN",
    "DNS_TKEY_MODE_GSS",
    "DNS_TKEY_MODE_RESOLVER_ASSIGN",
    "DNS_WINS_FLAG_SCOPE",
    "DNS_WINS_FLAG_LOCAL",
    "DNS_CONFIG_FLAG_ALLOC",
    "DNSREC_SECTION",
    "DNSREC_QUESTION",
    "DNSREC_ANSWER",
    "DNSREC_AUTHORITY",
    "DNSREC_ADDITIONAL",
    "DNSREC_ZONE",
    "DNSREC_PREREQ",
    "DNSREC_UPDATE",
    "DNSREC_DELETE",
    "DNSREC_NOEXIST",
    "DNS_QUERY_STANDARD",
    "DNS_QUERY_ACCEPT_TRUNCATED_RESPONSE",
    "DNS_QUERY_USE_TCP_ONLY",
    "DNS_QUERY_NO_RECURSION",
    "DNS_QUERY_BYPASS_CACHE",
    "DNS_QUERY_NO_WIRE_QUERY",
    "DNS_QUERY_NO_LOCAL_NAME",
    "DNS_QUERY_NO_HOSTS_FILE",
    "DNS_QUERY_NO_NETBT",
    "DNS_QUERY_WIRE_ONLY",
    "DNS_QUERY_RETURN_MESSAGE",
    "DNS_QUERY_MULTICAST_ONLY",
    "DNS_QUERY_NO_MULTICAST",
    "DNS_QUERY_TREAT_AS_FQDN",
    "DNS_QUERY_ADDRCONFIG",
    "DNS_QUERY_DUAL_ADDR",
    "DNS_QUERY_DONT_RESET_TTL_VALUES",
    "DNS_QUERY_DISABLE_IDN_ENCODING",
    "DNS_QUERY_APPEND_MULTILABEL",
    "DNS_QUERY_DNSSEC_OK",
    "DNS_QUERY_DNSSEC_CHECKING_DISABLED",
    "DNS_QUERY_RESERVED",
    "DNS_QUERY_CACHE_ONLY",
    "DNS_QUERY_REQUEST_VERSION1",
    "DNS_QUERY_REQUEST_VERSION2",
    "DNS_QUERY_RESULTS_VERSION1",
    "DNS_QUERY_REQUEST_VERSION3",
    "DNS_CUSTOM_SERVER_TYPE_UDP",
    "DNS_CUSTOM_SERVER_TYPE_DOH",
    "DNS_CUSTOM_SERVER_UDP_FALLBACK",
    "DNS_APP_SETTINGS_VERSION1",
    "DNS_APP_SETTINGS_EXCLUSIVE_SERVERS",
    "DNS_UPDATE_SECURITY_USE_DEFAULT",
    "DNS_UPDATE_SECURITY_OFF",
    "DNS_UPDATE_SECURITY_ON",
    "DNS_UPDATE_SECURITY_ONLY",
    "DNS_UPDATE_CACHE_SECURITY_CONTEXT",
    "DNS_UPDATE_TEST_USE_LOCAL_SYS_ACCT",
    "DNS_UPDATE_FORCE_SECURITY_NEGO",
    "DNS_UPDATE_TRY_ALL_MASTER_SERVERS",
    "DNS_UPDATE_SKIP_NO_UPDATE_ADAPTERS",
    "DNS_UPDATE_REMOTE_SERVER",
    "DNS_UPDATE_RESERVED",
    "DNS_VALSVR_ERROR_INVALID_ADDR",
    "DNS_VALSVR_ERROR_INVALID_NAME",
    "DNS_VALSVR_ERROR_UNREACHABLE",
    "DNS_VALSVR_ERROR_NO_RESPONSE",
    "DNS_VALSVR_ERROR_NO_AUTH",
    "DNS_VALSVR_ERROR_REFUSED",
    "DNS_VALSVR_ERROR_NO_TCP",
    "DNS_VALSVR_ERROR_UNKNOWN",
    "DNS_CONNECTION_NAME_MAX_LENGTH",
    "DNS_CONNECTION_PROXY_INFO_CURRENT_VERSION",
    "DNS_CONNECTION_PROXY_INFO_SERVER_MAX_LENGTH",
    "DNS_CONNECTION_PROXY_INFO_FRIENDLY_NAME_MAX_LENGTH",
    "DNS_CONNECTION_PROXY_INFO_USERNAME_MAX_LENGTH",
    "DNS_CONNECTION_PROXY_INFO_PASSWORD_MAX_LENGTH",
    "DNS_CONNECTION_PROXY_INFO_EXCEPTION_MAX_LENGTH",
    "DNS_CONNECTION_PROXY_INFO_EXTRA_INFO_MAX_LENGTH",
    "DNS_CONNECTION_PROXY_INFO_FLAG_DISABLED",
    "DNS_CONNECTION_PROXY_INFO_FLAG_BYPASSLOCAL",
    "DNS_CONNECTION_POLICY_ENTRY_ONDEMAND",
    "DnsContextHandle",
    "IP4_ARRAY",
    "IP6_ADDRESS",
    "DNS_ADDR",
    "DNS_ADDR_ARRAY",
    "DNS_HEADER",
    "DNS_HEADER_EXT",
    "DNS_WIRE_QUESTION",
    "DNS_WIRE_RECORD",
    "DNS_CONFIG_TYPE",
    "DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_W",
    "DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_A",
    "DNS_CONFIG_TYPE_DnsConfigPrimaryDomainName_UTF8",
    "DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_W",
    "DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_A",
    "DNS_CONFIG_TYPE_DnsConfigAdapterDomainName_UTF8",
    "DNS_CONFIG_TYPE_DnsConfigDnsServerList",
    "DNS_CONFIG_TYPE_DnsConfigSearchList",
    "DNS_CONFIG_TYPE_DnsConfigAdapterInfo",
    "DNS_CONFIG_TYPE_DnsConfigPrimaryHostNameRegistrationEnabled",
    "DNS_CONFIG_TYPE_DnsConfigAdapterHostNameRegistrationEnabled",
    "DNS_CONFIG_TYPE_DnsConfigAddressRegistrationMaxCount",
    "DNS_CONFIG_TYPE_DnsConfigHostName_W",
    "DNS_CONFIG_TYPE_DnsConfigHostName_A",
    "DNS_CONFIG_TYPE_DnsConfigHostName_UTF8",
    "DNS_CONFIG_TYPE_DnsConfigFullHostName_W",
    "DNS_CONFIG_TYPE_DnsConfigFullHostName_A",
    "DNS_CONFIG_TYPE_DnsConfigFullHostName_UTF8",
    "DNS_CONFIG_TYPE_DnsConfigNameServer",
    "DNS_A_DATA",
    "DNS_PTR_DATAW",
    "DNS_PTR_DATAA",
    "DNS_SOA_DATAW",
    "DNS_SOA_DATAA",
    "DNS_MINFO_DATAW",
    "DNS_MINFO_DATAA",
    "DNS_MX_DATAW",
    "DNS_MX_DATAA",
    "DNS_TXT_DATAW",
    "DNS_TXT_DATAA",
    "DNS_NULL_DATA",
    "DNS_WKS_DATA",
    "DNS_AAAA_DATA",
    "DNS_SIG_DATAW",
    "DNS_SIG_DATAA",
    "DNS_KEY_DATA",
    "DNS_DHCID_DATA",
    "DNS_NSEC_DATAW",
    "DNS_NSEC_DATAA",
    "DNS_NSEC3_DATA",
    "DNS_NSEC3PARAM_DATA",
    "DNS_TLSA_DATA",
    "DNS_DS_DATA",
    "DNS_OPT_DATA",
    "DNS_LOC_DATA",
    "DNS_NXT_DATAW",
    "DNS_NXT_DATAA",
    "DNS_SRV_DATAW",
    "DNS_SRV_DATAA",
    "DNS_NAPTR_DATAW",
    "DNS_NAPTR_DATAA",
    "DNS_ATMA_DATA",
    "DNS_TKEY_DATAW",
    "DNS_TKEY_DATAA",
    "DNS_TSIG_DATAW",
    "DNS_TSIG_DATAA",
    "DNS_UNKNOWN_DATA",
    "DNS_WINS_DATA",
    "DNS_WINSR_DATAW",
    "DNS_WINSR_DATAA",
    "DNS_RECORD_FLAGS",
    "DNS_SECTION",
    "DNS_SECTION_DnsSectionQuestion",
    "DNS_SECTION_DnsSectionAnswer",
    "DNS_SECTION_DnsSectionAuthority",
    "DNS_SECTION_DnsSectionAddtional",
    "DNS_RECORDW",
    "_DnsRecordOptW",
    "DNS_RECORDA",
    "_DnsRecordOptA",
    "DNS_RRSET",
    "DNS_PROXY_COMPLETION_ROUTINE",
    "DNS_PROXY_INFORMATION_TYPE",
    "DNS_PROXY_INFORMATION_DIRECT",
    "DNS_PROXY_INFORMATION_DEFAULT_SETTINGS",
    "DNS_PROXY_INFORMATION_PROXY_NAME",
    "DNS_PROXY_INFORMATION_DOES_NOT_EXIST",
    "DNS_PROXY_INFORMATION",
    "DNS_CHARSET",
    "DNS_CHARSET_DnsCharSetUnknown",
    "DNS_CHARSET_DnsCharSetUnicode",
    "DNS_CHARSET_DnsCharSetUtf8",
    "DNS_CHARSET_DnsCharSetAnsi",
    "DNS_FREE_TYPE",
    "DNS_FREE_TYPE_DnsFreeFlat",
    "DNS_FREE_TYPE_DnsFreeRecordList",
    "DNS_FREE_TYPE_DnsFreeParsedMessageFields",
    "DNS_QUERY_RESULT",
    "PDNS_QUERY_COMPLETION_ROUTINE",
    "DNS_QUERY_REQUEST",
    "DNS_QUERY_CANCEL",
    "DNS_CUSTOM_SERVER",
    "DNS_QUERY_REQUEST3",
    "DNS_APPLICATION_SETTINGS",
    "DNS_NAME_FORMAT",
    "DNS_NAME_FORMAT_DnsNameDomain",
    "DNS_NAME_FORMAT_DnsNameDomainLabel",
    "DNS_NAME_FORMAT_DnsNameHostnameFull",
    "DNS_NAME_FORMAT_DnsNameHostnameLabel",
    "DNS_NAME_FORMAT_DnsNameWildcard",
    "DNS_NAME_FORMAT_DnsNameSrvRecord",
    "DNS_NAME_FORMAT_DnsNameValidateTld",
    "DNS_MESSAGE_BUFFER",
    "DNS_CONNECTION_PROXY_TYPE",
    "DNS_CONNECTION_PROXY_TYPE_NULL",
    "DNS_CONNECTION_PROXY_TYPE_HTTP",
    "DNS_CONNECTION_PROXY_TYPE_WAP",
    "DNS_CONNECTION_PROXY_TYPE_SOCKS4",
    "DNS_CONNECTION_PROXY_TYPE_SOCKS5",
    "DNS_CONNECTION_PROXY_INFO_SWITCH",
    "DNS_CONNECTION_PROXY_INFO_SWITCH_CONFIG",
    "DNS_CONNECTION_PROXY_INFO_SWITCH_SCRIPT",
    "DNS_CONNECTION_PROXY_INFO_SWITCH_WPAD",
    "DNS_CONNECTION_PROXY_INFO",
    "DNS_CONNECTION_PROXY_INFO_EX",
    "DNS_CONNECTION_PROXY_ELEMENT",
    "DNS_CONNECTION_PROXY_LIST",
    "DNS_CONNECTION_NAME",
    "DNS_CONNECTION_NAME_LIST",
    "DNS_CONNECTION_IFINDEX_ENTRY",
    "DNS_CONNECTION_IFINDEX_LIST",
    "DNS_CONNECTION_POLICY_ENTRY",
    "DNS_CONNECTION_POLICY_ENTRY_LIST",
    "DNS_CONNECTION_POLICY_TAG",
    "TAG_DNS_CONNECTION_POLICY_TAG_DEFAULT",
    "TAG_DNS_CONNECTION_POLICY_TAG_CONNECTION_MANAGER",
    "TAG_DNS_CONNECTION_POLICY_TAG_WWWPT",
    "DNS_SERVICE_INSTANCE",
    "DNS_SERVICE_CANCEL",
    "PDNS_SERVICE_BROWSE_CALLBACK",
    "DNS_SERVICE_BROWSE_REQUEST",
    "PDNS_SERVICE_RESOLVE_COMPLETE",
    "DNS_SERVICE_RESOLVE_REQUEST",
    "PDNS_SERVICE_REGISTER_COMPLETE",
    "DNS_SERVICE_REGISTER_REQUEST",
    "MDNS_QUERY_HANDLE",
    "PMDNS_QUERY_CALLBACK",
    "MDNS_QUERY_REQUEST",
    "DnsQueryConfig",
    "DnsRecordCopyEx",
    "DnsRecordSetCopyEx",
    "DnsRecordCompare",
    "DnsRecordSetCompare",
    "DnsRecordSetDetach",
    "DnsFree",
    "DnsQuery_A",
    "DnsQuery_UTF8",
    "DnsQuery_W",
    "DnsQuery_",
    "DnsQueryEx",
    "DnsCancelQuery",
    "DnsFreeCustomServers",
    "DnsGetApplicationSettings",
    "DnsSetApplicationSettings",
    "DnsAcquireContextHandle_W",
    "DnsAcquireContextHandle_",
    "DnsAcquireContextHandle_A",
    "DnsReleaseContextHandle",
    "DnsModifyRecordsInSet_W",
    "DnsModifyRecordsInSet_",
    "DnsModifyRecordsInSet_A",
    "DnsModifyRecordsInSet_UTF8",
    "DnsReplaceRecordSetW",
    "DnsReplaceRecordSet",
    "DnsReplaceRecordSetA",
    "DnsReplaceRecordSetUTF8",
    "DnsValidateName_W",
    "DnsValidateName_",
    "DnsValidateName_A",
    "DnsValidateName_UTF8",
    "DnsNameCompare_A",
    "DnsNameCompare_W",
    "DnsNameCompare_",
    "DnsWriteQuestionToBuffer_W",
    "DnsWriteQuestionToBuffer_UTF8",
    "DnsExtractRecordsFromMessage_W",
    "DnsExtractRecordsFromMessage_UTF8",
    "DnsGetProxyInformation",
    "DnsFreeProxyName",
    "DnsConnectionGetProxyInfoForHostUrl",
    "DnsConnectionFreeProxyInfoEx",
    "DnsConnectionGetProxyInfo",
    "DnsConnectionFreeProxyInfo",
    "DnsConnectionSetProxyInfo",
    "DnsConnectionDeleteProxyInfo",
    "DnsConnectionGetProxyList",
    "DnsConnectionFreeProxyList",
    "DnsConnectionGetNameList",
    "DnsConnectionFreeNameList",
    "DnsConnectionUpdateIfIndexTable",
    "DnsConnectionSetPolicyEntries",
    "DnsConnectionDeletePolicyEntries",
    "DnsServiceConstructInstance",
    "DnsServiceCopyInstance",
    "DnsServiceFreeInstance",
    "DnsServiceBrowse",
    "DnsServiceBrowseCancel",
    "DnsServiceResolve",
    "DnsServiceResolveCancel",
    "DnsServiceRegister",
    "DnsServiceDeRegister",
    "DnsServiceRegisterCancel",
    "DnsStartMulticastQuery",
    "DnsStopMulticastQuery",
]
