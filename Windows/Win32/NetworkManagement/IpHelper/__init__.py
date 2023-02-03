from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.IpHelper
import Windows.Win32.NetworkManagement.Ndis
import Windows.Win32.Networking.WinSock
import Windows.Win32.System.IO
import Windows.Win32.System.WindowsProgramming
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
class ARP_SEND_REPLY(Structure):
    DestAddress: UInt32
    SrcAddress: UInt32
ANY_SIZE: UInt32 = 1
MAXLEN_PHYSADDR: UInt32 = 8
MAXLEN_IFDESCR: UInt32 = 256
MAX_INTERFACE_NAME_LEN: UInt32 = 256
MIN_IF_TYPE: UInt32 = 1
IF_TYPE_OTHER: UInt32 = 1
IF_TYPE_REGULAR_1822: UInt32 = 2
IF_TYPE_HDH_1822: UInt32 = 3
IF_TYPE_DDN_X25: UInt32 = 4
IF_TYPE_RFC877_X25: UInt32 = 5
IF_TYPE_ETHERNET_CSMACD: UInt32 = 6
IF_TYPE_IS088023_CSMACD: UInt32 = 7
IF_TYPE_ISO88024_TOKENBUS: UInt32 = 8
IF_TYPE_ISO88025_TOKENRING: UInt32 = 9
IF_TYPE_ISO88026_MAN: UInt32 = 10
IF_TYPE_STARLAN: UInt32 = 11
IF_TYPE_PROTEON_10MBIT: UInt32 = 12
IF_TYPE_PROTEON_80MBIT: UInt32 = 13
IF_TYPE_HYPERCHANNEL: UInt32 = 14
IF_TYPE_FDDI: UInt32 = 15
IF_TYPE_LAP_B: UInt32 = 16
IF_TYPE_SDLC: UInt32 = 17
IF_TYPE_DS1: UInt32 = 18
IF_TYPE_E1: UInt32 = 19
IF_TYPE_BASIC_ISDN: UInt32 = 20
IF_TYPE_PRIMARY_ISDN: UInt32 = 21
IF_TYPE_PROP_POINT2POINT_SERIAL: UInt32 = 22
IF_TYPE_PPP: UInt32 = 23
IF_TYPE_SOFTWARE_LOOPBACK: UInt32 = 24
IF_TYPE_EON: UInt32 = 25
IF_TYPE_ETHERNET_3MBIT: UInt32 = 26
IF_TYPE_NSIP: UInt32 = 27
IF_TYPE_SLIP: UInt32 = 28
IF_TYPE_ULTRA: UInt32 = 29
IF_TYPE_DS3: UInt32 = 30
IF_TYPE_SIP: UInt32 = 31
IF_TYPE_FRAMERELAY: UInt32 = 32
IF_TYPE_RS232: UInt32 = 33
IF_TYPE_PARA: UInt32 = 34
IF_TYPE_ARCNET: UInt32 = 35
IF_TYPE_ARCNET_PLUS: UInt32 = 36
IF_TYPE_ATM: UInt32 = 37
IF_TYPE_MIO_X25: UInt32 = 38
IF_TYPE_SONET: UInt32 = 39
IF_TYPE_X25_PLE: UInt32 = 40
IF_TYPE_ISO88022_LLC: UInt32 = 41
IF_TYPE_LOCALTALK: UInt32 = 42
IF_TYPE_SMDS_DXI: UInt32 = 43
IF_TYPE_FRAMERELAY_SERVICE: UInt32 = 44
IF_TYPE_V35: UInt32 = 45
IF_TYPE_HSSI: UInt32 = 46
IF_TYPE_HIPPI: UInt32 = 47
IF_TYPE_MODEM: UInt32 = 48
IF_TYPE_AAL5: UInt32 = 49
IF_TYPE_SONET_PATH: UInt32 = 50
IF_TYPE_SONET_VT: UInt32 = 51
IF_TYPE_SMDS_ICIP: UInt32 = 52
IF_TYPE_PROP_VIRTUAL: UInt32 = 53
IF_TYPE_PROP_MULTIPLEXOR: UInt32 = 54
IF_TYPE_IEEE80212: UInt32 = 55
IF_TYPE_FIBRECHANNEL: UInt32 = 56
IF_TYPE_HIPPIINTERFACE: UInt32 = 57
IF_TYPE_FRAMERELAY_INTERCONNECT: UInt32 = 58
IF_TYPE_AFLANE_8023: UInt32 = 59
IF_TYPE_AFLANE_8025: UInt32 = 60
IF_TYPE_CCTEMUL: UInt32 = 61
IF_TYPE_FASTETHER: UInt32 = 62
IF_TYPE_ISDN: UInt32 = 63
IF_TYPE_V11: UInt32 = 64
IF_TYPE_V36: UInt32 = 65
IF_TYPE_G703_64K: UInt32 = 66
IF_TYPE_G703_2MB: UInt32 = 67
IF_TYPE_QLLC: UInt32 = 68
IF_TYPE_FASTETHER_FX: UInt32 = 69
IF_TYPE_CHANNEL: UInt32 = 70
IF_TYPE_IEEE80211: UInt32 = 71
IF_TYPE_IBM370PARCHAN: UInt32 = 72
IF_TYPE_ESCON: UInt32 = 73
IF_TYPE_DLSW: UInt32 = 74
IF_TYPE_ISDN_S: UInt32 = 75
IF_TYPE_ISDN_U: UInt32 = 76
IF_TYPE_LAP_D: UInt32 = 77
IF_TYPE_IPSWITCH: UInt32 = 78
IF_TYPE_RSRB: UInt32 = 79
IF_TYPE_ATM_LOGICAL: UInt32 = 80
IF_TYPE_DS0: UInt32 = 81
IF_TYPE_DS0_BUNDLE: UInt32 = 82
IF_TYPE_BSC: UInt32 = 83
IF_TYPE_ASYNC: UInt32 = 84
IF_TYPE_CNR: UInt32 = 85
IF_TYPE_ISO88025R_DTR: UInt32 = 86
IF_TYPE_EPLRS: UInt32 = 87
IF_TYPE_ARAP: UInt32 = 88
IF_TYPE_PROP_CNLS: UInt32 = 89
IF_TYPE_HOSTPAD: UInt32 = 90
IF_TYPE_TERMPAD: UInt32 = 91
IF_TYPE_FRAMERELAY_MPI: UInt32 = 92
IF_TYPE_X213: UInt32 = 93
IF_TYPE_ADSL: UInt32 = 94
IF_TYPE_RADSL: UInt32 = 95
IF_TYPE_SDSL: UInt32 = 96
IF_TYPE_VDSL: UInt32 = 97
IF_TYPE_ISO88025_CRFPRINT: UInt32 = 98
IF_TYPE_MYRINET: UInt32 = 99
IF_TYPE_VOICE_EM: UInt32 = 100
IF_TYPE_VOICE_FXO: UInt32 = 101
IF_TYPE_VOICE_FXS: UInt32 = 102
IF_TYPE_VOICE_ENCAP: UInt32 = 103
IF_TYPE_VOICE_OVERIP: UInt32 = 104
IF_TYPE_ATM_DXI: UInt32 = 105
IF_TYPE_ATM_FUNI: UInt32 = 106
IF_TYPE_ATM_IMA: UInt32 = 107
IF_TYPE_PPPMULTILINKBUNDLE: UInt32 = 108
IF_TYPE_IPOVER_CDLC: UInt32 = 109
IF_TYPE_IPOVER_CLAW: UInt32 = 110
IF_TYPE_STACKTOSTACK: UInt32 = 111
IF_TYPE_VIRTUALIPADDRESS: UInt32 = 112
IF_TYPE_MPC: UInt32 = 113
IF_TYPE_IPOVER_ATM: UInt32 = 114
IF_TYPE_ISO88025_FIBER: UInt32 = 115
IF_TYPE_TDLC: UInt32 = 116
IF_TYPE_GIGABITETHERNET: UInt32 = 117
IF_TYPE_HDLC: UInt32 = 118
IF_TYPE_LAP_F: UInt32 = 119
IF_TYPE_V37: UInt32 = 120
IF_TYPE_X25_MLP: UInt32 = 121
IF_TYPE_X25_HUNTGROUP: UInt32 = 122
IF_TYPE_TRANSPHDLC: UInt32 = 123
IF_TYPE_INTERLEAVE: UInt32 = 124
IF_TYPE_FAST: UInt32 = 125
IF_TYPE_IP: UInt32 = 126
IF_TYPE_DOCSCABLE_MACLAYER: UInt32 = 127
IF_TYPE_DOCSCABLE_DOWNSTREAM: UInt32 = 128
IF_TYPE_DOCSCABLE_UPSTREAM: UInt32 = 129
IF_TYPE_A12MPPSWITCH: UInt32 = 130
IF_TYPE_TUNNEL: UInt32 = 131
IF_TYPE_COFFEE: UInt32 = 132
IF_TYPE_CES: UInt32 = 133
IF_TYPE_ATM_SUBINTERFACE: UInt32 = 134
IF_TYPE_L2_VLAN: UInt32 = 135
IF_TYPE_L3_IPVLAN: UInt32 = 136
IF_TYPE_L3_IPXVLAN: UInt32 = 137
IF_TYPE_DIGITALPOWERLINE: UInt32 = 138
IF_TYPE_MEDIAMAILOVERIP: UInt32 = 139
IF_TYPE_DTM: UInt32 = 140
IF_TYPE_DCN: UInt32 = 141
IF_TYPE_IPFORWARD: UInt32 = 142
IF_TYPE_MSDSL: UInt32 = 143
IF_TYPE_IEEE1394: UInt32 = 144
IF_TYPE_IF_GSN: UInt32 = 145
IF_TYPE_DVBRCC_MACLAYER: UInt32 = 146
IF_TYPE_DVBRCC_DOWNSTREAM: UInt32 = 147
IF_TYPE_DVBRCC_UPSTREAM: UInt32 = 148
IF_TYPE_ATM_VIRTUAL: UInt32 = 149
IF_TYPE_MPLS_TUNNEL: UInt32 = 150
IF_TYPE_SRP: UInt32 = 151
IF_TYPE_VOICEOVERATM: UInt32 = 152
IF_TYPE_VOICEOVERFRAMERELAY: UInt32 = 153
IF_TYPE_IDSL: UInt32 = 154
IF_TYPE_COMPOSITELINK: UInt32 = 155
IF_TYPE_SS7_SIGLINK: UInt32 = 156
IF_TYPE_PROP_WIRELESS_P2P: UInt32 = 157
IF_TYPE_FR_FORWARD: UInt32 = 158
IF_TYPE_RFC1483: UInt32 = 159
IF_TYPE_USB: UInt32 = 160
IF_TYPE_IEEE8023AD_LAG: UInt32 = 161
IF_TYPE_BGP_POLICY_ACCOUNTING: UInt32 = 162
IF_TYPE_FRF16_MFR_BUNDLE: UInt32 = 163
IF_TYPE_H323_GATEKEEPER: UInt32 = 164
IF_TYPE_H323_PROXY: UInt32 = 165
IF_TYPE_MPLS: UInt32 = 166
IF_TYPE_MF_SIGLINK: UInt32 = 167
IF_TYPE_HDSL2: UInt32 = 168
IF_TYPE_SHDSL: UInt32 = 169
IF_TYPE_DS1_FDL: UInt32 = 170
IF_TYPE_POS: UInt32 = 171
IF_TYPE_DVB_ASI_IN: UInt32 = 172
IF_TYPE_DVB_ASI_OUT: UInt32 = 173
IF_TYPE_PLC: UInt32 = 174
IF_TYPE_NFAS: UInt32 = 175
IF_TYPE_TR008: UInt32 = 176
IF_TYPE_GR303_RDT: UInt32 = 177
IF_TYPE_GR303_IDT: UInt32 = 178
IF_TYPE_ISUP: UInt32 = 179
IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER: UInt32 = 180
IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM: UInt32 = 181
IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM: UInt32 = 182
IF_TYPE_HIPERLAN2: UInt32 = 183
IF_TYPE_PROP_BWA_P2MP: UInt32 = 184
IF_TYPE_SONET_OVERHEAD_CHANNEL: UInt32 = 185
IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL: UInt32 = 186
IF_TYPE_AAL2: UInt32 = 187
IF_TYPE_RADIO_MAC: UInt32 = 188
IF_TYPE_ATM_RADIO: UInt32 = 189
IF_TYPE_IMT: UInt32 = 190
IF_TYPE_MVL: UInt32 = 191
IF_TYPE_REACH_DSL: UInt32 = 192
IF_TYPE_FR_DLCI_ENDPT: UInt32 = 193
IF_TYPE_ATM_VCI_ENDPT: UInt32 = 194
IF_TYPE_OPTICAL_CHANNEL: UInt32 = 195
IF_TYPE_OPTICAL_TRANSPORT: UInt32 = 196
IF_TYPE_IEEE80216_WMAN: UInt32 = 237
IF_TYPE_WWANPP: UInt32 = 243
IF_TYPE_WWANPP2: UInt32 = 244
IF_TYPE_IEEE802154: UInt32 = 259
IF_TYPE_XBOX_WIRELESS: UInt32 = 281
MAX_IF_TYPE: UInt32 = 281
IF_CHECK_NONE: UInt32 = 0
IF_CHECK_MCAST: UInt32 = 1
IF_CHECK_SEND: UInt32 = 2
IF_CONNECTION_DEDICATED: UInt32 = 1
IF_CONNECTION_PASSIVE: UInt32 = 2
IF_CONNECTION_DEMAND: UInt32 = 3
IF_ADMIN_STATUS_UP: UInt32 = 1
IF_ADMIN_STATUS_DOWN: UInt32 = 2
IF_ADMIN_STATUS_TESTING: UInt32 = 3
MIB_IF_TYPE_OTHER: UInt32 = 1
MIB_IF_TYPE_ETHERNET: UInt32 = 6
MIB_IF_TYPE_TOKENRING: UInt32 = 9
MIB_IF_TYPE_FDDI: UInt32 = 15
MIB_IF_TYPE_PPP: UInt32 = 23
MIB_IF_TYPE_LOOPBACK: UInt32 = 24
MIB_IF_TYPE_SLIP: UInt32 = 28
MIB_IF_ADMIN_STATUS_UP: UInt32 = 1
MIB_IF_ADMIN_STATUS_DOWN: UInt32 = 2
MIB_IF_ADMIN_STATUS_TESTING: UInt32 = 3
MIB_IPADDR_PRIMARY: UInt32 = 1
MIB_IPADDR_DYNAMIC: UInt32 = 4
MIB_IPADDR_DISCONNECTED: UInt32 = 8
MIB_IPADDR_DELETED: UInt32 = 64
MIB_IPADDR_TRANSIENT: UInt32 = 128
MIB_IPADDR_DNS_ELIGIBLE: UInt32 = 256
MIB_IPROUTE_METRIC_UNUSED: UInt32 = 4294967295
MIB_USE_CURRENT_TTL: UInt32 = 4294967295
MIB_USE_CURRENT_FORWARDING: UInt32 = 4294967295
ICMP6_INFOMSG_MASK: UInt32 = 128
IPRTRMGR_PID: UInt32 = 10000
IF_NUMBER: UInt32 = 0
IF_TABLE: UInt32 = 1
IF_ROW: UInt32 = 2
IP_STATS: UInt32 = 3
IP_ADDRTABLE: UInt32 = 4
IP_ADDRROW: UInt32 = 5
IP_FORWARDNUMBER: UInt32 = 6
IP_FORWARDTABLE: UInt32 = 7
IP_FORWARDROW: UInt32 = 8
IP_NETTABLE: UInt32 = 9
IP_NETROW: UInt32 = 10
ICMP_STATS: UInt32 = 11
TCP_STATS: UInt32 = 12
TCP_TABLE: UInt32 = 13
TCP_ROW: UInt32 = 14
UDP_STATS: UInt32 = 15
UDP_TABLE: UInt32 = 16
UDP_ROW: UInt32 = 17
MCAST_MFE: UInt32 = 18
MCAST_MFE_STATS: UInt32 = 19
BEST_IF: UInt32 = 20
BEST_ROUTE: UInt32 = 21
PROXY_ARP: UInt32 = 22
MCAST_IF_ENTRY: UInt32 = 23
MCAST_GLOBAL: UInt32 = 24
IF_STATUS: UInt32 = 25
MCAST_BOUNDARY: UInt32 = 26
MCAST_SCOPE: UInt32 = 27
DEST_MATCHING: UInt32 = 28
DEST_LONGER: UInt32 = 29
DEST_SHORTER: UInt32 = 30
ROUTE_MATCHING: UInt32 = 31
ROUTE_LONGER: UInt32 = 32
ROUTE_SHORTER: UInt32 = 33
ROUTE_STATE: UInt32 = 34
MCAST_MFE_STATS_EX: UInt32 = 35
IP6_STATS: UInt32 = 36
UDP6_STATS: UInt32 = 37
TCP6_STATS: UInt32 = 38
NUMBER_OF_EXPORTED_VARIABLES: UInt32 = 39
MAX_SCOPE_NAME_LEN: UInt32 = 255
MAX_MIB_OFFSET: UInt32 = 8
MIB_INVALID_TEREDO_PORT_NUMBER: UInt32 = 0
DNS_SETTINGS_VERSION1: UInt32 = 1
DNS_SETTINGS_VERSION2: UInt32 = 2
DNS_INTERFACE_SETTINGS_VERSION1: UInt32 = 1
DNS_INTERFACE_SETTINGS_VERSION2: UInt32 = 2
DNS_INTERFACE_SETTINGS_VERSION3: UInt32 = 3
DNS_SETTING_IPV6: UInt32 = 1
DNS_SETTING_NAMESERVER: UInt32 = 2
DNS_SETTING_SEARCHLIST: UInt32 = 4
DNS_SETTING_REGISTRATION_ENABLED: UInt32 = 8
DNS_SETTING_REGISTER_ADAPTER_NAME: UInt32 = 16
DNS_SETTING_DOMAIN: UInt32 = 32
DNS_SETTING_HOSTNAME: UInt32 = 64
DNS_SETTINGS_ENABLE_LLMNR: UInt32 = 128
DNS_SETTINGS_QUERY_ADAPTER_NAME: UInt32 = 256
DNS_SETTING_PROFILE_NAMESERVER: UInt32 = 512
DNS_SETTING_DISABLE_UNCONSTRAINED_QUERIES: UInt32 = 1024
DNS_SETTING_SUPPLEMENTAL_SEARCH_LIST: UInt32 = 2048
DNS_SETTING_DOH: UInt32 = 4096
DNS_SETTING_DOH_PROFILE: UInt32 = 8192
DNS_ENABLE_DOH: UInt32 = 1
DNS_DOH_POLICY_NOT_CONFIGURED: UInt32 = 4
DNS_DOH_POLICY_DISABLE: UInt32 = 8
DNS_DOH_POLICY_AUTO: UInt32 = 16
DNS_DOH_POLICY_REQUIRED: UInt32 = 32
DNS_SERVER_PROPERTY_VERSION1: UInt32 = 1
DNS_DOH_SERVER_SETTINGS_ENABLE_AUTO: UInt32 = 1
DNS_DOH_SERVER_SETTINGS_ENABLE: UInt32 = 2
DNS_DOH_SERVER_SETTINGS_FALLBACK_TO_UDP: UInt32 = 4
DNS_DOH_AUTO_UPGRADE_SERVER: UInt32 = 8
TCPIP_OWNING_MODULE_SIZE: UInt32 = 16
FD_FLAGS_NOSYN: UInt32 = 1
FD_FLAGS_ALLFLAGS: UInt32 = 1
LB_SRC_ADDR_USE_SRCADDR_FLAG: UInt32 = 1
LB_SRC_ADDR_USE_DSTADDR_FLAG: UInt32 = 2
LB_DST_ADDR_USE_SRCADDR_FLAG: UInt32 = 4
LB_DST_ADDR_USE_DSTADDR_FLAG: UInt32 = 8
LB_SRC_MASK_LATE_FLAG: UInt32 = 16
LB_DST_MASK_LATE_FLAG: UInt32 = 32
ERROR_BASE: UInt32 = 23000
PFERROR_NO_PF_INTERFACE: UInt32 = 23000
PFERROR_NO_FILTERS_GIVEN: UInt32 = 23001
PFERROR_BUFFER_TOO_SMALL: UInt32 = 23002
ERROR_IPV6_NOT_IMPLEMENTED: UInt32 = 23003
IP_EXPORT_INCLUDED: UInt32 = 1
MAX_ADAPTER_NAME: UInt32 = 128
IP_STATUS_BASE: UInt32 = 11000
IP_SUCCESS: UInt32 = 0
IP_BUF_TOO_SMALL: UInt32 = 11001
IP_DEST_NET_UNREACHABLE: UInt32 = 11002
IP_DEST_HOST_UNREACHABLE: UInt32 = 11003
IP_DEST_PROT_UNREACHABLE: UInt32 = 11004
IP_DEST_PORT_UNREACHABLE: UInt32 = 11005
IP_NO_RESOURCES: UInt32 = 11006
IP_BAD_OPTION: UInt32 = 11007
IP_HW_ERROR: UInt32 = 11008
IP_PACKET_TOO_BIG: UInt32 = 11009
IP_REQ_TIMED_OUT: UInt32 = 11010
IP_BAD_REQ: UInt32 = 11011
IP_BAD_ROUTE: UInt32 = 11012
IP_TTL_EXPIRED_TRANSIT: UInt32 = 11013
IP_TTL_EXPIRED_REASSEM: UInt32 = 11014
IP_PARAM_PROBLEM: UInt32 = 11015
IP_SOURCE_QUENCH: UInt32 = 11016
IP_OPTION_TOO_BIG: UInt32 = 11017
IP_BAD_DESTINATION: UInt32 = 11018
IP_DEST_NO_ROUTE: UInt32 = 11002
IP_DEST_ADDR_UNREACHABLE: UInt32 = 11003
IP_DEST_PROHIBITED: UInt32 = 11004
IP_HOP_LIMIT_EXCEEDED: UInt32 = 11013
IP_REASSEMBLY_TIME_EXCEEDED: UInt32 = 11014
IP_PARAMETER_PROBLEM: UInt32 = 11015
IP_DEST_UNREACHABLE: UInt32 = 11040
IP_TIME_EXCEEDED: UInt32 = 11041
IP_BAD_HEADER: UInt32 = 11042
IP_UNRECOGNIZED_NEXT_HEADER: UInt32 = 11043
IP_ICMP_ERROR: UInt32 = 11044
IP_DEST_SCOPE_MISMATCH: UInt32 = 11045
IP_ADDR_DELETED: UInt32 = 11019
IP_SPEC_MTU_CHANGE: UInt32 = 11020
IP_MTU_CHANGE: UInt32 = 11021
IP_UNLOAD: UInt32 = 11022
IP_ADDR_ADDED: UInt32 = 11023
IP_MEDIA_CONNECT: UInt32 = 11024
IP_MEDIA_DISCONNECT: UInt32 = 11025
IP_BIND_ADAPTER: UInt32 = 11026
IP_UNBIND_ADAPTER: UInt32 = 11027
IP_DEVICE_DOES_NOT_EXIST: UInt32 = 11028
IP_DUPLICATE_ADDRESS: UInt32 = 11029
IP_INTERFACE_METRIC_CHANGE: UInt32 = 11030
IP_RECONFIG_SECFLTR: UInt32 = 11031
IP_NEGOTIATING_IPSEC: UInt32 = 11032
IP_INTERFACE_WOL_CAPABILITY_CHANGE: UInt32 = 11033
IP_DUPLICATE_IPADD: UInt32 = 11034
IP_GENERAL_FAILURE: UInt32 = 11050
MAX_IP_STATUS: UInt32 = 11050
IP_PENDING: UInt32 = 11255
IP_FLAG_REVERSE: UInt32 = 1
IP_FLAG_DF: UInt32 = 2
MAX_OPT_SIZE: UInt32 = 40
IOCTL_IP_RTCHANGE_NOTIFY_REQUEST: UInt32 = 101
IOCTL_IP_ADDCHANGE_NOTIFY_REQUEST: UInt32 = 102
IOCTL_ARP_SEND_REQUEST: UInt32 = 103
IOCTL_IP_INTERFACE_INFO: UInt32 = 104
IOCTL_IP_GET_BEST_INTERFACE: UInt32 = 105
IOCTL_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS: UInt32 = 106
NET_STRING_IPV4_ADDRESS: UInt32 = 1
NET_STRING_IPV4_SERVICE: UInt32 = 2
NET_STRING_IPV4_NETWORK: UInt32 = 4
NET_STRING_IPV6_ADDRESS: UInt32 = 8
NET_STRING_IPV6_ADDRESS_NO_SCOPE: UInt32 = 16
NET_STRING_IPV6_SERVICE: UInt32 = 32
NET_STRING_IPV6_SERVICE_NO_SCOPE: UInt32 = 64
NET_STRING_IPV6_NETWORK: UInt32 = 128
NET_STRING_NAMED_ADDRESS: UInt32 = 256
NET_STRING_NAMED_SERVICE: UInt32 = 512
MAX_ADAPTER_DESCRIPTION_LENGTH: UInt32 = 128
MAX_ADAPTER_NAME_LENGTH: UInt32 = 256
MAX_ADAPTER_ADDRESS_LENGTH: UInt32 = 8
DEFAULT_MINIMUM_ENTITIES: UInt32 = 32
MAX_HOSTNAME_LEN: UInt32 = 128
MAX_DOMAIN_NAME_LEN: UInt32 = 128
MAX_SCOPE_ID_LEN: UInt32 = 256
MAX_DHCPV6_DUID_LENGTH: UInt32 = 130
MAX_DNS_SUFFIX_STRING_LENGTH: UInt32 = 256
BROADCAST_NODETYPE: UInt32 = 1
PEER_TO_PEER_NODETYPE: UInt32 = 2
MIXED_NODETYPE: UInt32 = 4
HYBRID_NODETYPE: UInt32 = 8
IP_ADAPTER_ADDRESS_DNS_ELIGIBLE: UInt32 = 1
IP_ADAPTER_ADDRESS_TRANSIENT: UInt32 = 2
IP_ADAPTER_DDNS_ENABLED: UInt32 = 1
IP_ADAPTER_REGISTER_ADAPTER_SUFFIX: UInt32 = 2
IP_ADAPTER_DHCP_ENABLED: UInt32 = 4
IP_ADAPTER_RECEIVE_ONLY: UInt32 = 8
IP_ADAPTER_NO_MULTICAST: UInt32 = 16
IP_ADAPTER_IPV6_OTHER_STATEFUL_CONFIG: UInt32 = 32
IP_ADAPTER_NETBIOS_OVER_TCPIP_ENABLED: UInt32 = 64
IP_ADAPTER_IPV4_ENABLED: UInt32 = 128
IP_ADAPTER_IPV6_ENABLED: UInt32 = 256
IP_ADAPTER_IPV6_MANAGE_ADDRESS_CONFIG: UInt32 = 512
GAA_FLAG_SKIP_DNS_INFO: UInt32 = 2048
IP_ROUTER_MANAGER_VERSION: UInt32 = 1
IP_GENERAL_INFO_BASE: UInt32 = 4294901760
IP_IN_FILTER_INFO: UInt32 = 4294901761
IP_OUT_FILTER_INFO: UInt32 = 4294901762
IP_GLOBAL_INFO: UInt32 = 4294901763
IP_INTERFACE_STATUS_INFO: UInt32 = 4294901764
IP_ROUTE_INFO: UInt32 = 4294901765
IP_PROT_PRIORITY_INFO: UInt32 = 4294901766
IP_ROUTER_DISC_INFO: UInt32 = 4294901767
IP_DEMAND_DIAL_FILTER_INFO: UInt32 = 4294901769
IP_MCAST_HEARBEAT_INFO: UInt32 = 4294901770
IP_MCAST_BOUNDARY_INFO: UInt32 = 4294901771
IP_IPINIP_CFG_INFO: UInt32 = 4294901772
IP_IFFILTER_INFO: UInt32 = 4294901773
IP_MCAST_LIMIT_INFO: UInt32 = 4294901774
IPV6_GLOBAL_INFO: UInt32 = 4294901775
IPV6_ROUTE_INFO: UInt32 = 4294901776
IP_IN_FILTER_INFO_V6: UInt32 = 4294901777
IP_OUT_FILTER_INFO_V6: UInt32 = 4294901778
IP_DEMAND_DIAL_FILTER_INFO_V6: UInt32 = 4294901779
IP_IFFILTER_INFO_V6: UInt32 = 4294901780
IP_FILTER_ENABLE_INFO: UInt32 = 4294901781
IP_FILTER_ENABLE_INFO_V6: UInt32 = 4294901782
IP_PROT_PRIORITY_INFO_EX: UInt32 = 4294901783
@winfunctype('IPHLPAPI.dll')
def GetIfEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIfEntry2Ex(Level: Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ENTRY_LEVEL, Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIfTable2(Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE2_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIfTable2Ex(Level: Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE_LEVEL, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE2_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIfStackTable(Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IFSTACK_TABLE_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetInvertedIfStackTable(Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_TABLE_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpInterfaceEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpInterfaceTable(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_TABLE_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def InitializeIpInterfaceEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def NotifyIpInterfaceChange(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Callback: Windows.Win32.NetworkManagement.IpHelper.PIPINTERFACE_CHANGE_CALLBACK, CallerContext: c_void_p, InitialNotification: Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def SetIpInterfaceEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetworkConnectionBandwidthEstimates(InterfaceIndex: UInt32, AddressFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, BandwidthEstimates: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def CreateUnicastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def DeleteUnicastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetUnicastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetUnicastIpAddressTable(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def InitializeUnicastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def NotifyUnicastIpAddressChange(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Callback: Windows.Win32.NetworkManagement.IpHelper.PUNICAST_IPADDRESS_CHANGE_CALLBACK, CallerContext: c_void_p, InitialNotification: Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def NotifyStableUnicastIpAddressTable(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE_head)), CallerCallback: Windows.Win32.NetworkManagement.IpHelper.PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK, CallerContext: c_void_p, NotificationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def SetUnicastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def CreateAnycastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def DeleteAnycastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetAnycastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetAnycastIpAddressTable(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_TABLE_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetMulticastIpAddressEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetMulticastIpAddressTable(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_TABLE_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpForwardEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpForwardEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetBestRoute2(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), InterfaceIndex: UInt32, SourceAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_INET_head), DestinationAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_INET_head), AddressSortOptions: UInt32, BestRoute: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head), BestSourceAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_INET_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpForwardEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpForwardTable2(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TABLE2_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def InitializeIpForwardEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def NotifyRouteChange2(AddressFamily: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Callback: Windows.Win32.NetworkManagement.IpHelper.PIPFORWARD_CHANGE_CALLBACK, CallerContext: c_void_p, InitialNotification: Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def SetIpForwardEntry2(Route: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def FlushIpPathTable(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpPathEntry(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPPATH_ROW_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpPathTable(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPPATH_TABLE_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpNetEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpNetEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def FlushIpNetTable2(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, InterfaceIndex: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetTable2(Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TABLE2_head))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ResolveIpNetEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head), SourceAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_INET_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def SetIpNetEntry2(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def NotifyTeredoPortChange(Callback: Windows.Win32.NetworkManagement.IpHelper.PTEREDO_PORT_CHANGE_CALLBACK, CallerContext: c_void_p, InitialNotification: Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetTeredoPort(Port: POINTER(UInt16)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def CancelMibChangeNotify2(NotificationHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def FreeMibTable(Memory: c_void_p) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def CreateSortedAddressPairs(SourceAddressList: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_IN6_head), SourceAddressCount: UInt32, DestinationAddressList: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_IN6_head), DestinationAddressCount: UInt32, AddressSortOptions: UInt32, SortedAddressPairList: POINTER(POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_IN6_PAIR_head)), SortedAddressPairCount: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertCompartmentGuidToId(CompartmentGuid: POINTER(Guid), CompartmentId: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertCompartmentIdToGuid(CompartmentId: UInt32, CompartmentGuid: POINTER(Guid)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceNameToLuidA(InterfaceName: Windows.Win32.Foundation.PSTR, InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceNameToLuidW(InterfaceName: Windows.Win32.Foundation.PWSTR, InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToNameA(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), InterfaceName: Windows.Win32.Foundation.PSTR, Length: UIntPtr) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToNameW(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), InterfaceName: Windows.Win32.Foundation.PWSTR, Length: UIntPtr) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToIndex(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), InterfaceIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceIndexToLuid(InterfaceIndex: UInt32, InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToAlias(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), InterfaceAlias: Windows.Win32.Foundation.PWSTR, Length: UIntPtr) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceAliasToLuid(InterfaceAlias: Windows.Win32.Foundation.PWSTR, InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToGuid(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), InterfaceGuid: POINTER(Guid)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceGuidToLuid(InterfaceGuid: POINTER(Guid), InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def if_nametoindex(InterfaceName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def if_indextoname(InterfaceIndex: UInt32, InterfaceName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('IPHLPAPI.dll')
def GetCurrentThreadCompartmentId() -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetCurrentThreadCompartmentId(CompartmentId: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetCurrentThreadCompartmentScope(CompartmentScope: POINTER(UInt32), CompartmentId: POINTER(UInt32)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def SetCurrentThreadCompartmentScope(CompartmentScope: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetJobCompartmentId(JobHandle: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetJobCompartmentId(JobHandle: Windows.Win32.Foundation.HANDLE, CompartmentId: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetSessionCompartmentId(SessionId: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetSessionCompartmentId(SessionId: UInt32, CompartmentId: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetDefaultCompartmentId() -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkInformation(NetworkGuid: POINTER(Guid), CompartmentId: POINTER(UInt32), SiteId: POINTER(UInt32), NetworkName: Windows.Win32.Foundation.PWSTR, Length: UInt32) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def SetNetworkInformation(NetworkGuid: POINTER(Guid), CompartmentId: UInt32, NetworkName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertLengthToIpv4Mask(MaskLength: UInt32, Mask: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def ConvertIpv4MaskToLength(Mask: UInt32, MaskLength: c_char_p_no) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetDnsSettings(Settings: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_SETTINGS_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def FreeDnsSettings(Settings: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_SETTINGS_head)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def SetDnsSettings(Settings: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_SETTINGS_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceDnsSettings(Interface: Guid, Settings: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def FreeInterfaceDnsSettings(Settings: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_head)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def SetInterfaceDnsSettings(Interface: Guid, Settings: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkConnectivityHint(ConnectivityHint: POINTER(Windows.Win32.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkConnectivityHintForInterface(InterfaceIndex: UInt32, ConnectivityHint: POINTER(Windows.Win32.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def NotifyNetworkConnectivityHintChange(Callback: Windows.Win32.NetworkManagement.IpHelper.PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK, CallerContext: c_void_p, InitialNotification: Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('IPHLPAPI.dll')
def IcmpCreateFile() -> Windows.Win32.NetworkManagement.IpHelper.IcmpHandle: ...
@winfunctype('IPHLPAPI.dll')
def Icmp6CreateFile() -> Windows.Win32.NetworkManagement.IpHelper.IcmpHandle: ...
@winfunctype('IPHLPAPI.dll')
def IcmpCloseHandle(IcmpHandle: Windows.Win32.NetworkManagement.IpHelper.IcmpHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IPHLPAPI.dll')
def IcmpSendEcho(IcmpHandle: Windows.Win32.NetworkManagement.IpHelper.IcmpHandle, DestinationAddress: UInt32, RequestData: c_void_p, RequestSize: UInt16, RequestOptions: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION_head), ReplyBuffer: c_void_p, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IcmpSendEcho2(IcmpHandle: Windows.Win32.NetworkManagement.IpHelper.IcmpHandle, Event: Windows.Win32.Foundation.HANDLE, ApcRoutine: Windows.Win32.System.WindowsProgramming.PIO_APC_ROUTINE, ApcContext: c_void_p, DestinationAddress: UInt32, RequestData: c_void_p, RequestSize: UInt16, RequestOptions: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION_head), ReplyBuffer: c_void_p, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IcmpSendEcho2Ex(IcmpHandle: Windows.Win32.NetworkManagement.IpHelper.IcmpHandle, Event: Windows.Win32.Foundation.HANDLE, ApcRoutine: Windows.Win32.System.WindowsProgramming.PIO_APC_ROUTINE, ApcContext: c_void_p, SourceAddress: UInt32, DestinationAddress: UInt32, RequestData: c_void_p, RequestSize: UInt16, RequestOptions: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION_head), ReplyBuffer: c_void_p, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def Icmp6SendEcho2(IcmpHandle: Windows.Win32.NetworkManagement.IpHelper.IcmpHandle, Event: Windows.Win32.Foundation.HANDLE, ApcRoutine: Windows.Win32.System.WindowsProgramming.PIO_APC_ROUTINE, ApcContext: c_void_p, SourceAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_IN6_head), DestinationAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_IN6_head), RequestData: c_void_p, RequestSize: UInt16, RequestOptions: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION_head), ReplyBuffer: c_void_p, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IcmpParseReplies(ReplyBuffer: c_void_p, ReplySize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def Icmp6ParseReplies(ReplyBuffer: c_void_p, ReplySize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetNumberOfInterfaces(pdwNumIf: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIfEntry(pIfRow: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IFROW_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIfTable(pIfTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IFTABLE_head), pdwSize: POINTER(UInt32), bOrder: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpAddrTable(pIpAddrTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPADDRTABLE_head), pdwSize: POINTER(UInt32), bOrder: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetTable(IpNetTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETTABLE_head), SizePointer: POINTER(UInt32), Order: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpForwardTable(pIpForwardTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDTABLE_head), pdwSize: POINTER(UInt32), bOrder: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpTable(TcpTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPTABLE_head), SizePointer: POINTER(UInt32), Order: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetExtendedTcpTable(pTcpTable: c_void_p, pdwSize: POINTER(UInt32), bOrder: Windows.Win32.Foundation.BOOL, ulAf: UInt32, TableClass: Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS, Reserved: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromTcpEntry(pTcpEntry: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_MODULE_head), Class: Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: c_void_p, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpTable(UdpTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UDPTABLE_head), SizePointer: POINTER(UInt32), Order: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetExtendedUdpTable(pUdpTable: c_void_p, pdwSize: POINTER(UInt32), bOrder: Windows.Win32.Foundation.BOOL, ulAf: UInt32, TableClass: Windows.Win32.NetworkManagement.IpHelper.UDP_TABLE_CLASS, Reserved: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromUdpEntry(pUdpEntry: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_MODULE_head), Class: Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: c_void_p, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpTable2(TcpTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPTABLE2_head), SizePointer: POINTER(UInt32), Order: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcp6Table(TcpTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6TABLE_head), SizePointer: POINTER(UInt32), Order: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcp6Table2(TcpTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6TABLE2_head), SizePointer: POINTER(UInt32), Order: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetPerTcpConnectionEStats(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH_head), EstatsType: Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: c_char_p_no, RwVersion: UInt32, RwSize: UInt32, Ros: c_char_p_no, RosVersion: UInt32, RosSize: UInt32, Rod: c_char_p_no, RodVersion: UInt32, RodSize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetPerTcpConnectionEStats(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH_head), EstatsType: Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: c_char_p_no, RwVersion: UInt32, RwSize: UInt32, Offset: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetPerTcp6ConnectionEStats(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_head), EstatsType: Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: c_char_p_no, RwVersion: UInt32, RwSize: UInt32, Ros: c_char_p_no, RosVersion: UInt32, RosSize: UInt32, Rod: c_char_p_no, RodVersion: UInt32, RodSize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetPerTcp6ConnectionEStats(Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_head), EstatsType: Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: c_char_p_no, RwVersion: UInt32, RwSize: UInt32, Offset: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromTcp6Entry(pTcpEntry: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_MODULE_head), Class: Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: c_void_p, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdp6Table(Udp6Table: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6TABLE_head), SizePointer: POINTER(UInt32), Order: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromUdp6Entry(pUdpEntry: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_MODULE_head), Class: Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: c_void_p, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromPidAndInfo(ulPid: UInt32, pInfo: POINTER(UInt64), Class: Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: c_void_p, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpStatistics(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIcmpStatistics(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_ICMP_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpStatistics(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPSTATS_LH_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpStatistics(Stats: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UDPSTATS_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpStatisticsEx(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpStatisticsEx(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIcmpStatisticsEx(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_ICMP_EX_XPSP1_head), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpStatisticsEx(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPSTATS_LH_head), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpStatisticsEx(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UDPSTATS_head), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpStatisticsEx2(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPSTATS2_head), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpStatisticsEx2(Statistics: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UDPSTATS2_head), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIfEntry(pIfRow: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IFROW_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpForwardEntry(pRoute: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpForwardEntry(pRoute: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpForwardEntry(pRoute: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpStatistics(pIpStats: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpTTL(nTTL: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpNetEntry(pArpEntry: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpNetEntry(pArpEntry: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpNetEntry(pArpEntry: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def FlushIpNetTable(dwIfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreateProxyArpEntry(dwAddress: UInt32, dwMask: UInt32, dwIfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteProxyArpEntry(dwAddress: UInt32, dwMask: UInt32, dwIfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetTcpEntry(pTcpRow: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceInfo(pIfTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_INTERFACE_INFO_head), dwOutBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUniDirectionalAdapterInfo(pIPIfInfo: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_UNIDIRECTIONAL_ADAPTER_ADDRESS_head), dwOutBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def NhpAllocateAndGetInterfaceInfoFromStack(ppTable: POINTER(POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_INTERFACE_NAME_INFO_W2KSP1_head)), pdwCount: POINTER(UInt32), bOrder: Windows.Win32.Foundation.BOOL, hHeap: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetBestInterface(dwDestAddr: UInt32, pdwBestIfIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetBestInterfaceEx(pDestAddr: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head), pdwBestIfIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetBestRoute(dwDestAddr: UInt32, dwSourceAddr: UInt32, pBestRoute: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def NotifyAddrChange(Handle: POINTER(Windows.Win32.Foundation.HANDLE), overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def NotifyRouteChange(Handle: POINTER(Windows.Win32.Foundation.HANDLE), overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CancelIPChangeNotify(notifyOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IPHLPAPI.dll')
def GetAdapterIndex(AdapterName: Windows.Win32.Foundation.PWSTR, IfIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def AddIPAddress(Address: UInt32, IpMask: UInt32, IfIndex: UInt32, NTEContext: POINTER(UInt32), NTEInstance: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIPAddress(NTEContext: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkParams(pFixedInfo: POINTER(Windows.Win32.NetworkManagement.IpHelper.FIXED_INFO_W2KSP1_head), pOutBufLen: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetAdaptersInfo(AdapterInfo: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INFO_head), SizePointer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetAdapterOrderMap() -> POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ORDER_MAP_head): ...
@winfunctype('IPHLPAPI.dll')
def GetAdaptersAddresses(Family: UInt32, Flags: Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS, Reserved: c_void_p, AdapterAddresses: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_LH_head), SizePointer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetPerAdapterInfo(IfIndex: UInt32, pPerAdapterInfo: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_PER_ADAPTER_INFO_W2KSP1_head), pOutBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceActiveTimestampCapabilities(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), TimestampCapabilites: POINTER(Windows.Win32.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceSupportedTimestampCapabilities(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), TimestampCapabilites: POINTER(Windows.Win32.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CaptureInterfaceHardwareCrossTimestamp(InterfaceLuid: POINTER(Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH_head), CrossTimestamp: POINTER(Windows.Win32.NetworkManagement.IpHelper.INTERFACE_HARDWARE_CROSSTIMESTAMP_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def RegisterInterfaceTimestampConfigChange(Callback: Windows.Win32.NetworkManagement.IpHelper.PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK, CallerContext: c_void_p, NotificationHandle: POINTER(Windows.Win32.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def UnregisterInterfaceTimestampConfigChange(NotificationHandle: Windows.Win32.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def IpReleaseAddress(AdapterInfo: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IpRenewAddress(AdapterInfo: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SendARP(DestIP: UInt32, SrcIP: UInt32, pMacAddr: c_void_p, PhyAddrLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetRTTAndHopCount(DestIpAddress: UInt32, HopCount: POINTER(UInt32), MaxHops: UInt32, RTT: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IPHLPAPI.dll')
def GetFriendlyIfIndex(IfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def EnableRouter(pHandle: POINTER(Windows.Win32.Foundation.HANDLE), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def UnenableRouter(pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpdwEnableCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DisableMediaSense(pHandle: POINTER(Windows.Win32.Foundation.HANDLE), pOverLapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def RestoreMediaSense(pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpdwEnableCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpErrorString(ErrorCode: UInt32, Buffer: Windows.Win32.Foundation.PWSTR, Size: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def ResolveNeighbor(NetworkAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head), PhysicalAddress: c_void_p, PhysicalAddressLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreatePersistentTcpPortReservation(StartPort: UInt16, NumberOfPorts: UInt16, Token: POINTER(UInt64)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreatePersistentUdpPortReservation(StartPort: UInt16, NumberOfPorts: UInt16, Token: POINTER(UInt64)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeletePersistentTcpPortReservation(StartPort: UInt16, NumberOfPorts: UInt16) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeletePersistentUdpPortReservation(StartPort: UInt16, NumberOfPorts: UInt16) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def LookupPersistentTcpPortReservation(StartPort: UInt16, NumberOfPorts: UInt16, Token: POINTER(UInt64)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def LookupPersistentUdpPortReservation(StartPort: UInt16, NumberOfPorts: UInt16, Token: POINTER(UInt64)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfCreateInterface(dwName: UInt32, inAction: Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION, outAction: Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION, bUseLog: Windows.Win32.Foundation.BOOL, bMustBeUnique: Windows.Win32.Foundation.BOOL, ppInterface: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfDeleteInterface(pInterface: c_void_p) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfAddFiltersToInterface(ih: c_void_p, cInFilters: UInt32, pfiltIn: POINTER(Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head), cOutFilters: UInt32, pfiltOut: POINTER(Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head), pfHandle: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRemoveFiltersFromInterface(ih: c_void_p, cInFilters: UInt32, pfiltIn: POINTER(Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head), cOutFilters: UInt32, pfiltOut: POINTER(Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRemoveFilterHandles(pInterface: c_void_p, cFilters: UInt32, pvHandles: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfUnBindInterface(pInterface: c_void_p) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfBindInterfaceToIndex(pInterface: c_void_p, dwIndex: UInt32, pfatLinkType: Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE, LinkIPAddress: c_char_p_no) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfBindInterfaceToIPAddress(pInterface: c_void_p, pfatType: Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE, IPAddress: c_char_p_no) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRebindFilters(pInterface: c_void_p, pLateBindInfo: POINTER(Windows.Win32.NetworkManagement.IpHelper.PF_LATEBIND_INFO_head)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfAddGlobalFilterToInterface(pInterface: c_void_p, gfFilter: Windows.Win32.NetworkManagement.IpHelper.GLOBAL_FILTER) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRemoveGlobalFilterFromInterface(pInterface: c_void_p, gfFilter: Windows.Win32.NetworkManagement.IpHelper.GLOBAL_FILTER) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfMakeLog(hEvent: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfSetLogBuffer(pbBuffer: c_char_p_no, dwSize: UInt32, dwThreshold: UInt32, dwEntries: UInt32, pdwLoggedEntries: POINTER(UInt32), pdwLostEntries: POINTER(UInt32), pdwSizeUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfDeleteLog() -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfGetInterfaceStatistics(pInterface: c_void_p, ppfStats: POINTER(Windows.Win32.NetworkManagement.IpHelper.PF_INTERFACE_STATS_head), pdwBufferSize: POINTER(UInt32), fResetCounters: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfTestPacket(pInInterface: c_void_p, pOutInterface: c_void_p, cBytes: UInt32, pbPacket: c_char_p_no, ppAction: POINTER(Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION)) -> UInt32: ...
class DNS_DOH_SERVER_SETTINGS(Structure):
    Template: Windows.Win32.Foundation.PWSTR
    Flags: UInt64
class DNS_INTERFACE_SETTINGS(Structure):
    Version: UInt32
    Flags: UInt64
    Domain: Windows.Win32.Foundation.PWSTR
    NameServer: Windows.Win32.Foundation.PWSTR
    SearchList: Windows.Win32.Foundation.PWSTR
    RegistrationEnabled: UInt32
    RegisterAdapterName: UInt32
    EnableLLMNR: UInt32
    QueryAdapterName: UInt32
    ProfileNameServer: Windows.Win32.Foundation.PWSTR
class DNS_INTERFACE_SETTINGS3(Structure):
    Version: UInt32
    Flags: UInt64
    Domain: Windows.Win32.Foundation.PWSTR
    NameServer: Windows.Win32.Foundation.PWSTR
    SearchList: Windows.Win32.Foundation.PWSTR
    RegistrationEnabled: UInt32
    RegisterAdapterName: UInt32
    EnableLLMNR: UInt32
    QueryAdapterName: UInt32
    ProfileNameServer: Windows.Win32.Foundation.PWSTR
    DisableUnconstrainedQueries: UInt32
    SupplementalSearchList: Windows.Win32.Foundation.PWSTR
    cServerProperties: UInt32
    ServerProperties: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_head)
    cProfileServerProperties: UInt32
    ProfileServerProperties: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_head)
class DNS_INTERFACE_SETTINGS_EX(Structure):
    SettingsV1: Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS
    DisableUnconstrainedQueries: UInt32
    SupplementalSearchList: Windows.Win32.Foundation.PWSTR
class DNS_SERVER_PROPERTY(Structure):
    Version: UInt32
    ServerIndex: UInt32
    Type: Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPE
    Property: Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPES
DNS_SERVER_PROPERTY_TYPE = Int32
DNS_SERVER_PROPERTY_TYPE_DnsServerInvalidProperty: DNS_SERVER_PROPERTY_TYPE = 0
DNS_SERVER_PROPERTY_TYPE_DnsServerDohProperty: DNS_SERVER_PROPERTY_TYPE = 1
class DNS_SERVER_PROPERTY_TYPES(Union):
    DohSettings: POINTER(Windows.Win32.NetworkManagement.IpHelper.DNS_DOH_SERVER_SETTINGS_head)
class DNS_SETTINGS(Structure):
    Version: UInt32
    Flags: UInt64
    Hostname: Windows.Win32.Foundation.PWSTR
    Domain: Windows.Win32.Foundation.PWSTR
    SearchList: Windows.Win32.Foundation.PWSTR
class DNS_SETTINGS2(Structure):
    Version: UInt32
    Flags: UInt64
    Hostname: Windows.Win32.Foundation.PWSTR
    Domain: Windows.Win32.Foundation.PWSTR
    SearchList: Windows.Win32.Foundation.PWSTR
    SettingFlags: UInt64
class FIXED_INFO_W2KSP1(Structure):
    HostName: Windows.Win32.Foundation.CHAR * 132
    DomainName: Windows.Win32.Foundation.CHAR * 132
    CurrentDnsServer: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING_head)
    DnsServerList: Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    NodeType: UInt32
    ScopeId: Windows.Win32.Foundation.CHAR * 260
    EnableRouting: UInt32
    EnableProxy: UInt32
    EnableDns: UInt32
GET_ADAPTERS_ADDRESSES_FLAGS = UInt32
GAA_FLAG_SKIP_UNICAST: GET_ADAPTERS_ADDRESSES_FLAGS = 1
GAA_FLAG_SKIP_ANYCAST: GET_ADAPTERS_ADDRESSES_FLAGS = 2
GAA_FLAG_SKIP_MULTICAST: GET_ADAPTERS_ADDRESSES_FLAGS = 4
GAA_FLAG_SKIP_DNS_SERVER: GET_ADAPTERS_ADDRESSES_FLAGS = 8
GAA_FLAG_INCLUDE_PREFIX: GET_ADAPTERS_ADDRESSES_FLAGS = 16
GAA_FLAG_SKIP_FRIENDLY_NAME: GET_ADAPTERS_ADDRESSES_FLAGS = 32
GAA_FLAG_INCLUDE_WINS_INFO: GET_ADAPTERS_ADDRESSES_FLAGS = 64
GAA_FLAG_INCLUDE_GATEWAYS: GET_ADAPTERS_ADDRESSES_FLAGS = 128
GAA_FLAG_INCLUDE_ALL_INTERFACES: GET_ADAPTERS_ADDRESSES_FLAGS = 256
GAA_FLAG_INCLUDE_ALL_COMPARTMENTS: GET_ADAPTERS_ADDRESSES_FLAGS = 512
GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER: GET_ADAPTERS_ADDRESSES_FLAGS = 1024
GLOBAL_FILTER = Int32
GF_FRAGMENTS: GLOBAL_FILTER = 2
GF_STRONGHOST: GLOBAL_FILTER = 8
GF_FRAGCACHE: GLOBAL_FILTER = 9
HIFTIMESTAMPCHANGE = IntPtr
ICMP4_TYPE = Int32
ICMP4_ECHO_REPLY: ICMP4_TYPE = 0
ICMP4_DST_UNREACH: ICMP4_TYPE = 3
ICMP4_SOURCE_QUENCH: ICMP4_TYPE = 4
ICMP4_REDIRECT: ICMP4_TYPE = 5
ICMP4_ECHO_REQUEST: ICMP4_TYPE = 8
ICMP4_ROUTER_ADVERT: ICMP4_TYPE = 9
ICMP4_ROUTER_SOLICIT: ICMP4_TYPE = 10
ICMP4_TIME_EXCEEDED: ICMP4_TYPE = 11
ICMP4_PARAM_PROB: ICMP4_TYPE = 12
ICMP4_TIMESTAMP_REQUEST: ICMP4_TYPE = 13
ICMP4_TIMESTAMP_REPLY: ICMP4_TYPE = 14
ICMP4_MASK_REQUEST: ICMP4_TYPE = 17
ICMP4_MASK_REPLY: ICMP4_TYPE = 18
ICMP6_TYPE = Int32
ICMP6_DST_UNREACH: ICMP6_TYPE = 1
ICMP6_PACKET_TOO_BIG: ICMP6_TYPE = 2
ICMP6_TIME_EXCEEDED: ICMP6_TYPE = 3
ICMP6_PARAM_PROB: ICMP6_TYPE = 4
ICMP6_ECHO_REQUEST: ICMP6_TYPE = 128
ICMP6_ECHO_REPLY: ICMP6_TYPE = 129
ICMP6_MEMBERSHIP_QUERY: ICMP6_TYPE = 130
ICMP6_MEMBERSHIP_REPORT: ICMP6_TYPE = 131
ICMP6_MEMBERSHIP_REDUCTION: ICMP6_TYPE = 132
ND_ROUTER_SOLICIT: ICMP6_TYPE = 133
ND_ROUTER_ADVERT: ICMP6_TYPE = 134
ND_NEIGHBOR_SOLICIT: ICMP6_TYPE = 135
ND_NEIGHBOR_ADVERT: ICMP6_TYPE = 136
ND_REDIRECT: ICMP6_TYPE = 137
ICMP6_V2_MEMBERSHIP_REPORT: ICMP6_TYPE = 143
class ICMPV6_ECHO_REPLY_LH(Structure):
    Address: Windows.Win32.NetworkManagement.IpHelper.IPV6_ADDRESS_EX
    Status: UInt32
    RoundTripTime: UInt32
class ICMP_ECHO_REPLY(Structure):
    Address: UInt32
    Status: UInt32
    RoundTripTime: UInt32
    DataSize: UInt16
    Reserved: UInt16
    Data: c_void_p
    Options: Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION
if ARCH in 'X64,ARM64':
    class ICMP_ECHO_REPLY32(Structure):
        Address: UInt32
        Status: UInt32
        RoundTripTime: UInt32
        DataSize: UInt16
        Reserved: UInt16
        Data: c_void_p
        Options: Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION32
IF_ACCESS_TYPE = Int32
IF_ACCESS_LOOPBACK: IF_ACCESS_TYPE = 1
IF_ACCESS_BROADCAST: IF_ACCESS_TYPE = 2
IF_ACCESS_POINT_TO_POINT: IF_ACCESS_TYPE = 3
IF_ACCESS_POINTTOPOINT: IF_ACCESS_TYPE = 3
IF_ACCESS_POINT_TO_MULTI_POINT: IF_ACCESS_TYPE = 4
IF_ACCESS_POINTTOMULTIPOINT: IF_ACCESS_TYPE = 4
class INTERFACE_HARDWARE_CROSSTIMESTAMP(Structure):
    SystemTimestamp1: UInt64
    HardwareClockTimestamp: UInt64
    SystemTimestamp2: UInt64
class INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES(Structure):
    PtpV2OverUdpIPv4EventMessageReceive: Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv4AllMessageReceive: Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv4EventMessageTransmit: Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv4AllMessageTransmit: Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6EventMessageReceive: Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6AllMessageReceive: Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6EventMessageTransmit: Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6AllMessageTransmit: Windows.Win32.Foundation.BOOLEAN
    AllReceive: Windows.Win32.Foundation.BOOLEAN
    AllTransmit: Windows.Win32.Foundation.BOOLEAN
    TaggedTransmit: Windows.Win32.Foundation.BOOLEAN
class INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES(Structure):
    AllReceive: Windows.Win32.Foundation.BOOLEAN
    AllTransmit: Windows.Win32.Foundation.BOOLEAN
    TaggedTransmit: Windows.Win32.Foundation.BOOLEAN
class INTERFACE_TIMESTAMP_CAPABILITIES(Structure):
    HardwareClockFrequencyHz: UInt64
    SupportsCrossTimestamp: Windows.Win32.Foundation.BOOLEAN
    HardwareCapabilities: Windows.Win32.NetworkManagement.IpHelper.INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES
    SoftwareCapabilities: Windows.Win32.NetworkManagement.IpHelper.INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES
INTERNAL_IF_OPER_STATUS = Int32
IF_OPER_STATUS_NON_OPERATIONAL: INTERNAL_IF_OPER_STATUS = 0
IF_OPER_STATUS_UNREACHABLE: INTERNAL_IF_OPER_STATUS = 1
IF_OPER_STATUS_DISCONNECTED: INTERNAL_IF_OPER_STATUS = 2
IF_OPER_STATUS_CONNECTING: INTERNAL_IF_OPER_STATUS = 3
IF_OPER_STATUS_CONNECTED: INTERNAL_IF_OPER_STATUS = 4
IF_OPER_STATUS_OPERATIONAL: INTERNAL_IF_OPER_STATUS = 5
class IPV6_ADDRESS_EX(Structure):
    sin6_port: UInt16
    sin6_flowinfo: UInt32
    sin6_addr: UInt16 * 8
    sin6_scope_id: UInt32
    _pack_ = 1
class IP_ADAPTER_ADDRESSES_LH(Structure):
    Anonymous1: _Anonymous1_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_LH_head)
    AdapterName: Windows.Win32.Foundation.PSTR
    FirstUnicastAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_LH_head)
    FirstAnycastAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP_head)
    FirstMulticastAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP_head)
    FirstDnsServerAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head)
    DnsSuffix: Windows.Win32.Foundation.PWSTR
    Description: Windows.Win32.Foundation.PWSTR
    FriendlyName: Windows.Win32.Foundation.PWSTR
    PhysicalAddress: Byte * 8
    PhysicalAddressLength: UInt32
    Anonymous2: _Anonymous2_e__Union
    Mtu: UInt32
    IfType: UInt32
    OperStatus: Windows.Win32.NetworkManagement.Ndis.IF_OPER_STATUS
    Ipv6IfIndex: UInt32
    ZoneIndices: UInt32 * 16
    FirstPrefix: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP_head)
    TransmitLinkSpeed: UInt64
    ReceiveLinkSpeed: UInt64
    FirstWinsServerAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_WINS_SERVER_ADDRESS_LH_head)
    FirstGatewayAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_GATEWAY_ADDRESS_LH_head)
    Ipv4Metric: UInt32
    Ipv6Metric: UInt32
    Luid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    Dhcpv4Server: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    CompartmentId: UInt32
    NetworkGuid: Guid
    ConnectionType: Windows.Win32.NetworkManagement.Ndis.NET_IF_CONNECTION_TYPE
    TunnelType: Windows.Win32.NetworkManagement.Ndis.TUNNEL_TYPE
    Dhcpv6Server: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    Dhcpv6ClientDuid: Byte * 130
    Dhcpv6ClientDuidLength: UInt32
    Dhcpv6Iaid: UInt32
    FirstDnsSuffix: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SUFFIX_head)
    class _Anonymous1_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            IfIndex: UInt32
    class _Anonymous2_e__Union(Union):
        Flags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class IP_ADAPTER_ADDRESSES_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_XP_head)
    AdapterName: Windows.Win32.Foundation.PSTR
    FirstUnicastAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_XP_head)
    FirstAnycastAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP_head)
    FirstMulticastAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP_head)
    FirstDnsServerAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head)
    DnsSuffix: Windows.Win32.Foundation.PWSTR
    Description: Windows.Win32.Foundation.PWSTR
    FriendlyName: Windows.Win32.Foundation.PWSTR
    PhysicalAddress: Byte * 8
    PhysicalAddressLength: UInt32
    Flags: UInt32
    Mtu: UInt32
    IfType: UInt32
    OperStatus: Windows.Win32.NetworkManagement.Ndis.IF_OPER_STATUS
    Ipv6IfIndex: UInt32
    ZoneIndices: UInt32 * 16
    FirstPrefix: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP_head)
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            IfIndex: UInt32
class IP_ADAPTER_ANYCAST_ADDRESS_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Flags: UInt32
class IP_ADAPTER_DNS_SERVER_ADDRESS_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Reserved: UInt32
class IP_ADAPTER_DNS_SUFFIX(Structure):
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SUFFIX_head)
    String: Char * 256
class IP_ADAPTER_GATEWAY_ADDRESS_LH(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_GATEWAY_ADDRESS_LH_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Reserved: UInt32
class IP_ADAPTER_INDEX_MAP(Structure):
    Index: UInt32
    Name: Char * 128
class IP_ADAPTER_INFO(Structure):
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INFO_head)
    ComboIndex: UInt32
    AdapterName: Windows.Win32.Foundation.CHAR * 260
    Description: Windows.Win32.Foundation.CHAR * 132
    AddressLength: UInt32
    Address: Byte * 8
    Index: UInt32
    Type: UInt32
    DhcpEnabled: UInt32
    CurrentIpAddress: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING_head)
    IpAddressList: Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    GatewayList: Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    DhcpServer: Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    HaveWins: Windows.Win32.Foundation.BOOL
    PrimaryWinsServer: Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    SecondaryWinsServer: Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    LeaseObtained: Int64
    LeaseExpires: Int64
class IP_ADAPTER_MULTICAST_ADDRESS_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Flags: UInt32
class IP_ADAPTER_ORDER_MAP(Structure):
    NumAdapters: UInt32
    AdapterOrder: UInt32 * 1
class IP_ADAPTER_PREFIX_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    PrefixLength: UInt32
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Flags: UInt32
class IP_ADAPTER_UNICAST_ADDRESS_LH(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_LH_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    PrefixOrigin: Windows.Win32.Networking.WinSock.NL_PREFIX_ORIGIN
    SuffixOrigin: Windows.Win32.Networking.WinSock.NL_SUFFIX_ORIGIN
    DadState: Windows.Win32.Networking.WinSock.NL_DAD_STATE
    ValidLifetime: UInt32
    PreferredLifetime: UInt32
    LeaseLifetime: UInt32
    OnLinkPrefixLength: Byte
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Flags: UInt32
class IP_ADAPTER_UNICAST_ADDRESS_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_XP_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    PrefixOrigin: Windows.Win32.Networking.WinSock.NL_PREFIX_ORIGIN
    SuffixOrigin: Windows.Win32.Networking.WinSock.NL_SUFFIX_ORIGIN
    DadState: Windows.Win32.Networking.WinSock.NL_DAD_STATE
    ValidLifetime: UInt32
    PreferredLifetime: UInt32
    LeaseLifetime: UInt32
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Flags: UInt32
class IP_ADAPTER_WINS_SERVER_ADDRESS_LH(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_WINS_SERVER_ADDRESS_LH_head)
    Address: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Reserved: UInt32
class IP_ADDRESS_PREFIX(Structure):
    Prefix: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    PrefixLength: Byte
class IP_ADDRESS_STRING(Structure):
    String: Windows.Win32.Foundation.CHAR * 16
class IP_ADDR_STRING(Structure):
    Next: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING_head)
    IpAddress: Windows.Win32.NetworkManagement.IpHelper.IP_ADDRESS_STRING
    IpMask: Windows.Win32.NetworkManagement.IpHelper.IP_ADDRESS_STRING
    Context: UInt32
class IP_INTERFACE_INFO(Structure):
    NumAdapters: Int32
    Adapter: Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP * 1
class IP_INTERFACE_NAME_INFO_W2KSP1(Structure):
    Index: UInt32
    MediaType: UInt32
    ConnectionType: Byte
    AccessType: Byte
    DeviceGuid: Guid
    InterfaceGuid: Guid
class IP_MCAST_COUNTER_INFO(Structure):
    InMcastOctets: UInt64
    OutMcastOctets: UInt64
    InMcastPkts: UInt64
    OutMcastPkts: UInt64
class IP_OPTION_INFORMATION(Structure):
    Ttl: Byte
    Tos: Byte
    Flags: Byte
    OptionsSize: Byte
    OptionsData: c_char_p_no
if ARCH in 'X64,ARM64':
    class IP_OPTION_INFORMATION32(Structure):
        Ttl: Byte
        Tos: Byte
        Flags: Byte
        OptionsSize: Byte
        OptionsData: c_char_p_no
class IP_PER_ADAPTER_INFO_W2KSP1(Structure):
    AutoconfigEnabled: UInt32
    AutoconfigActive: UInt32
    CurrentDnsServer: POINTER(Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING_head)
    DnsServerList: Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
class IP_UNIDIRECTIONAL_ADAPTER_ADDRESS(Structure):
    NumAdapters: UInt32
    Address: UInt32 * 1
IcmpHandle = IntPtr
class MIBICMPINFO(Structure):
    icmpInStats: Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS
    icmpOutStats: Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS
class MIBICMPSTATS(Structure):
    dwMsgs: UInt32
    dwErrors: UInt32
    dwDestUnreachs: UInt32
    dwTimeExcds: UInt32
    dwParmProbs: UInt32
    dwSrcQuenchs: UInt32
    dwRedirects: UInt32
    dwEchos: UInt32
    dwEchoReps: UInt32
    dwTimestamps: UInt32
    dwTimestampReps: UInt32
    dwAddrMasks: UInt32
    dwAddrMaskReps: UInt32
class MIBICMPSTATS_EX_XPSP1(Structure):
    dwMsgs: UInt32
    dwErrors: UInt32
    rgdwTypeCount: UInt32 * 256
class MIB_ANYCASTIPADDRESS_ROW(Structure):
    Address: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    ScopeId: Windows.Win32.Networking.WinSock.SCOPE_ID
class MIB_ANYCASTIPADDRESS_TABLE(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW * 1
class MIB_BEST_IF(Structure):
    dwDestAddr: UInt32
    dwIfIndex: UInt32
class MIB_BOUNDARYROW(Structure):
    dwGroupAddress: UInt32
    dwGroupMask: UInt32
class MIB_ICMP(Structure):
    stats: Windows.Win32.NetworkManagement.IpHelper.MIBICMPINFO
class MIB_ICMP_EX_XPSP1(Structure):
    icmpInStats: Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS_EX_XPSP1
    icmpOutStats: Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS_EX_XPSP1
class MIB_IFNUMBER(Structure):
    dwValue: UInt32
class MIB_IFROW(Structure):
    wszName: Char * 256
    dwIndex: UInt32
    dwType: UInt32
    dwMtu: UInt32
    dwSpeed: UInt32
    dwPhysAddrLen: UInt32
    bPhysAddr: Byte * 8
    dwAdminStatus: UInt32
    dwOperStatus: Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS
    dwLastChange: UInt32
    dwInOctets: UInt32
    dwInUcastPkts: UInt32
    dwInNUcastPkts: UInt32
    dwInDiscards: UInt32
    dwInErrors: UInt32
    dwInUnknownProtos: UInt32
    dwOutOctets: UInt32
    dwOutUcastPkts: UInt32
    dwOutNUcastPkts: UInt32
    dwOutDiscards: UInt32
    dwOutErrors: UInt32
    dwOutQLen: UInt32
    dwDescrLen: UInt32
    bDescr: Byte * 256
class MIB_IFSTACK_ROW(Structure):
    HigherLayerInterfaceIndex: UInt32
    LowerLayerInterfaceIndex: UInt32
class MIB_IFSTACK_TABLE(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_IFSTACK_ROW * 1
class MIB_IFSTATUS(Structure):
    dwIfIndex: UInt32
    dwAdminStatus: UInt32
    dwOperationalStatus: UInt32
    bMHbeatActive: Windows.Win32.Foundation.BOOL
    bMHbeatAlive: Windows.Win32.Foundation.BOOL
class MIB_IFTABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IFROW * 1
MIB_IF_ENTRY_LEVEL = Int32
MIB_IF_ENTRY_LEVEL_MibIfEntryNormal: MIB_IF_ENTRY_LEVEL = 0
MIB_IF_ENTRY_LEVEL_MibIfEntryNormalWithoutStatistics: MIB_IF_ENTRY_LEVEL = 2
class MIB_IF_ROW2(Structure):
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    InterfaceGuid: Guid
    Alias: Char * 257
    Description: Char * 257
    PhysicalAddressLength: UInt32
    PhysicalAddress: Byte * 32
    PermanentPhysicalAddress: Byte * 32
    Mtu: UInt32
    Type: UInt32
    TunnelType: Windows.Win32.NetworkManagement.Ndis.TUNNEL_TYPE
    MediaType: Windows.Win32.NetworkManagement.Ndis.NDIS_MEDIUM
    PhysicalMediumType: Windows.Win32.NetworkManagement.Ndis.NDIS_PHYSICAL_MEDIUM
    AccessType: Windows.Win32.NetworkManagement.Ndis.NET_IF_ACCESS_TYPE
    DirectionType: Windows.Win32.NetworkManagement.Ndis.NET_IF_DIRECTION_TYPE
    InterfaceAndOperStatusFlags: _InterfaceAndOperStatusFlags_e__Struct
    OperStatus: Windows.Win32.NetworkManagement.Ndis.IF_OPER_STATUS
    AdminStatus: Windows.Win32.NetworkManagement.Ndis.NET_IF_ADMIN_STATUS
    MediaConnectState: Windows.Win32.NetworkManagement.Ndis.NET_IF_MEDIA_CONNECT_STATE
    NetworkGuid: Guid
    ConnectionType: Windows.Win32.NetworkManagement.Ndis.NET_IF_CONNECTION_TYPE
    TransmitLinkSpeed: UInt64
    ReceiveLinkSpeed: UInt64
    InOctets: UInt64
    InUcastPkts: UInt64
    InNUcastPkts: UInt64
    InDiscards: UInt64
    InErrors: UInt64
    InUnknownProtos: UInt64
    InUcastOctets: UInt64
    InMulticastOctets: UInt64
    InBroadcastOctets: UInt64
    OutOctets: UInt64
    OutUcastPkts: UInt64
    OutNUcastPkts: UInt64
    OutDiscards: UInt64
    OutErrors: UInt64
    OutUcastOctets: UInt64
    OutMulticastOctets: UInt64
    OutBroadcastOctets: UInt64
    OutQLen: UInt64
    class _InterfaceAndOperStatusFlags_e__Struct(Structure):
        _bitfield: Byte
class MIB_IF_TABLE2(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ROW2 * 1
MIB_IF_TABLE_LEVEL = Int32
MIB_IF_TABLE_LEVEL_MibIfTableNormal: MIB_IF_TABLE_LEVEL = 0
MIB_IF_TABLE_LEVEL_MibIfTableRaw: MIB_IF_TABLE_LEVEL = 1
MIB_IF_TABLE_LEVEL_MibIfTableNormalWithoutStatistics: MIB_IF_TABLE_LEVEL = 2
class MIB_INVERTEDIFSTACK_ROW(Structure):
    LowerLayerInterfaceIndex: UInt32
    HigherLayerInterfaceIndex: UInt32
class MIB_INVERTEDIFSTACK_TABLE(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_ROW * 1
class MIB_IPADDRROW_W2K(Structure):
    dwAddr: UInt32
    dwIndex: UInt32
    dwMask: UInt32
    dwBCastAddr: UInt32
    dwReasmSize: UInt32
    unused1: UInt16
    unused2: UInt16
class MIB_IPADDRROW_XP(Structure):
    dwAddr: UInt32
    dwIndex: UInt32
    dwMask: UInt32
    dwBCastAddr: UInt32
    dwReasmSize: UInt32
    unused1: UInt16
    wType: UInt16
class MIB_IPADDRTABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPADDRROW_XP * 1
class MIB_IPDESTROW(Structure):
    ForwardRow: Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW
    dwForwardPreference: UInt32
    dwForwardViewSet: UInt32
class MIB_IPDESTTABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPDESTROW * 1
class MIB_IPFORWARDNUMBER(Structure):
    dwValue: UInt32
class MIB_IPFORWARDROW(Structure):
    dwForwardDest: UInt32
    dwForwardMask: UInt32
    dwForwardPolicy: UInt32
    dwForwardNextHop: UInt32
    dwForwardIfIndex: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    dwForwardAge: UInt32
    dwForwardNextHopAS: UInt32
    dwForwardMetric1: UInt32
    dwForwardMetric2: UInt32
    dwForwardMetric3: UInt32
    dwForwardMetric4: UInt32
    dwForwardMetric5: UInt32
    class _Anonymous1_e__Union(Union):
        dwForwardType: UInt32
        ForwardType: Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TYPE
    class _Anonymous2_e__Union(Union):
        dwForwardProto: UInt32
        ForwardProto: Windows.Win32.Networking.WinSock.NL_ROUTE_PROTOCOL
class MIB_IPFORWARDTABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW * 1
class MIB_IPFORWARD_ROW2(Structure):
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    DestinationPrefix: Windows.Win32.NetworkManagement.IpHelper.IP_ADDRESS_PREFIX
    NextHop: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    SitePrefixLength: Byte
    ValidLifetime: UInt32
    PreferredLifetime: UInt32
    Metric: UInt32
    Protocol: Windows.Win32.Networking.WinSock.NL_ROUTE_PROTOCOL
    Loopback: Windows.Win32.Foundation.BOOLEAN
    AutoconfigureAddress: Windows.Win32.Foundation.BOOLEAN
    Publish: Windows.Win32.Foundation.BOOLEAN
    Immortal: Windows.Win32.Foundation.BOOLEAN
    Age: UInt32
    Origin: Windows.Win32.Networking.WinSock.NL_ROUTE_ORIGIN
class MIB_IPFORWARD_TABLE2(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2 * 1
MIB_IPFORWARD_TYPE = Int32
MIB_IPROUTE_TYPE_OTHER: MIB_IPFORWARD_TYPE = 1
MIB_IPROUTE_TYPE_INVALID: MIB_IPFORWARD_TYPE = 2
MIB_IPROUTE_TYPE_DIRECT: MIB_IPFORWARD_TYPE = 3
MIB_IPROUTE_TYPE_INDIRECT: MIB_IPFORWARD_TYPE = 4
class MIB_IPINTERFACE_ROW(Structure):
    Family: Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    MaxReassemblySize: UInt32
    InterfaceIdentifier: UInt64
    MinRouterAdvertisementInterval: UInt32
    MaxRouterAdvertisementInterval: UInt32
    AdvertisingEnabled: Windows.Win32.Foundation.BOOLEAN
    ForwardingEnabled: Windows.Win32.Foundation.BOOLEAN
    WeakHostSend: Windows.Win32.Foundation.BOOLEAN
    WeakHostReceive: Windows.Win32.Foundation.BOOLEAN
    UseAutomaticMetric: Windows.Win32.Foundation.BOOLEAN
    UseNeighborUnreachabilityDetection: Windows.Win32.Foundation.BOOLEAN
    ManagedAddressConfigurationSupported: Windows.Win32.Foundation.BOOLEAN
    OtherStatefulConfigurationSupported: Windows.Win32.Foundation.BOOLEAN
    AdvertiseDefaultRoute: Windows.Win32.Foundation.BOOLEAN
    RouterDiscoveryBehavior: Windows.Win32.Networking.WinSock.NL_ROUTER_DISCOVERY_BEHAVIOR
    DadTransmits: UInt32
    BaseReachableTime: UInt32
    RetransmitTime: UInt32
    PathMtuDiscoveryTimeout: UInt32
    LinkLocalAddressBehavior: Windows.Win32.Networking.WinSock.NL_LINK_LOCAL_ADDRESS_BEHAVIOR
    LinkLocalAddressTimeout: UInt32
    ZoneIndices: UInt32 * 16
    SitePrefixLength: UInt32
    Metric: UInt32
    NlMtu: UInt32
    Connected: Windows.Win32.Foundation.BOOLEAN
    SupportsWakeUpPatterns: Windows.Win32.Foundation.BOOLEAN
    SupportsNeighborDiscovery: Windows.Win32.Foundation.BOOLEAN
    SupportsRouterDiscovery: Windows.Win32.Foundation.BOOLEAN
    ReachableTime: UInt32
    TransmitOffload: Windows.Win32.Networking.WinSock.NL_INTERFACE_OFFLOAD_ROD
    ReceiveOffload: Windows.Win32.Networking.WinSock.NL_INTERFACE_OFFLOAD_ROD
    DisableDefaultRoutes: Windows.Win32.Foundation.BOOLEAN
class MIB_IPINTERFACE_TABLE(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW * 1
class MIB_IPMCAST_BOUNDARY(Structure):
    dwIfIndex: UInt32
    dwGroupAddress: UInt32
    dwGroupMask: UInt32
    dwStatus: UInt32
class MIB_IPMCAST_BOUNDARY_TABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_BOUNDARY * 1
class MIB_IPMCAST_GLOBAL(Structure):
    dwEnable: UInt32
class MIB_IPMCAST_IF_ENTRY(Structure):
    dwIfIndex: UInt32
    dwTtl: UInt32
    dwProtocol: UInt32
    dwRateLimit: UInt32
    ulInMcastOctets: UInt32
    ulOutMcastOctets: UInt32
class MIB_IPMCAST_IF_TABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_IF_ENTRY * 1
class MIB_IPMCAST_MFE(Structure):
    dwGroup: UInt32
    dwSource: UInt32
    dwSrcMask: UInt32
    dwUpStrmNgbr: UInt32
    dwInIfIndex: UInt32
    dwInIfProtocol: UInt32
    dwRouteProtocol: UInt32
    dwRouteNetwork: UInt32
    dwRouteMask: UInt32
    ulUpTime: UInt32
    ulExpiryTime: UInt32
    ulTimeOut: UInt32
    ulNumOutIf: UInt32
    fFlags: UInt32
    dwReserved: UInt32
    rgmioOutInfo: Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_XP * 1
class MIB_IPMCAST_MFE_STATS(Structure):
    dwGroup: UInt32
    dwSource: UInt32
    dwSrcMask: UInt32
    dwUpStrmNgbr: UInt32
    dwInIfIndex: UInt32
    dwInIfProtocol: UInt32
    dwRouteProtocol: UInt32
    dwRouteNetwork: UInt32
    dwRouteMask: UInt32
    ulUpTime: UInt32
    ulExpiryTime: UInt32
    ulNumOutIf: UInt32
    ulInPkts: UInt32
    ulInOctets: UInt32
    ulPktsDifferentIf: UInt32
    ulQueueOverflow: UInt32
    rgmiosOutStats: Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_LH * 1
class MIB_IPMCAST_MFE_STATS_EX_XP(Structure):
    dwGroup: UInt32
    dwSource: UInt32
    dwSrcMask: UInt32
    dwUpStrmNgbr: UInt32
    dwInIfIndex: UInt32
    dwInIfProtocol: UInt32
    dwRouteProtocol: UInt32
    dwRouteNetwork: UInt32
    dwRouteMask: UInt32
    ulUpTime: UInt32
    ulExpiryTime: UInt32
    ulNumOutIf: UInt32
    ulInPkts: UInt32
    ulInOctets: UInt32
    ulPktsDifferentIf: UInt32
    ulQueueOverflow: UInt32
    ulUninitMfe: UInt32
    ulNegativeMfe: UInt32
    ulInDiscards: UInt32
    ulInHdrErrors: UInt32
    ulTotalOutPackets: UInt32
    rgmiosOutStats: Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_LH * 1
class MIB_IPMCAST_OIF_STATS_LH(Structure):
    dwOutIfIndex: UInt32
    dwNextHopAddr: UInt32
    dwDialContext: UInt32
    ulTtlTooLow: UInt32
    ulFragNeeded: UInt32
    ulOutPackets: UInt32
    ulOutDiscards: UInt32
class MIB_IPMCAST_OIF_STATS_W2K(Structure):
    dwOutIfIndex: UInt32
    dwNextHopAddr: UInt32
    pvDialContext: c_void_p
    ulTtlTooLow: UInt32
    ulFragNeeded: UInt32
    ulOutPackets: UInt32
    ulOutDiscards: UInt32
class MIB_IPMCAST_OIF_W2K(Structure):
    dwOutIfIndex: UInt32
    dwNextHopAddr: UInt32
    pvReserved: c_void_p
    dwReserved: UInt32
class MIB_IPMCAST_OIF_XP(Structure):
    dwOutIfIndex: UInt32
    dwNextHopAddr: UInt32
    dwReserved: UInt32
    dwReserved1: UInt32
class MIB_IPMCAST_SCOPE(Structure):
    dwGroupAddress: UInt32
    dwGroupMask: UInt32
    snNameBuffer: UInt16 * 256
    dwStatus: UInt32
class MIB_IPNETROW_LH(Structure):
    dwIndex: UInt32
    dwPhysAddrLen: UInt32
    bPhysAddr: Byte * 8
    dwAddr: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwType: UInt32
        Type: Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TYPE
class MIB_IPNETROW_W2K(Structure):
    dwIndex: UInt32
    dwPhysAddrLen: UInt32
    bPhysAddr: Byte * 8
    dwAddr: UInt32
    dwType: UInt32
class MIB_IPNETTABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH * 1
class MIB_IPNET_ROW2(Structure):
    Address: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceIndex: UInt32
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    PhysicalAddress: Byte * 32
    PhysicalAddressLength: UInt32
    State: Windows.Win32.Networking.WinSock.NL_NEIGHBOR_STATE
    Anonymous: _Anonymous_e__Union
    ReachabilityTime: _ReachabilityTime_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        Flags: Byte
        class _Anonymous_e__Struct(Structure):
            _bitfield: Byte
    class _ReachabilityTime_e__Union(Union):
        LastReachable: UInt32
        LastUnreachable: UInt32
class MIB_IPNET_TABLE2(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2 * 1
MIB_IPNET_TYPE = Int32
MIB_IPNET_TYPE_OTHER: MIB_IPNET_TYPE = 1
MIB_IPNET_TYPE_INVALID: MIB_IPNET_TYPE = 2
MIB_IPNET_TYPE_DYNAMIC: MIB_IPNET_TYPE = 3
MIB_IPNET_TYPE_STATIC: MIB_IPNET_TYPE = 4
class MIB_IPPATH_ROW(Structure):
    Source: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    Destination: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    CurrentNextHop: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    PathMtu: UInt32
    RttMean: UInt32
    RttDeviation: UInt32
    Anonymous: _Anonymous_e__Union
    IsReachable: Windows.Win32.Foundation.BOOLEAN
    LinkTransmitSpeed: UInt64
    LinkReceiveSpeed: UInt64
    class _Anonymous_e__Union(Union):
        LastReachable: UInt32
        LastUnreachable: UInt32
class MIB_IPPATH_TABLE(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPPATH_ROW * 1
MIB_IPSTATS_FORWARDING = Int32
MIB_IP_FORWARDING: MIB_IPSTATS_FORWARDING = 1
MIB_IP_NOT_FORWARDING: MIB_IPSTATS_FORWARDING = 2
class MIB_IPSTATS_LH(Structure):
    Anonymous: _Anonymous_e__Union
    dwDefaultTTL: UInt32
    dwInReceives: UInt32
    dwInHdrErrors: UInt32
    dwInAddrErrors: UInt32
    dwForwDatagrams: UInt32
    dwInUnknownProtos: UInt32
    dwInDiscards: UInt32
    dwInDelivers: UInt32
    dwOutRequests: UInt32
    dwRoutingDiscards: UInt32
    dwOutDiscards: UInt32
    dwOutNoRoutes: UInt32
    dwReasmTimeout: UInt32
    dwReasmReqds: UInt32
    dwReasmOks: UInt32
    dwReasmFails: UInt32
    dwFragOks: UInt32
    dwFragFails: UInt32
    dwFragCreates: UInt32
    dwNumIf: UInt32
    dwNumAddr: UInt32
    dwNumRoutes: UInt32
    class _Anonymous_e__Union(Union):
        dwForwarding: UInt32
        Forwarding: Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_FORWARDING
class MIB_IPSTATS_W2K(Structure):
    dwForwarding: UInt32
    dwDefaultTTL: UInt32
    dwInReceives: UInt32
    dwInHdrErrors: UInt32
    dwInAddrErrors: UInt32
    dwForwDatagrams: UInt32
    dwInUnknownProtos: UInt32
    dwInDiscards: UInt32
    dwInDelivers: UInt32
    dwOutRequests: UInt32
    dwRoutingDiscards: UInt32
    dwOutDiscards: UInt32
    dwOutNoRoutes: UInt32
    dwReasmTimeout: UInt32
    dwReasmReqds: UInt32
    dwReasmOks: UInt32
    dwReasmFails: UInt32
    dwFragOks: UInt32
    dwFragFails: UInt32
    dwFragCreates: UInt32
    dwNumIf: UInt32
    dwNumAddr: UInt32
    dwNumRoutes: UInt32
class MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES(Structure):
    InboundBandwidthInformation: Windows.Win32.Networking.WinSock.NL_BANDWIDTH_INFORMATION
    OutboundBandwidthInformation: Windows.Win32.Networking.WinSock.NL_BANDWIDTH_INFORMATION
class MIB_MCAST_LIMIT_ROW(Structure):
    dwTtl: UInt32
    dwRateLimit: UInt32
class MIB_MFE_STATS_TABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS * 1
class MIB_MFE_STATS_TABLE_EX_XP(Structure):
    dwNumEntries: UInt32
    table: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS_EX_XP_head) * 1
class MIB_MFE_TABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE * 1
class MIB_MULTICASTIPADDRESS_ROW(Structure):
    Address: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceIndex: UInt32
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    ScopeId: Windows.Win32.Networking.WinSock.SCOPE_ID
class MIB_MULTICASTIPADDRESS_TABLE(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_ROW * 1
MIB_NOTIFICATION_TYPE = Int32
MIB_NOTIFICATION_TYPE_MibParameterNotification: MIB_NOTIFICATION_TYPE = 0
MIB_NOTIFICATION_TYPE_MibAddInstance: MIB_NOTIFICATION_TYPE = 1
MIB_NOTIFICATION_TYPE_MibDeleteInstance: MIB_NOTIFICATION_TYPE = 2
MIB_NOTIFICATION_TYPE_MibInitialNotification: MIB_NOTIFICATION_TYPE = 3
class MIB_OPAQUE_INFO(Structure):
    dwId: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ullAlign: UInt64
        rgbyData: Byte * 1
class MIB_OPAQUE_QUERY(Structure):
    dwVarId: UInt32
    rgdwVarIndex: UInt32 * 1
class MIB_PROXYARP(Structure):
    dwAddress: UInt32
    dwMask: UInt32
    dwIfIndex: UInt32
class MIB_ROUTESTATE(Structure):
    bRoutesSetToStack: Windows.Win32.Foundation.BOOL
class MIB_TCP6ROW(Structure):
    State: Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE
    LocalAddr: Windows.Win32.Networking.WinSock.IN6_ADDR
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    RemoteAddr: Windows.Win32.Networking.WinSock.IN6_ADDR
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
class MIB_TCP6ROW2(Structure):
    LocalAddr: Windows.Win32.Networking.WinSock.IN6_ADDR
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    RemoteAddr: Windows.Win32.Networking.WinSock.IN6_ADDR
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
    State: Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE
    dwOwningPid: UInt32
    dwOffloadState: Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE
class MIB_TCP6ROW_OWNER_MODULE(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    ucRemoteAddr: Byte * 16
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
    dwState: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Windows.Win32.Foundation.LARGE_INTEGER
    OwningModuleInfo: UInt64 * 16
class MIB_TCP6ROW_OWNER_PID(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    ucRemoteAddr: Byte * 16
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
    dwState: UInt32
    dwOwningPid: UInt32
class MIB_TCP6TABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW * 1
class MIB_TCP6TABLE2(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW2 * 1
class MIB_TCP6TABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_MODULE * 1
class MIB_TCP6TABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_PID * 1
class MIB_TCPROW2(Structure):
    dwState: UInt32
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    dwOwningPid: UInt32
    dwOffloadState: Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE
class MIB_TCPROW_LH(Structure):
    Anonymous: _Anonymous_e__Union
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    class _Anonymous_e__Union(Union):
        dwState: UInt32
        State: Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE
class MIB_TCPROW_OWNER_MODULE(Structure):
    dwState: UInt32
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Windows.Win32.Foundation.LARGE_INTEGER
    OwningModuleInfo: UInt64 * 16
class MIB_TCPROW_OWNER_PID(Structure):
    dwState: UInt32
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    dwOwningPid: UInt32
class MIB_TCPROW_W2K(Structure):
    dwState: UInt32
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
class MIB_TCPSTATS2(Structure):
    RtoAlgorithm: Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM
    dwRtoMin: UInt32
    dwRtoMax: UInt32
    dwMaxConn: UInt32
    dwActiveOpens: UInt32
    dwPassiveOpens: UInt32
    dwAttemptFails: UInt32
    dwEstabResets: UInt32
    dwCurrEstab: UInt32
    dw64InSegs: UInt64
    dw64OutSegs: UInt64
    dwRetransSegs: UInt32
    dwInErrs: UInt32
    dwOutRsts: UInt32
    dwNumConns: UInt32
class MIB_TCPSTATS_LH(Structure):
    Anonymous: _Anonymous_e__Union
    dwRtoMin: UInt32
    dwRtoMax: UInt32
    dwMaxConn: UInt32
    dwActiveOpens: UInt32
    dwPassiveOpens: UInt32
    dwAttemptFails: UInt32
    dwEstabResets: UInt32
    dwCurrEstab: UInt32
    dwInSegs: UInt32
    dwOutSegs: UInt32
    dwRetransSegs: UInt32
    dwInErrs: UInt32
    dwOutRsts: UInt32
    dwNumConns: UInt32
    class _Anonymous_e__Union(Union):
        dwRtoAlgorithm: UInt32
        RtoAlgorithm: Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM
class MIB_TCPSTATS_W2K(Structure):
    dwRtoAlgorithm: UInt32
    dwRtoMin: UInt32
    dwRtoMax: UInt32
    dwMaxConn: UInt32
    dwActiveOpens: UInt32
    dwPassiveOpens: UInt32
    dwAttemptFails: UInt32
    dwEstabResets: UInt32
    dwCurrEstab: UInt32
    dwInSegs: UInt32
    dwOutSegs: UInt32
    dwRetransSegs: UInt32
    dwInErrs: UInt32
    dwOutRsts: UInt32
    dwNumConns: UInt32
class MIB_TCPTABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH * 1
class MIB_TCPTABLE2(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW2 * 1
class MIB_TCPTABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_MODULE * 1
class MIB_TCPTABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_PID * 1
MIB_TCP_STATE = Int32
MIB_TCP_STATE_CLOSED: MIB_TCP_STATE = 1
MIB_TCP_STATE_LISTEN: MIB_TCP_STATE = 2
MIB_TCP_STATE_SYN_SENT: MIB_TCP_STATE = 3
MIB_TCP_STATE_SYN_RCVD: MIB_TCP_STATE = 4
MIB_TCP_STATE_ESTAB: MIB_TCP_STATE = 5
MIB_TCP_STATE_FIN_WAIT1: MIB_TCP_STATE = 6
MIB_TCP_STATE_FIN_WAIT2: MIB_TCP_STATE = 7
MIB_TCP_STATE_CLOSE_WAIT: MIB_TCP_STATE = 8
MIB_TCP_STATE_CLOSING: MIB_TCP_STATE = 9
MIB_TCP_STATE_LAST_ACK: MIB_TCP_STATE = 10
MIB_TCP_STATE_TIME_WAIT: MIB_TCP_STATE = 11
MIB_TCP_STATE_DELETE_TCB: MIB_TCP_STATE = 12
MIB_TCP_STATE_RESERVED: MIB_TCP_STATE = 100
class MIB_UDP6ROW(Structure):
    dwLocalAddr: Windows.Win32.Networking.WinSock.IN6_ADDR
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
class MIB_UDP6ROW2(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Windows.Win32.Foundation.LARGE_INTEGER
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    ucRemoteAddr: Byte * 16
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            _bitfield: Int32
class MIB_UDP6ROW_OWNER_MODULE(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Windows.Win32.Foundation.LARGE_INTEGER
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            _bitfield: Int32
class MIB_UDP6ROW_OWNER_PID(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
class MIB_UDP6TABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW * 1
class MIB_UDP6TABLE2(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW2 * 1
class MIB_UDP6TABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_MODULE * 1
class MIB_UDP6TABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_PID * 1
class MIB_UDPROW(Structure):
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
class MIB_UDPROW2(Structure):
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Windows.Win32.Foundation.LARGE_INTEGER
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            _bitfield: Int32
class MIB_UDPROW_OWNER_MODULE(Structure):
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Windows.Win32.Foundation.LARGE_INTEGER
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            _bitfield: Int32
class MIB_UDPROW_OWNER_PID(Structure):
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
class MIB_UDPSTATS(Structure):
    dwInDatagrams: UInt32
    dwNoPorts: UInt32
    dwInErrors: UInt32
    dwOutDatagrams: UInt32
    dwNumAddrs: UInt32
class MIB_UDPSTATS2(Structure):
    dw64InDatagrams: UInt64
    dwNoPorts: UInt32
    dwInErrors: UInt32
    dw64OutDatagrams: UInt64
    dwNumAddrs: UInt32
class MIB_UDPTABLE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW * 1
class MIB_UDPTABLE2(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW2 * 1
class MIB_UDPTABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_MODULE * 1
class MIB_UDPTABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_PID * 1
class MIB_UNICASTIPADDRESS_ROW(Structure):
    Address: Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceLuid: Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    PrefixOrigin: Windows.Win32.Networking.WinSock.NL_PREFIX_ORIGIN
    SuffixOrigin: Windows.Win32.Networking.WinSock.NL_SUFFIX_ORIGIN
    ValidLifetime: UInt32
    PreferredLifetime: UInt32
    OnLinkPrefixLength: Byte
    SkipAsSource: Windows.Win32.Foundation.BOOLEAN
    DadState: Windows.Win32.Networking.WinSock.NL_DAD_STATE
    ScopeId: Windows.Win32.Networking.WinSock.SCOPE_ID
    CreationTimeStamp: Windows.Win32.Foundation.LARGE_INTEGER
class MIB_UNICASTIPADDRESS_TABLE(Structure):
    NumEntries: UInt32
    Table: Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW * 1
NET_ADDRESS_FORMAT = Int32
NET_ADDRESS_FORMAT_UNSPECIFIED: NET_ADDRESS_FORMAT = 0
NET_ADDRESS_DNS_NAME: NET_ADDRESS_FORMAT = 1
NET_ADDRESS_IPV4: NET_ADDRESS_FORMAT = 2
NET_ADDRESS_IPV6: NET_ADDRESS_FORMAT = 3
PFADDRESSTYPE = Int32
PF_IPV4: PFADDRESSTYPE = 0
PF_IPV6: PFADDRESSTYPE = 1
PFFORWARD_ACTION = Int32
PF_ACTION_FORWARD: PFFORWARD_ACTION = 0
PF_ACTION_DROP: PFFORWARD_ACTION = 1
PFFRAMETYPE = Int32
PFFT_FILTER: PFFRAMETYPE = 1
PFFT_FRAG: PFFRAMETYPE = 2
PFFT_SPOOF: PFFRAMETYPE = 3
class PFLOGFRAME(Structure):
    Timestamp: Windows.Win32.Foundation.LARGE_INTEGER
    pfeTypeOfFrame: Windows.Win32.NetworkManagement.IpHelper.PFFRAMETYPE
    dwTotalSizeUsed: UInt32
    dwFilterRule: UInt32
    wSizeOfAdditionalData: UInt16
    wSizeOfIpHeader: UInt16
    dwInterfaceName: UInt32
    dwIPIndex: UInt32
    bPacketData: Byte * 1
class PF_FILTER_DESCRIPTOR(Structure):
    dwFilterFlags: UInt32
    dwRule: UInt32
    pfatType: Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE
    SrcAddr: c_char_p_no
    SrcMask: c_char_p_no
    DstAddr: c_char_p_no
    DstMask: c_char_p_no
    dwProtocol: UInt32
    fLateBound: UInt32
    wSrcPort: UInt16
    wDstPort: UInt16
    wSrcPortHighRange: UInt16
    wDstPortHighRange: UInt16
class PF_FILTER_STATS(Structure):
    dwNumPacketsFiltered: UInt32
    info: Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR
class PF_INTERFACE_STATS(Structure):
    pvDriverContext: c_void_p
    dwFlags: UInt32
    dwInDrops: UInt32
    dwOutDrops: UInt32
    eaInAction: Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION
    eaOutAction: Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION
    dwNumInFilters: UInt32
    dwNumOutFilters: UInt32
    dwFrag: UInt32
    dwSpoof: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
    liSYN: Windows.Win32.Foundation.LARGE_INTEGER
    liTotalLogged: Windows.Win32.Foundation.LARGE_INTEGER
    dwLostLogEntries: UInt32
    FilterInfo: Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_STATS * 1
class PF_LATEBIND_INFO(Structure):
    SrcAddr: c_char_p_no
    DstAddr: c_char_p_no
    Mask: c_char_p_no
@winfunctype_pointer
def PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK(CallerContext: c_void_p) -> Void: ...
@winfunctype_pointer
def PIPFORWARD_CHANGE_CALLBACK(CallerContext: c_void_p, Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2_head), NotificationType: Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
@winfunctype_pointer
def PIPINTERFACE_CHANGE_CALLBACK(CallerContext: c_void_p, Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW_head), NotificationType: Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
@winfunctype_pointer
def PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK(CallerContext: c_void_p, ConnectivityHint: Windows.Win32.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT) -> Void: ...
@winfunctype_pointer
def PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK(CallerContext: c_void_p, AddressTable: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE_head)) -> Void: ...
@winfunctype_pointer
def PTEREDO_PORT_CHANGE_CALLBACK(CallerContext: c_void_p, Port: UInt16, NotificationType: Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
@winfunctype_pointer
def PUNICAST_IPADDRESS_CHANGE_CALLBACK(CallerContext: c_void_p, Row: POINTER(Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW_head), NotificationType: Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
class TCPIP_OWNER_MODULE_BASIC_INFO(Structure):
    pModuleName: Windows.Win32.Foundation.PWSTR
    pModulePath: Windows.Win32.Foundation.PWSTR
TCPIP_OWNER_MODULE_INFO_CLASS = Int32
TCPIP_OWNER_MODULE_INFO_BASIC: TCPIP_OWNER_MODULE_INFO_CLASS = 0
TCP_BOOLEAN_OPTIONAL = Int32
TCP_BOOLEAN_OPTIONAL_TcpBoolOptDisabled: TCP_BOOLEAN_OPTIONAL = 0
TCP_BOOLEAN_OPTIONAL_TcpBoolOptEnabled: TCP_BOOLEAN_OPTIONAL = 1
TCP_BOOLEAN_OPTIONAL_TcpBoolOptUnchanged: TCP_BOOLEAN_OPTIONAL = -1
TCP_CONNECTION_OFFLOAD_STATE = Int32
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateInHost: TCP_CONNECTION_OFFLOAD_STATE = 0
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloading: TCP_CONNECTION_OFFLOAD_STATE = 1
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloaded: TCP_CONNECTION_OFFLOAD_STATE = 2
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateUploading: TCP_CONNECTION_OFFLOAD_STATE = 3
TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateMax: TCP_CONNECTION_OFFLOAD_STATE = 4
class TCP_ESTATS_BANDWIDTH_ROD_v0(Structure):
    OutboundBandwidth: UInt64
    InboundBandwidth: UInt64
    OutboundInstability: UInt64
    InboundInstability: UInt64
    OutboundBandwidthPeaked: Windows.Win32.Foundation.BOOLEAN
    InboundBandwidthPeaked: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_BANDWIDTH_RW_v0(Structure):
    EnableCollectionOutbound: Windows.Win32.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL
    EnableCollectionInbound: Windows.Win32.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL
class TCP_ESTATS_DATA_ROD_v0(Structure):
    DataBytesOut: UInt64
    DataSegsOut: UInt64
    DataBytesIn: UInt64
    DataSegsIn: UInt64
    SegsOut: UInt64
    SegsIn: UInt64
    SoftErrors: UInt32
    SoftErrorReason: UInt32
    SndUna: UInt32
    SndNxt: UInt32
    SndMax: UInt32
    ThruBytesAcked: UInt64
    RcvNxt: UInt32
    ThruBytesReceived: UInt64
class TCP_ESTATS_DATA_RW_v0(Structure):
    EnableCollection: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_FINE_RTT_ROD_v0(Structure):
    RttVar: UInt32
    MaxRtt: UInt32
    MinRtt: UInt32
    SumRtt: UInt32
class TCP_ESTATS_FINE_RTT_RW_v0(Structure):
    EnableCollection: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_OBS_REC_ROD_v0(Structure):
    CurRwinRcvd: UInt32
    MaxRwinRcvd: UInt32
    MinRwinRcvd: UInt32
    WinScaleRcvd: Byte
class TCP_ESTATS_OBS_REC_RW_v0(Structure):
    EnableCollection: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_PATH_ROD_v0(Structure):
    FastRetran: UInt32
    Timeouts: UInt32
    SubsequentTimeouts: UInt32
    CurTimeoutCount: UInt32
    AbruptTimeouts: UInt32
    PktsRetrans: UInt32
    BytesRetrans: UInt32
    DupAcksIn: UInt32
    SacksRcvd: UInt32
    SackBlocksRcvd: UInt32
    CongSignals: UInt32
    PreCongSumCwnd: UInt32
    PreCongSumRtt: UInt32
    PostCongSumRtt: UInt32
    PostCongCountRtt: UInt32
    EcnSignals: UInt32
    EceRcvd: UInt32
    SendStall: UInt32
    QuenchRcvd: UInt32
    RetranThresh: UInt32
    SndDupAckEpisodes: UInt32
    SumBytesReordered: UInt32
    NonRecovDa: UInt32
    NonRecovDaEpisodes: UInt32
    AckAfterFr: UInt32
    DsackDups: UInt32
    SampleRtt: UInt32
    SmoothedRtt: UInt32
    RttVar: UInt32
    MaxRtt: UInt32
    MinRtt: UInt32
    SumRtt: UInt32
    CountRtt: UInt32
    CurRto: UInt32
    MaxRto: UInt32
    MinRto: UInt32
    CurMss: UInt32
    MaxMss: UInt32
    MinMss: UInt32
    SpuriousRtoDetections: UInt32
class TCP_ESTATS_PATH_RW_v0(Structure):
    EnableCollection: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_REC_ROD_v0(Structure):
    CurRwinSent: UInt32
    MaxRwinSent: UInt32
    MinRwinSent: UInt32
    LimRwin: UInt32
    DupAckEpisodes: UInt32
    DupAcksOut: UInt32
    CeRcvd: UInt32
    EcnSent: UInt32
    EcnNoncesRcvd: UInt32
    CurReasmQueue: UInt32
    MaxReasmQueue: UInt32
    CurAppRQueue: UIntPtr
    MaxAppRQueue: UIntPtr
    WinScaleSent: Byte
class TCP_ESTATS_REC_RW_v0(Structure):
    EnableCollection: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_SEND_BUFF_ROD_v0(Structure):
    CurRetxQueue: UIntPtr
    MaxRetxQueue: UIntPtr
    CurAppWQueue: UIntPtr
    MaxAppWQueue: UIntPtr
class TCP_ESTATS_SEND_BUFF_RW_v0(Structure):
    EnableCollection: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_SND_CONG_ROD_v0(Structure):
    SndLimTransRwin: UInt32
    SndLimTimeRwin: UInt32
    SndLimBytesRwin: UIntPtr
    SndLimTransCwnd: UInt32
    SndLimTimeCwnd: UInt32
    SndLimBytesCwnd: UIntPtr
    SndLimTransSnd: UInt32
    SndLimTimeSnd: UInt32
    SndLimBytesSnd: UIntPtr
    SlowStart: UInt32
    CongAvoid: UInt32
    OtherReductions: UInt32
    CurCwnd: UInt32
    MaxSsCwnd: UInt32
    MaxCaCwnd: UInt32
    CurSsthresh: UInt32
    MaxSsthresh: UInt32
    MinSsthresh: UInt32
class TCP_ESTATS_SND_CONG_ROS_v0(Structure):
    LimCwnd: UInt32
class TCP_ESTATS_SND_CONG_RW_v0(Structure):
    EnableCollection: Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_SYN_OPTS_ROS_v0(Structure):
    ActiveOpen: Windows.Win32.Foundation.BOOLEAN
    MssRcvd: UInt32
    MssSent: UInt32
TCP_ESTATS_TYPE = Int32
TCP_ESTATS_TYPE_TcpConnectionEstatsSynOpts: TCP_ESTATS_TYPE = 0
TCP_ESTATS_TYPE_TcpConnectionEstatsData: TCP_ESTATS_TYPE = 1
TCP_ESTATS_TYPE_TcpConnectionEstatsSndCong: TCP_ESTATS_TYPE = 2
TCP_ESTATS_TYPE_TcpConnectionEstatsPath: TCP_ESTATS_TYPE = 3
TCP_ESTATS_TYPE_TcpConnectionEstatsSendBuff: TCP_ESTATS_TYPE = 4
TCP_ESTATS_TYPE_TcpConnectionEstatsRec: TCP_ESTATS_TYPE = 5
TCP_ESTATS_TYPE_TcpConnectionEstatsObsRec: TCP_ESTATS_TYPE = 6
TCP_ESTATS_TYPE_TcpConnectionEstatsBandwidth: TCP_ESTATS_TYPE = 7
TCP_ESTATS_TYPE_TcpConnectionEstatsFineRtt: TCP_ESTATS_TYPE = 8
TCP_ESTATS_TYPE_TcpConnectionEstatsMaximum: TCP_ESTATS_TYPE = 9
class TCP_RESERVE_PORT_RANGE(Structure):
    UpperRange: UInt16
    LowerRange: UInt16
TCP_RTO_ALGORITHM = Int32
TCP_RTO_ALGORITHM_TcpRtoAlgorithmOther: TCP_RTO_ALGORITHM = 1
TCP_RTO_ALGORITHM_TcpRtoAlgorithmConstant: TCP_RTO_ALGORITHM = 2
TCP_RTO_ALGORITHM_TcpRtoAlgorithmRsre: TCP_RTO_ALGORITHM = 3
TCP_RTO_ALGORITHM_TcpRtoAlgorithmVanj: TCP_RTO_ALGORITHM = 4
TCP_RTO_ALGORITHM_MIB_TCP_RTO_OTHER: TCP_RTO_ALGORITHM = 1
TCP_RTO_ALGORITHM_MIB_TCP_RTO_CONSTANT: TCP_RTO_ALGORITHM = 2
TCP_RTO_ALGORITHM_MIB_TCP_RTO_RSRE: TCP_RTO_ALGORITHM = 3
TCP_RTO_ALGORITHM_MIB_TCP_RTO_VANJ: TCP_RTO_ALGORITHM = 4
TCP_SOFT_ERROR = Int32
TCP_SOFT_ERROR_TcpErrorNone: TCP_SOFT_ERROR = 0
TCP_SOFT_ERROR_TcpErrorBelowDataWindow: TCP_SOFT_ERROR = 1
TCP_SOFT_ERROR_TcpErrorAboveDataWindow: TCP_SOFT_ERROR = 2
TCP_SOFT_ERROR_TcpErrorBelowAckWindow: TCP_SOFT_ERROR = 3
TCP_SOFT_ERROR_TcpErrorAboveAckWindow: TCP_SOFT_ERROR = 4
TCP_SOFT_ERROR_TcpErrorBelowTsWindow: TCP_SOFT_ERROR = 5
TCP_SOFT_ERROR_TcpErrorAboveTsWindow: TCP_SOFT_ERROR = 6
TCP_SOFT_ERROR_TcpErrorDataChecksumError: TCP_SOFT_ERROR = 7
TCP_SOFT_ERROR_TcpErrorDataLengthError: TCP_SOFT_ERROR = 8
TCP_SOFT_ERROR_TcpErrorMaxSoftError: TCP_SOFT_ERROR = 9
TCP_TABLE_CLASS = Int32
TCP_TABLE_BASIC_LISTENER: TCP_TABLE_CLASS = 0
TCP_TABLE_BASIC_CONNECTIONS: TCP_TABLE_CLASS = 1
TCP_TABLE_BASIC_ALL: TCP_TABLE_CLASS = 2
TCP_TABLE_OWNER_PID_LISTENER: TCP_TABLE_CLASS = 3
TCP_TABLE_OWNER_PID_CONNECTIONS: TCP_TABLE_CLASS = 4
TCP_TABLE_OWNER_PID_ALL: TCP_TABLE_CLASS = 5
TCP_TABLE_OWNER_MODULE_LISTENER: TCP_TABLE_CLASS = 6
TCP_TABLE_OWNER_MODULE_CONNECTIONS: TCP_TABLE_CLASS = 7
TCP_TABLE_OWNER_MODULE_ALL: TCP_TABLE_CLASS = 8
UDP_TABLE_CLASS = Int32
UDP_TABLE_BASIC: UDP_TABLE_CLASS = 0
UDP_TABLE_OWNER_PID: UDP_TABLE_CLASS = 1
UDP_TABLE_OWNER_MODULE: UDP_TABLE_CLASS = 2
make_head(_module, 'ARP_SEND_REPLY')
make_head(_module, 'DNS_DOH_SERVER_SETTINGS')
make_head(_module, 'DNS_INTERFACE_SETTINGS')
make_head(_module, 'DNS_INTERFACE_SETTINGS3')
make_head(_module, 'DNS_INTERFACE_SETTINGS_EX')
make_head(_module, 'DNS_SERVER_PROPERTY')
make_head(_module, 'DNS_SERVER_PROPERTY_TYPES')
make_head(_module, 'DNS_SETTINGS')
make_head(_module, 'DNS_SETTINGS2')
make_head(_module, 'FIXED_INFO_W2KSP1')
make_head(_module, 'ICMPV6_ECHO_REPLY_LH')
make_head(_module, 'ICMP_ECHO_REPLY')
if ARCH in 'X64,ARM64':
    make_head(_module, 'ICMP_ECHO_REPLY32')
make_head(_module, 'INTERFACE_HARDWARE_CROSSTIMESTAMP')
make_head(_module, 'INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES')
make_head(_module, 'INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES')
make_head(_module, 'INTERFACE_TIMESTAMP_CAPABILITIES')
make_head(_module, 'IPV6_ADDRESS_EX')
make_head(_module, 'IP_ADAPTER_ADDRESSES_LH')
make_head(_module, 'IP_ADAPTER_ADDRESSES_XP')
make_head(_module, 'IP_ADAPTER_ANYCAST_ADDRESS_XP')
make_head(_module, 'IP_ADAPTER_DNS_SERVER_ADDRESS_XP')
make_head(_module, 'IP_ADAPTER_DNS_SUFFIX')
make_head(_module, 'IP_ADAPTER_GATEWAY_ADDRESS_LH')
make_head(_module, 'IP_ADAPTER_INDEX_MAP')
make_head(_module, 'IP_ADAPTER_INFO')
make_head(_module, 'IP_ADAPTER_MULTICAST_ADDRESS_XP')
make_head(_module, 'IP_ADAPTER_ORDER_MAP')
make_head(_module, 'IP_ADAPTER_PREFIX_XP')
make_head(_module, 'IP_ADAPTER_UNICAST_ADDRESS_LH')
make_head(_module, 'IP_ADAPTER_UNICAST_ADDRESS_XP')
make_head(_module, 'IP_ADAPTER_WINS_SERVER_ADDRESS_LH')
make_head(_module, 'IP_ADDRESS_PREFIX')
make_head(_module, 'IP_ADDRESS_STRING')
make_head(_module, 'IP_ADDR_STRING')
make_head(_module, 'IP_INTERFACE_INFO')
make_head(_module, 'IP_INTERFACE_NAME_INFO_W2KSP1')
make_head(_module, 'IP_MCAST_COUNTER_INFO')
make_head(_module, 'IP_OPTION_INFORMATION')
if ARCH in 'X64,ARM64':
    make_head(_module, 'IP_OPTION_INFORMATION32')
make_head(_module, 'IP_PER_ADAPTER_INFO_W2KSP1')
make_head(_module, 'IP_UNIDIRECTIONAL_ADAPTER_ADDRESS')
make_head(_module, 'MIBICMPINFO')
make_head(_module, 'MIBICMPSTATS')
make_head(_module, 'MIBICMPSTATS_EX_XPSP1')
make_head(_module, 'MIB_ANYCASTIPADDRESS_ROW')
make_head(_module, 'MIB_ANYCASTIPADDRESS_TABLE')
make_head(_module, 'MIB_BEST_IF')
make_head(_module, 'MIB_BOUNDARYROW')
make_head(_module, 'MIB_ICMP')
make_head(_module, 'MIB_ICMP_EX_XPSP1')
make_head(_module, 'MIB_IFNUMBER')
make_head(_module, 'MIB_IFROW')
make_head(_module, 'MIB_IFSTACK_ROW')
make_head(_module, 'MIB_IFSTACK_TABLE')
make_head(_module, 'MIB_IFSTATUS')
make_head(_module, 'MIB_IFTABLE')
make_head(_module, 'MIB_IF_ROW2')
make_head(_module, 'MIB_IF_TABLE2')
make_head(_module, 'MIB_INVERTEDIFSTACK_ROW')
make_head(_module, 'MIB_INVERTEDIFSTACK_TABLE')
make_head(_module, 'MIB_IPADDRROW_W2K')
make_head(_module, 'MIB_IPADDRROW_XP')
make_head(_module, 'MIB_IPADDRTABLE')
make_head(_module, 'MIB_IPDESTROW')
make_head(_module, 'MIB_IPDESTTABLE')
make_head(_module, 'MIB_IPFORWARDNUMBER')
make_head(_module, 'MIB_IPFORWARDROW')
make_head(_module, 'MIB_IPFORWARDTABLE')
make_head(_module, 'MIB_IPFORWARD_ROW2')
make_head(_module, 'MIB_IPFORWARD_TABLE2')
make_head(_module, 'MIB_IPINTERFACE_ROW')
make_head(_module, 'MIB_IPINTERFACE_TABLE')
make_head(_module, 'MIB_IPMCAST_BOUNDARY')
make_head(_module, 'MIB_IPMCAST_BOUNDARY_TABLE')
make_head(_module, 'MIB_IPMCAST_GLOBAL')
make_head(_module, 'MIB_IPMCAST_IF_ENTRY')
make_head(_module, 'MIB_IPMCAST_IF_TABLE')
make_head(_module, 'MIB_IPMCAST_MFE')
make_head(_module, 'MIB_IPMCAST_MFE_STATS')
make_head(_module, 'MIB_IPMCAST_MFE_STATS_EX_XP')
make_head(_module, 'MIB_IPMCAST_OIF_STATS_LH')
make_head(_module, 'MIB_IPMCAST_OIF_STATS_W2K')
make_head(_module, 'MIB_IPMCAST_OIF_W2K')
make_head(_module, 'MIB_IPMCAST_OIF_XP')
make_head(_module, 'MIB_IPMCAST_SCOPE')
make_head(_module, 'MIB_IPNETROW_LH')
make_head(_module, 'MIB_IPNETROW_W2K')
make_head(_module, 'MIB_IPNETTABLE')
make_head(_module, 'MIB_IPNET_ROW2')
make_head(_module, 'MIB_IPNET_TABLE2')
make_head(_module, 'MIB_IPPATH_ROW')
make_head(_module, 'MIB_IPPATH_TABLE')
make_head(_module, 'MIB_IPSTATS_LH')
make_head(_module, 'MIB_IPSTATS_W2K')
make_head(_module, 'MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES')
make_head(_module, 'MIB_MCAST_LIMIT_ROW')
make_head(_module, 'MIB_MFE_STATS_TABLE')
make_head(_module, 'MIB_MFE_STATS_TABLE_EX_XP')
make_head(_module, 'MIB_MFE_TABLE')
make_head(_module, 'MIB_MULTICASTIPADDRESS_ROW')
make_head(_module, 'MIB_MULTICASTIPADDRESS_TABLE')
make_head(_module, 'MIB_OPAQUE_INFO')
make_head(_module, 'MIB_OPAQUE_QUERY')
make_head(_module, 'MIB_PROXYARP')
make_head(_module, 'MIB_ROUTESTATE')
make_head(_module, 'MIB_TCP6ROW')
make_head(_module, 'MIB_TCP6ROW2')
make_head(_module, 'MIB_TCP6ROW_OWNER_MODULE')
make_head(_module, 'MIB_TCP6ROW_OWNER_PID')
make_head(_module, 'MIB_TCP6TABLE')
make_head(_module, 'MIB_TCP6TABLE2')
make_head(_module, 'MIB_TCP6TABLE_OWNER_MODULE')
make_head(_module, 'MIB_TCP6TABLE_OWNER_PID')
make_head(_module, 'MIB_TCPROW2')
make_head(_module, 'MIB_TCPROW_LH')
make_head(_module, 'MIB_TCPROW_OWNER_MODULE')
make_head(_module, 'MIB_TCPROW_OWNER_PID')
make_head(_module, 'MIB_TCPROW_W2K')
make_head(_module, 'MIB_TCPSTATS2')
make_head(_module, 'MIB_TCPSTATS_LH')
make_head(_module, 'MIB_TCPSTATS_W2K')
make_head(_module, 'MIB_TCPTABLE')
make_head(_module, 'MIB_TCPTABLE2')
make_head(_module, 'MIB_TCPTABLE_OWNER_MODULE')
make_head(_module, 'MIB_TCPTABLE_OWNER_PID')
make_head(_module, 'MIB_UDP6ROW')
make_head(_module, 'MIB_UDP6ROW2')
make_head(_module, 'MIB_UDP6ROW_OWNER_MODULE')
make_head(_module, 'MIB_UDP6ROW_OWNER_PID')
make_head(_module, 'MIB_UDP6TABLE')
make_head(_module, 'MIB_UDP6TABLE2')
make_head(_module, 'MIB_UDP6TABLE_OWNER_MODULE')
make_head(_module, 'MIB_UDP6TABLE_OWNER_PID')
make_head(_module, 'MIB_UDPROW')
make_head(_module, 'MIB_UDPROW2')
make_head(_module, 'MIB_UDPROW_OWNER_MODULE')
make_head(_module, 'MIB_UDPROW_OWNER_PID')
make_head(_module, 'MIB_UDPSTATS')
make_head(_module, 'MIB_UDPSTATS2')
make_head(_module, 'MIB_UDPTABLE')
make_head(_module, 'MIB_UDPTABLE2')
make_head(_module, 'MIB_UDPTABLE_OWNER_MODULE')
make_head(_module, 'MIB_UDPTABLE_OWNER_PID')
make_head(_module, 'MIB_UNICASTIPADDRESS_ROW')
make_head(_module, 'MIB_UNICASTIPADDRESS_TABLE')
make_head(_module, 'PFLOGFRAME')
make_head(_module, 'PF_FILTER_DESCRIPTOR')
make_head(_module, 'PF_FILTER_STATS')
make_head(_module, 'PF_INTERFACE_STATS')
make_head(_module, 'PF_LATEBIND_INFO')
make_head(_module, 'PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK')
make_head(_module, 'PIPFORWARD_CHANGE_CALLBACK')
make_head(_module, 'PIPINTERFACE_CHANGE_CALLBACK')
make_head(_module, 'PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK')
make_head(_module, 'PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK')
make_head(_module, 'PTEREDO_PORT_CHANGE_CALLBACK')
make_head(_module, 'PUNICAST_IPADDRESS_CHANGE_CALLBACK')
make_head(_module, 'TCPIP_OWNER_MODULE_BASIC_INFO')
make_head(_module, 'TCP_ESTATS_BANDWIDTH_ROD_v0')
make_head(_module, 'TCP_ESTATS_BANDWIDTH_RW_v0')
make_head(_module, 'TCP_ESTATS_DATA_ROD_v0')
make_head(_module, 'TCP_ESTATS_DATA_RW_v0')
make_head(_module, 'TCP_ESTATS_FINE_RTT_ROD_v0')
make_head(_module, 'TCP_ESTATS_FINE_RTT_RW_v0')
make_head(_module, 'TCP_ESTATS_OBS_REC_ROD_v0')
make_head(_module, 'TCP_ESTATS_OBS_REC_RW_v0')
make_head(_module, 'TCP_ESTATS_PATH_ROD_v0')
make_head(_module, 'TCP_ESTATS_PATH_RW_v0')
make_head(_module, 'TCP_ESTATS_REC_ROD_v0')
make_head(_module, 'TCP_ESTATS_REC_RW_v0')
make_head(_module, 'TCP_ESTATS_SEND_BUFF_ROD_v0')
make_head(_module, 'TCP_ESTATS_SEND_BUFF_RW_v0')
make_head(_module, 'TCP_ESTATS_SND_CONG_ROD_v0')
make_head(_module, 'TCP_ESTATS_SND_CONG_ROS_v0')
make_head(_module, 'TCP_ESTATS_SND_CONG_RW_v0')
make_head(_module, 'TCP_ESTATS_SYN_OPTS_ROS_v0')
make_head(_module, 'TCP_RESERVE_PORT_RANGE')
__all__ = [
    "ANY_SIZE",
    "ARP_SEND_REPLY",
    "AddIPAddress",
    "BEST_IF",
    "BEST_ROUTE",
    "BROADCAST_NODETYPE",
    "CancelIPChangeNotify",
    "CancelMibChangeNotify2",
    "CaptureInterfaceHardwareCrossTimestamp",
    "ConvertCompartmentGuidToId",
    "ConvertCompartmentIdToGuid",
    "ConvertInterfaceAliasToLuid",
    "ConvertInterfaceGuidToLuid",
    "ConvertInterfaceIndexToLuid",
    "ConvertInterfaceLuidToAlias",
    "ConvertInterfaceLuidToGuid",
    "ConvertInterfaceLuidToIndex",
    "ConvertInterfaceLuidToNameA",
    "ConvertInterfaceLuidToNameW",
    "ConvertInterfaceNameToLuidA",
    "ConvertInterfaceNameToLuidW",
    "ConvertIpv4MaskToLength",
    "ConvertLengthToIpv4Mask",
    "CreateAnycastIpAddressEntry",
    "CreateIpForwardEntry",
    "CreateIpForwardEntry2",
    "CreateIpNetEntry",
    "CreateIpNetEntry2",
    "CreatePersistentTcpPortReservation",
    "CreatePersistentUdpPortReservation",
    "CreateProxyArpEntry",
    "CreateSortedAddressPairs",
    "CreateUnicastIpAddressEntry",
    "DEFAULT_MINIMUM_ENTITIES",
    "DEST_LONGER",
    "DEST_MATCHING",
    "DEST_SHORTER",
    "DNS_DOH_AUTO_UPGRADE_SERVER",
    "DNS_DOH_POLICY_AUTO",
    "DNS_DOH_POLICY_DISABLE",
    "DNS_DOH_POLICY_NOT_CONFIGURED",
    "DNS_DOH_POLICY_REQUIRED",
    "DNS_DOH_SERVER_SETTINGS",
    "DNS_DOH_SERVER_SETTINGS_ENABLE",
    "DNS_DOH_SERVER_SETTINGS_ENABLE_AUTO",
    "DNS_DOH_SERVER_SETTINGS_FALLBACK_TO_UDP",
    "DNS_ENABLE_DOH",
    "DNS_INTERFACE_SETTINGS",
    "DNS_INTERFACE_SETTINGS3",
    "DNS_INTERFACE_SETTINGS_EX",
    "DNS_INTERFACE_SETTINGS_VERSION1",
    "DNS_INTERFACE_SETTINGS_VERSION2",
    "DNS_INTERFACE_SETTINGS_VERSION3",
    "DNS_SERVER_PROPERTY",
    "DNS_SERVER_PROPERTY_TYPE",
    "DNS_SERVER_PROPERTY_TYPES",
    "DNS_SERVER_PROPERTY_TYPE_DnsServerDohProperty",
    "DNS_SERVER_PROPERTY_TYPE_DnsServerInvalidProperty",
    "DNS_SERVER_PROPERTY_VERSION1",
    "DNS_SETTINGS",
    "DNS_SETTINGS2",
    "DNS_SETTINGS_ENABLE_LLMNR",
    "DNS_SETTINGS_QUERY_ADAPTER_NAME",
    "DNS_SETTINGS_VERSION1",
    "DNS_SETTINGS_VERSION2",
    "DNS_SETTING_DISABLE_UNCONSTRAINED_QUERIES",
    "DNS_SETTING_DOH",
    "DNS_SETTING_DOH_PROFILE",
    "DNS_SETTING_DOMAIN",
    "DNS_SETTING_HOSTNAME",
    "DNS_SETTING_IPV6",
    "DNS_SETTING_NAMESERVER",
    "DNS_SETTING_PROFILE_NAMESERVER",
    "DNS_SETTING_REGISTER_ADAPTER_NAME",
    "DNS_SETTING_REGISTRATION_ENABLED",
    "DNS_SETTING_SEARCHLIST",
    "DNS_SETTING_SUPPLEMENTAL_SEARCH_LIST",
    "DeleteAnycastIpAddressEntry",
    "DeleteIPAddress",
    "DeleteIpForwardEntry",
    "DeleteIpForwardEntry2",
    "DeleteIpNetEntry",
    "DeleteIpNetEntry2",
    "DeletePersistentTcpPortReservation",
    "DeletePersistentUdpPortReservation",
    "DeleteProxyArpEntry",
    "DeleteUnicastIpAddressEntry",
    "DisableMediaSense",
    "ERROR_BASE",
    "ERROR_IPV6_NOT_IMPLEMENTED",
    "EnableRouter",
    "FD_FLAGS_ALLFLAGS",
    "FD_FLAGS_NOSYN",
    "FIXED_INFO_W2KSP1",
    "FlushIpNetTable",
    "FlushIpNetTable2",
    "FlushIpPathTable",
    "FreeDnsSettings",
    "FreeInterfaceDnsSettings",
    "FreeMibTable",
    "GAA_FLAG_INCLUDE_ALL_COMPARTMENTS",
    "GAA_FLAG_INCLUDE_ALL_INTERFACES",
    "GAA_FLAG_INCLUDE_GATEWAYS",
    "GAA_FLAG_INCLUDE_PREFIX",
    "GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER",
    "GAA_FLAG_INCLUDE_WINS_INFO",
    "GAA_FLAG_SKIP_ANYCAST",
    "GAA_FLAG_SKIP_DNS_INFO",
    "GAA_FLAG_SKIP_DNS_SERVER",
    "GAA_FLAG_SKIP_FRIENDLY_NAME",
    "GAA_FLAG_SKIP_MULTICAST",
    "GAA_FLAG_SKIP_UNICAST",
    "GET_ADAPTERS_ADDRESSES_FLAGS",
    "GF_FRAGCACHE",
    "GF_FRAGMENTS",
    "GF_STRONGHOST",
    "GLOBAL_FILTER",
    "GetAdapterIndex",
    "GetAdapterOrderMap",
    "GetAdaptersAddresses",
    "GetAdaptersInfo",
    "GetAnycastIpAddressEntry",
    "GetAnycastIpAddressTable",
    "GetBestInterface",
    "GetBestInterfaceEx",
    "GetBestRoute",
    "GetBestRoute2",
    "GetCurrentThreadCompartmentId",
    "GetCurrentThreadCompartmentScope",
    "GetDefaultCompartmentId",
    "GetDnsSettings",
    "GetExtendedTcpTable",
    "GetExtendedUdpTable",
    "GetFriendlyIfIndex",
    "GetIcmpStatistics",
    "GetIcmpStatisticsEx",
    "GetIfEntry",
    "GetIfEntry2",
    "GetIfEntry2Ex",
    "GetIfStackTable",
    "GetIfTable",
    "GetIfTable2",
    "GetIfTable2Ex",
    "GetInterfaceActiveTimestampCapabilities",
    "GetInterfaceDnsSettings",
    "GetInterfaceInfo",
    "GetInterfaceSupportedTimestampCapabilities",
    "GetInvertedIfStackTable",
    "GetIpAddrTable",
    "GetIpErrorString",
    "GetIpForwardEntry2",
    "GetIpForwardTable",
    "GetIpForwardTable2",
    "GetIpInterfaceEntry",
    "GetIpInterfaceTable",
    "GetIpNetEntry2",
    "GetIpNetTable",
    "GetIpNetTable2",
    "GetIpNetworkConnectionBandwidthEstimates",
    "GetIpPathEntry",
    "GetIpPathTable",
    "GetIpStatistics",
    "GetIpStatisticsEx",
    "GetJobCompartmentId",
    "GetMulticastIpAddressEntry",
    "GetMulticastIpAddressTable",
    "GetNetworkConnectivityHint",
    "GetNetworkConnectivityHintForInterface",
    "GetNetworkInformation",
    "GetNetworkParams",
    "GetNumberOfInterfaces",
    "GetOwnerModuleFromPidAndInfo",
    "GetOwnerModuleFromTcp6Entry",
    "GetOwnerModuleFromTcpEntry",
    "GetOwnerModuleFromUdp6Entry",
    "GetOwnerModuleFromUdpEntry",
    "GetPerAdapterInfo",
    "GetPerTcp6ConnectionEStats",
    "GetPerTcpConnectionEStats",
    "GetRTTAndHopCount",
    "GetSessionCompartmentId",
    "GetTcp6Table",
    "GetTcp6Table2",
    "GetTcpStatistics",
    "GetTcpStatisticsEx",
    "GetTcpStatisticsEx2",
    "GetTcpTable",
    "GetTcpTable2",
    "GetTeredoPort",
    "GetUdp6Table",
    "GetUdpStatistics",
    "GetUdpStatisticsEx",
    "GetUdpStatisticsEx2",
    "GetUdpTable",
    "GetUniDirectionalAdapterInfo",
    "GetUnicastIpAddressEntry",
    "GetUnicastIpAddressTable",
    "HIFTIMESTAMPCHANGE",
    "HYBRID_NODETYPE",
    "ICMP4_DST_UNREACH",
    "ICMP4_ECHO_REPLY",
    "ICMP4_ECHO_REQUEST",
    "ICMP4_MASK_REPLY",
    "ICMP4_MASK_REQUEST",
    "ICMP4_PARAM_PROB",
    "ICMP4_REDIRECT",
    "ICMP4_ROUTER_ADVERT",
    "ICMP4_ROUTER_SOLICIT",
    "ICMP4_SOURCE_QUENCH",
    "ICMP4_TIMESTAMP_REPLY",
    "ICMP4_TIMESTAMP_REQUEST",
    "ICMP4_TIME_EXCEEDED",
    "ICMP4_TYPE",
    "ICMP6_DST_UNREACH",
    "ICMP6_ECHO_REPLY",
    "ICMP6_ECHO_REQUEST",
    "ICMP6_INFOMSG_MASK",
    "ICMP6_MEMBERSHIP_QUERY",
    "ICMP6_MEMBERSHIP_REDUCTION",
    "ICMP6_MEMBERSHIP_REPORT",
    "ICMP6_PACKET_TOO_BIG",
    "ICMP6_PARAM_PROB",
    "ICMP6_TIME_EXCEEDED",
    "ICMP6_TYPE",
    "ICMP6_V2_MEMBERSHIP_REPORT",
    "ICMPV6_ECHO_REPLY_LH",
    "ICMP_ECHO_REPLY",
    "ICMP_ECHO_REPLY32",
    "ICMP_STATS",
    "IF_ACCESS_BROADCAST",
    "IF_ACCESS_LOOPBACK",
    "IF_ACCESS_POINTTOMULTIPOINT",
    "IF_ACCESS_POINTTOPOINT",
    "IF_ACCESS_POINT_TO_MULTI_POINT",
    "IF_ACCESS_POINT_TO_POINT",
    "IF_ACCESS_TYPE",
    "IF_ADMIN_STATUS_DOWN",
    "IF_ADMIN_STATUS_TESTING",
    "IF_ADMIN_STATUS_UP",
    "IF_CHECK_MCAST",
    "IF_CHECK_NONE",
    "IF_CHECK_SEND",
    "IF_CONNECTION_DEDICATED",
    "IF_CONNECTION_DEMAND",
    "IF_CONNECTION_PASSIVE",
    "IF_NUMBER",
    "IF_OPER_STATUS_CONNECTED",
    "IF_OPER_STATUS_CONNECTING",
    "IF_OPER_STATUS_DISCONNECTED",
    "IF_OPER_STATUS_NON_OPERATIONAL",
    "IF_OPER_STATUS_OPERATIONAL",
    "IF_OPER_STATUS_UNREACHABLE",
    "IF_ROW",
    "IF_STATUS",
    "IF_TABLE",
    "IF_TYPE_A12MPPSWITCH",
    "IF_TYPE_AAL2",
    "IF_TYPE_AAL5",
    "IF_TYPE_ADSL",
    "IF_TYPE_AFLANE_8023",
    "IF_TYPE_AFLANE_8025",
    "IF_TYPE_ARAP",
    "IF_TYPE_ARCNET",
    "IF_TYPE_ARCNET_PLUS",
    "IF_TYPE_ASYNC",
    "IF_TYPE_ATM",
    "IF_TYPE_ATM_DXI",
    "IF_TYPE_ATM_FUNI",
    "IF_TYPE_ATM_IMA",
    "IF_TYPE_ATM_LOGICAL",
    "IF_TYPE_ATM_RADIO",
    "IF_TYPE_ATM_SUBINTERFACE",
    "IF_TYPE_ATM_VCI_ENDPT",
    "IF_TYPE_ATM_VIRTUAL",
    "IF_TYPE_BASIC_ISDN",
    "IF_TYPE_BGP_POLICY_ACCOUNTING",
    "IF_TYPE_BSC",
    "IF_TYPE_CCTEMUL",
    "IF_TYPE_CES",
    "IF_TYPE_CHANNEL",
    "IF_TYPE_CNR",
    "IF_TYPE_COFFEE",
    "IF_TYPE_COMPOSITELINK",
    "IF_TYPE_DCN",
    "IF_TYPE_DDN_X25",
    "IF_TYPE_DIGITALPOWERLINE",
    "IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL",
    "IF_TYPE_DLSW",
    "IF_TYPE_DOCSCABLE_DOWNSTREAM",
    "IF_TYPE_DOCSCABLE_MACLAYER",
    "IF_TYPE_DOCSCABLE_UPSTREAM",
    "IF_TYPE_DS0",
    "IF_TYPE_DS0_BUNDLE",
    "IF_TYPE_DS1",
    "IF_TYPE_DS1_FDL",
    "IF_TYPE_DS3",
    "IF_TYPE_DTM",
    "IF_TYPE_DVBRCC_DOWNSTREAM",
    "IF_TYPE_DVBRCC_MACLAYER",
    "IF_TYPE_DVBRCC_UPSTREAM",
    "IF_TYPE_DVB_ASI_IN",
    "IF_TYPE_DVB_ASI_OUT",
    "IF_TYPE_E1",
    "IF_TYPE_EON",
    "IF_TYPE_EPLRS",
    "IF_TYPE_ESCON",
    "IF_TYPE_ETHERNET_3MBIT",
    "IF_TYPE_ETHERNET_CSMACD",
    "IF_TYPE_FAST",
    "IF_TYPE_FASTETHER",
    "IF_TYPE_FASTETHER_FX",
    "IF_TYPE_FDDI",
    "IF_TYPE_FIBRECHANNEL",
    "IF_TYPE_FRAMERELAY",
    "IF_TYPE_FRAMERELAY_INTERCONNECT",
    "IF_TYPE_FRAMERELAY_MPI",
    "IF_TYPE_FRAMERELAY_SERVICE",
    "IF_TYPE_FRF16_MFR_BUNDLE",
    "IF_TYPE_FR_DLCI_ENDPT",
    "IF_TYPE_FR_FORWARD",
    "IF_TYPE_G703_2MB",
    "IF_TYPE_G703_64K",
    "IF_TYPE_GIGABITETHERNET",
    "IF_TYPE_GR303_IDT",
    "IF_TYPE_GR303_RDT",
    "IF_TYPE_H323_GATEKEEPER",
    "IF_TYPE_H323_PROXY",
    "IF_TYPE_HDH_1822",
    "IF_TYPE_HDLC",
    "IF_TYPE_HDSL2",
    "IF_TYPE_HIPERLAN2",
    "IF_TYPE_HIPPI",
    "IF_TYPE_HIPPIINTERFACE",
    "IF_TYPE_HOSTPAD",
    "IF_TYPE_HSSI",
    "IF_TYPE_HYPERCHANNEL",
    "IF_TYPE_IBM370PARCHAN",
    "IF_TYPE_IDSL",
    "IF_TYPE_IEEE1394",
    "IF_TYPE_IEEE80211",
    "IF_TYPE_IEEE80212",
    "IF_TYPE_IEEE802154",
    "IF_TYPE_IEEE80216_WMAN",
    "IF_TYPE_IEEE8023AD_LAG",
    "IF_TYPE_IF_GSN",
    "IF_TYPE_IMT",
    "IF_TYPE_INTERLEAVE",
    "IF_TYPE_IP",
    "IF_TYPE_IPFORWARD",
    "IF_TYPE_IPOVER_ATM",
    "IF_TYPE_IPOVER_CDLC",
    "IF_TYPE_IPOVER_CLAW",
    "IF_TYPE_IPSWITCH",
    "IF_TYPE_IS088023_CSMACD",
    "IF_TYPE_ISDN",
    "IF_TYPE_ISDN_S",
    "IF_TYPE_ISDN_U",
    "IF_TYPE_ISO88022_LLC",
    "IF_TYPE_ISO88024_TOKENBUS",
    "IF_TYPE_ISO88025R_DTR",
    "IF_TYPE_ISO88025_CRFPRINT",
    "IF_TYPE_ISO88025_FIBER",
    "IF_TYPE_ISO88025_TOKENRING",
    "IF_TYPE_ISO88026_MAN",
    "IF_TYPE_ISUP",
    "IF_TYPE_L2_VLAN",
    "IF_TYPE_L3_IPVLAN",
    "IF_TYPE_L3_IPXVLAN",
    "IF_TYPE_LAP_B",
    "IF_TYPE_LAP_D",
    "IF_TYPE_LAP_F",
    "IF_TYPE_LOCALTALK",
    "IF_TYPE_MEDIAMAILOVERIP",
    "IF_TYPE_MF_SIGLINK",
    "IF_TYPE_MIO_X25",
    "IF_TYPE_MODEM",
    "IF_TYPE_MPC",
    "IF_TYPE_MPLS",
    "IF_TYPE_MPLS_TUNNEL",
    "IF_TYPE_MSDSL",
    "IF_TYPE_MVL",
    "IF_TYPE_MYRINET",
    "IF_TYPE_NFAS",
    "IF_TYPE_NSIP",
    "IF_TYPE_OPTICAL_CHANNEL",
    "IF_TYPE_OPTICAL_TRANSPORT",
    "IF_TYPE_OTHER",
    "IF_TYPE_PARA",
    "IF_TYPE_PLC",
    "IF_TYPE_POS",
    "IF_TYPE_PPP",
    "IF_TYPE_PPPMULTILINKBUNDLE",
    "IF_TYPE_PRIMARY_ISDN",
    "IF_TYPE_PROP_BWA_P2MP",
    "IF_TYPE_PROP_CNLS",
    "IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM",
    "IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER",
    "IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM",
    "IF_TYPE_PROP_MULTIPLEXOR",
    "IF_TYPE_PROP_POINT2POINT_SERIAL",
    "IF_TYPE_PROP_VIRTUAL",
    "IF_TYPE_PROP_WIRELESS_P2P",
    "IF_TYPE_PROTEON_10MBIT",
    "IF_TYPE_PROTEON_80MBIT",
    "IF_TYPE_QLLC",
    "IF_TYPE_RADIO_MAC",
    "IF_TYPE_RADSL",
    "IF_TYPE_REACH_DSL",
    "IF_TYPE_REGULAR_1822",
    "IF_TYPE_RFC1483",
    "IF_TYPE_RFC877_X25",
    "IF_TYPE_RS232",
    "IF_TYPE_RSRB",
    "IF_TYPE_SDLC",
    "IF_TYPE_SDSL",
    "IF_TYPE_SHDSL",
    "IF_TYPE_SIP",
    "IF_TYPE_SLIP",
    "IF_TYPE_SMDS_DXI",
    "IF_TYPE_SMDS_ICIP",
    "IF_TYPE_SOFTWARE_LOOPBACK",
    "IF_TYPE_SONET",
    "IF_TYPE_SONET_OVERHEAD_CHANNEL",
    "IF_TYPE_SONET_PATH",
    "IF_TYPE_SONET_VT",
    "IF_TYPE_SRP",
    "IF_TYPE_SS7_SIGLINK",
    "IF_TYPE_STACKTOSTACK",
    "IF_TYPE_STARLAN",
    "IF_TYPE_TDLC",
    "IF_TYPE_TERMPAD",
    "IF_TYPE_TR008",
    "IF_TYPE_TRANSPHDLC",
    "IF_TYPE_TUNNEL",
    "IF_TYPE_ULTRA",
    "IF_TYPE_USB",
    "IF_TYPE_V11",
    "IF_TYPE_V35",
    "IF_TYPE_V36",
    "IF_TYPE_V37",
    "IF_TYPE_VDSL",
    "IF_TYPE_VIRTUALIPADDRESS",
    "IF_TYPE_VOICEOVERATM",
    "IF_TYPE_VOICEOVERFRAMERELAY",
    "IF_TYPE_VOICE_EM",
    "IF_TYPE_VOICE_ENCAP",
    "IF_TYPE_VOICE_FXO",
    "IF_TYPE_VOICE_FXS",
    "IF_TYPE_VOICE_OVERIP",
    "IF_TYPE_WWANPP",
    "IF_TYPE_WWANPP2",
    "IF_TYPE_X213",
    "IF_TYPE_X25_HUNTGROUP",
    "IF_TYPE_X25_MLP",
    "IF_TYPE_X25_PLE",
    "IF_TYPE_XBOX_WIRELESS",
    "INTERFACE_HARDWARE_CROSSTIMESTAMP",
    "INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES",
    "INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES",
    "INTERFACE_TIMESTAMP_CAPABILITIES",
    "INTERNAL_IF_OPER_STATUS",
    "IOCTL_ARP_SEND_REQUEST",
    "IOCTL_IP_ADDCHANGE_NOTIFY_REQUEST",
    "IOCTL_IP_GET_BEST_INTERFACE",
    "IOCTL_IP_INTERFACE_INFO",
    "IOCTL_IP_RTCHANGE_NOTIFY_REQUEST",
    "IOCTL_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS",
    "IP6_STATS",
    "IPRTRMGR_PID",
    "IPV6_ADDRESS_EX",
    "IPV6_GLOBAL_INFO",
    "IPV6_ROUTE_INFO",
    "IP_ADAPTER_ADDRESSES_LH",
    "IP_ADAPTER_ADDRESSES_XP",
    "IP_ADAPTER_ADDRESS_DNS_ELIGIBLE",
    "IP_ADAPTER_ADDRESS_TRANSIENT",
    "IP_ADAPTER_ANYCAST_ADDRESS_XP",
    "IP_ADAPTER_DDNS_ENABLED",
    "IP_ADAPTER_DHCP_ENABLED",
    "IP_ADAPTER_DNS_SERVER_ADDRESS_XP",
    "IP_ADAPTER_DNS_SUFFIX",
    "IP_ADAPTER_GATEWAY_ADDRESS_LH",
    "IP_ADAPTER_INDEX_MAP",
    "IP_ADAPTER_INFO",
    "IP_ADAPTER_IPV4_ENABLED",
    "IP_ADAPTER_IPV6_ENABLED",
    "IP_ADAPTER_IPV6_MANAGE_ADDRESS_CONFIG",
    "IP_ADAPTER_IPV6_OTHER_STATEFUL_CONFIG",
    "IP_ADAPTER_MULTICAST_ADDRESS_XP",
    "IP_ADAPTER_NETBIOS_OVER_TCPIP_ENABLED",
    "IP_ADAPTER_NO_MULTICAST",
    "IP_ADAPTER_ORDER_MAP",
    "IP_ADAPTER_PREFIX_XP",
    "IP_ADAPTER_RECEIVE_ONLY",
    "IP_ADAPTER_REGISTER_ADAPTER_SUFFIX",
    "IP_ADAPTER_UNICAST_ADDRESS_LH",
    "IP_ADAPTER_UNICAST_ADDRESS_XP",
    "IP_ADAPTER_WINS_SERVER_ADDRESS_LH",
    "IP_ADDRESS_PREFIX",
    "IP_ADDRESS_STRING",
    "IP_ADDRROW",
    "IP_ADDRTABLE",
    "IP_ADDR_ADDED",
    "IP_ADDR_DELETED",
    "IP_ADDR_STRING",
    "IP_BAD_DESTINATION",
    "IP_BAD_HEADER",
    "IP_BAD_OPTION",
    "IP_BAD_REQ",
    "IP_BAD_ROUTE",
    "IP_BIND_ADAPTER",
    "IP_BUF_TOO_SMALL",
    "IP_DEMAND_DIAL_FILTER_INFO",
    "IP_DEMAND_DIAL_FILTER_INFO_V6",
    "IP_DEST_ADDR_UNREACHABLE",
    "IP_DEST_HOST_UNREACHABLE",
    "IP_DEST_NET_UNREACHABLE",
    "IP_DEST_NO_ROUTE",
    "IP_DEST_PORT_UNREACHABLE",
    "IP_DEST_PROHIBITED",
    "IP_DEST_PROT_UNREACHABLE",
    "IP_DEST_SCOPE_MISMATCH",
    "IP_DEST_UNREACHABLE",
    "IP_DEVICE_DOES_NOT_EXIST",
    "IP_DUPLICATE_ADDRESS",
    "IP_DUPLICATE_IPADD",
    "IP_EXPORT_INCLUDED",
    "IP_FILTER_ENABLE_INFO",
    "IP_FILTER_ENABLE_INFO_V6",
    "IP_FLAG_DF",
    "IP_FLAG_REVERSE",
    "IP_FORWARDNUMBER",
    "IP_FORWARDROW",
    "IP_FORWARDTABLE",
    "IP_GENERAL_FAILURE",
    "IP_GENERAL_INFO_BASE",
    "IP_GLOBAL_INFO",
    "IP_HOP_LIMIT_EXCEEDED",
    "IP_HW_ERROR",
    "IP_ICMP_ERROR",
    "IP_IFFILTER_INFO",
    "IP_IFFILTER_INFO_V6",
    "IP_INTERFACE_INFO",
    "IP_INTERFACE_METRIC_CHANGE",
    "IP_INTERFACE_NAME_INFO_W2KSP1",
    "IP_INTERFACE_STATUS_INFO",
    "IP_INTERFACE_WOL_CAPABILITY_CHANGE",
    "IP_IN_FILTER_INFO",
    "IP_IN_FILTER_INFO_V6",
    "IP_IPINIP_CFG_INFO",
    "IP_MCAST_BOUNDARY_INFO",
    "IP_MCAST_COUNTER_INFO",
    "IP_MCAST_HEARBEAT_INFO",
    "IP_MCAST_LIMIT_INFO",
    "IP_MEDIA_CONNECT",
    "IP_MEDIA_DISCONNECT",
    "IP_MTU_CHANGE",
    "IP_NEGOTIATING_IPSEC",
    "IP_NETROW",
    "IP_NETTABLE",
    "IP_NO_RESOURCES",
    "IP_OPTION_INFORMATION",
    "IP_OPTION_INFORMATION32",
    "IP_OPTION_TOO_BIG",
    "IP_OUT_FILTER_INFO",
    "IP_OUT_FILTER_INFO_V6",
    "IP_PACKET_TOO_BIG",
    "IP_PARAMETER_PROBLEM",
    "IP_PARAM_PROBLEM",
    "IP_PENDING",
    "IP_PER_ADAPTER_INFO_W2KSP1",
    "IP_PROT_PRIORITY_INFO",
    "IP_PROT_PRIORITY_INFO_EX",
    "IP_REASSEMBLY_TIME_EXCEEDED",
    "IP_RECONFIG_SECFLTR",
    "IP_REQ_TIMED_OUT",
    "IP_ROUTER_DISC_INFO",
    "IP_ROUTER_MANAGER_VERSION",
    "IP_ROUTE_INFO",
    "IP_SOURCE_QUENCH",
    "IP_SPEC_MTU_CHANGE",
    "IP_STATS",
    "IP_STATUS_BASE",
    "IP_SUCCESS",
    "IP_TIME_EXCEEDED",
    "IP_TTL_EXPIRED_REASSEM",
    "IP_TTL_EXPIRED_TRANSIT",
    "IP_UNBIND_ADAPTER",
    "IP_UNIDIRECTIONAL_ADAPTER_ADDRESS",
    "IP_UNLOAD",
    "IP_UNRECOGNIZED_NEXT_HEADER",
    "Icmp6CreateFile",
    "Icmp6ParseReplies",
    "Icmp6SendEcho2",
    "IcmpCloseHandle",
    "IcmpCreateFile",
    "IcmpHandle",
    "IcmpParseReplies",
    "IcmpSendEcho",
    "IcmpSendEcho2",
    "IcmpSendEcho2Ex",
    "InitializeIpForwardEntry",
    "InitializeIpInterfaceEntry",
    "InitializeUnicastIpAddressEntry",
    "IpReleaseAddress",
    "IpRenewAddress",
    "LB_DST_ADDR_USE_DSTADDR_FLAG",
    "LB_DST_ADDR_USE_SRCADDR_FLAG",
    "LB_DST_MASK_LATE_FLAG",
    "LB_SRC_ADDR_USE_DSTADDR_FLAG",
    "LB_SRC_ADDR_USE_SRCADDR_FLAG",
    "LB_SRC_MASK_LATE_FLAG",
    "LookupPersistentTcpPortReservation",
    "LookupPersistentUdpPortReservation",
    "MAXLEN_IFDESCR",
    "MAXLEN_PHYSADDR",
    "MAX_ADAPTER_ADDRESS_LENGTH",
    "MAX_ADAPTER_DESCRIPTION_LENGTH",
    "MAX_ADAPTER_NAME",
    "MAX_ADAPTER_NAME_LENGTH",
    "MAX_DHCPV6_DUID_LENGTH",
    "MAX_DNS_SUFFIX_STRING_LENGTH",
    "MAX_DOMAIN_NAME_LEN",
    "MAX_HOSTNAME_LEN",
    "MAX_IF_TYPE",
    "MAX_INTERFACE_NAME_LEN",
    "MAX_IP_STATUS",
    "MAX_MIB_OFFSET",
    "MAX_OPT_SIZE",
    "MAX_SCOPE_ID_LEN",
    "MAX_SCOPE_NAME_LEN",
    "MCAST_BOUNDARY",
    "MCAST_GLOBAL",
    "MCAST_IF_ENTRY",
    "MCAST_MFE",
    "MCAST_MFE_STATS",
    "MCAST_MFE_STATS_EX",
    "MCAST_SCOPE",
    "MIBICMPINFO",
    "MIBICMPSTATS",
    "MIBICMPSTATS_EX_XPSP1",
    "MIB_ANYCASTIPADDRESS_ROW",
    "MIB_ANYCASTIPADDRESS_TABLE",
    "MIB_BEST_IF",
    "MIB_BOUNDARYROW",
    "MIB_ICMP",
    "MIB_ICMP_EX_XPSP1",
    "MIB_IFNUMBER",
    "MIB_IFROW",
    "MIB_IFSTACK_ROW",
    "MIB_IFSTACK_TABLE",
    "MIB_IFSTATUS",
    "MIB_IFTABLE",
    "MIB_IF_ADMIN_STATUS_DOWN",
    "MIB_IF_ADMIN_STATUS_TESTING",
    "MIB_IF_ADMIN_STATUS_UP",
    "MIB_IF_ENTRY_LEVEL",
    "MIB_IF_ENTRY_LEVEL_MibIfEntryNormal",
    "MIB_IF_ENTRY_LEVEL_MibIfEntryNormalWithoutStatistics",
    "MIB_IF_ROW2",
    "MIB_IF_TABLE2",
    "MIB_IF_TABLE_LEVEL",
    "MIB_IF_TABLE_LEVEL_MibIfTableNormal",
    "MIB_IF_TABLE_LEVEL_MibIfTableNormalWithoutStatistics",
    "MIB_IF_TABLE_LEVEL_MibIfTableRaw",
    "MIB_IF_TYPE_ETHERNET",
    "MIB_IF_TYPE_FDDI",
    "MIB_IF_TYPE_LOOPBACK",
    "MIB_IF_TYPE_OTHER",
    "MIB_IF_TYPE_PPP",
    "MIB_IF_TYPE_SLIP",
    "MIB_IF_TYPE_TOKENRING",
    "MIB_INVALID_TEREDO_PORT_NUMBER",
    "MIB_INVERTEDIFSTACK_ROW",
    "MIB_INVERTEDIFSTACK_TABLE",
    "MIB_IPADDRROW_W2K",
    "MIB_IPADDRROW_XP",
    "MIB_IPADDRTABLE",
    "MIB_IPADDR_DELETED",
    "MIB_IPADDR_DISCONNECTED",
    "MIB_IPADDR_DNS_ELIGIBLE",
    "MIB_IPADDR_DYNAMIC",
    "MIB_IPADDR_PRIMARY",
    "MIB_IPADDR_TRANSIENT",
    "MIB_IPDESTROW",
    "MIB_IPDESTTABLE",
    "MIB_IPFORWARDNUMBER",
    "MIB_IPFORWARDROW",
    "MIB_IPFORWARDTABLE",
    "MIB_IPFORWARD_ROW2",
    "MIB_IPFORWARD_TABLE2",
    "MIB_IPFORWARD_TYPE",
    "MIB_IPINTERFACE_ROW",
    "MIB_IPINTERFACE_TABLE",
    "MIB_IPMCAST_BOUNDARY",
    "MIB_IPMCAST_BOUNDARY_TABLE",
    "MIB_IPMCAST_GLOBAL",
    "MIB_IPMCAST_IF_ENTRY",
    "MIB_IPMCAST_IF_TABLE",
    "MIB_IPMCAST_MFE",
    "MIB_IPMCAST_MFE_STATS",
    "MIB_IPMCAST_MFE_STATS_EX_XP",
    "MIB_IPMCAST_OIF_STATS_LH",
    "MIB_IPMCAST_OIF_STATS_W2K",
    "MIB_IPMCAST_OIF_W2K",
    "MIB_IPMCAST_OIF_XP",
    "MIB_IPMCAST_SCOPE",
    "MIB_IPNETROW_LH",
    "MIB_IPNETROW_W2K",
    "MIB_IPNETTABLE",
    "MIB_IPNET_ROW2",
    "MIB_IPNET_TABLE2",
    "MIB_IPNET_TYPE",
    "MIB_IPNET_TYPE_DYNAMIC",
    "MIB_IPNET_TYPE_INVALID",
    "MIB_IPNET_TYPE_OTHER",
    "MIB_IPNET_TYPE_STATIC",
    "MIB_IPPATH_ROW",
    "MIB_IPPATH_TABLE",
    "MIB_IPROUTE_METRIC_UNUSED",
    "MIB_IPROUTE_TYPE_DIRECT",
    "MIB_IPROUTE_TYPE_INDIRECT",
    "MIB_IPROUTE_TYPE_INVALID",
    "MIB_IPROUTE_TYPE_OTHER",
    "MIB_IPSTATS_FORWARDING",
    "MIB_IPSTATS_LH",
    "MIB_IPSTATS_W2K",
    "MIB_IP_FORWARDING",
    "MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES",
    "MIB_IP_NOT_FORWARDING",
    "MIB_MCAST_LIMIT_ROW",
    "MIB_MFE_STATS_TABLE",
    "MIB_MFE_STATS_TABLE_EX_XP",
    "MIB_MFE_TABLE",
    "MIB_MULTICASTIPADDRESS_ROW",
    "MIB_MULTICASTIPADDRESS_TABLE",
    "MIB_NOTIFICATION_TYPE",
    "MIB_NOTIFICATION_TYPE_MibAddInstance",
    "MIB_NOTIFICATION_TYPE_MibDeleteInstance",
    "MIB_NOTIFICATION_TYPE_MibInitialNotification",
    "MIB_NOTIFICATION_TYPE_MibParameterNotification",
    "MIB_OPAQUE_INFO",
    "MIB_OPAQUE_QUERY",
    "MIB_PROXYARP",
    "MIB_ROUTESTATE",
    "MIB_TCP6ROW",
    "MIB_TCP6ROW2",
    "MIB_TCP6ROW_OWNER_MODULE",
    "MIB_TCP6ROW_OWNER_PID",
    "MIB_TCP6TABLE",
    "MIB_TCP6TABLE2",
    "MIB_TCP6TABLE_OWNER_MODULE",
    "MIB_TCP6TABLE_OWNER_PID",
    "MIB_TCPROW2",
    "MIB_TCPROW_LH",
    "MIB_TCPROW_OWNER_MODULE",
    "MIB_TCPROW_OWNER_PID",
    "MIB_TCPROW_W2K",
    "MIB_TCPSTATS2",
    "MIB_TCPSTATS_LH",
    "MIB_TCPSTATS_W2K",
    "MIB_TCPTABLE",
    "MIB_TCPTABLE2",
    "MIB_TCPTABLE_OWNER_MODULE",
    "MIB_TCPTABLE_OWNER_PID",
    "MIB_TCP_STATE",
    "MIB_TCP_STATE_CLOSED",
    "MIB_TCP_STATE_CLOSE_WAIT",
    "MIB_TCP_STATE_CLOSING",
    "MIB_TCP_STATE_DELETE_TCB",
    "MIB_TCP_STATE_ESTAB",
    "MIB_TCP_STATE_FIN_WAIT1",
    "MIB_TCP_STATE_FIN_WAIT2",
    "MIB_TCP_STATE_LAST_ACK",
    "MIB_TCP_STATE_LISTEN",
    "MIB_TCP_STATE_RESERVED",
    "MIB_TCP_STATE_SYN_RCVD",
    "MIB_TCP_STATE_SYN_SENT",
    "MIB_TCP_STATE_TIME_WAIT",
    "MIB_UDP6ROW",
    "MIB_UDP6ROW2",
    "MIB_UDP6ROW_OWNER_MODULE",
    "MIB_UDP6ROW_OWNER_PID",
    "MIB_UDP6TABLE",
    "MIB_UDP6TABLE2",
    "MIB_UDP6TABLE_OWNER_MODULE",
    "MIB_UDP6TABLE_OWNER_PID",
    "MIB_UDPROW",
    "MIB_UDPROW2",
    "MIB_UDPROW_OWNER_MODULE",
    "MIB_UDPROW_OWNER_PID",
    "MIB_UDPSTATS",
    "MIB_UDPSTATS2",
    "MIB_UDPTABLE",
    "MIB_UDPTABLE2",
    "MIB_UDPTABLE_OWNER_MODULE",
    "MIB_UDPTABLE_OWNER_PID",
    "MIB_UNICASTIPADDRESS_ROW",
    "MIB_UNICASTIPADDRESS_TABLE",
    "MIB_USE_CURRENT_FORWARDING",
    "MIB_USE_CURRENT_TTL",
    "MIN_IF_TYPE",
    "MIXED_NODETYPE",
    "ND_NEIGHBOR_ADVERT",
    "ND_NEIGHBOR_SOLICIT",
    "ND_REDIRECT",
    "ND_ROUTER_ADVERT",
    "ND_ROUTER_SOLICIT",
    "NET_ADDRESS_DNS_NAME",
    "NET_ADDRESS_FORMAT",
    "NET_ADDRESS_FORMAT_UNSPECIFIED",
    "NET_ADDRESS_IPV4",
    "NET_ADDRESS_IPV6",
    "NET_STRING_IPV4_ADDRESS",
    "NET_STRING_IPV4_NETWORK",
    "NET_STRING_IPV4_SERVICE",
    "NET_STRING_IPV6_ADDRESS",
    "NET_STRING_IPV6_ADDRESS_NO_SCOPE",
    "NET_STRING_IPV6_NETWORK",
    "NET_STRING_IPV6_SERVICE",
    "NET_STRING_IPV6_SERVICE_NO_SCOPE",
    "NET_STRING_NAMED_ADDRESS",
    "NET_STRING_NAMED_SERVICE",
    "NUMBER_OF_EXPORTED_VARIABLES",
    "NhpAllocateAndGetInterfaceInfoFromStack",
    "NotifyAddrChange",
    "NotifyIpInterfaceChange",
    "NotifyNetworkConnectivityHintChange",
    "NotifyRouteChange",
    "NotifyRouteChange2",
    "NotifyStableUnicastIpAddressTable",
    "NotifyTeredoPortChange",
    "NotifyUnicastIpAddressChange",
    "PEER_TO_PEER_NODETYPE",
    "PFADDRESSTYPE",
    "PFERROR_BUFFER_TOO_SMALL",
    "PFERROR_NO_FILTERS_GIVEN",
    "PFERROR_NO_PF_INTERFACE",
    "PFFORWARD_ACTION",
    "PFFRAMETYPE",
    "PFFT_FILTER",
    "PFFT_FRAG",
    "PFFT_SPOOF",
    "PFLOGFRAME",
    "PF_ACTION_DROP",
    "PF_ACTION_FORWARD",
    "PF_FILTER_DESCRIPTOR",
    "PF_FILTER_STATS",
    "PF_INTERFACE_STATS",
    "PF_IPV4",
    "PF_IPV6",
    "PF_LATEBIND_INFO",
    "PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK",
    "PIPFORWARD_CHANGE_CALLBACK",
    "PIPINTERFACE_CHANGE_CALLBACK",
    "PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK",
    "PROXY_ARP",
    "PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK",
    "PTEREDO_PORT_CHANGE_CALLBACK",
    "PUNICAST_IPADDRESS_CHANGE_CALLBACK",
    "PfAddFiltersToInterface",
    "PfAddGlobalFilterToInterface",
    "PfBindInterfaceToIPAddress",
    "PfBindInterfaceToIndex",
    "PfCreateInterface",
    "PfDeleteInterface",
    "PfDeleteLog",
    "PfGetInterfaceStatistics",
    "PfMakeLog",
    "PfRebindFilters",
    "PfRemoveFilterHandles",
    "PfRemoveFiltersFromInterface",
    "PfRemoveGlobalFilterFromInterface",
    "PfSetLogBuffer",
    "PfTestPacket",
    "PfUnBindInterface",
    "ROUTE_LONGER",
    "ROUTE_MATCHING",
    "ROUTE_SHORTER",
    "ROUTE_STATE",
    "RegisterInterfaceTimestampConfigChange",
    "ResolveIpNetEntry2",
    "ResolveNeighbor",
    "RestoreMediaSense",
    "SendARP",
    "SetCurrentThreadCompartmentId",
    "SetCurrentThreadCompartmentScope",
    "SetDnsSettings",
    "SetIfEntry",
    "SetInterfaceDnsSettings",
    "SetIpForwardEntry",
    "SetIpForwardEntry2",
    "SetIpInterfaceEntry",
    "SetIpNetEntry",
    "SetIpNetEntry2",
    "SetIpStatistics",
    "SetIpStatisticsEx",
    "SetIpTTL",
    "SetJobCompartmentId",
    "SetNetworkInformation",
    "SetPerTcp6ConnectionEStats",
    "SetPerTcpConnectionEStats",
    "SetSessionCompartmentId",
    "SetTcpEntry",
    "SetUnicastIpAddressEntry",
    "TCP6_STATS",
    "TCPIP_OWNER_MODULE_BASIC_INFO",
    "TCPIP_OWNER_MODULE_INFO_BASIC",
    "TCPIP_OWNER_MODULE_INFO_CLASS",
    "TCPIP_OWNING_MODULE_SIZE",
    "TCP_BOOLEAN_OPTIONAL",
    "TCP_BOOLEAN_OPTIONAL_TcpBoolOptDisabled",
    "TCP_BOOLEAN_OPTIONAL_TcpBoolOptEnabled",
    "TCP_BOOLEAN_OPTIONAL_TcpBoolOptUnchanged",
    "TCP_CONNECTION_OFFLOAD_STATE",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateInHost",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateMax",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloaded",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateOffloading",
    "TCP_CONNECTION_OFFLOAD_STATE_TcpConnectionOffloadStateUploading",
    "TCP_ESTATS_BANDWIDTH_ROD_v0",
    "TCP_ESTATS_BANDWIDTH_RW_v0",
    "TCP_ESTATS_DATA_ROD_v0",
    "TCP_ESTATS_DATA_RW_v0",
    "TCP_ESTATS_FINE_RTT_ROD_v0",
    "TCP_ESTATS_FINE_RTT_RW_v0",
    "TCP_ESTATS_OBS_REC_ROD_v0",
    "TCP_ESTATS_OBS_REC_RW_v0",
    "TCP_ESTATS_PATH_ROD_v0",
    "TCP_ESTATS_PATH_RW_v0",
    "TCP_ESTATS_REC_ROD_v0",
    "TCP_ESTATS_REC_RW_v0",
    "TCP_ESTATS_SEND_BUFF_ROD_v0",
    "TCP_ESTATS_SEND_BUFF_RW_v0",
    "TCP_ESTATS_SND_CONG_ROD_v0",
    "TCP_ESTATS_SND_CONG_ROS_v0",
    "TCP_ESTATS_SND_CONG_RW_v0",
    "TCP_ESTATS_SYN_OPTS_ROS_v0",
    "TCP_ESTATS_TYPE",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsBandwidth",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsData",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsFineRtt",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsMaximum",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsObsRec",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsPath",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsRec",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsSendBuff",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsSndCong",
    "TCP_ESTATS_TYPE_TcpConnectionEstatsSynOpts",
    "TCP_RESERVE_PORT_RANGE",
    "TCP_ROW",
    "TCP_RTO_ALGORITHM",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_CONSTANT",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_OTHER",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_RSRE",
    "TCP_RTO_ALGORITHM_MIB_TCP_RTO_VANJ",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmConstant",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmOther",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmRsre",
    "TCP_RTO_ALGORITHM_TcpRtoAlgorithmVanj",
    "TCP_SOFT_ERROR",
    "TCP_SOFT_ERROR_TcpErrorAboveAckWindow",
    "TCP_SOFT_ERROR_TcpErrorAboveDataWindow",
    "TCP_SOFT_ERROR_TcpErrorAboveTsWindow",
    "TCP_SOFT_ERROR_TcpErrorBelowAckWindow",
    "TCP_SOFT_ERROR_TcpErrorBelowDataWindow",
    "TCP_SOFT_ERROR_TcpErrorBelowTsWindow",
    "TCP_SOFT_ERROR_TcpErrorDataChecksumError",
    "TCP_SOFT_ERROR_TcpErrorDataLengthError",
    "TCP_SOFT_ERROR_TcpErrorMaxSoftError",
    "TCP_SOFT_ERROR_TcpErrorNone",
    "TCP_STATS",
    "TCP_TABLE",
    "TCP_TABLE_BASIC_ALL",
    "TCP_TABLE_BASIC_CONNECTIONS",
    "TCP_TABLE_BASIC_LISTENER",
    "TCP_TABLE_CLASS",
    "TCP_TABLE_OWNER_MODULE_ALL",
    "TCP_TABLE_OWNER_MODULE_CONNECTIONS",
    "TCP_TABLE_OWNER_MODULE_LISTENER",
    "TCP_TABLE_OWNER_PID_ALL",
    "TCP_TABLE_OWNER_PID_CONNECTIONS",
    "TCP_TABLE_OWNER_PID_LISTENER",
    "UDP6_STATS",
    "UDP_ROW",
    "UDP_STATS",
    "UDP_TABLE",
    "UDP_TABLE_BASIC",
    "UDP_TABLE_CLASS",
    "UDP_TABLE_OWNER_MODULE",
    "UDP_TABLE_OWNER_PID",
    "UnenableRouter",
    "UnregisterInterfaceTimestampConfigChange",
    "if_indextoname",
    "if_nametoindex",
]
_arch_optional = [
    "ICMP_ECHO_REPLY32",
    "IP_OPTION_INFORMATION32",
]
