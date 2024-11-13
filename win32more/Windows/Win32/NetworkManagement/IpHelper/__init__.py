from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.IpHelper
import win32more.Windows.Win32.NetworkManagement.Ndis
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.System.IO
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
DNS_INTERFACE_SETTINGS_VERSION4: UInt32 = 4
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
DNS_SETTING_ENCRYPTED_DNS_ADAPTER_FLAGS: UInt32 = 16384
DNS_SETTING_DDR: UInt32 = 32768
DNS_ENABLE_DOH: UInt32 = 1
DNS_DOH_POLICY_NOT_CONFIGURED: UInt32 = 4
DNS_DOH_POLICY_DISABLE: UInt32 = 8
DNS_DOH_POLICY_AUTO: UInt32 = 16
DNS_DOH_POLICY_REQUIRED: UInt32 = 32
DNS_ENABLE_DDR: UInt32 = 64
DNS_SERVER_PROPERTY_VERSION1: UInt32 = 1
DNS_DOH_SERVER_SETTINGS_ENABLE_AUTO: UInt32 = 1
DNS_DOH_SERVER_SETTINGS_ENABLE: UInt32 = 2
DNS_DOH_SERVER_SETTINGS_FALLBACK_TO_UDP: UInt32 = 4
DNS_DOH_AUTO_UPGRADE_SERVER: UInt32 = 8
DNS_DOH_SERVER_SETTINGS_ENABLE_DDR: UInt32 = 16
DNS_DDR_ADAPTER_ENABLE_DOH: UInt32 = 1
DNS_DDR_ADAPTER_ENABLE_UDP_FALLBACK: UInt32 = 2
TCPIP_OWNING_MODULE_SIZE: UInt32 = 16
FILTER_ICMP_TYPE_ANY: Byte = 255
FILTER_ICMP_CODE_ANY: Byte = 255
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
INTERFACE_TIMESTAMP_CAPABILITIES_VERSION_1: UInt32 = 1
INTERFACE_HARDWARE_CROSSTIMESTAMP_VERSION_1: UInt32 = 1
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
def IcmpCreateFile() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('IPHLPAPI.dll')
def Icmp6CreateFile() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('IPHLPAPI.dll')
def IcmpCloseHandle(IcmpHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IPHLPAPI.dll')
def IcmpSendEcho(IcmpHandle: win32more.Windows.Win32.Foundation.HANDLE, DestinationAddress: UInt32, RequestData: VoidPtr, RequestSize: UInt16, RequestOptions: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION), ReplyBuffer: VoidPtr, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IcmpSendEcho2(IcmpHandle: win32more.Windows.Win32.Foundation.HANDLE, Event: win32more.Windows.Win32.Foundation.HANDLE, ApcRoutine: win32more.Windows.Win32.System.IO.PIO_APC_ROUTINE, ApcContext: VoidPtr, DestinationAddress: UInt32, RequestData: VoidPtr, RequestSize: UInt16, RequestOptions: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION), ReplyBuffer: VoidPtr, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IcmpSendEcho2Ex(IcmpHandle: win32more.Windows.Win32.Foundation.HANDLE, Event: win32more.Windows.Win32.Foundation.HANDLE, ApcRoutine: win32more.Windows.Win32.System.IO.PIO_APC_ROUTINE, ApcContext: VoidPtr, SourceAddress: UInt32, DestinationAddress: UInt32, RequestData: VoidPtr, RequestSize: UInt16, RequestOptions: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION), ReplyBuffer: VoidPtr, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def Icmp6SendEcho2(IcmpHandle: win32more.Windows.Win32.Foundation.HANDLE, Event: win32more.Windows.Win32.Foundation.HANDLE, ApcRoutine: win32more.Windows.Win32.System.IO.PIO_APC_ROUTINE, ApcContext: VoidPtr, SourceAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN6), DestinationAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN6), RequestData: VoidPtr, RequestSize: UInt16, RequestOptions: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION), ReplyBuffer: VoidPtr, ReplySize: UInt32, Timeout: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IcmpParseReplies(ReplyBuffer: VoidPtr, ReplySize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def Icmp6ParseReplies(ReplyBuffer: VoidPtr, ReplySize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetNumberOfInterfaces(pdwNumIf: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIfEntry(pIfRow: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IFROW)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIfTable(pIfTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IFTABLE), pdwSize: POINTER(UInt32), bOrder: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpAddrTable(pIpAddrTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPADDRTABLE), pdwSize: POINTER(UInt32), bOrder: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetTable(IpNetTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETTABLE), SizePointer: POINTER(UInt32), Order: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpForwardTable(pIpForwardTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDTABLE), pdwSize: POINTER(UInt32), bOrder: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpTable(TcpTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPTABLE), SizePointer: POINTER(UInt32), Order: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetExtendedTcpTable(pTcpTable: VoidPtr, pdwSize: POINTER(UInt32), bOrder: win32more.Windows.Win32.Foundation.BOOL, ulAf: UInt32, TableClass: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS, Reserved: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromTcpEntry(pTcpEntry: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_MODULE), Class: win32more.Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: VoidPtr, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpTable(UdpTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPTABLE), SizePointer: POINTER(UInt32), Order: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetExtendedUdpTable(pUdpTable: VoidPtr, pdwSize: POINTER(UInt32), bOrder: win32more.Windows.Win32.Foundation.BOOL, ulAf: UInt32, TableClass: win32more.Windows.Win32.NetworkManagement.IpHelper.UDP_TABLE_CLASS, Reserved: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromUdpEntry(pUdpEntry: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_MODULE), Class: win32more.Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: VoidPtr, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpTable2(TcpTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPTABLE2), SizePointer: POINTER(UInt32), Order: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcp6Table(TcpTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6TABLE), SizePointer: POINTER(UInt32), Order: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcp6Table2(TcpTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6TABLE2), SizePointer: POINTER(UInt32), Order: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetPerTcpConnectionEStats(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH), EstatsType: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: POINTER(Byte), RwVersion: UInt32, RwSize: UInt32, Ros: POINTER(Byte), RosVersion: UInt32, RosSize: UInt32, Rod: POINTER(Byte), RodVersion: UInt32, RodSize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetPerTcpConnectionEStats(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH), EstatsType: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: POINTER(Byte), RwVersion: UInt32, RwSize: UInt32, Offset: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetPerTcp6ConnectionEStats(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW), EstatsType: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: POINTER(Byte), RwVersion: UInt32, RwSize: UInt32, Ros: POINTER(Byte), RosVersion: UInt32, RosSize: UInt32, Rod: POINTER(Byte), RodVersion: UInt32, RodSize: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetPerTcp6ConnectionEStats(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW), EstatsType: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE, Rw: POINTER(Byte), RwVersion: UInt32, RwSize: UInt32, Offset: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromTcp6Entry(pTcpEntry: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_MODULE), Class: win32more.Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: VoidPtr, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdp6Table(Udp6Table: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6TABLE), SizePointer: POINTER(UInt32), Order: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromUdp6Entry(pUdpEntry: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_MODULE), Class: win32more.Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: VoidPtr, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetOwnerModuleFromPidAndInfo(ulPid: UInt32, pInfo: POINTER(UInt64), Class: win32more.Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS, pBuffer: VoidPtr, pdwSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpStatistics(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIcmpStatistics(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_ICMP)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpStatistics(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPSTATS_LH)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpStatistics(Stats: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPSTATS)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpStatisticsEx(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpStatisticsEx(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIcmpStatisticsEx(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_ICMP_EX_XPSP1), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpStatisticsEx(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPSTATS_LH), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpStatisticsEx(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPSTATS), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetTcpStatisticsEx2(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPSTATS2), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUdpStatisticsEx2(Statistics: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPSTATS2), Family: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIfEntry(pIfRow: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IFROW)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpForwardEntry(pRoute: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpForwardEntry(pRoute: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpForwardEntry(pRoute: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpStatistics(pIpStats: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_LH)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpTTL(nTTL: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpNetEntry(pArpEntry: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetIpNetEntry(pArpEntry: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpNetEntry(pArpEntry: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def FlushIpNetTable(dwIfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CreateProxyArpEntry(dwAddress: UInt32, dwMask: UInt32, dwIfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteProxyArpEntry(dwAddress: UInt32, dwMask: UInt32, dwIfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SetTcpEntry(pTcpRow: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceInfo(pIfTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_INTERFACE_INFO), dwOutBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetUniDirectionalAdapterInfo(pIPIfInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_UNIDIRECTIONAL_ADAPTER_ADDRESS), dwOutBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def NhpAllocateAndGetInterfaceInfoFromStack(ppTable: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_INTERFACE_NAME_INFO_W2KSP1)), pdwCount: POINTER(UInt32), bOrder: win32more.Windows.Win32.Foundation.BOOL, hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetBestInterface(dwDestAddr: UInt32, pdwBestIfIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetBestInterfaceEx(pDestAddr: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR), pdwBestIfIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetBestRoute(dwDestAddr: UInt32, dwSourceAddr: UInt32, pBestRoute: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def NotifyAddrChange(Handle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def NotifyRouteChange(Handle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CancelIPChangeNotify(notifyOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IPHLPAPI.dll')
def GetAdapterIndex(AdapterName: win32more.Windows.Win32.Foundation.PWSTR, IfIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def AddIPAddress(Address: UInt32, IpMask: UInt32, IfIndex: UInt32, NTEContext: POINTER(UInt32), NTEInstance: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIPAddress(NTEContext: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkParams(pFixedInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.FIXED_INFO_W2KSP1), pOutBufLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetAdaptersInfo(AdapterInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INFO), SizePointer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetAdapterOrderMap() -> POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ORDER_MAP): ...
@winfunctype('IPHLPAPI.dll')
def GetAdaptersAddresses(Family: UInt32, Flags: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS, Reserved: VoidPtr, AdapterAddresses: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_LH), SizePointer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetPerAdapterInfo(IfIndex: UInt32, pPerAdapterInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_PER_ADAPTER_INFO_W2KSP1), pOutBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceActiveTimestampCapabilities(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), TimestampCapabilites: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceSupportedTimestampCapabilities(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), TimestampCapabilites: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def CaptureInterfaceHardwareCrossTimestamp(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), CrossTimestamp: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.INTERFACE_HARDWARE_CROSSTIMESTAMP)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def RegisterInterfaceTimestampConfigChange(Callback: win32more.Windows.Win32.NetworkManagement.IpHelper.PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK, CallerContext: VoidPtr, NotificationHandle: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def UnregisterInterfaceTimestampConfigChange(NotificationHandle: win32more.Windows.Win32.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE) -> Void: ...
@winfunctype('IPHLPAPI.DLL')
def GetInterfaceCurrentTimestampCapabilities(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), TimestampCapabilites: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES)) -> UInt32: ...
@winfunctype('IPHLPAPI.DLL')
def GetInterfaceHardwareTimestampCapabilities(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), TimestampCapabilites: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.INTERFACE_TIMESTAMP_CAPABILITIES)) -> UInt32: ...
@winfunctype('IPHLPAPI.DLL')
def NotifyIfTimestampConfigChange(CallerContext: VoidPtr, Callback: win32more.Windows.Win32.NetworkManagement.IpHelper.PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK, NotificationHandle: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE)) -> UInt32: ...
@winfunctype('IPHLPAPI.DLL')
def CancelIfTimestampConfigChange(NotificationHandle: win32more.Windows.Win32.NetworkManagement.IpHelper.HIFTIMESTAMPCHANGE) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def IpReleaseAddress(AdapterInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def IpRenewAddress(AdapterInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def SendARP(DestIP: UInt32, SrcIP: UInt32, pMacAddr: VoidPtr, PhyAddrLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetRTTAndHopCount(DestIpAddress: UInt32, HopCount: POINTER(UInt32), MaxHops: UInt32, RTT: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IPHLPAPI.dll')
def GetFriendlyIfIndex(IfIndex: UInt32) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def EnableRouter(pHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def UnenableRouter(pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpdwEnableCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def DisableMediaSense(pHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), pOverLapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def RestoreMediaSense(pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpdwEnableCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIpErrorString(ErrorCode: UInt32, Buffer: win32more.Windows.Win32.Foundation.PWSTR, Size: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def ResolveNeighbor(NetworkAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR), PhysicalAddress: VoidPtr, PhysicalAddressLength: POINTER(UInt32)) -> UInt32: ...
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
def ParseNetworkString(NetworkString: win32more.Windows.Win32.Foundation.PWSTR, Types: UInt32, AddressInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.NET_ADDRESS_INFO), PortNumber: POINTER(UInt16), PrefixLength: POINTER(Byte)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def GetIfEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIfEntry2Ex(Level: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ENTRY_LEVEL, Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIfTable2(Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE2))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIfTable2Ex(Level: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE_LEVEL, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE2))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIfStackTable(Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IFSTACK_TABLE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetInvertedIfStackTable(Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_TABLE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpInterfaceEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpInterfaceTable(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_TABLE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def InitializeIpInterfaceEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def NotifyIpInterfaceChange(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Callback: win32more.Windows.Win32.NetworkManagement.IpHelper.PIPINTERFACE_CHANGE_CALLBACK, CallerContext: VoidPtr, InitialNotification: win32more.Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def SetIpInterfaceEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetworkConnectionBandwidthEstimates(InterfaceIndex: UInt32, AddressFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, BandwidthEstimates: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def CreateUnicastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def DeleteUnicastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetUnicastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetUnicastIpAddressTable(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def InitializeUnicastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def NotifyUnicastIpAddressChange(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Callback: win32more.Windows.Win32.NetworkManagement.IpHelper.PUNICAST_IPADDRESS_CHANGE_CALLBACK, CallerContext: VoidPtr, InitialNotification: win32more.Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def NotifyStableUnicastIpAddressTable(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE)), CallerCallback: win32more.Windows.Win32.NetworkManagement.IpHelper.PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK, CallerContext: VoidPtr, NotificationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def SetUnicastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def CreateAnycastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def DeleteAnycastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetAnycastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetAnycastIpAddressTable(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_TABLE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetMulticastIpAddressEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetMulticastIpAddressTable(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_TABLE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpForwardEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpForwardEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetBestRoute2(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), InterfaceIndex: UInt32, SourceAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET), DestinationAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET), AddressSortOptions: UInt32, BestRoute: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2), BestSourceAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpForwardEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpForwardTable2(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TABLE2))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def InitializeIpForwardEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def NotifyRouteChange2(AddressFamily: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Callback: win32more.Windows.Win32.NetworkManagement.IpHelper.PIPFORWARD_CHANGE_CALLBACK, CallerContext: VoidPtr, InitialNotification: win32more.Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def SetIpForwardEntry2(Route: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def FlushIpPathTable(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpPathEntry(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPPATH_ROW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpPathTable(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPPATH_TABLE))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def CreateIpNetEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def DeleteIpNetEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def FlushIpNetTable2(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, InterfaceIndex: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetIpNetTable2(Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY, Table: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TABLE2))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ResolveIpNetEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2), SourceAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def SetIpNetEntry2(Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def NotifyTeredoPortChange(Callback: win32more.Windows.Win32.NetworkManagement.IpHelper.PTEREDO_PORT_CHANGE_CALLBACK, CallerContext: VoidPtr, InitialNotification: win32more.Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetTeredoPort(Port: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def CancelMibChangeNotify2(NotificationHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def FreeMibTable(Memory: VoidPtr) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def CreateSortedAddressPairs(SourceAddressList: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN6), SourceAddressCount: UInt32, DestinationAddressList: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN6), DestinationAddressCount: UInt32, AddressSortOptions: UInt32, SortedAddressPairList: POINTER(POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN6_PAIR)), SortedAddressPairCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertCompartmentGuidToId(CompartmentGuid: POINTER(Guid), CompartmentId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertCompartmentIdToGuid(CompartmentId: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID, CompartmentGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceNameToLuidA(InterfaceName: win32more.Windows.Win32.Foundation.PSTR, InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceNameToLuidW(InterfaceName: win32more.Windows.Win32.Foundation.PWSTR, InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
ConvertInterfaceNameToLuid = UnicodeAlias('ConvertInterfaceNameToLuidW')
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToNameA(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), InterfaceName: win32more.Windows.Win32.Foundation.PSTR, Length: UIntPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToNameW(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), InterfaceName: win32more.Windows.Win32.Foundation.PWSTR, Length: UIntPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
ConvertInterfaceLuidToName = UnicodeAlias('ConvertInterfaceLuidToNameW')
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToIndex(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), InterfaceIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceIndexToLuid(InterfaceIndex: UInt32, InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToAlias(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), InterfaceAlias: win32more.Windows.Win32.Foundation.PWSTR, Length: UIntPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceAliasToLuid(InterfaceAlias: win32more.Windows.Win32.Foundation.PWSTR, InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceLuidToGuid(InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH), InterfaceGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertInterfaceGuidToLuid(InterfaceGuid: POINTER(Guid), InterfaceLuid: POINTER(win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def if_nametoindex(InterfaceName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def if_indextoname(InterfaceIndex: UInt32, InterfaceName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('IPHLPAPI.dll')
def GetCurrentThreadCompartmentId() -> win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID: ...
@winfunctype('IPHLPAPI.dll')
def SetCurrentThreadCompartmentId(CompartmentId: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetCurrentThreadCompartmentScope(CompartmentScope: POINTER(UInt32), CompartmentId: POINTER(UInt32)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def SetCurrentThreadCompartmentScope(CompartmentScope: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetJobCompartmentId(JobHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID: ...
@winfunctype('IPHLPAPI.dll')
def SetJobCompartmentId(JobHandle: win32more.Windows.Win32.Foundation.HANDLE, CompartmentId: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetSessionCompartmentId(SessionId: UInt32) -> win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID: ...
@winfunctype('IPHLPAPI.dll')
def SetSessionCompartmentId(SessionId: UInt32, CompartmentId: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetDefaultCompartmentId() -> win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkInformation(NetworkGuid: POINTER(Guid), CompartmentId: POINTER(UInt32), SiteId: POINTER(UInt32), NetworkName: win32more.Windows.Win32.Foundation.PWSTR, Length: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def SetNetworkInformation(NetworkGuid: POINTER(Guid), CompartmentId: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID, NetworkName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertLengthToIpv4Mask(MaskLength: UInt32, Mask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def ConvertIpv4MaskToLength(Mask: UInt32, MaskLength: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetDnsSettings(Settings: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SETTINGS)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def FreeDnsSettings(Settings: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SETTINGS)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def SetDnsSettings(Settings: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SETTINGS)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetInterfaceDnsSettings(Interface: Guid, Settings: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def FreeInterfaceDnsSettings(Settings: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS)) -> Void: ...
@winfunctype('IPHLPAPI.dll')
def SetInterfaceDnsSettings(Interface: Guid, Settings: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkConnectivityHint(ConnectivityHint: POINTER(win32more.Windows.Win32.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def GetNetworkConnectivityHintForInterface(InterfaceIndex: UInt32, ConnectivityHint: POINTER(win32more.Windows.Win32.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def NotifyNetworkConnectivityHintChange(Callback: win32more.Windows.Win32.NetworkManagement.IpHelper.PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK, CallerContext: VoidPtr, InitialNotification: win32more.Windows.Win32.Foundation.BOOLEAN, NotificationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('IPHLPAPI.dll')
def PfCreateInterface(dwName: UInt32, inAction: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION, outAction: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION, bUseLog: win32more.Windows.Win32.Foundation.BOOL, bMustBeUnique: win32more.Windows.Win32.Foundation.BOOL, ppInterface: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfDeleteInterface(pInterface: VoidPtr) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfAddFiltersToInterface(ih: VoidPtr, cInFilters: UInt32, pfiltIn: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR), cOutFilters: UInt32, pfiltOut: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR), pfHandle: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRemoveFiltersFromInterface(ih: VoidPtr, cInFilters: UInt32, pfiltIn: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR), cOutFilters: UInt32, pfiltOut: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRemoveFilterHandles(pInterface: VoidPtr, cFilters: UInt32, pvHandles: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfUnBindInterface(pInterface: VoidPtr) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfBindInterfaceToIndex(pInterface: VoidPtr, dwIndex: UInt32, pfatLinkType: win32more.Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE, LinkIPAddress: POINTER(Byte)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfBindInterfaceToIPAddress(pInterface: VoidPtr, pfatType: win32more.Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE, IPAddress: POINTER(Byte)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRebindFilters(pInterface: VoidPtr, pLateBindInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.PF_LATEBIND_INFO)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfAddGlobalFilterToInterface(pInterface: VoidPtr, gfFilter: win32more.Windows.Win32.NetworkManagement.IpHelper.GLOBAL_FILTER) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfRemoveGlobalFilterFromInterface(pInterface: VoidPtr, gfFilter: win32more.Windows.Win32.NetworkManagement.IpHelper.GLOBAL_FILTER) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfMakeLog(hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfSetLogBuffer(pbBuffer: POINTER(Byte), dwSize: UInt32, dwThreshold: UInt32, dwEntries: UInt32, pdwLoggedEntries: POINTER(UInt32), pdwLostEntries: POINTER(UInt32), pdwSizeUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfDeleteLog() -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfGetInterfaceStatistics(pInterface: VoidPtr, ppfStats: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.PF_INTERFACE_STATS), pdwBufferSize: POINTER(UInt32), fResetCounters: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('IPHLPAPI.dll')
def PfTestPacket(pInInterface: VoidPtr, pOutInterface: VoidPtr, cBytes: UInt32, pbPacket: POINTER(Byte), ppAction: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION)) -> UInt32: ...
class DNS_DOH_SERVER_SETTINGS(Structure):
    Template: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt64
class DNS_INTERFACE_SETTINGS(Structure):
    Version: UInt32
    Flags: UInt64
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    NameServer: win32more.Windows.Win32.Foundation.PWSTR
    SearchList: win32more.Windows.Win32.Foundation.PWSTR
    RegistrationEnabled: UInt32
    RegisterAdapterName: UInt32
    EnableLLMNR: UInt32
    QueryAdapterName: UInt32
    ProfileNameServer: win32more.Windows.Win32.Foundation.PWSTR
class DNS_INTERFACE_SETTINGS3(Structure):
    Version: UInt32
    Flags: UInt64
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    NameServer: win32more.Windows.Win32.Foundation.PWSTR
    SearchList: win32more.Windows.Win32.Foundation.PWSTR
    RegistrationEnabled: UInt32
    RegisterAdapterName: UInt32
    EnableLLMNR: UInt32
    QueryAdapterName: UInt32
    ProfileNameServer: win32more.Windows.Win32.Foundation.PWSTR
    DisableUnconstrainedQueries: UInt32
    SupplementalSearchList: win32more.Windows.Win32.Foundation.PWSTR
    cServerProperties: UInt32
    ServerProperties: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY)
    cProfileServerProperties: UInt32
    ProfileServerProperties: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY)
class DNS_INTERFACE_SETTINGS4(Structure):
    Version: UInt32
    Flags: UInt64
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    NameServer: win32more.Windows.Win32.Foundation.PWSTR
    SearchList: win32more.Windows.Win32.Foundation.PWSTR
    RegistrationEnabled: UInt32
    RegisterAdapterName: UInt32
    EnableLLMNR: UInt32
    QueryAdapterName: UInt32
    ProfileNameServer: win32more.Windows.Win32.Foundation.PWSTR
    DisableUnconstrainedQueries: UInt32
    SupplementalSearchList: win32more.Windows.Win32.Foundation.PWSTR
    cServerProperties: UInt32
    ServerProperties: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY)
    cProfileServerProperties: UInt32
    ProfileServerProperties: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY)
    EncryptedDnsAdapterFlags: UInt32
class DNS_INTERFACE_SETTINGS_EX(Structure):
    SettingsV1: win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_INTERFACE_SETTINGS
    DisableUnconstrainedQueries: UInt32
    SupplementalSearchList: win32more.Windows.Win32.Foundation.PWSTR
class DNS_SERVER_PROPERTY(Structure):
    Version: UInt32
    ServerIndex: UInt32
    Type: win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPE
    Property: win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPES
DNS_SERVER_PROPERTY_TYPE = Int32
DnsServerInvalidProperty: win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPE = 0
DnsServerDohProperty: win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_SERVER_PROPERTY_TYPE = 1
class DNS_SERVER_PROPERTY_TYPES(Union):
    DohSettings: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.DNS_DOH_SERVER_SETTINGS)
class DNS_SETTINGS(Structure):
    Version: UInt32
    Flags: UInt64
    Hostname: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    SearchList: win32more.Windows.Win32.Foundation.PWSTR
class DNS_SETTINGS2(Structure):
    Version: UInt32
    Flags: UInt64
    Hostname: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    SearchList: win32more.Windows.Win32.Foundation.PWSTR
    SettingFlags: UInt64
class FIXED_INFO_W2KSP1(Structure):
    HostName: win32more.Windows.Win32.Foundation.CHAR * 132
    DomainName: win32more.Windows.Win32.Foundation.CHAR * 132
    CurrentDnsServer: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING)
    DnsServerList: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    NodeType: UInt32
    ScopeId: win32more.Windows.Win32.Foundation.CHAR * 260
    EnableRouting: UInt32
    EnableProxy: UInt32
    EnableDns: UInt32
GET_ADAPTERS_ADDRESSES_FLAGS = UInt32
GAA_FLAG_SKIP_UNICAST: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 1
GAA_FLAG_SKIP_ANYCAST: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 2
GAA_FLAG_SKIP_MULTICAST: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 4
GAA_FLAG_SKIP_DNS_SERVER: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 8
GAA_FLAG_INCLUDE_PREFIX: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 16
GAA_FLAG_SKIP_FRIENDLY_NAME: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 32
GAA_FLAG_INCLUDE_WINS_INFO: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 64
GAA_FLAG_INCLUDE_GATEWAYS: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 128
GAA_FLAG_INCLUDE_ALL_INTERFACES: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 256
GAA_FLAG_INCLUDE_ALL_COMPARTMENTS: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 512
GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER: win32more.Windows.Win32.NetworkManagement.IpHelper.GET_ADAPTERS_ADDRESSES_FLAGS = 1024
GLOBAL_FILTER = Int32
GF_FRAGMENTS: win32more.Windows.Win32.NetworkManagement.IpHelper.GLOBAL_FILTER = 2
GF_STRONGHOST: win32more.Windows.Win32.NetworkManagement.IpHelper.GLOBAL_FILTER = 8
GF_FRAGCACHE: win32more.Windows.Win32.NetworkManagement.IpHelper.GLOBAL_FILTER = 9
HIFTIMESTAMPCHANGE = VoidPtr
ICMP4_TYPE = Int32
ICMP4_ECHO_REPLY: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 0
ICMP4_DST_UNREACH: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 3
ICMP4_SOURCE_QUENCH: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 4
ICMP4_REDIRECT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 5
ICMP4_ECHO_REQUEST: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 8
ICMP4_ROUTER_ADVERT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 9
ICMP4_ROUTER_SOLICIT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 10
ICMP4_TIME_EXCEEDED: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 11
ICMP4_PARAM_PROB: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 12
ICMP4_TIMESTAMP_REQUEST: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 13
ICMP4_TIMESTAMP_REPLY: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 14
ICMP4_MASK_REQUEST: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 17
ICMP4_MASK_REPLY: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP4_TYPE = 18
ICMP6_TYPE = Int32
ICMP6_DST_UNREACH: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 1
ICMP6_PACKET_TOO_BIG: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 2
ICMP6_TIME_EXCEEDED: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 3
ICMP6_PARAM_PROB: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 4
ICMP6_ECHO_REQUEST: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 128
ICMP6_ECHO_REPLY: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 129
ICMP6_MEMBERSHIP_QUERY: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 130
ICMP6_MEMBERSHIP_REPORT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 131
ICMP6_MEMBERSHIP_REDUCTION: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 132
ND_ROUTER_SOLICIT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 133
ND_ROUTER_ADVERT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 134
ND_NEIGHBOR_SOLICIT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 135
ND_NEIGHBOR_ADVERT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 136
ND_REDIRECT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 137
ICMP6_V2_MEMBERSHIP_REPORT: win32more.Windows.Win32.NetworkManagement.IpHelper.ICMP6_TYPE = 143
class ICMPV6_ECHO_REPLY_LH(Structure):
    Address: win32more.Windows.Win32.NetworkManagement.IpHelper.IPV6_ADDRESS_EX
    Status: UInt32
    RoundTripTime: UInt32
class ICMP_ECHO_REPLY(Structure):
    Address: UInt32
    Status: UInt32
    RoundTripTime: UInt32
    DataSize: UInt16
    Reserved: UInt16
    Data: VoidPtr
    Options: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION
if ARCH in 'X64,ARM64':
    class ICMP_ECHO_REPLY32(Structure):
        Address: UInt32
        Status: UInt32
        RoundTripTime: UInt32
        DataSize: UInt16
        Reserved: UInt16
        Data: VoidPtr
        Options: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_OPTION_INFORMATION32
IF_ACCESS_TYPE = Int32
IF_ACCESS_LOOPBACK: win32more.Windows.Win32.NetworkManagement.IpHelper.IF_ACCESS_TYPE = 1
IF_ACCESS_BROADCAST: win32more.Windows.Win32.NetworkManagement.IpHelper.IF_ACCESS_TYPE = 2
IF_ACCESS_POINT_TO_POINT: win32more.Windows.Win32.NetworkManagement.IpHelper.IF_ACCESS_TYPE = 3
IF_ACCESS_POINTTOPOINT: win32more.Windows.Win32.NetworkManagement.IpHelper.IF_ACCESS_TYPE = 3
IF_ACCESS_POINT_TO_MULTI_POINT: win32more.Windows.Win32.NetworkManagement.IpHelper.IF_ACCESS_TYPE = 4
IF_ACCESS_POINTTOMULTIPOINT: win32more.Windows.Win32.NetworkManagement.IpHelper.IF_ACCESS_TYPE = 4
class INTERFACE_HARDWARE_CROSSTIMESTAMP(Structure):
    SystemTimestamp1: UInt64
    HardwareClockTimestamp: UInt64
    SystemTimestamp2: UInt64
class INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES(Structure):
    PtpV2OverUdpIPv4EventMessageReceive: win32more.Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv4AllMessageReceive: win32more.Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv4EventMessageTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv4AllMessageTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6EventMessageReceive: win32more.Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6AllMessageReceive: win32more.Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6EventMessageTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
    PtpV2OverUdpIPv6AllMessageTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
    AllReceive: win32more.Windows.Win32.Foundation.BOOLEAN
    AllTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
    TaggedTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
class INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES(Structure):
    AllReceive: win32more.Windows.Win32.Foundation.BOOLEAN
    AllTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
    TaggedTransmit: win32more.Windows.Win32.Foundation.BOOLEAN
class INTERFACE_TIMESTAMP_CAPABILITIES(Structure):
    HardwareClockFrequencyHz: UInt64
    SupportsCrossTimestamp: win32more.Windows.Win32.Foundation.BOOLEAN
    HardwareCapabilities: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES
    SoftwareCapabilities: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES
INTERNAL_IF_OPER_STATUS = Int32
IF_OPER_STATUS_NON_OPERATIONAL: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS = 0
IF_OPER_STATUS_UNREACHABLE: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS = 1
IF_OPER_STATUS_DISCONNECTED: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS = 2
IF_OPER_STATUS_CONNECTING: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS = 3
IF_OPER_STATUS_CONNECTED: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS = 4
IF_OPER_STATUS_OPERATIONAL: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS = 5
class IPV6_ADDRESS_EX(Structure):
    sin6_port: UInt16
    sin6_flowinfo: UInt32
    sin6_addr: UInt16 * 8
    sin6_scope_id: UInt32
    _pack_ = 1
class IP_ADAPTER_ADDRESSES_LH(Structure):
    Anonymous1: _Anonymous1_e__Union
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_LH)
    AdapterName: win32more.Windows.Win32.Foundation.PSTR
    FirstUnicastAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_LH)
    FirstAnycastAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP)
    FirstMulticastAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP)
    FirstDnsServerAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP)
    DnsSuffix: win32more.Windows.Win32.Foundation.PWSTR
    Description: win32more.Windows.Win32.Foundation.PWSTR
    FriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    PhysicalAddress: Byte * 8
    PhysicalAddressLength: UInt32
    Anonymous2: _Anonymous2_e__Union
    Mtu: UInt32
    IfType: UInt32
    OperStatus: win32more.Windows.Win32.NetworkManagement.Ndis.IF_OPER_STATUS
    Ipv6IfIndex: UInt32
    ZoneIndices: UInt32 * 16
    FirstPrefix: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP)
    TransmitLinkSpeed: UInt64
    ReceiveLinkSpeed: UInt64
    FirstWinsServerAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_WINS_SERVER_ADDRESS_LH)
    FirstGatewayAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_GATEWAY_ADDRESS_LH)
    Ipv4Metric: UInt32
    Ipv6Metric: UInt32
    Luid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    Dhcpv4Server: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    CompartmentId: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_COMPARTMENT_ID
    NetworkGuid: Guid
    ConnectionType: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_CONNECTION_TYPE
    TunnelType: win32more.Windows.Win32.NetworkManagement.Ndis.TUNNEL_TYPE
    Dhcpv6Server: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    Dhcpv6ClientDuid: Byte * 130
    Dhcpv6ClientDuidLength: UInt32
    Dhcpv6Iaid: UInt32
    FirstDnsSuffix: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SUFFIX)
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
            DdnsEnabled: Annotated[UInt32, 1]
            RegisterAdapterSuffix: Annotated[UInt32, 1]
            Dhcpv4Enabled: Annotated[UInt32, 1]
            ReceiveOnly: Annotated[UInt32, 1]
            NoMulticast: Annotated[UInt32, 1]
            Ipv6OtherStatefulConfig: Annotated[UInt32, 1]
            NetbiosOverTcpipEnabled: Annotated[UInt32, 1]
            Ipv4Enabled: Annotated[UInt32, 1]
            Ipv6Enabled: Annotated[UInt32, 1]
            Ipv6ManagedAddressConfigurationSupported: Annotated[UInt32, 1]
class IP_ADAPTER_ADDRESSES_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ADDRESSES_XP)
    AdapterName: win32more.Windows.Win32.Foundation.PSTR
    FirstUnicastAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_XP)
    FirstAnycastAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP)
    FirstMulticastAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP)
    FirstDnsServerAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP)
    DnsSuffix: win32more.Windows.Win32.Foundation.PWSTR
    Description: win32more.Windows.Win32.Foundation.PWSTR
    FriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    PhysicalAddress: Byte * 8
    PhysicalAddressLength: UInt32
    Flags: UInt32
    Mtu: UInt32
    IfType: UInt32
    OperStatus: win32more.Windows.Win32.NetworkManagement.Ndis.IF_OPER_STATUS
    Ipv6IfIndex: UInt32
    ZoneIndices: UInt32 * 16
    FirstPrefix: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP)
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            IfIndex: UInt32
class IP_ADAPTER_ANYCAST_ADDRESS_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_ANYCAST_ADDRESS_XP)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Flags: UInt32
class IP_ADAPTER_DNS_SERVER_ADDRESS_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SERVER_ADDRESS_XP)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Reserved: UInt32
class IP_ADAPTER_DNS_SUFFIX(Structure):
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_DNS_SUFFIX)
    String: Char * 256
class IP_ADAPTER_GATEWAY_ADDRESS_LH(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_GATEWAY_ADDRESS_LH)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
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
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INFO)
    ComboIndex: UInt32
    AdapterName: win32more.Windows.Win32.Foundation.CHAR * 260
    Description: win32more.Windows.Win32.Foundation.CHAR * 132
    AddressLength: UInt32
    Address: Byte * 8
    Index: UInt32
    Type: UInt32
    DhcpEnabled: UInt32
    CurrentIpAddress: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING)
    IpAddressList: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    GatewayList: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    DhcpServer: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    HaveWins: win32more.Windows.Win32.Foundation.BOOL
    PrimaryWinsServer: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    SecondaryWinsServer: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
    LeaseObtained: Int64
    LeaseExpires: Int64
class IP_ADAPTER_MULTICAST_ADDRESS_XP(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_MULTICAST_ADDRESS_XP)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
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
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_PREFIX_XP)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    PrefixLength: UInt32
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Flags: UInt32
class IP_ADAPTER_UNICAST_ADDRESS_LH(Structure):
    Anonymous: _Anonymous_e__Union
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_LH)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    PrefixOrigin: win32more.Windows.Win32.Networking.WinSock.NL_PREFIX_ORIGIN
    SuffixOrigin: win32more.Windows.Win32.Networking.WinSock.NL_SUFFIX_ORIGIN
    DadState: win32more.Windows.Win32.Networking.WinSock.NL_DAD_STATE
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
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_UNICAST_ADDRESS_XP)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    PrefixOrigin: win32more.Windows.Win32.Networking.WinSock.NL_PREFIX_ORIGIN
    SuffixOrigin: win32more.Windows.Win32.Networking.WinSock.NL_SUFFIX_ORIGIN
    DadState: win32more.Windows.Win32.Networking.WinSock.NL_DAD_STATE
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
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_WINS_SERVER_ADDRESS_LH)
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    class _Anonymous_e__Union(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Length: UInt32
            Reserved: UInt32
class IP_ADDRESS_PREFIX(Structure):
    Prefix: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    PrefixLength: Byte
class IP_ADDRESS_STRING(Structure):
    String: win32more.Windows.Win32.Foundation.CHAR * 16
class IP_ADDR_STRING(Structure):
    Next: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING)
    IpAddress: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDRESS_STRING
    IpMask: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDRESS_STRING
    Context: UInt32
class IP_INTERFACE_INFO(Structure):
    NumAdapters: Int32
    Adapter: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADAPTER_INDEX_MAP * 1
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
    OptionsData: POINTER(Byte)
if ARCH in 'X64,ARM64':
    class IP_OPTION_INFORMATION32(Structure):
        Ttl: Byte
        Tos: Byte
        Flags: Byte
        OptionsSize: Byte
        OptionsData: POINTER(Byte)
class IP_PER_ADAPTER_INFO_W2KSP1(Structure):
    AutoconfigEnabled: UInt32
    AutoconfigActive: UInt32
    CurrentDnsServer: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING)
    DnsServerList: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDR_STRING
class IP_UNIDIRECTIONAL_ADAPTER_ADDRESS(Structure):
    NumAdapters: UInt32
    Address: UInt32 * 1
class MIBICMPINFO(Structure):
    icmpInStats: win32more.Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS
    icmpOutStats: win32more.Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS
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
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    ScopeId: win32more.Windows.Win32.Networking.WinSock.SCOPE_ID
class MIB_ANYCASTIPADDRESS_TABLE(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_ANYCASTIPADDRESS_ROW * 1
class MIB_BEST_IF(Structure):
    dwDestAddr: UInt32
    dwIfIndex: UInt32
class MIB_BOUNDARYROW(Structure):
    dwGroupAddress: UInt32
    dwGroupMask: UInt32
class MIB_ICMP(Structure):
    stats: win32more.Windows.Win32.NetworkManagement.IpHelper.MIBICMPINFO
class MIB_ICMP_EX_XPSP1(Structure):
    icmpInStats: win32more.Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS_EX_XPSP1
    icmpOutStats: win32more.Windows.Win32.NetworkManagement.IpHelper.MIBICMPSTATS_EX_XPSP1
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
    dwOperStatus: win32more.Windows.Win32.NetworkManagement.IpHelper.INTERNAL_IF_OPER_STATUS
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
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IFSTACK_ROW * 1
class MIB_IFSTATUS(Structure):
    dwIfIndex: UInt32
    dwAdminStatus: UInt32
    dwOperationalStatus: UInt32
    bMHbeatActive: win32more.Windows.Win32.Foundation.BOOL
    bMHbeatAlive: win32more.Windows.Win32.Foundation.BOOL
class MIB_IFTABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IFROW * 1
MIB_IF_ENTRY_LEVEL = Int32
MibIfEntryNormal: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ENTRY_LEVEL = 0
MibIfEntryNormalWithoutStatistics: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ENTRY_LEVEL = 2
class MIB_IF_ROW2(Structure):
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    InterfaceGuid: Guid
    Alias: Char * 257
    Description: Char * 257
    PhysicalAddressLength: UInt32
    PhysicalAddress: Byte * 32
    PermanentPhysicalAddress: Byte * 32
    Mtu: UInt32
    Type: UInt32
    TunnelType: win32more.Windows.Win32.NetworkManagement.Ndis.TUNNEL_TYPE
    MediaType: win32more.Windows.Win32.NetworkManagement.Ndis.NDIS_MEDIUM
    PhysicalMediumType: win32more.Windows.Win32.NetworkManagement.Ndis.NDIS_PHYSICAL_MEDIUM
    AccessType: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_ACCESS_TYPE
    DirectionType: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_DIRECTION_TYPE
    InterfaceAndOperStatusFlags: _InterfaceAndOperStatusFlags_e__Struct
    OperStatus: win32more.Windows.Win32.NetworkManagement.Ndis.IF_OPER_STATUS
    AdminStatus: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_ADMIN_STATUS
    MediaConnectState: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_MEDIA_CONNECT_STATE
    NetworkGuid: Guid
    ConnectionType: win32more.Windows.Win32.NetworkManagement.Ndis.NET_IF_CONNECTION_TYPE
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
        HardwareInterface: Annotated[Byte, 1]
        FilterInterface: Annotated[Byte, 1]
        ConnectorPresent: Annotated[Byte, 1]
        NotAuthenticated: Annotated[Byte, 1]
        NotMediaConnected: Annotated[Byte, 1]
        Paused: Annotated[Byte, 1]
        LowPower: Annotated[Byte, 1]
        EndPointInterface: Annotated[Byte, 1]
class MIB_IF_TABLE2(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_ROW2 * 1
MIB_IF_TABLE_LEVEL = Int32
MibIfTableNormal: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE_LEVEL = 0
MibIfTableRaw: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE_LEVEL = 1
MibIfTableNormalWithoutStatistics: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IF_TABLE_LEVEL = 2
class MIB_INVERTEDIFSTACK_ROW(Structure):
    LowerLayerInterfaceIndex: UInt32
    HigherLayerInterfaceIndex: UInt32
class MIB_INVERTEDIFSTACK_TABLE(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_INVERTEDIFSTACK_ROW * 1
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
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPADDRROW_XP * 1
class MIB_IPDESTROW(Structure):
    ForwardRow: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW
    dwForwardPreference: UInt32
    dwForwardViewSet: UInt32
class MIB_IPDESTTABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPDESTROW * 1
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
        ForwardType: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TYPE
    class _Anonymous2_e__Union(Union):
        dwForwardProto: UInt32
        ForwardProto: win32more.Windows.Win32.Networking.WinSock.NL_ROUTE_PROTOCOL
class MIB_IPFORWARDTABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARDROW * 1
class MIB_IPFORWARD_ROW2(Structure):
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    DestinationPrefix: win32more.Windows.Win32.NetworkManagement.IpHelper.IP_ADDRESS_PREFIX
    NextHop: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    SitePrefixLength: Byte
    ValidLifetime: UInt32
    PreferredLifetime: UInt32
    Metric: UInt32
    Protocol: win32more.Windows.Win32.Networking.WinSock.NL_ROUTE_PROTOCOL
    Loopback: win32more.Windows.Win32.Foundation.BOOLEAN
    AutoconfigureAddress: win32more.Windows.Win32.Foundation.BOOLEAN
    Publish: win32more.Windows.Win32.Foundation.BOOLEAN
    Immortal: win32more.Windows.Win32.Foundation.BOOLEAN
    Age: UInt32
    Origin: win32more.Windows.Win32.Networking.WinSock.NL_ROUTE_ORIGIN
class MIB_IPFORWARD_TABLE2(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2 * 1
MIB_IPFORWARD_TYPE = Int32
MIB_IPROUTE_TYPE_OTHER: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TYPE = 1
MIB_IPROUTE_TYPE_INVALID: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TYPE = 2
MIB_IPROUTE_TYPE_DIRECT: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TYPE = 3
MIB_IPROUTE_TYPE_INDIRECT: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_TYPE = 4
class MIB_IPINTERFACE_ROW(Structure):
    Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    MaxReassemblySize: UInt32
    InterfaceIdentifier: UInt64
    MinRouterAdvertisementInterval: UInt32
    MaxRouterAdvertisementInterval: UInt32
    AdvertisingEnabled: win32more.Windows.Win32.Foundation.BOOLEAN
    ForwardingEnabled: win32more.Windows.Win32.Foundation.BOOLEAN
    WeakHostSend: win32more.Windows.Win32.Foundation.BOOLEAN
    WeakHostReceive: win32more.Windows.Win32.Foundation.BOOLEAN
    UseAutomaticMetric: win32more.Windows.Win32.Foundation.BOOLEAN
    UseNeighborUnreachabilityDetection: win32more.Windows.Win32.Foundation.BOOLEAN
    ManagedAddressConfigurationSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    OtherStatefulConfigurationSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    AdvertiseDefaultRoute: win32more.Windows.Win32.Foundation.BOOLEAN
    RouterDiscoveryBehavior: win32more.Windows.Win32.Networking.WinSock.NL_ROUTER_DISCOVERY_BEHAVIOR
    DadTransmits: UInt32
    BaseReachableTime: UInt32
    RetransmitTime: UInt32
    PathMtuDiscoveryTimeout: UInt32
    LinkLocalAddressBehavior: win32more.Windows.Win32.Networking.WinSock.NL_LINK_LOCAL_ADDRESS_BEHAVIOR
    LinkLocalAddressTimeout: UInt32
    ZoneIndices: UInt32 * 16
    SitePrefixLength: UInt32
    Metric: UInt32
    NlMtu: UInt32
    Connected: win32more.Windows.Win32.Foundation.BOOLEAN
    SupportsWakeUpPatterns: win32more.Windows.Win32.Foundation.BOOLEAN
    SupportsNeighborDiscovery: win32more.Windows.Win32.Foundation.BOOLEAN
    SupportsRouterDiscovery: win32more.Windows.Win32.Foundation.BOOLEAN
    ReachableTime: UInt32
    TransmitOffload: win32more.Windows.Win32.Networking.WinSock.NL_INTERFACE_OFFLOAD_ROD
    ReceiveOffload: win32more.Windows.Win32.Networking.WinSock.NL_INTERFACE_OFFLOAD_ROD
    DisableDefaultRoutes: win32more.Windows.Win32.Foundation.BOOLEAN
class MIB_IPINTERFACE_TABLE(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW * 1
class MIB_IPMCAST_BOUNDARY(Structure):
    dwIfIndex: UInt32
    dwGroupAddress: UInt32
    dwGroupMask: UInt32
    dwStatus: UInt32
class MIB_IPMCAST_BOUNDARY_TABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_BOUNDARY * 1
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
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_IF_ENTRY * 1
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
    rgmioOutInfo: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_XP * 1
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
    rgmiosOutStats: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_LH * 1
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
    rgmiosOutStats: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_OIF_STATS_LH * 1
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
    pvDialContext: VoidPtr
    ulTtlTooLow: UInt32
    ulFragNeeded: UInt32
    ulOutPackets: UInt32
    ulOutDiscards: UInt32
class MIB_IPMCAST_OIF_W2K(Structure):
    dwOutIfIndex: UInt32
    dwNextHopAddr: UInt32
    pvReserved: VoidPtr
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
        Type: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TYPE
class MIB_IPNETROW_W2K(Structure):
    dwIndex: UInt32
    dwPhysAddrLen: UInt32
    bPhysAddr: Byte * 8
    dwAddr: UInt32
    dwType: UInt32
class MIB_IPNETTABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNETROW_LH * 1
class MIB_IPNET_ROW2(Structure):
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceIndex: UInt32
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    PhysicalAddress: Byte * 32
    PhysicalAddressLength: UInt32
    State: win32more.Windows.Win32.Networking.WinSock.NL_NEIGHBOR_STATE
    Anonymous: _Anonymous_e__Union
    ReachabilityTime: _ReachabilityTime_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        Flags: Byte
        class _Anonymous_e__Struct(Structure):
            IsRouter: Annotated[Byte, 1]
            IsUnreachable: Annotated[Byte, 1]
    class _ReachabilityTime_e__Union(Union):
        LastReachable: UInt32
        LastUnreachable: UInt32
class MIB_IPNET_TABLE2(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_ROW2 * 1
MIB_IPNET_TYPE = Int32
MIB_IPNET_TYPE_OTHER: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TYPE = 1
MIB_IPNET_TYPE_INVALID: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TYPE = 2
MIB_IPNET_TYPE_DYNAMIC: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TYPE = 3
MIB_IPNET_TYPE_STATIC: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPNET_TYPE = 4
class MIB_IPPATH_ROW(Structure):
    Source: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    Destination: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    CurrentNextHop: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    PathMtu: UInt32
    RttMean: UInt32
    RttDeviation: UInt32
    Anonymous: _Anonymous_e__Union
    IsReachable: win32more.Windows.Win32.Foundation.BOOLEAN
    LinkTransmitSpeed: UInt64
    LinkReceiveSpeed: UInt64
    class _Anonymous_e__Union(Union):
        LastReachable: UInt32
        LastUnreachable: UInt32
class MIB_IPPATH_TABLE(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPPATH_ROW * 1
MIB_IPSTATS_FORWARDING = Int32
MIB_IP_FORWARDING: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_FORWARDING = 1
MIB_IP_NOT_FORWARDING: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_FORWARDING = 2
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
        Forwarding: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPSTATS_FORWARDING
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
    InboundBandwidthInformation: win32more.Windows.Win32.Networking.WinSock.NL_BANDWIDTH_INFORMATION
    OutboundBandwidthInformation: win32more.Windows.Win32.Networking.WinSock.NL_BANDWIDTH_INFORMATION
class MIB_MCAST_LIMIT_ROW(Structure):
    dwTtl: UInt32
    dwRateLimit: UInt32
class MIB_MFE_STATS_TABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS * 1
class MIB_MFE_STATS_TABLE_EX_XP(Structure):
    dwNumEntries: UInt32
    table: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE_STATS_EX_XP) * 1
class MIB_MFE_TABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPMCAST_MFE * 1
class MIB_MULTICASTIPADDRESS_ROW(Structure):
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceIndex: UInt32
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    ScopeId: win32more.Windows.Win32.Networking.WinSock.SCOPE_ID
class MIB_MULTICASTIPADDRESS_TABLE(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_MULTICASTIPADDRESS_ROW * 1
MIB_NOTIFICATION_TYPE = Int32
MibParameterNotification: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE = 0
MibAddInstance: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE = 1
MibDeleteInstance: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE = 2
MibInitialNotification: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE = 3
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
    bRoutesSetToStack: win32more.Windows.Win32.Foundation.BOOL
class MIB_TCP6ROW(Structure):
    State: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE
    LocalAddr: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    RemoteAddr: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
class MIB_TCP6ROW2(Structure):
    LocalAddr: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    RemoteAddr: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
    State: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE
    dwOwningPid: UInt32
    dwOffloadState: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE
class MIB_TCP6ROW_OWNER_MODULE(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    ucRemoteAddr: Byte * 16
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
    dwState: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Int64
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
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW * 1
class MIB_TCP6TABLE2(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW2 * 1
class MIB_TCP6TABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_MODULE * 1
class MIB_TCP6TABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP6ROW_OWNER_PID * 1
class MIB_TCPROW2(Structure):
    dwState: UInt32
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    dwOwningPid: UInt32
    dwOffloadState: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE
class MIB_TCPROW_LH(Structure):
    Anonymous: _Anonymous_e__Union
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    class _Anonymous_e__Union(Union):
        dwState: UInt32
        State: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE
class MIB_TCPROW_OWNER_MODULE(Structure):
    dwState: UInt32
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Int64
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
    RtoAlgorithm: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM
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
        RtoAlgorithm: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM
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
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_LH * 1
class MIB_TCPTABLE2(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW2 * 1
class MIB_TCPTABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_MODULE * 1
class MIB_TCPTABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCPROW_OWNER_PID * 1
MIB_TCP_STATE = Int32
MIB_TCP_STATE_CLOSED: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 1
MIB_TCP_STATE_LISTEN: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 2
MIB_TCP_STATE_SYN_SENT: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 3
MIB_TCP_STATE_SYN_RCVD: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 4
MIB_TCP_STATE_ESTAB: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 5
MIB_TCP_STATE_FIN_WAIT1: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 6
MIB_TCP_STATE_FIN_WAIT2: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 7
MIB_TCP_STATE_CLOSE_WAIT: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 8
MIB_TCP_STATE_CLOSING: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 9
MIB_TCP_STATE_LAST_ACK: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 10
MIB_TCP_STATE_TIME_WAIT: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 11
MIB_TCP_STATE_DELETE_TCB: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 12
MIB_TCP_STATE_RESERVED: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_TCP_STATE = 100
class MIB_UDP6ROW(Structure):
    dwLocalAddr: win32more.Windows.Win32.Networking.WinSock.IN6_ADDR
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
class MIB_UDP6ROW2(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Int64
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    ucRemoteAddr: Byte * 16
    dwRemoteScopeId: UInt32
    dwRemotePort: UInt32
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            SpecificPortBind: Annotated[Int32, 1]
class MIB_UDP6ROW_OWNER_MODULE(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Int64
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            SpecificPortBind: Annotated[Int32, 1]
class MIB_UDP6ROW_OWNER_PID(Structure):
    ucLocalAddr: Byte * 16
    dwLocalScopeId: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
class MIB_UDP6TABLE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW * 1
class MIB_UDP6TABLE2(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW2 * 1
class MIB_UDP6TABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_MODULE * 1
class MIB_UDP6TABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDP6ROW_OWNER_PID * 1
class MIB_UDPROW(Structure):
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
class MIB_UDPROW2(Structure):
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Int64
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    dwRemoteAddr: UInt32
    dwRemotePort: UInt32
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            SpecificPortBind: Annotated[Int32, 1]
class MIB_UDPROW_OWNER_MODULE(Structure):
    dwLocalAddr: UInt32
    dwLocalPort: UInt32
    dwOwningPid: UInt32
    liCreateTimestamp: Int64
    Anonymous: _Anonymous_e__Union
    OwningModuleInfo: UInt64 * 16
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        dwFlags: Int32
        class _Anonymous_e__Struct(Structure):
            SpecificPortBind: Annotated[Int32, 1]
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
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW * 1
class MIB_UDPTABLE2(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW2 * 1
class MIB_UDPTABLE_OWNER_MODULE(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_MODULE * 1
class MIB_UDPTABLE_OWNER_PID(Structure):
    dwNumEntries: UInt32
    table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UDPROW_OWNER_PID * 1
class MIB_UNICASTIPADDRESS_ROW(Structure):
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_INET
    InterfaceLuid: win32more.Windows.Win32.NetworkManagement.Ndis.NET_LUID_LH
    InterfaceIndex: UInt32
    PrefixOrigin: win32more.Windows.Win32.Networking.WinSock.NL_PREFIX_ORIGIN
    SuffixOrigin: win32more.Windows.Win32.Networking.WinSock.NL_SUFFIX_ORIGIN
    ValidLifetime: UInt32
    PreferredLifetime: UInt32
    OnLinkPrefixLength: Byte
    SkipAsSource: win32more.Windows.Win32.Foundation.BOOLEAN
    DadState: win32more.Windows.Win32.Networking.WinSock.NL_DAD_STATE
    ScopeId: win32more.Windows.Win32.Networking.WinSock.SCOPE_ID
    CreationTimeStamp: Int64
class MIB_UNICASTIPADDRESS_TABLE(Structure):
    NumEntries: UInt32
    Table: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW * 1
NET_ADDRESS_FORMAT = Int32
NET_ADDRESS_FORMAT_UNSPECIFIED: win32more.Windows.Win32.NetworkManagement.IpHelper.NET_ADDRESS_FORMAT = 0
NET_ADDRESS_DNS_NAME: win32more.Windows.Win32.NetworkManagement.IpHelper.NET_ADDRESS_FORMAT = 1
NET_ADDRESS_IPV4: win32more.Windows.Win32.NetworkManagement.IpHelper.NET_ADDRESS_FORMAT = 2
NET_ADDRESS_IPV6: win32more.Windows.Win32.NetworkManagement.IpHelper.NET_ADDRESS_FORMAT = 3
class NET_ADDRESS_INFO(Structure):
    Format: win32more.Windows.Win32.NetworkManagement.IpHelper.NET_ADDRESS_FORMAT
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        NamedAddress: _NamedAddress_e__Struct
        Ipv4Address: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN
        Ipv6Address: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN6
        IpAddress: win32more.Windows.Win32.Networking.WinSock.SOCKADDR
        class _NamedAddress_e__Struct(Structure):
            Address: Char * 256
            Port: Char * 6
PFADDRESSTYPE = Int32
PF_IPV4: win32more.Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE = 0
PF_IPV6: win32more.Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE = 1
PFFORWARD_ACTION = Int32
PF_ACTION_FORWARD: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION = 0
PF_ACTION_DROP: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION = 1
PFFRAMETYPE = Int32
PFFT_FILTER: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFRAMETYPE = 1
PFFT_FRAG: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFRAMETYPE = 2
PFFT_SPOOF: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFRAMETYPE = 3
class PFLOGFRAME(Structure):
    Timestamp: Int64
    pfeTypeOfFrame: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFRAMETYPE
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
    pfatType: win32more.Windows.Win32.NetworkManagement.IpHelper.PFADDRESSTYPE
    SrcAddr: POINTER(Byte)
    SrcMask: POINTER(Byte)
    DstAddr: POINTER(Byte)
    DstMask: POINTER(Byte)
    dwProtocol: UInt32
    fLateBound: UInt32
    wSrcPort: UInt16
    wDstPort: UInt16
    wSrcPortHighRange: UInt16
    wDstPortHighRange: UInt16
class PF_FILTER_STATS(Structure):
    dwNumPacketsFiltered: UInt32
    info: win32more.Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_DESCRIPTOR
class PF_INTERFACE_STATS(Structure):
    pvDriverContext: VoidPtr
    dwFlags: UInt32
    dwInDrops: UInt32
    dwOutDrops: UInt32
    eaInAction: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION
    eaOutAction: win32more.Windows.Win32.NetworkManagement.IpHelper.PFFORWARD_ACTION
    dwNumInFilters: UInt32
    dwNumOutFilters: UInt32
    dwFrag: UInt32
    dwSpoof: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
    liSYN: Int64
    liTotalLogged: Int64
    dwLostLogEntries: UInt32
    FilterInfo: win32more.Windows.Win32.NetworkManagement.IpHelper.PF_FILTER_STATS * 1
class PF_LATEBIND_INFO(Structure):
    SrcAddr: POINTER(Byte)
    DstAddr: POINTER(Byte)
    Mask: POINTER(Byte)
@winfunctype_pointer
def PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK(CallerContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PIPFORWARD_CHANGE_CALLBACK(CallerContext: VoidPtr, Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPFORWARD_ROW2), NotificationType: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
@winfunctype_pointer
def PIPINTERFACE_CHANGE_CALLBACK(CallerContext: VoidPtr, Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_IPINTERFACE_ROW), NotificationType: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
@winfunctype_pointer
def PNETWORK_CONNECTIVITY_HINT_CHANGE_CALLBACK(CallerContext: VoidPtr, ConnectivityHint: win32more.Windows.Win32.Networking.WinSock.NL_NETWORK_CONNECTIVITY_HINT) -> Void: ...
@winfunctype_pointer
def PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK(CallerContext: VoidPtr, AddressTable: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_TABLE)) -> Void: ...
@winfunctype_pointer
def PTEREDO_PORT_CHANGE_CALLBACK(CallerContext: VoidPtr, Port: UInt16, NotificationType: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
@winfunctype_pointer
def PUNICAST_IPADDRESS_CHANGE_CALLBACK(CallerContext: VoidPtr, Row: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_UNICASTIPADDRESS_ROW), NotificationType: win32more.Windows.Win32.NetworkManagement.IpHelper.MIB_NOTIFICATION_TYPE) -> Void: ...
class TCPIP_OWNER_MODULE_BASIC_INFO(Structure):
    pModuleName: win32more.Windows.Win32.Foundation.PWSTR
    pModulePath: win32more.Windows.Win32.Foundation.PWSTR
TCPIP_OWNER_MODULE_INFO_CLASS = Int32
TCPIP_OWNER_MODULE_INFO_BASIC: win32more.Windows.Win32.NetworkManagement.IpHelper.TCPIP_OWNER_MODULE_INFO_CLASS = 0
TCP_BOOLEAN_OPTIONAL = Int32
TcpBoolOptDisabled: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL = 0
TcpBoolOptEnabled: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL = 1
TcpBoolOptUnchanged: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL = -1
TCP_CONNECTION_OFFLOAD_STATE = Int32
TcpConnectionOffloadStateInHost: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE = 0
TcpConnectionOffloadStateOffloading: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE = 1
TcpConnectionOffloadStateOffloaded: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE = 2
TcpConnectionOffloadStateUploading: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE = 3
TcpConnectionOffloadStateMax: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_CONNECTION_OFFLOAD_STATE = 4
class TCP_ESTATS_BANDWIDTH_ROD_v0(Structure):
    OutboundBandwidth: UInt64
    InboundBandwidth: UInt64
    OutboundInstability: UInt64
    InboundInstability: UInt64
    OutboundBandwidthPeaked: win32more.Windows.Win32.Foundation.BOOLEAN
    InboundBandwidthPeaked: win32more.Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_BANDWIDTH_RW_v0(Structure):
    EnableCollectionOutbound: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL
    EnableCollectionInbound: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_BOOLEAN_OPTIONAL
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
    EnableCollection: win32more.Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_FINE_RTT_ROD_v0(Structure):
    RttVar: UInt32
    MaxRtt: UInt32
    MinRtt: UInt32
    SumRtt: UInt32
class TCP_ESTATS_FINE_RTT_RW_v0(Structure):
    EnableCollection: win32more.Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_OBS_REC_ROD_v0(Structure):
    CurRwinRcvd: UInt32
    MaxRwinRcvd: UInt32
    MinRwinRcvd: UInt32
    WinScaleRcvd: Byte
class TCP_ESTATS_OBS_REC_RW_v0(Structure):
    EnableCollection: win32more.Windows.Win32.Foundation.BOOLEAN
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
    EnableCollection: win32more.Windows.Win32.Foundation.BOOLEAN
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
    EnableCollection: win32more.Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_SEND_BUFF_ROD_v0(Structure):
    CurRetxQueue: UIntPtr
    MaxRetxQueue: UIntPtr
    CurAppWQueue: UIntPtr
    MaxAppWQueue: UIntPtr
class TCP_ESTATS_SEND_BUFF_RW_v0(Structure):
    EnableCollection: win32more.Windows.Win32.Foundation.BOOLEAN
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
    EnableCollection: win32more.Windows.Win32.Foundation.BOOLEAN
class TCP_ESTATS_SYN_OPTS_ROS_v0(Structure):
    ActiveOpen: win32more.Windows.Win32.Foundation.BOOLEAN
    MssRcvd: UInt32
    MssSent: UInt32
TCP_ESTATS_TYPE = Int32
TcpConnectionEstatsSynOpts: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 0
TcpConnectionEstatsData: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 1
TcpConnectionEstatsSndCong: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 2
TcpConnectionEstatsPath: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 3
TcpConnectionEstatsSendBuff: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 4
TcpConnectionEstatsRec: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 5
TcpConnectionEstatsObsRec: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 6
TcpConnectionEstatsBandwidth: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 7
TcpConnectionEstatsFineRtt: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 8
TcpConnectionEstatsMaximum: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_ESTATS_TYPE = 9
class TCP_RESERVE_PORT_RANGE(Structure):
    UpperRange: UInt16
    LowerRange: UInt16
TCP_RTO_ALGORITHM = Int32
TcpRtoAlgorithmOther: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 1
TcpRtoAlgorithmConstant: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 2
TcpRtoAlgorithmRsre: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 3
TcpRtoAlgorithmVanj: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 4
MIB_TCP_RTO_OTHER: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 1
MIB_TCP_RTO_CONSTANT: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 2
MIB_TCP_RTO_RSRE: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 3
MIB_TCP_RTO_VANJ: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_RTO_ALGORITHM = 4
TCP_SOFT_ERROR = Int32
TcpErrorNone: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 0
TcpErrorBelowDataWindow: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 1
TcpErrorAboveDataWindow: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 2
TcpErrorBelowAckWindow: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 3
TcpErrorAboveAckWindow: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 4
TcpErrorBelowTsWindow: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 5
TcpErrorAboveTsWindow: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 6
TcpErrorDataChecksumError: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 7
TcpErrorDataLengthError: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 8
TcpErrorMaxSoftError: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_SOFT_ERROR = 9
TCP_TABLE_CLASS = Int32
TCP_TABLE_BASIC_LISTENER: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 0
TCP_TABLE_BASIC_CONNECTIONS: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 1
TCP_TABLE_BASIC_ALL: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 2
TCP_TABLE_OWNER_PID_LISTENER: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 3
TCP_TABLE_OWNER_PID_CONNECTIONS: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 4
TCP_TABLE_OWNER_PID_ALL: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 5
TCP_TABLE_OWNER_MODULE_LISTENER: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 6
TCP_TABLE_OWNER_MODULE_CONNECTIONS: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 7
TCP_TABLE_OWNER_MODULE_ALL: win32more.Windows.Win32.NetworkManagement.IpHelper.TCP_TABLE_CLASS = 8
UDP_TABLE_CLASS = Int32
UDP_TABLE_BASIC: win32more.Windows.Win32.NetworkManagement.IpHelper.UDP_TABLE_CLASS = 0
UDP_TABLE_OWNER_PID: win32more.Windows.Win32.NetworkManagement.IpHelper.UDP_TABLE_CLASS = 1
UDP_TABLE_OWNER_MODULE: win32more.Windows.Win32.NetworkManagement.IpHelper.UDP_TABLE_CLASS = 2


make_ready(__name__)
