from win32more import *
import win32more.Foundation
import win32more.NetworkManagement.IpHelper
import win32more.NetworkManagement.Ndis
import win32more.Networking.WinSock
import win32more.System.IO
import win32more.System.WindowsProgramming

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
NET_IF_OPER_STATUS_DOWN_NOT_AUTHENTICATED = 1
NET_IF_OPER_STATUS_DOWN_NOT_MEDIA_CONNECTED = 2
NET_IF_OPER_STATUS_DORMANT_PAUSED = 4
NET_IF_OPER_STATUS_DORMANT_LOW_POWER = 8
NET_IF_OID_IF_ALIAS = 1
NET_IF_OID_COMPARTMENT_ID = 2
NET_IF_OID_NETWORK_GUID = 3
NET_IF_OID_IF_ENTRY = 4
NET_SITEID_UNSPECIFIED = 0
NET_SITEID_MAXUSER = 134217727
NET_SITEID_MAXSYSTEM = 268435455
NET_IFLUID_UNSPECIFIED = 0
NIIF_HARDWARE_INTERFACE = 1
NIIF_FILTER_INTERFACE = 2
NIIF_NDIS_RESERVED1 = 4
NIIF_NDIS_RESERVED2 = 8
NIIF_NDIS_RESERVED3 = 16
NIIF_NDIS_WDM_INTERFACE = 32
NIIF_NDIS_ENDPOINT_INTERFACE = 64
NIIF_NDIS_ISCSI_INTERFACE = 128
NIIF_NDIS_RESERVED4 = 256
IF_MAX_STRING_SIZE = 256
IF_MAX_PHYS_ADDRESS_LENGTH = 32
ANY_SIZE = 1
MAXLEN_PHYSADDR = 8
MAXLEN_IFDESCR = 256
MAX_INTERFACE_NAME_LEN = 256
MIN_IF_TYPE = 1
IF_TYPE_OTHER = 1
IF_TYPE_REGULAR_1822 = 2
IF_TYPE_HDH_1822 = 3
IF_TYPE_DDN_X25 = 4
IF_TYPE_RFC877_X25 = 5
IF_TYPE_ETHERNET_CSMACD = 6
IF_TYPE_IS088023_CSMACD = 7
IF_TYPE_ISO88024_TOKENBUS = 8
IF_TYPE_ISO88025_TOKENRING = 9
IF_TYPE_ISO88026_MAN = 10
IF_TYPE_STARLAN = 11
IF_TYPE_PROTEON_10MBIT = 12
IF_TYPE_PROTEON_80MBIT = 13
IF_TYPE_HYPERCHANNEL = 14
IF_TYPE_FDDI = 15
IF_TYPE_LAP_B = 16
IF_TYPE_SDLC = 17
IF_TYPE_DS1 = 18
IF_TYPE_E1 = 19
IF_TYPE_BASIC_ISDN = 20
IF_TYPE_PRIMARY_ISDN = 21
IF_TYPE_PROP_POINT2POINT_SERIAL = 22
IF_TYPE_PPP = 23
IF_TYPE_SOFTWARE_LOOPBACK = 24
IF_TYPE_EON = 25
IF_TYPE_ETHERNET_3MBIT = 26
IF_TYPE_NSIP = 27
IF_TYPE_SLIP = 28
IF_TYPE_ULTRA = 29
IF_TYPE_DS3 = 30
IF_TYPE_SIP = 31
IF_TYPE_FRAMERELAY = 32
IF_TYPE_RS232 = 33
IF_TYPE_PARA = 34
IF_TYPE_ARCNET = 35
IF_TYPE_ARCNET_PLUS = 36
IF_TYPE_ATM = 37
IF_TYPE_MIO_X25 = 38
IF_TYPE_SONET = 39
IF_TYPE_X25_PLE = 40
IF_TYPE_ISO88022_LLC = 41
IF_TYPE_LOCALTALK = 42
IF_TYPE_SMDS_DXI = 43
IF_TYPE_FRAMERELAY_SERVICE = 44
IF_TYPE_V35 = 45
IF_TYPE_HSSI = 46
IF_TYPE_HIPPI = 47
IF_TYPE_MODEM = 48
IF_TYPE_AAL5 = 49
IF_TYPE_SONET_PATH = 50
IF_TYPE_SONET_VT = 51
IF_TYPE_SMDS_ICIP = 52
IF_TYPE_PROP_VIRTUAL = 53
IF_TYPE_PROP_MULTIPLEXOR = 54
IF_TYPE_IEEE80212 = 55
IF_TYPE_FIBRECHANNEL = 56
IF_TYPE_HIPPIINTERFACE = 57
IF_TYPE_FRAMERELAY_INTERCONNECT = 58
IF_TYPE_AFLANE_8023 = 59
IF_TYPE_AFLANE_8025 = 60
IF_TYPE_CCTEMUL = 61
IF_TYPE_FASTETHER = 62
IF_TYPE_ISDN = 63
IF_TYPE_V11 = 64
IF_TYPE_V36 = 65
IF_TYPE_G703_64K = 66
IF_TYPE_G703_2MB = 67
IF_TYPE_QLLC = 68
IF_TYPE_FASTETHER_FX = 69
IF_TYPE_CHANNEL = 70
IF_TYPE_IEEE80211 = 71
IF_TYPE_IBM370PARCHAN = 72
IF_TYPE_ESCON = 73
IF_TYPE_DLSW = 74
IF_TYPE_ISDN_S = 75
IF_TYPE_ISDN_U = 76
IF_TYPE_LAP_D = 77
IF_TYPE_IPSWITCH = 78
IF_TYPE_RSRB = 79
IF_TYPE_ATM_LOGICAL = 80
IF_TYPE_DS0 = 81
IF_TYPE_DS0_BUNDLE = 82
IF_TYPE_BSC = 83
IF_TYPE_ASYNC = 84
IF_TYPE_CNR = 85
IF_TYPE_ISO88025R_DTR = 86
IF_TYPE_EPLRS = 87
IF_TYPE_ARAP = 88
IF_TYPE_PROP_CNLS = 89
IF_TYPE_HOSTPAD = 90
IF_TYPE_TERMPAD = 91
IF_TYPE_FRAMERELAY_MPI = 92
IF_TYPE_X213 = 93
IF_TYPE_ADSL = 94
IF_TYPE_RADSL = 95
IF_TYPE_SDSL = 96
IF_TYPE_VDSL = 97
IF_TYPE_ISO88025_CRFPRINT = 98
IF_TYPE_MYRINET = 99
IF_TYPE_VOICE_EM = 100
IF_TYPE_VOICE_FXO = 101
IF_TYPE_VOICE_FXS = 102
IF_TYPE_VOICE_ENCAP = 103
IF_TYPE_VOICE_OVERIP = 104
IF_TYPE_ATM_DXI = 105
IF_TYPE_ATM_FUNI = 106
IF_TYPE_ATM_IMA = 107
IF_TYPE_PPPMULTILINKBUNDLE = 108
IF_TYPE_IPOVER_CDLC = 109
IF_TYPE_IPOVER_CLAW = 110
IF_TYPE_STACKTOSTACK = 111
IF_TYPE_VIRTUALIPADDRESS = 112
IF_TYPE_MPC = 113
IF_TYPE_IPOVER_ATM = 114
IF_TYPE_ISO88025_FIBER = 115
IF_TYPE_TDLC = 116
IF_TYPE_GIGABITETHERNET = 117
IF_TYPE_HDLC = 118
IF_TYPE_LAP_F = 119
IF_TYPE_V37 = 120
IF_TYPE_X25_MLP = 121
IF_TYPE_X25_HUNTGROUP = 122
IF_TYPE_TRANSPHDLC = 123
IF_TYPE_INTERLEAVE = 124
IF_TYPE_FAST = 125
IF_TYPE_IP = 126
IF_TYPE_DOCSCABLE_MACLAYER = 127
IF_TYPE_DOCSCABLE_DOWNSTREAM = 128
IF_TYPE_DOCSCABLE_UPSTREAM = 129
IF_TYPE_A12MPPSWITCH = 130
IF_TYPE_TUNNEL = 131
IF_TYPE_COFFEE = 132
IF_TYPE_CES = 133
IF_TYPE_ATM_SUBINTERFACE = 134
IF_TYPE_L2_VLAN = 135
IF_TYPE_L3_IPVLAN = 136
IF_TYPE_L3_IPXVLAN = 137
IF_TYPE_DIGITALPOWERLINE = 138
IF_TYPE_MEDIAMAILOVERIP = 139
IF_TYPE_DTM = 140
IF_TYPE_DCN = 141
IF_TYPE_IPFORWARD = 142
IF_TYPE_MSDSL = 143
IF_TYPE_IEEE1394 = 144
IF_TYPE_IF_GSN = 145
IF_TYPE_DVBRCC_MACLAYER = 146
IF_TYPE_DVBRCC_DOWNSTREAM = 147
IF_TYPE_DVBRCC_UPSTREAM = 148
IF_TYPE_ATM_VIRTUAL = 149
IF_TYPE_MPLS_TUNNEL = 150
IF_TYPE_SRP = 151
IF_TYPE_VOICEOVERATM = 152
IF_TYPE_VOICEOVERFRAMERELAY = 153
IF_TYPE_IDSL = 154
IF_TYPE_COMPOSITELINK = 155
IF_TYPE_SS7_SIGLINK = 156
IF_TYPE_PROP_WIRELESS_P2P = 157
IF_TYPE_FR_FORWARD = 158
IF_TYPE_RFC1483 = 159
IF_TYPE_USB = 160
IF_TYPE_IEEE8023AD_LAG = 161
IF_TYPE_BGP_POLICY_ACCOUNTING = 162
IF_TYPE_FRF16_MFR_BUNDLE = 163
IF_TYPE_H323_GATEKEEPER = 164
IF_TYPE_H323_PROXY = 165
IF_TYPE_MPLS = 166
IF_TYPE_MF_SIGLINK = 167
IF_TYPE_HDSL2 = 168
IF_TYPE_SHDSL = 169
IF_TYPE_DS1_FDL = 170
IF_TYPE_POS = 171
IF_TYPE_DVB_ASI_IN = 172
IF_TYPE_DVB_ASI_OUT = 173
IF_TYPE_PLC = 174
IF_TYPE_NFAS = 175
IF_TYPE_TR008 = 176
IF_TYPE_GR303_RDT = 177
IF_TYPE_GR303_IDT = 178
IF_TYPE_ISUP = 179
IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER = 180
IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM = 181
IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM = 182
IF_TYPE_HIPERLAN2 = 183
IF_TYPE_PROP_BWA_P2MP = 184
IF_TYPE_SONET_OVERHEAD_CHANNEL = 185
IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL = 186
IF_TYPE_AAL2 = 187
IF_TYPE_RADIO_MAC = 188
IF_TYPE_ATM_RADIO = 189
IF_TYPE_IMT = 190
IF_TYPE_MVL = 191
IF_TYPE_REACH_DSL = 192
IF_TYPE_FR_DLCI_ENDPT = 193
IF_TYPE_ATM_VCI_ENDPT = 194
IF_TYPE_OPTICAL_CHANNEL = 195
IF_TYPE_OPTICAL_TRANSPORT = 196
IF_TYPE_IEEE80216_WMAN = 237
IF_TYPE_WWANPP = 243
IF_TYPE_WWANPP2 = 244
IF_TYPE_IEEE802154 = 259
IF_TYPE_XBOX_WIRELESS = 281
MAX_IF_TYPE = 281
IF_CHECK_NONE = 0
IF_CHECK_MCAST = 1
IF_CHECK_SEND = 2
IF_CONNECTION_DEDICATED = 1
IF_CONNECTION_PASSIVE = 2
IF_CONNECTION_DEMAND = 3
IF_ADMIN_STATUS_UP = 1
IF_ADMIN_STATUS_DOWN = 2
IF_ADMIN_STATUS_TESTING = 3
MIB_IF_TYPE_OTHER = 1
MIB_IF_TYPE_ETHERNET = 6
MIB_IF_TYPE_TOKENRING = 9
MIB_IF_TYPE_FDDI = 15
MIB_IF_TYPE_PPP = 23
MIB_IF_TYPE_LOOPBACK = 24
MIB_IF_TYPE_SLIP = 28
MIB_IF_ADMIN_STATUS_UP = 1
MIB_IF_ADMIN_STATUS_DOWN = 2
MIB_IF_ADMIN_STATUS_TESTING = 3
MIB_IPADDR_PRIMARY = 1
MIB_IPADDR_DYNAMIC = 4
MIB_IPADDR_DISCONNECTED = 8
MIB_IPADDR_DELETED = 64
MIB_IPADDR_TRANSIENT = 128
MIB_IPADDR_DNS_ELIGIBLE = 256
MIB_IPROUTE_METRIC_UNUSED = 4294967295
MIB_USE_CURRENT_TTL = 4294967295
MIB_USE_CURRENT_FORWARDING = 4294967295
ICMP6_INFOMSG_MASK = 128
IPRTRMGR_PID = 10000
IF_NUMBER = 0
IF_TABLE = 1
IF_ROW = 2
IP_STATS = 3
IP_ADDRTABLE = 4
IP_ADDRROW = 5
IP_FORWARDNUMBER = 6
IP_FORWARDTABLE = 7
IP_FORWARDROW = 8
IP_NETTABLE = 9
IP_NETROW = 10
ICMP_STATS = 11
TCP_STATS = 12
TCP_TABLE = 13
TCP_ROW = 14
UDP_STATS = 15
UDP_TABLE = 16
UDP_ROW = 17
MCAST_MFE = 18
MCAST_MFE_STATS = 19
BEST_IF = 20
BEST_ROUTE = 21
PROXY_ARP = 22
MCAST_IF_ENTRY = 23
MCAST_GLOBAL = 24
IF_STATUS = 25
MCAST_BOUNDARY = 26
MCAST_SCOPE = 27
DEST_MATCHING = 28
DEST_LONGER = 29
DEST_SHORTER = 30
ROUTE_MATCHING = 31
ROUTE_LONGER = 32
ROUTE_SHORTER = 33
ROUTE_STATE = 34
MCAST_MFE_STATS_EX = 35
IP6_STATS = 36
UDP6_STATS = 37
TCP6_STATS = 38
NUMBER_OF_EXPORTED_VARIABLES = 39
MAX_SCOPE_NAME_LEN = 255
MAX_MIB_OFFSET = 8
MIB_INVALID_TEREDO_PORT_NUMBER = 0
DNS_SETTINGS_VERSION1 = 1
DNS_SETTINGS_VERSION2 = 2
DNS_INTERFACE_SETTINGS_VERSION1 = 1
DNS_INTERFACE_SETTINGS_VERSION2 = 2
DNS_INTERFACE_SETTINGS_VERSION3 = 3
DNS_SETTING_IPV6 = 1
DNS_SETTING_NAMESERVER = 2
DNS_SETTING_SEARCHLIST = 4
DNS_SETTING_REGISTRATION_ENABLED = 8
DNS_SETTING_REGISTER_ADAPTER_NAME = 16
DNS_SETTING_DOMAIN = 32
DNS_SETTING_HOSTNAME = 64
DNS_SETTINGS_ENABLE_LLMNR = 128
DNS_SETTINGS_QUERY_ADAPTER_NAME = 256
DNS_SETTING_PROFILE_NAMESERVER = 512
DNS_SETTING_DISABLE_UNCONSTRAINED_QUERIES = 1024
DNS_SETTING_SUPPLEMENTAL_SEARCH_LIST = 2048
DNS_SETTING_DOH = 4096
DNS_SETTING_DOH_PROFILE = 8192
DNS_ENABLE_DOH = 1
DNS_DOH_POLICY_NOT_CONFIGURED = 4
DNS_DOH_POLICY_DISABLE = 8
DNS_DOH_POLICY_AUTO = 16
DNS_DOH_POLICY_REQUIRED = 32
DNS_SERVER_PROPERTY_VERSION1 = 1
DNS_DOH_SERVER_SETTINGS_ENABLE_AUTO = 1
DNS_DOH_SERVER_SETTINGS_ENABLE = 2
DNS_DOH_SERVER_SETTINGS_FALLBACK_TO_UDP = 4
DNS_DOH_AUTO_UPGRADE_SERVER = 8
TCPIP_OWNING_MODULE_SIZE = 16
FD_FLAGS_NOSYN = 1
FD_FLAGS_ALLFLAGS = 1
LB_SRC_ADDR_USE_SRCADDR_FLAG = 1
LB_SRC_ADDR_USE_DSTADDR_FLAG = 2
LB_DST_ADDR_USE_SRCADDR_FLAG = 4
LB_DST_ADDR_USE_DSTADDR_FLAG = 8
LB_SRC_MASK_LATE_FLAG = 16
LB_DST_MASK_LATE_FLAG = 32
ERROR_BASE = 23000
PFERROR_NO_PF_INTERFACE = 23000
PFERROR_NO_FILTERS_GIVEN = 23001
PFERROR_BUFFER_TOO_SMALL = 23002
ERROR_IPV6_NOT_IMPLEMENTED = 23003
IP_EXPORT_INCLUDED = 1
MAX_ADAPTER_NAME = 128
IP_STATUS_BASE = 11000
IP_SUCCESS = 0
IP_BUF_TOO_SMALL = 11001
IP_DEST_NET_UNREACHABLE = 11002
IP_DEST_HOST_UNREACHABLE = 11003
IP_DEST_PROT_UNREACHABLE = 11004
IP_DEST_PORT_UNREACHABLE = 11005
IP_NO_RESOURCES = 11006
IP_BAD_OPTION = 11007
IP_HW_ERROR = 11008
IP_PACKET_TOO_BIG = 11009
IP_REQ_TIMED_OUT = 11010
IP_BAD_REQ = 11011
IP_BAD_ROUTE = 11012
IP_TTL_EXPIRED_TRANSIT = 11013
IP_TTL_EXPIRED_REASSEM = 11014
IP_PARAM_PROBLEM = 11015
IP_SOURCE_QUENCH = 11016
IP_OPTION_TOO_BIG = 11017
IP_BAD_DESTINATION = 11018
IP_DEST_NO_ROUTE = 11002
IP_DEST_ADDR_UNREACHABLE = 11003
IP_DEST_PROHIBITED = 11004
IP_HOP_LIMIT_EXCEEDED = 11013
IP_REASSEMBLY_TIME_EXCEEDED = 11014
IP_PARAMETER_PROBLEM = 11015
IP_DEST_UNREACHABLE = 11040
IP_TIME_EXCEEDED = 11041
IP_BAD_HEADER = 11042
IP_UNRECOGNIZED_NEXT_HEADER = 11043
IP_ICMP_ERROR = 11044
IP_DEST_SCOPE_MISMATCH = 11045
IP_ADDR_DELETED = 11019
IP_SPEC_MTU_CHANGE = 11020
IP_MTU_CHANGE = 11021
IP_UNLOAD = 11022
IP_ADDR_ADDED = 11023
IP_MEDIA_CONNECT = 11024
IP_MEDIA_DISCONNECT = 11025
IP_BIND_ADAPTER = 11026
IP_UNBIND_ADAPTER = 11027
IP_DEVICE_DOES_NOT_EXIST = 11028
IP_DUPLICATE_ADDRESS = 11029
IP_INTERFACE_METRIC_CHANGE = 11030
IP_RECONFIG_SECFLTR = 11031
IP_NEGOTIATING_IPSEC = 11032
IP_INTERFACE_WOL_CAPABILITY_CHANGE = 11033
IP_DUPLICATE_IPADD = 11034
IP_GENERAL_FAILURE = 11050
MAX_IP_STATUS = 11050
IP_PENDING = 11255
IP_FLAG_REVERSE = 1
IP_FLAG_DF = 2
MAX_OPT_SIZE = 40
IOCTL_IP_RTCHANGE_NOTIFY_REQUEST = 101
IOCTL_IP_ADDCHANGE_NOTIFY_REQUEST = 102
IOCTL_ARP_SEND_REQUEST = 103
IOCTL_IP_INTERFACE_INFO = 104
IOCTL_IP_GET_BEST_INTERFACE = 105
IOCTL_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS = 106
NET_STRING_IPV4_ADDRESS = 1
NET_STRING_IPV4_SERVICE = 2
NET_STRING_IPV4_NETWORK = 4
NET_STRING_IPV6_ADDRESS = 8
NET_STRING_IPV6_ADDRESS_NO_SCOPE = 16
NET_STRING_IPV6_SERVICE = 32
NET_STRING_IPV6_SERVICE_NO_SCOPE = 64
NET_STRING_IPV6_NETWORK = 128
NET_STRING_NAMED_ADDRESS = 256
NET_STRING_NAMED_SERVICE = 512
MAX_ADAPTER_DESCRIPTION_LENGTH = 128
MAX_ADAPTER_NAME_LENGTH = 256
MAX_ADAPTER_ADDRESS_LENGTH = 8
DEFAULT_MINIMUM_ENTITIES = 32
MAX_HOSTNAME_LEN = 128
MAX_DOMAIN_NAME_LEN = 128
MAX_SCOPE_ID_LEN = 256
MAX_DHCPV6_DUID_LENGTH = 130
MAX_DNS_SUFFIX_STRING_LENGTH = 256
BROADCAST_NODETYPE = 1
PEER_TO_PEER_NODETYPE = 2
MIXED_NODETYPE = 4
HYBRID_NODETYPE = 8
IP_ADAPTER_ADDRESS_DNS_ELIGIBLE = 1
IP_ADAPTER_ADDRESS_TRANSIENT = 2
IP_ADAPTER_DDNS_ENABLED = 1
IP_ADAPTER_REGISTER_ADAPTER_SUFFIX = 2
IP_ADAPTER_DHCP_ENABLED = 4
IP_ADAPTER_RECEIVE_ONLY = 8
IP_ADAPTER_NO_MULTICAST = 16
IP_ADAPTER_IPV6_OTHER_STATEFUL_CONFIG = 32
IP_ADAPTER_NETBIOS_OVER_TCPIP_ENABLED = 64
IP_ADAPTER_IPV4_ENABLED = 128
IP_ADAPTER_IPV6_ENABLED = 256
IP_ADAPTER_IPV6_MANAGE_ADDRESS_CONFIG = 512
GAA_FLAG_SKIP_DNS_INFO = 2048
IP_ROUTER_MANAGER_VERSION = 1
IP_GENERAL_INFO_BASE = 4294901760
IP_IN_FILTER_INFO = 4294901761
IP_OUT_FILTER_INFO = 4294901762
IP_GLOBAL_INFO = 4294901763
IP_INTERFACE_STATUS_INFO = 4294901764
IP_ROUTE_INFO = 4294901765
IP_PROT_PRIORITY_INFO = 4294901766
IP_ROUTER_DISC_INFO = 4294901767
IP_DEMAND_DIAL_FILTER_INFO = 4294901769
IP_MCAST_HEARBEAT_INFO = 4294901770
IP_MCAST_BOUNDARY_INFO = 4294901771
IP_IPINIP_CFG_INFO = 4294901772
IP_IFFILTER_INFO = 4294901773
IP_MCAST_LIMIT_INFO = 4294901774
IPV6_GLOBAL_INFO = 4294901775
IPV6_ROUTE_INFO = 4294901776
IP_IN_FILTER_INFO_V6 = 4294901777
IP_OUT_FILTER_INFO_V6 = 4294901778
IP_DEMAND_DIAL_FILTER_INFO_V6 = 4294901779
IP_IFFILTER_INFO_V6 = 4294901780
IP_FILTER_ENABLE_INFO = 4294901781
IP_FILTER_ENABLE_INFO_V6 = 4294901782
IP_PROT_PRIORITY_INFO_EX = 4294901783
ADDRESS_FAMILY = UInt32
AF_INET = 2
AF_INET6 = 23
AF_UNSPEC = 0
GET_ADAPTERS_ADDRESSES_FLAGS = UInt32
GAA_FLAG_SKIP_UNICAST = 1
GAA_FLAG_SKIP_ANYCAST = 2
GAA_FLAG_SKIP_MULTICAST = 4
GAA_FLAG_SKIP_DNS_SERVER = 8
GAA_FLAG_INCLUDE_PREFIX = 16
GAA_FLAG_SKIP_FRIENDLY_NAME = 32
GAA_FLAG_INCLUDE_WINS_INFO = 64
GAA_FLAG_INCLUDE_GATEWAYS = 128
GAA_FLAG_INCLUDE_ALL_INTERFACES = 256
GAA_FLAG_INCLUDE_ALL_COMPARTMENTS = 512
GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER = 1024
IcmpHandle = IntPtr
HIFTIMESTAMPCHANGE = IntPtr
def _define_ip_option_information_head():
    class ip_option_information(Structure):
        pass
    return ip_option_information
def _define_ip_option_information():
    ip_option_information = win32more.NetworkManagement.IpHelper.ip_option_information_head
    ip_option_information._fields_ = [
        ("Ttl", Byte),
        ("Tos", Byte),
        ("Flags", Byte),
        ("OptionsSize", Byte),
        ("OptionsData", c_char_p_no),
    ]
    return ip_option_information
def _define_ip_option_information32_head():
    class ip_option_information32(Structure):
        pass
    return ip_option_information32
def _define_ip_option_information32():
    ip_option_information32 = win32more.NetworkManagement.IpHelper.ip_option_information32_head
    ip_option_information32._fields_ = [
        ("Ttl", Byte),
        ("Tos", Byte),
        ("Flags", Byte),
        ("OptionsSize", Byte),
        ("OptionsData", c_char_p_no),
    ]
    return ip_option_information32
def _define_icmp_echo_reply_head():
    class icmp_echo_reply(Structure):
        pass
    return icmp_echo_reply
def _define_icmp_echo_reply():
    icmp_echo_reply = win32more.NetworkManagement.IpHelper.icmp_echo_reply_head
    icmp_echo_reply._fields_ = [
        ("Address", UInt32),
        ("Status", UInt32),
        ("RoundTripTime", UInt32),
        ("DataSize", UInt16),
        ("Reserved", UInt16),
        ("Data", c_void_p),
        ("Options", win32more.NetworkManagement.IpHelper.ip_option_information),
    ]
    return icmp_echo_reply
def _define_icmp_echo_reply32_head():
    class icmp_echo_reply32(Structure):
        pass
    return icmp_echo_reply32
def _define_icmp_echo_reply32():
    icmp_echo_reply32 = win32more.NetworkManagement.IpHelper.icmp_echo_reply32_head
    icmp_echo_reply32._fields_ = [
        ("Address", UInt32),
        ("Status", UInt32),
        ("RoundTripTime", UInt32),
        ("DataSize", UInt16),
        ("Reserved", UInt16),
        ("Data", c_void_p),
        ("Options", win32more.NetworkManagement.IpHelper.ip_option_information32),
    ]
    return icmp_echo_reply32
def _define_IPV6_ADDRESS_EX_head():
    class IPV6_ADDRESS_EX(Structure):
        pass
    return IPV6_ADDRESS_EX
def _define_IPV6_ADDRESS_EX():
    IPV6_ADDRESS_EX = win32more.NetworkManagement.IpHelper.IPV6_ADDRESS_EX_head
    IPV6_ADDRESS_EX._pack_ = 1
    IPV6_ADDRESS_EX._fields_ = [
        ("sin6_port", UInt16),
        ("sin6_flowinfo", UInt32),
        ("sin6_addr", UInt16 * 8),
        ("sin6_scope_id", UInt32),
    ]
    return IPV6_ADDRESS_EX
def _define_icmpv6_echo_reply_lh_head():
    class icmpv6_echo_reply_lh(Structure):
        pass
    return icmpv6_echo_reply_lh
def _define_icmpv6_echo_reply_lh():
    icmpv6_echo_reply_lh = win32more.NetworkManagement.IpHelper.icmpv6_echo_reply_lh_head
    icmpv6_echo_reply_lh._fields_ = [
        ("Address", win32more.NetworkManagement.IpHelper.IPV6_ADDRESS_EX),
        ("Status", UInt32),
        ("RoundTripTime", UInt32),
    ]
    return icmpv6_echo_reply_lh
def _define_arp_send_reply_head():
    class arp_send_reply(Structure):
        pass
    return arp_send_reply
def _define_arp_send_reply():
    arp_send_reply = win32more.NetworkManagement.IpHelper.arp_send_reply_head
    arp_send_reply._fields_ = [
        ("DestAddress", UInt32),
        ("SrcAddress", UInt32),
    ]
    return arp_send_reply
def _define_tcp_reserve_port_range_head():
    class tcp_reserve_port_range(Structure):
        pass
    return tcp_reserve_port_range
def _define_tcp_reserve_port_range():
    tcp_reserve_port_range = win32more.NetworkManagement.IpHelper.tcp_reserve_port_range_head
    tcp_reserve_port_range._fields_ = [
        ("UpperRange", UInt16),
        ("LowerRange", UInt16),
    ]
    return tcp_reserve_port_range
def _define_IP_ADAPTER_INDEX_MAP_head():
    class IP_ADAPTER_INDEX_MAP(Structure):
        pass
    return IP_ADAPTER_INDEX_MAP
def _define_IP_ADAPTER_INDEX_MAP():
    IP_ADAPTER_INDEX_MAP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP_head
    IP_ADAPTER_INDEX_MAP._fields_ = [
        ("Index", UInt32),
        ("Name", Char * 128),
    ]
    return IP_ADAPTER_INDEX_MAP
def _define_IP_INTERFACE_INFO_head():
    class IP_INTERFACE_INFO(Structure):
        pass
    return IP_INTERFACE_INFO
def _define_IP_INTERFACE_INFO():
    IP_INTERFACE_INFO = win32more.NetworkManagement.IpHelper.IP_INTERFACE_INFO_head
    IP_INTERFACE_INFO._fields_ = [
        ("NumAdapters", Int32),
        ("Adapter", win32more.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP * 0),
    ]
    return IP_INTERFACE_INFO
def _define_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS_head():
    class IP_UNIDIRECTIONAL_ADAPTER_ADDRESS(Structure):
        pass
    return IP_UNIDIRECTIONAL_ADAPTER_ADDRESS
def _define_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS():
    IP_UNIDIRECTIONAL_ADAPTER_ADDRESS = win32more.NetworkManagement.IpHelper.IP_UNIDIRECTIONAL_ADAPTER_ADDRESS_head
    IP_UNIDIRECTIONAL_ADAPTER_ADDRESS._fields_ = [
        ("NumAdapters", UInt32),
        ("Address", UInt32 * 0),
    ]
    return IP_UNIDIRECTIONAL_ADAPTER_ADDRESS
def _define_IP_ADAPTER_ORDER_MAP_head():
    class IP_ADAPTER_ORDER_MAP(Structure):
        pass
    return IP_ADAPTER_ORDER_MAP
def _define_IP_ADAPTER_ORDER_MAP():
    IP_ADAPTER_ORDER_MAP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_ORDER_MAP_head
    IP_ADAPTER_ORDER_MAP._fields_ = [
        ("NumAdapters", UInt32),
        ("AdapterOrder", UInt32 * 0),
    ]
    return IP_ADAPTER_ORDER_MAP
def _define_IP_MCAST_COUNTER_INFO_head():
    class IP_MCAST_COUNTER_INFO(Structure):
        pass
    return IP_MCAST_COUNTER_INFO
def _define_IP_MCAST_COUNTER_INFO():
    IP_MCAST_COUNTER_INFO = win32more.NetworkManagement.IpHelper.IP_MCAST_COUNTER_INFO_head
    IP_MCAST_COUNTER_INFO._fields_ = [
        ("InMcastOctets", UInt64),
        ("OutMcastOctets", UInt64),
        ("InMcastPkts", UInt64),
        ("OutMcastPkts", UInt64),
    ]
    return IP_MCAST_COUNTER_INFO
IF_ACCESS_TYPE = Int32
IF_ACCESS_LOOPBACK = 1
IF_ACCESS_BROADCAST = 2
IF_ACCESS_POINT_TO_POINT = 3
IF_ACCESS_POINTTOPOINT = 3
IF_ACCESS_POINT_TO_MULTI_POINT = 4
IF_ACCESS_POINTTOMULTIPOINT = 4
INTERNAL_IF_OPER_STATUS = Int32
IF_OPER_STATUS_NON_OPERATIONAL = 0
IF_OPER_STATUS_UNREACHABLE = 1
IF_OPER_STATUS_DISCONNECTED = 2
IF_OPER_STATUS_CONNECTING = 3
IF_OPER_STATUS_CONNECTED = 4
IF_OPER_STATUS_OPERATIONAL = 5
NET_IF_OPER_STATUS = Int32
NET_IF_OPER_STATUS_UP = 1
NET_IF_OPER_STATUS_DOWN = 2
NET_IF_OPER_STATUS_TESTING = 3
NET_IF_OPER_STATUS_UNKNOWN = 4
NET_IF_OPER_STATUS_DORMANT = 5
NET_IF_OPER_STATUS_NOT_PRESENT = 6
NET_IF_OPER_STATUS_LOWER_LAYER_DOWN = 7
NET_IF_ADMIN_STATUS = Int32
NET_IF_ADMIN_STATUS_UP = 1
NET_IF_ADMIN_STATUS_DOWN = 2
NET_IF_ADMIN_STATUS_TESTING = 3
NET_IF_RCV_ADDRESS_TYPE = Int32
NET_IF_RCV_ADDRESS_TYPE_OTHER = 1
NET_IF_RCV_ADDRESS_TYPE_VOLATILE = 2
NET_IF_RCV_ADDRESS_TYPE_NON_VOLATILE = 3
def _define_NET_IF_RCV_ADDRESS_LH_head():
    class NET_IF_RCV_ADDRESS_LH(Structure):
        pass
    return NET_IF_RCV_ADDRESS_LH
def _define_NET_IF_RCV_ADDRESS_LH():
    NET_IF_RCV_ADDRESS_LH = win32more.NetworkManagement.IpHelper.NET_IF_RCV_ADDRESS_LH_head
    NET_IF_RCV_ADDRESS_LH._fields_ = [
        ("ifRcvAddressType", win32more.NetworkManagement.IpHelper.NET_IF_RCV_ADDRESS_TYPE),
        ("ifRcvAddressLength", UInt16),
        ("ifRcvAddressOffset", UInt16),
    ]
    return NET_IF_RCV_ADDRESS_LH
def _define_NET_IF_ALIAS_LH_head():
    class NET_IF_ALIAS_LH(Structure):
        pass
    return NET_IF_ALIAS_LH
def _define_NET_IF_ALIAS_LH():
    NET_IF_ALIAS_LH = win32more.NetworkManagement.IpHelper.NET_IF_ALIAS_LH_head
    NET_IF_ALIAS_LH._fields_ = [
        ("ifAliasLength", UInt16),
        ("ifAliasOffset", UInt16),
    ]
    return NET_IF_ALIAS_LH
def _define_NET_LUID_LH_head():
    class NET_LUID_LH(Union):
        pass
    return NET_LUID_LH
def _define_NET_LUID_LH():
    NET_LUID_LH = win32more.NetworkManagement.IpHelper.NET_LUID_LH_head
    class NET_LUID_LH__Info_e__Struct(Structure):
        pass
    NET_LUID_LH__Info_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    NET_LUID_LH._fields_ = [
        ("Value", UInt64),
        ("Info", NET_LUID_LH__Info_e__Struct),
    ]
    return NET_LUID_LH
NET_IF_CONNECTION_TYPE = Int32
NET_IF_CONNECTION_DEDICATED = 1
NET_IF_CONNECTION_PASSIVE = 2
NET_IF_CONNECTION_DEMAND = 3
NET_IF_CONNECTION_MAXIMUM = 4
TUNNEL_TYPE = Int32
TUNNEL_TYPE_NONE = 0
TUNNEL_TYPE_OTHER = 1
TUNNEL_TYPE_DIRECT = 2
TUNNEL_TYPE_6TO4 = 11
TUNNEL_TYPE_ISATAP = 13
TUNNEL_TYPE_TEREDO = 14
TUNNEL_TYPE_IPHTTPS = 15
NET_IF_ACCESS_TYPE = Int32
NET_IF_ACCESS_LOOPBACK = 1
NET_IF_ACCESS_BROADCAST = 2
NET_IF_ACCESS_POINT_TO_POINT = 3
NET_IF_ACCESS_POINT_TO_MULTI_POINT = 4
NET_IF_ACCESS_MAXIMUM = 5
NET_IF_DIRECTION_TYPE = Int32
NET_IF_DIRECTION_SENDRECEIVE = 0
NET_IF_DIRECTION_SENDONLY = 1
NET_IF_DIRECTION_RECEIVEONLY = 2
NET_IF_DIRECTION_MAXIMUM = 3
NET_IF_MEDIA_CONNECT_STATE = Int32
NET_IF_MEDIA_CONNECT_STATE_MediaConnectStateUnknown = 0
NET_IF_MEDIA_CONNECT_STATE_MediaConnectStateConnected = 1
NET_IF_MEDIA_CONNECT_STATE_MediaConnectStateDisconnected = 2
NET_IF_MEDIA_DUPLEX_STATE = Int32
NET_IF_MEDIA_DUPLEX_STATE_MediaDuplexStateUnknown = 0
NET_IF_MEDIA_DUPLEX_STATE_MediaDuplexStateHalf = 1
NET_IF_MEDIA_DUPLEX_STATE_MediaDuplexStateFull = 2
def _define_NET_PHYSICAL_LOCATION_LH_head():
    class NET_PHYSICAL_LOCATION_LH(Structure):
        pass
    return NET_PHYSICAL_LOCATION_LH
def _define_NET_PHYSICAL_LOCATION_LH():
    NET_PHYSICAL_LOCATION_LH = win32more.NetworkManagement.IpHelper.NET_PHYSICAL_LOCATION_LH_head
    NET_PHYSICAL_LOCATION_LH._fields_ = [
        ("BusNumber", UInt32),
        ("SlotNumber", UInt32),
        ("FunctionNumber", UInt32),
    ]
    return NET_PHYSICAL_LOCATION_LH
def _define_IF_COUNTED_STRING_LH_head():
    class IF_COUNTED_STRING_LH(Structure):
        pass
    return IF_COUNTED_STRING_LH
def _define_IF_COUNTED_STRING_LH():
    IF_COUNTED_STRING_LH = win32more.NetworkManagement.IpHelper.IF_COUNTED_STRING_LH_head
    IF_COUNTED_STRING_LH._fields_ = [
        ("Length", UInt16),
        ("String", Char * 257),
    ]
    return IF_COUNTED_STRING_LH
def _define_IF_PHYSICAL_ADDRESS_LH_head():
    class IF_PHYSICAL_ADDRESS_LH(Structure):
        pass
    return IF_PHYSICAL_ADDRESS_LH
def _define_IF_PHYSICAL_ADDRESS_LH():
    IF_PHYSICAL_ADDRESS_LH = win32more.NetworkManagement.IpHelper.IF_PHYSICAL_ADDRESS_LH_head
    IF_PHYSICAL_ADDRESS_LH._fields_ = [
        ("Length", UInt16),
        ("Address", Byte * 32),
    ]
    return IF_PHYSICAL_ADDRESS_LH
IF_ADMINISTRATIVE_STATE = Int32
IF_ADMINISTRATIVE_DISABLED = 0
IF_ADMINISTRATIVE_ENABLED = 1
IF_ADMINISTRATIVE_DEMANDDIAL = 2
IF_OPER_STATUS = Int32
IF_OPER_STATUS_IfOperStatusUp = 1
IF_OPER_STATUS_IfOperStatusDown = 2
IF_OPER_STATUS_IfOperStatusTesting = 3
IF_OPER_STATUS_IfOperStatusUnknown = 4
IF_OPER_STATUS_IfOperStatusDormant = 5
IF_OPER_STATUS_IfOperStatusNotPresent = 6
IF_OPER_STATUS_IfOperStatusLowerLayerDown = 7
def _define_NDIS_INTERFACE_INFORMATION_head():
    class NDIS_INTERFACE_INFORMATION(Structure):
        pass
    return NDIS_INTERFACE_INFORMATION
def _define_NDIS_INTERFACE_INFORMATION():
    NDIS_INTERFACE_INFORMATION = win32more.NetworkManagement.IpHelper.NDIS_INTERFACE_INFORMATION_head
    NDIS_INTERFACE_INFORMATION._fields_ = [
        ("ifOperStatus", win32more.NetworkManagement.IpHelper.NET_IF_OPER_STATUS),
        ("ifOperStatusFlags", UInt32),
        ("MediaConnectState", win32more.NetworkManagement.IpHelper.NET_IF_MEDIA_CONNECT_STATE),
        ("MediaDuplexState", win32more.NetworkManagement.IpHelper.NET_IF_MEDIA_DUPLEX_STATE),
        ("ifMtu", UInt32),
        ("ifPromiscuousMode", win32more.Foundation.BOOLEAN),
        ("ifDeviceWakeUpEnable", win32more.Foundation.BOOLEAN),
        ("XmitLinkSpeed", UInt64),
        ("RcvLinkSpeed", UInt64),
        ("ifLastChange", UInt64),
        ("ifCounterDiscontinuityTime", UInt64),
        ("ifInUnknownProtos", UInt64),
        ("ifInDiscards", UInt64),
        ("ifInErrors", UInt64),
        ("ifHCInOctets", UInt64),
        ("ifHCInUcastPkts", UInt64),
        ("ifHCInMulticastPkts", UInt64),
        ("ifHCInBroadcastPkts", UInt64),
        ("ifHCOutOctets", UInt64),
        ("ifHCOutUcastPkts", UInt64),
        ("ifHCOutMulticastPkts", UInt64),
        ("ifHCOutBroadcastPkts", UInt64),
        ("ifOutErrors", UInt64),
        ("ifOutDiscards", UInt64),
        ("ifHCInUcastOctets", UInt64),
        ("ifHCInMulticastOctets", UInt64),
        ("ifHCInBroadcastOctets", UInt64),
        ("ifHCOutUcastOctets", UInt64),
        ("ifHCOutMulticastOctets", UInt64),
        ("ifHCOutBroadcastOctets", UInt64),
        ("CompartmentId", UInt32),
        ("SupportedStatistics", UInt32),
    ]
    return NDIS_INTERFACE_INFORMATION
MIB_NOTIFICATION_TYPE = Int32
MIB_NOTIFICATION_TYPE_MibParameterNotification = 0
MIB_NOTIFICATION_TYPE_MibAddInstance = 1
MIB_NOTIFICATION_TYPE_MibDeleteInstance = 2
MIB_NOTIFICATION_TYPE_MibInitialNotification = 3
def _define_MIB_IF_ROW2_head():
    class MIB_IF_ROW2(Structure):
        pass
    return MIB_IF_ROW2
def _define_MIB_IF_ROW2():
    MIB_IF_ROW2 = win32more.NetworkManagement.IpHelper.MIB_IF_ROW2_head
    class MIB_IF_ROW2__InterfaceAndOperStatusFlags_e__Struct(Structure):
        pass
    MIB_IF_ROW2__InterfaceAndOperStatusFlags_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    MIB_IF_ROW2._fields_ = [
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("InterfaceIndex", UInt32),
        ("InterfaceGuid", Guid),
        ("Alias", Char * 257),
        ("Description", Char * 257),
        ("PhysicalAddressLength", UInt32),
        ("PhysicalAddress", Byte * 32),
        ("PermanentPhysicalAddress", Byte * 32),
        ("Mtu", UInt32),
        ("Type", UInt32),
        ("TunnelType", win32more.NetworkManagement.IpHelper.TUNNEL_TYPE),
        ("MediaType", win32more.NetworkManagement.Ndis.NDIS_MEDIUM),
        ("PhysicalMediumType", win32more.NetworkManagement.Ndis.NDIS_PHYSICAL_MEDIUM),
        ("AccessType", win32more.NetworkManagement.IpHelper.NET_IF_ACCESS_TYPE),
        ("DirectionType", win32more.NetworkManagement.IpHelper.NET_IF_DIRECTION_TYPE),
        ("InterfaceAndOperStatusFlags", MIB_IF_ROW2__InterfaceAndOperStatusFlags_e__Struct),
        ("OperStatus", win32more.NetworkManagement.IpHelper.IF_OPER_STATUS),
        ("AdminStatus", win32more.NetworkManagement.IpHelper.NET_IF_ADMIN_STATUS),
        ("MediaConnectState", win32more.NetworkManagement.IpHelper.NET_IF_MEDIA_CONNECT_STATE),
        ("NetworkGuid", Guid),
        ("ConnectionType", win32more.NetworkManagement.IpHelper.NET_IF_CONNECTION_TYPE),
        ("TransmitLinkSpeed", UInt64),
        ("ReceiveLinkSpeed", UInt64),
        ("InOctets", UInt64),
        ("InUcastPkts", UInt64),
        ("InNUcastPkts", UInt64),
        ("InDiscards", UInt64),
        ("InErrors", UInt64),
        ("InUnknownProtos", UInt64),
        ("InUcastOctets", UInt64),
        ("InMulticastOctets", UInt64),
        ("InBroadcastOctets", UInt64),
        ("OutOctets", UInt64),
        ("OutUcastPkts", UInt64),
        ("OutNUcastPkts", UInt64),
        ("OutDiscards", UInt64),
        ("OutErrors", UInt64),
        ("OutUcastOctets", UInt64),
        ("OutMulticastOctets", UInt64),
        ("OutBroadcastOctets", UInt64),
        ("OutQLen", UInt64),
    ]
    return MIB_IF_ROW2
def _define_MIB_IF_TABLE2_head():
    class MIB_IF_TABLE2(Structure):
        pass
    return MIB_IF_TABLE2
def _define_MIB_IF_TABLE2():
    MIB_IF_TABLE2 = win32more.NetworkManagement.IpHelper.MIB_IF_TABLE2_head
    MIB_IF_TABLE2._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_IF_ROW2 * 0),
    ]
    return MIB_IF_TABLE2
MIB_IF_ENTRY_LEVEL = Int32
MIB_IF_ENTRY_LEVEL_MibIfEntryNormal = 0
MIB_IF_ENTRY_LEVEL_MibIfEntryNormalWithoutStatistics = 2
MIB_IF_TABLE_LEVEL = Int32
MIB_IF_TABLE_LEVEL_MibIfTableNormal = 0
MIB_IF_TABLE_LEVEL_MibIfTableRaw = 1
MIB_IF_TABLE_LEVEL_MibIfTableNormalWithoutStatistics = 2
def _define_MIB_IPINTERFACE_ROW_head():
    class MIB_IPINTERFACE_ROW(Structure):
        pass
    return MIB_IPINTERFACE_ROW
def _define_MIB_IPINTERFACE_ROW():
    MIB_IPINTERFACE_ROW = win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head
    MIB_IPINTERFACE_ROW._fields_ = [
        ("Family", UInt16),
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("InterfaceIndex", UInt32),
        ("MaxReassemblySize", UInt32),
        ("InterfaceIdentifier", UInt64),
        ("MinRouterAdvertisementInterval", UInt32),
        ("MaxRouterAdvertisementInterval", UInt32),
        ("AdvertisingEnabled", win32more.Foundation.BOOLEAN),
        ("ForwardingEnabled", win32more.Foundation.BOOLEAN),
        ("WeakHostSend", win32more.Foundation.BOOLEAN),
        ("WeakHostReceive", win32more.Foundation.BOOLEAN),
        ("UseAutomaticMetric", win32more.Foundation.BOOLEAN),
        ("UseNeighborUnreachabilityDetection", win32more.Foundation.BOOLEAN),
        ("ManagedAddressConfigurationSupported", win32more.Foundation.BOOLEAN),
        ("OtherStatefulConfigurationSupported", win32more.Foundation.BOOLEAN),
        ("AdvertiseDefaultRoute", win32more.Foundation.BOOLEAN),
        ("RouterDiscoveryBehavior", win32more.Networking.WinSock.NL_ROUTER_DISCOVERY_BEHAVIOR),
        ("DadTransmits", UInt32),
        ("BaseReachableTime", UInt32),
        ("RetransmitTime", UInt32),
        ("PathMtuDiscoveryTimeout", UInt32),
        ("LinkLocalAddressBehavior", win32more.Networking.WinSock.NL_LINK_LOCAL_ADDRESS_BEHAVIOR),
        ("LinkLocalAddressTimeout", UInt32),
        ("ZoneIndices", UInt32 * 16),
        ("SitePrefixLength", UInt32),
        ("Metric", UInt32),
        ("NlMtu", UInt32),
        ("Connected", win32more.Foundation.BOOLEAN),
        ("SupportsWakeUpPatterns", win32more.Foundation.BOOLEAN),
        ("SupportsNeighborDiscovery", win32more.Foundation.BOOLEAN),
        ("SupportsRouterDiscovery", win32more.Foundation.BOOLEAN),
        ("ReachableTime", UInt32),
        ("TransmitOffload", win32more.Networking.WinSock.NL_INTERFACE_OFFLOAD_ROD),
        ("ReceiveOffload", win32more.Networking.WinSock.NL_INTERFACE_OFFLOAD_ROD),
        ("DisableDefaultRoutes", win32more.Foundation.BOOLEAN),
    ]
    return MIB_IPINTERFACE_ROW
def _define_MIB_IPINTERFACE_TABLE_head():
    class MIB_IPINTERFACE_TABLE(Structure):
        pass
    return MIB_IPINTERFACE_TABLE
def _define_MIB_IPINTERFACE_TABLE():
    MIB_IPINTERFACE_TABLE = win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_TABLE_head
    MIB_IPINTERFACE_TABLE._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW * 0),
    ]
    return MIB_IPINTERFACE_TABLE
def _define_MIB_IFSTACK_ROW_head():
    class MIB_IFSTACK_ROW(Structure):
        pass
    return MIB_IFSTACK_ROW
def _define_MIB_IFSTACK_ROW():
    MIB_IFSTACK_ROW = win32more.NetworkManagement.IpHelper.MIB_IFSTACK_ROW_head
    MIB_IFSTACK_ROW._fields_ = [
        ("HigherLayerInterfaceIndex", UInt32),
        ("LowerLayerInterfaceIndex", UInt32),
    ]
    return MIB_IFSTACK_ROW
def _define_MIB_INVERTEDIFSTACK_ROW_head():
    class MIB_INVERTEDIFSTACK_ROW(Structure):
        pass
    return MIB_INVERTEDIFSTACK_ROW
def _define_MIB_INVERTEDIFSTACK_ROW():
    MIB_INVERTEDIFSTACK_ROW = win32more.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_ROW_head
    MIB_INVERTEDIFSTACK_ROW._fields_ = [
        ("LowerLayerInterfaceIndex", UInt32),
        ("HigherLayerInterfaceIndex", UInt32),
    ]
    return MIB_INVERTEDIFSTACK_ROW
def _define_MIB_IFSTACK_TABLE_head():
    class MIB_IFSTACK_TABLE(Structure):
        pass
    return MIB_IFSTACK_TABLE
def _define_MIB_IFSTACK_TABLE():
    MIB_IFSTACK_TABLE = win32more.NetworkManagement.IpHelper.MIB_IFSTACK_TABLE_head
    MIB_IFSTACK_TABLE._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_IFSTACK_ROW * 0),
    ]
    return MIB_IFSTACK_TABLE
def _define_MIB_INVERTEDIFSTACK_TABLE_head():
    class MIB_INVERTEDIFSTACK_TABLE(Structure):
        pass
    return MIB_INVERTEDIFSTACK_TABLE
def _define_MIB_INVERTEDIFSTACK_TABLE():
    MIB_INVERTEDIFSTACK_TABLE = win32more.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_TABLE_head
    MIB_INVERTEDIFSTACK_TABLE._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_ROW * 0),
    ]
    return MIB_INVERTEDIFSTACK_TABLE
def _define_PIPINTERFACE_CHANGE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head),win32more.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE, use_last_error=False)
def _define_MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES_head():
    class MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES(Structure):
        pass
    return MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES
def _define_MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES():
    MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES = win32more.NetworkManagement.IpHelper.MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES_head
    MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES._fields_ = [
        ("InboundBandwidthInformation", win32more.Networking.WinSock.NL_BANDWIDTH_INFORMATION),
        ("OutboundBandwidthInformation", win32more.Networking.WinSock.NL_BANDWIDTH_INFORMATION),
    ]
    return MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES
def _define_MIB_UNICASTIPADDRESS_ROW_head():
    class MIB_UNICASTIPADDRESS_ROW(Structure):
        pass
    return MIB_UNICASTIPADDRESS_ROW
def _define_MIB_UNICASTIPADDRESS_ROW():
    MIB_UNICASTIPADDRESS_ROW = win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head
    MIB_UNICASTIPADDRESS_ROW._fields_ = [
        ("Address", win32more.Networking.WinSock.SOCKADDR_INET),
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("InterfaceIndex", UInt32),
        ("PrefixOrigin", win32more.Networking.WinSock.NL_PREFIX_ORIGIN),
        ("SuffixOrigin", win32more.Networking.WinSock.NL_SUFFIX_ORIGIN),
        ("ValidLifetime", UInt32),
        ("PreferredLifetime", UInt32),
        ("OnLinkPrefixLength", Byte),
        ("SkipAsSource", win32more.Foundation.BOOLEAN),
        ("DadState", win32more.Networking.WinSock.NL_DAD_STATE),
        ("ScopeId", win32more.Networking.WinSock.SCOPE_ID),
        ("CreationTimeStamp", win32more.Foundation.LARGE_INTEGER),
    ]
    return MIB_UNICASTIPADDRESS_ROW
def _define_MIB_UNICASTIPADDRESS_TABLE_head():
    class MIB_UNICASTIPADDRESS_TABLE(Structure):
        pass
    return MIB_UNICASTIPADDRESS_TABLE
def _define_MIB_UNICASTIPADDRESS_TABLE():
    MIB_UNICASTIPADDRESS_TABLE = win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE_head
    MIB_UNICASTIPADDRESS_TABLE._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW * 0),
    ]
    return MIB_UNICASTIPADDRESS_TABLE
def _define_PUNICAST_IPADDRESS_CHANGE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head),win32more.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE, use_last_error=False)
def _define_PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE_head), use_last_error=False)
def _define_MIB_ANYCASTIPADDRESS_ROW_head():
    class MIB_ANYCASTIPADDRESS_ROW(Structure):
        pass
    return MIB_ANYCASTIPADDRESS_ROW
def _define_MIB_ANYCASTIPADDRESS_ROW():
    MIB_ANYCASTIPADDRESS_ROW = win32more.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW_head
    MIB_ANYCASTIPADDRESS_ROW._fields_ = [
        ("Address", win32more.Networking.WinSock.SOCKADDR_INET),
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("InterfaceIndex", UInt32),
        ("ScopeId", win32more.Networking.WinSock.SCOPE_ID),
    ]
    return MIB_ANYCASTIPADDRESS_ROW
def _define_MIB_ANYCASTIPADDRESS_TABLE_head():
    class MIB_ANYCASTIPADDRESS_TABLE(Structure):
        pass
    return MIB_ANYCASTIPADDRESS_TABLE
def _define_MIB_ANYCASTIPADDRESS_TABLE():
    MIB_ANYCASTIPADDRESS_TABLE = win32more.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_TABLE_head
    MIB_ANYCASTIPADDRESS_TABLE._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW * 0),
    ]
    return MIB_ANYCASTIPADDRESS_TABLE
def _define_MIB_MULTICASTIPADDRESS_ROW_head():
    class MIB_MULTICASTIPADDRESS_ROW(Structure):
        pass
    return MIB_MULTICASTIPADDRESS_ROW
def _define_MIB_MULTICASTIPADDRESS_ROW():
    MIB_MULTICASTIPADDRESS_ROW = win32more.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_ROW_head
    MIB_MULTICASTIPADDRESS_ROW._fields_ = [
        ("Address", win32more.Networking.WinSock.SOCKADDR_INET),
        ("InterfaceIndex", UInt32),
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("ScopeId", win32more.Networking.WinSock.SCOPE_ID),
    ]
    return MIB_MULTICASTIPADDRESS_ROW
def _define_MIB_MULTICASTIPADDRESS_TABLE_head():
    class MIB_MULTICASTIPADDRESS_TABLE(Structure):
        pass
    return MIB_MULTICASTIPADDRESS_TABLE
def _define_MIB_MULTICASTIPADDRESS_TABLE():
    MIB_MULTICASTIPADDRESS_TABLE = win32more.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_TABLE_head
    MIB_MULTICASTIPADDRESS_TABLE._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_ROW * 0),
    ]
    return MIB_MULTICASTIPADDRESS_TABLE
def _define_IP_ADDRESS_PREFIX_head():
    class IP_ADDRESS_PREFIX(Structure):
        pass
    return IP_ADDRESS_PREFIX
def _define_IP_ADDRESS_PREFIX():
    IP_ADDRESS_PREFIX = win32more.NetworkManagement.IpHelper.IP_ADDRESS_PREFIX_head
    IP_ADDRESS_PREFIX._fields_ = [
        ("Prefix", win32more.Networking.WinSock.SOCKADDR_INET),
        ("PrefixLength", Byte),
    ]
    return IP_ADDRESS_PREFIX
def _define_MIB_IPFORWARD_ROW2_head():
    class MIB_IPFORWARD_ROW2(Structure):
        pass
    return MIB_IPFORWARD_ROW2
def _define_MIB_IPFORWARD_ROW2():
    MIB_IPFORWARD_ROW2 = win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head
    MIB_IPFORWARD_ROW2._fields_ = [
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("InterfaceIndex", UInt32),
        ("DestinationPrefix", win32more.NetworkManagement.IpHelper.IP_ADDRESS_PREFIX),
        ("NextHop", win32more.Networking.WinSock.SOCKADDR_INET),
        ("SitePrefixLength", Byte),
        ("ValidLifetime", UInt32),
        ("PreferredLifetime", UInt32),
        ("Metric", UInt32),
        ("Protocol", win32more.Networking.WinSock.NL_ROUTE_PROTOCOL),
        ("Loopback", win32more.Foundation.BOOLEAN),
        ("AutoconfigureAddress", win32more.Foundation.BOOLEAN),
        ("Publish", win32more.Foundation.BOOLEAN),
        ("Immortal", win32more.Foundation.BOOLEAN),
        ("Age", UInt32),
        ("Origin", win32more.Networking.WinSock.NL_ROUTE_ORIGIN),
    ]
    return MIB_IPFORWARD_ROW2
def _define_MIB_IPFORWARD_TABLE2_head():
    class MIB_IPFORWARD_TABLE2(Structure):
        pass
    return MIB_IPFORWARD_TABLE2
def _define_MIB_IPFORWARD_TABLE2():
    MIB_IPFORWARD_TABLE2 = win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_TABLE2_head
    MIB_IPFORWARD_TABLE2._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2 * 0),
    ]
    return MIB_IPFORWARD_TABLE2
def _define_PIPFORWARD_CHANGE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head),win32more.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE, use_last_error=False)
def _define_MIB_IPPATH_ROW_head():
    class MIB_IPPATH_ROW(Structure):
        pass
    return MIB_IPPATH_ROW
def _define_MIB_IPPATH_ROW():
    MIB_IPPATH_ROW = win32more.NetworkManagement.IpHelper.MIB_IPPATH_ROW_head
    class MIB_IPPATH_ROW__Anonymous_e__Union(Union):
        pass
    MIB_IPPATH_ROW__Anonymous_e__Union._fields_ = [
        ("LastReachable", UInt32),
        ("LastUnreachable", UInt32),
    ]
    MIB_IPPATH_ROW._anonymous_ = [
        'Anonymous',
    ]
    MIB_IPPATH_ROW._fields_ = [
        ("Source", win32more.Networking.WinSock.SOCKADDR_INET),
        ("Destination", win32more.Networking.WinSock.SOCKADDR_INET),
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("InterfaceIndex", UInt32),
        ("CurrentNextHop", win32more.Networking.WinSock.SOCKADDR_INET),
        ("PathMtu", UInt32),
        ("RttMean", UInt32),
        ("RttDeviation", UInt32),
        ("Anonymous", MIB_IPPATH_ROW__Anonymous_e__Union),
        ("IsReachable", win32more.Foundation.BOOLEAN),
        ("LinkTransmitSpeed", UInt64),
        ("LinkReceiveSpeed", UInt64),
    ]
    return MIB_IPPATH_ROW
def _define_MIB_IPPATH_TABLE_head():
    class MIB_IPPATH_TABLE(Structure):
        pass
    return MIB_IPPATH_TABLE
def _define_MIB_IPPATH_TABLE():
    MIB_IPPATH_TABLE = win32more.NetworkManagement.IpHelper.MIB_IPPATH_TABLE_head
    MIB_IPPATH_TABLE._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_IPPATH_ROW * 0),
    ]
    return MIB_IPPATH_TABLE
def _define_MIB_IPNET_ROW2_head():
    class MIB_IPNET_ROW2(Structure):
        pass
    return MIB_IPNET_ROW2
def _define_MIB_IPNET_ROW2():
    MIB_IPNET_ROW2 = win32more.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head
    class MIB_IPNET_ROW2__Anonymous_e__Union(Union):
        pass
    class MIB_IPNET_ROW2__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIB_IPNET_ROW2__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    MIB_IPNET_ROW2__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIB_IPNET_ROW2__Anonymous_e__Union._fields_ = [
        ("Anonymous", MIB_IPNET_ROW2__Anonymous_e__Union__Anonymous_e__Struct),
        ("Flags", Byte),
    ]
    class MIB_IPNET_ROW2__ReachabilityTime_e__Union(Union):
        pass
    MIB_IPNET_ROW2__ReachabilityTime_e__Union._fields_ = [
        ("LastReachable", UInt32),
        ("LastUnreachable", UInt32),
    ]
    MIB_IPNET_ROW2._anonymous_ = [
        'Anonymous',
    ]
    MIB_IPNET_ROW2._fields_ = [
        ("Address", win32more.Networking.WinSock.SOCKADDR_INET),
        ("InterfaceIndex", UInt32),
        ("InterfaceLuid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("PhysicalAddress", Byte * 32),
        ("PhysicalAddressLength", UInt32),
        ("State", win32more.Networking.WinSock.NL_NEIGHBOR_STATE),
        ("Anonymous", MIB_IPNET_ROW2__Anonymous_e__Union),
        ("ReachabilityTime", MIB_IPNET_ROW2__ReachabilityTime_e__Union),
    ]
    return MIB_IPNET_ROW2
def _define_MIB_IPNET_TABLE2_head():
    class MIB_IPNET_TABLE2(Structure):
        pass
    return MIB_IPNET_TABLE2
def _define_MIB_IPNET_TABLE2():
    MIB_IPNET_TABLE2 = win32more.NetworkManagement.IpHelper.MIB_IPNET_TABLE2_head
    MIB_IPNET_TABLE2._fields_ = [
        ("NumEntries", UInt32),
        ("Table", win32more.NetworkManagement.IpHelper.MIB_IPNET_ROW2 * 0),
    ]
    return MIB_IPNET_TABLE2
def _define_PTEREDO_PORT_CHANGE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,UInt16,win32more.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE, use_last_error=False)
def _define_DNS_SETTINGS_head():
    class DNS_SETTINGS(Structure):
        pass
    return DNS_SETTINGS
def _define_DNS_SETTINGS():
    DNS_SETTINGS = win32more.NetworkManagement.IpHelper.DNS_SETTINGS_head
    DNS_SETTINGS._fields_ = [
        ("Version", UInt32),
        ("Flags", UInt64),
        ("Hostname", win32more.Foundation.PWSTR),
        ("Domain", win32more.Foundation.PWSTR),
        ("SearchList", win32more.Foundation.PWSTR),
    ]
    return DNS_SETTINGS
def _define_DNS_SETTINGS2_head():
    class DNS_SETTINGS2(Structure):
        pass
    return DNS_SETTINGS2
def _define_DNS_SETTINGS2():
    DNS_SETTINGS2 = win32more.NetworkManagement.IpHelper.DNS_SETTINGS2_head
    DNS_SETTINGS2._fields_ = [
        ("Version", UInt32),
        ("Flags", UInt64),
        ("Hostname", win32more.Foundation.PWSTR),
        ("Domain", win32more.Foundation.PWSTR),
        ("SearchList", win32more.Foundation.PWSTR),
        ("SettingFlags", UInt64),
    ]
    return DNS_SETTINGS2
def _define_DNS_DOH_SERVER_SETTINGS_head():
    class DNS_DOH_SERVER_SETTINGS(Structure):
        pass
    return DNS_DOH_SERVER_SETTINGS
def _define_DNS_DOH_SERVER_SETTINGS():
    DNS_DOH_SERVER_SETTINGS = win32more.NetworkManagement.IpHelper.DNS_DOH_SERVER_SETTINGS_head
    DNS_DOH_SERVER_SETTINGS._fields_ = [
        ("Template", win32more.Foundation.PWSTR),
        ("Flags", UInt64),
    ]
    return DNS_DOH_SERVER_SETTINGS
DNS_SERVER_PROPERTY_TYPE = Int32
DNS_SERVER_PROPERTY_TYPE_DnsServerInvalidProperty = 0
DNS_SERVER_PROPERTY_TYPE_DnsServerDohProperty = 1
def _define_DNS_SERVER_PROPERTY_TYPES_head():
    class DNS_SERVER_PROPERTY_TYPES(Union):
        pass
    return DNS_SERVER_PROPERTY_TYPES
def _define_DNS_SERVER_PROPERTY_TYPES():
    DNS_SERVER_PROPERTY_TYPES = win32more.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPES_head
    DNS_SERVER_PROPERTY_TYPES._fields_ = [
        ("DohSettings", POINTER(win32more.NetworkManagement.IpHelper.DNS_DOH_SERVER_SETTINGS_head)),
    ]
    return DNS_SERVER_PROPERTY_TYPES
def _define_DNS_SERVER_PROPERTY_head():
    class DNS_SERVER_PROPERTY(Structure):
        pass
    return DNS_SERVER_PROPERTY
def _define_DNS_SERVER_PROPERTY():
    DNS_SERVER_PROPERTY = win32more.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_head
    DNS_SERVER_PROPERTY._fields_ = [
        ("Version", UInt32),
        ("ServerIndex", UInt32),
        ("Type", win32more.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPE),
        ("Property", win32more.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPES),
    ]
    return DNS_SERVER_PROPERTY
def _define_DNS_INTERFACE_SETTINGS_head():
    class DNS_INTERFACE_SETTINGS(Structure):
        pass
    return DNS_INTERFACE_SETTINGS
def _define_DNS_INTERFACE_SETTINGS():
    DNS_INTERFACE_SETTINGS = win32more.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_head
    DNS_INTERFACE_SETTINGS._fields_ = [
        ("Version", UInt32),
        ("Flags", UInt64),
        ("Domain", win32more.Foundation.PWSTR),
        ("NameServer", win32more.Foundation.PWSTR),
        ("SearchList", win32more.Foundation.PWSTR),
        ("RegistrationEnabled", UInt32),
        ("RegisterAdapterName", UInt32),
        ("EnableLLMNR", UInt32),
        ("QueryAdapterName", UInt32),
        ("ProfileNameServer", win32more.Foundation.PWSTR),
    ]
    return DNS_INTERFACE_SETTINGS
def _define_DNS_INTERFACE_SETTINGS_EX_head():
    class DNS_INTERFACE_SETTINGS_EX(Structure):
        pass
    return DNS_INTERFACE_SETTINGS_EX
def _define_DNS_INTERFACE_SETTINGS_EX():
    DNS_INTERFACE_SETTINGS_EX = win32more.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_EX_head
    DNS_INTERFACE_SETTINGS_EX._fields_ = [
        ("SettingsV1", win32more.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS),
        ("DisableUnconstrainedQueries", UInt32),
        ("SupplementalSearchList", win32more.Foundation.PWSTR),
    ]
    return DNS_INTERFACE_SETTINGS_EX
def _define_DNS_INTERFACE_SETTINGS3_head():
    class DNS_INTERFACE_SETTINGS3(Structure):
        pass
    return DNS_INTERFACE_SETTINGS3
def _define_DNS_INTERFACE_SETTINGS3():
    DNS_INTERFACE_SETTINGS3 = win32more.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS3_head
    DNS_INTERFACE_SETTINGS3._fields_ = [
        ("Version", UInt32),
        ("Flags", UInt64),
        ("Domain", win32more.Foundation.PWSTR),
        ("NameServer", win32more.Foundation.PWSTR),
        ("SearchList", win32more.Foundation.PWSTR),
        ("RegistrationEnabled", UInt32),
        ("RegisterAdapterName", UInt32),
        ("EnableLLMNR", UInt32),
        ("QueryAdapterName", UInt32),
        ("ProfileNameServer", win32more.Foundation.PWSTR),
        ("DisableUnconstrainedQueries", UInt32),
        ("SupplementalSearchList", win32more.Foundation.PWSTR),
        ("cServerProperties", UInt32),
        ("ServerProperties", POINTER(win32more.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_head)),
        ("cProfileServerProperties", UInt32),
        ("ProfileServerProperties", POINTER(win32more.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_head)),
    ]
    return DNS_INTERFACE_SETTINGS3
def _define_PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,win32more.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT, use_last_error=False)
def _define_MIB_OPAQUE_QUERY_head():
    class MIB_OPAQUE_QUERY(Structure):
        pass
    return MIB_OPAQUE_QUERY
def _define_MIB_OPAQUE_QUERY():
    MIB_OPAQUE_QUERY = win32more.NetworkManagement.IpHelper.MIB_OPAQUE_QUERY_head
    MIB_OPAQUE_QUERY._fields_ = [
        ("dwVarId", UInt32),
        ("rgdwVarIndex", UInt32 * 0),
    ]
    return MIB_OPAQUE_QUERY
def _define_MIB_IFNUMBER_head():
    class MIB_IFNUMBER(Structure):
        pass
    return MIB_IFNUMBER
def _define_MIB_IFNUMBER():
    MIB_IFNUMBER = win32more.NetworkManagement.IpHelper.MIB_IFNUMBER_head
    MIB_IFNUMBER._fields_ = [
        ("dwValue", UInt32),
    ]
    return MIB_IFNUMBER
def _define_MIB_IFROW_head():
    class MIB_IFROW(Structure):
        pass
    return MIB_IFROW
def _define_MIB_IFROW():
    MIB_IFROW = win32more.NetworkManagement.IpHelper.MIB_IFROW_head
    MIB_IFROW._fields_ = [
        ("wszName", Char * 256),
        ("dwIndex", UInt32),
        ("dwType", UInt32),
        ("dwMtu", UInt32),
        ("dwSpeed", UInt32),
        ("dwPhysAddrLen", UInt32),
        ("bPhysAddr", Byte * 8),
        ("dwAdminStatus", UInt32),
        ("dwOperStatus", win32more.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS),
        ("dwLastChange", UInt32),
        ("dwInOctets", UInt32),
        ("dwInUcastPkts", UInt32),
        ("dwInNUcastPkts", UInt32),
        ("dwInDiscards", UInt32),
        ("dwInErrors", UInt32),
        ("dwInUnknownProtos", UInt32),
        ("dwOutOctets", UInt32),
        ("dwOutUcastPkts", UInt32),
        ("dwOutNUcastPkts", UInt32),
        ("dwOutDiscards", UInt32),
        ("dwOutErrors", UInt32),
        ("dwOutQLen", UInt32),
        ("dwDescrLen", UInt32),
        ("bDescr", Byte * 256),
    ]
    return MIB_IFROW
def _define_MIB_IFTABLE_head():
    class MIB_IFTABLE(Structure):
        pass
    return MIB_IFTABLE
def _define_MIB_IFTABLE():
    MIB_IFTABLE = win32more.NetworkManagement.IpHelper.MIB_IFTABLE_head
    MIB_IFTABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IFROW * 0),
    ]
    return MIB_IFTABLE
def _define_MIB_IPADDRROW_XP_head():
    class MIB_IPADDRROW_XP(Structure):
        pass
    return MIB_IPADDRROW_XP
def _define_MIB_IPADDRROW_XP():
    MIB_IPADDRROW_XP = win32more.NetworkManagement.IpHelper.MIB_IPADDRROW_XP_head
    MIB_IPADDRROW_XP._fields_ = [
        ("dwAddr", UInt32),
        ("dwIndex", UInt32),
        ("dwMask", UInt32),
        ("dwBCastAddr", UInt32),
        ("dwReasmSize", UInt32),
        ("unused1", UInt16),
        ("wType", UInt16),
    ]
    return MIB_IPADDRROW_XP
def _define_MIB_IPADDRROW_W2K_head():
    class MIB_IPADDRROW_W2K(Structure):
        pass
    return MIB_IPADDRROW_W2K
def _define_MIB_IPADDRROW_W2K():
    MIB_IPADDRROW_W2K = win32more.NetworkManagement.IpHelper.MIB_IPADDRROW_W2K_head
    MIB_IPADDRROW_W2K._fields_ = [
        ("dwAddr", UInt32),
        ("dwIndex", UInt32),
        ("dwMask", UInt32),
        ("dwBCastAddr", UInt32),
        ("dwReasmSize", UInt32),
        ("unused1", UInt16),
        ("unused2", UInt16),
    ]
    return MIB_IPADDRROW_W2K
def _define_MIB_IPADDRTABLE_head():
    class MIB_IPADDRTABLE(Structure):
        pass
    return MIB_IPADDRTABLE
def _define_MIB_IPADDRTABLE():
    MIB_IPADDRTABLE = win32more.NetworkManagement.IpHelper.MIB_IPADDRTABLE_head
    MIB_IPADDRTABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPADDRROW_XP * 0),
    ]
    return MIB_IPADDRTABLE
def _define_MIB_IPFORWARDNUMBER_head():
    class MIB_IPFORWARDNUMBER(Structure):
        pass
    return MIB_IPFORWARDNUMBER
def _define_MIB_IPFORWARDNUMBER():
    MIB_IPFORWARDNUMBER = win32more.NetworkManagement.IpHelper.MIB_IPFORWARDNUMBER_head
    MIB_IPFORWARDNUMBER._fields_ = [
        ("dwValue", UInt32),
    ]
    return MIB_IPFORWARDNUMBER
MIB_IPFORWARD_TYPE = Int32
MIB_IPROUTE_TYPE_OTHER = 1
MIB_IPROUTE_TYPE_INVALID = 2
MIB_IPROUTE_TYPE_DIRECT = 3
MIB_IPROUTE_TYPE_INDIRECT = 4
def _define_MIB_IPFORWARDROW_head():
    class MIB_IPFORWARDROW(Structure):
        pass
    return MIB_IPFORWARDROW
def _define_MIB_IPFORWARDROW():
    MIB_IPFORWARDROW = win32more.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head
    class MIB_IPFORWARDROW__Anonymous1_e__Union(Union):
        pass
    MIB_IPFORWARDROW__Anonymous1_e__Union._fields_ = [
        ("dwForwardType", UInt32),
        ("ForwardType", win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_TYPE),
    ]
    class MIB_IPFORWARDROW__Anonymous2_e__Union(Union):
        pass
    MIB_IPFORWARDROW__Anonymous2_e__Union._fields_ = [
        ("dwForwardProto", UInt32),
        ("ForwardProto", win32more.Networking.WinSock.NL_ROUTE_PROTOCOL),
    ]
    MIB_IPFORWARDROW._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    MIB_IPFORWARDROW._fields_ = [
        ("dwForwardDest", UInt32),
        ("dwForwardMask", UInt32),
        ("dwForwardPolicy", UInt32),
        ("dwForwardNextHop", UInt32),
        ("dwForwardIfIndex", UInt32),
        ("Anonymous1", MIB_IPFORWARDROW__Anonymous1_e__Union),
        ("Anonymous2", MIB_IPFORWARDROW__Anonymous2_e__Union),
        ("dwForwardAge", UInt32),
        ("dwForwardNextHopAS", UInt32),
        ("dwForwardMetric1", UInt32),
        ("dwForwardMetric2", UInt32),
        ("dwForwardMetric3", UInt32),
        ("dwForwardMetric4", UInt32),
        ("dwForwardMetric5", UInt32),
    ]
    return MIB_IPFORWARDROW
def _define_MIB_IPFORWARDTABLE_head():
    class MIB_IPFORWARDTABLE(Structure):
        pass
    return MIB_IPFORWARDTABLE
def _define_MIB_IPFORWARDTABLE():
    MIB_IPFORWARDTABLE = win32more.NetworkManagement.IpHelper.MIB_IPFORWARDTABLE_head
    MIB_IPFORWARDTABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPFORWARDROW * 0),
    ]
    return MIB_IPFORWARDTABLE
MIB_IPNET_TYPE = Int32
MIB_IPNET_TYPE_OTHER = 1
MIB_IPNET_TYPE_INVALID = 2
MIB_IPNET_TYPE_DYNAMIC = 3
MIB_IPNET_TYPE_STATIC = 4
def _define_MIB_IPNETROW_LH_head():
    class MIB_IPNETROW_LH(Structure):
        pass
    return MIB_IPNETROW_LH
def _define_MIB_IPNETROW_LH():
    MIB_IPNETROW_LH = win32more.NetworkManagement.IpHelper.MIB_IPNETROW_LH_head
    class MIB_IPNETROW_LH__Anonymous_e__Union(Union):
        pass
    MIB_IPNETROW_LH__Anonymous_e__Union._fields_ = [
        ("dwType", UInt32),
        ("Type", win32more.NetworkManagement.IpHelper.MIB_IPNET_TYPE),
    ]
    MIB_IPNETROW_LH._anonymous_ = [
        'Anonymous',
    ]
    MIB_IPNETROW_LH._fields_ = [
        ("dwIndex", UInt32),
        ("dwPhysAddrLen", UInt32),
        ("bPhysAddr", Byte * 8),
        ("dwAddr", UInt32),
        ("Anonymous", MIB_IPNETROW_LH__Anonymous_e__Union),
    ]
    return MIB_IPNETROW_LH
def _define_MIB_IPNETROW_W2K_head():
    class MIB_IPNETROW_W2K(Structure):
        pass
    return MIB_IPNETROW_W2K
def _define_MIB_IPNETROW_W2K():
    MIB_IPNETROW_W2K = win32more.NetworkManagement.IpHelper.MIB_IPNETROW_W2K_head
    MIB_IPNETROW_W2K._fields_ = [
        ("dwIndex", UInt32),
        ("dwPhysAddrLen", UInt32),
        ("bPhysAddr", Byte * 8),
        ("dwAddr", UInt32),
        ("dwType", UInt32),
    ]
    return MIB_IPNETROW_W2K
def _define_MIB_IPNETTABLE_head():
    class MIB_IPNETTABLE(Structure):
        pass
    return MIB_IPNETTABLE
def _define_MIB_IPNETTABLE():
    MIB_IPNETTABLE = win32more.NetworkManagement.IpHelper.MIB_IPNETTABLE_head
    MIB_IPNETTABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPNETROW_LH * 0),
    ]
    return MIB_IPNETTABLE
MIB_IPSTATS_FORWARDING = Int32
MIB_IP_FORWARDING = 1
MIB_IP_NOT_FORWARDING = 2
def _define_MIB_IPSTATS_LH_head():
    class MIB_IPSTATS_LH(Structure):
        pass
    return MIB_IPSTATS_LH
def _define_MIB_IPSTATS_LH():
    MIB_IPSTATS_LH = win32more.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head
    class MIB_IPSTATS_LH__Anonymous_e__Union(Union):
        pass
    MIB_IPSTATS_LH__Anonymous_e__Union._fields_ = [
        ("dwForwarding", UInt32),
        ("Forwarding", win32more.NetworkManagement.IpHelper.MIB_IPSTATS_FORWARDING),
    ]
    MIB_IPSTATS_LH._anonymous_ = [
        'Anonymous',
    ]
    MIB_IPSTATS_LH._fields_ = [
        ("Anonymous", MIB_IPSTATS_LH__Anonymous_e__Union),
        ("dwDefaultTTL", UInt32),
        ("dwInReceives", UInt32),
        ("dwInHdrErrors", UInt32),
        ("dwInAddrErrors", UInt32),
        ("dwForwDatagrams", UInt32),
        ("dwInUnknownProtos", UInt32),
        ("dwInDiscards", UInt32),
        ("dwInDelivers", UInt32),
        ("dwOutRequests", UInt32),
        ("dwRoutingDiscards", UInt32),
        ("dwOutDiscards", UInt32),
        ("dwOutNoRoutes", UInt32),
        ("dwReasmTimeout", UInt32),
        ("dwReasmReqds", UInt32),
        ("dwReasmOks", UInt32),
        ("dwReasmFails", UInt32),
        ("dwFragOks", UInt32),
        ("dwFragFails", UInt32),
        ("dwFragCreates", UInt32),
        ("dwNumIf", UInt32),
        ("dwNumAddr", UInt32),
        ("dwNumRoutes", UInt32),
    ]
    return MIB_IPSTATS_LH
def _define_MIB_IPSTATS_W2K_head():
    class MIB_IPSTATS_W2K(Structure):
        pass
    return MIB_IPSTATS_W2K
def _define_MIB_IPSTATS_W2K():
    MIB_IPSTATS_W2K = win32more.NetworkManagement.IpHelper.MIB_IPSTATS_W2K_head
    MIB_IPSTATS_W2K._fields_ = [
        ("dwForwarding", UInt32),
        ("dwDefaultTTL", UInt32),
        ("dwInReceives", UInt32),
        ("dwInHdrErrors", UInt32),
        ("dwInAddrErrors", UInt32),
        ("dwForwDatagrams", UInt32),
        ("dwInUnknownProtos", UInt32),
        ("dwInDiscards", UInt32),
        ("dwInDelivers", UInt32),
        ("dwOutRequests", UInt32),
        ("dwRoutingDiscards", UInt32),
        ("dwOutDiscards", UInt32),
        ("dwOutNoRoutes", UInt32),
        ("dwReasmTimeout", UInt32),
        ("dwReasmReqds", UInt32),
        ("dwReasmOks", UInt32),
        ("dwReasmFails", UInt32),
        ("dwFragOks", UInt32),
        ("dwFragFails", UInt32),
        ("dwFragCreates", UInt32),
        ("dwNumIf", UInt32),
        ("dwNumAddr", UInt32),
        ("dwNumRoutes", UInt32),
    ]
    return MIB_IPSTATS_W2K
def _define_MIBICMPSTATS_head():
    class MIBICMPSTATS(Structure):
        pass
    return MIBICMPSTATS
def _define_MIBICMPSTATS():
    MIBICMPSTATS = win32more.NetworkManagement.IpHelper.MIBICMPSTATS_head
    MIBICMPSTATS._fields_ = [
        ("dwMsgs", UInt32),
        ("dwErrors", UInt32),
        ("dwDestUnreachs", UInt32),
        ("dwTimeExcds", UInt32),
        ("dwParmProbs", UInt32),
        ("dwSrcQuenchs", UInt32),
        ("dwRedirects", UInt32),
        ("dwEchos", UInt32),
        ("dwEchoReps", UInt32),
        ("dwTimestamps", UInt32),
        ("dwTimestampReps", UInt32),
        ("dwAddrMasks", UInt32),
        ("dwAddrMaskReps", UInt32),
    ]
    return MIBICMPSTATS
def _define_MIBICMPINFO_head():
    class MIBICMPINFO(Structure):
        pass
    return MIBICMPINFO
def _define_MIBICMPINFO():
    MIBICMPINFO = win32more.NetworkManagement.IpHelper.MIBICMPINFO_head
    MIBICMPINFO._fields_ = [
        ("icmpInStats", win32more.NetworkManagement.IpHelper.MIBICMPSTATS),
        ("icmpOutStats", win32more.NetworkManagement.IpHelper.MIBICMPSTATS),
    ]
    return MIBICMPINFO
def _define_MIB_ICMP_head():
    class MIB_ICMP(Structure):
        pass
    return MIB_ICMP
def _define_MIB_ICMP():
    MIB_ICMP = win32more.NetworkManagement.IpHelper.MIB_ICMP_head
    MIB_ICMP._fields_ = [
        ("stats", win32more.NetworkManagement.IpHelper.MIBICMPINFO),
    ]
    return MIB_ICMP
def _define_MIBICMPSTATS_EX_XPSP1_head():
    class MIBICMPSTATS_EX_XPSP1(Structure):
        pass
    return MIBICMPSTATS_EX_XPSP1
def _define_MIBICMPSTATS_EX_XPSP1():
    MIBICMPSTATS_EX_XPSP1 = win32more.NetworkManagement.IpHelper.MIBICMPSTATS_EX_XPSP1_head
    MIBICMPSTATS_EX_XPSP1._fields_ = [
        ("dwMsgs", UInt32),
        ("dwErrors", UInt32),
        ("rgdwTypeCount", UInt32 * 256),
    ]
    return MIBICMPSTATS_EX_XPSP1
def _define_MIB_ICMP_EX_XPSP1_head():
    class MIB_ICMP_EX_XPSP1(Structure):
        pass
    return MIB_ICMP_EX_XPSP1
def _define_MIB_ICMP_EX_XPSP1():
    MIB_ICMP_EX_XPSP1 = win32more.NetworkManagement.IpHelper.MIB_ICMP_EX_XPSP1_head
    MIB_ICMP_EX_XPSP1._fields_ = [
        ("icmpInStats", win32more.NetworkManagement.IpHelper.MIBICMPSTATS_EX_XPSP1),
        ("icmpOutStats", win32more.NetworkManagement.IpHelper.MIBICMPSTATS_EX_XPSP1),
    ]
    return MIB_ICMP_EX_XPSP1
ICMP6_TYPE = Int32
ICMP6_DST_UNREACH = 1
ICMP6_PACKET_TOO_BIG = 2
ICMP6_TIME_EXCEEDED = 3
ICMP6_PARAM_PROB = 4
ICMP6_ECHO_REQUEST = 128
ICMP6_ECHO_REPLY = 129
ICMP6_MEMBERSHIP_QUERY = 130
ICMP6_MEMBERSHIP_REPORT = 131
ICMP6_MEMBERSHIP_REDUCTION = 132
ND_ROUTER_SOLICIT = 133
ND_ROUTER_ADVERT = 134
ND_NEIGHBOR_SOLICIT = 135
ND_NEIGHBOR_ADVERT = 136
ND_REDIRECT = 137
ICMP6_V2_MEMBERSHIP_REPORT = 143
ICMP4_TYPE = Int32
ICMP4_ECHO_REPLY = 0
ICMP4_DST_UNREACH = 3
ICMP4_SOURCE_QUENCH = 4
ICMP4_REDIRECT = 5
ICMP4_ECHO_REQUEST = 8
ICMP4_ROUTER_ADVERT = 9
ICMP4_ROUTER_SOLICIT = 10
ICMP4_TIME_EXCEEDED = 11
ICMP4_PARAM_PROB = 12
ICMP4_TIMESTAMP_REQUEST = 13
ICMP4_TIMESTAMP_REPLY = 14
ICMP4_MASK_REQUEST = 17
ICMP4_MASK_REPLY = 18
def _define_MIB_IPMCAST_OIF_XP_head():
    class MIB_IPMCAST_OIF_XP(Structure):
        pass
    return MIB_IPMCAST_OIF_XP
def _define_MIB_IPMCAST_OIF_XP():
    MIB_IPMCAST_OIF_XP = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_XP_head
    MIB_IPMCAST_OIF_XP._fields_ = [
        ("dwOutIfIndex", UInt32),
        ("dwNextHopAddr", UInt32),
        ("dwReserved", UInt32),
        ("dwReserved1", UInt32),
    ]
    return MIB_IPMCAST_OIF_XP
def _define_MIB_IPMCAST_OIF_W2K_head():
    class MIB_IPMCAST_OIF_W2K(Structure):
        pass
    return MIB_IPMCAST_OIF_W2K
def _define_MIB_IPMCAST_OIF_W2K():
    MIB_IPMCAST_OIF_W2K = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_W2K_head
    MIB_IPMCAST_OIF_W2K._fields_ = [
        ("dwOutIfIndex", UInt32),
        ("dwNextHopAddr", UInt32),
        ("pvReserved", c_void_p),
        ("dwReserved", UInt32),
    ]
    return MIB_IPMCAST_OIF_W2K
def _define_MIB_IPMCAST_MFE_head():
    class MIB_IPMCAST_MFE(Structure):
        pass
    return MIB_IPMCAST_MFE
def _define_MIB_IPMCAST_MFE():
    MIB_IPMCAST_MFE = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_head
    MIB_IPMCAST_MFE._fields_ = [
        ("dwGroup", UInt32),
        ("dwSource", UInt32),
        ("dwSrcMask", UInt32),
        ("dwUpStrmNgbr", UInt32),
        ("dwInIfIndex", UInt32),
        ("dwInIfProtocol", UInt32),
        ("dwRouteProtocol", UInt32),
        ("dwRouteNetwork", UInt32),
        ("dwRouteMask", UInt32),
        ("ulUpTime", UInt32),
        ("ulExpiryTime", UInt32),
        ("ulTimeOut", UInt32),
        ("ulNumOutIf", UInt32),
        ("fFlags", UInt32),
        ("dwReserved", UInt32),
        ("rgmioOutInfo", win32more.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_XP * 0),
    ]
    return MIB_IPMCAST_MFE
def _define_MIB_MFE_TABLE_head():
    class MIB_MFE_TABLE(Structure):
        pass
    return MIB_MFE_TABLE
def _define_MIB_MFE_TABLE():
    MIB_MFE_TABLE = win32more.NetworkManagement.IpHelper.MIB_MFE_TABLE_head
    MIB_MFE_TABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE * 0),
    ]
    return MIB_MFE_TABLE
def _define_MIB_IPMCAST_OIF_STATS_LH_head():
    class MIB_IPMCAST_OIF_STATS_LH(Structure):
        pass
    return MIB_IPMCAST_OIF_STATS_LH
def _define_MIB_IPMCAST_OIF_STATS_LH():
    MIB_IPMCAST_OIF_STATS_LH = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_LH_head
    MIB_IPMCAST_OIF_STATS_LH._fields_ = [
        ("dwOutIfIndex", UInt32),
        ("dwNextHopAddr", UInt32),
        ("dwDialContext", UInt32),
        ("ulTtlTooLow", UInt32),
        ("ulFragNeeded", UInt32),
        ("ulOutPackets", UInt32),
        ("ulOutDiscards", UInt32),
    ]
    return MIB_IPMCAST_OIF_STATS_LH
def _define_MIB_IPMCAST_OIF_STATS_W2K_head():
    class MIB_IPMCAST_OIF_STATS_W2K(Structure):
        pass
    return MIB_IPMCAST_OIF_STATS_W2K
def _define_MIB_IPMCAST_OIF_STATS_W2K():
    MIB_IPMCAST_OIF_STATS_W2K = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_W2K_head
    MIB_IPMCAST_OIF_STATS_W2K._fields_ = [
        ("dwOutIfIndex", UInt32),
        ("dwNextHopAddr", UInt32),
        ("pvDialContext", c_void_p),
        ("ulTtlTooLow", UInt32),
        ("ulFragNeeded", UInt32),
        ("ulOutPackets", UInt32),
        ("ulOutDiscards", UInt32),
    ]
    return MIB_IPMCAST_OIF_STATS_W2K
def _define_MIB_IPMCAST_MFE_STATS_head():
    class MIB_IPMCAST_MFE_STATS(Structure):
        pass
    return MIB_IPMCAST_MFE_STATS
def _define_MIB_IPMCAST_MFE_STATS():
    MIB_IPMCAST_MFE_STATS = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS_head
    MIB_IPMCAST_MFE_STATS._fields_ = [
        ("dwGroup", UInt32),
        ("dwSource", UInt32),
        ("dwSrcMask", UInt32),
        ("dwUpStrmNgbr", UInt32),
        ("dwInIfIndex", UInt32),
        ("dwInIfProtocol", UInt32),
        ("dwRouteProtocol", UInt32),
        ("dwRouteNetwork", UInt32),
        ("dwRouteMask", UInt32),
        ("ulUpTime", UInt32),
        ("ulExpiryTime", UInt32),
        ("ulNumOutIf", UInt32),
        ("ulInPkts", UInt32),
        ("ulInOctets", UInt32),
        ("ulPktsDifferentIf", UInt32),
        ("ulQueueOverflow", UInt32),
        ("rgmiosOutStats", win32more.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_LH * 0),
    ]
    return MIB_IPMCAST_MFE_STATS
def _define_MIB_MFE_STATS_TABLE_head():
    class MIB_MFE_STATS_TABLE(Structure):
        pass
    return MIB_MFE_STATS_TABLE
def _define_MIB_MFE_STATS_TABLE():
    MIB_MFE_STATS_TABLE = win32more.NetworkManagement.IpHelper.MIB_MFE_STATS_TABLE_head
    MIB_MFE_STATS_TABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS * 0),
    ]
    return MIB_MFE_STATS_TABLE
def _define_MIB_IPMCAST_MFE_STATS_EX_XP_head():
    class MIB_IPMCAST_MFE_STATS_EX_XP(Structure):
        pass
    return MIB_IPMCAST_MFE_STATS_EX_XP
def _define_MIB_IPMCAST_MFE_STATS_EX_XP():
    MIB_IPMCAST_MFE_STATS_EX_XP = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS_EX_XP_head
    MIB_IPMCAST_MFE_STATS_EX_XP._fields_ = [
        ("dwGroup", UInt32),
        ("dwSource", UInt32),
        ("dwSrcMask", UInt32),
        ("dwUpStrmNgbr", UInt32),
        ("dwInIfIndex", UInt32),
        ("dwInIfProtocol", UInt32),
        ("dwRouteProtocol", UInt32),
        ("dwRouteNetwork", UInt32),
        ("dwRouteMask", UInt32),
        ("ulUpTime", UInt32),
        ("ulExpiryTime", UInt32),
        ("ulNumOutIf", UInt32),
        ("ulInPkts", UInt32),
        ("ulInOctets", UInt32),
        ("ulPktsDifferentIf", UInt32),
        ("ulQueueOverflow", UInt32),
        ("ulUninitMfe", UInt32),
        ("ulNegativeMfe", UInt32),
        ("ulInDiscards", UInt32),
        ("ulInHdrErrors", UInt32),
        ("ulTotalOutPackets", UInt32),
        ("rgmiosOutStats", win32more.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_LH * 0),
    ]
    return MIB_IPMCAST_MFE_STATS_EX_XP
def _define_MIB_MFE_STATS_TABLE_EX_XP_head():
    class MIB_MFE_STATS_TABLE_EX_XP(Structure):
        pass
    return MIB_MFE_STATS_TABLE_EX_XP
def _define_MIB_MFE_STATS_TABLE_EX_XP():
    MIB_MFE_STATS_TABLE_EX_XP = win32more.NetworkManagement.IpHelper.MIB_MFE_STATS_TABLE_EX_XP_head
    MIB_MFE_STATS_TABLE_EX_XP._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", POINTER(win32more.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS_EX_XP_head) * 0),
    ]
    return MIB_MFE_STATS_TABLE_EX_XP
def _define_MIB_IPMCAST_GLOBAL_head():
    class MIB_IPMCAST_GLOBAL(Structure):
        pass
    return MIB_IPMCAST_GLOBAL
def _define_MIB_IPMCAST_GLOBAL():
    MIB_IPMCAST_GLOBAL = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_GLOBAL_head
    MIB_IPMCAST_GLOBAL._fields_ = [
        ("dwEnable", UInt32),
    ]
    return MIB_IPMCAST_GLOBAL
def _define_MIB_IPMCAST_IF_ENTRY_head():
    class MIB_IPMCAST_IF_ENTRY(Structure):
        pass
    return MIB_IPMCAST_IF_ENTRY
def _define_MIB_IPMCAST_IF_ENTRY():
    MIB_IPMCAST_IF_ENTRY = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_IF_ENTRY_head
    MIB_IPMCAST_IF_ENTRY._fields_ = [
        ("dwIfIndex", UInt32),
        ("dwTtl", UInt32),
        ("dwProtocol", UInt32),
        ("dwRateLimit", UInt32),
        ("ulInMcastOctets", UInt32),
        ("ulOutMcastOctets", UInt32),
    ]
    return MIB_IPMCAST_IF_ENTRY
def _define_MIB_IPMCAST_IF_TABLE_head():
    class MIB_IPMCAST_IF_TABLE(Structure):
        pass
    return MIB_IPMCAST_IF_TABLE
def _define_MIB_IPMCAST_IF_TABLE():
    MIB_IPMCAST_IF_TABLE = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_IF_TABLE_head
    MIB_IPMCAST_IF_TABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPMCAST_IF_ENTRY * 0),
    ]
    return MIB_IPMCAST_IF_TABLE
MIB_TCP_STATE = Int32
MIB_TCP_STATE_CLOSED = 1
MIB_TCP_STATE_LISTEN = 2
MIB_TCP_STATE_SYN_SENT = 3
MIB_TCP_STATE_SYN_RCVD = 4
MIB_TCP_STATE_ESTAB = 5
MIB_TCP_STATE_FIN_WAIT1 = 6
MIB_TCP_STATE_FIN_WAIT2 = 7
MIB_TCP_STATE_CLOSE_WAIT = 8
MIB_TCP_STATE_CLOSING = 9
MIB_TCP_STATE_LAST_ACK = 10
MIB_TCP_STATE_TIME_WAIT = 11
MIB_TCP_STATE_DELETE_TCB = 12
MIB_TCP_STATE_RESERVED = 100
TCP_CONNECTION_OFFLOAD_STATE = Int32
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateInHost = 0
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloading = 1
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloaded = 2
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateUploading = 3
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateMax = 4
def _define_MIB_TCPROW_LH_head():
    class MIB_TCPROW_LH(Structure):
        pass
    return MIB_TCPROW_LH
def _define_MIB_TCPROW_LH():
    MIB_TCPROW_LH = win32more.NetworkManagement.IpHelper.MIB_TCPROW_LH_head
    class MIB_TCPROW_LH__Anonymous_e__Union(Union):
        pass
    MIB_TCPROW_LH__Anonymous_e__Union._fields_ = [
        ("dwState", UInt32),
        ("State", win32more.NetworkManagement.IpHelper.MIB_TCP_STATE),
    ]
    MIB_TCPROW_LH._anonymous_ = [
        'Anonymous',
    ]
    MIB_TCPROW_LH._fields_ = [
        ("Anonymous", MIB_TCPROW_LH__Anonymous_e__Union),
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwRemoteAddr", UInt32),
        ("dwRemotePort", UInt32),
    ]
    return MIB_TCPROW_LH
def _define_MIB_TCPROW_W2K_head():
    class MIB_TCPROW_W2K(Structure):
        pass
    return MIB_TCPROW_W2K
def _define_MIB_TCPROW_W2K():
    MIB_TCPROW_W2K = win32more.NetworkManagement.IpHelper.MIB_TCPROW_W2K_head
    MIB_TCPROW_W2K._fields_ = [
        ("dwState", UInt32),
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwRemoteAddr", UInt32),
        ("dwRemotePort", UInt32),
    ]
    return MIB_TCPROW_W2K
def _define_MIB_TCPTABLE_head():
    class MIB_TCPTABLE(Structure):
        pass
    return MIB_TCPTABLE
def _define_MIB_TCPTABLE():
    MIB_TCPTABLE = win32more.NetworkManagement.IpHelper.MIB_TCPTABLE_head
    MIB_TCPTABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCPROW_LH * 0),
    ]
    return MIB_TCPTABLE
def _define_MIB_TCPROW2_head():
    class MIB_TCPROW2(Structure):
        pass
    return MIB_TCPROW2
def _define_MIB_TCPROW2():
    MIB_TCPROW2 = win32more.NetworkManagement.IpHelper.MIB_TCPROW2_head
    MIB_TCPROW2._fields_ = [
        ("dwState", UInt32),
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwRemoteAddr", UInt32),
        ("dwRemotePort", UInt32),
        ("dwOwningPid", UInt32),
        ("dwOffloadState", win32more.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE),
    ]
    return MIB_TCPROW2
def _define_MIB_TCPTABLE2_head():
    class MIB_TCPTABLE2(Structure):
        pass
    return MIB_TCPTABLE2
def _define_MIB_TCPTABLE2():
    MIB_TCPTABLE2 = win32more.NetworkManagement.IpHelper.MIB_TCPTABLE2_head
    MIB_TCPTABLE2._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCPROW2 * 0),
    ]
    return MIB_TCPTABLE2
def _define_MIB_TCPROW_OWNER_PID_head():
    class MIB_TCPROW_OWNER_PID(Structure):
        pass
    return MIB_TCPROW_OWNER_PID
def _define_MIB_TCPROW_OWNER_PID():
    MIB_TCPROW_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_PID_head
    MIB_TCPROW_OWNER_PID._fields_ = [
        ("dwState", UInt32),
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwRemoteAddr", UInt32),
        ("dwRemotePort", UInt32),
        ("dwOwningPid", UInt32),
    ]
    return MIB_TCPROW_OWNER_PID
def _define_MIB_TCPTABLE_OWNER_PID_head():
    class MIB_TCPTABLE_OWNER_PID(Structure):
        pass
    return MIB_TCPTABLE_OWNER_PID
def _define_MIB_TCPTABLE_OWNER_PID():
    MIB_TCPTABLE_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_TCPTABLE_OWNER_PID_head
    MIB_TCPTABLE_OWNER_PID._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_PID * 0),
    ]
    return MIB_TCPTABLE_OWNER_PID
def _define_MIB_TCPROW_OWNER_MODULE_head():
    class MIB_TCPROW_OWNER_MODULE(Structure):
        pass
    return MIB_TCPROW_OWNER_MODULE
def _define_MIB_TCPROW_OWNER_MODULE():
    MIB_TCPROW_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_MODULE_head
    MIB_TCPROW_OWNER_MODULE._fields_ = [
        ("dwState", UInt32),
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwRemoteAddr", UInt32),
        ("dwRemotePort", UInt32),
        ("dwOwningPid", UInt32),
        ("liCreateTimestamp", win32more.Foundation.LARGE_INTEGER),
        ("OwningModuleInfo", UInt64 * 16),
    ]
    return MIB_TCPROW_OWNER_MODULE
def _define_MIB_TCPTABLE_OWNER_MODULE_head():
    class MIB_TCPTABLE_OWNER_MODULE(Structure):
        pass
    return MIB_TCPTABLE_OWNER_MODULE
def _define_MIB_TCPTABLE_OWNER_MODULE():
    MIB_TCPTABLE_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_TCPTABLE_OWNER_MODULE_head
    MIB_TCPTABLE_OWNER_MODULE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_MODULE * 0),
    ]
    return MIB_TCPTABLE_OWNER_MODULE
def _define_MIB_TCP6ROW_head():
    class MIB_TCP6ROW(Structure):
        pass
    return MIB_TCP6ROW
def _define_MIB_TCP6ROW():
    MIB_TCP6ROW = win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_head
    MIB_TCP6ROW._fields_ = [
        ("State", win32more.NetworkManagement.IpHelper.MIB_TCP_STATE),
        ("LocalAddr", win32more.Networking.WinSock.IN6_ADDR),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
        ("RemoteAddr", win32more.Networking.WinSock.IN6_ADDR),
        ("dwRemoteScopeId", UInt32),
        ("dwRemotePort", UInt32),
    ]
    return MIB_TCP6ROW
def _define_MIB_TCP6TABLE_head():
    class MIB_TCP6TABLE(Structure):
        pass
    return MIB_TCP6TABLE
def _define_MIB_TCP6TABLE():
    MIB_TCP6TABLE = win32more.NetworkManagement.IpHelper.MIB_TCP6TABLE_head
    MIB_TCP6TABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCP6ROW * 0),
    ]
    return MIB_TCP6TABLE
def _define_MIB_TCP6ROW2_head():
    class MIB_TCP6ROW2(Structure):
        pass
    return MIB_TCP6ROW2
def _define_MIB_TCP6ROW2():
    MIB_TCP6ROW2 = win32more.NetworkManagement.IpHelper.MIB_TCP6ROW2_head
    MIB_TCP6ROW2._fields_ = [
        ("LocalAddr", win32more.Networking.WinSock.IN6_ADDR),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
        ("RemoteAddr", win32more.Networking.WinSock.IN6_ADDR),
        ("dwRemoteScopeId", UInt32),
        ("dwRemotePort", UInt32),
        ("State", win32more.NetworkManagement.IpHelper.MIB_TCP_STATE),
        ("dwOwningPid", UInt32),
        ("dwOffloadState", win32more.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE),
    ]
    return MIB_TCP6ROW2
def _define_MIB_TCP6TABLE2_head():
    class MIB_TCP6TABLE2(Structure):
        pass
    return MIB_TCP6TABLE2
def _define_MIB_TCP6TABLE2():
    MIB_TCP6TABLE2 = win32more.NetworkManagement.IpHelper.MIB_TCP6TABLE2_head
    MIB_TCP6TABLE2._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCP6ROW2 * 0),
    ]
    return MIB_TCP6TABLE2
def _define_MIB_TCP6ROW_OWNER_PID_head():
    class MIB_TCP6ROW_OWNER_PID(Structure):
        pass
    return MIB_TCP6ROW_OWNER_PID
def _define_MIB_TCP6ROW_OWNER_PID():
    MIB_TCP6ROW_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_PID_head
    MIB_TCP6ROW_OWNER_PID._fields_ = [
        ("ucLocalAddr", Byte * 16),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
        ("ucRemoteAddr", Byte * 16),
        ("dwRemoteScopeId", UInt32),
        ("dwRemotePort", UInt32),
        ("dwState", UInt32),
        ("dwOwningPid", UInt32),
    ]
    return MIB_TCP6ROW_OWNER_PID
def _define_MIB_TCP6TABLE_OWNER_PID_head():
    class MIB_TCP6TABLE_OWNER_PID(Structure):
        pass
    return MIB_TCP6TABLE_OWNER_PID
def _define_MIB_TCP6TABLE_OWNER_PID():
    MIB_TCP6TABLE_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_TCP6TABLE_OWNER_PID_head
    MIB_TCP6TABLE_OWNER_PID._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_PID * 0),
    ]
    return MIB_TCP6TABLE_OWNER_PID
def _define_MIB_TCP6ROW_OWNER_MODULE_head():
    class MIB_TCP6ROW_OWNER_MODULE(Structure):
        pass
    return MIB_TCP6ROW_OWNER_MODULE
def _define_MIB_TCP6ROW_OWNER_MODULE():
    MIB_TCP6ROW_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_MODULE_head
    MIB_TCP6ROW_OWNER_MODULE._fields_ = [
        ("ucLocalAddr", Byte * 16),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
        ("ucRemoteAddr", Byte * 16),
        ("dwRemoteScopeId", UInt32),
        ("dwRemotePort", UInt32),
        ("dwState", UInt32),
        ("dwOwningPid", UInt32),
        ("liCreateTimestamp", win32more.Foundation.LARGE_INTEGER),
        ("OwningModuleInfo", UInt64 * 16),
    ]
    return MIB_TCP6ROW_OWNER_MODULE
def _define_MIB_TCP6TABLE_OWNER_MODULE_head():
    class MIB_TCP6TABLE_OWNER_MODULE(Structure):
        pass
    return MIB_TCP6TABLE_OWNER_MODULE
def _define_MIB_TCP6TABLE_OWNER_MODULE():
    MIB_TCP6TABLE_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_TCP6TABLE_OWNER_MODULE_head
    MIB_TCP6TABLE_OWNER_MODULE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_MODULE * 0),
    ]
    return MIB_TCP6TABLE_OWNER_MODULE
TCP_RTO_ALGORITHM = Int32
TCP_RTO_ALGORITHM_TcpRtoAlgorithmOther = 1
TCP_RTO_ALGORITHM_TcpRtoAlgorithmConstant = 2
TCP_RTO_ALGORITHM_TcpRtoAlgorithmRsre = 3
TCP_RTO_ALGORITHM_TcpRtoAlgorithmVanj = 4
TCP_RTO_ALGORITHM_MIB_TCP_RTO_OTHER = 1
TCP_RTO_ALGORITHM_MIB_TCP_RTO_CONSTANT = 2
TCP_RTO_ALGORITHM_MIB_TCP_RTO_RSRE = 3
TCP_RTO_ALGORITHM_MIB_TCP_RTO_VANJ = 4
def _define_MIB_TCPSTATS_LH_head():
    class MIB_TCPSTATS_LH(Structure):
        pass
    return MIB_TCPSTATS_LH
def _define_MIB_TCPSTATS_LH():
    MIB_TCPSTATS_LH = win32more.NetworkManagement.IpHelper.MIB_TCPSTATS_LH_head
    class MIB_TCPSTATS_LH__Anonymous_e__Union(Union):
        pass
    MIB_TCPSTATS_LH__Anonymous_e__Union._fields_ = [
        ("dwRtoAlgorithm", UInt32),
        ("RtoAlgorithm", win32more.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM),
    ]
    MIB_TCPSTATS_LH._anonymous_ = [
        'Anonymous',
    ]
    MIB_TCPSTATS_LH._fields_ = [
        ("Anonymous", MIB_TCPSTATS_LH__Anonymous_e__Union),
        ("dwRtoMin", UInt32),
        ("dwRtoMax", UInt32),
        ("dwMaxConn", UInt32),
        ("dwActiveOpens", UInt32),
        ("dwPassiveOpens", UInt32),
        ("dwAttemptFails", UInt32),
        ("dwEstabResets", UInt32),
        ("dwCurrEstab", UInt32),
        ("dwInSegs", UInt32),
        ("dwOutSegs", UInt32),
        ("dwRetransSegs", UInt32),
        ("dwInErrs", UInt32),
        ("dwOutRsts", UInt32),
        ("dwNumConns", UInt32),
    ]
    return MIB_TCPSTATS_LH
def _define_MIB_TCPSTATS_W2K_head():
    class MIB_TCPSTATS_W2K(Structure):
        pass
    return MIB_TCPSTATS_W2K
def _define_MIB_TCPSTATS_W2K():
    MIB_TCPSTATS_W2K = win32more.NetworkManagement.IpHelper.MIB_TCPSTATS_W2K_head
    MIB_TCPSTATS_W2K._fields_ = [
        ("dwRtoAlgorithm", UInt32),
        ("dwRtoMin", UInt32),
        ("dwRtoMax", UInt32),
        ("dwMaxConn", UInt32),
        ("dwActiveOpens", UInt32),
        ("dwPassiveOpens", UInt32),
        ("dwAttemptFails", UInt32),
        ("dwEstabResets", UInt32),
        ("dwCurrEstab", UInt32),
        ("dwInSegs", UInt32),
        ("dwOutSegs", UInt32),
        ("dwRetransSegs", UInt32),
        ("dwInErrs", UInt32),
        ("dwOutRsts", UInt32),
        ("dwNumConns", UInt32),
    ]
    return MIB_TCPSTATS_W2K
def _define_MIB_TCPSTATS2_head():
    class MIB_TCPSTATS2(Structure):
        pass
    return MIB_TCPSTATS2
def _define_MIB_TCPSTATS2():
    MIB_TCPSTATS2 = win32more.NetworkManagement.IpHelper.MIB_TCPSTATS2_head
    MIB_TCPSTATS2._fields_ = [
        ("RtoAlgorithm", win32more.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM),
        ("dwRtoMin", UInt32),
        ("dwRtoMax", UInt32),
        ("dwMaxConn", UInt32),
        ("dwActiveOpens", UInt32),
        ("dwPassiveOpens", UInt32),
        ("dwAttemptFails", UInt32),
        ("dwEstabResets", UInt32),
        ("dwCurrEstab", UInt32),
        ("dw64InSegs", UInt64),
        ("dw64OutSegs", UInt64),
        ("dwRetransSegs", UInt32),
        ("dwInErrs", UInt32),
        ("dwOutRsts", UInt32),
        ("dwNumConns", UInt32),
    ]
    return MIB_TCPSTATS2
def _define_MIB_UDPROW_head():
    class MIB_UDPROW(Structure):
        pass
    return MIB_UDPROW
def _define_MIB_UDPROW():
    MIB_UDPROW = win32more.NetworkManagement.IpHelper.MIB_UDPROW_head
    MIB_UDPROW._fields_ = [
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
    ]
    return MIB_UDPROW
def _define_MIB_UDPTABLE_head():
    class MIB_UDPTABLE(Structure):
        pass
    return MIB_UDPTABLE
def _define_MIB_UDPTABLE():
    MIB_UDPTABLE = win32more.NetworkManagement.IpHelper.MIB_UDPTABLE_head
    MIB_UDPTABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDPROW * 0),
    ]
    return MIB_UDPTABLE
def _define_MIB_UDPROW_OWNER_PID_head():
    class MIB_UDPROW_OWNER_PID(Structure):
        pass
    return MIB_UDPROW_OWNER_PID
def _define_MIB_UDPROW_OWNER_PID():
    MIB_UDPROW_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_PID_head
    MIB_UDPROW_OWNER_PID._fields_ = [
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwOwningPid", UInt32),
    ]
    return MIB_UDPROW_OWNER_PID
def _define_MIB_UDPTABLE_OWNER_PID_head():
    class MIB_UDPTABLE_OWNER_PID(Structure):
        pass
    return MIB_UDPTABLE_OWNER_PID
def _define_MIB_UDPTABLE_OWNER_PID():
    MIB_UDPTABLE_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_UDPTABLE_OWNER_PID_head
    MIB_UDPTABLE_OWNER_PID._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_PID * 0),
    ]
    return MIB_UDPTABLE_OWNER_PID
def _define_MIB_UDPROW_OWNER_MODULE_head():
    class MIB_UDPROW_OWNER_MODULE(Structure):
        pass
    return MIB_UDPROW_OWNER_MODULE
def _define_MIB_UDPROW_OWNER_MODULE():
    MIB_UDPROW_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_MODULE_head
    class MIB_UDPROW_OWNER_MODULE__Anonymous_e__Union(Union):
        pass
    class MIB_UDPROW_OWNER_MODULE__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIB_UDPROW_OWNER_MODULE__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Int32),
    ]
    MIB_UDPROW_OWNER_MODULE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDPROW_OWNER_MODULE__Anonymous_e__Union._fields_ = [
        ("Anonymous", MIB_UDPROW_OWNER_MODULE__Anonymous_e__Union__Anonymous_e__Struct),
        ("dwFlags", Int32),
    ]
    MIB_UDPROW_OWNER_MODULE._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDPROW_OWNER_MODULE._fields_ = [
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwOwningPid", UInt32),
        ("liCreateTimestamp", win32more.Foundation.LARGE_INTEGER),
        ("Anonymous", MIB_UDPROW_OWNER_MODULE__Anonymous_e__Union),
        ("OwningModuleInfo", UInt64 * 16),
    ]
    return MIB_UDPROW_OWNER_MODULE
def _define_MIB_UDPTABLE_OWNER_MODULE_head():
    class MIB_UDPTABLE_OWNER_MODULE(Structure):
        pass
    return MIB_UDPTABLE_OWNER_MODULE
def _define_MIB_UDPTABLE_OWNER_MODULE():
    MIB_UDPTABLE_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_UDPTABLE_OWNER_MODULE_head
    MIB_UDPTABLE_OWNER_MODULE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_MODULE * 0),
    ]
    return MIB_UDPTABLE_OWNER_MODULE
def _define_MIB_UDPROW2_head():
    class MIB_UDPROW2(Structure):
        pass
    return MIB_UDPROW2
def _define_MIB_UDPROW2():
    MIB_UDPROW2 = win32more.NetworkManagement.IpHelper.MIB_UDPROW2_head
    class MIB_UDPROW2__Anonymous_e__Union(Union):
        pass
    class MIB_UDPROW2__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIB_UDPROW2__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Int32),
    ]
    MIB_UDPROW2__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDPROW2__Anonymous_e__Union._fields_ = [
        ("Anonymous", MIB_UDPROW2__Anonymous_e__Union__Anonymous_e__Struct),
        ("dwFlags", Int32),
    ]
    MIB_UDPROW2._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDPROW2._fields_ = [
        ("dwLocalAddr", UInt32),
        ("dwLocalPort", UInt32),
        ("dwOwningPid", UInt32),
        ("liCreateTimestamp", win32more.Foundation.LARGE_INTEGER),
        ("Anonymous", MIB_UDPROW2__Anonymous_e__Union),
        ("OwningModuleInfo", UInt64 * 16),
        ("dwRemoteAddr", UInt32),
        ("dwRemotePort", UInt32),
    ]
    return MIB_UDPROW2
def _define_MIB_UDPTABLE2_head():
    class MIB_UDPTABLE2(Structure):
        pass
    return MIB_UDPTABLE2
def _define_MIB_UDPTABLE2():
    MIB_UDPTABLE2 = win32more.NetworkManagement.IpHelper.MIB_UDPTABLE2_head
    MIB_UDPTABLE2._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDPROW2 * 0),
    ]
    return MIB_UDPTABLE2
def _define_MIB_UDP6ROW_head():
    class MIB_UDP6ROW(Structure):
        pass
    return MIB_UDP6ROW
def _define_MIB_UDP6ROW():
    MIB_UDP6ROW = win32more.NetworkManagement.IpHelper.MIB_UDP6ROW_head
    MIB_UDP6ROW._fields_ = [
        ("dwLocalAddr", win32more.Networking.WinSock.IN6_ADDR),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
    ]
    return MIB_UDP6ROW
def _define_MIB_UDP6TABLE_head():
    class MIB_UDP6TABLE(Structure):
        pass
    return MIB_UDP6TABLE
def _define_MIB_UDP6TABLE():
    MIB_UDP6TABLE = win32more.NetworkManagement.IpHelper.MIB_UDP6TABLE_head
    MIB_UDP6TABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDP6ROW * 0),
    ]
    return MIB_UDP6TABLE
def _define_MIB_UDP6ROW_OWNER_PID_head():
    class MIB_UDP6ROW_OWNER_PID(Structure):
        pass
    return MIB_UDP6ROW_OWNER_PID
def _define_MIB_UDP6ROW_OWNER_PID():
    MIB_UDP6ROW_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_PID_head
    MIB_UDP6ROW_OWNER_PID._fields_ = [
        ("ucLocalAddr", Byte * 16),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
        ("dwOwningPid", UInt32),
    ]
    return MIB_UDP6ROW_OWNER_PID
def _define_MIB_UDP6TABLE_OWNER_PID_head():
    class MIB_UDP6TABLE_OWNER_PID(Structure):
        pass
    return MIB_UDP6TABLE_OWNER_PID
def _define_MIB_UDP6TABLE_OWNER_PID():
    MIB_UDP6TABLE_OWNER_PID = win32more.NetworkManagement.IpHelper.MIB_UDP6TABLE_OWNER_PID_head
    MIB_UDP6TABLE_OWNER_PID._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_PID * 0),
    ]
    return MIB_UDP6TABLE_OWNER_PID
def _define_MIB_UDP6ROW_OWNER_MODULE_head():
    class MIB_UDP6ROW_OWNER_MODULE(Structure):
        pass
    return MIB_UDP6ROW_OWNER_MODULE
def _define_MIB_UDP6ROW_OWNER_MODULE():
    MIB_UDP6ROW_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_MODULE_head
    class MIB_UDP6ROW_OWNER_MODULE__Anonymous_e__Union(Union):
        pass
    class MIB_UDP6ROW_OWNER_MODULE__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIB_UDP6ROW_OWNER_MODULE__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Int32),
    ]
    MIB_UDP6ROW_OWNER_MODULE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDP6ROW_OWNER_MODULE__Anonymous_e__Union._fields_ = [
        ("Anonymous", MIB_UDP6ROW_OWNER_MODULE__Anonymous_e__Union__Anonymous_e__Struct),
        ("dwFlags", Int32),
    ]
    MIB_UDP6ROW_OWNER_MODULE._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDP6ROW_OWNER_MODULE._fields_ = [
        ("ucLocalAddr", Byte * 16),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
        ("dwOwningPid", UInt32),
        ("liCreateTimestamp", win32more.Foundation.LARGE_INTEGER),
        ("Anonymous", MIB_UDP6ROW_OWNER_MODULE__Anonymous_e__Union),
        ("OwningModuleInfo", UInt64 * 16),
    ]
    return MIB_UDP6ROW_OWNER_MODULE
def _define_MIB_UDP6TABLE_OWNER_MODULE_head():
    class MIB_UDP6TABLE_OWNER_MODULE(Structure):
        pass
    return MIB_UDP6TABLE_OWNER_MODULE
def _define_MIB_UDP6TABLE_OWNER_MODULE():
    MIB_UDP6TABLE_OWNER_MODULE = win32more.NetworkManagement.IpHelper.MIB_UDP6TABLE_OWNER_MODULE_head
    MIB_UDP6TABLE_OWNER_MODULE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_MODULE * 0),
    ]
    return MIB_UDP6TABLE_OWNER_MODULE
def _define_MIB_UDP6ROW2_head():
    class MIB_UDP6ROW2(Structure):
        pass
    return MIB_UDP6ROW2
def _define_MIB_UDP6ROW2():
    MIB_UDP6ROW2 = win32more.NetworkManagement.IpHelper.MIB_UDP6ROW2_head
    class MIB_UDP6ROW2__Anonymous_e__Union(Union):
        pass
    class MIB_UDP6ROW2__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIB_UDP6ROW2__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Int32),
    ]
    MIB_UDP6ROW2__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDP6ROW2__Anonymous_e__Union._fields_ = [
        ("Anonymous", MIB_UDP6ROW2__Anonymous_e__Union__Anonymous_e__Struct),
        ("dwFlags", Int32),
    ]
    MIB_UDP6ROW2._anonymous_ = [
        'Anonymous',
    ]
    MIB_UDP6ROW2._fields_ = [
        ("ucLocalAddr", Byte * 16),
        ("dwLocalScopeId", UInt32),
        ("dwLocalPort", UInt32),
        ("dwOwningPid", UInt32),
        ("liCreateTimestamp", win32more.Foundation.LARGE_INTEGER),
        ("Anonymous", MIB_UDP6ROW2__Anonymous_e__Union),
        ("OwningModuleInfo", UInt64 * 16),
        ("ucRemoteAddr", Byte * 16),
        ("dwRemoteScopeId", UInt32),
        ("dwRemotePort", UInt32),
    ]
    return MIB_UDP6ROW2
def _define_MIB_UDP6TABLE2_head():
    class MIB_UDP6TABLE2(Structure):
        pass
    return MIB_UDP6TABLE2
def _define_MIB_UDP6TABLE2():
    MIB_UDP6TABLE2 = win32more.NetworkManagement.IpHelper.MIB_UDP6TABLE2_head
    MIB_UDP6TABLE2._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_UDP6ROW2 * 0),
    ]
    return MIB_UDP6TABLE2
def _define_MIB_UDPSTATS_head():
    class MIB_UDPSTATS(Structure):
        pass
    return MIB_UDPSTATS
def _define_MIB_UDPSTATS():
    MIB_UDPSTATS = win32more.NetworkManagement.IpHelper.MIB_UDPSTATS_head
    MIB_UDPSTATS._fields_ = [
        ("dwInDatagrams", UInt32),
        ("dwNoPorts", UInt32),
        ("dwInErrors", UInt32),
        ("dwOutDatagrams", UInt32),
        ("dwNumAddrs", UInt32),
    ]
    return MIB_UDPSTATS
def _define_MIB_UDPSTATS2_head():
    class MIB_UDPSTATS2(Structure):
        pass
    return MIB_UDPSTATS2
def _define_MIB_UDPSTATS2():
    MIB_UDPSTATS2 = win32more.NetworkManagement.IpHelper.MIB_UDPSTATS2_head
    MIB_UDPSTATS2._fields_ = [
        ("dw64InDatagrams", UInt64),
        ("dwNoPorts", UInt32),
        ("dwInErrors", UInt32),
        ("dw64OutDatagrams", UInt64),
        ("dwNumAddrs", UInt32),
    ]
    return MIB_UDPSTATS2
TCP_TABLE_CLASS = Int32
TCP_TABLE_BASIC_LISTENER = 0
TCP_TABLE_BASIC_CONNECTIONS = 1
TCP_TABLE_BASIC_ALL = 2
TCP_TABLE_OWNER_PID_LISTENER = 3
TCP_TABLE_OWNER_PID_CONNECTIONS = 4
TCP_TABLE_OWNER_PID_ALL = 5
TCP_TABLE_OWNER_MODULE_LISTENER = 6
TCP_TABLE_OWNER_MODULE_CONNECTIONS = 7
TCP_TABLE_OWNER_MODULE_ALL = 8
UDP_TABLE_CLASS = Int32
UDP_TABLE_BASIC = 0
UDP_TABLE_OWNER_PID = 1
UDP_TABLE_OWNER_MODULE = 2
TCPIP_OWNER_MODULE_INFO_CLASS = Int32
TCPIP_OWNER_MODULE_INFO_BASIC = 0
def _define_TCPIP_OWNER_MODULE_BASIC_INFO_head():
    class TCPIP_OWNER_MODULE_BASIC_INFO(Structure):
        pass
    return TCPIP_OWNER_MODULE_BASIC_INFO
def _define_TCPIP_OWNER_MODULE_BASIC_INFO():
    TCPIP_OWNER_MODULE_BASIC_INFO = win32more.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_BASIC_INFO_head
    TCPIP_OWNER_MODULE_BASIC_INFO._fields_ = [
        ("pModuleName", win32more.Foundation.PWSTR),
        ("pModulePath", win32more.Foundation.PWSTR),
    ]
    return TCPIP_OWNER_MODULE_BASIC_INFO
def _define_MIB_IPMCAST_BOUNDARY_head():
    class MIB_IPMCAST_BOUNDARY(Structure):
        pass
    return MIB_IPMCAST_BOUNDARY
def _define_MIB_IPMCAST_BOUNDARY():
    MIB_IPMCAST_BOUNDARY = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_BOUNDARY_head
    MIB_IPMCAST_BOUNDARY._fields_ = [
        ("dwIfIndex", UInt32),
        ("dwGroupAddress", UInt32),
        ("dwGroupMask", UInt32),
        ("dwStatus", UInt32),
    ]
    return MIB_IPMCAST_BOUNDARY
def _define_MIB_IPMCAST_BOUNDARY_TABLE_head():
    class MIB_IPMCAST_BOUNDARY_TABLE(Structure):
        pass
    return MIB_IPMCAST_BOUNDARY_TABLE
def _define_MIB_IPMCAST_BOUNDARY_TABLE():
    MIB_IPMCAST_BOUNDARY_TABLE = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_BOUNDARY_TABLE_head
    MIB_IPMCAST_BOUNDARY_TABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPMCAST_BOUNDARY * 0),
    ]
    return MIB_IPMCAST_BOUNDARY_TABLE
def _define_MIB_BOUNDARYROW_head():
    class MIB_BOUNDARYROW(Structure):
        pass
    return MIB_BOUNDARYROW
def _define_MIB_BOUNDARYROW():
    MIB_BOUNDARYROW = win32more.NetworkManagement.IpHelper.MIB_BOUNDARYROW_head
    MIB_BOUNDARYROW._fields_ = [
        ("dwGroupAddress", UInt32),
        ("dwGroupMask", UInt32),
    ]
    return MIB_BOUNDARYROW
def _define_MIB_MCAST_LIMIT_ROW_head():
    class MIB_MCAST_LIMIT_ROW(Structure):
        pass
    return MIB_MCAST_LIMIT_ROW
def _define_MIB_MCAST_LIMIT_ROW():
    MIB_MCAST_LIMIT_ROW = win32more.NetworkManagement.IpHelper.MIB_MCAST_LIMIT_ROW_head
    MIB_MCAST_LIMIT_ROW._fields_ = [
        ("dwTtl", UInt32),
        ("dwRateLimit", UInt32),
    ]
    return MIB_MCAST_LIMIT_ROW
def _define_MIB_IPMCAST_SCOPE_head():
    class MIB_IPMCAST_SCOPE(Structure):
        pass
    return MIB_IPMCAST_SCOPE
def _define_MIB_IPMCAST_SCOPE():
    MIB_IPMCAST_SCOPE = win32more.NetworkManagement.IpHelper.MIB_IPMCAST_SCOPE_head
    MIB_IPMCAST_SCOPE._fields_ = [
        ("dwGroupAddress", UInt32),
        ("dwGroupMask", UInt32),
        ("snNameBuffer", UInt16 * 256),
        ("dwStatus", UInt32),
    ]
    return MIB_IPMCAST_SCOPE
def _define_MIB_IPDESTROW_head():
    class MIB_IPDESTROW(Structure):
        pass
    return MIB_IPDESTROW
def _define_MIB_IPDESTROW():
    MIB_IPDESTROW = win32more.NetworkManagement.IpHelper.MIB_IPDESTROW_head
    MIB_IPDESTROW._fields_ = [
        ("ForwardRow", win32more.NetworkManagement.IpHelper.MIB_IPFORWARDROW),
        ("dwForwardPreference", UInt32),
        ("dwForwardViewSet", UInt32),
    ]
    return MIB_IPDESTROW
def _define_MIB_IPDESTTABLE_head():
    class MIB_IPDESTTABLE(Structure):
        pass
    return MIB_IPDESTTABLE
def _define_MIB_IPDESTTABLE():
    MIB_IPDESTTABLE = win32more.NetworkManagement.IpHelper.MIB_IPDESTTABLE_head
    MIB_IPDESTTABLE._fields_ = [
        ("dwNumEntries", UInt32),
        ("table", win32more.NetworkManagement.IpHelper.MIB_IPDESTROW * 0),
    ]
    return MIB_IPDESTTABLE
def _define_MIB_BEST_IF_head():
    class MIB_BEST_IF(Structure):
        pass
    return MIB_BEST_IF
def _define_MIB_BEST_IF():
    MIB_BEST_IF = win32more.NetworkManagement.IpHelper.MIB_BEST_IF_head
    MIB_BEST_IF._fields_ = [
        ("dwDestAddr", UInt32),
        ("dwIfIndex", UInt32),
    ]
    return MIB_BEST_IF
def _define_MIB_PROXYARP_head():
    class MIB_PROXYARP(Structure):
        pass
    return MIB_PROXYARP
def _define_MIB_PROXYARP():
    MIB_PROXYARP = win32more.NetworkManagement.IpHelper.MIB_PROXYARP_head
    MIB_PROXYARP._fields_ = [
        ("dwAddress", UInt32),
        ("dwMask", UInt32),
        ("dwIfIndex", UInt32),
    ]
    return MIB_PROXYARP
def _define_MIB_IFSTATUS_head():
    class MIB_IFSTATUS(Structure):
        pass
    return MIB_IFSTATUS
def _define_MIB_IFSTATUS():
    MIB_IFSTATUS = win32more.NetworkManagement.IpHelper.MIB_IFSTATUS_head
    MIB_IFSTATUS._fields_ = [
        ("dwIfIndex", UInt32),
        ("dwAdminStatus", UInt32),
        ("dwOperationalStatus", UInt32),
        ("bMHbeatActive", win32more.Foundation.BOOL),
        ("bMHbeatAlive", win32more.Foundation.BOOL),
    ]
    return MIB_IFSTATUS
def _define_MIB_ROUTESTATE_head():
    class MIB_ROUTESTATE(Structure):
        pass
    return MIB_ROUTESTATE
def _define_MIB_ROUTESTATE():
    MIB_ROUTESTATE = win32more.NetworkManagement.IpHelper.MIB_ROUTESTATE_head
    MIB_ROUTESTATE._fields_ = [
        ("bRoutesSetToStack", win32more.Foundation.BOOL),
    ]
    return MIB_ROUTESTATE
def _define_MIB_OPAQUE_INFO_head():
    class MIB_OPAQUE_INFO(Structure):
        pass
    return MIB_OPAQUE_INFO
def _define_MIB_OPAQUE_INFO():
    MIB_OPAQUE_INFO = win32more.NetworkManagement.IpHelper.MIB_OPAQUE_INFO_head
    class MIB_OPAQUE_INFO__Anonymous_e__Union(Union):
        pass
    MIB_OPAQUE_INFO__Anonymous_e__Union._fields_ = [
        ("ullAlign", UInt64),
        ("rgbyData", Byte * 0),
    ]
    MIB_OPAQUE_INFO._anonymous_ = [
        'Anonymous',
    ]
    MIB_OPAQUE_INFO._fields_ = [
        ("dwId", UInt32),
        ("Anonymous", MIB_OPAQUE_INFO__Anonymous_e__Union),
    ]
    return MIB_OPAQUE_INFO
def _define_IP_ADDRESS_STRING_head():
    class IP_ADDRESS_STRING(Structure):
        pass
    return IP_ADDRESS_STRING
def _define_IP_ADDRESS_STRING():
    IP_ADDRESS_STRING = win32more.NetworkManagement.IpHelper.IP_ADDRESS_STRING_head
    IP_ADDRESS_STRING._fields_ = [
        ("String", win32more.Foundation.CHAR * 16),
    ]
    return IP_ADDRESS_STRING
def _define_IP_ADDR_STRING_head():
    class IP_ADDR_STRING(Structure):
        pass
    return IP_ADDR_STRING
def _define_IP_ADDR_STRING():
    IP_ADDR_STRING = win32more.NetworkManagement.IpHelper.IP_ADDR_STRING_head
    IP_ADDR_STRING._fields_ = [
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADDR_STRING_head)),
        ("IpAddress", win32more.NetworkManagement.IpHelper.IP_ADDRESS_STRING),
        ("IpMask", win32more.NetworkManagement.IpHelper.IP_ADDRESS_STRING),
        ("Context", UInt32),
    ]
    return IP_ADDR_STRING
def _define_IP_ADAPTER_INFO_head():
    class IP_ADAPTER_INFO(Structure):
        pass
    return IP_ADAPTER_INFO
def _define_IP_ADAPTER_INFO():
    IP_ADAPTER_INFO = win32more.NetworkManagement.IpHelper.IP_ADAPTER_INFO_head
    IP_ADAPTER_INFO._fields_ = [
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_INFO_head)),
        ("ComboIndex", UInt32),
        ("AdapterName", win32more.Foundation.CHAR * 260),
        ("Description", win32more.Foundation.CHAR * 132),
        ("AddressLength", UInt32),
        ("Address", Byte * 8),
        ("Index", UInt32),
        ("Type", UInt32),
        ("DhcpEnabled", UInt32),
        ("CurrentIpAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADDR_STRING_head)),
        ("IpAddressList", win32more.NetworkManagement.IpHelper.IP_ADDR_STRING),
        ("GatewayList", win32more.NetworkManagement.IpHelper.IP_ADDR_STRING),
        ("DhcpServer", win32more.NetworkManagement.IpHelper.IP_ADDR_STRING),
        ("HaveWins", win32more.Foundation.BOOL),
        ("PrimaryWinsServer", win32more.NetworkManagement.IpHelper.IP_ADDR_STRING),
        ("SecondaryWinsServer", win32more.NetworkManagement.IpHelper.IP_ADDR_STRING),
        ("LeaseObtained", Int64),
        ("LeaseExpires", Int64),
    ]
    return IP_ADAPTER_INFO
def _define_IP_ADAPTER_UNICAST_ADDRESS_LH_head():
    class IP_ADAPTER_UNICAST_ADDRESS_LH(Structure):
        pass
    return IP_ADAPTER_UNICAST_ADDRESS_LH
def _define_IP_ADAPTER_UNICAST_ADDRESS_LH():
    IP_ADAPTER_UNICAST_ADDRESS_LH = win32more.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_LH_head
    class IP_ADAPTER_UNICAST_ADDRESS_LH__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_UNICAST_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_UNICAST_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Flags", UInt32),
    ]
    IP_ADAPTER_UNICAST_ADDRESS_LH__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_UNICAST_ADDRESS_LH__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_UNICAST_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_UNICAST_ADDRESS_LH._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_UNICAST_ADDRESS_LH._fields_ = [
        ("Anonymous", IP_ADAPTER_UNICAST_ADDRESS_LH__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_LH_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
        ("PrefixOrigin", win32more.Networking.WinSock.NL_PREFIX_ORIGIN),
        ("SuffixOrigin", win32more.Networking.WinSock.NL_SUFFIX_ORIGIN),
        ("DadState", win32more.Networking.WinSock.NL_DAD_STATE),
        ("ValidLifetime", UInt32),
        ("PreferredLifetime", UInt32),
        ("LeaseLifetime", UInt32),
        ("OnLinkPrefixLength", Byte),
    ]
    return IP_ADAPTER_UNICAST_ADDRESS_LH
def _define_IP_ADAPTER_UNICAST_ADDRESS_XP_head():
    class IP_ADAPTER_UNICAST_ADDRESS_XP(Structure):
        pass
    return IP_ADAPTER_UNICAST_ADDRESS_XP
def _define_IP_ADAPTER_UNICAST_ADDRESS_XP():
    IP_ADAPTER_UNICAST_ADDRESS_XP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_XP_head
    class IP_ADAPTER_UNICAST_ADDRESS_XP__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_UNICAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_UNICAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Flags", UInt32),
    ]
    IP_ADAPTER_UNICAST_ADDRESS_XP__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_UNICAST_ADDRESS_XP__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_UNICAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_UNICAST_ADDRESS_XP._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_UNICAST_ADDRESS_XP._fields_ = [
        ("Anonymous", IP_ADAPTER_UNICAST_ADDRESS_XP__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_XP_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
        ("PrefixOrigin", win32more.Networking.WinSock.NL_PREFIX_ORIGIN),
        ("SuffixOrigin", win32more.Networking.WinSock.NL_SUFFIX_ORIGIN),
        ("DadState", win32more.Networking.WinSock.NL_DAD_STATE),
        ("ValidLifetime", UInt32),
        ("PreferredLifetime", UInt32),
        ("LeaseLifetime", UInt32),
    ]
    return IP_ADAPTER_UNICAST_ADDRESS_XP
def _define_IP_ADAPTER_ANYCAST_ADDRESS_XP_head():
    class IP_ADAPTER_ANYCAST_ADDRESS_XP(Structure):
        pass
    return IP_ADAPTER_ANYCAST_ADDRESS_XP
def _define_IP_ADAPTER_ANYCAST_ADDRESS_XP():
    IP_ADAPTER_ANYCAST_ADDRESS_XP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP_head
    class IP_ADAPTER_ANYCAST_ADDRESS_XP__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_ANYCAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_ANYCAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Flags", UInt32),
    ]
    IP_ADAPTER_ANYCAST_ADDRESS_XP__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_ANYCAST_ADDRESS_XP__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_ANYCAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_ANYCAST_ADDRESS_XP._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_ANYCAST_ADDRESS_XP._fields_ = [
        ("Anonymous", IP_ADAPTER_ANYCAST_ADDRESS_XP__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
    ]
    return IP_ADAPTER_ANYCAST_ADDRESS_XP
def _define_IP_ADAPTER_MULTICAST_ADDRESS_XP_head():
    class IP_ADAPTER_MULTICAST_ADDRESS_XP(Structure):
        pass
    return IP_ADAPTER_MULTICAST_ADDRESS_XP
def _define_IP_ADAPTER_MULTICAST_ADDRESS_XP():
    IP_ADAPTER_MULTICAST_ADDRESS_XP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP_head
    class IP_ADAPTER_MULTICAST_ADDRESS_XP__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_MULTICAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_MULTICAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Flags", UInt32),
    ]
    IP_ADAPTER_MULTICAST_ADDRESS_XP__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_MULTICAST_ADDRESS_XP__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_MULTICAST_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_MULTICAST_ADDRESS_XP._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_MULTICAST_ADDRESS_XP._fields_ = [
        ("Anonymous", IP_ADAPTER_MULTICAST_ADDRESS_XP__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
    ]
    return IP_ADAPTER_MULTICAST_ADDRESS_XP
def _define_IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head():
    class IP_ADAPTER_DNS_SERVER_ADDRESS_XP(Structure):
        pass
    return IP_ADAPTER_DNS_SERVER_ADDRESS_XP
def _define_IP_ADAPTER_DNS_SERVER_ADDRESS_XP():
    IP_ADAPTER_DNS_SERVER_ADDRESS_XP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head
    class IP_ADAPTER_DNS_SERVER_ADDRESS_XP__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_DNS_SERVER_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_DNS_SERVER_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Reserved", UInt32),
    ]
    IP_ADAPTER_DNS_SERVER_ADDRESS_XP__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_DNS_SERVER_ADDRESS_XP__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_DNS_SERVER_ADDRESS_XP__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_DNS_SERVER_ADDRESS_XP._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_DNS_SERVER_ADDRESS_XP._fields_ = [
        ("Anonymous", IP_ADAPTER_DNS_SERVER_ADDRESS_XP__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
    ]
    return IP_ADAPTER_DNS_SERVER_ADDRESS_XP
def _define_IP_ADAPTER_WINS_SERVER_ADDRESS_LH_head():
    class IP_ADAPTER_WINS_SERVER_ADDRESS_LH(Structure):
        pass
    return IP_ADAPTER_WINS_SERVER_ADDRESS_LH
def _define_IP_ADAPTER_WINS_SERVER_ADDRESS_LH():
    IP_ADAPTER_WINS_SERVER_ADDRESS_LH = win32more.NetworkManagement.IpHelper.IP_ADAPTER_WINS_SERVER_ADDRESS_LH_head
    class IP_ADAPTER_WINS_SERVER_ADDRESS_LH__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_WINS_SERVER_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_WINS_SERVER_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Reserved", UInt32),
    ]
    IP_ADAPTER_WINS_SERVER_ADDRESS_LH__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_WINS_SERVER_ADDRESS_LH__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_WINS_SERVER_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_WINS_SERVER_ADDRESS_LH._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_WINS_SERVER_ADDRESS_LH._fields_ = [
        ("Anonymous", IP_ADAPTER_WINS_SERVER_ADDRESS_LH__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_WINS_SERVER_ADDRESS_LH_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
    ]
    return IP_ADAPTER_WINS_SERVER_ADDRESS_LH
def _define_IP_ADAPTER_GATEWAY_ADDRESS_LH_head():
    class IP_ADAPTER_GATEWAY_ADDRESS_LH(Structure):
        pass
    return IP_ADAPTER_GATEWAY_ADDRESS_LH
def _define_IP_ADAPTER_GATEWAY_ADDRESS_LH():
    IP_ADAPTER_GATEWAY_ADDRESS_LH = win32more.NetworkManagement.IpHelper.IP_ADAPTER_GATEWAY_ADDRESS_LH_head
    class IP_ADAPTER_GATEWAY_ADDRESS_LH__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_GATEWAY_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_GATEWAY_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Reserved", UInt32),
    ]
    IP_ADAPTER_GATEWAY_ADDRESS_LH__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_GATEWAY_ADDRESS_LH__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_GATEWAY_ADDRESS_LH__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_GATEWAY_ADDRESS_LH._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_GATEWAY_ADDRESS_LH._fields_ = [
        ("Anonymous", IP_ADAPTER_GATEWAY_ADDRESS_LH__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_GATEWAY_ADDRESS_LH_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
    ]
    return IP_ADAPTER_GATEWAY_ADDRESS_LH
def _define_IP_ADAPTER_PREFIX_XP_head():
    class IP_ADAPTER_PREFIX_XP(Structure):
        pass
    return IP_ADAPTER_PREFIX_XP
def _define_IP_ADAPTER_PREFIX_XP():
    IP_ADAPTER_PREFIX_XP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP_head
    class IP_ADAPTER_PREFIX_XP__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_PREFIX_XP__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_PREFIX_XP__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("Flags", UInt32),
    ]
    IP_ADAPTER_PREFIX_XP__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_PREFIX_XP__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_PREFIX_XP__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_PREFIX_XP._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_PREFIX_XP._fields_ = [
        ("Anonymous", IP_ADAPTER_PREFIX_XP__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP_head)),
        ("Address", win32more.Networking.WinSock.SOCKET_ADDRESS),
        ("PrefixLength", UInt32),
    ]
    return IP_ADAPTER_PREFIX_XP
def _define_IP_ADAPTER_DNS_SUFFIX_head():
    class IP_ADAPTER_DNS_SUFFIX(Structure):
        pass
    return IP_ADAPTER_DNS_SUFFIX
def _define_IP_ADAPTER_DNS_SUFFIX():
    IP_ADAPTER_DNS_SUFFIX = win32more.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SUFFIX_head
    IP_ADAPTER_DNS_SUFFIX._fields_ = [
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SUFFIX_head)),
        ("String", Char * 256),
    ]
    return IP_ADAPTER_DNS_SUFFIX
def _define_IP_ADAPTER_ADDRESSES_LH_head():
    class IP_ADAPTER_ADDRESSES_LH(Structure):
        pass
    return IP_ADAPTER_ADDRESSES_LH
def _define_IP_ADAPTER_ADDRESSES_LH():
    IP_ADAPTER_ADDRESSES_LH = win32more.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_LH_head
    class IP_ADAPTER_ADDRESSES_LH__Anonymous2_e__Union(Union):
        pass
    class IP_ADAPTER_ADDRESSES_LH__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_ADDRESSES_LH__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    IP_ADAPTER_ADDRESSES_LH__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_ADDRESSES_LH__Anonymous2_e__Union._fields_ = [
        ("Flags", UInt32),
        ("Anonymous", IP_ADAPTER_ADDRESSES_LH__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    class IP_ADAPTER_ADDRESSES_LH__Anonymous1_e__Union(Union):
        pass
    class IP_ADAPTER_ADDRESSES_LH__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_ADDRESSES_LH__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("IfIndex", UInt32),
    ]
    IP_ADAPTER_ADDRESSES_LH__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_ADDRESSES_LH__Anonymous1_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_ADDRESSES_LH__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_ADDRESSES_LH._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    IP_ADAPTER_ADDRESSES_LH._fields_ = [
        ("Anonymous1", IP_ADAPTER_ADDRESSES_LH__Anonymous1_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_LH_head)),
        ("AdapterName", win32more.Foundation.PSTR),
        ("FirstUnicastAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_LH_head)),
        ("FirstAnycastAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP_head)),
        ("FirstMulticastAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP_head)),
        ("FirstDnsServerAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head)),
        ("DnsSuffix", win32more.Foundation.PWSTR),
        ("Description", win32more.Foundation.PWSTR),
        ("FriendlyName", win32more.Foundation.PWSTR),
        ("PhysicalAddress", Byte * 8),
        ("PhysicalAddressLength", UInt32),
        ("Anonymous2", IP_ADAPTER_ADDRESSES_LH__Anonymous2_e__Union),
        ("Mtu", UInt32),
        ("IfType", UInt32),
        ("OperStatus", win32more.NetworkManagement.IpHelper.IF_OPER_STATUS),
        ("Ipv6IfIndex", UInt32),
        ("ZoneIndices", UInt32 * 16),
        ("FirstPrefix", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP_head)),
        ("TransmitLinkSpeed", UInt64),
        ("ReceiveLinkSpeed", UInt64),
        ("FirstWinsServerAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_WINS_SERVER_ADDRESS_LH_head)),
        ("FirstGatewayAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_GATEWAY_ADDRESS_LH_head)),
        ("Ipv4Metric", UInt32),
        ("Ipv6Metric", UInt32),
        ("Luid", win32more.NetworkManagement.IpHelper.NET_LUID_LH),
        ("Dhcpv4Server", win32more.Networking.WinSock.SOCKET_ADDRESS),
        ("CompartmentId", UInt32),
        ("NetworkGuid", Guid),
        ("ConnectionType", win32more.NetworkManagement.IpHelper.NET_IF_CONNECTION_TYPE),
        ("TunnelType", win32more.NetworkManagement.IpHelper.TUNNEL_TYPE),
        ("Dhcpv6Server", win32more.Networking.WinSock.SOCKET_ADDRESS),
        ("Dhcpv6ClientDuid", Byte * 130),
        ("Dhcpv6ClientDuidLength", UInt32),
        ("Dhcpv6Iaid", UInt32),
        ("FirstDnsSuffix", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SUFFIX_head)),
    ]
    return IP_ADAPTER_ADDRESSES_LH
def _define_IP_ADAPTER_ADDRESSES_XP_head():
    class IP_ADAPTER_ADDRESSES_XP(Structure):
        pass
    return IP_ADAPTER_ADDRESSES_XP
def _define_IP_ADAPTER_ADDRESSES_XP():
    IP_ADAPTER_ADDRESSES_XP = win32more.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_XP_head
    class IP_ADAPTER_ADDRESSES_XP__Anonymous_e__Union(Union):
        pass
    class IP_ADAPTER_ADDRESSES_XP__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IP_ADAPTER_ADDRESSES_XP__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Length", UInt32),
        ("IfIndex", UInt32),
    ]
    IP_ADAPTER_ADDRESSES_XP__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_ADDRESSES_XP__Anonymous_e__Union._fields_ = [
        ("Alignment", UInt64),
        ("Anonymous", IP_ADAPTER_ADDRESSES_XP__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IP_ADAPTER_ADDRESSES_XP._anonymous_ = [
        'Anonymous',
    ]
    IP_ADAPTER_ADDRESSES_XP._fields_ = [
        ("Anonymous", IP_ADAPTER_ADDRESSES_XP__Anonymous_e__Union),
        ("Next", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_XP_head)),
        ("AdapterName", win32more.Foundation.PSTR),
        ("FirstUnicastAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_XP_head)),
        ("FirstAnycastAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP_head)),
        ("FirstMulticastAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP_head)),
        ("FirstDnsServerAddress", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head)),
        ("DnsSuffix", win32more.Foundation.PWSTR),
        ("Description", win32more.Foundation.PWSTR),
        ("FriendlyName", win32more.Foundation.PWSTR),
        ("PhysicalAddress", Byte * 8),
        ("PhysicalAddressLength", UInt32),
        ("Flags", UInt32),
        ("Mtu", UInt32),
        ("IfType", UInt32),
        ("OperStatus", win32more.NetworkManagement.IpHelper.IF_OPER_STATUS),
        ("Ipv6IfIndex", UInt32),
        ("ZoneIndices", UInt32 * 16),
        ("FirstPrefix", POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP_head)),
    ]
    return IP_ADAPTER_ADDRESSES_XP
def _define_IP_PER_ADAPTER_INFO_W2KSP1_head():
    class IP_PER_ADAPTER_INFO_W2KSP1(Structure):
        pass
    return IP_PER_ADAPTER_INFO_W2KSP1
def _define_IP_PER_ADAPTER_INFO_W2KSP1():
    IP_PER_ADAPTER_INFO_W2KSP1 = win32more.NetworkManagement.IpHelper.IP_PER_ADAPTER_INFO_W2KSP1_head
    IP_PER_ADAPTER_INFO_W2KSP1._fields_ = [
        ("AutoconfigEnabled", UInt32),
        ("AutoconfigActive", UInt32),
        ("CurrentDnsServer", POINTER(win32more.NetworkManagement.IpHelper.IP_ADDR_STRING_head)),
        ("DnsServerList", win32more.NetworkManagement.IpHelper.IP_ADDR_STRING),
    ]
    return IP_PER_ADAPTER_INFO_W2KSP1
def _define_FIXED_INFO_W2KSP1_head():
    class FIXED_INFO_W2KSP1(Structure):
        pass
    return FIXED_INFO_W2KSP1
def _define_FIXED_INFO_W2KSP1():
    FIXED_INFO_W2KSP1 = win32more.NetworkManagement.IpHelper.FIXED_INFO_W2KSP1_head
    FIXED_INFO_W2KSP1._fields_ = [
        ("HostName", win32more.Foundation.CHAR * 132),
        ("DomainName", win32more.Foundation.CHAR * 132),
        ("CurrentDnsServer", POINTER(win32more.NetworkManagement.IpHelper.IP_ADDR_STRING_head)),
        ("DnsServerList", win32more.NetworkManagement.IpHelper.IP_ADDR_STRING),
        ("NodeType", UInt32),
        ("ScopeId", win32more.Foundation.CHAR * 260),
        ("EnableRouting", UInt32),
        ("EnableProxy", UInt32),
        ("EnableDns", UInt32),
    ]
    return FIXED_INFO_W2KSP1
def _define_ip_interface_name_info_w2ksp1_head():
    class ip_interface_name_info_w2ksp1(Structure):
        pass
    return ip_interface_name_info_w2ksp1
def _define_ip_interface_name_info_w2ksp1():
    ip_interface_name_info_w2ksp1 = win32more.NetworkManagement.IpHelper.ip_interface_name_info_w2ksp1_head
    ip_interface_name_info_w2ksp1._fields_ = [
        ("Index", UInt32),
        ("MediaType", UInt32),
        ("ConnectionType", Byte),
        ("AccessType", Byte),
        ("DeviceGuid", Guid),
        ("InterfaceGuid", Guid),
    ]
    return ip_interface_name_info_w2ksp1
TCP_ESTATS_TYPE = Int32
TCP_ESTATS_TYPE_TcpConnectionEstatsSynOpts = 0
TCP_ESTATS_TYPE_TcpConnectionEstatsData = 1
TCP_ESTATS_TYPE_TcpConnectionEstatsSndCong = 2
TCP_ESTATS_TYPE_TcpConnectionEstatsPath = 3
TCP_ESTATS_TYPE_TcpConnectionEstatsSendBuff = 4
TCP_ESTATS_TYPE_TcpConnectionEstatsRec = 5
TCP_ESTATS_TYPE_TcpConnectionEstatsObsRec = 6
TCP_ESTATS_TYPE_TcpConnectionEstatsBandwidth = 7
TCP_ESTATS_TYPE_TcpConnectionEstatsFineRtt = 8
TCP_ESTATS_TYPE_TcpConnectionEstatsMaximum = 9
TCP_BOOLEAN_OPTIONAL = Int32
TCP_BOOLEAN_OPTIONAL_TcpBoolOptDisabled = 0
TCP_BOOLEAN_OPTIONAL_TcpBoolOptEnabled = 1
TCP_BOOLEAN_OPTIONAL_TcpBoolOptUnchanged = -1
def _define_TCP_ESTATS_SYN_OPTS_ROS_v0_head():
    class TCP_ESTATS_SYN_OPTS_ROS_v0(Structure):
        pass
    return TCP_ESTATS_SYN_OPTS_ROS_v0
def _define_TCP_ESTATS_SYN_OPTS_ROS_v0():
    TCP_ESTATS_SYN_OPTS_ROS_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_SYN_OPTS_ROS_v0_head
    TCP_ESTATS_SYN_OPTS_ROS_v0._fields_ = [
        ("ActiveOpen", win32more.Foundation.BOOLEAN),
        ("MssRcvd", UInt32),
        ("MssSent", UInt32),
    ]
    return TCP_ESTATS_SYN_OPTS_ROS_v0
TCP_SOFT_ERROR = Int32
TCP_SOFT_ERROR_TcpErrorNone = 0
TCP_SOFT_ERROR_TcpErrorBelowDataWindow = 1
TCP_SOFT_ERROR_TcpErrorAboveDataWindow = 2
TCP_SOFT_ERROR_TcpErrorBelowAckWindow = 3
TCP_SOFT_ERROR_TcpErrorAboveAckWindow = 4
TCP_SOFT_ERROR_TcpErrorBelowTsWindow = 5
TCP_SOFT_ERROR_TcpErrorAboveTsWindow = 6
TCP_SOFT_ERROR_TcpErrorDataChecksumError = 7
TCP_SOFT_ERROR_TcpErrorDataLengthError = 8
TCP_SOFT_ERROR_TcpErrorMaxSoftError = 9
def _define_TCP_ESTATS_DATA_ROD_v0_head():
    class TCP_ESTATS_DATA_ROD_v0(Structure):
        pass
    return TCP_ESTATS_DATA_ROD_v0
def _define_TCP_ESTATS_DATA_ROD_v0():
    TCP_ESTATS_DATA_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_DATA_ROD_v0_head
    TCP_ESTATS_DATA_ROD_v0._fields_ = [
        ("DataBytesOut", UInt64),
        ("DataSegsOut", UInt64),
        ("DataBytesIn", UInt64),
        ("DataSegsIn", UInt64),
        ("SegsOut", UInt64),
        ("SegsIn", UInt64),
        ("SoftErrors", UInt32),
        ("SoftErrorReason", UInt32),
        ("SndUna", UInt32),
        ("SndNxt", UInt32),
        ("SndMax", UInt32),
        ("ThruBytesAcked", UInt64),
        ("RcvNxt", UInt32),
        ("ThruBytesReceived", UInt64),
    ]
    return TCP_ESTATS_DATA_ROD_v0
def _define_TCP_ESTATS_DATA_RW_v0_head():
    class TCP_ESTATS_DATA_RW_v0(Structure):
        pass
    return TCP_ESTATS_DATA_RW_v0
def _define_TCP_ESTATS_DATA_RW_v0():
    TCP_ESTATS_DATA_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_DATA_RW_v0_head
    TCP_ESTATS_DATA_RW_v0._fields_ = [
        ("EnableCollection", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_DATA_RW_v0
def _define_TCP_ESTATS_SND_CONG_ROD_v0_head():
    class TCP_ESTATS_SND_CONG_ROD_v0(Structure):
        pass
    return TCP_ESTATS_SND_CONG_ROD_v0
def _define_TCP_ESTATS_SND_CONG_ROD_v0():
    TCP_ESTATS_SND_CONG_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_SND_CONG_ROD_v0_head
    TCP_ESTATS_SND_CONG_ROD_v0._fields_ = [
        ("SndLimTransRwin", UInt32),
        ("SndLimTimeRwin", UInt32),
        ("SndLimBytesRwin", UIntPtr),
        ("SndLimTransCwnd", UInt32),
        ("SndLimTimeCwnd", UInt32),
        ("SndLimBytesCwnd", UIntPtr),
        ("SndLimTransSnd", UInt32),
        ("SndLimTimeSnd", UInt32),
        ("SndLimBytesSnd", UIntPtr),
        ("SlowStart", UInt32),
        ("CongAvoid", UInt32),
        ("OtherReductions", UInt32),
        ("CurCwnd", UInt32),
        ("MaxSsCwnd", UInt32),
        ("MaxCaCwnd", UInt32),
        ("CurSsthresh", UInt32),
        ("MaxSsthresh", UInt32),
        ("MinSsthresh", UInt32),
    ]
    return TCP_ESTATS_SND_CONG_ROD_v0
def _define_TCP_ESTATS_SND_CONG_ROS_v0_head():
    class TCP_ESTATS_SND_CONG_ROS_v0(Structure):
        pass
    return TCP_ESTATS_SND_CONG_ROS_v0
def _define_TCP_ESTATS_SND_CONG_ROS_v0():
    TCP_ESTATS_SND_CONG_ROS_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_SND_CONG_ROS_v0_head
    TCP_ESTATS_SND_CONG_ROS_v0._fields_ = [
        ("LimCwnd", UInt32),
    ]
    return TCP_ESTATS_SND_CONG_ROS_v0
def _define_TCP_ESTATS_SND_CONG_RW_v0_head():
    class TCP_ESTATS_SND_CONG_RW_v0(Structure):
        pass
    return TCP_ESTATS_SND_CONG_RW_v0
def _define_TCP_ESTATS_SND_CONG_RW_v0():
    TCP_ESTATS_SND_CONG_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_SND_CONG_RW_v0_head
    TCP_ESTATS_SND_CONG_RW_v0._fields_ = [
        ("EnableCollection", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_SND_CONG_RW_v0
def _define_TCP_ESTATS_PATH_ROD_v0_head():
    class TCP_ESTATS_PATH_ROD_v0(Structure):
        pass
    return TCP_ESTATS_PATH_ROD_v0
def _define_TCP_ESTATS_PATH_ROD_v0():
    TCP_ESTATS_PATH_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_PATH_ROD_v0_head
    TCP_ESTATS_PATH_ROD_v0._fields_ = [
        ("FastRetran", UInt32),
        ("Timeouts", UInt32),
        ("SubsequentTimeouts", UInt32),
        ("CurTimeoutCount", UInt32),
        ("AbruptTimeouts", UInt32),
        ("PktsRetrans", UInt32),
        ("BytesRetrans", UInt32),
        ("DupAcksIn", UInt32),
        ("SacksRcvd", UInt32),
        ("SackBlocksRcvd", UInt32),
        ("CongSignals", UInt32),
        ("PreCongSumCwnd", UInt32),
        ("PreCongSumRtt", UInt32),
        ("PostCongSumRtt", UInt32),
        ("PostCongCountRtt", UInt32),
        ("EcnSignals", UInt32),
        ("EceRcvd", UInt32),
        ("SendStall", UInt32),
        ("QuenchRcvd", UInt32),
        ("RetranThresh", UInt32),
        ("SndDupAckEpisodes", UInt32),
        ("SumBytesReordered", UInt32),
        ("NonRecovDa", UInt32),
        ("NonRecovDaEpisodes", UInt32),
        ("AckAfterFr", UInt32),
        ("DsackDups", UInt32),
        ("SampleRtt", UInt32),
        ("SmoothedRtt", UInt32),
        ("RttVar", UInt32),
        ("MaxRtt", UInt32),
        ("MinRtt", UInt32),
        ("SumRtt", UInt32),
        ("CountRtt", UInt32),
        ("CurRto", UInt32),
        ("MaxRto", UInt32),
        ("MinRto", UInt32),
        ("CurMss", UInt32),
        ("MaxMss", UInt32),
        ("MinMss", UInt32),
        ("SpuriousRtoDetections", UInt32),
    ]
    return TCP_ESTATS_PATH_ROD_v0
def _define_TCP_ESTATS_PATH_RW_v0_head():
    class TCP_ESTATS_PATH_RW_v0(Structure):
        pass
    return TCP_ESTATS_PATH_RW_v0
def _define_TCP_ESTATS_PATH_RW_v0():
    TCP_ESTATS_PATH_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_PATH_RW_v0_head
    TCP_ESTATS_PATH_RW_v0._fields_ = [
        ("EnableCollection", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_PATH_RW_v0
def _define_TCP_ESTATS_SEND_BUFF_ROD_v0_head():
    class TCP_ESTATS_SEND_BUFF_ROD_v0(Structure):
        pass
    return TCP_ESTATS_SEND_BUFF_ROD_v0
def _define_TCP_ESTATS_SEND_BUFF_ROD_v0():
    TCP_ESTATS_SEND_BUFF_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_SEND_BUFF_ROD_v0_head
    TCP_ESTATS_SEND_BUFF_ROD_v0._fields_ = [
        ("CurRetxQueue", UIntPtr),
        ("MaxRetxQueue", UIntPtr),
        ("CurAppWQueue", UIntPtr),
        ("MaxAppWQueue", UIntPtr),
    ]
    return TCP_ESTATS_SEND_BUFF_ROD_v0
def _define_TCP_ESTATS_SEND_BUFF_RW_v0_head():
    class TCP_ESTATS_SEND_BUFF_RW_v0(Structure):
        pass
    return TCP_ESTATS_SEND_BUFF_RW_v0
def _define_TCP_ESTATS_SEND_BUFF_RW_v0():
    TCP_ESTATS_SEND_BUFF_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_SEND_BUFF_RW_v0_head
    TCP_ESTATS_SEND_BUFF_RW_v0._fields_ = [
        ("EnableCollection", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_SEND_BUFF_RW_v0
def _define_TCP_ESTATS_REC_ROD_v0_head():
    class TCP_ESTATS_REC_ROD_v0(Structure):
        pass
    return TCP_ESTATS_REC_ROD_v0
def _define_TCP_ESTATS_REC_ROD_v0():
    TCP_ESTATS_REC_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_REC_ROD_v0_head
    TCP_ESTATS_REC_ROD_v0._fields_ = [
        ("CurRwinSent", UInt32),
        ("MaxRwinSent", UInt32),
        ("MinRwinSent", UInt32),
        ("LimRwin", UInt32),
        ("DupAckEpisodes", UInt32),
        ("DupAcksOut", UInt32),
        ("CeRcvd", UInt32),
        ("EcnSent", UInt32),
        ("EcnNoncesRcvd", UInt32),
        ("CurReasmQueue", UInt32),
        ("MaxReasmQueue", UInt32),
        ("CurAppRQueue", UIntPtr),
        ("MaxAppRQueue", UIntPtr),
        ("WinScaleSent", Byte),
    ]
    return TCP_ESTATS_REC_ROD_v0
def _define_TCP_ESTATS_REC_RW_v0_head():
    class TCP_ESTATS_REC_RW_v0(Structure):
        pass
    return TCP_ESTATS_REC_RW_v0
def _define_TCP_ESTATS_REC_RW_v0():
    TCP_ESTATS_REC_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_REC_RW_v0_head
    TCP_ESTATS_REC_RW_v0._fields_ = [
        ("EnableCollection", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_REC_RW_v0
def _define_TCP_ESTATS_OBS_REC_ROD_v0_head():
    class TCP_ESTATS_OBS_REC_ROD_v0(Structure):
        pass
    return TCP_ESTATS_OBS_REC_ROD_v0
def _define_TCP_ESTATS_OBS_REC_ROD_v0():
    TCP_ESTATS_OBS_REC_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_OBS_REC_ROD_v0_head
    TCP_ESTATS_OBS_REC_ROD_v0._fields_ = [
        ("CurRwinRcvd", UInt32),
        ("MaxRwinRcvd", UInt32),
        ("MinRwinRcvd", UInt32),
        ("WinScaleRcvd", Byte),
    ]
    return TCP_ESTATS_OBS_REC_ROD_v0
def _define_TCP_ESTATS_OBS_REC_RW_v0_head():
    class TCP_ESTATS_OBS_REC_RW_v0(Structure):
        pass
    return TCP_ESTATS_OBS_REC_RW_v0
def _define_TCP_ESTATS_OBS_REC_RW_v0():
    TCP_ESTATS_OBS_REC_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_OBS_REC_RW_v0_head
    TCP_ESTATS_OBS_REC_RW_v0._fields_ = [
        ("EnableCollection", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_OBS_REC_RW_v0
def _define_TCP_ESTATS_BANDWIDTH_RW_v0_head():
    class TCP_ESTATS_BANDWIDTH_RW_v0(Structure):
        pass
    return TCP_ESTATS_BANDWIDTH_RW_v0
def _define_TCP_ESTATS_BANDWIDTH_RW_v0():
    TCP_ESTATS_BANDWIDTH_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_BANDWIDTH_RW_v0_head
    TCP_ESTATS_BANDWIDTH_RW_v0._fields_ = [
        ("EnableCollectionOutbound", win32more.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL),
        ("EnableCollectionInbound", win32more.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL),
    ]
    return TCP_ESTATS_BANDWIDTH_RW_v0
def _define_TCP_ESTATS_BANDWIDTH_ROD_v0_head():
    class TCP_ESTATS_BANDWIDTH_ROD_v0(Structure):
        pass
    return TCP_ESTATS_BANDWIDTH_ROD_v0
def _define_TCP_ESTATS_BANDWIDTH_ROD_v0():
    TCP_ESTATS_BANDWIDTH_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_BANDWIDTH_ROD_v0_head
    TCP_ESTATS_BANDWIDTH_ROD_v0._fields_ = [
        ("OutboundBandwidth", UInt64),
        ("InboundBandwidth", UInt64),
        ("OutboundInstability", UInt64),
        ("InboundInstability", UInt64),
        ("OutboundBandwidthPeaked", win32more.Foundation.BOOLEAN),
        ("InboundBandwidthPeaked", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_BANDWIDTH_ROD_v0
def _define_TCP_ESTATS_FINE_RTT_RW_v0_head():
    class TCP_ESTATS_FINE_RTT_RW_v0(Structure):
        pass
    return TCP_ESTATS_FINE_RTT_RW_v0
def _define_TCP_ESTATS_FINE_RTT_RW_v0():
    TCP_ESTATS_FINE_RTT_RW_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_FINE_RTT_RW_v0_head
    TCP_ESTATS_FINE_RTT_RW_v0._fields_ = [
        ("EnableCollection", win32more.Foundation.BOOLEAN),
    ]
    return TCP_ESTATS_FINE_RTT_RW_v0
def _define_TCP_ESTATS_FINE_RTT_ROD_v0_head():
    class TCP_ESTATS_FINE_RTT_ROD_v0(Structure):
        pass
    return TCP_ESTATS_FINE_RTT_ROD_v0
def _define_TCP_ESTATS_FINE_RTT_ROD_v0():
    TCP_ESTATS_FINE_RTT_ROD_v0 = win32more.NetworkManagement.IpHelper.TCP_ESTATS_FINE_RTT_ROD_v0_head
    TCP_ESTATS_FINE_RTT_ROD_v0._fields_ = [
        ("RttVar", UInt32),
        ("MaxRtt", UInt32),
        ("MinRtt", UInt32),
        ("SumRtt", UInt32),
    ]
    return TCP_ESTATS_FINE_RTT_ROD_v0
def _define_INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES_head():
    class INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES(Structure):
        pass
    return INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES
def _define_INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES():
    INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES = win32more.NetworkManagement.IpHelper.INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES_head
    INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES._fields_ = [
        ("PtpV2OverUdpIPv4EventMessageReceive", win32more.Foundation.BOOLEAN),
        ("PtpV2OverUdpIPv4AllMessageReceive", win32more.Foundation.BOOLEAN),
        ("PtpV2OverUdpIPv4EventMessageTransmit", win32more.Foundation.BOOLEAN),
        ("PtpV2OverUdpIPv4AllMessageTransmit", win32more.Foundation.BOOLEAN),
        ("PtpV2OverUdpIPv6EventMessageReceive", win32more.Foundation.BOOLEAN),
        ("PtpV2OverUdpIPv6AllMessageReceive", win32more.Foundation.BOOLEAN),
        ("PtpV2OverUdpIPv6EventMessageTransmit", win32more.Foundation.BOOLEAN),
        ("PtpV2OverUdpIPv6AllMessageTransmit", win32more.Foundation.BOOLEAN),
        ("AllReceive", win32more.Foundation.BOOLEAN),
        ("AllTransmit", win32more.Foundation.BOOLEAN),
        ("TaggedTransmit", win32more.Foundation.BOOLEAN),
    ]
    return INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES
def _define_INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES_head():
    class INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES(Structure):
        pass
    return INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES
def _define_INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES():
    INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES = win32more.NetworkManagement.IpHelper.INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES_head
    INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES._fields_ = [
        ("AllReceive", win32more.Foundation.BOOLEAN),
        ("AllTransmit", win32more.Foundation.BOOLEAN),
        ("TaggedTransmit", win32more.Foundation.BOOLEAN),
    ]
    return INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES
def _define_INTERFACE_TIMESTAMP_CAPABILITIES_head():
    class INTERFACE_TIMESTAMP_CAPABILITIES(Structure):
        pass
    return INTERFACE_TIMESTAMP_CAPABILITIES
def _define_INTERFACE_TIMESTAMP_CAPABILITIES():
    INTERFACE_TIMESTAMP_CAPABILITIES = win32more.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES_head
    INTERFACE_TIMESTAMP_CAPABILITIES._fields_ = [
        ("HardwareClockFrequencyHz", UInt64),
        ("SupportsCrossTimestamp", win32more.Foundation.BOOLEAN),
        ("HardwareCapabilities", win32more.NetworkManagement.IpHelper.INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES),
        ("SoftwareCapabilities", win32more.NetworkManagement.IpHelper.INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES),
    ]
    return INTERFACE_TIMESTAMP_CAPABILITIES
def _define_INTERFACE_HARDWARE_CROSSTIMESTAMP_head():
    class INTERFACE_HARDWARE_CROSSTIMESTAMP(Structure):
        pass
    return INTERFACE_HARDWARE_CROSSTIMESTAMP
def _define_INTERFACE_HARDWARE_CROSSTIMESTAMP():
    INTERFACE_HARDWARE_CROSSTIMESTAMP = win32more.NetworkManagement.IpHelper.INTERFACE_HARDWARE_CROSSTIMESTAMP_head
    INTERFACE_HARDWARE_CROSSTIMESTAMP._fields_ = [
        ("SystemTimestamp1", UInt64),
        ("HardwareClockTimestamp", UInt64),
        ("SystemTimestamp2", UInt64),
    ]
    return INTERFACE_HARDWARE_CROSSTIMESTAMP
def _define_PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
NET_ADDRESS_FORMAT = Int32
NET_ADDRESS_FORMAT_UNSPECIFIED = 0
NET_ADDRESS_DNS_NAME = 1
NET_ADDRESS_IPV4 = 2
NET_ADDRESS_IPV6 = 3
GLOBAL_FILTER = Int32
GF_FRAGMENTS = 2
GF_STRONGHOST = 8
GF_FRAGCACHE = 9
PFFORWARD_ACTION = Int32
PF_ACTION_FORWARD = 0
PF_ACTION_DROP = 1
PFADDRESSTYPE = Int32
PF_IPV4 = 0
PF_IPV6 = 1
def _define_PF_FILTER_DESCRIPTOR_head():
    class PF_FILTER_DESCRIPTOR(Structure):
        pass
    return PF_FILTER_DESCRIPTOR
def _define_PF_FILTER_DESCRIPTOR():
    PF_FILTER_DESCRIPTOR = win32more.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head
    PF_FILTER_DESCRIPTOR._fields_ = [
        ("dwFilterFlags", UInt32),
        ("dwRule", UInt32),
        ("pfatType", win32more.NetworkManagement.IpHelper.PFADDRESSTYPE),
        ("SrcAddr", c_char_p_no),
        ("SrcMask", c_char_p_no),
        ("DstAddr", c_char_p_no),
        ("DstMask", c_char_p_no),
        ("dwProtocol", UInt32),
        ("fLateBound", UInt32),
        ("wSrcPort", UInt16),
        ("wDstPort", UInt16),
        ("wSrcPortHighRange", UInt16),
        ("wDstPortHighRange", UInt16),
    ]
    return PF_FILTER_DESCRIPTOR
def _define_PF_FILTER_STATS_head():
    class PF_FILTER_STATS(Structure):
        pass
    return PF_FILTER_STATS
def _define_PF_FILTER_STATS():
    PF_FILTER_STATS = win32more.NetworkManagement.IpHelper.PF_FILTER_STATS_head
    PF_FILTER_STATS._fields_ = [
        ("dwNumPacketsFiltered", UInt32),
        ("info", win32more.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR),
    ]
    return PF_FILTER_STATS
def _define_PF_INTERFACE_STATS_head():
    class PF_INTERFACE_STATS(Structure):
        pass
    return PF_INTERFACE_STATS
def _define_PF_INTERFACE_STATS():
    PF_INTERFACE_STATS = win32more.NetworkManagement.IpHelper.PF_INTERFACE_STATS_head
    PF_INTERFACE_STATS._fields_ = [
        ("pvDriverContext", c_void_p),
        ("dwFlags", UInt32),
        ("dwInDrops", UInt32),
        ("dwOutDrops", UInt32),
        ("eaInAction", win32more.NetworkManagement.IpHelper.PFFORWARD_ACTION),
        ("eaOutAction", win32more.NetworkManagement.IpHelper.PFFORWARD_ACTION),
        ("dwNumInFilters", UInt32),
        ("dwNumOutFilters", UInt32),
        ("dwFrag", UInt32),
        ("dwSpoof", UInt32),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
        ("liSYN", win32more.Foundation.LARGE_INTEGER),
        ("liTotalLogged", win32more.Foundation.LARGE_INTEGER),
        ("dwLostLogEntries", UInt32),
        ("FilterInfo", win32more.NetworkManagement.IpHelper.PF_FILTER_STATS * 0),
    ]
    return PF_INTERFACE_STATS
def _define_PF_LATEBIND_INFO_head():
    class PF_LATEBIND_INFO(Structure):
        pass
    return PF_LATEBIND_INFO
def _define_PF_LATEBIND_INFO():
    PF_LATEBIND_INFO = win32more.NetworkManagement.IpHelper.PF_LATEBIND_INFO_head
    PF_LATEBIND_INFO._fields_ = [
        ("SrcAddr", c_char_p_no),
        ("DstAddr", c_char_p_no),
        ("Mask", c_char_p_no),
    ]
    return PF_LATEBIND_INFO
PFFRAMETYPE = Int32
PFFT_FILTER = 1
PFFT_FRAG = 2
PFFT_SPOOF = 3
def _define_PFLOGFRAME_head():
    class PFLOGFRAME(Structure):
        pass
    return PFLOGFRAME
def _define_PFLOGFRAME():
    PFLOGFRAME = win32more.NetworkManagement.IpHelper.PFLOGFRAME_head
    PFLOGFRAME._fields_ = [
        ("Timestamp", win32more.Foundation.LARGE_INTEGER),
        ("pfeTypeOfFrame", win32more.NetworkManagement.IpHelper.PFFRAMETYPE),
        ("dwTotalSizeUsed", UInt32),
        ("dwFilterRule", UInt32),
        ("wSizeOfAdditionalData", UInt16),
        ("wSizeOfIpHeader", UInt16),
        ("dwInterfaceName", UInt32),
        ("dwIPIndex", UInt32),
        ("bPacketData", Byte * 0),
    ]
    return PFLOGFRAME
def _define_GetIfEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IF_ROW2_head), use_last_error=False)(("GetIfEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIfEntry2Ex():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.NetworkManagement.IpHelper.MIB_IF_ENTRY_LEVEL,POINTER(win32more.NetworkManagement.IpHelper.MIB_IF_ROW2_head), use_last_error=False)(("GetIfEntry2Ex", windll["IPHLPAPI"]), ((1, 'Level'),(1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIfTable2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_IF_TABLE2_head)), use_last_error=False)(("GetIfTable2", windll["IPHLPAPI"]), ((1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIfTable2Ex():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.NetworkManagement.IpHelper.MIB_IF_TABLE_LEVEL,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_IF_TABLE2_head)), use_last_error=False)(("GetIfTable2Ex", windll["IPHLPAPI"]), ((1, 'Level'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIfStackTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_IFSTACK_TABLE_head)), use_last_error=False)(("GetIfStackTable", windll["IPHLPAPI"]), ((1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInvertedIfStackTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_TABLE_head)), use_last_error=False)(("GetInvertedIfStackTable", windll["IPHLPAPI"]), ((1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpInterfaceEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head), use_last_error=False)(("GetIpInterfaceEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpInterfaceTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_TABLE_head)), use_last_error=False)(("GetIpInterfaceTable", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeIpInterfaceEntry():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head), use_last_error=False)(("InitializeIpInterfaceEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyIpInterfaceChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,win32more.NetworkManagement.IpHelper.PIPINTERFACE_CHANGE_CALLBACK,c_void_p,win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NotifyIpInterfaceChange", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Callback'),(1, 'CallerContext'),(1, 'InitialNotification'),(1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpInterfaceEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head), use_last_error=False)(("SetIpInterfaceEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpNetworkConnectionBandwidthEstimates():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,UInt16,POINTER(win32more.NetworkManagement.IpHelper.MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES_head), use_last_error=False)(("GetIpNetworkConnectionBandwidthEstimates", windll["IPHLPAPI"]), ((1, 'InterfaceIndex'),(1, 'AddressFamily'),(1, 'BandwidthEstimates'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateUnicastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head), use_last_error=False)(("CreateUnicastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteUnicastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head), use_last_error=False)(("DeleteUnicastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUnicastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head), use_last_error=False)(("GetUnicastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUnicastIpAddressTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE_head)), use_last_error=False)(("GetUnicastIpAddressTable", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeUnicastIpAddressEntry():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head), use_last_error=False)(("InitializeUnicastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyUnicastIpAddressChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,win32more.NetworkManagement.IpHelper.PUNICAST_IPADDRESS_CHANGE_CALLBACK,c_void_p,win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NotifyUnicastIpAddressChange", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Callback'),(1, 'CallerContext'),(1, 'InitialNotification'),(1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyStableUnicastIpAddressTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE_head)),win32more.NetworkManagement.IpHelper.PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK,c_void_p,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NotifyStableUnicastIpAddressTable", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),(1, 'CallerCallback'),(1, 'CallerContext'),(1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUnicastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head), use_last_error=False)(("SetUnicastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAnycastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW_head), use_last_error=False)(("CreateAnycastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteAnycastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW_head), use_last_error=False)(("DeleteAnycastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAnycastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW_head), use_last_error=False)(("GetAnycastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAnycastIpAddressTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_TABLE_head)), use_last_error=False)(("GetAnycastIpAddressTable", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMulticastIpAddressEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_ROW_head), use_last_error=False)(("GetMulticastIpAddressEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMulticastIpAddressTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_TABLE_head)), use_last_error=False)(("GetMulticastIpAddressTable", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateIpForwardEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head), use_last_error=False)(("CreateIpForwardEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteIpForwardEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head), use_last_error=False)(("DeleteIpForwardEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBestRoute2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),UInt32,POINTER(win32more.Networking.WinSock.SOCKADDR_INET_head),POINTER(win32more.Networking.WinSock.SOCKADDR_INET_head),UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head),POINTER(win32more.Networking.WinSock.SOCKADDR_INET_head), use_last_error=False)(("GetBestRoute2", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'InterfaceIndex'),(1, 'SourceAddress'),(1, 'DestinationAddress'),(1, 'AddressSortOptions'),(1, 'BestRoute'),(1, 'BestSourceAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpForwardEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head), use_last_error=False)(("GetIpForwardEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpForwardTable2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_TABLE2_head)), use_last_error=False)(("GetIpForwardTable2", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeIpForwardEntry():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head), use_last_error=False)(("InitializeIpForwardEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyRouteChange2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,win32more.NetworkManagement.IpHelper.PIPFORWARD_CHANGE_CALLBACK,c_void_p,win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NotifyRouteChange2", windll["IPHLPAPI"]), ((1, 'AddressFamily'),(1, 'Callback'),(1, 'CallerContext'),(1, 'InitialNotification'),(1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpForwardEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head), use_last_error=False)(("SetIpForwardEntry2", windll["IPHLPAPI"]), ((1, 'Route'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushIpPathTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16, use_last_error=False)(("FlushIpPathTable", windll["IPHLPAPI"]), ((1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpPathEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPPATH_ROW_head), use_last_error=False)(("GetIpPathEntry", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpPathTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_IPPATH_TABLE_head)), use_last_error=False)(("GetIpPathTable", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateIpNetEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head), use_last_error=False)(("CreateIpNetEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteIpNetEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head), use_last_error=False)(("DeleteIpNetEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushIpNetTable2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,UInt32, use_last_error=False)(("FlushIpNetTable2", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'InterfaceIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpNetEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head), use_last_error=False)(("GetIpNetEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpNetTable2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt16,POINTER(POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNET_TABLE2_head)), use_last_error=False)(("GetIpNetTable2", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Table'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResolveIpNetEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head),POINTER(win32more.Networking.WinSock.SOCKADDR_INET_head), use_last_error=False)(("ResolveIpNetEntry2", windll["IPHLPAPI"]), ((1, 'Row'),(1, 'SourceAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpNetEntry2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head), use_last_error=False)(("SetIpNetEntry2", windll["IPHLPAPI"]), ((1, 'Row'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyTeredoPortChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.NetworkManagement.IpHelper.PTEREDO_PORT_CHANGE_CALLBACK,c_void_p,win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NotifyTeredoPortChange", windll["IPHLPAPI"]), ((1, 'Callback'),(1, 'CallerContext'),(1, 'InitialNotification'),(1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTeredoPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(UInt16), use_last_error=False)(("GetTeredoPort", windll["IPHLPAPI"]), ((1, 'Port'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelMibChangeNotify2():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE, use_last_error=False)(("CancelMibChangeNotify2", windll["IPHLPAPI"]), ((1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeMibTable():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("FreeMibTable", windll["IPHLPAPI"]), ((1, 'Memory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSortedAddressPairs():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Networking.WinSock.SOCKADDR_IN6_head),UInt32,POINTER(win32more.Networking.WinSock.SOCKADDR_IN6_head),UInt32,UInt32,POINTER(POINTER(win32more.Networking.WinSock.SOCKADDR_IN6_PAIR_head)),POINTER(UInt32), use_last_error=False)(("CreateSortedAddressPairs", windll["IPHLPAPI"]), ((1, 'SourceAddressList'),(1, 'SourceAddressCount'),(1, 'DestinationAddressList'),(1, 'DestinationAddressCount'),(1, 'AddressSortOptions'),(1, 'SortedAddressPairList'),(1, 'SortedAddressPairCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertCompartmentGuidToId():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(Guid),POINTER(UInt32), use_last_error=False)(("ConvertCompartmentGuidToId", windll["IPHLPAPI"]), ((1, 'CompartmentGuid'),(1, 'CompartmentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertCompartmentIdToGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(Guid), use_last_error=False)(("ConvertCompartmentIdToGuid", windll["IPHLPAPI"]), ((1, 'CompartmentId'),(1, 'CompartmentGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceNameToLuidA():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head), use_last_error=False)(("ConvertInterfaceNameToLuidA", windll["IPHLPAPI"]), ((1, 'InterfaceName'),(1, 'InterfaceLuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceNameToLuidW():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head), use_last_error=False)(("ConvertInterfaceNameToLuidW", windll["IPHLPAPI"]), ((1, 'InterfaceName'),(1, 'InterfaceLuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceNameToLuid():
    return win32more.NetworkManagement.IpHelper.ConvertInterfaceNameToLuidW
def _define_ConvertInterfaceLuidToNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(Byte),UIntPtr, use_last_error=False)(("ConvertInterfaceLuidToNameA", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'InterfaceName'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceLuidToNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(Char),UIntPtr, use_last_error=False)(("ConvertInterfaceLuidToNameW", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'InterfaceName'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceLuidToName():
    return win32more.NetworkManagement.IpHelper.ConvertInterfaceLuidToNameW
def _define_ConvertInterfaceLuidToIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(UInt32), use_last_error=False)(("ConvertInterfaceLuidToIndex", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'InterfaceIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceIndexToLuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head), use_last_error=False)(("ConvertInterfaceIndexToLuid", windll["IPHLPAPI"]), ((1, 'InterfaceIndex'),(1, 'InterfaceLuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceLuidToAlias():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(Char),UIntPtr, use_last_error=False)(("ConvertInterfaceLuidToAlias", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'InterfaceAlias'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceAliasToLuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head), use_last_error=False)(("ConvertInterfaceAliasToLuid", windll["IPHLPAPI"]), ((1, 'InterfaceAlias'),(1, 'InterfaceLuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceLuidToGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(Guid), use_last_error=False)(("ConvertInterfaceLuidToGuid", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'InterfaceGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertInterfaceGuidToLuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(Guid),POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head), use_last_error=False)(("ConvertInterfaceGuidToLuid", windll["IPHLPAPI"]), ((1, 'InterfaceGuid'),(1, 'InterfaceLuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_if_nametoindex():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("if_nametoindex", windll["IPHLPAPI"]), ((1, 'InterfaceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_if_indextoname():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,UInt32,POINTER(Byte), use_last_error=False)(("if_indextoname", windll["IPHLPAPI"]), ((1, 'InterfaceIndex'),(1, 'InterfaceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentThreadCompartmentId():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetCurrentThreadCompartmentId", windll["IPHLPAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCurrentThreadCompartmentId():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32, use_last_error=False)(("SetCurrentThreadCompartmentId", windll["IPHLPAPI"]), ((1, 'CompartmentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentThreadCompartmentScope():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetCurrentThreadCompartmentScope", windll["IPHLPAPI"]), ((1, 'CompartmentScope'),(1, 'CompartmentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCurrentThreadCompartmentScope():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32, use_last_error=False)(("SetCurrentThreadCompartmentScope", windll["IPHLPAPI"]), ((1, 'CompartmentScope'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetJobCompartmentId():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("GetJobCompartmentId", windll["IPHLPAPI"]), ((1, 'JobHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetJobCompartmentId():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("SetJobCompartmentId", windll["IPHLPAPI"]), ((1, 'JobHandle'),(1, 'CompartmentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSessionCompartmentId():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("GetSessionCompartmentId", windll["IPHLPAPI"]), ((1, 'SessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSessionCompartmentId():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,UInt32, use_last_error=False)(("SetSessionCompartmentId", windll["IPHLPAPI"]), ((1, 'SessionId'),(1, 'CompartmentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDefaultCompartmentId():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetDefaultCompartmentId", windll["IPHLPAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNetworkInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(Guid),POINTER(UInt32),POINTER(UInt32),POINTER(Char),UInt32, use_last_error=False)(("GetNetworkInformation", windll["IPHLPAPI"]), ((1, 'NetworkGuid'),(1, 'CompartmentId'),(1, 'SiteId'),(1, 'NetworkName'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetNetworkInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(Guid),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("SetNetworkInformation", windll["IPHLPAPI"]), ((1, 'NetworkGuid'),(1, 'CompartmentId'),(1, 'NetworkName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertLengthToIpv4Mask():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(UInt32), use_last_error=False)(("ConvertLengthToIpv4Mask", windll["IPHLPAPI"]), ((1, 'MaskLength'),(1, 'Mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertIpv4MaskToLength():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,c_char_p_no, use_last_error=False)(("ConvertIpv4MaskToLength", windll["IPHLPAPI"]), ((1, 'Mask'),(1, 'MaskLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDnsSettings():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.DNS_SETTINGS_head), use_last_error=False)(("GetDnsSettings", windll["IPHLPAPI"]), ((1, 'Settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeDnsSettings():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.IpHelper.DNS_SETTINGS_head), use_last_error=False)(("FreeDnsSettings", windll["IPHLPAPI"]), ((1, 'Settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDnsSettings():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.NetworkManagement.IpHelper.DNS_SETTINGS_head), use_last_error=False)(("SetDnsSettings", windll["IPHLPAPI"]), ((1, 'Settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInterfaceDnsSettings():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,Guid,POINTER(win32more.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_head), use_last_error=False)(("GetInterfaceDnsSettings", windll["IPHLPAPI"]), ((1, 'Interface'),(1, 'Settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeInterfaceDnsSettings():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_head), use_last_error=False)(("FreeInterfaceDnsSettings", windll["IPHLPAPI"]), ((1, 'Settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetInterfaceDnsSettings():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,Guid,POINTER(win32more.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_head), use_last_error=False)(("SetInterfaceDnsSettings", windll["IPHLPAPI"]), ((1, 'Interface'),(1, 'Settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNetworkConnectivityHint():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT_head), use_last_error=False)(("GetNetworkConnectivityHint", windll["IPHLPAPI"]), ((1, 'ConnectivityHint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNetworkConnectivityHintForInterface():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(win32more.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT_head), use_last_error=False)(("GetNetworkConnectivityHintForInterface", windll["IPHLPAPI"]), ((1, 'InterfaceIndex'),(1, 'ConnectivityHint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyNetworkConnectivityHintChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.NetworkManagement.IpHelper.PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK,c_void_p,win32more.Foundation.BOOLEAN,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NotifyNetworkConnectivityHintChange", windll["IPHLPAPI"]), ((1, 'Callback'),(1, 'CallerContext'),(1, 'InitialNotification'),(1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IcmpCreateFile():
    try:
        return WINFUNCTYPE(win32more.NetworkManagement.IpHelper.IcmpHandle, use_last_error=True)(("IcmpCreateFile", windll["IPHLPAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_Icmp6CreateFile():
    try:
        return WINFUNCTYPE(win32more.NetworkManagement.IpHelper.IcmpHandle, use_last_error=True)(("Icmp6CreateFile", windll["IPHLPAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_IcmpCloseHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.NetworkManagement.IpHelper.IcmpHandle, use_last_error=True)(("IcmpCloseHandle", windll["IPHLPAPI"]), ((1, 'IcmpHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IcmpSendEcho():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.IpHelper.IcmpHandle,UInt32,c_void_p,UInt16,POINTER(win32more.NetworkManagement.IpHelper.ip_option_information_head),c_void_p,UInt32,UInt32, use_last_error=True)(("IcmpSendEcho", windll["IPHLPAPI"]), ((1, 'IcmpHandle'),(1, 'DestinationAddress'),(1, 'RequestData'),(1, 'RequestSize'),(1, 'RequestOptions'),(1, 'ReplyBuffer'),(1, 'ReplySize'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IcmpSendEcho2():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.IpHelper.IcmpHandle,win32more.Foundation.HANDLE,win32more.System.WindowsProgramming.PIO_APC_ROUTINE,c_void_p,UInt32,c_void_p,UInt16,POINTER(win32more.NetworkManagement.IpHelper.ip_option_information_head),c_void_p,UInt32,UInt32, use_last_error=True)(("IcmpSendEcho2", windll["IPHLPAPI"]), ((1, 'IcmpHandle'),(1, 'Event'),(1, 'ApcRoutine'),(1, 'ApcContext'),(1, 'DestinationAddress'),(1, 'RequestData'),(1, 'RequestSize'),(1, 'RequestOptions'),(1, 'ReplyBuffer'),(1, 'ReplySize'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IcmpSendEcho2Ex():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.IpHelper.IcmpHandle,win32more.Foundation.HANDLE,win32more.System.WindowsProgramming.PIO_APC_ROUTINE,c_void_p,UInt32,UInt32,c_void_p,UInt16,POINTER(win32more.NetworkManagement.IpHelper.ip_option_information_head),c_void_p,UInt32,UInt32, use_last_error=True)(("IcmpSendEcho2Ex", windll["IPHLPAPI"]), ((1, 'IcmpHandle'),(1, 'Event'),(1, 'ApcRoutine'),(1, 'ApcContext'),(1, 'SourceAddress'),(1, 'DestinationAddress'),(1, 'RequestData'),(1, 'RequestSize'),(1, 'RequestOptions'),(1, 'ReplyBuffer'),(1, 'ReplySize'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Icmp6SendEcho2():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.IpHelper.IcmpHandle,win32more.Foundation.HANDLE,win32more.System.WindowsProgramming.PIO_APC_ROUTINE,c_void_p,POINTER(win32more.Networking.WinSock.SOCKADDR_IN6_head),POINTER(win32more.Networking.WinSock.SOCKADDR_IN6_head),c_void_p,UInt16,POINTER(win32more.NetworkManagement.IpHelper.ip_option_information_head),c_void_p,UInt32,UInt32, use_last_error=True)(("Icmp6SendEcho2", windll["IPHLPAPI"]), ((1, 'IcmpHandle'),(1, 'Event'),(1, 'ApcRoutine'),(1, 'ApcContext'),(1, 'SourceAddress'),(1, 'DestinationAddress'),(1, 'RequestData'),(1, 'RequestSize'),(1, 'RequestOptions'),(1, 'ReplyBuffer'),(1, 'ReplySize'),(1, 'Timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IcmpParseReplies():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32, use_last_error=True)(("IcmpParseReplies", windll["IPHLPAPI"]), ((1, 'ReplyBuffer'),(1, 'ReplySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Icmp6ParseReplies():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32, use_last_error=True)(("Icmp6ParseReplies", windll["IPHLPAPI"]), ((1, 'ReplyBuffer'),(1, 'ReplySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumberOfInterfaces():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32), use_last_error=False)(("GetNumberOfInterfaces", windll["IPHLPAPI"]), ((1, 'pdwNumIf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIfEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IFROW_head), use_last_error=False)(("GetIfEntry", windll["IPHLPAPI"]), ((1, 'pIfRow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIfTable():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IFTABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetIfTable", windll["IPHLPAPI"]), ((1, 'pIfTable'),(1, 'pdwSize'),(1, 'bOrder'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpAddrTable():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPADDRTABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetIpAddrTable", windll["IPHLPAPI"]), ((1, 'pIpAddrTable'),(1, 'pdwSize'),(1, 'bOrder'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpNetTable():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNETTABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetIpNetTable", windll["IPHLPAPI"]), ((1, 'IpNetTable'),(1, 'SizePointer'),(1, 'Order'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpForwardTable():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARDTABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetIpForwardTable", windll["IPHLPAPI"]), ((1, 'pIpForwardTable'),(1, 'pdwSize'),(1, 'bOrder'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTcpTable():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPTABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetTcpTable", windll["IPHLPAPI"]), ((1, 'TcpTable'),(1, 'SizePointer'),(1, 'Order'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExtendedTcpTable():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(UInt32),win32more.Foundation.BOOL,UInt32,win32more.NetworkManagement.IpHelper.TCP_TABLE_CLASS,UInt32, use_last_error=False)(("GetExtendedTcpTable", windll["IPHLPAPI"]), ((1, 'pTcpTable'),(1, 'pdwSize'),(1, 'bOrder'),(1, 'ulAf'),(1, 'TableClass'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOwnerModuleFromTcpEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_MODULE_head),win32more.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS,c_void_p,POINTER(UInt32), use_last_error=False)(("GetOwnerModuleFromTcpEntry", windll["IPHLPAPI"]), ((1, 'pTcpEntry'),(1, 'Class'),(1, 'pBuffer'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUdpTable():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_UDPTABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetUdpTable", windll["IPHLPAPI"]), ((1, 'UdpTable'),(1, 'SizePointer'),(1, 'Order'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExtendedUdpTable():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(UInt32),win32more.Foundation.BOOL,UInt32,win32more.NetworkManagement.IpHelper.UDP_TABLE_CLASS,UInt32, use_last_error=False)(("GetExtendedUdpTable", windll["IPHLPAPI"]), ((1, 'pUdpTable'),(1, 'pdwSize'),(1, 'bOrder'),(1, 'ulAf'),(1, 'TableClass'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOwnerModuleFromUdpEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_MODULE_head),win32more.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS,c_void_p,POINTER(UInt32), use_last_error=False)(("GetOwnerModuleFromUdpEntry", windll["IPHLPAPI"]), ((1, 'pUdpEntry'),(1, 'Class'),(1, 'pBuffer'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTcpTable2():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPTABLE2_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetTcpTable2", windll["IPHLPAPI"]), ((1, 'TcpTable'),(1, 'SizePointer'),(1, 'Order'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTcp6Table():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCP6TABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetTcp6Table", windll["IPHLPAPI"]), ((1, 'TcpTable'),(1, 'SizePointer'),(1, 'Order'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTcp6Table2():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCP6TABLE2_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetTcp6Table2", windll["IPHLPAPI"]), ((1, 'TcpTable'),(1, 'SizePointer'),(1, 'Order'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPerTcpConnectionEStats():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPROW_LH_head),win32more.NetworkManagement.IpHelper.TCP_ESTATS_TYPE,c_char_p_no,UInt32,UInt32,c_char_p_no,UInt32,UInt32,c_char_p_no,UInt32,UInt32, use_last_error=False)(("GetPerTcpConnectionEStats", windll["IPHLPAPI"]), ((1, 'Row'),(1, 'EstatsType'),(1, 'Rw'),(1, 'RwVersion'),(1, 'RwSize'),(1, 'Ros'),(1, 'RosVersion'),(1, 'RosSize'),(1, 'Rod'),(1, 'RodVersion'),(1, 'RodSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPerTcpConnectionEStats():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPROW_LH_head),win32more.NetworkManagement.IpHelper.TCP_ESTATS_TYPE,c_char_p_no,UInt32,UInt32,UInt32, use_last_error=False)(("SetPerTcpConnectionEStats", windll["IPHLPAPI"]), ((1, 'Row'),(1, 'EstatsType'),(1, 'Rw'),(1, 'RwVersion'),(1, 'RwSize'),(1, 'Offset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPerTcp6ConnectionEStats():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_head),win32more.NetworkManagement.IpHelper.TCP_ESTATS_TYPE,c_char_p_no,UInt32,UInt32,c_char_p_no,UInt32,UInt32,c_char_p_no,UInt32,UInt32, use_last_error=False)(("GetPerTcp6ConnectionEStats", windll["IPHLPAPI"]), ((1, 'Row'),(1, 'EstatsType'),(1, 'Rw'),(1, 'RwVersion'),(1, 'RwSize'),(1, 'Ros'),(1, 'RosVersion'),(1, 'RosSize'),(1, 'Rod'),(1, 'RodVersion'),(1, 'RodSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPerTcp6ConnectionEStats():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_head),win32more.NetworkManagement.IpHelper.TCP_ESTATS_TYPE,c_char_p_no,UInt32,UInt32,UInt32, use_last_error=False)(("SetPerTcp6ConnectionEStats", windll["IPHLPAPI"]), ((1, 'Row'),(1, 'EstatsType'),(1, 'Rw'),(1, 'RwVersion'),(1, 'RwSize'),(1, 'Offset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOwnerModuleFromTcp6Entry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_MODULE_head),win32more.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS,c_void_p,POINTER(UInt32), use_last_error=False)(("GetOwnerModuleFromTcp6Entry", windll["IPHLPAPI"]), ((1, 'pTcpEntry'),(1, 'Class'),(1, 'pBuffer'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUdp6Table():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_UDP6TABLE_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("GetUdp6Table", windll["IPHLPAPI"]), ((1, 'Udp6Table'),(1, 'SizePointer'),(1, 'Order'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOwnerModuleFromUdp6Entry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_MODULE_head),win32more.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS,c_void_p,POINTER(UInt32), use_last_error=False)(("GetOwnerModuleFromUdp6Entry", windll["IPHLPAPI"]), ((1, 'pUdpEntry'),(1, 'Class'),(1, 'pBuffer'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOwnerModuleFromPidAndInfo():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt64),win32more.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS,c_void_p,POINTER(UInt32), use_last_error=False)(("GetOwnerModuleFromPidAndInfo", windll["IPHLPAPI"]), ((1, 'ulPid'),(1, 'pInfo'),(1, 'Class'),(1, 'pBuffer'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpStatistics():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head), use_last_error=False)(("GetIpStatistics", windll["IPHLPAPI"]), ((1, 'Statistics'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIcmpStatistics():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_ICMP_head), use_last_error=False)(("GetIcmpStatistics", windll["IPHLPAPI"]), ((1, 'Statistics'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTcpStatistics():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPSTATS_LH_head), use_last_error=False)(("GetTcpStatistics", windll["IPHLPAPI"]), ((1, 'Statistics'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUdpStatistics():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_UDPSTATS_head), use_last_error=False)(("GetUdpStatistics", windll["IPHLPAPI"]), ((1, 'Stats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpStatisticsEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head),UInt32, use_last_error=False)(("SetIpStatisticsEx", windll["IPHLPAPI"]), ((1, 'Statistics'),(1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpStatisticsEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head),win32more.NetworkManagement.IpHelper.ADDRESS_FAMILY, use_last_error=False)(("GetIpStatisticsEx", windll["IPHLPAPI"]), ((1, 'Statistics'),(1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIcmpStatisticsEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_ICMP_EX_XPSP1_head),UInt32, use_last_error=False)(("GetIcmpStatisticsEx", windll["IPHLPAPI"]), ((1, 'Statistics'),(1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTcpStatisticsEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPSTATS_LH_head),win32more.NetworkManagement.IpHelper.ADDRESS_FAMILY, use_last_error=False)(("GetTcpStatisticsEx", windll["IPHLPAPI"]), ((1, 'Statistics'),(1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUdpStatisticsEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_UDPSTATS_head),win32more.NetworkManagement.IpHelper.ADDRESS_FAMILY, use_last_error=False)(("GetUdpStatisticsEx", windll["IPHLPAPI"]), ((1, 'Statistics'),(1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTcpStatisticsEx2():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPSTATS2_head),win32more.NetworkManagement.IpHelper.ADDRESS_FAMILY, use_last_error=False)(("GetTcpStatisticsEx2", windll["IPHLPAPI"]), ((1, 'Statistics'),(1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUdpStatisticsEx2():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_UDPSTATS2_head),win32more.NetworkManagement.IpHelper.ADDRESS_FAMILY, use_last_error=False)(("GetUdpStatisticsEx2", windll["IPHLPAPI"]), ((1, 'Statistics'),(1, 'Family'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIfEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IFROW_head), use_last_error=False)(("SetIfEntry", windll["IPHLPAPI"]), ((1, 'pIfRow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateIpForwardEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head), use_last_error=False)(("CreateIpForwardEntry", windll["IPHLPAPI"]), ((1, 'pRoute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpForwardEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head), use_last_error=False)(("SetIpForwardEntry", windll["IPHLPAPI"]), ((1, 'pRoute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteIpForwardEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head), use_last_error=False)(("DeleteIpForwardEntry", windll["IPHLPAPI"]), ((1, 'pRoute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpStatistics():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head), use_last_error=False)(("SetIpStatistics", windll["IPHLPAPI"]), ((1, 'pIpStats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpTTL():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("SetIpTTL", windll["IPHLPAPI"]), ((1, 'nTTL'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateIpNetEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNETROW_LH_head), use_last_error=False)(("CreateIpNetEntry", windll["IPHLPAPI"]), ((1, 'pArpEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIpNetEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNETROW_LH_head), use_last_error=False)(("SetIpNetEntry", windll["IPHLPAPI"]), ((1, 'pArpEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteIpNetEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPNETROW_LH_head), use_last_error=False)(("DeleteIpNetEntry", windll["IPHLPAPI"]), ((1, 'pArpEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushIpNetTable():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("FlushIpNetTable", windll["IPHLPAPI"]), ((1, 'dwIfIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProxyArpEntry():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,UInt32, use_last_error=False)(("CreateProxyArpEntry", windll["IPHLPAPI"]), ((1, 'dwAddress'),(1, 'dwMask'),(1, 'dwIfIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteProxyArpEntry():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,UInt32, use_last_error=False)(("DeleteProxyArpEntry", windll["IPHLPAPI"]), ((1, 'dwAddress'),(1, 'dwMask'),(1, 'dwIfIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTcpEntry():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_TCPROW_LH_head), use_last_error=False)(("SetTcpEntry", windll["IPHLPAPI"]), ((1, 'pTcpRow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInterfaceInfo():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.IP_INTERFACE_INFO_head),POINTER(UInt32), use_last_error=False)(("GetInterfaceInfo", windll["IPHLPAPI"]), ((1, 'pIfTable'),(1, 'dwOutBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUniDirectionalAdapterInfo():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.IP_UNIDIRECTIONAL_ADAPTER_ADDRESS_head),POINTER(UInt32), use_last_error=False)(("GetUniDirectionalAdapterInfo", windll["IPHLPAPI"]), ((1, 'pIPIfInfo'),(1, 'dwOutBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NhpAllocateAndGetInterfaceInfoFromStack():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.NetworkManagement.IpHelper.ip_interface_name_info_w2ksp1_head)),POINTER(UInt32),win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("NhpAllocateAndGetInterfaceInfoFromStack", windll["IPHLPAPI"]), ((1, 'ppTable'),(1, 'pdwCount'),(1, 'bOrder'),(1, 'hHeap'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBestInterface():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("GetBestInterface", windll["IPHLPAPI"]), ((1, 'dwDestAddr'),(1, 'pdwBestIfIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBestInterfaceEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.WinSock.SOCKADDR_head),POINTER(UInt32), use_last_error=False)(("GetBestInterfaceEx", windll["IPHLPAPI"]), ((1, 'pDestAddr'),(1, 'pdwBestIfIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBestRoute():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,POINTER(win32more.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head), use_last_error=False)(("GetBestRoute", windll["IPHLPAPI"]), ((1, 'dwDestAddr'),(1, 'dwSourceAddr'),(1, 'pBestRoute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyAddrChange():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("NotifyAddrChange", windll["IPHLPAPI"]), ((1, 'Handle'),(1, 'overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyRouteChange():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("NotifyRouteChange", windll["IPHLPAPI"]), ((1, 'Handle'),(1, 'overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelIPChangeNotify():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("CancelIPChangeNotify", windll["IPHLPAPI"]), ((1, 'notifyOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAdapterIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("GetAdapterIndex", windll["IPHLPAPI"]), ((1, 'AdapterName'),(1, 'IfIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddIPAddress():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("AddIPAddress", windll["IPHLPAPI"]), ((1, 'Address'),(1, 'IpMask'),(1, 'IfIndex'),(1, 'NTEContext'),(1, 'NTEInstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteIPAddress():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("DeleteIPAddress", windll["IPHLPAPI"]), ((1, 'NTEContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNetworkParams():
    try:
        return WINFUNCTYPE(win32more.Foundation.WIN32_ERROR,POINTER(win32more.NetworkManagement.IpHelper.FIXED_INFO_W2KSP1_head),POINTER(UInt32), use_last_error=False)(("GetNetworkParams", windll["IPHLPAPI"]), ((1, 'pFixedInfo'),(1, 'pOutBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAdaptersInfo():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_INFO_head),POINTER(UInt32), use_last_error=False)(("GetAdaptersInfo", windll["IPHLPAPI"]), ((1, 'AdapterInfo'),(1, 'SizePointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAdapterOrderMap():
    try:
        return WINFUNCTYPE(POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_ORDER_MAP_head), use_last_error=False)(("GetAdapterOrderMap", windll["IPHLPAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAdaptersAddresses():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.IpHelper.ADDRESS_FAMILY,win32more.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_LH_head),POINTER(UInt32), use_last_error=False)(("GetAdaptersAddresses", windll["IPHLPAPI"]), ((1, 'Family'),(1, 'Flags'),(1, 'Reserved'),(1, 'AdapterAddresses'),(1, 'SizePointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPerAdapterInfo():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.NetworkManagement.IpHelper.IP_PER_ADAPTER_INFO_W2KSP1_head),POINTER(UInt32), use_last_error=False)(("GetPerAdapterInfo", windll["IPHLPAPI"]), ((1, 'IfIndex'),(1, 'pPerAdapterInfo'),(1, 'pOutBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInterfaceActiveTimestampCapabilities():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(win32more.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES_head), use_last_error=False)(("GetInterfaceActiveTimestampCapabilities", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'TimestampCapabilites'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInterfaceSupportedTimestampCapabilities():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(win32more.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES_head), use_last_error=False)(("GetInterfaceSupportedTimestampCapabilities", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'TimestampCapabilites'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CaptureInterfaceHardwareCrossTimestamp():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.NET_LUID_LH_head),POINTER(win32more.NetworkManagement.IpHelper.INTERFACE_HARDWARE_CROSSTIMESTAMP_head), use_last_error=False)(("CaptureInterfaceHardwareCrossTimestamp", windll["IPHLPAPI"]), ((1, 'InterfaceLuid'),(1, 'CrossTimestamp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterInterfaceTimestampConfigChange():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.IpHelper.PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE), use_last_error=False)(("RegisterInterfaceTimestampConfigChange", windll["IPHLPAPI"]), ((1, 'Callback'),(1, 'CallerContext'),(1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterInterfaceTimestampConfigChange():
    try:
        return WINFUNCTYPE(Void,win32more.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE, use_last_error=False)(("UnregisterInterfaceTimestampConfigChange", windll["IPHLPAPI"]), ((1, 'NotificationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IpReleaseAddress():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP_head), use_last_error=False)(("IpReleaseAddress", windll["IPHLPAPI"]), ((1, 'AdapterInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IpRenewAddress():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP_head), use_last_error=False)(("IpRenewAddress", windll["IPHLPAPI"]), ((1, 'AdapterInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendARP():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,c_void_p,POINTER(UInt32), use_last_error=False)(("SendARP", windll["IPHLPAPI"]), ((1, 'DestIP'),(1, 'SrcIP'),(1, 'pMacAddr'),(1, 'PhyAddrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRTTAndHopCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=True)(("GetRTTAndHopCount", windll["IPHLPAPI"]), ((1, 'DestIpAddress'),(1, 'HopCount'),(1, 'MaxHops'),(1, 'RTT'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFriendlyIfIndex():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("GetFriendlyIfIndex", windll["IPHLPAPI"]), ((1, 'IfIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableRouter():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("EnableRouter", windll["IPHLPAPI"]), ((1, 'pHandle'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnenableRouter():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32), use_last_error=False)(("UnenableRouter", windll["IPHLPAPI"]), ((1, 'pOverlapped'),(1, 'lpdwEnableCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisableMediaSense():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("DisableMediaSense", windll["IPHLPAPI"]), ((1, 'pHandle'),(1, 'pOverLapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RestoreMediaSense():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(UInt32), use_last_error=False)(("RestoreMediaSense", windll["IPHLPAPI"]), ((1, 'pOverlapped'),(1, 'lpdwEnableCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIpErrorString():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("GetIpErrorString", windll["IPHLPAPI"]), ((1, 'ErrorCode'),(1, 'Buffer'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResolveNeighbor():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Networking.WinSock.SOCKADDR_head),c_void_p,POINTER(UInt32), use_last_error=False)(("ResolveNeighbor", windll["IPHLPAPI"]), ((1, 'NetworkAddress'),(1, 'PhysicalAddress'),(1, 'PhysicalAddressLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePersistentTcpPortReservation():
    try:
        return WINFUNCTYPE(UInt32,UInt16,UInt16,POINTER(UInt64), use_last_error=False)(("CreatePersistentTcpPortReservation", windll["IPHLPAPI"]), ((1, 'StartPort'),(1, 'NumberOfPorts'),(1, 'Token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePersistentUdpPortReservation():
    try:
        return WINFUNCTYPE(UInt32,UInt16,UInt16,POINTER(UInt64), use_last_error=False)(("CreatePersistentUdpPortReservation", windll["IPHLPAPI"]), ((1, 'StartPort'),(1, 'NumberOfPorts'),(1, 'Token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeletePersistentTcpPortReservation():
    try:
        return WINFUNCTYPE(UInt32,UInt16,UInt16, use_last_error=False)(("DeletePersistentTcpPortReservation", windll["IPHLPAPI"]), ((1, 'StartPort'),(1, 'NumberOfPorts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeletePersistentUdpPortReservation():
    try:
        return WINFUNCTYPE(UInt32,UInt16,UInt16, use_last_error=False)(("DeletePersistentUdpPortReservation", windll["IPHLPAPI"]), ((1, 'StartPort'),(1, 'NumberOfPorts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPersistentTcpPortReservation():
    try:
        return WINFUNCTYPE(UInt32,UInt16,UInt16,POINTER(UInt64), use_last_error=False)(("LookupPersistentTcpPortReservation", windll["IPHLPAPI"]), ((1, 'StartPort'),(1, 'NumberOfPorts'),(1, 'Token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPersistentUdpPortReservation():
    try:
        return WINFUNCTYPE(UInt32,UInt16,UInt16,POINTER(UInt64), use_last_error=False)(("LookupPersistentUdpPortReservation", windll["IPHLPAPI"]), ((1, 'StartPort'),(1, 'NumberOfPorts'),(1, 'Token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfCreateInterface():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.NetworkManagement.IpHelper.PFFORWARD_ACTION,win32more.NetworkManagement.IpHelper.PFFORWARD_ACTION,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(c_void_p), use_last_error=False)(("PfCreateInterface", windll["IPHLPAPI"]), ((1, 'dwName'),(1, 'inAction'),(1, 'outAction'),(1, 'bUseLog'),(1, 'bMustBeUnique'),(1, 'ppInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfDeleteInterface():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("PfDeleteInterface", windll["IPHLPAPI"]), ((1, 'pInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfAddFiltersToInterface():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(win32more.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head),UInt32,POINTER(win32more.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head),POINTER(c_void_p), use_last_error=False)(("PfAddFiltersToInterface", windll["IPHLPAPI"]), ((1, 'ih'),(1, 'cInFilters'),(1, 'pfiltIn'),(1, 'cOutFilters'),(1, 'pfiltOut'),(1, 'pfHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfRemoveFiltersFromInterface():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(win32more.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head),UInt32,POINTER(win32more.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head), use_last_error=False)(("PfRemoveFiltersFromInterface", windll["IPHLPAPI"]), ((1, 'ih'),(1, 'cInFilters'),(1, 'pfiltIn'),(1, 'cOutFilters'),(1, 'pfiltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfRemoveFilterHandles():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(c_void_p), use_last_error=False)(("PfRemoveFilterHandles", windll["IPHLPAPI"]), ((1, 'pInterface'),(1, 'cFilters'),(1, 'pvHandles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfUnBindInterface():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("PfUnBindInterface", windll["IPHLPAPI"]), ((1, 'pInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfBindInterfaceToIndex():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,win32more.NetworkManagement.IpHelper.PFADDRESSTYPE,c_char_p_no, use_last_error=False)(("PfBindInterfaceToIndex", windll["IPHLPAPI"]), ((1, 'pInterface'),(1, 'dwIndex'),(1, 'pfatLinkType'),(1, 'LinkIPAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfBindInterfaceToIPAddress():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.NetworkManagement.IpHelper.PFADDRESSTYPE,c_char_p_no, use_last_error=False)(("PfBindInterfaceToIPAddress", windll["IPHLPAPI"]), ((1, 'pInterface'),(1, 'pfatType'),(1, 'IPAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfRebindFilters():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.PF_LATEBIND_INFO_head), use_last_error=False)(("PfRebindFilters", windll["IPHLPAPI"]), ((1, 'pInterface'),(1, 'pLateBindInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfAddGlobalFilterToInterface():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.NetworkManagement.IpHelper.GLOBAL_FILTER, use_last_error=False)(("PfAddGlobalFilterToInterface", windll["IPHLPAPI"]), ((1, 'pInterface'),(1, 'gfFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfRemoveGlobalFilterFromInterface():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.NetworkManagement.IpHelper.GLOBAL_FILTER, use_last_error=False)(("PfRemoveGlobalFilterFromInterface", windll["IPHLPAPI"]), ((1, 'pInterface'),(1, 'gfFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfMakeLog():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("PfMakeLog", windll["IPHLPAPI"]), ((1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfSetLogBuffer():
    try:
        return WINFUNCTYPE(UInt32,c_char_p_no,UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("PfSetLogBuffer", windll["IPHLPAPI"]), ((1, 'pbBuffer'),(1, 'dwSize'),(1, 'dwThreshold'),(1, 'dwEntries'),(1, 'pdwLoggedEntries'),(1, 'pdwLostEntries'),(1, 'pdwSizeUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfDeleteLog():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("PfDeleteLog", windll["IPHLPAPI"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfGetInterfaceStatistics():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(win32more.NetworkManagement.IpHelper.PF_INTERFACE_STATS_head),POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(("PfGetInterfaceStatistics", windll["IPHLPAPI"]), ((1, 'pInterface'),(1, 'ppfStats'),(1, 'pdwBufferSize'),(1, 'fResetCounters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PfTestPacket():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,UInt32,c_char_p_no,POINTER(win32more.NetworkManagement.IpHelper.PFFORWARD_ACTION), use_last_error=False)(("PfTestPacket", windll["IPHLPAPI"]), ((1, 'pInInterface'),(1, 'pOutInterface'),(1, 'cBytes'),(1, 'pbPacket'),(1, 'ppAction'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "NET_IF_OPER_STATUS_DOWN_NOT_AUTHENTICATED",
    "NET_IF_OPER_STATUS_DOWN_NOT_MEDIA_CONNECTED",
    "NET_IF_OPER_STATUS_DORMANT_PAUSED",
    "NET_IF_OPER_STATUS_DORMANT_LOW_POWER",
    "NET_IF_OID_IF_ALIAS",
    "NET_IF_OID_COMPARTMENT_ID",
    "NET_IF_OID_NETWORK_GUID",
    "NET_IF_OID_IF_ENTRY",
    "NET_SITEID_UNSPECIFIED",
    "NET_SITEID_MAXUSER",
    "NET_SITEID_MAXSYSTEM",
    "NET_IFLUID_UNSPECIFIED",
    "NIIF_HARDWARE_INTERFACE",
    "NIIF_FILTER_INTERFACE",
    "NIIF_NDIS_RESERVED1",
    "NIIF_NDIS_RESERVED2",
    "NIIF_NDIS_RESERVED3",
    "NIIF_NDIS_WDM_INTERFACE",
    "NIIF_NDIS_ENDPOINT_INTERFACE",
    "NIIF_NDIS_ISCSI_INTERFACE",
    "NIIF_NDIS_RESERVED4",
    "IF_MAX_STRING_SIZE",
    "IF_MAX_PHYS_ADDRESS_LENGTH",
    "ANY_SIZE",
    "MAXLEN_PHYSADDR",
    "MAXLEN_IFDESCR",
    "MAX_INTERFACE_NAME_LEN",
    "MIN_IF_TYPE",
    "IF_TYPE_OTHER",
    "IF_TYPE_REGULAR_1822",
    "IF_TYPE_HDH_1822",
    "IF_TYPE_DDN_X25",
    "IF_TYPE_RFC877_X25",
    "IF_TYPE_ETHERNET_CSMACD",
    "IF_TYPE_IS088023_CSMACD",
    "IF_TYPE_ISO88024_TOKENBUS",
    "IF_TYPE_ISO88025_TOKENRING",
    "IF_TYPE_ISO88026_MAN",
    "IF_TYPE_STARLAN",
    "IF_TYPE_PROTEON_10MBIT",
    "IF_TYPE_PROTEON_80MBIT",
    "IF_TYPE_HYPERCHANNEL",
    "IF_TYPE_FDDI",
    "IF_TYPE_LAP_B",
    "IF_TYPE_SDLC",
    "IF_TYPE_DS1",
    "IF_TYPE_E1",
    "IF_TYPE_BASIC_ISDN",
    "IF_TYPE_PRIMARY_ISDN",
    "IF_TYPE_PROP_POINT2POINT_SERIAL",
    "IF_TYPE_PPP",
    "IF_TYPE_SOFTWARE_LOOPBACK",
    "IF_TYPE_EON",
    "IF_TYPE_ETHERNET_3MBIT",
    "IF_TYPE_NSIP",
    "IF_TYPE_SLIP",
    "IF_TYPE_ULTRA",
    "IF_TYPE_DS3",
    "IF_TYPE_SIP",
    "IF_TYPE_FRAMERELAY",
    "IF_TYPE_RS232",
    "IF_TYPE_PARA",
    "IF_TYPE_ARCNET",
    "IF_TYPE_ARCNET_PLUS",
    "IF_TYPE_ATM",
    "IF_TYPE_MIO_X25",
    "IF_TYPE_SONET",
    "IF_TYPE_X25_PLE",
    "IF_TYPE_ISO88022_LLC",
    "IF_TYPE_LOCALTALK",
    "IF_TYPE_SMDS_DXI",
    "IF_TYPE_FRAMERELAY_SERVICE",
    "IF_TYPE_V35",
    "IF_TYPE_HSSI",
    "IF_TYPE_HIPPI",
    "IF_TYPE_MODEM",
    "IF_TYPE_AAL5",
    "IF_TYPE_SONET_PATH",
    "IF_TYPE_SONET_VT",
    "IF_TYPE_SMDS_ICIP",
    "IF_TYPE_PROP_VIRTUAL",
    "IF_TYPE_PROP_MULTIPLEXOR",
    "IF_TYPE_IEEE80212",
    "IF_TYPE_FIBRECHANNEL",
    "IF_TYPE_HIPPIINTERFACE",
    "IF_TYPE_FRAMERELAY_INTERCONNECT",
    "IF_TYPE_AFLANE_8023",
    "IF_TYPE_AFLANE_8025",
    "IF_TYPE_CCTEMUL",
    "IF_TYPE_FASTETHER",
    "IF_TYPE_ISDN",
    "IF_TYPE_V11",
    "IF_TYPE_V36",
    "IF_TYPE_G703_64K",
    "IF_TYPE_G703_2MB",
    "IF_TYPE_QLLC",
    "IF_TYPE_FASTETHER_FX",
    "IF_TYPE_CHANNEL",
    "IF_TYPE_IEEE80211",
    "IF_TYPE_IBM370PARCHAN",
    "IF_TYPE_ESCON",
    "IF_TYPE_DLSW",
    "IF_TYPE_ISDN_S",
    "IF_TYPE_ISDN_U",
    "IF_TYPE_LAP_D",
    "IF_TYPE_IPSWITCH",
    "IF_TYPE_RSRB",
    "IF_TYPE_ATM_LOGICAL",
    "IF_TYPE_DS0",
    "IF_TYPE_DS0_BUNDLE",
    "IF_TYPE_BSC",
    "IF_TYPE_ASYNC",
    "IF_TYPE_CNR",
    "IF_TYPE_ISO88025R_DTR",
    "IF_TYPE_EPLRS",
    "IF_TYPE_ARAP",
    "IF_TYPE_PROP_CNLS",
    "IF_TYPE_HOSTPAD",
    "IF_TYPE_TERMPAD",
    "IF_TYPE_FRAMERELAY_MPI",
    "IF_TYPE_X213",
    "IF_TYPE_ADSL",
    "IF_TYPE_RADSL",
    "IF_TYPE_SDSL",
    "IF_TYPE_VDSL",
    "IF_TYPE_ISO88025_CRFPRINT",
    "IF_TYPE_MYRINET",
    "IF_TYPE_VOICE_EM",
    "IF_TYPE_VOICE_FXO",
    "IF_TYPE_VOICE_FXS",
    "IF_TYPE_VOICE_ENCAP",
    "IF_TYPE_VOICE_OVERIP",
    "IF_TYPE_ATM_DXI",
    "IF_TYPE_ATM_FUNI",
    "IF_TYPE_ATM_IMA",
    "IF_TYPE_PPPMULTILINKBUNDLE",
    "IF_TYPE_IPOVER_CDLC",
    "IF_TYPE_IPOVER_CLAW",
    "IF_TYPE_STACKTOSTACK",
    "IF_TYPE_VIRTUALIPADDRESS",
    "IF_TYPE_MPC",
    "IF_TYPE_IPOVER_ATM",
    "IF_TYPE_ISO88025_FIBER",
    "IF_TYPE_TDLC",
    "IF_TYPE_GIGABITETHERNET",
    "IF_TYPE_HDLC",
    "IF_TYPE_LAP_F",
    "IF_TYPE_V37",
    "IF_TYPE_X25_MLP",
    "IF_TYPE_X25_HUNTGROUP",
    "IF_TYPE_TRANSPHDLC",
    "IF_TYPE_INTERLEAVE",
    "IF_TYPE_FAST",
    "IF_TYPE_IP",
    "IF_TYPE_DOCSCABLE_MACLAYER",
    "IF_TYPE_DOCSCABLE_DOWNSTREAM",
    "IF_TYPE_DOCSCABLE_UPSTREAM",
    "IF_TYPE_A12MPPSWITCH",
    "IF_TYPE_TUNNEL",
    "IF_TYPE_COFFEE",
    "IF_TYPE_CES",
    "IF_TYPE_ATM_SUBINTERFACE",
    "IF_TYPE_L2_VLAN",
    "IF_TYPE_L3_IPVLAN",
    "IF_TYPE_L3_IPXVLAN",
    "IF_TYPE_DIGITALPOWERLINE",
    "IF_TYPE_MEDIAMAILOVERIP",
    "IF_TYPE_DTM",
    "IF_TYPE_DCN",
    "IF_TYPE_IPFORWARD",
    "IF_TYPE_MSDSL",
    "IF_TYPE_IEEE1394",
    "IF_TYPE_IF_GSN",
    "IF_TYPE_DVBRCC_MACLAYER",
    "IF_TYPE_DVBRCC_DOWNSTREAM",
    "IF_TYPE_DVBRCC_UPSTREAM",
    "IF_TYPE_ATM_VIRTUAL",
    "IF_TYPE_MPLS_TUNNEL",
    "IF_TYPE_SRP",
    "IF_TYPE_VOICEOVERATM",
    "IF_TYPE_VOICEOVERFRAMERELAY",
    "IF_TYPE_IDSL",
    "IF_TYPE_COMPOSITELINK",
    "IF_TYPE_SS7_SIGLINK",
    "IF_TYPE_PROP_WIRELESS_P2P",
    "IF_TYPE_FR_FORWARD",
    "IF_TYPE_RFC1483",
    "IF_TYPE_USB",
    "IF_TYPE_IEEE8023AD_LAG",
    "IF_TYPE_BGP_POLICY_ACCOUNTING",
    "IF_TYPE_FRF16_MFR_BUNDLE",
    "IF_TYPE_H323_GATEKEEPER",
    "IF_TYPE_H323_PROXY",
    "IF_TYPE_MPLS",
    "IF_TYPE_MF_SIGLINK",
    "IF_TYPE_HDSL2",
    "IF_TYPE_SHDSL",
    "IF_TYPE_DS1_FDL",
    "IF_TYPE_POS",
    "IF_TYPE_DVB_ASI_IN",
    "IF_TYPE_DVB_ASI_OUT",
    "IF_TYPE_PLC",
    "IF_TYPE_NFAS",
    "IF_TYPE_TR008",
    "IF_TYPE_GR303_RDT",
    "IF_TYPE_GR303_IDT",
    "IF_TYPE_ISUP",
    "IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER",
    "IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM",
    "IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM",
    "IF_TYPE_HIPERLAN2",
    "IF_TYPE_PROP_BWA_P2MP",
    "IF_TYPE_SONET_OVERHEAD_CHANNEL",
    "IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL",
    "IF_TYPE_AAL2",
    "IF_TYPE_RADIO_MAC",
    "IF_TYPE_ATM_RADIO",
    "IF_TYPE_IMT",
    "IF_TYPE_MVL",
    "IF_TYPE_REACH_DSL",
    "IF_TYPE_FR_DLCI_ENDPT",
    "IF_TYPE_ATM_VCI_ENDPT",
    "IF_TYPE_OPTICAL_CHANNEL",
    "IF_TYPE_OPTICAL_TRANSPORT",
    "IF_TYPE_IEEE80216_WMAN",
    "IF_TYPE_WWANPP",
    "IF_TYPE_WWANPP2",
    "IF_TYPE_IEEE802154",
    "IF_TYPE_XBOX_WIRELESS",
    "MAX_IF_TYPE",
    "IF_CHECK_NONE",
    "IF_CHECK_MCAST",
    "IF_CHECK_SEND",
    "IF_CONNECTION_DEDICATED",
    "IF_CONNECTION_PASSIVE",
    "IF_CONNECTION_DEMAND",
    "IF_ADMIN_STATUS_UP",
    "IF_ADMIN_STATUS_DOWN",
    "IF_ADMIN_STATUS_TESTING",
    "MIB_IF_TYPE_OTHER",
    "MIB_IF_TYPE_ETHERNET",
    "MIB_IF_TYPE_TOKENRING",
    "MIB_IF_TYPE_FDDI",
    "MIB_IF_TYPE_PPP",
    "MIB_IF_TYPE_LOOPBACK",
    "MIB_IF_TYPE_SLIP",
    "MIB_IF_ADMIN_STATUS_UP",
    "MIB_IF_ADMIN_STATUS_DOWN",
    "MIB_IF_ADMIN_STATUS_TESTING",
    "MIB_IPADDR_PRIMARY",
    "MIB_IPADDR_DYNAMIC",
    "MIB_IPADDR_DISCONNECTED",
    "MIB_IPADDR_DELETED",
    "MIB_IPADDR_TRANSIENT",
    "MIB_IPADDR_DNS_ELIGIBLE",
    "MIB_IPROUTE_METRIC_UNUSED",
    "MIB_USE_CURRENT_TTL",
    "MIB_USE_CURRENT_FORWARDING",
    "ICMP6_INFOMSG_MASK",
    "IPRTRMGR_PID",
    "IF_NUMBER",
    "IF_TABLE",
    "IF_ROW",
    "IP_STATS",
    "IP_ADDRTABLE",
    "IP_ADDRROW",
    "IP_FORWARDNUMBER",
    "IP_FORWARDTABLE",
    "IP_FORWARDROW",
    "IP_NETTABLE",
    "IP_NETROW",
    "ICMP_STATS",
    "TCP_STATS",
    "TCP_TABLE",
    "TCP_ROW",
    "UDP_STATS",
    "UDP_TABLE",
    "UDP_ROW",
    "MCAST_MFE",
    "MCAST_MFE_STATS",
    "BEST_IF",
    "BEST_ROUTE",
    "PROXY_ARP",
    "MCAST_IF_ENTRY",
    "MCAST_GLOBAL",
    "IF_STATUS",
    "MCAST_BOUNDARY",
    "MCAST_SCOPE",
    "DEST_MATCHING",
    "DEST_LONGER",
    "DEST_SHORTER",
    "ROUTE_MATCHING",
    "ROUTE_LONGER",
    "ROUTE_SHORTER",
    "ROUTE_STATE",
    "MCAST_MFE_STATS_EX",
    "IP6_STATS",
    "UDP6_STATS",
    "TCP6_STATS",
    "NUMBER_OF_EXPORTED_VARIABLES",
    "MAX_SCOPE_NAME_LEN",
    "MAX_MIB_OFFSET",
    "MIB_INVALID_TEREDO_PORT_NUMBER",
    "DNS_SETTINGS_VERSION1",
    "DNS_SETTINGS_VERSION2",
    "DNS_INTERFACE_SETTINGS_VERSION1",
    "DNS_INTERFACE_SETTINGS_VERSION2",
    "DNS_INTERFACE_SETTINGS_VERSION3",
    "DNS_SETTING_IPV6",
    "DNS_SETTING_NAMESERVER",
    "DNS_SETTING_SEARCHLIST",
    "DNS_SETTING_REGISTRATION_ENABLED",
    "DNS_SETTING_REGISTER_ADAPTER_NAME",
    "DNS_SETTING_DOMAIN",
    "DNS_SETTING_HOSTNAME",
    "DNS_SETTINGS_ENABLE_LLMNR",
    "DNS_SETTINGS_QUERY_ADAPTER_NAME",
    "DNS_SETTING_PROFILE_NAMESERVER",
    "DNS_SETTING_DISABLE_UNCONSTRAINED_QUERIES",
    "DNS_SETTING_SUPPLEMENTAL_SEARCH_LIST",
    "DNS_SETTING_DOH",
    "DNS_SETTING_DOH_PROFILE",
    "DNS_ENABLE_DOH",
    "DNS_DOH_POLICY_NOT_CONFIGURED",
    "DNS_DOH_POLICY_DISABLE",
    "DNS_DOH_POLICY_AUTO",
    "DNS_DOH_POLICY_REQUIRED",
    "DNS_SERVER_PROPERTY_VERSION1",
    "DNS_DOH_SERVER_SETTINGS_ENABLE_AUTO",
    "DNS_DOH_SERVER_SETTINGS_ENABLE",
    "DNS_DOH_SERVER_SETTINGS_FALLBACK_TO_UDP",
    "DNS_DOH_AUTO_UPGRADE_SERVER",
    "TCPIP_OWNING_MODULE_SIZE",
    "FD_FLAGS_NOSYN",
    "FD_FLAGS_ALLFLAGS",
    "LB_SRC_ADDR_USE_SRCADDR_FLAG",
    "LB_SRC_ADDR_USE_DSTADDR_FLAG",
    "LB_DST_ADDR_USE_SRCADDR_FLAG",
    "LB_DST_ADDR_USE_DSTADDR_FLAG",
    "LB_SRC_MASK_LATE_FLAG",
    "LB_DST_MASK_LATE_FLAG",
    "ERROR_BASE",
    "PFERROR_NO_PF_INTERFACE",
    "PFERROR_NO_FILTERS_GIVEN",
    "PFERROR_BUFFER_TOO_SMALL",
    "ERROR_IPV6_NOT_IMPLEMENTED",
    "IP_EXPORT_INCLUDED",
    "MAX_ADAPTER_NAME",
    "IP_STATUS_BASE",
    "IP_SUCCESS",
    "IP_BUF_TOO_SMALL",
    "IP_DEST_NET_UNREACHABLE",
    "IP_DEST_HOST_UNREACHABLE",
    "IP_DEST_PROT_UNREACHABLE",
    "IP_DEST_PORT_UNREACHABLE",
    "IP_NO_RESOURCES",
    "IP_BAD_OPTION",
    "IP_HW_ERROR",
    "IP_PACKET_TOO_BIG",
    "IP_REQ_TIMED_OUT",
    "IP_BAD_REQ",
    "IP_BAD_ROUTE",
    "IP_TTL_EXPIRED_TRANSIT",
    "IP_TTL_EXPIRED_REASSEM",
    "IP_PARAM_PROBLEM",
    "IP_SOURCE_QUENCH",
    "IP_OPTION_TOO_BIG",
    "IP_BAD_DESTINATION",
    "IP_DEST_NO_ROUTE",
    "IP_DEST_ADDR_UNREACHABLE",
    "IP_DEST_PROHIBITED",
    "IP_HOP_LIMIT_EXCEEDED",
    "IP_REASSEMBLY_TIME_EXCEEDED",
    "IP_PARAMETER_PROBLEM",
    "IP_DEST_UNREACHABLE",
    "IP_TIME_EXCEEDED",
    "IP_BAD_HEADER",
    "IP_UNRECOGNIZED_NEXT_HEADER",
    "IP_ICMP_ERROR",
    "IP_DEST_SCOPE_MISMATCH",
    "IP_ADDR_DELETED",
    "IP_SPEC_MTU_CHANGE",
    "IP_MTU_CHANGE",
    "IP_UNLOAD",
    "IP_ADDR_ADDED",
    "IP_MEDIA_CONNECT",
    "IP_MEDIA_DISCONNECT",
    "IP_BIND_ADAPTER",
    "IP_UNBIND_ADAPTER",
    "IP_DEVICE_DOES_NOT_EXIST",
    "IP_DUPLICATE_ADDRESS",
    "IP_INTERFACE_METRIC_CHANGE",
    "IP_RECONFIG_SECFLTR",
    "IP_NEGOTIATING_IPSEC",
    "IP_INTERFACE_WOL_CAPABILITY_CHANGE",
    "IP_DUPLICATE_IPADD",
    "IP_GENERAL_FAILURE",
    "MAX_IP_STATUS",
    "IP_PENDING",
    "IP_FLAG_REVERSE",
    "IP_FLAG_DF",
    "MAX_OPT_SIZE",
    "IOCTL_IP_RTCHANGE_NOTIFY_REQUEST",
    "IOCTL_IP_ADDCHANGE_NOTIFY_REQUEST",
    "IOCTL_ARP_SEND_REQUEST",
    "IOCTL_IP_INTERFACE_INFO",
    "IOCTL_IP_GET_BEST_INTERFACE",
    "IOCTL_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS",
    "NET_STRING_IPV4_ADDRESS",
    "NET_STRING_IPV4_SERVICE",
    "NET_STRING_IPV4_NETWORK",
    "NET_STRING_IPV6_ADDRESS",
    "NET_STRING_IPV6_ADDRESS_NO_SCOPE",
    "NET_STRING_IPV6_SERVICE",
    "NET_STRING_IPV6_SERVICE_NO_SCOPE",
    "NET_STRING_IPV6_NETWORK",
    "NET_STRING_NAMED_ADDRESS",
    "NET_STRING_NAMED_SERVICE",
    "MAX_ADAPTER_DESCRIPTION_LENGTH",
    "MAX_ADAPTER_NAME_LENGTH",
    "MAX_ADAPTER_ADDRESS_LENGTH",
    "DEFAULT_MINIMUM_ENTITIES",
    "MAX_HOSTNAME_LEN",
    "MAX_DOMAIN_NAME_LEN",
    "MAX_SCOPE_ID_LEN",
    "MAX_DHCPV6_DUID_LENGTH",
    "MAX_DNS_SUFFIX_STRING_LENGTH",
    "BROADCAST_NODETYPE",
    "PEER_TO_PEER_NODETYPE",
    "MIXED_NODETYPE",
    "HYBRID_NODETYPE",
    "IP_ADAPTER_ADDRESS_DNS_ELIGIBLE",
    "IP_ADAPTER_ADDRESS_TRANSIENT",
    "IP_ADAPTER_DDNS_ENABLED",
    "IP_ADAPTER_REGISTER_ADAPTER_SUFFIX",
    "IP_ADAPTER_DHCP_ENABLED",
    "IP_ADAPTER_RECEIVE_ONLY",
    "IP_ADAPTER_NO_MULTICAST",
    "IP_ADAPTER_IPV6_OTHER_STATEFUL_CONFIG",
    "IP_ADAPTER_NETBIOS_OVER_TCPIP_ENABLED",
    "IP_ADAPTER_IPV4_ENABLED",
    "IP_ADAPTER_IPV6_ENABLED",
    "IP_ADAPTER_IPV6_MANAGE_ADDRESS_CONFIG",
    "GAA_FLAG_SKIP_DNS_INFO",
    "IP_ROUTER_MANAGER_VERSION",
    "IP_GENERAL_INFO_BASE",
    "IP_IN_FILTER_INFO",
    "IP_OUT_FILTER_INFO",
    "IP_GLOBAL_INFO",
    "IP_INTERFACE_STATUS_INFO",
    "IP_ROUTE_INFO",
    "IP_PROT_PRIORITY_INFO",
    "IP_ROUTER_DISC_INFO",
    "IP_DEMAND_DIAL_FILTER_INFO",
    "IP_MCAST_HEARBEAT_INFO",
    "IP_MCAST_BOUNDARY_INFO",
    "IP_IPINIP_CFG_INFO",
    "IP_IFFILTER_INFO",
    "IP_MCAST_LIMIT_INFO",
    "IPV6_GLOBAL_INFO",
    "IPV6_ROUTE_INFO",
    "IP_IN_FILTER_INFO_V6",
    "IP_OUT_FILTER_INFO_V6",
    "IP_DEMAND_DIAL_FILTER_INFO_V6",
    "IP_IFFILTER_INFO_V6",
    "IP_FILTER_ENABLE_INFO",
    "IP_FILTER_ENABLE_INFO_V6",
    "IP_PROT_PRIORITY_INFO_EX",
    "ADDRESS_FAMILY",
    "AF_INET",
    "AF_INET6",
    "AF_UNSPEC",
    "GET_ADAPTERS_ADDRESSES_FLAGS",
    "GAA_FLAG_SKIP_UNICAST",
    "GAA_FLAG_SKIP_ANYCAST",
    "GAA_FLAG_SKIP_MULTICAST",
    "GAA_FLAG_SKIP_DNS_SERVER",
    "GAA_FLAG_INCLUDE_PREFIX",
    "GAA_FLAG_SKIP_FRIENDLY_NAME",
    "GAA_FLAG_INCLUDE_WINS_INFO",
    "GAA_FLAG_INCLUDE_GATEWAYS",
    "GAA_FLAG_INCLUDE_ALL_INTERFACES",
    "GAA_FLAG_INCLUDE_ALL_COMPARTMENTS",
    "GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER",
    "IcmpHandle",
    "HIFTIMESTAMPCHANGE",
    "ip_option_information",
    "ip_option_information32",
    "icmp_echo_reply",
    "icmp_echo_reply32",
    "IPV6_ADDRESS_EX",
    "icmpv6_echo_reply_lh",
    "arp_send_reply",
    "tcp_reserve_port_range",
    "IP_ADAPTER_INDEX_MAP",
    "IP_INTERFACE_INFO",
    "IP_UNIDIRECTIONAL_ADAPTER_ADDRESS",
    "IP_ADAPTER_ORDER_MAP",
    "IP_MCAST_COUNTER_INFO",
    "IF_ACCESS_TYPE",
    "IF_ACCESS_LOOPBACK",
    "IF_ACCESS_BROADCAST",
    "IF_ACCESS_POINT_TO_POINT",
    "IF_ACCESS_POINTTOPOINT",
    "IF_ACCESS_POINT_TO_MULTI_POINT",
    "IF_ACCESS_POINTTOMULTIPOINT",
    "INTERNAL_IF_OPER_STATUS",
    "IF_OPER_STATUS_NON_OPERATIONAL",
    "IF_OPER_STATUS_UNREACHABLE",
    "IF_OPER_STATUS_DISCONNECTED",
    "IF_OPER_STATUS_CONNECTING",
    "IF_OPER_STATUS_CONNECTED",
    "IF_OPER_STATUS_OPERATIONAL",
    "NET_IF_OPER_STATUS",
    "NET_IF_OPER_STATUS_UP",
    "NET_IF_OPER_STATUS_DOWN",
    "NET_IF_OPER_STATUS_TESTING",
    "NET_IF_OPER_STATUS_UNKNOWN",
    "NET_IF_OPER_STATUS_DORMANT",
    "NET_IF_OPER_STATUS_NOT_PRESENT",
    "NET_IF_OPER_STATUS_LOWER_LAYER_DOWN",
    "NET_IF_ADMIN_STATUS",
    "NET_IF_ADMIN_STATUS_UP",
    "NET_IF_ADMIN_STATUS_DOWN",
    "NET_IF_ADMIN_STATUS_TESTING",
    "NET_IF_RCV_ADDRESS_TYPE",
    "NET_IF_RCV_ADDRESS_TYPE_OTHER",
    "NET_IF_RCV_ADDRESS_TYPE_VOLATILE",
    "NET_IF_RCV_ADDRESS_TYPE_NON_VOLATILE",
    "NET_IF_RCV_ADDRESS_LH",
    "NET_IF_ALIAS_LH",
    "NET_LUID_LH",
    "NET_IF_CONNECTION_TYPE",
    "NET_IF_CONNECTION_DEDICATED",
    "NET_IF_CONNECTION_PASSIVE",
    "NET_IF_CONNECTION_DEMAND",
    "NET_IF_CONNECTION_MAXIMUM",
    "TUNNEL_TYPE",
    "TUNNEL_TYPE_NONE",
    "TUNNEL_TYPE_OTHER",
    "TUNNEL_TYPE_DIRECT",
    "TUNNEL_TYPE_6TO4",
    "TUNNEL_TYPE_ISATAP",
    "TUNNEL_TYPE_TEREDO",
    "TUNNEL_TYPE_IPHTTPS",
    "NET_IF_ACCESS_TYPE",
    "NET_IF_ACCESS_LOOPBACK",
    "NET_IF_ACCESS_BROADCAST",
    "NET_IF_ACCESS_POINT_TO_POINT",
    "NET_IF_ACCESS_POINT_TO_MULTI_POINT",
    "NET_IF_ACCESS_MAXIMUM",
    "NET_IF_DIRECTION_TYPE",
    "NET_IF_DIRECTION_SENDRECEIVE",
    "NET_IF_DIRECTION_SENDONLY",
    "NET_IF_DIRECTION_RECEIVEONLY",
    "NET_IF_DIRECTION_MAXIMUM",
    "NET_IF_MEDIA_CONNECT_STATE",
    "NET_IF_MEDIA_CONNECT_STATE_MediaConnectStateUnknown",
    "NET_IF_MEDIA_CONNECT_STATE_MediaConnectStateConnected",
    "NET_IF_MEDIA_CONNECT_STATE_MediaConnectStateDisconnected",
    "NET_IF_MEDIA_DUPLEX_STATE",
    "NET_IF_MEDIA_DUPLEX_STATE_MediaDuplexStateUnknown",
    "NET_IF_MEDIA_DUPLEX_STATE_MediaDuplexStateHalf",
    "NET_IF_MEDIA_DUPLEX_STATE_MediaDuplexStateFull",
    "NET_PHYSICAL_LOCATION_LH",
    "IF_COUNTED_STRING_LH",
    "IF_PHYSICAL_ADDRESS_LH",
    "IF_ADMINISTRATIVE_STATE",
    "IF_ADMINISTRATIVE_DISABLED",
    "IF_ADMINISTRATIVE_ENABLED",
    "IF_ADMINISTRATIVE_DEMANDDIAL",
    "IF_OPER_STATUS",
    "IF_OPER_STATUS_IfOperStatusUp",
    "IF_OPER_STATUS_IfOperStatusDown",
    "IF_OPER_STATUS_IfOperStatusTesting",
    "IF_OPER_STATUS_IfOperStatusUnknown",
    "IF_OPER_STATUS_IfOperStatusDormant",
    "IF_OPER_STATUS_IfOperStatusNotPresent",
    "IF_OPER_STATUS_IfOperStatusLowerLayerDown",
    "NDIS_INTERFACE_INFORMATION",
    "MIB_NOTIFICATION_TYPE",
    "MIB_NOTIFICATION_TYPE_MibParameterNotification",
    "MIB_NOTIFICATION_TYPE_MibAddInstance",
    "MIB_NOTIFICATION_TYPE_MibDeleteInstance",
    "MIB_NOTIFICATION_TYPE_MibInitialNotification",
    "MIB_IF_ROW2",
    "MIB_IF_TABLE2",
    "MIB_IF_ENTRY_LEVEL",
    "MIB_IF_ENTRY_LEVEL_MibIfEntryNormal",
    "MIB_IF_ENTRY_LEVEL_MibIfEntryNormalWithoutStatistics",
    "MIB_IF_TABLE_LEVEL",
    "MIB_IF_TABLE_LEVEL_MibIfTableNormal",
    "MIB_IF_TABLE_LEVEL_MibIfTableRaw",
    "MIB_IF_TABLE_LEVEL_MibIfTableNormalWithoutStatistics",
    "MIB_IPINTERFACE_ROW",
    "MIB_IPINTERFACE_TABLE",
    "MIB_IFSTACK_ROW",
    "MIB_INVERTEDIFSTACK_ROW",
    "MIB_IFSTACK_TABLE",
    "MIB_INVERTEDIFSTACK_TABLE",
    "PIPINTERFACE_CHANGE_CALLBACK",
    "MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES",
    "MIB_UNICASTIPADDRESS_ROW",
    "MIB_UNICASTIPADDRESS_TABLE",
    "PUNICAST_IPADDRESS_CHANGE_CALLBACK",
    "PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK",
    "MIB_ANYCASTIPADDRESS_ROW",
    "MIB_ANYCASTIPADDRESS_TABLE",
    "MIB_MULTICASTIPADDRESS_ROW",
    "MIB_MULTICASTIPADDRESS_TABLE",
    "IP_ADDRESS_PREFIX",
    "MIB_IPFORWARD_ROW2",
    "MIB_IPFORWARD_TABLE2",
    "PIPFORWARD_CHANGE_CALLBACK",
    "MIB_IPPATH_ROW",
    "MIB_IPPATH_TABLE",
    "MIB_IPNET_ROW2",
    "MIB_IPNET_TABLE2",
    "PTEREDO_PORT_CHANGE_CALLBACK",
    "DNS_SETTINGS",
    "DNS_SETTINGS2",
    "DNS_DOH_SERVER_SETTINGS",
    "DNS_SERVER_PROPERTY_TYPE",
    "DNS_SERVER_PROPERTY_TYPE_DnsServerInvalidProperty",
    "DNS_SERVER_PROPERTY_TYPE_DnsServerDohProperty",
    "DNS_SERVER_PROPERTY_TYPES",
    "DNS_SERVER_PROPERTY",
    "DNS_INTERFACE_SETTINGS",
    "DNS_INTERFACE_SETTINGS_EX",
    "DNS_INTERFACE_SETTINGS3",
    "PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK",
    "MIB_OPAQUE_QUERY",
    "MIB_IFNUMBER",
    "MIB_IFROW",
    "MIB_IFTABLE",
    "MIB_IPADDRROW_XP",
    "MIB_IPADDRROW_W2K",
    "MIB_IPADDRTABLE",
    "MIB_IPFORWARDNUMBER",
    "MIB_IPFORWARD_TYPE",
    "MIB_IPROUTE_TYPE_OTHER",
    "MIB_IPROUTE_TYPE_INVALID",
    "MIB_IPROUTE_TYPE_DIRECT",
    "MIB_IPROUTE_TYPE_INDIRECT",
    "MIB_IPFORWARDROW",
    "MIB_IPFORWARDTABLE",
    "MIB_IPNET_TYPE",
    "MIB_IPNET_TYPE_OTHER",
    "MIB_IPNET_TYPE_INVALID",
    "MIB_IPNET_TYPE_DYNAMIC",
    "MIB_IPNET_TYPE_STATIC",
    "MIB_IPNETROW_LH",
    "MIB_IPNETROW_W2K",
    "MIB_IPNETTABLE",
    "MIB_IPSTATS_FORWARDING",
    "MIB_IP_FORWARDING",
    "MIB_IP_NOT_FORWARDING",
    "MIB_IPSTATS_LH",
    "MIB_IPSTATS_W2K",
    "MIBICMPSTATS",
    "MIBICMPINFO",
    "MIB_ICMP",
    "MIBICMPSTATS_EX_XPSP1",
    "MIB_ICMP_EX_XPSP1",
    "ICMP6_TYPE",
    "ICMP6_DST_UNREACH",
    "ICMP6_PACKET_TOO_BIG",
    "ICMP6_TIME_EXCEEDED",
    "ICMP6_PARAM_PROB",
    "ICMP6_ECHO_REQUEST",
    "ICMP6_ECHO_REPLY",
    "ICMP6_MEMBERSHIP_QUERY",
    "ICMP6_MEMBERSHIP_REPORT",
    "ICMP6_MEMBERSHIP_REDUCTION",
    "ND_ROUTER_SOLICIT",
    "ND_ROUTER_ADVERT",
    "ND_NEIGHBOR_SOLICIT",
    "ND_NEIGHBOR_ADVERT",
    "ND_REDIRECT",
    "ICMP6_V2_MEMBERSHIP_REPORT",
    "ICMP4_TYPE",
    "ICMP4_ECHO_REPLY",
    "ICMP4_DST_UNREACH",
    "ICMP4_SOURCE_QUENCH",
    "ICMP4_REDIRECT",
    "ICMP4_ECHO_REQUEST",
    "ICMP4_ROUTER_ADVERT",
    "ICMP4_ROUTER_SOLICIT",
    "ICMP4_TIME_EXCEEDED",
    "ICMP4_PARAM_PROB",
    "ICMP4_TIMESTAMP_REQUEST",
    "ICMP4_TIMESTAMP_REPLY",
    "ICMP4_MASK_REQUEST",
    "ICMP4_MASK_REPLY",
    "MIB_IPMCAST_OIF_XP",
    "MIB_IPMCAST_OIF_W2K",
    "MIB_IPMCAST_MFE",
    "MIB_MFE_TABLE",
    "MIB_IPMCAST_OIF_STATS_LH",
    "MIB_IPMCAST_OIF_STATS_W2K",
    "MIB_IPMCAST_MFE_STATS",
    "MIB_MFE_STATS_TABLE",
    "MIB_IPMCAST_MFE_STATS_EX_XP",
    "MIB_MFE_STATS_TABLE_EX_XP",
    "MIB_IPMCAST_GLOBAL",
    "MIB_IPMCAST_IF_ENTRY",
    "MIB_IPMCAST_IF_TABLE",
    "MIB_TCP_STATE",
    "MIB_TCP_STATE_CLOSED",
    "MIB_TCP_STATE_LISTEN",
    "MIB_TCP_STATE_SYN_SENT",
    "MIB_TCP_STATE_SYN_RCVD",
    "MIB_TCP_STATE_ESTAB",
    "MIB_TCP_STATE_FIN_WAIT1",
    "MIB_TCP_STATE_FIN_WAIT2",
    "MIB_TCP_STATE_CLOSE_WAIT",
    "MIB_TCP_STATE_CLOSING",
    "MIB_TCP_STATE_LAST_ACK",
    "MIB_TCP_STATE_TIME_WAIT",
    "MIB_TCP_STATE_DELETE_TCB",
    "MIB_TCP_STATE_RESERVED",
    "TCP_CONNECTION_OFFLOAD_STATE",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateInHost",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloading",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloaded",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateUploading",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateMax",
    "MIB_TCPROW_LH",
    "MIB_TCPROW_W2K",
    "MIB_TCPTABLE",
    "MIB_TCPROW2",
    "MIB_TCPTABLE2",
    "MIB_TCPROW_OWNER_PID",
    "MIB_TCPTABLE_OWNER_PID",
    "MIB_TCPROW_OWNER_MODULE",
    "MIB_TCPTABLE_OWNER_MODULE",
    "MIB_TCP6ROW",
    "MIB_TCP6TABLE",
    "MIB_TCP6ROW2",
    "MIB_TCP6TABLE2",
    "MIB_TCP6ROW_OWNER_PID",
    "MIB_TCP6TABLE_OWNER_PID",
    "MIB_TCP6ROW_OWNER_MODULE",
    "MIB_TCP6TABLE_OWNER_MODULE",
    "TCP_RTO_ALGORITHM",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmOther",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmConstant",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmRsre",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmVanj",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_OTHER",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_CONSTANT",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_RSRE",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_VANJ",
    "MIB_TCPSTATS_LH",
    "MIB_TCPSTATS_W2K",
    "MIB_TCPSTATS2",
    "MIB_UDPROW",
    "MIB_UDPTABLE",
    "MIB_UDPROW_OWNER_PID",
    "MIB_UDPTABLE_OWNER_PID",
    "MIB_UDPROW_OWNER_MODULE",
    "MIB_UDPTABLE_OWNER_MODULE",
    "MIB_UDPROW2",
    "MIB_UDPTABLE2",
    "MIB_UDP6ROW",
    "MIB_UDP6TABLE",
    "MIB_UDP6ROW_OWNER_PID",
    "MIB_UDP6TABLE_OWNER_PID",
    "MIB_UDP6ROW_OWNER_MODULE",
    "MIB_UDP6TABLE_OWNER_MODULE",
    "MIB_UDP6ROW2",
    "MIB_UDP6TABLE2",
    "MIB_UDPSTATS",
    "MIB_UDPSTATS2",
    "TCP_TABLE_CLASS",
    "TCP_TABLE_BASIC_LISTENER",
    "TCP_TABLE_BASIC_CONNECTIONS",
    "TCP_TABLE_BASIC_ALL",
    "TCP_TABLE_OWNER_PID_LISTENER",
    "TCP_TABLE_OWNER_PID_CONNECTIONS",
    "TCP_TABLE_OWNER_PID_ALL",
    "TCP_TABLE_OWNER_MODULE_LISTENER",
    "TCP_TABLE_OWNER_MODULE_CONNECTIONS",
    "TCP_TABLE_OWNER_MODULE_ALL",
    "UDP_TABLE_CLASS",
    "UDP_TABLE_BASIC",
    "UDP_TABLE_OWNER_PID",
    "UDP_TABLE_OWNER_MODULE",
    "TCPIP_OWNER_MODULE_INFO_CLASS",
    "TCPIP_OWNER_MODULE_INFO_BASIC",
    "TCPIP_OWNER_MODULE_BASIC_INFO",
    "MIB_IPMCAST_BOUNDARY",
    "MIB_IPMCAST_BOUNDARY_TABLE",
    "MIB_BOUNDARYROW",
    "MIB_MCAST_LIMIT_ROW",
    "MIB_IPMCAST_SCOPE",
    "MIB_IPDESTROW",
    "MIB_IPDESTTABLE",
    "MIB_BEST_IF",
    "MIB_PROXYARP",
    "MIB_IFSTATUS",
    "MIB_ROUTESTATE",
    "MIB_OPAQUE_INFO",
    "IP_ADDRESS_STRING",
    "IP_ADDR_STRING",
    "IP_ADAPTER_INFO",
    "IP_ADAPTER_UNICAST_ADDRESS_LH",
    "IP_ADAPTER_UNICAST_ADDRESS_XP",
    "IP_ADAPTER_ANYCAST_ADDRESS_XP",
    "IP_ADAPTER_MULTICAST_ADDRESS_XP",
    "IP_ADAPTER_DNS_SERVER_ADDRESS_XP",
    "IP_ADAPTER_WINS_SERVER_ADDRESS_LH",
    "IP_ADAPTER_GATEWAY_ADDRESS_LH",
    "IP_ADAPTER_PREFIX_XP",
    "IP_ADAPTER_DNS_SUFFIX",
    "IP_ADAPTER_ADDRESSES_LH",
    "IP_ADAPTER_ADDRESSES_XP",
    "IP_PER_ADAPTER_INFO_W2KSP1",
    "FIXED_INFO_W2KSP1",
    "ip_interface_name_info_w2ksp1",
    "TCP_ESTATS_TYPE",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsSynOpts",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsData",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsSndCong",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsPath",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsSendBuff",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsRec",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsObsRec",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsBandwidth",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsFineRtt",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsMaximum",
    "TCP_BOOLEAN_OPTIONAL",
    "TCP_BOOLEAN_OPTIONAL_TcpBoolOptDisabled",
    "TCP_BOOLEAN_OPTIONAL_TcpBoolOptEnabled",
    "TCP_BOOLEAN_OPTIONAL_TcpBoolOptUnchanged",
    "TCP_ESTATS_SYN_OPTS_ROS_v0",
    "TCP_SOFT_ERROR",
    "TCP_SOFT_ERROR_TcpErrorNone",
    "TCP_SOFT_ERROR_TcpErrorBelowDataWindow",
    "TCP_SOFT_ERROR_TcpErrorAboveDataWindow",
    "TCP_SOFT_ERROR_TcpErrorBelowAckWindow",
    "TCP_SOFT_ERROR_TcpErrorAboveAckWindow",
    "TCP_SOFT_ERROR_TcpErrorBelowTsWindow",
    "TCP_SOFT_ERROR_TcpErrorAboveTsWindow",
    "TCP_SOFT_ERROR_TcpErrorDataChecksumError",
    "TCP_SOFT_ERROR_TcpErrorDataLengthError",
    "TCP_SOFT_ERROR_TcpErrorMaxSoftError",
    "TCP_ESTATS_DATA_ROD_v0",
    "TCP_ESTATS_DATA_RW_v0",
    "TCP_ESTATS_SND_CONG_ROD_v0",
    "TCP_ESTATS_SND_CONG_ROS_v0",
    "TCP_ESTATS_SND_CONG_RW_v0",
    "TCP_ESTATS_PATH_ROD_v0",
    "TCP_ESTATS_PATH_RW_v0",
    "TCP_ESTATS_SEND_BUFF_ROD_v0",
    "TCP_ESTATS_SEND_BUFF_RW_v0",
    "TCP_ESTATS_REC_ROD_v0",
    "TCP_ESTATS_REC_RW_v0",
    "TCP_ESTATS_OBS_REC_ROD_v0",
    "TCP_ESTATS_OBS_REC_RW_v0",
    "TCP_ESTATS_BANDWIDTH_RW_v0",
    "TCP_ESTATS_BANDWIDTH_ROD_v0",
    "TCP_ESTATS_FINE_RTT_RW_v0",
    "TCP_ESTATS_FINE_RTT_ROD_v0",
    "INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES",
    "INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES",
    "INTERFACE_TIMESTAMP_CAPABILITIES",
    "INTERFACE_HARDWARE_CROSSTIMESTAMP",
    "PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK",
    "NET_ADDRESS_FORMAT",
    "NET_ADDRESS_FORMAT_UNSPECIFIED",
    "NET_ADDRESS_DNS_NAME",
    "NET_ADDRESS_IPV4",
    "NET_ADDRESS_IPV6",
    "GLOBAL_FILTER",
    "GF_FRAGMENTS",
    "GF_STRONGHOST",
    "GF_FRAGCACHE",
    "PFFORWARD_ACTION",
    "PF_ACTION_FORWARD",
    "PF_ACTION_DROP",
    "PFADDRESSTYPE",
    "PF_IPV4",
    "PF_IPV6",
    "PF_FILTER_DESCRIPTOR",
    "PF_FILTER_STATS",
    "PF_INTERFACE_STATS",
    "PF_LATEBIND_INFO",
    "PFFRAMETYPE",
    "PFFT_FILTER",
    "PFFT_FRAG",
    "PFFT_SPOOF",
    "PFLOGFRAME",
    "GetIfEntry2",
    "GetIfEntry2Ex",
    "GetIfTable2",
    "GetIfTable2Ex",
    "GetIfStackTable",
    "GetInvertedIfStackTable",
    "GetIpInterfaceEntry",
    "GetIpInterfaceTable",
    "InitializeIpInterfaceEntry",
    "NotifyIpInterfaceChange",
    "SetIpInterfaceEntry",
    "GetIpNetworkConnectionBandwidthEstimates",
    "CreateUnicastIpAddressEntry",
    "DeleteUnicastIpAddressEntry",
    "GetUnicastIpAddressEntry",
    "GetUnicastIpAddressTable",
    "InitializeUnicastIpAddressEntry",
    "NotifyUnicastIpAddressChange",
    "NotifyStableUnicastIpAddressTable",
    "SetUnicastIpAddressEntry",
    "CreateAnycastIpAddressEntry",
    "DeleteAnycastIpAddressEntry",
    "GetAnycastIpAddressEntry",
    "GetAnycastIpAddressTable",
    "GetMulticastIpAddressEntry",
    "GetMulticastIpAddressTable",
    "CreateIpForwardEntry2",
    "DeleteIpForwardEntry2",
    "GetBestRoute2",
    "GetIpForwardEntry2",
    "GetIpForwardTable2",
    "InitializeIpForwardEntry",
    "NotifyRouteChange2",
    "SetIpForwardEntry2",
    "FlushIpPathTable",
    "GetIpPathEntry",
    "GetIpPathTable",
    "CreateIpNetEntry2",
    "DeleteIpNetEntry2",
    "FlushIpNetTable2",
    "GetIpNetEntry2",
    "GetIpNetTable2",
    "ResolveIpNetEntry2",
    "SetIpNetEntry2",
    "NotifyTeredoPortChange",
    "GetTeredoPort",
    "CancelMibChangeNotify2",
    "FreeMibTable",
    "CreateSortedAddressPairs",
    "ConvertCompartmentGuidToId",
    "ConvertCompartmentIdToGuid",
    "ConvertInterfaceNameToLuidA",
    "ConvertInterfaceNameToLuidW",
    "ConvertInterfaceNameToLuid",
    "ConvertInterfaceLuidToNameA",
    "ConvertInterfaceLuidToNameW",
    "ConvertInterfaceLuidToName",
    "ConvertInterfaceLuidToIndex",
    "ConvertInterfaceIndexToLuid",
    "ConvertInterfaceLuidToAlias",
    "ConvertInterfaceAliasToLuid",
    "ConvertInterfaceLuidToGuid",
    "ConvertInterfaceGuidToLuid",
    "if_nametoindex",
    "if_indextoname",
    "GetCurrentThreadCompartmentId",
    "SetCurrentThreadCompartmentId",
    "GetCurrentThreadCompartmentScope",
    "SetCurrentThreadCompartmentScope",
    "GetJobCompartmentId",
    "SetJobCompartmentId",
    "GetSessionCompartmentId",
    "SetSessionCompartmentId",
    "GetDefaultCompartmentId",
    "GetNetworkInformation",
    "SetNetworkInformation",
    "ConvertLengthToIpv4Mask",
    "ConvertIpv4MaskToLength",
    "GetDnsSettings",
    "FreeDnsSettings",
    "SetDnsSettings",
    "GetInterfaceDnsSettings",
    "FreeInterfaceDnsSettings",
    "SetInterfaceDnsSettings",
    "GetNetworkConnectivityHint",
    "GetNetworkConnectivityHintForInterface",
    "NotifyNetworkConnectivityHintChange",
    "IcmpCreateFile",
    "Icmp6CreateFile",
    "IcmpCloseHandle",
    "IcmpSendEcho",
    "IcmpSendEcho2",
    "IcmpSendEcho2Ex",
    "Icmp6SendEcho2",
    "IcmpParseReplies",
    "Icmp6ParseReplies",
    "GetNumberOfInterfaces",
    "GetIfEntry",
    "GetIfTable",
    "GetIpAddrTable",
    "GetIpNetTable",
    "GetIpForwardTable",
    "GetTcpTable",
    "GetExtendedTcpTable",
    "GetOwnerModuleFromTcpEntry",
    "GetUdpTable",
    "GetExtendedUdpTable",
    "GetOwnerModuleFromUdpEntry",
    "GetTcpTable2",
    "GetTcp6Table",
    "GetTcp6Table2",
    "GetPerTcpConnectionEStats",
    "SetPerTcpConnectionEStats",
    "GetPerTcp6ConnectionEStats",
    "SetPerTcp6ConnectionEStats",
    "GetOwnerModuleFromTcp6Entry",
    "GetUdp6Table",
    "GetOwnerModuleFromUdp6Entry",
    "GetOwnerModuleFromPidAndInfo",
    "GetIpStatistics",
    "GetIcmpStatistics",
    "GetTcpStatistics",
    "GetUdpStatistics",
    "SetIpStatisticsEx",
    "GetIpStatisticsEx",
    "GetIcmpStatisticsEx",
    "GetTcpStatisticsEx",
    "GetUdpStatisticsEx",
    "GetTcpStatisticsEx2",
    "GetUdpStatisticsEx2",
    "SetIfEntry",
    "CreateIpForwardEntry",
    "SetIpForwardEntry",
    "DeleteIpForwardEntry",
    "SetIpStatistics",
    "SetIpTTL",
    "CreateIpNetEntry",
    "SetIpNetEntry",
    "DeleteIpNetEntry",
    "FlushIpNetTable",
    "CreateProxyArpEntry",
    "DeleteProxyArpEntry",
    "SetTcpEntry",
    "GetInterfaceInfo",
    "GetUniDirectionalAdapterInfo",
    "NhpAllocateAndGetInterfaceInfoFromStack",
    "GetBestInterface",
    "GetBestInterfaceEx",
    "GetBestRoute",
    "NotifyAddrChange",
    "NotifyRouteChange",
    "CancelIPChangeNotify",
    "GetAdapterIndex",
    "AddIPAddress",
    "DeleteIPAddress",
    "GetNetworkParams",
    "GetAdaptersInfo",
    "GetAdapterOrderMap",
    "GetAdaptersAddresses",
    "GetPerAdapterInfo",
    "GetInterfaceActiveTimestampCapabilities",
    "GetInterfaceSupportedTimestampCapabilities",
    "CaptureInterfaceHardwareCrossTimestamp",
    "RegisterInterfaceTimestampConfigChange",
    "UnregisterInterfaceTimestampConfigChange",
    "IpReleaseAddress",
    "IpRenewAddress",
    "SendARP",
    "GetRTTAndHopCount",
    "GetFriendlyIfIndex",
    "EnableRouter",
    "UnenableRouter",
    "DisableMediaSense",
    "RestoreMediaSense",
    "GetIpErrorString",
    "ResolveNeighbor",
    "CreatePersistentTcpPortReservation",
    "CreatePersistentUdpPortReservation",
    "DeletePersistentTcpPortReservation",
    "DeletePersistentUdpPortReservation",
    "LookupPersistentTcpPortReservation",
    "LookupPersistentUdpPortReservation",
    "PfCreateInterface",
    "PfDeleteInterface",
    "PfAddFiltersToInterface",
    "PfRemoveFiltersFromInterface",
    "PfRemoveFilterHandles",
    "PfUnBindInterface",
    "PfBindInterfaceToIndex",
    "PfBindInterfaceToIPAddress",
    "PfRebindFilters",
    "PfAddGlobalFilterToInterface",
    "PfRemoveGlobalFilterFromInterface",
    "PfMakeLog",
    "PfSetLogBuffer",
    "PfDeleteLog",
    "PfGetInterfaceStatistics",
    "PfTestPacket",
]
